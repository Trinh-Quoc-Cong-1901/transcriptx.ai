"""YouTube thumbnail v3 for can-chatgpt-watch-videos.

Style: dark cinematic background, 3-line headline on the left with the key word on a red bar,
a TranscriptX AI robot mascot on the right in a "thinking" pose (hand on chin, looking up-left).
The mascot is drawn here (no stock photo / no generated person).
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(f'{HERE}/../../can-chatgpt-watch-videos/images/video/can-chatgpt-watch-videos-transcriptx-mcp-thumbnail.jpg')
LOGO = os.path.abspath(f'{HERE}/../brand/logo/logo_256.png')
PREVIEW = sys.argv[1] if len(sys.argv) > 1 else None

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


# ---------------- background ----------------
img = vgrad((W, H), (20, 16, 15), (8, 7, 7)).convert('RGBA')
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((1250, 150, 2700, 1600), fill=(150, 60, 25, 120))
gd.ellipse((-400, 300, 900, 1500), fill=(90, 30, 20, 70))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(260)))
# faint "MCP" watermark, like the script text in the reference
wm = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(wm).text((70, 1440), 'MCP', font=F(520, 9), fill=(255, 255, 255, 9), anchor='ld')
img.alpha_composite(wm)


# ---------------- robot mascot ----------------
from mascot import robot
bot = robot()
# soft shadow of the robot on the background
sh = Image.new('RGBA', bot.size, (0, 0, 0, 0))
sh.putalpha(bot.split()[3].point(lambda v: int(v * 0.6)))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(40)), (1330 + 30, 120 + 30))
img.alpha_composite(bot, (1330, 120))


# ---------------- headline ----------------
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
    bbox = m.getbbox()
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gh = bbox[3] - bbox[1]
    g.paste(vgrad((W, gh), (255, 255, 255), (200, 200, 204)).convert('RGBA'), (0, bbox[1]))
    g.putalpha(m)
    img.alpha_composite(g)
    return bbox


grad_text('CAN CHATGPT', 165, 130, 470)
# red bar + the key word
bar_y0, bar_y1 = 520, 860
bar = vgrad((1240, bar_y1 - bar_y0), (232, 70, 58), (176, 34, 30)).convert('RGBA')
img.alpha_composite(bar, (110, bar_y0))
grad_text('WATCH', 330, 130, 820)
grad_text('VIDEOS?', 165, 470, 1060)

# brand, top-left (like the creator name in the reference)
logo = Image.open(LOGO).convert('L').resize((64, 64), Image.LANCZOS)
mark = Image.new('RGBA', logo.size, (255, 255, 255, 255))
mark.putalpha(logo.point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(mark, (120, 96))
ImageDraw.Draw(img).text((200, 128), 'TranscriptX', font=F(52, 0), fill=(255, 255, 255), anchor='lm')

rgb = img.convert('RGB').filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
rgb.save(OUT, 'JPEG', quality=100, subsampling=0, optimize=True)
print(OUT, rgb.size, os.path.getsize(OUT) // 1024, 'KB')
# YouTube upload file: 1280x720 (YouTube's max display size), downscaled here and re-sharpened,
# lossless PNG so YouTube gets clean edges instead of re-scaling a big JPEG itself.
yt = img.convert('RGB').resize((1280, 720), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=1))
YT = OUT.replace('-thumbnail.jpg', '-thumbnail-youtube.png')
yt.save(YT, 'PNG', optimize=True)
print(YT, yt.size, os.path.getsize(YT) // 1024, 'KB')
if PREVIEW:
    yt.save(f'{PREVIEW}/thumb_half.png')
    rgb.crop((1300, 100, 2560, 1000)).save(f'{PREVIEW}/thumb_crop.png')
