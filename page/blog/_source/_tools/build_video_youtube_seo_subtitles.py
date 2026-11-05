"""YouTube knowledge video (2560x1440, 60 fps, English voice-over): "YouTube SEO: The One Thing Almost Everyone Ignores".

Script: social_content/03-youtube-seo-subtitles/script.md. Claims are limited to YouTube Help:
  - search relevance = "how well the title, tags, description, and video content match your search query" (answer/16090438)
  - "Subtitle and caption files contain the text of what is said in the video" / "larger audience" (answer/2734796)
Part 1 = explainer cards (no third-party screens). Part 2 = workflow on real screens:
TranscriptX (homepage -> Upload menu -> transcript -> Edit -> Download .srt) and YouTube Studio
(external/youtube/youtube-studio-*.png, user captures 2026-11-05; Studio screens are used in video only).
Voice-over: edge-tts en-US-AvaNeural, one line per scene, over the soft ducked music bed (gen_soft_music.py).

Run:  python3 build_video_youtube_seo_subtitles.py          (full render + voice)
      python3 build_video_youtube_seo_subtitles.py stills   (2 stills per scene, no encode, SKIP_VO=1 recommended)
"""
import math, os, sys
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFilter

import video_hq as vk
from video_hq import W, H, U, SW, SH, BG, DARK, ACCENT, GREY, GREEN, ease, lerp

bv = vk.bv
ROOT = os.path.abspath(f'{vk.HERE}/../../../..')
OUT = f'{ROOT}/social_content/03-youtube-seo-subtitles'
BASE = 'youtube-seo-subtitles'
SCRATCH = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/6c996221-4dc2-4dbb-ba03-fc2ed24b5881/scratchpad'
SHEET = f'{SCRATCH}/seo_sheet.png'
RED = (200, 52, 44)
vk.STEPS[:] = ['Upload', 'Transcript', 'Check names', 'Download .srt', 'YouTube Studio']

# ---------- voice-over: one line per scene ----------
VOICE = os.environ.get('VO_VOICE', 'en-US-AvaNeural')
RATE = os.environ.get('VO_RATE', '+4%')
EDGE_TTS = os.environ.get('EDGE_TTS', os.path.expanduser('~/Library/Python/3.9/bin/edge-tts'))
VO_LINES = [
    (0.3, "You spent an hour on your title and your thumbnail. But there's one box almost every creator leaves empty. "
          "And it's the one that tells YouTube what you actually said."),
    (0.3, "It's subtitles. Not the auto-captions YouTube makes for you, but your own subtitle file, uploaded with the video. "
          "Here's why it matters, and how to add one in about five minutes."),
    (0.3, "YouTube's own help page says search looks at how well your title, tags, description, and video content "
          "match what people search for."),
    (0.3, "Your title is a few words. Your description, a few lines. But a ten minute video can hold around fifteen hundred spoken words."),
    (0.3, "And YouTube describes a subtitle file as the text of what is said in the video. "
          "Every word, every topic, every keyword you mention, in a form YouTube can read."),
    (0.3, "But YouTube already makes auto-captions, right? It does, but they're a guess. "
          "Names, brand words and niche terms are where they slip most. And those are often your keywords."),
    (0.3, "There's a second win. Many people watch with the sound off, or in their second language. "
          "YouTube says captions help you share your videos with a larger audience. "
          "And viewers who can follow along keep watching. Watch time is one of the signals YouTube uses."),
    (0.3, "To be fair, subtitles won't rescue a weak video, and YouTube doesn't say how much they count. "
          "They're simply the cheapest SEO win most channels skip."),
    (0.3, "Here's the workflow. Open TranscriptX, click Upload, and pick your video, "
          "from your computer, Google Drive, Dropbox or OneDrive."),
    (0.3, "TranscriptX turns your speech into text, with a timestamp on every paragraph."),
    (0.3, "Give it a quick read, and fix any names with the edit button, so your keywords are spelled right."),
    (0.3, "Then click Download, and pick S R T."),
    (0.3, "Now open your video in YouTube Studio. Your title and description are set. Next, click Subtitles."),
    (0.3, "Add your language, choose Upload file, then With timing, and select your S R T file."),
    (0.3, "Your subtitles line up with the video, line by line. Click Done, and publish."),
    (0.3, "Title, thumbnail, tags, and now subtitles. Try it on your next upload. Get your S R T free at transcriptx dot A I."),
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


VO = _make_vo() if not os.environ.get('SKIP_VO') else [(None, 0.0)] * len(VO_LINES)


def dur(i, base):
    return max(base, VO_LINES[i][0] + VO[i][1] + 0.7)


def fade(s, st, d=0.45):
    return ease((s - st) / d)


def centre(b):
    return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)


def load(rel):
    return Image.open(f'{bv.SRC}/{rel}').convert('RGB')


LOGO = bv.logo.resize((int(46 * U), int(46 * U)), Image.LANCZOS)
LOGO.putalpha(LOGO.convert('L').point(lambda v: 0 if v > 235 else 255))
LOGO_BIG = bv.logo.resize((int(84 * U), int(84 * U)), Image.LANCZOS)
LOGO_BIG.putalpha(LOGO_BIG.convert('L').point(lambda v: 0 if v > 235 else 255))


# ---------- drawing helpers for the explainer cards ----------
@lru_cache(maxsize=16)
def card_sprite(w, h, radius=int(22 * U)):
    g = int(36 * U)
    out = Image.new('RGBA', (w + 2 * g, h + 2 * g), (0, 0, 0, 0))
    sh = Image.new('RGBA', out.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((g, g + 16, g + w, g + h + 16), radius, fill=(70, 40, 20, 60))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(18 * U))))
    ImageDraw.Draw(out).rounded_rectangle((g, g, g + w, g + h), radius, fill=(255, 255, 255, 255), outline=(232, 228, 220, 255))
    return out, g


def card(img, x, y, w, h, a=1.0):
    spr, g = card_sprite(int(w), int(h))
    vk.paste_fade(img, spr, (x - g, y + 18 * U * (1 - a) - g), a)
    return y + 18 * U * (1 - a)


def brand(img, a=1.0):
    x0 = int(110 * U)
    vk.paste_fade(img, LOGO, (x0, int(62 * U)), a)
    vk.text(img, (x0 + 60 * U, 62 * U + 23 * U), 'TranscriptX  ·  YouTube SEO', 26 * U, GREY, a, bold=False)


def check_box(d, x, y, size, state, a=1.0, pulse=0.0):
    """state: 'on' (orange tick), 'empty' (pulsing red outline)."""
    al = int(255 * a)
    if state == 'on':
        d.rounded_rectangle((x, y, x + size, y + size), int(size * 0.22), fill=ACCENT + (al,))
        vk._check(d, x + size / 2, y + size / 2, size * 0.55, (255, 255, 255, al), max(3, int(size * 0.12)))
    else:
        col = tuple(int(c0 + (c1 - c0) * pulse) for c0, c1 in zip((200, 196, 188), RED))
        d.rounded_rectangle((x, y, x + size, y + size), int(size * 0.22), outline=col + (al,), width=max(3, int(size * 0.09)))


ITEMS = ['Title', 'Thumbnail', 'Description', 'Tags', 'Subtitles']


def checklist(img, x, y, s, ticks, a=1.0, done_all=False):
    """ticks: list of start times for the first 4 ticks; the 5th stays empty unless done_all."""
    w, row = 560 * U, 84 * U
    cy = card(img, x, y, w, row * 5 + 50 * U, a)
    d = ImageDraw.Draw(img, 'RGBA')
    for k, name in enumerate(ITEMS):
        ry = cy + 25 * U + k * row
        last = k == 4
        on = done_all or (not last and s >= ticks[k])
        pulse = 0.5 + 0.5 * math.sin(s * 5) if last and not done_all else 0
        check_box(d, x + 40 * U, ry + 18 * U, 46 * U, 'on' if on else 'empty', a, pulse)
        col = (RED if (last and not done_all) else DARK)
        vk.text(img, (x + 112 * U, ry + 41 * U), name, 38 * U, col, a)
        if k < 4:
            d.line((x + 30 * U, ry + row, x + w - 30 * U, ry + row), fill=(236, 232, 224, int(255 * a)), width=2)


# ---------- 0. hook: the checklist with one empty box ----------
def s_hook(t, s):
    img = vk.glow_bg((0.5, 0.05, 0.95, 0.9), 70).copy()
    brand(img, fade(s, 0))
    x0 = int(110 * U)
    for k, (txt, col, st) in enumerate([('The one thing', DARK, 0.2), ('almost everyone', DARK, 0.4), ('ignores', ACCENT, 0.6)]):
        a = fade(s, st)
        vk.text(img, (x0 - 4, 300 * U + k * 80 * U + 26 * U * (1 - a)), txt, 64 * U, col, a)
    vk.text(img, (x0, 610 * U), 'Most creators do four of these five.', 30 * U, GREY, fade(s, 2.4), bold=False)
    checklist(img, W - 560 * U - 100 * U, 170 * U, s, [1.0, 1.5, 2.0, 2.5], fade(s, 0.3, 0.7))
    return img


vk.scene(dur(0, 5.0), s_hook)


# ---------- 1. it's subtitles: your own file, not auto-captions ----------
def chip(img, cx, cy, txt, color, a, icon=None):
    f = vk.font(32 * U, True)
    d = ImageDraw.Draw(img, 'RGBA')
    tw = d.textlength(txt, font=f) + (44 * U if icon else 0)
    h = 40 * U
    y = cy + 14 * U * (1 - a)
    d.rounded_rectangle((cx - tw / 2 - 30 * U, y - h, cx + tw / 2 + 30 * U, y + h), int(h), fill=color + (int(245 * a),))
    tx = cx - tw / 2
    al = int(255 * a)
    if icon == 'x':
        r = 11 * U
        d.line((tx + 6 * U, y - r, tx + 6 * U + 2 * r, y + r), fill=(255, 255, 255, al), width=int(5 * U))
        d.line((tx + 6 * U, y + r, tx + 6 * U + 2 * r, y - r), fill=(255, 255, 255, al), width=int(5 * U))
        tx += 44 * U
    elif icon == 'ok':
        vk._check(d, tx + 16 * U, y, 26 * U, (255, 255, 255, al), int(5 * U))
        tx += 44 * U
    d.text((tx, y), txt, font=f, fill=(255, 255, 255, al), anchor='lm')


def s_subs(t, s):
    img = vk.glow_bg((0.25, 0.1, 0.75, 0.8), 65).copy()
    brand(img, 1)
    a = fade(s, 0.1, 0.5)
    k = 0.92 + 0.08 * a
    vk.text(img, (W / 2, 330 * U), 'Subtitles', 150 * U * k, DARK, a, anchor='mm')
    d = ImageDraw.Draw(img, 'RGBA')
    u = ease((s - 0.6) / 0.6)
    if u > 0:
        hw = 330 * U * u
        d.rounded_rectangle((W / 2 - hw, 418 * U, W / 2 + hw, 432 * U), int(7 * U), fill=ACCENT + (255,))
    chip(img, W / 2 - 330 * U, 560 * U, 'Auto-captions: a guess', GREY, fade(s, 2.2), 'x')
    chip(img, W / 2 + 330 * U, 560 * U, 'Your own .srt file', ACCENT, fade(s, 3.2), 'ok')
    return img


vk.scene(dur(1, 5.0), s_subs)


# ---------- 2 + 4. quotes from YouTube Help ----------
def quote_scene(lines, mark, source, st_mark=1.6):
    """lines: quote lines; mark: (line index, substring) to underline in orange."""
    def fn(t, s):
        img = vk.glow_bg((0.2, 0.1, 0.8, 0.85), 60).copy()
        brand(img, 1)
        a = fade(s, 0.1, 0.5)
        w, h = 1220 * U, (110 + 92 * len(lines)) * U
        x, y = (W - w) / 2, 200 * U
        cy = card(img, x, y, w, h, a)
        vk.text(img, (x + 60 * U, cy + 60 * U), 'YouTube Help', 26 * U, RED, a)
        f = vk.font(46 * U, True)
        d = ImageDraw.Draw(img, 'RGBA')
        for k, ln in enumerate(lines):
            ly = cy + 140 * U + k * 92 * U
            if k == mark[0]:
                i = ln.find(mark[1])
                x0 = x + 60 * U + d.textlength(ln[:i], font=f)
                x1 = x0 + d.textlength(mark[1], font=f)
                m = ease((s - st_mark) / 0.5)
                if m > 0:
                    d.rounded_rectangle((x0 - 8 * U, ly - 34 * U, x0 - 8 * U + (x1 - x0 + 16 * U) * m, ly + 34 * U),
                                        int(10 * U), fill=(250, 214, 190, int(255 * a)))
            vk.text(img, (x + 60 * U, ly), ln, 46 * U, DARK, a)
        vk.text(img, (W / 2, cy + h + 70 * U), source, 26 * U, GREY, fade(s, 0.8), bold=False, anchor='mm')
        return img
    return fn


vk.scene(dur(2, 5.0), quote_scene(
    ['“…how well the title, tags, description,', 'and video content match your search query.”'],
    (1, 'video content'), 'support.google.com/youtube/answer/16090438  ·  How YouTube search works', st_mark=3.4))


# ---------- 3. how many words each field holds ----------
BARS = [('Title', '~8 words', 8), ('Description', '~60 words', 60), ('What you say in 10 min', '~1,500 words', 1500)]


def s_words(t, s):
    img = vk.glow_bg((0.2, 0.1, 0.8, 0.85), 60).copy()
    brand(img, 1)
    vk.text(img, (110 * U, 200 * U), 'How much text YouTube can read', 54 * U, DARK, fade(s, 0.1))
    d = ImageDraw.Draw(img, 'RGBA')
    x0, bw_max = 560 * U, W - 560 * U - 160 * U
    starts = [0.4, 1.3, 2.6]
    for k, (name, lab, n) in enumerate(BARS):
        a = fade(s, starts[k], 0.4)
        y = 340 * U + k * 130 * U
        vk.text(img, (110 * U, y), name, 34 * U, DARK if k < 2 else ACCENT, a)
        grow = ease((s - starts[k]) / 0.9)
        bw = max(52 * U, bw_max * n / 1500) * grow              # true scale: the short fields really are tiny
        if grow > 0:
            d.rounded_rectangle((x0, y - 26 * U, x0 + bw, y + 26 * U), int(26 * U),
                                fill=(ACCENT if k == 2 else (214, 208, 198)) + (int(255 * a),))
        vk.text(img, (x0 + bw + 24 * U, y), lab, 30 * U, GREY, a * (1 if k < 2 else 0), bold=True)
        if k == 2 and grow > 0.6:
            vk.text(img, (x0 + 30 * U, y), lab, 30 * U, (255, 255, 255), ease((grow - 0.6) / 0.4), bold=True)
    vk.text(img, (110 * U, 730 * U), 'Typical speaking pace: about 150 words per minute.', 24 * U, GREY, fade(s, 3.4), bold=False)
    return img


vk.scene(dur(3, 5.0), s_words)

vk.scene(dur(4, 5.0), quote_scene(
    ['“Subtitle and caption files contain', 'the text of what is said in the video.”'],
    (1, 'what is said in the video'), 'support.google.com/youtube/answer/2734796  ·  Add subtitles & captions', st_mark=2.2))


# ---------- 5. auto-captions guess (illustrative example) ----------
def s_auto(t, s):
    img = vk.glow_bg((0.2, 0.1, 0.8, 0.85), 60).copy()
    brand(img, 1)
    vk.text(img, (W / 2, 200 * U), 'Auto-captions guess. Your keywords pay for it.', 54 * U, DARK, fade(s, 0.1), anchor='mm')
    w, h = 1080 * U, 150 * U
    x = (W - w) / 2
    d = ImageDraw.Draw(img, 'RGBA')
    rows = [('Auto-captions', 'add transcript ex to chat GPT', 'transcript ex', RED, 1.6),
            ('Your .srt', 'Add TranscriptX to ChatGPT', 'TranscriptX', GREEN, 3.6)]
    for k, (lab, line, bad, col, st) in enumerate(rows):
        a = fade(s, st)
        y = card(img, x, 300 * U + k * 200 * U, w, h, a)
        vk.text(img, (x + 50 * U, y + 44 * U), lab.upper(), 22 * U, col, a)
        f = vk.font(46 * U, True)
        tx = x + 50 * U
        vk.text(img, (tx, y + 100 * U), line, 46 * U, DARK, a)
        i = line.find(bad)
        bx0 = tx + d.textlength(line[:i], font=f)
        bx1 = bx0 + d.textlength(bad, font=f)
        m = ease((s - st - 0.6) / 0.4)
        if m > 0:
            if k == 0:
                d.line((bx0, y + 100 * U, bx0 + (bx1 - bx0) * m, y + 100 * U), fill=RED + (int(255 * a),), width=int(5 * U))
            else:
                d.rounded_rectangle((bx0 - 6 * U, y + 128 * U, bx0 - 6 * U + (bx1 - bx0 + 12 * U) * m, y + 134 * U),
                                    int(3 * U), fill=GREEN + (int(255 * a),))
    vk.text(img, (W / 2, 740 * U), 'Illustrative example', 24 * U, GREY, fade(s, 1.6), bold=False, anchor='mm')
    return img


vk.scene(dur(5, 5.0), s_auto)


# ---------- 6. the second win: reach ----------
def icon_muted(d, cx, cy, r, col):
    d.polygon([(cx - r * 0.9, cy - r * 0.3), (cx - r * 0.45, cy - r * 0.3), (cx, cy - r * 0.75), (cx, cy + r * 0.75),
               (cx - r * 0.45, cy + r * 0.3), (cx - r * 0.9, cy + r * 0.3)], fill=col)
    wd = max(4, int(r * 0.13))
    d.line((cx + r * 0.3, cy - r * 0.35, cx + r * 0.95, cy + r * 0.35), fill=col, width=wd)
    d.line((cx + r * 0.3, cy + r * 0.35, cx + r * 0.95, cy - r * 0.35), fill=col, width=wd)


def icon_globe(d, cx, cy, r, col):
    wd = max(4, int(r * 0.11))
    d.ellipse((cx - r * 0.85, cy - r * 0.85, cx + r * 0.85, cy + r * 0.85), outline=col, width=wd)
    d.ellipse((cx - r * 0.38, cy - r * 0.85, cx + r * 0.38, cy + r * 0.85), outline=col, width=wd)
    d.line((cx - r * 0.85, cy, cx + r * 0.85, cy), fill=col, width=wd)


def icon_cc(d, cx, cy, r, col):
    d.rounded_rectangle((cx - r * 0.95, cy - r * 0.65, cx + r * 0.95, cy + r * 0.65), int(r * 0.2), fill=col)
    d.text((cx, cy), 'CC', font=vk.font(r * 0.8, True), fill=(255, 255, 255, 255), anchor='mm')


REACH = [(icon_muted, 'Sound off'), (icon_globe, 'Second language'), (icon_cc, 'Deaf or hard of hearing')]


def s_reach(t, s):
    img = vk.glow_bg((0.2, 0.1, 0.8, 0.85), 60).copy()
    brand(img, 1)
    vk.text(img, (W / 2, 190 * U), 'Win #2: more people can follow along', 54 * U, DARK, fade(s, 0.1), anchor='mm')
    cw, ch, gap = 380 * U, 300 * U, 50 * U
    x0 = (W - (3 * cw + 2 * gap)) / 2
    for k, (ic, lab) in enumerate(REACH):
        a = fade(s, 0.8 + k * 0.5)
        x = x0 + k * (cw + gap)
        y = card(img, x, 270 * U, cw, ch, a)
        d = ImageDraw.Draw(img, 'RGBA')
        ic(d, x + cw / 2, y + 120 * U, 62 * U, ACCENT + (int(255 * a),))
        vk.text(img, (x + cw / 2, y + 240 * U), lab, 30 * U, DARK, a, anchor='mm')
    vk.text(img, (W / 2, 660 * U), '“Subtitles and captions allow you to share your videos with a larger audience”',
            30 * U, DARK, fade(s, 6.0), bold=False, anchor='mm')
    vk.text(img, (W / 2, 705 * U), 'YouTube Help', 22 * U, GREY, fade(s, 6.0), anchor='mm')
    vk.badge(img, (W / 2, 770 * U), 'Viewers who follow along keep watching', fade(s, 9.0), color=DARK)
    return img


vk.scene(dur(6, 6.0), s_reach)


# ---------- 7. to be fair ----------
def s_fair(t, s):
    img = vk.glow_bg((0.25, 0.15, 0.75, 0.85), 55).copy()
    brand(img, 1)
    vk.text(img, (W / 2, 330 * U), 'Not magic.', 110 * U, DARK, fade(s, 0.2), anchor='mm')
    vk.text(img, (W / 2, 470 * U), 'Just free.', 110 * U, ACCENT, fade(s, 4.5), anchor='mm')
    vk.text(img, (W / 2, 600 * U), "YouTube doesn't publish how much subtitles count.", 30 * U, GREY, fade(s, 2.0), bold=False, anchor='mm')
    return img


vk.scene(dur(7, 5.0), s_fair)


# ---------- part 2: the workflow on real screens ----------
HOME = load('homepage/homepage.png')                                   # 2000x999
MENU = Image.open(f'{bv.SRC}/upload/upload-source-options.png').convert('RGB')   # 528x418
RESULT = load('transcript/transcript-result-light.png')               # 2000x987
DLMENU = load('transcript/transcript-download-menu-open.png')         # 2000x995
STUDIO = load('external/youtube/youtube-studio-video-details.png')    # 2576x1201
EDITOR = load('external/youtube/youtube-studio-subtitles-editor.png') # 2576x1203

# Upload menu pasted onto the homepage so its Upload button sits on the homepage's Upload button
UPLOAD = (672, 515, 800, 562)
mk = (UPLOAD[2] - UPLOAD[0]) / (255 - 65)
menu = MENU.resize((round(MENU.width * mk), round(MENU.height * mk)), Image.LANCZOS)
HOME_MENU = HOME.copy()
HOME_MENU.paste(menu, (round(UPLOAD[0] - 65 * mk), round(UPLOAD[1] - 333 * mk)))
DEVICE = (round(UPLOAD[0] - 65 * mk + 95 * mk), round(UPLOAD[1] - 333 * mk + 30 * mk),
          round(UPLOAD[0] - 65 * mk + 390 * mk), round(UPLOAD[1] - 333 * mk + 80 * mk))


def screen_scene(i, base, step, cap, images, zoom_boxes, clicks=(), outlines=(), badges=(), max_up=1.4, pad=0.2,
                 swaps=()):
    """images: dict name->RGB; zoom_boxes: list of (t_start, name, box) keyframes;
    clicks: (t, name, box); outlines: (t0, t1, name, box); badges: (t0, t1, name, box, text, dx, dy, color);
    swaps: (t, from_name, to_name) crossfades for the screen image."""
    pads = {k: vk.pad16x9(v) for k, v in images.items()}
    ref = next(iter(images))

    def sh(name, b):
        return bv.shift(b, pads[name][1])

    keys = [(st, vk.full(pads[n][0]) if b is None else vk.view(sh(n, b), pads[n][0].size, pad=pad, max_up=max_up))
            for st, n, b in zoom_boxes]

    def rect_at(s):
        r = keys[0][1]
        for k in range(1, len(keys)):
            st = keys[k][0]
            r = lerp(r, keys[k][1], ease((s - st) / 1.0)) if s > st else r
        return r

    def fn(t, s):
        rect = rect_at(s)
        name = ref
        sc = vk.render(pads[name][0], rect)
        for st, a_name, b_name in swaps:
            if s >= st:
                f = ease((s - st) / 0.25)
                sc_b = vk.render(pads[b_name][0], rect)
                sc = Image.blend(sc, sc_b, f) if f < 1 else sc_b
        for t0, t1, n, b in outlines:
            a = ease((s - t0) / 0.3) * (1 - ease((s - t1) / 0.3))
            vk.outline(sc, vk.box_s(sh(n, b), rect), a, pad=5)
        for t0, t1, n, b, txt, dx, dy, col in badges:
            a = ease((s - t0) / 0.3) * (1 - ease((s - t1) / 0.3))
            bb = vk.box_s(sh(n, b), rect)
            vk.badge(sc, ((bb[0] + bb[2]) / 2 + dx * U, bb[1] + dy * U), txt, a, color=col)
        # cursor: travels to each click target in turn
        if clicks:
            pos = (SW * 0.55, SH * 0.88)
            pressed = False
            for k, (tc, n, b) in enumerate(clicks):
                c, kk = vk.to_s(centre(sh(n, b)), rect)
                target = (c[0] + 8, c[1] + 8)
                if s >= tc - 1.1:
                    pos = vk.path(pos, target, (s - (tc - 1.1)) / 0.9)
                cl = (s - tc) / 0.45
                vk.ring(sc, c, cl, max(1.0, kk))
                pressed = pressed or vk.press(cl)
            vk.cursor(sc, pos, pressed)
        return vk.caption(vk.frame(sc, step), step, cap, ease(s / 0.35))

    vk.scene(dur(i, base), fn)


# 1. Upload
screen_scene(8, 5.5, 1, 'Click Upload and pick your video', {'home': HOME, 'menu': HOME_MENU},
             [(0, 'home', None), (0.3, 'home', (650, 290, 1700, 640))],
             clicks=[(2.0, 'home', UPLOAD), (4.0, 'home', DEVICE)], swaps=[(2.1, 'home', 'menu')],
             outlines=[(2.6, 9.0, 'home', (628, 300, 990, 500))], max_up=1.5, pad=0.15)

# 2. transcript with timestamps
TS1, TS2 = (408, 230, 494, 256), (408, 398, 494, 424)
screen_scene(9, 4.0, 2, 'Your speech as text, with timestamps', {'res': RESULT},
             [(0, 'res', None), (0.3, 'res', (395, 40, 1400, 620))],
             outlines=[(1.3, 9.0, 'res', TS1), (1.8, 9.0, 'res', TS2)], max_up=1.4, pad=0.08)

# 3. edit: fix names
PENCIL = (409, 127, 457, 176)
screen_scene(10, 4.5, 3, 'Fix names and keywords with Edit', {'res': RESULT},
             [(0, 'res', (395, 40, 1400, 620)), (0.6, 'res', (395, 40, 1100, 420))],
             clicks=[(2.2, 'res', PENCIL)], outlines=[(1.6, 9.0, 'res', PENCIL)],
             badges=[(2.6, 9.0, 'res', PENCIL, 'Edit', 0, -40, DARK)], max_up=1.6, pad=0.1)

# 4. Download -> .srt
DLBTN, SRT = (1180, 126, 1228, 174), (978, 352, 1055, 392)
screen_scene(11, 4.2, 4, 'Click Download, then pick .srt', {'res': RESULT, 'dl': DLMENU},
             [(0, 'res', (395, 40, 1400, 620)), (0.3, 'res', (900, 90, 1400, 460))],
             clicks=[(1.5, 'res', DLBTN), (3.0, 'res', SRT)], swaps=[(1.6, 'res', 'dl')],
             outlines=[(2.4, 9.0, 'res', SRT)], max_up=1.6, pad=0.12)

# 5a. YouTube Studio: title + description set, click Subtitles
TITLE, DESC, SUBS = (447, 222, 1580, 348), (447, 390, 1580, 1126), (30, 790, 260, 845)
screen_scene(12, 5.0, 5, 'In YouTube Studio, click Subtitles', {'st': STUDIO},
             [(0, 'st', None)],
             clicks=[(4.2, 'st', SUBS)],
             outlines=[(1.2, 3.6, 'st', TITLE), (2.0, 3.6, 'st', DESC), (3.4, 9.0, 'st', SUBS)],
             badges=[(1.4, 3.6, 'st', TITLE, '✓ Title', 420, 30, GREEN), (2.2, 3.6, 'st', DESC, '✓ Description', 420, 30, GREEN)],
             max_up=1.2)


# 5b. the upload flow inside Studio (Add language -> Upload file -> With timing -> choose .srt)
FLOW = ['Add language', 'Upload file', 'With timing', 'Choose your .srt']
STUDIO_DIM = None


def s_flow(t, s):
    global STUDIO_DIM
    if STUDIO_DIM is None:
        p, _ = vk.pad16x9(STUDIO)
        sc = vk.render(p, vk.full(p)).filter(ImageFilter.GaussianBlur(int(10 * U)))
        STUDIO_DIM = Image.blend(sc, Image.new('RGB', sc.size, BG), 0.55)
    sc = STUDIO_DIM.copy()
    d = ImageDraw.Draw(sc, 'RGBA')
    vk.text(sc, (SW / 2, 240 * U), 'YouTube Studio  ›  Subtitles', 40 * U, DARK, fade(s, 0.1), anchor='mm')
    fs, gap = 34 * U, 64 * U
    while True:                                   # shrink until the 4 chips fit the screen width
        f = vk.font(fs, True)
        widths = [d.textlength(x, font=f) + 2.2 * fs for x in FLOW]
        if sum(widths) + gap * 3 <= SW - 160 * U:
            break
        fs -= 1
    x = (SW - (sum(widths) + gap * 3)) / 2
    y = SH / 2
    for k, (txt, w) in enumerate(zip(FLOW, widths)):
        a = fade(s, 0.6 + k * 0.9, 0.35)
        hot = k == 2
        y0 = y + 14 * U * (1 - a)
        d.rounded_rectangle((x, y0 - 44 * U, x + w, y0 + 44 * U), int(44 * U),
                            fill=(ACCENT if hot else DARK) + (int(245 * a),))
        d.text((x + w / 2, y0), txt, font=f, fill=(255, 255, 255, int(255 * a)), anchor='mm')
        if k < 3:
            aa = fade(s, 1.2 + k * 0.9, 0.3)
            ax = x + w + gap / 2
            d.polygon([(ax - 12 * U, y - 16 * U), (ax + 12 * U, y), (ax - 12 * U, y + 16 * U)], fill=GREY + (int(255 * aa),))
        x += w + gap
    vk.text(sc, (SW / 2, SH / 2 + 130 * U), '"With timing": your .srt already has the timestamps', 28 * U, GREY,
            fade(s, 3.4), bold=False, anchor='mm')
    return vk.caption(vk.frame(sc, 5), 5, 'Upload file  ›  With timing  ›  your .srt', ease(s / 0.35))


vk.scene(dur(13, 5.0), s_flow)

# 5c. subtitles editor: lines matched, click Done
CUES, PREVIEW, DONE = (535, 325, 1250, 712), (1468, 505, 1893, 543), (1866, 103, 1972, 160)
screen_scene(14, 4.5, 5, 'Subtitles synced. Click Done, then publish', {'ed': EDITOR},
             [(0, 'ed', None)],
             clicks=[(3.4, 'ed', DONE)],
             outlines=[(0.6, 9.0, 'ed', CUES), (1.4, 9.0, 'ed', PREVIEW), (2.8, 9.0, 'ed', DONE)],
             badges=[(1.6, 9.0, 'ed', PREVIEW, 'Shows on your video', 0, -40, DARK)], max_up=1.2)


# ---------- outro: every box ticked ----------
def s_outro(t, s):
    img = vk.glow_bg((0.05, 0.1, 0.55, 0.9), 65).copy()
    brand(img, 1)
    checklist(img, 150 * U, 160 * U, s, [0, 0, 0, 0], 1.0, done_all=s > 1.2)
    xr = W / 2 + 340 * U
    a = fade(s, 1.6)
    vk.paste_fade(img, LOGO_BIG, (xr - LOGO_BIG.width / 2, 230 * U), a)
    vk.text(img, (xr, 380 * U), 'Now every box is ticked', 52 * U, DARK, a, anchor='mm')
    vk.text(img, (xr, 445 * U), 'Get your .srt free, then upload it with your video.', 28 * U, GREY, fade(s, 2.0), bold=False, anchor='mm')
    a3 = fade(s, 2.6)
    p = 1 + 0.025 * max(0.0, math.sin((s - 3.0) * 5)) if s > 3.0 else 1
    bw, bh = 460 * U * p, 76 * U * p
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle((xr - bw / 2, 560 * U - bh / 2, xr + bw / 2, 560 * U + bh / 2), int(bh / 2), fill=ACCENT + (int(255 * a3),))
    vk.text(img, (xr, 560 * U), 'transcriptx.ai', 38 * U, (255, 255, 255), a3, anchor='mm')
    return img


vk.scene(dur(15, 5.0), s_outro)


def add_voice(mp4, xfade=0.35, gain_db=3, music_db=-5):
    """Mux voice-over + soft ducked music bed under the silent render (same as build_video_chatgpt_mcp.py)."""
    import subprocess, tempfile, imageio_ffmpeg, gen_soft_music
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    XF, t, starts = round(xfade * vk.FPS), 0, []
    for n, _ in vk.scenes:
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
    if len(sys.argv) > 1 and sys.argv[1] == 'stills':
        for k, (n, fn) in enumerate(vk.scenes):
            for frac in (0.5, 0.97):
                fn(frac, frac * n / vk.FPS).resize((1280, 720), Image.LANCZOS).save(f'{SCRATCH}/seo_st{k:02d}_{int(frac * 100)}.png')
        print('stills', len(vk.scenes))
    else:
        vk.export(OUT, BASE, poster_at=3.0, preview_sheet=SHEET)
        add_voice(f'{OUT}/video/{BASE}.mp4')
        aw = f'{OUT}/{BASE}.webp'
        if os.path.exists(aw):
            os.remove(aw)
