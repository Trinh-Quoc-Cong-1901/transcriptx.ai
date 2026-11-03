"""Host version of the can-chatgpt-watch-videos walkthrough: same steps and voice-over, plus a cartoon presenter.

Reuses scenes 1-6 and the voice-over from build_video_chatgpt_mcp.py (that file and its video stay untouched):
- new dark intro + outro templates with the presenter large and waving,
- a round facecam with the presenter lip-syncing to the voice-over on every walkthrough step (presenter.py).
Output: can-chatgpt-watch-videos-transcriptx-mcp-host.mp4 (+ poster) next to the original video.
"""
import math, os
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg

import video_hq as vk
from video_hq import W, H, U, DARK, ACCENT, ease
import build_video_chatgpt_mcp as base
import presenter

BASE = 'can-chatgpt-watch-videos-transcriptx-mcp-host' + os.environ.get('VO_SUFFIX', '')
MUSIC_DB = float(os.environ.get('MUSIC_DB', '-5'))
SHEET = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/6805d401-fdc8-4e4f-831f-aba74e6ebdff/scratchpad/host_sheet.png'
LIP = presenter.Lipsync([f for f, _ in base.VO], imageio_ffmpeg.get_ffmpeg_exe(), vk.FPS)
WHITE, SOFT = (255, 255, 255), (196, 190, 180)
INK = (30, 29, 27)


def mouth(k, s):
    return LIP.at(k, s - base.VO_LINES[k][0])


# ---------- dark template (intro + outro) ----------

def _dark_bg():
    img = Image.new('RGBA', (W, H), INK + (255,))
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    gd.ellipse((-0.12 * W, 0.18 * H, 0.52 * W, 1.3 * H), fill=ACCENT + (120,))
    gd.ellipse((0.62 * W, -0.35 * H, 1.15 * W, 0.45 * H), fill=(90, 70, 160, 60))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(int(140 * U))))
    d = ImageDraw.Draw(img, 'RGBA')
    step = int(34 * U)
    for y in range(step // 2, H, step):                     # faint dot grid
        for x in range(step // 2, W, step):
            d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, 14))
    return img


DARK_BG = _dark_bg()
STAGE_C, STAGE_R = (int(330 * U), int(560 * U)), int(270 * U)


def _stage():
    """Accent disc the presenter stands in, with a soft white rim."""
    img = DARK_BG.copy()
    d = ImageDraw.Draw(img, 'RGBA')
    cx, cy = STAGE_C
    r = STAGE_R
    d.ellipse((cx - r - 10 * U, cy - r - 10 * U, cx + r + 10 * U, cy + r + 10 * U), fill=(255, 255, 255, 30))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ACCENT + (255,))
    d.ellipse((cx - r * 0.82, cy - r * 0.82, cx + r * 0.82, cy + r * 0.82), outline=(255, 255, 255, 40), width=int(3 * U))
    return img


STAGE_BG = _stage().convert('RGB')
HOST_SIZE = int(560 * U)


def host(img, mouth_amt, s, a=1.0, wave=True):
    """Presenter standing in the stage disc; the bottom of the shirt runs off the frame."""
    spr = presenter.sprite(HOST_SIZE, mouth_amt, s, wave_t=s if wave else None, look=1)
    rise = 60 * U * (1 - a)
    bob = 6 * U * math.sin(s * 2.0) + 8 * U * mouth_amt
    x = STAGE_C[0] - HOST_SIZE / 2
    y = H - HOST_SIZE * 0.86 + rise + bob
    return vk.paste_fade(img, spr, (x, y), a)


def pill(img, xy, txt, size, a, fill, color=WHITE, logo=None, pad=26):
    if a <= 0:
        return 0
    f = vk.font(size, True)
    d = ImageDraw.Draw(img, 'RGBA')
    tw = d.textlength(txt, font=f)
    lw = logo.width + 14 * U if logo else 0
    h = size * 1.9
    x, y = xy
    w = tw + lw + pad * U * 2
    d.rounded_rectangle((x, y - h / 2, x + w, y + h / 2), int(h / 2), fill=fill + (int(255 * a),))
    if logo:
        vk.paste_fade(img, logo, (x + pad * U, y - logo.height / 2), a)
    d.text((x + pad * U + lw, y), txt, font=f, fill=color + (int(255 * a),), anchor='lm')
    return w


LOGO_S = base.bv.logo.resize((int(34 * U), int(34 * U)), Image.LANCZOS)
LOGO_S.putalpha(LOGO_S.convert('L').point(lambda v: 0 if v > 235 else 255))
WIN, WG = vk.window(base.NOLINK.crop((690, 105, 1780, 720)), int(980 * U / 1.8))
NOREAD = base.NOREAD
X0 = int(690 * U)


def intro(t, s):
    img = STAGE_BG.copy()
    fade = lambda st, d=0.45: ease((s - st) / d)
    host(img, mouth(0, s), s, fade(0, 0.6))
    pill(img, (X0, 120 * U), 'TranscriptX  ·  Quick guide', 22 * U, fade(0.1), (255, 255, 255), color=DARK, logo=LOGO_S)
    for k, (txt, col, st) in enumerate([('Can ChatGPT', WHITE, 0.25), ('watch videos?', ACCENT, 0.5)]):
        a = fade(st)
        vk.text(img, (X0 - 4, 225 * U + k * 82 * U + 24 * U * (1 - a)), txt, 72 * U, col, a)
    aw = fade(1.0, 0.7)
    wx, wy = X0 - WG, 360 * U + 80 * U * (1 - aw)
    vk.paste_fade(img, WIN, (wx, wy), aw)
    k = (WIN.width - 2 * WG) / 1090
    nb = (wx + WG + (NOREAD[0] - 690) * k, wy + WG + (NOREAD[1] - 105) * k,
          wx + WG + (NOREAD[2] - 690) * k, wy + WG + (NOREAD[3] - 105) * k)
    vk.outline(img, nb, fade(1.9, 0.3), pad=6)
    vk.badge(img, (wx + WIN.width / 2, wy + WIN.height - 4 * U), "ChatGPT can't read the link", fade(2.1, 0.3), color=ACCENT)
    return img


CHECKS = ['Works in ChatGPT and Claude', 'Full transcript with timestamps', 'Free every day, no account needed to try']


def outro(t, s):
    img = STAGE_BG.copy()
    fade = lambda st, d=0.4: ease((s - st) / d)
    host(img, mouth(7, s), s)
    pill(img, (X0, 150 * U), 'TranscriptX', 22 * U, fade(0), (255, 255, 255), color=DARK, logo=LOGO_S)
    for k, (txt, col) in enumerate([('Let ChatGPT and Claude', WHITE), ('read any video', ACCENT)]):
        a = fade(0.1 + k * 0.15)
        vk.text(img, (X0 - 4, 255 * U + k * 70 * U + 20 * U * (1 - a)), txt, 58 * U, col, a)
    d = ImageDraw.Draw(img, 'RGBA')
    for k, txt in enumerate(CHECKS):
        a = fade(0.6 + k * 0.2)
        y = 435 * U + k * 54 * U
        if a > 0:
            d.ellipse((X0, y - 17 * U, X0 + 34 * U, y + 17 * U), fill=ACCENT + (int(255 * a),))
            vk._check(d, X0 + 17 * U, y, 15 * U, (255, 255, 255, int(255 * a)), max(3, int(3.4 * U)))
        vk.text(img, (X0 + 52 * U, y), txt, 30 * U, SOFT, a, bold=False)
    a3 = fade(1.3)
    p = 1 + 0.03 * max(0.0, math.sin((s - 1.7) * 5)) if s > 1.7 else 1
    pw = pill(Image.new('RGBA', (1, 1)), (0, 0), 'transcriptx.ai/transcription-mcp', 32 * U, 1, ACCENT)
    if a3 > 0:
        bw, bh = pw * p, 32 * U * 1.9 * p
        cx, cy = X0 + pw / 2, 650 * U
        d.rounded_rectangle((cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2), int(bh / 2), fill=WHITE + (int(255 * a3),))
        vk.text(img, (cx, cy), 'transcriptx.ai/transcription-mcp', 32 * U, ACCENT, a3, anchor='mm')
    return img


# ---------- facecam on the walkthrough steps ----------
CAM_D = int(176 * U)
CAM_C = (W - 34 * U - CAM_D / 2, H - 178 * U - CAM_D / 2)


def with_cam(fn, k, fade_in=False):
    def g(t, s):
        img = fn(t, s)
        a = ease((s - 0.1) / 0.45) if fade_in else 1.0
        return presenter.bubble(img, CAM_C, CAM_D, mouth(k, s), s, a=a, look=-1)
    return g


scenes = vk.scenes
assert len(scenes) == 8, len(scenes)
scenes[0] = (scenes[0][0], intro)
for k in range(1, 7):
    scenes[k] = (scenes[k][0], with_cam(scenes[k][1], k, fade_in=(k == 1)))
scenes[7] = (max(scenes[7][0], round(4.6 * vk.FPS)), outro)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'stills':
        d = os.path.dirname(SHEET)
        for k, (n, fn) in enumerate(vk.scenes):
            for frac in (0.5, 0.95):
                fn(frac, frac * n / vk.FPS).convert('RGB').save(f'{d}/host_st{k}_{int(frac * 100)}.png')
    else:
        vk.export(base.OUT, BASE, poster_at=3.0, preview_sheet=SHEET)
        base.add_voice(f'{base.OUT}/video/{BASE}.mp4', music_db=MUSIC_DB)
        aw = f'{base.OUT}/{BASE}.webp'
        if os.path.exists(aw):
            os.remove(aw)
