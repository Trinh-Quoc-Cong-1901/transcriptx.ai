"""Usage: python3 build_gap.py  (reads ../urls/, writes ../doi-thu-tong-hop-trang.xlsx)
v2: tool-page gaps checked against llms.txt (live pages) + blog topic clusters that drive traffic to tool pages."""
import os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.normpath(f"{HERE}/..")                 # page/blog/_source/competitors
BLOG = os.path.normpath(f"{COMP}/../..")               # page/blog
U = f"{COMP}/urls"
OUT = f"{COMP}/doi-thu-tong-hop-trang.xlsx"
TOPICS_MD = f"{BLOG}/_blog_topics.md"

def load(p):
    return [l.strip() for l in open(p, encoding="utf-8") if l.strip()]

SITES = {
    "Otter": load(f"{U}/otter.txt"), "Descript": load(f"{U}/descript.txt"),
    "Rev": load(f"{U}/rev.txt"), "Sonix": load(f"{U}/sonix.txt"),
    "Trint": load(f"{U}/trint.txt"), "Notta": load(f"{U}/notta.txt"),
    "ElevenLabs": [l.split("\t")[1].strip() for l in open(f"{U}/elevenlabs.tsv", encoding="utf-8")],
    "TurboScribe": [u for u in load(f"{U}/turboscribe.txt") if not re.search(r"\.com/(uw/|u/tools/)", u)],
}
NAMES = list(SITES)
BLOG_RX = re.compile(r"/(blog|resources|learn|articles|help|brain|strategy-hub|creator-hub|guide)/")
SKIP_RX = re.compile(r"/(transcripts|author|authors|tag|category|news|case-study|cases|customers|webinars?)/")
def path(u): return re.sub(r"^https?://[^/]+", "", u).lower()
def is_blog(u): return bool(BLOG_RX.search(path(u) + "/")) and not SKIP_RX.search(path(u) + "/")
def is_land(u): return not BLOG_RX.search(path(u) + "/") and not SKIP_RX.search(path(u) + "/")

HEAD_FILL = PatternFill("solid", fgColor="CC582E"); HEAD_FONT = Font(bold=True, color="FFFFFF")
FILL = {"Đã có": "E2EFDA", "Đã có, thêm H2/FAQ": "E2EFDA", "Làm trang mới": "F8CBAD", "Viết blog": "FFE699",
        "Bỏ": "EDEDED", "Chờ xác minh": "DDEBF7", "Đã đăng": "E2EFDA", "Đang viết": "E2EFDA", "Có trong kế hoạch": "FFF2CC",
        "Chưa có": "F8CBAD", "P1": "F8CBAD", "P2": "FFE699", "P3": "EDEDED"}

def style(ws, widths, wrap=True, freeze="B2"):
    for c in ws[1]:
        c.fill, c.font = HEAD_FILL, HEAD_FONT
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=wrap)
            if isinstance(c.value, str) and c.value in FILL:
                c.fill = PatternFill("solid", fgColor=FILL[c.value])
    ws.row_dimensions[1].height = 40
    ws.freeze_panes = freeze
    ws.auto_filter.ref = ws.dimensions

# =============== PART 1: tool / landing pages (checked against llms.txt) ===============
# (theme, regex, việc cần làm, trang TranscriptX đang phủ, cách làm)
T = [
 ("YouTube transcript", r"youtube.*(transcri|to-text)|transcri.*youtube", "Đã có", "/youtube-transcript/, /download-youtube-transcript/", ""),
 ("YouTube subtitle download", r"youtube.*(subtitle|caption)|(subtitle|caption).*youtube", "Đã có", "/youtube-subtitle-downloader/", ""),
 ("YouTube / video summarizer", r"(video|youtube)-summar|summar.*(video|youtube)", "Đã có", "/youtube-video-summarizer/, /claude-youtube-summary/", ""),
 ("TikTok / Instagram / Facebook / X", r"(tiktok|instagram|facebook|twitter).*(transcri|to-text|caption)", "Đã có", "/tiktok-transcript/, /instagram-transcript/, /facebook-transcript/, /x-transcript/ …", ""),
 ("Audio to text", r"audio-to-text|audio-file-to-text|transcribe-audio|audio-transcription|convert-audio-to-text", "Đã có", "/audio-to-text/", ""),
 ("Video to text", r"video-to-text|video-transcription|transcribe-video", "Đã có", "/video-to-text/", ""),
 ("MP3 / WAV / M4A / AAC / OGG … to text", r"(mp3|wav|m4a|aac|ogg|flac|aiff|wma|opus|amr)-to-(text|transcript)|mp3-transcri", "Đã có, thêm H2/FAQ", "/audio-to-text/ (llms.txt: nhận MP3, WAV, M4A…)", "Không làm trang mới. Thêm H2 'MP3 to text' và FAQ cho WAV/M4A vào /audio-to-text/. Chỉ tách trang khi volume rất lớn"),
 ("MP4 / MOV / WebM to text", r"(mp4|mov|webm|mkv|avi)-to-text", "Đã có, thêm H2/FAQ", "/video-to-text/", "Như trên, thêm H2 'MP4 to text' vào /video-to-text/"),
 ("Voice to text / voice memo / dictation / voice recorder", r"voice-to-text|voice-input|voice-typing|voice-memo|dictat|voice-recorder|audio-recorder", "Đã có, thêm H2/FAQ", "/voice-to-text/ (ghi âm trên trình duyệt)", "Thêm H2/FAQ 'voice memo', 'online voice recorder'"),
 ("Voicemail / voice message", r"voicemail|voice-message|whatsapp|voice-note", "Đã có, thêm H2/FAQ", "/voicemail-to-text/", "Thêm FAQ 'WhatsApp voice message'"),
 ("Live / real-time / speech to text", r"real-?time|live-transcri|trintlive|speech-to-text(-software|-online)?/?$|convert-speech-to-text", "Đã có", "/live-transcription/, /real-time-speech-to-text/", ""),
 ("API", r"(speech|transcri)[a-z-]*-api|/api(/|$)", "Đã có", "/speech-to-text-api/, /transcription-api/ …", ""),
 ("Unlimited / large files", r"unlimited|large-(audio|file|video)|long-audio", "Đã có", "/unlimited-transcription/, /transcribe-large-audio-files/", ""),
 ("AI / free transcription (head term)", r"^/(free-)?(ai-)?transcription(-software|-tool|-service)?s?/?$|free-(ai-)?transcri|transcribe-for-free", "Đã có", "Homepage /", ""),
 ("ChatGPT / Claude", r"chatgpt|claude|gpt", "Đã có", "/transcription-mcp/, /claude-transcribe-audio/, /claude-youtube-summary/", "Lợi thế: ít đối thủ có"),
 ("Google Drive / Dropbox / OneDrive", r"dropbox|google-drive|onedrive", "Đã có, thêm H2/FAQ", "Upload từ Drive/Dropbox/OneDrive (trên mọi trang file)", "Chưa cần trang riêng"),
 ("Transcription theo ngôn ngữ", r"(transcri|speech-to-text|languages)/[a-z]+$|-(audio|video)-to-text$", "Đã có", "100+ ngôn ngữ tự nhận diện; 19 bản dịch mỗi trang", "Chỉ làm trang riêng cho ngôn ngữ đã kiểm chứng"),
 ("Audio to Word / DOCX / PDF", r"to-(microsoft-)?word|to-docx|to-pdf", "Đã có, thêm H2/FAQ", "Xuất .docx/.pdf trên mọi trang", "Viết blog how-to (xem sheet Blog)"),
 ("Podcast / Interview / Lecture / Zoom-Meet-Teams", r"podcast|interview|lecture|zoom(?!-(in|out))|google-?meet|teams-(recording|meeting)|microsoft-teams", "Viết blog", "/audio-to-text/, /video-to-text/, /live-transcription/", "Không làm tool page mới; viết blog how-to dẫn về trang file (xem sheet Blog)"),
 ("Subtitle / caption generator (file → SRT/VTT)", r"subtitle-generator|caption-generator|auto-?subtitle|auto-?caption|ai-subtitle|ai-caption|generate-(video-)?(subtitles|captions)|to-(srt|vtt)|srt-generator", "Làm trang mới", "Chưa có: /youtube-subtitle-downloader/ chỉ cho link YouTube", "Trang /subtitle-generator/: upload video → SRT/VTT. Dùng khung /youtube-subtitle-downloader/"),
 ("Caption converter (SRT ↔ VTT)", r"caption-converter|srt-to-vtt|vtt-to-srt", "Làm trang mới", "Chưa có", "Ưu tiên thấp. Có thể thay bằng blog srt-vs-vtt"),
 ("Subtitle / audio translation", r"translat", "Chờ xác minh", "", "Chỉ làm khi xác minh có dịch"),
 ("Mobile app", r"mobile-app|iphone|android|ios-app", "Chờ xác minh", "", "Xem _source/mobile/"),
 ("Meeting bot / note-taker", r"meeting-(notes|minutes|assistant|recorder)|note-?taker|ai-notes", "Bỏ", "", "Không có bot họp"),
 ("Medical / legal", r"medical|legal|court|hipaa", "Bỏ", "", ""),
 ("Downloader / file converter", r"downloader|extract-audio|to-mp3|audio-joiner|trimmer", "Bỏ", "", "Ngoài lõi, rủi ro bản quyền"),
 ("Add subtitles to video (gắn cứng)", r"add-(subtitles|captions|srt|vtt)", "Bỏ", "", "Không gắn được phụ đề vào video; làm blog how-to thay thế"),
]
tool_rows = []
for t, rx, act, tx, how in T:
    r = re.compile(rx); cells = []; n = 0; ex = []
    for s in NAMES:
        hits = [u for u in SITES[s] if is_land(u) and r.search(path(u))]
        cells.append(len(hits) or ""); n += 1 if hits else 0; ex += hits[:1]
    tool_rows.append([t] + cells + [n, act, tx, how, "\n".join(ex[:3])])
ORD = {"Làm trang mới": 0, "Đã có, thêm H2/FAQ": 1, "Viết blog": 2, "Chờ xác minh": 3, "Đã có": 4, "Bỏ": 5}
tool_rows.sort(key=lambda r: (ORD[r[len(NAMES) + 2]], -r[len(NAMES) + 1]))

# =============== PART 2: blog topic clusters ===============
topics_md = open(TOPICS_MD, encoding="utf-8").read()
PLANNED = set(re.findall(r"`(?:/blog/)?([a-z0-9-]+)/?`", topics_md))
PUBLISHED = {"how-to-get-youtube-transcript", "how-to-download-youtube-subtitles", "how-to-summarize-a-youtube-video",
             "can-chatgpt-watch-videos", "best-transcription-software", "how-long-to-transcribe-1-hour-of-audio",
             "how-to-transcribe-audio-faster"}
# every post folder with a kw.md that is not in PUBLISHED counts as a draft in progress
DRAFT = {d for d in os.listdir(BLOG) if os.path.isfile(f"{BLOG}/{d}/kw.md")} - PUBLISHED

# (cụm bài, regex trên slug, slug đề xuất của TranscriptX, trang tool nhận traffic, ghi chú)
BT = [
 ("How to get / transcribe a YouTube video transcript", r"youtube.*transcri|transcri.*youtube|youtube-to-text", "how-to-get-youtube-transcript", "/youtube-transcript/", ""),
 ("Download / turn on YouTube subtitles & captions", r"youtube.*(subtitle|caption|cc)|(subtitle|caption).*youtube", "how-to-download-youtube-subtitles", "/youtube-subtitle-downloader/", ""),
 ("Summarize a YouTube video / video", r"summar.*(video|youtube)|(video|youtube).*summar", "how-to-summarize-a-youtube-video", "/youtube-video-summarizer/", ""),
 ("Transcribe / caption TikTok", r"tiktok", "how-to-transcribe-tiktok", "/tiktok-transcript/", ""),
 ("Transcribe / caption Instagram Reels", r"instagram|reels", "how-to-transcribe-instagram-reels", "/instagram-transcript/", ""),
 ("Transcribe a Facebook video", r"facebook.*(transcri|to-text|caption)", "how-to-transcribe-facebook-video", "/facebook-transcript/", ""),
 ("How to transcribe audio to text (general / free)", r"how-to-transcribe-audio|transcribe-audio-to-text|convert-audio-to-text|audio-to-text|transcribe-audio-for-free|audio-files?-to-text", "how-to-transcribe-audio-to-text", "/audio-to-text/", "Cụm lớn, nhiều bên viết"),
 ("Convert MP3 / WAV / M4A / AMR … to text", r"(mp3|wav|m4a|aac|ogg|flac|aiff|wma|amr|opus)-(to|files?-to)-text|transcribe-(mp3|wav|m4a)", "how-to-convert-mp3-to-text", "/audio-to-text/", "Rev, Sonix viết theo từng định dạng"),
 ("How to transcribe a video / MP4", r"how-to-transcribe-(a-)?video|video-to-text|transcribe-(mp4|mov)|mp4-to-text", "how-to-transcribe-video", "/video-to-text/", ""),
 ("Transcribe in Google Docs", r"google-docs", "how-to-transcribe-audio-in-google-docs", "/audio-to-text/", ""),
 ("Transcribe in Microsoft Word / audio to Word", r"microsoft-word|in-word|to-word|word-transcri", "how-to-transcribe-audio-in-word", "/audio-to-text/", ""),
 ("How to transcribe an interview", r"interview", "how-to-transcribe-an-interview", "/audio-to-text/", "Có 'Speakers' trên Pro"),
 ("How to transcribe a podcast", r"podcast.*transcri|transcri.*podcast", "how-to-transcribe-podcast", "/audio-to-text/", ""),
 ("Transcribe Zoom / Google Meet / Teams recordings", r"zoom(?!-(in|out))|google-meet|microsoft-teams|teams-(meeting|recording|transcri)|webex|gotomeeting", "how-to-transcribe-zoom-recording", "/video-to-text/", "Chỉ góc file ghi, không có bot"),
 ("Lecture / class / student notes", r"lecture|class-notes|student.*(transcri|notes|note-taking)|study-notes", "how-to-transcribe-a-lecture", "/live-transcription/", ""),
 ("Voice memo (iPhone) to text", r"voice-memo", "how-to-transcribe-voice-memos", "/voice-to-text/", ""),
 ("Voicemail / WhatsApp voice message to text", r"voicemail|voice-message|whatsapp|voice-note", "whatsapp-voice-message-to-text", "/voicemail-to-text/", ""),
 ("Dictation / speech to text on iPhone, Mac, Windows", r"dictat|speech-to-text-(on|for|in)-|voice-typing|talk-to-text|voice-to-text-on", "how-to-use-speech-to-text-on-iphone", "/voice-to-text/", ""),
 ("How to add subtitles / captions to a video", r"(add|burn|embed)-(subtitles|captions|srt)|how-to-(add|put)-(subtitles|captions)", "how-to-add-subtitles", "/youtube-subtitle-downloader/ (SRT)", "Rev, Descript có hàng trăm bài theo từng phần mềm/nền tảng"),
 ("SRT / VTT files explained, SRT vs VTT", r"srt|vtt|subtitle-file|caption-file|caption-format", "srt-vs-vtt", "/youtube-subtitle-downloader/", ""),
 ("Closed captions vs subtitles / caption basics", r"closed-caption|captions-vs-subtitles|subtitles-vs-captions|open-captions|what-are-captions", "captions-vs-subtitles", "/youtube-subtitle-downloader/", ""),
 ("Transcript with timestamps", r"timestamp", "transcript-with-timestamps", "/download-youtube-transcript/", ""),
 ("Speaker identification / diarization", r"speaker-(identification|diarization|label)|diarization|multiple-speakers", "speaker-identification-transcription", "/audio-to-text/", "Tính năng Pro"),
 ("Transcription accuracy / AI vs human", r"accura|ai-vs-human|human-vs-ai|word-error-rate", "transcription-accuracy-benchmark", "/audio-to-text/", "Chỉ viết khi tự đo"),
 ("How long / how much does transcription cost", r"how-long.*transcri|transcri.*(cost|price|pricing|rates|per-minute)|(cost|price|pricing|rates).*transcri", "transcription-cost-per-minute", "/pricing/", ""),
 ("Transcript formatting / verbatim vs clean", r"verbatim|format.*transcri|transcri.*format|clean-verbatim|transcription-style", "verbatim-vs-clean-verbatim", "/audio-to-text/", "Bài kiến thức, dễ được AI search trích"),
 ("What is transcription / speech recognition / ASR", r"what-is-(transcription|speech|asr|automatic-speech)|speech-recognition|automatic-speech", "what-is-speech-to-text", "/", ""),
 ("Multilingual / language detection / translate transcript", r"multilingual|language-detection|translate-(audio|video|transcript|subtitles)", "auto-language-detection", "/audio-to-text/", "Dịch: chờ xác minh"),
 ("ChatGPT / Whisper / Claude for transcription", r"chatgpt|whisper|claude|openai", "can-chatgpt-transcribe-audio", "/transcription-mcp/", "Lợi thế MCP"),
 ("Is online transcription safe / legal", r"transcri.*(secur|privacy|safe|confidential)|(secur|privacy|safe|confidential).*transcri|legal-to-(transcribe|record)|record.*without.*(permission|consent)", "is-online-transcription-safe", "/", ""),
 ("Repurpose video → blog post / content", r"repurpos|video-to-blog|blog-post-from|turn-.*-into-(blog|article)", "youtube-video-to-blog-post", "/youtube-transcript/", ""),
 ("Meeting notes / minutes templates", r"meeting-(notes|minutes)|minutes-template|meeting-summary|meeting-recap", "meeting-minutes-template", "/audio-to-text/", "Traffic lớn nhưng khách tìm bot họp: chuyển đổi thấp"),
 ("Best transcription software / apps", r"best-.*(transcri|speech-to-text|dictation|caption|subtitle|voice-to-text)", "best-transcription-software", "/", "Đã có 1 bài; còn best free, best iPhone…"),
 ("Alternatives", r"alternative", "otter-alternative", "/", "Kế hoạch BOFU"),
 ("X vs Y", r"(transcri|otter|rev|descript|sonix|trint|notta|fireflies|scribe|whisper|caption|subtitle|speech-to-text|tactiq|fathom).*-vs-|-vs-.*(transcri|otter|rev|descript|sonix|trint|notta|fireflies|scribe|whisper|caption|subtitle|speech-to-text|tactiq|fathom)", "otter-vs-fireflies", "/", "Kế hoạch BOFU"),
 ("Become a transcriptionist / transcription jobs", r"transcriptionist|transcription-jobs|become-a-transcri|practice-transcri|typing-speed", "", "", "Bỏ: traffic không chuyển đổi"),
 ("Medical / legal transcription", r"medical|legal|court|law-enforcement|deposition|hipaa", "", "", "Bỏ"),
]
blog_urls = {s: [u for u in SITES[s] if is_blog(u)] for s in NAMES}
blog_rows, blog_url_rows = [], []
for name, rx, slug, tool, note in BT:
    r = re.compile(rx); cells = []; n = 0; total = 0; ex = []
    for s in NAMES:
        hits = [u for u in blog_urls[s] if r.search(path(u).rstrip("/").rsplit("/", 1)[-1])]
        cells.append(len(hits) or ""); n += 1 if hits else 0; total += len(hits); ex += hits[:1]
        blog_url_rows += [(name, s, u) for u in hits]
    if not slug:
        status, pr = "Bỏ", "Bỏ"
    elif slug in PUBLISHED:
        status, pr = "Đã đăng", "—"
    elif slug in DRAFT:
        status, pr = "Đang viết", "—"
    elif slug in PLANNED:
        status = "Có trong kế hoạch"
        pr = "P1" if n >= 5 else "P2" if n >= 3 else "P3"
    else:
        status = "Chưa có"
        pr = "P1" if n >= 5 else "P2" if n >= 3 else "P3"
    if "chuyển đổi thấp" in note and pr == "P1":
        pr = "P3"
    blog_rows.append([name] + cells + [n, total, status, pr, slug, tool, note, "\n".join(ex[:3])])
BO = {"P1": 0, "P2": 1, "P3": 2, "—": 3, "Bỏ": 4}
blog_rows.sort(key=lambda r: (BO[r[len(NAMES) + 4]], -r[len(NAMES) + 1], -r[len(NAMES) + 2]))

# =============== write ===============
wb = Workbook(); wb.remove(wb.active)

ws = wb.create_sheet("Blog kéo traffic")
ws.append(["Cụm bài blog"] + [f"{s}\n(số bài)" for s in NAMES] +
          ["Số đối thủ viết", "Tổng số bài", "TranscriptX", "Ưu tiên", "Slug đề xuất", "Dẫn traffic về trang", "Ghi chú", "Ví dụ bài đối thủ"])
for r in blog_rows: ws.append(r)
style(ws, [40] + [10] * len(NAMES) + [10, 9, 16, 8, 34, 28, 36, 60])

ws = wb.create_sheet("Tool page (đã sửa)")
ws.append(["Loại trang"] + [f"{s}\n(landing)" for s in NAMES] + ["Số đối thủ có", "Việc cần làm", "TranscriptX đang phủ bằng", "Cách làm", "Ví dụ URL đối thủ"])
for r in tool_rows: ws.append(r)
style(ws, [40] + [10] * len(NAMES) + [10, 18, 40, 52, 60])

ws = wb.create_sheet("URL blog đối thủ theo cụm")
ws.append(["Cụm bài", "Đối thủ", "URL"])
for r in blog_url_rows: ws.append(r)
style(ws, [44, 12, 100], wrap=False, freeze="A2")

ws = wb.create_sheet("Ghi chú")
ws.append(["Mục", "Nội dung"])
for r in [
    ("Nguồn", "Sitemap của Otter, Descript, Rev, Sonix, Trint, Notta, ElevenLabs, TurboScribe, lấy ngày 2026-11-04. Happy Scribe chặn bot (403) nên chưa có."),
    ("Cách làm", "Chỉ đọc URL, không mở nội dung trang. Gán cụm bằng từ khoá trong URL nên có thể lệch một ít."),
    ("Trang TranscriptX", "Đối chiếu với page/llms.txt (danh sách trang đang chạy) và page/blog/_blog_topics.md (kế hoạch blog)."),
    ("Blog: Ưu tiên", "P1: ≥5 đối thủ viết, P2: 3–4, P3: ≤2. Cụm đã đăng ghi '—'. Cột 'Dẫn traffic về trang' = tool page mà bài phải link về (CTA)."),
    ("Tool page: Việc cần làm", "'Đã có' = giữ nguyên. 'Đã có, thêm H2/FAQ' = trang hiện có đã làm được việc này, chỉ cần thêm keyword. 'Viết blog' = không làm trang mới, viết bài dẫn về trang có. 'Làm trang mới' = chỉ khi chưa có trang nào làm việc đó."),
]: ws.append(r)
style(ws, [22, 120], freeze="A2")

wb.save(OUT)
print("BLOG"); [print(r[len(NAMES) + 4], "|", r[0], "| sites", r[len(NAMES) + 1], "posts", r[len(NAMES) + 2], "|", r[len(NAMES) + 3]) for r in blog_rows]
print("TOOL"); [print(r[len(NAMES) + 2], "|", r[0], "|", r[len(NAMES) + 1]) for r in tool_rows]
