# TranscriptX – Ghi chú SEO: khoảng trống Google đang hiểu

> Ngày ghi: 13/10/2026
> Nguồn đối chiếu: bản tóm tắt Google (AI Overview) và nội dung thực tế trên transcriptx.ai
> Mục tiêu: lấp các khoảng trống bằng blog riêng cho từng phần, kết hợp technical SEO và cập nhật nội dung website.

---

## 0. Google đang hiểu đúng (giữ nguyên, củng cố thêm)

- Miễn phí, không cần tài khoản (đăng nhập chỉ để lưu lịch sử)
- Dán link công khai: YouTube, TikTok, Facebook, Instagram, X
- Upload file audio/video (MP3, MP4, voice memo)
- Hơn 100 ngôn ngữ, có tiếng Việt, tự nhận diện ngôn ngữ
- Gắn nhãn người nói (speaker label)
- Xuất file TXT, DOCX, PDF, SRT, VTT
- Nhóm người dùng: freelancer, người làm content TikTok/Reels, sinh viên, người cần phụ đề .srt miễn phí

---

## 1. Google BỎ SÓT: cần viết blog riêng

| # | Khoảng trống | Bài blog đề xuất | Trang đích để link về | Trạng thái |
|---|---|---|---|---|
| 1 | Tích hợp **Claude / ChatGPT (MCP)**, điểm khác biệt lớn nhất | Cách transcribe audio/video ngay trong Claude và ChatGPT | /transcription-mcp/, /claude-transcribe-audio/, /claude-youtube-summary/ | [ ] |
| 2 | **Ghi âm trực tiếp / real-time** | Chuyển giọng nói thành văn bản real-time trên trình duyệt | /live-transcription/, /real-time-speech-to-text/, /voice-to-text/ | [ ] |
| 3 | Thiếu nền tảng **Vimeo, LinkedIn, Twitch, Dailymotion** | Mỗi nền tảng 1 bài hướng dẫn và 1 tool page riêng | Tạo mới /vimeo-transcript/, /linkedin-transcript/, /twitch-transcript/, /dailymotion-transcript/ | [ ] |
| 4 | **Tóm tắt video YouTube** | Tóm tắt video YouTube dài bằng AI | /youtube-video-summarizer/ | [ ] |
| 5 | **Tải caption/phụ đề** có sẵn | Tải phụ đề YouTube, TikTok, Instagram | /youtube-subtitle-downloader/, /tiktok-caption-downloader/, /instagram-caption-downloader/ | [ ] |
| 6 | **Bật/tắt timestamp**, **lọc tạp âm** | Transcript, caption và subtitle khác nhau thế nào | Trang chủ, /video-to-text/ | [ ] |
| 7 | Hỗ trợ link **Google Drive, Dropbox, OneDrive, podcast, direct media URL** | Transcribe file từ Google Drive/Dropbox không cần tải về | /audio-to-text/, /video-to-text/ | [ ] |

---

## 2. Google HIỂU MƠ HỒ: cần làm rõ bằng content và technical

### 2.1 "Chạy trực tiếp trên trình duyệt"
- **Vấn đề:** site không giải thích file được xử lý ở đâu, lưu bao lâu, có bị xóa không.
- **Việc cần làm:**
  - [ ] Viết lại Privacy Policy: nơi xử lý, thời hạn lưu, cơ chế xóa, có dùng dữ liệu để train AI hay không
  - [ ] Blog: "TranscriptX có an toàn cho file nội bộ/bảo mật không?"
  - [ ] Thêm khối "Quyền riêng tư" ngắn gọn trên trang chủ và trong FAQ

### 2.2 "Không giới hạn dung lượng"
- **Vấn đề:** site nói nhiều lần nhưng không có số liệu cụ thể.
- **Việc cần làm:**
  - [ ] Công bố thời lượng hoặc dung lượng tối đa đã test (ví dụ file 3 giờ, 2GB)
  - [ ] Ghi thời gian xử lý thực tế (ví dụ 1 giờ audio mất khoảng X phút)
  - [ ] Đưa con số vào FAQ và schema `featureList`

### 2.3 "Hoàn toàn miễn phí" trong khi có trang /pricing/
- **Vấn đề:** dễ khiến Google tóm tắt sai hoặc người dùng nghi ngờ.
- **Việc cần làm:**
  - [ ] Trang /pricing/ ghi rõ cái gì miễn phí, cái gì giới hạn hoặc trả phí (nếu có)
  - [ ] Thống nhất một câu định vị dùng chung trên toàn site

---

## 3. Nhược điểm Google ĐANG NÊU: phản biện bằng content và tính năng

### 3.1 Độ chính xác tiếng Việt phụ thuộc chất lượng âm thanh
- [ ] Blog benchmark có số liệu: WER theo giọng Bắc, Trung, Nam; có nhạc nền và không có; podcast và hội thoại nhiều người
- [ ] Blog mẹo: "Cách tăng độ chính xác khi chuyển tiếng Việt thành văn bản"
- [ ] Tính năng (nếu làm được): sửa transcript trực tiếp trên web, từ điển tên riêng hoặc thuật ngữ
- [ ] Tạo trang /vi/ chuyên cho tiếng Việt: "Chuyển giọng nói tiếng Việt thành văn bản"

### 3.2 Không đọc được link riêng tư
- [ ] Blog hướng dẫn cách xử lý thay thế: tải file về rồi upload, hoặc dùng link Google Drive, Dropbox, OneDrive
- [ ] Thêm thông báo lỗi rõ ràng trên tool khi gặp link private, kèm hướng dẫn ngay tại chỗ

---

## 4. Technical SEO

- [ ] **Schema `SoftwareApplication`**: `applicationCategory`, `operatingSystem: Web`, `offers.price = 0`, `featureList` liệt kê đủ nền tảng, MCP, live transcription, định dạng xuất, số ngôn ngữ
- [ ] **Schema `FAQPage`** trên trang chủ, /faq/ và từng tool page
- [ ] **Schema `HowTo`** trên các trang hướng dẫn (YouTube transcript, audio to text…)
- [ ] **Schema `Organization`** kèm logo, sameAs (mạng xã hội), contact
- [ ] **Phiên bản tiếng Việt `/vi/`** và `hreflang` (en ↔ vi); ưu tiên trang chủ và 4–5 tool page chính
- [ ] **Tạo mục /blog/**: hiện site chưa có. Đưa vào menu nav và footer
- [ ] **Internal link**: mỗi bài blog link về đúng tool page; tool page link ngược về bài blog liên quan
- [ ] **Sitemap**: thêm blog và các trang mới, submit lại trên Google Search Console
- [ ] **E-E-A-T**: trang About ghi rõ ai làm sản phẩm, thông tin liên hệ, ngày cập nhật; bài blog có tác giả và ngày cập nhật

---

## 5. Thứ tự ưu tiên

1. Blog MCP / Claude / ChatGPT (điểm khác biệt, Google chưa biết)
2. Privacy Policy và giới hạn file (số liệu cụ thể)
3. Benchmark độ chính xác tiếng Việt
4. Phiên bản `/vi/`, `hreflang` và schema
5. Tool page và blog cho Vimeo, LinkedIn, Twitch, Dailymotion
6. Các bài còn lại (tóm tắt YouTube, tải caption, link Drive/Dropbox, link private)

---

## 6. Kiểm tra lại sau khi cập nhật

- [ ] Hỏi lại Google / AI Overview cùng câu hỏi sau 2–4 tuần và so sánh với mục 0–3
- [ ] Theo dõi GSC: impression và click cho các truy vấn mới (MCP, real-time, tiếng Việt, Vimeo…)
- [ ] Ghi kết quả vào file `TranscriptX Backlinks.xlsx` (sheet KPI) hoặc thêm sheet "Content plan"
