🔥 TranscriptX – TikTok Caption Downloader (Hindi / hi)

URL:
/hi/tiktok-caption-downloader

Intent chính:

TikTok सबटाइटल डाउनलोड करें — tải file phụ đề TikTok có timecode, miễn phí, không cần đăng nhập

Trang này nhắm đến người dùng Ấn Độ có một video TikTok công khai và muốn **tải file phụ đề (सबटाइटल फ़ाइल)** của nó — file có mốc thời gian từng dòng — để gắn lại lên clip khi đăng lại, để dịch sang ngôn ngữ khác, hoặc để phục vụ người khiếm thính.

Người dùng chỉ dán link, công cụ dựng phụ đề từ **âm thanh** của video và trả về file có timecode. Không tài khoản, không cài đặt.

---

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/hi/instagram-caption-downloader`.**
>
> Dù tên gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/hi/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (मो tả, hashtag, emoji) → **कैप्शन** | Lời **NÓI** trong video |
> | Nguồn dữ liệu | Phần text của bài đăng | **Âm thanh của clip** |
> | Kết quả | Đoạn text đọc được | **File phụ đề có timecode (सबटाइटल फ़ाइल)** |
> | Từ trục | `कैप्शन` | **`सबटाइटल`** |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram, `कैप्शन` là **từ chỉ kết quả** của trang. **Ở trang này thì không**: kết quả luôn gọi là `सबटाइटल` / `सबटाइटल फ़ाइल`. Đừng áp nhầm quy tắc của trang kia.

> ⚠️ **PHÂN ĐỊNH VỚI `/hi/tiktok-transcript`: TRỤC LÀ TIMING, KHÔNG PHẢI VIẾT-VS-NÓI.**
>
> Cả hai trang đều lấy lời **NÓI** từ audio — điểm khác biệt duy nhất là **timing**:
>
> - Trang này → **सबटाइटल फ़ाइल** khớp thời gian, để chạy đè lên video.
> - `/hi/tiktok-transcript` → **सादा टेक्स्ट** để đọc / copy, không timecode.
>
> Bản EN cài sẵn **3 chốt chặn**, bản `hi` giữ nguyên cả ba, dịch sát, **không rút gọn, không gộp**:
>
> 1. **Section 2 — cả section** dành riêng để phân định, có internal link `[TikTok Transcript](/hi/tiktok-transcript)` ở item 2.
> 2. **FAQ 3** — "TikTok सबटाइटल और ट्रांसक्रिप्ट में क्या फ़र्क़ है?"
> 3. **Section 1 đoạn 2** — câu giải thích vì sao trang này tồn tại tách riêng.

---

## ⚠️ Mục riêng — KW `tiktok video ka text kaise nikale` bị HẠ TRỌNG SỐ

| Keyword | Volume | Xử lý |
| ------- | ------ | ----- |
| tiktok video ka text kaise nikale | 0–10 | ⚠️ hạ trọng số — **chỉ đặt ở `seo.schemaDescription`**, kèm neo ngữ cảnh |

**Lý do:** cụm này nghiêng về intent **transcript** — người tìm muốn *text thuần để đọc*, đúng ra thuộc `/hi/tiktok-transcript`. Nếu đặt vào `title` / `h1` / `h2`, trang này sẽ tự nhận vai trò của trang kia và **ăn thịt** nó (cannibalization), đồng thời làm page type bị hiểu sai (Google thấy trang "text" nhưng nội dung lại là "file có timing").

**Cách xử lý đã chốt:**

- Chuỗi Hinglish nguyên văn `tiktok video ka text kaise nikale` **chỉ nằm ở `seo.schemaDescription`**, và đặt trong ngữ cảnh nói rõ kết quả là **टाइमिंग वाली सबटाइटल फ़ाइल** — để Google khớp lexical mà không hiểu nhầm page type.
- Trong body Devanagari, dạng nghĩa tương ứng (`TikTok वीडियो का टेक्स्ट`) chỉ được chạm **một lần duy nhất**, ở **section 1 đoạn 1**, và bắt buộc đi kèm neo phủ định *"पढ़ने वाला पैराग्राफ़ नहीं, बल्कि टाइमिंग वाली सबटाइटल फ़ाइल"*. Không thêm câu mới.
- **Không** dùng cụm này ở `hero`, `h2` bất kỳ, hay `conclusion`.

**Kết quả:** 3 keyword đúng intent làm trục chính + 1 keyword hạ trọng số phủ ở tầng meta.

---

## ⚠️ Lưu ý riêng — chiến lược Hinglish vs Devanagari

Section `## Hindi (hi)` trong `2_loc_kw.md` **chỉ có 4 keyword**, và **cả 4 đều ở mức `0 – 10`**, và **cả 4 đều ở dạng Hinglish (chữ Latin)**:

| # | Keyword (nguyên dạng) | Volume | Dạng chữ | Intent |
| - | --------------------- | ------ | -------- | ------ |
| 1 | tiktok subtitle download kaise kare | 0 – 10 | Hinglish | ✅ đúng — tải file phụ đề |
| 2 | tiktok video ka text kaise nikale | 0 – 10 | Hinglish | ⚠️ nghiêng transcript → hạ trọng số |
| 3 | tiktok subtitle kaise download kare | 0 – 10 | Hinglish | ✅ đúng — biến thể đảo trật tự của #1 |
| 4 | tiktok caption save kaise kare | 0 – 10 | Hinglish | ✅ đúng — lưu phụ đề |

**0 keyword Devanagari.** Tình huống này **khớp chính xác** với `/hi/instagram-transcript` (5 keyword, tất cả Hinglish, tất cả 0–10) và `/hi/facebook-transcript`. Vì vậy **áp dụng lại nguyên si chiến lược 2 tầng đã chốt ở đó**:

- **Tầng hiển thị** (`seo.title`, `seo.ogTitle`, `hero.h1`, `hero.subtitle`, `hero.placeholder`, `hero.button`, mọi `h2`/`h3`, toàn bộ body, FAQ, `conclusion`): **Devanagari 100%**. Tên riêng và định dạng giữ Latin (TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT, URL). **Tuyệt đối không để một chuỗi Hinglish nào lọt vào tầng này** — H1 nửa Latin nửa Devanagari trông như trang spam.
- **Tầng meta** (`seo.description`, `seo.ogDescription`, `seo.schemaDescription`): **chèn nguyên văn chuỗi Hinglish**. Meta không phải văn bản người đọc lướt trong bài, nên chuỗi Latin nằm ở đó không phá nhịp đọc mà vẫn cho Google một khớp lexical chính xác với truy vấn thật.

**Lý do chọn cách này thay vì 2 phương án còn lại:**

| Phương án | Vì sao loại |
| --------- | ----------- |
| Viết toàn bộ body bằng Hinglish (khớp 100% keyword) | Trái với `/hi/instagram-transcript`, `/hi/instagram-caption-downloader`, `/hi/facebook-transcript` (đều đã chốt Devanagari); hreflang `hi` mà nội dung chữ Latin gây tín hiệu ngôn ngữ mâu thuẫn. |
| Bỏ hẳn Hinglish, chỉ Devanagari | **0/4 keyword đã search xuất hiện ở bất kỳ đâu** — mất trắng lớp dữ liệu duy nhất có được cho tiếng Hindi. |
| ✅ Devanagari ở tầng hiển thị + Hinglish ở tầng meta | Giữ chất lượng đọc, nhất quán toàn site tiếng Hindi, vẫn phủ được **4/4** keyword đã search. |

**Phân bổ 4 chuỗi Hinglish ở tầng meta:**

| Chuỗi Hinglish | Đặt ở |
| -------------- | ----- |
| tiktok subtitle download kaise kare | `seo.description` |
| tiktok subtitle kaise download kare | `seo.description` |
| tiktok caption save kaise kare | `seo.ogDescription` |
| tiktok video ka text kaise nikale | `seo.schemaDescription` *(kèm neo ngữ cảnh "सबटाइटल फ़ाइल")* |

**Tỉ lệ nội dung:** 3 keyword ✅ dùng đầy đủ + 1 keyword ⚠️ hạ trọng số + ~14 cụm 🔄 dịch bổ sung (Devanagari) → xấp xỉ **20% đã search / 80% dịch bổ sung**.

**Nhận định:** volume gần 0 **KHÔNG** có nghĩa thị trường Ấn Độ nhỏ. Người Ấn tìm chủ đề này chủ yếu **bằng tiếng Anh** (`tiktok subtitles download`, `tiktok caption downloader`) — traffic Ấn Độ đã nằm sẵn trong `en.json`. Bản `hi` xếp **ưu tiên THẤP** về ROI keyword, vẫn nên làm vì tín hiệu hreflang/UX, chi phí biên thấp và hỗ trợ AI/GEO trả lời truy vấn tiếng Hindi.

---

## Từ khóa chính

**tiktok subtitle download kaise kare** (0–10) ✅ *đã search*

> Chọn KW này vì: (a) là cụm **trung tâm nhất** về ngữ nghĩa (subtitle → download), khớp đúng page type "tải file phụ đề"; (b) KW #3 `tiktok subtitle kaise download kare` chỉ là biến thể đảo trật tự của chính nó, chọn nó là phủ được cả hai; (c) KW #2 nghiêng transcript, KW #4 hẹp hơn (save chứ không phải download).
>
> Dạng Devanagari dùng ở title/H1/H2/body: **TikTok सबटाइटल डाउनलोड करें**
> Dạng Hinglish `tiktok subtitle download kaise kare` đặt ở `seo.description`.

*(KW chính thứ hai — dùng cho `quickAnswer` và H2 section 3: `tiktok subtitle kaise download kare` → **TikTok सबटाइटल कैसे डाउनलोड करें**.)*

---

## Từ khóa phụ

### Nhóm Download / Save (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok subtitle download kaise kare | 0–10 | ✅ đã search *(KW chính)* → **TikTok सबटाइटल डाउनलोड करें** |
| tiktok subtitle kaise download kare | 0–10 | ✅ đã search → **TikTok सबटाइटल कैसे डाउनलोड करें** |
| tiktok caption save kaise kare | 0–10 | ✅ đã search → **TikTok सबटाइटल सेव करें** |
| — | — | 🔄 dịch bổ sung: **TikTok सबटाइटल फ़ाइल डाउनलोड** (subtitle file download) |
| — | — | 🔄 dịch bổ sung: **TikTok सबटाइटल ऑनलाइन डाउनलोड** (download online) |
| — | — | 🔄 dịch bổ sung: **TikTok सबटाइटल निकालें** (extract subtitles) |

### Nhóm Danh từ (phủ head term)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **TikTok सबटाइटल** (tiktok subtitles) |
| — | — | 🔄 dịch bổ sung: **TikTok वीडियो के सबटाइटल** (tiktok video captions) |
| — | — | 🔄 dịch bổ sung: **TikTok पर सबटाइटल** (captions on tiktok) |
| — | — | 🔄 dịch bổ sung: **टाइमिंग वाली सबटाइटल फ़ाइल** (timed subtitle file) |

### Nhóm Dịch / Đa ngôn ngữ (khớp đúng section 5 bản EN)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **TikTok सबटाइटल का अनुवाद करें** (translate tiktok subtitles) |
| — | — | 🔄 dịch bổ sung: **100+ भाषाओं में TikTok सबटाइटल** (100+ languages) |

### Nhóm định dạng / kỹ thuật

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| — | — | 🔄 dịch bổ sung: **TikTok SRT फ़ाइल** (tiktok SRT file) |
| — | — | 🔄 dịch bổ sung: **फ्री TikTok सबटाइटल डाउनलोडर** (free downloader) |

### Nhóm ranh giới — dùng CÓ ĐIỀU KIỆN

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok video ka text kaise nikale | 0–10 | ⚠️ ✅ đã search — intent nghiêng **transcript** → chỉ đặt ở `seo.schemaDescription` + 1 lần neo ở section 1 đoạn 1. Xem mục hạ trọng số ở trên. |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, dạng Devanagari phải xuất hiện trong `title`/`h1`/`h2`, dạng Hinglish nguyên văn phải xuất hiện trong `seo.description`/`ogDescription`/`schemaDescription`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

> ⚠️ **Chỉ có 3 keyword đúng intent hoàn toàn, tất cả cùng band `0 – 10`.** Không có cụm nào áp đảo để dồn lực. Chiến lược: **dùng `सबटाइटल` làm từ trục xuyên suốt**, phủ đều 3 nhóm Devanagari, phần còn lại là dịch tự nhiên.

---

## Search Intent

Người dùng Ấn Độ thấy một video TikTok và cần **file phụ đề** của nó — không phải để đọc, mà để **dùng lại**:

- Đăng lại clip (repost) lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có phụ đề.
- Dịch phụ đề sang tiếng Hindi hoặc ngôn ngữ khác rồi gắn lại — hoặc ngược lại, dịch phụ đề Hindi sang tiếng Anh để tiếp cận khán giả toàn cầu.
- Sửa lại phụ đề tự động của TikTok vốn hay nhận sai tiếng Hindi và tiếng Anh giọng Ấn.
- Làm phụ đề cho người khiếm thính.

Họ kỳ vọng:

- Dán link là ra file, không cần đăng nhập TikTok.
- File có **timecode từng dòng**, mở được bằng phần mềm dựng phim.
- Chạy được cả khi video gốc **không bật phụ đề trên màn hình**.
- Sửa được chữ trong file trước khi dùng.
- **Hoàn toàn miễn phí** — độ nhạy giá ở thị trường Ấn Độ rất cao.
- **Chạy tốt trên điện thoại** — gần như 100% người Ấn dùng TikTok/short-video bằng app rồi copy link sang trình duyệt.

### Khác biệt so với bản tiếng Anh

1. **Keyword tồn tại ở hệ chữ khác với nội dung — vấn đề bản EN không hề có.** Bản EN: keyword và body cùng một hệ chữ. Bản `hi`: keyword là Latin (Hinglish), body là Devanagari. Bắt buộc tách hai tầng (meta = Hinglish, body = Devanagari) — quyết định biên tập không tồn tại ở bất kỳ ngôn ngữ nào khác của trang này.
2. **Tiếng Hindi có hai từ mượn `कैप्शन` và `सबटाइटल`, và phải chọn dứt khoát.** Bản EN dùng `captions` và `subtitles` xen kẽ thoải mái vì cả hai đều chỉ chữ chạy trên video. Bản `hi` **không được** làm vậy: `कैप्शन` đã bị `/hi/instagram-caption-downloader` chiếm làm từ chỉ *chữ viết dưới bài*. Vì thế `सबटाइटल` là từ chỉ kết quả duy nhất của trang này; `कैप्शन` chỉ được dùng ở nghĩa hẹp **"chữ hiện sẵn trên màn hình video"** (auto-caption của TikTok), và chỉ ở **thế phủ định / phân định**.
3. **Rủi ro nhiễu "tải video" lớn hơn nhiều lần bản EN.** `tiktok video download` / `tiktok without watermark` / `टिकटॉक वीडियो डाउनलोड` ở Ấn Độ có volume **khổng lồ** và SERP toàn downloader video. Bản EN gần như không có rủi ro này ở mức đó. Bản `hi` phải kiểm soát chặt chữ `डाउनलोड` (xem quy tắc ở mục loại trừ).
4. **"फ्री / मुफ़्त" phải nặng hơn "free" của bản EN.** Bản EN nhắc "free" như một thuộc tính; bản `hi` cần **फ्री** xuất hiện ở `title`, `description`, `hero.subtitle`, FAQ 2 và `conclusion` — thị trường Ấn Độ cực nhạy giá.
5. **Nỗi lo "phụ đề tự động của TikTok nhận sai tiếng Hindi" là điểm bán hàng riêng.** Bản EN chỉ nói "shaky auto-captions" chung chung — bản `hi` nhấn đúng nỗi đau này ở **section 4 item 3**, trong đúng câu đã có sẵn, không thêm câu.
6. **Trộn thuật ngữ tiếng Anh là chuẩn, không phải lỗi.** Người Ấn viết web thật sự dùng **वीडियो, सबटाइटल, टेक्स्ट, फ़ाइल, लिंक, पेस्ट, कॉपी, ब्राउज़र, डाउनलोड, टाइमिंग, एडिटर**. **Tránh** Hindi văn chương (`उपशीर्षक`, `प्रतिलेखन`, `दृश्य-श्रव्य`) — không ai search và không ai đọc như vậy.

---

## Đối tượng người dùng

- Người làm content re-upload / tổng hợp clip short-video Ấn Độ
- Editor video, freelancer dựng phim
- Người cross-post TikTok sang Instagram Reels / YouTube Shorts
- Người dịch phụ đề cho khán giả nói tiếng Hindi và tiếng vùng miền
- Marketer chạy nội dung đa ngôn ngữ (Hindi ↔ English)
- Người làm nội dung cho người khiếm thính
- Người muốn sửa phụ đề tự động nhận sai tiếng Hindi của TikTok
- Sinh viên / người học tiếng Anh muốn đọc lại lời nói nhanh trong clip

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps` ở section 3, đúng 5 `items` ở section 4, đúng 2 đoạn ở section 5, đúng **8 FAQ**, đúng 2 đoạn `conclusion`. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** TikTok सबटाइटल डाउनलोड करें | tiktok subtitle download kaise kare ✅ *(dạng Devanagari; dạng Hinglish ở `description`)* |
| — | **quickAnswer** | tiktok subtitle kaise download kare ✅ → **TikTok वीडियो के सबटाइटल कैसे डाउनलोड करें?** |
| 1 | TikTok सबटाइटल डाउनलोडर क्या करता है | TikTok सबटाइटल 🔄, टाइमिंग वाली सबटाइटल फ़ाइल 🔄 + ⚠️ **neo duy nhất** của `TikTok वीडियो का टेक्स्ट` ở đoạn 1 + **chốt phân định 3** ở đoạn 2 |
| 2 | सबटाइटल या ट्रांसक्रिप्ट: आपको क्या चाहिए? | *(**chốt phân định 1** — cả section, internal link `/hi/tiktok-transcript` ở item 2)* |
| 3 | TikTok सबटाइटल कैसे डाउनलोड करें | tiktok subtitle kaise download kare ✅, TikTok सबटाइटल फ़ाइल डाउनलोड 🔄 |
| 4 | डाउनलोड किए हुए TikTok सबटाइटल का क्या करें | tiktok caption save kaise kare ✅ *(dạng Devanagari **सबटाइटल सेव करें** ở item 5)*, TikTok पर सबटाइटल 🔄 *(item 3)* |
| 5 | 100+ भाषाओं में TikTok सबटाइटल डाउनलोड करें | TikTok सबटाइटल का अनुवाद करें 🔄, 100+ भाषाओं में TikTok सबटाइटल 🔄 |
| 6 | अक्सर पूछे जाने वाले सवाल | फ्री TikTok सबटाइटल डाउनलोडर 🔄 *(FAQ 2)* + **chốt phân định 2 (FAQ 3)** + long-tail |
| — | **conclusion** | TikTok सबटाइटल डाउनलोड करें ✅, फ्री |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- **Toàn bộ 4 chuỗi Hinglish nằm ở tầng meta, không ở body:**
  - `seo.description` → `tiktok subtitle download kaise kare`, `tiktok subtitle kaise download kare`
  - `seo.ogDescription` → `tiktok caption save kaise kare`
  - `seo.schemaDescription` → `tiktok video ka text kaise nikale` *(kèm neo "सबटाइटल फ़ाइल")*
  - **Không chuỗi Hinglish nào được xuất hiện trong `hero`, `sections` hay `conclusion`.**
- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho việc này. Dịch đủ 2 item, giữ link `[TikTok Transcript](/hi/tiktok-transcript)` ở item 2. Trục phân định là **timing**, không phải viết-vs-nói.
- **FAQ 3** là chốt thứ hai — dịch sát, không rút gọn, nhắc lại tên công cụ TikTok Transcript.
- **Section 1 đoạn 2** là chốt thứ ba — câu giải thích vì sao trang này tách riêng khỏi trang transcript. Giữ nguyên trọng lượng, không nén thành mệnh đề phụ.
- **`कैप्शन` chỉ xuất hiện ở thế phủ định / phân định**, đúng **2 vị trí**: section 4 item 3 (auto-caption của TikTok hay nhận sai tiếng Hindi) và FAQ 5 (video không có कैप्शन trên màn hình vẫn chạy — xuất hiện ở cả `q` và `a` của cùng FAQ đó). **Không** đẩy lên H1/H2, **không** dùng làm từ chỉ kết quả của trang.
- **Neo cho KW hạ trọng số** chỉ ở section 1 đoạn 1, trong câu vốn đã có, kèm mệnh đề phủ định "không phải đoạn văn để đọc". Không thêm câu.
- **Nỗi lo phụ đề tự động sai tiếng Hindi** xử lý **trong câu đã có** ở section 4 item 3, không thêm câu mới.
- **Section 5 đúng 2 đoạn** (khác trang Instagram caption vốn có 3 ở vị trí tương ứng).

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `tiktok video se text nikale` / `टिकटॉक वीडियो को टेक्स्ट में बदलें` / `टिकटॉक ट्रांसक्रिप्ट` → **/hi/tiktok-transcript** (text thuần, **không** timing). Kéo vào đây sẽ ăn thịt trang kia.
- `instagram caption download` / `इंस्टाग्राम कैप्शन डाउनलोड` / `पोस्ट का विवरण कॉपी` → **/hi/instagram-caption-downloader** (chữ **VIẾT** dưới bài, khác hẳn)
- `youtube video ka transcript` / `यूट्यूब सबटाइटल डाउनलोड` → **/hi/youtube-transcript**
- ⛔ **NHÓM TẢI VIDEO — nhiễm nguy hiểm nhất của cụm TikTok tiếng Hindi:**
  `tiktok video download` / `tiktok video download kaise kare` / `tiktok without watermark` / `tiktok download without watermark` / `टिकटॉक वीडियो डाउनलोड` / `बिना वॉटरमार्क टिकटॉक`
  → intent **tải file VIDEO về máy**, SERP hoàn toàn là downloader video. Volume ở Ấn Độ **khổng lồ** — gấp nhiều bậc so với toàn bộ 4 keyword của trang này cộng lại — nên sức hút nhiễm rất mạnh. Trang này tải **file phụ đề**, không tải video. Kéo nhóm này vào sẽ làm lệch page type và phá luôn cả cụm.
  **Quy tắc cứng:** chữ `डाउनलोड` chỉ được đi với tân ngữ **`सबटाइटल` / `फ़ाइल` / `टेक्स्ट`**, **không bao giờ** với `वीडियो` / `क्लिप` / `Reel` / `Shorts`.
- `टिकटॉक पर सबटाइटल कैसे ऑन करें` → **hướng dẫn thao tác trong app**, không phải công cụ tải file.
- `टेक्स्ट को आवाज़ में बदलें` / `टेक्स्ट टू स्पीच` → **NGƯỢC intent**, thuộc trang Text-to-Speech.

---

## Internal linking

- ↔ **/hi/tiktok-transcript** (khi user chỉ cần text thuần để đọc, không cần timing) — link quan trọng nhất, nằm ở **section 2 item 2**, nhắc lại (không link) ở **FAQ 3**. Tạo cặp phân định hai chiều theo trục timing.

---

## Ghi chú kỹ thuật cho hi.json

- `lang="hi"`, `dir="ltr"` — Devanagari viết trái sang phải, **không** cần RTL.
- Giữ nguyên Latin, không phiên âm sang Devanagari: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT, URL**.
- Thuật ngữ kỹ thuật phổ thông thì Devanagari hóa: वीडियो, सबटाइटल, टेक्स्ट, फ़ाइल, ट्रांसक्रिप्ट, लिंक, पेस्ट, कॉपी, एडिट, ब्राउज़र, डाउनलोड, टाइमिंग, एडिटर, ऑडियो.
- Số đếm dùng chữ số Latin (100+) — chuẩn trên web tiếng Hindi.
- Xưng hô: dùng thể lịch sự **"आप"** xuyên suốt, **không** dùng "तू"/"तुम" — nhất quán tuyệt đối với `/hi/instagram-transcript` và `/hi/instagram-caption-downloader`.
- Nukta (़) dùng nhất quán: फ़ाइल, फ़ॉर्मैट, ज़्यादा, आवाज़, सिर्फ़, फ़र्क़, ज़रूरत.
- Chuỗi Hinglish **chỉ** được phép nằm trong `seo.description`, `seo.ogDescription`, `seo.schemaDescription`. `seo.title`, `seo.ogTitle` và `hero.h1` **không** chứa Hinglish thô.
- Internal link trong `sections[1].items[1]` giữ nguyên cú pháp markdown, đổi path: `[TikTok Transcript](/hi/tiktok-transcript)`.
- Tuyệt đối không để chuỗi **`वीडियो डाउनलोड`** xuất hiện ở bất kỳ đâu.
- Tránh lặp `सबटाइटल` quá dày: dùng xen kẽ `सबटाइटल फ़ाइल`, `सबटाइटल की लाइन`, `टाइमिंग वाली फ़ाइल`, `फ़ाइल`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**; S1 `content` **3** · S2 `intro` 1 + `items` 2 · S3 `steps` 4 · S4 `intro` 1 + `items` 5 · S5 `content` **2** · S6 `items` **8**; `conclusion` h2 + 2 đoạn.
- Văn phong: Hindi đời thường pha thuật ngữ Anh như người Ấn thực sự viết trên web. **Tránh** dịch máy word-by-word và **tránh** Hindi văn chương nặng.
