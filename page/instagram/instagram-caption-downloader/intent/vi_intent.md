🔥 TranscriptX – Instagram Caption Downloader (Vietnamese / vi)

URL:
/vi/instagram-caption-downloader

Intent chính:

Tải caption Instagram miễn phí — lấy nguyên văn phần mô tả bài đăng thành text

Trang này là **bản tiếng Việt** của trang Instagram Caption Downloader. Nhắm đến người dùng Việt muốn lấy **caption / phần mô tả** (đoạn chữ mà tác giả **GÕ** dưới bài đăng) từ một Instagram Post, Reel hoặc video — để sao chép, lưu lại, dịch, phân tích hoặc tái sử dụng.

Gộp toàn bộ intent đồng nghĩa **tải / lấy / copy / lưu** vì tất cả cho ra **cùng một kết quả**: caption Instagram → text.

> ⚠️ **PHÂN ĐỊNH INTENT SỐNG CÒN: Caption ≠ Transcript.** Trang này lấy chữ tác giả **VIẾT** (mô tả bài đăng, hashtag, emoji). Trang anh em `/vi/instagram-transcript` lấy chữ người ta **NÓI** trong video (lời thoại, voiceover, âm thanh trong Reel). Section 2 của `en.json` tồn tại **chính là để phân định điều này** — bản `vi` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau. Trong tiếng Việt rủi ro này còn cao hơn tiếng Anh: từ "phụ đề" và "nội dung video" bị dùng lẫn lộn cho cả hai thứ, nên bản vi phải nói thẳng **"chữ bạn đọc thấy dưới bài đăng"** vs **"lời được nói trong clip"**, không dùng chữ "phụ đề" ở bất kỳ đâu trên trang này.

> ⚠️ **RỦI RO DỊCH LỚN NHẤT: cụm `tải video instagram`.** Ở thị trường Việt, `tải video instagram` / `download video instagram` / `tải reels instagram` có volume rất lớn và SERP **100% là downloader video** (snapinsta, igram, savefrom...). Trang này tải **CHỮ**, không tải video. **Quy tắc bắt buộc:** mọi chỗ "tải" phải có tân ngữ rõ ràng — **`tải caption`**, **`tải mô tả`**, **`tải nội dung bài đăng`**, **`tải phần chữ`** — và **KHÔNG BAO GIỜ** để chuỗi `"tải video"` xuất hiện trong `vi.json`. Lưu ý keyword `tải caption video instagram` là hợp lệ (tân ngữ là `caption`), nhưng khi viết phải giữ nguyên trật tự `tải caption video Instagram`, tuyệt đối không đảo thành `tải video...`. Trang `/vi/facebook-transcript` đã xử lý đúng cơ chế phòng thủ này — tham chiếu trực tiếp.

> ⚠️ **VOLUME PHẲNG 100% — cả 10 keyword đều `0–10`.** Khác hẳn bản `de` (có `instagram text kopieren` 100–1K) hay bản `pt`/`id` (có head term 100–1K). Bản vi **không có head term nào để dồn**. Hệ quả chiến lược: thay vì tập trung trọng số vào một cụm, phải **phủ đều cả 10 keyword** — mỗi keyword được cấp ít nhất một vị trí có trọng số (title / H1 / H2 / H3 / câu mở FAQ), không keyword nào bị bỏ rơi hoàn toàn trong body. Đây là chiến lược long-tail thuần: trang thắng bằng **độ phủ biến thể**, không bằng độ mạnh của một truy vấn.

> ℹ️ **`caption` giữ nguyên tiếng Anh hay dịch thành "mô tả"? — DÙNG CẢ HAI, có phân bổ.** Cả hai đều có keyword đã search: `tải caption instagram` (0–10) và `tải mô tả bài viết instagram` / `tải mô tả instagram` (0–10). Giới social media Việt gọi thẳng là **"caption"** — đây là từ mượn đã hoàn toàn nhập tịch, dùng phổ biến hơn hẳn trong nhóm creator, marketer, agency. Ngược lại người dùng phổ thông gõ **"mô tả bài viết"** hoặc **"nội dung bài đăng"**.
>
> **Phân bổ đã chốt:**
> - **`caption`** = trục chính → dùng ở `seo.title`, `hero.h1`, `hero.button`, H2 section 1/3/5, phần lớn FAQ. Khớp tên công cụ và cách nhóm đối tượng chính thực sự nói.
> - **`mô tả`** = trục song song → H2 section 4, các đoạn body giải thích khái niệm (section 1 đoạn 1, section 5), FAQ 1 và FAQ 3. Bắt nhóm người dùng phổ thông và làm câu văn tự nhiên hơn tiếng Việt.
> - **`nội dung bài đăng`** = trục thứ ba, chỉ trong body — bắt keyword `lấy nội dung bài đăng instagram`.
> - Nguyên tắc viết: **lần đầu xuất hiện trong section 1 phải đặt hai từ cạnh nhau** ("caption — tức phần mô tả tác giả viết dưới bài đăng") để Google gắn hai cụm vào cùng một thực thể, sau đó dùng xen kẽ tự do.

---

## Từ khóa chính

tải caption instagram (0–10) ✅ *đã search*

---

## Từ khóa phụ

### Nhóm Tải (trục chính, khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tải caption instagram | 0–10 | ✅ đã search *(KW chính)* |
| tải caption video instagram | 0–10 | ✅ đã search |
| tải caption instagram online | 0–10 | ✅ đã search |
| tải caption reels instagram | 0–10 | ✅ đã search |
| tải caption instagram bằng link | 0–10 | ✅ đã search |
| tải caption instagram miễn phí | — | 🔄 dịch bổ sung (free) |

### Nhóm Lấy / Copy (đưa xuống H2 section 5 + body theo quyết định đã chốt)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| cách lấy caption instagram | 0–10 | ✅ đã search |
| cách copy caption instagram | 0–10 | ✅ đã search |
| lấy nội dung bài đăng instagram | 0–10 | ✅ đã search |
| copy caption instagram không cần app | — | 🔄 dịch bổ sung (no install) |
| lưu caption instagram | — | 🔄 dịch bổ sung (save a caption) |

### Nhóm Mô tả / Nội dung (trục song song cho người dùng phổ thông)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tải mô tả bài viết instagram | 0–10 | ✅ đã search |
| tải mô tả instagram | 0–10 | ✅ đã search |
| lấy mô tả bài đăng instagram | — | 🔄 dịch bổ sung (biến thể) |
| tải hashtag từ bài đăng instagram | — | 🔄 dịch bổ sung (keep the hashtag set) |
| dịch caption instagram | — | 🔄 dịch bổ sung (translate a caption) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `h3` / `description` / câu mở FAQ. 🔄 *dịch bổ sung* = chỉ rải trong body để phủ ngữ nghĩa, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Việt thấy một caption Instagram hay — của chính mình, của đối thủ, hoặc của một tài khoản nước ngoài — và muốn lấy nguyên văn phần chữ đó ra khỏi app. Lý do rất cụ thể: **Instagram không có nút copy caption**, bôi đen trên điện thoại thì rất khó, hay dính nhầm tên tài khoản hoặc phần bình luận, và với caption dài kèm cả chục hashtag thì gần như không bôi trọn được.

Họ thường kỳ vọng:

- Chỉ cần **dán link bài đăng**, không đăng nhập Instagram, không cài app.
- Lấy **nguyên vẹn hashtag, emoji và ngắt dòng** — không bị gộp thành một cục chữ.
- Chạy được với bài ảnh đơn, Carousel, Reel và video.
- **Miễn phí thật**, không giới hạn số lần.
- Copy phát một là dán được sang Notes, Google Docs, Excel hoặc công cụ lên lịch đăng bài.
- Chạy tốt **trên điện thoại** — phần lớn người Việt dùng Instagram trong app điện thoại, nên luồng "copy link trong app → mở trình duyệt → dán" phải mượt.

### Khác biệt so với bản tiếng Anh

1. **Phải chủ động phòng thủ trước cụm "tải video instagram" — bản EN không có vấn đề này.** Trong tiếng Anh, `download` đi với `caption` là đã đủ rõ nghĩa, và cụm `instagram downloader` không tự động kéo trang về intent tải video. Trong tiếng Việt thì chuỗi "tải" + "instagram" đứng gần nhau tự nó đã là truy vấn downloader video khổng lồ. Vì vậy bản vi bắt buộc phải ghép "tải" với tân ngữ ở **mọi lần xuất hiện**, kể cả trong `hero.button` (dùng "Tải caption" chứ không phải "Tải xuống") và trong `placeholder`. Đây là ràng buộc biên tập, không phải tùy chọn phong cách.

2. **Volume phẳng tuyệt đối buộc đổi chiến lược từ "dồn head term" sang "phủ đều".** Bản EN có `instagram caption downloader` ở band 10K–100K và một loạt keyword phụ 1K–10K — tức có phễu rõ ràng, dồn trọng số vào head term là hợp lý. Bản vi cả 10 keyword đều `0–10`, không có tín hiệu nào nói cụm nào mạnh hơn cụm nào. Hệ quả: mỗi keyword phải được cấp một chỗ có trọng số riêng, và ba trục từ vựng (`caption` / `mô tả` / `nội dung bài đăng`) phải được **cố ý xen kẽ** thay vì chọn một trục như bản EN chọn `caption`.

3. **Tiếng Việt có ba cách gọi song song cho cùng một thứ, bản EN chỉ có một.** Bản EN dùng `caption` và `description` gần như đồng nghĩa hoàn toàn. Bản vi có `caption` (từ mượn, giới creator), `mô tả bài viết` (phổ thông, gần với cách Instagram Việt hóa giao diện) và `nội dung bài đăng` (trung tính, hơi hành chính) — ba tầng ngôn ngữ của ba nhóm người dùng khác nhau, đều có keyword riêng. Bản EN không cần tầng phân bổ này.

4. **Rủi ro nhầm với "phụ đề" cao hơn bản EN.** Người Việt hay gọi phần chữ hiện trong video Reel là "phụ đề", và cũng có người gọi caption dưới bài là "phụ đề". Bản EN không có sự mập mờ này vì `caption` (dưới bài) và `subtitle` (trong video) tách bạch. Bản vi vì thế **cấm dùng chữ "phụ đề" toàn trang**, và section 2 phải mô tả bằng hành động ("chữ được **viết** dưới bài" vs "lời được **nói** trong clip") thay vì bằng thuật ngữ.

5. **Nhấn mạnh luồng điện thoại mạnh hơn.** Bản EN mô tả cả desktop và mobile ngang hàng. Ở Việt Nam Instagram gần như là nền tảng mobile-only, nên section 3 (các bước) phải mô tả luồng trong app điện thoại làm mặc định (menu ba chấm → Sao chép liên kết), desktop chỉ nhắc phụ.

---

## Đối tượng người dùng

- Social media manager / nhân viên marketing Việt (phân tích caption đối thủ, làm báo cáo nội dung)
- Content creator, KOC, KOL (lưu swipe file những caption chạy tốt)
- Freelancer / agency nhận quản trị Instagram cho khách
- Chủ shop bán hàng online cần lưu lại nội dung bài đăng và bộ hashtag
- Người muốn dịch caption của tài khoản nước ngoài để hiểu hoặc để học cách viết
- Người cần lưu caption trước khi bài bị chỉnh sửa hoặc gỡ
- Sinh viên, người học marketing sưu tầm ví dụ caption để phân tích

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `vi.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, `conclusion` gồm h2 + 2 đoạn. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (vi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Tải caption Instagram | tải caption instagram *(KW chính)* |
| — | **quickAnswer** | tải caption instagram bằng link, tải caption instagram |
| 1 | Công cụ tải caption Instagram làm được gì | tải caption instagram, tải caption video instagram, tải mô tả instagram |
| 2 | Caption hay transcript: bạn cần cái nào? | *(phân định chữ VIẾT vs chữ NÓI + internal link `/vi/instagram-transcript`)* |
| 3 | Cách tải caption Instagram | tải caption instagram, tải caption instagram bằng link, tải caption reels instagram |
| 4 | Tải mô tả bài viết Instagram về rồi làm gì | tải mô tả bài viết instagram, lấy nội dung bài đăng instagram, tải caption reels instagram |
| 5 | **Cách copy caption Instagram — hashtag, emoji và định dạng giữ nguyên** | **cách copy caption instagram**, **cách lấy caption instagram**, tải caption video instagram |
| 6 | Câu hỏi thường gặp | tải caption instagram online, tải mô tả instagram, cách lấy caption instagram + long-tail |
| — | **conclusion** | tải caption instagram, miễn phí |

### Ghi chú riêng cho bản vi (KHÔNG tạo section mới)

- **Section 5 là van xả cho toàn bộ nhóm `lấy` / `copy`.** Theo quyết định đã chốt, H1 giữ khung "tải", còn nhóm copy/lấy dồn xuống H2 section 5 — giống hệt cách `de.json` đưa `Text kopieren` xuống H2 section 5. Đây là bám đúng nghĩa gốc chứ không phải nhét keyword: bản EN section này vốn đã nói về việc "what you copy reads the same as what was on the post".
- **Section 2 giữ nguyên vai trò phân định.** Internal link đổi thành `[Instagram Transcript](/vi/instagram-transcript)`. Hai `h3` phải mở đầu bằng động từ đối lập rõ: item 1 = "Tải caption nếu bạn cần phần chữ **được viết**", item 2 = "Lấy transcript nếu bạn cần lời **được nói**".
- **Chữ "phụ đề" bị cấm toàn file** — xem khác biệt số 4 ở trên.
- `tải caption reels instagram` đặt ở **section 3 (step 1)** và **section 4 (item cuối — bộ hashtag)**, đúng chỗ bản EN đã nhắc tới Reel.
- `lấy nội dung bài đăng instagram` đặt ở **section 4 item 2** (lưu lại trước khi bài bị sửa) — ngữ cảnh tự nhiên nhất cho cụm "nội dung bài đăng".
- `tải mô tả instagram` và `tải caption instagram online` gom vào **FAQ 1** và **FAQ 8**, đúng chỗ bản EN đã có sẵn câu hỏi "for free" và "several captions".
- `cách lấy caption instagram` đặt ở **section 5 đoạn 2** và **FAQ 3**.
- Cụm `caption` và `mô tả` phải đứng cạnh nhau ở **section 1 đoạn 1** để buộc hai thực thể lại với nhau (xem ghi chú phân bổ ở đầu file).
- Chuỗi **"tải video"** bị cấm tuyệt đối. Kiểm tra trước khi giao: `grep -n "tải video" vi.json` phải rỗng.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `tải video instagram` / `download video instagram` / `tải reels instagram` / `tải ảnh instagram` / `instagram downloader` → **intent tải VIDEO/ẢNH**, SERP toàn downloader media. Đây là nhóm nhiễm nguy hiểm nhất của thị trường Việt: trang này tải **chữ**, không tải video. **Quy tắc dịch:** mọi chỗ "tải" phải có tân ngữ `caption` / `mô tả` / `nội dung` / `văn bản`; chuỗi `"tải video"` không được xuất hiện ở bất kỳ đâu.
- `lấy text từ video instagram` / `chuyển reel instagram thành văn bản` / `transcript instagram` / `bóc băng reel instagram` → **/vi/instagram-transcript** (chữ **NÓI** trong video, không phải chữ **VIẾT** dưới bài)
- `chuyển video youtube thành văn bản` / `lấy phụ đề youtube` → **/vi/youtube-transcript**
- `chuyển video tiktok thành văn bản` / `lấy text từ video tiktok` → **/vi/tiktok-transcript**
- `chuyển âm thanh thành văn bản` / `bóc băng ghi âm` → **/vi/audio-to-text**
- `viết caption instagram hay` / `caption hay cho instagram` / `caption thả thính` → **intent NGƯỢC**: người dùng muốn **sáng tác** caption mới, không phải lấy caption có sẵn. Volume rất lớn ở VN nhưng hoàn toàn khác page type — tuyệt đối không chạm tới.
- `tải bio instagram` / `copy bình luận instagram` → gần về mặt kỹ thuật nhưng khác đối tượng, không tối ưu riêng

---

## Internal linking

- ↔ **/vi/instagram-transcript** — khi người dùng cần lời **NÓI** trong Reel/video thay vì caption **VIẾT**. Đây là link **quan trọng nhất của trang**, đặt trong **section 2, item 2**, giữ nguyên cú pháp markdown: `[Instagram Transcript](/vi/instagram-transcript)`. Link này vừa là lối thoát cho người dùng vào nhầm trang, vừa là tín hiệu gửi Google rằng hai trang phục vụ hai intent tách bạch.
- → /vi/youtube-transcript, /vi/tiktok-transcript (cross-cluster, cùng nhu cầu lấy chữ từ mạng xã hội khác)

---

## Ghi chú kỹ thuật cho vi.json

- Cấu trúc JSON khớp **100%** với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**, section 1 `content` 3 đoạn, section 2 `intro` 1 + `items` 2, section 3 `steps` 4, section 4 `intro` 1 + `items` 5, section 5 `content` 3 đoạn, section 6 `items` **8** (q/a), `conclusion` h2 + 2 đoạn.
- `lang="vi"`, `dir="ltr"`.
- Giữ nguyên Latin, không dịch: **TranscriptX, Instagram, Reel, Reels, Carousel, hashtag, emoji, caption, link, URL**.
- **Reel / Reels** giữ nguyên tiếng Anh (số ít "một Reel", số nhiều "Reels") — người Việt gọi đúng như vậy.
- **caption** viết thường, không viết hoa giữa câu (khác bản `de` phải viết hoa danh từ).
- Xưng hô **"bạn"** nhất quán toàn trang, đồng bộ với `/vi/facebook-transcript` và `/vi/audio-to-text`. Không dùng "quý khách", "các bạn".
- Thuật ngữ đồng bộ với cụm vi: **"bản transcript"**, **"trình duyệt"**, **"miễn phí"**, **"không cần tài khoản"**, **"công khai"** (cho public post), **"sao chép"** (dùng xen kẽ với từ mượn "copy").
- Gọi menu Instagram theo tên Việt hóa trong app: **"menu ba chấm"**, **"Sao chép liên kết"**.
- Internal link section 2 giữ cú pháp markdown: `[Instagram Transcript](/vi/instagram-transcript)`.
- **Kiểm tra bắt buộc trước khi giao:**
  - `grep -n "tải video" vi.json` → phải **rỗng**.
  - `grep -n "phụ đề" vi.json` → phải **rỗng**.
  - shape check với `en.json` → phải in `vi.json -> True`.
