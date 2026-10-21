🔥 TranscriptX – Download YouTube Transcript (Arabic / ar)

URL:
/ar/download-youtube-transcript

Intent chính:

Tải nội dung chữ (transcript) của video YouTube về thiết bị dưới dạng file — TXT, DOCX, PDF, SRT — miễn phí

Trang này nhắm đến người dùng Ả Rập muốn **tải bản nội dung chữ của video YouTube xuống máy** dưới dạng file: để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc trên màn hình.

---

## 🚨 CỤM YOUTUBE 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/ar/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ (không phải theo volume):**

> **`ترجمة` mang nghĩa phụ đề khớp giờ cho editor → `/ar/youtube-subtitle-downloader`**
> **`نص` / `تفريغ` (tài liệu để đọc / lưu / nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 tự định nghĩa ranh giới — trang này ra **tài liệu** (`مستند` để đọc/lưu/nộp), trang kia ra **file phụ đề khớp giờ cho phần mềm dựng phim**.

### Kết quả kiểm trùng keyword ar (12 KW trang này × 12 KW trang subtitle)

| Loại | Số cụm | Chi tiết |
| ---- | ------ | -------- |
| Trùng **tuyệt đối** (chuỗi giống hệt) | **0** | — |
| Trùng **thân từ** (chung stem `ترجمة فيديو يوتيوب`) | **1** ⚠️ | `تنزيل ترجمة فيديو يوتيوب نص` (trang này) × `تحميل ترجمة فيديو يوتيوب` + `تنزيل ترجمة فيديو يوتيوب srt` (trang subtitle) |

**Bảng cụm trùng và cách xử lý:**

| Keyword | Volume | Thuộc trang | Xử lý ở trang này |
| ------- | ------ | ----------- | ----------------- |
| `تنزيل ترجمة فيديو يوتيوب نص` | 0–10 | **TRANG NÀY** (có đuôi `نص` neo rõ là muốn văn bản) | Dùng **đúng 1 lần**, ở **S6 đoạn 2**, ngay trong câu trỏ sang `/ar/youtube-subtitle-downloader`. **Không bao giờ** vào title/H1/H2. |
| `تحميل ترجمة فيديو يوتيوب` | 100–1K | `/ar/youtube-subtitle-downloader` | ❌ Không tối ưu ở đây |
| `تحميل ترجمة يوتيوب` | 100–1K | `/ar/youtube-subtitle-downloader` | ❌ Không tối ưu ở đây |
| `موقع تحميل ترجمة يوتيوب` | 10–100 | `/ar/youtube-subtitle-downloader` | ❌ Không tối ưu ở đây |

**Hệ quả:** trang này **không có cụm nào ≥ 100 volume**. Toàn bộ 12 keyword đều ở mức 0–10. Volume mạnh của cụm YouTube tiếng Ả Rập tập trung ở nhóm `ترجمة` — mà nhóm đó thuộc trang subtitle. Chiến lược: **không nhồi mật độ, phủ đều 12 cụm**, mỗi cụm một vị trí neo.

---

## ⚠️ MỤC RIÊNG: QUY TẮC NEO NGHĨA `نص` VÀ `ترجمة`

Đây là hai từ đa nghĩa nguy hiểm nhất của bản ar. Sai một chỗ là lệch intent cả trang.

### (a) `نص` — phủ cả chữ viết lẫn chữ nói

`نص` để trần có thể hiểu là "văn bản" chung chung, thậm chí là "điều khoản/quy định". **Luôn phải có định ngữ neo lại:**

| ✅ Dùng | ❌ Tránh |
| ------ | ------- |
| `النص المكتوب` (chữ đã viết ra) | `النص` để trần ở title/H1/H2 |
| `نص الفيديو` (chữ của video) | `تحميل النص` không rõ của cái gì |
| `نص فيديو يوتيوب` | |
| `نصوص يوتيوب` (số nhiều, đã rõ ngữ cảnh) | |

Trong body, sau khi ngữ cảnh đã được thiết lập ở câu trước, `النص` để trần là chấp nhận được — nhưng **mọi tiêu đề (title, H1, 7 H2, conclusion h2) phải có định ngữ**.

### (b) `ترجمة` — vừa là "phụ đề" vừa là "bản dịch"

| Trường hợp | Cách viết bắt buộc |
| ---------- | ------------------ |
| Khi nhắc **phụ đề** (danh từ) | Phải neo `ملف الترجمة الموقوت` (file phụ đề khớp giờ). Chỉ được xuất hiện ở **S2 mục SRT** và **S6 câu trỏ sang trang kia**. |
| Khi nói **hành động dịch** (động từ) | Phải có tân ngữ rõ: `ترجمة النص`, `ترجمته إلى لغة أخرى`. Không để `الترجمة` đứng một mình. |

**Kết quả của trang này LUÔN gọi là `النص` / `التفريغ` — KHÔNG BAO GIỜ gọi là `ترجمة`.** Đây là ranh giới ngữ nghĩa với trang subtitle.

### (c) `تحميل` — quy tắc tân ngữ

`تحميل` chỉ được đi với `النص` / `التفريغ` / `الملف`. **KHÔNG BAO GIỜ đi với `الفيديو` / `فيديو`.**

Lý do: nhóm `تحميل فيديو يوتيوب` là intent **tải file video (mp4)**, volume khổng lồ ở thị trường Ả Rập, SERP toàn downloader video. Trang này chỉ tải **chữ**. Để lọt một chuỗi `تحميل الفيديو` là mời nhầm traffic vào rồi bounce.

Cấu trúc `تحميل نص فيديو يوتيوب` hợp lệ vì `تحميل` chi phối `نص`, còn `فيديو يوتيوب` chỉ là bổ ngữ của `نص` — đây chính là keyword chính.

---

## Lưu ý hamza (bám `/ar/video-to-text`)

- **`إلى`** (hamza đầy đủ) dùng ở **title, H1, mọi H2, conclusion h2** — vị trí trang trọng, chuẩn chính tả.
- **`الى`** (dạng rút gọn phổ biến trên web Ả Rập) rải trong **body** — bám thói quen gõ thật của người dùng, đúng biến thể họ search.
- Trang này ít dùng giới từ `إلى` hơn `/ar/video-to-text` (vì intent là "tải file" chứ không phải "chuyển đổi"), nên chỉ áp dụng ở vài chỗ có thật, **không cố nhét thêm**.

---

## Từ khóa chính

**`تحميل نص فيديو يوتيوب` (0–10)** ✅ *đã search*

Đây là cụm chuẩn nhất trong 12 cụm: có đủ 3 thành phần `تحميل` + `نص` + `فيديو يوتيوب`, và nó là **lõi chung** của cụm đuôi dài `تحميل نص فيديو يوتيوب txt`. Neo vào đây thì đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm `تحميل` (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تحميل نص فيديو يوتيوب | 0–10 | ✅ đã search *(KW chính)* |
| تحميل النص المكتوب من يوتيوب | 0–10 | ✅ đã search |
| تحميل تفريغ فيديو يوتيوب | 0–10 | ✅ đã search |
| تحميل نصوص يوتيوب | 0–10 | ✅ đã search |
| تحميل نص فيديو يوتيوب txt | 0–10 | ✅ đã search |
| تحميل ترانسكريبت يوتيوب | 0–10 | ✅ đã search — từ mượn chuyển tự |
| youtube transcript تحميل | 0–10 | ✅ đã search — trộn Latin |

### Nhóm `تنزيل` (biến thể đồng nghĩa)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تنزيل نص يوتيوب | 0–10 | ✅ đã search |
| تنزيل نص الفيديو من يوتيوب | 0–10 | ✅ đã search |
| تنزيل ترجمة فيديو يوتيوب نص | 0–10 | ⚠️ ✅ đã search — **chỉ 1 lần ở S6**, xem bảng kiểm trùng |

### Nhóm `حفظ` (lưu giữ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| حفظ نص فيديو يوتيوب | 0–10 | ✅ đã search |

### Nhóm trộn Latin

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download youtube transcript عربي | 0–10 | ✅ đã search — đặt ở S5 (mục đa ngôn ngữ) |

### Dịch bổ sung (chỉ rải body, không vào tiêu đề)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| حفظ النص على جهازك | — | 🔄 dịch bổ sung (save to device) |
| تصدير النص بصيغة PDF | — | 🔄 dịch bổ sung (export PDF) |
| تحميل التفريغ بصيغة DOCX | — | 🔄 dịch bổ sung (DOCX) |
| قراءة النص بدون إنترنت | — | 🔄 dịch bổ sung (offline) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện ở `title` / `h1` / `h2` / `description` / body. 🔄 *dịch bổ sung* = chỉ rải body.

**Tổng: 12/12 keyword đã search đều được áp dụng.**

---

## Search Intent

Người dùng Ả Rập **đã biết mình muốn nội dung chữ của video** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài extension.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline**.
- Miễn phí, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Ả Rập, kể cả video nói phương ngữ.

### Khác biệt so với bản tiếng Anh

1. **Phải chủ động nhường toàn bộ nhóm `ترجمة` cho trang subtitle.** Bản EN không có vấn đề này vì "transcript" và "subtitle" là hai từ tách bạch. Tiếng Ả Rập thì `ترجمة` bị dùng lẫn cho cả "phụ đề" lẫn "bản dịch", và nó lại là nhóm có volume mạnh nhất (100–1K). Đây là ràng buộc riêng nặng nhất của bản ar — xem khối cảnh báo đầu file.

2. **Phải dập nhiễm intent tải VIDEO.** Cụm `تحميل فيديو يوتيوب` có volume cực lớn ở thị trường Ả Rập và SERP toàn downloader mp4. Bản EN không gặp vấn đề này vì "download transcript" đã tự tách. Quy tắc cứng: mọi chỗ `تحميل` phải có tân ngữ `النص` / `التفريغ` / `الملف`.

3. **`نص` phải luôn có định ngữ ở tiêu đề.** Bản EN dùng "transcript" — một từ, một nghĩa, không cần neo. Tiếng Ả Rập `نص` mơ hồ nên mọi H2 phải mang `النص المكتوب` / `نص الفيديو` / `التفريغ`. Đây là công việc bản EN không có.

4. **Có hai biến thể động từ song song: `تحميل` và `تنزيل`.** Bản EN chỉ có một động từ "download". Bản ar phải phân bổ cả hai (7 cụm `تحميل`, 3 cụm `تنزيل`) để phủ hết truy vấn, thay vì lặp một từ.

5. **Từ mượn chuyển tự `ترانسكريبت` và cụm trộn Latin `youtube transcript`** là hiện tượng riêng của thị trường Ả Rập — người dùng kỹ thuật gõ lẫn hai bảng chữ. Bản EN không có khái niệm này. Xử lý ở FAQ, nơi giọng văn hỏi-đáp cho phép nhắc tên gọi khác mà không gãy văn phong.

6. **Nhấn PDF/DOCX mạnh hơn bản EN.** Người dùng Ả Rập (sinh viên, hành chính) thường cần bản nộp được; PDF cũng là định dạng giữ được hướng chữ RTL ổn định nhất khi gửi đi.

---

## Đối tượng người dùng

- Sinh viên, nghiên cứu sinh (lưu nội dung chữ bài giảng, phỏng vấn vào thư mục đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng / hành chính (tải DOCX làm biên bản, tài liệu nội bộ)
- Người học ngoại ngữ (tải TXT đọc offline, đối chiếu)
- Người làm nội dung cần bản nháp có timecode (SRT)
- Người cần đưa nội dung chữ vào công cụ khác yêu cầu upload file
- Người ở khu vực mạng chập chờn — cần file mở được offline

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ar.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps` ở S3, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ar) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** تحميل نص فيديو يوتيوب | تحميل نص فيديو يوتيوب *(KW chính)* |
| — | **quickAnswer** | تنزيل نص يوتيوب |
| 1 | ماذا يمنحك تحميل النص المكتوب من يوتيوب | تحميل النص المكتوب من يوتيوب, تحميل نص فيديو يوتيوب |
| 2 | أي صيغة تختار عند التحميل؟ | تحميل نص فيديو يوتيوب txt *(mục TXT)*; `ملف الترجمة الموقوت` *(mục SRT — lần duy nhất `ترجمة` xuất hiện ngoài S6)* |
| 3 | كيفية تحميل نص فيديو يوتيوب | تحميل نص فيديو يوتيوب, تنزيل نص الفيديو من يوتيوب |
| 4 | حين تحتاج الملف لا النص على الشاشة | حفظ نص فيديو يوتيوب, تحميل تفريغ فيديو يوتيوب |
| 5 | تحميل نصوص يوتيوب بأكثر من 100 لغة | تحميل نصوص يوتيوب, download youtube transcript عربي |
| 6 | متى تكون أداة أخرى أنسب | ⚠️ **تنزيل ترجمة فيديو يوتيوب نص — đúng 1 lần, trong câu trỏ sang `/ar/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | الأسئلة الشائعة | تحميل ترانسكريبت يوتيوب, youtube transcript تحميل, تحميل نص فيديو يوتيوب txt + long-tail |
| — | **conclusion** | تحميل نص فيديو يوتيوب, مجانا |

### Ghi chú riêng cho bản ar (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây cũng là chỗ duy nhất cụm `تنزيل ترجمة فيديو يوتيوب نص` được xuất hiện, và là chỗ duy nhất được phép mô tả `ملف الترجمة الموقوت` như một sản phẩm của trang khác.
- Nỗi lo nhận dạng **tiếng Ả Rập và phương ngữ** xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Ả Rập — **không thêm câu, không thêm đoạn**.
- `ترانسكريبت` (chuyển tự) dùng đúng **1 lần** ở FAQ, làm từ đồng nghĩa nhận diện. Nhiều hơn sẽ nghe lai căng, lệch giọng văn.
- Cụm trộn Latin `youtube transcript تحميل` đặt ở FAQ cùng chỗ với `ترانسكريبت` — một câu hỏi gom cả hai cách gọi, không tách thành FAQ mới.
- Xưng hô ngôi hai số ít giống đực (`أنت` ẩn, động từ `ارفع` / `الصق` / `اختر`), nhất quán với `/ar/video-to-text`.

---

## Không nên tối ưu cho các keyword

### → `/ar/youtube-subtitle-downloader` (file phụ đề khớp giờ cho editor)
`تحميل ترجمة يوتيوب` · `تحميل ترجمة فيديو يوتيوب` · `تنزيل ترجمة من يوتيوب` · `تحميل ملف ترجمة يوتيوب` · `تحميل ترجمة يوتيوب srt` · `استخراج ترجمة يوتيوب` · `موقع تحميل ترجمة يوتيوب` · `تحميل subtitle يوتيوب` · `تحميل الترجمة العربية من يوتيوب`
→ Toàn bộ nhóm `ترجمة`. Xem quy tắc "1 lần ở S6" ở trên.

### → `/ar/youtube-transcript` (đọc/copy trên màn hình, không tải file)
`تفريغ فيديو يوتيوب` · `نص فيديو يوتيوب` (không có động từ tải) · `عرض نص فيديو يوتيوب`

### → `/ar/youtube-video-summarizer` (tóm tắt)
`تلخيص فيديو يوتيوب` · `ملخص فيديو يوتيوب`

### → intent TẢI VIDEO — loại tuyệt đối
`تحميل فيديو يوتيوب` · `تنزيل فيديو من يوتيوب` · `تحميل فيديو يوتيوب mp4` · `برنامج تحميل فيديوهات يوتيوب` · `youtube downloader`
→ SERP toàn downloader mp4, volume khổng lồ, **hoàn toàn sai intent**. Quy tắc cứng: chuỗi `تحميل` + `الفيديو`/`فيديو` (tân ngữ trực tiếp) **không được xuất hiện ở bất kỳ đâu trong ar.json**.

### → `/ar/video-to-text` (upload file từ máy, không dán link)
`تحويل الفيديو الى نص` (không có chữ يوتيوب)

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/ar/youtube-transcript` — chỉ muốn đọc/copy trên màn hình, không cần file
- → `/ar/youtube-subtitle-downloader` — cần `ملف الترجمة الموقوت` cho phần mềm dựng phim. **Đây là link quan trọng nhất, cũng là chỗ neo duy nhất của cụm `تنزيل ترجمة فيديو يوتيوب نص`**
- → `/ar/youtube-video-summarizer` — chỉ cần ý chính, không cần toàn văn

---

## Ghi chú kỹ thuật cho ar.json

- `dir="rtl"`. **Số đếm dùng chữ số Latin** (100، 4) không dùng chữ số Ả Rập-Ấn (١٠٠).
- Giữ nguyên Latin: **TranscriptX, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- **YouTube → `يوتيوب`** (chuyển tự, không giữ Latin) — trừ trong keyword trộn Latin ở FAQ và trong tên internal link.
- Cấu trúc: **7 section**, **8 FAQ**. S1 `content` 3 · S2 `intro` 1 + `items` 4 · S3 `steps` 4 · S4 `intro` 1 + `items` 5 · S5 `content` 2 · S6 `content` 2 · S7 `items` 8 · conclusion `content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown `[نص الرابط](/ar/...)`, đổi path sang `/ar/...`.
- Dấu phẩy Ả Rập `،` trong danh sách; dấu chấm câu Latin `.` cuối câu (bám `/ar/video-to-text`).
- **Kiểm tra bắt buộc trước khi giao:** grep chuỗi `تحميل الفيديو` / `تحميل فيديو` / `تنزيل الفيديو` / `تنزيل فيديو` — phải trả về **0 kết quả**.
