# Notes: downsub-alternative

## 1. Bài nói về gì

**Excerpt (EN, dán vào blog)** (145/250)
```
Compares DownSub with TranscriptX for downloading subtitles, including videos with no captions, and explains when each tool is the better choice.
```

Bài "alternative" viết công bằng, cho người đang dùng DownSub (hoặc SaveSubs) và gặp video không có phụ đề hoặc phụ đề tự động sai. DownSub tải phụ đề có sẵn; TranscriptX tự chép phụ đề từ âm thanh nên dùng được cả với video không có phụ đề, sửa được trước khi tải, xuất 5 định dạng. Có mục "khi nào DownSub vẫn tốt hơn". Dẫn về `/youtube-subtitle-downloader/`.

## 2. Dàn ý
- **H1** DownSub Alternative: Get Subtitles Even When a Video Has None
- **Quick answer** (50 từ, có đúng cụm "DownSub alternative"): DownSub tốt khi có phụ đề sẵn; không có hoặc sai thì dùng TranscriptX.
- **Intro:** DownSub làm gì, khi nào người ta tìm cái thay thế.
- **H2 DownSub vs TranscriptX at a Glance:** câu chốt (tải có sẵn vs tự viết) + bảng 9 tiêu chí + nguồn bằng chữ.
- **H2 Why People Look for a DownSub Alternative:** 4 lý do.
- **H2 What to Look for in a DownSub Alternative:** 6 tiêu chí chọn (mới, 2026-11-04).
- **H2 How TranscriptX Works as a DownSub Alternative:** 4 bước + 2 ảnh, Copy ≠ Download.
- **H2 When DownSub Is Still the Better Choice:** 3 điểm mạnh thật của DownSub + quy tắc chọn.
- **H2 Looking for a SaveSubs Alternative Too?:** nhắm keyword phụ, chọn SRT/VTT/TXT-DOCX-PDF, ảnh file VTT. Không đưa claim về SaveSubs.
- **H2 Other Ways to Get Subtitles From a Video:** YouTube Studio (video của mình) + 3 tool khác của TranscriptX.
- **FAQ (6):** best alternative, video không phụ đề, có free không, sửa trước khi tải, có dịch không, SRT hay VTT.
- **H2 CTA.**

**Link nội bộ:** /youtube-subtitle-downloader/ (3 lần, CTA chính), /youtube-transcript/, /download-youtube-transcript/, /video-to-text/, /pricing/, /blog/how-to-download-subtitles-from-youtube/ (2 lần). Tất cả đều có trong `page/llms.txt`.

## 3. Hình ảnh (theo thứ tự trong bài)
Ảnh thật của TranscriptX, crop giữ nguyên pixel gốc (không phóng to/thu nhỏ), viền cam #CC582E vẽ sau khi crop, WebP lossless. Script: `_source/_tools/build_visuals_downsub.py`.
1. **`downsub-alternative-youtube-subtitle-downloader.webp`** (1145×390) · H2 "How TranscriptX Works", sau bước 1 · trang YouTube Subtitle Downloader, khoanh cam ô "Paste a YouTube video URL..." (thấy cả dòng Works with) · nguồn `_source/youtube-subtitle-downloader/youtube-subtitle-downloader-tool.png` · alt: `TranscriptX YouTube Subtitle Downloader with the "Paste a YouTube video URL..." box outlined`
2. **`downsub-alternative-download-srt-vtt.webp`** (1030×440) · sau bước 4 · menu Download đang mở, khoanh cam nút Download (cạnh Copy) và 2 dòng .srt/.vtt; Copy không khoanh · nguồn `_source/transcript/transcript-download-menu-open.png` · alt: `TranscriptX Download menu open next to the Copy button, with the .srt and .vtt subtitle formats outlined`
3. **`downsub-alternative-vtt-subtitle-file.webp`** (1060×470) · H2 SaveSubs, sau danh sách định dạng · file .vtt xuất từ TranscriptX, khoanh dòng thời gian đầu tiên · nguồn `_source/export-files/export-vtt-file.png` · alt: `A VTT subtitle file exported from TranscriptX, with the first timing line outlined`

Ảnh 2 và 3 là nội dung mẫu (bài hát), không phải video thiếu phụ đề thật. Nếu có ảnh kết quả từ một video không có phụ đề thì nên thay ảnh 2.

**Ảnh bìa / ảnh chia sẻ mạng xã hội** (không chèn trong thân bài; Cover trong CMS + og:image)
- `downsub-alternative-cover.webp` (2400×1260) và `downsub-alternative-og-1200x630.jpg`.
- Kiểu thumbnail móc tò mò, thông điệp user chọn (2026-11-04): lấy phụ đề từ video không có caption. Dòng nhỏ "Video has no captions?", chữ khổng lồ "GET SUBTITLES" (trắng), "anyway." (cam), bên phải là file .vtt thật xuất từ TranscriptX (chính là phụ đề nhận được). Không gạch, không mũi tên, không khoanh, không logo đối thủ.
- Không khẳng định gì về kết quả của DownSub. Bản trước "0 SUBTITLES / to download?" đã thay.
- Script: `_source/_tools/build_cover_downsub.py` (dùng `cover_kit.make_hook_cover`).
- Alt: `Video has no captions? Get subtitles anyway: a VTT subtitle file TranscriptX wrote from the video's audio`

## 4. Video
Chưa làm (bài ngắn, không bắt buộc). Nếu làm: dán link video không có phụ đề → transcript hiện ra → Edit sửa 1 tên → Download → .srt.

## 5. Nguồn đối thủ
Chi tiết, nguồn và ngày kiểm tra: `_source/competitors/downsub.md`.
- DownSub, https://downsub.com, kiểm tra 2026-11-03: tải phụ đề có sẵn từ YouTube và ~40–50 site (Viki, Viu, WeTV, Hotstar, Dailymotion, Vimeo, TikTok, X, Instagram…); SRT, VTT, TXT; chọn ngôn ngữ và định dạng; "No extensions or software required"; có link Pro và API, không ghi giá. Không nói gì về chép video không có phụ đề, sửa phụ đề, tài khoản, upload file.
- SaveSubs, https://savesubs.com, kiểm tra 2026-11-03: trang chỉ hiện "Please wait...". Bài **không** đưa claim nào về SaveSubs.
- Trong bài chỉ ghi nguồn bằng chữ ("DownSub's own homepage, checked November 2026"), không link ra trang đối thủ.

## 6. Cần kiểm chứng
- Bảng ghi DownSub "Not covered / Not offered / Not stated on its site": đúng theo trang chủ, chưa test thực tế. **Test cùng file đề xuất:** 1 video YouTube không có phụ đề + 1 video có phụ đề tự động, chạy trên DownSub và TranscriptX, ghi số bước và kết quả. Chưa chạy, bài không đưa kết quả test nào.
- "100+ languages detected": theo trang tool và llms.txt.
- Nút **Edit** trên trang kết quả của luồng YouTube: `_index.md` ghi Edit ở trang kết quả chung.
- Câu "Free to try, no account needed" / "Not required to try": user xác nhận giữ nguyên (2026-11-04).
