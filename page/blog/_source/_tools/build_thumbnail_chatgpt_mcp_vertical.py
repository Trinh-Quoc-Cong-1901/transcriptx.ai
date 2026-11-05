"""Vertical 9:16 cover (TikTok / Reels / Shorts) for can-chatgpt-watch-videos, same style as the
YouTube thumbnail v3 (build_thumbnail_chatgpt_mcp.py). Rendered at 2160x3840, saved at 1080x1920 as
PNG + JPG (TikTok/Facebook don't take WebP).

Safe zones: headline + robot face sit inside the centre 3:4 band (y 240-1680 at 1080x1920) that TikTok
shows in the profile grid; nothing important under the right-side buttons or the bottom caption area.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mascot import robot

OUT = os.path.abspath(f'{HERE}/../../can-chatgpt-watch-videos/images/video/can-chatgpt-watch-videos-transcriptx-mcp-thumbnail-vertical')
LOGO = os.path.abspath(f'{HERE}/../brand/logo/logo_256.png')
PREVIEW = sys.argv[1] if len(sys.argv) > 1 else None

W, H = 2160, 3840
AV = '/System/Library/Fonts/Avenir Next.ttc'


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
gd.ellipse((-200, 1700, 2400, 4200), fill=(150, 60, 25, 130))
gd.ellipse((-600, 300, 1400, 1900), fill=(90, 30, 20, 60))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(300)))

# robot, centred a bit left of the right-side TikTok buttons
bot = robot()
k = 1.3
bot = bot.resize((int(bot.width * k), int(bot.height * k)), Image.LANCZOS)
bx, by = (W - bot.width) // 2 - 90, H - bot.height + 60   # body runs off the bottom edge
sh = Image.new('RGBA', bot.size, (0, 0, 0, 0))
sh.putalpha(bot.split()[3].point(lambda v: int(v * 0.6)))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(50)), (bx + 36, by + 36))
img.alpha_composite(bot, (bx, by))


def grad_text(text, size, x, y, stroke=9):
    f = F(size)
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).text((x, y), text, font=f, fill=255, anchor='ms')
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    shadow.putalpha(m.point(lambda v: int(v * 0.7)))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)), (10, 18))
    st = Image.new('L', (W, H), 0)
    ImageDraw.Draw(st).text((x, y), text, font=f, fill=255, anchor='ms', stroke_width=stroke)
    dk = Image.new('RGBA', (W, H), (16, 12, 12, 255))
    dk.putalpha(st)
    img.alpha_composite(dk)
    b = m.getbbox()
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g.paste(vgrad((W, b[3] - b[1]), (255, 255, 255), (200, 200, 204)).convert('RGBA'), (0, b[1]))
    g.putalpha(m)
    img.alpha_composite(g)
    return b


def fit(text, size, max_w):
    d = ImageDraw.Draw(Image.new('L', (1, 1)))
    while d.textlength(text, font=F(size)) > max_w:
        size -= 5
    return size


cx = W // 2
grad_text('CAN CHATGPT', fit('CAN CHATGPT', 300, 1840), cx, 960)
bar_y0, bar_y1 = 1030, 1500
bar = vgrad((1900, bar_y1 - bar_y0), (232, 70, 58), (176, 34, 30)).convert('RGBA')
img.alpha_composite(bar, ((W - 1900) // 2, bar_y0))
grad_text('WATCH', fit('WATCH', 560, 1780), cx, 1440, stroke=12)
grad_text('VIDEOS?', fit('VIDEOS?', 300, 1500), cx, 1800)

# brand, top centre (below TikTok's top bar)
logo = Image.open(LOGO).convert('L').resize((92, 92), Image.LANCZOS)
mark = Image.new('RGBA', logo.size, (255, 255, 255, 255))
mark.putalpha(logo.point(lambda v: 0 if v > 235 else 255))
d = ImageDraw.Draw(img)
tw = d.textlength('TranscriptX', font=F(76, 0))
lx = int(cx - (92 + 24 + tw) / 2)
img.alpha_composite(mark, (lx, 560))
d.text((lx + 116, 606), 'TranscriptX', font=F(76, 0), fill=(255, 255, 255), anchor='lm')

final = img.convert('RGB').resize((1080, 1920), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=80, threshold=1))
final.save(OUT + '.png', 'PNG', optimize=True)
final.save(OUT + '.jpg', 'JPEG', quality=95, subsampling=0, optimize=True)
print(OUT + '.png / .jpg', final.size)
if PREVIEW:
    final.crop((0, 240, 1080, 1680)).save(f'{PREVIEW}/vertical_grid_3x4.png')
