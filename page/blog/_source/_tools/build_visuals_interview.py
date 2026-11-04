"""Screenshots for the blog post how-to-transcribe-an-interview.

Crops real TranscriptX screenshots from _source at native pixels (no resizing),
draws an orange (#CC582E) rounded outline on the part that matters, and saves
lossless WebP into the post's images/ folder.

Run: python3 page/blog/_source/_tools/build_visuals_interview.py
"""
import pathlib
from PIL import Image, ImageDraw

SRC = pathlib.Path(__file__).resolve().parents[1]
OUT = SRC.parent / "how-to-transcribe-an-interview" / "images"
ORANGE = (204, 88, 46)

# name: (source, crop box, [outline boxes in source coords], line width)
SHOTS = {
    "upload-interview-recording-transcriptx.webp":
        ("upload/upload-source-options.png", (0, 0, 528, 418), [(62, 7, 514, 316)], 5),
    "record-interview-in-browser.webp":
        ("record/recording-in-progress.png", (820, 340, 1520, 1000), [(1000, 380, 1340, 545), (1118, 878, 1222, 980)], 6),
    "interview-transcript-with-timestamps.webp":
        ("record/recording-transcript-result.png", (380, 30, 1420, 560), [(398, 228, 506, 258), (398, 396, 506, 426)], 5),
    "interview-notes-tab-transcriptx.webp":
        ("transcript/transcript-notes-tab.png", (470, 40, 1995, 760), [(1470, 368, 1965, 560)], 6),
    "download-interview-transcript-docx.webp":
        ("transcript/transcript-download-menu-open.png", (380, 30, 1420, 470), [(1178, 124, 1230, 176), (972, 240, 1216, 288)], 5),
}

def build(name, src, crop, boxes, width):
    im = Image.open(SRC / src).convert("RGB").crop(crop)
    # add a margin in the page colour so outlines near the edge are never clipped
    M = 28
    canvas = Image.new("RGB", (im.width + 2 * M, im.height + 2 * M), im.getpixel((im.width - 2, im.height // 2)))
    canvas.paste(im, (M, M)); im = canvas
    crop = (crop[0] - M, crop[1] - M)
    d = ImageDraw.Draw(im)
    for (x0, y0, x1, y1) in boxes:
        pad = 8
        box = (x0 - crop[0] - pad, y0 - crop[1] - pad, x1 - crop[0] + pad, y1 - crop[1] + pad)
        d.rounded_rectangle(box, radius=16, outline=ORANGE, width=width)
    out = OUT / name
    im.save(out, "WEBP", lossless=True, quality=100, method=6)
    if out.stat().st_size > 900_000:
        im.save(out, "WEBP", quality=95, method=6)
    print(name, im.size, f"{out.stat().st_size // 1024} KB")

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n, (s, c, b, w) in SHOTS.items():
        build(n, s, c, b, w)
