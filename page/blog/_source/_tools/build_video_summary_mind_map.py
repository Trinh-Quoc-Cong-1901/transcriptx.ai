"""Preview video (2560x1440, 60 fps) of the coming-soon Notes / Summary / Mind map panel, for how-to-summarize-a-youtube-video.

The app screen is the real 2026-10-29 capture (transcript/transcript-notes-tab.png, retina 2000x1273). The transcript column
and the right panel are re-drawn on top of it so they can scroll, highlight and fill in:
hook -> 1 type notes -> 2 Summary with timestamps -> 3 click a timestamp, transcript jumps there -> 4 Mind map grows -> CTA.
Summary and Mind map are not live yet, so the hook, a badge and the CTA all say "Coming soon".
Voice-over: edge-tts en-US-AvaNeural (+4%), one line per scene, over a soft ducked music bed (gen_soft_music.py).
"""
import math, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont

import video_hq as vk
from video_hq import W, H, U, SW, SH, BG, DARK, ACCENT, GREY, ease, lerp

bv = vk.bv
SRC = bv.SRC
OUT = os.path.abspath(f'{vk.HERE}/../../how-to-summarize-a-youtube-video/images')
BASE = 'transcriptx-summary-mind-map-preview'
SHEET = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/ea9bc2ca-d557-4155-bd4f-5b5af8927b38/scratchpad/summary_sheet.png'
vk.STEPS[:] = ['Notes', 'Summary', 'Jump to text', 'Mind map']

# ---------- voice-over (one line per scene; scenes stretch to fit their line) ----------
VOICE, RATE = 'en-US-AvaNeural', '+4%'             # same voice as speak-live-promo.mp4 (Microsoft neural, via edge-tts)
EDGE_TTS = os.environ.get('EDGE_TTS', 'edge-tts')   # path to the edge-tts CLI (pip install edge-tts)
VO_LINES = [                                      # (start offset in the scene, text)
    (0.3, 'Coming soon to TranscriptX: Notes, Summary and Mind map, right next to your transcript.'),
    (0.35, 'First, type your own notes beside the transcript.'),
    (0.5, 'Open Summary to get the key points, each with its timestamp.'),
    (0.55, 'Click a timestamp, and the transcript jumps straight to that moment.'),
    (0.5, 'Mind map shows the whole video at a glance.'),
    (0.3, 'Summary and Mind map are coming soon. Pro users get the beta first.'),
]


def _make_vo():
    import subprocess, tempfile, imageio_ffmpeg
    d = tempfile.mkdtemp(prefix='vo_')
    out = []
    for k, (_, line) in enumerate(VO_LINES):
        f = f'{d}/l{k}.mp3'
        subprocess.run([EDGE_TTS, '--voice', VOICE, f'--rate={RATE}', '--text', line, '--write-media', f],
                       check=True, capture_output=True)
        err = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-i', f], capture_output=True, text=True).stderr
        h, m_, sec = err.split('Duration: ')[1].split(',')[0].split(':')
        out.append((f, int(h) * 3600 + int(m_) * 60 + float(sec)))
    return out


VO = _make_vo() if not os.environ.get('SKIP_VO') else [(None, 0.0)] * len(VO_LINES)   # SKIP_VO=1: stills/images only


def dur(i, base):
    return max(base, VO_LINES[i][0] + VO[i][1] + 0.7)


# ---------- sources ----------
SHOT = {k: Image.open(f'{SRC}/transcript/transcript-{k}.png').convert('RGB')
        for k in ('notes-tab', 'summary-coming-soon', 'mind-map-coming-soon')}
TABS = {'notes': 'notes-tab', 'summary': 'summary-coming-soon', 'mindmap': 'mind-map-coming-soon'}
APP = SHOT['notes-tab']
TAB_BOX = (1446, 360, 1998, 436)                 # tab strip incl. underline
TAB_X = {'notes': 1520, 'summary': 1648, 'mindmap': 1800}
TAB_Y = 393
PANEL = (1446, 437, 1998, 1270)
PANEL_BG = (246, 245, 240)
TR = (440, 250, 1430, 1158)                      # transcript column
TR_BG = (250, 249, 245)
TX0, TXW = 495, 891
INK = (38, 37, 33)
TS_INK = (128, 124, 116)
NOTE_PH = (1480, 515, 1990, 560)                 # "Add a note..." placeholder

SF = '/System/Library/Fonts/SFNS.ttf'
MONO = '/System/Library/Fonts/SFNSMono.ttf'


@lru_cache(maxsize=32)
def F(size, bold=False, mono=False):
    f = ImageFont.truetype(MONO if mono else SF, size)
    if bold and not mono:
        try:
            f.set_variation_by_name('Semibold')
        except Exception:
            pass
    return f


def wrap(s, f, width):
    lines, cur = [], ''
    for w in s.split():
        t = (cur + ' ' + w).strip()
        if F_len(t, f) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur]


def F_len(s, f):
    return f.getlength(s)


# ---------- transcript ----------
PARAS = [
    ('00:00.33', 0.0, 'When I was 16, my father said, "You can do anything you want with your life. You just have to be willing to work hard to get it." That\'s when I decided: when I die, I want to be remembered for the life I lived, not the money I made.'),
    ('00:13.65', 13.65, 'Once upon a younger year, when all our shadows disappeared, the animals inside came out to play. We went face to face with all our fears, learned our lessons through the tears, made memories we knew would never fade. One day my father, he told me, "Son, don\'t let it slip away." He took me in his arms, I heard him say, "When you get older, your wild heart will live for younger days.'),
    ('00:40.11', 40.11, 'Think of me if ever you\'re afraid." He said, "One day you\'ll leave this world behind, so live a life you will remember." My father told me when I was just a child, "These are the nights to never die." My father told me— When the sun declines, start pouring down, light a fire they can\'t put out, carve your name into those shining stars.'),
    ('01:36.51', 96.51, 'He said, "Go venture far beyond the shores, don\'t forsake this life of yours. I\'ll guide you home no matter where you are." One day my father, he told me, "Son, don\'t let it slip away." When I was just a kid, I heard him say, "When you get older, your wild heart will live for younger days. Think of me if ever you\'re afraid."'),
    ('01:59.42', 119.42, 'He said, "One day you\'ll leave this world behind, so live a life you will remember." My father told me when I was just a child, "These are the nights to never die." My father told me— "These are the nights to never die." My father told me— My father told me—'),
]
LH, TS_GAP, PARA_GAP = 47.7, 49, 67
LAYOUT = []                                      # (ts_y, [line ys], lines)
_y = 306
for ts, _, txt in PARAS:
    lines = wrap(txt, F(30), TXW)
    ys = [_y + TS_GAP + k * LH for k in range(len(lines))]
    LAYOUT.append((_y, ys, lines))
    _y = ys[-1] + PARA_GAP
CONTENT_H = _y - 306


def scroll_to(i, top=330):
    return LAYOUT[i][0] - top


def draw_transcript(img, scroll=0.0, hl=None, hl_a=0.0):
    x0, y0, x1, y1 = TR
    layer = Image.new('RGB', (x1 - x0, y1 - y0), TR_BG)
    d = ImageDraw.Draw(layer, 'RGBA')
    for i, (ts_y, ys, lines) in enumerate(LAYOUT):
        top = ts_y - scroll - y0
        if top > y1 - y0 or ys[-1] - scroll - y0 < -60:
            continue
        if hl == i and hl_a > 0:
            bx0, by0, bx1, by1 = TX0 - 22 - x0, top - 26, TX0 + TXW + 22 - x0, ys[-1] - scroll - y0 + 26
            d.rounded_rectangle((bx0, by0, bx1, by1), 16, fill=ACCENT + (int(30 * hl_a),))
            d.rounded_rectangle((bx0, by0 + 6, bx0 + 6, by1 - 6), 3, fill=ACCENT + (int(255 * hl_a),))
        d.text((TX0 - x0, top), PARAS[i][0], font=F(21, mono=True), fill=TS_INK, anchor='lm')
        for ly, s in zip(ys, lines):
            if ly - scroll > y1 - 34:
                break
            d.text((TX0 - x0, ly - scroll - y0), s, font=F(30), fill=INK, anchor='lm')
    # top and bottom fades like the app
    for k in range(70):
        a = int(255 * (k / 70) ** 1.6)
        d.line((0, y1 - y0 - 70 + k, x1 - x0, y1 - y0 - 70 + k), fill=TR_BG + (a,))
    for k in range(40):
        d.line((0, k, x1 - x0, k), fill=TR_BG + (int(255 * (1 - k / 40) ** 1.4),))
    img.paste(layer, (x0, y0))
    ImageDraw.Draw(img).rectangle((x0, y1, x1, 1160), fill=TR_BG)     # clipped glyphs left in the capture
    # scrollbar thumb
    dd = ImageDraw.Draw(img)
    dd.rectangle((1430, 250, 1442, 1158), fill=TR_BG)
    view = y1 - y0
    th = view * view / (CONTENT_H + 200)
    ty = 268 + (view - th - 30) * min(1, scroll / max(1, CONTENT_H + 200 - view))
    dd.rounded_rectangle((1433, ty, 1440, ty + th), 4, fill=(220, 217, 208))


PLAYER_T = (494, 1214)
PLAYER_PATCH = APP.crop((680, 1190, 746, 1238))          # empty strip of the same player bar


def draw_time(img, sec):
    img.paste(PLAYER_PATCH, (486, 1190))
    d = ImageDraw.Draw(img)
    d.text(PLAYER_T, f'{int(sec // 60)}:{int(sec % 60):02d}', font=F(27), fill=(52, 50, 45), anchor='lm')


# ---------- right panel ----------
def panel_clear(img, top=PANEL[1]):
    ImageDraw.Draw(img).rectangle((PANEL[0] + 2, top, PANEL[2], PANEL[3]), fill=PANEL_BG)


def set_tab(img, tab):
    img.paste(SHOT[TABS[tab]].crop(TAB_BOX), TAB_BOX[:2])


NOTE_LINES = [
    ('text', 'Dad at 16: work hard for what you want.'),
    ('text', 'Be remembered for the life, not the money.'),
    ('check', 'Rewatch the chorus at 00:40'),
]
NOTE_CHARS = sum(len(s) for _, s in NOTE_LINES)


def draw_notes(img, n_chars, caret):
    d = ImageDraw.Draw(img)
    d.rectangle(NOTE_PH, fill=PANEL_BG)
    if n_chars <= 0 and not caret:
        d.text((1487, 538), 'Add a note...', font=F(27), fill=(150, 146, 138), anchor='lm')
        return
    y, left, cx, cy = 538, n_chars, 1487, 538
    for kind, s in NOTE_LINES:
        if left <= 0:
            break
        part = s[:left]
        left -= len(s)
        x = 1487
        if kind == 'check':
            d.rounded_rectangle((x, y - 13, x + 26, y + 13), 5, outline=(120, 116, 108), width=2)
            x += 40
        for k, ln in enumerate(wrap(part, F(26), 1975 - x)):
            d.text((x, y), ln, font=F(26), fill=INK, anchor='lm')
            cx, cy = x + F(26).getlength(ln) + 3, y
            y += 40
        y += 14
    if caret:
        d.line((cx, cy - 16, cx, cy + 16), fill=INK, width=2)


SUMMARY_OVERVIEW = "A son remembers his father's advice: work hard, face your fears and live a life worth remembering."
KEY_POINTS = [
    ('00:00', 0.0, 'At 16, his father tells him he can do anything if he works hard for it.'),
    ('00:13', 13.65, 'Childhood memories: facing fears and learning through tears.'),
    ('00:40', 40.11, '"Live a life you will remember." These are the nights to never die.'),
    ('01:36', 96.51, 'His father promises to guide him home, wherever he goes.'),
]
CHIP_W, CHIP_H = 92, 38


def summary_layout():
    y = 492
    rows = {'overview': []}
    rows['h1'] = y
    y += 46
    for ln in wrap(SUMMARY_OVERVIEW, F(25), 490):
        rows['overview'].append(y)
        y += 38
    y += 30
    rows['h2'] = y
    y += 52
    rows['points'] = []
    for ts, _, txt in KEY_POINTS:
        lines = wrap(txt, F(25), 1975 - 1487 - CHIP_W - 16)
        rows['points'].append((y, lines))
        y += len(lines) * 37 + 26
    return rows


SUM = summary_layout()


def chip_box(i):
    y = SUM['points'][i][0]
    return (1487, y - CHIP_H / 2, 1487 + CHIP_W, y + CHIP_H / 2)


def draw_summary(img, reveal, active=None, hover=None):
    """reveal: 0..1 progress of the panel filling in (shimmer first, then rows)."""
    panel_clear(img)
    d = ImageDraw.Draw(img, 'RGBA')
    if reveal < 0.22:                                         # generating shimmer
        ph = (reveal / 0.22 * 3) % 1
        for k, w in enumerate((470, 420, 490, 300, 450, 380)):
            y = 500 + k * 54
            d.rounded_rectangle((1487, y, 1487 + w, y + 22), 11, fill=(232, 229, 221))
            sx = 1487 + (w + 200) * ph - 100
            lo, hi = max(1487, sx - 60), min(1487 + w, sx + 60)
            if hi - lo > 22:
                d.rounded_rectangle((lo, y, hi, y + 22), 11, fill=(242, 240, 234))
        d.text((1487, 500 + 6 * 54 + 14), 'Summarizing…', font=F(23), fill=(150, 146, 138), anchor='lm')
        return
    r = (reveal - 0.22) / 0.78
    steps = 2 + len(KEY_POINTS)

    def a_of(k):
        return ease(r * steps - k)

    a = a_of(0)
    d.text((1487, SUM['h1']), 'Overview', font=F(25, True), fill=INK + (int(255 * a),), anchor='lm')
    for y, ln in zip(SUM['overview'], wrap(SUMMARY_OVERVIEW, F(25), 490)):
        d.text((1487, y + 8 * (1 - a)), ln, font=F(25), fill=(70, 67, 61, int(255 * a)), anchor='lm')
    a = a_of(1)
    d.text((1487, SUM['h2']), 'Key points', font=F(25, True), fill=INK + (int(255 * a),), anchor='lm')
    for i, (ts, _, _) in enumerate(KEY_POINTS):
        a = a_of(2 + i)
        if a <= 0:
            continue
        y, lines = SUM['points'][i]
        dy = 10 * (1 - a)
        on = active == i
        x0, y0, x1, y1 = chip_box(i)
        fill = ACCENT + (int(255 * a),) if on else (ACCENT[0], ACCENT[1], ACCENT[2], int((40 if hover == i else 26) * a))
        d.rounded_rectangle((x0, y0 + dy, x1, y1 + dy), 19, fill=fill)
        d.text(((x0 + x1) / 2, y + dy), ts, font=F(21, mono=True), fill=((255, 255, 255) if on else ACCENT) + (int(255 * a),), anchor='mm')
        for k, ln in enumerate(lines):
            d.text((1487 + CHIP_W + 16, y + k * 37 + dy), ln, font=F(25), fill=INK + (int(255 * a),), anchor='lm')


# mind map: root on the left, 4 branches on the right
MM_ROOT = (1470, 736, 1622, 916)
MM_NODES = [
    ('Work hard', '00:00', 'You can do anything you want'),
    ('Face your fears', '00:13', 'Lessons learned through tears'),
    ('Nights to never die', '00:40', "Light a fire they can't put out"),
    ('Go venture far', '01:36', "He'll guide you home"),
]
MM_X0, MM_X1 = 1672, 1984
MM_YS = [478, 656, 834, 1012]
MM_H = 150


def bezier(p0, p3, t):
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.55, p0[1])
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.45, p3[1])
    pts = []
    for k in range(int(40 * t) + 1):
        u = k / 40
        pts.append(tuple((1 - u) ** 3 * a + 3 * (1 - u) ** 2 * u * b + 3 * (1 - u) * u * u * c + u ** 3 * e
                         for a, b, c, e in zip(p0, p1, p2, p3)))
    return pts


def draw_mindmap(img, grow):
    panel_clear(img)
    d = ImageDraw.Draw(img, 'RGBA')
    a = ease(grow / 0.2)
    x0, y0, x1, y1 = MM_ROOT
    k = 0.9 + 0.1 * a
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    hw, hh = (x1 - x0) / 2 * k, (y1 - y0) / 2 * k
    d.rounded_rectangle((cx - hw, cy - hh, cx + hw, cy + hh), 22, fill=DARK + (int(255 * a),))
    for j, ln in enumerate(['Live a life', 'you will', 'remember']):
        d.text((cx, cy - 38 + j * 38), ln, font=F(24, True), fill=(255, 255, 255, int(255 * a)), anchor='mm')
    for i, (title, ts, leaf) in enumerate(MM_NODES):
        g = (grow - 0.18 - i * 0.12) / 0.3
        if g <= 0:
            continue
        ny = MM_YS[i]
        pts = bezier((x1, cy), (MM_X0, ny + MM_H / 2), min(1, g / 0.6))
        if len(pts) > 1:
            d.line(pts, fill=ACCENT + (200,), width=4, joint='curve')
        na = ease((g - 0.55) / 0.45)
        if na <= 0:
            continue
        dx = 14 * (1 - na)
        d.rounded_rectangle((MM_X0 + dx, ny, MM_X1 + dx, ny + MM_H), 18, fill=(255, 255, 255, int(255 * na)),
                            outline=(226, 222, 212, int(255 * na)), width=2)
        d.rounded_rectangle((MM_X0 + dx, ny + 14, MM_X0 + dx + 6, ny + MM_H - 14), 3, fill=ACCENT + (int(255 * na),))
        d.text((MM_X0 + 24 + dx, ny + 32), ts, font=F(19, mono=True), fill=ACCENT + (int(255 * na),), anchor='lm')
        d.text((MM_X0 + 24 + dx, ny + 72), title, font=F(25, True), fill=INK + (int(255 * na),), anchor='lm')
        d.text((MM_X0 + 24 + dx, ny + 114), leaf, font=F(21), fill=(110, 106, 98, int(255 * na)), anchor='lm')


# ---------- composed app state ----------
def app(tab='notes', notes=(0, False), summary=None, mindmap=None, scroll=0.0, hl=None, hl_a=0.0, t_sec=0.0):
    img = APP.copy()
    set_tab(img, tab)
    draw_transcript(img, scroll, hl, hl_a)
    draw_time(img, t_sec)
    if tab == 'notes':
        draw_notes(img, *notes)
    elif tab == 'summary':
        draw_summary(img, *summary)
    else:
        draw_mindmap(img, mindmap)
    return img


PAD, OFF = vk.pad16x9(APP, color=TR_BG)


def padded(img):
    p = Image.new('RGB', PAD.size, TR_BG)
    p.paste(img, OFF)
    return p


def P(pt):
    return bv.shift(pt, OFF)


FULL = vk.full(PAD)
ZOOM = vk.view(P((440, 230, 1998, 1250)), PAD.size, pad=0.0, max_up=1.3)      # retina source
PZOOM = vk.view(P((1180, 430, 1998, 1268)), PAD.size, pad=0.02, max_up=1.3)


def shot(state, rect):
    return vk.render(padded(state), rect)


def coming_soon(out, a):
    """Badge beside the step bar, outside the app screen so it never covers the UI."""
    vk.badge(out, (200 * U, 39 * U), 'Coming soon · preview', a, color=ACCENT)
    return out


# ---------- hook ----------
LOGO = bv.logo.resize((int(52 * U), int(52 * U)), Image.LANCZOS)
LOGO.putalpha(LOGO.convert('L').point(lambda v: 0 if v > 235 else 255))
HOOK_STATE = app('summary', summary=(1.0, 2), hl=2, hl_a=1.0, t_sec=40.11)
WIN_INTRO, WG = vk.window(HOOK_STATE.crop((436, 0, 2000, 1273)), int(720 * U * 0.82))


def intro(t, s):
    img = vk.glow_bg().copy()
    fade = lambda st, d=0.45: ease((s - st) / d)
    x0 = int(110 * U)
    vk.paste_fade(img, LOGO, (x0, int(150 * U)), fade(0))
    vk.text(img, (x0 + 66 * U, 176 * U), 'TranscriptX', 34 * U, DARK, fade(0))
    vk.text(img, (x0, 252 * U), 'COMING SOON', 26 * U, ACCENT, fade(0.15))
    for k, (txt, col, st) in enumerate([('Notes, Summary', DARK, 0.25), ('and Mind map', ACCENT, 0.5), ('next to your transcript.', DARK, 0.75)]):
        a = fade(st, 0.45)
        vk.text(img, (x0 - 4, 330 * U + k * 78 * U + 26 * U * (1 - a)), txt, 60 * U, col, a)
    a = fade(1.15)
    vk.text(img, (x0, 600 * U), 'Key points with timestamps. One click', 29 * U, GREY, a, bold=False)
    vk.text(img, (x0, 642 * U), 'jumps to that moment in the transcript.', 29 * U, GREY, a, bold=False)
    aw = fade(0.3, 0.9)
    vk.paste_fade(img, WIN_INTRO, (W - WIN_INTRO.width - 30 * U, 120 * U + 140 * U * (1 - aw) - 10 * U * s), aw)
    return img


vk.scene(dur(0, 3.8), intro)

# ---------- 1. Notes ----------
NOTE_AT = P((1560, 538))


def s1(t, s):
    rect = lerp(FULL, ZOOM, ease(s / 1.0))
    click = (s - 1.1) / 0.45
    typing = (s - 1.45) / 2.6
    n = int(NOTE_CHARS * max(0.0, min(1.0, typing)))
    caret = s > 1.3 and (int(s * 2.5) % 2 == 0 or 0 < typing < 1)
    sc = shot(app('notes', notes=(n, caret)), rect)
    tab_box = vk.box_s(P((1478, 365, 1562, 432)), rect)
    vk.outline(sc, tab_box, ease((s - 0.4) / 0.3) * (1 - ease((s - 1.3) / 0.3)), pad=4)
    pos, k = vk.to_s(NOTE_AT, rect)
    vk.ring(sc, pos, click, k)
    vk.cursor(sc, vk.path((SW * 0.45, SH * 0.82), (pos[0] + 6, pos[1] + 8), (s - 0.3) / 0.8), vk.press(click))
    return vk.caption(vk.frame(sc, 1), 1, 'Type your own notes next to the transcript', ease(s / 0.35))


vk.scene(dur(1, 4.6), s1)

# ---------- 2. Summary ----------
SUM_TAB = P((TAB_X['summary'], TAB_Y))


def s2(t, s):
    click = (s - 0.7) / 0.45
    tab = 'summary' if s > 0.8 else 'notes'
    rev = max(0.0, min(1.0, (s - 0.85) / 2.6))
    st = app(tab, notes=(NOTE_CHARS, False), summary=(rev, None)) if tab == 'notes' else app(tab, summary=(rev, None))
    sc = shot(st, ZOOM)
    pos, k = vk.to_s(SUM_TAB, ZOOM)
    start, _ = vk.to_s(NOTE_AT, ZOOM)
    vk.ring(sc, pos, click, k)
    vk.cursor(sc, vk.path((start[0] + 6, start[1] + 8), (pos[0] + 6, pos[1] + 8), s / 0.7), vk.press(click))
    return vk.caption(coming_soon(vk.frame(sc, 2), ease((s - 1.0) / 0.3)), 2, 'Summary: the key points, each with its timestamp', ease(s / 0.35))


vk.scene(dur(2, 4.0), s2)

# ---------- 3. Click a timestamp -> transcript jumps there ----------
def chip_c(i):
    x0, y0, x1, y1 = chip_box(i)
    return P(((x0 + x1) / 2, (y0 + y1) / 2))


S_TOP = scroll_to(3)


def s3(t, s):
    c1, c2 = (s - 0.8) / 0.45, (s - 3.0) / 0.45
    if s < 0.95:
        active, hl, hl_a, scroll, ts = None, None, 0.0, 0.0, 0.0
    elif s < 3.15:
        active, hl, hl_a, scroll, ts = 2, 2, ease((s - 0.95) / 0.3), 0.0, 40.11
    else:
        e = ease((s - 3.15) / 0.7)
        active, hl, hl_a, scroll, ts = 3, 3, ease((s - 3.6) / 0.3), S_TOP * e, 96.51
    hover = 2 if 0.5 < s < 0.95 else (3 if 2.6 < s < 3.15 else None)
    sc = shot(app('summary', summary=(1.0, active, hover), scroll=scroll, hl=hl, hl_a=hl_a, t_sec=ts), ZOOM)
    p1, k = vk.to_s(chip_c(2), ZOOM)
    p2, _ = vk.to_s(chip_c(3), ZOOM)
    start, _ = vk.to_s(SUM_TAB, ZOOM)
    vk.ring(sc, p1, c1, k)
    vk.ring(sc, p2, c2, k)
    if s < 2.3:
        pos = vk.path((start[0] + 6, start[1] + 8), (p1[0] + 4, p1[1] + 6), s / 0.8)
    else:
        pos = vk.path((p1[0] + 4, p1[1] + 6), (p2[0] + 4, p2[1] + 6), (s - 2.3) / 0.7, arc=16)
    vk.cursor(sc, pos, vk.press(c1) or vk.press(c2))
    if 1.2 < s < 2.9:
        bx = vk.box_s(P((TX0 - 22, LAYOUT[2][0] - 26, TX0 + TXW + 22, LAYOUT[2][1][-1] + 26)), ZOOM)
        vk.badge(sc, (bx[2] - 130 * U, bx[1] - 4 * U), 'Jumped to 00:40',
                 ease((s - 1.2) / 0.3) * (1 - ease((s - 2.6) / 0.3)), color=DARK)
    return vk.caption(coming_soon(vk.frame(sc, 3), 1.0), 3, 'Click a timestamp to jump to that part', ease(s / 0.35))


vk.scene(dur(3, 5.2), s3)

# ---------- 4. Mind map ----------
MM_TAB = P((TAB_X['mindmap'], TAB_Y))


def s4(t, s):
    click = (s - 0.7) / 0.45
    tab = 'mindmap' if s > 0.8 else 'summary'
    grow = max(0.0, min(1.0, (s - 0.9) / 2.4))
    base = dict(scroll=S_TOP, hl=3, hl_a=1.0 - ease((s - 0.8) / 0.4), t_sec=96.51)
    st = app(tab, mindmap=grow, **base) if tab == 'mindmap' else app(tab, summary=(1.0, 3), **base)
    rect = lerp(ZOOM, PZOOM, ease((s - 1.0) / 1.6))
    sc = shot(st, rect)
    pos, k = vk.to_s(MM_TAB, rect)
    start, _ = vk.to_s(chip_c(3), ZOOM)
    vk.ring(sc, pos, click, k)
    vk.cursor(sc, vk.path((start[0] + 4, start[1] + 6), (pos[0] + 6, pos[1] + 8), s / 0.7), vk.press(click))
    return vk.caption(coming_soon(vk.frame(sc, 4), 1.0), 4, 'Mind map: the whole video at a glance', ease(s / 0.35))


vk.scene(dur(4, 4.6), s4)

# ---------- CTA ----------
LOGO_BIG = bv.logo.resize((int(84 * U), int(84 * U)), Image.LANCZOS)
LOGO_BIG.putalpha(LOGO_BIG.convert('L').point(lambda v: 0 if v > 235 else 255))


def outro(t, s):
    img = vk.glow_bg((0.27, 0.15, 0.73, 0.9), 60).copy()
    a = ease(s / 0.4)
    vk.paste_fade(img, LOGO_BIG, (W / 2 - LOGO_BIG.width / 2, 190 * U), a)
    vk.text(img, (W / 2, 340 * U), 'Summary and Mind map are coming soon', 52 * U, DARK, a, anchor='mm')
    vk.text(img, (W / 2, 408 * U), 'Get the transcript free today. Pro users get the beta first.', 32 * U, GREY, ease((s - 0.3) / 0.4), bold=False, anchor='mm')
    a3 = ease((s - 0.6) / 0.4)
    p = 1 + 0.025 * max(0.0, math.sin((s - 1.0) * 5)) if s > 1.0 else 1
    bw, bh = 520 * U * p, 76 * U * p
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle((W / 2 - bw / 2, 500 * U - bh / 2, W / 2 + bw / 2, 500 * U + bh / 2), int(bh / 2), fill=ACCENT + (int(255 * a3),))
    vk.text(img, (W / 2, 500 * U), 'transcriptx.ai', 34 * U, (255, 255, 255), a3, anchor='mm')
    return img


vk.scene(dur(5, 3.4), outro)

def add_voice(mp4, xfade=0.35, gain_db=3, music_db=-5):
    """Mux voice-over + a soft music bed (gen_soft_music.py) under the silent render. Each line is delayed to its
    scene start; the music ducks under the voice (sidechain). AAC 192k, video stream copied."""
    import subprocess, tempfile, imageio_ffmpeg, gen_soft_music
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    XF, t, starts = round(xfade * vk.FPS), 0, []
    for n, _ in vk.scenes:                         # same timeline as vk.export (scenes overlap by the crossfade)
        starts.append(t / vk.FPS)
        t += n - XF
    total = (sum(n for n, _ in vk.scenes) - XF * (len(vk.scenes) - 1)) / vk.FPS
    args, chains = [ff, '-y', '-loglevel', 'error', '-i', mp4], []
    for k, ((f, _), (off, _)) in enumerate(zip(VO, VO_LINES)):
        args += ['-i', f]
        ms = int((starts[k] + off) * 1000)
        chains.append(f'[{k + 1}:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms}[v{k}]')
    music = f'{tempfile.mkdtemp(prefix="bed_")}/bed.wav'
    gen_soft_music.write(music, total + 0.5)
    args += ['-i', music]
    mi = len(VO) + 1
    mix = ''.join(f'[v{k}]' for k in range(len(VO)))
    fc = (';'.join(chains) + f';{mix}amix=inputs={len(VO)}:normalize=0,volume={gain_db}dB,apad,atrim=0:{total:.3f},asplit=2[vo][sc]'
          f';[{mi}:a]volume={music_db}dB[bed];[bed][sc]sidechaincompress=threshold=0.02:ratio=5:attack=30:release=600[duck]'
          f';[vo][duck]amix=inputs=2:normalize=0,atrim=0:{total:.3f}[a]')
    tmp = mp4.replace('.mp4', '.tmp.mp4')
    subprocess.run(args + ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                           '-movflags', '+faststart', tmp], check=True)
    os.replace(tmp, mp4)
    print('voice added', round(total, 2), 's')


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'voice':                 # only re-mux the voice onto the last render
        add_voice(f'{OUT}/video/{BASE}.mp4')
    elif len(sys.argv) > 1 and sys.argv[1] == 'stills':                # quick check without encoding
        d = os.path.dirname(SHEET)
        app('notes', notes=(NOTE_CHARS, False)).save(f'{d}/st_notes.png')
        app('summary', summary=(1.0, 2), hl=2, hl_a=1.0, t_sec=40.11).save(f'{d}/st_summary.png')
        app('summary', summary=(1.0, 3), scroll=S_TOP, hl=3, hl_a=1.0, t_sec=96.51).save(f'{d}/st_summary2.png')
        app('mindmap', mindmap=1.0, scroll=S_TOP, t_sec=96.51).save(f'{d}/st_mindmap.png')
        app('summary', summary=(0.1, None)).save(f'{d}/st_gen.png')
    else:
        vk.export(OUT, BASE, poster_at=3.2, preview_sheet=SHEET)
        add_voice(f'{OUT}/video/{BASE}.mp4')
