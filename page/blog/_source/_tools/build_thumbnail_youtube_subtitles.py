"""YouTube thumbnail (1280x720) for the how-to-download-youtube-subtitles video."""
import importlib.util, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)
spec = importlib.util.spec_from_file_location('subs', f'{HERE}/build_visuals_youtube_subtitles.py')
subs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subs)

S = 2                       # render natively at 2560x1440 for a crisp thumbnail
TW, TH = int(1280 * S), int(720 * S)
BG, DARK, ACCENT, font = bv.BG, bv.DARK, bv.ACCENT, bv.font

img = Image.new('RGBA', (TW, TH), BG + (255,))
glow = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((int(560 * S), -int(40 * S), int(1400 * S), int(800 * S)), fill=(236, 160, 115, 110))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(int(110 * S))))

# the exported .vtt file, right side, timing line circled
vtt = bv.highlight(subs.vtt, (6, 64, 394, 92), pad=6, width=6).crop((0, 0, 1060, 980))
w = min(int(600 * S), 1060)    # never upscale the retina .vtt shot
shot = vtt.resize((w, round(vtt.height * w / vtt.width)), Image.LANCZOS)
win = shot.convert('RGBA')
m = Image.new('L', win.size, 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, win.width - 1, win.height - 1), int(18 * S), fill=255)
win.putalpha(m)
x, y = int(620 * S), int(70 * S)
sh = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((x, y + int(18 * S), x + win.width, y + win.height + int(18 * S)), int(18 * S), fill=(60, 35, 15, 110))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(int(26 * S))))
img.alpha_composite(win, (x, y))

d = ImageDraw.Draw(img)
# .SRT / .VTT file chips over the window
for k, (lbl, col) in enumerate([('.SRT', DARK), ('.VTT', ACCENT)]):
    cx = int(1000 * S) + k * int(150 * S)
    d.rounded_rectangle((cx - int(66 * S), int(560 * S), cx + int(66 * S), int(640 * S)), int(18 * S), fill=col + (255,))
    d.text((cx, int(600 * S)), lbl, font=font(int(40 * S), True), fill=(255, 255, 255, 255), anchor='mm')

d.rounded_rectangle((int(56 * S), int(92 * S), int(300 * S), int(150 * S)), int(29 * S), fill=(230, 33, 23, 255))
d.polygon([(int(82 * S), int(106 * S)), (int(82 * S), int(136 * S)), (int(106 * S), int(121 * S))], fill=(255, 255, 255, 255))
d.text((int(120 * S), int(121 * S)), 'YouTube', font=font(int(34 * S), True), fill=(255, 255, 255, 255), anchor='lm')
d.text((int(52 * S), int(248 * S)), 'Download', font=font(int(98 * S), True), fill=DARK + (255,), anchor='lm')
d.text((int(52 * S), int(352 * S)), 'Subtitles', font=font(int(98 * S), True), fill=ACCENT + (255,), anchor='lm')
d.rounded_rectangle((int(56 * S), int(430 * S), int(470 * S), int(510 * S)), int(40 * S), fill=DARK + (255,))
d.text((int(263 * S), int(470 * S)), 'even without CC', font=font(int(42 * S), True), fill=(255, 255, 255, 255), anchor='mm')
lg = bv.logo.resize((int(46 * S), int(46 * S)), Image.LANCZOS)
lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(lg, (int(58 * S), int(626 * S)))
d.text((int(116 * S), int(649 * S)), 'TranscriptX.ai', font=font(int(32 * S), True), fill=DARK + (255,), anchor='lm')

out = f'{subs.OUT}/video/how-to-download-youtube-subtitles-transcriptx-thumbnail.jpg'
os.makedirs(os.path.dirname(out), exist_ok=True)
img.convert('RGB').save(out, 'JPEG', quality=95, subsampling=0, optimize=True)
print(out, os.path.getsize(out) // 1024, 'KB')
