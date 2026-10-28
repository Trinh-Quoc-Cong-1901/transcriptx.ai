"""Shared helpers for TranscriptX walkthrough videos (cursor, click ring, badges, progress bar, framing, export).

Usage:
    import video_kit as vk
    vk.STEPS[:] = ['Copy link', 'Paste', ...]
    vk.scene(2.5, lambda t, s: frame)   # t: 0..1, s: seconds into the scene
    vk.export(out_dir, 'basename')
"""
import importlib.util, math, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)

W, H, FPS = bv.W, bv.H, bv.FPS
BG, DARK, ACCENT = bv.BG, bv.DARK, bv.ACCENT
GREEN = (46, 125, 72)
font, ease, lerp, render = bv.font, bv.ease, bv.lerp, bv.render
STEPS = []
scenes = []


def to_out(pt, rect):
    s = W / (rect[2] - rect[0])
    return ((pt[0] - rect[0]) * s, (pt[1] - rect[1]) * s), s


def box_out(box, rect):
    (x0, y0), _ = to_out(box[:2], rect)
    (x1, y1), _ = to_out(box[2:], rect)
    return (x0, y0, x1, y1)


def cursor(frame, pos, press=0.0):
    x, y = pos
    k = 2.1 * (1 - 0.12 * press)
    pts = [(0, 0), (0, 17), (4.5, 13), (7.5, 20), (10, 19), (7, 12.5), (12.5, 12.5)]
    poly = [(x + px * k, y + py * k) for px, py in pts]
    sh = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).polygon([(px + 2, py + 4) for px, py in poly], fill=(0, 0, 0, 90))
    out = frame.convert('RGBA')
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    d = ImageDraw.Draw(out)
    d.polygon(poly, fill=(255, 255, 255, 255))
    d.line(poly + [poly[0]], fill=(20, 20, 20, 255), width=2, joint='curve')
    return out.convert('RGB')


def ring(frame, c, t, s=1.0):
    if not 0 <= t <= 1:
        return frame
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    r = (10 + 40 * ease(t)) * s
    ImageDraw.Draw(lay).ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), outline=ACCENT + (int(220 * (1 - t)),), width=max(3, int(4 * s)))
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def outline(frame, box, a=1.0, pad=8, width=4):
    if a <= 0:
        return frame
    x0, y0, x1, y1 = box
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle((x0 - pad, y0 - pad, x1 + pad, y1 + pad), min(26, (y1 - y0) // 2 + pad),
                                          outline=ACCENT + (int(255 * a),), width=width)
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def check(d, cx, cy, size, fill, width=3):
    d.line([(cx - size * 0.5, cy), (cx - size * 0.15, cy + size * 0.35), (cx + size * 0.5, cy - size * 0.35)],
           fill=fill, width=width, joint='curve')


def badge(frame, xy, text, a=1.0, color=GREEN):
    if a <= 0:
        return frame
    f = font(24, True)
    d0 = ImageDraw.Draw(frame)
    ok = text.startswith('✓')
    text = text.lstrip('✓ ')
    tw = d0.textlength(text, font=f) + (30 if ok else 0)
    x, y = xy
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    yo = 10 * (1 - a)
    d.rounded_rectangle((x - tw / 2 - 20, y - 24 + yo, x + tw / 2 + 20, y + 24 + yo), 24, fill=color + (int(245 * a),))
    tx = x - tw / 2
    if ok:
        check(d, tx + 10, y + yo, 16, (255, 255, 255, int(255 * a)), 4)
        tx += 30
    d.text((tx, y + yo), text, font=f, fill=(255, 255, 255, int(255 * a)), anchor='lm')
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def progress(frame, active):
    f = font(19, True)
    d0 = ImageDraw.Draw(frame)
    widths = [d0.textlength(s, font=f) + 58 for s in STEPS]
    total = sum(widths) + 8 * (len(STEPS) - 1) + 16
    x = (W - total) / 2
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle((x, 16, x + total, 60), 22, fill=(255, 255, 255, 235), outline=(225, 222, 214, 255))
    cx = x + 8
    for i, (s, w) in enumerate(zip(STEPS, widths)):
        on, done = i + 1 == active, i + 1 < active
        if on:
            d.rounded_rectangle((cx, 21, cx + w, 55), 17, fill=DARK + (255,))
        col = (255, 255, 255, 255) if on else ((60, 58, 52, 255) if done else (150, 146, 138, 255))
        dot = ACCENT if (on or done) else (200, 196, 188)
        d.ellipse((cx + 12, 28, cx + 32, 48), fill=dot + (255,))
        if done:
            check(d, cx + 22, 38, 10, (255, 255, 255, 255), 2)
        else:
            d.text((cx + 22, 38), str(i + 1), font=font(13, True), fill=(255, 255, 255, 255), anchor='mm')
        d.text((cx + 42, 38), s, font=f, fill=col, anchor='lm')
        cx += w + 8
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def band(fr, active):
    """Shrink the scene into a framed screen under the progress bar."""
    sw, sh_ = int(W * 0.9), int(H * 0.9)
    x, y = (W - sw) // 2, 72
    canvas = Image.new('RGBA', (W, H), BG + (255,))
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x, y + 10, x + sw, y + sh_ + 10), 18, fill=(60, 40, 20, 60))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    scr = fr.resize((sw, sh_), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', (sw, sh_), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, sw - 1, sh_ - 1), 18, fill=255)
    scr.putalpha(m)
    canvas.alpha_composite(scr, (x, y))
    return progress(canvas.convert('RGB'), active)


def cap(frame, step, text, a=1.0):
    return bv.caption(frame, step, text, a)


def path(p0, p1, t):
    e = ease(t)
    return (p0[0] + (p1[0] - p0[0]) * e, p0[1] + (p1[1] - p0[1]) * e - 40 * (1 - (2 * e - 1) ** 2))


def press(click):
    return 1.0 if 0 <= click < 0.25 else 0.0


def window(img, w, bar=30, radius=14):
    h = round(img.height * w / img.width)
    shot = img.resize((w, h), Image.LANCZOS)
    win = Image.new('RGBA', (w, h + bar), (0, 0, 0, 0))
    m = Image.new('L', win.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h + bar - 1), radius, fill=255)
    body = Image.new('RGBA', win.size, (236, 233, 226, 255))
    body.paste(shot, (0, bar))
    dd = ImageDraw.Draw(body)
    for k, c in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
        dd.ellipse((14 + k * 20, bar // 2 - 6, 26 + k * 20, bar // 2 + 6), fill=c)
    win.paste(body, (0, 0), m)
    sh = Image.new('RGBA', (w + 120, h + bar + 120), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((60, 78, w + 60, h + bar + 78), 16, fill=(60, 40, 20, 80))
    sh = sh.filter(ImageFilter.GaussianBlur(24))
    sh.alpha_composite(win, (60, 60))
    return sh


def fade_layer(img, layer, a):
    layer.putalpha(layer.getchannel('A').point(lambda v: int(v * a)))
    img.alpha_composite(layer)


def glow_bg(box=(620, 60, 1380, 820), alpha=70):
    img = Image.new('RGBA', (W, H), BG + (255,))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse(box, fill=(236, 170, 130, alpha))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(90)))
    return img


def scene(dur, fn):
    n = max(1, round(dur * FPS))
    scenes.append([fn(i / max(1, n - 1), i / FPS) for i in range(n)])


def export(out_dir, base, poster_at=2.6, sheet_path=None):
    import imageio_ffmpeg
    xf = round(0.3 * FPS)
    frames = list(scenes[0])
    for sc in scenes[1:]:
        for k in range(xf):
            frames[-xf + k] = Image.blend(frames[-xf + k], sc[k], (k + 1) / (xf + 1))
        frames += sc[xf:]
    vdir = f'{out_dir}/video'
    os.makedirs(vdir, exist_ok=True)
    mp4 = f'{vdir}/{base}.mp4'
    w = imageio_ffmpeg.write_frames(mp4, (W, H), fps=FPS, codec='libx264', quality=7, macro_block_size=16,
                                    output_params=['-movflags', '+faststart'])
    w.send(None)
    for f in frames:
        w.send(f.tobytes())
    w.close()
    print('mp4', round(len(frames) / FPS, 1), 's', os.path.getsize(mp4) // 1024, 'KB')
    frames[round(poster_at * FPS)].save(f'{vdir}/{base}-poster.webp', 'WEBP', quality=86)
    small = [f.resize((960, 600), Image.LANCZOS) for f in frames[::3]]
    aw = f'{out_dir}/{base}.webp'
    small[0].save(aw, 'WEBP', save_all=True, append_images=small[1:], duration=100, loop=0, quality=62, method=4)
    print('webp', os.path.getsize(aw) // 1024, 'KB')
    if sheet_path:
        sheet = Image.new('RGB', (640 * 4, 400 * 5), 'white')
        idx = [int(len(frames) * k / 20) + 5 for k in range(20)]
        for k, i in enumerate(idx):
            sheet.paste(frames[min(i, len(frames) - 1)].resize((640, 400)), ((k % 4) * 640, (k // 4) * 400))
        sheet.save(sheet_path)
    return frames
