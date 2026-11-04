# Ghi chú – How to Transcribe a Podcast

## 1. Bài nói về gì
**Excerpt (EN, dán vào blog)** (205/250)
```
How to transcribe a podcast three ways: read the built-in transcript on Spotify or Apple Podcasts, or get editable text from a YouTube link or an audio file with TranscriptX and download it as DOCX or SRT.
```

Bài how-to cho 2 nhóm: người nghe muốn lấy chữ của một tập podcast, và người làm podcast muốn có transcript cho show của mình. Bài mở đầu bằng transcript có sẵn trong Spotify và Apple Podcasts (cụm "spotify podcast transcript" có volume 1K–10K, cạnh tranh thấp). Điểm chuyển sang TranscriptX: transcript trong app chỉ đọc được, còn TranscriptX cho bản sửa được, tải về .docx/.srt. Bài dẫn traffic về `/audio-to-text/` (CTA chính) và `/youtube-transcript/`.

## 2. Dàn ý
- **H1** How to Transcribe a Podcast: Get a Transcript of Any Episode
- **Quick answer:** xem app trước (Spotify/Apple, chỉ đọc) → muốn sửa và lưu thì dán link YouTube hoặc upload file vào TranscriptX → Copy hoặc Download
- **Intro:** transcript podcast là gì, để làm gì, 3 cách
- **H2 How Do You Transcribe a Podcast?:** bảng 4 cách (Spotify, Apple, YouTube + TranscriptX, file + TranscriptX)
- **H2 How to Get a Transcript of a Spotify Podcast:** 4 bước trong app Spotify, không phải tập nào cũng có, không xuất file được
- **H2 How to See the Transcript on Apple Podcasts:** 4 bước, nút Transcript, tìm kiếm và bấm dòng để nhảy tới
- **H2 How to Transcribe a Podcast From a YouTube Link:** 7 bước trên `/youtube-transcript/`, Copy và Download là 2 bước riêng, test 4 phút ≈ 6 giây
- **H2 How to Transcribe a Podcast Audio File (Podcast to Text):** 6 bước trên `/audio-to-text/`: Upload → 4 nguồn → chọn file → mũi tên → Edit → Copy / Download. Hơn 100 ngôn ngữ, file dài tuỳ gói
- **H2 How to Transcribe Your Own Podcast:** quy trình cho podcaster: xuất file → upload → sửa tên → tải .docx/.pdf, .srt/.vtt, .txt. Speakers trên Pro, Record trên trình duyệt
- **H2 Tips for a Cleaner Podcast Transcript:** file sạch, nhạc và nói chồng, sửa tên, bật/tắt timestamp, lọc nhiễu (Pro)
- **H2 Can You Transcribe a Podcast for Free?:** app miễn phí nhưng chỉ đọc; TranscriptX free mỗi ngày, không cần tài khoản để thử, link /pricing/
- **FAQ (6):** vì sao không có transcript trong app; mất bao lâu (link bài 1 giờ audio); có hợp pháp không; có tên người nói không (Pro); làm phụ đề được không; ChatGPT có chép lời podcast được không (link /transcription-mcp/ + bài ChatGPT)
- **H2 CTA:** Transcribe Your Next Podcast Episode → `/audio-to-text/`

**Link nội bộ:** /audio-to-text/, /youtube-transcript/, /video-to-text/, /transcribe-large-audio-files/, /pricing/, /transcription-mcp/, /blog/how-long-does-it-take-to-transcribe-1-hour-of-audio/, /blog/can-chatgpt-watch-videos-here-s-how-to-make-it-read-them/ (URL blog lấy theo page/llms.txt)

## 3. Hình ảnh
**Ảnh bìa / ảnh chia sẻ mạng xã hội** (không chèn trong thân bài; đặt làm Cover trong CMS và og:image)
- `how-to-transcribe-podcast-cover.webp` (2400×1260, dựng thẳng ở 2x): ảnh cover trong CMS.
- `how-to-transcribe-podcast-og-1200x630.jpg`: bản 1200×630 cho Facebook, LinkedIn, X, Zalo.
- Nội dung: badge 🎙 PODCAST, tiêu đề "Podcast / to text", dòng "Get a transcript of any episode", 4 chip .docx .pdf .srt .txt, logo TranscriptX.ai. Bên phải là màn hình kết quả thật của TranscriptX, khoanh cam menu Download (.txt .docx .pdf | .srt .vtt). Thẻ file "episode-42.mp3 · 58:14" có sóng âm chỉ là hình minh hoạ đầu vào, không phải ảnh giao diện.
- Nguồn: `_source/transcript/transcript-download-menu-open.png` (crop, giữ nguyên pixel retina). Script: `_source/_tools/build_cover_podcast.py`.
- Alt: `Podcast to text with TranscriptX: an episode file becomes a transcript you can download as DOCX, PDF, SRT or TXT`

Ảnh trong thân bài: chờ Bước 4 (xem đề xuất trong chat).

## 4. Video
Chờ duyệt.

## 5. Cần kiểm chứng
- **Link Spotify / Apple Podcasts trên TranscriptX:** chưa test. Bài KHÔNG nói TranscriptX nhận link Spotify/Apple. Nếu test chạy được, nên thêm một H2 "Paste a Spotify or Apple Podcasts link" và sửa bảng so sánh.
- **Các bước trong Spotify** (transcript nằm dưới nút phát trong trình phát đầy đủ, chạm để mở toàn màn hình; không phải tập nào cũng có; không xuất file): lấy từ kiến thức chung, cần mở app kiểm tra lại.
- **Các bước trong Apple Podcasts** (nút Transcript hình bong bóng thoại có dấu ngoặc kép; tìm kiếm; bấm dòng để nhảy; có trên iPhone, iPad, Mac; không phải ngôn ngữ nào cũng có): lấy từ kiến thức chung, cần kiểm tra lại.
- **Trang `/audio-to-text/`:** kho `_source` chưa có ảnh trang này. Các bước upload dựa trên ảnh `upload/upload-source-options.png` (menu Upload trên trang chủ) và llms.txt.
- "Typing it by hand takes several times the length of the audio": dựa trên câu của trang Pricing ("Typing up 1 hour of audio takes about 4 hours").
- Câu về pháp lý (FAQ "Is it legal…") viết chung chung, không phải tư vấn pháp lý.
