# notes · how-to-summarize-a-youtube-video

## 1. Bài nói về gì

Excerpt (English, dán vào blog), 170 ký tự:
```
How to summarize a YouTube video in TranscriptX: get the timestamped transcript, write key points in Notes, and a first look at the Summary and Mind map tabs coming soon.
```

Bài hướng dẫn tóm tắt video YouTube **ngay trong TranscriptX**: lấy transcript có timestamp → tự ghi ý chính ở tab **Notes** (dùng được ngay) → tab **Summary** (sắp ra mắt: ý chính kèm giây, bấm vào thì transcript nhảy tới đoạn đó) → tab **Mind map** (sắp ra mắt: sơ đồ cây). Summary và Mind map là tính năng của chính website TranscriptX, **không liên quan ChatGPT/Claude** (user nhắc 2026-10-29), nên bài không nhắc ChatGPT/Claude. Dành cho sinh viên, người xem bài giảng, cuộc họp, podcast dài.

Khi Summary/Mind map ra mắt: bỏ chữ "(coming soon)" ở Step 3–4, FAQ "Does TranscriptX summarize… automatically?" và bảng cuối; thay ảnh preview bằng ảnh thật. Giữ nguyên URL.

## 2. Dàn ý
- **Quick answer**: transcript → Notes; Summary (ý chính + timestamp bấm được) và Mind map sắp có.
- **Intro**. Sau khi đăng video lên YouTube: chèn block `youtube` ngay sau intro (bài chỉ dùng ảnh tĩnh, user yêu cầu 2026-10-29).
- **Why a good summary starts with the transcript**: tóm tắt dựa trên lời nói; timestamp để kiểm chứng.
- **Step 1: Get the transcript**: 3 bước trên `/youtube-transcript/`.
- **Step 2: Write your own summary in Notes**: tab Notes, định dạng, checklist, link, timestamp.
- **Step 3: Summary (coming soon)**: trích câu trên giao diện, 3 ý (ý chính / timestamp / bấm để nhảy), Pro beta trước.
- **Step 4: Mind map (coming soon)**: sơ đồ cây, trích câu trên giao diện.
- **Copy or download the transcript**: Copy và Download là 2 nút riêng; 5 định dạng; tắt timestamp được.
- **When a YouTube video summary helps most**: bài giảng, cuộc họp, podcast/phỏng vấn, tutorial.
- **Notes, Summary or Mind map: which one do you need?**: bảng có cột "Available".
- **FAQ**: 6 câu (miễn phí, tự động chưa, timestamp làm gì, mind map, bài giảng/cuộc họp dài, transcript vs notes vs summary).
- **Summarize your next YouTube video**: CTA về `/youtube-transcript/`.

≈ 1,630 từ. Link nội bộ: `/youtube-transcript/`, `/blog/how-to-get-youtube-transcript/`, `/`.

## 3. Hình ảnh (theo thứ tự trong bài)
Script: `_source/_tools/build_visuals_summary_mind_map.py`. Tất cả là ảnh tĩnh.

| # | File | Vị trí | Nội dung · khoanh | Nguồn | Alt |
|---|---|---|---|---|---|
| 2 | `summarize-youtube-video-paste-link.webp` | Step 1 | Trang YouTube Transcript · khoanh ô dán link | `youtube-transcript/youtube-transcript-tool.png` | YouTube Transcript page on TranscriptX with the box to paste a YouTube video link |
| 3 | `transcriptx-notes-next-to-transcript.webp` | Step 2 | Tab Notes có 2 dòng ghi chú + 1 checklist · khoanh panel Notes | `transcript/transcript-notes-tab.png` + vẽ chữ ghi chú | Notes tab in TranscriptX with key points typed next to the YouTube transcript |
| 4 | `transcriptx-summary-timestamps-preview.webp` | Step 3 | **Mô phỏng** tab Summary: 4 ý chính có chip giây, 00:40 đang chọn, đoạn 00:40.11 tô sáng, trình phát 0:40 · khoanh chip 00:40 | ảnh thật + vẽ đè | Preview of the TranscriptX Summary tab: key points with timestamps, and the transcript jumping to 00:40 |
| 5 | `transcriptx-mind-map-preview.webp` | Step 4 | **Mô phỏng** tab Mind map: gốc "Live a life you will remember" + 4 nhánh | ảnh thật + vẽ đè | Preview of the TranscriptX Mind map tab: a tree with the main idea of a video and four branches |
| 6 | `youtube-transcript-copy-button.webp` | Copy or download | Trang transcript · khoanh nút **Copy** | `transcript/transcript-notes-tab.png` | TranscriptX transcript page with the Copy button highlighted |
| 7 | `youtube-transcript-download-formats.webp` | Copy or download | Menu Download 5 định dạng | `transcript/download-format-menu.png` | TranscriptX Download menu with .txt, .docx, .pdf, .srt and .vtt formats |

Ảnh 4, 5 và video là **mô phỏng** tính năng sắp ra mắt; bài luôn ghi "preview" / "coming soon" ngay cạnh.

## 4. Video (mô phỏng, user duyệt 2026-10-29)
- `images/video/transcriptx-summary-mind-map-preview.mp4`: 2560×1440, 60 fps, 30,9 s. Script: `_source/_tools/build_video_summary_mind_map.py`.
- Poster: `images/video/transcriptx-summary-mind-map-preview-poster.webp`. Thumbnail: `images/video/transcriptx-summary-mind-map-preview-thumbnail.jpg` (`build_thumbnail_summary_mind_map.py`).
- YouTube: `images/video/youtube-video.md`.
- Nền là ảnh chụp thật; cột transcript và panel phải được vẽ lại. Nội dung Summary/Mind map do mình viết từ transcript "Father's Advice". Mốc `01:59.42` của đoạn cuối là số giả định.
- Cảnh: hook "COMING SOON" → 1 Notes (gõ ghi chú) → 2 Summary (ý chính + chip giây) → 3 bấm 00:40 rồi 01:36, transcript nhảy tới và tô sáng → 4 Mind map mọc nhánh → CTA. Nhãn "Coming soon · preview" hiện suốt Summary/Mind map.
- Giọng đọc: **edge-tts `en-US-AvaNeural`, `--rate=+4%`** (cùng giọng `speak-live-promo.mp4`). Khi dựng lại cần edge-tts; đặt `EDGE_TTS=<đường dẫn>` nếu không có trên PATH. Chỉ ghép lại tiếng: `python3 build_video_summary_mind_map.py voice`.
- Nhạc nền: tự tổng hợp (`gen_soft_music.py`: piano rải nốt 76 BPM + pad), tự nhỏ lại khi có giọng; giọng ≈ −16 dB, nhạc giữa các câu ≈ −25 dB.
- Lời thoại:
  1. "Coming soon to TranscriptX: Notes, Summary and Mind map, right next to your transcript."
  2. "First, type your own notes beside the transcript."
  3. "Open Summary to get the key points, each with its timestamp."
  4. "Click a timestamp, and the transcript jumps straight to that moment."
  5. "Mind map shows the whole video at a glance."
  6. "Summary and Mind map are coming soon. Pro users get the beta first."

## 5. Cần kiểm chứng
- **Trang `/youtube-video-summarizer/`** đang viết như thể tóm tắt đã chạy (nút **Summarize Video**, "summary in seconds"), mâu thuẫn với Summary "Coming soon" trong app. Bài **chưa link** sang trang đó.
- **Tab Notes**: "timestamps in your notes" dựa trên icon 🕒 trong ảnh và mô tả trong `_index.md`.
- **Summary/Mind map**: mô tả theo lời user (2026-10-29) và câu trên giao diện. Định dạng thật (có Overview không, mind map có timestamp không) chưa biết, bài không hứa.
