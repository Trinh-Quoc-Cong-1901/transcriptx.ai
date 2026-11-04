"""Blog cover / social share image for how-to-transcribe-podcast.
Renders natively at 2400x1260 (2x of the 1200x630 OG size) and also exports a 1200x630 JPG for og:image."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(f'{HERE}/..')
OUT = os.path.normpath(f'{HERE}/../../how-to-transcribe-podcast/images')
CHECK = sys.argv[1] if len(sys.argv) > 1 else None
FONT = '/System/Library/Fonts/HelveticaNeue.ttc'
BG, DARK, ACCENT = (248, 247, 244), (43, 42, 38), (204, 88, 46)
W, H = 2400, 1260

def font(size, bold=False):
    return ImageFont.truetype(FONT, size, index=1 if bold else 0)

img = Image.new('RGBA', (W, H), BG + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((1150, -250, 2750, 1450), fill=(236, 160, 115, 120))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(170)))

# ---- real TranscriptX result: title, toolbar with Download menu open, timed paragraphs (native retina pixels)
shot = Image.open(f'{SRC}/transcript/transcript-download-menu-open.png').convert('RGB')
shot = shot.crop((380, 30, 1410, 640))           # 1030 x 610
win = shot.convert('RGBA')
m = Image.new('L', win.size, 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, win.width - 1, win.height - 1), 28, fill=255)
win.putalpha(m)
wx, wy = W - win.width - 110, 300
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((wx, wy + 30, wx + win.width, wy + win.height + 30), 28, fill=(70, 40, 20, 120))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(40)))
img.alpha_composite(win, (wx, wy))
d = ImageDraw.Draw(img)
# orange outline on the Download menu (shot coords: menu ~ 960-1228 x 185-448 in source → minus crop offset)
mx0, my0, mx1, my1 = wx + 960 - 380 - 10, wy + 184 - 30 - 10, wx + 1228 - 380 + 10, wy + 448 - 30 + 10
d.rounded_rectangle((mx0, my0, mx1, my1), 26, outline=ACCENT + (255,), width=7)

# ---- podcast file card (audio in) overlapping the screenshot bottom-left
cx, cy, cw, ch = wx - 150, wy + win.height - 150, 640, 230
sh2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh2).rounded_rectangle((cx, cy + 22, cx + cw, cy + ch + 22), 36, fill=(70, 40, 20, 110))
img.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(30)))
d = ImageDraw.Draw(img)
d.rounded_rectangle((cx, cy, cx + cw, cy + ch), 36, fill=(255, 255, 255, 255))
# mic icon in accent circle
ic = (cx + 40, cy + 40, cx + 150, cy + 150)
d.ellipse(ic, fill=ACCENT + (255,))
mcx, mcy = (ic[0] + ic[2]) // 2, (ic[1] + ic[3]) // 2
d.rounded_rectangle((mcx - 16, mcy - 36, mcx + 16, mcy + 10), 16, fill=(255, 255, 255, 255))
d.arc((mcx - 30, mcy - 22, mcx + 30, mcy + 26), 0, 180, fill=(255, 255, 255, 255), width=7)
d.line((mcx, mcy + 26, mcx, mcy + 40), fill=(255, 255, 255, 255), width=7)
d.text((cx + 180, cy + 72), 'episode-42.mp3', font=font(46, True), fill=DARK + (255,), anchor='lm')
d.text((cx + 180, cy + 124), '58:14', font=font(38), fill=(130, 126, 118, 255), anchor='lm')
# waveform
bx, by = cx + 44, cy + 196
for i in range(46):
    h = 10 + 26 * abs(math.sin(i * 0.55) * math.cos(i * 0.21)) + (8 if i % 5 == 0 else 0)
    x = bx + i * 12
    col = ACCENT if i < 20 else (214, 205, 192)
    d.rounded_rectangle((x, by - h / 2, x + 6, by + h / 2), 3, fill=col + (255,))

# ---- left: badge, headline, sub, chips, logo
d.rounded_rectangle((110, 150, 520, 250), 50, fill=DARK + (255,))
mx, my = 172, 200
d.rounded_rectangle((mx - 13, my - 30, mx + 13, my + 8), 13, fill=(255, 255, 255, 255))
d.arc((mx - 24, my - 18, mx + 24, my + 20), 0, 180, fill=(255, 255, 255, 255), width=6)
d.line((mx, my + 20, mx, my + 32), fill=(255, 255, 255, 255), width=6)
d.text((218, 200), 'PODCAST', font=font(54, True), fill=(255, 255, 255, 255), anchor='lm')
d.text((100, 410), 'Podcast', font=font(210, True), fill=DARK + (255,), anchor='lm')
d.text((100, 620), 'to text', font=font(210, True), fill=ACCENT + (255,), anchor='lm')
d.text((110, 790), 'Get a transcript of any episode', font=font(62), fill=(80, 77, 70, 255), anchor='lm')
x = 110
for lbl in ['.docx', '.pdf', '.srt', '.txt']:
    tw = d.textlength(lbl, font=font(54, True))
    d.rounded_rectangle((x, 880, x + tw + 64, 976), 48, fill=(255, 255, 255, 255), outline=(225, 216, 204, 255), width=3)
    d.text((x + 32 + tw / 2, 928), lbl, font=font(54, True), fill=ACCENT + (255,), anchor='mm')
    x += tw + 64 + 22
lg = Image.open(f'{SRC}/brand/logo/logo_256.png').convert('RGBA').resize((84, 84), Image.LANCZOS)
lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(lg, (108, 1086))
d.text((214, 1128), 'TranscriptX.ai', font=font(60, True), fill=DARK + (255,), anchor='lm')

os.makedirs(OUT, exist_ok=True)
rgb = img.convert('RGB')
cover = f'{OUT}/how-to-transcribe-podcast-cover.webp'
rgb.save(cover, 'WEBP', quality=95, method=6)
og = f'{OUT}/how-to-transcribe-podcast-og-1200x630.jpg'
rgb.resize((1200, 630), Image.LANCZOS).save(og, 'JPEG', quality=92, subsampling=0, optimize=True)
if CHECK:
    rgb.crop((wx, wy, wx + 1000, wy + 600)).save(f'{CHECK}/cover_100pct.png')
    rgb.resize((480, 252), Image.LANCZOS).save(f'{CHECK}/cover_small.png')
for f in (cover, og):
    print(f, os.path.getsize(f) // 1024, 'KB')
