# Nghiên cứu SEO cho API của TranscriptX

Ngày nghiên cứu: 08/10/2026
Đối thủ đã xem: Supadata.ai, TranscriptAPI.com, youtube-transcript.io, AssemblyAI. Ngoài ra có tham khảo các bài so sánh: ScrapeCreators, SocialKit, EasyTranscriber, các actor trên Apify và TranscriptFetch.

> Lưu ý: volume ở đây chỉ chia theo mức độ ưu tiên, không phải số đo thật. Trước khi chốt, nên kiểm tra lại volume và KD bằng Ahrefs/Semrush hoặc Keyword Planner.

---

## 1. Tóm tắt nhanh

- Thị trường chia thành 2 nhóm, và TranscriptX phải chọn đánh nhóm 1:
  1. **API lấy transcript từ URL video** (YouTube/TikTok/IG/FB). Đối thủ ở đây là Supadata, TranscriptAPI, youtube-transcript.io, ScrapeCreators. Đây là các site nhỏ, SEO đánh được.
  2. **API speech-to-text thuần** (upload file audio). Đối thủ là AssemblyAI, Deepgram, OpenAI Whisper, Google. Các site này domain rất mạnh và giá rẻ ($0.0025–0.006/phút). Vẫn làm trang mẹ "Speech-to-Text API" để gom cây sản phẩm (xem mục 3), nhưng **không kỳ vọng thắng từ khoá đầu "speech to text api" sớm**. Nên thắng ở trang con trước: theo định dạng (mp3/mp4/wav), theo URL và theo social.
- Lợi thế sẵn có của TranscriptX là **đã có tool free theo từng nền tảng** (youtube, tiktok, instagram, facebook, audio, live). Supadata cũng làm đúng mô hình này: tool free kéo traffic, sau đó đẩy sang API. Mình chỉ cần thêm cụm trang API song song với từng tool.
- Điểm khác biệt nên nhấn mạnh:
  - **Có AI fallback**: video không có phụ đề thì vẫn transcribe được bằng audio. TranscriptAPI và youtube-transcript.io không có cái này.
  - Hỗ trợ đa nền tảng.
  - Hơn 100 ngôn ngữ.
  - Có speaker separation.
  - Xuất được SRT/VTT/DOCX/PDF.
  - **Có MCP cho AI agent**, đây là xu hướng 2026 mà đối thủ nào cũng đang làm.

---

## 2. Đối thủ làm gì (rút gọn)

| Đối thủ | Nền tảng | Free | Giá | Điểm mạnh SEO |
|---|---|---|---|---|
| **Supadata.ai** | YT, TikTok, IG, FB, X, file | 100 request/tháng, không cần thẻ | ~$0.99/1K request | Mỗi nền tảng có 1 trang API riêng và 1 tool free riêng; có blog so sánh "best youtube transcript api"; có trang /mcp, /nocode, /playground |
| **TranscriptAPI.com** | Chỉ YouTube | 100 credit cho agent | $5/tháng cho 1.000 credit | Title nhồi keyword: "YouTube Transcript API with Search, Channels & Playlists"; có MCP, Agent Skills; trang /workflows, /what-to-build |
| **youtube-transcript.io** | Chỉ YouTube | 25/tháng | ~$8–10/1K | Trang /api là docs ngắn (cURL/Node/Python), có template n8n/Make, bulk playlist/CSV |
| **ScrapeCreators** | Nhiều mạng xã hội | 100 credit (1 lần) | ~$0.99/1K | Bán thêm stats, metrics |
| **AssemblyAI / Deepgram** | Upload audio | $50 credit / có free | $0.15–0.21/giờ | Domain mạnh, không nên đánh trực diện |

**Cấu trúc trang API của Supadata** (trang top cho "youtube transcript api", khoảng 1.500–1.800 chữ):
- Title: `YouTube Transcript API — Free Tier, No Quota, Python & JS SDKs | Supadata`
- H1: YouTube Transcript API
- H2 theo thứ tự:
  1. Supadata vs. Alternatives
  2. AI Fallback Transcription
  3. Built for Developers
  4. Use Cases
  5. Pricing
  6. Trusted by
  7. Performance & Capabilities
  8. Code Examples (cURL/Python/JS + JSON response)
  9. FAQ
  10. Other APIs
  11. CTA
- FAQ:
  - What happens when a video has no captions?
  - Languages?
  - Timestamps?
  - Rate limits?
  - Batch?
  - SDKs?
  - Free tier?
  - Public endpoint without API key?
  - Fetch by video ID?

=> Nên copy cấu trúc này rồi làm tốt hơn.

---

## 3. Cây sản phẩm: Speech-to-Text là mẹ (cập nhật theo yêu cầu)

Cách hiểu: mọi thứ đều là **"âm thanh vào → text ra"**, chỉ khác **nguồn đầu vào**.

```
Speech-to-Text API (trang mẹ / pillar)
├── File to Text  (upload file)
│   ├── Audio to Text  → mp3, wav, m4a, aac, flac, ogg, opus, wma
│   └── Video to Text  → mp4, mov, webm, mkv, avi
└── Link to Text  (gửi URL)
    ├── Link trực tiếp → URL .mp3/.mp4/.wav, Google Drive, Dropbox, S3/presigned URL
    └── Link social   → YouTube, TikTok, Instagram, Facebook, X (Twitter)
```

> Danh sách định dạng/nguồn ở trên là gợi ý. **Chỉ ghi lên site những gì API thực sự hỗ trợ.**

**Về mặt kỹ thuật API cũng nên đi theo cây này**: 1 endpoint chung, ví dụ `POST /v1/transcribe` nhận *hoặc* `file` *hoặc* `url`, server tự nhận diện nguồn (file / link trực tiếp / YouTube / TikTok…). Khi đó câu marketing "One API for any file or link" là đúng, và docs cũng gọn.

### Lưu ý SEO quan trọng khi đặt Speech-to-Text làm mẹ
- Từ khoá **"speech to text api"** cực khó (Google, AssemblyAI, Deepgram, OpenAI, ElevenLabs). Trang mẹ vẫn cần có để gom link nội bộ, nhưng **traffic thật sẽ đến từ trang con** trong 3–6 tháng đầu.
- Dev tìm YouTube **không** gõ "speech to text", họ gõ **"youtube transcript api"**. Vì vậy trang con social phải giữ keyword "transcript" trong title/slug, không đổi thành "youtube speech to text api".
- Cây phân cấp nên thể hiện bằng **breadcrumb + internal link**, không cần lồng URL nhiều tầng (giải thích ở mục 4).

---

## 4. Từ khoá theo từng trang

> 📌 Dữ liệu từ khoá crawl thật (Google Autocomplete + sitemap đối thủ) nằm ở `keyword/kw_api.md` và `keyword/kw_api_autocomplete.csv`.

### Tầng 1: Trang mẹ
| Trang | Keyword chính | Keyword phụ | Độ khó |
|---|---|---|---|
| `/api/speech-to-text` | speech to text api | transcription api, audio transcription api, voice to text api, speech recognition api, ai transcription api | Rất khó |

### Tầng 2: Nhánh File và Link
| Trang | Keyword chính | Keyword phụ | Độ khó |
|---|---|---|---|
| `/api/audio-to-text` | audio to text api | audio transcription api, transcribe audio api, voice recording to text api | Khó |
| `/api/video-to-text` | video to text api | video transcription api, transcribe video api, video transcript api | Trung bình |
| `/api/url-to-text` | transcribe audio from url api | audio url to text, video url to text api, transcribe from link api, google drive audio to text api | Dễ (ít người làm trang riêng) |

### Tầng 3a: Theo định dạng file
Chỉ làm trang riêng cho **3 định dạng lớn**. Các định dạng còn lại liệt kê trong bảng "Supported formats" ở trang cha, để tránh trang mỏng và trùng nội dung.

| Trang | Keyword chính | Keyword phụ |
|---|---|---|
| `/api/mp3-to-text` | mp3 to text api | transcribe mp3 api, mp3 transcription api python |
| `/api/mp4-to-text` | mp4 to text api | convert mp4 to text api, mp4 transcription api |
| `/api/wav-to-text` | wav to text api | wav transcription api, transcribe wav file api |

Mỗi trang định dạng phải có nội dung riêng của định dạng đó, không chỉ đổi chữ:
- **MP3**: podcast, ghi âm điện thoại, bitrate thấp vẫn nhận tốt.
- **MP4**: không cần tự tách audio bằng ffmpeg, API tự xử lý; nói thêm về file lớn.
- **WAV**: file nặng nên nên dùng upload theo URL, nói về sample rate, ghi âm call center.

Hiện đối thủ chủ yếu là blog của AssemblyAI và marketplace (Zyla, ApyHub), nên **đây là cụm dễ lên top**.

### Tầng 3b: Theo nguồn link social
| Trang | Keyword chính | Keyword phụ |
|---|---|---|
| `/api/youtube-transcript` | youtube transcript api | youtube captions api, youtube subtitles api, youtube video to text api, youtube transcript api python/free |
| `/api/tiktok-transcript` | tiktok transcript api | tiktok video to text api, tiktok captions api |
| `/api/instagram-transcript` | instagram transcript api | instagram reels transcript api, instagram video to text api |
| `/api/facebook-transcript` | facebook video transcript api | facebook reels transcript api |
| `/api/x-transcript` (làm sau) | twitter video transcript api | x video to text api |

### Từ khoá long-tail để viết blog / docs
- Theo file:
  - transcribe large audio file api
  - mp3 to text python
  - transcribe audio file node js
  - whisper api alternative
  - batch audio transcription api
- Theo link:
  - transcribe audio from url python
  - google drive audio to text
  - dropbox video transcription
  - podcast url to text api
- YouTube:
  - youtube transcript api without api key
  - youtube-transcript-api blocked / IP blocked (cơ hội lớn)
  - youtube playlist / channel transcript api
  - youtube transcript to json / srt
- AI agent:
  - transcript api for ai agents
  - speech to text mcp
  - youtube mcp server
- So sánh:
  - best speech to text api
  - best youtube transcript api
  - assemblyai alternative, supadata alternative
  - whisper api vs …
  - free transcription api

### Cấu trúc URL đề xuất

```
/api                         ← trang giới thiệu API chung (giá, key, docs)
/api/speech-to-text          ← PILLAR
  /api/audio-to-text         ← nhánh File
    /api/mp3-to-text
    /api/wav-to-text
  /api/video-to-text         ← nhánh File
    /api/mp4-to-text
  /api/url-to-text           ← nhánh Link trực tiếp
  /api/youtube-transcript    ← nhánh Link social
  /api/tiktok-transcript
  /api/instagram-transcript
  /api/facebook-transcript
/api/pricing
/api/mcp                     ← MCP cho Claude/ChatGPT/Cursor
/api/integrations            ← n8n, Make, Zapier
/docs                        ← subfolder, KHÔNG để subdomain
/playground
```

**Vì sao URL để phẳng `/api/xxx` mà không lồng `/api/speech-to-text/file/audio/mp3-to-text`?**
- URL ngắn và chứa đúng keyword thì tốt hơn. Google không cần URL lồng mới hiểu được cấp bậc.
- Sau này nếu đổi cây (ví dụ chuyển "video" sang nhánh khác) thì không phải redirect.
- Cấp bậc được thể hiện bằng:
  - **Breadcrumb** (có schema BreadcrumbList). Ví dụ: `Home › API › Speech to Text › Link to Text › YouTube Transcript API`.
  - **Internal link**:
    - Trang mẹ link xuống tất cả trang con.
    - Trang con link lên trang mẹ và link sang các trang anh em cùng nhánh.
    - Mỗi trang con có một block "Other sources": File (MP3, WAV, MP4) và Link (URL, YouTube, TikTok…).

**Internal link với tool free hiện có** (link 2 chiều):

| Tool free | Trang API |
|---|---|
| `/audio-to-text`, `/voice-to-text` | `/api/audio-to-text` |
| `/video-to-text` | `/api/video-to-text` |
| `/youtube-transcript` | `/api/youtube-transcript` |
| `/tiktok-transcript` | `/api/tiktok-transcript` |
| `/instagram-transcript` | `/api/instagram-transcript` |
| `/facebook-transcript` | `/api/facebook-transcript` |

### Thứ tự làm trang (ưu tiên dễ thắng trước)
1. `/api` và `/api/speech-to-text`: nền, chưa mong lên top ngay.
2. `/api/youtube-transcript`: nhu cầu lớn nhất, đối thủ nhỏ.
3. `/api/video-to-text` và `/api/url-to-text`.
4. `/api/mp3-to-text`, `/api/mp4-to-text`, `/api/wav-to-text`: dễ lên top.
5. `/api/audio-to-text`.
6. TikTok, Instagram, Facebook.
7. Blog long-tail và các trang so sánh.

---

## 5. Template 1 trang API (ví dụ YouTube)

- **Title** (≤60 ký tự): `YouTube Transcript API – Free Tier, AI Fallback | TranscriptX`
- **Meta**: `Get YouTube transcripts via API in 100+ languages. Timestamps, SRT/VTT, AI transcription for videos without captions. 100 free requests.`
- **H1**: YouTube Transcript API
- Ngay dưới H1: 1 câu mô tả, 2 nút (Get API key / Try playground), kèm **code cURL 3 dòng**. Dev cần thấy code ngay ở màn hình đầu.
- **H2 Features**:
  - Native captions + AI fallback
  - 100+ ngôn ngữ
  - Timestamps
  - Speaker separation
  - Định dạng xuất JSON/TXT/SRT/VTT
  - Batch / playlist / channel
- **H2 Code examples**: tab cURL / Python / JavaScript, kèm JSON response mẫu.
- **H2 Use cases**:
  - AI/RAG
  - Tóm tắt video
  - Phụ đề
  - SEO content
  - Nghiên cứu
  - Social listening
- **H2 TranscriptX vs alternatives**: bảng so với Supadata / TranscriptAPI / youtube-transcript.io / youtube-transcript-api (thư viện Python), so sánh các tiêu chí giá, free, AI fallback, đa nền tảng, MCP. Phải ghi trung thực, không bịa số.
- **H2 Pricing**: tóm tắt giá + link sang /api/pricing.
- **H2 Integrations**: MCP, n8n, Make, Zapier, SDK.
- **H2 FAQ** (8–10 câu, có schema FAQPage). Lấy theo bộ câu hỏi của Supadata và thêm:
  - Is it legal?
  - Does it work for private videos?
  - Why does youtube-transcript-api get blocked?
- **CTA cuối trang**.
- Độ dài: 1.500–2.000 chữ.
- Schema: `SoftwareApplication` / `WebAPI` + `FAQPage` + `BreadcrumbList`.

Các trang TikTok/IG/FB/audio dùng chung template này, nhưng **viết lại nội dung riêng** để tránh trùng lặp, nhất là phần use case và FAQ đặc thù của từng nền tảng. Ví dụ: Reels thường không có caption nên luôn dùng AI.

---

## 6. Định giá (tham khảo để không lệch thị trường)
- Free tier: **100 request/tháng, không cần thẻ**. Đây là chuẩn chung, đối thủ nào cũng có.
- Giá rẻ nhất trong nhóm: khoảng **$1/1.000 request** cho transcript có sẵn caption.
- Request phải dùng AI (không có caption) thì tính credit theo phút audio.
- Có gói tháng từ **$5–9**. TranscriptAPI bán $5/1K credit, Transcribe.so bán $9/tháng.
- Rate limit cần công bố rõ (ví dụ 60–200 RPM) và trả mã 429 kèm header `Retry-After`.

---

## 7. Lộ trình triển khai

**Tuần 1–2: Làm nền**
- Làm `/api`, `/api/speech-to-text` (trang mẹ), `/api/youtube-transcript`, `/docs` và `/api/pricing`.
- Thêm box CTA sang API trên tất cả các trang tool hiện có.
- Submit sitemap, kiểm tra index trong GSC.

**Tuần 3–4: Mở rộng**
- Làm `/api/video-to-text`, `/api/url-to-text`, `/api/mp3-to-text`, `/api/mp4-to-text`, `/api/wav-to-text` và `/api/audio-to-text`.
- Sau đó làm TikTok / Instagram / Facebook.
- Làm trang `/api/mcp` và `/api/integrations` (n8n template, Make blueprint).
- Viết 2 blog: `best youtube transcript api` và `youtube transcript api python`.

**Tháng 2**
- Viết blog long-tail:
  - youtube-transcript-api bị blocked
  - không cần API key
  - lấy transcript cả playlist/channel
  - transcript cho RAG/LLM
- Viết các trang "alternative" (supadata alternative…).

**Tháng 2–3: Off-page (dev SEO sống nhờ kênh này)**
- Đăng lên **RapidAPI**. Supadata có mặt ở đây và kéo được backlink + traffic.
- Đăng lên publicapis.io, Product Hunt, các danh sách MCP (mcp.so, glama, smithery), danh sách n8n/Make templates, awesome-lists trên GitHub.
- Làm SDK Python/JS open-source trên GitHub/PyPI/npm. README trỏ link về site.
- Trả lời trên StackOverflow, Reddit (r/learnpython, r/n8n, r/LocalLLaMA) ở các câu hỏi về lỗi youtube-transcript-api.
- Viết bài trên dev.to / Hashnode / Medium với code mẫu.

**Đo lường**
- Theo dõi trong GSC: impressions/position cho cụm "transcript api".
- Theo dõi số lượt đăng ký API key, tỉ lệ chuyển từ tool free sang API.

---

## 8. Checklist nhanh mỗi trang API
- [ ] Keyword chính có trong Title, H1, URL, câu đầu tiên
- [ ] Có code mẫu ngay màn hình đầu
- [ ] Có JSON response mẫu
- [ ] Có bảng so sánh với đối thủ
- [ ] FAQ có schema
- [ ] Link 2 chiều với tool free tương ứng
- [ ] Link sang docs, pricing, playground
- [ ] Đa ngôn ngữ: trang API **nên để tiếng Anh trước**, vì dev search bằng tiếng Anh. Chỉ dịch khi đã có traffic.

---

## Nguồn
- https://supadata.ai
- https://supadata.ai/youtube-transcript-api
- https://supadata.ai/blog/best-youtube-transcript-api
- https://transcriptapi.com
- https://transcriptapi.com/blog/youtube-transcript-api-complete-developer-guide
- https://www.youtube-transcript.io/api
- https://www.assemblyai.com/pricing
- https://assemblyai.com/blog/how-to-convert-an-mp3-file-to-text-with-an-api
- https://zylalabs.com/api-marketplace/tools/mp3+to+text+api/4917
- https://apyhub.com/apyhub/service/transcribe-speech-to-text.md
- https://developers.deepgram.com/docs/python-sdk-pre-recorded-transcription
- https://github.com/jdepoix/youtube-transcript-api
- https://apify.com/amrameng/video-transcript-api
- https://publicapis.io/transcriptfetch-api
- https://www.capterra.co.uk/software/1233875/Transcribe-so
- https://dev.to/eli_9c82b7dfe52c1bc371ffe/ai-transcription-pricing-2026-whisper-vs-deepgram-vs-assemblyai-2eec
