🔥 TranscriptX – Instagram Transcript (Hindi / hi)

URL:
/hi/instagram-transcript

Intent chính:

Instagram Reel/वीडियो में बोली गई बात का ट्रांसक्रिप्ट फ्री में पाएँ (ऑनलाइन, बिना साइन-अप)

Trang này là **bản tiếng Hindi của trang trụ (hub)** cụm Instagram Transcript. Nhắm đến người dùng Ấn Độ có một Reel / video post / IGTV / Live đã lưu trên Instagram và muốn dán link để lấy **toàn bộ lời NÓI** trong clip thành văn bản — để đọc, sao chép, chỉnh sửa, dịch hoặc lưu lại.

Gộp toàn bộ intent đồng nghĩa **टेक्स्ट निकालना / ट्रांसक्राइब करना / टेक्स्ट में बदलना / ट्रांसक्रिप्ट बनाना** vì tất cả cho ra **cùng một kết quả**: video Instagram → text.

---

## ⚠️ PHÂN ĐỊNH SỐNG CÒN: Transcript ≠ Caption

Trang này lấy chữ người ta **NÓI** trong Reel/video (nguồn = **âm thanh**). Trang anh em `/hi/instagram-caption-downloader` lấy chữ tác giả **GÕ** dưới bài — ở đó gọi là **कैप्शन** (mô tả, hashtag, emoji). Hai trang, hai intent, hai nguồn dữ liệu khác nhau.

Bản EN đã cài sẵn **hai chốt chặn**, bản `hi` phải dịch sát cả hai, **không rút gọn, không gộp**:

1. **Section 7, đoạn 3** — câu "Looking for the written caption a creator posted under the Reel...?" kèm link sang trang caption.
2. **FAQ 8** — "Is this the same as downloading the Instagram caption?" → trả lời **No**, kèm chỉ dẫn sang Instagram Caption Downloader.

### ⚠️ Sắc thái riêng của KW `instagram video se caption nikale`

Keyword thứ 5 của bản `hi` dùng chữ **"caption"** nhưng ý người tìm là **lấy text từ trong video** (lời nói / phụ đề của clip), **KHÔNG** phải lấy mô tả tác giả gõ dưới bài. Đây là chỗ dễ nhầm nhất của cả bản `hi`.

Cách xử lý đã chốt:

- Chuỗi Hinglish nguyên văn `instagram video se caption nikale` **chỉ đặt ở `seo.schemaDescription`**, và đặt trong ngữ cảnh nói rõ nguồn là **वीडियो में बोले गए शब्द** (lời nói trong video) — để Google khớp lexical mà không khiến trang bị hiểu là trang caption.
- Trong body Devanagari, **không** dùng `कैप्शन` theo nghĩa "text cần lấy". `कैप्शन` chỉ được xuất hiện ở **thế phủ định / phân định**: section 4 (chạy được **cả khi không có** कैप्शन), section 7 đoạn 3 và FAQ 8 (đây **không phải** कैप्शन downloader), FAQ 4 (Reel không có कैप्शन vẫn chạy). Giống hệt cách bản EN dùng chữ "captions".
- Từ chỉ kết quả của trang này luôn là **टेक्स्ट / ट्रांसक्रिप्ट**, không bao giờ là `कैप्शन`.

Nhờ vậy trang này **không mâu thuẫn thuật ngữ** với `/hi/instagram-caption-downloader` (trang đó dùng `कैप्शन` cho chữ viết dưới bài, và đã link ngược sang `/hi/instagram-transcript` cho lời nói).

---

## ⚠️ Lưu ý riêng — chiến lược Hinglish vs Devanagari

Section `## Hindi (hi)` trong `2_loc_kw.md` **chỉ có 5 keyword**, và **cả 5 đều ở mức `0 – 10`**, và **cả 5 đều ở dạng Hinglish (chữ Latin)**:

| # | Keyword (nguyên dạng) | Volume | Dạng chữ |
| - | --------------------- | ------ | -------- |
| 1 | instagram video se text nikale | 0 – 10 | Hinglish |
| 2 | instagram reel transcribe kare | 0 – 10 | Hinglish |
| 3 | instagram video ka text kaise nikale | 0 – 10 | Hinglish |
| 4 | instagram reel ka text nikalna | 0 – 10 | Hinglish |
| 5 | instagram video se caption nikale | 0 – 10 | Hinglish |

**0 keyword Devanagari.** Đây là điểm khác biệt then chốt so với trang anh em `/hi/instagram-caption-downloader` — trang đó **có 3 keyword Devanagari thật** (`इंस्टाग्राम कैप्शन डाउनलोड`, `इंस्टाग्राम रील्स कैप्शन डाउनलोड`...) nên đặt được Devanagari thẳng vào `title`/`h1`/`h2` mà vẫn khớp keyword. Trang này **không có lựa chọn đó**.

Tình huống này **khớp chính xác** với `/hi/facebook-transcript` (cũng 0 keyword Devanagari, 6 keyword Hinglish, toàn bộ 0–10). Vì vậy **áp dụng lại nguyên si chiến lược 2 tầng đã chốt ở đó**:

- **Tầng hiển thị (`seo.title`, `hero.h1`, `hero.subtitle`, `hero.placeholder`, `hero.button`, mọi `h2`/`h3`, toàn bộ body, FAQ, `conclusion`): Devanagari 100%.** Tên riêng và định dạng giữ Latin (TranscriptX, Instagram, Reel/Reels, IGTV, Live, TXT, DOCX, PDF, SRT, VTT, URL). **Tuyệt đối không để một chuỗi Hinglish nào lọt vào tầng này** — H1 nửa Latin nửa Devanagari trông như trang spam.
- **Tầng meta (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): chèn nguyên văn chuỗi Hinglish.** Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin nằm ở đó không phá nhịp đọc mà vẫn cho Google một khớp lexical chính xác với truy vấn thật.

**Lý do chọn cách này thay vì 2 phương án còn lại:**

| Phương án | Vì sao loại |
| --------- | ----------- |
| Viết toàn bộ body bằng Hinglish (khớp 100% keyword) | Trái với `/hi/facebook-transcript`, `/hi/instagram-caption-downloader` và `/hi/audio-to-text` (đều đã chốt Devanagari); hreflang `hi` mà nội dung chữ Latin gây tín hiệu ngôn ngữ mâu thuẫn. |
| Bỏ hẳn Hinglish, chỉ Devanagari | **0/5 keyword đã search xuất hiện ở bất kỳ đâu** — mất trắng lớp dữ liệu duy nhất có được cho tiếng Hindi. |
| ✅ Devanagari ở tầng hiển thị + Hinglish ở tầng meta | Giữ chất lượng đọc, nhất quán toàn site tiếng Hindi, vẫn phủ được **5/5** keyword đã search. |

**Tỉ lệ nội dung của trang này:**

- **5 keyword ✅ đã search** (tất cả dùng được, không có keyword nào phải loại)
- **~15 cụm 🔄 dịch bổ sung** (Devanagari, dịch tự nhiên từ bản EN)
- → xấp xỉ **25% đã search / 75% dịch bổ sung** — tỉ lệ dịch bổ sung cao nhất trong tất cả các ngôn ngữ của trang này (bản `ko` có 13 keyword ✅, tỉ lệ ngược lại khoảng 75%/25%).

**Nhận định:** volume gần 0 **KHÔNG** có nghĩa thị trường Ấn Độ nhỏ. Người Ấn tìm chủ đề công nghệ này chủ yếu **bằng tiếng Anh** (`instagram transcript`, `instagram video to text`) — traffic Ấn Độ đã nằm sẵn trong `en.json`. Bản `hi` xếp **ưu tiên THẤP** về ROI keyword, vẫn nên làm vì tín hiệu hreflang/UX, chi phí biên thấp và hỗ trợ AI/GEO trả lời truy vấn tiếng Hindi.

---

## Từ khóa chính

**instagram video se text nikale** (0–10) ✅ *đã search*

> Chọn KW này vì: (a) là cụm **trung tâm nhất** về ngữ nghĩa (video → text), khớp đúng vai trò trang trụ; (b) hai KW `...ka text kaise nikale` và `...ka text nikalna` là biến thể how-to/danh động từ của chính nó, nên chọn nó là phủ được cả nhóm; (c) các KW còn lại hoặc là dạng câu hỏi (hợp `quickAnswer`/FAQ hơn) hoặc gắn riêng với Reel.
>
> Dạng Devanagari dùng ở title/H1/body: **Instagram वीडियो से टेक्स्ट निकालें**
> Dạng Hinglish `instagram video se text nikale` đặt ở `seo.description`.

*(KW chính thứ hai — dùng cho `quickAnswer` và section 3: `instagram video ka text kaise nikale` → **Instagram वीडियो का टेक्स्ट कैसे निकालें**.)*

---

## Từ khóa phụ

### Nhóm Text extraction (टेक्स्ट निकालना — trục chính, tương ứng "instagram video to text")

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram video se text nikale | 0–10 | ✅ đã search *(KW chính)* → **Instagram वीडियो से टेक्स्ट निकालें** |
| instagram video ka text kaise nikale | 0–10 | ✅ đã search → **Instagram वीडियो का टेक्स्ट कैसे निकालें** |
| — | — | 🔄 dịch bổ sung: **Instagram वीडियो को टेक्स्ट में बदलें** (instagram video to text) |
| — | — | 🔄 dịch bổ sung: **Instagram वीडियो का टेक्स्ट** (text of an instagram video) |
| — | — | 🔄 dịch bổ sung: **Instagram की आवाज़ को टेक्स्ट में बदलें** (instagram audio to text) |

### Nhóm Reel (trọng số cao nhất — Instagram ở Ấn Độ = Reels)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram reel transcribe kare | 0–10 | ✅ đã search → **Instagram Reel ट्रांसक्राइब करें** |
| instagram reel ka text nikalna | 0–10 | ✅ đã search → **Instagram Reel का टेक्स्ट निकालना** |
| — | — | 🔄 dịch bổ sung: **Instagram Reel को टेक्स्ट में बदलें** (reel to text) |
| — | — | 🔄 dịch bổ sung: **वायरल Reel की स्क्रिप्ट** (viral reel script) |

### Nhóm Transcript (ट्रांसक्रिप्ट — không có KW đã search, hoàn toàn dịch bổ sung)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **Instagram वीडियो का ट्रांसक्रिप्ट** (instagram transcript) |
| — | — | 🔄 dịch bổ sung: **Instagram ट्रांसक्रिप्ट जनरेटर** (instagram transcript generator) |
| — | — | 🔄 dịch bổ sung: **Instagram वीडियो ट्रांसक्रिप्शन** (instagram video transcription) |
| — | — | 🔄 dịch bổ sung: **फ्री Instagram ट्रांसक्रिप्ट** (free instagram transcript) |
| — | — | 🔄 dịch bổ sung: **लिंक से Instagram ट्रांसक्रिप्ट** (instagram transcript from link) |
| — | — | 🔄 dịch bổ sung: **Instagram ट्रांसक्रिप्ट डाउनलोड करें** (download instagram transcript) |

> ⚠️ Không có một keyword đã search nào chứa chữ `transcript` ở dạng danh từ (chỉ có động từ `transcribe kare`). Vì thế **`ट्रांसक्रिप्ट` không được đặt ở H1**, mà chỉ dùng ở `seo.title` (sau dấu —), ở H2 số 4 và rải trong body. H1 dành cho cụm khớp KW chính.

### Nhóm định dạng nội dung Instagram (IGTV / Live)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **IGTV और लंबे Instagram वीडियो का टेक्स्ट** (IGTV) |
| — | — | 🔄 dịch bổ sung: **सेव किया हुआ Instagram Live ट्रांसक्राइब करें** (saved live) |

### Nhóm ranh giới — dùng CÓ ĐIỀU KIỆN

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram video se caption nikale | 0–10 | ⚠️ ✅ đã search — dùng chữ "caption" nhưng intent là **lấy text từ video** → chỉ đặt ở `seo.schemaDescription`, xem mục phân định ở trên |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, dạng Devanagari phải xuất hiện trong `title`/`h1`/`h2`, dạng Hinglish nguyên văn phải xuất hiện trong `seo.description`/`ogDescription`/`schemaDescription`. 🔄 *dịch bổ sung* = chỉ rải trong body để phủ ngữ nghĩa, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Ấn Độ lướt thấy một Reel đáng giá — mẹo nấu ăn, mẹo học, review sản phẩm, bài giảng ngắn, phân tích tin tức — và muốn giữ lại **lời nói** trong đó thành chữ, vì Reel trôi cực nhanh và phần giá trị thường chỉ nằm ở một câu.

Họ thường kỳ vọng:

- Chỉ cần **dán link**, không tải file, không cài app, không đăng nhập Instagram.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — gần như 100% người Ấn dùng Instagram bằng app điện thoại rồi copy link sang trình duyệt.
- Chạy được cả khi Reel **không có** कैप्शन/phụ đề trên màn hình.
- Nhận dạng được **tiếng Hindi** và tiếng Anh giọng Ấn, cũng như các tiếng vùng miền khác.
- Xử lý được **nhạc nền lớn và người nói rất nhanh** — đặc trưng của Reel.
- Tách được nhiều người nói (Reel dạng duet / collab / phỏng vấn).

### Khác biệt so với bản tiếng Anh

1. **Trục keyword là `टेक्स्ट निकालना`, không phải `transcript`.** Bản EN có `instagram transcript` (10K–100K) làm trục danh từ, đủ mạnh để đặt thẳng vào H1. Bản `hi` **không có một keyword nào chứa chữ transcript ở dạng danh từ** — 4/5 keyword xoay quanh `text nikale/nikalna`. Hệ quả: H1 bản `hi` là **Instagram वीडियो से टेक्स्ट निकालें**, còn `ट्रांसक्रिप्ट` lùi xuống title/H2/body. Đây là đảo trọng số mà bản EN và bản `ko` đều không có.
2. **Keyword tồn tại ở hệ chữ khác với nội dung — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ. Bản `hi`: keyword là Latin (Hinglish), body là Devanagari. Bắt buộc tách hai tầng (meta = Hinglish, body = Devanagari) — quyết định biên tập không tồn tại ở bất kỳ ngôn ngữ nào khác của trang này.
3. **`Reel` nặng ký hơn hẳn bản EN.** Bản EN đối xử Reels và video posts khá cân bằng. Bản `hi` có **2/5 keyword gắn riêng với Reel** (`instagram reel transcribe kare`, `instagram reel ka text nikalna`) — item Reels ở section 6 phải viết dày nhất, và section 1 phải mở bằng bối cảnh Reel chứ không phải "video" chung chung.
4. **"फ्री / मुफ़्त" phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần **फ्री** xuất hiện ở `title`, `description`, `hero.subtitle`, section 1 đoạn 4, section 2 và `conclusion` — thị trường Ấn Độ cực nhạy giá, đây là yếu tố quyết định click.
5. **Rủi ro nhiễu "tải video" lớn hơn nhiều lần bản EN.** `instagram video download` / `reels download` ở Ấn Độ có volume khổng lồ và SERP toàn downloader. Bản EN gần như không có rủi ro này ở mức đó. Bản `hi` phải kiểm soát chặt chữ `डाउनलोड` (xem quy tắc ở mục loại trừ).
6. **Trộn thuật ngữ tiếng Anh là chuẩn, không phải lỗi.** Người Ấn viết web thật sự dùng **वीडियो, टेक्स्ट, ट्रांसक्रिप्ट, लिंक, पेस्ट, कॉपी, ब्राउज़र, डाउनलोड, स्पीकर**. **Tránh** Hindi văn chương (`प्रतिलेखन`, `दृश्य-श्रव्य`, `पाठ`) — không ai search và không ai đọc như vậy. Giống hệt quy tắc của `/hi/facebook-transcript` và `/hi/audio-to-text`.

---

## Đối tượng người dùng

- Người xem Reels muốn lưu lại mẹo / công thức / ghi chú học tập
- Content creator và Reels creator Ấn Độ nghiên cứu hook của Reel viral
- Marketing / Social media manager phân tích Reel của đối thủ
- Sinh viên, học viên coaching class xem bài giảng ngắn trên Reel/IGTV
- Người học ngoại ngữ (đọc chậm lời nói nhanh trong Reel tiếng nước ngoài)
- Người làm phụ đề cần bản nháp text (SRT/VTT)
- Nhà báo cần trích dẫn phát biểu từ Reel/Live
- Người lưu nội dung Live đã lưu trước khi bị xóa
- Người khiếm thính hoặc ở nơi không bật được tiếng

---

## Map H2 → keyword (bám ĐÚNG 9 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng 9 section của `en.json`, cùng số đoạn `content`, đúng 10 `specs`, đúng 4 `steps`, đúng 5 `items` ở section 6, đúng 9 FAQ, đúng 2 đoạn `conclusion`. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Instagram वीडियो से टेक्स्ट निकालें | instagram video se text nikale ✅ *(dạng Devanagari; dạng Hinglish ở `description`)* |
| — | **quickAnswer** | instagram video ka text kaise nikale ✅ → **Instagram वीडियो का टेक्स्ट कैसे निकालें?** |
| 1 | Instagram ट्रांसक्रिप्ट क्या है? | Instagram वीडियो का ट्रांसक्रिप्ट 🔄, instagram reel ka text nikalna ✅, instagram video se text nikale ✅ *(mở bằng bối cảnh Reel)* |
| 2 | एक नज़र में Instagram ट्रांसक्रिप्ट | *(bảng thông số — फ्री / 100+ भाषाएँ / बिना साइन-अप)* |
| 3 | Instagram वीडियो या Reel का टेक्स्ट कैसे निकालें | instagram video ka text kaise nikale ✅, लिंक से Instagram ट्रांसक्रिप्ट 🔄 |
| 4 | बिना कैप्शन वाला Instagram ट्रांसक्रिप्ट जनरेटर | Instagram ट्रांसक्रिप्ट जनरेटर 🔄, instagram reel transcribe kare ✅, Instagram वीडियो ट्रांसक्रिप्शन 🔄 |
| 5 | Instagram वीडियो को टेक्स्ट में बदलें | Instagram वीडियो को टेक्स्ट में बदलें 🔄, Instagram की आवाज़ को टेक्स्ट में बदलें 🔄, instagram video se text nikale ✅ |
| 6 | Instagram पर आप क्या-क्या ट्रांसक्राइब कर सकते हैं | instagram reel ka text nikalna ✅ *(item 1)*, IGTV 🔄 *(item 3)*, सेव किया हुआ Live 🔄 *(item 4)* |
| 7 | कॉपी करें, एडिट करें, अनुवाद करें या डाउनलोड करें | Instagram ट्रांसक्रिप्ट डाउनलोड करें 🔄 + **chốt phân định 1** *(link sang /hi/instagram-caption-downloader, /hi/tiktok-transcript, /hi/youtube-transcript)* |
| 8 | सटीकता और भाषाएँ | Instagram वीडियो ट्रांसक्रिप्शन 🔄 *(+ nhấn tiếng Hindi và tiếng vùng miền Ấn Độ)* |
| 9 | अक्सर पूछे जाने वाले सवाल | फ्री Instagram ट्रांसक्रिप्ट 🔄, instagram reel transcribe kare ✅ + **chốt phân định 2 (FAQ 8)** + long-tail |
| — | **conclusion** | instagram video se text nikale ✅, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **Toàn bộ 5 chuỗi Hinglish nằm ở tầng meta, không ở body:**
  - `seo.description` → `instagram video se text nikale`, `instagram video ka text kaise nikale`
  - `seo.ogDescription` → `instagram reel transcribe kare`
  - `seo.schemaDescription` → `instagram reel ka text nikalna`, `instagram video se caption nikale`
  - **Không chuỗi Hinglish nào được xuất hiện trong `hero`, `sections` hay `conclusion`.**
- **Section 1 phải mang chất Instagram, không phải Facebook.** Bản EN đoạn 2 đã nói rõ: Reel sinh ra để xem một lần rồi lướt qua, giá trị nằm ở một câu (mẹo trong tutorial 15 giây, câu chốt khiến Reel viral). Bản `hi` giữ nguyên trọng tâm đó — **không** bê bối cảnh Facebook Live dài / webinar / họp cộng đồng sang.
- **Section 6 phải mang chất Instagram.** 5 item theo đúng bản EN: Reels → video posts → IGTV & video dài → Live đã lưu → nội dung how-to/giáo dục. Item Reels (item 1) viết dày nhất và đặt nguyên cụm **Instagram Reel का टेक्स्ट निकालना**. Item 5 (recipe/workout/tutorial nhồi trong Reel ngắn) rất đúng thị hiếu Ấn Độ, giữ nguyên.
- **Sắc thái Reel xử lý trong section 4:** nhấn đúng ý bản EN — nói nhanh, trending audio, nhạc nền — vì đó là đặc trưng Reel, đồng thời là câu trả lời cho lo lắng "nhạc to thế này có nhận được không".
- **Nỗi lo "có nhận dạng tiếng Hindi không" xử lý bên trong section 8**, bằng cách thay ví dụ ngôn ngữ của bản EN (Portuguese / Arabic) bằng ví dụ tiếng Hindi và một tiếng vùng miền Ấn Độ — **không thêm câu, không thêm H2**.
- **Section 3 step 1** giữ nguyên ý "three-dot menu / address bar" nhưng diễn đạt theo thực tế mobile-first của Ấn Độ (copy link từ app điện thoại), **vẫn không thêm câu**.
- **`कैप्शन` chỉ xuất hiện ở thế phủ định/phân định** — section 4 (chạy cả khi không có कैप्शन), section 7 đoạn 3, FAQ 4, FAQ 8. **Không** đẩy lên H1, **không** dùng làm từ chỉ kết quả của trang.
- **Hai chốt phân định (section 7 đoạn 3 + FAQ 8) dịch sát, không rút gọn.** Đây là yêu cầu giống hệt bản `ko`.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `instagram caption download` / `इंस्टाग्राम कैप्शन डाउनलोड` / `पोस्ट का विवरण कॉपी` → **/hi/instagram-caption-downloader** (chữ **VIẾT** dưới bài, không phải chữ **NÓI** trong video)
- `youtube video ka transcript` / `यूट्यूब वीडियो को टेक्स्ट में बदलें` → **/hi/youtube-transcript**
- `tiktok video se text nikale` / `टिकटॉक ट्रांसक्रिप्ट` → **/hi/tiktok-transcript**
- `audio ko text me kaise badle` / `ऑडियो को टेक्स्ट में बदलें` / `MP3 को टेक्स्ट में बदलें` → **/hi/audio-to-text** (nguồn là **file âm thanh**, không phải video Instagram)
- ⛔ **NHÓM TẢI VIDEO — nhiễm nguy hiểm nhất của cụm Instagram tiếng Hindi:**
  `instagram video download` / `instagram video download kaise kare` / `reels download` / `insta reel download` / `इंस्टाग्राम वीडियो डाउनलोड` / `रील्स डाउनलोड` / `इंस्टाग्राम वीडियो सेव करें`
  → intent **tải file VIDEO về máy**, SERP hoàn toàn là downloader. Volume ở Ấn Độ **khổng lồ** (gấp nhiều bậc so với toàn bộ 5 keyword của trang này cộng lại), nên sức hút nhiễm rất mạnh. Trang này lấy **CHỮ**, không tải video. Kéo nhóm này vào sẽ làm lệch page type và phá luôn cả cụm.
  **Quy tắc cứng:** chữ `डाउनलोड` chỉ được đi với tân ngữ **`ट्रांसक्रिप्ट` / `टेक्स्ट` / `फ़ाइल`**, **không bao giờ** với `वीडियो` / `Reel` / `Reels`.
- `टेक्स्ट को आवाज़ में बदलें` / `टेक्स्ट टू स्पीच` → **NGƯỢC intent**, thuộc trang Text-to-Speech

---

## Internal linking

- ↔ **/hi/instagram-caption-downloader** (khi user muốn chữ **VIẾT** dưới bài thay vì lời nói) — link quan trọng nhất, nằm ở **section 7 đoạn 3**, nhắc lại ở **FAQ 8**. Trang caption cũng đã link ngược sang trang này, tạo cặp phân định hai chiều.
- → /hi/tiktok-transcript, /hi/youtube-transcript (cross-cluster: cùng nhu cầu transcript, nền tảng khác — cùng nằm ở section 7 đoạn 3)

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, Instagram, IGTV, Reel, Reels, Live, TXT, DOCX, PDF, SRT, VTT, URL**.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: वीडियो, टेक्स्ट, ट्रांसक्रिप्ट, ट्रांसक्राइब, ट्रांसक्रिप्शन, लिंक, पेस्ट, कॉपी, एडिट, ब्राउज़र, डाउनलोड, एक्सपोर्ट, कैप्शन, सबटाइटल, स्पीकर, हैशटैग.
- Nhãn `specs` dịch **giống hệt** `/hi/facebook-transcript` để đồng bộ toàn site: कीमत / अकाउंट ज़रूरी / इंस्टॉलेशन / इनपुट / किन पर चलता है / भाषाएँ / स्पीकर की पहचान / कैप्शन न हों तब भी चलता है / एक्सपोर्ट फ़ॉर्मैट / डिवाइस.
- Số đếm dùng chữ số Latin (100+, 5) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **"आप"** xuyên suốt, **không** dùng "तू"/"तुम" — nhất quán tuyệt đối với `/hi/facebook-transcript` và `/hi/instagram-caption-downloader`.
- Nukta (़) dùng nhất quán: फ़ाइल, फ़ॉर्मैट, ज़्यादा, आवाज़, सिर्फ़, फ़ीड, रेफ़रेंस.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle` và `hero.h1` **không** chứa Hinglish thô.
- Internal link trong `sections[6]` (section 7) giữ nguyên cú pháp markdown, đổi path: `[Instagram Caption Downloader](/hi/instagram-caption-downloader)`, `[TikTok Transcript](/hi/tiktok-transcript)`, `[YouTube Transcript](/hi/youtube-transcript)`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **9 sections**; S1 `content` 4 · S2 `specs` 10 · S3 `steps` 4 · S4 `content` 3 · S5 `content` 2 · S6 `intro` 1 + `items` 5 · S7 `content` 3 · S8 `content` 3 · S9 `items` **9**; `conclusion` h2 + 2 đoạn.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** dịch máy word-by-word và **tránh** Hindi văn chương nặng.
