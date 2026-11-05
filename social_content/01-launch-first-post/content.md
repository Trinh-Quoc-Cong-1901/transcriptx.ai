# Bài đầu tiên: ra mắt TranscriptX trên 6 nền tảng

**Đã chọn mặc định (người dùng bảo cứ làm):**
- Chế độ: `short` + carousel Instagram (để có bài giới thiệu cho lưới Instagram).
- Ngôn ngữ đăng: **tiếng Anh** (thị trường quốc tế, các trang brand đều tên tiếng Anh).
- Tài khoản: **brand TranscriptX**. TikTok có thêm caption cho tài khoản cá nhân (nếu có).
- Trang đích: `https://transcriptx.ai/` · Mã chiến dịch: `launch-first-post`
- Video: quay màn hình thật, không có người, giọng hay cảnh do AI tạo, nên **không cần nhãn AI**. Nếu dùng giọng đọc AI thì bật nhãn.

---

## 1. Tóm tắt chiến lược
- **Người xem:** creator, podcaster, marketer, sinh viên phải gõ lại lời nói trong video hoặc audio, hoặc phải tua tìm một câu.
- **Thông điệp:** Dán link video là có ngay bản chữ kèm mốc thời gian để copy hoặc tải về.
- **Từ khoá chính:** video to text · **Từ khoá phụ:** transcribe video, youtube transcript, audio to text, subtitles SRT, free transcription

---

## 2. Kịch bản video ngắn (dùng chung cho Reels / TikTok / Shorts / Facebook Reels)

| Thời điểm | Hình ảnh trên màn hình | Lời đọc | Chữ hiện trên video |
|---|---|---|---|
| 0–3s | Video dài đang phát, con trỏ bấm tạm dừng liên tục | Still typing out videos by hand? | Still typing videos by hand? |
| 3–8s | Trang YouTube: bấm **Share** → **Copy link** | Copy the video link. | 1. Copy the link |
| 8–14s | Trang chủ TranscriptX: dán link vào ô *"Upload a file or paste a video link..."* → bấm mũi tên ↑ | Paste it into TranscriptX. Hit the arrow. | 2. Paste + hit ↑ |
| 14–20s | Thanh **Uploading → Recognizing speech** → transcript hiện ra, có mốc thời gian | A 4-minute video took about 6 seconds. | 4-min video → ~6 sec |
| 20–25s | Bấm **Copy** | Copy the text, timestamps included. | Copy = text |
| 25–31s | Bấm **Download** (nút cạnh Copy) → menu .txt .docx .pdf / .srt .vtt | Or download it as a doc or subtitles. | Download = TXT DOCX PDF SRT VTT |
| 31–36s | Bấm **Upload** → menu From this device / Google Drive / Dropbox / OneDrive, rồi lướt qua nút **Record** | No link? Upload a file or record. | Files · Drive · Dropbox · Record |
| 36–40s | Trang kết quả, logo nhỏ góc dưới | Free to try. Link in bio. | Free to try → link in bio |

**Tổng thời lượng ước tính:** ~40 giây.

**3 hook thay thế (A/B):**
- A (vấn đề): "Still typing out videos by hand?"
- B (kết quả bất ngờ): "This 4-minute video became text in 6 seconds."
- C (sai lầm hay gặp): "Stop scrubbing the timeline to find one quote."

**Ảnh bìa:** chữ to **"6 SECONDS?"**, nền là ảnh cắt trang transcript thật của TranscriptX (`transcript/transcript-result-light.png`), không thêm mũi tên, vòng tròn hay danh sách tính năng.

**Ghi chú quay dựng:**
- Màn hình YouTube chỉ xuất hiện trong video, không dùng làm ảnh tĩnh.
- Phụ đề hiện suốt video (làm bằng chính TranscriptX → Download .srt).
- Xuất file gốc 9:16 không có logo nền tảng khác. Mỗi nền tảng tải lên từ file gốc, không tải lại bản đã có watermark TikTok.
- Dựng bằng `page/blog/_source/_tools/video_hq.py` nếu muốn đồng bộ chất lượng với video blog.

---

## 3. TikTok

### Tài khoản brand
```text
YouTube video to text in about 6 seconds 👀 Copy the link, paste it, done. Free to try, link in bio.

#transcription #videototext #contentcreator #aitools
```
- **Góc nội dung:** demo thao tác, nhanh và gọn.
- **Nhạc gợi ý:** nhạc điện tử hoặc lo-fi trong thư viện TikTok, nhịp vừa (~100–110 BPM), cắt cảnh theo phách.
- **Giờ đăng:** Thứ 5, 05/11, 19:40 (giờ ET)
- **Link bio:** `https://transcriptx.ai/?utm_source=tiktok&utm_medium=social&utm_campaign=launch-first-post`

### Tài khoản cá nhân (nếu có), góc khác: mẹo tìm câu nói
```text
Turn your video to text, then Ctrl+F the quote you need. No more scrubbing the timeline 🔍 Tool's in my bio.

#creatortips #videoediting #transcription #productivity
```
- **Góc nội dung:** mẹo cho người dựng video. Cắt bản dựng riêng, mở bằng cảnh tua timeline rồi chuyển sang Ctrl+F trên transcript. Không đăng lại y nguyên video của brand.
- **Nhạc gợi ý:** nhạc vui, nảy (~120 BPM), có một nhịp "drop" đúng lúc Ctrl+F tìm ra câu.
- **Giờ đăng:** Thứ 7, 07/11, 20:00 (giờ ET), khác ngày với brand.
- **Link bio:** dùng link UTM giống bên trên.

---

## 4. Instagram

### Reels (brand, mời tài khoản cá nhân làm Collab nếu có)
```text
Copy a video link. Paste it. Get the full transcript with timestamps in seconds.

Works with YouTube, TikTok, Instagram, Facebook and X links. Or upload a file.
Copy the text, or download it as .txt .docx .pdf .srt .vtt.
Free to try, no sign-up.

👉 Link in bio.

#transcription #videototext #contentcreator #reelstips #subtitles
```
- Hook: 80 ký tự, hiện trọn trước nút "more".
- **Collab:** brand đăng chính, mời tài khoản cá nhân làm Collab.
- **Giờ đăng:** Thứ 5, 05/11, 19:20 (giờ ET)
- **Link bio:** `https://transcriptx.ai/?utm_source=instagram&utm_medium=social&utm_campaign=launch-first-post`

### Carousel giới thiệu (brand), 8 slide

| Slide | Tiêu đề | Nội dung | Gợi ý hình (ảnh thật TranscriptX) |
|---|---|---|---|
| 1 | Any video or audio. Text in seconds. | (logo TranscriptX nhỏ) | `brand/cover-producthunt-1270x760.png` cắt vuông |
| 2 | Paste a link | YouTube, TikTok, Instagram, Facebook, X and more. Paste it, hit the arrow. | `homepage/homepage.png` |
| 3 | Or upload a file | From your device, Google Drive, Dropbox or OneDrive. | `upload/upload-source-options.png` |
| 4 | Or just record | Hit Record, talk, keep the page open. Your words turn into text. | `record/recording-in-progress.png` |
| 5 | Text with timestamps | Every paragraph has a timestamp. Edit the text right on the page. | `transcript/transcript-result-light.png` |
| 6 | Copy or download | Copy grabs the text. Download gives .txt .docx .pdf .srt .vtt. | `transcript/transcript-download-menu-open.png` |
| 7 | Free to try | No sign-up needed. Sign in to keep your history on every device. | `mobile/mobile-homepage.png` |
| 8 | Follow for weekly tips | Small, practical tips for video and audio. Try it free, link in bio. | logo + handle @contact.transcriptx |

```text
Slide 1: Any video or audio. Text in seconds.
Slide 2: Paste a link — YouTube, TikTok, Instagram, Facebook, X and more. Paste it, hit the arrow.
Slide 3: Or upload a file — From your device, Google Drive, Dropbox or OneDrive.
Slide 4: Or just record — Hit Record, talk, keep the page open. Your words turn into text.
Slide 5: Text with timestamps — Every paragraph has a timestamp. Edit the text right on the page.
Slide 6: Copy or download — Copy grabs the text. Download gives .txt .docx .pdf .srt .vtt.
Slide 7: Free to try — No sign-up needed. Sign in to keep your history on every device.
Slide 8: Follow for weekly tips — Small, practical tips for video and audio. Try it free, link in bio.
```

**Caption carousel:**
```text
Hi, we're TranscriptX 👋

If it has speech in it, we turn it into text: videos, podcasts, lectures, voice notes.
Swipe to see the 3 ways in and the 2 ways out.

Save this for the next time you need a transcript. Link in bio.

#transcription #audiototext #studytips #podcasting #aitools
```
- **Giờ đăng:** Thứ 6, 06/11, 19:00 (giờ ET). Ghim lên đầu trang cá nhân.
- **Lưu ý:** slide 8 hứa "weekly tips", nên chỉ giữ chữ này khi bạn chắc đăng đều hằng tuần.

---

## 5. YouTube Shorts (kênh @AITransciptx)
**Tiêu đề** (39 ký tự):
```text
YouTube Video to Text in Seconds (Free)
```
**Mô tả:**
```text
Turn any YouTube video to text: copy the link, paste it into TranscriptX, and get the full transcript with timestamps. Copy it, or download it as TXT, DOCX, PDF, SRT or VTT for subtitles.

Try it free: https://transcriptx.ai/?utm_source=youtube&utm_medium=social&utm_campaign=launch-first-post

#shorts #transcription #youtubetips
```
- **Giờ đăng:** Thứ 5, 05/11, 20:00 (giờ ET)
- Ghi chú: tải lên từ file gốc, bật phụ đề.

---

## 6. Facebook

### Bản 1: bài trên Page (đăng kèm video Reels, ghim lên đầu Page)
```text
If you've ever paused a video 50 times just to type out what someone said, this page is for you.

TranscriptX turns video and audio into text with timestamps. Paste a YouTube, TikTok, Instagram, Facebook or X link, or upload a file, and the transcript is ready in seconds. Copy it, or download it as TXT, DOCX, PDF, SRT or VTT.

Free to try, no sign-up 👉 https://transcriptx.ai/

We'll post short, practical tips here for creators, students and anyone who works with spoken content. What do you transcribe most often?
```
- **Giờ đăng:** Thứ 5, 05/11, 19:00 (giờ ET). Đây là bài mở màn, đăng đầu tiên.

### Bản 2: đăng group (creator, podcast, video editing)
```text
Quick tip for anyone who edits interviews or long videos:

Instead of scrubbing the timeline to find one quote, I turn the video into a transcript first and search it with Ctrl+F. Every line has a timestamp, so I can jump straight to that spot in the edit.

Bonus: the same transcript becomes a subtitle file (SRT/VTT) and a starting point for a blog post or show notes.

How do you all find quotes in long footage?
```
**Bình luận đầu tiên:**
```text
A few people asked which tool: I use TranscriptX (paste a link or upload a file). Disclosure: I'm on the team.
https://transcriptx.ai/
```
- **Giờ đăng:** rải trong tuần sau, mỗi group một ngày, không đăng cùng lúc nhiều group.
- **Đọc luật group trước khi đăng.** Nhiều group cấm link, khi đó bỏ bình luận chứa link.
- Mình đã thêm câu "Disclosure: I'm on the team" để giữ uy tín, tránh bị coi là quảng cáo giấu mặt.

---

## 7. X (@transcriptxai)

### Bài đơn (219/280 ký tự)
```text
Typing out a video by hand takes forever.

Paste the link into TranscriptX instead: full text with timestamps in seconds. Copy it, or export TXT, DOCX, PDF, SRT or VTT.

Free to try, no sign-up 👇
https://transcriptx.ai/?utm_source=x&utm_medium=social&utm_campaign=launch-first-post
```

### Thread 6 bài (đăng hôm sau, khác giờ bài đơn)
```text
1/ Every video you post already hides a blog draft, a subtitle file and a list of quotable lines.

You just need the words as text. Here's the quick way to get them 🧵
```
```text
2/ Copy the video link.

YouTube, TikTok, Instagram, Facebook, X and more.

No link? Upload the file from your device, Google Drive, Dropbox or OneDrive. Or hit Record and just talk.
```
```text
3/ Paste it into TranscriptX and hit the arrow.

In our test, a 4-minute YouTube video came back as text in about 6 seconds. Every paragraph has a timestamp.
```
```text
4/ Pick what you need:

Copy → the text, with timestamps
Download → .txt .docx .pdf for documents, .srt .vtt for subtitles

Two buttons, side by side.
```
```text
5/ What creators do with it:

• pull quotes for social posts
• turn a video into a blog draft
• add captions to a Reel or Short
• Ctrl+F a long interview instead of scrubbing the timeline
```
```text
6/ Free to try, no sign-up:
https://transcriptx.ai/?utm_source=x&utm_medium=social&utm_campaign=launch-first-post

Follow @transcriptxai for more small tips like this.
```
Số ký tự: 166 · 182 · 157 · 150 · 187 · 105 (link tính 23).
- **Giờ đăng:** bài đơn Thứ 5, 05/11, 20:20 kèm video; thread Thứ 6, 06/11, 20:00 (giờ ET). Ghim thread.
- Không dùng hashtag.

---

## 8. Threads (412/500 ký tự)
```text
Honest question for anyone who edits video: how long does it take you to find one quote in a 40-minute recording?

That's the reason TranscriptX exists. Paste a link or upload a file, get the full transcript with timestamps, then search it like a document.

This is our first post here 👋 We'll share small, practical tips for working with video and audio.

What's the most annoying part of your editing workflow?
```
- **Topic tag:** `Content Creators`
- **Link:** đặt ở **reply đầu tiên**, không để trong bài, để bài được đọc như một cuộc trò chuyện:
```text
Try it free, no sign-up: https://transcriptx.ai/?utm_source=threads&utm_medium=social&utm_campaign=launch-first-post
```
- **Giờ đăng:** Thứ 5, 05/11, 20:40 (giờ ET)

---

## 9. Bảng link UTM
| Nền tảng | Link |
|---|---|
| TikTok | https://transcriptx.ai/?utm_source=tiktok&utm_medium=social&utm_campaign=launch-first-post |
| Instagram | https://transcriptx.ai/?utm_source=instagram&utm_medium=social&utm_campaign=launch-first-post |
| YouTube | https://transcriptx.ai/?utm_source=youtube&utm_medium=social&utm_campaign=launch-first-post |
| Facebook | https://transcriptx.ai/ |
| X | https://transcriptx.ai/?utm_source=x&utm_medium=social&utm_campaign=launch-first-post |
| Threads | https://transcriptx.ai/?utm_source=threads&utm_medium=social&utm_campaign=launch-first-post |

---

## 10. Lịch đăng (giờ ET; giờ Việt Nam = ET + 12 tiếng)
| Nền tảng | Tài khoản | Ngày | Giờ ET | Giờ VN |
|---|---|---|---|---|
| Facebook Page + Reels | Brand | Thứ 5, 05/11 | 19:00 | 07:00 Thứ 6, 06/11 |
| Instagram Reels | Brand (Collab) | Thứ 5, 05/11 | 19:20 | 07:20 Thứ 6 |
| TikTok | Brand | Thứ 5, 05/11 | 19:40 | 07:40 Thứ 6 |
| YouTube Shorts | Brand | Thứ 5, 05/11 | 20:00 | 08:00 Thứ 6 |
| X (bài đơn) | Brand | Thứ 5, 05/11 | 20:20 | 08:20 Thứ 6 |
| Threads | Brand | Thứ 5, 05/11 | 20:40 | 08:40 Thứ 6 |
| Instagram Carousel | Brand | Thứ 6, 06/11 | 19:00 | 07:00 Thứ 7, 07/11 |
| X (thread) | Brand | Thứ 6, 06/11 | 20:00 | 08:00 Thứ 7 |
| TikTok | Cá nhân | Thứ 7, 07/11 | 20:00 | 08:00 CN, 08/11 |
| Facebook groups | Cá nhân | Tuần 09/11 trở đi | 19:00–21:00 | sáng hôm sau |

---

## 11. Checklist trước khi đăng
```text
[ ] 3 giây đầu nêu vấn đề của người xem ("Still typing out videos by hand?")
[ ] File gốc không có logo nền tảng khác
[ ] Đã sửa caption và hashtag theo từng nền tảng
[ ] Đã bật nhãn AI nếu video có người hoặc cảnh AI trông như thật (mặc định: không cần)
[ ] Có phụ đề hiển thị trên video
[ ] Link đã gắn đúng UTM
[ ] Bio TikTok/Instagram đã thay bằng link UTM của nền tảng đó
[ ] Ghim: bài Facebook, carousel Instagram, thread X
[ ] Đọc luật từng group Facebook trước khi đăng
```
