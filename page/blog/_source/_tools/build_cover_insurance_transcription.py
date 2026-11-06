"""Share image (one PNG, cover + og:image) for the insurance transcription post (page/blog/insurance-transcription/).
Hook: kicker "The claimant said" + giant "$1,500" + orange "or $5,000?" (amounts check from the post's
"What to check" table; an example, not a product claim).
Focal visual: the real Record transcript screen, with its paragraph text replaced by a made-up recorded
statement (no real claim or person) so the picture matches the topic. Timestamps and UI are untouched.
Usage: python3 build_cover_insurance_transcription.py [check_dir]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import make_hook_cover, retext_shot

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'insurance-transcription'
SHOT, CROP = 'record/recording-transcript-result.png', (395, 215, 1390, 545)
img = retext_shot(SHOT, CROP, [
    'This is a recorded statement for your auto claim, taken by phone with your permission. '
    'Can you tell me what happened?',
    'I was stopped at the light on Main Street when the other car hit my rear bumper. '
    'The body shop estimate came to $1,500.',
], line_tops=(58, 226), max_w=750)   # wrap inside the part of the card that stays on canvas
check = sys.argv[1] if len(sys.argv) > 1 else None
if check:
    img.save(f'{check}/{SLUG}_shot_retext.png')
out = make_hook_cover(
    SLUG, os.path.normpath(f'{HERE}/../../{SLUG}/images'),
    kicker='The claimant said', big='$1,500', small='or $5,000?',
    shot=SHOT, crop=CROP, shot_img=img, scale=1.3, png_only=True,
    check_dir=check,
)
for f in out:
    print(f, os.path.getsize(f) // 1024, 'KB')
