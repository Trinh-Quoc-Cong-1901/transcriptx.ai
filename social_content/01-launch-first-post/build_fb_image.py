"""Facebook post image (1080x1350, 4:5) for launch-first-post. Output PNG + JPG (FB does not accept WebP)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, '../../page/blog/_source'))
FONT = '/System/Library/Fonts/HelveticaNeue.ttc'
BG, DARK, ACCENT, MUTED = (248, 247, 244), (43, 42, 38), (204, 88, 46), (80, 77, 70)
W, H = 1080, 1350

def f(size, bold=True):
    return ImageFont.truetype(FONT, size, index=1 if bold else 0)

img = Image.new('RGBA', (W, H), BG + (255,))
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((300, 500, 1500, 1700), fill=(236, 160, 115, 110))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(140)))
d = ImageDraw.Draw(img)

# hook
d.text((80, 120), 'Still typing out', font=f(92), fill=DARK)
d.text((80, 225), 'videos by hand?', font=f(92), fill=ACCENT)
d.text((82, 350), 'Paste the link. Get the text in seconds.', font=f(40, False), fill=MUTED)

# real screenshot: transcript column only (no video thumbnail)
crop = (380, 30, 1410, 640)
sc = 0.90
shot = Image.open(f'{SRC}/transcript/transcript-result-light.png').convert('RGB').crop(crop)
shot = shot.resize((int(shot.width * sc), int(shot.height * sc)), Image.LANCZOS).convert('RGBA')
pad = 28
card = Image.new('RGBA', (shot.width + 2 * pad, shot.height + 2 * pad), (255, 255, 255, 255))
card.alpha_composite(shot, (pad, pad))
m = Image.new('L', card.size, 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, card.width - 1, card.height - 1), 30, fill=255)
card.putalpha(m)
cx, cy = (W - card.width) // 2, 500
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((cx, cy + 24, cx + card.width, cy + card.height + 24), 30, fill=(70, 40, 20, 90))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
img.alpha_composite(card, (cx, cy))
d = ImageDraw.Draw(img)

def to_canvas(x, y):
    return cx + pad + (x - crop[0]) * sc, cy + pad + (y - crop[1]) * sc

# outline the Copy button and the first timestamp
for box in [(1244, 127, 1383, 176), (408, 230, 494, 256)]:
    x0, y0 = to_canvas(box[0], box[1]); x1, y1 = to_canvas(box[2], box[3])
    d.rounded_rectangle((x0 - 9, y0 - 9, x1 + 9, y1 + 9), 18, outline=ACCENT, width=5)

# footer: logo + domain
logo = Image.open(f'{SRC}/brand/logo/logo_256.png').convert('RGBA').resize((64, 64), Image.LANCZOS)
logo.putdata([(r, g, b, 0) if r > 235 and g > 235 and b > 235 else (r, g, b, a) for r, g, b, a in logo.getdata()])
fy = H - 130
img.alpha_composite(logo, (80, fy))
d.text((160, fy + 32), 'TranscriptX.ai', font=f(40), fill=DARK, anchor='lm')
txt = 'Free to try'
tw = d.textlength(txt, font=f(34))
d.rounded_rectangle((W - 80 - tw - 60, fy + 2, W - 80, fy + 62), 30, fill=DARK)
d.text((W - 80 - (tw + 60) / 2, fy + 32), txt, font=f(34), fill='white', anchor='mm')

out = os.path.join(HERE, 'images', 'fb-launch-1080x1350')
rgb = img.convert('RGB')
rgb.save(out + '.png', optimize=True)
rgb.save(out + '.jpg', quality=92, subsampling=0)
print(out)
