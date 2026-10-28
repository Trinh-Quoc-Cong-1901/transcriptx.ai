# Danh sách chủ đề blog cho TranscriptX

Lọc từ `TranscriptX_SEO_Strategy.xlsx` (sheet `05_20_Pillar`, `06_100_Cluster`, `11_Content_Gap`).
Chỉ giữ các chủ đề **viết được thành bài kiến thức**: intent Informational (how-to, giải thích) và các bài so sánh / listicle.
Bỏ ra ngoài: tool page, landing theo định dạng/nền tảng, trang use case, pricing, about, trang bản địa.

URL trong file Excel dùng `/guides/…`. Ở đây mình đổi sang `/blog/<slug>` cho khớp với 3 bài đã có trong `page/blog/`.

**Quy tắc khi viết** (rút từ chính file Excel và lần sửa trang unlimited):
- Không hứa quá. Không viết "unlimited", "no paywall", "free forever" nếu sản phẩm không đúng như vậy.
- Không tự công bố % độ chính xác nếu chưa tự đo.
- Mục nào ghi **Cần xác minh** thì phải kiểm tra tính năng thật trước khi viết.
- Mỗi bài nhúng tool hoặc CTA dẫn về đúng tool page liên quan.

---

## Đã có trong `page/blog/`

| Slug | Liên quan trong Excel |
|---|---|
| `how-long-to-transcribe-1-hour-of-audio` | KD16-03 (chi phí / thời gian chép lời) |
| `how-to-transcribe-audio-faster` | KD18 (How-to Guides Hub) |
| `youtube-transcript-api-python` | KD14 (Transcript API) |

---

## ⭐ So sánh & BOFU (nhóm ưu tiên)

Cập nhật 2026-10-28. Danh sách đối thủ lấy từ SERP các keyword "best youtube transcript generator", "best AI transcription software", "best free transcription software", "turboscribe alternatives", "tiktok transcript generator", "youtube subtitle downloader", "youtube video summarizer". Hầu hết bài top SERP là blog của chính các vendor (Sonix, HappyScribe, NoteGPT, BibiGPT, Plaud…): mình viết được bài kiểu này, và phải viết công bằng hơn họ.

### Lợi thế để dựa vào (theo `_source/_index.md`)
- Free dùng hằng ngày, **không cần tài khoản** để thử (300 credits/ngày khi đăng nhập, file tới 500MB).
- Pro **$5.99/tháng** (yearly $71.88): rẻ hơn hầu hết đối thủ trả phí. Giá đối thủ phải kiểm tra lại lúc viết.
- **Một chỗ dán mọi link**: YouTube, TikTok, Instagram, Facebook, X… cộng upload (máy, Drive, Dropbox, OneDrive) và Record.
- Export **.txt .docx .pdf .srt .vtt**, timestamp bật/tắt được.
- **Chạy ngay trong ChatGPT và Claude** (connector MCP). Ít đối thủ có.
- Pro: nhận diện người nói, Live mode, lọc nhiễu.

### Không được hứa (đối thủ có, mình không có hoặc chưa có)
- Bot tự vào Zoom/Meet/Teams ghi biên bản (Otter, Fireflies, Fathom, Notta).
- Chép lời bởi người thật (Rev, HappyScribe).
- Sửa video bằng cách sửa chữ (Descript).
- Summary và Mind map đang **sắp ra mắt**: chưa dùng làm điểm so sánh.
- Dịch phụ đề, chat với video, flashcard: **cần xác minh** trước khi nhắc tới.

### Quy tắc riêng cho bài so sánh
1. Mỗi đối thủ có hồ sơ `_source/competitors/<tên>.md`: giá, giới hạn gói free, định dạng xuất, nguồn hỗ trợ. Mỗi dòng có link nguồn + **ngày kiểm tra**.
2. Test **cùng 1 video YouTube + 1 file audio** trên cả hai bên, ghi thời gian, số bước và kết quả.
3. Bảng so sánh đặt ngay sau khối `answer`. Mỗi bài có mục "Khi nào nên dùng <đối thủ>": nói thật điểm mạnh của họ.
4. Ảnh tĩnh trong bài chỉ chụp TranscriptX. Thông tin đối thủ thể hiện bằng bảng + link nguồn. Ảnh đối thủ (nếu cần) chỉ dùng trong video.
5. Không dùng logo đối thủ, không tự công bố % độ chính xác.

---

### ④ Trang BOFU theo 3 dạng (nhóm chuyển đổi cao nhất)

Người tìm các keyword này **đã biết mình cần tool**, chỉ đang chọn giữa các bên. Mỗi bài phải giúp họ ra quyết định ngay trong bài: bảng so sánh ở đầu, "chọn bên nào khi nào", CTA dùng thử free không cần tài khoản.

#### Dạng 1 · "[đối thủ] alternative" (người đang dùng X, muốn đổi)
Khung bài: answer → bảng TranscriptX vs X → vì sao người ta rời X (giới hạn free, giá, thiếu nguồn link…, có nguồn) → TranscriptX làm việc đó thế nào (ảnh TranscriptX) → khi nào vẫn nên ở lại X → 2–4 lựa chọn khác ngắn gọn → FAQ → CTA.

| # | Ưu tiên | Keyword chính | Slug | Góc viết |
|---|---|---|---|---|
| 1.1 | P0 | notegpt alternative | `notegpt-alternative` | NoteGPT mạnh summary/flashcard. Mình: không cần tài khoản, nhiều nền tảng link, SRT/VTT, chạy trong ChatGPT/Claude. |
| 1.2 | P0 | turboscribe alternative | `turboscribe-alternative` | Gói free TurboScribe giới hạn số file/độ dài (cần xác minh). Mình nhận link mạng xã hội, Pro $5.99. |
| 1.3 | P1 | otter ai alternative | `otter-alternative` | Cần bot vào họp thì dùng Otter. Chép file/link thì dùng mình. |
| 1.4 | P1 | tactiq alternative | `tactiq-alternative` | Tactiq là extension Chrome. Mình chạy web, mobile, trong ChatGPT. |
| 1.5 | P1 | downsub alternative | `downsub-alternative` | DownSub chỉ tải CC có sẵn. Video không có CC mình vẫn chép được. Gộp SaveSubs. |
| 1.6 | P1 | happyscribe alternative | `happyscribe-alternative` | Họ mạnh về người thật chép + dịch. Viết cho người chỉ cần AI, rẻ. |
| 1.7 | P1 | sonix alternative | `sonix-alternative` | So chi phí 10 giờ audio/tháng. |
| 1.8 | P1 | notta alternative | `notta-alternative` | |
| 1.9 | P1 | transkriptor alternative | `transkriptor-alternative` | |
| 1.10 | P1 | rev alternative | `rev-alternative` | Ghi rõ: cần người thật chép thì dùng Rev. |
| 1.11 | P2 | youtube-transcript.io alternative | `youtube-transcript-io-alternative` | |
| 1.12 | P2 | maestra alternative | `maestra-alternative` | |
| 1.13 | P2 | descript alternative (transcription) | `descript-alternative-transcription` | Chỉ so phần chép lời. |
| 1.14 | P2 | eightify / glasp alternative | `youtube-summarizer-alternatives` | **Chờ Summary ra mắt.** |

#### Dạng 2 · "X vs Y" (người đang phân vân giữa 2 bên)
Hai kiểu:
- **X vs TranscriptX**: volume thấp nhưng người tìm sắp mua. Viết ngắn (1,000–1,400 từ), bảng chi tiết, kết luận "chọn X nếu…, chọn TranscriptX nếu…".
- **X vs Y (không có mình)**: volume cao hơn. Mình làm trọng tài công bằng, so đủ 2 bên, cuối bài thêm mục "Cần chép link/file giá rẻ? Thử TranscriptX". Không chen TranscriptX vào bảng chính.

Khung bài: answer (ai thắng ở nhu cầu nào) → bảng so sánh → từng tiêu chí (giá, gói free, nguồn hỗ trợ, export, ngôn ngữ, tính năng riêng) → test cùng 1 file → kết luận theo nhu cầu → FAQ → CTA.

| # | Ưu tiên | Keyword chính | Slug | Kiểu |
|---|---|---|---|---|
| 2.1 | P1 | notegpt vs tactiq | `notegpt-vs-tactiq` | X vs Y |
| 2.2 | P1 | turboscribe vs otter | `turboscribe-vs-otter` | X vs Y |
| 2.3 | P1 | otter vs fireflies | `otter-vs-fireflies` | X vs Y (mình chỉ nhắc ở cuối) |
| 2.4 | P1 | turboscribe vs happyscribe | `turboscribe-vs-happyscribe` | X vs Y |
| 2.5 | P2 | rev vs otter | `rev-vs-otter` | X vs Y |
| 2.6 | P2 | descript vs otter | `descript-vs-otter` | X vs Y |
| 2.7 | P1 | youtube transcript vs transcriptx | `youtube-built-in-transcript-vs-transcriptx` | X vs TranscriptX (KD15-04) |
| 2.8 | P2 | transcriptx vs notegpt | `transcriptx-vs-notegpt` | X vs TranscriptX |
| 2.9 | P2 | transcriptx vs turboscribe | `transcriptx-vs-turboscribe` | X vs TranscriptX |
| 2.10 | P2 | whisper vs transcriptx (online) | `whisper-vs-transcriptx` | X vs TranscriptX: Whisper cần cài, mình chỉ dán link |

#### Dạng 3 · "Best … tools 2026" (listicle, volume cao nhất)
Khung bài: answer (top 3 theo nhu cầu) → bảng tổng hợp → **cách mình test** (cùng 1 video/file, tiêu chí, ngày test) → từng tool: phù hợp với ai, ưu, nhược, giá, gói free → bảng "chọn theo nhu cầu" → FAQ → CTA.
- TranscriptX được đặt ở vị trí đầu **chỉ cho nhu cầu nó thật sự thắng** (vd. "free, không cần tài khoản, nhiều nền tảng link"). Các nhu cầu khác ghi đúng tool thắng.
- Tiêu đề có "2026", cập nhật lại giá và giới hạn mỗi quý.

| # | Ưu tiên | Keyword chính | Slug | Tool trong list |
|---|---|---|---|---|
| 3.1 | P0 | best youtube transcript generator | `best-youtube-transcript-generator` | TranscriptX, NoteGPT, Tactiq, youtube-transcript.io, Recall, Glasp, transcript gốc YouTube |
| 3.2 | P0 | best free transcription software | `best-free-transcription-software` | TranscriptX, TurboScribe, Whisper/MacWhisper, Notta, Otter, Word, oTranscribe (KD15-05) |
| 3.3 | P1 | best ai transcription software | `best-ai-transcription-software` | TranscriptX, Sonix, HappyScribe, Rev, Otter, Descript, Transkriptor |
| 3.4 | P1 | best video to text converter | `best-video-to-text-converter` | dẫn về `/video-to-text/` |
| 3.5 | P1 | best tiktok transcript generator | `best-tiktok-transcript-generator` | ShortTranscript, GetTheScript, TokScribe, Kapwing, Maestra |
| 3.6 | P2 | best youtube subtitle downloader | `best-youtube-subtitle-downloader` | DownSub, SaveSubs, YouSubtitles |
| 3.7 | P2 | best audio to text converter | `best-audio-to-text-converter` | dẫn về `/audio-to-text/` |
| 3.8 | P2 | best youtube video summarizer | `best-youtube-video-summarizer` | **Chờ Summary ra mắt.** |

### Volume (Google Keyword Planner, user gửi 2026-10-28) và thứ tự viết

Mỗi bài = 1 cụm keyword. Volume ghi theo khoảng của Keyword Planner.

| Thứ tự | Slug | Dạng | Keyword chính · volume | Keyword phụ trong cụm · volume | Độ hợp với TranscriptX |
|---|---|---|---|---|---|
| 1 | `downsub-alternative` | Alternative | downsub alternative · 100–1K | savesubs alternative · 100–1K | Rất cao: dẫn về `/youtube-subtitle-downloader/`. Gộp DownSub + SaveSubs vào 1 bài (cùng loại tool) |
| 2 | `notegpt-alternative` | Alternative | notegpt alternative · 100–1K | notegpt alternatives · 10–100 | Rất cao |
| 3 | `turboscribe-alternative` | Alternative | turboscribe alternative · 100–1K | turboscribe alternatives free · 10–100 | Rất cao |
| 4 | `best-free-transcription-software` | Best | best free transcription software · 100–1K | free transcription software · 1K–10K; best free transcription app, free transcription apps, best free audio transcription, best free transcribe audio to text, best transcription app free, free software transcribe audio to text, best free app to transcribe audio to text, best audio to text converter free, speech to text transcription free, transcribe an audio file to text free · đều 100–1K | Cao: Free không cần tài khoản. Cụm lớn nhất |
| 5 | `best-youtube-transcript-generator` | Best | best youtube transcript generator · 100–1K | | Rất cao |
| 6 | `otter-alternative` | Alternative | otter ai alternative · 100–1K | otter ai competitors, alternatives to otter ai · 100–1K; otter ai alternatives free, similar to otter ai, otter ai free alternatives, apps similar to otter ai, sites like otter ai, websites like otter ai, otter ai similar, free alternative to otter ai · 10–100 | Trung bình: không có bot họp. Góc viết: ghi âm/Record, file và link |
| 7 | `happyscribe-alternative` | Alternative | happyscribe alternative · 100–1K | happyscribe alternatives · 100–1K | Cao |
| 8 | `best-transcription-software` | Best | best transcribing app · 1K–10K | best transcribe software · 1K–10K; best audio transcription software, best transcription ai, best transcription tools, best app for transcribing audio, programs to transcribe audio to text, online transcription software, professional transcription software · 100–1K | Cao. Khác bài 4: bài này so cả gói trả phí |
| 9 | `otter-vs-fireflies` | X vs Y | otter vs fireflies · 100–1K | otter ai vs fireflies, fireflies ai vs otter ai, fireflies vs otter · 100–1K | Thấp: mình chỉ là trọng tài, nhắc TranscriptX ở cuối. Lấy traffic, ít chuyển đổi |
| 10 | `rev-alternative` | Alternative | rev alternative · 10–100 | rev com alternatives, alternatives to rev, alternatives to rev com, alternatives to rev transcription, rev alternatives for freelancers, rev com alternatives for freelancers · 10–100 | Cao (với người chỉ cần AI) |
| 11 | `best-iphone-transcription-app` | Best | best iphone transcription app · 100–1K | | **Cần xác minh** trải nghiệm TranscriptX trên iPhone (`_source/mobile/`) |
| 12 | `descript-alternative-transcription` | Alternative | descript alternative · 100–1K | alternative to descript, descript free alternative, descript alternative free, descript competitor, software like descript · 10–100 | Thấp: Descript là app sửa video. Chỉ viết góc "chỉ cần chép lời" |
| 13 | `tactiq-alternative` | Alternative | tactiq alternative · 10–100 | | Cao, volume nhỏ |
| 14 | `notta-alternative` | Alternative | notta alternative · 10–100 | | Trung bình |
| 15 | `transkriptor-alternative` | Alternative | transkriptor alternative · 10–100 | | Cao, volume nhỏ |

**Bỏ (0–10):** sonix alternative, youtube transcript io alternative, notegpt vs tactiq.

**Chưa có volume** (user chưa tra): turboscribe vs otter, turboscribe vs happyscribe, rev vs otter, descript vs otter, best video to text converter, best tiktok transcript generator, best youtube subtitle downloader, free transcription software no sign up. Giữ trong danh sách, tra sau.

**Không làm blog:**
- transcribe a video for free · 10K–100K: người tìm muốn **dùng tool ngay**, nên nhắm bằng tool page `/video-to-text/`, không phải bài so sánh.
- best meeting transcription software · 100–1K và offline transcription software · 100–1K: TranscriptX không có bot họp và không chạy offline.

---

## Tổng hợp nhanh (30 bài, dòng 25 gộp 5 bài how-to)

| # | ID | Ưu tiên | Keyword chính | Slug đề xuất | Nhóm |
|---|---|---|---|---|---|
| 1 | KD01-02 | P0 | how to get transcript of youtube video | `how-to-get-youtube-transcript` | How-to YouTube |
| 2 | KD02-04 | P1 | how to download subtitles from youtube | `how-to-download-youtube-subtitles` | How-to YouTube |
| 3 | KD02-05 | P1 | youtube transcript without timestamps | `youtube-transcript-without-timestamps` | How-to YouTube |
| 4 | KD03-05 | P1 | how to transcribe a video | `how-to-transcribe-video` | How-to chung |
| 5 | KD06-04 | P1 | how to get transcript of tiktok video | `how-to-transcribe-tiktok` | How-to mạng xã hội |
| 6 | KD08-05 | P1 | chatgpt summarize youtube video | `summarize-youtube-with-chatgpt` | AI & ChatGPT |
| 7 | KD13-04 | P1 | can chatgpt watch youtube videos | `can-chatgpt-watch-youtube-videos` | AI & ChatGPT |
| 8 | KD14-02 | P1 | youtube transcript api blocked | `youtube-transcript-api-ip-blocked` | Developer |
| 9 | KD15-01 | P1 | turboscribe alternative | `turboscribe-alternative` | So sánh |
| 10 | KD15-02 | P1 | otter ai alternative | `otter-alternative` | So sánh |
| 11 | KD15-03 | P1 | notegpt alternative | `notegpt-alternative` | So sánh |
| 12 | KD15-05 | P1 | best free transcription software | `best-free-transcription-software` | So sánh |
| 13 | KD17-02 | P1 | is online transcription safe | `is-online-transcription-safe` | Kiến thức / Trust |
| 14 | KD02-03 | P2 | download youtube subtitles in english | `download-youtube-subtitles-any-language` | How-to YouTube |
| 15 | KD07-05 | P2 | how to transcribe instagram reels | `how-to-transcribe-instagram-reels` | How-to mạng xã hội |
| 16 | KD09-05 | P2 | srt vs vtt | `srt-vs-vtt` | Kiến thức |
| 17 | KD11-05 | P2 | detect language from audio | `auto-language-detection` | Kiến thức |
| 18 | KD13-05 | P2 | summarize podcast with ai | `summarize-podcast-with-ai` | AI & ChatGPT |
| 19 | KD14-05 | P2 | youtube transcript n8n | `youtube-transcript-n8n` | Developer |
| 20 | KD15-04 | P2 | youtube transcript vs | `youtube-built-in-transcript-vs-transcriptx` | So sánh |
| 21 | KD16-03 | P2 | transcription cost per minute | `transcription-cost-per-minute` | Kiến thức |
| 22 | KD17-03 | P2 | is it legal to transcribe youtube videos | `is-it-legal-to-transcribe-youtube-videos` | Kiến thức / Trust |
| 23 | KD17-04 | P2 | speaker identification transcription | `speaker-identification-transcription` | Kiến thức |
| 24 | KD17-05 | P2 | transcript with timestamps | `transcript-with-timestamps` | Kiến thức |
| 25 | KD18-01 → 05 | P2 | 5 bài how-to (podcast, Zoom, blog post, subtitles, iPhone) | xem nhóm 2 bên dưới | How-to chung |
| 26 | KD17-01 | P1 | most accurate transcription software | `transcription-accuracy-benchmark` | Research |

---

## 1. How-to YouTube

### KD01-02 · P0 · how to get transcript of youtube video
- **Slug:** `/blog/how-to-get-youtube-transcript`
- **Nội dung:** cách lấy transcript trên desktop, mobile, app YouTube và bằng TranscriptX; ảnh chụp từng bước.
- **Link về:** `/youtube-transcript/`

### KD02-04 · P1 · how to download subtitles from youtube
- **Slug:** `/blog/how-to-download-youtube-subtitles`
- **Nội dung:** cách thủ công so với dùng tool; xử lý video không có phụ đề.
- **Link về:** `/youtube-subtitle-downloader/`, `/download-youtube-transcript/`

### KD02-05 · P1 · youtube transcript without timestamps
- **Slug:** `/blog/youtube-transcript-without-timestamps`
- **Nội dung:** pain point phổ biến khi copy transcript từ YouTube; hướng dẫn tắt timestamp trong tool.
- **Link về:** `/download-youtube-transcript/`

### KD02-03 · P2 · download youtube subtitles in english
- **Slug:** `/blog/download-youtube-subtitles-any-language`
- **Nội dung:** dịch phụ đề rồi tải về.
- **Cần xác minh:** tính năng dịch transcript.

---

## 2. How-to chung (video, audio, podcast, meeting)

### KD03-05 · P1 · how to transcribe a video
- **Slug:** `/blog/how-to-transcribe-video`
- **Nội dung:** 3 cách: chép tay, auto-caption, AI; dẫn về tool.
- **Link về:** `/video-to-text/`

### KD18-01 · P2 · how to transcribe a podcast
- **Slug:** `/blog/how-to-transcribe-podcast`
- **Link về:** `/audio-to-text/`

### KD18-02 · P2 · how to transcribe zoom recording
- **Slug:** `/blog/how-to-transcribe-zoom-recording`
- **Link về:** `/video-to-text/`

### KD18-03 · P2 · youtube video to blog post
- **Slug:** `/blog/youtube-video-to-blog-post`
- **Link về:** `/youtube-transcript/`, `/youtube-video-summarizer/`

### KD18-04 · P2 · how to add subtitles to video
- **Slug:** `/blog/how-to-add-subtitles`
- **Link về:** tool tạo SRT/VTT

### KD18-05 · P2 · how to transcribe audio on iphone
- **Slug:** `/blog/transcribe-audio-iphone`
- **Link về:** `/voice-to-text/`, `/audio-to-text/`

---

## 3. How-to mạng xã hội

### KD06-04 · P1 · how to get transcript of tiktok video
- **Slug:** `/blog/how-to-transcribe-tiktok`
- **Nội dung:** cách làm trên app và trên web.
- **Link về:** `/tiktok-transcript/`

### KD07-05 · P2 · how to transcribe instagram reels
- **Slug:** `/blog/how-to-transcribe-instagram-reels`
- **Link về:** `/instagram-transcript/`

---

## 4. AI & ChatGPT (lợi thế riêng: connector)

### KD08-05 · P1 · chatgpt summarize youtube video
- **Slug:** `/blog/summarize-youtube-with-chatgpt`
- **Link về:** `/connectors/`, `/youtube-video-summarizer/`

### KD13-04 · P1 · can chatgpt watch youtube videos
- **Slug:** `/blog/can-chatgpt-watch-youtube-videos`
- **Nội dung:** câu hỏi phổ biến; giải thích giới hạn của ChatGPT rồi dẫn về connector.
- **Link về:** `/connectors/`

### KD13-05 · P2 · summarize podcast with ai
- **Slug:** `/blog/summarize-podcast-with-ai`
- **Link về:** `/connectors/`

---

## 5. Developer

### KD14-02 · P1 · youtube transcript api blocked
- **Slug:** `/blog/youtube-transcript-api-ip-blocked`
- **Nội dung:** dev dùng thư viện `youtube-transcript-api` bị YouTube chặn IP; cách xử lý. Excel đánh giá là cơ hội lớn.
- **Liên kết nội bộ:** bài đã có `youtube-transcript-api-python`.

### KD14-05 · P2 · youtube transcript n8n
- **Slug:** `/blog/youtube-transcript-n8n`

---

## 6. So sánh / Alternative

Đã chuyển lên đầu file, xem mục **⭐ So sánh / Alternative**.

---

## 7. Kiến thức / Trust

### KD17-02 · P1 · is online transcription safe
- **Slug:** `/blog/is-online-transcription-safe`
- **Cần xác minh:** thời gian lưu file, mã hoá.

### KD09-05 · P2 · srt vs vtt
- **Slug:** `/blog/srt-vs-vtt`

### KD11-05 · P2 · detect language from audio
- **Slug:** `/blog/auto-language-detection`

### KD16-03 · P2 · transcription cost per minute
- **Slug:** `/blog/transcription-cost-per-minute`
- **Nội dung:** so sánh AI với dịch vụ chép lời thủ công (khoảng $1–1.5/phút).
- **Liên kết nội bộ:** bài đã có `how-long-to-transcribe-1-hour-of-audio`.

### KD17-03 · P2 · is it legal to transcribe youtube videos
- **Slug:** `/blog/is-it-legal-to-transcribe-youtube-videos`
- **Cần xác minh:** nhờ người có chuyên môn pháp lý xem lại.

### KD17-04 · P2 · speaker identification transcription
- **Slug:** `/blog/speaker-identification-transcription`
- **Cần xác minh:** tính năng nhận diện người nói.

### KD17-05 · P2 · transcript with timestamps
- **Slug:** `/blog/transcript-with-timestamps`

---

## 8. Research (cần số liệu thật)

### KD17-01 · P1 · most accurate transcription software
- **Slug:** `/blog/transcription-accuracy-benchmark`
- **Ghi chú:** chỉ viết khi đã tự đo độ chính xác trên dữ liệu test thật. Không viết bài này bằng số ước lượng.
