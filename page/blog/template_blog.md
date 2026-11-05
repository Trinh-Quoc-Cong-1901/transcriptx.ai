# Mẫu brief viết bài cho blog TranscriptX

Gửi mẫu này cho Claude mỗi khi cần viết một bài mới. Mục có dấu **(bắt buộc)** cần điền, các mục còn lại có thể bỏ trống để Claude tự chọn.

---

## 1. Từ khóa chính (bắt buộc)

```
Keyword: how to add subtitles to youtube videos
```

- Chỉ ghi **một** cụm. Claude sẽ dùng cụm này làm focus keyword, đặt vào tiêu đề, meta title và đoạn mở đầu.
- Nên chọn cụm có volume tốt và mức cạnh tranh "Thấp" trong Keyword Planner.

## 2. Danh sách từ khóa phụ (bắt buộc)

Dán nguyên dữ liệu từ Keyword Planner, không cần định dạng lại:

```
how to put subtitles on youtube videos
1 N – 10 N  0%  -90%  Thấp ...
how to add captions to youtube videos
1 N – 10 N  0%  0%  Thấp ...
```

- Claude chọn tối đa khoảng 15–20 cụm để đưa vào bài, phần SEO keywords và FAQ.
- Cụm nào **bắt buộc phải có** thì đánh dấu `*` ở đầu dòng.

## 3. Góc nhìn và thông điệp chính (bắt buộc)

Viết 1–3 câu: bài muốn người đọc hiểu điều gì, khác bài khác ở đâu.

```
Góc: Mọi người chỉ lo title, description, tag mà bỏ qua phụ đề.
Phụ đề giúp YouTube hiểu nội dung video. Dùng TranscriptX để lấy SRT miễn phí rồi upload lên.
```

## 4. Tool TranscriptX muốn dẫn tới

Chọn **một** slug (khối tool, CTA và link trong bài sẽ trỏ về đây):

| Slug | Tên tool |
|---|---|
| `home` | Trang chủ |
| `transcription-mcp` | Transcription MCP |
| `youtube-transcript` | YouTube Transcript |
| `download-youtube-transcript` | Download YouTube Transcript |
| `youtube-subtitle-downloader` | YouTube Subtitle Downloader |
| `youtube-video-summarizer` | YouTube Video Summarizer |
| `tiktok-transcript` | TikTok Transcript |
| `tiktok-caption-downloader` | TikTok Caption Downloader |
| `instagram-transcript` | Instagram Transcript |
| `instagram-caption-downloader` | Instagram Caption Downloader |
| `facebook-transcript` | Facebook Transcript |
| `x-transcript` | X Transcription |
| `twitter-transcript` | Twitter to Text |
| `x-spaces-transcript` | X Spaces Transcript |
| `twitter-spaces-transcript` | Twitter Spaces Transcript |
| `audio-to-text` | Audio to Text |
| `video-to-text` | Video to Text |
| `voice-to-text` | Voice to Text |
| `voicemail-to-text` | Voicemail to Text |
| `interview-transcription` | Interview Transcription |
| `live-transcription` | Live Transcription |
| `real-time-speech-to-text` | Real-Time Speech to Text |
| `unlimited-transcription` | Unlimited Transcription |
| `transcribe-large-audio-files` | Transcribe Large Audio Files |

```
Tool: video-to-text
```

## 5. Chuyên mục (topic)

| Slug | Tên |
|---|---|
| `guides` | Hướng dẫn |
| `youtube-social` | YouTube & mạng xã hội |
| `audio-podcasts` | Âm thanh & podcast |
| `comparisons` | So sánh |

```
Topic: youtube-social
```

## 6. Loại bài

Chọn một (giúp Claude chọn bố cục phù hợp):

- `how-to`: hướng dẫn từng bước (có HowTo schema)
- `comparison`: so sánh với công cụ khác, dạng "X alternative" hoặc "X vs Y"
- `explainer`: giải thích khái niệm, "what is…", "does… work"
- `listicle`: danh sách, "best…", "top 5…"

```
Loại: how-to
```

## 7. Ảnh chụp màn hình

- Đính kèm ảnh vào tin nhắn và ghi chú mỗi ảnh dùng cho bước nào.
- Ảnh nên là `.png`, `.jpg` hoặc `.webp`, rộng 1000–1200px, có khoanh đỏ phần cần chú ý.
- Không có ảnh thì Claude vẫn viết bài, và ghi chú vị trí nên chèn ảnh sau.

```
Ảnh 1: màn hình Video to Text sau khi upload  → bước 1
Ảnh 2: menu Download chọn .srt               → bước 4
Ảnh 3: YouTube Studio > Subtitles > Upload file → phần upload
```

## 8. Ngôn ngữ

```
Ngôn ngữ gốc: en
Dịch thêm: vi, es
```

Các ngôn ngữ hỗ trợ: `en, ar, bn, de, es, fr, hi, id, it, ja, ko, ms, my, pt, ru, th, tr, ur, vi`

## 9. Đăng bài

Chọn một:

- `draft`: chỉ lưu nháp để bạn duyệt (**mặc định**)
- `publish`: xuất bản ngay
- `schedule`: hẹn giờ, ghi rõ ngày giờ (ví dụ `2026-11-10 08:00 giờ Việt Nam`)

```
Đăng: draft
```

## 10. Ghi chú thêm (tùy chọn)

- Đối thủ hoặc bài tham khảo (dán link)
- Điều **không** được nói (ví dụ: không hứa "chắc chắn lên top")
- Bài cũ cần liên kết nội bộ tới
- Ảnh bìa: `video | mic | file | live | compare`, tông màu: `clay | oat | sage | sky | rose`

---

## Mẫu điền nhanh (copy và sửa)

```
Keyword: 
Từ khóa phụ:
[dán từ Keyword Planner]

Góc: 
Tool: 
Topic: 
Loại: 
Ảnh: [đính kèm + ghi chú]
Ngôn ngữ gốc: en | Dịch thêm: 
Đăng: draft
Ghi chú: 
```

---

## Claude sẽ tự làm những gì

Khi nhận brief, Claude sẽ:

1. Kiểm tra bài cũ trên blog để không viết trùng và để thêm liên kết nội bộ.
2. Tra cứu thông tin hiện hành (giao diện YouTube Studio, tính năng mới…) để bài viết chính xác.
3. Viết bài theo chuẩn blog:
   - **H1** dạng câu hỏi của người đọc
   - **Lede** 1–2 câu mở đầu
   - **Answer block** 40–60 từ trả lời thẳng (dùng cho AI search và featured snippet)
   - Các **H2** tạo mục lục, có bảng, danh sách và bước làm
   - **Khối tool** và **CTA** dẫn về tool đã chọn
   - **FAQ** 5–7 câu (FAQPage schema)
4. Điền SEO: meta title ≤ 60 ký tự, meta description ≤ 155 ký tự, focus keyword, tối đa 20 từ khóa phụ.
5. Cài đặt: topic, tag, tác giả, ảnh bìa, schema.
6. Lưu nháp và gửi link editor để bạn duyệt.
7. Chỉ xuất bản, hẹn giờ hoặc dịch khi bạn yêu cầu rõ.