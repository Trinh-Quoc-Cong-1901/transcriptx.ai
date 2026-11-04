import re, sys, glob, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

MAPS = sys.argv[1]
OUT = sys.argv[2]
BASE = "https://elevenlabs.io"

rows = []  # (sitemap, url, path, lastmod)
for f in sorted(glob.glob(os.path.join(MAPS, "*.xml"))):
    name = os.path.basename(f).replace("__en.xml", "").replace(".xml", "")
    xml = open(f, encoding="utf-8").read()
    for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
        loc = re.search(r"<loc>([^<]+)</loc>", block)
        lm = re.search(r"<lastmod>([^<]+)</lastmod>", block)
        if not loc:
            continue
        u = loc.group(1).strip()
        rows.append((name, u, u.replace(BASE, "") or "/", (lm.group(1)[:10] if lm else "")))
lastmod = {r[2]: r[3] for r in rows}

# ---------- Sheet 2: tool / landing pages ----------
# (path, nhóm, ElevenLabs làm gì (đoán từ URL), TranscriptX đã có, trang TranscriptX, đề xuất, ưu tiên)
TOOLS = [
 ("/speech-to-text", "Hub STT", "Trang chính Speech to Text (Scribe)", "Chưa có trang riêng", "/ (homepage), /speech-to-text-api/", "Cân nhắc tool page /speech-to-text/ (head term lớn)", "P1"),
 ("/audio-to-text", "Theo nguồn", "Chuyển audio sang text", "Có", "/audio-to-text/", "Đã có, so on-page với họ", "—"),
 ("/video-to-text", "Theo nguồn", "Chuyển video sang text", "Có", "/video-to-text/", "Đã có", "—"),
 ("/mp3-to-text", "Theo định dạng file", "MP3 sang text", "Chưa có", "", "Tool page theo định dạng (dùng lại khối upload)", "P1"),
 ("/mp4-to-text", "Theo định dạng file", "MP4 sang text", "Chưa có", "", "Tool page theo định dạng", "P1"),
 ("/wav-to-text", "Theo định dạng file", "WAV sang text", "Chưa có", "", "Tool page theo định dạng", "P2"),
 ("/m4a-to-text", "Theo định dạng file", "M4A sang text (voice memo iPhone)", "Chưa có", "", "Tool page hoặc gộp vào bài voice memo", "P2"),
 ("/ogg-to-text", "Theo định dạng file", "OGG sang text (voice note WhatsApp/Telegram)", "Chưa có", "", "Tool page hoặc bài WhatsApp voice to text", "P2"),
 ("/youtube-transcript-generator", "Theo nền tảng", "YouTube transcript", "Có", "/youtube-transcript/", "Đã có", "—"),
 ("/tiktok-transcript-generator", "Theo nền tảng", "TikTok transcript", "Có", "/tiktok-transcript/", "Đã có", "—"),
 ("/instagram-transcript-generator", "Theo nền tảng", "Instagram transcript", "Có", "/instagram-transcript/", "Đã có", "—"),
 ("/facebook-video-transcript-generator", "Theo nền tảng", "Facebook video transcript", "Có", "/facebook-transcript/", "Đã có", "—"),
 ("/podcast-transcript-generator", "Theo nền tảng", "Podcast transcript", "Chưa có", "", "Tool page /podcast-transcript/ hoặc bài how-to-transcribe-podcast", "P1"),
 ("/zoom-transcript-generator", "Theo nền tảng", "Zoom transcript (từ file ghi)", "Chưa có", "", "Chỉ góc 'upload file ghi Zoom', KHÔNG hứa bot vào họp", "P2"),
 ("/google-meet-transcript-generator", "Theo nền tảng", "Google Meet transcript", "Chưa có", "", "Như Zoom: chỉ chép file ghi", "P2"),
 ("/voicemail-to-text", "Theo nguồn", "Voicemail sang text", "Có", "/voicemail-to-text/", "Đã có", "—"),
 ("/subtitle-generator", "Phụ đề", "Tạo phụ đề tự động", "Chưa có trang riêng", "(có xuất SRT/VTT)", "Tool page /subtitle-generator/ dựa trên xuất SRT/VTT", "P1"),
 ("/caption-generator", "Phụ đề", "Tạo caption cho video", "Chưa có trang riêng", "(có xuất SRT/VTT)", "Gộp với subtitle-generator hoặc trang riêng", "P2"),
 ("/subtitle-translator", "Phụ đề", "Dịch phụ đề", "Cần xác minh", "", "Chỉ làm nếu TranscriptX có dịch (đang 'cần xác minh')", "Chờ"),
 ("/realtime-speech-to-text", "Realtime", "STT thời gian thực", "Có", "/real-time-speech-to-text/", "Đã có", "—"),
 ("/speech-to-text-api", "API", "API STT", "Có", "/speech-to-text-api/", "Đã có", "—"),
 ("/realtime-speech-to-text-api", "API", "API STT realtime", "Cần xác minh", "", "Chỉ làm nếu API có realtime", "Chờ"),
 ("/translate-audio", "Dịch (dubbing)", "Dịch audio bằng giọng AI + 55 cặp ngôn ngữ", "Không", "", "Không phù hợp (lồng tiếng, không phải chép lời)", "Bỏ"),
 ("/translate-video", "Dịch (dubbing)", "Dịch video + 55 cặp ngôn ngữ", "Không", "", "Không phù hợp", "Bỏ"),
 ("/voice-isolator", "Xử lý audio", "Tách giọng, lọc nhiễu", "Một phần", "(lọc nhiễu trên Pro)", "Chỉ nhắc trong bài, không làm trang", "Bỏ"),
 ("/students", "Đối tượng", "Trang cho sinh viên", "Chưa có", "", "Gợi ý bài how-to-transcribe-a-lecture", "P2"),
 ("/use-cases/podcasts", "Use case", "Hub use case podcast", "Chưa có", "", "Tham khảo cho bài podcast", "P2"),
 ("/use-cases/youtube", "Use case", "Hub use case YouTube", "—", "", "Tham khảo", "—"),
 ("/use-cases/tiktok", "Use case", "Hub use case TikTok", "—", "", "Tham khảo", "—"),
 ("/insights/speech-to-text-api-integration", "Developer", "Hướng dẫn tích hợp API STT", "Một phần", "/speech-to-text-api/", "Bài developer tương tự cho API của mình", "P2"),
 ("/webinars/building-reliable-voice-transcription-with-scribe", "Webinar", "Webinar về Scribe", "—", "", "Không làm", "Bỏ"),
]

# ---------- Sheet 3: blog posts ----------
# (path, chủ đề, loại, TranscriptX đã có/kế hoạch, slug đề xuất, đề xuất, ưu tiên)
BLOG = [
 ("/blog/how-to-transcribe-a-youtube-video", "How-to YouTube", "How-to", "Đã có", "how-to-get-youtube-transcript", "Đã đăng, không sửa", "—"),
 ("/blog/how-to-transcribe-an-interview", "Phỏng vấn", "How-to", "Chưa có", "how-to-transcribe-an-interview", "Viết: upload/Record, speaker (Pro), xuất .docx", "P1"),
 ("/blog/how-to-transcribe-a-podcast", "Podcast", "How-to", "Kế hoạch (KD18-01)", "how-to-transcribe-podcast", "Viết: dán link/upload, SRT cho video podcast", "P1"),
 ("/blog/how-to-transcribe-zoom-meetings", "Zoom", "How-to", "Kế hoạch (KD18-02)", "how-to-transcribe-zoom-recording", "Viết góc file ghi, nói rõ không có bot họp", "P1"),
 ("/blog/how-to-add-subtitles-to-a-video", "Phụ đề", "How-to", "Kế hoạch (KD18-04)", "how-to-add-subtitles", "Viết: xuất SRT/VTT rồi gắn vào video", "P1"),
 ("/blog/audio-transcription-with-timestamps", "Timestamp", "Kiến thức/How-to", "Kế hoạch (KD17-05)", "transcript-with-timestamps", "Viết: bật/tắt timestamp, SRT/VTT", "P1"),
 ("/blog/what-is-speaker-diarization", "Nhận diện người nói", "Kiến thức", "Kế hoạch (KD17-04)", "speaker-identification-transcription", "Viết, ghi rõ tính năng trên Pro", "P2"),
 ("/blog/what-is-multilingual-transcription", "Đa ngôn ngữ", "Kiến thức", "Kế hoạch gần (KD11-05)", "multilingual-transcription", "Viết nếu xác minh được tự nhận diện ngôn ngữ", "P2"),
 ("/blog/real-time-vs-batch-transcription", "Realtime vs file", "Kiến thức", "Chưa có", "real-time-vs-batch-transcription", "Viết: Live mode vs upload file", "P2"),
 ("/blog/speech-to-text-for-content-creators", "Creator", "Use case", "Chưa có", "speech-to-text-for-content-creators", "Viết: TikTok/Reels/YouTube, caption, repurpose", "P2"),
 ("/blog/text-to-speech-vs-speech-to-text", "Kiến thức", "Kiến thức", "Chưa có", "text-to-speech-vs-speech-to-text", "Bài ngắn, dễ được AI search trích", "P2"),
 ("/blog/automatic-speech-recognition-asr", "Kiến thức", "Kiến thức", "Chưa có", "what-is-asr", "Bài định nghĩa, link về tool", "P3"),
 ("/blog/word-error-rate-wer", "Độ chính xác", "Kiến thức", "Kế hoạch (KD17-01)", "transcription-accuracy-benchmark", "Chỉ viết khi tự đo WER thật", "Chờ"),
 ("/blog/what-is-call-transcription", "Cuộc gọi", "Kiến thức", "Chưa có", "call-transcription", "Góc upload file ghi âm cuộc gọi", "P3"),
 ("/blog/medical-speech-to-text", "Y tế", "Kiến thức", "Không", "", "Bỏ: không có cam kết bảo mật/HIPAA", "Bỏ"),
 ("/blog/meeting-transcription-api", "API họp", "Developer", "Không", "", "Bỏ: không có bot họp", "Bỏ"),
 ("/blog/how-to-clean-up-audio-for-podcasts", "Âm thanh", "How-to", "Một phần", "", "Có thể nhắc lọc nhiễu (Pro) trong bài podcast", "P3"),
 ("/blog/meet-scribe", "Tin sản phẩm", "Ra mắt", "—", "", "Tin riêng của ElevenLabs, không viết", "Bỏ"),
 ("/blog/introducing-scribe-v2", "Tin sản phẩm", "Ra mắt", "—", "", "Không viết", "Bỏ"),
 ("/blog/scribe-v2-just-got-an-upgrade", "Tin sản phẩm", "Ra mắt", "—", "", "Không viết", "Bỏ"),
 ("/blog/introducing-scribe-v2-realtime", "Tin sản phẩm", "Ra mắt", "—", "", "Không viết", "Bỏ"),
 ("/blog/how-scribe-v2-realtime-works", "Tin sản phẩm", "Kỹ thuật", "—", "", "Không viết", "Bỏ"),
 ("/blog/scribe-v2-realtime-in-elevenlabs-agents", "Tin sản phẩm", "Ra mắt", "—", "", "Không viết", "Bỏ"),
 ("/blog/scribe-v2-medical-generally-available", "Tin sản phẩm", "Ra mắt", "—", "", "Không viết", "Bỏ"),
 ("/blog/real-time-speech-to-text-under-200ms", "Tin sản phẩm", "Kỹ thuật", "—", "", "Không viết", "Bỏ"),
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

wb = Workbook()
wb.remove(wb.active)

# Sheet 1: overview
counts = {}
for r in rows:
    counts[r[0]] = counts.get(r[0], 0) + 1
REL = {
 "pagesv2": "Trang chính và tool page. Có khoảng 20 trang về chép lời (sheet 2)",
 "speech-to-text": "99 trang STT theo ngôn ngữ (sheet 4)",
 "articles": "Blog. Khoảng 25 bài về chép lời (sheet 3)",
 "translate-audio-pages": "Dịch audio bằng lồng tiếng. Không phù hợp",
 "translate-video-pages": "Dịch video bằng lồng tiếng. Không phù hợp",
 "languages": "Trang text-to-speech theo ngôn ngữ. Không phù hợp",
 "use-cases": "Hub use case (podcast, YouTube, TikTok)",
 "insights": "1 bài về tích hợp API STT",
 "webinars": "1 webinar về Scribe",
 "sound-effect-categories": "Sound effects. Không phù hợp",
 "voice-library-collections": "Thư viện giọng. Không phù hợp",
 "music-categories": "Nhạc AI. Không phù hợp",
 "creative-templates": "Ảnh/video AI. Không phù hợp",
 "voice-changer-categories": "Đổi giọng. Không phù hợp",
 "ai-answering-service-categories": "Voice agent. Không phù hợp",
 "chatbot-categories": "Chatbot. Không phù hợp",
 "convai-integrations": "Tích hợp agent. Không phù hợp",
 "soundboards": "Soundboard. Không phù hợp",
 "external-model-pages": "Trang model bên ngoài. Không phù hợp",
 "article-authors": "Trang tác giả",
}
ov = sorted(((k, v, REL.get(k, "")) for k, v in counts.items()), key=lambda x: -x[1])
ws = sheet(wb, "Tổng quan", ["Nhóm sitemap", "Số URL", "Ghi chú (liên quan chép lời?)"], ov, [32, 10, 70])
ws.append([])
ws.append(["Tổng URL tiếng Anh", len(rows), "Nguồn: elevenlabs.io/sitemap.xml, lấy ngày 2026-11-04. Chỉ đọc URL, không mở nội dung trang."])

t = [(BASE + p, g, d, lastmod.get(p, ""), has, tx, rec, pr) for p, g, d, has, tx, rec, pr in TOOLS]
sheet(wb, "Tool pages STT", ["URL ElevenLabs", "Nhóm", "Họ làm gì (đoán từ URL)", "Lastmod", "TranscriptX đã có?", "Trang TranscriptX", "Đề xuất", "Ưu tiên"],
      t, [48, 18, 36, 12, 18, 26, 46, 9], prio_col=8, link_col=1)

b = [(BASE + p, topic, kind, lastmod.get(p, ""), has, slug, rec, pr) for p, topic, kind, has, slug, rec, pr in BLOG]
sheet(wb, "Blog STT", ["URL ElevenLabs", "Chủ đề", "Loại bài", "Lastmod", "TranscriptX đã có / kế hoạch", "Slug đề xuất", "Đề xuất", "Ưu tiên"],
      b, [56, 18, 14, 12, 22, 34, 46, 9], prio_col=8, link_col=1)

langs = [(r[1], r[2].split("/")[-1], r[3]) for r in rows if r[0] == "speech-to-text"]
ws = sheet(wb, "STT theo ngôn ngữ", ["URL ElevenLabs", "Ngôn ngữ", "Lastmod"], langs, [48, 22, 12], link_col=1)
ws.insert_rows(1)
ws["A1"] = ("Họ có 99 trang /speech-to-text/<ngôn ngữ> (programmatic SEO). TranscriptX đang dịch tool page sang 19 locale. "
            "Có thể làm kiểu /<ngôn ngữ>-speech-to-text/, nhưng chỉ làm khi xác minh được TranscriptX chép lời tốt ngôn ngữ đó.")
ws["A1"].font = Font(italic=True)
ws.freeze_panes = "A3"
ws.auto_filter.ref = f"A2:C{ws.max_row}"

sheet(wb, "Tất cả URL", ["Nhóm sitemap", "URL", "Path", "Lastmod"], rows, [28, 70, 60, 12], link_col=None)

wb.save(OUT)
print("saved", OUT, len(rows), "urls")
