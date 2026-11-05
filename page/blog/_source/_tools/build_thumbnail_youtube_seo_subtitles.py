"""YouTube thumbnail for "YouTube SEO: The One Thing Almost Everyone Ignores".

Same style as build_thumbnail_chatgpt_mcp.py (dark cinematic background, gradient headline, key word on a red bar).
Right side: an SEO checklist card, three boxes ticked, "Subtitles" with a red X, circled in red. One hook, one image.
Writes <OUT>/thumbnail/youtube-seo-subtitles-thumbnail.jpg (2560x1440) + -youtube.png (1280x720 upload file).
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(f'{HERE}/../../../../social_content/03-youtube-seo-subtitles/thumbnail')
os.makedirs(OUT_DIR, exist_ok=True)
OUT = f'{OUT_DIR}/youtube-seo-subtitles-thumbnail.jpg'
LOGO = os.path.abspath(f'{HERE}/../brand/logo/logo_256.png')

W, H = 2560, 1440
AV = '/System/Library/Fonts/Avenir Next.ttc'
ORANGE = (214, 92, 46)
RED = (214, 52, 44)


def F(size, idx=8):
    return ImageFont.truetype(AV, size, index=idx)


def vgrad(size, top, bottom):
    w, h = size
    g = Image.new('RGB', (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        g.putpixel((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return g.resize((w, h))


img = vgrad((W, H), (20, 16, 15), (8, 7, 7)).convert('RGBA')
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((1300, 100, 2750, 1550), fill=(150, 60, 25, 120))
gd.ellipse((-400, 300, 900, 1500), fill=(90, 30, 20, 70))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(260)))
wm = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(wm).text((70, 1440), 'SEO', font=F(520, 9), fill=(255, 255, 255, 9), anchor='ld')
img.alpha_composite(wm)

# ---------- checklist card (right) ----------
cw, ch = 980, 1060
card = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
cd = ImageDraw.Draw(card)
cd.rounded_rectangle((0, 0, cw - 1, ch - 1), 56, fill=(250, 248, 244, 255))
rows = ['Title', 'Thumbnail', 'Tags', 'Subtitles']
row_h = 230
for k, name in enumerate(rows):
    y = 70 + k * row_h
    bx, by, bs = 80, y + 40, 130
    last = k == len(rows) - 1
    if last:
        cd.rounded_rectangle((bx, by, bx + bs, by + bs), 30, fill=RED)          # red X = missing
        cd.line((bx + 38, by + 38, bx + bs - 38, by + bs - 38), fill='white', width=18)
        cd.line((bx + 38, by + bs - 38, bx + bs - 38, by + 38), fill='white', width=18)
    else:
        cd.rounded_rectangle((bx, by, bx + bs, by + bs), 30, fill=ORANGE)
        cd.line([(bx + 32, by + 68), (bx + 56, by + 94), (bx + 100, by + 40)], fill='white', width=18, joint='curve')
    cd.text((bx + bs + 60, by + bs / 2), name, font=F(110), fill=RED if last else (40, 36, 34), anchor='lm')
    if not last:
        cd.line((70, y + row_h - 10, cw - 70, y + row_h - 10), fill=(226, 220, 210), width=4)
card = card.rotate(4, resample=Image.BICUBIC, expand=True)
cx, cy = 1450, 200
sh = Image.new('RGBA', card.size, (0, 0, 0, 0))
sh.putalpha(card.split()[3].point(lambda v: int(v * 0.65)))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(45)), (cx + 30, cy + 40))
img.alpha_composite(card, (cx, cy))

# red hand-drawn style ring around the empty "Subtitles" row
ring = Image.new('RGBA', (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rx0, ry0, rx1, ry1 = 1490, 975, 2440, 1235
for k in range(3):
    rd.ellipse((rx0 + k * 6, ry0 - k * 4, rx1 - k * 5, ry1 + k * 3), outline=RED + (255,), width=16)
img.alpha_composite(ring)


# ---------- headline (left) ----------
def grad_text(text, size, x, y, anchor='ls'):
    f = F(size)
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).text((x, y), text, font=f, fill=255, anchor=anchor)
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    shadow.putalpha(m.point(lambda v: int(v * 0.7)))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(14)), (8, 14))
    st = Image.new('L', (W, H), 0)
    ImageDraw.Draw(st).text((x, y), text, font=f, fill=255, anchor=anchor, stroke_width=7)
    dk = Image.new('RGBA', (W, H), (16, 12, 12, 255))
    dk.putalpha(st)
    img.alpha_composite(dk)
    b = m.getbbox()
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g.paste(vgrad((W, b[3] - b[1]), (255, 255, 255), (200, 200, 204)).convert('RGBA'), (0, b[1]))
    g.putalpha(m)
    img.alpha_composite(g)


def fit(text, size, max_w):
    d = ImageDraw.Draw(Image.new('L', (1, 1)))
    while d.textlength(text, font=F(size)) > max_w:
        size -= 4
    return size


# "YOUTUBE SEO / MISSING / SUBTITLES?": topic first, then the problem
grad_text('YOUTUBE SEO', fit('YOUTUBE SEO', 200, 1220), 120, 480)
bar = vgrad((1240, 340), (232, 70, 58), (176, 34, 30)).convert('RGBA')
img.alpha_composite(bar, (100, 550))
grad_text('MISSING', fit('MISSING', 300, 1180), 135, 835)
grad_text('SUBTITLES?', fit('SUBTITLES?', 200, 1220), 120, 1110)

logo = Image.open(LOGO).convert('L').resize((64, 64), Image.LANCZOS)
mark = Image.new('RGBA', logo.size, (255, 255, 255, 255))
mark.putalpha(logo.point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(mark, (120, 96))
ImageDraw.Draw(img).text((200, 128), 'TranscriptX', font=F(52, 0), fill=(255, 255, 255), anchor='lm')

rgb = img.convert('RGB').filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
rgb.save(OUT, 'JPEG', quality=100, subsampling=0, optimize=True)
yt = img.convert('RGB').resize((1280, 720), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=1))
yt.save(OUT.replace('.jpg', '-youtube.png'), 'PNG', optimize=True)
print(OUT)
