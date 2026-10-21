🔥 TranscriptX – YouTube Subtitle Downloader (Arabic / ar)

URL:
/ar/youtube-subtitle-downloader

Intent chính:

تحميل ترجمة يوتيوب — tải **file phụ đề khớp giờ** (SRT · VTT) của video YouTube, miễn phí

Trang này nhắm đến người dùng Ả Rập muốn **tải file phụ đề có timecode** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại video kèm phụ đề, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu tiếp cận (accessibility).

---

## 🚨 CỤM YOUTUBE 5 TRANG — TRANG NÀY LÀ BÊN **NHẬN** KEYWORD

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột trực tiếp với `/ar/download-youtube-transcript`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ (không phải theo volume):**

> **`ترجمة` mang nghĩa phụ đề khớp giờ cho editor → TRANG NÀY**
> **`نص` / `تفريغ` (tài liệu để đọc / lưu / nộp) → `/ar/download-youtube-transcript`**

Căn cứ: bản EN section 1 đoạn 2 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Trang này ĐƯỢC NHẬN toàn bộ nhóm `ترجمة`

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `تحميل ترجمة يوتيوب` | **100 – 1K** | Cụm mạnh nhất của cả cụm YouTube tiếng Ả Rập. **Trang này lấy làm H1.** |
| `تحميل ترجمة فيديو يوتيوب` | **100 – 1K** | Đồng hạng. Trang kia đã chủ động nhường. |
| `موقع تحميل ترجمة يوتيوب` | 10 – 100 | Trang kia không dùng |
| 9 cụm còn lại của nhóm `ترجمة` | 0 – 10 | Trang kia liệt kê ở mục "Không nên tối ưu" |

### ⚠️ TOÀN BỘ SỨC MẠNH CỦA CỤM YOUTUBE TIẾNG Ả RẬP NẰM Ở TRANG NÀY

Sau khi nhường nhóm `ترجمة` cho trang này, bản `ar` của `/ar/download-youtube-transcript` **không còn cụm nào ≥ 100 volume** — cả 12 keyword của trang đó đều ở mức 0–10 (đọc `../download-youtube-transcript/intent/ar_intent.md`, mục "Hệ quả").

Nghĩa là: **trang này gánh 100% volume có thật của cụm YouTube tiếng Ả Rập** — 2 cụm ở mức 100–1K + 1 cụm ở mức 10–100. Đây là trang duy nhất trong cụm 5 trang bản `ar` có cơ hội xếp hạng thật. **Đầu tư kỹ, không cắt bớt, không viết qua loa.**

Chiều ngược lại: trang này **tuyệt đối không được lấn** nhóm `نص` / `تفريغ`. Hai từ đó chỉ xuất hiện ở:
- Section 1 đoạn 2 (câu định nghĩa ranh giới)
- Section 6 (câu trỏ sang trang kia)
- FAQ 5 (câu hỏi "phụ đề khác gì bản chép lời")

---

## ⚠️ MỤC RIÊNG: QUY TẮC NEO NGHĨA KÉP CỦA `ترجمة`

Đây là ràng buộc ngôn ngữ nặng nhất của bản `ar`. `ترجمة` mang **hai nghĩa cùng lúc**:

| Nghĩa | Tiếng Việt | Vai trò ở trang này |
| ----- | ---------- | ------------------- |
| (a) **phụ đề** (danh từ, vật thể) | file phụ đề khớp giờ | **Trục chính của trang.** Là kết quả người dùng tải về. |
| (b) **bản dịch / hành động dịch** (danh động từ) | dịch sang ngôn ngữ khác | Chỉ là **một use-case** ở section 4 và section 5. |

Vấn đề: **section 5 nói về việc DỊCH phụ đề**, nên hai nghĩa đứng sát nhau trong cùng một trang. Nếu để `الترجمة` trần trụi, người đọc (và Google) không biết đang nói phụ đề hay bản dịch.

### Quy tắc neo bắt buộc

| Nghĩa | Cách viết bắt buộc | Ví dụ dùng trong `ar.json` |
| ----- | ------------------ | -------------------------- |
| **(a) phụ đề** | Phải kèm **danh từ chỉ vật**: `ملف الترجمة` · `سطور الترجمة` · `الترجمة الموقوتة` · `ملف ترجمة موقوت` | `ملف الترجمة ليس مجرد الكلمات…` · `سطور الترجمة` (S2, S4, S5, FAQ) |
| **(b) hành động dịch** | Phải có **tân ngữ rõ ràng**: `ترجمة النص إلى لغة أخرى` · `ترجمة السطور الى لغة أخرى` · `يترجمه` | S3 bước 4 · S4 item 3 · FAQ 6 |

**Kiểm tra khi review:** mọi lần `الترجمة` xuất hiện, hỏi "đây là vật hay hành động?" — nếu là vật mà không có `ملف` / `سطور` / `الموقوتة` đi kèm và ngữ cảnh câu trước chưa neo rõ, phải sửa.

### `تحميل` — quy tắc tân ngữ

`تحميل` / `تنزيل` chỉ được đi với `الترجمة` / `ملف الترجمة` / `SRT` / `VTT`. **KHÔNG BAO GIỜ đi với `الفيديو` / `فيديو`.**

Lý do: nhóm `تحميل فيديو يوتيوب` là intent **tải file video mp4**, volume khổng lồ ở thị trường Ả Rập, SERP toàn downloader. Trang này tải **file phụ đề**. Để lọt một chuỗi `تحميل الفيديو` là mời nhầm traffic rồi bounce.

Cấu trúc `تحميل ترجمة فيديو يوتيوب` **hợp lệ** vì `تحميل` chi phối `ترجمة`, còn `فيديو يوتيوب` chỉ là bổ ngữ của `ترجمة` — đây chính là keyword đồng hạng 100–1K.

---

## Lưu ý hamza (bám `/ar/download-youtube-transcript` và `/ar/video-to-text`)

- **`إلى`** (hamza đầy đủ) dùng ở **title, H1, mọi H2, h3, conclusion h2** — vị trí trang trọng, chuẩn chính tả.
- **`الى`** (dạng rút gọn phổ biến trên web Ả Rập) rải trong **body** — bám thói quen gõ thật của người dùng.
- Trang này dùng `إلى` / `الى` khá nhiều vì section 4 và 5 đều nói về **dịch sang ngôn ngữ khác** — đúng chỗ để phân bổ tự nhiên, không cần cố nhét.

---

## Từ khóa chính

**`تحميل ترجمة يوتيوب` (100 – 1K)** ✅ *đã search*

Cụm mạnh nhất và chuẩn nhất: đủ `تحميل` + `ترجمة` + `يوتيوب`, và là **lõi chung** của các đuôi dài `تحميل ترجمة يوتيوب srt`, `موقع تحميل ترجمة يوتيوب`, `تحميل ملف ترجمة يوتيوب`. Neo vào đây thì đuôi dài tự phủ theo.

## Từ khóa đồng hạng

**`تحميل ترجمة فيديو يوتيوب` (100 – 1K)** ✅ *đã search* — đặt ở `quickAnswer` (biến thể câu hỏi) và S4 item 2.

---

## Từ khóa phụ

### Nhóm `تحميل` (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تحميل ترجمة يوتيوب | 100 – 1K | ✅ đã search *(KW chính)* |
| تحميل ترجمة فيديو يوتيوب | 100 – 1K | ✅ đã search *(đồng hạng)* |
| موقع تحميل ترجمة يوتيوب | 10 – 100 | ✅ đã search |
| تحميل ملف ترجمة يوتيوب | 0 – 10 | ✅ đã search |
| تحميل ترجمة يوتيوب srt | 0 – 10 | ✅ đã search |
| تحميل الترجمة العربية من يوتيوب | 0 – 10 | ✅ đã search |

### Nhóm `تنزيل` (biến thể đồng nghĩa)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تنزيل ترجمة من يوتيوب | 0 – 10 | ✅ đã search |
| تنزيل ملف الترجمة من يوتيوب | 0 – 10 | ✅ đã search |
| تنزيل ترجمة فيديو يوتيوب srt | 0 – 10 | ✅ đã search |

### Nhóm `استخراج` (trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| استخراج ترجمة يوتيوب | 0 – 10 | ✅ đã search — cấp hẳn nửa sau H2 section 1 |

### Nhóm trộn Latin

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تحميل subtitle يوتيوب | 0 – 10 | ✅ đã search — đặt ở FAQ 1 |
| youtube تحميل ترجمة | 0 – 10 | ✅ đã search — đặt ở FAQ 8 |

### Dịch bổ sung (chỉ rải body, không vào tiêu đề)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| الطوابع الزمنية | — | 🔄 dịch bổ sung (timestamps) |
| ملف الترجمة الموقوت | — | 🔄 dịch bổ sung (timed subtitle file) |
| تعديل ملف الترجمة | — | 🔄 dịch bổ sung (edit subtitle file) |
| برنامج المونتاج | — | 🔄 dịch bổ sung (video editor) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện ở `title` / `h1` / `h2` / `description` / body. 🔄 *dịch bổ sung* = chỉ rải body.

**Tổng: 12/12 keyword đã search đều được áp dụng.**

---

## Search Intent

Người dùng Ả Rập **cần file phụ đề để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn phụ đề vào bản dựng.
- Đăng lại video lên kênh mình kèm phụ đề mà không phải gõ lại.
- Dịch phụ đề sang tiếng Ả Rập (hoặc từ Ả Rập sang ngôn ngữ khác) rồi gắn lại — nhu cầu rất lớn ở thị trường này.
- Sửa phụ đề tự động của YouTube vốn hay sai với tiếng Ả Rập.
- Đáp ứng yêu cầu tiếp cận cho người khiếm thính.

Họ kỳ vọng: dán link là ra file, chọn được SRT hay VTT, có timecode từng dòng, mở sửa được bằng text editor, miễn phí, không cài extension.

### Khác biệt so với bản tiếng Anh

1. **`ترجمة` mang nghĩa kép "phụ đề" + "bản dịch", bản EN không có vấn đề này.** Tiếng Anh tách bạch `subtitle` và `translation`. Tiếng Ả Rập gộp làm một, mà section 5 của trang lại nói đúng về việc dịch. Phải neo nghĩa bằng danh từ chỉ vật / tân ngữ ở từng chỗ — xem mục quy tắc riêng ở trên. Đây là ràng buộc bản EN hoàn toàn không có.

2. **Trang này là bên NHẬN keyword, và nhận toàn bộ volume của cụm.** Bản EN không có vấn đề phân chia vì `transcript` và `subtitle` tách bạch tự nhiên. Bản `ar` thì nhóm `ترجمة` bị kéo về cả hai trang, và sau khi phân chia, trang đối xứng không còn cụm nào ≥ 100. Nghĩa là bản `ar` của trang này quan trọng hơn bản EN của nó rất nhiều trong nội bộ cụm.

3. **Phải dập nhiễm intent tải VIDEO.** Cụm `تحميل فيديو يوتيوب` có volume cực lớn ở thị trường Ả Rập và SERP toàn downloader mp4. Bản EN không gặp vấn đề này vì "download subtitles" đã tự tách. Quy tắc cứng: mọi chỗ `تحميل` / `تنزيل` phải có tân ngữ `الترجمة` / `ملف الترجمة` / `SRT` / `VTT`.

4. **Không có cặp đồng nghĩa `subtitles` / `captions` để chống lặp.** Bản EN xen kẽ hai từ này suốt trang. Tiếng Ả Rập chỉ có `ترجمة`. Phải chống lặp bằng cách đổi cấu trúc câu và luân phiên `ملف الترجمة` / `سطور الترجمة` / `الترجمة الموقوتة`.

5. **Hai biến thể động từ song song: `تحميل` và `تنزيل`.** Bản EN chỉ có một động từ "download". Bản `ar` phải phân bổ cả hai (6 cụm `تحميل`, 3 cụm `تنزيل`) để phủ hết truy vấn thay vì lặp một từ.

6. **Nhu cầu phụ đề tiếng Ả Rập được nhấn mạnh hơn.** Cụm `تحميل الترجمة العربية من يوتيوب` cho thấy người dùng lo nhận dạng tiếng Ả Rập (fusha vs phương ngữ). Xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.

---

## Đối tượng người dùng

- Editor video, freelancer dựng phim (nạp SRT vào Premiere / Final Cut / Resolve)
- Người re-upload / tổng hợp video lên kênh riêng
- Người làm phụ đề (subteam) dịch nội dung nước ngoài sang tiếng Ả Rập
- Marketer chạy nội dung đa ngôn ngữ cho thị trường MENA
- Người làm nội dung cho người khiếm thính (yêu cầu accessibility)
- Người muốn sửa phụ đề tự động sai của YouTube với tiếng Ả Rập
- Người học ngoại ngữ cần file phụ đề khớp giờ để đối chiếu

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ar.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2 (khác trang download-transcript vốn có 4), đúng 4 `steps` ở S3, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ar) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** تحميل ترجمة يوتيوب | تحميل ترجمة يوتيوب *(KW chính)* |
| — | **quickAnswer** | تحميل ترجمة فيديو يوتيوب *(đồng hạng)* |
| 1 | ما هو ملف الترجمة فعلًا — وما الذي يمنحك إياه استخراج ترجمة يوتيوب | استخراج ترجمة يوتيوب, تحميل ملف ترجمة يوتيوب |
| 2 | SRT أم VTT: أي صيغة ترجمة تحمّل؟ | تحميل ترجمة يوتيوب srt |
| 3 | كيفية تحميل ترجمة يوتيوب | تحميل ترجمة يوتيوب, تنزيل ملف الترجمة من يوتيوب |
| 4 | ماذا تفعل بملف الترجمة بعد تحميله | تحميل ترجمة فيديو يوتيوب |
| 5 | تحميل الترجمة بأكثر من 100 لغة | تحميل الترجمة العربية من يوتيوب |
| 6 | ترجمة موقوتة أم نص مكتوب أم ملخّص؟ | *(3 internal link — chốt phân định)* |
| 7 | الأسئلة الشائعة | موقع تحميل ترجمة يوتيوب, تنزيل ترجمة من يوتيوب, تحميل subtitle يوتيوب, تنزيل ترجمة فيديو يوتيوب srt, youtube تحميل ترجمة |
| — | **conclusion** | تحميل ترجمة يوتيوب, مجانا |

### Ghi chú riêng cho bản ar (KHÔNG tạo section mới)

- **Section 1 đoạn 2 là câu chống cannibalization mạnh nhất trang.** Dịch sát bản EN, không rút gọn: `النص المكتوب كلام تقرأه وحده قائمًا بذاته؛ أمّا ملف الترجمة فنصّ مبني ليجري بمحاذاة الفيديو، مضبوطًا على الكلام إطارًا بإطار.` Đây là chỗ duy nhất ngoài S6 và FAQ 5 được nhắc `النص المكتوب`.
- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Nhãn link phải khớp H1 thật của trang đích: `تفريغ فيديو يوتيوب`, `تحميل نص فيديو يوتيوب`, `تلخيص فيديو يوتيوب`.
- Nỗi lo nhận dạng **tiếng Ả Rập và phương ngữ** xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu, không thêm đoạn.
- Hai cụm trộn Latin (`تحميل subtitle يوتيوب`, `youtube تحميل ترجمة`) đặt ở **FAQ 1 và FAQ 8**, mỗi chỗ một cụm, nhét vào câu có sẵn — **không tạo FAQ mới, không thêm câu**.
- Xưng hô ngôi hai số ít giống đực (`أنت` ẩn, động từ `الصق` / `اختر` / `حمّل`), nhất quán với `/ar/download-youtube-transcript` và `/ar/video-to-text`.

---

## Không nên tối ưu cho các keyword

### → `/ar/download-youtube-transcript` (tài liệu chữ để đọc / lưu / nộp)
`تحميل نص فيديو يوتيوب` · `تحميل النص المكتوب من يوتيوب` · `تحميل تفريغ فيديو يوتيوب` · `تحميل نصوص يوتيوب` · `تحميل نص فيديو يوتيوب txt` · `تحميل ترانسكريبت يوتيوب` · `تنزيل نص يوتيوب` · `حفظ نص فيديو يوتيوب`
→ Toàn bộ nhóm `نص` / `تفريغ`. Chỉ được nhắc ở S1 đoạn 2, S6, và FAQ 5.

### → `/ar/youtube-transcript` (đọc / copy trên màn hình, không tải file)
`تفريغ فيديو يوتيوب` · `عرض نص فيديو يوتيوب` · `قراءة نص فيديو يوتيوب`

### → `/ar/youtube-video-summarizer` (tóm tắt)
`تلخيص فيديو يوتيوب` · `ملخص فيديو يوتيوب`

### → intent TẢI VIDEO — loại tuyệt đối
`تحميل فيديو يوتيوب` · `تنزيل فيديو من يوتيوب` · `تحميل فيديو يوتيوب mp4` · `برنامج تحميل فيديوهات يوتيوب` · `تحميل فيديو يوتيوب مع الترجمة` · `youtube downloader`
→ SERP toàn downloader mp4, volume khổng lồ, **hoàn toàn sai intent**. Quy tắc cứng: chuỗi `تحميل`/`تنزيل` + `الفيديو`/`فيديو` (tân ngữ trực tiếp) **không được xuất hiện ở bất kỳ đâu trong ar.json**.

### → hướng dẫn bật phụ đề trong app, không phải công cụ tải
`تشغيل الترجمة في يوتيوب` · `تفعيل الترجمة التلقائية يوتيوب` · `إعدادات الترجمة يوتيوب`
→ Người dùng chỉ muốn bật CC trong app YouTube, không muốn tải file gì cả. Sai intent hoàn toàn.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/ar/youtube-transcript` — chỉ muốn đọc chữ thuần trên màn hình, không timecode, không tải file
- → `/ar/download-youtube-transcript` — muốn lưu chữ thành TXT / DOCX / PDF. **Đây là trang đối xứng, link quan trọng nhất**
- → `/ar/youtube-video-summarizer` — chỉ cần ý chính, không cần từng dòng

---

## Ghi chú kỹ thuật cho ar.json

- `dir="rtl"`. **Số đếm dùng chữ số Latin** (100، 00:01:12) không dùng chữ số Ả Rập-Ấn (١٠٠).
- Giữ nguyên Latin: **TranscriptX, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, SubRip, WebVTT**.
- **YouTube → `يوتيوب`** · **Instagram → `انستقرام`** · **TikTok → `تيك توك`** (chuyển tự, không giữ Latin) — trừ trong 2 keyword trộn Latin ở FAQ.
- Cấu trúc: **7 section**, **8 FAQ**. S1 `content` 3 · S2 `intro` 1 + `items` **2** · S3 `steps` 4 · S4 `intro` 1 + `items` 5 · S5 `content` 2 · S6 `content` 2 · S7 `items` 8 · conclusion `content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown `[نص الرابط](/ar/...)`, path `/ar/...`.
- Dấu phẩy Ả Rập `،` trong danh sách; dấu chấm câu Latin `.` cuối câu (bám `/ar/download-youtube-transcript`).
- **Kiểm tra bắt buộc trước khi giao:**
  1. `python3 shape_check.py en.json ar.json` → phải in `ar.json -> True`
  2. grep chuỗi `تحميل الفيديو` / `تحميل فيديو` / `تنزيل الفيديو` / `تنزيل فيديو` — phải trả về **0 kết quả**
  3. Rà từng lần xuất hiện `الترجمة`: nghĩa "vật" phải có `ملف`/`سطور`/`الموقوتة` neo; nghĩa "hành động" phải có tân ngữ
