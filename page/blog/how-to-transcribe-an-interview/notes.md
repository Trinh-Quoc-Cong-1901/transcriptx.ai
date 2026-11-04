# Notes: how-to-transcribe-an-interview

## Bài nói về gì

Excerpt (169 ký tự):
```
A step-by-step guide to transcribing interviews and focus groups for qualitative research, from a clear recording and an AI draft to checking, anonymising and exporting.
```

Bài hướng dẫn chép lời phỏng vấn cho nghiên cứu định tính: chuẩn bị (đồng ý ghi âm, ghi âm rõ, chọn kiểu verbatim, mã người tham gia) → 5 bước với TranscriptX → định dạng, ẩn danh, focus group → so sánh tự gõ / AI / dịch vụ người thật. Dành cho sinh viên làm luận văn, nhà nghiên cứu, UX researcher. Dẫn về trang tính năng `/interview-transcription/`.

## Dàn ý
- **H1 + Quick answer:** ghi rõ → tải lên → nháp có timestamp → soát, gán người nói, ẩn danh → xuất Word.
- **Intro:** tự gõ 4–6 giờ cho 1 giờ audio (số từ bài đã đăng how-long-…).
- **What Does Transcribing an Interview Involve?** transcript là dữ liệu; 4 phần: header, hội thoại, nhãn người nói, timestamp.
- **Before You Start:** 4 việc: consent, ghi âm rõ, chọn kiểu chép, mã người tham gia.
- **How to Transcribe an Interview Step by Step:** 5 H3: Upload/Record → nháp → gán người nói (Pro) → soát + Notes → Download .docx / Copy.
- **Verbatim or Clean:** bảng 3 kiểu.
- **How to Transcribe Qualitative Interviews for Analysis:** quy ước định dạng.
- **How to Anonymise an Interview Transcript:** 4 bước.
- **How to Transcribe a Focus Group:** 4 mẹo.
- **Manual, AI or a Transcription Service?** bảng 3 cột + link bài how-long.
- **FAQ:** 6 câu hỏi thật (bao lâu, free, tự làm hay AI, độ chính xác, có cần chép hết, có an toàn).
- **CTA:** về `/interview-transcription/`.

## Hình ảnh (đã dựng 2026-11-03)
Ảnh chụp thật trong `_source`, crop đúng pixel gốc (không phóng to/thu nhỏ), viền cam #CC582E, WebP lossless. Script: `_source/_tools/build_visuals_interview.py`.
1. `upload-interview-recording-transcriptx.webp` · Step 1, sau đoạn Upload · menu Upload, khoanh 4 nguồn · nguồn `_source/upload/upload-source-options.png` · alt: "TranscriptX Upload menu with From this device, Google Drive, Dropbox and OneDrive options"
2. `record-interview-in-browser.webp` · Step 1, sau đoạn Record · đồng hồ ghi âm + "Keep this page open while recording", khoanh đồng hồ và nút tạm dừng · nguồn `_source/record/recording-in-progress.png` · alt: "TranscriptX recording an in-person interview in the browser with a running timer"
3. `interview-transcript-with-timestamps.webp` · Step 2 · kết quả sau khi ghi âm, khoanh 2 timestamp · nguồn `_source/record/recording-transcript-result.png` · alt: "Transcript in TranscriptX with a timestamp above each paragraph"
4. `interview-notes-tab-transcriptx.webp` · Step 4 · transcript + panel phải, khoanh tab Notes và thanh công cụ (có nút timestamp) · nguồn `_source/transcript/transcript-notes-tab.png` · alt: "Notes tab beside a transcript in TranscriptX for adding codes and memos"
5. `download-interview-transcript-docx.webp` · Step 5 · menu Download mở, khoanh nút Download và dòng .docx; Copy nằm cạnh, không khoanh · nguồn `_source/transcript/transcript-download-menu-open.png` · alt: "TranscriptX Download menu open with the .docx format highlighted next to the Copy button"

Ảnh 3–5 là nội dung mẫu (bài hát, bản ghi thử), chưa phải phỏng vấn thật. Nếu có ảnh từ một file phỏng vấn thật (có nhãn người nói, gói Pro) thì nên thay ảnh 3.

## Ảnh bìa / ảnh chia sẻ mạng xã hội (dựng 2026-11-04, kiểu thumbnail "móc tò mò")
Không chèn trong thân bài: đặt làm Cover trong CMS và og:image.
- `how-to-transcribe-an-interview-cover.webp` (2400×1260): Cover trong CMS.
- `how-to-transcribe-an-interview-og-1200x630.jpg`: ảnh khi share link (Facebook, LinkedIn, X, Zalo).
- Nội dung: nền tối, dòng nhỏ "1-hour interview", chữ khổng lồ "4 HOURS" (trắng), "of typing?" (cam), bên phải là transcript thật tràn ra mép phải. Không gạch, không mũi tên, không khoanh, không liệt kê tính năng. User chọn con số cụ thể (4 giờ) thay vì "Zero typing".
- Số "4 hours": trang Pricing ("Typing up 1 hour of audio takes about 4 hours"), ghi trong `_source/_index.md`.
- Nguồn ảnh: `_source/record/recording-transcript-result.png` (crop phần transcript, 1.3× retina). Script: `_source/_tools/build_cover_interview.py` → `cover_kit.make_hook_cover`.
- Alt: `A 1-hour interview takes about 4 hours to type by hand; TranscriptX gives you a timestamped transcript instead`

## Cần kiểm chứng
- **Trang `/interview-transcription/` chưa lên web** (bản EN đang chờ duyệt). Bài link tới trang này 3 lần; phải deploy trang trước khi đăng bài, hoặc tạm đổi link sang `/audio-to-text/`.
- Nút **Speakers** (👥) trên thanh công cụ: có đổi tên người nói được không? Bài chỉ viết "make sure each label matches your participant IDs", không hứa đổi tên.
- Kiểu transcript của TranscriptX: giữ "um/uh" (verbatim) hay bỏ (clean)? Bài không khẳng định, chỉ nói thêm ký hiệu khi soát nếu cần full verbatim.
- Bật/tắt timestamp nằm ở đâu (⚙?): bài không mô tả vị trí.
- "Uploaded files are deleted automatically" lấy từ trang Pricing (FAQ, "within 12 hours"), đọc 2026-11-03.
- "Usually a day or more" (dịch vụ người thật) và "checking takes about as long as listening once": kiến thức chung.
- Upload nhận file video (Zoom/Teams .mp4): theo trang Video to Text; nên thử 1 file .mp4 Zoom.
