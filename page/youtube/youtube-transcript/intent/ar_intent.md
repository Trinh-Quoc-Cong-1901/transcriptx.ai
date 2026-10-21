🔥 TranscriptX – YouTube Transcript (Arabic / ar)

URL:
/ar/youtube-transcript

Intent chính:

تفريغ فيديو يوتيوب / الحصول على نص فيديو يوتيوب أونلاين، مجانا

Trang này nhắm đến người dùng nói tiếng Ả Rập muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, chuyển sang ngôn ngữ khác hoặc xuất file. Dán URL là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này **giữ trọn họ từ `تفريغ` / `نص`**, và giữ luôn nhóm **`استخراج النص`** (extractor) + nhóm **`تحويل … الى نص`** (convert) vì mọi cụm trong danh sách `ar` đều **có chữ `يوتيوب`**, nên không đụng trang generic `/ar/video-to-text` đã hoàn thành.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ **14 keyword** trong section `## Arabic (ar)` đều thuộc về trang này.

### ⚠️ NGOẠI LỆ — nhóm `ترجمة` (phụ đề)

Nhóm `ترجمة` **thuộc trọn `/ar/youtube-subtitle-downloader`** — trang đó đã chốt và hiện gánh toàn bộ volume mạnh của nhóm này (`تحميل ترجمة يوتيوب`).

May mắn là **danh sách keyword `ar` của trang này KHÔNG có cụm `ترجمة` nào**, nên không có xung đột thực tế. Trong nội dung, `ترجمة` chỉ xuất hiện ở hai vai trò được phép (xem mục "quy tắc neo" bên dưới), và **ở S11 trong câu trỏ sang trang subtitle**.

### Ranh giới giữ TRONG NỘI DUNG

- **S11** — chứa cả **4 internal link**, là chốt phân định chính. Dịch sát, không rút gọn vế nào.
- **FAQ 10** (`نص` vs `ملف الترجمة`) — chốt với `/ar/youtube-subtitle-downloader`.
- **FAQ 4** (`إنشاء` vs `استخراج`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một URL.

---

## 🚫 LỖI DỮ LIỆU HỆ THỐNG — ĐÃ KIỂM

Đã rà toàn bộ section `## Arabic (ar)` trong `2_loc_kw.md`:

| Loại lỗi cần kiểm | Kết quả ở section `ar` |
| ----------------- | ---------------------- |
| Dòng nhãn `Keyword ideas` | ❌ **Không có** |
| Dòng nhãn `Keywords you provided` | ❌ **Không có** |
| Cụm `texttomp3` (TTS — intent NGƯỢC) | ❌ **Không có** |
| Cụm garbled / sai chính tả | ❌ **Không có** |

> ⚠️ Ba lỗi trên **có xuất hiện** ở các section `## Spanish (es)`, `## French (fr)`, `## Vietnamese (vi)` của cùng file — đây là lỗi export hệ thống. Section `ar` **sạch**.

Một dòng cần lưu ý (giữ, không loại): `youtube transcript بالعربي` (0–10) — cụm **lai Latin/Ả Rập**, là cách người dùng Ả Rập thật sự gõ khi tìm công cụ. Không phải rác. Không cấp H2 riêng (volume quá thấp), chỉ để `TranscriptX` + `يوتيوب` cùng xuất hiện tự nhiên trong body là đủ khớp.

### 📊 Số keyword thực: **14 / 14 — không loại dòng nào**

---

## 🔒 QUY TẮC NEO `نص` VÀ `ترجمة` (mục riêng — quan trọng nhất của bản ar)

### 1. `نص` PHẢI LUÔN CÓ ĐỊNH NGỮ — không bao giờ để trần

`نص` trần trong tiếng Ả Rập nghĩa quá rộng ("văn bản", "điều khoản", "bản kinh"). Bắt buộc gắn định ngữ:

| Dạng dùng | Nghĩa |
| --------- | ----- |
| `النص المكتوب` | văn bản đã viết ra (dạng dùng nhiều nhất) |
| `نص فيديو يوتيوب` / `نص الفيديو` | nội dung chữ của video |
| `الكلام المنطوق` | lời nói (khi cần nhấn nguồn là audio) |
| `التفريغ` | bản tự nó (danh từ chỉ kết quả) |

### 2. `ترجمة` — chỉ 2 vai trò được phép

`ترجمة` trong tiếng Ả Rập vừa nghĩa "dịch" vừa nghĩa "phụ đề", nên nếu dùng bừa sẽ **kéo trang này vào SERP phụ đề** và cannibalize `/ar/youtube-subtitle-downloader`.

**Được dùng:**
1. Nói về **caption có sẵn của YouTube** → luôn có định ngữ: `الترجمة المصاحبة` (caption creator thêm), `الترجمة التلقائية` (auto-caption).
2. **S11 + FAQ 10** — khi trỏ sang trang subtitle hoặc so sánh transcript vs phụ đề.

**KHÔNG được dùng:**
- **Kết quả của trang này KHÔNG BAO GIỜ gọi là `ترجمة`** — luôn là `التفريغ` / `النص المكتوب`.
- **`ترجمة` không được lên bất kỳ heading nào** (`h1`/`h2`/`h3`). Đã verify bằng script → CLEAN.

### 3. Xử lý động từ "translate" — thay bằng `نقل … الى لغة أخرى`

Bản EN có `translate` ở **H2 của S11** ("Copy, Edit, Translate or Download"). Dịch thẳng thành `الترجمة` sẽ vi phạm quy tắc (2). Giải pháp: dùng **`انقله إلى لغة أخرى`** ("chuyển nó sang ngôn ngữ khác").

- H2 S11: `انسخ النص أو عدّله أو انقله إلى لغة أخرى أو حمّله`
- Áp dụng nhất quán toàn trang: `hero.subtitle`, `quickAnswer`, S3 bước 4, S6 item 5, S8, S11, FAQ 1, FAQ 9, conclusion.

Đây là **thay đổi chủ động, không phải dịch sai** — giữ đúng nghĩa mà không đụng cụm phụ đề.

### 4. `تحميل` chỉ đi với `النص` / `التفريغ` / `الملف` — KHÔNG BAO GIỜ với `الفيديو`

`تحميل فيديو يوتيوب` là cụm khổng lồ trong tiếng Ả Rập, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ.

- S3 bước 2, EN "no file to download first" → `لا ملف تحتاج الى تحميله أولًا` (giữ `ملف`, không dùng `فيديو`).
- Verify: `grep -o 'تحميل[^.]\{0,40\}الفيديو'` → **0 kết quả**.

---

## ✍️ Lưu ý hamza (`إلى` vs `الى`)

Theo đúng tiền lệ `/ar/video-to-text/ar.json`:

- **`إلى` (hamza chuẩn)** → dùng ở `seo.title`, `seo.description`, `hero.h1`, `hero.subtitle`, **mọi `h2`** — vị trí trang trọng, được index và hiển thị.
- **`الى` (không hamza)** → rải trong body (`content`, `intro`, `items`, FAQ `a`) — đúng dạng người dùng Ả Rập gõ khi search (`تحويل فيديو يوتيوب الى نص`, `تحويل يوتيوب الى نص`, `تفريغ صوت يوتيوب الى نص` đều không hamza trong `2_loc_kw.md`).

Google khớp cả hai dạng; cách chia này vừa giữ chuẩn chính tả ở chỗ hiển thị, vừa khớp truy vấn thật ở body.

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói, طوابع زمنية tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **تفريغ / get** — lấy bản transcript,
- **مولد / generate** — dựng transcript từ audio khi video không có caption,
- **استخراج / extract** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

Kết quả trang này **luôn gọi là `التفريغ` hoặc `النص المكتوب`** — **không bao giờ** gọi là `ترجمة`.

---

## Từ khóa chính

**تفريغ فيديو يوتيوب (100 – 1K)** ✅ *đã search* → **H1**

Đây là cụm mạnh nhất trong danh sách `ar` (đồng hạng với 3 cụm khác cùng bậc 100–1K, nhưng là cụm **ngắn gọn, đúng danh từ nghiệp vụ, và đã được dùng làm anchor text trỏ về trang này từ 4 trang anh em** — xem mục Internal linking). Xuất hiện ở `seo.title`, `hero.h1`, `ogTitle`, H2 của S1, S2, S10 và FAQ 2.

---

## Từ khóa phụ

### Nhóm `تفريغ` (danh từ nghiệp vụ — trục chính, thuộc trọn trang này)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تفريغ فيديو يوتيوب | 100 – 1K | ✅ đã search *(KW chính)* |
| تفريغ يوتيوب | 10 – 100 | ✅ đã search |
| تفريغ صوت يوتيوب الى نص | 0 – 10 | ✅ đã search |

### Nhóm `تحويل … الى نص` (chuyển đổi — bắt buộc có `يوتيوب`)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| تحويل فيديو يوتيوب الى نص | 100 – 1K | ✅ đã search |
| تحويل يوتيوب الى نص | 100 – 1K | ✅ đã search |
| تحويل فيديو الى نص يوتيوب | 0 – 10 | ✅ đã search |

### Nhóm `استخراج` / `جلب` (rút chữ ra)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| استخراج النص من فيديو يوتيوب | 100 – 1K | ✅ đã search |
| استخراج ترانسكريبت يوتيوب | 0 – 10 | ✅ đã search |
| جلب النص من يوتيوب | 0 – 10 | ✅ đã search |

### Nhóm `نص` (danh từ kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| نص فيديو يوتيوب | 10 – 100 | ✅ đã search |
| كتابة نص فيديو يوتيوب | 0 – 10 | ✅ đã search |
| نسخ نص فيديو يوتيوب | 0 – 10 | ✅ đã search |

### Nhóm `مولد` (generator)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| مولد نص يوتيوب | 0 – 10 | ✅ đã search |

### Cụm lai Latin/Ả Rập

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transcript بالعربي | 0 – 10 | ✅ đã search *(không cấp H2, khớp tự nhiên qua body)* |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| فصل المتحدثين | — | 🔄 dịch bổ sung (speaker separation) |
| الطوابع الزمنية | — | 🔄 dịch bổ sung (timestamps) |
| أكثر من 100 لغة | — | 🔄 dịch bổ sung (100+ languages) |
| بدون تسجيل / مجانا | — | 🔄 dịch bổ sung (no sign-up / free) |
| الكلام المنطوق | — | 🔄 dịch bổ sung (spoken content) |
| النص الخام | — | 🔄 dịch bổ sung (raw script) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng Ả Rập muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán URL YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Chuyển sang ngôn ngữ khác — nhu cầu AR ⇄ EN rất nặng.
- Hoạt động **cả khi video không có caption** — kỳ vọng phân biệt lớn nhất, vì tỷ lệ video tiếng Ả Rập có caption thấp hơn hẳn tiếng Anh.
- Tách được ai nói câu nào (phỏng vấn, tọa đàm, khutbah, hội thảo).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Ả Rập không có một danh từ tương đương `transcript`.** Bản EN dựng toàn trang quanh một từ duy nhất. Tiếng Ả Rập phải chia thành **ba họ độc lập**: `تفريغ` (thuật ngữ nghiệp vụ, 100–1K), `تحويل … الى نص` (mô tả hành động, 100–1K ×2), `استخراج النص` (100–1K). Ba họ **volume gần ngang nhau** — không được dịch tất cả về một từ, phải cấp section riêng: `تفريغ` giữ H1 + S1 + S2 + S7 + S10, `تحويل` giữ S3, `استخراج` giữ S5.

2. **`ترجمة` là bẫy đa nghĩa không tồn tại trong tiếng Anh.** EN tách sạch `transcript` ≠ `subtitles` ≠ `translate`. Tiếng Ả Rập gộp hai nghĩa sau vào cùng một từ `ترجمة`. Đây là ràng buộc **nặng nhất** của bản ar và không có tương đương ở bản es (`transcripción` ≠ `subtítulos` ≠ `traducir` tách sạch). Hệ quả: động từ "translate" phải viết lại thành `نقل … الى لغة أخرى`, và H2 của S11 đổi cấu trúc so với EN.

3. **`نص` để trần vô nghĩa, khác hẳn `text` trong tiếng Anh.** EN có thể viết "as text" ở bất cứ đâu. Tiếng Ả Rập bắt buộc gắn định ngữ (`النص المكتوب`, `نص الفيديو`, `الكلام المنطوق`). Đây là ràng buộc ngữ pháp/ngữ nghĩa thật, không phải style.

4. **Volume tổng của tiếng Ả Rập thấp hơn nhiều so với es/en.** Cụm mạnh nhất chỉ 100–1K (es đạt 10K–100K, en đạt 1M–10M). Hệ quả chiến lược: **không có cụm nào đủ mạnh để tách trang riêng** — càng khẳng định quyết định gộp cả 3 intent (get/generate/extract) vào một URL. Tất cả 14 cụm phải dồn vào đúng trang này.

5. **`تحميل` chịu áp lực cannibalization từ nhóm tải video MP4 nặng hơn EN.** Trong tiếng Ả Rập `تحميل فيديو يوتيوب` là cụm rất lớn, SERP toàn downloader. Bản EN không chịu áp lực này ở cùng mức. Kỷ luật cứng đã nêu ở mục quy tắc neo.

6. **Hamza không nhất quán trong truy vấn thật.** 100% cụm `الى` trong danh sách keyword `ar` viết **không hamza**, trong khi chuẩn chính tả là `إلى`. Bản EN không có vấn đề tương ứng. Giải pháp chia vị trí đã nêu ở mục hamza.

7. **RTL + số Latin.** Trang phải `dir="rtl"`; số đếm giữ dạng Latin (`100`, `5`) chứ không dùng số Ả Rập-Ấn (`١٠٠`) — đúng thói quen hiển thị công cụ web và nhất quán với `/ar/video-to-text`.

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần النص الخام để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ AR ⇄ EN ⇄ FR
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `ar.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (ar) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** تفريغ فيديو يوتيوب | تفريغ فيديو يوتيوب *(KW chính)* |
| — | **quickAnswer** | تفريغ فيديو يوتيوب, تحويل فيديو يوتيوب الى نص |
| 1 | ما هو تفريغ فيديو يوتيوب؟ | تفريغ فيديو يوتيوب, نص فيديو يوتيوب, كتابة نص فيديو يوتيوب |
| 2 | تفريغ فيديو يوتيوب في نظرة سريعة *(`specs` × 10)* | تفريغ فيديو يوتيوب |
| 3 | كيفية تحويل فيديو يوتيوب إلى نص *(`steps` × 4)* | تحويل فيديو يوتيوب الى نص, تحويل فيديو الى نص يوتيوب |
| 4 | مولد نص يوتيوب | مولد نص يوتيوب, كتابة نص فيديو يوتيوب |
| 5 | استخراج النص من فيديو يوتيوب | استخراج النص من فيديو يوتيوب, استخراج ترانسكريبت يوتيوب, جلب النص من يوتيوب |
| 6 | استخدامات نص فيديو يوتيوب *(`items` × 6)* | نص فيديو يوتيوب, نسخ نص فيديو يوتيوب |
| 7 | تفريغ يوتيوب بأي لغة | تفريغ يوتيوب, تفريغ صوت يوتيوب الى نص, تحويل يوتيوب الى نص |
| 8 | TranscriptX مقابل التفريغ المدمج في يوتيوب *(`items` × 2)* | تفريغ يوتيوب *(so sánh với الترجمة التلقائية)* |
| 9 | الدقة وما الذي يؤثر فيها | *(E-E-A-T, không nhắm KW)* |
| 10 | متى قد لا ينجح تفريغ فيديو يوتيوب *(`items` × 5)* | تفريغ فيديو يوتيوب |
| 11 | انسخ النص أو عدّله أو انقله إلى لغة أخرى أو حمّله | *(4 internal link — chốt phân định)* |
| 12 | الأسئلة الشائعة *(12 FAQ)* | long-tail + toàn bộ 14 biến thể đã search |
| — | **conclusion** *(3 đoạn)* | نص فيديو يوتيوب, تفريغ فيديو يوتيوب, مجانا |

### Ghi chú riêng cho bản ar (KHÔNG tạo section mới)

- **S2 tái dùng ĐÚNG 8/10 nhãn `specs` đã duyệt ở `/ar/video-to-text/ar.json`**: `السعر`, `التسجيل`, `التثبيت`, `اللغات`, `فصل المتحدثين`, `الطوابع الزمنية`, `الأجهزة`, `صيغ التصدير` — giữ nguyên cả giá trị khi trùng (`مجانا`, `غير مطلوب`, `لا شيء — يعمل داخل المتصفّح`, `أكثر من 100، تُكتشف تلقائيًا`, `نعم — كل متحدث بعلامة خاصة`, `اختيارية — تُفعَّل أو تُطفأ لكل نص`, `متصفّحات الكمبيوتر والجهاز اللوحي والهاتف`, `TXT، DOCX، PDF، SRT، VTT`).
  Hai nhãn **mới riêng của trang này** (bản video-to-text nhận file, trang này nhận URL nên hai dòng `حد حجم الملف` / `الصيغ المقبولة` không áp dụng):
  - `المُدخل` → `رابط أي فيديو يوتيوب عام` (Input)
  - `يعمل بلا ترجمة مصاحبة` → `نعم — يُنشَأ النص من الصوت` (Works when the video has no captions)
  Nhãn thứ hai là **chỗ duy nhất `ترجمة` xuất hiện trong `specs`** — hợp lệ vì nói về caption có sẵn của YouTube, và là `label` chứ không phải heading.
- **S4 và S5 là hai section gộp intent** (generator + extractor). Dịch sát, **không gộp lại**, vì mỗi section giữ một họ keyword riêng của tiếng Ả Rập (`مولد` vs `استخراج`).
- **S8 là section so sánh** với transcript tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. Đây là nơi `الترجمة المصاحبة` / `الترجمة التلقائية` được dùng đúng vai trò.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào.
- Xưng hô **ngôi hai số ít, thể mệnh lệnh** (`الصق`, `انسخ`, `عدّله`, `صدّره`, `جهازك`) — nhất quán với `/ar/youtube-subtitle-downloader/ar.json`, `/ar/download-youtube-transcript/ar.json` và `/ar/video-to-text/ar.json`.
- Nhấn `مجانا` ở `title`, `description`, S1 đoạn cuối, FAQ 2 và `conclusion.h2` — đúng vị trí bản EN.
- Chuỗi format `TXT وDOCX وPDF وSRT وVTT` trong câu văn (dùng و nối), nhưng trong `specs.value` giữ dạng liệt kê `TXT، DOCX، PDF، SRT، VTT` — khớp `/ar/video-to-text/ar.json`.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`تحميل نص فيديو يوتيوب` / `تنزيل تفريغ يوتيوب`** → **`/ar/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`تحميل ترجمة يوتيوب` / `تنزيل ترجمة يوتيوب SRT` / `استخراج ترجمة يوتيوب`** → **`/ar/youtube-subtitle-downloader`**. **Toàn bộ nhóm `ترجمة` thuộc trọn trang đó** — đây là ngoại lệ đã chốt.
- **`تحويل فيديو يوتيوب إلى نص`**: giữ ở hub này — không còn trang riêng cho cách gọi "video sang chữ". Các cụm `تحويل … يوتيوب … الى نص` cũng giữ ở đây vì đúng intent transcript.
- **`تلخيص فيديو يوتيوب` / `ملخص فيديو يوتيوب`** → **`/ar/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`تحويل الفيديو الى نص` / `استخراج النص من الفيديو` / `تفريغ فيديو`** (KHÔNG có chữ `يوتيوب`) → **`/ar/video-to-text`** — **đã hoàn thành**. Mọi cụm dùng ở trang này **bắt buộc phải có `يوتيوب`**.
- **`تحويل الصوت الى نص` / `تفريغ صوتي`** (không có `يوتيوب`) → **`/ar/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`تحميل فيديو من يوتيوب` / `تنزيل فيديوهات يوتيوب` / `يوتيوب الى mp4`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng đã nêu ở mục quy tắc neo (4).

### Sai intent hoàn toàn

- **Mọi cụm TTS** (`تحويل النص الى كلام`, `قراءة النص بصوت`, `texttomp3`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. *(Không có trong danh sách `ar`, nhưng ghi để phòng vòng sau.)*
- **`تفعيل الترجمة في يوتيوب` / `كيف اشغل الترجمة في يوتيوب`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Anchor **tái dùng đúng anchor đã chốt ở 4 trang anh em** (grep xác nhận đã dùng thống nhất trong repo):

| Link | Anchor (ar) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/ar/download-youtube-transcript` | تحميل نص فيديو يوتيوب | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/ar/youtube-subtitle-downloader` | تحميل ترجمة يوتيوب | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/ar/youtube-video-summarizer` | تلخيص فيديو يوتيوب | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây bằng anchor **`تفريغ فيديو يوتيوب`** — đúng bằng KW chính của trang này.

---

## Ghi chú kỹ thuật cho ar.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Trang render `dir="rtl"`. **Số đếm giữ dạng Latin** (`100`, `5`, `2`) — không dùng số Ả Rập-Ấn.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`. **`YouTube` → `يوتيوب`** (khác các mục trên — đây là từ đã Ả-Rập-hóa hoàn toàn và là dạng người dùng gõ khi search).
- Khi từ Latin đứng sau و nối, viết dính không cách: `وDOCX`, `وPDF`, `وTranscriptX` — chuẩn chính tả Ả Rập, khớp các trang ar đã duyệt.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/ar/...)`, path prefix `/ar/`.
- Thuật ngữ khớp các trang ar đã duyệt: `الطوابع الزمنية` (timestamps), `فصل المتحدثين` (speaker separation), `الملف` (file), `الرابط` (link), `المتصفّح` (browser), `بدون تسجيل` (no sign-up), `تُكتشف تلقائيًا` (auto-detected), `عام` (public).
- `hero.placeholder` giữ đúng chuỗi đã dùng ở 2 trang YouTube anh em: `الصق رابط فيديو يوتيوب...`. `hero.button` ngắn: `احصل على النص`.
- **Kiểm tra bắt buộc trước khi bàn giao — ĐÃ CHẠY, ĐỀU PASS:**
  1. `python3 shape_check.py en.json ar.json` → `ar.json -> True` ✅
  2. `grep -o 'تحميل[^.]\{0,40\}الفيديو' ar.json` → **0 kết quả** ✅
  3. `ترجمة` trên `h1`/`h2`/`h3` bất kỳ → **CLEAN (0)** ✅
  4. `grep -c 'texttomp3'` → **0** ✅
  5. 4 path internal link đúng prefix `/ar/`, đủ 4, không thừa không thiếu ✅
