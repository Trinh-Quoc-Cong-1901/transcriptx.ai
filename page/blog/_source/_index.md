# TranscriptX — Kho ảnh sản phẩm (nguồn cho blog)

Ảnh chụp giao diện thật của app TranscriptX.ai. Có 2 đợt chụp:
- **Đợt 2026-10-27** (đang đăng nhập gói Pro): đây là giao diện MỚI NHẤT, ưu tiên dùng.
- **Đợt 2026-10-12** (chưa đăng nhập, lấy từ thư mục `/image` của repo): giao diện cũ hơn, có vài chỗ khác. Xem mục "⚠️ Khác biệt giữa 2 đợt" ở cuối file.
Khi viết bài, chỉ mô tả các bước, nút và tính năng **có trong ảnh ở đây**. Muốn dùng ảnh nào thì copy sang `page/blog/<slug>/images/`, đổi tên theo từ khóa của bài và chuyển sang `.webp`.

## Bố cục chung của app
- **Sidebar trái:** logo TranscriptX.ai, nút thu gọn sidebar, **New session**, **Speak live**, **History** (danh sách các transcript cũ). Dưới cùng là tên tài khoản và gói đang dùng (vd. `AI Transciptx · Pro ⌄`).
- **Vùng chính:** nội dung của trang đang mở.

---

## homepage/
### homepage.png
Trang chủ, tức màn hình **New session**.
- H1: **"AI Transcription for Video and Audio"**
- Ô nhập: *"Upload a file or paste a video link..."*
- Nút **Upload**, **Record** và nút gửi (mũi tên ↑)
- Dòng "Works with": **YouTube, Instagram, Facebook, TikTok, X & more**
- Dùng cho bước: "Mở TranscriptX → dán link hoặc tải file lên".

## homepage/ (đợt 10-12)
### homepage-signed-out.png
Trang chủ khi **chưa đăng nhập**. Sidebar thu gọn chỉ còn icon (☰, +, 🎙), dưới cùng có nút đăng nhập (→]). Ô nhập, nút Upload/Record và dòng Works with giống bản 10-27.

## youtube-transcript/
### youtube-transcript-tool.png
Trang tool **YouTube Transcript** (`/youtube-transcript/`). Đây là trang dùng cho mọi bài về YouTube; KHÔNG dùng ảnh homepage cho các bài này.
- H1: **"YouTube Transcript"**
- Ô nhập: *"Paste a YouTube video URL..."*
- Nút **Upload**, **Record** và nút gửi (mũi tên ↑)
- Dòng "Works with": YouTube, Instagram, Facebook, TikTok, X & more
- Dùng cho bước: "Mở trang YouTube Transcript → dán link → bấm mũi tên".

### youtube-transcript-link-pasted.png (đợt 10-12, chưa đăng nhập)
Trang YouTube Transcript **đã dán link** `https://youtu.be/YfDqONbzYPc` vào ô, chưa bấm gửi. Dùng cho bước "Dán link".

### youtube-transcript-result-info-panel.png (đợt 10-12)
Kết quả transcript của video *Shayne Ward - Until You (Audio)*, khớp với ảnh Share của YouTube trong `external/youtube/`.
- Thanh công cụ trái: ⚙ (cài đặt hiển thị), 👥 (người nói), ✏️ **Edit**. Bên phải: 🔗 share, ⬇ download, nút **Copy text**
- Các đoạn có timestamp (`00:12.28`, `00:53.70`, `01:40.58`, `02:24.00`)
- Panel phải: video preview và khối **Info**: Source (link youtu.be), Duration 4:09, Language English, Date 10/12/2026
- Trình phát `0:00 / 4:10`, tốc độ `1x`

### demo-youtube-to-transcript.gif (đợt 10-12, ~10 giây, 1280×800)
GIF trọn quy trình trên trang YouTube Transcript:
1. Ô trống "Paste a YouTube video URL..."
2. Gõ hoặc dán dần link `https://youtu.be/YfDqONbzYPc`
3. Bấm gửi → màn hình đang xử lý: tiêu đề video hiện ngay, thanh trạng thái **Uploading 7% → 17%… → Recognizing speech**, nút **Notify me when done** và **Cancel**; transcript là các dòng xám (skeleton); panel phải đã có video + Info
4. Khung cuối: transcript hoàn chỉnh (giống `youtube-transcript-result-info-panel.png`)
- Dùng được ngay làm GIF "dán link → nhận transcript" cho các bài về YouTube.

## youtube-subtitle-downloader/
### youtube-subtitle-downloader-tool.png
Trang tool **YouTube Subtitle Downloader** (`/youtube-subtitle-downloader/`).
- H1: **"YouTube Subtitle Downloader"**
- Ô nhập: *"Paste a YouTube video URL..."*, có nút **Upload**, **Record** và nút gửi (mũi tên ↑).
- Dòng "Works with": YouTube, Instagram, Facebook, TikTok, X & more.
- Dùng cho các bài về tải phụ đề (SRT/VTT).

## export-files/
### export-vtt-file.png
File **.vtt** xuất từ TranscriptX, mở trong trình soạn thảo. Tên file: `Shayne Ward - Until You (Audio) - TranscriptX.ai.vtt`.
- Mỗi đoạn gồm một dòng thời gian `00:00:12.344 --> 00:00:18.526` và 1–2 dòng chữ.
- Câu được chia ngắn, vừa để làm phụ đề.
- Dùng cho phần SRT vs VTT, hoặc cảnh "mở file" trong video.
- (Chưa có ảnh file .srt.)

## external/youtube/ (giao diện YouTube, không phải của TranscriptX)
Đây là nguồn để làm GIF/video quay các bước: lấy link trên YouTube → dán vào TranscriptX.
### youtube-share-copy-link.png
Trang video YouTube (desktop) khi đang mở hộp thoại **Share**. Video mẫu: *Shayne Ward - Until You (Audio)*.
- Hộp **Share**: nút **Copy link**, dòng *"No one can see your link"*
- **Share to**: Embed, X, Messenger, WhatsApp, Facebook, More
- Ô link `https://youtu.be/...` + nút **Copy**
- Ô tick **Start at 0:04**
- Bên dưới video: tên video, kênh, nút Subscribe, mô tả có chữ **...more**
- Dùng cho bước: "Bấm **Share** dưới video → **Copy link**" (hoặc bấm **Copy** cạnh ô link).
- Kịch bản GIF chuẩn: mở video → bấm Share → Copy link → mở trang YouTube Transcript của TranscriptX → dán vào "Paste a YouTube video URL..." → bấm mũi tên → trang transcript hiện ra → bấm Copy.

## mobile/
### mobile-homepage.png
Trang chủ trên điện thoại: H1 "AI Transcription for Video and Audio", ô **"Video link or audio file"** có nút **dán (📋)** ở góc phải, Upload, Record, nút ↑, dòng Works with (icon), khối "What is TranscriptX?". Các bước giống desktop.

### mobile-transcript-result.png
Kết quả transcript trên điện thoại: tiêu đề rút gọn, các đoạn có timestamp, bảng kéo lên có Notes / Summary / Mind map và nút ▶ phát. Thanh dưới cùng: ⋯, 👥, **Copy**, ⬇ download, +.

## _tools/
- `build_visuals_youtube_transcript.py`: script dựng ảnh khoanh nổi bật, ảnh ghép 2 điện thoại, video MP4 và WebP động (zoom, ripple khi click, chú thích từng bước) cho bài how-to-get-youtube-transcript. Bài mới có thể copy script này, đổi nguồn ảnh và kịch bản.
- `video_hq.py`: **bộ dựng video chuẩn YouTube, dùng cho mọi video mới**. Xuất 2560×1440 (1440p), 60 fps, x264 CRF 14. Giới hạn mức phóng to cho từng nguồn (`max_up`), chi tiết nhỏ hiện bằng khung phóng to cắt từ ảnh retina (`callout`), ảnh phải phóng to được làm nét lại. Mỗi lần dựng có thêm ảnh cắt 100% để kiểm tra độ nét. Dựng từng khung rồi đẩy thẳng vào bộ nén, ảnh chỉ co giãn 1 lần, GIF được nội suy để chuyển động mượt.
- `video_kit.py`: (cũ, 1280×800 30 fps, không dùng nữa) bộ hàm dùng chung để dựng video (con trỏ, vòng click, nhãn, thanh tiến trình, khung màn hình, chuyển cảnh, xuất MP4/WebP). Bài mới dùng file này.
- `build_visuals_youtube_subtitles.py`, `build_video_youtube_subtitles.py`, `build_thumbnail_youtube_subtitles.py`: ảnh, video và thumbnail cho bài how-to-download-youtube-subtitles.
- `build_thumbnail_youtube_transcript.py`: thumbnail YouTube 1280×720 ("YouTube Video to Transcript in seconds" + ảnh trang kết quả).
- `build_video_youtube_transcript_v2.py`: video hướng dẫn bản 2 (đang dùng). Mở đầu nổi bật, con trỏ chuột di chuyển và bấm, thanh tiến trình 5 bước, chuyển cảnh mờ dần. **Copy** (chép nội dung) và **Download** (nút cạnh Copy, mở menu định dạng) là 2 bước riêng.

## brand/
- `cover-producthunt-1270x760.png`: ảnh cover Product Hunt. Bên trái là logo, câu **"Any video or audio. Text in seconds."**, các tag YouTube, TikTok, Instagram, Facebook, Live, Claude & ChatGPT. Bên phải là mockup trang transcript. Dùng làm ảnh cover hoặc OG cho bài tổng quan.
- `logo/logo_256.png`, `logo_512.png`, `logo_1600.png`: logo TranscriptX (3 gạch ngang màu đen xám).
- `brand-info.md`: bio, thông tin cốt lõi, link mạng xã hội. ⚠️ Có câu "No sign-up / không giới hạn dung lượng file". Câu này mâu thuẫn với trang Pricing (500MB/2GB), không dùng trong bài.

## upload/
### upload-source-options.png
Menu xổ ra khi bấm **Upload**, gồm 4 nguồn:
1. **From this device**
2. **Google Drive**
3. **Dropbox**
4. **OneDrive**
- Dùng cho bước: "Bấm Upload → chọn nguồn file".

## record/
### recording-in-progress.png
Màn hình đang ghi âm sau khi bấm **Record** trên trang chủ.
- Đồng hồ đếm giờ lớn ở giữa (vd. `0:13`)
- Dòng chữ: *"Keep this page open while recording"*
- Nút tạm dừng (⏸) hình tròn ở dưới cùng
- Dùng cho bước: "Bấm Record → nói → giữ nguyên trang trong lúc ghi".

### recording-transcript-result.png
Kết quả sau khi ghi âm xong.
- Tiêu đề là tên file ghi âm: `recording-2026-10-27-0854.webm`
- Thanh công cụ: ✏️ Edit, 👥 Speakers, ⋯ More, ⬇ Download, nút **Copy**
- Transcript chia theo đoạn, mỗi đoạn có **timestamp** (vd. `00:10.95`, `00:21.69`)
- Trình phát audio ở dưới: thời gian `0:00 / 0:27`, lùi/tiến, chỉnh tốc độ `1x`
- Panel bên phải: hình sóng âm, 3 tab **Notes | Summary | Mind map**. Tab Notes có thanh định dạng (H, B, I, list, checklist, link, timestamp) và ô *"Add a note..."*
- ⚠️ **Summary và Mind map SẮP RA MẮT.** Chưa được viết như tính năng đã có.

## speak-live/
### speak-live-start.png
Trang **Speak live**, mở từ sidebar.
- H1: **"Live Transcription – Transcribe Speech in Real Time"**
- Nút tròn lớn **Start** (phím tắt `⌘K`)
- Ô chọn ngôn ngữ: **English ⌄**
- Live mode là tính năng của gói **Pro** (xem pricing).

## transcript/
### transcript-result-light.png
Kết quả transcript thông thường từ link video YouTube (video Vevo "The Nights").
- Tiêu đề do AI tự đặt: **"Father's Advice About Living a Memorable Life"**
- Thanh công cụ giống phần record: Edit, Speakers, More, Download, **Copy**
- Các đoạn có timestamp (`00:00.33`, `00:13.65`, `00:40.11`, `01:36.51`)
- Trình phát `0:00 / 3:11`, tốc độ `1x`
- Panel phải: **video preview** (phát được ngay trong app), tab Notes / Summary / Mind map
- Sidebar History: item đang chọn được highlight

### transcript-result-dark-mode.png
Cùng transcript ở trên nhưng ở **dark mode**, tab **Mind map** đang mở.
- Mind map hiện: **"Coming soon — A map of this transcript's ideas — the whole talk at a glance."** và *"You're on Pro — you'll get the beta first."*
- Dùng để minh họa giao diện tối và lộ trình tính năng. Không mô tả Mind map như tính năng đã chạy.

### transcript-download-menu-open.png
Trang kết quả *Father's Advice* với menu **Download** (⬇) đang mở: **.txt, .docx, .pdf** | **.srt, .vtt**.

### download-format-menu.png
Ảnh cận cảnh menu Download (5 định dạng, nhóm tài liệu và nhóm phụ đề cách nhau bằng một vạch).

## account/
### account-menu-open.png
Toàn màn hình trang chủ khi đang mở menu tài khoản (bấm tên tài khoản ở góc dưới bên trái).

### account-menu-detail.png
Ảnh cận cảnh menu tài khoản / settings:
- Tên tài khoản + thống kê: `1 transcripts · 3 min`
- **Pro plan** + nút **Manage plan**
- **Today's credits**: thanh credit đã dùng/còn lại, *"Resets tomorrow at 7:00 AM"* (credit reset mỗi ngày)
- **Ngôn ngữ giao diện:** English ⌄
- **Giao diện:** System ⌄ (sáng / tối / theo hệ thống)
- **Use in ChatGPT & Claude ↗**
- **Help & feedback**
- **Sign out**
- **Delete all my data** (chữ đỏ)

## chatgpt-claude/
### mcp-chatgpt-claude-setup.png
Trang **Use in ChatGPT & Claude** (MCP).
- H1: **"Transcription MCP – Transcribe Right Inside ChatGPT and Claude"**
- Mô tả: thêm TranscriptX một lần, rồi dán link YouTube/podcast hoặc đính kèm file, AI assistant sẽ nhận transcript để tóm tắt, dịch hoặc hỏi đáp.
- Badge: ✓ Free every day · ✓ No account needed to try · ✓ Never reads your other messages
- Ghi chú **Preview**: app chính thức đang chờ ChatGPT và Claude duyệt; tạm thời tự thêm bằng link.
- **ChatGPT (Custom MCP Server)**, nút **Add to ChatGPT**:
  1. Bấm nút: ChatGPT mở Plugins, link được copy sẵn.
  2. Bấm + › Add custom MCP server, dán link, tick "I understand", rồi bấm Create.
- **Claude (Custom Connector)**, chạy trên claude.ai và Claude Desktop, nút **Add to Claude**:
  1. Bấm nút: Claude mở Settings › Connectors, link được copy sẵn.
  2. Bấm Add custom connector, dán link.
  3. Bấm Connect, rồi đăng nhập bằng Google hoặc dùng thử không cần tài khoản.
- Link MCP: `https://transcriptx.ai/mcp`

## pricing/
### pricing-free-vs-pro.png
Trang **Pricing**.
- **Free: $0**, "Everyday transcription". Ai cũng dùng miễn phí được; đăng nhập để giữ lịch sử trên mọi thiết bị. Nút **Use it free**.
  - Scribe X1 model
  - 300 credits a day when signed in
  - Paste a link or upload files
  - Edit, share, export .txt .docx .pdf .srt .vtt
  - Works right inside ChatGPT and Claude
- **Pro: $5.99/month** ("Less than $0.20 a day"). Câu dẫn: *"Typing up 1 hour of audio takes about 4 hours. Let Pro do it."* Gồm mọi thứ của Free, cộng thêm:
  - Scribe X1 Pro model
  - Knows who's speaking (nhận diện người nói)
  - Live mode
  - Noise reduction
  - Unlimited transcription

---

## pricing/pricing-yearly-toggle.png (đợt 10-12)
Trang Pricing khi chưa đăng nhập, có công tắc **Yearly −50% / Monthly** (đang chọn Yearly).
- Free $0: giống bản 10-27, nhưng ghi **"Paste a link or upload files up to 500MB"**
- Pro $5.99/month: "$71.88 billed yearly — save $72 vs. monthly. Less than $0.20 a day.", nút **Upgrade to Pro**, "Keep this price for as long as you stay subscribed"
- Pro gồm: Scribe X1 Pro model, Knows who's speaking, Live mode, Noise reduction, **1,500 credits a day · Files up to 2GB**

## ✅ Thông tin sản phẩm user đã xác nhận (2026-10-27)
- Mọi ảnh trong kho đều là sản phẩm thật, đúng tính năng. Không đặt nghi vấn "phiên bản cũ/mới".
- Video YouTube ~4 phút: transcript xong trong khoảng **6 giây**.
- Timestamp **bật/tắt được**. Nút **Copy** chỉ chép nội dung (kèm timestamp). Nút **Download** nằm ngay cạnh Copy, bấm vào mới mở menu .txt .docx .pdf .srt .vtt. Đây là 2 thao tác riêng, không được trộn lẫn.
- **Free, không cần đăng nhập** vẫn dùng được. Gói Free dùng khá thoải mái (không ghi con số cụ thể trong bài).
- **Pro: 1,500 credits/ngày.**

## Quy tắc khi viết bài
- Tính năng **Pro-only**: nhận diện người nói, Live mode / Speak live, lọc nhiễu, không giới hạn. Không viết như thể gói Free cũng có.
- **Sắp ra mắt**: Summary, Mind map.
- Định dạng export: .txt .docx .pdf .srt .vtt
- Nguồn upload: thiết bị, Google Drive, Dropbox, OneDrive. Link: YouTube, Instagram, Facebook, TikTok, X và nhiều nguồn khác.
- Bài viết về tool nào thì dùng ảnh của **đúng trang tool đó** (vd. bài YouTube → `youtube-transcript/`). Nếu kho chưa có ảnh trang tool đó, phải báo user để chụp, không lấy ảnh homepage thay thế.
- Khi có ảnh hoặc gif mới, bổ sung vào file này.
