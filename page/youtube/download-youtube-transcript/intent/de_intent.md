🔥 TranscriptX – Download YouTube Transcript (German / de)

URL:
/de/download-youtube-transcript

Intent chính:

Tải transcript video YouTube về máy (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Đức muốn **tải bản transcript của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcript trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/de/youtube-subtitle-downloader`. **Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **`Untertitel` (file phụ đề khớp giờ cho editor) → `/de/youtube-subtitle-downloader`**
> **`Transkript` (tài liệu để đọc/lưu/nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 đã tự định nghĩa ranh giới — trang này ra **tài liệu để đọc/lưu/nộp**; trang kia ra **file phụ đề khớp giờ cho phần mềm dựng phim**.

### ✅ Kết quả kiểm trùng: 0 keyword trùng

Đã đối chiếu 11 keyword de của trang này với 9 keyword de của `/de/youtube-subtitle-downloader`:

| Trang | Danh sách de | Từ khóa lõi |
| ----- | ------------ | ----------- |
| **download-youtube-transcript** (trang này) | 11 keyword | `Transkript` (9) · `Transkription` (1) · `Text` (2) · `transcript` (1) |
| `/de/youtube-subtitle-downloader` | 9 keyword | `Untertitel` (8) · `captions` (1) |
| **Số keyword trùng khít** | **0** ✅ | — |

### 🎉 Lợi thế riêng của tiếng Đức: `Untertitel` vs `Transkript` tách bạch hoàn toàn

Đây là điểm khác biệt lớn nhất so với bản **vi** và **pt**:

- Bản **vi** phải hy sinh keyword mạnh nhất (`tải phụ đề youtube`, 100–1K) cho trang kia, vì tiếng Việt dùng chữ "phụ đề" lẫn cho cả hai khái niệm — phải neo đẩy đi từng câu.
- Tiếng Đức thì `Untertitel` (phụ đề khớp giờ) và `Transkript` (bản chép lời dạng tài liệu) là **hai từ riêng biệt, người bản ngữ không nhầm lẫn**. Việc phân định gần như **miễn phí**: chỉ cần chọn đúng từ là ranh giới tự có.
- **Hệ quả:** trang này **không mất keyword nào**, không cần kỹ thuật neo đẩy đi. Kết quả tải về luôn gọi là `Transkript` / `Text`. Từ `Untertitel` chỉ xuất hiện đúng **2 chỗ**: mục SRT ở S2 và câu trỏ sang trang kia ở S6.

**Ngoại lệ duy nhất:** `youtube untertitel als text herunterladen` (10–100) có chứa `Untertitel` nhưng vế **`als Text`** neo rõ là muốn văn bản để đọc → **thuộc trang này**. Trang kia giữ cụm song song `youtube untertitel als srt herunterladen` — ranh giới `als Text` vs `als SRT` rất sạch.

---

## Lỗi dữ liệu trong file nguồn

Đã soát phần `## German (de)` của `2_loc_kw.md`:

- ❌ **Không có** dòng rác `Keyword ideas` / `Keywords you provided` (khác phần `## Vietnamese (vi)` — phần vi có cả 2 dòng rác này).
- ❌ **Không có** keyword trùng lặp trong nội bộ danh sách de.
- ❌ **Không có** keyword sai intent kiểu "tải VIDEO" (khác bản vi phải loại tới 4 cụm).

**Số keyword thực: 11 dòng thô − 0 rác − 0 sai intent = 11 keyword, dùng được toàn bộ.**

⚠️ **Một cái bẫy chuỗi ký tự cần lưu ý:** keyword `transkript von youtube video herunterladen` có chứa chuỗi con `youtube video herunterladen` — vốn là intent **tải file video mp4**. Keyword này hợp lệ vì tân ngữ thật của `herunterladen` là `Transkript`. Nhưng khi viết `de.json` phải giữ nguyên trật tự `Transkript von einem YouTube-Video herunterladen`, **tuyệt đối không để `Video` đứng liền trước `herunterladen`**.

---

## Từ khóa chính

**youtube transkript herunterladen** (100 – 1K) ✅ *đã search*

Cụm mạnh nhất trong toàn danh sách de và cũng là **lõi chung** của 5 cụm đuôi dài khác (`... als txt ...`, `... pdf ...`, `transkript von youtube video ...`, `youtube transkription ...`, `youtube video transkript downloaden`). Neo vào đây thì các đuôi dài tự phủ theo. Khác bản vi, ở đây cụm mạnh nhất **thuộc về đúng trang này** — không phải nhường đi đâu cả.

---

## Từ khóa phụ

### Nhóm `herunterladen` (trục chính — 6 cụm)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript herunterladen | 100 – 1K | ✅ đã search *(KW chính)* |
| youtube untertitel als text herunterladen | 10 – 100 | ✅ đã search — luôn kèm vế `als Text`, chỉ dùng ở S2 (mục TXT) |
| transkript von youtube video herunterladen | 10 – 100 | ✅ đã search — giữ trật tự, `Video` không đứng cạnh `herunterladen` |
| youtube transkription herunterladen | 0 – 10 | ✅ đã search |
| youtube transkript als txt herunterladen | 0 – 10 | ✅ đã search |
| youtube video text herunterladen | 0 – 10 | ✅ đã search |
| youtube transkript pdf herunterladen | 0 – 10 | ✅ đã search |

### Nhóm `speichern` (lưu về máy)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript speichern | 0 – 10 | ✅ đã search |

### Nhóm `exportieren` (xuất định dạng)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript exportieren | 10 – 100 | ✅ đã search |

### Nhóm mượn tiếng Anh (người Đức hay gõ lẫn)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video transkript downloaden | 0 – 10 | ✅ đã search — `downloaden` là động từ mượn đã Đức hóa, dùng 1 lần |
| download youtube transcript deutsch | 0 – 10 | ✅ đã search — neo ở `seo.description` + 1 FAQ |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript als docx herunterladen | — | 🔄 dịch bổ sung (DOCX) |
| youtube transkript offline lesen | — | 🔄 dịch bổ sung (offline) |
| youtube transkript kostenlos herunterladen | — | 🔄 dịch bổ sung (free) |
| transkript auf dem gerät speichern | — | 🔄 dịch bổ sung (save to device) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ **Volume trang này thấp hơn `/de/video-to-text`.** "Transkript herunterladen" là nhu cầu hẹp hơn "Video transkribieren". Không nhồi mật độ — chiến lược là **phủ đều 11 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Đức **đã biết mình muốn transcript** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài extension.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline**.
- Miễn phí, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Đức (kể cả giọng vùng Áo/Thụy Sĩ).

### Khác biệt so với bản tiếng Anh

1. **Không cần né tránh cụm phụ đề — nhưng phải chọn từ có kỷ luật.** Bản EN có sẵn "transcript" vs "subtitle" tách bạch; tiếng Đức cũng vậy (`Transkript` vs `Untertitel`). Điểm khác là tiếng Đức **có thêm** `Transkription` (chỉ *quá trình* chép lời) — không được dùng thay cho `Transkript` (chỉ *kết quả*, tức file tải về). Trong 11 keyword chỉ có 1 cụm dùng `Transkription`, neo đúng ở S3 (phần mô tả hệ thống đang chép lời).

2. **Bẫy `herunterladen` + `Video`.** Tiếng Đức đẩy động từ ra cuối câu, nên rất dễ vô tình tạo ra chuỗi `... YouTube-Video herunterladen` — đúng bằng keyword của nhóm tải file mp4, một nhóm có volume rất lớn ở Đức và SERP toàn video downloader. Bản EN không gặp vì trật tự SVO giữ động từ đứng trước tân ngữ. **Quy tắc: mọi `herunterladen` phải có tân ngữ `Transkript` / `Text` / `Datei` đứng liền trước.**

3. **Cặp `herunterladen` / `downloaden` cùng tồn tại.** Người Đức gõ cả hai. Bản EN chỉ có "download". Xử lý: `herunterladen` là dạng chuẩn dùng xuyên suốt; `downloaden` dùng **đúng 1 lần** ở S3 (bám cụm `youtube video transkript downloaden`), nhiều hơn sẽ nghe như Denglisch bừa bãi.

4. **Danh từ ghép thay cho cụm giới từ.** Tiếng Đức gộp `YouTube-Transkript`, `Transkript-Datei`, `Untertiteldatei` thành một từ. Điều này làm mật độ keyword đọc tự nhiên hơn bản EN, nhưng cũng nghĩa là phải giữ dấu gạch nối nhất quán ở `YouTube-Transkript` / `YouTube-Video`.

5. **Nhấn PDF/DOCX mạnh hơn bản EN.** Danh sách de có riêng cụm `youtube transkript pdf herunterladen`; môi trường học thuật và văn phòng Đức chuộng bản PDF nộp lưu và DOCX để biên tập.

---

## Đối tượng người dùng

- Sinh viên, nghiên cứu sinh (lưu transcript bài giảng, phỏng vấn vào thư mục đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX để làm biên bản, tài liệu nội bộ)
- Người học tiếng Đức / người Đức học ngoại ngữ (tải TXT đọc offline)
- Người làm phụ đề cần bản nháp có timecode (SRT)
- Người cần đưa transcript vào công cụ khác yêu cầu upload file

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `de.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (de) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Transkript herunterladen | youtube transkript herunterladen *(KW chính)* |
| — | **quickAnswer** | youtube transkript herunterladen, transkript von youtube video herunterladen |
| 1 | Was dir ein heruntergeladenes Transkript bringt | youtube transkript herunterladen, youtube video text herunterladen |
| 2 | Welches Format solltest du herunterladen? | youtube transkript als txt herunterladen, youtube untertitel **als text** herunterladen *(mục TXT)*, youtube transkript pdf herunterladen *(mục PDF)* |
| 3 | So lädst du ein YouTube Transkript herunter | transkript von youtube video herunterladen, youtube transkription herunterladen, youtube video transkript downloaden |
| 4 | Wenn du die Datei brauchst, nicht nur den Text | youtube transkript speichern, youtube transkript exportieren |
| 5 | Transkripte in über 100 Sprachen herunterladen | youtube transkript herunterladen *(+ nhấn tiếng Đức)* |
| 6 | Wenn ein anderes Tool besser passt | ⚠️ **`Untertitel` xuất hiện ở đây, trong câu trỏ sang `/de/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | Häufige Fragen | youtube transkript exportieren, youtube transkript als txt herunterladen, download youtube transcript deutsch + long-tail |
| — | **conclusion** | youtube transkript herunterladen, kostenlos |

### Ghi chú riêng cho bản de (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là 1 trong 2 chỗ duy nhất từ `Untertitel` được phép xuất hiện.
- Từ `Untertitel` chỉ dùng **2 lần**: (a) S2 mục SRT — mô tả công dụng làm phụ đề; (b) S6 — câu trỏ sang `/de/youtube-subtitle-downloader`. Ngoài ra, cụm keyword `Untertitel als Text` dùng **1 lần** ở S2 mục TXT, luôn giữ nguyên vế `als Text`.
- `Transkription` dùng đúng **1 lần** ở S3 (mô tả quá trình chép lời). Mọi chỗ khác chỉ dùng `Transkript`.
- `downloaden` dùng đúng **1 lần** ở S3. Mọi chỗ khác dùng `herunterladen`.
- Nỗi lo nhận dạng tiếng Đức xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Đức — không thêm câu.

---

## Không nên tối ưu cho các keyword

- **`youtube untertitel herunterladen` / `untertitel von youtube herunterladen` / `youtube untertitel downloader` / `youtube untertitel als srt herunterladen` / `youtube captions herunterladen`** → **/de/youtube-subtitle-downloader** (file phụ đề khớp giờ cho phần mềm dựng phim). Trang này không được đặt `Untertitel` vào `title` / `h1` / `h2`.
- `youtube transkript` / `youtube transkript anzeigen` / `youtube transkript kopieren` → **/de/youtube-transcript** (đọc và copy trên màn hình, không tải file).
- `youtube video zusammenfassen` / `youtube zusammenfassung` → **/de/youtube-video-summarizer**.
- **`youtube video herunterladen` / `youtube downloader` / `youtube mp4 herunterladen` / `youtube video downloaden`** → **intent tải VIDEO**, SERP toàn video downloader. Trang này tải **chữ**. Quy tắc: `herunterladen` luôn phải có tân ngữ `Transkript` / `Text` / `Datei` đứng liền trước, **không bao giờ `Video`**.
- `video transkribieren` / `video in text umwandeln` (không có chữ youtube) → **/de/video-to-text** (upload file từ máy, không dán link).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/de/youtube-transcript` (chỉ muốn đọc/copy trên màn hình, không cần file)
- → `/de/youtube-subtitle-downloader` (cần file phụ đề khớp giờ cho phần mềm dựng phim) — **đây là link quan trọng nhất, cũng là chỗ duy nhất `Untertiteldatei` được neo**
- → `/de/youtube-video-summarizer` (chỉ cần ý chính, không cần toàn văn)

---

## Ghi chú kỹ thuật cho de.json

- Xưng hô **`du`** xuyên suốt, nhất quán với `/de/video-to-text`. **Tuyệt đối không trộn `Sie`** (kể cả trong FAQ).
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- Danh từ ghép giữ dấu gạch nối nhất quán: `YouTube-Transkript`, `YouTube-Video`, `YouTube-Link`, `Transkript-Datei`.
- Cấu trúc: **7 section**, **8 FAQ**, S1 = `content` 3, S2 = `intro` 1 + `items` 4, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5 = `content` 2, S6 = `content` 2, S7 = `items` 8, conclusion = `content` 2. **Trang này KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/de/...`.
- **Tuyệt đối không để chuỗi `Video herunterladen` hoặc `Video downloaden` xuất hiện.**
