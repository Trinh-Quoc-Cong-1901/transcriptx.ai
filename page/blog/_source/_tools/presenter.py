"""Cartoon presenter for walkthrough videos: a flat-style host who lip-syncs to the voice-over.

- `Lipsync(mp3s)`: per-frame mouth openness (0..1) from each voice line's loudness (60 fps, pure Python).
- `draw(size, mouth, blink, wave, look)`: the character (head + shoulders, optional waving arm), RGBA, cached.
- `bubble(img, ...)`: round "facecam" with the presenter, pasted over a walkthrough frame.
Mouth, blink and wave are quantized so sprites stay cached and rendering stays fast.
"""
import array, math, subprocess
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFilter

SKIN = (243, 201, 170)
SKIN_SH = (226, 176, 142)
HAIR = (58, 40, 32)
HAIR_HI = (92, 64, 50)
SHIRT = (204, 88, 46)          # brand accent
SHIRT_SH = (176, 70, 34)
EYE = (40, 34, 30)
LIP = (120, 40, 42)
MOUTH_IN = (92, 30, 34)
TONGUE = (222, 112, 112)
BLUSH = (240, 150, 130, 90)
SS = 2                         # supersampling for clean edges


class Lipsync:
    """Mouth openness per frame for each voice line (index k), at `fps`."""

    def __init__(self, mp3s, ff, fps=60):
        self.fps, self.env = fps, []
        for f in mp3s:
            if not f:
                self.env.append([])
                continue
            raw = subprocess.run([ff, '-v', 'error', '-i', f, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'],
                                 capture_output=True, check=True).stdout
            a = array.array('h', raw)
            hop = 16000 // fps
            rms = [math.sqrt(sum(v * v for v in a[i:i + hop]) / hop) for i in range(0, len(a) - hop, hop)]
            ref = sorted(rms)[int(len(rms) * 0.95)] or 1
            out, cur = [], 0.0
            for r in rms:
                x = min(1.0, max(0.0, (r / ref - 0.08) / 0.8))
                cur = x if x > cur else cur * 0.55 + x * 0.45      # fast attack, soft release
                out.append(cur)
            self.env.append(out)

    def at(self, k, s):
        e = self.env[k] if k < len(self.env) else []
        i = int(s * self.fps)
        return e[i] if 0 <= i < len(e) else 0.0


def blink_at(s, seed=0):
    """0 = open, 1 = closed. A quick blink roughly every 3-4 s."""
    period = 3.4 + (seed % 3) * 0.4
    p = (s + seed * 1.3) % period
    return max(0.0, 1 - abs(p - 0.09) / 0.09) if p < 0.18 else 0.0


@lru_cache(maxsize=512)
def draw(size, mouth=0, blink=0, wave=None, look=0):
    """Presenter sprite, size x size RGBA. mouth 0..6, blink 0..3, wave None or angle step, look -2..2 (pupils)."""
    S = size * SS
    u = S / 100
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = S / 2

    # shoulders + shirt
    d.rounded_rectangle((cx - 40 * u, 74 * u, cx + 40 * u, 130 * u), int(22 * u), fill=SHIRT)
    d.polygon([(cx - 10 * u, 74 * u), (cx + 10 * u, 74 * u), (cx, 86 * u)], fill=SHIRT_SH)
    # neck
    d.rounded_rectangle((cx - 7.5 * u, 58 * u, cx + 7.5 * u, 80 * u), int(6 * u), fill=SKIN_SH)
    d.polygon([(cx - 9 * u, 74 * u), (cx + 9 * u, 74 * u), (cx, 83 * u)], fill=SKIN_SH)
    # collar (white V)
    d.line([(cx - 11 * u, 74 * u), (cx, 85 * u), (cx + 11 * u, 74 * u)], fill=(255, 255, 255), width=int(2.6 * u), joint='curve')

    # waving arm (behind the head on the right side)
    if wave is not None:
        ang = math.radians(-8 + 16 * math.sin(wave * math.pi / 4))       # forearm swings around the elbow
        sx, sy = cx + 30 * u, 84 * u
        ex, ey = cx + 41 * u, 70 * u
        hx, hy = ex + 20 * u * math.sin(ang), ey - 20 * u * math.cos(ang)
        d.line([(sx, sy), (ex, ey)], fill=SHIRT, width=int(12 * u))
        d.ellipse((ex - 6 * u, ey - 6 * u, ex + 6 * u, ey + 6 * u), fill=SHIRT)
        d.line([(ex, ey), (hx, hy)], fill=SKIN_SH, width=int(7.5 * u))
        d.ellipse((ex - 6 * u, ey - 6 * u, ex + 6 * u, ey + 6 * u), fill=SHIRT)
        for f in range(4):                                  # spread fingers + thumb
            fa = ang + math.radians(-27 + f * 16)
            fx, fy = hx + 11.5 * u * math.sin(fa), hy - 11.5 * u * math.cos(fa)
            d.line([(hx, hy), (fx, fy)], fill=SKIN, width=int(3.6 * u))
            d.ellipse((fx - 1.8 * u, fy - 1.8 * u, fx + 1.8 * u, fy + 1.8 * u), fill=SKIN)
        ta = ang + math.radians(-75)
        d.line([(hx, hy + 1 * u), (hx + 9.5 * u * math.sin(ta), hy + 1 * u - 9.5 * u * math.cos(ta))], fill=SKIN, width=int(3.2 * u))
        d.ellipse((hx - 5 * u, hy - 4.5 * u, hx + 5 * u, hy + 5.5 * u), fill=SKIN)

    # hair (back, a shoulder-length bob)
    d.rounded_rectangle((cx - 27 * u, 14 * u, cx + 27 * u, 70 * u), int(24 * u), fill=HAIR)
    # head
    d.ellipse((cx - 22 * u, 15 * u, cx + 22 * u, 66 * u), fill=SKIN)
    # ears
    for sgn in (-1, 1):
        d.ellipse((cx + sgn * 22 * u - 4 * u, 38 * u, cx + sgn * 22 * u + 4 * u, 48 * u), fill=SKIN_SH)
    # fringe
    d.chord((cx - 25 * u, 8 * u, cx + 25 * u, 52 * u), 180, 360, fill=HAIR)
    d.pieslice((cx - 30 * u, 12 * u, cx + 6 * u, 46 * u), 200, 330, fill=HAIR)
    d.arc((cx - 16 * u, 13 * u, cx + 14 * u, 30 * u), 200, 300, fill=HAIR_HI, width=int(1.6 * u))

    # eyes
    ey = 40 * u
    for sgn in (-1, 1):
        ex = cx + sgn * 9 * u
        h = 4.6 * u * (1 - blink / 3)
        if h > 0.6 * u:
            d.ellipse((ex - 3.6 * u, ey - h, ex + 3.6 * u, ey + h), fill=(255, 255, 255))
            px = ex + look * 0.9 * u
            ph = min(h, 3.0 * u)
            d.ellipse((px - 2.6 * u, ey - ph, px + 2.6 * u, ey + ph), fill=EYE)
            d.ellipse((px + 0.4 * u, ey - ph * 0.7, px + 1.6 * u, ey - ph * 0.7 + 1.2 * u), fill=(255, 255, 255))
        else:
            d.arc((ex - 3.8 * u, ey - 2 * u, ex + 3.8 * u, ey + 2 * u), 10, 170, fill=EYE, width=int(1.3 * u))
        lift = mouth * 0.25 * u
        d.line([(ex - 4.5 * u, ey - 8 * u - lift), (ex + 4.5 * u, ey - 8.8 * u - lift + sgn * 0.6 * u)],
               fill=HAIR, width=int(1.6 * u))
        d.ellipse((ex - 4.5 * u + sgn * 1.5 * u, ey + 6 * u, ex + 4.5 * u + sgn * 1.5 * u, ey + 10 * u), fill=BLUSH)
    # nose
    d.arc((cx - 2.2 * u, 45 * u, cx + 2.2 * u, 50 * u), 20, 160, fill=SKIN_SH, width=int(1.3 * u))

    # mouth
    my = 55.5 * u
    if mouth <= 0:
        d.arc((cx - 6.5 * u, my - 4.5 * u, cx + 6.5 * u, my + 2 * u), 20, 160, fill=LIP, width=int(1.7 * u))
    else:
        o = mouth / 6
        mw, mh = (5.2 + 1.2 * math.sin(mouth * 1.7)) * u, (1.2 + 5.6 * o) * u
        d.rounded_rectangle((cx - mw, my - mh * 0.45, cx + mw, my + mh * 0.55), int(min(mw, mh * 0.5) + 1), fill=MOUTH_IN)
        if mouth >= 2:
            d.rectangle((cx - mw * 0.7, my - mh * 0.45, cx + mw * 0.7, my - mh * 0.45 + 1.3 * u), fill=(255, 255, 255))
            d.ellipse((cx - mw * 0.6, my + mh * 0.05, cx + mw * 0.6, my + mh * 0.55), fill=TONGUE)
    return img.resize((size, size), Image.LANCZOS)


def sprite(size, mouth_amt, s, seed=0, wave_t=None, look=0):
    m = int(round(min(1.0, mouth_amt) * 6))
    b = int(round(blink_at(s, seed) * 3))
    w = None if wave_t is None else int(wave_t * 16) % 8
    return draw(int(size), m, b, w, look)


@lru_cache(maxsize=4)
def _bubble_base(d, ring_col, bg_col):
    g = int(d * 0.12)
    out = Image.new('RGBA', (d + g * 2, d + g * 2), (0, 0, 0, 0))
    sh = Image.new('RGBA', out.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((g, g + d * 0.04, g + d, g + d * 1.04), fill=(40, 25, 10, 110))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(d * 0.05)))
    disc = Image.new('RGBA', (d * SS, d * SS), (0, 0, 0, 0))
    dd = ImageDraw.Draw(disc)
    dd.ellipse((0, 0, d * SS - 1, d * SS - 1), fill=ring_col)
    r = d * SS * 0.045
    dd.ellipse((r, r, d * SS - 1 - r, d * SS - 1 - r), fill=bg_col)
    out.alpha_composite(disc.resize((d, d), Image.LANCZOS), (g, g))
    mask = Image.new('L', (d * SS, d * SS), 0)
    ImageDraw.Draw(mask).ellipse((r, r, d * SS - 1 - r, d * SS - 1 - r), fill=255)
    return out, g, mask.resize((d, d), Image.LANCZOS)


def bubble(img, center, d, mouth_amt, s, a=1.0, ring_col=(255, 255, 255, 255), bg_col=(253, 228, 210, 255), look=0):
    """Round facecam (diameter d) centred on `center`, presenter talking inside."""
    if a <= 0:
        return img
    base, g, mask = _bubble_base(int(d), ring_col, bg_col)
    card = base.copy()
    ch = sprite(d * 1.12, mouth_amt, s, look=look)
    bob = int(d * 0.012 * math.sin(s * 2.1) + d * 0.015 * mouth_amt)
    inner = Image.new('RGBA', (int(d), int(d)), (0, 0, 0, 0))
    inner.alpha_composite(ch, (int(d / 2 - ch.width / 2), int(d * 0.03 + bob)))
    al = inner.getchannel('A')
    inner.putalpha(Image.composite(al, Image.new('L', al.size, 0), mask))
    card.alpha_composite(inner, (g, g))
    k = 0.85 + 0.15 * a
    if k < 1:
        card = card.resize((int(card.width * k), int(card.height * k)), Image.LANCZOS)
    if a < 1:
        card.putalpha(card.getchannel('A').point(lambda v: int(v * a)))
    img.paste(card, (int(center[0] - card.width / 2), int(center[1] - card.height / 2)), card)
    return img
