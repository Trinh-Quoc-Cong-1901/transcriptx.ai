# Định hướng trang mới từ bộ từ khoá `new.md`

29/10/2026 · Dựa trên `keyword/tukhoamoi/new.md` (Keyword Planner), đối chiếu với các trang đang có trong `page/`, kế hoạch blog `page/blog/_blog_topics.md` và kho sản phẩm `page/blog/_source/_index.md`.

## 0. Bảng tổng: trang nào là Tính năng, trang nào là Blog

Đã rà toàn bộ 26 trang trong `page/` (đọc H1, H2, H3 của từng `en.json` và mọi `intent/1_kw.md`) và kế hoạch blog trong `_blog_topics.md`. Chủ đề nào đã có trang hoặc có mục riêng thì **không làm trang mới**, chỉ bổ sung vào trang đó.

- **Tính năng:** trang công cụ mới có ô dán link/tải file. Làm trong `page/`, có `intent/1_kw.md` và 19 file ngôn ngữ. Chỉ làm khi chưa trang nào nhắm từ khoá đó.
- **Cập nhật:** trang đã có. Thêm từ khoá vào H2, H3 hoặc FAQ sẵn có, hoặc nâng một H3 lên thành H2.
- **Blog:** bài hướng dẫn trong `page/blog/<slug>/`, dẫn về trang Tính năng.

| # | Ưu tiên | Loại | URL | Từ khoá (volume) | Đã có ở đâu / lý do |
|---|---|---|---|---|---|
| 1 | P1 | Cập nhật | `/youtube-transcript/` | + youtube video to text, youtube to text, youtube video to text converter, transcribe youtube video to text, youtube video transcriber (10K–100K) | `1_kw.md` chưa có các biến thể "to text" |
| 2 | P1 | Cập nhật | `/audio-to-text/` | + **mp3 to text** (10K–100K), audio into text, sound to text, transcribe sound to text, sound into text (100K–1M) | Đã có H3 **MP3** và **M4A and AAC** trong "Supported Audio Formats". Nâng MP3 lên H2 "MP3 to Text", không làm trang `/mp3-to-text/` riêng |
| 3 | P1 | Cập nhật | `/voice-to-text/` | + **voice memo to text** (1K–10K), transcribe voice memos, voice memo to text converter, voice into text (100K–1M), speech to text converter (10K–100K) | Đã có H3 **"Voice memos and notes"**. Nâng lên H2 "Voice Memo to Text", không làm trang `/voice-memo-to-text/` riêng |
| 4 | P2 | Cập nhật | `/video-to-text/` | + mp4 to text (chưa có volume) | Đã có H3 **MP4** và **"Zoom, Teams and Meet recordings"** |
| 5 | P2 | Cập nhật | `/live-transcription/` | + live captioning (10K–100K) | Chỉ thêm khi Live mode hiện chữ trực tiếp trên màn hình |
| 6 | P1 | **Tính năng** | `/interview-transcription/` | interview transcription (1K–10K), qualitative research transcription, research transcription, transcribe interview audio to text | Chưa có trang nào nhắm. Ở các trang khác chỉ là 1 dòng H3 "Interviews" |
| 7 | P1 | **Tính năng** | `/meeting-transcription/` | meeting transcription (1K–10K), zoom transcription, teams meeting transcription, google meet transcription | Chưa có trang nào nhắm. Phải nói rõ không có bot tự vào họp |
| 8 | P2 | **Tính năng** | `/auto-caption-generator/` | auto caption generator, auto captions, automatic captions, captions for videos (10K–100K) | Chưa có trang tạo phụ đề (`/youtube-subtitle-downloader/` là tải phụ đề có sẵn). Kiểm tra SERP trước |
| 9 | P1 | Blog | `how-to-transcribe-voice-memos-on-iphone` | transcribe voice memos on iphone (1K–10K) | Thay bài `transcribe-audio-iphone` (chưa viết) → `/voice-to-text/` |
| 10 | P1 | Blog | `how-to-transcribe-an-interview` | how to transcribe interviews for qualitative research (100–1K) | → `/interview-transcription/` |
| 11 | P1 | Blog | `verbatim-vs-intelligent-verbatim` | verbatim transcription (1K–10K) | → `/interview-transcription/` |
| 12 | P1 | Blog | `how-to-transcribe-teams-meeting` | microsoft teams transcript (1K–10K) | → `/meeting-transcription/` |
| 13 | P2 | Blog | `how-to-transcribe-google-meet` | google meet transcription (1K–10K) | → `/meeting-transcription/` |
| 14 | P2 | Blog | `how-to-transcribe-a-lecture` | lecture transcription, transcribe lecture, lecture to notes ai (100–1K) | Thay cho trang `/lecture-transcription/` (đã có H3 Lectures) → `/audio-to-text/` |
| 15 | P2 | Blog (đã có kế hoạch) | `how-to-transcribe-podcast` | how to transcribe a podcast, podcast transcription | Thay cho trang `/podcast-transcription/` (đã có H3 Podcasts) → `/audio-to-text/` |
| 16 | P2 | Blog (đã có kế hoạch) | `how-to-transcribe-zoom-recording` | transcribe zoom recording, zoom recording transcript (100–1K) | → `/meeting-transcription/` |
| 17 | P2 | Blog (đã có kế hoạch) | `how-to-add-subtitles` | add subtitles to video (10K–100K) | → `/auto-caption-generator/` |
| 18 | P3 | Blog | `how-to-transcribe-a-deposition` | deposition transcription (1K–10K), legal transcript format | Không làm trang dịch vụ Legal → `/interview-transcription/` |
| 19 | P3 | Blog | `voicemail-to-text` | voicemail to text (100K–1M) | → `/voice-to-text/` |

**Tổng:** 5 trang cập nhật, **3 trang Tính năng mới** (interview, meeting, auto caption), 11 bài blog (8 bài mới, 3 bài đã có trong kế hoạch).

**Đã bỏ so với bản trước:** `/mp3-to-text/`, `/voice-memo-to-text/`, `/lecture-transcription/`, `/podcast-transcription/`. Nội dung của 4 trang này đã có trong `/audio-to-text/` và `/voice-to-text/`; làm trang riêng sẽ trùng nội dung và tranh từ khoá với chính các trang đó.

## 1. Tóm tắt: bạn cần làm gì

1. **Không làm lại các trang đầu bảng.** Video to text, audio to text, YouTube transcript, voice to text, live transcription đều **đã có trang**. Việc cần làm là bổ sung các biến thể còn thiếu vào những trang đó (mục 3).
2. **Bổ sung từ khoá cho các trang đang có**, kể cả mp3 to text và voice memo to text: nâng các H3 sẵn có thành H2 trong `/audio-to-text/` và `/voice-to-text/` (mục 0, dòng 2–3).
3. **Chỉ làm 3 trang Tính năng mới**, vì chưa trang nào nhắm các từ này: **Interview Transcription**, **Meeting Transcription** (P1), **Auto Caption Generator** (P2).
4. **Viết 8 bài blog mới** để dẫn traffic về các trang trên (mục 5). Không trùng với kế hoạch blog hiện có.
5. **Không làm trang "dịch vụ" Legal/Medical** theo kiểu bảng giá theo phút và cam kết chứng nhận như đánh giá cũ đề xuất. Lý do ở mục 2.
6. **Bỏ qua** các cụm nhiễu (mục 6).

## 2. Đánh giá lại dữ liệu

### Sửa lại kết luận cũ trong `new.md`

Đánh giá cũ xếp **Legal** và **Academic/Research "services"** là ưu tiên 1, kèm bảng giá theo phút và cam kết bảo mật, độ chính xác. Cách này **không khớp với sản phẩm**:

- TranscriptX là công cụ AI tự phục vụ: dán link hoặc tải file lên, nhận transcript. Không có người chép lời, không có chứng nhận, không bán theo phút. `_blog_topics.md` ghi rõ "Không được hứa: chép lời bởi người thật".
- Người tìm "legal transcription services", "court transcribers", "certified legal transcription" muốn **thuê** người chép lời có chứng nhận, đúng định dạng của toà. Một trang AI sẽ không đáp ứng được ý định đó và dễ bị coi là hứa quá.
- Ngược lại, **Interview/Research** rất hợp: nhà nghiên cứu, sinh viên, nhà báo tự tải file phỏng vấn lên, cần timestamp, tách người nói (Pro) và xuất .docx. Đây là ưu tiên 1 thật sự.
- **Legal** chỉ nên đi bằng blog thông tin (cách chép lời khai, định dạng transcript pháp lý), không làm landing page dịch vụ.

### Cụm nào khớp với TranscriptX

| Cụm | Khớp | Ghi chú |
|---|---|---|
| Video / YouTube / Audio | ✅ Rất khớp | Đã có trang, chỉ cần tối ưu thêm |
| MP3 / Voice memo | ✅ Rất khớp | Chưa có trang riêng, làm mới |
| Interview / Research | ✅ Khớp | Tải file, timestamp, tách người nói (Pro), .docx |
| Meeting (Zoom/Teams/Meet) | 🟡 Khớp một phần | Không có bot vào họp. Chỉ hứa: tải bản ghi lên hoặc dùng Live mode (Pro) |
| Caption / Subtitle | 🟡 Khớp một phần | Xuất được file .srt/.vtt, **không** gắn chữ lên video |
| Lecture / Education | 🟡 Khớp | Phần "khoá học, chứng chỉ transcription" là nhiễu |
| Legal / Insurance / Police | ⚠️ Ý định sai | Người tìm muốn thuê dịch vụ có chứng nhận. Chỉ viết blog |
| Medical | ❌ | Từ lớn nhất là tìm việc. AI scribe cần HIPAA, không hứa được |
| Call / Voicemail | ❌ phần lớn | Nhiễu thương hiệu TextNow. "voicemail to text" là tính năng của điện thoại/nhà mạng |
| Financial / Sermon | ❌ | Người tìm muốn **đọc** transcript hoặc bài giảng có sẵn |

## 3. Tối ưu trang đang có (không làm trang mới)

Thêm các từ dưới đây vào H2, FAQ hoặc đoạn văn của trang tương ứng (cả `intent/1_kw.md` và `en.json`). Không làm trang riêng cho chúng để tránh 2 trang tranh nhau cùng từ khoá.

| Trang | Đã nhắm | Thêm từ `new.md` (volume) |
|---|---|---|
| `/youtube-transcript/` | youtube transcript, transcribe from youtube, youtube transcript generator… | youtube video to text (10K–100K), youtube to text (10K–100K), youtube video to text converter (10K–100K), transcribe youtube video to text (10K–100K), youtube video transcriber (10K–100K) |
| `/video-to-text/` | video to text, transcribe video to text free… | video transcriber (10K–100K, kiểm tra đã có trong H1/H2 chưa), mp4 to text (chưa có volume) |
| `/audio-to-text/` | audio to text, transcribe audio, audio to text converter… | audio into text (100K–1M), transcribe sound to text (100K–1M), sound to text transcription (100K–1M), sound into text (100K–1M), audio transcription free (10K–100K) |
| `/voice-to-text/` | voice to text, transcribe a voice recording… | voice into text (100K–1M), speech to text converter (10K–100K) |
| `/live-transcription/` | live transcription, real time transcription… | live captioning (10K–100K). Chỉ thêm nếu Live mode hiển thị chữ trực tiếp trên màn hình; không hứa CART cho sự kiện |

## 4. Trang mới đề xuất

> ⚠️ **Cập nhật 29/10 sau khi rà toàn bộ `page/`:** chỉ làm **interview**, **meeting** và **auto caption**. Bốn trang **MP3**, **Voice Memo**, **Lecture** và **Podcast** dưới đây **không làm trang riêng**. Nội dung đã có trong `/audio-to-text/` (H3 MP3, M4A, Podcasts, Lectures) và `/voice-to-text/` (H3 Voice memos). Phần từ khoá của 4 trang này dùng để bổ sung vào 2 trang đó hoặc cho blog (xem mục 0).

### Tổng quan

| Ưu tiên | URL | Loại trang | Intent | Từ khoá chính (volume) |
|---|---|---|---|---|
| P1 | `/mp3-to-text/` | Tool | Mua/dùng ngay: đổi file MP3 thành chữ | mp3 to text (10K–100K) |
| P1 | `/voice-memo-to-text/` | Tool | Mua/dùng ngay: chép lời ghi âm trên iPhone | voice memo to text (1K–10K) |
| P1 | `/interview-transcription/` | Use-case | Mua: công cụ chép lời phỏng vấn, nghiên cứu | interview transcription (1K–10K) |
| P1 | `/meeting-transcription/` | Use-case | Mua: chép lời bản ghi cuộc họp | meeting transcription (1K–10K) |
| P2 | `/auto-caption-generator/` | Tool | Mua: tạo file phụ đề cho video | auto caption generator (10K–100K) |
| P2 | `/lecture-transcription/` | Use-case | Mua: chép lời bài giảng, ghi chú | lecture transcription (100–1K) |
| P2 | `/podcast-transcription/` | Use-case | Mua: chép lời podcast | podcast transcription (**chưa có volume**) |

### P1 · `/mp3-to-text/` – MP3 to Text · ❌ không làm trang riêng (xem mục 0)

- **Intent:** người có sẵn file .mp3 (podcast tải về, ghi âm, nhạc) muốn ra văn bản ngay, thường muốn miễn phí. Ý định giao dịch, cùng nhóm với audio-to-text nhưng nhắm theo định dạng file.
- **Từ khoá chính:** `mp3 to text` (10K–100K)
- **Từ khoá phụ:**
  - mp3 to text converter
  - convert mp3 to text
  - mp3 to text free
  - mp3 transcription
  - transcribe mp3 to text
  - mp3 file to text
  - free mp3 to text converter
  - mp3 to text online

  (Các biến thể này chưa có volume, cần tra.)
- **Góc nội dung:** tải .mp3 lên (từ máy, Google Drive, Dropbox, OneDrive), nhận transcript có timestamp, xuất .txt/.docx/.pdf/.srt/.vtt. Free mỗi ngày, file đến 500MB (Pro 2GB).
- **Tránh trùng:** `/audio-to-text/` giữ các từ "audio"; trang này chỉ nhắm "mp3".

### P1 · `/voice-memo-to-text/` – Voice Memo to Text · ❌ không làm trang riêng (xem mục 0)

- **Intent:** người dùng iPhone có ghi âm trong app Voice Memos, muốn chuyển thành chữ. Ý định giao dịch, nhiều người làm trên điện thoại.
- **Từ khoá chính:** `voice memo to text` (1K–10K)
- **Từ khoá phụ:**

  | Nhóm volume | Từ khoá |
  |---|---|
  | 1K–10K | transcribe voice memos, transcribe iphone voice memo, voice memo to text converter, transcribe voice memos on iphone, voice memo transcribe |
  | 100–1K | convert voice memo to text, voice memo transcription free, transcribe apple voice memos, voice memo transcription app, voice note transcription |

- **Góc nội dung:** xuất file .m4a từ Voice Memos (Share → Save to Files), tải lên TranscriptX trên điện thoại. Có ảnh giao diện mobile trong `_source/mobile/`.
- **Tránh trùng:** `/voice-to-text/` nhắm "voice recording" chung; trang này nhắm app Voice Memos và iPhone. Bài blog `transcribe-audio-iphone` (KD18-05) nên chuyển sang dẫn về trang này.
- ⚠️ **Cần xác nhận:** TranscriptX nhận file .m4a.

### P1 · `/interview-transcription/` – Interview Transcription

- **Intent:** nhà nghiên cứu, sinh viên làm luận văn, nhà báo, HR cần chép lời bản ghi phỏng vấn để phân tích hoặc trích dẫn. Ý định mua công cụ. Cạnh tranh quảng cáo rất thấp.
- **Từ khoá chính:** `interview transcription` (1K–10K)
- **Từ khoá phụ:**

  | Nhóm volume | Từ khoá |
  |---|---|
  | 1K–10K | interview transcribe, transcribing the interview, qualitative research transcription, research transcription, qualitative transcription |
  | 100–1K | transcribe interview audio to text, interview transcription software, focus group transcription |
  | 10–100 | interview transcription app, transcribe interview free |

- **Góc nội dung:** tải file hoặc ghi âm trực tiếp (Record). Transcript có timestamp để trích dẫn, tách người nói trên gói Pro, xuất .docx cho NVivo/Word. Nói rõ là chép lời bằng AI, nên đọc lại trước khi trích dẫn.
- **Không viết:** "certified", "verbatim service", "human-verified", "academic transcription services".

### P1 · `/meeting-transcription/` – Meeting Transcription

- **Intent:** người có bản ghi Zoom, Teams hoặc Google Meet cần biên bản bằng chữ. Ý định mua.
- **Từ khoá chính:** `meeting transcription` (1K–10K)
- **Từ khoá phụ:**

  | Nhóm volume | Từ khoá |
  |---|---|
  | 1K–10K | zoom transcription, zoom meeting transcription, teams meeting transcription, microsoft teams transcript, google meet transcription |
  | 100–1K | transcribe zoom recording, zoom recording transcript, transcribe meeting audio to text |

- **Góc nội dung:** tải bản ghi cuộc họp lên, hoặc dùng Live mode (Pro) cho cuộc họp đang diễn ra. Tab Notes ghi quyết định và việc cần làm. Summary sắp ra mắt.
- ⚠️ **Phải nói thật:** TranscriptX **không có bot tự vào cuộc họp** như Otter hay Fireflies. Không nhắm "ai note taker", "fireflies ai note taker", "ai meeting minutes" cho tới khi Summary ra mắt.

### P2 · `/auto-caption-generator/` – Auto Caption Generator

- **Intent:** creator muốn có phụ đề cho video. Nhiều người muốn chữ hiện thẳng trên video (kiểu CapCut). Trang này phục vụ nhóm cần **file phụ đề** để tải lên YouTube hoặc phần mềm dựng.
- **Từ khoá chính:** `auto caption generator` (10K–100K)
- **Từ khoá phụ:**
  - auto captions (10K–100K)
  - automatic captions (10K–100K)
  - captions for videos (10K–100K)
  - add subtitles to video (10K–100K, dẫn sang blog `how-to-add-subtitles`)
  - srt file generator (chưa có volume)
- **Góc nội dung:** dán link hoặc tải video lên, tải về .srt/.vtt, rồi đưa vào YouTube Studio, Premiere hay CapCut.
- ⚠️ **Phải nói thật:** TranscriptX không gắn phụ đề trực tiếp lên video. Kiểm tra lại SERP trước khi làm: nếu top 10 toàn là công cụ gắn phụ đề lên video thì hạ xuống P3.

### P2 · `/lecture-transcription/` – Lecture Transcription · ❌ không làm trang riêng (xem mục 0)

- **Intent:** sinh viên muốn chép lời bài giảng hoặc video khoá học để ôn bài. Ý định mua/dùng.
- **Từ khoá chính:** `lecture transcription` (100–1K)
- **Từ khoá phụ:**
  - transcribe lecture (100–1K)
  - lecture to notes ai (100–1K)
  - transcribe lectures to text
  - lecture recording to text
  - how to convert lecture recordings to text
  - webinar transcription
- **Góc nội dung:** ghi âm trực tiếp trong lớp (Record) hoặc dán link YouTube bài giảng. Tab Notes ghi ý chính ngay cạnh transcript. Summary và Mind map sắp ra mắt. Liên kết với bài blog tóm tắt video YouTube.
- **Không nhắm:** "transcription courses", "transcription certification". Đó là người tìm khoá học nghề.

### P2 · `/podcast-transcription/` – Podcast Transcription · ❌ không làm trang riêng (xem mục 0)

- **Intent:** podcaster cần transcript cho show notes và SEO; người nghe cần chữ của một tập podcast.
- **Từ khoá chính:** `podcast transcription` (**chưa có volume**, cần tra trước khi làm)
- **Từ khoá phụ (cần tra):**
  - podcast transcript
  - transcribe podcast
  - podcast to text
  - podcast transcription free
  - podcast show notes generator
- **Góc nội dung:** dán link podcast hoặc tải file lên, có timestamp, xuất .docx/.srt. Tính năng tách người nói (Pro) hữu ích cho podcast có khách mời. Bài `how-to-transcribe-podcast` (KD18-01) đã có trong kế hoạch, dẫn về trang này.

## 5. Blog mới (thông tin, dẫn về trang ở mục 4)

Danh sách dưới đây chưa có trong `_blog_topics.md`. Nhóm 1 là để ủng hộ trang P1.

| Ưu tiên | Slug | Intent | Từ khoá chính (volume) | Từ khoá phụ | Dẫn về |
|---|---|---|---|---|---|
| P1 | `how-to-transcribe-an-interview` | Tìm hiểu: cách chép lời phỏng vấn định tính | how to transcribe interviews for qualitative research (100–1K) | how to transcribe qualitative interviews, transcribing qualitative interviews, how to transcribe an interview qualitative research, transcript in qualitative research (đều 100–1K) | `/interview-transcription/` |
| P1 | `verbatim-vs-intelligent-verbatim` | Tìm hiểu: các kiểu chép lời | verbatim transcription (1K–10K) | intelligent verbatim, clean verbatim, full verbatim transcription, intelligent verbatim transcription (100–1K) | `/interview-transcription/` |
| P1 | `how-to-transcribe-voice-memos-on-iphone` | Tìm hiểu: làm trên iPhone | transcribe voice memos on iphone (1K–10K) | transcribe voice memos from iphone, iphone transcribe voice memo, transcribe apple voice memos | `/voice-memo-to-text/` (thay cho `transcribe-audio-iphone`) |
| P1 | `how-to-transcribe-teams-meeting` | Tìm hiểu | microsoft teams transcript (1K–10K) | teams transcription, teams meeting transcription, microsoft transcription | `/meeting-transcription/` |
| P2 | `how-to-transcribe-google-meet` | Tìm hiểu | google meet transcription (1K–10K) | google meet transcribing | `/meeting-transcription/` |
| P2 | `how-to-transcribe-a-lecture` | Tìm hiểu | transcribe lecture (100–1K) | how to transcribe lectures, transcribe lectures to text free | `/lecture-transcription/` |
| P3 | `how-to-transcribe-a-deposition` | Tìm hiểu (pháp lý) | deposition transcription (1K–10K, tăng 900%) | legal transcript format (100–1K), legal transcription, court transcription | `/interview-transcription/` |
| P3 | `voicemail-to-text` | Tìm hiểu | voicemail to text (100K–1M) | free voicemail to text, voicemail transcription, voicemail to text apps | `/voice-to-text/` |

Ghi chú:
- **Deposition / legal (P3):** viết như bài hướng dẫn. Nói rõ toà án thường yêu cầu bản chép lời có chứng nhận, còn AI hợp để làm bản nháp hoặc tìm nội dung nhanh.
- **Voicemail (P3):** volume rất lớn, nhưng phần lớn người tìm muốn bật tính năng trên iPhone/Android. Chỉ viết khi đã làm xong P1–P2.
- **Bài đã có trong kế hoạch, gắn thêm từ khoá mới:**
  - `how-to-transcribe-zoom-recording` nhận: transcribe zoom recording, how to transcribe a zoom recording, zoom recording transcript.
  - `how-to-add-subtitles` nhận: add subtitles to video (10K–100K).

## 6. Bỏ qua / để sau

| Cụm | Lý do |
|---|---|
| text to video, text to speech, animator free, text on video | Sản phẩm khác (tạo video, đọc văn bản) |
| TextNow, free text and call app, talkatone, dingtone | Tìm thương hiệu app gọi điện |
| medical transcriptionist, certified medical transcriptionist, medical transcription remote/from home | Tìm việc làm |
| ai medical scribe, hipaa compliant transcription, ambient clinical documentation | Cần HIPAA và tích hợp EHR; TranscriptX không hứa được |
| transcription courses, transcription training, certification | Tìm khoá học nghề |
| earnings call transcript (theo công ty), seeking alpha | Muốn đọc transcript có sẵn |
| sermon on the mount text, text sermons | Muốn đọc văn bản bài giảng |
| legal / court / insurance / police transcription services | Muốn thuê người có chứng nhận. Chỉ viết blog P3 như mục 5 |
| ai note taking, fireflies ai note taker, ai meeting minutes | Cần bot họp + tóm tắt. Xem lại khi Summary ra mắt |
| translate voice to text, translate voicemail to text | Cần xác minh TranscriptX có dịch không trước khi nhắm |
| speech to text for dyslexia (100–1K) | Có thể viết blog về hỗ trợ tiếp cận sau, không ưu tiên |

## 7. Thứ tự làm

1. **Tuần 1:** cập nhật 5 trang đang có theo mục 3. Ít công nhất, tận dụng được volume lớn.
2. **Tuần 2:** nâng H2 "MP3 to Text" trong `/audio-to-text/` và H2 "Voice Memo to Text" trong `/voice-to-text/`. Viết bài `how-to-transcribe-voice-memos-on-iphone`.
3. **Tuần 3–5:** làm `/interview-transcription/` và `/meeting-transcription/`, kèm 3 bài: interview, verbatim, Teams.
4. **Tuần 6+:** làm `/auto-caption-generator/` (kiểm tra SERP trước), rồi viết blog P2–P3 (lecture, podcast, Google Meet, Zoom, add subtitles, deposition, voicemail).

## 8. Cần kiểm chứng trước khi viết

- **File .m4a** (Voice Memos) và **.mp3** có tải lên được không; giới hạn dung lượng hiện tại (Pricing ghi Free 500MB / Pro 2GB).
- **Tách người nói** là tính năng Pro. Đoạn trong `page/homepage/homepage_intent.md` ghi "Dung lượng file: Không giới hạn" và "Tách người nói: Có" là **mâu thuẫn** với trang Pricing. Nên sửa file đó để các trang mới không chép sai.
- **Kiểu chép lời** của AI: verbatim (giữ cả "uh, um") hay clean. Cần biết trước khi viết bài verbatim.
- TranscriptX có **dịch transcript** không. Nếu có thì mở thêm cụm "translate".
- **Volume còn thiếu:** podcast transcription, mp3/mp4 variants, srt file generator.
- **KD (độ khó SEO)** của các từ P1 trên Ahrefs/Semrush. Keyword Planner chỉ cho biết cạnh tranh quảng cáo, không cho biết độ khó SEO.
