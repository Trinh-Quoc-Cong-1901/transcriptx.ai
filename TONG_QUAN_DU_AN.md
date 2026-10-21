# Tổng quan dự án SEO — TranscriptX.ai

> File này mô tả ngắn gọn dự án đang làm gì. Dùng làm "Project instructions" trên claude.ai
> hoặc làm CLAUDE.md trong Claude Code. Cập nhật lần cuối: 2026-10-12.

## 1. TranscriptX.ai là gì
Website công cụ AI **chuyển video/audio thành văn bản (transcript)**:
- Lấy transcript từ link: **YouTube, TikTok, Instagram, Facebook**
- Upload file **audio/video → text**, voice to text
- **Live / real-time transcription** (nói thành chữ trực tiếp)
- Tóm tắt video YouTube bằng AI
- **API** cho lập trình viên và **MCP server / connector** cho Claude, ChatGPT
- Điểm mạnh: có AI fallback (video không có phụ đề vẫn ra transcript), 100+ ngôn ngữ,
  tách người nói, xuất SRT/VTT/DOCX/PDF.

## 2. Mục tiêu dự án
Làm **SEO quốc tế** để kéo traffic tự nhiên về các trang công cụ, rồi chuyển một phần sang API/MCP.

## 3. Đang làm những việc gì
| Mảng | Nội dung | Thư mục |
|---|---|---|
| Nghiên cứu từ khoá | Keyword theo từng nền tảng: YouTube, TikTok, Instagram, Facebook, audio, video, live, API | `keyword/` |
| Trang công cụ (landing page) | Mỗi keyword chính một trang (vd `/youtube-transcript`, `/tiktok-video-to-text`, `/audio-to-text`…). Nội dung viết bằng JSON, **đa ngôn ngữ** | `page/` (danh sách URL ở `page.md`) |
| Đa ngôn ngữ | Tiếng Anh + 13 ngôn ngữ có nghiên cứu keyword local (fr, de, es, id, ms, pt, tr, it, ja, ko, hi, ar, vi) + 5 ngôn ngữ chỉ dịch (bn, ur, ru, th, my) | `promt/dich_nn.md` |
| Trang MCP / AI | Trang nhắm keyword kiểu "can ChatGPT/Claude transcribe audio", "transcription MCP" | `mcp_transciption/` |
| API | Nghiên cứu SEO cho cụm trang API transcript | `api_transcript/` |
| Trang phụ | About, Contact, FAQ, Privacy, Terms, Copyright, How to install | `trang_phu/` |
| Đối thủ | 9 đối thủ chính: proactor.ai, transcribeyt.com, transcriptx.xyz (trùng tên), transcript365.com, scribesnap.ai, transcribex.io, vocascript.com, wayin.ai, transcriptly.org | `competitors/` |
| Backlink | Phân tích backlink đối thủ và **kế hoạch backlink** (directory AI, MCP directory, Product Hunt, outreach) | `bacnklink/KE_HOACH_BACKLINK_TranscriptX.md` |
| Chiến lược tổng | File Excel chiến lược SEO (pillar/cluster, roadmap, KPI) | `TranscriptX_SEO_Strategy.xlsx` |
| Promo | Video quảng cáo ngắn | `promo/` |

## 4. Quy trình làm một trang (tóm tắt)
1. Chọn keyword chính → lọc keyword phụ (`intent/1_kw.md`, `2_loc_kw.md`)
2. Phân tích search intent → viết nội dung tiếng Anh (`en.json`)
3. Tìm keyword local từng ngôn ngữ → viết bản cho từng ngôn ngữ (`vi.json`, `ja.json`…)

## 5. Quy ước khi trả lời
- Trao đổi bằng **tiếng Việt**; nội dung website viết bằng **tiếng Anh** và các ngôn ngữ đích.
- Ưu tiên câu trả lời ngắn, thực tế, bám đúng dự án TranscriptX.ai.
- Không đề xuất SEO mũ đen (PBN, link farm, spam comment).
