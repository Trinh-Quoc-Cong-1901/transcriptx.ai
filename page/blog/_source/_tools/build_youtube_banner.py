"""TranscriptX YouTube channel banner, 2560x1440 (PNG, lossless).

YouTube shows: TV = full 2560x1440, desktop = 2560x423 middle strip, mobile/all devices = 1546x423 safe area
(x 507-2053, y 508-931). Logo, headline, platforms and the wave->text graphic all sit inside the safe area;
the robot mascot sits just right of it (desktop/TV only), the rest is background for TV.
Copy comes from brand/brand-info.md and the Product Hunt cover ("Any video or audio. Text in seconds.").
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mascot import robot, vgrad

OUT = os.path.abspath(f'{HERE}/../brand/youtube-banner-2560x1440.png')
LOGO = os.path.abspath(f'{HERE}/../brand/logo/logo_512.png')
PREVIEW = sys.argv[1] if len(sys.argv) > 1 else None

W, H = 2560, 1440
SX0, SY0, SX1, SY1 = 507, 508, 2053, 931          # safe area (all devices)
AV = '/System/Library/Fonts/Avenir Next.ttc'
ORANGE = (226, 98, 50)
ORANGE_HI = (255, 150, 90)
WHITE = (255, 255, 255)
MUTED = (178, 170, 166)


def F(size, idx=8):
    return ImageFont.truetype(AV, size, index=idx)


# ---------- background ----------
img = vgrad((W, H), (22, 17, 16), (9, 8, 8)).convert('RGBA')
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((1500, 350, 2700, 1150), fill=(170, 66, 26, 130))
gd.ellipse((200, 500, 1300, 1000), fill=(110, 40, 22, 70))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(230)))
# dot grid (subtle texture)
dots = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dots)
for y in range(20, H, 48):
    for x in range(20, W, 48):
        dd.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, 16))
img.alpha_composite(dots)

# ---------- wave -> text graphic (right half of the safe area) ----------
# audio bars on the left turn into transcript lines on the right
g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(g)
cy = (SY0 + SY1) // 2
gx0, gx1 = 1450, 2030
n_bars = 7
bw, gap = 15, 12
for i in range(n_bars):
    x = gx0 + i * (bw + gap)
    t = i / (n_bars - 1)
    amp = (0.35 + 0.65 * abs(math.sin(i * 1.7 + 0.6))) * (1 - 0.35 * t) * 150
    d.rounded_rectangle((x, cy - amp, x + bw, cy + amp), bw // 2, fill=ORANGE + (255,))
# arrow chevron
ax = gx0 + n_bars * (bw + gap) + 16
d.line((ax, cy - 40, ax + 34, cy, ax, cy + 40), fill=ORANGE_HI + (255,), width=12, joint='curve')
# transcript card
cx0, cx1 = ax + 70, gx1
cyt, cyb = cy - 175, cy + 175
card = Image.new('RGBA', (W, H), (0, 0, 0, 0))
cd = ImageDraw.Draw(card)
cd.rounded_rectangle((cx0, cyt, cx1, cyb), 34, fill=(255, 255, 255, 18), outline=(255, 255, 255, 60), width=3)
f_ts = F(26, 0)
rows = [(0.92, '00:00'), (0.78, None), (0.86, '00:12'), (0.6, None), (0.82, '00:31')]
y = cyt + 50
for k, (frac, ts) in enumerate(rows):
    x = cx0 + 36
    if ts:
        cd.text((x, y), ts, font=f_ts, fill=ORANGE_HI + (255,), anchor='lm')
        x += 92
    width = (cx1 - 36 - x) * frac
    cd.rounded_rectangle((x, y - 11, x + width, y + 11), 11, fill=(255, 255, 255, 215 if k % 2 == 0 else 150))
    y += 62
img.alpha_composite(g)
img.alpha_composite(card)

# ---------- robot mascot, just right of the safe area (desktop + TV) ----------
bot = robot()
k = 620 / bot.height
bot = bot.resize((round(bot.width * k), round(bot.height * k)), Image.LANCZOS)
bx, by = 2085, SY1 - bot.height + 150
fade = Image.new('L', bot.size, 255)
fd = ImageDraw.Draw(fade)
for yy in range(bot.height - 200, bot.height):
    fd.line((0, yy, bot.width, yy), fill=int(255 * (bot.height - yy) / 200))
bot.putalpha(Image.composite(bot.split()[3], Image.new('L', bot.size, 0), fade))
sh = Image.new('RGBA', bot.size, (0, 0, 0, 0))
sh.putalpha(bot.split()[3].point(lambda v: int(v * 0.55)))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)), (bx + 18, by + 22))
img.alpha_composite(bot, (bx, by))

# ---------- text block (left half of the safe area) ----------
d = ImageDraw.Draw(img)
tx = SX0 + 40
# logo + wordmark
logo = Image.open(LOGO).convert('L').resize((62, 62), Image.LANCZOS)
mark = Image.new('RGBA', logo.size, WHITE + (255,))
mark.putalpha(logo.point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(mark, (tx, SY0 + 34))
fw = F(54, 0)
d.text((tx + 82, SY0 + 66), 'TranscriptX', font=fw, fill=WHITE, anchor='lm')
d.text((tx + 82 + d.textlength('TranscriptX', font=fw), SY0 + 66), '.ai', font=fw, fill=MUTED, anchor='lm')
# headline
fh = F(84)
d.text((tx, SY0 + 205), 'Any video or audio.', font=fh, fill=WHITE, anchor='ls', stroke_width=1, stroke_fill=WHITE)
d.text((tx, SY0 + 310), 'Text in seconds.', font=fh, fill=ORANGE, anchor='ls', stroke_width=1, stroke_fill=ORANGE)
# platform chips
fc = F(27, 2)
x, y = tx, SY0 + 345
for label in ['YouTube', 'TikTok', 'Instagram', 'ChatGPT & Claude']:
    w = d.textlength(label, font=fc) + 48
    ch = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ch).rounded_rectangle((x, y, x + w, y + 54), 27, outline=(255, 255, 255, 120), width=2, fill=(255, 255, 255, 18))
    img.alpha_composite(ch)
    d = ImageDraw.Draw(img)
    d.text((x + w / 2, y + 27), label, font=fc, fill=(235, 230, 226), anchor='mm')
    x += w + 14

rgb = img.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.5, percent=60, threshold=2))
rgb.save(OUT, 'PNG', optimize=True)
print(OUT, rgb.size, round(os.path.getsize(OUT) / 1024 / 1024, 2), 'MB')

if PREVIEW:
    rgb.resize((1280, 720), Image.LANCZOS).save(f'{PREVIEW}/banner_tv.png')
    rgb.crop((0, SY0, W, SY1)).resize((1280, 212), Image.LANCZOS).save(f'{PREVIEW}/banner_desktop.png')
    rgb.crop((SX0, SY0, SX1, SY1)).save(f'{PREVIEW}/banner_mobile.png')
