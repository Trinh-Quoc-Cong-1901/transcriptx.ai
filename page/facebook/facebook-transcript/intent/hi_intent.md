🔥 TranscriptX – Facebook Transcript (Hindi / hi)

URL:
/hi/facebook-transcript

Intent chính:

Facebook वीडियो का ट्रांसक्रिप्ट फ्री में पाएँ (ऑनलाइन, बिना साइन-अप)

Trang này là **bản tiếng Hindi của trang trụ (hub)** cụm Facebook. Nhắm đến người dùng Ấn Độ có một video Facebook (bài đăng video, Reel, Watch, bản Facebook Live đã lưu, video trong group/page) và muốn dán link để lấy toàn bộ lời nói thành văn bản — để đọc, sao chép, chỉnh sửa, trích dẫn hoặc lưu lại.

Gộp toàn bộ intent đồng nghĩa **transcript निकालना / टेक्स्ट में बदलना / टेक्स्ट निकालना** vì tất cả cho ra **cùng một kết quả**: video Facebook → text.

---

## ⚠️ CẢNH BÁO QUAN TRỌNG — đây là ngôn ngữ có dữ liệu keyword mỏng nhất của trang này

Section `## Hindi (hi)` trong `2_loc_kw.md` **chỉ có 6 keyword**, và **cả 6 đều ở mức `0 – 10`**:

| # | Keyword (nguyên dạng) | Volume |
| - | --------------------- | ------ |
| 1 | facebook video ko text me kaise badle | 0 – 10 |
| 2 | facebook video se text nikale | 0 – 10 |
| 3 | facebook video ki transcript kaise nikale | 0 – 10 |
| 4 | facebook video ka transcript | 0 – 10 |
| 5 | facebook video se subtitle kaise nikale | 0 – 10 |
| 6 | facebook reel ko text me kaise badle | 0 – 10 |

So sánh trong cùng file `2_loc_kw.md`: `es` có 14 kw với 2 kw ở mức 100–1K; `ar` có 14 kw; `id`/`ms`/`it`/`pt` mỗi bản 13–14 kw và đều có ít nhất 1 kw ở mức 10–100. Bản `hi` **ít keyword nhất (6)** và **không có một keyword nào vượt mức 0–10** — mỏng nhất về cả số lượng lẫn volume.

### Hệ quả trực tiếp lên nội dung

- 6 keyword **không đủ để phủ 9 section**. Trung bình mỗi keyword phải "gánh" 1,5 section, trong khi bản `es`/`ar` có 14 keyword cho cùng 9 section.
- Buộc phải **dịch bổ sung nhiều hơn hẳn các ngôn ngữ khác**. Tỉ lệ mục tiêu của trang này:
  - **6 keyword ✅ đã search** (thực tế dùng được cho intent chính: **5** — xem mục loại trừ)
  - **~14 cụm 🔄 dịch bổ sung** (Devanagari, dịch tự nhiên từ bản EN)
  - → tỉ lệ xấp xỉ **30% đã search / 70% dịch bổ sung**, ngược hẳn với bản `ar` và `es` (khoảng **80% / 20%**).
- Không có nhóm keyword thứ hai đủ mạnh để "gánh" một H2 riêng (như `تفريغ` của bản `ar` hay `a texto` của bản `es`). Vì vậy **H2 bám sát bản dịch tự nhiên của EN**, không đảo cấu trúc để chạy theo keyword.

**Nhận định (giống bản audio-to-text tiếng Hindi):** volume gần 0 **KHÔNG** có nghĩa thị trường Ấn Độ nhỏ. Người Ấn Độ tìm chủ đề công nghệ này chủ yếu **bằng tiếng Anh** (`facebook transcript`, `facebook video to text`) — traffic Ấn Độ đã nằm sẵn trong `en.json`. Bản `hi` xếp **ưu tiên THẤP** về ROI keyword, vẫn nên làm vì tín hiệu hreflang/UX, chi phí biên thấp và hỗ trợ AI/GEO trả lời truy vấn tiếng Hindi.

---

## ⚠️ Toàn bộ 6 keyword ở dạng Hinglish (chữ Latin), KHÔNG có keyword Devanagari nào

Đây là điểm khác biệt lớn nhất giữa bản `hi` của trang này và **mọi ngôn ngữ khác** trong `2_loc_kw.md`. Bản `ar` 100% chữ Ả Rập, `ja` 100% kana/kanji, `ko` 100% hangul — riêng `hi` là **100% Romanized Hindi (Hinglish)**: `facebook video ko text me kaise badle`, `facebook video ka transcript`...

Lý do: bàn phím Devanagari không phải mặc định trên điện thoại Ấn Độ, và toàn bộ thuật ngữ của chủ đề này (facebook, video, text, transcript, subtitle, reel) vốn đã là từ tiếng Anh — người dùng gõ thẳng bằng chữ Latin nhanh hơn nhiều.

### Chiến lược đã chốt — KHỚP với `/hi/audio-to-text`

Trang `audio-to-text` tiếng Hindi đã giải quyết đúng bài toán này và chốt 3 quy tắc (xem `audio-to-text/intent/hi_intent.md`, mục "Lưu ý về Hinglish"):

1. **Giữ nguyên dạng Latin khi liệt kê keyword**, không chuyển sang Devanagari trong file intent.
2. **Body viết bằng Devanagari** — nhồi Hinglish vào văn bản Devanagari "trông rất lạ và làm giảm chất lượng nội dung".
3. **Bắt Hinglish qua meta / URL / anchor ở tầng kỹ thuật, không qua body copy.**

Trang Facebook này **áp dụng nguyên si 3 quy tắc đó**, chỉ mở rộng thêm cho tình huống 100% keyword là Hinglish:

- **Tầng hiển thị (title, H1, tất cả H2/H3, toàn bộ body, FAQ, conclusion): Devanagari 100%.** Tên riêng và định dạng giữ Latin (TranscriptX, Facebook, Reels, Watch, Live, TXT, DOCX, PDF, SRT, VTT) — đúng như `audio-to-text/hi.json` đã làm với YouTube, TikTok, MP3, ChatGPT.
- **Tầng meta (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn nguyên văn chuỗi Hinglish.** Đây chính là "tầng kỹ thuật" mà trang audio-to-text chỉ định. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin nằm ở đó không phá nhịp đọc, mà vẫn cho Google một khớp lexical chính xác với truy vấn thật.
- **`seo.title`, `hero.h1`, mọi `h2`/`h3`: TUYỆT ĐỐI không chèn Hinglish thô.** Đây là điểm khác với bản `ar`/`es` (nơi keyword đã search được đặt thẳng vào title/H1) — vì ở bản `hi`, làm vậy sẽ tạo ra một H1 nửa Latin nửa Devanagari, trông như trang spam.

**Lý do chọn cách này thay vì 2 phương án còn lại:**

| Phương án | Vì sao loại |
| --------- | ----------- |
| Viết toàn bộ body bằng Hinglish (khớp 100% keyword) | Trái hoàn toàn với `/hi/audio-to-text` (đã chốt Devanagari), phá vỡ tính nhất quán của cả site tiếng Hindi; hreflang `hi` mà nội dung là chữ Latin sẽ gây tín hiệu ngôn ngữ mâu thuẫn. |
| Bỏ hẳn Hinglish, chỉ Devanagari | Thì **0/6 keyword đã search xuất hiện ở bất kỳ đâu** — mất trắng lớp dữ liệu duy nhất có được cho tiếng Hindi. |
| ✅ Devanagari ở body + Hinglish ở meta | Giữ chất lượng đọc, giữ nhất quán với audio-to-text, vẫn phủ được 5/6 keyword đã search. |

---

## Từ khóa chính

**facebook video ka transcript** (0–10) ✅ *đã search*

> Chọn KW này vì: (a) là **dạng danh từ**, khớp đúng vai trò **trang trụ** của cụm Facebook (tương ứng `facebook transcript` của bản EN); (b) chứa từ `transcript` — trục ngữ nghĩa của cả cụm; (c) các KW còn lại đều là **dạng câu hỏi how-to**, hợp với `quickAnswer`/FAQ hơn là với `title`/`H1`.
>
> Dạng Devanagari dùng ở title/H1/body: **Facebook वीडियो का ट्रांसक्रिप्ट**
> Dạng Hinglish `facebook video ka transcript` đặt ở `seo.ogDescription`.

*(KW chính thứ hai — dùng cho `quickAnswer` và section 3: `facebook video ko text me kaise badle` → **Facebook वीडियो को टेक्स्ट में कैसे बदलें**.)*

---

## Từ khóa phụ

### Nhóm Transcript (ट्रांसक्रिप्ट — trục chính, tương ứng "facebook transcript")

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook video ka transcript | 0–10 | ✅ đã search *(KW chính)* → **Facebook वीडियो का ट्रांसक्रिप्ट** |
| facebook video ki transcript kaise nikale | 0–10 | ✅ đã search → **Facebook वीडियो की ट्रांसक्रिप्ट कैसे निकालें** |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो ट्रांसक्रिप्शन** (facebook video transcription) |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो ट्रांसक्राइब करें** (transcribe facebook video) |
| — | — | 🔄 dịch bổ sung: **फ्री Facebook ट्रांसक्रिप्ट** (facebook transcript free) |

### Nhóm Text conversion (टेक्स्ट में बदलना / टेक्स्ट निकालना — tương ứng "facebook video to text")

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook video ko text me kaise badle | 0–10 | ✅ đã search → **Facebook वीडियो को टेक्स्ट में कैसे बदलें** |
| facebook video se text nikale | 0–10 | ✅ đã search → **Facebook वीडियो से टेक्स्ट निकालें** |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो को टेक्स्ट में बदलें** (facebook video to text) |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो का टेक्स्ट** (text of a facebook video) |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो की आवाज़ को टेक्स्ट में बदलें** (facebook video audio to text) |

### Nhóm Định dạng nội dung Facebook (Reel / Live)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook reel ko text me kaise badle | 0–10 | ✅ đã search → **Facebook Reel को टेक्स्ट में कैसे बदलें** |
| — | — | 🔄 dịch bổ sung: **Facebook Live को टेक्स्ट में बदलें** (transcribe facebook live) |
| — | — | 🔄 dịch bổ sung: **सेव किया हुआ Facebook Live ट्रांसक्राइब करें** (saved facebook live) |
| — | — | 🔄 dịch bổ sung: **Facebook ग्रुप और पेज के वीडियो का ट्रांसक्रिप्ट** (group/page videos) |

### Nhóm Công cụ / AI / Free

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **Facebook ट्रांसक्रिप्ट जनरेटर** (facebook transcript generator) |
| — | — | 🔄 dịch bổ sung: **AI से Facebook वीडियो ट्रांसक्राइब करें** (facebook transcript ai) |
| — | — | 🔄 dịch bổ sung: **Facebook वीडियो ट्रांसक्रिप्ट ऑनलाइन** (facebook transcript online) |
| — | — | 🔄 dịch bổ sung: **बिना साइन-अप Facebook ट्रांसक्रिप्ट** (no sign-up) |

### Nhóm lân cận — dùng HẠN CHẾ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook video se subtitle kaise nikale | 0–10 | ⚠️ ✅ đã search nhưng là intent **phụ đề** → **Facebook वीडियो से सबटाइटल कैसे निकालें** |

> ⚠️ **Xử lý `facebook video se subtitle kaise nikale`:** đây là intent **tạo/lấy phụ đề**, lân cận chứ không trùng intent trang (video → transcript). Giữ lại vì TranscriptX thật sự xuất SRT/VTT, nhưng **CHỈ dùng trong body (section 7 — nói về xuất SRT/VTT) và FAQ (câu 5, câu 9)**, dưới dạng Devanagari `सबटाइटल`. **KHÔNG** đặt vào `seo.title`, `hero.h1` hay bất kỳ `h2` nào, và **không** chèn chuỗi Hinglish của nó vào meta — 3 slot meta được dành cho 5 keyword đúng intent chính.

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, dạng Devanagari phải xuất hiện trong `title`/`h1`/`h2`, dạng Hinglish nguyên văn phải xuất hiện trong `seo.description`/`ogDescription`/`schemaDescription`. 🔄 *dịch bổ sung* = chỉ rải trong body để phủ ngữ nghĩa, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Ấn Độ có một video Facebook — thường là **bản Facebook Live đã lưu** (lớp học online, coaching class, satsang/pravachan, webinar, Q&A của page), video trong group, hoặc Reel — và muốn lấy nội dung lời nói thành text để đọc, tìm kiếm, ghi chú, trích dẫn hoặc lưu trước khi bị xóa.

Họ thường kỳ vọng:

- Chỉ cần **dán link**, không tải file, không cài app.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — phần lớn người dùng Ấn Độ mở Facebook bằng app điện thoại, rồi copy link sang trình duyệt.
- Chạy được cả khi video **không có phụ đề** sẵn.
- Nhận dạng được **tiếng Hindi** và tiếng Anh giọng Ấn, cũng như các thứ tiếng vùng miền khác.
- Tách được nhiều người nói (quan trọng với Live / phỏng vấn / thảo luận nhóm).
- Không cần đăng nhập Facebook.

### Khác biệt so với bản tiếng Anh

1. **Không có keyword nào đủ mạnh để "gánh" H2 — ngược hẳn bản `ar`/`es`.** Bản EN có `facebook transcript` (1K–10K) và `facebook transcript generator` (1K–10K) là hai trục song song, đủ mạnh để mỗi trục có H2 riêng. Bản `hi` chỉ có 6 keyword cùng mức 0–10, không có trục thứ hai. Hệ quả: H2 của bản `hi` **dịch sát bản EN**, không được viết lại để chạy theo một nhóm keyword — vì không có nhóm nào đáng để chạy theo.
2. **Keyword tồn tại ở dạng chữ viết khác với nội dung — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ. Bản `hi`: keyword là Latin (Hinglish), body là Devanagari. Bắt buộc phải tách hai tầng (meta = Hinglish, body = Devanagari) — một quyết định biên tập không tồn tại ở bất kỳ ngôn ngữ nào khác của trang này.
3. **"फ्री / मुफ़्त" phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần từ "फ्री" xuất hiện ở `title`, `description`, `hero.subtitle`, section 4 và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
4. **Facebook Live nặng ký hơn, và Reel có keyword riêng.** Bản EN xử lý Live và Reels ngang nhau trong section 6. Bản `hi` có hẳn `facebook reel ko text me kaise badle` — item Reels ở section 6 phải viết dày dặn ngang item Live, đặt nguyên cụm Devanagari tương ứng vào đó.
5. **Trộn thuật ngữ tiếng Anh là chuẩn, không phải lỗi.** Người Ấn viết web thật sự dùng "वीडियो", "टेक्स्ट", "ट्रांसक्रिप्ट", "लिंक", "पेस्ट", "ब्राउज़र", "डाउनलोड". **Tránh** Hindi văn chương ("दृश्य-श्रव्य", "पाठ", "प्रतिलेखन") — không ai search và không ai đọc như vậy. Giống hệt quy tắc của `/hi/audio-to-text`.

---

## Đối tượng người dùng

- Sinh viên / học viên coaching class xem lớp học phát trên Facebook Live
- Người xem Facebook Live tôn giáo (satsang, pravachan, kirtan) và nội dung cộng đồng
- Admin group / page Facebook tiếng Hindi
- Marketing / Social media / Community manager
- Nhà báo, phóng viên cần trích dẫn phát biểu từ video Facebook
- Content creator tái sử dụng nội dung (Reel → post, thread, blog)
- Giáo viên, nhà nghiên cứu cần ghi chú từ webinar/panel
- Người cần lưu nội dung video trước khi bị xóa
- Người khiếm thính hoặc ở nơi không bật được tiếng

---

## Map H2 → keyword (bám ĐÚNG 9 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng 9 section của `en.json`, cùng số đoạn `content`, đúng 10 `specs`, đúng 4 `steps`, đúng 5 `items` ở section 6, đúng 9 FAQ, đúng 2 đoạn `conclusion`. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Facebook वीडियो का ट्रांसक्रिप्ट | facebook video ka transcript ✅ *(dạng Devanagari; dạng Hinglish ở ogDescription)* |
| — | **quickAnswer** | facebook video ki transcript kaise nikale ✅ → **Facebook वीडियो की ट्रांसक्रिप्ट कैसे निकालें?** |
| 1 | Facebook ट्रांसक्रिप्ट क्या है? | facebook video ka transcript ✅, facebook video se text nikale ✅, Facebook वीडियो ट्रांसक्रिप्शन 🔄 |
| 2 | एक नज़र में Facebook ट्रांसक्रिप्ट | *(bảng thông số — फ्री / 100+ भाषाएँ / बिना साइन-अप)* |
| 3 | Facebook वीडियो को टेक्स्ट में कैसे बदलें | facebook video ko text me kaise badle ✅, facebook video ki transcript kaise nikale ✅ |
| 4 | बिना कैप्शन वाला Facebook ट्रांसक्रिप्ट जनरेटर | Facebook ट्रांसक्रिप्ट जनरेटर 🔄, AI से Facebook वीडियो ट्रांसक्राइब करें 🔄, Facebook वीडियो की आवाज़ को टेक्स्ट में बदलें 🔄 |
| 5 | Facebook वीडियो से टेक्स्ट निकालें | facebook video se text nikale ✅, Facebook वीडियो को टेक्स्ट में बदलें 🔄, Facebook वीडियो का टेक्स्ट 🔄 |
| 6 | Facebook पर आप क्या-क्या ट्रांसक्राइब कर सकते हैं | facebook reel ko text me kaise badle ✅ *(item 3)*, Facebook Live को टेक्स्ट में बदलें 🔄 *(item 1)* |
| 7 | कॉपी करें, एडिट करें, अनुवाद करें या डाउनलोड करें | *(internal link sang /hi/youtube-transcript, /hi/tiktok-transcript, /hi/audio-to-text)* + सबटाइटल ⚠️ *(SRT/VTT)* |
| 8 | सटीकता और भाषाएँ | Facebook वीडियो ट्रांसक्रिप्शन 🔄 *(+ nhấn tiếng Hindi và các tiếng vùng miền Ấn Độ)* |
| 9 | अक्सर पूछे जाने वाले सवाल | फ्री Facebook ट्रांसक्रिप्ट 🔄, Facebook वीडियो ट्रांसक्रिप्ट ऑनलाइन 🔄, सबटाइटल ⚠️ *(FAQ 5 + FAQ 9)* + long-tail |
| — | **conclusion** | facebook video ka transcript ✅, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **Toàn bộ 5 chuỗi Hinglish đúng intent nằm ở tầng meta, không ở body:** `facebook video ko text me kaise badle` → `seo.description`; `facebook video ka transcript` → `seo.ogDescription`; `facebook video se text nikale`, `facebook video ki transcript kaise nikale`, `facebook reel ko text me kaise badle` → `seo.schemaDescription`. Không chuỗi Hinglish nào được xuất hiện trong `hero`, `sections` hay `conclusion`.
- Nỗi lo "công cụ có nhận dạng được **tiếng Hindi** không" xử lý **bên trong section 8**, bằng cách thay ví dụ ngôn ngữ của bản EN (Spanish Live / Tagalog Reel) bằng ví dụ có tiếng Hindi và một tiếng vùng miền Ấn Độ — **không thêm câu, không thêm H2**.
- Cụm `Facebook Live को टेक्स्ट में बदलें` 🔄 đặt vào **item số 1 của section 6** (Saved Facebook Live) — đúng chỗ, không cần section mới.
- Keyword `facebook reel ko text me kaise badle` (dạng Devanagari **Facebook Reel को टेक्स्ट में कैसे बदलें**) đặt vào **item số 3 của section 6** (Reels), viết nguyên cụm.
- `सबटाइटल` chỉ xuất hiện ở **section 7** (đoạn nói về xuất SRT/VTT) và **FAQ 5 / FAQ 9** — đúng chỗ bản EN đã có sẵn nội dung về captions và export. Không đẩy lên H2.
- Bản EN section 3 step 1 nhắc "three-dot menu / address bar" — bản `hi` giữ nguyên ý nhưng diễn đạt theo thực tế mobile-first của Ấn Độ (copy link từ app điện thoại), **vẫn không thêm câu**.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- youtube video ka transcript / यूट्यूब वीडियो को टेक्स्ट में बदलें → **/hi/youtube-transcript**
- tiktok video se text nikale / टिकटॉक ट्रांसक्रिप्ट → **/hi/tiktok-transcript**
- audio ko text me kaise badle / ऑडियो को टेक्स्ट में बदलें / MP3 को टेक्स्ट में बदलें → **/hi/audio-to-text** (nguồn là **file âm thanh**, không phải video Facebook)
- voice ko text me kaise badle / बोलकर लिखना / डिक्टेशन → **/hi/voice-to-text**
- facebook video download kaise kare / फेसबुक वीडियो डाउनलोड → intent **tải video**, KHÔNG phải transcript. Đây là nhóm nhiễm nguy hiểm nhất của cụm Facebook tiếng Hindi vì volume rất lớn và SERP hoàn toàn là downloader — kéo vào sẽ làm lệch page type.
- टेक्स्ट को आवाज़ में बदलें / टेक्स्ट टू स्पीच → **NGƯỢC intent**, thuộc trang Text-to-Speech

---

## Internal linking

- ↔ /hi/youtube-transcript, /hi/tiktok-transcript (cross-cluster: cùng nhu cầu transcript, nền tảng khác)
- → /hi/audio-to-text (khi user có file âm thanh thay vì video Facebook)

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, TXT, DOCX, PDF, SRT, VTT, Facebook, Reel/Reels, Watch, Live, URL**. Đây là quy tắc đã dùng ở `audio-to-text/hi.json` (YouTube, TikTok, MP3, ChatGPT giữ Latin).
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: वीडियो, टेक्स्ट, ट्रांसक्रिप्ट, ट्रांसक्राइब, लिंक, पेस्ट, कॉपी, एडिट, ब्राउज़र, डाउनलोड, एक्सपोर्ट, कैप्शन, सबटाइटल, स्पीकर.
- Số đếm dùng chữ số Latin (100+, 5) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **"आप"** xuyên suốt, **không** dùng "तू"/"तुम" — **nhất quán tuyệt đối với `audio-to-text/hi.json`**.
- Nukta (़) dùng nhất quán: फ़ाइल, फ़ॉर्मैट, ज़्यादा, आवाज़, सिर्फ़.
- Chuỗi Hinglish chỉ được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title` và `hero.h1` **không** chứa Hinglish thô.
- Internal link trong `sections[6]` (section 7) giữ nguyên cú pháp markdown, đổi path: `[YouTube ट्रांसक्रिप्ट](/hi/youtube-transcript)`, `[TikTok ट्रांसक्रिप्ट](/hi/tiktok-transcript)`, `[ऑडियो टू टेक्स्ट](/hi/audio-to-text)`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, 9 sections, 10 specs, 4 steps, 5 items (section 6), 9 FAQ, `conclusion` h2 + 2 đoạn.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** dịch máy word-by-word và **tránh** Hindi văn chương nặng.
