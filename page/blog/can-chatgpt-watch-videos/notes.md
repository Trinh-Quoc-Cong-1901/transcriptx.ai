# Notes: can-chatgpt-watch-videos

## Bài nói về gì

Excerpt (169 ký tự):
```
Why ChatGPT and Claude can't watch videos, the old copy-and-paste workaround, and how to connect TranscriptX's Transcription MCP so they read the transcript from a link.
```

Bài giới thiệu trang **Transcription MCP** (`/transcription-mcp/`) theo mạch: ChatGPT/Claude không xem/nghe được video → dán link thì nó đoán từ tiêu đề, mô tả → trước giờ phải tự kể lại hoặc copy transcript rồi dán vào → cách mới: thêm TranscriptX vào ChatGPT/Claude một lần, dán link là AI tự lấy transcript. Dành cho người hay dùng ChatGPT/Claude để hỏi về video, bài giảng, podcast.

## Dàn ý
- **H1 + Quick answer:** không, ChatGPT đọc chữ; cách nhanh nhất là thêm Transcription MCP.
- **Intro:** cảnh dán link YouTube, ChatGPT trả lời tự tin nhưng sai.
- **Can ChatGPT Watch Videos?** Nó làm việc với chữ; với link chỉ có tiêu đề, mô tả; với file thì không có phần lời nói.
- **Can ChatGPT Watch YouTube Videos? What Happens When You Paste a Link:** 3 bước: đọc trang, trả lời từ đó, không nói là đang đoán. Gom ý "access / open youtube links".
- **Can ChatGPT Analyze Videos? It Needs the Words First:** transcript giúp được gì; giới hạn: chỉ có lời nói, không có những gì chỉ hiện trên hình.
- **Two Workarounds People Have Used So Far:** (1) tự kể lại; (2) copy transcript từ `/youtube-transcript/` bằng nút **Copy** rồi dán vào.
- **The New Way: Connect TranscriptX to ChatGPT and Claude:** MCP là gì (1 đoạn), 3 việc AI làm được (transcribe, transcribe_file, get_transcript), app chính thức đang chờ duyệt.
  - H3 **How to add TranscriptX to ChatGPT:** 3 bước + Developer mode.
- **Can Claude Watch Videos?** Cùng giới hạn; connector chạy trên claude.ai và Claude Desktop.
  - H3 **How to add TranscriptX to Claude:** 3 bước.
- **How to Get ChatGPT to Watch a YouTube Video:** 5 câu lệnh mẫu; kết quả trong chat (đầu transcript, Copy/Export TXT SRT VTT, link bản đầy đủ); upload file.
- **What Can You Transcribe Inside the Chat?** Danh sách nguồn.
- **Is It Free, and Does It Read My Chats?** Free mỗi ngày, Pro nâng giới hạn, không mua trong chat; chỉ nhận link/file, file xoá trong 12 giờ, ngắt kết nối bất cứ lúc nào.
- **Copy and Paste or Connector: Which One to Use:** bảng so sánh 2 cách.
- **FAQ:** 6 câu (summarize, open links, AI nào xem được YouTube/Gemini, Claude, cần tài khoản không, file upload).
- **CTA:** về `/transcription-mcp/`.

## Hình ảnh
1. `copy-youtube-transcript-for-chatgpt.webp` · mục "Two Workarounds", sau 4 bước copy · trang transcript, khoanh cam nút **Copy** · nguồn `_source/transcript/transcript-notes-tab.png` · alt: "TranscriptX transcript page with the Copy button highlighted, ready to paste into ChatGPT"
2. `transcription-mcp-add-to-chatgpt-claude.webp` · mục "The New Way", sau đoạn giải thích MCP · trang Transcription MCP, khoanh cam **Add to ChatGPT** và **Add to Claude** · nguồn `_source/chatgpt-claude/transcription-mcp-page.png` · alt: "The TranscriptX Transcription MCP page with the Add to ChatGPT and Add to Claude buttons"
3. `chatgpt-transcriptx-allow-access.webp` · H3 "How to add TranscriptX to ChatGPT", sau bước 3 · màn hình xin quyền của TranscriptX (trang transcriptx.ai), khoanh cam **Allow**, email đã làm mờ · nguồn `_source/chatgpt-claude/chatgpt-transcriptx-allow-access.png` · alt: "TranscriptX permission screen asking to connect ChatGPT, with the Allow button highlighted"

Ảnh giao diện ChatGPT (plugin, ô chat, kết quả) chỉ dùng trong video.

## Video
`images/video/can-chatgpt-watch-videos-transcriptx-mcp.mp4` · 2560×1440, 60 fps, ~50 s, lồng tiếng Anh (edge-tts en-US-AvaNeural) + nhạc nền nhẹ. Script: `_source/_tools/build_video_chatgpt_mcp.py`. Thumbnail + ảnh tĩnh: `_source/_tools/build_visuals_chatgpt_mcp.py`.
1. Hook "Can ChatGPT watch videos?" + câu trả lời thật của ChatGPT Free ("couldn't retrieve its actual content from the link").
2. Trang `/transcription-mcp/`, bấm **Add to ChatGPT**.
3. Trang plugin TranscriptX trong ChatGPT, bấm **Install plugin**.
4. Màn hình xin quyền, bấm **Allow** (nhãn "or Continue as guest"), email làm mờ.
5. Chọn TranscriptX, gõ "Transcribe this video:" + link, bấm gửi.
6. Thẻ kết quả trong chat: "Processed in 8 s", khoanh **Export** và **Copy transcript**.
7. Quay lại trang MCP, bấm **Add to Claude**.
8. CTA `transcriptx.ai/transcription-mcp`.
Gói YouTube: `images/video/youtube-video.md`.

## Nguồn
- Trang `https://transcriptx.ai/transcription-mcp/` (đọc 2026-10-29): các bước ChatGPT/Claude, Developer mode, nguồn hỗ trợ, 3 tool, kết quả (Copy, Export TXT/SRT/VTT, link bản đầy đủ), giới hạn (free daily allowance, Pro, không mua trong chat, link private/đã xoá không chép được), privacy (chỉ nhận link/file, file xoá trong 12 giờ, ngắt kết nối trong settings), badge "Never reads your other messages".
- `_source/_index.md` mục `chatgpt-claude/`.

## Cần kiểm chứng
- Đã test 2026-10-29 (user, ChatGPT gói Free): dán link YouTube → ChatGPT trả lời "I couldn't retrieve its actual content from the link". Cài plugin TranscriptX → Allow → "Transcribe this video: <link>" → video 3 phút "Processed in 8s", thẻ có Edit / Export / Copy transcript. Ảnh trong `_source/chatgpt-claude/`.
- Chưa test: ChatGPT đọc tiêu đề/mô tả rồi đoán (câu "or works from the title and description"), và upload file video vào ChatGPT. Viết theo hiểu biết chung.
- Luồng thật (Install plugin) khác chữ trên trang MCP (Add custom MCP server). Bài ghi luồng thật, để cách custom server làm phương án phụ. Nên sửa lại chữ bước 1–2 trên trang `/transcription-mcp/` cho khớp.
- Phần Claude chưa test (chưa có ảnh): các bước lấy từ trang `/transcription-mcp/`.
- Claude "không xem được video, không nghe được audio từ link YouTube": kiến thức chung, nên thử lại.
- Gemini "có tích hợp YouTube": kiến thức chung, chưa kiểm tra trên trang của Google.
- "Signing in … keeps your transcripts in your TranscriptX history, on every device" lấy từ bài how-to-get-youtube-transcript đã đăng.
