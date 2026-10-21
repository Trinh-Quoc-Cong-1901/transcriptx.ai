🔥 TranscriptX – Video to Text (Malay / ms)

URL:
/ms/video-to-text

Intent chính:

video ke teks (tukar fail video kepada teks percuma dalam talian)

Trang này là **bản tiếng Mã Lai của trang trụ (hub)** cụm Video to Text. Nhắm đến người dùng Malaysia / Brunei / Singapore **đã có sẵn fail video** (MP4, MOV, AVI, MKV, WebM — rakaman mesyuarat Zoom/Teams, rakaman skrin, footage kamera) và muốn lấy phần **suara dalam video** ra thành teks để đọc, cari, petik, buat minit hoặc buat sarikata.

Gộp toàn bộ intent đồng nghĩa **transkrip / tukar / convert / ekstrak** vì tất cả cho ra **cùng một kết quả**: fail video → teks.

---

> ⚠️ **Phân định với `/ms/audio-to-text`: LOẠI FILE.** Trang này nhận **fail VIDEO** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **fail AUDIO** (MP3, WAV, M4A, AAC, FLAC, OGG). Kiểm tra dữ liệu: hai danh sách keyword có **0 keyword trùng nhau** — người dùng Mã Lai tự phân biệt rất sạch giữa `video ke teks` và `transkrip audio ke teks`. Chốt chặn nằm ở **section 10 đoạn 3** (link sang `/ms/audio-to-text`). Không kéo keyword audio về trang này.

> ⚠️ **Phân định với các trang nền tảng: FILE vs LINK.** Trang này để **muat naik fail** từ peranti; các trang `/ms/youtube-transcript`, `/ms/tiktok-transcript`, `/ms/instagram-transcript` để **tampal pautan**. Cả 4 internal link nằm cùng **section 10 đoạn 3**, và câu chốt phải nói rõ hai cơ chế khác nhau (muat naik fail vs tampal pautan) để không ăn thịt lẫn nhau.

> 🚨 **CHỐNG TRÙNG VỚI `/id/video-to-text` (đã hoàn thành, H1 = `Transkrip Video ke Teks`).**
>
> **Sự thật dữ liệu, không phải lỗi:** ba keyword mạnh nhất của ms và id **trùng nhau từng ký tự** và **cùng band `1K – 10K`**:
>
> | Keyword | ms | id |
> | ------- | -- | -- |
> | video ke teks | 1K – 10K | 1K – 10K |
> | transkrip video | 1K – 10K | 1K – 10K |
> | transkrip video ke teks | 1K – 10K | 1K – 10K |
>
> Đây là hệ quả của việc Malay và Indonesian dùng chung gốc từ `video`, `ke`, `teks`, `transkrip`. **Không thể tránh trùng ở vùng H1/title** — và cũng không nên tránh, vì đó là keyword có volume cao nhất của cả hai thị trường. Hai trang tách nhau bằng **hreflang `ms` vs `id`** và bằng **toàn bộ phần còn lại của nội dung**.
>
> **Biện pháp tách chặt phần còn lại:**
>
> - **H1 khác chuỗi:** id dùng `Transkrip Video ke Teks`; ms dùng **`Video ke Teks`** (ngắn hơn, khớp đúng KW #1, và không lặp lại nguyên chuỗi H1 của id).
> - **Title khác hẳn:** id = `Transkrip Video ke Teks — Ubah Video Jadi Teks Gratis`; ms = `Video ke Teks — Tukar Video kepada Teks Percuma`.
> - **Bảng từ vựng bắt buộc:**
>
> | Ý nghĩa | ✅ ms (dùng) | ❌ id (CẤM tuyệt đối ở file này) |
> | ------- | ----------- | ------------------------------ |
> | chuyển đổi | **tukar** | mengubah / ubah / mengonversi |
> | trở thành | **kepada** | menjadi / jadi |
> | miễn phí | **percuma** | gratis |
> | có thể | **boleh** | bisa |
> | chỉ | **sahaja** | saja |
> | tải lên | **muat naik** | unggah |
> | tải xuống | **muat turun** | unduh |
> | tệp | **fail** | berkas / file |
> | trình tạo | **penjana** | pembuat / generator |
> | trình chuyển đổi | **penukar** | konverter |
> | phần mềm | **perisian** | software / perangkat lunak |
> | trực tuyến | **dalam talian** | online / daring |
> | thiết bị | **peranti** | perangkat |
> | trình duyệt | **pelayar** | browser |
> | điện thoại | **telefon** | HP |
> | phụ đề | **sarikata** | subtitle |
> | cuộc họp | **mesyuarat** | rapat |
> | phỏng vấn | **temu bual** | wawancara |
> | biên bản | **minit** | notulen |
> | dấu thời gian | **cap masa** | timestamp |
>
> - **Ví dụ ngữ cảnh phải khác hẳn.** `id.json` đã dùng: *seminar kampus*, *kajian yang direkam panitia*, *klip dikirim teman lewat WhatsApp*, *wartawan*. Bản ms ở **section 7** dùng bối cảnh Malaysia khác hẳn: *taklimat jabatan*, *bengkel latihan*, *kelas dalam talian / MOOC*, *majlis dan ceramah*, *klip dihantar melalui Telegram*. Không lặp lại bất kỳ ví dụ nào của id.

> ⚠️ **LỖI DỮ LIỆU trong `2_loc_kw.md` section `## Malay (ms)`.**
>
> 1. **Dòng bị dính volume + keyword vào nhau:** dòng `0 – 10ekstrak teks dari video` là **hai thứ bị nối liền** — `0 – 10` là volume của keyword đứng trước nó (`tukar suara video kepada teks`), còn `ekstrak teks dari video` là **một keyword riêng** có volume `10 – 100` ở dòng kế tiếp. Đã tách đúng.
> 2. **Không có dòng rác `Keyword ideas` / `Keywords you provided`** trong section ms (khác với de, es, fr, vi vốn có).
> 3. **Không có keyword trùng lặp** trong section ms (khác với es vốn lặp `desgrabador video online`).
> 4. **Số keyword thực: 15.** Đếm thô theo cặp dòng sẽ ra **14** vì dòng dính ở mục (1) làm mất một keyword. Con số đúng là **15**.

---

## Từ khóa chính

**video ke teks** (1K – 10K) ✅ *đã search*

> Chọn KW này làm H1 vì: (a) nằm ở **band cao nhất** `1K – 10K`, (b) là **lõi chung** của 3 KW đuôi dài khác trong danh sách (`transkrip video ke teks`, `video ke teks percuma`, `tukar video ke teks`), nên phủ luôn mà không phải lặp, (c) chuỗi ngắn, **không trùng nguyên văn H1 của `/id/video-to-text`**.

## Từ khóa đồng hạng

**transkrip video** (1K – 10K) ✅ *đã search* — đặt ở `seo.title`... không, đặt ở **H2 section 5** và `schemaDescription`.

**transkrip video ke teks** (1K – 10K) ✅ *đã search* — đặt ở **H2 section 5** (nguyên văn) và FAQ.

Ba KW này cùng band cao nhất. `video ke teks` lấy H1; hai KW `transkrip...` phân bổ xuống section 1 và section 5 để không dồn một chỗ.

---

## Từ khóa phụ

### Nhóm Core (video → teks, band cao nhất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video ke teks | 1K – 10K | ✅ đã search *(KW chính)* |
| transkrip video | 1K – 10K | ✅ đã search |
| transkrip video ke teks | 1K – 10K | ✅ đã search |

### Nhóm Tukar (động từ chuyển đổi)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tukar video kepada teks | 10 – 100 | ✅ đã search |
| tukar video ke teks | 0 – 10 | ✅ đã search |
| cara tukar video kepada teks | 0 – 10 | ✅ đã search |
| tukar video kepada teks dalam talian | 0 – 10 | ✅ đã search *(biến thể `... online` — xem ghi chú)* |
| tukar video ke tulisan | 0 – 10 | ✅ đã search |

### Nhóm Percuma (miễn phí)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video ke teks percuma | 0 – 10 | ✅ đã search |
| transkrip video percuma | 0 – 10 | ✅ đã search |

### Nhóm Suara / Ekstrak (nhấn nguồn là ÂM THANH — chống nhiễm OCR)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tukar suara video kepada teks | 0 – 10 | ✅ đã search *(dòng bị dính — đã tách)* |
| ekstrak teks dari video | 10 – 100 | ✅ đã search |

### Nhóm Format / Aplikasi

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tukar mp4 ke teks | 0 – 10 | ✅ đã search |
| aplikasi tukar video kepada teks | 0 – 10 | ✅ đã search |

### KW đã search nhưng KHÔNG dùng

| Keyword | Volume | Lý do loại |
| ------- | ------ | ---------- |
| tukar video jadi teks | 0 – 10 | Chứa **`jadi`** — từ Indonesia nằm trong danh sách cấm tuyệt đối để chống trùng với `/id/video-to-text`. Volume `0 – 10` không đủ để đánh đổi rủi ro trùng. **Bỏ hoàn toàn.** |

### Dịch bổ sung (chỉ rải body, KHÔNG đặt vào title/H1/H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| penukar video ke teks | — | 🔄 dịch bổ sung (video to text converter) |
| penjana transkrip video | — | 🔄 dịch bổ sung (video transcript generator) |
| transkrip mesyuarat | — | 🔄 dịch bổ sung (transcribe meetings) |
| transkrip temu bual | — | 🔄 dịch bổ sung (transcribe interviews) |
| transkrip kuliah | — | 🔄 dịch bổ sung (transcribe lectures) |
| fail video ke teks | — | 🔄 dịch bổ sung (video file to text) |
| transkrip video bahasa Melayu | — | 🔄 dịch bổ sung (Malay video transcription) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, được phép đặt vào `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = **chỉ rải body** (`content`, `steps`, `items`, FAQ answers).

---

## Search Intent

Người dùng Mã Lai **đã có fail video trong tay** — rakaman mesyuarat Zoom/Teams/Meet, rakaman skrin, webinar, kuliah dalam talian, footage kamera atau telefon — và muốn lấy phần **pertuturan** ra thành chữ để đọc, cari, petik, buat minit mesyuarat, buat nota ulang kaji hoặc buat sarikata.

Họ kỳ vọng:

- **Muat naik fail là chạy**, không cần pasang perisian.
- **Tanpa had saiz / panjang** — rakaman mesyuarat 2–3 jam là chuyện thường.
- Phân biệt được **berbilang penutur** (quan trọng nhất với minit mesyuarat).
- **Percuma thật** — 2 keyword riêng chứa `percuma`.
- Nhiều **format eksport**, đặc biệt **DOCX** để làm dokumen và **SRT** để làm sarikata.
- Nhận dạng tốt **bahasa Melayu** và rakaman trộn Melayu–English.
- Chạy tốt trên **telefon** (thị trường mobile-first rất mạnh).

### Khác biệt so với bản tiếng Anh

1. **`transkrip` là danh từ trụ, ngang hàng với động từ.** Bản EN có trục động từ rõ (`convert` / `transcribe`). Tiếng Mã Lai có **danh từ `transkrip video` đạt cùng band cao nhất `1K – 10K`** với `video ke teks`, trong khi động từ `tukar video kepada teks` chỉ `10 – 100`. Vì vậy phải phân bổ: danh từ `transkrip` giữ H2 section 1 và 5; động từ `tukar` giữ H2 section 3 và quickAnswer — không dồn hết vào động từ như bản EN.
2. **`percuma` nặng ký hơn "free" của bản EN.** Có 2 keyword riêng chứa `percuma` (`video ke teks percuma`, `transkrip video percuma`), trong khi bản EN chỉ có `free` như một tính từ phụ trợ. Cần lặp `percuma` ở title, H1 subtitle, H2 section 4 và conclusion.
3. **Nhóm `suara video` / `ekstrak teks dari video` là intent riêng và là bẫy OCR.** `ekstrak teks dari video` (10 – 100) có thể bị hiểu nhầm thành **đọc chữ TRÊN màn hình** (OCR). Bản EN không có mơ hồ này. Phải chủ động chốt nguồn là **âm thanh** bằng cụm `tukar suara video kepada teks` ở **section 5 và section 8**, và đóng khung `ekstrak teks dari video` bằng ngữ cảnh pertuturan.
4. **Code-switching Anh–Mã là bình thường ở Malaysia.** Giữ nguyên Latin cho MP4/MOV/AVI/MKV/WebM/TXT/DOCX/PDF/SRT/VTT và tên thương hiệu, không "Mã hoá" chúng — người dùng gõ lẫn hai thứ tiếng.
5. **Bối cảnh đa ngôn ngữ trong một rakaman.** Người Malaysia thường có rakaman trộn Melayu–English–Mandarin–Tamil. Section 9 phải nhắc rõ **bahasa Melayu** để trấn an — chèn vào **đúng câu ví dụ đã có sẵn** của bản EN (thay German/Vietnamese), KHÔNG thêm câu mới.

---

## Đối tượng người dùng

- Pekerja pejabat, setiausaha (rakaman mesyuarat Zoom/Teams/Meet → minit)
- Wartawan / pemberita (temu bual bergambar)
- Pensyarah, guru, pelajar (kuliah dan kelas dalam talian dirakam)
- Pasukan latihan & HR (rakaman skrin, bengkel → dokumentasi)
- Content creator & marketer Malaysia (webinar → artikel)
- Penggiat kandungan agama & penceramah (ceramah, majlis dirakam)
- Người làm sarikata (SRT/VTT)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ms.json` phải dịch đúng **11 section**, đúng **10 `specs`**, đúng **4 `steps`**, section 6 = `intro` 1 + `items` **4**, section 7 = `intro` 1 + `items` **6**, đúng **10 FAQ** (khác `/ms/audio-to-text` vốn có 11), `conclusion.content` **2** đoạn. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu.

| # | H2 (ms) | Keyword nhắm | Trạng thái |
| - | ------- | ------------ | ---------- |
| — | **H1:** Video ke Teks | video ke teks *(KW chính)* | ✅ |
| — | **quickAnswer** | cara tukar video kepada teks | ✅ |
| 1 | Apakah Itu Penukaran Video ke Teks? | video ke teks, transkrip video, ekstrak teks dari video | ✅ |
| 2 | Video ke Teks Sepintas Lalu | *(bảng 10 thông số — Percuma / tanpa had / 100+ bahasa)* | — |
| 3 | Cara Tukar Fail Video kepada Teks | cara tukar video kepada teks, tukar video kepada teks, muat naik fail | ✅ |
| 4 | Penukar Video ke Teks Percuma | video ke teks percuma, transkrip video percuma, aplikasi tukar video kepada teks, penjana transkrip video | ✅ + 🔄 |
| 5 | Buat Transkrip Video ke Teks dengan Tepat | **transkrip video ke teks**, transkrip video, tukar suara video kepada teks | ✅ |
| 6 | Format Video yang Disokong | tukar mp4 ke teks *(áp vào item MP4)* | ✅ |
| 7 | Apa yang Boleh Anda Transkrip | transkrip mesyuarat, transkrip temu bual, transkrip kuliah *(bối cảnh Malaysia)* | 🔄 |
| 8 | Sejauh Mana Tepatnya Penukaran Video ke Teks? | tukar suara video kepada teks, video ke teks | ✅ |
| 9 | Video ke Teks dalam Lebih 100 Bahasa | video ke teks, tukar video kepada teks dalam talian, transkrip video bahasa Melayu | ✅ + 🔄 |
| 10 | Eksport dalam Lima Format | *(4 internal link: /ms/audio-to-text, /ms/youtube-transcript, /ms/tiktok-transcript, /ms/instagram-transcript)* | — |
| 11 | Soalan Lazim | tukar video ke teks, tukar video ke tulisan, ekstrak teks dari video, video ke teks percuma, transkrip video percuma | ✅ |
| — | **conclusion** | video ke teks, percuma | ✅ |

### Ghi chú riêng cho bản ms (KHÔNG tạo section mới)

1. **Section 5 + Section 8** là hai nơi duy nhất chứa cụm `tukar suara video kepada teks`. Đây là **chốt chống nhiễm OCR**: nói rõ công cụ lấy **suara dalam video**, không phải chữ hiển thị trên skrin. Đặt đúng 1 lần mỗi section.
2. **`ekstrak teks dari video`** xuất hiện **đúng 2 lần**: section 1 đoạn 2 và FAQ #9. Mỗi lần đều phải nằm cạnh ngữ cảnh **pertuturan / suara** để không kéo về intent OCR.
3. **Section 9** — chèn `bahasa Melayu` vào **đúng câu ví dụ đã có sẵn** của bản EN (thay ví dụ German/Vietnamese bằng Melayu + một ngôn ngữ khác). Không thêm câu.
4. **Section 6** — `tukar mp4 ke teks` áp vào item MP4. Giữ đúng **4 item**, không thêm.
5. **Section 7 — ví dụ Malaysia bắt buộc khác id:** taklimat jabatan, bengkel latihan, kelas dalam talian / MOOC, majlis dan ceramah, Telegram. **Không dùng** seminar kampus / kajian panitia / WhatsApp (đã có ở `id.json`).
6. **Biến thể `tukar video kepada teks online`** — trong body dùng dạng chuẩn **`dalam talian`** để nhất quán thuật ngữ với `/ms/audio-to-text` (file đó dùng `dalam talian` xuyên suốt). `online` là từ nằm trong bảng cấm chống trùng id, nên **không viết dạng thô**; KW này được phủ ngữ nghĩa qua `dalam talian` ở section 9. Đây là đánh đổi có chủ ý: volume `0 – 10` không đáng để phá nhất quán thuật ngữ và mở cửa cho từ vựng id.
7. **`tukar video ke tulisan`** đặt ở FAQ #1 — nơi bản EN nói về "convert for free", ghép tự nhiên với `percuma`.
8. **Nhãn `specs`** copy **y nguyên chuỗi** từ `/ms/audio-to-text/ms.json`, chỉ đổi **giá trị** của `Format diterima` sang format video.

---

## Không nên tối ưu cho các keyword

- **`tukar video jadi teks`** (0 – 10, có trong danh sách đã search) → chứa `jadi`, từ Indonesia bị cấm ở file này. **Loại hoàn toàn**, không dùng dù chỉ trong body.
- `transkrip audio` / `tukar audio kepada teks` / `mp3 ke teks` → **/ms/audio-to-text** (fail âm thanh). Dữ liệu đã tự tách sạch (0 keyword trùng), chỉ cần không chủ động kéo về.
- `transkrip YouTube` / `transkrip TikTok` / `transkrip Instagram` / `sarikata YouTube` → **các trang nền tảng riêng** (tampal pautan, không muat naik fail).
- `tukar suara kepada teks` / nota suara / imlak → **/ms/voice-to-text**.
- **`muat turun video`** / `tukar MP4 kepada MP3` / `mampat video` → **intent xử lý FAIL video**, không phải lấy chữ. Quy tắc cứng: **`muat turun` chỉ đi với `transkrip` / `teks` / `fail teks`, KHÔNG BAO GIỜ với `video`.**
- `ekstrak teks dari gambar` / `OCR` / `baca teks pada skrin` → **intent đọc chữ TRÊN màn hình**, khác hẳn. Trang này lấy **suara**. Nhóm `tukar suara video kepada teks` ở section 5 + 8 là chốt phân định.
- `letak sarikata pada video` → intent gắn sarikata vào video; trang này chỉ **eksport fail SRT/VTT** (section 10 + FAQ #8), không gắn hộ.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link** — nhiều nhất trong các trang đã làm. Câu chốt phải phân định **hai trục** cùng lúc:

- **Trục LOẠI FILE:** → `/ms/audio-to-text` (khi nguồn là **fail audio** MP3/WAV/M4A thay vì fail video).
- **Trục FILE vs PAUTAN:** → `/ms/youtube-transcript`, `/ms/tiktok-transcript`, `/ms/instagram-transcript` (khi video nằm **trên nền tảng** — tampal pautan thay vì muat naik fail).

---

## Ghi chú kỹ thuật cho ms.json

- `lang="ms"`, `dir="ltr"`.
- **Cấu trúc JSON khớp 100% với `en.json`**: 11 section, 10 `specs`, 4 `steps`, S6 `intro` 1 + `items` 4, S7 `intro` 1 + `items` 6, **10 FAQ**, `conclusion.content` 2 đoạn. Verify bằng script so sánh shape.
- **Giữ nguyên Latin, không dịch:** MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT, TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad, YouTube, TikTok, Instagram, Telegram.
- Xưng hô **"anda"** xuyên suốt (trang trọng vừa phải, chuẩn Malaysia web copy). Không dùng "kamu" / "kau" / "Anda" viết hoa kiểu id.
- **Nhãn `specs` copy y nguyên** từ `/ms/audio-to-text/ms.json`: Harga / Akaun diperlukan / Pemasangan / Had saiz fail / Format diterima / Bahasa / Pengasingan penutur / Cap masa / Format eksport / Peranti. **Chỉ đổi giá trị** của `Format diterima` sang `MP4, MOV, AVI, MKV, WebM dan banyak lagi`.
- Internal link `sections[9]` giữ nguyên cú pháp markdown, path `/ms/...`.
- Số đếm dùng chữ số Latin (100+, 5).
- **Grep kiểm tra không lẫn từ Indonesia:** `unggah`, `unduh`, `gratis`, `bisa`, `saja`, `berkas`, `mengubah`, `menjadi`, `jadi`, `daring`, `wawancara`, `rapat`, `notulen`, `konverter`, `perangkat`, `subtitle`, `timestamp`, `browser`, `online`.
- **KHÔNG nhồi keyword.** Mật độ KW chính `video ke teks` giữ ~1%, ưu tiên văn phong tự nhiên.
