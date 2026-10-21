🔥 TranscriptX – Video to Text (Hindi / hi)

URL:
/hi/video-to-text

Intent chính:

वीडियो को टेक्स्ट में बदलें (ऑनलाइन, फ्री)

Trang này là **bản tiếng Hindi của trang trụ (hub)** cụm Video to Text. Nhắm đến người dùng Ấn Độ **đã có sẵn file video** — bản ghi Zoom/Teams/Meet, screen recording, bài giảng quay hình, footage máy quay/điện thoại, video tải về — và muốn lấy **phần lời nói bên trong** ra thành chữ để đọc, tìm kiếm, trích dẫn, làm biên bản, làm phụ đề hoặc đưa vào AI.

Gộp toàn bộ intent đồng nghĩa **बदलना / निकालना / ट्रांसक्राइब करना / कन्वर्ट करना** vì tất cả cho ra **cùng một kết quả**: file video → văn bản.

---

## ⚠️ Phân định với `/hi/audio-to-text`: LOẠI FILE

Trang này nhận **वीडियो फ़ाइल** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **ऑडियो फ़ाइल** (MP3, WAV, M4A, AAC...). Đây là ranh giới cứng, người dùng tự phân biệt rất rõ bằng loại file họ đang cầm trong tay.

Chốt chặn nằm ở **section 10 đoạn 3**, nơi có link `[ऑडियो टू टेक्स्ट](/hi/audio-to-text)`. Câu điều hướng phải nói rõ: *nếu nguồn của bạn thật ra là file âm thanh chứ không phải video*.

Hệ quả bắt buộc khi dịch: mọi chỗ nói về file đầu vào của trang này phải gắn từ **वीडियो** (`वीडियो फ़ाइल`, `वीडियो अपलोड करें`), không được viết trống `फ़ाइल अपलोड करें` ở những vị trí trọng số cao (H1, H2, quickAnswer, spec `स्वीकृत फ़ॉर्मैट`) — nếu không hai trang sẽ mờ ranh giới.

---

## ⚠️ Phân định với các trang nền tảng: FILE vs LINK

Trang này để **वीडियो फ़ाइल अपलोड करें** (tải file lên từ máy/điện thoại). Ba trang nền tảng `/hi/youtube-transcript`, `/hi/tiktok-transcript`, `/hi/instagram-transcript` để **लिंक पेस्ट करें** (dán đường dẫn, không có file trên máy).

Cả 4 internal link nằm chung ở **section 10 đoạn 3** — nhiều link nhất trong các trang `hi` đã làm. Câu dẫn phải nêu rõ tiêu chí chọn: *video nằm trên nền tảng thì dán link, video nằm trên thiết bị thì upload file*.

Không được kéo `यूट्यूब वीडियो को टेक्स्ट में बदलें` / `रील को टेक्स्ट में बदलें` về trang này.

---

## ⚠️ Mục riêng — chiến lược Hinglish vs Devanagari

Section `## Hindi (hi)` trong `2_loc_kw.md` **chỉ có 7 keyword** — mỏng nhất trong toàn bộ trang này (bản `es` có 15, bản `id`/`ja` có 16). Nhưng điều đáng chú ý hơn số lượng là: **danh sách trộn CẢ HAI hệ chữ**.

| Dạng | Số lượng | Ví dụ |
| ---- | -------- | ----- |
| **Hinglish (chữ Latin)** | 5 | `video se text kaise nikale`, `video transcribe kaise kare` |
| **Devanagari (chữ Hindi thật)** | **2** | `वीडियो को टेक्स्ट में बदलें`, `वीडियो से टेक्स्ट कैसे निकाले` |

### 🎯 Trang này KHÁC `/hi/facebook-transcript`, GIỐNG `/hi/instagram-caption-downloader`

- `/hi/facebook-transcript` có **0 keyword Devanagari** → buộc phải tự dịch 100% tầng hiển thị, **không một keyword đã search nào lọt được vào H1/H2**, chỉ nhét được vào meta.
- `/hi/instagram-caption-downloader` có **3 keyword Devanagari** → đặt được nguyên văn vào H1/quickAnswer/H2.
- **Trang này có 2 keyword Devanagari** → cùng nhóm với Instagram, **phải khai thác triệt để**. Đây là hai slot lexical duy nhất khớp trực tiếp được với truy vấn thật ở tầng hiển thị, không được "dịch lại cho mượt hơn".

### Chiến lược đã chốt — hai tầng (khớp Instagram Caption Downloader)

1. **Tầng hiển thị** (`seo.title`, `hero.h1`, mọi `h2`/`h3`, toàn bộ body, FAQ, conclusion): **Devanagari 100%**.
   - 2 cụm Devanagari đã search đặt **nguyên văn** (dạng chuỗi con liền mạch, không chèn từ vào giữa) ở vị trí trọng số cao nhất.
   - Tên riêng và định dạng giữ Latin.
2. **Tầng meta** (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn **nguyên văn 5 chuỗi Hinglish**. Meta không phải văn bản người đọc lướt trong bài nên chuỗi Latin ở đó không phá nhịp đọc, mà vẫn cho Google khớp lexical chính xác với cách người Ấn thực sự gõ.
3. **TUYỆT ĐỐI không chèn Hinglish thô** vào `title` / `h1` / `h2` / body / FAQ / conclusion. Một H1 nửa Latin nửa Devanagari trông như trang spam.

> ⚠️ **`video se text kaise nikale` (100–1K) là keyword mạnh nhất của cả trang** — cao hơn 6 cụm còn lại một bậc độ lớn. Nhưng nó là **Hinglish**, nên theo quy tắc hai tầng nó nằm ở `seo.description` (slot meta mạnh nhất). **Nghĩa** của nó được cấp hẳn tầng hiển thị qua cụm Devanagari song sinh `वीडियो से टेक्स्ट कैसे निकाले` — hai chuỗi này là cùng một truy vấn viết bằng hai hệ chữ, nên phủ được cả hai phía.

---

## ⚠️ Mục riêng — rủi ro nhiễm OCR

Cụm `video se text nikale` / `वीडियो से टेक्स्ट कैसे निकाले` đọc mộc **có thể bị hiểu thành OCR** — tức "lấy chữ hiển thị TRÊN màn hình video" (subtitle cháy vào hình, chữ trong slide, watermark). Đây là intent hoàn toàn khác và SERP khác hẳn.

Trang này lấy **वीडियो में बोली गई बात** — âm thanh, lời nói, giọng người — không phải chữ trên khung hình.

**Cách chốt (không thêm section, không thêm câu):**
- **Section 5** (`सटीकता के साथ वीडियो को टेक्स्ट में बदलें`): nói rõ TranscriptX xử lý **बोली गई बात / आवाज़**, nhấn các yếu tố chỉ tồn tại ở âm thanh (viराम-chiếu dấu câu, tách người nói, lhaja/giọng, tạp âm nền).
- **Section 8** (`वीडियो टू टेक्स्ट कितना सटीक है?`): toàn bộ đoạn nói về chất lượng **ऑडियो** của bản ghi — gūñj, nhạc nền, nhiều người nói chồng nhau. Không có yếu tố nào của OCR (độ nét chữ, font, độ phân giải) được nhắc tới.
- **Section 3 step 2** nói rõ công cụ **वीडियो में से ऑडियो निकालकर** rồi mới ट्रांसक्राइब — câu này một mình đã loại bỏ hiểu lầm OCR.

Đây là cách xử lý y hệt bản `es` (nhóm `audio de video` / `voz de video`), chỉ khác là bản `hi` phải làm bằng cách chọn từ khi dịch vì không có keyword riêng để dựa vào.

---

## ⚠️ Quy tắc `डाउनलोड` — nhóm nhiễm nguy hiểm nhất

Ở Ấn Độ nhóm `video download` / `वीडियो डाउनलोड` có **volume khổng lồ**, gấp hàng nghìn lần mọi keyword của trang này, và SERP hoàn toàn là công cụ tải video. Tiếng Hindi dùng chung đúng một từ `डाउनलोड` cho cả hai intent nên rủi ro cao hơn hẳn bản `de`/`fr`.

**QUY TẮC BẮT BUỘC:** `डाउनलोड` **phải luôn** đi kèm tân ngữ `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`. **KHÔNG BAO GIỜ** viết `वीडियो डाउनलोड करें` — kể cả trong FAQ hay conclusion. Với video luôn dùng động từ `अपलोड करें`.

---

## Từ khóa chính

**video se text kaise nikale** (100–1K) ✅ *đã search, **Hinglish*** — keyword mạnh nhất, cao hơn 6 cụm còn lại một bậc.

> Đặt nguyên văn ở `seo.description`. Nghĩa của nó lên tầng hiển thị qua cụm Devanagari song sinh (xem dưới).

## Từ khóa chính ở tầng hiển thị

**वीडियो को टेक्स्ट में बदलें** (0–10) ✅ *đã search, **Devanagari*** → `seo.title` + `hero.h1`

**वीडियो से टेक्स्ट कैसे निकाले** (0–10) ✅ *đã search, **Devanagari*** → `quickAnswer.question` + **H2 section 3**

---

## Từ khóa phụ

### Nhóm Devanagari — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng hiển thị 🇮🇳

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| वीडियो को टेक्स्ट में बदलें | 0–10 | ✅ đã search — **Devanagari** → `seo.title`, `hero.h1`, **H2 section 5** (dạng chuỗi con), conclusion |
| वीडियो से टेक्स्ट कैसे निकाले | 0–10 | ✅ đã search — **Devanagari** → `quickAnswer.question` (+`?`), **H2 section 3**, FAQ 1 |

### Nhóm Hinglish — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng meta 🔤

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video se text kaise nikale | 100–1K | ✅ đã search — **Hinglish** → `seo.description` *(KW chính)* |
| video se text banaye | 0–10 | ✅ đã search — **Hinglish** → `seo.description` |
| video transcribe kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| video ko likhit me badle | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| video se likhit me convert | 0–10 | ✅ đã search — **Hinglish** → `seo.schemaDescription` |

### Dịch bổ sung (chỉ rải trong body, KHÔNG đặt vào title/H1)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| वीडियो ट्रांसक्रिप्शन | — | 🔄 dịch bổ sung (video transcription) |
| वीडियो ट्रांसक्राइब करें | — | 🔄 dịch bổ sung (transcribe video) |
| फ्री वीडियो ट्रांसक्राइबर | — | 🔄 dịch bổ sung (free video transcriber) |
| वीडियो टू टेक्स्ट कन्वर्टर | — | 🔄 dịch bổ sung (video to text converter) |
| वीडियो फ़ाइल को टेक्स्ट में बदलें | — | 🔄 dịch bổ sung (video file to text) |
| वीडियो को टेक्स्ट में बदलें फ्री | — | 🔄 dịch bổ sung (video to text free) |
| MP4 को टेक्स्ट में बदलें | — | 🔄 dịch bổ sung (mp4 to text) |
| वीडियो ट्रांसक्रिप्ट जनरेटर | — | 🔄 dịch bổ sung (video transcript generator) |
| मीटिंग रिकॉर्डिंग को टेक्स्ट में बदलें | — | 🔄 dịch bổ sung (Zoom/Teams recording) |
| वीडियो में बोली गई बात को टेक्स्ट में बदलें | — | 🔄 dịch bổ sung (chống nhiễm OCR) |
| वीडियो से सबटाइटल बनाएँ | — | 🔄 dịch bổ sung (subtitle from video) |

### Tỉ lệ

- **Đã search: 7 keyword** (2 Devanagari + 5 Hinglish) — **~39%**
- **Dịch bổ sung: 11 cụm** — **~61%**

So sánh: bản `es` có 15/15 đã search (100%), bản `hi` này chỉ 7 và trong đó chỉ **2 cụm dùng được ở tầng hiển thị**. Phần lớn nội dung buộc phải **dịch tự nhiên** bằng thuật ngữ Hindi thông dụng nhất trên web — không đủ dữ liệu để tối ưu theo keyword như bản `es` hay `ar`.

**Nguyên tắc dùng:** ✅ *đã search, Devanagari* = ưu tiên tuyệt đối, đặt **nguyên văn** vào `title`/`h1`/`quickAnswer`/`h2`/FAQ. ✅ *đã search, Hinglish* = đặt **nguyên văn** vào `seo.description`/`ogDescription`/`schemaDescription`, **không** vào body. 🔄 *dịch bổ sung* = chỉ rải trong body.

---

## Search Intent

Người dùng Ấn Độ **đã có file video trong tay** — bản ghi cuộc họp Zoom/Teams/Meet, screen recording hướng dẫn, webinar, bài giảng coaching quay hình, footage phỏng vấn, video tải về — và muốn lấy phần lời nói ra thành chữ để đọc, tìm kiếm, trích dẫn, làm biên bản, làm tài liệu hoặc làm phụ đề.

Họ kỳ vọng:

- Tải file video lên là chạy, **không cài phần mềm**.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — phần lớn người dùng Ấn Độ vào web bằng mobile.
- **Không giới hạn dung lượng / thời lượng** — bản ghi họp 2–3 tiếng là chuyện thường.
- Hỗ trợ nhiều định dạng: MP4, MOV, AVI, MKV, WebM.
- Phân biệt được **nhiều người nói** (quan trọng nhất với biên bản họp).
- Nhận dạng tốt tiếng Hindi và tiếng Anh giọng Ấn.
- Xuất DOCX để làm tài liệu, SRT để làm phụ đề.

### Khác biệt so với bản tiếng Anh

1. **Keyword tồn tại ở HAI hệ chữ cùng lúc — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ, mọi keyword đều đặt tự do vào bất kỳ đâu. Bản `hi`: 5 keyword Latin (Hinglish) + 2 keyword Devanagari, bắt buộc tách hai tầng. Đây là quyết định biên tập không tồn tại ở bản EN hay bất kỳ ngôn ngữ châu Âu nào của trang này.
2. **Dữ liệu mỏng hơn hẳn — 7 keyword so với 19 của bản EN.** Bản EN có ba nhóm động từ riêng biệt đủ volume để cấp H2 riêng (`convert` / `transcribe` / `transcriber`); bản `hi` không có nhóm nào đủ mạnh. H2 phải bám sát bản dịch tự nhiên của EN thay vì được lái theo keyword.
3. **Rủi ro OCR là vấn đề riêng của tiếng Hindi.** Động từ `निकालना` (rút ra, lấy ra) trung tính về nguồn — nó không nói rõ lấy từ âm thanh hay từ khung hình, trong khi "transcribe" của bản EN đã tự mang nghĩa âm thanh. Bản `hi` phải chủ động chốt nguồn là lời nói ở section 3/5/8, việc bản EN không cần làm.
4. **`फ्री / मुफ़्त` phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần từ `फ्री` xuất hiện ở `title`, `description`, `hero.subtitle`, section 4 và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
5. **Mobile-first.** Bản EN nhắc "desktop, tablet and mobile" như thông tin phụ; bản `hi` nên để `फ़ोन` xuất hiện tự nhiên và sớm hơn trong section 4 — nhưng **không thêm câu mới**, chỉ đảo trọng số từ ngữ trong các câu đã có.
6. **Nhóm `वीडियो डाउनलोड` là mìn.** Bản EN không có rủi ro này vì "download the transcript" và "download the video" là hai cụm rõ ràng khác nhau trong SERP tiếng Anh của chủ đề transcription. Ở Ấn Độ, `डाउनलोड` đứng gần `वीडियो` sẽ kéo trang lệch sang page type hoàn toàn khác.

---

## Đối tượng người dùng

- Nhân viên văn phòng, trợ lý (biên bản họp Zoom/Teams/Meet)
- Sinh viên, người luyện thi (bài giảng coaching class quay hình)
- Giáo viên, người làm khóa học online (screen recording → tài liệu)
- Nhà báo, phóng viên (bóc băng phỏng vấn quay hình)
- YouTuber / content creator Ấn Độ (webinar, video → bài viết)
- Người tạo phụ đề (xuất SRT/VTT)
- Marketer (webinar, hội thảo → nội dung)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **11 section**, cùng số đoạn `content`, đúng **10 `specs`**, đúng **4 `steps`**, section 6 = `intro` 1 + `items` **4**, section 7 = `intro` 1 + `items` **6**, đúng **10 FAQ** (khác `/hi/audio-to-text` vốn có 11), `conclusion` = h2 + **2 đoạn**. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** वीडियो को टेक्स्ट में बदलें | **वीडियो को टेक्स्ट में बदलें ✅ (Devanagari, nguyên văn)** |
| — | **quickAnswer** | **वीडियो से टेक्स्ट कैसे निकाले? ✅ (Devanagari, nguyên văn + `?`)** |
| 1 | वीडियो को टेक्स्ट में बदलना क्या है? | वीडियो को टेक्स्ट में बदलें ✅, वीडियो ट्रांसक्रिप्शन 🔄 |
| 2 | एक नज़र में वीडियो टू टेक्स्ट | *(bảng 10 thông số — फ्री / कोई सीमा नहीं / 100+ भाषाएँ / MP4, MOV, AVI, MKV, WebM)* |
| 3 | **वीडियो फ़ाइल से टेक्स्ट कैसे निकाले** | **वीडियो से टेक्स्ट कैसे निकाले ✅ (Devanagari, nguyên văn ở H2)**, वीडियो फ़ाइल को टेक्स्ट में बदलें 🔄 · ⚠️ step 2 chốt nguồn = ऑडियो (chống OCR) |
| 4 | एक फ्री वीडियो ट्रांसक्राइबर | फ्री वीडियो ट्रांसक्राइबर 🔄, वीडियो टू टेक्स्ट कन्वर्टर 🔄, वीडियो ट्रांसक्रिप्ट जनरेटर 🔄, वीडियो को टेक्स्ट में बदलें फ्री 🔄 · mobile-first (`फ़ोन`) |
| 5 | **सटीकता के साथ वीडियो को टेक्स्ट में बदलें** | **वीडियो को टेक्स्ट में बदलें ✅ (Devanagari, chuỗi con liền mạch ở H2)**, वीडियो ट्रांसक्राइब करें 🔄 · ⚠️ chốt nguồn = बोली गई बात (chống OCR) |
| 6 | सपोर्टेड वीडियो फ़ॉर्मैट | MP4 को टेक्स्ट में बदलें 🔄 *(MP4, MOV, AVI+MKV, WebM)* |
| 7 | आप क्या-क्या ट्रांसक्राइब कर सकते हैं | मीटिंग रिकॉर्डिंग को टेक्स्ट में बदलें 🔄, वीडियो ट्रांसक्रिप्शन 🔄 *(Zoom/Teams/Meet, screen recording, webinar, footage, lecture, archived)* |
| 8 | वीडियो टू टेक्स्ट कितना सटीक है? | वीडियो में बोली गई बात को टेक्स्ट में बदलें 🔄 · ⚠️ toàn đoạn nói về chất lượng ऑडियो (chống OCR) |
| 9 | 100 से ज़्यादा भाषाओं में वीडियो टू टेक्स्ट | वीडियो ट्रांसक्रिप्शन 🔄 *(đổi ví dụ German/Vietnamese của EN sang có tiếng Hindi)* |
| 10 | अपना ट्रांसक्रिप्ट पाँच फ़ॉर्मैट में एक्सपोर्ट करें | वीडियो से सबटाइटल बनाएँ 🔄 · **4 internal link ở đoạn 3** |
| 11 | अक्सर पूछे जाने वाले सवाल | **वीडियो से टेक्स्ट कैसे निकाले ✅ (FAQ 1)**, वीडियो को टेक्स्ट में बदलें फ्री 🔄, फ्री वीडियो ट्रांसक्राइबर 🔄 + long-tail |
| — | **conclusion** | **वीडियो को टेक्स्ट में बदलें ✅**, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **5 chuỗi Hinglish nằm HOÀN TOÀN ở tầng meta, không một chuỗi nào trong `hero`/`sections`/`conclusion`:**
  - `seo.description` → `video se text kaise nikale` *(KW mạnh nhất, đặt sớm trong câu)* + `video se text banaye`
  - `seo.ogDescription` → `video transcribe kaise kare` + `video ko likhit me badle`
  - `seo.schemaDescription` → `video se likhit me convert`
- **2 cụm Devanagari đặt NGUYÊN VĂN, không sửa một chữ, không chèn từ vào giữa chuỗi:**
  - `वीडियो को टेक्स्ट में बदलें` → `seo.title` (đầu chuỗi), `seo.ogTitle`, `hero.h1` (nguyên văn 100%), `sections[4].h2` dạng `सटीकता के साथ वीडियो को टेक्स्ट में बदलें` (chuỗi con liền mạch), `conclusion.h2` dạng `अपने वीडियो को फ्री में टेक्स्ट में बदलें` — **lưu ý:** chỉ H1 và title giữ chuỗi 100% liền mạch; conclusion là biến thể có chèn `फ्री में`, chấp nhận được vì không phải slot trọng số cao nhất.
  - `वीडियो से टेक्स्ट कैसे निकाले` → `quickAnswer.question` (thêm `?`) **và** `sections[2].h2` dạng `वीडियो फ़ाइल से टेक्स्ट कैसे निकाले` (chèn `फ़ाइल` để phân định FILE vs LINK — đánh đổi có chủ đích, chuỗi vẫn khớp gần tuyệt đối) **và** FAQ 1 nguyên văn.
- Section 9 của bản EN dùng ví dụ German/Vietnamese — bản `hi` **đổi thành ví dụ có tiếng Hindi** (giống cách bản `es` làm), **không thêm câu**, chỉ thay danh từ ngôn ngữ trong câu đã có.
- Section 6 item "MOV" nhắc iPhone/iPad/QuickTime — giữ nguyên, nhưng section 4 dùng `फ़ोन` chung chung hơn để phù hợp thực tế Android-dominant ở Ấn Độ. Vẫn **không thêm câu**.
- Section 3 step 1 bản EN nhắc "or paste a link to the video" — **giữ nguyên** (bản EN có), nhưng không nhấn, vì trọng tâm phân định của trang này là upload file.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `audio ko text me kaise badle` / `ऑडियो को टेक्स्ट में बदलें` / `MP3 को टेक्स्ट में बदलें` → **/hi/audio-to-text** (file ÂM THANH, không phải file VIDEO)
- `voice ko text me kaise badle` / `आवाज को टेक्स्ट में बदलें` / `बोलकर लिखना` / डिक्टेशन → **/hi/voice-to-text**
- `youtube video ka transcript` / `यूट्यूब वीडियो को टेक्स्ट में बदलें` → **/hi/youtube-transcript** (dán LINK)
- `tiktok video se text nikale` / `टिकटॉक ट्रांसक्रिप्ट` → **/hi/tiktok-transcript** (dán LINK)
- `instagram reel se text nikale` / `रील को टेक्स्ट में बदलें` → **/hi/instagram-transcript** (dán LINK)
- `टेक्स्ट को आवाज में बदलें` / टेक्स्ट टू स्पीच → **trang Text-to-Speech (ngược intent)**
- ⚠️ **NHÓM NHIỄM NGUY HIỂM NHẤT — tải VIDEO:** `video download` / `वीडियो डाउनलोड` / `वीडियो डाउनलोडर` / `mp4 download` / `video download karne wala app`.
  - Volume khổng lồ ở Ấn Độ, SERP hoàn toàn là công cụ tải video. Kéo vào sẽ làm lệch page type ngay lập tức.
  - **QUY TẮC BẮT BUỘC:** `डाउनलोड` chỉ đi với `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`. Với video luôn dùng `अपलोड करें`.
- ⚠️ **NHÓM NHIỄM THỨ HAI — OCR:** `वीडियो से टेक्स्ट कॉपी करें` hiểu theo nghĩa chữ trên màn hình, `स्क्रीनशॉट से टेक्स्ट निकालें`, `इमेज से टेक्स्ट`, OCR. Trang này lấy **lời nói**, không lấy chữ trên khung hình. Xem mục riêng ở trên.
- `वीडियो एडिट करें` / `वीडियो कंप्रेस करें` / `MP4 को MP3 में बदलें` → intent **xử lý FILE video**, không phải lấy chữ.
- `वीडियो में सबटाइटल लगाएँ` → intent gắn phụ đề lên video; trang này chỉ **xuất file SRT/VTT** (section 10 + FAQ 8), không gắn hộ.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link** — nhiều nhất trong các trang `hi` đã làm:

- → **/hi/audio-to-text** (khi nguồn là file ÂM THANH thay vì file video) — đây là ranh giới LOẠI FILE
- → **/hi/youtube-transcript**, **/hi/tiktok-transcript**, **/hi/instagram-transcript** (khi video nằm trên nền tảng, **dán link** thay vì upload file) — đây là ranh giới FILE vs LINK

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **11 sections**, `conclusion` h2 + 2 đoạn.
  - S1 `content` 4 | S2 `specs` **10** | S3 `steps` **4** | S4 `content` 3 | S5 `content` 3 | S6 `intro` 1 + `items` **4** | S7 `intro` 1 + `items` **6** | S8 `content` 3 | S9 `content` 2 | S10 `content` 3 | S11 `items` **10**
- **Nhãn `specs` COPY Y NGUYÊN từ `/hi/audio-to-text/hi.json`, không tự dịch lại:** कीमत · अकाउंट ज़रूरी · इंस्टॉलेशन · फ़ाइल साइज़ की सीमा · स्वीकृत फ़ॉर्मैट · भाषाएँ · स्पीकर की पहचान · टाइमस्टैम्प · एक्सपोर्ट फ़ॉर्मैट · डिवाइस. Chỉ đổi **giá trị** của `स्वीकृत फ़ॉर्मैट` sang định dạng video (MP4, MOV, AVI, MKV, WebM और अन्य).
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad**.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: वीडियो, टेक्स्ट, फ़ाइल, अपलोड, कन्वर्ट, ट्रांसक्रिप्ट, ट्रांसक्राइब, फ़ॉर्मैट, एक्सपोर्ट, ब्राउज़र, स्पीकर, टाइमस्टैम्प, सबटाइटल, कैप्शन, रिकॉर्डिंग.
- Số đếm dùng chữ số Latin (100+, 5) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **`आप`** xuyên suốt, **không** dùng `तू`/`तुम` — nhất quán tuyệt đối với `/hi/audio-to-text` và `/hi/instagram-caption-downloader`.
- Nukta (़) dùng nhất quán: फ़ाइल, फ़ॉर्मैट, ज़्यादा, सिर्फ़, ज़रूरत, आवाज़, फ़ोन.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle`, `hero.h1` và mọi `h2`/`h3` **không** chứa Hinglish thô.
- Internal link `sections[9].content[2]` giữ nguyên cú pháp markdown, đổi path sang `/hi/audio-to-text`, `/hi/youtube-transcript`, `/hi/tiktok-transcript`, `/hi/instagram-transcript`.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** Hindi văn chương nặng (दृश्य-श्रव्य, पाठ, अभिलेखन) và **tránh** dịch máy word-by-word.
