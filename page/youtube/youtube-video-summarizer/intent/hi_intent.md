🔥 TranscriptX – YouTube Video Summarizer (Hindi / hi)

URL:
/hi/youtube-video-summarizer

Intent chính:

यूट्यूब वीडियो का सारांश — AI से फ्री में निकालें

Trang này nhắm đến người dùng Ấn Độ muốn **nắm ý chính của một video YouTube mà không phải xem hết** — dán link, AI đọc toàn bộ nội dung rồi trả về bản tóm tắt ngắn gồm kết luận, các ý chính và chi tiết đáng nhớ.

---

## ✅ KHÔNG CÓ NHIỄM DỮ LIỆU

Khác hẳn bản `vi` (8/17 keyword là rác về game Minecraft), section `## Hindi (hi)` trong `2_loc_kw.md` **hoàn toàn sạch**:

- **Không** có dòng nhãn công cụ (`Keyword ideas` / `Keywords you provided`).
- **Không** có keyword lạc intent — cả 8 cụm đều xoay quanh `summary` / `summarize` / `nichod`, đúng intent tóm tắt.

**Số keyword thực: 8/8.**

> Ghi chú: hai cụm `youtube video ka nichod` và `youtube video ka nichod nikale` thoạt nhìn lạ, nhưng **không phải rác**. `निचोड़` (nichod) là từ Hindi đời thường nghĩa là "phần cốt lõi / cái đọng lại" — đúng intent tóm tắt. Đã giữ và dùng làm từ chống lặp cho `सारांश` trong body.

---

## 🚨 MỤC RIÊNG — 0/8 KEYWORD LÀ DEVANAGARI

Đây là phát hiện quan trọng nhất của bản `hi` trang này.

| Dạng | Số lượng | Keyword |
| ---- | -------- | ------- |
| **Hinglish (chữ Latin)** | **8** | `youtube video ka summary kaise nikale`, `youtube video summarize karna`, `youtube video ka summary`, `ai se youtube video summarize`, `youtube video ka nichod`, `youtube video summarize kaise kare`, `youtube video ka summary hindi me`, `youtube video ka nichod nikale` |
| **Devanagari (chữ Hindi thật)** | **0** | — |

**Không một keyword đã search nào có thể đặt nguyên văn vào `h1` / `h2` / `quickAnswer` ở tầng hiển thị.**

### So sánh với các trang `hi` đã làm

- `/hi/download-youtube-transcript`: **3** cụm Devanagari (2 dùng được) → đặt nguyên văn vào title/h1/H2.
- `/hi/video-to-text`: **2** cụm Devanagari dùng được → title+h1 và quickAnswer+H2 S3.
- `/hi/instagram-caption-downloader`: **3** cụm Devanagari.
- `/hi/facebook-transcript`: **0** cụm Devanagari → không keyword nào lọt vào H1/H2.
- **Trang này: 0 cụm Devanagari** → **cùng nhóm với `/hi/facebook-transcript`**, đây là trường hợp cực đoan nhất.

### Chiến lược đã chốt — hai tầng (áp lại theo dữ liệu thực tế)

Chiến lược 2 tầng của `/hi/download-youtube-transcript` vẫn áp dụng, nhưng **lệch hẳn về một phía** vì tầng hiển thị không có nguyên liệu:

1. **Tầng meta** (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn **nguyên văn cả 8 chuỗi Hinglish**. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin ở đó không phá nhịp đọc, mà vẫn cho Google khớp lexical đúng cách người Ấn thực sự gõ. **Đây là nơi DUY NHẤT trang này khớp được keyword đã search.**
2. **Tầng hiển thị** (`seo.title`, `seo.ogTitle`, `hero.*`, `quickAnswer`, mọi `h2`/`h3`, toàn bộ body, FAQ, conclusion): **Devanagari 100%**, dùng **bản dịch tự nhiên** của các cụm Hinglish — `summary` → `सारांश`, `nichod` → `निचोड़`, `summarize kaise kare` → `सारांश कैसे निकालें`.
3. **TUYỆT ĐỐI không chèn Hinglish thô** vào `title` / `ogTitle` / `h1` / `h2` / `h3` / body / FAQ / conclusion. Một H1 nửa Latin nửa Devanagari trông như trang spam.

> ⚠️ **Khác `/hi/download-youtube-transcript` ở một điểm quan trọng:** ở trang đó việc chia hai tầng **không mất gì** vì cả 8 cụm đều cùng mức `0–10`. **Ở trang này cụm mạnh nhất `youtube video ka summary kaise nikale` đạt `10–100`** — cao hơn hẳn 7 cụm còn lại (đều `0–10`) — và nó **buộc phải nằm ở tầng meta**. Đây là một đánh đổi thật, giống tình huống `/hi/video-to-text`. Bù lại bằng cách đặt nó **ngay đầu `seo.description`**, vị trí trọng số cao nhất của tầng meta.

### Ghi chú về từ `यूट्यूब` vs `YouTube`

Vì **không có** keyword Devanagari nào cần bảo toàn nguyên văn, trang này **không bị ràng buộc** như `/hi/download-youtube-transcript`.

**Quy ước đã chốt (đơn giản hơn):**
- Viết **`यूट्यूब`** (Devanagari) ở các slot tiêu đề: `seo.title`, `seo.ogTitle`, `hero.h1`, `quickAnswer.question`, `conclusion.h2`, FAQ 1 — để tầng hiển thị đọc thuần Hindi, không lổn nhổn.
- Viết **`YouTube`** (Latin) trong **body prose** và trong **nhãn 3 internal link** (đó là tên sản phẩm).

Đây chính là cách viết bình thường trên web tiếng Hindi — cả hai dạng đều phổ biến, Google khớp được cả hai.

---

## ✅ TRANG NÀY SẠCH XUNG ĐỘT VỚI 4 TRANG YOUTUBE KIA

Đã kiểm chéo toàn cụm 5 trang YouTube: **0 keyword trùng** ở **cả 13 ngôn ngữ**. Riêng bản `hi` càng sạch vì trang này dùng `summary` / `सारांश` / `निचोड़`, còn 4 trang kia dùng `transcript` / `ट्रांसक्रिप्ट`, `subtitle` / `सबटाइटल`, `text` / `टेक्स्ट`.

Không cần nhường hay neo đẩy đi cụm nào — khác hẳn cặp `download-transcript` ↔ `subtitle-downloader` (phải nhường 1 cụm).

Ranh giới vẫn phải giữ trong nội dung — bản EN cài **3 chốt**, đã dịch sát cả ba:

1. **S1 đoạn 3** — *"ट्रांसक्रिप्ट आपको एक-एक शब्द देता है; सारांश यह तय करता है कि कौन-से शब्द आपके समय के लायक़ थे।"*
2. **FAQ 4** — *"सारांश और ट्रांसक्रिप्ट में क्या फ़र्क़ है?"*
3. **S7 đoạn 2** — chứa cả 3 internal link.

---

## Từ khóa chính (tầng meta)

**youtube video ka summary kaise nikale** (10–100) ✅ *đã search, **Hinglish***

Cụm mạnh nhất của cả trang và là **lõi chung** của các cụm còn lại. Vì là Hinglish nên **buộc nằm ở tầng meta** → đặt **ngay đầu `seo.description`**.

## Từ khóa chính (tầng hiển thị — bản dịch)

**यूट्यूब वीडियो का सारांश** 🔄 *dịch từ `youtube video ka summary`*

→ `seo.title`, `seo.ogTitle`, `hero.h1`, `conclusion.h2`.
Dạng câu hỏi **`यूट्यूब वीडियो का सारांश कैसे निकालें?`** (dịch từ cụm chính) → `quickAnswer.question`.

Đây là **cùng một truy vấn viết bằng hai hệ chữ** — phủ được cả hai phía người dùng Ấn Độ (gõ Latin và đọc Devanagari).

---

## Từ khóa phụ

### Nhóm Hinglish — ĐÃ SEARCH, đặt NGUYÊN VĂN ở tầng meta 🔤

| Keyword | Volume | Nguồn | Vị trí neo |
| ------- | ------ | ----- | ---------- |
| youtube video ka summary kaise nikale | 10–100 | ✅ đã search — Hinglish *(KW chính)* | `seo.description` **đầu chuỗi** |
| youtube video ka summary hindi me | 0–10 | ✅ đã search — Hinglish | `seo.description` |
| youtube video summarize kaise kare | 0–10 | ✅ đã search — Hinglish | `seo.ogDescription` **đầu chuỗi** |
| youtube video ka summary | 0–10 | ✅ đã search — Hinglish | `seo.ogDescription` |
| ai se youtube video summarize | 0–10 | ✅ đã search — Hinglish | `seo.schemaDescription` |
| youtube video summarize karna | 0–10 | ✅ đã search — Hinglish | `seo.schemaDescription` |
| youtube video ka nichod nikale | 0–10 | ✅ đã search — Hinglish | `seo.schemaDescription` |
| youtube video ka nichod | 0–10 | ✅ đã search — Hinglish | phủ theo dạng **chuỗi con** của cụm trên ✅ |

**Cả 8/8 cụm đã search đều có mặt nguyên văn trong tầng meta** (đã verify bằng script).

### Nhóm Devanagari — DỊCH BỔ SUNG, đặt ở tầng hiển thị 🇮🇳

| Keyword | Volume | Nguồn | Vị trí neo |
| ------- | ------ | ----- | ---------- |
| यूट्यूब वीडियो का सारांश | — | 🔄 dịch bổ sung *(từ KW chính)* | `title`, `ogTitle`, `h1`, `conclusion.h2` |
| यूट्यूब वीडियो का सारांश कैसे निकालें | — | 🔄 dịch bổ sung | `quickAnswer.question`, FAQ 1 |
| AI से यूट्यूब वीडियो का सारांश | — | 🔄 dịch bổ sung | **H2 S3** |
| वीडियो का निचोड़ | — | 🔄 dịch bổ sung *(từ `nichod`)* | S1 đoạn 2, S2 đoạn 2, S4 item 1, FAQ 4, conclusion |
| मुख्य बातें | — | 🔄 dịch bổ sung (key points) | rải body |
| लंबे वीडियो का सारांश | — | 🔄 dịch bổ sung (long video) | FAQ 6 |
| पॉडकास्ट का सारांश | — | 🔄 dịch bổ sung (podcast) | FAQ 6 |
| लेक्चर का सारांश | — | 🔄 dịch bổ sung (lecture) | S5 item 1 |
| सारांश टूल | — | 🔄 dịch bổ sung (tool) | FAQ 7 |
| फ्री में सारांश | — | 🔄 dịch bổ sung (free) | FAQ 1, conclusion |

### Tỉ lệ

- **Đã search: 8 keyword** — **dùng được cả 8**, nhưng **100% nằm ở tầng meta**, **0 cụm ở tầng hiển thị**.
- **Dịch bổ sung: 10 cụm** — gánh **toàn bộ** tầng hiển thị (title, h1, mọi h2, body, FAQ, conclusion).
- **Đã search / tổng số cụm dùng trên trang = 8 / 18 ≈ 44%. Dịch bổ sung ≈ 56%.**
- **Ở tầng hiển thị: đã search 0%, dịch bổ sung 100%.** Đây là con số đáng lưu ý nhất — nặng hơn cả `/hi/download-youtube-transcript` (2 cụm ở tầng hiển thị) và ngang `/hi/facebook-transcript`.

> ⚠️ **KHUYẾN NGHỊ SEARCH BỔ SUNG — DỮ LIỆU MỎNG NHẤT TRANG NÀY, ƯU TIÊN CAO HƠN `tr`.**
> Hai vấn đề chồng nhau:
> 1. **Chỉ 1/8 cụm đạt `10 – 100`, 7/8 ở mức `0 – 10`.** So sánh: bản `es` cụm mạnh nhất đạt `10K – 100K`, `id`/`ja`/`ko` đạt `1K – 10K`. Ấn Độ là thị trường YouTube lớn nhất thế giới — con số này gần như chắc chắn **không phản ánh thực tế**.
> 2. **0/8 cụm Devanagari.** Bộ search rõ ràng chỉ quét nhánh Hinglish. Các trang `hi` khác trong repo đều có 2–3 cụm Devanagari, nên việc trang này có **đúng 0** cụm là dấu hiệu **quét thiếu**, không phải thị trường không tồn tại.
>
> **Nên search lại, ưu tiên nhánh Devanagari:** `यूट्यूब वीडियो का सारांश`, `यूट्यूब वीडियो सारांश कैसे निकालें`, `वीडियो का सारांश बनाएँ`, `यूट्यूब वीडियो समरी`, `AI से वीडियो सारांश`, `यूट्यूब वीडियो का सारांश हिंदी में`, `लंबे वीडियो का सारांश`.
> **Và bổ sung nhánh Hinglish còn thiếu:** `youtube video summary hindi`, `youtube video summary tool`, `youtube video ka saransh`, `video summarize kaise kare`, `youtube summary nikalne wala app`.
> Đặc biệt đáng ngờ: từ **`समरी`** (transliteration Devanagari của "summary", rất phổ biến trên web Hindi) **hoàn toàn vắng mặt** — gần như chắc chắn có volume chưa được quét.

**Nguyên tắc dùng:**
✅ *đã search, Hinglish* = đặt **nguyên văn** vào `seo.description`/`ogDescription`/`schemaDescription`, **không** vào body.
🔄 *dịch bổ sung* = gánh tầng hiển thị, viết thật tự nhiên bằng thuật ngữ Hindi thông dụng nhất trên web.

---

## Search Intent

Người dùng Ấn Độ gặp một video YouTube dài — bài giảng coaching class, podcast, talk, review 20 phút — và muốn **biết nó nói gì trong một phút** để quyết định có đáng xem hết không.

Họ kỳ vọng:

- Dán link là ra tóm tắt trong vài giây, không đăng nhập.
- AI đọc **toàn bộ video**, không phải chỉ mô tả hay vài phút đầu.
- Tóm tắt đủ ngắn để đọc nhanh nhưng có **con số, tên, khuyến nghị cụ thể**, không chung chung.
- Nhận dạng tốt **tiếng Hindi** và tiếng Anh giọng Ấn.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — phần lớn người dùng Ấn Độ vào web bằng mobile.
- Không giới hạn độ dài video (bài giảng coaching class 2–3 tiếng là chuyện thường).

### Khác biệt so với bản tiếng Anh

1. **Keyword tồn tại ở MỘT hệ chữ duy nhất, và đó là hệ chữ SAI cho tầng hiển thị — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ, mọi keyword đặt tự do vào bất kỳ đâu. Bản `hi`: 8/8 keyword là Latin (Hinglish) trong khi tầng hiển thị bắt buộc Devanagari. Đây là quyết định biên tập không tồn tại ở bản EN hay bất kỳ ngôn ngữ châu Âu nào của trang này.
2. **Nhóm `वीडियो डाउनलोड` là mìn — bản EN không có rủi ro này.** Xem mục riêng bên dưới.
3. **Dữ liệu mỏng hơn hẳn — 7/8 cụm ở `0–10`, so với bản EN có 5 cụm đều `10K–100K`.** Bản EN có thể lái H2 theo keyword; bản `hi` phải **bám sát bản dịch tự nhiên của EN** hoàn toàn.
4. **`सारांश` là từ duy nhất cho kết quả, nhưng `निचोड़` cứu được việc lặp.** Bản EN xen kẽ `summary` (danh từ) và `summarize` (động từ). Tiếng Hindi có `सारांश` (danh từ) + `सारांश निकालना/बनाना` (động từ) + **`निचोड़`** (từ đời thường cho "cái đọng lại") — dùng `निचोड़` xen kẽ vừa chống lặp vừa khớp 2 keyword đã search.
5. **`फ्री` phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần `फ्री` ở `title`, `description`, FAQ 1 và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
6. **Nỗi lo nhận dạng tiếng Hindi xử lý trong S6** — thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Hindi. **Không thêm câu mới.**

---

## ⚠️ QUY TẮC `डाउनलोड` — NHÓM NHIỄM NGUY HIỂM NHẤT

Ở Ấn Độ nhóm `youtube video download` / `यूट्यूब वीडियो डाउनलोड` có **volume khổng lồ**, gấp hàng nghìn lần mọi keyword của trang này, và SERP hoàn toàn là công cụ tải video MP4. Tiếng Hindi dùng chung đúng một từ `डाउनलोड` cho cả hai intent nên rủi ro cao hơn hẳn bản `de`/`fr`/`vi`.

**Trang này KHÔNG tải gì cả — nó đọc và tóm tắt.**

**QUY TẮC BẮT BUỘC:** `डाउनलोड` **phải luôn** đi kèm tân ngữ `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`.
**KHÔNG BAO GIỜ** viết `वीडियो डाउनलोड` — kể cả trong FAQ, S1 hay conclusion.

**Kết quả kiểm tra `hi.json`:** từ `डाउनलोड` xuất hiện **đúng 1 lần duy nhất**, trong nhãn internal link **`यूट्यूब ट्रांसक्रिप्ट डाउनलोड`** ở S7 đoạn 2 — có tân ngữ `ट्रांसक्रिप्ट` đứng ngay trước ✅. Chuỗi `वीडियो डाउनलोड` **không xuất hiện** ✅.

Trang này an toàn hơn `/hi/download-youtube-transcript` rất nhiều, vì bản thân intent tóm tắt **không cần** động từ `डाउनलोड` ở đâu cả.

---

## ⚠️ `सबटाइटल` BỊ CẤM TUYỆT ĐỐI

Từ `सबटाइटल` thuộc trang `/hi/youtube-subtitle-downloader`. **Không xuất hiện một lần nào** trong `hi.json` ✅ (đã verify bằng grep).

Kết quả của trang này **luôn gọi là `सारांश`**. Từ đối lập `ट्रांसक्रिप्ट` chỉ được xuất hiện ở **S1 đoạn 3, S7 đoạn 2, FAQ 4 và FAQ 8** — đúng như bài mẫu `vi.json` đã duyệt.

> Ghi chú: từ `समरी` (transliteration của "summary") **cố tình không dùng** trong file, để giữ `सारांश` là từ duy nhất chỉ kết quả — nhất quán với quy tắc đã chốt. Nếu vòng search bổ sung xác nhận `समरी` có volume thật, đây là điểm nên xem lại.

---

## Đối tượng người dùng

- Sinh viên, học viên luyện thi (quyết định bài giảng coaching class có đáng xem hết không, biến ý chính thành ghi chú ôn tập)
- Người đi làm (nắm nội dung talk, earnings call, phỏng vấn ngành giữa các cuộc họp)
- Nghiên cứu sinh (quét nhanh nhiều video để chọn ra vài cái đáng xem kỹ và trích dẫn)
- Content creator, marketer Ấn Độ (rút thông điệp cốt lõi từ video dài để làm bài đăng, kịch bản)
- Người nghe podcast trên YouTube muốn nắm ý trước khi nghe
- Giáo viên, người làm khóa học online (tóm tắt video tham khảo thành handout)
- Người học ngoại ngữ (hiểu video tiếng nước ngoài qua bản tóm tắt tiếng Hindi)

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng 4 `steps`, đúng **4 `items`** ở S4 và S5, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.** Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** यूट्यूब वीडियो का सारांश | यूट्यूब वीडियो का सारांश 🔄 *(dịch từ KW chính)* |
| — | **quickAnswer** | यूट्यूब वीडियो का सारांश कैसे निकालें? 🔄 |
| 1 | वीडियो का सारांश आपको क्या देता है | वीडियो का निचोड़ 🔄 (đoạn 2) *(+ chốt phân định với ट्रांसक्रिप्ट ở đoạn 3)* |
| 2 | पूरा देखने के बजाय सारांश क्यों | वीडियो का निचोड़ 🔄 (đoạn 2) |
| 3 | AI से यूट्यूब वीडियो का सारांश कैसे बनाएँ | AI से यूट्यूब वीडियो का सारांश 🔄 |
| 4 | एक अच्छे सारांश में क्या होता है | *(4 items — मुख्य निचोड़ / मुख्य बातें / ठोस ब्यौरे / बनावट)* |
| 5 | सारांश किनके काम आता है | *(4 items — छात्र / प्रोफ़ेशनल / रिसर्चर / क्रिएटर)* |
| 6 | 100 से ज़्यादा भाषाओं में वीडियो का सारांश | *(+ nhấn tiếng Hindi, ऑनलाइन)* |
| 7 | जब सारांश से ज़्यादा की ज़रूरत हो | *(3 internal link — chốt phân định)* |
| 8 | अक्सर पूछे जाने वाले सवाल | फ्री में सारांश 🔄, सारांश टूल 🔄, लंबे वीडियो / पॉडकास्ट का सारांश 🔄 |
| — | **conclusion** | यूट्यूब वीडियो का सारांश 🔄, फ्री |
| — | **seo.description** | **youtube video ka summary kaise nikale ✅** *(đầu chuỗi)*, **youtube video ka summary hindi me ✅** |
| — | **seo.ogDescription** | **youtube video summarize kaise kare ✅** *(đầu chuỗi)*, **youtube video ka summary ✅** |
| — | **seo.schemaDescription** | **ai se youtube video summarize ✅**, **youtube video summarize karna ✅**, **youtube video ka nichod nikale ✅** |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **8 chuỗi Hinglish nằm HOÀN TOÀN ở tầng meta, không một chuỗi nào trong `hero`/`sections`/`conclusion`.** Đã verify bằng script quét toàn bộ block ngoài `seo` — **0 chuỗi Latin nhiều từ nào lọt ra** ✅.
- **S1 đoạn 3, FAQ 4 và S7 là ba chốt phân định** với trang transcript — dịch sát, không rút gọn. Đây là những chỗ duy nhất `ट्रांसक्रिप्ट` được nhắc như một khái niệm đối lập.
- **S3 step 4** cố tình dùng `पूरा टेक्स्ट` thay vì `ट्रांसक्रिप्ट` (bản EN có *"pull the full transcript"*) — để không làm loãng ba chốt phân định.
- **S6** thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Hindi — **không thêm câu**.
- `निचोड़` dùng ở **5 chỗ** (S1 đoạn 2, S1 đoạn 3, S2 đoạn 2, S4 item 1, FAQ 4, conclusion) — vừa chống lặp `सारांश` vừa neo 2 keyword đã search về mặt ngữ nghĩa.
- Mobile-first và `फ्री` đảo lên sớm hơn trong title/description/FAQ 1 — **không thêm câu**, chỉ đổi trọng số từ ngữ trong các câu đã có.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `यूट्यूब ट्रांसक्रिप्ट` / `youtube ka transcript kaise dekhe` → **/hi/youtube-transcript** (đọc + copy trên màn hình)
- `यूट्यूब ट्रांसक्रिप्ट डाउनलोड करें` / `youtube transcript kaise download kare` → **/hi/download-youtube-transcript**
- **`यूट्यूब सबटाइटल डाउनलोड करें` / `youtube subtitle download kaise kare` / `srt फाइल`** → **/hi/youtube-subtitle-downloader**. Từ `सबटाइटल` **bị cấm tuyệt đối** ở trang này.
- `वीडियो को टेक्स्ट में बदलें` / `video se text kaise nikale` (không có chữ YouTube) → **/hi/video-to-text** (upload file từ máy, không dán link)
- ⚠️ **NHÓM NHIỄM NGUY HIỂM NHẤT — tải VIDEO:** `youtube video download` / `यूट्यूब वीडियो डाउनलोड` / `यूट्यूब वीडियो डाउनलोडर` / `youtube se video kaise download kare` / `mp4 download`.
  - **Volume khổng lồ ở Ấn Độ**, SERP hoàn toàn là công cụ tải video. Kéo vào sẽ làm lệch page type ngay lập tức.
  - **QUY TẮC BẮT BUỘC:** `डाउनलोड` chỉ đi với `ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`. **KHÔNG BAO GIỜ** `वीडियो डाउनलोड`.
- `यूट्यूब से MP3 डाउनलोड` → intent tải **âm thanh**, không phải chữ.
- `टेक्स्ट सारांश` / `आर्टिकल का सारांश` / `पैराग्राफ सारांश` → intent tóm tắt **chữ**, không phải video — không thuộc trang này.
- `यूट्यूब पर सबटाइटल कैसे लगाएँ` → hướng dẫn **thao tác trong YouTube**, không phải công cụ.

---

## Internal linking

Section 7 đoạn 2 chứa **cả 3 link**:

- → **/hi/youtube-transcript** — khi cần toàn văn, từng chữ một, không phải ý chính (nhãn `YouTube ट्रांसक्रिप्ट`)
- → **/hi/download-youtube-transcript** — khi cần lưu toàn văn thành file để giữ lại (nhãn `यूट्यूब ट्रांसक्रिप्ट डाउनलोड`, có tân ngữ `ट्रांसक्रिप्ट` neo từ `डाउनलोड`)

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Cấu trúc JSON khớp **100%** với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **8 sections**, `conclusion` h2 + 2 đoạn. **KHÔNG có `specs`.**
  - S1 `content` **3** | S2 `content` **3** | S3 `steps` **4** | S4 `intro` 1 + `items` **4** | S5 `intro` 1 + `items` **4** | S6 `content` **2** | S7 `content` **2** | S8 `items` **8**
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, YouTube, AI, URL**.
  - Ngoại lệ có chủ đích: **`यूट्यूब`** viết Devanagari ở các slot tiêu đề (title, ogTitle, h1, quickAnswer.question, conclusion.h2, FAQ 1) — xem mục "Ghi chú về từ `यूट्यूब` vs `YouTube`" phía trên.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: सारांश, निचोड़, ट्रांसक्रिप्ट, टेक्स्ट, फ़ाइल, लिंक, वीडियो, ब्राउज़र, ओवरव्यू, डिस्क्रिप्शन, पॉडकास्ट, ऑनलाइन, रिकॉर्डिंग, क्रिएटर, मार्केटर, रिसर्चर, प्रोफ़ेशनल.
- Số đếm dùng chữ số Latin (100+, 4) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **`आप`** xuyên suốt, **không** dùng `तू`/`तुम` — nhất quán tuyệt đối với `/hi/video-to-text`, `/hi/download-youtube-transcript`, `/hi/youtube-subtitle-downloader`.
- **Nukta (़) dùng nhất quán:** फ़ाइल, ज़्यादा, सिर्फ़, ज़रूरत, फ़ैसला, फ़र्क़, ख़ुद, ख़र्च, आख़िर, लायक़, क़ीमत, मक़सद, साफ़, फ़ायदा, पैराग्राफ़, कॉन्फ़्रेंस, प्रोफ़ेशनल, सॉफ़्टवेयर, तेज़, चीज़, अंदाज़ा, रिवीज़न, नज़र, ज़रिए.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle`, `hero.*` và mọi `h2`/`h3` **không** chứa Hinglish thô.
- **Tuyệt đối không để chuỗi `वीडियो डाउनलोड` xuất hiện ở bất kỳ đâu trong file.**
- **Tuyệt đối không để chuỗi `सबटाइटल` xuất hiện ở bất kỳ đâu trong file.**
- Internal link `sections[6].content[1]` giữ nguyên cú pháp markdown, đổi path sang `/hi/...`.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** Hindi văn chương nặng (सारसंक्षेप, अभिलेख, प्रतिलिपि) và **tránh** dịch máy word-by-word.

---

## Verify đã chạy

```
python3 shape_check.py en.json hi.json      → True
grep -o 'वीडियो डाउनलोड' hi.json            → rỗng ✅
grep -o 'सबटाइटल' hi.json                   → rỗng ✅
grep -o 'समरी' hi.json                      → rỗng ✅
grep -oE '.{20}डाउनलोड.{20}' hi.json        → 1 hit duy nhất, có tân ngữ ट्रांसक्रिप्ट ✅
```

- **8/8 chuỗi Hinglish có mặt nguyên văn trong tầng meta** ✅
- **0 chuỗi Hinglish lọt ra ngoài block `seo`** ✅ (script quét regex `[a-z]{3,}(?: [a-z]{2,}){2,}` trên toàn bộ `hero`/`sections`/`conclusion` → rỗng)
- **3 internal link đúng path `/hi/`** ✅
