"""Share image (cover + og:image) for the financial transcription post (page/blog/finance-transcription/):
ONE PNG, hook style. Hook: kicker "Earnings call transcript" + giant "15% or 50%?" + orange "One wrong digit."
(the post's core angle: a misheard figure; example numbers, not a product claim).
Focal visual: the real transcript screen, with its paragraph text replaced by a made-up earnings call
excerpt (fictional company) so the picture matches the topic. Timestamps and UI are untouched."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import make_hook_cover, retext_shot

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'what-is-financial-transcription'
SHOT, CROP = 'record/recording-transcript-result.png', (395, 215, 1390, 545)
img = retext_shot(SHOT, CROP, [
    'CFO: Revenue for the third quarter was 412 million dollars, up 15% year over year. '
    'Gross margin improved by 40 basis points.',
    'Analyst: Thanks. Can you walk us through the full-year guidance and what you expect '
    'for margins in the second half?',
], line_tops=(58, 226), max_w=750)
if len(sys.argv) > 1:
    img.save(f'{sys.argv[1]}/{SLUG}_shot_retext.png')
out = make_hook_cover(
    SLUG, os.path.normpath(f'{HERE}/../../finance-transcription/images'),
    kicker='Earnings call transcript', big='15% or 50%?', small='One wrong digit.',
    shot=SHOT, crop=CROP, shot_img=img, scale=1.3, png_only=True,
    check_dir=sys.argv[1] if len(sys.argv) > 1 else None,
)
for f in out:
    print(f, os.path.getsize(f) // 1024, 'KB')
