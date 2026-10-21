🔥 TranscriptX – Video to Text (Vietnamese / vi)

URL:
/vi/video-to-text

Intent chính:

Chuyển video thành văn bản online miễn phí

Trang này là **trang trụ (hub)** cụm Video to Text bản tiếng Việt. Nhắm đến người dùng đã **có sẵn file video trong máy** (MP4, MOV, bản ghi Zoom/Teams/Meet, screen recording, footage máy quay, video tải về) và muốn lấy phần lời nói bên trong thành chữ viết.

Gộp toàn bộ intent đồng nghĩa **chuyển / chuyển đổi / tách lời** vì tất cả cho ra **cùng một kết quả**: file video → văn bản. Tiếng Việt không phân biệt "convert" và "transcribe" thành hai động từ riêng như tiếng Anh — cả hai đều là "chuyển".

> ⚠️ **Phân định với `/vi/audio-to-text`: LOẠI FILE.** Trang này nhận **file VIDEO** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **file ÂM THANH** (MP3, WAV, M4A...). Đối chiếu hai danh sách keyword `vi` cho thấy **0 keyword trùng nhau** — người dùng Việt tự phân biệt rất rõ theo loại file họ đang cầm. Chốt chặn nằm ở **section 10 đoạn 3** (link sang `/vi/audio-to-text`). Không kéo cụm `chuyển âm thanh thành văn bản` / `chuyển file ghi âm` về trang này.

> ⚠️ **Phân định với các trang nền tảng: FILE vs LINK.** Trang này để **tải file lên từ máy**; các trang `/vi/youtube-transcript`, `/vi/tiktok-transcript`, `/vi/instagram-transcript` để **dán link**. Cùng section 10 đoạn 3 chứa link sang cả ba. Đây cũng chính là chỗ dập nhiễm hai keyword YouTube bị loại ở mục dưới — người tìm "video YouTube" được đẩy sang đúng trang thay vì ở lại đây.

---

## 🚫 HAI KEYWORD YOUTUBE BỊ LOẠI + DÒNG RÁC

Danh sách `vi` trong `2_loc_kw.md` có **15 keyword thô + 1 dòng rác**. Trong đó **2 cụm `100 – 1K` thuộc trang khác**.

### Loại hoàn toàn — KHÔNG dùng ở title / H1 / H2 / body

| Keyword | Volume | Lý do loại |
| ------- | ------ | ---------- |
| chuyển video youtube sang văn bản | 100–1K | Intent **dán link YouTube**, không phải tải file lên. Thuộc **/vi/youtube-transcript** — repo đã có sẵn thư mục `youtube/youtube-transcript`. Kéo vào đây sẽ ăn thịt trang kia và làm sai kỳ vọng người dùng (họ vào rồi phát hiện phải có file trong máy). |
| chuyển video youtube thành văn bản | 100–1K | Như trên — biến thể `thành` của cùng một intent. |

**Cách xử lý thay vì loại bỏ trắng:** section 10 đoạn 3 nói rõ "khi video nằm trên nền tảng thay vì trong máy" và trỏ sang `/vi/youtube-transcript`. Người tìm hai cụm trên vẫn được phục vụ, nhưng bằng **link nội bộ**, không bằng cách tối ưu trang này cho từ khóa của trang khác.

### Dòng rác trong file nguồn

`Keyword ideas` là **nhãn của công cụ search**, không phải keyword — bỏ qua.

### Intent lân cận — hạ xuống body

| Keyword | Volume | Vị trí cho phép |
| ------- | ------ | --------------- |
| tạo phụ đề từ video | 10–100 | **Chỉ section 10 và FAQ 8.** Trang này **xuất file SRT/VTT** để bạn tự nạp vào trình phát, **không gắn phụ đề hộ lên video**. Đặt lên title/H1/H2 sẽ hứa quá lời. |

**Tổng kết số liệu:** 15 keyword thô − 1 dòng rác (không tính) = 15 keyword; **loại 2 cụm YouTube** → **13 keyword thực** dùng cho trang này, trong đó 12 cụm lên được title/H1/H2/body và 1 cụm (`tạo phụ đề từ video`) chỉ nằm ở body cuối trang.

---

## ⚠️ RỦI RO OCR — TRANG NÀY LẤY TIẾNG NÓI, KHÔNG LẤY CHỮ TRÊN MÀN HÌNH

Cụm `chuyển video thành văn bản` trong tiếng Việt **mơ hồ hai nghĩa**: (a) bóc lời nói trong video ra chữ, (b) đọc chữ đang hiển thị trên khung hình (OCR / lấy text từ video slide). SERP nghiêng hẳn về (a), nhưng một phần lưu lượng vào với kỳ vọng (b).

**Cách chốt:**

- Cụm `chuyển âm thanh video thành văn bản` (100–1K) — keyword có thật, volume thật — dùng ở **section 5** và **section 8** để nói rõ nguồn dữ liệu là **âm thanh bên trong video**.
- Cụm `tách lời từ video` (100–1K) đặt ở **section 1**: chữ "lời" tự nó loại nghĩa OCR.
- Section 3 bước 2 mô tả rõ công cụ "lấy phần âm thanh ra khỏi video" trước khi xử lý.
- Không dùng bất kỳ cụm nào kiểu "lấy chữ trên màn hình", "trích text từ hình ảnh", "đọc chữ trong video".

---

## ⚠️ RỦI RO `tải video`

Cụm `tải video` có volume rất lớn ở Việt Nam và SERP toàn công cụ **downloader video**. Trang này không tải video về máy — nó nhận video vào và trả chữ ra.

**Quy tắc bắt buộc:** mọi chỗ xuất hiện động từ "tải" phải có tân ngữ là `bản transcript` / `văn bản` / `file text` / `file video lên`. **Không bao giờ** để chuỗi "tải video" đứng liền nhau.

Kiểm tra cuối: `grep "tải video" vi.json` phải trả về rỗng.

---

## Từ khóa chính

chuyển video thành văn bản (1K–10K) ✅ *đã search*

Đây là cụm **mạnh nhất** trong danh sách vi và cũng là **lõi chung** của 5 biến thể khác (`... online`, `cách ...`, `chuyển đổi ...`, `phần mềm ...`, `chuyển video thành text`). Lấy nguyên văn làm **H1** và mở đầu **seo.title**.

---

## Từ khóa phụ

### Nhóm Chuyển ... thành văn bản (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| chuyển video thành văn bản | 1K–10K | ✅ đã search *(KW chính)* |
| chuyển video thành văn bản online | 100–1K | ✅ đã search |
| chuyển đổi video thành văn bản | 100–1K | ✅ đã search |
| cách chuyển video thành văn bản | 100–1K | ✅ đã search |
| chuyển video sang văn bản | 100–1K | ✅ đã search |
| chuyển từ video sang văn bản | 100–1K | ✅ đã search |

### Nhóm Text / MP4 (biến thể Latin)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| chuyển video sang text | 100–1K | ✅ đã search |
| chuyển video thành text | 100–1K | ✅ đã search |
| chuyển mp4 sang text | 100–1K | ✅ đã search |

### Nhóm Âm thanh trong video (chống nhiễm OCR)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| chuyển âm thanh video thành văn bản | 100–1K | ✅ đã search |
| tách lời từ video | 100–1K | ✅ đã search |

### Nhóm Công cụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| phần mềm chuyển video thành văn bản | 10–100 | ✅ đã search |

### Intent lân cận (chỉ body cuối trang)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tạo phụ đề từ video | 10–100 | ✅ đã search *(chỉ S10 + FAQ 8)* |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| bóc băng video | — | 🔄 dịch bổ sung (transcribe video) |
| chuyển video họp Zoom thành văn bản | — | 🔄 dịch bổ sung (Zoom recording) |
| bản transcript video | — | 🔄 dịch bổ sung (video transcript) |
| lấy văn bản từ video | — | 🔄 dịch bổ sung (extract text) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Việt **đã có file video trong máy** — bản ghi họp Zoom/Teams/Meet, screen recording hướng dẫn, webinar, bài giảng quay lại, video phỏng vấn quay bằng máy ảnh hoặc điện thoại — và muốn lấy phần lời nói ra thành chữ để đọc nhanh, tìm kiếm, trích dẫn, làm biên bản, làm tài liệu hoặc đưa vào AI.

Họ kỳ vọng:

- Tải file lên là chạy ngay, không cài phần mềm.
- **Không giới hạn dung lượng / thời lượng** — bản ghi họp 2–3 tiếng là chuyện thường.
- Phân biệt được **nhiều người nói** (quan trọng nhất với biên bản họp).
- **Miễn phí thật**, không có tường thu phí ở bước cuối.
- Nhận diện **tiếng Việt có dấu** chuẩn — nỗi lo lớn nhất của người dùng Việt.
- Xuất được **DOCX** để làm tài liệu và **SRT** để làm phụ đề.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Việt không tách "convert" và "transcribe" thành hai động từ.** Bản EN dựng hẳn hai section riêng quanh sự đối lập convert / transcribe (section 4 và 5). Tiếng Việt chỉ có một chữ "chuyển", nên section 5 phải đổi trục: thay vì đối lập từ ngữ, nó đối lập **mức độ chính xác cần thiết** — "chuyển cho biết nội dung" so với "chuyển để trích dẫn, để làm biên bản, để căn cứ hành động". Cụm `bóc băng` đưa vào đây làm sắc thái nghề nghiệp.
2. **Nỗi lo tiếng Việt có dấu là nỗi lo số một, bản EN không có tương đương.** Người dùng Việt mặc định các công cụ nước ngoài trả về tiếng Việt không dấu hoặc sai dấu. Xử lý ở **section 9**, thay ví dụ ngôn ngữ của bản EN (German/Vietnamese) bằng ví dụ đặt tiếng Việt lên đầu — không thêm câu.
3. **Rủi ro nhiễm OCR nặng hơn hẳn bản EN.** "Video to text" trong tiếng Anh gần như luôn hiểu là lời nói; "chuyển video thành văn bản" trong tiếng Việt có thể hiểu là lấy chữ trên khung hình. Bản EN không cần chống nhiễm này; bản vi phải chống ở section 1, 3, 5 và 8.
4. **Cụm `tải video` là bẫy riêng của tiếng Việt.** SERP `tải video` ở Việt Nam toàn downloader. Bản EN không có vấn đề tương ứng vì "download video" và "video to text" tách bạch. Bản vi phải kiểm soát tân ngữ của mọi động từ "tải".
5. **Hai keyword YouTube có volume thật nằm ngay trong danh sách vi**, trong khi danh sách EN sạch. Bản vi phải chủ động loại và điều hướng, bản EN thì không cần.

---

## Đối tượng người dùng

- Nhân viên văn phòng, thư ký, trợ lý (biên bản họp Zoom/Teams/Meet)
- Nhà báo, phóng viên (bóc băng phỏng vấn quay hình)
- Giáo viên, sinh viên (bài giảng ghi hình, lớp học online)
- Người làm khóa học online, tài liệu nội bộ (screen recording → tài liệu hướng dẫn)
- Content creator, marketer (webinar → bài viết, video → kịch bản)
- Người dựng phim, người làm phụ đề (cần file SRT/VTT)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `vi.json` phải dịch đúng **11 section**, cùng số đoạn `content`, đúng 10 `specs`, đúng 4 `steps`, đúng 4 `items` ở section 6, đúng 6 `items` ở section 7, đúng **10 FAQ**.

| # | H2 (vi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Chuyển video thành văn bản | chuyển video thành văn bản *(KW chính)* |
| — | **quickAnswer** | cách chuyển video thành văn bản |
| 1 | Chuyển video thành văn bản là gì? | chuyển video thành văn bản, tách lời từ video, chuyển video sang văn bản |
| 2 | Chuyển video thành văn bản – tổng quan nhanh | *(bảng 10 thông số — miễn phí / không giới hạn / hơn 100 ngôn ngữ)* |
| 3 | Cách chuyển file video thành văn bản | **cách chuyển video thành văn bản**, chuyển từ video sang văn bản |
| 4 | Phần mềm chuyển video thành văn bản miễn phí | **phần mềm chuyển video thành văn bản**, chuyển video thành văn bản online |
| 5 | Bóc băng video chính xác | chuyển âm thanh video thành văn bản, chuyển đổi video thành văn bản |
| 6 | Các định dạng video được hỗ trợ | *(MP4, MOV, AVI, MKV, WebM)* + **chuyển mp4 sang text** |
| 7 | Bạn có thể chuyển những loại video nào | *(Zoom/Teams/Meet, screen recording, webinar, bài giảng...)* |
| 8 | Chuyển video thành văn bản chính xác đến đâu? | chuyển âm thanh video thành văn bản *(chốt nguồn là âm thanh)* |
| 9 | Chuyển video sang text với hơn 100 ngôn ngữ | **chuyển video sang text**, chuyển video thành text *(+ nhấn tiếng Việt có dấu)* |
| 10 | Xuất bản transcript ra năm định dạng | tạo phụ đề từ video + *(4 internal link: /vi/audio-to-text, /vi/youtube-transcript, /vi/tiktok-transcript, /vi/instagram-transcript)* |
| 11 | Câu hỏi thường gặp | chuyển video thành văn bản online, chuyển mp4 sang text, tạo phụ đề từ video + long-tail |
| — | **conclusion** | chuyển video thành văn bản, miễn phí |

### Ghi chú riêng cho bản vi (KHÔNG tạo section mới)

- **Section 5 đổi trục** so với bản EN: không đối lập "convert vs transcribe" (tiếng Việt không có), mà đối lập **mức độ tin cậy cần thiết**. Cụm `bóc băng` xuất hiện ở H2 section 5 và rải trong body — đây là từ nghề, dùng nhiều ở giới báo chí và thư ký.
- **Nỗi lo tiếng Việt có dấu** xử lý **trong section 9**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ đặt tiếng Việt lên trước — không thêm câu.
- **Section 10 đoạn 3 là chốt chặn kép**: vừa phân định audio vs video (loại file), vừa phân định file vs link (nền tảng). Đủ 4 link ở đúng một đoạn.
- `tạo phụ đề từ video` chỉ xuất hiện ở **section 10 đoạn 2** và **FAQ 8**, luôn đi kèm mô tả "xuất file SRT/VTT" để không hứa gắn phụ đề hộ.
- Thuật ngữ nhất quán với `/vi/audio-to-text`: **"bản transcript"**, **"gán nhãn từng người nói"**, **"tự động nhận diện"**, **"dấu thời gian"**. Xưng hô **"bạn"**.

---

## Không nên tối ưu cho các keyword

- `chuyển video youtube sang văn bản` / `chuyển video youtube thành văn bản` → **/vi/youtube-transcript** (dán link, không tải file lên). **Loại hoàn toàn** khỏi title/H1/H2/body — chỉ điều hướng bằng internal link ở section 10.
- `chuyển âm thanh thành văn bản` / `chuyển file ghi âm thành văn bản` / `chuyển mp3 sang text` → **/vi/audio-to-text** (file âm thanh). Dữ liệu đã tự tách sạch, chỉ cần không chủ động kéo về.
- `chuyển video tiktok thành văn bản` / `lấy text video instagram` → **các trang nền tảng riêng**.
- **`tải video` / `tải video về máy` / `nén video` / `chuyển mp4 sang mp3`** → **intent xử lý FILE video**, không phải lấy chữ. Quy tắc: "tải" chỉ đi với `bản transcript` / `văn bản` / `file text` / `file video lên`, **không bao giờ** đứng liền với "video".
- `lấy chữ trong video` hiểu theo nghĩa **OCR** / `trích text từ hình ảnh` → intent đọc chữ **trên màn hình**, khác hẳn. Trang này lấy **tiếng nói**. Nhóm `chuyển âm thanh video thành văn bản` và `tách lời từ video` giúp phân định điều này.
- `gắn phụ đề vào video` / `ghép sub vào video` → intent chèn phụ đề; trang này chỉ **xuất file SRT/VTT** (section 10 + FAQ 8), không gắn hộ.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link** — nhiều nhất trong các trang đã làm:

- → /vi/audio-to-text (khi nguồn là file âm thanh thay vì file video — phân định theo **loại file**)
- → /vi/youtube-transcript, /vi/tiktok-transcript, /vi/instagram-transcript (khi video nằm trên nền tảng, **dán link** thay vì tải file lên — phân định theo **file vs link**, đồng thời dập nhiễm 2 keyword YouTube bị loại)

---

## Ghi chú kỹ thuật cho vi.json

- Xưng **"bạn"**, nhất quán với `/vi/audio-to-text` và các trang vi khác trong repo.
- Nhãn `specs` **copy y nguyên chuỗi** từ `/vi/audio-to-text` (Chi phí / Yêu cầu tài khoản / Cài đặt / Giới hạn dung lượng / Định dạng hỗ trợ / Ngôn ngữ / Phân biệt người nói / Dấu thời gian / Định dạng xuất / Thiết bị) — **chỉ đổi giá trị của `Định dạng hỗ trợ`** sang định dạng video.
- Giữ nguyên Latin: **MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT**; thương hiệu **TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad**.
- Cấu trúc: **11 section**, **10 FAQ** (khác `/vi/audio-to-text` vốn có 11), section 6 = `intro` 1 + `items` 4, section 7 = `intro` 1 + `items` 6.
- Internal link section 10 giữ cú pháp markdown, đổi path sang `/vi/...`.
- **Kiểm tra bắt buộc trước khi giao:** `grep "tải video" vi.json` phải rỗng.
