"""YouTube thumbnail (1280x720) for the how-to-get-youtube-transcript walkthrough video."""
import importlib.util, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)

TW, TH = 1280, 720
BG, DARK, ACCENT, font = bv.BG, bv.DARK, bv.ACCENT, bv.font

img = Image.new('RGBA', (TW, TH), BG + (255,))
glow = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((560, -40, 1400, 800), fill=(236, 160, 115, 110))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))

# result screenshot in a browser window, right side, slightly oversized for punch
res = bv.gif_frames[40]
w = 760
h = round(res.height * w / res.width)
shot = res.resize((w, h), Image.LANCZOS)
bar = 34
win = Image.new('RGBA', (w, h + bar), (236, 233, 226, 255))
win.paste(shot, (0, bar))
d = ImageDraw.Draw(win)
for k, c in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
    d.ellipse((16 + k * 22, 11, 30 + k * 22, 25), fill=c)
m = Image.new('L', win.size, 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, win.width - 1, win.height - 1), 18, fill=255)
win.putalpha(m)
# orange ring on the timestamped text so the eye lands on the result
ImageDraw.Draw(win).rounded_rectangle((50, bar + 92, 520, bar + 290), 14, outline=ACCENT + (255,), width=5)
sh = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
x, y = 560, 120
ImageDraw.Draw(sh).rounded_rectangle((x, y + 18, x + w, y + h + bar + 18), 18, fill=(60, 35, 15, 110))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)))
img.alpha_composite(win, (x, y))

d = ImageDraw.Draw(img)
# YouTube-red chip + headline
d.rounded_rectangle((56, 92, 300, 150), 29, fill=(230, 33, 23, 255))
d.polygon([(82, 106), (82, 136), (106, 121)], fill=(255, 255, 255, 255))
d.text((120, 121), 'YouTube', font=font(34, True), fill=(255, 255, 255, 255), anchor='lm')
d.text((52, 248), 'Video to', font=font(98, True), fill=DARK + (255,), anchor='lm')
d.text((52, 352), 'Transcript', font=font(98, True), fill=ACCENT + (255,), anchor='lm')
# "in 6 seconds" sticker
d.rounded_rectangle((56, 430, 400, 510), 40, fill=DARK + (255,))
d.text((228, 470), 'in seconds', font=font(46, True), fill=(255, 255, 255, 255), anchor='mm')
d.text((60, 566), 'TXT · DOCX · PDF · SRT · VTT', font=font(30, True), fill=(95, 90, 82, 255), anchor='lm')
lg = bv.logo.resize((46, 46), Image.LANCZOS)
lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(lg, (58, 626))
d.text((116, 649), 'TranscriptX.ai', font=font(32, True), fill=DARK + (255,), anchor='lm')

out = f'{bv.OUT}/video/how-to-get-youtube-transcript-transcriptx-thumbnail.jpg'
img.convert('RGB').save(out, 'JPEG', quality=90)
print(out, os.path.getsize(out) // 1024, 'KB')
