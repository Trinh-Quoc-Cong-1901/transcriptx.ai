"""Share image (cover + og:image) for what-is-medical-transcription: ONE PNG, hook style.
Hook: kicker "Dictated note" + giant "Celexa" + orange "or Celebrex?" (common sound-alike drug pair).
Focal visual: the real Record transcript screen, with its paragraph text replaced by a made-up
clinic dictation (no real patient) so the picture matches the topic. Timestamps and UI are untouched."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import make_hook_cover, retext_shot

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'what-is-medical-transcription'
SHOT, CROP = 'record/recording-transcript-result.png', (395, 215, 1390, 545)
img = retext_shot(SHOT, CROP, [
    'Patient seen for follow-up of hypertension. Denies chest pain or shortness of breath. '
    'Current medication: Celexa 20 mg once daily.',
    'Blood pressure today 138 over 86. Plan: continue lisinopril 10 mg daily and recheck '
    'in three months.',
], line_tops=(58, 226), max_w=750)   # wrap inside the part of the card that stays on canvas
if len(sys.argv) > 1:
    img.save(f'{sys.argv[1]}/{SLUG}_shot_retext.png')
out = make_hook_cover(
    SLUG, os.path.normpath(f'{HERE}/../../{SLUG}/images'),
    kicker='Dictated note', big='Celexa', small='or Celebrex?',
    shot=SHOT, crop=CROP, shot_img=img, scale=1.3, png_only=True,
    check_dir=sys.argv[1] if len(sys.argv) > 1 else None,
)
for f in out:
    print(f, os.path.getsize(f) // 1024, 'KB')
