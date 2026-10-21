🔥 TranscriptX – YouTube Transcript API

URL:
/api/youtube-transcript

Intent chính:

YouTube Transcript API – Get Any YouTube Transcript With One API Call

Developer cần lấy transcript YouTube **bằng code** (app, AI agent, RAG, automation). Intent: thương mại/giao dịch — so sánh giải pháp rồi lấy API key.

Hai nhóm người tìm:
1. **Đang dùng YouTube Data API chính thức** (youtube api get captions / captions download / api transcript) → bị chặn vì `captions.download` cần OAuth và chỉ tải được caption của video mình sở hữu/quản lý.
2. **Tìm dịch vụ transcript API** (youtube transcript api, youtube video transcript api) → so sánh, muốn free tier, code mẫu.

---

## Bố cục trang
1. `apiGuide` (pending – dev bổ sung): lấy key, cURL, Python, JS, JSON response.
2. Content SEO:
   - H2 What Is a YouTube Transcript API?
   - H2 At a Glance (specs – chỉ thông tin đã xác nhận)
   - H2 Why the Official YouTube API Can't Get Transcripts *(góc mạnh nhất – cover nhóm "youtube api …")*
   - H2 YouTube Captions and Subtitles API *(captions, subtitles)*
   - H2 Works With or Without Captions *(transcribe từ audio)*
   - H2 What Developers Build With It (use cases)
   - H2 How It Compares (vs YouTube Data API, vs thư viện youtube-transcript-api)
   - H2 Beyond YouTube (link TikTok API, /api)
   - H2 FAQ

## Thông tin đã xác nhận được dùng
100+ ngôn ngữ, speaker labels, timestamps, TXT/DOCX/PDF/SRT/VTT, transcribe từ audio, 1 giờ audio 1–2 phút, ~95%, file 10 giờ ~10 phút, không xử lý video private/unlisted/cần đăng nhập, có MCP, hỗ trợ TikTok/IG/FB/Vimeo/X/LinkedIn/Twitch/Dailymotion/Reddit.

## ⚠️ Chưa ghi (chờ dev)
Endpoint, base URL, free tier API, giá, rate limit, SDK, format JSON.

## Internal linking
- → /api, /api/tiktok-transcript, /api/pricing
- ↔ /youtube-transcript (tool free)
- ↔ /blog/youtube-transcript-api-python
