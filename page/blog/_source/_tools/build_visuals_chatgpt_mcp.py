"""Static images + YouTube thumbnail for can-chatgpt-watch-videos (TranscriptX screens only in the article).

Article: transcript page (Copy), Transcription MCP page (Add to ChatGPT / Add to Claude), the TranscriptX permission
screen (email blurred). Thumbnail: headline + the real "Transcribe this video" prompt and the two Add buttons.
"""
import importlib.util, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)
OUT = os.path.abspath(f'{HERE}/../../can-chatgpt-watch-videos/images')
SCRATCH = '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/57a5198f-d025-4ecd-adfc-f019bf34083a/scratchpad'
hl = bv.highlight
os.makedirs(f'{OUT}/video', exist_ok=True)


def load(p):
    return Image.open(f'{bv.SRC}/{p}').convert('RGB')


def save(img, name):
    """Native pixels (no resize), lossless; lossy q95 only if the file passes ~900 KB."""
    path = f'{OUT}/{name}'
    img = img.convert('RGB')
    img.save(path, 'WEBP', lossless=True, quality=100, method=6)
    if os.path.getsize(path) > 900 * 1024:
        img.save(path, 'WEBP', quality=95, method=6)
    print(name, img.size, os.path.getsize(path) // 1024, 'KB')


# 1. transcript page, Copy button (same capture and box as the summarize post)
app = load('transcript/transcript-notes-tab.png')
save(hl(app.crop((436, 0, 2000, 760)), (1212 - 436, 160, 1385 - 436, 222), pad=8), 'copy-youtube-transcript-for-chatgpt.webp')

# 2. Transcription MCP page: both Add buttons
mcp = load('chatgpt-claude/transcription-mcp-page.png').crop((560, 120, 1790, 1160))
mcp = hl(mcp, (629 - 560, 711 - 120, 1131 - 560, 770 - 120), pad=8)
mcp = hl(mcp, (1221 - 560, 711 - 120, 1723 - 560, 770 - 120), pad=8)
save(mcp, 'transcription-mcp-add-to-chatgpt-claude.webp')

# 3. TranscriptX permission screen (email already blurred in the source)
allow = load('chatgpt-claude/chatgpt-transcriptx-allow-access.png').crop((660, 120, 1340, 1150))
save(hl(allow, (739 - 660, 819 - 120, 1261 - 660, 878 - 120), pad=8), 'chatgpt-transcriptx-allow-access.webp')

# ---------- thumbnail 2560x1440 ----------
S = 2
TW, TH = 1280 * S, 720 * S
BG, DARK, ACCENT, font = bv.BG, bv.DARK, bv.ACCENT, bv.font
img = Image.new('RGBA', (TW, TH), BG + (255,))
glow = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((560 * S, -40 * S, 1400 * S, 800 * S), fill=(236, 160, 115, 110))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110 * S)))


def card(src, box, k, x, y):
    c = src.crop(box)
    c = c.resize((round(c.width * k), round(c.height * k)), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', c.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, c.width - 1, c.height - 1), 18 * S, fill=255)
    c.putalpha(m)
    sh = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x, y + 16 * S, x + c.width, y + c.height + 16 * S), 18 * S, fill=(60, 35, 15, 100))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24 * S)))
    img.alpha_composite(c, (int(x), int(y)))
    return c.size


prompt = load('chatgpt-claude/chatgpt-transcriptx-transcribe-prompt.png')
pw, ph = card(prompt, (712, 540, 1752, 700), 1.3, TW - 1352 - 50 * S, 370 * S)
card(btns := load('chatgpt-claude/transcription-mcp-page.png'), (600, 690, 1752, 790), 1.15, TW - 1325 - 60 * S, 370 * S + ph + 50 * S)

d = ImageDraw.Draw(img)
d.text((52 * S, 150 * S), 'Can ChatGPT', font=font(92 * S, True), fill=DARK + (255,), anchor='lm')
d.text((52 * S, 250 * S), 'watch videos?', font=font(92 * S, True), fill=ACCENT + (255,), anchor='lm')
tf = font(38 * S, True)
tw = d.textlength('Now it can read them', font=tf)
d.rounded_rectangle((56 * S, 372 * S, 56 * S + tw + 56 * S, 440 * S), 34 * S, fill=DARK + (255,))
d.text((84 * S, 406 * S), 'Now it can read them', font=tf, fill=(255, 255, 255, 255), anchor='lm')
lg = bv.logo.resize((46 * S, 46 * S), Image.LANCZOS)
lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(lg, (58 * S, 626 * S))
d.text((116 * S, 649 * S), 'TranscriptX.ai', font=font(32 * S, True), fill=DARK + (255,), anchor='lm')

out = f'{OUT}/video/can-chatgpt-watch-videos-transcriptx-mcp-thumbnail.jpg'
rgb = img.convert('RGB')
rgb.save(out, 'JPEG', quality=95, subsampling=0, optimize=True)
rgb.crop((TW - 1500, 230 * S, TW - 600, 230 * S + 700)).save(f'{SCRATCH}/thumb_100pct.png')
rgb.resize((320, 180), Image.LANCZOS).save(f'{SCRATCH}/thumb_small.png')
rgb.resize((1280, 720), Image.LANCZOS).save(f'{SCRATCH}/thumb_half.png')
print(out, os.path.getsize(out) // 1024, 'KB')
