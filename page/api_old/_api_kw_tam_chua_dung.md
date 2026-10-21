# Cụm API – Quy ước và từ khoá chưa dùng

Nguồn volume: `api_transcript/api_kw.md` (Keyword Planner, 10/2026).

## Quy ước
- URL dạng `/api/...` → **cần dev xác nhận `/api/` không trùng route backend và không bị chặn trong robots.txt**.
- Mỗi `en.json` có khối `apiGuide` ở trên cùng (status: pending) → phần hướng dẫn lấy key + code, dev bổ sung sau. Content SEO nằm trong `sections`.
- Content SEO **không ghi** endpoint, giá API, rate limit, free tier của API cho tới khi dev xác nhận.
- Cột "Cạnh tranh" trong Keyword Planner = cạnh tranh giá thầu Ads, **không phải độ khó SEO**.
- Volume 10–100 → H2 trong trang gần nhất, chưa tách URL.

## Từ khoá gộp làm H2, chưa tách trang
- instagram transcript api (10–100) → H2 trong /api
- facebook transcript api (10–100) → H2 trong /api
- audio transcription api, video transcription api (10–100) → H2 trong /api
- speech to text api key (10–100) → khối apiGuide /api + /api/pricing

## Chưa tra volume / bỏ
- mp3/mp4/wav to text api, url to text api, whisper api alternative, transcript api mcp, twitter/x transcript api → tra lại sau 3 tháng.
