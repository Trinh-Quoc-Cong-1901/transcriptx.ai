"""YouTube-quality walkthrough (2560x1440, 60 fps, sharpness-guarded) for how-to-download-youtube-subtitles.

One sample video (Shayne Ward - Until You) from start to end:
hook -> 1 Share/Copy link -> 2 paste into YouTube Subtitle Downloader, click arrow -> 3 transcribing (real recording,
frame-interpolated) -> result -> 4 Download (button next to Copy) -> 5 pick .vtt -> the .vtt file -> phone -> CTA.
"""
import importlib.util, math
from PIL import Image, ImageDraw

import video_hq as vk
from video_hq import W, H, U, SW, SH, BG, DARK, ACCENT, GREY, ease, lerp

bv = vk.bv
spec = importlib.util.spec_from_file_location('subs', f'{vk.HERE}/build_visuals_youtube_subtitles.py')
subs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subs)

OUT = subs.OUT
BASE = 'how-to-download-youtube-subtitles-transcriptx'
vk.STEPS[:] = ['Copy link', 'Paste', 'Transcribe', 'Download', 'SRT / VTT']
SHEET = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/6f038fa0-0daa-4715-9ce4-3db7161bd7dc/scratchpad/subs_hq_sheet.png'

# ---------- sources ----------
gif_pad = [vk.pad16x9(f, color=(250, 249, 245)) for f in bv.gif_frames]   # 1280x800 -> 16:9
GIF = [p[0] for p in gif_pad]
GOFF = gif_pad[0][1]


def g(pt):                     # GIF coords -> padded coords
    return bv.shift(pt, GOFF)


RES = GIF[40]
GIF_DL = g((681, 110))
GIF_COPY = g((711, 92, 828, 128))
MENU_BOX = g((561, 129, 695, 262))
ROWS = [0.114, 0.30, 0.47, 0.69, 0.87]

_raw = Image.open(f'{bv.SRC}/transcript/download-format-menu.png').convert('RGBA').crop((0, 0, 401, 397))
MENU = Image.new('RGBA', _raw.size, (250, 249, 245, 255))
MENU.alpha_composite(_raw)
_m = Image.new('L', MENU.size, 0)
ImageDraw.Draw(_m).rounded_rectangle((0, 0, MENU.width - 1, MENU.height - 1), 22, fill=255)
MENU.putalpha(_m)

VTT = subs.vtt
VTT_HL = bv.highlight(VTT, (6, 64, 394, 92), pad=6, width=5)

# ---------- intro ----------
WIN_INTRO, WG = vk.window(VTT.crop((0, 0, 1060, 980)), int(600 * U * 0.82))
LOGO = bv.logo.resize((int(52 * U), int(52 * U)), Image.LANCZOS)
LOGO.putalpha(LOGO.convert('L').point(lambda v: 0 if v > 235 else 255))


def intro(t, s):
    img = vk.glow_bg().copy()
    fade = lambda st, d=0.45: ease((s - st) / d)
    x0 = int(120 * U)
    vk.paste_fade(img, LOGO, (x0, int(150 * U)), fade(0))
    vk.text(img, (x0 + 66 * U, 176 * U), 'TranscriptX', 34 * U, DARK, fade(0))
    for k, (txt, col, st) in enumerate([('YouTube subtitles', DARK, 0.25), ('as SRT or VTT', ACCENT, 0.5), ('in seconds.', DARK, 0.75)]):
        a = fade(st, 0.45)
        vk.text(img, (x0 - 4, 300 * U + k * 82 * U + 26 * U * (1 - a)), txt, 64 * U, col, a)
    a = fade(1.15)
    vk.text(img, (x0, 590 * U), 'Paste a YouTube link, download the subtitle file.', 29 * U, GREY, a, bold=False)
    vk.text(img, (x0, 632 * U), 'Works even without captions. Free, no sign-up.', 29 * U, GREY, a, bold=False)
    aw = fade(0.3, 0.9)
    drift = 10 * U * s
    vk.paste_fade(img, WIN_INTRO, (W - WIN_INTRO.width - 40 * U, 90 * U + 140 * U * (1 - aw) - drift), aw)
    return img


vk.scene(3.8, intro)

# ---------- 1. YouTube Share -> Copy link ----------
base1, off1 = vk.pad16x9(bv.share)
btn1 = bv.shift(bv.SHARE_COPY, off1)
f1 = vk.full(base1)
z1 = vk.view(btn1, base1.size, pad=1.4, max_up=1.8)          # 1x source
c1 = ((btn1[0] + btn1[2]) / 2, (btn1[1] + btn1[3]) / 2)


def s1(t, s):
    rect = lerp(f1, z1, ease((s - 0.25) / 1.2))
    sc = vk.render(base1, rect)
    cpos, _ = vk.to_s(c1, rect)
    b = vk.box_s(btn1, rect)
    click = (s - 1.75) / 0.5
    vk.outline(sc, b, ease((s - 1.6) / 0.3))
    vk.ring(sc, cpos, click, 1.3)
    vk.cursor(sc, vk.path((SW * 0.22, SH * 0.78), (cpos[0] + 12, cpos[1] + 8), (s - 0.6) / 1.0), vk.press(click))
    vk.badge(sc, (cpos[0], b[3] + 80 * U), '✓ Link copied', ease((s - 1.95) / 0.3))
    out = vk.frame(sc, 1)
    return vk.caption(out, 1, 'On YouTube, click Share, then Copy link', ease(s / 0.35))


vk.scene(3.0, s1)

# ---------- 2. Paste into YouTube Subtitle Downloader ----------
base2, off2 = vk.pad16x9(subs.sub_tool)
inp = bv.shift(subs.SUB_INPUT, off2)
f2 = vk.full(base2)
z2 = vk.view(inp, base2.size, pad=0.14, max_up=1.3)          # retina source
arrow = bv.shift((1651, 538), off2)
LINK = 'https://youtu.be/YfDqONbzYPc'
IN_BG = subs.sub_tool.getpixel((900, 470))
F_IN = vk.font(30, False)


def typed(n, caret):
    img = base2.copy()
    d = ImageDraw.Draw(img)
    x, y = inp[0] + 28, inp[1] + 44
    d.rectangle((x - 4, y - 22, x + 760, y + 22), fill=IN_BG)
    txt = LINK[:n]
    d.text((x, y), txt, font=F_IN, fill=(40, 39, 36), anchor='lm')
    if caret:
        cx = x + d.textlength(txt, font=F_IN) + 3
        d.line((cx, y - 18, cx, y + 18), fill=(40, 39, 36), width=2)
    return img


def s2(t, s):
    rect = lerp(f2, z2, ease(s / 1.0))
    n = int(len(LINK) * ease((s - 1.0) / 0.55)) if s > 1.0 else 0
    caret = (int(s * 2.5) % 2 == 0) or 0 < n < len(LINK)
    sc = vk.render(typed(n, caret) if s > 0.6 else base2, rect)
    vk.outline(sc, vk.box_s(inp, rect), ease((s - 0.3) / 0.3), pad=4)
    hold, _ = vk.to_s((inp[0] + 230, inp[1] + 150), rect)
    vk.cursor(sc, hold)
    if 0.95 < s < 1.75:
        vk.badge(sc, (SW / 2, SH * 0.74), 'Paste  ·  Cmd+V / Ctrl+V', ease((s - 0.95) / 0.2) * (1 - ease((s - 1.55) / 0.2)), color=DARK)
    return vk.caption(vk.frame(sc, 2), 2, 'Paste it into YouTube Subtitle Downloader', ease(s / 0.35))


vk.scene(2.2, s2)


def s2b(t, s):
    rect = lerp(z2, f2, ease((s - 0.85) / 0.5))
    sc = vk.render(typed(len(LINK), False), rect)
    a_out, k = vk.to_s(arrow, rect)
    start, _ = vk.to_s((inp[0] + 230, inp[1] + 150), z2)
    click = (s - 0.6) / 0.45
    vk.ring(sc, a_out, click, k * 1.6)
    vk.cursor(sc, vk.path(start, (a_out[0] + 6, a_out[1] + 6), s / 0.6), vk.press(click))
    return vk.caption(vk.frame(sc, 2), 2, 'Click the arrow to start')


vk.scene(1.45, s2b)

# ---------- 3. Transcribing (real recording, interpolated) -> result ----------
TL, T_PROC = vk.gif_timeline(list(range(29, 40)), bv.gif_durs, stretch=1.15)
fg = vk.full(GIF[0])
pz = vk.view(g((90, 130, 850, 480)), GIF[0].size, pad=0.04, max_up=1.85)   # 1x recording


def s3(t, s):
    rect = lerp(fg, pz, 0.45 * ease(s / T_PROC))
    sc = vk.render(vk.gif_at(GIF, TL, s), rect)
    vk.badge(sc, (SW - 230 * U, 150 * U), 'About 6 s for a 4-min video', ease((s - 0.4) / 0.3), color=DARK)
    return vk.caption(vk.frame(sc, 3), 3, 'TranscriptX listens to the audio', ease(s / 0.35))


vk.scene(T_PROC, s3)
tz = vk.view(g((100, 160, 830, 450)), GIF[0].size, pad=0.06, max_up=1.85)
p_end = lerp(fg, pz, 0.45)


def s3b(t, s):
    rect = lerp(p_end, tz, ease((s - 0.2) / 1.4))
    sc = vk.render(RES, rect)
    vk.badge(sc, (SW - 220 * U, 300 * U), '✓ Transcript ready', ease(s / 0.3))
    return vk.caption(vk.frame(sc, 3), 3, 'Timed lines, built from the audio')


vk.scene(2.4, s3b)

# ---------- 4. Download (next to Copy) ----------
tb = vk.view(g((560, 80, 840, 140)), GIF[0].size, pad=1.1, max_up=1.85)


def menu(sc, rect, a, hover=None, pick=None):
    if a <= 0:
        return sc
    x0, y0, x1, y1 = vk.box_s(MENU_BOX, rect)
    k = 0.93 + 0.07 * a
    mw, mh = int((x1 - x0) * k), int((y1 - y0) * k)
    m = MENU.resize((mw, mh), Image.LANCZOS)
    hl = Image.new('RGBA', m.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(hl)
    for idx, al in ((hover, 34), (pick, 60)):
        if idx is not None:
            cy = mh * ROWS[idx]
            d.rounded_rectangle((8, cy - mh * 0.075, mw - 8, cy + mh * 0.075), 8, fill=(204, 88, 46, al))
    m.alpha_composite(hl)
    m.putalpha(_m.resize((mw, mh)))
    sd = ImageDraw.Draw(sc, 'RGBA')
    sd.rounded_rectangle((x1 - mw + 4, y0 + 10, x1 + 4, y0 + mh + 14), 16, fill=(0, 0, 0, int(28 * a)))
    return vk.paste_fade(sc, m, (x1 - mw, y0), a)


def s4(t, s):
    rect = lerp(tz, tb, ease(s / 0.9))
    sc = vk.render(RES, rect)
    dpos, k = vk.to_s(GIF_DL, rect)
    cb = vk.box_s(GIF_COPY, rect)
    r = 17 * k
    vk.outline(sc, (dpos[0] - r, dpos[1] - r, dpos[0] + r, dpos[1] + r), ease((s - 0.95) / 0.3), pad=5)
    lbl = ease((s - 1.0) / 0.3) * (1 - ease((s - 2.1) / 0.25))
    vk.badge(sc, ((dpos[0] + cb[2]) / 2, dpos[1] - 80 * U), 'Download is next to Copy', lbl, color=DARK)
    click = (s - 1.85) / 0.45
    vk.ring(sc, dpos, click, k / 1.7)
    menu(sc, rect, ease((s - 2.05) / 0.3))
    vk.cursor(sc, vk.path((SW * 0.35, SH * 0.74), (dpos[0] + 6, dpos[1] + 6), (s - 0.7) / 1.0), vk.press(click))
    return vk.caption(vk.frame(sc, 4), 4, 'Click Download, next to Copy', ease(s / 0.35))


vk.scene(3.0, s4)

# ---------- 5. Pick .srt or .vtt (crisp magnified menu cut from the retina capture) ----------
CW = int(MENU.width * 1.15)                 # never more than ~1.2x the retina source
CH = round(MENU.height * CW / MENU.width)
MENU_FLAT = Image.new('RGB', MENU.size, (250, 249, 245))
MENU_FLAT.paste(MENU, (0, 0), MENU)


def s5(t, s):
    rect = tb
    sc = vk.render(RES, rect)
    x0, y0, x1, y1 = vk.box_s(MENU_BOX, rect)
    menu(sc, rect, 1.0)
    a = ease(s / 0.45)
    cx, cy = x1 + 70 * U, max(40 * U, y0 - 60 * U)
    d = ImageDraw.Draw(sc, 'RGBA')
    d.line((x1 + 4, (y0 + y1) / 2, cx, cy + CH / 2), fill=ACCENT + (int(160 * a),), width=max(2, int(2 * U)))
    vk.callout(sc, MENU_FLAT, (0, 0, MENU.width, MENU.height), (cx, cy), CW, a)
    if a >= 1:
        hover = 3 if s < 1.5 else 4
        pick = 4 if s > 1.85 else None
        for idx, al in ((hover, 36), (pick, 64)):
            if idx is not None:
                ry = cy + CH * ROWS[idx]
                d.rounded_rectangle((cx + 10, ry - CH * 0.072, cx + CW - 10, ry + CH * 0.072), int(10 * U), fill=(204, 88, 46, al))
        vk.outline(sc, (cx + 8, cy + CH * 0.6, cx + CW - 8, cy + CH * 0.97), ease((s - 0.6) / 0.3), pad=4)
        tgt = (cx + CW * 0.42, cy + CH * ROWS[hover])
        click = (s - 1.8) / 0.45
        vk.ring(sc, tgt, click, 1.2)
        start, _ = vk.to_s(GIF_DL, rect)
        pos = vk.path(start, tgt, (s - 0.45) / 0.8, arc=30) if s < 1.25 else \
            (tgt if s > 1.5 else lerp(tgt, tgt, 1))
        if 1.25 <= s <= 1.5:
            pos = lerp((cx + CW * 0.42, cy + CH * ROWS[3]), (cx + CW * 0.42, cy + CH * ROWS[4]), ease((s - 1.25) / 0.25))
        vk.cursor(sc, pos, vk.press(click))
        vk.badge(sc, (cx + CW / 2, cy + CH + 70 * U), '✓ .vtt file saved', ease((s - 2.05) / 0.3))
    return vk.caption(vk.frame(sc, 5), 5, 'Pick .srt or .vtt to save the subtitles', ease(s / 0.35))


vk.scene(3.2, s5)

# ---------- the .vtt file ----------
VTT_W = 1060                                    # retina file crop shown at native width (no upscaling)


def s6(t, s):
    img = vk.glow_bg((0.15, 0.05, 0.85, 0.95), 50).copy()
    top = 620 * ease((s - 1.4) / 2.4)
    src = VTT_HL if s < 1.4 else VTT
    crop = src.crop((0, int(top), 1060, int(top) + 760))
    win, gp = vk.window(crop, VTT_W)
    a = ease(s / 0.5)
    vk.paste_fade(img, win, ((W - win.width) / 2, 92 * U - gp + 60 * U * (1 - a)), a)
    vk.badge(img, (W / 2 + 380 * U, 205 * U), 'Start --> end time + text', ease((s - 0.45) / 0.3) * (1 - ease((s - 1.3) / 0.3)), color=DARK)
    vk.progress_only(img, 5)
    return vk.caption(img, 5, 'Timed subtitles, ready for any player', ease((s - 0.2) / 0.35))


vk.scene(3.8, s6)

# ---------- phone ----------
DUO = subs.phone_duo_download()
DUO = DUO.resize((round(DUO.width * min(1000, H * 0.8) / DUO.height), int(min(1000, H * 0.8))), Image.LANCZOS)


def sp(t, s):
    img = Image.new('RGB', (W, H), BG)
    a = ease(s / 0.6)
    img.paste(DUO, ((W - DUO.width) // 2, int(18 * U + 90 * (1 - a))))
    if a < 1:
        img = Image.blend(Image.new('RGB', (W, H), BG), img, a)
    return vk.caption(img, None, 'Same steps on your phone: Download is in the bottom bar', ease((s - 0.3) / 0.35))


vk.scene(2.9, sp)

# ---------- CTA ----------
LOGO_BIG = bv.logo.resize((int(84 * U), int(84 * U)), Image.LANCZOS)
LOGO_BIG.putalpha(LOGO_BIG.convert('L').point(lambda v: 0 if v > 235 else 255))


def outro(t, s):
    img = vk.glow_bg((0.27, 0.15, 0.73, 0.9), 60).copy()
    a = ease(s / 0.4)
    vk.paste_fade(img, LOGO_BIG, (W / 2 - LOGO_BIG.width / 2, 200 * U), a)
    vk.text(img, (W / 2, 350 * U), 'Download subtitles from any YouTube video', 52 * U, DARK, a, anchor='mm')
    vk.text(img, (W / 2, 418 * U), 'SRT or VTT. Free. No account needed.', 32 * U, GREY, ease((s - 0.3) / 0.4), bold=False, anchor='mm')
    a3 = ease((s - 0.6) / 0.4)
    p = 1 + 0.025 * max(0.0, math.sin((s - 1.0) * 5)) if s > 1.0 else 1
    bw, bh = 700 * U * p, 76 * U * p
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle((W / 2 - bw / 2, 505 * U - bh / 2, W / 2 + bw / 2, 505 * U + bh / 2), int(bh / 2), fill=ACCENT + (int(255 * a3),))
    vk.text(img, (W / 2, 505 * U), 'transcriptx.ai/youtube-subtitle-downloader', 30 * U, (255, 255, 255), a3, anchor='mm')
    return img


vk.scene(3.4, outro)

if __name__ == '__main__':
    vk.export(OUT, BASE, poster_at=3.2, preview_sheet=SHEET)
