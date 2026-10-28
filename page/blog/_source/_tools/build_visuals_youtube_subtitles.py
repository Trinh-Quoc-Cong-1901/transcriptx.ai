"""Static images for how-to-download-youtube-subtitles (reuses helpers from build_visuals_youtube_transcript.py)."""
import importlib.util, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('bv', f'{HERE}/build_visuals_youtube_transcript.py')
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)

OUT = f'{bv.ROOT}/how-to-download-youtube-subtitles/images'
os.makedirs(OUT, exist_ok=True)

sub_tool = bv.load('youtube-subtitle-downloader/youtube-subtitle-downloader-tool.png')   # 2000x999
vtt = bv.load('export-files/export-vtt-file.png')                                        # 1376x1556

SUB_INPUT = (653, 384, 1692, 580)
DL_BTN = (1180, 126, 1228, 174)            # transcript-result-light / download-menu-open (2000px)
SUBTITLE_ROWS = (966, 346, 1222, 446)      # .srt + .vtt rows in the open menu


def save(img, name, width=1600):
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(f'{OUT}/{name}', 'WEBP', quality=84)
    print(name, img.size, os.path.getsize(f'{OUT}/{name}') // 1024, 'KB')


def phone_duo_download():
    """Phone home + phone result, with the bottom-bar Download button highlighted."""
    res = bv.highlight(bv.m_result, (425, 1218, 491, 1282), pad=6, width=4)
    canvas = Image.new('RGBA', (1600, 1000), bv.BG + (255,))
    a, b = bv.phone(bv.m_home, 860), bv.phone(res, 860)
    gap = 90
    x = (1600 - a.width - b.width - gap + 80) // 2
    canvas.alpha_composite(a, (x - 40, 30))
    canvas.alpha_composite(b, (x + a.width - 80 + gap, 30))
    return canvas.convert('RGB')


def vtt_window():
    """Top of the exported .vtt file, in a soft frame."""
    crop = vtt.crop((0, 0, 1060, 760))
    crop = bv.highlight(crop, (6, 64, 394, 92), pad=6, width=4)
    pad = 40
    canvas = Image.new('RGB', (crop.width + pad * 2, crop.height + pad * 2), bv.BG)
    canvas.paste(crop, (pad, pad))
    return canvas


if __name__ == '__main__':
    save(bv.highlight(sub_tool, SUB_INPUT, pad=8), 'youtube-subtitle-downloader-paste-link.webp')
    save(bv.highlight(bv.result, DL_BTN, pad=8), 'youtube-subtitles-download-button-next-to-copy.webp')
    save(bv.highlight(bv.highlight(bv.dl, SUBTITLE_ROWS, pad=4), DL_BTN, pad=6), 'download-youtube-subtitles-srt-vtt.webp')
    save(vtt_window(), 'youtube-subtitles-vtt-file-example.webp', width=1200)
    save(phone_duo_download(), 'download-youtube-subtitles-on-phone.webp')
