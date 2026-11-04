"""Reusable blog cover / social share (og:image) builder for TranscriptX posts.

Renders natively at 2400x1260 (2x of the 1200x630 OG size), never upscales the screenshot,
draws outlines after cropping, and writes:
  images/<slug>-cover.webp          (CMS cover, 2400x1260)
  images/<slug>-og-1200x630.jpg     (og:image for Facebook, LinkedIn, X, Zalo)
plus QA files (100% crop of the screenshot, 480px small preview) into check_dir.

Layout: left = badge + 2-line headline (line 2 in brand orange) + one sub line + chips + logo;
right = a real TranscriptX screenshot crop with orange outlines on what matters, and an
optional "input file" card (mic + file name + duration + waveform) overlapping it.
"""
import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = '/System/Library/Fonts/HelveticaNeue.ttc'
BG, DARK, ACCENT, MUTED = (248, 247, 244), (43, 42, 38), (204, 88, 46), (80, 77, 70)
W, H = 2400, 1260
SRC = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def font(size, bold=False):
    return ImageFont.truetype(FONT, size, index=1 if bold else 0)


def _mic(d, cx, cy, s, col):
    d.rounded_rectangle((cx - 13 * s, cy - 30 * s, cx + 13 * s, cy + 8 * s), 13 * s, fill=col)
    d.arc((cx - 24 * s, cy - 18 * s, cx + 24 * s, cy + 20 * s), 0, 180, fill=col, width=max(3, int(6 * s)))
    d.line((cx, cy + 20 * s, cx, cy + 32 * s), fill=col, width=max(3, int(6 * s)))


def _fit(d, text, size, max_w, bold=True, min_size=40):
    while d.textlength(text, font=font(size, bold)) > max_w and size > min_size:
        size -= 6
    return size


def make_cover(slug, out_dir, *, badge, line1, line2, sub, chips, shot, crop, highlights=(),
               file_card=None, check_dir=None, shot_y=300, card_min_x=1300, card_dy=120, tag=None):
    """shot: path relative to _source; crop: (x0,y0,x1,y1) in source pixels;
    highlights: list of (x0,y0,x1,y1) in SOURCE pixels to outline in orange;
    file_card: (name, duration) or None."""
    img = Image.new('RGBA', (W, H), BG + (255,))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((1150, -250, 2750, 1450), fill=(236, 160, 115, 120))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(170)))

    # screenshot at native retina pixels (no resize)
    s = Image.open(f'{SRC}/{shot}').convert('RGB').crop(crop).convert('RGBA')
    m = Image.new('L', s.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, s.width - 1, s.height - 1), 28, fill=255)
    s.putalpha(m)
    wx, wy = W - s.width - 110, shot_y
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((wx, wy + 30, wx + s.width, wy + s.height + 30), 28, fill=(70, 40, 20, 120))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(40)))
    img.alpha_composite(s, (wx, wy))
    d = ImageDraw.Draw(img)
    for x0, y0, x1, y1 in highlights:
        d.rounded_rectangle((wx + x0 - crop[0] - 10, wy + y0 - crop[1] - 10, wx + x1 - crop[0] + 10, wy + y1 - crop[1] + 10),
                            22, outline=ACCENT + (255,), width=7)

    if tag:   # dark pill above the screenshot that names the outlined detail
        tw = d.textlength(tag, font=font(40, True))
        d.rounded_rectangle((wx + 4, wy - 96, wx + tw + 64, wy - 26), 35, fill=DARK + (255,))
        d.text((wx + 34 + tw / 2, wy - 61), tag, font=font(40, True), fill=(255, 255, 255, 255), anchor='mm')
        d.polygon([(wx + 70, wy - 27), (wx + 96, wy - 27), (wx + 83, wy - 8)], fill=DARK + (255,))

    if file_card:
        name, dur = file_card
        cw, ch = 640, 230
        # sit in the screenshot's lower area, but never left of the text column's safe edge
        cx, cy = max(wx - 150, card_min_x), wy + s.height - card_dy
        sh2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh2).rounded_rectangle((cx, cy + 22, cx + cw, cy + ch + 22), 36, fill=(70, 40, 20, 110))
        img.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(30)))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((cx, cy, cx + cw, cy + ch), 36, fill=(255, 255, 255, 255))
        d.ellipse((cx + 40, cy + 40, cx + 150, cy + 150), fill=ACCENT + (255,))
        mcx, mcy, wht = cx + 95, cy + 95, (255, 255, 255, 255)
        d.rounded_rectangle((mcx - 16, mcy - 36, mcx + 16, mcy + 10), 16, fill=wht)
        d.arc((mcx - 30, mcy - 22, mcx + 30, mcy + 26), 0, 180, fill=wht, width=7)
        d.line((mcx, mcy + 26, mcx, mcy + 40), fill=wht, width=7)
        nsz = _fit(d, name, 46, cw - 210)
        d.text((cx + 180, cy + 72), name, font=font(min(nsz, 46), True), fill=DARK + (255,), anchor='lm')
        d.text((cx + 180, cy + 124), dur, font=font(38), fill=(130, 126, 118, 255), anchor='lm')
        bx, by = cx + 44, cy + 196
        for i in range(46):
            h = 10 + 26 * abs(math.sin(i * 0.55) * math.cos(i * 0.21)) + (8 if i % 5 == 0 else 0)
            x = bx + i * 12
            d.rounded_rectangle((x, by - h / 2, x + 6, by + h / 2), 3, fill=(ACCENT if i < 20 else (214, 205, 192)) + (255,))

    # left column
    left_max = 1060
    bw = d.textlength(badge, font=font(54, True))
    d.rounded_rectangle((110, 150, 110 + 108 + bw + 46, 250), 50, fill=DARK + (255,))
    _mic(d, 172, 200, 1, (255, 255, 255, 255))
    d.text((218, 200), badge, font=font(54, True), fill=(255, 255, 255, 255), anchor='lm')
    hs = min(_fit(d, line1, 210, max(left_max, 1000)), _fit(d, line2, 210, max(left_max, 1000)))
    d.text((100, 410), line1, font=font(hs, True), fill=DARK + (255,), anchor='lm')
    d.text((100, 410 + int(hs * 1.0)), line2, font=font(hs, True), fill=ACCENT + (255,), anchor='lm')
    d.text((110, 790), sub, font=font(_fit(d, sub, 62, 1080, False), False), fill=MUTED + (255,), anchor='lm')
    x = 110
    for lbl in chips:
        tw = d.textlength(lbl, font=font(50, True))
        d.rounded_rectangle((x, 880, x + tw + 60, 972), 46, fill=(255, 255, 255, 255), outline=(225, 216, 204, 255), width=3)
        d.text((x + 30 + tw / 2, 926), lbl, font=font(50, True), fill=ACCENT + (255,), anchor='mm')
        x += tw + 60 + 20
    lg = Image.open(f'{SRC}/brand/logo/logo_256.png').convert('RGBA').resize((84, 84), Image.LANCZOS)
    lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
    img.alpha_composite(lg, (108, 1086))
    d.text((214, 1128), 'TranscriptX.ai', font=font(60, True), fill=DARK + (255,), anchor='lm')

    os.makedirs(out_dir, exist_ok=True)
    rgb = img.convert('RGB')
    cover = f'{out_dir}/{slug}-cover.webp'
    rgb.save(cover, 'WEBP', quality=95, method=6)
    og = f'{out_dir}/{slug}-og-1200x630.jpg'
    rgb.resize((1200, 630), Image.LANCZOS).save(og, 'JPEG', quality=92, subsampling=0, optimize=True)
    if check_dir:
        rgb.crop((wx, wy, wx + min(1000, s.width), wy + min(600, s.height))).save(f'{check_dir}/{slug}_cover_100pct.png')
        rgb.resize((480, 252), Image.LANCZOS).save(f'{check_dir}/{slug}_cover_small.png')
    return cover, og


# ---------------------------------------------------------------------------
# Hook style (YouTube-thumbnail look): ONE big curiosity line, ONE focal visual.
# Dark background for contrast in social feeds, max ~4 words of headline, no feature list.
# ---------------------------------------------------------------------------
INK = (24, 22, 20)


def make_hook_cover(slug, out_dir, *, big, strike=False, small, kicker=None, shot, crop, scale=1.25,
                    highlight=None, check_dir=None, card_x=1380):
    """big: the giant line (e.g. '4 HOURS'); strike: orange strikethrough on it;
    small: second line under it (e.g. 'of typing?'); kicker: tiny line above (context);
    shot/crop: one real TranscriptX screenshot crop, shown at `scale` (<=1.3 of retina);
    highlight: (x0,y0,x1,y1) in source px to ring in orange + arrow from the headline."""
    img = Image.new('RGBA', (W, H), INK + (255,))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((1300, -200, 2900, 1500), fill=ACCENT + (120,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(220)))

    # focal visual: screenshot card bleeding off the right edge
    s = Image.open(f'{SRC}/{shot}').convert('RGB').crop(crop)
    s = s.resize((round(s.width * scale), round(s.height * scale)), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', s.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, s.width + 60, s.height - 1), 36, fill=255)
    s.putalpha(m)
    wx, wy = max(card_x, W - s.width + 40), (H - s.height) // 2 - 20   # bleeds off the right edge
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((wx - 10, wy + 30, W + 100, wy + s.height + 40), 36, fill=(0, 0, 0, 170))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(50)))
    img.alpha_composite(s, (wx, wy))
    d = ImageDraw.Draw(img)
    if highlight:
        x0, y0, x1, y1 = highlight
        rx0, ry0 = wx + (x0 - crop[0]) * scale - 16, wy + (y0 - crop[1]) * scale - 14
        rx1, ry1 = wx + (x1 - crop[0]) * scale + 16, wy + (y1 - crop[1]) * scale + 14
        d.rounded_rectangle((rx0, ry0, rx1, ry1), 26, outline=ACCENT + (255,), width=10)

    # headline
    x = 110
    if kicker:
        d.text((x + 4, 300), kicker, font=font(64, True), fill=(200, 192, 182, 255), anchor='lm')
    bs = _fit(d, big, 300, wx - x - 120, True, 120)
    by = 520
    d.text((x, by), big, font=font(bs, True), fill=(255, 255, 255, 255), anchor='lm')
    bw = d.textlength(big, font=font(bs, True))
    if strike:
        d.line((x - 10, by + 6, x + bw + 10, by - 14), fill=ACCENT + (255,), width=max(18, bs // 11))
    ss = _fit(d, small, 190, wx - x - 200, True, 90)
    sy = by + int(bs * 0.62) + int(ss * 0.62)
    d.text((x, sy), small, font=font(ss, True), fill=ACCENT + (255,), anchor='lm')
    if highlight:   # curved arrow from the end of the small line to the ring
        sw = d.textlength(small, font=font(ss, True))
        ax, ay = x + sw + 50, sy - 20
        tx, ty = rx0 - 24, (ry0 + ry1) / 2
        pts = []
        for i in range(41):
            t = i / 40
            cx_, cy_ = tx - 40, ay + 10   # go right first, then up into the ring
            pts.append(((1 - t) ** 2 * ax + 2 * (1 - t) * t * cx_ + t * t * tx, (1 - t) ** 2 * ay + 2 * (1 - t) * t * cy_ + t * t * ty))
        d.line(pts, fill=ACCENT + (255,), width=12, joint='curve')
        ang = math.atan2(pts[-1][1] - pts[-4][1], pts[-1][0] - pts[-4][0])
        L = 46
        d.polygon([(tx, ty), (tx - L * math.cos(ang - 0.45), ty - L * math.sin(ang - 0.45)),
                   (tx - L * math.cos(ang + 0.45), ty - L * math.sin(ang + 0.45))], fill=ACCENT + (255,))

    lg = Image.open(f'{SRC}/brand/logo/logo_256.png').convert('RGBA').resize((72, 72), Image.LANCZOS)
    a = lg.convert('L').point(lambda v: 0 if v > 235 else 255)
    white = Image.new('RGBA', lg.size, (255, 255, 255, 255)); white.putalpha(a)
    img.alpha_composite(white, (112, 1100))
    d.text((204, 1136), 'TranscriptX.ai', font=font(54, True), fill=(255, 255, 255, 255), anchor='lm')

    os.makedirs(out_dir, exist_ok=True)
    rgb = img.convert('RGB')
    cover = f'{out_dir}/{slug}-cover.webp'
    rgb.save(cover, 'WEBP', quality=95, method=6)
    og = f'{out_dir}/{slug}-og-1200x630.jpg'
    rgb.resize((1200, 630), Image.LANCZOS).save(og, 'JPEG', quality=92, subsampling=0, optimize=True)
    if check_dir:
        rgb.crop((wx, wy, min(W, wx + 1000), wy + min(600, s.height))).save(f'{check_dir}/{slug}_cover_100pct.png')
        rgb.resize((480, 252), Image.LANCZOS).save(f'{check_dir}/{slug}_cover_small.png')
    return cover, og
