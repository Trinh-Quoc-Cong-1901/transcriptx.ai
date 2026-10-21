# Từ khoá API – kết quả crawl (08/10/2026)

**Cách crawl:**
- **Google Autocomplete** (US, tiếng Anh): mỗi seed được ghép thêm a–z và các tiền tố "best/free/how to/open source/cheapest". Tổng cộng 32 seed, ~1.300 gợi ý sau khi lọc nhiễu.
  - File đầy đủ: `kw_api_autocomplete.csv`.
  - Cột `goi_y_truc_tiep_tu_seed = x` nghĩa là Google gợi ý ngay khi gõ seed. Đây là nhóm có nhu cầu cao nhất.
- **Sitemap đối thủ**: Supadata, TranscriptAPI, ScrapeCreators, SocialKit, AssemblyAI, Deepgram.

> Autocomplete **không cho số volume**. Nó chỉ cho biết từ khoá có người search thật và mức phổ biến tương đối. Muốn có volume và KD thì đưa file CSV vào Ahrefs/Semrush/Keyword Planner.

---

## A. Kết quả theo cây sản phẩm

### 1. Speech-to-Text API (trang mẹ)
**Gợi ý trực tiếp từ Google:**
- speech to text api
- speech to text api free
- speech to text api key
- speech to text api pricing
- speech to text api open source
- speech to text api python
- speech to text api javascript
- speech to text api real time
- speech to text api comparison
- speech to text api benchmark
- best speech to text api
- cheapest speech to text api
- free speech to text api key

**Các nhóm liên quan:**
- **transcription api**: free, pricing, service, comparison, batch transcription api, cheapest transcription api, best transcription api, transcript api key, **transcript api mcp**.
- **voice to text api**: free, pricing, python, open source, cost, voice to text converter api.
- **audio transcription api**: free, best, cheapest, real time, voice transcription api.
- **whisper api**: pricing, free, **whisper api alternative / free alternative**, cost per minute, max file size, word timestamps, error 429, n8n.

**Nhận xét:**
- Nhóm này **bị brand chiếm**: google, openai, elevenlabs, azure, gemini, deepgram, groq đều xuất hiện trong gợi ý, nên rất khó lên top.
- Ngách nên đánh: **"whisper api alternative"**, **"cheapest / free speech to text api"**, **"speech to text api + ngôn ngữ"**. Google gợi ý cả hindi, urdu, "for indian languages", zalo (tiếng Việt).
- Khi gõ "transcription api", Google gợi ý luôn "youtube transcript api". Nghĩa là cụm "transcript api" chủ yếu là người tìm YouTube.

### 2a. File → Audio
**Gợi ý:**
- audio to text api: free, pricing, best
- audio to text converter api
- transcribe audio to text api
- sound to text api
- api to convert audio to text
- free api to convert audio to text
- **mp3 to text api**, mp3 to text api free
- **wav to text api**
- m4a to text api: **không có gợi ý**, nên không làm trang riêng.
- audio file transcription api: **không có gợi ý**.

### 2b. File → Video
**Gợi ý:**
- video to text api: free
- video to text converter api
- transcribe video to text api
- video transcription api: free
- ai video transcription api
- **mp4 to text api**
- video transcript generator api
- batch: chưa thấy gợi ý riêng cho video

**Nhận xét định dạng:**
- **Chỉ mp3, mp4, wav có nhu cầu dạng "… to text api"**. Kết luận cũ (chỉ làm 3 trang định dạng) là đúng.
- Lưu ý từ "video to text api" bị lẫn rất nhiều với "**text to video** api" (Sora, Runway, Kling…). Title và H1 phải viết rõ "Video to Text (Transcription) API".

### 3a. Link trực tiếp
**Gợi ý (phần lớn là ý định dùng tool, không phải API):**
- transcribe audio from url / from link
- transcribe audio url to text (free)
- audio url to text converter
- audio link to text converter (free/online/ai)
- video url to text converter (free/ai/online)
- **video link to text no sign up**
- video link to text generator / extractor / summary / script
- transcribe video to text with url
- **Google Drive**:
  - transcript from drive link
  - transcribe from google drive link
  - transcribe audio to text from google drive
  - transcribe video from google drive link
- **Nguồn khác Google gợi ý khi gõ "transcribe from …"**:
  - spotify link
  - podcast link
  - soundcloud link
  - vimeo link
  - zoom link
  - linkedin video
  - reel link
  - mp3 link
  - x link

**Nhận xét quan trọng:**
- Cụm "link/url to text" có **rất nhiều biến thể** nhưng gần như toàn là người dùng tool.
- Vì vậy nên làm **2 trang**:
  1. **Tool free** `/video-link-to-text` (hoặc `/link-to-text`). Keyword: video link to text, audio link to text converter, transcribe from link, no sign up.
  2. **Trang API** `/api/url-to-text`. Keyword: transcribe audio from url api, audio url to text api, transcribe video url api.
- Có thể mở rộng nguồn link nếu sản phẩm hỗ trợ: Google Drive, Dropbox, Vimeo, Spotify/podcast, SoundCloud, Zoom, LinkedIn.

### 3b. Link social
**YouTube** (nhu cầu lớn nhất, long-tail dày nhất)

| Nhóm | Gợi ý |
|---|---|
| Chính | youtube transcript api, **free**, **python**, **rate limit**, github, key, documentation, get transcript, npm |
| Lỗi / thay thế (cơ hội lớn) | **youtube transcript api blocked**, **ip blocked**, **ip ban**, **not working**, **too many requests**, error, webshare, **alternative**, official |
| Ngôn ngữ code | javascript, typescript, js, nodejs, java, c#, flutter, react, pip, pypi, in python |
| AI / tự động hoá | **mcp**, **claude**, **for claude**, langchain, **n8n**, dify, skill, vercel, docker |
| Marketplace | rapidapi, apify (đối thủ đang ăn traffic qua đây) |
| Khác | how to get / how to use youtube transcript api, is there a youtube transcript api, is free, cost, limits, endpoint, youtube transcript scraper api, extractor api, search api, best youtube transcript api, cheapest youtube transcript api |
| Captions / subtitles | youtube captions api (python), youtube api captions download, captions list, youtube data api captions.download, youtube live captions api, youtube subtitles api, download youtube subtitles api, youtube subtitle extractor api |
| Video to text | youtube video to text api, youtube timed text api, transcribe youtube video to text api, youtube video transcript api free, fetch/get youtube video transcript api |

**TikTok**:
- tiktok transcript api, tiktok transcript api free
- tiktok video transcript api
- get tiktok transcript api
- tiktok transcript generator api
- tiktok transcript apify, apify tiktok transcript scraper, supadata tiktok transcript api

**Instagram**:
- instagram transcript api
- **instagram reel transcript api**
- instagram video transcript api
- instagram reel transcript apify, supadata instagram transcript api

**Facebook**: gần như không có nhu cầu dạng API (chỉ có "apify's facebook video transcript extractor"). **Để ưu tiên thấp.**

**X/Twitter**: nhu cầu thiên về tool: twitter video transcript generator (free), extractor, download, no sign up, x twitter video transcript. Nên **làm tool free trước**, API sau.

---

## B. Đối thủ đang làm những trang gì (từ sitemap)

| Đối thủ | Số URL | Kiểu trang đáng học |
|---|---|---|
| **Supadata** | 29 | Mỗi nền tảng 1 trang API (`/youtube-transcript-api`, `/tiktok-…`, `/instagram-…`, `/twitter-…`, `/video-transcript-api`) và 1 tool free (`/youtube-transcript`…). Có thêm `/mcp`, `/nocode`, `/playground` và 4 bài blog how-to. **Ít trang nhưng vẫn top**, nhờ backlink và brand. |
| **ScrapeCreators** | 2.750 | **Programmatic**: `/tutorials/how-to-scrape-{platform}-transcript-with-{python,nodejs,go,php,java,ruby,rust,…}` (13 ngôn ngữ × nhiều nền tảng); mỗi endpoint 1 trang; trang API cho cả nền tảng ngách: **rumble, kick, linkedin, reddit, facebook ad library**. |
| **SocialKit** | 219 | `/{platform}-apis/transcript`, `/video-apis/transcript`; tool free: `*-transcript-extractor`, `*-video-summarizer`, **youtube-bulk-transcript-downloader, channel-transcripts, playlist-transcripts**, `video-file-transcript-extractor`, `transcript-cleaner`, `subtitle-format-converter`; trang `/alternatives/…` và `/use-cases/…`. |
| **TranscriptAPI** | 68 | **60 trang `/workflows/…`** theo use case, ví dụ: playlist-to-rag-chunks, video-to-seo-blog-post, video-to-x-thread, video-to-podcast-show-notes, earnings-call-tracker, brand-mention-monitor-slack… |
| **AssemblyAI** | 1.644 | `/explore/audio-to-text-api`, `/explore/python-speech-to-text-api`, `/explore/javascript-speech-to-text-api`, `/explore/real-time-transcription`; trang `/compare/x-vs-assemblyai`; mỗi câu FAQ trong docs là 1 trang, ví dụ `how-can-i-transcribe-youtube-videos`, `does-it-cost-extra-to-export-srt-or-vtt-captions`. |
| **Deepgram** | 1.362 | **Mỗi ngôn ngữ 1 trang**: `/product/speech-to-text/{vietnamese, hindi, japanese, …}`, khoảng 50 trang. |

---

## C. Kết luận: nên làm gì (theo thứ tự)

1. **`/api/youtube-transcript`** + các trang con theo **ngôn ngữ code**: `/python`, `/javascript` (nodejs), sau đó java, c#.
   - Lý do: "youtube transcript api python / npm / javascript" đều có trong gợi ý trực tiếp.
2. **Bài "YouTube Transcript API blocked / IP blocked / too many requests – fix"** và **"youtube transcript api alternative"**.
   - Đây là nhóm dev đang bị lỗi và cần giải pháp, nên chuyển đổi cao nhất.
3. **`/api/mcp`**: các gợi ý "youtube transcript api mcp / claude / for claude", "transcript api mcp" đều có.
   - Thêm template **n8n** (`youtube transcript api n8n`, `whisper api n8n`).
4. **`/api/video-to-text`**, **`/api/audio-to-text`**, **`/api/mp3-to-text`**, **`/api/mp4-to-text`**, **`/api/wav-to-text`**.
5. **Link**:
   - Tool free `/video-link-to-text` (traffic lớn).
   - Trang API `/api/url-to-text`.
   - Trang con Google Drive (nếu hỗ trợ).
6. **`/api/tiktok-transcript`** và **`/api/instagram-transcript`** (nhấn mạnh **reel**).
   - Facebook và X để sau.
7. **Programmatic** (sau khi các trang chính đã index):
   - **Ngôn ngữ**: `/api/speech-to-text/{language}` theo kiểu Deepgram. Ưu tiên ngôn ngữ dự án đã có sẵn: vi, hi, id, ja, ko, fr, de, es, pt…
   - **Workflow / use case** theo kiểu TranscriptAPI: youtube-to-rag, video-to-blog-post, podcast-show-notes…
   - **Trang compare/alternative**: whisper api alternative, supadata alternative, youtube-transcript-api (python) alternative, assemblyai alternative.
   - **Tool bổ trợ** theo kiểu SocialKit: bulk / playlist / channel transcript, subtitle format converter. Có thể tận dụng chính tool hiện có của TranscriptX.
8. **Đăng lên RapidAPI và Apify Store**: Google gợi ý "youtube transcript api rapidapi", "tiktok transcript apify", tức là người dùng tìm thẳng trên các marketplace đó.

---

## Nguồn sitemap đã crawl
- https://supadata.ai/sitemap.xml
- https://transcriptapi.com/sitemap.xml
- https://scrapecreators.com/sitemap.xml
- https://www.socialkit.dev/sitemap.xml
- https://www.assemblyai.com/sitemap.xml
- https://deepgram.com/sitemap.xml
- Google Autocomplete: `suggestqueries.google.com` (hl=en, gl=us)
