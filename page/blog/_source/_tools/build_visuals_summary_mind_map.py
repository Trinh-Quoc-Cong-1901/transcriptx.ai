"""Static images for how-to-summarize-a-youtube-video: native retina pixels, tight crops, lossless WebP, orange outline.

Real screens: YouTube Transcript tool, transcript page (Copy), Download menu, Use in ChatGPT & Claude page.
Previews (coming soon): Summary with timestamps and Mind map, drawn on the real transcript page by
build_video_summary_mind_map.app(); the article text says they are previews.
"""
import importlib.util, os
os.environ['SKIP_VO'] = '1'
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('mm', f'{HERE}/build_video_summary_mind_map.py')
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)
bv = mm.bv
OUT = mm.OUT
hl = bv.highlight


def save(img, name):
    """Native pixels (no resize), lossless; lossy q95 only if the file passes ~900 KB."""
    path = f'{OUT}/{name}'
    img = img.convert('RGB')
    img.save(path, 'WEBP', lossless=True, quality=100, method=6)
    if os.path.getsize(path) > 900 * 1024:
        img.save(path, 'WEBP', quality=95, method=6)
    print(name, img.size, os.path.getsize(path) // 1024, 'KB')


# 1. paste the link on the YouTube Transcript page
save(hl(bv.load('youtube-transcript/youtube-transcript-tool.png').crop((480, 240, 1870, 720)),
        bv.shift(bv.TOOL_INPUT, (-480, -240)), pad=8), 'summarize-youtube-video-paste-link.webp')

# 2. transcript page, Copy button
save(hl(mm.APP.crop((436, 0, 2000, 760)), (1212 - 436, 160, 1385 - 436, 222), pad=8), 'youtube-transcript-copy-button.webp')

# 3. Download menu (separate button next to Copy)
menu = Image.open(f'{bv.SRC}/transcript/download-format-menu.png').convert('RGBA').crop((0, 0, 401, 397))   # drop page text under the menu
card = Image.new('RGB', (menu.width + 80, menu.height + 80), (250, 249, 245))
card.paste(menu, (40, 40), menu)
save(card, 'youtube-transcript-download-formats.webp')

# 4. Notes tab with notes typed next to the transcript
notes = mm.app('notes', notes=(mm.NOTE_CHARS, False))
save(hl(notes.crop((960, 330, 2000, 830)), (1470 - 960, 365 - 330, 1990 - 960, 760 - 330), pad=6), 'transcriptx-notes-next-to-transcript.webp')

# 5. Summary preview: key points with timestamps, 00:40 clicked -> paragraph highlighted
x0, y0, x1, y1 = mm.chip_box(2)
summ = mm.app('summary', summary=(1.0, 2), hl=2, hl_a=1.0, t_sec=40.11)
save(hl(summ.crop((436, 360, 2000, 1273)), (x0 - 436, y0 - 360, x1 - 436, y1 - 360), pad=8), 'transcriptx-summary-timestamps-preview.webp')

# 6. Mind map preview
mind = mm.app('mindmap', mindmap=1.0, scroll=mm.S_TOP, t_sec=96.51)
save(mind.crop((436, 230, 2000, 1273)), 'transcriptx-mind-map-preview.webp')
