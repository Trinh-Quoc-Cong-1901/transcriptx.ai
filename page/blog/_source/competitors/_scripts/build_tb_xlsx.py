import re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

SRC, OUT = sys.argv[1], sys.argv[2]
BASE = "https://turboscribe.com"
paths = [l.strip() for l in open(SRC, encoding="utf-8") if l.strip()]

def classify(p):
    s = p.lstrip("/")
    if re.match(r"^uw?/tools/", s): return "Landing /u/tools/ + /uw/tools/ (bản trùng)", "Programmatic"
    if re.match(r"^uw/", s): return "Landing /uw/ (bản trùng của /u/)", "Programmatic"
    if re.match(r"^u/(convert|transcribe)-[a-z-]+-audio-to-text$", s) and not re.search(r"(speech|video|audio-and-video)", s.split("/")[1][:20]):
        return "Landing theo ngôn ngữ (/u/)", "Programmatic"
    if s.startswith("u/"): return "Landing use case / định dạng (/u/)", "Landing"
    if re.match(r"^(transcription|speech-to-text|free-transcription|convert-audio-to-text)/", s): return f"Trang theo ngôn ngữ (/{s.split('/')[0]}/)", "Programmatic"
    if s.startswith("transcription-"): return "Trang theo thành phố Mỹ", "Programmatic"
    if s.startswith("l/") and s.endswith("-alternative"): return "Alternative (/l/)", "So sánh"
    if s.startswith("l/"): return "Landing keyword (/l/)", "Landing"
    if s.startswith("learn/") and "-vs-" in s: return "X vs Y (/learn/)", "So sánh"
    if s.startswith("learn/"): return "Bài hướng dẫn (/learn/)", "Blog"
    if s.startswith("blog/"): return "Blog sản phẩm", "Blog"
    if s.startswith("help/"): return "Help", "Help"
    if s.startswith("advisory/"): return "Cảnh báo khách hàng", "Khác"
    if s.startswith("free-"): return "Landing free-* theo use case", "Landing"
    if s.startswith("downloader/"): return "Downloader (tải video/audio)", "Tool phụ"
    if s.startswith("convert/"): return "Đổi định dạng audio (không ra text)", "Tool phụ"
    return "Trang hệ thống", "Khác"

rows = []
for p in paths:
    g, kind = classify(p)
    rows.append((kind, g, BASE + p, p))

# ----- Ý tưởng cho TranscriptX: (URL mẫu của TurboScribe, cụm, TranscriptX đã có?, trang TranscriptX, đề xuất, loại nội dung, ưu tiên)
IDEAS = [
 ("/l/youtube-transcript-generator", "YouTube transcript", "Có", "/youtube-transcript/", "Đã có", "Tool page", "—"),
 ("/u/transcribe-youtube-video", "YouTube transcript", "Có", "/youtube-transcript/", "Đã có", "Tool page", "—"),
 ("/l/youtube-captions-and-subtitles", "YouTube subtitles", "Có", "/youtube-subtitle-downloader/", "Đã có", "Tool page", "—"),
 ("/l/audio-to-text", "Audio to text", "Có", "/audio-to-text/", "Đã có. Họ có hơn 15 biến thể (/l/transcribe-audio-to-text, /l/turn-audio-into-text…). Gom vào H2/FAQ của trang mình", "Tool page", "—"),
 ("/l/video-to-text", "Video to text", "Có", "/video-to-text/", "Đã có", "Tool page", "—"),
 ("/l/voice-to-text", "Voice to text", "Có", "/voice-to-text/", "Đã có", "Tool page", "—"),
 ("/l/mp3-to-text", "MP3 to text", "Chưa có", "", "Tool page /mp3-to-text/ (họ có 4 trang: mp3-to-text, ai-mp3-to-text, instant-mp3-to-text, transcribe-mp3-to-text)", "Tool page", "P1"),
 ("/u/mp4-to-text-converter", "MP4 to text", "Chưa có", "", "Tool page /mp4-to-text/", "Tool page", "P1"),
 ("/l/mp3-to-srt", "MP3/MP4/Audio to SRT", "Chưa có", "(có xuất SRT)", "Tool page /mp3-to-srt/ hoặc /srt-generator/ (họ còn có mp4-to-srt, audio-to-srt)", "Tool page", "P1"),
 ("/l/mp3-to-vtt", "MP3 to VTT", "Chưa có", "(có xuất VTT)", "Gộp với SRT hoặc bài srt-vs-vtt", "Tool page/Blog", "P2"),
 ("/l/generate-video-subtitles", "Subtitle / caption generator", "Chưa có", "(có xuất SRT/VTT)", "Tool page /subtitle-generator/ (họ có hơn 8 trang: auto-subtitles, ai-captions, free-captions…)", "Tool page", "P1"),
 ("/l/convert-audio-to-microsoft-word", "Audio to Word", "Chưa có", "(có xuất .docx)", "Tool page /audio-to-word/ + bài how-to-convert-audio-to-word", "Tool page + Blog", "P1"),
 ("/learn/how-to-convert-audio-to-microsoft-word", "Audio to Word", "Chưa có", "", "Blog how-to (cặp với tool page trên)", "Blog", "P1"),
 ("/u/transcribe-voice-memos", "Voice memos", "Chưa có", "", "Blog how-to-transcribe-voice-memos", "Blog", "P1"),
 ("/u/transcribe-lectures-and-seminars-to-text", "Bài giảng", "Chưa có", "", "Blog how-to-transcribe-a-lecture", "Blog", "P2"),
 ("/u/transcribe-job-interviews", "Phỏng vấn", "Chưa có", "", "Blog how-to-transcribe-an-interview (họ còn có free-interview-transcription)", "Blog", "P1"),
 ("/free-podcast-transcription", "Podcast", "Kế hoạch", "", "Blog how-to-transcribe-podcast / tool page podcast", "Blog", "P1"),
 ("/u/transcribe-zoom-meetings-to-text", "Zoom / Meet / Teams (file ghi)", "Chưa có", "", "Chỉ góc upload file ghi, không hứa bot họp. Họ có Zoom, Google Meet, Teams", "Blog", "P2"),
 ("/u/transcribe-phone-calls", "Cuộc gọi", "Chưa có", "", "Blog: chép file ghi âm cuộc gọi (họ có sales calls, support calls)", "Blog", "P3"),
 ("/free-sermon-transcription", "Sermon (bài giảng nhà thờ)", "Chưa có", "", "Niche rõ ở Mỹ (họ có 3 trang). Tra volume trước", "Blog/Landing", "P2"),
 ("/u/transcribe-online-courses", "Khoá học online", "Chưa có", "", "Blog cho người học", "Blog", "P3"),
 ("/u/transcription-tool-for-language-learners", "Học ngoại ngữ", "Chưa có", "", "Blog: dùng transcript YouTube để học ngoại ngữ", "Blog", "P2"),
 ("/u/transcribe-for-free-no-account-required", "Free không cần tài khoản", "Có (lợi thế)", "", "Đúng lợi thế của mình: đưa vào H2 các tool page / bài best-free", "Góc viết", "P1"),
 ("/free-whisper-transcription", "Whisper", "Chưa có", "", "Bài kiến thức 'Whisper transcription online' (họ có whisper-ai-transcription-tool, turboscribe-vs-whisper)", "Blog", "P2"),
 ("/l/can-chatgpt-transcribe-audio", "ChatGPT", "Gần có", "/blog/can-chatgpt-watch-videos/", "Bài 'can ChatGPT transcribe audio': góc connector TranscriptX trong ChatGPT", "Blog", "P1"),
 ("/l/translate-audio-to-english", "Dịch audio", "Cần xác minh", "", "Chỉ làm nếu TranscriptX có dịch", "Tool page", "Chờ"),
 ("/l/medical-transcription-for-healthcare-professionals", "Y tế / pháp lý", "Không", "", "Bỏ: không có cam kết HIPAA, độ chính xác chuyên ngành", "—", "Bỏ"),
 ("/l/otter-ai-alternative", "Alternative", "Kế hoạch", "", "Họ có 12 trang alternative: Otter, Transkriptor, Notta, HappyScribe, Sonix, Trint, Descript, MacWhisper, GoTranscript, Good Tape, Express Scribe, Cockatoo… → thêm vào danh sách BOFU", "So sánh", "P2"),
 ("/learn/turboscribe-vs-otter-ai", "X vs Y", "Kế hoạch", "", "Họ có 9 trang 'turboscribe vs X'. Tham khảo cách làm cho 'transcriptx vs X'", "So sánh", "P3"),
 ("/l/best-transcription-software", "Best", "Có", "/blog/best-transcription-software/", "Đã có", "Blog", "—"),
 ("/learn/how-to-transcribe-youtube-videos-for-free", "YouTube free", "Có", "/blog/how-to-get-youtube-transcript/", "Đã có", "Blog", "—"),
 ("/learn/how-to-transcribe-audio-to-text-for-free", "Audio free", "Một phần", "/blog/how-to-transcribe-audio-faster/", "Bài 'how to transcribe audio to text for free' (cụm free volume cao, xem tool page audio-to-text để tránh trùng)", "Blog", "P2"),
 ("/learn/are-ai-generated-transcripts-admissible-in-court", "Pháp lý", "Không", "", "Bỏ", "—", "Bỏ"),
 ("/transcription/Vietnamese", "Theo ngôn ngữ", "Một phần", "(19 locale)", "Họ có 4 bộ × 105 ngôn ngữ + 2 bộ /u/ × khoảng 100 ngôn ngữ. Có thể làm /<ngôn ngữ>-transcription/ cho các ngôn ngữ đã kiểm chứng", "Programmatic", "P2"),
 ("/transcription-seattle", "Theo thành phố", "Không", "", "97 trang theo thành phố Mỹ: nội dung mỏng, không nên làm", "Programmatic", "Bỏ"),
 ("/downloader/youtube/mp3/free", "Downloader", "Không", "", "Tải video/MP3: rủi ro bản quyền, không phải chép lời", "Tool phụ", "Bỏ"),
 ("/convert/wav-to-mp3", "Đổi định dạng audio", "Không", "", "Tool phụ kéo traffic (24 trang). Chỉ cân nhắc nếu muốn làm free tools", "Tool phụ", "P3"),
]

HEAD_FILL = PatternFill("solid", fgColor="CC582E")
HEAD_FONT = Font(bold=True, color="FFFFFF")
PRIO_FILL = {"P1": "FCE4D6", "P2": "FFF2CC", "P3": "EDEDED", "Bỏ": "F2F2F2", "Chờ": "DDEBF7"}

def sheet(wb, title, header, data, widths, prio_col=None, link_col=None):
    ws = wb.create_sheet(title)
    ws.append(header)
    for c in ws[1]:
        c.fill, c.font = HEAD_FILL, HEAD_FONT
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for r in data:
        ws.append(list(r))
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=True)
        if link_col:
            c = row[link_col - 1]
            if c.value and str(c.value).startswith("http"):
                c.hyperlink = c.value
                c.font = Font(color="0563C1", underline="single")
        if prio_col:
            p = row[prio_col - 1].value
            if p in PRIO_FILL:
                row[prio_col - 1].fill = PatternFill("solid", fgColor=PRIO_FILL[p])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    return ws

wb = Workbook(); wb.remove(wb.active)

cnt = {}
for kind, g, u, p in rows:
    cnt[(kind, g)] = cnt.get((kind, g), 0) + 1
ov = sorted(((k, g, n) for (k, g), n in cnt.items()), key=lambda x: -x[2])
ws = sheet(wb, "Tổng quan", ["Loại", "Nhóm URL", "Số URL"], ov, [16, 44, 10])
ws.append([])
ws.append(["Tổng", "", len(rows)])
ws.append(["Nguồn", "turboscribe.com/__sitemap.xml (khai báo trong robots.txt), lấy ngày 2026-11-04. Chỉ đọc URL, không mở trang. Sitemap không có lastmod.", ""])
ws.append(["Nhận xét", "Phần lớn là SEO programmatic: khoảng 1.000 URL theo ngôn ngữ/thành phố, /u/, /uw/, /u/tools/ là cùng một bộ trang lặp lại. Nội dung đáng học: /l/ (57 trang: 45 keyword + 12 alternative), /learn/ (17), free-* (22), use case trong /u/.", ""])

sheet(wb, "Ý tưởng cho TranscriptX",
      ["URL mẫu TurboScribe", "Cụm chủ đề", "TranscriptX đã có?", "Trang TranscriptX", "Đề xuất", "Loại nội dung", "Ưu tiên"],
      [(BASE + a, b, c, d, e, f, g) for a, b, c, d, e, f, g in IDEAS],
      [52, 26, 16, 30, 60, 16, 9], prio_col=7, link_col=1)

focus = [r for r in rows if r[0] in ("Landing", "So sánh", "Blog", "Help")]
sheet(wb, "Landing + Blog (lọc)", ["Loại", "Nhóm URL", "URL", "Path"], focus, [14, 36, 64, 52], link_col=3)
sheet(wb, "Tất cả URL", ["Loại", "Nhóm URL", "URL", "Path"], rows, [14, 36, 64, 52])
wb.save(OUT)
print("saved", len(rows), "focus", len(focus))
