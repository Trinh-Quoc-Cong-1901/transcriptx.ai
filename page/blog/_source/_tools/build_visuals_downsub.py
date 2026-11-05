"""Article images for downsub-alternative.
Crop real TranscriptX screenshots at native retina pixels (no resize), draw orange outlines after cropping,
save lossless WebP (fallback lossy q95 only if > 900 KB)."""
import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(f'{HERE}/..')
OUT = os.path.normpath(f'{HERE}/../../downsub-alternative/images')
CHECK = sys.argv[1] if len(sys.argv) > 1 else None
ACCENT = (204, 88, 46)
os.makedirs(OUT, exist_ok=True)


def shot(path, crop, rings, name, width=7, pad=10, radius=22):
    im = Image.open(f'{SRC}/{path}').convert('RGB').crop(crop)
    d = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in rings:
        d.rounded_rectangle((x0 - crop[0] - pad, y0 - crop[1] - pad, x1 - crop[0] + pad, y1 - crop[1] + pad),
                            radius, outline=ACCENT, width=width)
    f = f'{OUT}/{name}'
    im.save(f, 'WEBP', lossless=True, quality=100, method=6)
    if os.path.getsize(f) > 900 * 1024:
        im.save(f, 'WEBP', quality=95, method=6)
    if CHECK:
        im.crop((0, 0, min(900, im.width), min(500, im.height))).save(f'{CHECK}/{name}_100pct.png')
    print(name, im.size, os.path.getsize(f) // 1024, 'KB')


# 1. Tool page: the "Paste a YouTube video URL..." box (plus Works with row for context)
shot('youtube-subtitle-downloader/youtube-subtitle-downloader-tool.png', (600, 260, 1745, 650),
     [(653, 384, 1692, 580)], 'downsub-alternative-youtube-subtitle-downloader.webp')

# 2. Result page: Download button (next to Copy) and the .srt / .vtt rows of the open menu
shot('transcript/transcript-download-menu-open.png', (380, 30, 1410, 470),
     [(1180, 126, 1228, 174), (966, 346, 1222, 446)], 'downsub-alternative-download-srt-vtt.webp', pad=8)

# 3. The exported .vtt file: title bar and the first cues, first timing line outlined
shot('export-files/export-vtt-file.png', (0, 0, 1060, 470),
     [(4, 64, 396, 88)], 'downsub-alternative-vtt-subtitle-file.webp', width=5, pad=4, radius=10)
