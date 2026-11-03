# Trang mới nên làm

29/10/2026 · Mọi trang dưới đây đều lấy từ bộ từ khoá mới `keyword/tukhoamoi/new.md`. Đã bỏ những gì **bạn đã làm**: 26 trang tính năng trong `page/` (kể cả các mục có sẵn như MP3, Voice memos, Podcasts, Lectures trong `/audio-to-text/` và `/voice-to-text/`) và 7 bài blog đã viết. Chi tiết lý do ở `dinh-huong-trang-moi.md`.

## Bảng tổng

| # | Ưu tiên | Loại | URL | Intent | Từ khoá chính (volume) |
|---|---|---|---|---|---|
| 1 | P1 | Tính năng | `/interview-transcription/` | Mua công cụ: chép lời phỏng vấn, nghiên cứu | interview transcription (1K–10K) |
| 2 | P1 | Tính năng | `/meeting-transcription/` | Mua công cụ: chép lời bản ghi cuộc họp | meeting transcription (1K–10K) |
| 3 | P2 | Tính năng | `/auto-caption-generator/` | Dùng ngay: tạo file phụ đề cho video | auto caption generator (10K–100K) |
| 4 | P1 | Blog | `/blog/how-to-transcribe-an-interview/` | Tìm hiểu: cách chép lời phỏng vấn | how to transcribe interviews for qualitative research (100–1K) |
| 5 | P1 | Blog | `/blog/verbatim-vs-intelligent-verbatim/` | Tìm hiểu: các kiểu chép lời | verbatim transcription (1K–10K) |
| 6 | P1 | Blog | `/blog/how-to-transcribe-voice-memos-on-iphone/` | Tìm hiểu: làm trên iPhone | transcribe voice memos on iphone (1K–10K) |
| 7 | P1 | Blog | `/blog/how-to-transcribe-teams-meeting/` | Tìm hiểu | microsoft teams transcript (1K–10K) |
| 8 | P2 | Blog | `/blog/how-to-transcribe-google-meet/` | Tìm hiểu | google meet transcription (1K–10K) |
| 9 | P2 | Blog | `/blog/how-to-transcribe-a-lecture/` | Tìm hiểu | lecture transcription (100–1K) |
| 10 | P3 | Blog | `/blog/how-to-transcribe-a-deposition/` | Tìm hiểu (pháp lý) | deposition transcription (1K–10K) |
| 11 | P3 | Blog | `/blog/voicemail-to-text/` | Tìm hiểu | voicemail to text (100K–1M) |
| 12 | P1 | Blog | `/blog/how-to-transcribe-zoom-recording/` | Tìm hiểu | zoom transcription (1K–10K) |
| 13 | P2 | Blog | `/blog/how-to-add-subtitles-to-video/` | Tìm hiểu | add subtitles to video (10K–100K) |
| 14 | P2 | Blog | `/blog/how-to-transcribe-a-podcast/` | Tìm hiểu | podcast transcription (chưa có volume) |

**Tính năng:** trang công cụ có ô dán link hoặc tải file, làm trong `page/`, có `intent/1_kw.md` và 19 file ngôn ngữ.
**Blog:** làm trong `page/blog/<slug>/` theo skill `transcriptx-blog`, có link dẫn về trang Tính năng.

Thứ tự làm: 1 → 2 (kèm blog 4, 5, 7, 12) → 6 → 3 (kèm blog 13) → 8, 9, 14 → 10, 11.

---

## Trang Tính năng

### 1. `/interview-transcription/` · P1

- **Intent:** nhà nghiên cứu, sinh viên làm luận văn, nhà báo, HR có file ghi âm phỏng vấn, cần bản chữ để phân tích hoặc trích dẫn. Ý định mua công cụ.
- **Từ khoá chính:** `interview transcription` (1K–10K)
- **Từ khoá phụ:**

  | Volume | Từ khoá |
  |---|---|
  | 1K–10K | interview transcribe, transcribing the interview, qualitative research transcription, research transcription, qualitative transcription |
  | 100–1K | transcribe interview audio to text, interview transcription software, focus group transcription |
  | 10–100 | interview transcription app, transcribe interview free, transcribe interview online |

- **Góc nội dung:**
  - Tải file lên hoặc ghi âm trực tiếp bằng **Record**.
  - Timestamp ở từng đoạn để trích dẫn đúng chỗ.
  - Tách người nói (gói Pro): biết câu nào của người phỏng vấn, câu nào của người trả lời.
  - Xuất .docx để đưa vào Word hoặc phần mềm phân tích định tính.
  - Tab Notes để đánh dấu ý chính trong lúc đọc.
- **Không được viết:** "certified", "human-verified", "academic transcription services", "verbatim service". Ghi rõ đây là chép lời bằng AI, nên đọc lại trước khi trích dẫn.
- **Blog dẫn về:** #4, #5, #10.

### 2. `/meeting-transcription/` · P1

- **Intent:** người có bản ghi Zoom, Microsoft Teams hoặc Google Meet, cần biên bản bằng chữ. Ý định mua công cụ.
- **Từ khoá chính:** `meeting transcription` (1K–10K)
- **Từ khoá phụ:**

  | Volume | Từ khoá |
  |---|---|
  | 1K–10K | zoom transcription, zoom meeting transcription, teams meeting transcription, google meet transcription, transcribe zoom |
  | 100–1K | transcribe zoom recording, zoom recording transcript, transcribe meeting audio to text |

- **Góc nội dung:**
  - Tải bản ghi cuộc họp lên (.mp4 hoặc .m4a từ Zoom, Teams, Meet).
  - Dùng Live mode (gói Pro) cho cuộc họp đang diễn ra.
  - Tab Notes ghi quyết định và việc cần làm, dùng checklist.
  - Summary sắp ra mắt.
  - Mỗi nền tảng một đoạn ngắn: bản ghi được lưu ở đâu.
- **Phải nói thật:** TranscriptX **không có bot tự vào cuộc họp** như Otter hay Fireflies. Không nhắm "ai note taker", "ai meeting minutes" cho đến khi Summary ra mắt.
- **Blog dẫn về:** #7, #8, #12.

### 3. `/auto-caption-generator/` · P2

- **Intent:** creator cần phụ đề cho video để đăng YouTube hoặc đưa vào phần mềm dựng. Ý định dùng ngay.
- **Từ khoá chính:** `auto caption generator` (10K–100K)
- **Từ khoá phụ:**

  | Volume | Từ khoá |
  |---|---|
  | 10K–100K | auto captions, automatic captions, captions for videos |
  | chưa có volume | srt file generator, subtitle generator, caption generator for video |

- **Góc nội dung:**
  - Dán link hoặc tải video lên.
  - Tải phụ đề về dạng **.srt** hoặc **.vtt**.
  - Hướng dẫn đưa file vào YouTube Studio, Premiere hoặc CapCut.
- **Phải nói thật:** TranscriptX tạo **file phụ đề**, **không gắn chữ trực tiếp lên video**.
- ⚠️ **Trước khi làm:** xem 10 kết quả đầu trên Google. Nếu toàn là công cụ gắn chữ lên video (CapCut, VEED) thì hạ xuống P3.
- **Blog dẫn về:** #13.

---

## Bài Blog

### 4. `how-to-transcribe-an-interview` · P1

- **Intent:** tìm cách chép lời phỏng vấn cho nghiên cứu định tính.
- **Từ khoá chính:** `how to transcribe interviews for qualitative research` (100–1K)
- **Từ khoá phụ (đều 100–1K):**
  - how to transcribe qualitative interviews
  - transcribing qualitative interviews
  - transcribing interviews for qualitative research
  - how to transcribe an interview qualitative research
  - transcript in qualitative research
- **Dẫn về:** `/interview-transcription/`

### 5. `verbatim-vs-intelligent-verbatim` · P1

- **Intent:** muốn hiểu sự khác nhau giữa các kiểu chép lời.
- **Từ khoá chính:** `verbatim transcription` (1K–10K)
- **Từ khoá phụ (100–1K):**
  - intelligent verbatim
  - clean verbatim
  - full verbatim transcription
  - intelligent verbatim transcription
  - clean verbatim transcription
- **Dẫn về:** `/interview-transcription/`
- ⚠️ **Cần biết trước:** transcript AI của TranscriptX giữ cả "uh, um" (verbatim) hay bỏ đi (clean).

### 6. `how-to-transcribe-voice-memos-on-iphone` · P1

- **Intent:** người dùng iPhone muốn chuyển ghi âm trong app Voice Memos thành chữ.
- **Từ khoá chính:** `transcribe voice memos on iphone` (1K–10K)
- **Từ khoá phụ:**

  | Volume | Từ khoá |
  |---|---|
  | 1K–10K | transcribe iphone voice memo, transcribe voice memos from iphone, iphone transcribe voice memo, voice memo to text |
  | 100–1K | transcribe apple voice memos, iphone voice memo to text, convert voice memo to text |

- **Dẫn về:** `/voice-to-text/`. Trang này đã có mục "Voice memos and notes"; nên nâng mục đó lên H2.
- ⚠️ **Cần biết trước:** TranscriptX nhận file .m4a.

### 7. `how-to-transcribe-teams-meeting` · P1

- **Intent:** muốn lấy transcript cuộc họp Microsoft Teams.
- **Từ khoá chính:** `microsoft teams transcript` (1K–10K)
- **Từ khoá phụ (1K–10K):**
  - teams transcription
  - teams meeting transcription
  - microsoft transcription
- **Dẫn về:** `/meeting-transcription/`

### 8. `how-to-transcribe-google-meet` · P2

- **Intent:** muốn lấy transcript cuộc họp Google Meet.
- **Từ khoá chính:** `google meet transcription` (1K–10K)
- **Từ khoá phụ:**
  - google meet transcribing (1K–10K)
- **Dẫn về:** `/meeting-transcription/`

### 9. `how-to-transcribe-a-lecture` · P2

- **Intent:** sinh viên muốn chép lời bài giảng để ôn bài.
- **Từ khoá chính:** `lecture transcription` (100–1K)
- **Từ khoá phụ:**
  - transcribe lecture (100–1K)
  - lecture to notes ai (100–1K)
  - how to transcribe lectures
  - transcribe lectures to text
  - lecture recording to text
  - how to convert lecture recordings to text
- **Dẫn về:** `/audio-to-text/` và bài `how-to-summarize-a-youtube-video`. Nhắc tới tab Notes; Summary và Mind map sắp ra mắt.

### 10. `how-to-transcribe-a-deposition` · P3

- **Intent:** tìm cách chép lời khai và định dạng transcript pháp lý.
- **Từ khoá chính:** `deposition transcription` (1K–10K, tăng 900% trong 3 tháng)
- **Từ khoá phụ:**
  - legal transcript format (100–1K)
  - legal transcription (1K–10K)
  - court transcription (1K–10K)
- **Dẫn về:** `/interview-transcription/`
- **Phải nói thật:** toà án thường yêu cầu bản chép lời có chứng nhận. AI hợp để làm bản nháp hoặc tìm nhanh nội dung. Không làm trang dịch vụ Legal.

### 11. `voicemail-to-text` · P3

- **Intent:** muốn đọc voicemail bằng chữ. Phần lớn người tìm muốn bật tính năng có sẵn trên iPhone hoặc Android.
- **Từ khoá chính:** `voicemail to text` (100K–1M)
- **Từ khoá phụ:**
  - free voicemail to text (10K–100K)
  - voicemail to text apps (10K–100K)
  - voicemail transcription (1K–10K)
- **Dẫn về:** `/voice-to-text/`
- **Góc nội dung:** hướng dẫn bật tính năng trên điện thoại trước, rồi cách lưu file voicemail và tải lên TranscriptX khi cần bản chữ đầy đủ. Chỉ viết sau khi đã làm xong P1–P2.

### 12. `how-to-transcribe-zoom-recording` · P1

- **Intent:** có bản ghi Zoom, muốn ra chữ.
- **Từ khoá chính:** `zoom transcription` (1K–10K)
- **Từ khoá phụ:**

  | Volume | Từ khoá |
  |---|---|
  | 1K–10K | zoom meeting transcription, zoom transcript, transcribe zoom |
  | 100–1K | transcribe zoom recording, how to transcribe zoom meetings, how to transcribe a zoom recording, zoom recording transcript |

- **Dẫn về:** `/meeting-transcription/`
- **Góc nội dung:** tìm bản ghi Zoom (cloud hoặc máy tính), tải lên TranscriptX, xuất .docx. Nói rõ là không có bot tự vào họp.

### 13. `how-to-add-subtitles-to-video` · P2

- **Intent:** muốn thêm phụ đề cho video của mình.
- **Từ khoá chính:** `add subtitles to video` (10K–100K)
- **Từ khoá phụ:**
  - captions for videos (10K–100K)
  - closed captioning (10K–100K)
  - how to add captions to video (chưa có volume)
  - closed captions vs subtitles (chưa có volume)
- **Dẫn về:** `/auto-caption-generator/` và `/youtube-subtitle-downloader/`
- **Góc nội dung:** tạo file .srt/.vtt bằng TranscriptX, rồi tải lên YouTube Studio hoặc phần mềm dựng (đưa ảnh bên thứ ba vào video, không đưa vào bài).

### 14. `how-to-transcribe-a-podcast` · P2

- **Intent:** podcaster muốn transcript cho show notes; người nghe muốn chữ của một tập.
- **Từ khoá chính:** `podcast transcription` (chưa có volume, cần tra)
- **Từ khoá phụ (chưa có volume):**
  - how to transcribe a podcast
  - podcast to text
  - podcast show notes generator
  - repurpose podcast into content
- **Dẫn về:** `/audio-to-text/` (đã có mục Podcasts)

---

## Cần kiểm chứng trước khi viết

- TranscriptX nhận file **.m4a** (cho bài #6 và trang #2).
- Transcript AI ra kiểu **verbatim hay clean** (cho bài #5).
- **Live mode** có dùng được cho cuộc họp Zoom/Teams đang diễn ra không, nghe qua micro hay âm thanh hệ thống (cho trang #2).
- **Volume** của: srt file generator, subtitle generator (cho trang #3).
- **KD** (độ khó SEO) của các từ khoá P1 trên Ahrefs/Semrush.
