🔥 TranscriptX – Download YouTube Transcript (Hindi / hi)

URL:
/hi/download-youtube-transcript

Intent chính:

यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें — फ्री (TXT, DOCX, PDF, SRT)

Trang này nhắm đến người dùng Ấn Độ muốn **tải bản transcript của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcript trên màn hình (`/hi/youtube-transcript`).

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/hi/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **`सबटाइटल` (file phụ đề khớp giờ cho phần mềm dựng phim) → `/hi/youtube-subtitle-downloader`**
> **`ट्रांसक्रिप्ट` / `टेक्स्ट` (tài liệu để đọc / lưu / nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 tự định nghĩa ranh giới — *"if what you really need is a timed caption file for a video editor rather than a document, the YouTube Subtitle Downloader exports SRT and VTT instead"*.

### Kết quả kiểm trùng chéo với `../youtube-subtitle-downloader/2_loc_kw.md` (section `## Hindi (hi)`)

Danh sách hi của trang kia có 7 keyword, **toàn bộ đều xoay quanh `subtitle` / `सबटाइटल` / `srt`**:

| Keyword trang kia | Hệ chữ |
| ----------------- | ------ |
| youtube se subtitle kaise download kare | Hinglish |
| youtube ki subtitle download kare | Hinglish |
| youtube subtitle download kaise kare | Hinglish |
| youtube subtitle download karne wala app | Hinglish |
| यूट्यूब सबटाइटल डाउनलोड कैसे करें | Devanagari |
| यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें | Devanagari |
| यूट्यूब से srt फाइल कैसे डाउनलोड करें | Devanagari |

**Số cụm trùng: 1**

| Cụm trùng | Volume | Thuộc về | Xử lý ở trang này |
| --------- | ------ | -------- | ----------------- |
| `यूट्यूब सबटाइटल डाउनलोड करें` | 0–10 | ⚠️ **`/hi/youtube-subtitle-downloader`** (gần như trùng khít với `यूट्यूब सबटाइटल डाउनलोड कैसे करें` của trang kia) | **Neo đẩy đi** — đúng **1 lần** ở **S6 đoạn 2**, ngay trong câu trỏ sang trang kia |

7 cụm còn lại của trang này **không trùng một chữ nào** với trang kia — vì trang này dùng `ट्रांसक्रिप्ट` / `टेक्स्ट`, trang kia dùng `सबटाइटल` / `srt`. Ranh giới ở bản `hi` **sạch hơn hẳn bản `vi`** (bản vi mất cụm mạnh nhất `tải phụ đề youtube` 100–1K; bản hi chỉ nhường 1 cụm 0–10).

### Quy tắc dùng từ `सबटाइटल` trong trang này

Kết quả của trang này **luôn gọi là `ट्रांसक्रिप्ट` hoặc `टेक्स्ट`**. Chỉ có **đúng 2 chỗ** được nhắc `सबटाइटल`, và cả hai đều phải **neo**:

1. **S2 mục SRT** → `टाइमकोड वाली सबटाइटल फ़ाइल` (không bao giờ để `सबटाइटल` đứng trần)
2. **S6 đoạn 2** → trong câu trỏ sang `/hi/youtube-subtitle-downloader`, cũng neo bằng `टाइमकोड वाली सबटाइटल फ़ाइल`

**Tuyệt đối không đặt `सबटाइटल` vào `title` / `h1` / bất kỳ `h2` nào.**

---

## ⚠️ MỤC RIÊNG — CHIẾN LƯỢC HINGLISH vs DEVANAGARI

Section `## Hindi (hi)` trong `2_loc_kw.md` của trang này **chỉ có 8 keyword** — mỏng (bản `de` có 11, bản `it`/`ja`/`tr` có 12). Nhưng điểm quan trọng hơn số lượng: **danh sách trộn CẢ HAI hệ chữ**, và **toàn bộ 8 cụm đều ở mức 0–10**.

### Dữ liệu thực tế của trang này

| Dạng | Số lượng | Keyword |
| ---- | -------- | ------- |
| **Hinglish (chữ Latin)** | **5** | `youtube transcript kaise download kare`, `youtube ka transcript download`, `youtube video ka text download kaise kare`, `youtube transcript save kaise kare`, `youtube video transcript nikale` |
| **Devanagari (chữ Hindi thật)** | **3** | `यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें`, `यूट्यूब वीडियो का टेक्स्ट कैसे निकाले`, `यूट्यूब सबटाइटल डाउनलोड करें` |

**Trong 3 cụm Devanagari, 1 cụm (`यूट्यूब सबटाइटल डाउनलोड करें`) phải nhường trang khác → chỉ còn 2 slot Devanagari dùng được ở tầng hiển thị.**

### So sánh với các trang `hi` đã làm

- `/hi/facebook-transcript`: **0** keyword Devanagari → không một keyword đã search nào lọt được vào H1/H2.
- `/hi/video-to-text`: **2** keyword Devanagari dùng được → đặt nguyên văn vào `title`+`h1` và `quickAnswer`+`H2 S3`.
- `/hi/instagram-caption-downloader`: **3** keyword Devanagari.
- **Trang này: 3 cụm Devanagari, 2 dùng được** → **cùng nhóm với `/hi/video-to-text`**, áp dụng lại **y hệt chiến lược 2 tầng đã chốt ở trang đó**.

### Chiến lược đã chốt — hai tầng (khớp `/hi/video-to-text`)

1. **Tầng hiển thị** (`seo.title`, `seo.ogTitle`, `hero.*`, `quickAnswer`, mọi `h2`/`h3`, toàn bộ body, FAQ, conclusion): **Devanagari 100%**.
   - 2 cụm Devanagari dùng được đặt **nguyên văn** (chuỗi con liền mạch, không chèn từ vào giữa) ở vị trí trọng số cao nhất.
   - Tên riêng và định dạng giữ Latin.
2. **Tầng meta** (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn **nguyên văn cả 5 chuỗi Hinglish**. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin ở đó không phá nhịp đọc, mà vẫn cho Google khớp lexical đúng cách người Ấn thực sự gõ.
3. **TUYỆT ĐỐI không chèn Hinglish thô** vào `title` / `ogTitle` / `h1` / `h2` / `h3` / body / FAQ / conclusion. Một H1 nửa Latin nửa Devanagari trông như trang spam.

> ⚠️ **Khác `/hi/video-to-text` ở một điểm:** ở trang đó cụm Hinglish mạnh nhất đạt 100–1K, cao hơn hẳn phần còn lại, nên việc "hy sinh" nó xuống tầng meta là một đánh đổi thật. **Ở trang này cả 8 cụm đều 0–10** — không cụm nào mạnh hơn cụm nào, nên việc chia hai tầng **không mất gì cả**. Chiến lược này ở đây là thuần lợi.

### Ghi chú riêng về từ `यूट्यूब` vs `YouTube`

Quy tắc chung của repo là giữ Latin `YouTube`. Nhưng **cả 2 cụm Devanagari dùng được đều mở đầu bằng `यूट्यूब`** — đây là 2 slot khớp lexical duy nhất của cả trang, không được phá.

**Quy ước đã chốt:**
- Viết **`यूट्यूब`** (Devanagari) ở **các slot chứa keyword đã search**: `seo.title`, `seo.ogTitle`, `hero.h1`, `quickAnswer.question`, `h2` S1/S3/S5, `conclusion.h2`, FAQ 1.
- Viết **`YouTube`** (Latin) trong **body prose** và trong **nhãn 3 internal link** (đó là tên sản phẩm: YouTube Transcript, YouTube Subtitle Downloader, YouTube Video Summarizer).

Đây chính là đánh đổi `/hi/video-to-text` đã làm (`[YouTube ट्रांसक्रिप्ट](/hi/youtube-transcript)`), và là cách viết bình thường trên web tiếng Hindi — cả hai dạng đều phổ biến, Google khớp được cả hai.

---

## ⚠️ QUY TẮC `डाउनलोड` — NHÓM NHIỄM NGUY HIỂM NHẤT

Ở Ấn Độ nhóm `youtube video download` / `यूट्यूब वीडियो डाउनलोड` có **volume khổng lồ**, gấp hàng nghìn lần mọi keyword của trang này, và SERP hoàn toàn là công cụ tải video MP4. Tiếng Hindi dùng chung đúng một từ `डाउनलोड` cho cả hai intent nên rủi ro cao hơn hẳn bản `de`/`fr`/`vi`.

**QUY TẮC BẮT BUỘC:** `डाउनलोड` **phải luôn** đi kèm tân ngữ `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`.
**KHÔNG BAO GIỜ** viết `वीडियो डाउनलोड करें` — kể cả trong FAQ, S1 hay conclusion.

Chỗ nguy hiểm nhất là **S1 đoạn 3** của bản EN (*"The video itself stays on YouTube"*) — câu này có `video` đứng gần `download`. Bản dịch phải tách hẳn: `वीडियो खुद YouTube पर ही रहता है` và cụm `डाउनलोड` không được xuất hiện trong cùng mệnh đề đó.

---

## Từ khóa chính

**यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें** (0–10) ✅ *đã search, **Devanagari***

→ `quickAnswer.question` (nguyên văn + `?`) và **H2 section 3** (nguyên văn 100%).
→ Dạng rút gọn `यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें` (chuỗi con liền mạch `यूट्यूब ट्रांसक्रिप्ट डाउनलोड`) → `seo.title`, `seo.ogTitle`, `hero.h1`.

Đây là cụm duy nhất chứa đủ cả 3 thành phần intent của trang: `यूट्यूब` + `ट्रांसक्रिप्ट` + `डाउनलोड`.

## Từ khóa chính ở tầng meta

**youtube transcript kaise download kare** (0–10) ✅ *đã search, **Hinglish*** → `seo.description` (đặt sớm trong câu).

Đây là **cùng một truy vấn viết bằng hai hệ chữ** với từ khóa chính ở trên — nên phủ được cả hai phía người dùng Ấn Độ (gõ Devanagari và gõ Latin).

---

## Từ khóa phụ

### Nhóm Devanagari — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng hiển thị 🇮🇳

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें | 0–10 | ✅ đã search — **Devanagari** *(KW chính)* → `quickAnswer.question`, **H2 S3** (nguyên văn); chuỗi con → `seo.title`, `seo.ogTitle`, `hero.h1`, `conclusion.h2` |
| यूट्यूब वीडियो का टेक्स्ट कैसे निकाले | 0–10 | ✅ đã search — **Devanagari** → **FAQ 1** (nguyên văn), S1 body (nguyên văn); chuỗi con `यूट्यूब वीडियो का टेक्स्ट` → **H2 S1** |
| यूट्यूब सबटाइटल डाउनलोड करें | 0–10 | ⚠️ **thuộc `/hi/youtube-subtitle-downloader`** — đúng **1 lần** ở **S6 đoạn 2**, trong câu trỏ đi, neo bằng `टाइमकोड वाली सबटाइटल फ़ाइल`. **KHÔNG** vào title/h1/h2 |

### Nhóm Hinglish — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng meta 🔤

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transcript kaise download kare | 0–10 | ✅ đã search — **Hinglish** → `seo.description` *(KW chính tầng meta, đặt đầu chuỗi)* |
| youtube ka transcript download | 0–10 | ✅ đã search — **Hinglish** → `seo.description` |
| youtube video ka text download kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| youtube transcript save kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| youtube video transcript nikale | 0–10 | ✅ đã search — **Hinglish** → `seo.schemaDescription` |

### Dịch bổ sung (chỉ rải body, KHÔNG đặt vào title/H1)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| यूट्यूब ट्रांसक्रिप्ट डाउनलोड फ्री | — | 🔄 dịch bổ sung (free download) |
| यूट्यूब ट्रांसक्रिप्ट TXT में डाउनलोड करें | — | 🔄 dịch bổ sung (TXT) |
| यूट्यूब ट्रांसक्रिप्ट PDF में डाउनलोड करें | — | 🔄 dịch bổ sung (PDF) |
| यूट्यूब ट्रांसक्रिप्ट DOCX में डाउनलोड करें | — | 🔄 dịch bổ sung (DOCX) |
| यूट्यूब ट्रांसक्रिप्ट सेव करें | — | 🔄 dịch bổ sung (save transcript) |
| यूट्यूब वीडियो का ट्रांसक्रिप्ट फ़ाइल में सेव करें | — | 🔄 dịch bổ sung (save as file) |
| ऑफ़लाइन पढ़ने के लिए ट्रांसक्रिप्ट डाउनलोड करें | — | 🔄 dịch bổ sung (offline) |
| टाइमस्टैम्प के साथ ट्रांसक्रिप्ट डाउनलोड करें | — | 🔄 dịch bổ sung (timestamps) |
| यूट्यूब ट्रांसक्रिप्ट डाउनलोडर | — | 🔄 dịch bổ sung (downloader) |
| लंबे वीडियो का ट्रांसक्रिप्ट डाउनलोड करें | — | 🔄 dịch bổ sung (long video) |

### Tỉ lệ

- **Đã search: 8 keyword** — trong đó **7 dùng được ở trang này** (2 Devanagari tầng hiển thị + 5 Hinglish tầng meta), **1 nhường trang khác**.
- **Dịch bổ sung: 10 cụm.**
- **Đã search / tổng số cụm dùng trên trang = 7 / 17 ≈ 41%. Dịch bổ sung ≈ 59%.**
- Trong đó **chỉ 2 cụm đã search dùng được ở tầng hiển thị** (H1/H2/quickAnswer/FAQ) — giống hệt tình huống `/hi/video-to-text`.

**Nguyên tắc dùng:**
✅ *đã search, Devanagari* = ưu tiên tuyệt đối, đặt **nguyên văn** vào `title`/`h1`/`quickAnswer`/`h2`/FAQ.
✅ *đã search, Hinglish* = đặt **nguyên văn** vào `seo.description`/`ogDescription`/`schemaDescription`, **không** vào body.
🔄 *dịch bổ sung* = chỉ rải trong body.

> ⚠️ **Toàn bộ 8 cụm đều 0–10.** Không cố nhồi mật độ — chiến lược là **phủ đều 7 cụm dùng được**, mỗi cụm một vị trí neo, và **dịch phần còn lại thật tự nhiên** bằng thuật ngữ Hindi thông dụng nhất trên web.

---

## Search Intent

Người dùng Ấn Độ **đã biết mình muốn transcript** và đang ở bước tiếp theo: lấy nó thành **file trên máy hoặc trên điện thoại**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, **không đăng nhập, không cài extension/app**.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline** (rất quan trọng ở Ấn Độ — dữ liệu di động chập chờn, tàu/xe).
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — phần lớn người dùng Ấn Độ vào web bằng mobile, file phải lưu được vào bộ nhớ máy.
- Không giới hạn độ dài video (bài giảng coaching class 2–3 tiếng là chuyện thường).
- Nhận dạng tốt **tiếng Hindi** và tiếng Anh giọng Ấn.

### Khác biệt so với bản tiếng Anh

1. **Keyword tồn tại ở HAI hệ chữ cùng lúc — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ, mọi keyword đặt tự do vào bất kỳ đâu. Bản `hi`: 5 keyword Latin (Hinglish) + 3 Devanagari, bắt buộc tách hai tầng hiển thị/meta. Đây là quyết định biên tập không tồn tại ở bản EN hay bất kỳ ngôn ngữ châu Âu nào của trang này.
2. **Nhóm `वीडियो डाउनलोड` là mìn — bản EN không có rủi ro này.** Trong SERP tiếng Anh, "download the transcript" và "download the video" là hai cụm rõ ràng khác nhau. Ở Ấn Độ chỉ có **một** từ `डाउनलोड`, và nhóm tải video MP4 có volume gấp hàng nghìn lần. `डाउनलोड` đứng gần `वीडियो` sẽ kéo trang lệch hẳn sang page type khác. Xem mục riêng ở trên.
3. **Phải chủ động nhường cụm `सबटाइटल` cho trang anh em.** Bản EN không gặp vì "transcript" và "subtitle" tách bạch tự nhiên. Bản `hi` có hẳn một keyword đã search (`यूट्यूब सबटाइटल डाउनलोड करें`) thuộc trang khác — xử lý bằng neo đẩy đi ở S6.
4. **Dữ liệu mỏng hơn hẳn — 8 keyword đều 0–10, so với bản EN có 5 cụm đều 10K–100K.** Bản EN có thể lái H2 theo keyword; bản `hi` phải **bám sát bản dịch tự nhiên của EN** và chỉ áp keyword bằng cách chọn từ khi dịch.
5. **`फ्री / मुफ़्त` phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần `फ्री` xuất hiện ở `title`, `description`, `hero.subtitle`, FAQ và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
6. **Mobile-first + offline nặng hơn.** Bản EN nhắc "your computer's downloads folder or your phone's storage" như thông tin phụ; bản `hi` để `फ़ोन` và `ऑफ़लाइन` xuất hiện tự nhiên và sớm hơn — nhưng **không thêm câu mới**, chỉ đảo trọng số từ ngữ trong các câu đã có.

---

## Đối tượng người dùng

- Sinh viên, học viên luyện thi (lưu transcript bài giảng coaching class vào thư mục môn học, đọc offline)
- Nghiên cứu sinh (lưu transcript phỏng vấn, tọa đàm, phim tài liệu vào kho tư liệu đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ hoặc chuyển private)
- Nhân viên văn phòng (tải DOCX để làm tài liệu, biên bản nội bộ)
- Giáo viên, người làm khóa học online (transcript → giáo trình, handout in ra)
- Blogger / content creator Ấn Độ (transcript video → bài viết)
- Người học ngoại ngữ (tải TXT đọc offline trên tàu, trên xe)
- Người cần đưa transcript vào công cụ khác yêu cầu **upload file** chứ không nhận text dán vào

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **7 section**, cùng số đoạn `content`, S2 = `intro` 1 + `items` **4**, S3 = `steps` **4**, S4 = `intro` 1 + `items` **5**, S5 = `content` **2**, S6 = `content` **2**, S7 = **8 FAQ**, `conclusion` = h2 + **2 đoạn**. **Trang này KHÔNG có `specs`.** Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें | **यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें ✅ (Devanagari, chuỗi con `यूट्यूब ट्रांसक्रिप्ट डाउनलोड`)** |
| — | **quickAnswer** | **यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें? ✅ (Devanagari, nguyên văn + `?`)** |
| 1 | यूट्यूब वीडियो का टेक्स्ट डाउनलोड करने से आपको क्या मिलता है | **यूट्यूब वीडियो का टेक्स्ट कैसे निकाले ✅** (nguyên văn trong body; chuỗi con `यूट्यूब वीडियो का टेक्स्ट` ở H2), यूट्यूब ट्रांसक्रिप्ट सेव करें 🔄 · ⚠️ đoạn 3 = chỗ nguy hiểm nhất của quy tắc `डाउनलोड` |
| 2 | आपको कौन-सा फ़ॉर्मैट डाउनलोड करना चाहिए? | ...TXT/PDF/DOCX में डाउनलोड करें 🔄 · ⚠️ mục SRT phải neo `टाइमकोड वाली सबटाइटल फ़ाइल` |
| 3 | **यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें** | **यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें ✅ (Devanagari, NGUYÊN VĂN 100% ở H2)**, टाइमस्टैम्प के साथ ट्रांसक्रिप्ट डाउनलोड करें 🔄 |
| 4 | जब आपको सिर्फ़ टेक्स्ट नहीं, पूरी फ़ाइल चाहिए | यूट्यूब वीडियो का ट्रांसक्रिप्ट फ़ाइल में सेव करें 🔄, ऑफ़लाइन पढ़ने के लिए ट्रांसक्रिप्ट डाउनलोड करें 🔄 |
| 5 | 100 से ज़्यादा भाषाओं में यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें | यूट्यूब ट्रांसक्रिप्ट डाउनलोड फ्री 🔄 *(+ đổi ví dụ ngôn ngữ sang có tiếng Hindi)* |
| 6 | जब कोई दूसरा टूल ज़्यादा सही बैठता है | ⚠️ **यूट्यूब सबटाइटल डाउनलोड करें — đúng 1 lần, trong câu trỏ sang `/hi/youtube-subtitle-downloader`, neo bằng `टाइमकोड वाली सबटाइटल फ़ाइल`** + 2 link còn lại |
| 7 | अक्सर पूछे जाने वाले सवाल | **यूट्यूब वीडियो का टेक्स्ट कैसे निकाले ✅ (FAQ 1, nguyên văn)**, यूट्यूब ट्रांसक्रिप्ट डाउनलोड फ्री 🔄, ...TXT/DOCX/PDF 🔄, लंबे वीडियो का ट्रांसक्रिप्ट डाउनलोड करें 🔄 |
| — | **conclusion** | **यूट्यूब ट्रांसक्रिप्ट डाउनलोड ✅ (chuỗi con)**, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **5 chuỗi Hinglish nằm HOÀN TOÀN ở tầng meta, không một chuỗi nào trong `hero`/`sections`/`conclusion`:**
  - `seo.description` → `youtube transcript kaise download kare` *(đặt đầu chuỗi)* + `youtube ka transcript download`
  - `seo.ogDescription` → `youtube video ka text download kaise kare` + `youtube transcript save kaise kare`
  - `seo.schemaDescription` → `youtube video transcript nikale`
- **2 cụm Devanagari dùng được đặt NGUYÊN VĂN, không sửa một chữ, không chèn từ vào giữa chuỗi:**
  - `यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें` → `quickAnswer.question` (thêm `?`) **và** `sections[2].h2` (nguyên văn 100%). Ở `seo.title`/`ogTitle`/`hero.h1`/`conclusion.h2` dùng dạng `यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें` — bỏ `कैसे`, chuỗi con `यूट्यूब ट्रांसक्रिप्ट डाउनलोड` vẫn liền mạch. H1 là câu lệnh hành động nên không được mang `कैसे` (đó là dạng câu hỏi, thuộc quickAnswer và H2 S3).
  - `यूट्यूब वीडियो का टेक्स्ट कैसे निकाले` → **FAQ 1** nguyên văn (+ vế `और डाउनलोड करें?`) **và** `sections[0].content[0]` nguyên văn. `sections[0].h2` chỉ mang chuỗi con `यूट्यूब वीडियो का टेक्स्ट` — cố tình **không** đưa `कैसे निकाले` lên H2 S1, vì S1 là section lợi ích còn S3 mới là section hướng dẫn; để hai H2 cùng mang `कैसे` sẽ trùng chủ đề và làm loãng H2 S3.
- **S2 mục SRT** và **S6 đoạn 2** là **hai chỗ duy nhất** từ `सबटाइटल` được xuất hiện, cả hai đều neo `टाइमकोड वाली सबटाइटल फ़ाइल`.
- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp. Đây cũng là chỗ duy nhất cụm `यूट्यूब सबटाइटल डाउनलोड करें` được xuất hiện.
- Nỗi lo nhận dạng **tiếng Hindi** xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Hindi — **không thêm câu**.
- Mobile-first (`फ़ोन`) và `ऑफ़लाइन` đảo lên sớm hơn trong S4 và FAQ 5 — **không thêm câu**, chỉ đổi trọng số từ ngữ trong các câu đã có.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- **`यूट्यूब सबटाइटल डाउनलोड करें` / `यूट्यूब सबटाइटल डाउनलोड कैसे करें` / `यूट्यूब से srt फाइल कैसे डाउनलोड करें` / `youtube subtitle download kaise kare`** → **/hi/youtube-subtitle-downloader** (file phụ đề khớp giờ cho phần mềm dựng phim). Xem quy tắc **1 lần ở S6** phía trên.
- `यूट्यूब ट्रांसक्रिप्ट` / `youtube ka transcript kaise dekhe` / `यूट्यूब ट्रांसक्रिप्ट पढ़ें` → **/hi/youtube-transcript** (đọc + copy trên màn hình, **không** tải file).
- `यूट्यूब वीडियो का सारांश` / `यूट्यूब वीडियो समरी` / `youtube video summary hindi` → **/hi/youtube-video-summarizer**.
- `वीडियो को टेक्स्ट में बदलें` / `video se text kaise nikale` (không có chữ YouTube) → **/hi/video-to-text** (upload file từ máy, không dán link).
- ⚠️ **NHÓM NHIỄM NGUY HIỂM NHẤT — tải VIDEO:** `youtube video download` / `यूट्यूब वीडियो डाउनलोड` / `यूट्यूब वीडियो डाउनलोडर` / `youtube se video kaise download kare` / `mp4 download` / `youtube video download karne wala app`.
  - **Volume khổng lồ ở Ấn Độ**, SERP hoàn toàn là công cụ tải video. Kéo vào sẽ làm lệch page type ngay lập tức.
  - **QUY TẮC BẮT BUỘC:** `डाउनलोड` chỉ đi với `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`. **KHÔNG BAO GIỜ** `वीडियो डाउनलोड`.
- `यूट्यूब से MP3 डाउनलोड` / `यूट्यूब ऑडियो डाउनलोड` → intent tải **âm thanh**, không phải chữ.
- `यूट्यूब पर सबटाइटल कैसे लगाएँ` / `यूट्यूब सबटाइटल ऑन करें` → hướng dẫn **thao tác trong YouTube / YouTube Studio**, không phải công cụ.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → **/hi/youtube-transcript** — khi chỉ muốn đọc/copy trên màn hình, không cần lưu file nào cả
- → **/hi/youtube-subtitle-downloader** — khi cần **`टाइमकोड वाली सबटाइटल फ़ाइल`** cho phần mềm dựng phim (SRT/VTT) chứ không phải một tài liệu để đọc. **Đây là link quan trọng nhất, cũng là chỗ neo duy nhất của cụm `यूट्यूब सबटाइटल डाउनलोड करें`**
- → **/hi/youtube-video-summarizer** — khi toàn văn là nhiều hơn mức cần, chỉ cần ý chính

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Cấu trúc JSON khớp **100%** với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **7 sections**, `conclusion` h2 + 2 đoạn. **KHÔNG có `specs`.**
  - S1 `content` **3** | S2 `intro` 1 + `items` **4** | S3 `steps` **4** | S4 `intro` 1 + `items` **5** | S5 `content` **2** | S6 `content` **2** | S7 `items` **8**
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
  - Ngoại lệ có chủ đích: **`यूट्यूब`** viết Devanagari ở các slot chứa keyword đã search (title, ogTitle, h1, quickAnswer.question, h2 S1/S3/S5, conclusion.h2, FAQ 1) — xem mục "Ghi chú riêng về từ `यूट्यूब` vs `YouTube`" phía trên.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: ट्रांसक्रिप्ट, टेक्स्ट, फ़ाइल, डाउनलोड, फ़ॉर्मैट, एक्सपोर्ट, ब्राउज़र, स्पीकर, टाइमस्टैम्प, टाइमकोड, सबटाइटल, कैप्शन, लिंक, वीडियो, ऑफ़लाइन, डिवाइस, फ़ोन.
- Số đếm dùng chữ số Latin (100+, 4) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **`आप`** xuyên suốt, **không** dùng `तू`/`तुम` — nhất quán tuyệt đối với `/hi/video-to-text`, `/hi/audio-to-text`, `/hi/instagram-caption-downloader`.
- **Nukta (़) dùng nhất quán:** फ़ाइल, फ़ॉर्मैट, ज़्यादा, सिर्फ़, ज़रूरत, आवाज़, फ़ोन, ऑफ़लाइन, फ़ोल्डर, ख़ुद.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle`, `hero.*` và mọi `h2`/`h3` **không** chứa Hinglish thô.
- Internal link `sections[5].content[1]` giữ nguyên cú pháp markdown, đổi path sang `/hi/youtube-transcript`, `/hi/youtube-subtitle-downloader`, `/hi/youtube-video-summarizer`.
- **Tuyệt đối không để chuỗi `वीडियो डाउनलोड` xuất hiện ở bất kỳ đâu trong file.**
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** Hindi văn chương nặng (पाठ, अभिलेख, प्रतिलिपि) và **tránh** dịch máy word-by-word.
