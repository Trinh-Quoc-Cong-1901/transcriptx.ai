🔥 TranscriptX – Instagram Caption Downloader (Hindi / hi)

URL:
/hi/instagram-caption-downloader

Intent chính:

Instagram कैप्शन फ्री में डाउनलोड और कॉपी करें

Trang này là **bản tiếng Hindi** của trang Instagram Caption Downloader. Nhắm đến người dùng Ấn Độ muốn lấy **caption / कैप्शन / विवरण** (phần chữ do tác giả **GÕ** dưới bài đăng) từ Instagram Post, Reel hoặc Video — để sao chép, lưu, dịch, phân tích hoặc tái sử dụng.

Gộp toàn bộ intent đồng nghĩa **डाउनलोड करना / कॉपी करना / सेव करना** vì tất cả cho ra **cùng một kết quả**: caption Instagram → text.

> ⚠️ **PHÂN ĐỊNH INTENT SỐNG CÒN: Caption ≠ Transcript.** Trang này lấy chữ tác giả **VIẾT** (कैप्शन, विवरण, हैशटैग, इमोजी). Trang anh em `/hi/instagram-transcript` lấy chữ người ta **NÓI** trong video (आवाज़, बोले गए शब्द). Section 2 của `en.json` tồn tại chính để phân định điều này — bản `hi` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau.

---

## ⚠️ Lưu ý riêng bản hi — chiến lược Hinglish vs Devanagari

Section `## Hindi (hi)` trong `2_loc_kw.md` có **9 keyword**, và **khác hẳn mọi bản `hi` khác của site**: danh sách này có **CẢ HAI hệ chữ**.

| Dạng | Số lượng | Ví dụ |
| ---- | -------- | ----- |
| **Hinglish (chữ Latin)** | 6 | `instagram se caption copy kaise kare`, `instagram post ka text download` |
| **Devanagari (chữ Hindi thật)** | **3** | `इंस्टाग्राम कैप्शन डाउनलोड कैसे करें`, `इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें`, `इंस्टाग्राम रील्स कैप्शन डाउनलोड करें` |

### 🎯 Đây là ĐIỂM KHÁC BIỆT LỚN NHẤT so với bản `/hi/facebook-transcript`

Trang `/hi/facebook-transcript` có **0 keyword Devanagari** — cả 6 keyword đều là Hinglish. Vì vậy bản Facebook buộc phải **tự dịch 100%** phần Devanagari ở tầng hiển thị, và **không một keyword đã search nào xuất hiện được ở H1/H2** — chỉ nhét được vào meta.

Trang này thì khác: **có 3 cụm Devanagari đã search thật**. Nghĩa là bản `hi` của trang này **làm được điều bản Facebook không làm được**: đặt keyword đã search **nguyên văn vào tầng hiển thị** (H1, quickAnswer, H2, FAQ) mà vẫn giữ chữ Devanagari sạch. Đây là lợi thế phải khai thác triệt để, không được bỏ phí.

### Chiến lược đã chốt — hai tầng, khớp `/hi/facebook-transcript`

Vẫn giữ nguyên khung 2 tầng mà bản Facebook đã chốt (và bản `/hi/audio-to-text` đặt nền), chỉ **mở rộng thêm** cho tình huống có keyword Devanagari:

1. **Tầng hiển thị (`seo.title`, `hero.h1`, mọi `h2`/`h3`, toàn bộ body, FAQ, conclusion): Devanagari 100%.**
   - **Mới so với bản Facebook:** 3 cụm Devanagari đã search được đặt **nguyên văn** vào đây, không phải dịch bổ sung.
   - Tên riêng và định dạng giữ Latin: **TranscriptX, Instagram, Reel, Reels, Carousel, URL**.
2. **Tầng meta (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn nguyên văn 6 chuỗi Hinglish.**
   - Giống hệt cách bản Facebook xử lý. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin nằm ở đó không phá nhịp đọc mà vẫn cho Google khớp lexical chính xác với truy vấn thật.
3. **TUYỆT ĐỐI không chèn Hinglish thô vào `title` / `h1` / `h2` / body.** Một H1 nửa Latin nửa Devanagari trông như trang spam. Quy tắc này giữ y nguyên từ bản Facebook.

> ⚠️ **Về chữ `Instagram` vs `इंस्टाग्राम`:** quy tắc chung của site là giữ tên nền tảng ở dạng Latin (`/hi/facebook-transcript` giữ `Facebook` xuyên suốt). Bản này **giữ `Instagram` Latin ở H1, title và body**, **ngoại trừ** đúng những chỗ đặt 3 keyword Devanagari nguyên văn — ở đó viết `इंस्टाग्राम` đúng như keyword để khớp lexical tuyệt đối. Đây là ngoại lệ có chủ đích, không phải bất nhất.

> ⚠️ **H1 GIỮ KHUNG `डाउनलोड` — đã chốt.** Keyword mạnh nhất là `instagram se caption copy kaise kare` (10–100), intent **COPY**. Nhưng H1 vẫn đóng khung **डाउनलोड करें** để khớp bản EN + URL `/hi/instagram-caption-downloader`. Nhóm `कॉपी` được đưa xuống **H2 section 5 + body** — giống hệt cách `de.json` xử lý `instagram text kopieren`. Đủ trọng số SEO mà không đánh đổi độ chính xác của page type.

> ⚠️ **H1 BẮT BUỘC chứa keyword tiếng Hindi đã search.** **KHÔNG** được để nguyên tên tiếng Anh `Instagram Caption Downloader` làm H1 — như vậy H1 bắt được **0 keyword**. H1 đúng: **`Instagram कैप्शन डाउनलोड करें`**. So sánh: bản `de` H1 = `Instagram Caption herunterladen` (đã Đức hóa động từ), bản `hi` phải Hindi hóa tương ứng.

---

## Từ khóa chính

**instagram se caption copy kaise kare** (10–100) ✅ *đã search* — keyword mạnh nhất, band cao nhất trong cả 9 keyword.

> Intent là **COPY**, không phải download. Theo quyết định đã chốt: chuỗi Hinglish này đặt ở `seo.description` (slot meta mạnh nhất), còn **nghĩa** của nó (कॉपी करें) được cấp hẳn **H2 section 5** dưới dạng Devanagari.

## Từ khóa chính ở tầng hiển thị (H1)

**इंस्टाग्राम कैप्शन डाउनलोड कैसे करें** (0–10) ✅ *đã search, Devanagari* — trục download, khớp URL và bản EN.

> Dạng dùng ở H1: **Instagram कैप्शन डाउनलोड करें**
> Dạng nguyên văn keyword đặt ở **`quickAnswer.question`**: `इंस्टाग्राम कैप्शन डाउनलोड कैसे करें?`

---

## Từ khóa phụ

### Nhóm Devanagari — ĐÃ SEARCH, đặt nguyên văn ở tầng hiển thị 🇮🇳

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| इंस्टाग्राम कैप्शन डाउनलोड कैसे करें | 0–10 | ✅ đã search — **Devanagari** → `quickAnswer.question` + H2 section 3 |
| इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें | 0–10 | ✅ đã search — **Devanagari** → **H2 section 5** |
| इंस्टाग्राम रील्स कैप्शन डाउनलोड करें | 0–10 | ✅ đã search — **Devanagari** → section 4 (item hashtag) + FAQ 3 |

### Nhóm Copy / कॉपी (volume cao nhất — dồn vào section 5)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram se caption copy kaise kare | 10–100 | ✅ đã search — **Hinglish** → `seo.description` |
| instagram caption copy kare | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें | 0–10 | ✅ đã search — **Devanagari** → H2 section 5 |

### Nhóm Download / डाउनलोड (trục chính, khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram post caption download kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.description` |
| instagram caption download link se | 0–10 | ✅ đã search — **Hinglish** → `seo.ogDescription` |
| इंस्टाग्राम कैप्शन डाउनलोड कैसे करें | 0–10 | ✅ đã search — **Devanagari** → quickAnswer + H2 section 3 |
| इंस्टाग्राम रील्स कैप्शन डाउनलोड करें | 0–10 | ✅ đã search — **Devanagari** → section 4 + FAQ 3 |

### Nhóm Text / Save (टेक्स्ट, सेव)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram post ka text download | 0–10 | ✅ đã search — **Hinglish** → `seo.schemaDescription` |
| instagram caption save kaise kare | 0–10 | ✅ đã search — **Hinglish** → `seo.schemaDescription` |

### Dịch bổ sung (chỉ rải trong body, KHÔNG đặt vào title/H1)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| Instagram कैप्शन डाउनलोडर | — | 🔄 dịch bổ sung (tên công cụ) |
| Instagram विवरण डाउनलोड करें | — | 🔄 dịch bổ sung (instagram description download) |
| Instagram वीडियो कैप्शन डाउनलोड | — | 🔄 dịch bổ sung (instagram video caption download) |
| Instagram हैशटैग कॉपी करें | — | 🔄 dịch bổ sung (keep the hashtag set) |
| Instagram कैप्शन ऑनलाइन डाउनलोड | — | 🔄 dịch bổ sung (caption download online) |
| लिंक से Instagram कैप्शन निकालें | — | 🔄 dịch bổ sung (extract via link) |
| बिना ऐप Instagram कैप्शन कॉपी | — | 🔄 dịch bổ sung (no install) |

**Nguyên tắc dùng:** ✅ *đã search, Devanagari* = ưu tiên tuyệt đối, đặt **nguyên văn** vào `h1`/`quickAnswer`/`h2`/FAQ. ✅ *đã search, Hinglish* = đặt **nguyên văn** vào `seo.description` / `ogDescription` / `schemaDescription`, **không** vào body. 🔄 *dịch bổ sung* = chỉ rải trong body.

---

## Search Intent

Người dùng Ấn Độ thấy một caption Instagram hay (của mình hoặc của đối thủ) và muốn lấy nguyên văn phần chữ đó ra ngoài app — vì Instagram **không có nút copy caption**, và bôi đen trên điện thoại thì rất khó, hay dính nhầm chỗ.

Họ thường kỳ vọng:

- Chỉ cần dán link bài đăng, không đăng nhập Instagram.
- Lấy **nguyên vẹn** hashtag, emoji và ngắt dòng — không bị gộp thành một cục.
- Chạy được với Post ảnh, Carousel, Reel và Video.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — phần lớn người Ấn mở Instagram bằng app rồi copy link sang trình duyệt.
- Copy được ngay để dán sang chỗ khác, hoặc dịch sang tiếng Hindi/tiếng Anh.

### Khác biệt so với bản tiếng Anh

1. **Intent `कॉपी` mạnh hơn `डाउनलोड`.** Bản EN đóng khung là "downloader" và toàn bộ cụm download đều có volume thật (10K–100K cho KW chính). Bản `hi` thì ngược: keyword duy nhất vượt band `0–10` là `instagram se caption copy kaise kare` (10–100) — intent **copy**. Đã xử lý bằng cách giữ H1 download nhưng cấp hẳn **H2 section 5** cho nhóm `कॉपी` (đúng như bản `de` làm với `text kopieren`).
2. **Keyword tồn tại ở HAI hệ chữ cùng lúc — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ. Bản `hi`: 6 keyword Latin (Hinglish) + 3 keyword Devanagari. Bắt buộc tách hai tầng (meta = Hinglish, hiển thị = Devanagari) — một quyết định biên tập không tồn tại ở bản EN hay bất kỳ ngôn ngữ châu Âu nào của trang này.
3. **Bản `hi` này ĐẶT ĐƯỢC keyword đã search vào H1/H2 — bản `hi` của Facebook thì không.** Facebook `hi` có 0 keyword Devanagari nên H1 hoàn toàn là dịch bổ sung. Ở đây 3 cụm Devanagari cho phép H1/quickAnswer/H2 section 5/FAQ 3 khớp lexical trực tiếp. Đây là điểm mạnh riêng phải nói rõ để không ai "dịch lại" 3 cụm đó cho mượt hơn.
4. **`फ्री / मुफ़्त` phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần từ `फ्री` xuất hiện ở `title`, `description`, `hero.subtitle`, FAQ 1 và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
5. **`रील्स` viết Devanagari khi nằm trong keyword, `Reels` viết Latin ở mọi chỗ khác.** Keyword `इंस्टाग्राम रील्स कैप्शन डाउनलोड करें` dùng `रील्स`; phần còn lại của trang giữ `Reel`/`Reels` Latin theo quy tắc site.
6. **Trộn thuật ngữ tiếng Anh là chuẩn, không phải lỗi.** Người Ấn viết web thật sự dùng `कैप्शन`, `हैशटैग`, `इमोजी`, `लिंक`, `पेस्ट`, `कॉपी`, `डाउनलोड`, `ब्राउज़र`. **Tránh** Hindi văn chương (`शीर्षक`, `अनुशीर्षक`, `विवरणिका`) — không ai search và không ai đọc như vậy.

---

## Đối tượng người dùng

- Social media manager / marketing Ấn Độ (phân tích caption đối thủ)
- Content creator Hindi (lưu swipe file caption hiệu quả)
- Freelancer làm Instagram cho khách hàng địa phương
- Chủ shop nhỏ / doanh nghiệp bán hàng qua Instagram
- Người muốn dịch caption tiếng Anh sang Hindi (hoặc ngược lại)
- Người lưu lại caption trước khi bài bị sửa/xóa
- Sinh viên / người học content marketing nghiên cứu hook và CTA
- Người sưu tầm bộ hashtag để dùng lại cho bài của mình

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, đúng 2 đoạn `conclusion`. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Instagram कैप्शन डाउनलोड करें | इंस्टाग्राम कैप्शन डाउनलोड कैसे करें ✅ *(Devanagari, dạng rút gọn)* |
| — | **quickAnswer** | **इंस्टाग्राम कैप्शन डाउनलोड कैसे करें?** ✅ *(Devanagari, nguyên văn 100%)* |
| 1 | Instagram कैप्शन डाउनलोडर क्या करता है | Instagram कैप्शन डाउनलोडर 🔄, Instagram वीडियो कैप्शन डाउनलोड 🔄, Instagram विवरण डाउनलोड करें 🔄 |
| 2 | कैप्शन या ट्रांसक्रिप्ट: आपको क्या चाहिए? | *(phân định + internal link `[Instagram Transcript](/hi/instagram-transcript)`)* |
| 3 | **इंस्टाग्राम कैप्शन डाउनलोड कैसे करें** | **इंस्टाग्राम कैप्शन डाउनलोड कैसे करें ✅ (Devanagari, nguyên văn ở H2)**, लिंक से Instagram कैप्शन निकालें 🔄 |
| 4 | डाउनलोड किए हुए कैप्शन का क्या करें | **इंस्टाग्राम रील्स कैप्शन डाउनलोड करें ✅ (Devanagari, item 5)**, Instagram हैशटैग कॉपी करें 🔄, Instagram विवरण डाउनलोड करें 🔄 |
| 5 | **इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें — हैशटैग, इमोजी और फ़ॉर्मैटिंग जस के तस** | **इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें ✅ (Devanagari, nguyên văn ở H2)** + van xả cho toàn bộ nhóm copy |
| 6 | अक्सर पूछे जाने वाले सवाल | **इंस्टाग्राम रील्स कैप्शन डाउनलोड करें ✅ (FAQ 3)**, Instagram कैप्शन ऑनलाइन डाउनलोड 🔄, बिना ऐप Instagram कैप्शन कॉपी 🔄 + long-tail |
| — | **conclusion** | Instagram कैप्शन डाउनलोड करें ✅, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **6 chuỗi Hinglish nằm HOÀN TOÀN ở tầng meta, không một chuỗi nào trong `hero`/`sections`/`conclusion`:**
  - `seo.description` → `instagram se caption copy kaise kare` *(KW mạnh nhất)* + `instagram post caption download kaise kare`
  - `seo.ogDescription` → `instagram caption copy kare` + `instagram caption download link se`
  - `seo.schemaDescription` → `instagram post ka text download` + `instagram caption save kaise kare`
- **3 cụm Devanagari đặt NGUYÊN VĂN, không sửa một chữ:**
  - `इंस्टाग्राम कैप्शन डाउनलोड कैसे करें` → `quickAnswer.question` (thêm dấu `?`) **và** `sections[2].h2` (H2 section 3). Đặt hai chỗ vì đây là dạng how-to, khớp cả quick answer lẫn section hướng dẫn.
  - `इंस्टाग्राम पोस्ट का कैप्शन कॉपी करें` → `sections[4].h2` (H2 section 5). Bản EN section này vốn nói về "what you copy reads the same as what was on the post" — đưa cụm copy lên đây là **bám đúng nghĩa gốc**, không phải nhét keyword. Giống hệt cách `de.json` xử lý.
  - `इंस्टाग्राम रील्स कैप्शन डाउनलोड करें` → `sections[3].items[4].content` (item "Keep the hashtag set" — đúng chỗ `de.json` đặt `Instagram Reels Caption speichern`) **và** FAQ 3 (câu hỏi về Reel/video).
- Section 2 giữ nguyên vai trò phân định Caption/Transcript. Link nội bộ: `[Instagram Transcript](/hi/instagram-transcript)`.
- Bản EN section 3 step 1 nhắc "three-dot menu / desktop URL" — bản `hi` giữ nguyên ý nhưng diễn đạt theo thực tế mobile-first của Ấn Độ (copy link từ app điện thoại), **vẫn không thêm câu**.
- `विवरण` (description) dùng xen kẽ với `कैप्शन` tối thiểu 3 lần trong body (section 1, section 2, FAQ 1) để phủ nhóm `instagram description download`.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `instagram video se text nikale` / `इंस्टाग्राम वीडियो का ट्रांसक्रिप्ट` / `रील को टेक्स्ट में बदलें` → **/hi/instagram-transcript** (chữ **NÓI**, không phải chữ **VIẾT**)
- `youtube video ka transcript` / `यूट्यूब ट्रांसक्रिप्ट` → **/hi/youtube-transcript**
- `tiktok video se text nikale` / `टिकटॉक ट्रांसक्रिप्ट` → **/hi/tiktok-transcript**
- `audio ko text me kaise badle` / `ऑडियो को टेक्स्ट में बदलें` → **/hi/audio-to-text**
- ⚠️ **NHÓM NHIỄM NGUY HIỂM NHẤT — tải VIDEO:** `instagram video download` / `instagram reels download` / `इंस्टाग्राम वीडियो डाउनलोड` / `रील्स डाउनलोड` / `instagram downloader` / `reels download karne wala app`.
  - Ở Ấn Độ nhóm này có **volume khổng lồ** (gấp hàng nghìn lần mọi keyword caption) và SERP **hoàn toàn** là downloader video/reels. Kéo vào sẽ làm lệch page type ngay lập tức và làm trang mất hẳn cơ hội xếp hạng cho intent caption.
  - Nguy hiểm gấp bội bản `de`/`fr` vì tiếng Hindi dùng chung đúng một từ `डाउनलोड` cho cả hai intent, trong khi tiếng Đức còn phân biệt được `herunterladen` + tân ngữ.
  - **QUY TẮC BẮT BUỘC KHI DỊCH:** mọi chỗ có `डाउनलोड` **phải luôn** đi kèm tân ngữ `कैप्शन` / `विवरण` / `टेक्स्ट`. **KHÔNG BAO GIỜ** viết `वीडियो डाउनलोड करें`, `रील डाउनलोड करें` hay `Instagram डाउनलोड` đứng trơ trọi — kể cả trong FAQ hay conclusion.
- `instagram bio copy kare` / `instagram comment copy` → tuy gần nhóm copy nhưng khác đối tượng, không tối ưu riêng
- `instagram caption ideas` / `कैप्शन आइडियाज` / `attitude caption hindi` → intent **sáng tạo caption mới**, ngược hoàn toàn với trang này (trang này **lấy** caption có sẵn). Volume rất lớn ở Ấn Độ nhưng tuyệt đối không chạm.

---

## Internal linking

- ↔ **/hi/instagram-transcript** (khi user muốn chữ **NÓI** trong Reel/Video thay vì caption viết) — đây là link quan trọng nhất, nằm ở **section 2**
- → /hi/youtube-transcript, /hi/tiktok-transcript (cross-cluster)
- → /hi/facebook-transcript (cùng cụm mạng xã hội tiếng Hindi)

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**, `conclusion` h2 + 2 đoạn.
  - Section 1: `content` 3 | Section 2: `intro` 1 + `items` 2 | Section 3: `steps` 4 | Section 4: `intro` 1 + `items` 5 | Section 5: `content` 3 | Section 6: `items` **8** (q/a)
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, Instagram, Reel, Reels, Carousel, URL**. Ngoại lệ duy nhất: bên trong 3 keyword Devanagari nguyên văn thì viết `इंस्टाग्राम` và `रील्स` đúng như keyword.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: कैप्शन, विवरण, हैशटैग, इमोजी, टेक्स्ट, लिंक, पेस्ट, कॉपी, डाउनलोड, सेव, ब्राउज़र, अनुवाद, पोस्ट, क्रिएटर.
- Xưng hô: dùng thể lịch sự **`आप`** xuyên suốt, **không** dùng `तू`/`तुम` — nhất quán tuyệt đối với `/hi/facebook-transcript` và `/hi/audio-to-text`.
- Nukta (़) dùng nhất quán: फ़ॉर्मैट, ज़्यादा, सिर्फ़, ज़रूरत, फ़ाइल, तरीक़ा → thống nhất với `/hi/facebook-transcript`.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `hero.h1` và mọi `h2`/`h3` **không** chứa Hinglish thô.
- Internal link section 2 giữ nguyên cú pháp markdown, đổi path: `[Instagram Transcript](/hi/instagram-transcript)`.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** dịch máy word-by-word và **tránh** Hindi văn chương nặng.
