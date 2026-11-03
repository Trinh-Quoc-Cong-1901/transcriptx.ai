"""YouTube-quality walkthrough (2560x1440, 60 fps) with English voice-over, for can-chatgpt-watch-videos.

Real 2026-10-29 captures in chatgpt-claude/ (retina 2000px, the result screen is 1x 1372px):
hook (ChatGPT can't read the link) -> 1 Add to ChatGPT on /transcription-mcp/ -> 2 Install plugin -> 3 Allow
(email blurred) -> 4 "Transcribe this video: <link>" -> 5 transcript in the chat -> Claude -> CTA.
Voice-over: edge-tts en-US-AvaNeural (+4%), one line per scene, over a soft ducked music bed (gen_soft_music.py).
"""
import math, os
from PIL import Image, ImageDraw

import video_hq as vk
from video_hq import W, H, U, SW, SH, BG, DARK, ACCENT, GREY, ease, lerp

bv = vk.bv
SRC = f'{bv.SRC}/chatgpt-claude'
OUT = os.path.abspath(f'{vk.HERE}/../../can-chatgpt-watch-videos/images')
BASE = 'can-chatgpt-watch-videos-transcriptx-mcp'
SHEET = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/57a5198f-d025-4ecd-adfc-f019bf34083a/scratchpad/mcp_sheet.png'
vk.STEPS[:] = ['Add to ChatGPT', 'Install', 'Allow', 'Ask', 'Transcript']

# ---------- voice-over (one line per scene; scenes stretch to fit their line) ----------
VOICE = os.environ.get('VO_VOICE', 'en-US-AvaNeural')
RATE = os.environ.get('VO_RATE', '+4%')
EDGE_TTS = os.environ.get('EDGE_TTS', 'edge-tts')
VO_LINES = [
    (0.3, "Can ChatGPT watch YouTube videos? Paste a link, and it can't read a word that's said in it."),
    (0.3, 'Here is the fix. Open the TranscriptX Transcription MCP page, and click Add to ChatGPT.'),
    (0.3, 'ChatGPT opens the TranscriptX plugin. Click Install plugin.'),
    (0.3, 'Click Allow to sign in, or continue as a guest. No account needed.'),
    (0.3, 'Now pick TranscriptX, type: transcribe this video, and paste your link.'),
    (0.3, 'In seconds, the full transcript is right in the chat, with timestamps, ready to copy or export.'),
    (0.3, 'Using Claude? Click Add to Claude, and it works the same way.'),
    (0.3, 'Add TranscriptX to ChatGPT or Claude, free, at transcriptx dot A I.'),
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


def load(name):
    return Image.open(f'{SRC}/{name}.png').convert('RGB')


NOLINK = load('chatgpt-youtube-link-no-transcript')
MCP = load('transcription-mcp-page')
PLUGIN = load('chatgpt-transcriptx-plugin-install')
ALLOW = load('chatgpt-transcriptx-allow-access')
PROMPT = load('chatgpt-transcriptx-transcribe-prompt')
RESULT = load('chatgpt-transcriptx-transcript-result')


def centre(b):
    return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)


def click_scene(img, zoom_box, btn, step, cap, i, base, max_up=1.3, pad=0.35, extra=None, click_at=1.6):
    """Zoom from the full screen to zoom_box, move the cursor onto btn and click it."""
    padded, off = vk.pad16x9(img)
    sh = lambda b: bv.shift(b, off)
    b = sh(btn)
    f0 = vk.full(padded)
    z = vk.view(sh(zoom_box), padded.size, pad=pad, max_up=max_up)
    c = centre(b)

    def fn(t, s):
        rect = lerp(f0, z, ease((s - 0.2) / 1.1))
        sc = vk.render(padded, rect)
        cpos, k = vk.to_s(c, rect)
        bb = vk.box_s(b, rect)
        click = (s - click_at) / 0.45
        vk.outline(sc, bb, ease((s - (click_at - 0.35)) / 0.3), pad=5)
        vk.ring(sc, cpos, click, max(1.0, k))
        vk.cursor(sc, vk.path((SW * 0.5, SH * 0.85), (cpos[0] + 8, cpos[1] + 8), (s - 0.5) / 1.0), vk.press(click))
        if extra:
            extra(sc, rect, s, sh)
        return vk.caption(vk.frame(sc, step), step, cap, ease(s / 0.35))

    vk.scene(dur(i, base), fn)


# ---------- hook: ChatGPT can't read the link ----------
WIN, WG = vk.window(NOLINK.crop((690, 105, 1780, 720)), int(1240 * U / 1.8))
LOGO = bv.logo.resize((int(52 * U), int(52 * U)), Image.LANCZOS)
LOGO.putalpha(LOGO.convert('L').point(lambda v: 0 if v > 235 else 255))
NOREAD = (700, 270, 1690, 310)            # "...couldn't retrieve its actual content from the link."


def intro(t, s):
    img = vk.glow_bg().copy()
    fade = lambda st, d=0.45: ease((s - st) / d)
    x0 = int(110 * U)
    vk.paste_fade(img, LOGO, (x0, int(150 * U)), fade(0))
    vk.text(img, (x0 + 66 * U, 176 * U), 'TranscriptX', 34 * U, DARK, fade(0))
    for k, (txt, col, st) in enumerate([('Can ChatGPT', DARK, 0.2), ('watch videos?', ACCENT, 0.45)]):
        a = fade(st)
        vk.text(img, (x0 - 4, 310 * U + k * 86 * U + 26 * U * (1 - a)), txt, 70 * U, col, a)
    a = fade(2.2)
    vk.text(img, (x0, 520 * U), "Not on its own. It can't hear the video.", 30 * U, GREY, a, bold=False)
    vk.text(img, (x0, 562 * U), 'Add TranscriptX and it reads every word.', 30 * U, GREY, a, bold=False)
    aw = fade(0.3, 0.9)
    wx, wy = W - WIN.width - 30 * U, 120 * U + 120 * U * (1 - aw)
    vk.paste_fade(img, WIN, (wx, wy), aw)
    k = (WIN.width - 2 * WG) / 1090
    nb = (wx + WG + (NOREAD[0] - 690) * k, wy + WG + (NOREAD[1] - 105) * k,
          wx + WG + (NOREAD[2] - 690) * k, wy + WG + (NOREAD[3] - 105) * k)
    vk.outline(img, nb, fade(1.4, 0.3), pad=6)
    vk.badge(img, (wx + WIN.width / 2, wy + WIN.height + 20 * U), "ChatGPT can't read the link", fade(1.6, 0.3), color=DARK)
    return img


vk.scene(dur(0, 4.2), intro)

# ---------- 1. Add to ChatGPT on the Transcription MCP page ----------
ADD_GPT = (629, 711, 1131, 770)
ADD_CLAUDE = (1221, 711, 1723, 770)
click_scene(MCP, (596, 557, 1164, 1147), ADD_GPT, 1, 'On transcriptx.ai/transcription-mcp, click Add to ChatGPT', 1, 3.6,
            pad=0.12)

# ---------- 2. Install plugin ----------
INSTALL = (1539, 118, 1722, 166)
click_scene(PLUGIN, (742, 100, 1722, 530), INSTALL, 2, 'ChatGPT opens the TranscriptX plugin: click Install plugin', 2, 3.4,
            pad=0.1)

# ---------- 3. Allow (or continue as guest) ----------
ALLOW_BTN = (739, 819, 1261, 878)
GUEST = (920, 900, 1080, 932)


def guest_badge(sc, rect, s, sh):
    g = vk.box_s(sh(GUEST), rect)
    vk.badge(sc, (g[2] + 290 * U, (g[1] + g[3]) / 2), 'or Continue as guest', ease((s - 2.2) / 0.3), color=DARK)


click_scene(ALLOW, (700, 145, 1300, 1060), ALLOW_BTN, 3, 'Click Allow, or continue as a guest', 3, 3.6, pad=0.04,
            extra=guest_badge)

# ---------- 4. Ask: "Transcribe this video: <link>" ----------
PROMPT_BOX = (708, 535, 1755, 707)
SEND = (1696, 649, 1742, 695)
PROMPT_IN = (730, 556, 1735, 626)
IN_BG = PROMPT.getpixel((1300, 650))


def typed(frac):
    """Prompt line revealed left to right (the real typed text, uncovered progressively)."""
    img = PROMPT.copy()
    if frac < 1:
        d = ImageDraw.Draw(img)
        x0, y0, x1, y1 = PROMPT_IN
        # two lines: reveal line 1 then line 2
        split = 0.75
        if frac < split:
            cut = x0 + (x1 - x0) * frac / split
            d.rectangle((cut, y0, x1, y0 + 34), fill=IN_BG)
            d.rectangle((x0, y0 + 35, x1, y1), fill=IN_BG)
        else:
            cut = x0 + (300) * (frac - split) / (1 - split)
            d.rectangle((cut, y0 + 35, x1, y1), fill=IN_BG)
    return img


padded4, off4 = vk.pad16x9(PROMPT)
f4 = vk.full(padded4)
z4 = vk.view(bv.shift(PROMPT_BOX, off4), padded4.size, pad=0.08, max_up=1.3)


def s4(t, s):
    rect = lerp(f4, z4, ease((s - 0.1) / 0.9))
    frac = max(0.0, min(1.0, (s - 0.9) / 1.8))
    pimg, _ = vk.pad16x9(typed(frac))
    sc = vk.render(pimg, rect)
    vk.outline(sc, vk.box_s(bv.shift(PROMPT_IN, off4), rect), ease((s - 0.5) / 0.3) * (1 - ease((s - 2.9) / 0.3)), pad=4)
    c, k = vk.to_s(centre(bv.shift(SEND, off4)), rect)
    click = (s - 3.3) / 0.45
    vk.ring(sc, c, click, max(1.0, k))
    vk.cursor(sc, vk.path((SW * 0.45, SH * 0.82), (c[0] + 8, c[1] + 8), (s - 2.4) / 0.8), vk.press(click))
    return vk.caption(vk.frame(sc, 4), 4, 'Pick TranscriptX, type "Transcribe this video:" and paste the link', ease(s / 0.35))


vk.scene(dur(4, 4.0), s4)

# ---------- 5. The transcript, right in the chat (1x capture: max_up 1.8) ----------
CARD = (486, 272, 1205, 750)
PROC = (486, 210, 600, 234)
EXPORT = (935, 368, 1025, 401)
COPY = (1037, 368, 1187, 401)
padded5, off5 = vk.pad16x9(RESULT)
f5 = vk.full(padded5)
z5 = vk.view(bv.shift((486, 80, 1205, 750), off5), padded5.size, pad=0.02, max_up=1.8)
zb = vk.view(bv.shift((486, 200, 1205, 420), off5), padded5.size, pad=0.06, max_up=1.8)


def s5(t, s):
    rect = lerp(f5, z5, ease(s / 1.0)) if s < 2.4 else lerp(z5, zb, ease((s - 2.4) / 0.9))
    sc = vk.render(padded5, rect)
    p = vk.box_s(bv.shift(PROC, off5), rect)
    vk.badge(sc, (p[2] + 170 * U, (p[1] + p[3]) / 2), '✓ Processed in 8 s', ease((s - 0.9) / 0.3) * (1 - ease((s - 2.3) / 0.3)))
    a = ease((s - 3.1) / 0.3)
    e, c = vk.box_s(bv.shift(EXPORT, off5), rect), vk.box_s(bv.shift(COPY, off5), rect)
    vk.outline(sc, e, a, pad=4)
    vk.outline(sc, c, a, pad=4)
    vk.badge(sc, ((e[0] + c[2]) / 2, e[1] - 75 * U), 'Export .txt .srt .vtt  ·  Copy transcript', ease((s - 3.3) / 0.3), color=DARK)
    return vk.caption(vk.frame(sc, 5), 5, 'The transcript, with timestamps, right in the chat', ease(s / 0.35))


vk.scene(dur(5, 5.0), s5)

# ---------- Claude ----------
padded6, off6 = vk.pad16x9(MCP)
z6 = vk.view(bv.shift((1188, 557, 1756, 1147), off6), padded6.size, pad=0.12, max_up=1.3)
z6a = vk.view(bv.shift((596, 557, 1164, 1147), off6), padded6.size, pad=0.12, max_up=1.3)


def s6(t, s):
    rect = lerp(z6a, z6, ease((s - 0.1) / 1.0))
    sc = vk.render(padded6, rect)
    b = vk.box_s(bv.shift(ADD_CLAUDE, off6), rect)
    c = centre(b)
    click = (s - 1.7) / 0.45
    vk.outline(sc, b, ease((s - 1.3) / 0.3), pad=5)
    vk.ring(sc, c, click, 1.3)
    vk.cursor(sc, vk.path((SW * 0.3, SH * 0.8), (c[0] + 8, c[1] + 8), (s - 0.6) / 1.0), vk.press(click))
    return vk.caption(vk.frame(sc, 6), None, 'Using Claude? Click Add to Claude', ease(s / 0.35))


vk.scene(dur(6, 3.4), s6)

# ---------- CTA ----------
LOGO_BIG = bv.logo.resize((int(84 * U), int(84 * U)), Image.LANCZOS)
LOGO_BIG.putalpha(LOGO_BIG.convert('L').point(lambda v: 0 if v > 235 else 255))


def outro(t, s):
    img = vk.glow_bg((0.27, 0.15, 0.73, 0.9), 60).copy()
    a = ease(s / 0.4)
    vk.paste_fade(img, LOGO_BIG, (W / 2 - LOGO_BIG.width / 2, 190 * U), a)
    vk.text(img, (W / 2, 340 * U), 'Let ChatGPT and Claude read any video', 54 * U, DARK, a, anchor='mm')
    vk.text(img, (W / 2, 408 * U), 'Free every day. No account needed to try.', 32 * U, GREY, ease((s - 0.3) / 0.4), bold=False, anchor='mm')
    a3 = ease((s - 0.6) / 0.4)
    p = 1 + 0.025 * max(0.0, math.sin((s - 1.0) * 5)) if s > 1.0 else 1
    bw, bh = 720 * U * p, 76 * U * p
    d = ImageDraw.Draw(img, 'RGBA')
    d.rounded_rectangle((W / 2 - bw / 2, 500 * U - bh / 2, W / 2 + bw / 2, 500 * U + bh / 2), int(bh / 2), fill=ACCENT + (int(255 * a3),))
    vk.text(img, (W / 2, 500 * U), 'transcriptx.ai/transcription-mcp', 34 * U, (255, 255, 255), a3, anchor='mm')
    return img


vk.scene(dur(7, 3.6), outro)


def add_voice(mp4, xfade=0.35, gain_db=3, music_db=-5):
    """Mux voice-over + soft ducked music bed under the silent render (same as build_video_summary_mind_map.py)."""
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
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'stills':          # one frame per scene, no encoding
        d = os.path.dirname(SHEET)
        for k, (n, fn) in enumerate(vk.scenes):
            for frac in (0.5, 0.95):
                fn(frac, frac * n / vk.FPS).save(f'{d}/mcp_st{k}_{int(frac * 100)}.png')
    else:
        vk.export(OUT, BASE, poster_at=3.0, preview_sheet=SHEET)
        add_voice(f'{OUT}/video/{BASE}.mp4')
        aw = f'{OUT}/{BASE}.webp'                                  # article images stay static
        if os.path.exists(aw):
            os.remove(aw)
