"""Cover + og:image for how-to-transcribe-an-interview: hook style, no strike/arrow/ring.
Hook: kicker "1-hour interview" + giant "4 HOURS" + "of typing?" (user prefers a concrete number).
Claim source: Pricing page "Typing up 1 hour of audio takes about 4 hours" (_source/_index.md)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import make_hook_cover

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'how-to-transcribe-an-interview'
out = make_hook_cover(
    SLUG, os.path.normpath(f'{HERE}/../../{SLUG}/images'),
    kicker='1-hour interview',
    big='4 HOURS',
    small='of typing?',
    shot='record/recording-transcript-result.png',
    crop=(395, 215, 1390, 545),            # just the transcript: two timestamped paragraphs (bleeds off the right edge)
    scale=1.3,
    check_dir=sys.argv[1] if len(sys.argv) > 1 else None,
)
for f in out:
    print(f, os.path.getsize(f) // 1024, 'KB')
