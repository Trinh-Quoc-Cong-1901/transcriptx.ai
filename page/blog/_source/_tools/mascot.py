"""TranscriptX robot mascot (white + brand orange, thinking pose: hand on chin, one brow raised).

robot() -> RGBA image 1250x1440, transparent background. Used by the YouTube thumbnail and channel banner.
"""
from PIL import Image, ImageDraw, ImageFilter, ImageChops

ORANGE = (214, 92, 46)


def vgrad(size, top, bottom):
    w, h = size
    g = Image.new('RGB', (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        g.putpixel((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return g.resize((w, h))



def shape(size, draw_fn):
    m = Image.new('L', size, 0)
    draw_fn(ImageDraw.Draw(m))
    return m


def paint(layer, mask, top, bottom, rim=None, rim_dx=-26, outline=0):
    """Fill mask with a vertical gradient; optional warm rim light on the right edge."""
    if outline:
        o = mask.resize((mask.width // 8, mask.height // 8)).filter(ImageFilter.MaxFilter(2 * (outline // 8) + 1))
        o = o.resize(mask.size, Image.BILINEAR).point(lambda v: 255 if v > 100 else 0)
        dk = Image.new('RGBA', mask.size, (28, 22, 20, 255))
        dk.putalpha(o)
        layer.alpha_composite(dk)
    fill = vgrad(mask.size, top, bottom).convert('RGBA')
    fill.putalpha(mask)
    layer.alpha_composite(fill)
    if rim:
        inner = ImageChops.offset(mask, rim_dx, 0)
        edge = ImageChops.subtract(mask, inner).filter(ImageFilter.GaussianBlur(10))
        r = Image.new('RGBA', mask.size, rim + (0,))
        r.putalpha(edge.point(lambda v: int(v * 0.85)))
        layer.alpha_composite(r)



def robot():
    RS = 2
    RW, RH = 1250 * RS, 1440 * RS
    bot = Image.new('RGBA', (RW, RH), (0, 0, 0, 0))
    WHITE_T, WHITE_B = (250, 248, 245), (196, 192, 188)
    DARK_T, DARK_B = (40, 40, 46), (12, 12, 16)
    ORG_T, ORG_B = (236, 120, 70), (176, 66, 30)
    RIM = (255, 150, 90)
    s = lambda *v: tuple(int(x * RS) for x in v)

    # torso
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(170, 930, 1130, 1700), 260 * RS, fill=255)), WHITE_T, (150, 146, 142), RIM)
    # chest panel + TranscriptX mark
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(470, 1080, 830, 1330), 70 * RS, fill=255)), DARK_T, DARK_B)
    cd = ImageDraw.Draw(bot)
    for i, (x0, x1) in enumerate([(540, 760), (540, 760), (540, 690)]):
        y = 1150 + i * 55
        cd.rounded_rectangle(s(x0, y, x1, y + 26), 13 * RS, fill=ORANGE + (255,))
    # neck
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(520, 820, 780, 980), 50 * RS, fill=255)), (70, 70, 76), (30, 30, 34))
    # antenna
    cd.line(s(650, 200, 700, 70), fill=(200, 196, 192, 255), width=22 * RS)
    ag = Image.new('RGBA', (RW, RH), (0, 0, 0, 0))
    ImageDraw.Draw(ag).ellipse(s(640, 10, 760, 130), fill=(255, 140, 70, 200))
    bot.alpha_composite(ag.filter(ImageFilter.GaussianBlur(40 * RS)))
    paint(bot, shape((RW, RH), lambda d: d.ellipse(s(655, 25, 745, 115), fill=255)), (255, 170, 110), ORG_B)
    # ear pods
    for x0 in (165, 1035):
        paint(bot, shape((RW, RH), lambda d, x0=x0: d.rounded_rectangle(s(x0, 380, x0 + 110, 640), 55 * RS, fill=255)), ORG_T, ORG_B, RIM)
    # head
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(230, 170, 1070, 870), 250 * RS, fill=255)), WHITE_T, WHITE_B, RIM)
    # visor
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(300, 290, 1000, 760), 190 * RS, fill=255)), DARK_T, DARK_B)
    # visor reflection
    rf = Image.new('RGBA', (RW, RH), (0, 0, 0, 0))
    ImageDraw.Draw(rf).rounded_rectangle(s(360, 320, 640, 360), 20 * RS, fill=(255, 255, 255, 40))
    bot.alpha_composite(rf)
    # eyes: looking up-left, one brow raised (curious)
    EYE = (255, 170, 90)
    eg = Image.new('RGBA', (RW, RH), (0, 0, 0, 0))
    ed = ImageDraw.Draw(eg)
    ed.rounded_rectangle(s(430, 420, 540, 560), 55 * RS, fill=EYE + (255,))
    ed.rounded_rectangle(s(680, 430, 790, 550), 55 * RS, fill=EYE + (255,))
    ed.line(s(410, 385, 560, 395), fill=EYE + (255,), width=20 * RS)          # flat brow
    ed.line(s(670, 380, 820, 345), fill=EYE + (255,), width=20 * RS)          # raised brow
    ed.line(s(560, 660, 680, 650), fill=EYE + (200,), width=14 * RS)          # small "hmm" mouth
    bot.alpha_composite(eg.filter(ImageFilter.GaussianBlur(28 * RS)))
    bot.alpha_composite(eg.filter(ImageFilter.GaussianBlur(8 * RS)))
    bot.alpha_composite(eg)
    # pupils highlights
    for cx, cy in ((462, 455), (712, 462)):
        cd.ellipse(s(cx - 16, cy - 16, cx + 16, cy + 16), fill=(255, 240, 220, 255))
    # arm: elbow low-left, forearm up to chin (dark outline separates it from the torso)
    OL = 22 * RS
    paint(bot, shape((RW, RH), lambda d: d.line(s(250, 1500, 330, 1210), fill=255, width=190 * RS)), WHITE_T, (170, 166, 162), RIM, outline=OL)
    paint(bot, shape((RW, RH), lambda d: d.line(s(330, 1230, 530, 930), fill=255, width=175 * RS)), WHITE_T, (185, 181, 177), RIM, outline=OL)
    paint(bot, shape((RW, RH), lambda d: d.ellipse(s(235, 1135, 425, 1325), fill=255)), ORG_T, ORG_B, outline=OL)   # elbow joint
    paint(bot, shape((RW, RH), lambda d: d.ellipse(s(445, 880, 615, 1000), fill=255)), ORG_T, ORG_B, outline=OL)    # wrist joint
    # fist under the chin
    paint(bot, shape((RW, RH), lambda d: d.rounded_rectangle(s(410, 770, 660, 960), 85 * RS, fill=255)), WHITE_T, (190, 186, 182), RIM, outline=OL)
    cd = ImageDraw.Draw(bot)
    for i in range(3):
        x = 470 + i * 60
        cd.line(s(x, 800, x, 860), fill=(160, 156, 152, 255), width=10 * RS)

    bot = bot.resize((RW // RS, RH // RS), Image.LANCZOS)

    return bot
