"""Cover + og:image for downsub-alternative (hook style: kicker + concrete number + payoff question).
Hook (user, 2026-11-04): get subtitles from a video that has no captions.
"Video has no captions?" / "GET SUBTITLES" / "anyway." - no claim about DownSub's own result.
Visual: a real .vtt file exported from TranscriptX (the subtitles you get)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cover_kit import make_hook_cover

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'downsub-alternative'
out = make_hook_cover(
    SLUG, os.path.normpath(f'{HERE}/../../{SLUG}/images'),
    kicker='Video has no captions?',
    big='GET SUBTITLES',
    small='anyway.',
    shot='export-files/export-vtt-file.png',
    crop=(0, 0, 900, 560),                 # file title bar + first timed cues
    scale=1.25,
    check_dir=sys.argv[1] if len(sys.argv) > 1 else None,
)
for f in out:
    print(f, os.path.getsize(f) // 1024, 'KB')
