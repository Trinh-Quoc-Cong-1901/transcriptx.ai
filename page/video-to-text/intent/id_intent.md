🔥 TranscriptX – Video to Text (Indonesian / id)

URL:
/id/video-to-text

Intent chính:

Mengubah video menjadi teks online gratis

Trang này là **trang trụ (hub)** cụm Video to Text bản tiếng Indonesia. Nhắm đến người dùng Indonesia đã **có sẵn file video** (MP4, MOV, bản ghi Zoom/Teams/Meet, screen recording, footage máy quay/HP) và muốn chuyển lời nói bên trong thành văn bản.

Gộp toàn bộ intent đồng nghĩa **transkrip / mengubah / ubah / convert / ekstrak** vì tất cả cho ra **cùng một kết quả**: file video → teks.

> ⚠️ **Lưu ý ngôn ngữ Indonesia:** người dùng Indonesia **trộn từ tiếng Anh vào truy vấn** rất mạnh — `convert video ke teks`, `video jadi teks online`, `ubah mp4 jadi teks`. Đây là **keyword hợp lệ**, giữ nguyên dạng lai, KHÔNG "sửa" thành tiếng Indonesia thuần. Tồn tại song song 2 register: trang trọng (`mengubah video menjadi teks`) và khẩu ngữ (`mengubah video jadi teks` / `ubah ... jadi ...`) — **cả hai đều có volume**, phải rải cả hai trong body.

> ⚠️ **Phân định với `/id/audio-to-text`: LOẠI FILE.** Trang này nhận **file VIDEO** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **file ÂM THANH** (MP3, WAV, M4A...). Đối chiếu 2 danh sách keyword cho thấy **0 keyword trùng nhau** — người dùng tự phân biệt rất sạch, không cần can thiệp. Chốt chặn nằm ở **section 10 đoạn 3** (link sang `/id/audio-to-text` kèm liệt kê MP3/WAV/M4A để người đọc tự nhận ra mình cầm loại file nào).

> ⚠️ **Phân định với các trang nền tảng: FILE vs LINK.** Trang này để **unggah file dari perangkat**; các trang `/id/youtube-transcript`, `/id/tiktok-transcript`, `/id/instagram-transcript` để **tempel tautan (dán link)**. Cùng section 10 đoạn 3 chứa cả ba, với câu chốt "cukup menempel link tanpa mengunggah apa pun". Đây là **4 internal link** — nhiều nhất trong các trang đã làm.

---

## ⚠️ Chống trùng với `/ms/video-to-text` (làm song song)

Tiếng Indonesia và tiếng Mã Lai dùng chung một phần từ vựng. Dữ liệu keyword của hai ngôn ngữ ở trang này **trùng 3 cụm đầu bảng, cùng band `1K – 10K`**:

| Keyword | id | ms |
| ------- | -- | -- |
| video ke teks | 1K–10K | 1K–10K |
| transkrip video | 1K–10K | 1K–10K |
| transkrip video ke teks | 1K–10K | 1K–10K |

> 🔴 **H1 trùng là do DỮ LIỆU, không phải do lười.** Cả hai ngôn ngữ có **cùng bộ head term mạnh nhất**. Không có cách nào tách H1 mà không hy sinh keyword mạnh nhất của một trong hai bên. Chấp nhận trùng ở H1, **tách triệt để ở toàn bộ phần còn lại** bằng bảng dưới.

### Bảng từ vựng phân biệt (BẮT BUỘC tuân thủ trong `id.json`)

| Ý nghĩa | ✅ Dùng (id) | ❌ CẤM (dạng Mã Lai) |
| ------- | ----------- | ------------------- |
| chuyển đổi | `mengubah`, `ubah`, `mengonversi` | `tukar`, `menukar` |
| giới từ "sang / thành" | `menjadi`, `jadi`, `ke` | `kepada` |
| miễn phí | `gratis` | `percuma` |
| có thể | `bisa`, `dapat` | `boleh` |
| chỉ / thôi | `saja` | `sahaja` |
| tải xuống | `unduh`, `mengunduh` | `muat turun` |
| tệp tin | `file` | `fail` |
| video | `video` | `video` *(trùng, không tránh được)* |

> 📌 **Ghi chú về `file` vs `berkas`:** brief gợi ý `berkas` để đối lập với `fail` của tiếng Mã Lai. Nhưng `/id/audio-to-text` đã chốt dùng `file` (KBBI hợp lệ, và **người Indonesia search bằng `file`, không search bằng `berkas`** — xem `Batas ukuran file` trong bảng `specs`). **Giữ `file`** để nhất quán cụm và không trượt keyword; điều quan trọng là **tuyệt đối không xuất hiện `fail`**, và mục tiêu chống trùng đã đạt qua 7 cặp từ còn lại.

> 📌 **`kepada` là từ tiếng Indonesia hợp lệ**, nhưng ở trang này nó là **dấu vân tay của keyword Mã Lai** (`tukar video kepada teks`). Vì vậy loại bỏ hoàn toàn, thay bằng `ke` / `untuk`.

### Tách thêm bằng ví dụ ngữ cảnh Indonesia

Ngoài từ vựng, tách bằng **bối cảnh sử dụng chỉ có ở Indonesia**, chèn vào section 7 (không thêm câu, chỉ đổi ví dụ):

- `seminar kampus`, `kajian yang direkam panitia` — thay cho "talks/events" chung chung của bản EN.
- `klip yang dikirimkan teman lewat WhatsApp` — WhatsApp là kênh chia sẻ video áp đảo ở Indonesia.
- `rekaman perkuliahan` — bối cảnh mahasiswa, nhóm người dùng lớn nhất.

---

## ⚠️ Mục lỗi dữ liệu

- Danh sách `## Indonesian (id)` trong `2_loc_kw.md` **sạch**: 16 keyword, **không có dòng rác `Keyword ideas`**, **không có cụm trùng lặp** (khác hẳn bản `es` phải khử trùng và bản `ms` bị dính lỗi gộp dòng `0 – 10ekstrak teks dari video`).
- Số keyword thực: **16/16 đều dùng được**.

---

## Từ khóa chính

video ke teks (1K–10K) ✅ *đã search*

## Từ khóa đồng hạng

transkrip video (1K–10K) ✅ *đã search*
transkrip video ke teks (1K–10K) ✅ *đã search*

> **Chốt H1: `Transkrip Video ke Teks`.** Cụm này **chứa trọn vẹn cả ba head term cùng band `1K – 10K`** trong đúng một dòng: `transkrip video` + `video ke teks` + `transkrip video ke teks`. Không có phương án nào phủ được nhiều hơn.
>
> Đồng thời nó xử lý luôn **rủi ro nghĩa kép của `transkrip`**: trong tiếng Indonesia `transkrip` đứng một mình thường được hiểu là **bảng điểm** (`transkrip nilai`) — một intent hoàn toàn khác. Vì vậy `transkrip` **luôn phải đi kèm `video`** ở mọi vị trí SEO (title, H1, H2, description). Không bao giờ để `transkrip` đứng trơ.
>
> Cấu trúc H1 cũng khớp **1:1 với trang anh em `/id/audio-to-text`** (`Transkrip Audio ke Teks`), giữ nhận diện cụm.

---

## Từ khóa phụ

### Nhóm Core (video → teks)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video ke teks | 1K–10K | ✅ đã search *(KW chính)* |
| transkrip video | 1K–10K | ✅ đã search |
| transkrip video ke teks | 1K–10K | ✅ đã search |
| video ke teks gratis | 100–1K | ✅ đã search |
| video jadi teks online | 10–100 | ✅ đã search |

### Nhóm Mengubah / Ubah (register trang trọng + khẩu ngữ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| mengubah video menjadi teks | 100–1K | ✅ đã search *(trang trọng)* |
| mengubah video jadi teks | 100–1K | ✅ đã search *(khẩu ngữ)* |
| cara mengubah video menjadi teks | 100–1K | ✅ đã search |
| mengubah video ke tulisan | 0–10 | ✅ đã search |

### Nhóm Convert (code-mixing — GIỮ NGUYÊN tiếng Anh)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| convert video ke teks | 100–1K | ✅ đã search |
| convert video ke teks gratis | 10–100 | ✅ đã search |

### Nhóm Suara / Ekstrak (nhấn nguồn là TIẾNG NÓI trong video)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| mengubah suara video menjadi teks | 10–100 | ✅ đã search |
| ekstrak teks dari video | 10–100 | ✅ đã search |

### Nhóm Aplikasi / Otomatis / Format

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transkrip video otomatis | 10–100 | ✅ đã search |
| aplikasi mengubah video jadi teks | 0–10 | ✅ đã search |
| ubah mp4 jadi teks | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| konverter video ke teks | — | 🔄 dịch bổ sung (video to text converter) |
| transkrip rapat | — | 🔄 dịch bổ sung (transcribe meetings) |
| transkrip wawancara | — | 🔄 dịch bổ sung (transcribe interviews) |
| notulen | — | 🔄 dịch bổ sung (meeting minutes) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Indonesia **đã có file video trong tay** — bản ghi Zoom/Teams/Meet, screen recording, webinar, rekaman perkuliahan, footage phỏng vấn, clip nhận qua WhatsApp — và muốn lấy phần lời nói ra thành chữ để đọc, tìm kiếm, trích dẫn, làm notulen hoặc làm tài liệu.

Họ kỳ vọng:

- Unggah file là chạy, **tanpa install aplikasi**.
- **Gratis thật** — thị trường Indonesia cực nhạy giá; `gratis` nằm trong 2 keyword riêng.
- **Không giới hạn dung lượng / thời lượng** — rekaman rapat 2–3 tiếng là chuyện thường.
- Phân biệt được **nhiều người nói** (quan trọng nhất với notulen rapat).
- Nhận dạng tốt **Bahasa Indonesia** (lo ngại công cụ chỉ chạy tốt tiếng Anh).
- Chạy được trên **HP** — phần lớn traffic Indonesia là điện thoại.
- Xuất nhiều định dạng, đặc biệt **DOCX** (tài liệu) và **SRT** (subtitle).

### Khác biệt so với bản tiếng Anh

1. **Code-mixing là chuẩn mực, không phải lỗi.** `convert`, `online`, `transkrip`, `mp4`, `format` giữ nguyên tiếng Anh. Dịch thuần Indonesia (`berkas`, `daring`, `pengubahan`) sẽ trượt keyword và đọc như văn bản hành chính. Bản EN không có hiện tượng này.
2. **Hai register song song, cả hai đều có volume ngang nhau (100–1K).** `mengubah video menjadi teks` (trang trọng → H2/quickAnswer) và `mengubah video jadi teks` (khẩu ngữ → body/FAQ). Bản EN chỉ có một cách nói "convert a video to text", nên phải chủ động phân bổ ra 2 vị trí khác nhau.
3. **`transkrip` mang nghĩa kép, bản EN không có rủi ro này.** `transkrip` đứng một mình = *bảng điểm* (`transkrip nilai`). Luôn viết `transkrip video`. Đây là ràng buộc ngôn ngữ riêng của bản id.
4. **`unduh` bị nhiễm intent nặng hơn "download" của bản EN.** Nhóm truy vấn `download video` cực phổ biến ở Indonesia (người dùng muốn tải video về máy, không phải lấy chữ). Quy tắc cứng: `unduh` / `download` **chỉ đi với `transkrip` / `teks` / `file` teks**, **không bao giờ** đứng cạnh `video`. Vì vậy item cuối section 7 của bản EN ("Downloaded and archived video") được đổi thành **`Video simpanan dan arsip`** — vẫn đúng số item, vẫn đúng ý, nhưng cắt sạch tín hiệu `download video`.
5. **`gratis` nặng ký hơn "free" của bản EN.** Lặp ở title, ogTitle, description, H2 section 4, FAQ 1, FAQ 4 và conclusion.
6. **Nhóm `suara video` / `ekstrak teks dari video` là intent riêng.** Người dùng nói rõ họ muốn lấy **tiếng nói bên trong video**, không phải chữ hiển thị trên màn hình — giúp phân định với intent OCR. Dùng ở section 5, section 8 và FAQ 9.

---

## Đối tượng người dùng

- Mahasiswa (rekaman perkuliahan, skripsi, penelitian)
- Nhân viên văn phòng (rekaman rapat Zoom/Teams/Meet → notulen)
- Nhà báo / Wartawan (bóc băng phỏng vấn quay hình)
- Giáo viên, người làm kursus online (screen recording → modul)
- Nhà nghiên cứu định tính (transkrip FGD quay hình)
- Content creator, marketer (webinar → bài viết)
- Người tạo subtitle (SRT/VTT)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `id.json` phải dịch đúng **11 section**, cùng số đoạn `content`, đúng **10 `specs`**, đúng **4 `steps`**, section 6 = `intro` 1 + `items` **4**, section 7 = `intro` 1 + `items` **6**, đúng **10 FAQ** (khác `/id/audio-to-text` vốn có 11), conclusion 2 đoạn.

| # | H2 (id) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Transkrip Video ke Teks | video ke teks, transkrip video, transkrip video ke teks *(KW chính + 2 đồng hạng)* |
| — | **quickAnswer** | **cara mengubah video menjadi teks** *(đặt nguyên văn ở `question`)* |
| 1 | Apa Itu Konversi Video ke Teks? | video ke teks, transkrip video, ekstrak teks dari video |
| 2 | Transkrip Video ke Teks Sekilas | *(bảng 10 thông số — Gratis / tanpa batas / 100+ bahasa)* |
| 3 | Cara Mengubah File Video Menjadi Teks | mengubah video menjadi teks, mengubah video jadi teks |
| 4 | Konverter Video ke Teks Gratis | **video ke teks gratis**, convert video ke teks, convert video ke teks gratis, aplikasi mengubah video jadi teks, video jadi teks online |
| 5 | Transkrip Video ke Teks dengan Akurat | **transkrip video ke teks**, transkrip video, transkrip video otomatis, mengubah suara video menjadi teks |
| 6 | Format Video yang Didukung | *(MP4, MOV, AVI, MKV, WebM)* + **ubah mp4 jadi teks** |
| 7 | Apa Saja yang Bisa Ditranskrip | *(Zoom/Teams/Meet, screen recording, webinar, seminar kampus, perkuliahan)* + transkrip rapat, transkrip wawancara |
| 8 | Seberapa Akurat Konversi Video ke Teks? | mengubah suara video menjadi teks, mengubah video menjadi teks |
| 9 | Video ke Teks dalam Lebih dari 100 Bahasa | video ke teks, video jadi teks online *(+ nhấn Bahasa Indonesia)* |
| 10 | Ekspor dalam Lima Format | *(4 internal link: /id/audio-to-text, /id/youtube-transcript, /id/tiktok-transcript, /id/instagram-transcript)* |
| 11 | Pertanyaan yang Sering Diajukan | video ke teks gratis, mengubah video ke tulisan, ekstrak teks dari video, aplikasi mengubah video jadi teks + long-tail |
| — | **conclusion** | mengubah video jadi teks, gratis |

### Ghi chú riêng cho bản id (KHÔNG tạo section mới)

- **`ubah mp4 jadi teks` đặt đúng 1 lần**, trong item `MP4` của section 6 — đúng chỗ bản EN đang nói về định dạng MP4. Không thêm câu.
- **Lo ngại "có hỗ trợ Bahasa Indonesia không"** xử lý bằng cách **đổi ví dụ ngôn ngữ ở section 9**: bản EN dùng German/Vietnamese → bản id đổi thành **Bahasa Indonesia + bahasa Inggris**. Vẫn đúng 2 đoạn, không thêm câu.
- **Thông điệp "tidak perlu install aplikasi"** đã có sẵn trong bản EN (section 4 + FAQ 9) — chỉ cần chọn đúng từ `aplikasi` khi dịch để bắt KW `aplikasi mengubah video jadi teks`, không viết thêm.
- **Ví dụ ngữ cảnh Indonesia** (seminar kampus, kajian, WhatsApp, perkuliahan) chỉ **thay chỗ ví dụ chung chung của bản EN** trong section 7 — số item vẫn đúng 6.
- Cặp `mengubah` / `ubah`: dạng đầy đủ `mengubah` dùng ở H2 và quickAnswer, dạng rút gọn `ubah` dùng ở `hero.button`, body và conclusion — phủ cả hai register mà không đội thêm câu.

---

## Không nên tối ưu cho các keyword

- `transkrip audio` / `mp3 ke teks` / `mengubah audio menjadi teks` → **/id/audio-to-text** (file âm thanh). Dữ liệu đã tự tách sạch (0 keyword trùng), chỉ cần không chủ động kéo về.
- `transkrip YouTube` / `TikTok` / `Instagram` / `download subtitle YouTube` → **các trang nền tảng riêng** (tempel link, không unggah file).
- **`download video` / `aplikasi download video` / `convert mp4 ke mp3` / `kompres video`** → **intent xử lý FILE video**, không phải lấy chữ. Quy tắc cứng: `unduh` / `download` chỉ đi với `transkrip` / `teks` / `file` teks, **không bao giờ** với `video`.
- `transkrip nilai` / `transkrip akademik` → **bảng điểm**, intent hoàn toàn khác. Đây chính là lý do `transkrip` không bao giờ đứng một mình.
- `ekstrak teks dari gambar` / `OCR` / `baca tulisan di video` → **intent đọc chữ TRÊN màn hình**. Trang này lấy **tiếng nói**; nhóm `suara video` giúp phân định điều này.
- `menambahkan subtitle ke video` → intent gắn phụ đề; trang này chỉ **xuất file SRT/VTT** (section 10 + FAQ 8), không gắn hộ.
- `teks ke suara` / `text to speech` → **ngược intent**.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link**:

- → `/id/audio-to-text` — khi nguồn là **file âm thanh** (MP3, WAV, M4A) thay vì video. *(phân định LOẠI FILE)*
- → `/id/youtube-transcript`, `/id/tiktok-transcript`, `/id/instagram-transcript` — khi video **nằm trên nền tảng**, tempel link thay vì unggah file. *(phân định FILE vs LINK)*

---

## Ghi chú kỹ thuật cho id.json

- `dir="ltr"` — không cần đảo layout.
- Xưng hô **"Anda"** xuyên suốt, nhất quán với `/id/audio-to-text`. KHÔNG dùng `kamu` / `kalian`.
- Nhãn `specs` **giống hệt 10 nhãn của `/id/audio-to-text`**: `Harga` / `Perlu akun` / `Instalasi` / `Batas ukuran file` / `Format yang diterima` / `Bahasa` / `Pemisahan pembicara` / `Timestamp` / `Format ekspor` / `Perangkat`. **Chỉ đổi giá trị của `Format yang diterima`** sang định dạng video (MP4, MOV, AVI, MKV, WebM).
  > 📌 Brief ghi nhãn là `Format yang didukung`, nhưng file `/id/audio-to-text/id.json` thực tế dùng **`Format yang diterima`**. Yêu cầu "tái dùng ĐÚNG 10 nhãn của trang anh em" được ưu tiên → giữ `Format yang diterima`. (`Format Video yang Didukung` vẫn xuất hiện, nhưng ở **H2 section 6**, đúng như bản EN.)
- Giữ nguyên Latin: **MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT**; thương hiệu **TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad, WhatsApp, YouTube, TikTok, Instagram**.
- Từ mượn đã chuẩn KBBI (`transkrip`, `konversi`, `konverter`, `format`, `file`, `aplikasi`, `online`, `gratis`, `timestamp`, `subtitle`, `browser`) giữ nguyên — **không** thay bằng từ thuần (`berkas`, `daring`, `cuma-cuma`, `penanda waktu`, `peramban`) vì người dùng không search bằng những từ đó.
- **Không được xuất hiện**: `tukar`, `kepada`, `percuma`, `boleh`, `sahaja`, `muat turun`, `fail`.
- Internal link section 10 giữ cú pháp markdown, path `/id/...`.
- Cấu trúc JSON khớp 100% `en.json`: **11 section**, **10 specs**, **4 steps**, S6 intro 1 + items 4, S7 intro 1 + items 6, **10 FAQ**, conclusion 2 đoạn.
