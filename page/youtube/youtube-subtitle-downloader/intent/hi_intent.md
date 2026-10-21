🔥 TranscriptX – YouTube Subtitle Downloader (Hindi / hi)

URL:
/hi/youtube-subtitle-downloader

Intent chính:

यूट्यूब सबटाइटल डाउनलोड करें — SRT · VTT, फ्री

Trang này nhắm đến người dùng Ấn Độ muốn **tải file phụ đề có timecode** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại kèm phụ đề, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu tiếp cận.

---

## 🚨 CỤM YOUTUBE 5 TRANG — TRANG NÀY LÀ BÊN **NHẬN** KEYWORD

Repo có 5 trang YouTube dễ ăn thịt nhau. Quy tắc phân chia đã chốt từ khi làm `/hi/download-youtube-transcript`, phân **theo ngữ nghĩa từ**:

> **`सबटाइटल` (file phụ đề khớp giờ cho phần mềm dựng phim) → TRANG NÀY**
> **`ट्रांसक्रिप्ट` / `टेक्स्ट` (tài liệu để đọc / lưu / nộp) → `/hi/download-youtube-transcript`**

Căn cứ: bản EN section 1 đoạn 2 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Trang này ĐƯỢC NHẬN 1 cụm từ `/hi/download-youtube-transcript`

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `यूट्यूब सबटाइटल डाउनलोड करें` | 0–10 | Nằm trong danh sách `hi` của trang đối xứng, nhưng mang chữ `सबटाइटल` → thuộc trang này. Trang kia đã **nhường**, chỉ dùng đúng **1 lần** ở S6 đoạn 2 trong câu trỏ sang đây, neo bằng `टाइमकोड वाली सबटाइटल फ़ाइल`. **Trang này lấy nguyên văn làm `hero.h1`.** |

Đây là cụm Devanagari **duy nhất trong toàn cụm 5 trang** trùng khít với dạng câu lệnh hành động của H1 trang này — không được để trang khác giữ.

Ngược lại, trang này **không lấy** một chữ nào từ nhóm `ट्रांसक्रिप्ट` / `टेक्स्ट` của trang kia. Ranh giới bản `hi` **sạch tuyệt đối**: 7/7 keyword của trang này đều xoay quanh `subtitle` / `सबटाइटल` / `srt`, không cụm nào chứa `transcript`/`ट्रांसक्रिप्ट`.

### Quy tắc dùng từ `ट्रांसक्रिप्ट` trong trang này

Kết quả của trang này **luôn gọi là `सबटाइटल`** (hoặc `सबटाइटल फ़ाइल`). Chỉ có **đúng 3 chỗ** được nhắc `ट्रांसक्रिप्ट`, cả ba đều là chỗ phân định chủ động:

1. **S1 đoạn 2** — câu định nghĩa ranh giới của bản EN (`ट्रांसक्रिप्ट` = chữ để đọc, `सबटाइटल फ़ाइल` = chữ chạy đè lên video)
2. **S6 `h2`** — `सबटाइटल, ट्रांसक्रिप्ट या समरी — आपको क्या चाहिए?` (chốt phân định). Trong body S6, hai trang anh em gọi bằng **nhãn link Latin** (`YouTube Transcript`, `Download YouTube Transcript`) vì đó là tên sản phẩm — không đếm là dùng từ `ट्रांसक्रिप्ट` Devanagari.
3. **FAQ 5** — "सबटाइटल और ट्रांसक्रिप्ट में क्या फ़र्क़ है?"

Tổng số lần `ट्रांसक्रिप्ट` xuất hiện trong `hi.json` = **6**, phân bố: S1 = 2, S6 h2 = 1, FAQ 5 = 3. **`hero` = 0, `seo` = 0, `conclusion` = 0.**

**Tuyệt đối không đặt `ट्रांसक्रिप्ट` vào `title` / `ogTitle` / `h1` / bất kỳ `h2` nào / `conclusion`.**

---

## ⚠️ MỤC RIÊNG — CHIẾN LƯỢC HINGLISH vs DEVANAGARI (theo dữ liệu thực tế của trang này)

Section `## Hindi (hi)` trong `2_loc_kw.md` của trang này **chỉ có 7 keyword** — mỏng nhất trong các ngôn ngữ của trang (`ja`/`ko` có 10, `it`/`es` có 9–10). Và **toàn bộ 7 cụm đều ở mức 0–10**.

### Dữ liệu thực tế — danh sách trộn CẢ HAI hệ chữ

| Dạng | Số lượng | Keyword |
| ---- | -------- | ------- |
| **Hinglish (chữ Latin)** | **4** | `youtube se subtitle kaise download kare`, `youtube ki subtitle download kare`, `youtube subtitle download kaise kare`, `youtube subtitle download karne wala app` |
| **Devanagari (chữ Hindi thật)** | **3** | `यूट्यूब सबटाइटल डाउनलोड कैसे करें`, `यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें`, `यूट्यूब से srt फाइल कैसे डाउनलोड करें` |

**Có cụm Devanagari thật, không phải toàn Hinglish** — đây là điều kiện đủ để chạy chiến lược 2 tầng. Cộng thêm **1 cụm Devanagari nhận từ trang đối xứng** (`यूट्यूब सबटाइटल डाउनलोड करें`) → **4 slot Devanagari dùng được ở tầng hiển thị**.

### So sánh với các trang `hi` đã làm

- `/hi/facebook-transcript`: **0** keyword Devanagari → không keyword đã search nào lọt được vào H1/H2.
- `/hi/video-to-text`: **2** Devanagari dùng được.
- `/hi/download-youtube-transcript` (trang đối xứng): **3** Devanagari, **2 dùng được** (1 nhường trang này).
- `/hi/instagram-caption-downloader`: **3** Devanagari.
- **Trang này: 3 Devanagari của mình + 1 nhận về = 4 dùng được** → **nhiều slot Devanagari nhất trong cả cụm YouTube bản `hi`**. Chiến lược 2 tầng chạy được ở mức đầy đủ nhất.

### Chiến lược đã chốt — hai tầng (khớp `/hi/download-youtube-transcript` và `/hi/video-to-text`)

1. **Tầng hiển thị** (`seo.title`, `seo.ogTitle`, `hero.*`, `quickAnswer`, mọi `h2`/`h3`, toàn bộ body, FAQ, conclusion): **Devanagari 100%**.
   - 4 cụm Devanagari đặt **nguyên văn** (chuỗi con liền mạch, không chèn từ vào giữa) ở vị trí trọng số cao nhất.
   - Tên riêng và định dạng giữ Latin.
2. **Tầng meta** (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn **nguyên văn cả 4 chuỗi Hinglish**. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin ở đó không phá nhịp đọc, mà vẫn cho Google khớp lexical đúng cách người Ấn thực sự gõ.
3. **TUYỆT ĐỐI không chèn Hinglish thô** vào `title` / `ogTitle` / `h1` / `h2` / `h3` / body / FAQ / conclusion. Một H1 nửa Latin nửa Devanagari trông như trang spam.

> ⚠️ **Cả 7 cụm đều 0–10** — không cụm nào mạnh hơn cụm nào, nên việc chia hai tầng **không hy sinh gì cả**. Khác `/hi/video-to-text` (nơi cụm Hinglish mạnh nhất đạt 100–1K và việc đẩy nó xuống meta là đánh đổi thật). Ở trang này chiến lược 2 tầng là **thuần lợi**.

### ⚠️ Ngoại lệ nukta có chủ đích — `फाइल` vs `फ़ाइल`

Keyword đã search `यूट्यूब से srt फाइल कैसे डाउनलोड करें` viết `फाइल` **không nukta**, trong khi quy ước repo (`/hi/download-youtube-transcript`, `/hi/video-to-text`) là `फ़ाइल` **có nukta**.

**Chốt:** giữ `फ़ाइल` có nukta **ở toàn bộ file**, trừ **đúng 1 chỗ** — `sections[1].items[0].content` (mục SRT), nơi đặt keyword **nguyên văn** để khớp lexical. Chữ `srt` trong keyword viết hoa thành `SRT` theo quy ước Latin của repo (tìm kiếm không phân biệt hoa thường nên không mất khớp).

### Ghi chú riêng về từ `यूट्यूब` vs `YouTube`

Quy tắc chung của repo là giữ Latin `YouTube`. Nhưng **cả 4 cụm Devanagari dùng được đều mở đầu bằng `यूट्यूब`**.

**Quy ước đã chốt (giống trang đối xứng):**
- Viết **`यूट्यूब`** (Devanagari) ở **các slot chứa keyword đã search**: `seo.title`, `seo.ogTitle`, `hero.h1`, `quickAnswer.question`, `h2` S3/S5, `conclusion.h2`, FAQ 1, FAQ 2.
- Viết **`YouTube`** (Latin) trong **body prose**, `hero.placeholder`, và trong **nhãn 3 internal link** (đó là tên sản phẩm).

---

## ⚠️ QUY TẮC `डाउनलोड` — NHÓM NHIỄM NGUY HIỂM NHẤT

Ở Ấn Độ nhóm `youtube video download` / `यूट्यूब वीडियो डाउनलोड` có **volume khổng lồ**, gấp hàng nghìn lần mọi keyword của trang này, và SERP hoàn toàn là công cụ tải video MP4. Tiếng Hindi dùng chung đúng một từ `डाउनलोड` cho cả hai intent.

**QUY TẮC BẮT BUỘC:** `डाउनलोड` **phải luôn** đi kèm tân ngữ `सबटाइटल` / `फ़ाइल` / `SRT` / `VTT`.
**KHÔNG BAO GIỜ** viết `वीडियो डाउनलोड करें` — kể cả trong FAQ, S1 hay conclusion.

Chỗ nguy hiểm nhất là **S1 đoạn 3** (`generates that timed file from the audio of a YouTube video and lets you download it`) — có `वीडियो` đứng gần `डाउनलोड`. Bản dịch tách hẳn: tân ngữ của `डाउनलोड` phải là `वह फ़ाइल`, không được để `वीडियो` làm tân ngữ gần nhất.

Rủi ro thứ hai riêng của trang này: **S4 mục "Re-upload a video with captions"**. Ở đó động từ phải là `अपलोड`, tuyệt đối không được xuất hiện `डाउनलोड` trong cùng câu với `वीडियो`.

---

## Từ khóa chính

**यूट्यूब सबटाइटल डाउनलोड कैसे करें** (0–10) ✅ *đã search, **Devanagari***

→ `quickAnswer.question` (nguyên văn + `?`) và **H2 section 3** (nguyên văn 100%).
→ Dạng câu lệnh `यूट्यूब सबटाइटल डाउनलोड करें` (cụm nhận từ trang đối xứng, cũng là chuỗi con `यूट्यूब सबटाइटल डाउनलोड` liền mạch) → `seo.title`, `seo.ogTitle`, `hero.h1`, `conclusion.h2`.

Đây là cụm duy nhất chứa đủ cả 3 thành phần intent của trang: `यूट्यूब` + `सबटाइटल` + `डाउनलोड`.

## Từ khóa chính ở tầng meta

**youtube se subtitle kaise download kare** (0–10) ✅ *đã search, **Hinglish*** → `seo.description` (đặt đầu chuỗi).

Đây là **cùng một truy vấn viết bằng hai hệ chữ** với từ khóa chính ở trên — phủ được cả hai phía người dùng Ấn Độ (gõ Devanagari và gõ Latin).

---

## Từ khóa phụ

### Nhóm Devanagari — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng hiển thị 🇮🇳

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| यूट्यूब सबटाइटल डाउनलोड कैसे करें | 0–10 | ✅ đã search — **Devanagari** *(KW chính)* → `quickAnswer.question`, **H2 S3** (nguyên văn); chuỗi con → `seo.title`, `seo.ogTitle` |
| यूट्यूब सबटाइटल डाउनलोड करें | 0–10 | ✅ đã search — **Devanagari**, **nhận từ `/hi/download-youtube-transcript`** → `hero.h1` (nguyên văn), `conclusion.h2` (nguyên văn), FAQ 2 |
| यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें | 0–10 | ✅ đã search — **Devanagari** → **FAQ 1** (nguyên văn) và `sections[0].content[2]` (nguyên văn) |
| यूट्यूब से srt फाइल कैसे डाउनलोड करें | 0–10 | ✅ đã search — **Devanagari** → `sections[1].items[0].content` (mục SRT, nguyên văn — xem ngoại lệ nukta ở trên) |

### Nhóm Hinglish — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng meta 🔤

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube se subtitle kaise download kare | 0–10 | ✅ đã search — **Hinglish** → `seo.description` *(KW chính tầng meta, đặt đầu chuỗi)* |
| youtube subtitle download kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.description` |
| youtube ki subtitle download kare | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| youtube subtitle download karne wala app | 0–10 | ✅ đã search — **Hinglish** → `seo.schemaDescription` |

### Dịch bổ sung (chỉ rải body, KHÔNG đặt vào title/H1)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| सबटाइटल फ़ाइल डाउनलोड करें | — | 🔄 dịch bổ sung (subtitle file) |
| यूट्यूब कैप्शन डाउनलोड करें | — | 🔄 dịch bổ sung (captions downloader) |
| यूट्यूब SRT डाउनलोड | — | 🔄 dịch bổ sung (SRT) |
| यूट्यूब VTT डाउनलोड | — | 🔄 dịch bổ sung (VTT) |
| टाइमकोड वाली सबटाइटल फ़ाइल | — | 🔄 dịch bổ sung (timed caption file) |
| सबटाइटल फ़ाइल एडिट करें | — | 🔄 dịch bổ sung (edit subtitle file) |
| सबटाइटल का अनुवाद करें | — | 🔄 dịch bổ sung (translate subtitles) |
| हिंदी सबटाइटल डाउनलोड करें | — | 🔄 dịch bổ sung (Hindi subtitles) |
| सबटाइटल फ्री में डाउनलोड करें | — | 🔄 dịch bổ sung (free) |
| वीडियो एडिटर के लिए सबटाइटल | — | 🔄 dịch bổ sung (for video editor) |
| सबटाइटल डाउनलोडर | — | 🔄 dịch bổ sung (downloader) |

### Tỉ lệ

- **Đã search: 7 keyword của trang này + 1 nhận từ trang đối xứng = 8 cụm dùng được** (4 Devanagari tầng hiển thị + 4 Hinglish tầng meta). **Không nhường cụm nào đi.**
- **Dịch bổ sung: 11 cụm.**
- **Đã search / tổng số cụm dùng trên trang = 8 / 19 ≈ 42%. Dịch bổ sung ≈ 58%.**
- Trong đó **4 cụm đã search dùng được ở tầng hiển thị** (H1/H2/quickAnswer/FAQ/S2) — **cao hơn `/hi/download-youtube-transcript` (2) và `/hi/video-to-text` (2)**.

**Nguyên tắc dùng:**
✅ *đã search, Devanagari* = ưu tiên tuyệt đối, đặt **nguyên văn** vào `title`/`h1`/`quickAnswer`/`h2`/FAQ.
✅ *đã search, Hinglish* = đặt **nguyên văn** vào `seo.description`/`ogDescription`/`schemaDescription`, **không** vào body.
🔄 *dịch bổ sung* = chỉ rải trong body.

> ⚠️ **Toàn bộ 7 cụm đều 0–10.** Không cố nhồi mật độ — chiến lược là **phủ đều 8 cụm dùng được**, mỗi cụm một vị trí neo, và **dịch phần còn lại thật tự nhiên** bằng thuật ngữ Hindi thông dụng nhất trên web.

---

## Search Intent

Người dùng Ấn Độ **cần file phụ đề để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn phụ đề vào bản dựng.
- Đăng lại video lên kênh mình kèm phụ đề mà không phải gõ lại.
- Dịch phụ đề sang tiếng Hindi hoặc ngôn ngữ khác rồi gắn lại — thị trường nội dung đa ngôn ngữ Ấn Độ rất lớn.
- Sửa phụ đề tự động của YouTube vốn hay sai tên riêng.
- Đáp ứng yêu cầu tiếp cận cho người khiếm thính.

Họ kỳ vọng: dán link là ra file, chọn được SRT hay VTT, có timecode từng dòng, mở sửa được, **miễn phí** (độ nhạy giá rất cao), **không cài app/extension** — điểm này quan trọng vì có hẳn keyword `youtube subtitle download karne wala app`, tức người dùng đang tìm app và trang web không-cần-cài là lợi thế bán hàng trực tiếp.

### Khác biệt so với bản tiếng Anh

1. **Keyword tồn tại ở HAI hệ chữ cùng lúc — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ. Bản `hi`: 4 keyword Latin (Hinglish) + 3 Devanagari, bắt buộc tách hai tầng hiển thị/meta.
2. **Nhóm `वीडियो डाउनलोड` là mìn — bản EN không có rủi ro này.** Trong SERP tiếng Anh, "download subtitles" và "download the video" tách bạch. Ở Ấn Độ chỉ có **một** từ `डाउनलोड`, nhóm tải video MP4 volume gấp hàng nghìn lần. Xem mục riêng ở trên.
3. **Dữ liệu mỏng hơn hẳn — 7 cụm đều 0–10, so với bản EN có 15 cụm đều 10K–100K.** Bản EN lái H2 theo keyword thoải mái; bản `hi` phải **bám sát bản dịch tự nhiên của EN**, chỉ áp keyword bằng cách chọn từ khi dịch.
4. **`सबटाइटल` là trục gần như duy nhất.** Bản EN xen kẽ `subtitles` / `captions` để đỡ lặp. Tiếng Hindi có `कैप्शन` nhưng dùng ít hơn hẳn — chống lặp chủ yếu bằng `सबटाइटल फ़ाइल` / `सबटाइटल की लाइन` / `टाइमकोड` xen kẽ, `कैप्शन` chỉ dùng thưa.
5. **`फ्री / मुफ़्त` phải nặng hơn "free" của bản EN.** Cần xuất hiện ở `title`, `description`, `hero.subtitle`, FAQ 2 và `conclusion` — thị trường Ấn Độ cực nhạy giá.
6. **"Không cần cài app" phải nổi hơn bản EN.** Bản EN nhắc "no install" như thuộc tính phụ; bản `hi` có keyword tìm app nên `कुछ इंस्टॉल करने की ज़रूरत नहीं` / `कोई ऐप नहीं` đưa lên sớm trong `hero.subtitle` — **không thêm câu**, chỉ đảo trọng số từ.
7. **Nỗi lo nhận dạng tiếng Hindi** xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.

---

## Đối tượng người dùng

- Editor video, freelancer dựng phim Ấn Độ (nạp SRT vào Premiere/Final Cut/Resolve)
- YouTuber / người re-upload, tổng hợp video lên kênh riêng
- Người làm phụ đề (subteam), dịch sub Hindi ⇄ Anh
- Marketer chạy nội dung đa ngôn ngữ cho thị trường đa ngữ Ấn Độ
- Giáo viên, người làm khóa học online cần phụ đề cho bài giảng
- Người làm nội dung cho người khiếm thính
- Người muốn sửa phụ đề tự động sai của YouTube
- Người đang tìm "app tải sub" nhưng không muốn cài gì

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **7 section**, S1 `content` **3**, S2 = `intro` 1 + `items` **2** (khác trang download-transcript vốn có 4), S3 = `steps` **4**, S4 = `intro` 1 + `items` **5**, S5 = `content` **2**, S6 = `content` **2**, S7 = **8 FAQ**, `conclusion` = h2 + **2 đoạn**. **Trang này KHÔNG có `specs`.** Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** यूट्यूब सबटाइटल डाउनलोड करें | **यूट्यूब सबटाइटल डाउनलोड करें ✅ (Devanagari, nguyên văn — cụm nhận từ trang đối xứng)** |
| — | **quickAnswer** | **यूट्यूब सबटाइटल डाउनलोड कैसे करें? ✅ (Devanagari, nguyên văn + `?`)** |
| 1 | सबटाइटल फ़ाइल असल में होती क्या है | **यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें ✅** (nguyên văn ở `content[2]`), टाइमकोड वाली सबटाइटल फ़ाइल 🔄 · ⚠️ **đoạn 2 = câu chống cannibalization mạnh nhất trang**, đoạn 3 = chỗ nguy hiểm nhất của quy tắc `डाउनलोड` |
| 2 | SRT या VTT — कौन-सा सबटाइटल फ़ॉर्मैट डाउनलोड करें | **यूट्यूब से srt फाइल कैसे डाउनलोड करें ✅** (nguyên văn ở `items[0].content`), यूट्यूब VTT डाउनलोड 🔄 |
| 3 | **यूट्यूब सबटाइटल डाउनलोड कैसे करें** | **यूट्यूब सबटाइटल डाउनलोड कैसे करें ✅ (Devanagari, NGUYÊN VĂN 100% ở H2)**, सबटाइटल फ़ाइल डाउनलोड करें 🔄 |
| 4 | डाउनलोड की हुई सबटाइटल फ़ाइल से आप क्या कर सकते हैं | वीडियो एडिटर के लिए सबटाइटल 🔄, सबटाइटल का अनुवाद करें 🔄, सबटाइटल फ़ाइल एडिट करें 🔄 · ⚠️ mục re-upload chỉ được dùng `अपलोड` |
| 5 | 100 से ज़्यादा भाषाओं में यूट्यूब सबटाइटल डाउनलोड करें | हिंदी सबटाइटल डाउनलोड करें 🔄, सबटाइटल का अनुवाद करें 🔄 *(+ đổi ví dụ ngôn ngữ sang có tiếng Hindi)* |
| 6 | सबटाइटल, ट्रांसक्रिप्ट या समरी — आपको क्या चाहिए? | *(3 internal link — **chốt phân định**, dịch sát cả 3 vế)* |
| 7 | अक्सर पूछे जाने वाले सवाल | **यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें ✅ (FAQ 1, nguyên văn)**, **यूट्यूब सबटाइटल डाउनलोड ✅ (FAQ 2)**, सबटाइटल फ्री में डाउनलोड करें 🔄, सबटाइटल डाउनलोडर 🔄 |
| — | **conclusion** | **यूट्यूब सबटाइटल डाउनलोड करें ✅ (nguyên văn)**, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **4 chuỗi Hinglish nằm HOÀN TOÀN ở tầng meta, không một chuỗi nào trong `hero`/`sections`/`conclusion`:**
  - `seo.description` → `youtube se subtitle kaise download kare` *(đặt đầu chuỗi)* + `youtube subtitle download kaise kare`
  - `seo.ogDescription` → `youtube ki subtitle download kare`
  - `seo.schemaDescription` → `youtube subtitle download karne wala app`
- **4 cụm Devanagari đặt NGUYÊN VĂN, không sửa một chữ, không chèn từ vào giữa chuỗi:**
  - `यूट्यूब सबटाइटल डाउनलोड करें` → `hero.h1` + `conclusion.h2` (nguyên văn, dạng câu lệnh hành động).
  - `यूट्यूब सबटाइटल डाउनलोड कैसे करें` → `quickAnswer.question` (+ `?`) **và** `sections[2].h2` (nguyên văn 100%). H1 **không** mang `कैसे` — đó là dạng câu hỏi, thuộc quickAnswer và H2 S3.
  - `यूट्यूब वीडियो से सबटाइटल कैसे डाउनलोड करें` → **FAQ 1** nguyên văn (+ `?`) **và** `sections[0].content[2]` nguyên văn.
  - `यूट्यूब से SRT फाइल कैसे डाउनलोड करें` → `sections[1].items[0].content` nguyên văn (ngoại lệ nukta duy nhất của file).
- **S1 đoạn 2** là định nghĩa ranh giới của bản EN — **dịch sát, không rút gọn**. Đây là câu chống cannibalization mạnh nhất trang, và là chỗ duy nhất ngoài S6/FAQ 5 được nhắc `ट्रांसक्रिप्ट`.
- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp.
- Nỗi lo nhận dạng **tiếng Hindi** xử lý **trong section 5** — không thêm câu.
- "Không cần cài app" đảo lên sớm trong `hero.subtitle` và FAQ 2 — **không thêm câu**, chỉ đổi trọng số từ ngữ.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- **`यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें` / `यूट्यूब ट्रांसक्रिप्ट डाउनलोड कैसे करें` / `youtube transcript kaise download kare` / `यूट्यूब वीडियो का टेक्स्ट कैसे निकाले`** → **/hi/download-youtube-transcript** (tài liệu để đọc/lưu/nộp, TXT/DOCX/PDF). Chỉ được nhắc ở S1 đoạn 2, S6 và FAQ 5.
- `यूट्यूब ट्रांसक्रिप्ट` / `youtube ka transcript kaise dekhe` / `यूट्यूब ट्रांसक्रिप्ट पढ़ें` → **/hi/youtube-transcript** (đọc + copy trên màn hình, **không** tải file).
- `यूट्यूब वीडियो का सारांश` / `यूट्यूब वीडियो समरी` → **/hi/youtube-video-summarizer**.
- ⚠️ **NHÓM NHIỄM NGUY HIỂM NHẤT — tải VIDEO:** `youtube video download` / `यूट्यूब वीडियो डाउनलोड` / `यूट्यूब वीडियो डाउनलोडर` / `youtube se video kaise download kare` / `mp4 download` / `youtube video download karne wala app`.
  - **QUY TẮC BẮT BUỘC:** `डाउनलोड` chỉ đi với `सबटाइटल` / `फ़ाइल` / `SRT` / `VTT`. **KHÔNG BAO GIỜ** `वीडियो डाउनलोड`.
  - ⚠️ Đặc biệt lưu ý cụm `...download karne wala app` — keyword của trang này (`youtube subtitle download karne wala app`) chỉ khác cụm tải video đúng một chữ `subtitle`. Chuỗi này chỉ được đặt ở `schemaDescription` và **bắt buộc giữ nguyên chữ `subtitle`** ở giữa.
- `यूट्यूब से MP3 डाउनलोड` / `यूट्यूब ऑडियो डाउनलोड` → intent tải **âm thanh**.
- `यूट्यूब पर सबटाइटल कैसे लगाएँ` / `यूट्यूब सबटाइटल ऑन करें` / `यूट्यूब कैप्शन सेटिंग` → hướng dẫn **thao tác trong YouTube / YouTube Studio**, không phải công cụ tải.
- `सबटाइटल कैसे बनाएँ` / `सबटाइटल एडिटर` → công cụ **tạo/soạn** phụ đề từ đầu, không phải trích từ video có sẵn.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → **/hi/youtube-transcript** — chỉ cần chữ thuần đọc trên màn hình, không timecode, không đồng bộ với playback
- → **/hi/download-youtube-transcript** — lưu chữ đó thành tài liệu TXT / DOCX / PDF. **Đây là trang đối xứng, link quan trọng nhất**
- → **/hi/youtube-video-summarizer** — chỉ cần biết video nói gì, không cần caption từng dòng

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Cấu trúc JSON khớp **100%** với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **7 sections**, `conclusion` h2 + 2 đoạn. **KHÔNG có `specs`.**
  - S1 `content` **3** | S2 `intro` 1 + `items` **2** | S3 `steps` **4** | S4 `intro` 1 + `items` **5** | S5 `content` **2** | S6 `content` **2** | S7 `items` **8**
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok, SubRip, WebVTT**.
  - Ngoại lệ có chủ đích: **`यूट्यूब`** viết Devanagari ở các slot chứa keyword đã search — xem mục "`यूट्यूब` vs `YouTube`" phía trên.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: सबटाइटल, कैप्शन, फ़ाइल, डाउनलोड, फ़ॉर्मैट, एक्सपोर्ट, ब्राउज़र, टाइमकोड, टाइमस्टैम्प, लिंक, वीडियो, प्लेयर, एडिटर, प्लैटफ़ॉर्म, ऐप, इंस्टॉल.
- Số đếm dùng chữ số Latin (100+, 00:01:12) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **`आप`** xuyên suốt, **không** dùng `तू`/`तुम` — nhất quán tuyệt đối với `/hi/download-youtube-transcript`, `/hi/video-to-text`, `/hi/audio-to-text`, `/hi/instagram-caption-downloader`.
- **Nukta (़) dùng nhất quán:** फ़ाइल, फ़ॉर्मैट, ज़्यादा, सिर्फ़, ज़रूरत, आवाज़, फ़र्क़, फ़ोन, ऑफ़लाइन, ख़ुद, प्लैटफ़ॉर्म. **Ngoại lệ duy nhất:** `फाइल` trong chuỗi keyword nguyên văn ở `sections[1].items[0].content`.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle`, `hero.*` và mọi `h2`/`h3` **không** chứa Hinglish thô.
- Internal link `sections[5].content[1]` giữ nguyên cú pháp markdown, đổi path sang `/hi/youtube-transcript`, `/hi/download-youtube-transcript`, `/hi/youtube-video-summarizer`.
- **Tuyệt đối không để chuỗi `वीडियो डाउनलोड` xuất hiện ở bất kỳ đâu trong file.**
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** Hindi văn chương nặng (उपशीर्षक, अनुलेख, प्रतिलिपि) và **tránh** dịch máy word-by-word.
