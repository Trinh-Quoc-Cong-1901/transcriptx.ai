"""YouTube thumbnail (2560x1440, rendered natively) for the Summary / Mind map preview video."""
import importlib.util, os
os.environ['SKIP_VO'] = '1'
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('mm', f'{HERE}/build_video_summary_mind_map.py')
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)
bv = mm.bv
S = 2
TW, TH = 1280 * S, 720 * S
BG, DARK, ACCENT, font = bv.BG, bv.DARK, bv.ACCENT, bv.font

img = Image.new('RGBA', (TW, TH), BG + (255,))
glow = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((560 * S, -40 * S, 1400 * S, 800 * S), fill=(236, 160, 115, 110))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110 * S)))

# real transcript page with the Summary preview: 00:40 clicked, paragraph highlighted (shown at native size, no upscale)
x0, y0, x1, y1 = mm.chip_box(2)
st = bv.highlight(mm.app('summary', summary=(1.0, 2), hl=2, hl_a=1.0, t_sec=40.11), (x0, y0, x1, y1), pad=8, width=7)
shot = st.crop((1452, 360, 2000, 1110))                     # just the Summary panel: tabs, overview, key points
shot = shot.resize((round(shot.width * 1.3), round(shot.height * 1.3)), Image.LANCZOS)   # 1.3x of retina = max
win = shot.convert('RGBA')
m = Image.new('L', win.size, 0)
ImageDraw.Draw(m).rounded_rectangle((0, 0, win.width - 1, win.height - 1), 18 * S, fill=255)
win.putalpha(m)
x, y = TW - win.width - 110 * S, 200 * S
sh = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((x, y + 18 * S, x + win.width, y + win.height + 18 * S), 18 * S, fill=(60, 35, 15, 110))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26 * S)))
img.alpha_composite(win, (x, y))

d = ImageDraw.Draw(img)
d.rounded_rectangle((56 * S, 92 * S, 300 * S, 150 * S), 29 * S, fill=(230, 33, 23, 255))
d.polygon([(82 * S, 106 * S), (82 * S, 136 * S), (106 * S, 121 * S)], fill=(255, 255, 255, 255))
d.text((120 * S, 121 * S), 'YouTube', font=font(34 * S, True), fill=(255, 255, 255, 255), anchor='lm')
d.text((52 * S, 250 * S), 'Summarize', font=font(92 * S, True), fill=DARK + (255,), anchor='lm')
d.text((52 * S, 350 * S), 'any video', font=font(92 * S, True), fill=ACCENT + (255,), anchor='lm')
for k, lbl in enumerate(['Notes', 'Summary', 'Mind map']):
    yy = 440 * S + k * 62 * S
    d.rounded_rectangle((56 * S, yy, 56 * S + 46 * S, yy + 46 * S), 12 * S, fill=ACCENT + (255,))
    d.line([(68 * S, yy + 24 * S), (77 * S, yy + 33 * S), (92 * S, yy + 15 * S)], fill=(255, 255, 255, 255), width=5 * S // 2)
    d.text((118 * S, yy + 23 * S), lbl, font=font(40 * S, True), fill=DARK + (255,), anchor='lm')
d.rounded_rectangle((x + 4 * S, y - 86 * S, x + 264 * S, y - 30 * S), 28 * S, fill=DARK + (255,))
d.text((x + 134 * S, y - 58 * S), 'COMING SOON', font=font(30 * S, True), fill=(255, 255, 255, 255), anchor='mm')
lg = bv.logo.resize((46 * S, 46 * S), Image.LANCZOS)
lg.putalpha(lg.convert('L').point(lambda v: 0 if v > 235 else 255))
img.alpha_composite(lg, (58 * S, 626 * S))
d.text((116 * S, 649 * S), 'TranscriptX.ai', font=font(32 * S, True), fill=DARK + (255,), anchor='lm')

out = f'{mm.OUT}/video/{mm.BASE}-thumbnail.jpg'
img.convert('RGB').save(out, 'JPEG', quality=95, subsampling=0, optimize=True)
img.convert('RGB').crop((TW // 2, TH // 4, TW // 2 + 900, TH // 4 + 700)).save(
    '/private/tmp/claude-501/-Users-trinhquoccong-Documents-seo-main-TranscriptX-ai/ea9bc2ca-d557-4155-bd4f-5b5af8927b38/scratchpad/thumb_100pct.png')
print(out, os.path.getsize(out) // 1024, 'KB')
