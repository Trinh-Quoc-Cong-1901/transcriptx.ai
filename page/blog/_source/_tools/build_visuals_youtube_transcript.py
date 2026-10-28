"""Build article visuals for how-to-get-youtube-transcript from page/blog/_source.

Outputs (into the post's images/):
  static highlighted webp screenshots, a phone duo image,
  how-to-get-youtube-transcript-transcriptx.mp4 (1280x800, 30fps) and an animated .webp (960x600).
"""
import math, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import imageio_ffmpeg

ROOT = '/Users/trinhquoccong/Documents/seo-main/TranscriptX.ai/page/blog'
SRC = f'{ROOT}/_source'
OUT = f'{ROOT}/how-to-get-youtube-transcript/images'

BG = (248, 247, 244)
DARK = (43, 42, 38)
ACCENT = (204, 88, 46)
W, H = 1280, 800
FPS = 30
FONT = '/System/Library/Fonts/HelveticaNeue.ttc'


def font(size, bold=False):
    return ImageFont.truetype(FONT, size, index=1 if bold else 0)


def load(p):
    return Image.open(f'{SRC}/{p}').convert('RGB')


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return tuple(x + (y - x) * t for x, y in zip(a, b))


# ---------- drawing helpers ----------

def highlight(img, box, alpha=1.0, width=None, pad=10):
    """Orange rounded outline + soft glow around box (image coords)."""
    if alpha <= 0:
        return img
    x0, y0, x1, y1 = box
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    w = width or max(4, round(img.width / 300))
    r = min(28, (y1 - y0) // 2)
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((x0, y0, x1, y1), r, outline=ACCENT + (int(70 * alpha),), width=w * 3)
    layer = layer.filter(ImageFilter.GaussianBlur(w * 1.5))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((x0, y0, x1, y1), r, outline=ACCENT + (int(255 * alpha),), width=w)
    out = img.convert('RGBA')
    out.alpha_composite(layer)
    return out.convert('RGB')


def ripple(img, center, t, scale=1.0):
    """Click ripple, t in 0..1."""
    if not 0 <= t <= 1:
        return img
    cx, cy = center
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = (14 + 46 * t) * scale
    a = int(200 * (1 - t))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=ACCENT + (a,), width=max(3, int(5 * scale)))
    r2 = 12 * scale
    d.ellipse((cx - r2, cy - r2, cx + r2, cy + r2), fill=ACCENT + (int(70 * (1 - t)),))
    out = img.convert('RGBA')
    out.alpha_composite(layer)
    return out.convert('RGB')


def pad_to_aspect(img, aspect=W / H, color=None):
    color = color or img.getpixel((5, 5))
    w, h = img.size
    if w / h > aspect:
        nh = round(w / aspect)
        canvas = Image.new('RGB', (w, nh), color)
        off = (0, (nh - h) // 2)
    else:
        nw = round(h * aspect)
        canvas = Image.new('RGB', (nw, h), color)
        off = ((nw - w) // 2, 0)
    canvas.paste(img, off)
    return canvas, off


def shift(box, off):
    if len(box) == 2:
        return (box[0] + off[0], box[1] + off[1])
    return (box[0] + off[0], box[1] + off[1], box[2] + off[0], box[3] + off[1])


def view_for(box, img_size, zoom_pad=0.35):
    """16:10 crop rect centred on box, clamped inside the image."""
    iw, ih = img_size
    x0, y0, x1, y1 = box
    bw, bh = (x1 - x0) * (1 + zoom_pad * 2), (y1 - y0) * (1 + zoom_pad * 2)
    if bw / bh < W / H:
        bw = bh * W / H
    else:
        bh = bw * H / W
    bw, bh = min(bw, iw), min(bh, ih)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    cx = min(max(cx, bw / 2), iw - bw / 2)
    cy = min(max(cy, bh / 2), ih - bh / 2)
    return (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2)


def render(img, rect, size=(W, H)):
    x0, y0, x1, y1 = rect
    return img.resize(size, Image.LANCZOS, box=(x0, y0, x1, y1))


def caption(frame, step, text, alpha=1.0):
    if alpha <= 0:
        return frame
    f_txt = font(30, True)
    f_num = font(26, True)
    d0 = ImageDraw.Draw(frame)
    tw = d0.textlength(text, font=f_txt)
    pill_h = 64
    num_w = 44 if step else 0
    pw = tw + 48 + (num_w + 14 if step else 0)
    x0 = (W - pw) / 2
    y0 = H - pill_h - 34
    layer = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    shadow = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((x0, y0 + 6, x0 + pw, y0 + pill_h + 6), pill_h // 2, fill=(0, 0, 0, int(60 * alpha)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((x0, y0, x0 + pw, y0 + pill_h), pill_h // 2, fill=DARK + (int(240 * alpha),))
    tx = x0 + 24
    if step:
        cy = y0 + pill_h / 2
        d.ellipse((tx, cy - 22, tx + 44, cy + 22), fill=ACCENT + (int(255 * alpha),))
        d.text((tx + 22, cy), str(step), font=f_num, fill=(255, 255, 255, int(255 * alpha)), anchor='mm')
        tx += num_w + 14
    d.text((tx, y0 + pill_h / 2), text, font=f_txt, fill=(255, 255, 255, int(255 * alpha)), anchor='lm')
    out = frame.convert('RGBA')
    out.alpha_composite(shadow)
    out.alpha_composite(layer)
    return out.convert('RGB')


def rounded(img, radius):
    mask = Image.new('L', img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius, fill=255)
    out = Image.new('RGBA', img.size)
    out.paste(img, (0, 0), mask)
    return out


def phone(img, height):
    """Simple phone frame around a mobile screenshot."""
    scr = img.resize((round(img.width * height / img.height), height), Image.LANCZOS)
    bez = max(10, height // 55)
    fw, fh = scr.width + bez * 2, scr.height + bez * 2
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    ImageDraw.Draw(frame).rounded_rectangle((0, 0, fw - 1, fh - 1), bez * 4, fill=(30, 30, 30, 255))
    frame.alpha_composite(rounded(scr, bez * 3), (bez, bez))
    sh = Image.new('RGBA', (fw + 80, fh + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((40, 52, fw + 40, fh + 52), bez * 4, fill=(0, 0, 0, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    sh.alpha_composite(frame, (40, 40))
    return sh


# ---------- sources ----------
share = load('external/youtube/youtube-share-copy-link.png')            # 1501x1048
tool = load('youtube-transcript/youtube-transcript-tool.png')          # 2000x1001
result = load('transcript/transcript-result-light.png')                # 2000x987
dl = load('transcript/transcript-download-menu-open.png')              # 2000x995
m_home = load('mobile/mobile-homepage.png')
m_result = load('mobile/mobile-transcript-result.png')
gif = Image.open(f'{SRC}/youtube-transcript/demo-youtube-to-transcript.gif')
gif_frames, gif_durs = [], []
for i in range(gif.n_frames):
    gif.seek(i)
    gif_frames.append(gif.convert('RGB'))
    gif_durs.append(gif.info.get('duration', 100))
logo = Image.open(f'{SRC}/brand/logo/logo_256.png').convert('RGBA')

SHARE_COPY = (958, 256, 1142, 318)
TOOL_INPUT = (653, 384, 1692, 580)
DL_BTN = (1180, 126, 1228, 174)
DL_MENU = (960, 184, 1228, 450)
RES_COPY = (1245, 127, 1383, 176)
GIF_INPUT = (284, 305, 1052, 450)
GIF_ARROW = (1022, 420)
GIF_COPY = (711, 92, 828, 128)


def save_webp(img, name, width=1600):
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(f'{OUT}/{name}', 'WEBP', quality=84)
    print('static', name, img.size, os.path.getsize(f'{OUT}/{name}') // 1024, 'KB')


def phone_duo():
    canvas = Image.new('RGBA', (1600, 1000), BG + (255,))
    a, b = phone(m_home, 860), phone(m_result, 860)
    gap = 90
    x = (1600 - a.width - b.width - gap + 80) // 2
    canvas.alpha_composite(a, (x - 40, 30))
    canvas.alpha_composite(b, (x + a.width - 80 + gap, 30))
    return canvas.convert('RGB')


def statics():
    save_webp(highlight(share, SHARE_COPY), 'copy-youtube-video-link-share.webp')
    save_webp(highlight(tool, TOOL_INPUT, pad=8), 'youtube-transcript-tool-paste-link.webp')
    save_webp(highlight(highlight(dl, DL_MENU, pad=6), DL_BTN, pad=6), 'download-youtube-transcript-txt-docx-pdf-srt-vtt.webp')
    save_webp(phone_duo(), 'youtube-transcript-on-phone-transcriptx.webp')


# ---------- video ----------
frames = []  # list of (image, duration_ms)


def add(img, n=1):
    for _ in range(n):
        frames.append(img)


def secs(s):
    return max(1, round(s * FPS))


def kb_scene(base, start_rect, end_rect, dur, fx=None, step=None, text=None, cap_in=0.0):
    n = secs(dur)
    for i in range(n):
        t = i / max(1, n - 1)
        rect = lerp(start_rect, end_rect, ease(t))
        img = fx(base, t) if fx else base
        fr = render(img, rect)
        if text:
            fr = caption(fr, step, text, ease((i / FPS - cap_in) / 0.35) if cap_in is not None else 1)
        add(fr)


def card(title, sub, dur, url=None):
    n = secs(dur)
    for i in range(n):
        t = i / FPS
        a = ease(t / 0.5) * (1 - ease((t - dur + 0.4) / 0.4))
        img = Image.new('RGBA', (W, H), BG + (255,))
        d = ImageDraw.Draw(img)
        lg = logo.resize((96, 96), Image.LANCZOS)
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        layer.alpha_composite(lg, (W // 2 - 48, 210))
        ld = ImageDraw.Draw(layer)
        ld.text((W // 2, 360), title, font=font(54, True), fill=DARK + (255,), anchor='mm')
        ld.text((W // 2, 430), sub, font=font(30), fill=(110, 106, 98, 255), anchor='mm')
        if url:
            ld.rounded_rectangle((W // 2 - 300, 490, W // 2 + 300, 556), 33, fill=DARK + (255,))
            ld.text((W // 2, 523), url, font=font(28, True), fill=(255, 255, 255, 255), anchor='mm')
        r, g, b, al = layer.split()
        layer.putalpha(al.point(lambda v: int(v * a)))
        img.alpha_composite(layer)
        add(img.convert('RGB'))


def build_video():
    card('How to Get a YouTube Transcript', 'with TranscriptX, in 4 steps', 2.6)

    # Step 1: YouTube Share -> Copy link
    base, off = pad_to_aspect(share)
    full = (0, 0, base.width, base.height)
    btn = shift(SHARE_COPY, off)
    zoom = view_for(btn, base.size, zoom_pad=1.6)
    cap = (1, 'On YouTube, click Share, then Copy link')
    kb_scene(base, full, full, 0.7, step=cap[0], text=cap[1], cap_in=0.1)
    kb_scene(base, full, zoom, 1.3, step=cap[0], text=cap[1], cap_in=None)
    center = ((btn[0] + btn[2]) / 2, (btn[1] + btn[3]) / 2)
    kb_scene(base, zoom, zoom, 1.6, fx=lambda b, t: ripple(highlight(b, btn, alpha=ease(t * 3)), center, (t - 0.35) / 0.5, 1.6),
             step=cap[0], text=cap[1], cap_in=None)

    # Step 2: paste in TranscriptX (real recording, zoomed on the input while typing)
    cap = (2, 'Paste the link into TranscriptX')
    gfull = (0, 0, W, H)
    gzoom = view_for(GIF_INPUT, (W, H), zoom_pad=0.04)
    typing = list(range(0, 29))
    t_total = sum(gif_durs[i] for i in typing) / 1000
    elapsed = 0.0
    for i in typing:
        n = secs(gif_durs[i] / 1000 if i not in (0, 28) else (0.8 if i == 0 else 0.6))
        for k in range(n):
            tt = elapsed / FPS
            rect = lerp(gfull, gzoom, ease(tt / 0.9))
            add(caption(render(gif_frames[i], rect), cap[0], cap[1], ease(tt / 0.35)))
            elapsed += 1
    # click the arrow
    n = secs(1.0)
    for k in range(n):
        t = k / (n - 1)
        img = ripple(highlight(gif_frames[28], (GIF_ARROW[0] - 20, GIF_ARROW[1] - 20, GIF_ARROW[0] + 20, GIF_ARROW[1] + 20), alpha=ease(t * 3), pad=6),
                     GIF_ARROW, (t - 0.3) / 0.6)
        add(caption(render(img, lerp(gzoom, gfull, ease((t - 0.6) / 0.4))), cap[0], 'Click the arrow to start'))

    # Step 3: processing -> transcript
    cap = (3, 'Your transcript is ready in seconds')
    for i in range(29, 40):
        add(caption(render(gif_frames[i], gfull), cap[0], cap[1]), secs(gif_durs[i] / 1000))
    res = gif_frames[40]
    text_zone = view_for((100, 160, 830, 450), (W, H), zoom_pad=0.08)
    kb_scene(res, gfull, gfull, 0.8, step=cap[0], text=cap[1], cap_in=None)
    kb_scene(res, gfull, text_zone, 1.4, step=cap[0], text='Timestamped paragraphs, with the video on the side', cap_in=None)
    kb_scene(res, text_zone, text_zone, 1.0, step=cap[0], text='Timestamped paragraphs, with the video on the side', cap_in=None)

    # Step 4: copy or download
    cap = (4, 'Copy it, or download TXT, DOCX, PDF, SRT, VTT')
    base, off = pad_to_aspect(result)
    full = (0, 0, base.width, base.height)
    cbtn = shift(RES_COPY, off)
    czoom = view_for((1170, 120, 1390, 180), base.size, zoom_pad=1.4)
    ccenter = ((cbtn[0] + cbtn[2]) / 2, (cbtn[1] + cbtn[3]) / 2)
    kb_scene(base, full, czoom, 1.2, step=cap[0], text=cap[1], cap_in=0.0)
    kb_scene(base, czoom, czoom, 1.3, fx=lambda b, t: ripple(highlight(b, cbtn, alpha=ease(t * 3)), ccenter, (t - 0.3) / 0.5, 1.5),
             step=cap[0], text='Click Copy to grab the whole transcript', cap_in=None)
    base2, off2 = pad_to_aspect(dl)
    menu = shift(DL_MENU, off2)
    dbtn = shift(DL_BTN, off2)
    mzoom = view_for((menu[0], dbtn[1], dbtn[2] + 160, menu[3]), base2.size, zoom_pad=0.35)
    kb_scene(base2, czoom, mzoom, 1.0, step=cap[0], text='Or download it as a file', cap_in=None)
    kb_scene(base2, mzoom, mzoom, 2.0, fx=lambda b, t: highlight(b, menu, alpha=ease(t * 2.5), pad=6),
             step=cap[0], text='TXT, DOCX, PDF, SRT or VTT', cap_in=None)

    # Phone
    d = phone_duo()
    d = d.resize((round(d.width * 680 / d.height), 680), Image.LANCZOS)
    duo = Image.new('RGB', (W, H), BG)
    duo.paste(d, ((W - d.width) // 2, 6))
    n = secs(2.8)
    for k in range(n):
        t = k / (n - 1)
        rect = lerp((64, 40, W - 64, H - 40), (0, 0, W, H), ease(t))
        add(caption(render(duo, rect), None, 'Works the same on your phone', ease(t / 0.15)))

    card('Get a transcript of any YouTube video', 'Free · No account needed', 3.0, url='transcriptx.ai/youtube-transcript')

    # crossfade-free; write mp4
    mp4 = f'{OUT}/how-to-get-youtube-transcript-transcriptx.mp4'
    w = imageio_ffmpeg.write_frames(mp4, (W, H), fps=FPS, codec='libx264', quality=7,
                                    macro_block_size=16, output_params=['-pix_fmt', 'yuv420p', '-movflags', '+faststart'])
    w.send(None)
    for f in frames:
        w.send(f.tobytes())
    w.close()
    print('mp4', len(frames) / FPS, 's', os.path.getsize(mp4) // 1024, 'KB')

    frames[secs(2.6) + secs(2.0)].save(f'{OUT}/how-to-get-youtube-transcript-transcriptx-poster.webp', 'WEBP', quality=84)

    # animated webp for the article: 10 fps, 960x600
    step = FPS // 10
    small = [f.resize((960, 600), Image.LANCZOS) for f in frames[::step]]
    awebp = f'{OUT}/how-to-get-youtube-transcript-transcriptx.webp'
    small[0].save(awebp, 'WEBP', save_all=True, append_images=small[1:], duration=100, loop=0, quality=62, method=4)
    print('webp anim', len(small), 'frames', os.path.getsize(awebp) // 1024, 'KB')


if __name__ == '__main__':
    statics()
    if 'static' not in sys.argv:
        build_video()
