# Cụm API – Quy ước và keyword chưa dùng

## Cấu trúc
- Hub: /transcription-api
- Trang con (URL phẳng, có chữ "api" trong slug): /speech-to-text-api, /youtube-transcript-api, /tiktok-transcript-api, /facebook-transcript-api, /instagram-transcript-api
- Quan hệ cha–con thể hiện bằng `breadcrumb` (đã có trong en.json) + internal link.
- Bỏ trang pricing riêng.

## Quy ước viết
- Ngắn gọn, mỗi trang 4–6 H2, không nhồi biến thể keyword.
- Không ghi endpoint, giá, free tier, rate limit cho tới khi dev xác nhận (`apiGuide`, `pricingBlock` = pending).
- Chỉ dùng số liệu đã xác nhận: 100+ ngôn ngữ, ~95%, 1h audio = 1–2 phút, file 10h ≈ 10 phút, không giới hạn dung lượng, xoá file sau vài ngày, không train AI, có MCP.
- Không nhắc X / Twitter trong cụm này (2 nền tảng tách riêng, làm trang sau nếu có volume).

## Keyword chưa dùng / để sau
- speech to text api pricing, cheapest speech to text api (10–100) → `pricingBlock` trong hub khi có giá
- speech to text api key (10–100) → `apiGuide` của hub
- youtube transcript api python / github / javascript, youtube_transcript_api → blog (đã có /blog/youtube-transcript-api-python)
- youtube api get transcript / get captions / get subtitles / captions download → biến thể, không đưa vào bài
- mp3/mp4/wav to text api, whisper api alternative, transcript api mcp → tra volume sau
