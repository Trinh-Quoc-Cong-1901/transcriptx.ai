"""Walkthrough video v2 for how-to-get-youtube-transcript.

One sample video (Shayne Ward - Until You) from start to end:
hook intro -> 1 Share/Copy link -> 2 paste into YouTube Transcript -> 3 transcribing -> result
-> 4 Copy (copies the text) -> 5 Download (button next to Copy) opens the format menu -> phone -> CTA.
Animated cursor with clicks, 5-step progress bar, crossfades between scenes.
Reuses helpers + sources from build_visuals_youtube_transcript.py.
"""
import importlib.util, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)

W, H, FPS = bv.W, bv.H, bv.FPS
BG, DARK, ACCENT = bv.BG, bv.DARK, bv.ACCENT
font, ease, lerp, render = bv.font, bv.ease, bv.lerp, bv.render
OUT = bv.OUT
GREEN = (46, 125, 72)

STEPS = ['Copy link', 'Paste', 'Transcribe', 'Copy', 'Download']

menu_img = Image.open(f'{bv.SRC}/transcript/download-format-menu.png').convert('RGBA')
res = bv.gif_frames[40]                  # Shayne Ward result, 1280x800
GIF_DL = (681, 110)                       # download icon, next to Copy
GIF_COPY_C = (769, 110)                   # Copy button centre
MENU_BOX = (561, 129, 695, 262)           # where the menu opens (base coords)


# ---------- overlays in output space ----------

def to_out(pt, rect):
    s = W / (rect[2] - rect[0])
    return ((pt[0] - rect[0]) * s, (pt[1] - rect[1]) * s), s


def cursor(frame, pos, press=0.0):
    x, y = pos
    k = 2.1 * (1 - 0.12 * press)
    pts = [(0, 0), (0, 17), (4.5, 13), (7.5, 20), (10, 19), (7, 12.5), (12.5, 12.5)]
    poly = [(x + px * k, y + py * k) for px, py in pts]
    sh = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).polygon([(px + 2, py + 4) for px, py in poly], fill=(0, 0, 0, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    out = frame.convert('RGBA')
    out.alpha_composite(sh)
    d = ImageDraw.Draw(out)
    d.polygon(poly, fill=(255, 255, 255, 255))
    d.line(poly + [poly[0]], fill=(20, 20, 20, 255), width=2, joint='curve')
    return out.convert('RGB')


def ring(frame, c, t, s=1.0):
    if not 0 <= t <= 1:
        return frame
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    r = (10 + 40 * ease(t)) * s
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), outline=ACCENT + (int(220 * (1 - t)),), width=max(3, int(4 * s)))
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def outline(frame, box, a=1.0, pad=8):
    if a <= 0:
        return frame
    x0, y0, x1, y1 = box
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle((x0 - pad, y0 - pad, x1 + pad, y1 + pad), min(26, (y1 - y0) // 2 + pad), outline=ACCENT + (int(255 * a),), width=4)
    out = frame.convert('RGBA')
    out.alpha_composite(lay)
    return out.convert('RGB')


def check(d, cx, cy, size, fill, width=3):
    d.line([(cx - size * 0.5, cy), (cx - size * 0.15, cy + size * 0.35), (cx + size * 0.5, cy - size * 0.35)],
           fill=fill, width=width, joint='curve')


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


def badge(frame, xy, text, a=1.0, color=GREEN):
    if a <= 0:
        return frame
    f = font(24, True)
    d0 = ImageDraw.Draw(frame)
    tw = d0.textlength(text, font=f)
    x, y = xy
    lay = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    yo = 10 * (1 - a)
    ok = text.startswith('✓')
    text = text.lstrip('✓ ')
    tw = d0.textlength(text, font=f) + (30 if ok else 0)
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
    """Top bar: 5 labelled steps, active one in accent."""
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


def cap(frame, step, text, a=1.0):
    return bv.caption(frame, step, text, a)


def path(p0, p1, t):
    """Cursor path with a slight arc."""
    e = ease(t)
    x = p0[0] + (p1[0] - p0[0]) * e
    y = p0[1] + (p1[1] - p0[1]) * e - 40 * (1 - (2 * e - 1) ** 2)
    return (x, y)


# ---------- scenes ----------
scenes = []


def scene(dur, fn):
    n = max(1, round(dur * FPS))
    scenes.append([fn(i / max(1, n - 1), i / FPS) for i in range(n)])


def window(img, w):
    """Screenshot in a browser-window frame with shadow."""
    h = round(img.height * w / img.width)
    shot = img.resize((w, h), Image.LANCZOS)
    bar = 30
    win = Image.new('RGBA', (w, h + bar), (0, 0, 0, 0))
    m = Image.new('L', win.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h + bar - 1), 14, fill=255)
    body = Image.new('RGBA', win.size, (236, 233, 226, 255))
    body.paste(shot, (0, bar))
    dd = ImageDraw.Draw(body)
    for k, c in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
        dd.ellipse((14 + k * 20, 10, 26 + k * 20, 22), fill=c)
    win.paste(body, (0, 0), m)
    sh = Image.new('RGBA', (w + 120, h + bar + 120), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((60, 78, w + 60, h + bar + 78), 16, fill=(60, 40, 20, 80))
    sh = sh.filter(ImageFilter.GaussianBlur(24))
    sh.alpha_composite(win, (60, 60))
    return sh


WIN = window(res, 700)


def intro(t, s):
    img = Image.new('RGBA', (W, H), BG + (255,))
    # warm glow
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((620, 60, 1380, 820), fill=(236, 170, 130, 70))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(img)

    def fade(start, dur=0.45):
        return ease((s - start) / dur)

    a = fade(0.0)
    lg = bv.logo.resize((44, 44), Image.LANCZOS)
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    lay.alpha_composite(lg, (80, 150))
    ImageDraw.Draw(lay).text((136, 172), 'TranscriptX', font=font(30, True), fill=DARK + (255,), anchor='lm')
    lay.putalpha(lay.getchannel('A').point(lambda v: int(v * a)))
    img.alpha_composite(lay)
    lines = [('YouTube video', DARK, 0.25), ('to transcript', ACCENT, 0.55), ('in seconds.', DARK, 0.85)]
    for k, (txt, col, st) in enumerate(lines):
        al = fade(st, 0.4)
        yo = 24 * (1 - al)
        d.text((78, 270 + k * 78 + yo), txt, font=font(70, True), fill=col + (int(255 * al),), anchor='lm')
    al = fade(1.25)
    d.text((80, 510), 'Paste a link. Copy the text or download', font=font(26), fill=(105, 100, 92, int(255 * al)), anchor='lm')
    d.text((80, 546), 'TXT, DOCX, PDF, SRT, VTT. Free, no sign-up.', font=font(26), fill=(105, 100, 92, int(255 * al)), anchor='lm')
    # window slides up
    aw = fade(0.35, 0.8)
    x = 560
    y = 140 + 120 * (1 - aw)
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    lay.alpha_composite(WIN, (int(x), int(y)))
    lay.putalpha(lay.getchannel('A').point(lambda v: int(v * aw)))
    img.alpha_composite(lay)
    return img.convert('RGB')


scene(3.6, intro)

# 1. Share -> Copy link
base1, off1 = bv.pad_to_aspect(bv.share)
full1 = (0, 0, base1.width, base1.height)
btn1 = bv.shift(bv.SHARE_COPY, off1)
z1 = bv.view_for(btn1, base1.size, zoom_pad=1.5)
c1 = ((btn1[0] + btn1[2]) / 2, (btn1[1] + btn1[3]) / 2)


def s1(t, s):
    rect = lerp(full1, z1, ease((s - 0.3) / 1.1))
    fr = render(base1, rect)
    cpos, sc = to_out(c1, rect)
    bpos, _ = to_out(btn1[:2], rect)
    bend, _ = to_out(btn1[2:], rect)
    p = path((W * 0.25, H * 0.75), (cpos[0] + 10, cpos[1] + 6), (s - 0.6) / 0.9)
    click = (s - 1.6) / 0.5
    fr = outline(fr, (*bpos, *bend), ease((s - 1.5) / 0.3))
    fr = ring(fr, cpos, click, 1.2)
    fr = cursor(fr, p, press=1.0 if 0 <= click < 0.25 else 0.0)
    fr = badge(fr, (cpos[0], bend[1] + 70), '✓ Link copied', ease((s - 1.8) / 0.3))
    fr = band(fr, 1)
    return cap(fr, 1, 'On YouTube, click Share, then Copy link', ease(s / 0.3))


scene(2.8, s1)

# 2. Paste into YouTube Transcript (real recording) + click arrow
gfull = (0, 0, W, H)
gz = bv.view_for(bv.GIF_INPUT, (W, H), zoom_pad=0.06)
typing = []
for i in range(0, 29):
    d = 0.5 if i == 0 else (0.5 if i == 28 else bv.gif_durs[i] / 1000)
    typing += [i] * max(1, round(d * FPS))
n2 = len(typing)


def s2(t, s):
    i = typing[min(len(typing) - 1, int(t * (n2 - 1)))]
    rect = lerp(gfull, gz, ease(s / 0.8))
    fr = render(bv.gif_frames[i], rect)
    p, _ = to_out((bv.GIF_INPUT[0] + 60, bv.GIF_INPUT[1] + 60), rect)
    fr = outline(fr, (*to_out(bv.GIF_INPUT[:2], rect)[0], *to_out(bv.GIF_INPUT[2:], rect)[0]), ease((s - 0.2) / 0.3), pad=4)
    fr = cursor(fr, (p[0] + 20, p[1] + 30))
    fr = band(fr, 2)
    return cap(fr, 2, 'Paste the link into YouTube Transcript', ease(s / 0.3))


scene(n2 / FPS, s2)


def s2b(t, s):
    rect = lerp(gz, gfull, ease((s - 0.75) / 0.45))
    fr = render(bv.gif_frames[28], rect)
    a_out, sc = to_out(bv.GIF_ARROW, rect)
    start, _ = to_out((bv.GIF_INPUT[0] + 80, bv.GIF_INPUT[1] + 90), gz)
    p = path(start, (a_out[0] + 6, a_out[1] + 6), s / 0.5)
    click = (s - 0.5) / 0.45
    fr = ring(fr, a_out, click, sc)
    fr = cursor(fr, p, press=1.0 if 0 <= click < 0.25 else 0.0)
    fr = band(fr, 2)
    return cap(fr, 2, 'Click the arrow to start')


scene(1.25, s2b)

# 3. Transcribing (real frames) -> result
proc = []
for i in range(29, 40):
    proc += [i] * max(1, round(bv.gif_durs[i] / 1000 * FPS))


def s3(t, s):
    i = proc[min(len(proc) - 1, int(t * (len(proc) - 1)))]
    fr = render(bv.gif_frames[i], gfull)
    fr = badge(fr, (W - 210, 120), 'About 6 s for a 4-min video', ease((s - 0.4) / 0.3), color=DARK)
    fr = band(fr, 3)
    return cap(fr, 3, 'TranscriptX transcribes the audio', ease(s / 0.3))


scene(len(proc) / FPS, s3)

tz = bv.view_for((100, 160, 830, 450), (W, H), zoom_pad=0.06)


def s3b(t, s):
    rect = lerp(gfull, tz, ease((s - 0.5) / 1.3))
    fr = render(res, rect)
    fr = badge(fr, (W - 205, 262), '✓ Transcript ready', ease(s / 0.3))
    fr = band(fr, 3)
    return cap(fr, 3, 'Timestamped paragraphs, ready to use')


scene(2.6, s3b)

# 4. Copy = copies the text
tb = bv.view_for((560, 80, 840, 140), (W, H), zoom_pad=1.15)


def s4(t, s):
    rect = lerp(tz, tb, ease(s / 0.8))
    fr = render(res, rect)
    cpos, sc = to_out(GIF_COPY_C, rect)
    p = path((W * 0.35, H * 0.7), (cpos[0] + 8, cpos[1] + 6), (s - 0.6) / 0.7)
    click = (s - 1.35) / 0.5
    b0, _ = to_out((711, 92), rect)
    b1, _ = to_out((828, 128), rect)
    fr = outline(fr, (*b0, *b1), ease((s - 1.2) / 0.3), pad=6)
    fr = ring(fr, cpos, click, sc / 1.5)
    fr = cursor(fr, p, press=1.0 if 0 <= click < 0.25 else 0.0)
    fr = badge(fr, (cpos[0] - 40, b1[1] + 80), '✓ Whole transcript copied', ease((s - 1.5) / 0.3))
    fr = band(fr, 4)
    return cap(fr, 4, 'Click Copy to copy the whole transcript', ease(s / 0.3))


scene(2.9, s4)


# 5. Download = the button right next to Copy -> format menu
def paste_menu(fr, rect, a):
    if a <= 0:
        return fr
    (x0, y0), s = to_out(MENU_BOX[:2], rect)
    (x1, y1), _ = to_out(MENU_BOX[2:], rect)
    sc = 0.92 + 0.08 * a
    mw, mh = (x1 - x0) * sc, (y1 - y0) * sc
    m = menu_img.resize((int(mw), int(mh)), Image.LANCZOS)
    m.putalpha(m.getchannel('A').point(lambda v: int(v * a)))
    sh = Image.new('RGBA', fr.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x1 - mw, y0 + 6, x1, y0 + mh + 10), 14, fill=(0, 0, 0, int(55 * a)))
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    out = fr.convert('RGBA')
    out.alpha_composite(sh)
    out.alpha_composite(m, (int(x1 - mw), int(y0)))
    return out.convert('RGB')


tm = bv.view_for((540, 85, 860, 270), (W, H), zoom_pad=0.12)


def s5(t, s):
    rect = lerp(tb, tm, ease((s - 0.9) / 0.8))
    fr = render(res, rect)
    cpos, _ = to_out(GIF_COPY_C, tb)
    dpos, sc = to_out(GIF_DL, rect)
    p = path((cpos[0] + 8, cpos[1] + 6), (dpos[0] + 6, dpos[1] + 6), s / 0.7)
    click = (s - 0.75) / 0.45
    fr = ring(fr, dpos, click, sc / 1.5)
    fr = badge(fr, (to_out((681, 60), rect)[0][0], to_out((681, 60), rect)[0][1]), 'Download, next to Copy', ease((s - 0.2) / 0.3) * (1 - ease((s - 1.0) / 0.3)), color=DARK)
    fr = paste_menu(fr, rect, ease((s - 0.95) / 0.3))
    mpos = p
    if s > 1.9:
        (mx0, my0), _ = to_out(MENU_BOX[:2], rect)
        (mx1, my1), _ = to_out(MENU_BOX[2:], rect)
        rows = [0.12, 0.30, 0.48, 0.69, 0.87]
        k = min(4, int((s - 1.9) / 0.45))
        ty = my0 + (my1 - my0) * rows[k]
        mpos = (mx0 + (mx1 - mx0) * 0.55, ty)
    fr = cursor(fr, mpos, press=1.0 if 0 <= click < 0.25 else 0.0)
    fr = band(fr, 5)
    return cap(fr, 5, 'Click Download for TXT, DOCX, PDF, SRT or VTT', ease(s / 0.3))


scene(4.3, s5)

# Phone
pa, pb = bv.phone(bv.m_home, 600), bv.phone(bv.m_result, 600)


def sp(t, s):
    img = Image.new('RGBA', (W, H), BG + (255,))
    gap = 70
    x = (W - pa.width - pb.width - gap + 80) // 2
    for k, ph in enumerate((pa, pb)):
        a = ease((s - 0.15 * k) / 0.6)
        y = 30 + 140 * (1 - a)
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        lay.alpha_composite(ph, (int(x - 40 + k * (pa.width - 80 + gap)), int(y)))
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * a)))
        img.alpha_composite(lay)
    fr = img.convert('RGB')
    return cap(fr, None, 'Same steps on your phone', ease((s - 0.3) / 0.3))


scene(2.6, sp)


def outro(t, s):
    img = Image.new('RGBA', (W, H), BG + (255,))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((340, 120, 940, 720), fill=(236, 170, 130, 60))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(img)
    a = ease(s / 0.4)
    lg = bv.logo.resize((80, 80), Image.LANCZOS)
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    lay.alpha_composite(lg, (W // 2 - 40, 190))
    lay.putalpha(lay.getchannel('A').point(lambda v: int(v * a)))
    img.alpha_composite(lay)
    d.text((W // 2, 330), 'Get the transcript of any YouTube video', font=font(50, True), fill=DARK + (int(255 * a),), anchor='mm')
    a2 = ease((s - 0.3) / 0.4)
    d.text((W // 2, 392), 'Free. No account needed.', font=font(30), fill=(105, 100, 92, int(255 * a2)), anchor='mm')
    a3 = ease((s - 0.6) / 0.4)
    pulse = 1 + 0.03 * max(0, __import__('math').sin((s - 1.0) * 5)) if s > 1.0 else 1
    bw, bh = 560 * pulse, 70 * pulse
    d.rounded_rectangle((W / 2 - bw / 2, 470 - bh / 2, W / 2 + bw / 2, 470 + bh / 2), bh / 2, fill=ACCENT + (int(255 * a3),))
    d.text((W // 2, 470), 'transcriptx.ai/youtube-transcript', font=font(30, True), fill=(255, 255, 255, int(255 * a3)), anchor='mm')
    return img.convert('RGB')


scene(3.0, outro)


# ---------- assemble with crossfades ----------
XF = round(0.3 * FPS)
frames = list(scenes[0])
for sc in scenes[1:]:
    for k in range(XF):
        a = (k + 1) / (XF + 1)
        frames[-XF + k] = Image.blend(frames[-XF + k], sc[k], a)
    frames += sc[XF:]

mp4 = f'{OUT}/video/how-to-get-youtube-transcript-transcriptx.mp4'
import imageio_ffmpeg
w = imageio_ffmpeg.write_frames(mp4, (W, H), fps=FPS, codec='libx264', quality=7, macro_block_size=16,
                                output_params=['-movflags', '+faststart'])
w.send(None)
for f in frames:
    w.send(f.tobytes())
w.close()
print('mp4', round(len(frames) / FPS, 1), 's', os.path.getsize(mp4) // 1024, 'KB')

frames[round(2.6 * FPS)].save(f'{OUT}/video/how-to-get-youtube-transcript-transcriptx-poster.webp', 'WEBP', quality=86)
small = [f.resize((960, 600), Image.LANCZOS) for f in frames[::3]]
aw = f'{OUT}/how-to-get-youtube-transcript-transcriptx.webp'
small[0].save(aw, 'WEBP', save_all=True, append_images=small[1:], duration=100, loop=0, quality=62, method=4)
print('webp', os.path.getsize(aw) // 1024, 'KB')

# contact sheet for review
sheet = Image.new('RGB', (640 * 4, 400 * 4), 'white')
idx = [int(len(frames) * k / 16) + 5 for k in range(16)]
for k, i in enumerate(idx):
    sheet.paste(frames[min(i, len(frames) - 1)].resize((640, 400)), ((k % 4) * 640, (k // 4) * 400))
sheet.save('/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/6f038fa0-0daa-4715-9ce4-3db7161bd7dc/scratchpad/v2_sheet.png')
