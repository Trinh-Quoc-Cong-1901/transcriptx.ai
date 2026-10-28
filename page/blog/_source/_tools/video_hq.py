"""High-quality walkthrough video kit: 2560x1440 (1440p), 60 fps, streamed to x264 (CRF 14).

Why 1440p: YouTube encodes 1440p uploads with VP9/AV1 at a much higher bitrate, so the video stays sharp even
when watched at 1080p.
Sharpness rules: never upscale a source more than its MAX_UP (see `view(..., max_up=)`); show small details as
crisp callouts cut from retina sources instead of zooming low-res frames; upscaled frames get an unsharp mask.

- Scenes are (frames, fn(t, s) -> RGB frame) and are rendered lazily, so memory stays low.
- Screens are rendered once, straight from the source rect to their final size (no double resampling).
- Overlays draw with ImageDraw in RGBA-blend mode on small patches; cursor/caption/progress sprites are cached.
- GIF recordings are frame-interpolated (crossfade between neighbouring frames) for smooth motion.
"""
import importlib.util, math, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)

W, H, FPS = 2560, 1440, 60
U = H / 800                       # size unit relative to the old 800px layouts
BG, DARK, ACCENT = bv.BG, bv.DARK, bv.ACCENT
GREEN = (46, 125, 72)
GREY = (105, 100, 92)
ease, lerp = bv.ease, bv.lerp
STEPS = []
scenes = []

# framed screen under the progress bar
SW, SH = int(W * 0.88), int(H * 0.88)
SX, SY = (W - SW) // 2, int(92 * U * 0.8)


@lru_cache(maxsize=64)
def font(size, bold=False):
    return bv.font(int(size), bold)


# ---------- geometry ----------

def pad16x9(img, color=None):
    return bv.pad_to_aspect(img, aspect=W / H, color=color)


def view(box, size, pad=0.3, max_up=None):
    """16:9 crop around box. max_up caps how much the source may be enlarged on screen (sharpness guard)."""
    iw, ih = size
    x0, y0, x1, y1 = box
    bw, bh = (x1 - x0) * (1 + pad * 2), (y1 - y0) * (1 + pad * 2)
    if bw / bh < W / H:
        bw = bh * W / H
    else:
        bh = bw * H / W
    if max_up:
        min_w = SW / max_up
        if bw < min_w:
            bw, bh = min_w, min_w * H / W
    bw, bh = min(bw, iw), min(bh, ih)
    cx = min(max((x0 + x1) / 2, bw / 2), iw - bw / 2)
    cy = min(max((y0 + y1) / 2, bh / 2), ih - bh / 2)
    return (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2)


def full(img):
    return (0, 0, img.width, img.height)


def render(img, rect, size=(SW, SH)):
    out = img.resize(size, Image.LANCZOS, box=rect)
    up = size[0] / (rect[2] - rect[0])
    if up > 1.15:
        out = out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=int(min(110, 50 + 40 * (up - 1))), threshold=2))
    return out


def callout(img, src, crop, xy, width, a=1.0, radius=None):
    """Crisp magnified card cut from a (retina) source. width should stay <= crop width * 1.2."""
    if a <= 0:
        return img
    c = src.crop(crop)
    h = round(c.height * width / c.width)
    c = c.resize((int(width), h), Image.LANCZOS).convert('RGBA')
    r = radius or int(14 * U)
    m = Image.new('L', c.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, c.width - 1, c.height - 1), r, fill=255)
    c.putalpha(m)
    g = int(26 * U)
    card = Image.new('RGBA', (c.width + g * 2, c.height + g * 2), (0, 0, 0, 0))
    sh = Image.new('RGBA', card.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((g, g + 10, g + c.width, g + c.height + 10), r, fill=(40, 25, 10, 90))
    card.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(16 * U))))
    card.alpha_composite(c, (g, g))
    ImageDraw.Draw(card).rounded_rectangle((g, g, g + c.width - 1, g + c.height - 1), r, outline=(225, 222, 214, 255), width=2)
    k = 0.94 + 0.06 * a
    if k < 1:
        card = card.resize((int(card.width * k), int(card.height * k)), Image.LANCZOS)
    return paste_fade(img, card, (xy[0] - g, xy[1] - g), a)


def to_s(pt, rect, size=(SW, SH)):
    k = size[0] / (rect[2] - rect[0])
    return ((pt[0] - rect[0]) * k, (pt[1] - rect[1]) * k), k


def box_s(box, rect, size=(SW, SH)):
    (a, b), _ = to_s(box[:2], rect, size)
    (c, d), _ = to_s(box[2:], rect, size)
    return (a, b, c, d)


def path(p0, p1, t, arc=40):
    e = ease(t)
    return (p0[0] + (p1[0] - p0[0]) * e, p0[1] + (p1[1] - p0[1]) * e - arc * U * (1 - (2 * e - 1) ** 2))


# ---------- sprites ----------

@lru_cache(maxsize=4)
def cursor_sprite(pressed):
    k = 2.3 * U * (0.88 if pressed else 1.0)
    pts = [(0, 0), (0, 17), (4.5, 13), (7.5, 20), (10, 19), (7, 12.5), (12.5, 12.5)]
    pad = int(12 * U)
    w, h = int(13 * k) + pad * 2, int(21 * k) + pad * 2
    spr = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    sh = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(sh).polygon([(pad + x * k + 2, pad + y * k + 5) for x, y in pts], fill=(0, 0, 0, 110))
    spr.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
    d = ImageDraw.Draw(spr)
    poly = [(pad + x * k, pad + y * k) for x, y in pts]
    d.polygon(poly, fill=(255, 255, 255, 255))
    d.line(poly + [poly[0]], fill=(20, 20, 20, 255), width=max(2, int(1.6 * U)), joint='curve')
    return spr, pad


def cursor(img, pos, pressed=False):
    spr, pad = cursor_sprite(bool(pressed))
    img.paste(spr, (int(pos[0] - pad), int(pos[1] - pad)), spr)
    return img


def press(click):
    return 0 <= click < 0.25


def ring(img, c, t, scale=1.0):
    if not 0 <= t <= 1:
        return img
    d = ImageDraw.Draw(img, 'RGBA')
    r = (12 + 46 * ease(t)) * U * scale
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), outline=ACCENT + (int(230 * (1 - t)),), width=max(3, int(4 * U)))
    return img


def outline(img, box, a=1.0, pad=8):
    if a <= 0:
        return img
    p = pad * U
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle((x0 - p, y0 - p, x1 + p, y1 + p), min(int(26 * U), int((y1 - y0) / 2 + p)),
                        outline=ACCENT + (int(255 * a),), width=max(3, int(4 * U)))
    return img


def _check(d, cx, cy, size, fill, width):
    d.line([(cx - size * 0.5, cy), (cx - size * 0.15, cy + size * 0.35), (cx + size * 0.5, cy - size * 0.35)],
           fill=fill, width=width, joint='curve')


def badge(img, xy, text, a=1.0, color=GREEN):
    if a <= 0:
        return img
    f = font(25 * U, True)
    d = ImageDraw.Draw(img, 'RGBA')
    ok = text.startswith('✓')
    text = text.lstrip('✓ ')
    tw = d.textlength(text, font=f) + (32 * U if ok else 0)
    x, y = xy
    y += 12 * U * (1 - a)
    h = 26 * U
    d.rounded_rectangle((x - tw / 2 - 22 * U, y - h, x + tw / 2 + 22 * U, y + h), int(h), fill=color + (int(245 * a),))
    tx = x - tw / 2
    if ok:
        _check(d, tx + 11 * U, y, 17 * U, (255, 255, 255, int(255 * a)), max(3, int(4 * U)))
        tx += 32 * U
    d.text((tx, y), text, font=f, fill=(255, 255, 255, int(255 * a)), anchor='lm')
    return img


@lru_cache(maxsize=32)
def _caption_patch(step, text):
    f_txt, f_num = font(32 * U, True), font(27 * U, True)
    tmp = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    tw = tmp.textlength(text, font=f_txt)
    ph = int(68 * U)
    num_w = int(46 * U) if step else 0
    pw = int(tw + 52 * U + (num_w + 14 * U if step else 0))
    pad = int(20 * U)
    patch = Image.new('RGBA', (pw + pad * 2, ph + pad * 2), (0, 0, 0, 0))
    sh = Image.new('RGBA', patch.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 6, pad + pw, pad + ph + 6), ph // 2, fill=(0, 0, 0, 70))
    patch.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(patch)
    d.rounded_rectangle((pad, pad, pad + pw, pad + ph), ph // 2, fill=DARK + (242,))
    tx = pad + 26 * U
    cy = pad + ph / 2
    if step:
        d.ellipse((tx, cy - 23 * U, tx + 46 * U, cy + 23 * U), fill=ACCENT + (255,))
        d.text((tx + 23 * U, cy), str(step), font=f_num, fill=(255, 255, 255, 255), anchor='mm')
        tx += num_w + 14 * U
    d.text((tx, cy), text, font=f_txt, fill=(255, 255, 255, 255), anchor='lm')
    return patch, pad


def caption(img, step, text, a=1.0):
    if a <= 0:
        return img
    patch, pad = _caption_patch(step, text)
    if a < 1:
        patch = patch.copy()
        patch.putalpha(patch.getchannel('A').point(lambda v: int(v * a)))
    x = (W - patch.width) // 2
    y = int(H - patch.height + pad - 30 * U + 14 * U * (1 - a))
    img.paste(patch, (x, y), patch)
    return img


@lru_cache(maxsize=16)
def _progress_patch(active):
    f = font(20 * U, True)
    tmp = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    widths = [tmp.textlength(s, font=f) + 62 * U for s in STEPS]
    gap = 8 * U
    total = int(sum(widths) + gap * (len(STEPS) - 1) + 16 * U)
    h = int(46 * U)
    patch = Image.new('RGBA', (total + 2, h + 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(patch)
    d.rounded_rectangle((0, 0, total, h), h // 2, fill=(255, 255, 255, 240), outline=(225, 222, 214, 255))
    cx = 8 * U
    for i, (s, w) in enumerate(zip(STEPS, widths)):
        on, done = i + 1 == active, i + 1 < active
        if on:
            d.rounded_rectangle((cx, 5 * U, cx + w, h - 5 * U), int((h - 10 * U) / 2), fill=DARK + (255,))
        col = (255, 255, 255, 255) if on else ((60, 58, 52, 255) if done else (150, 146, 138, 255))
        d.ellipse((cx + 12 * U, h / 2 - 11 * U, cx + 34 * U, h / 2 + 11 * U), fill=(ACCENT if (on or done) else (200, 196, 188)) + (255,))
        if done:
            _check(d, cx + 23 * U, h / 2, 11 * U, (255, 255, 255, 255), max(2, int(2.2 * U)))
        else:
            d.text((cx + 23 * U, h / 2), str(i + 1), font=font(14 * U, True), fill=(255, 255, 255, 255), anchor='mm')
        d.text((cx + 44 * U, h / 2), s, font=f, fill=col, anchor='lm')
        cx += w + gap
    return patch


@lru_cache(maxsize=1)
def _band_bg():
    bg = Image.new('RGBA', (W, H), BG + (255,))
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((SX, SY + 14, SX + SW, SY + SH + 14), int(20 * U), fill=(60, 40, 20, 60))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(18 * U))))
    mask = Image.new('L', (SW, SH), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, SW - 1, SH - 1), int(20 * U), fill=255)
    return bg.convert('RGB'), mask


def frame(screen, active):
    """Place a rendered screen (SW x SH) under the progress bar."""
    bg, mask = _band_bg()
    out = bg.copy()
    out.paste(screen, (SX, SY), mask)
    p = _progress_patch(active)
    out.paste(p, ((W - p.width) // 2, int(16 * U)), p)
    return out


def progress_only(img, active):
    p = _progress_patch(active)
    img.paste(p, ((W - p.width) // 2, int(16 * U)), p)
    return img


def window(img, w, bar=0, radius=16):
    h = round(img.height * w / img.width)
    shot = img.resize((w, h), Image.LANCZOS)
    win = Image.new('RGBA', (w, h + bar), (236, 233, 226, 255))
    win.paste(shot, (0, bar))
    d = ImageDraw.Draw(win)
    if bar:
        for k, c in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
            d.ellipse((16 + k * 22, bar / 2 - 7, 30 + k * 22, bar / 2 + 7), fill=c)
    m = Image.new('L', win.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h + bar - 1), radius, fill=255)
    win.putalpha(m)
    g = int(40 * U)
    out = Image.new('RGBA', (w + g * 2, h + bar + g * 2), (0, 0, 0, 0))
    sh = Image.new('RGBA', out.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((g, g + 22, g + w, g + h + bar + 22), radius, fill=(60, 35, 15, 85))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(22 * U))))
    out.alpha_composite(win, (g, g))
    return out, g


@lru_cache(maxsize=4)
def glow_bg(box=(0.33, 0.06, 0.72, 0.76), alpha=70):
    img = Image.new('RGBA', (W, H), BG + (255,))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse((box[0] * W, box[1] * H, box[2] * W, box[3] * H), fill=(236, 170, 130, alpha))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(int(120 * U))))
    return img.convert('RGB')


def paste_fade(img, sprite, xy, a):
    if a <= 0:
        return img
    if a < 1:
        sprite = sprite.copy()
        sprite.putalpha(sprite.getchannel('A').point(lambda v: int(v * a)))
    img.paste(sprite, (int(xy[0]), int(xy[1])), sprite)
    return img


def text(img, xy, s, size, color, a=1.0, bold=True, anchor='lm'):
    if a <= 0:
        return img
    ImageDraw.Draw(img, 'RGBA').text(xy, s, font=font(size, bold), fill=color + (int(255 * a),), anchor=anchor)
    return img


# ---------- recordings ----------

def gif_timeline(frames_idx, durs, stretch=1.0):
    """Cumulative timeline (seconds) for a list of GIF frame indexes."""
    tl, t = [], 0.0
    for i in frames_idx:
        tl.append((t, i))
        t += durs[i] / 1000 * stretch
    return tl, t


def gif_at(frames, tl, s, blend=0.35):
    """Frame at time s; crossfades into the next frame during the last `blend` share of each hold."""
    k = 0
    while k + 1 < len(tl) and tl[k + 1][0] <= s:
        k += 1
    cur = frames[tl[k][1]]
    if k + 1 >= len(tl):
        return cur
    t0, t1 = tl[k][0], tl[k + 1][0]
    f = (s - t0) / max(1e-6, t1 - t0)
    start = 1 - blend
    if f <= start:
        return cur
    return Image.blend(cur, frames[tl[k + 1][1]], ease((f - start) / blend))


# ---------- timeline + export ----------

def scene(dur, fn):
    scenes.append((max(1, round(dur * FPS)), fn))


def export(out_dir, base, poster_at=3.0, xfade=0.35, preview_sheet=None):
    import imageio_ffmpeg
    vdir = f'{out_dir}/video'
    os.makedirs(vdir, exist_ok=True)
    mp4 = f'{vdir}/{base}.mp4'
    w = imageio_ffmpeg.write_frames(
        mp4, (W, H), fps=FPS, codec='libx264', quality=None, bitrate=None, macro_block_size=8,
        output_params=['-crf', '14', '-preset', 'slow', '-profile:v', 'high', '-x264-params', 'aq-mode=3', '-movflags', '+faststart'])
    w.send(None)
    XF = round(xfade * FPS)
    tail = []
    small, sheet, n_out = [], [], 0
    poster_idx = round(poster_at * FPS)
    total = sum(n for n, _ in scenes) - XF * (len(scenes) - 1)
    sheet_at = {int(total * k / 20) + 10 for k in range(20)}
    crop_at = {int(total * k / 6) + 30 for k in range(1, 6)}
    crops = []

    def emit(f):
        nonlocal n_out
        w.send(f.tobytes())
        if n_out % 5 == 0:
            small.append(f.resize((960, 540), Image.LANCZOS))
        if n_out == poster_idx:
            f.save(f'{vdir}/{base}-poster.webp', 'WEBP', quality=88)
        if preview_sheet and n_out in sheet_at:
            sheet.append(f.resize((640, 360), Image.LANCZOS))
        if preview_sheet and n_out in crop_at:
            crops.append(f)
        n_out += 1

    for si, (n, fn) in enumerate(scenes):
        for i in range(n):
            f = fn(i / max(1, n - 1), i / FPS)
            if si > 0 and i < XF:
                f = Image.blend(tail[i], f, ease((i + 1) / (XF + 1)))
                if i == XF - 1:
                    tail = []
                emit(f)
                continue
            if si < len(scenes) - 1 and i >= n - XF:
                tail.append(f)
            else:
                emit(f)
    w.close()
    print('mp4', round(n_out / FPS, 1), 's', W, 'x', H, FPS, 'fps', os.path.getsize(mp4) // 1024, 'KB')
    aw = f'{out_dir}/{base}.webp'
    small[0].save(aw, 'WEBP', save_all=True, append_images=small[1:], duration=round(5000 / FPS), loop=0, quality=65, method=4)
    print('webp', len(small), 'frames', os.path.getsize(aw) // 1024, 'KB')
    if preview_sheet:
        cols = 4
        rows = math.ceil(len(sheet) / cols)
        sh = Image.new('RGB', (640 * cols, 360 * rows), 'white')
        for k, f in enumerate(sheet):
            sh.paste(f, ((k % cols) * 640, (k // cols) * 360))
        sh.save(preview_sheet)
        # 100% crops from the centre of a few frames, to check real sharpness
        cw, ch = 1000, 560
        cs = Image.new('RGB', (cw, ch * len(crops)), 'white')
        for k, f in enumerate(crops):
            cs.paste(f.crop(((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2)), (0, k * ch))
        cs.save(preview_sheet.replace('.png', '_100pct.png'))
