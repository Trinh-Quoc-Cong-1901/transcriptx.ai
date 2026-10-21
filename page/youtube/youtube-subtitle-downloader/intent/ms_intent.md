🔥 TranscriptX – YouTube Subtitle Downloader (Malay / ms)

URL:
/ms/youtube-subtitle-downloader

Intent chính:

download sarikata youtube (SRT · VTT, percuma)

Trang này nhắm đến người dùng Malaysia muốn **tải file phụ đề có cap masa (timecode)** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại kèm sarikata, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu tiếp cận.

---

## 🚨 CỤM YOUTUBE 5 TRANG — TRANG NÀY LÀ BÊN **NHẬN** KEYWORD

Repo có 5 trang YouTube. Quy tắc phân chia **theo ngữ nghĩa từ**, đã chốt từ khi làm `/ms/download-youtube-transcript`:

> **Từ nghĩa "phụ đề" (`sarikata`) → TRANG NÀY**
> **Từ nghĩa "bản chép lời" (`transkrip`) → `/ms/download-youtube-transcript`**

Căn cứ: bản EN section 1 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Trang này ĐƯỢC NHẬN cụm `sarikata` từ trang đối xứng

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `download sarikata youtube` | 0 – 10 | Cụm mạnh nhất của trang. `/ms/download-youtube-transcript` đã nhường — trang đó chỉ dùng 1 lần ở câu trỏ sang đây (section 6). **Trang này lấy làm H1.** |
| `muat turun sarikata youtube` | 0 – 10 | Biến thể thuần Mã Lai của cụm trên. Trang kia không dùng. |
| `download fail sarikata youtube` | 0 – 10 | Trang kia không dùng. |

### ⚠️ CỤM TRANG ĐỐI XỨNG ĐANG GIỮ — KHÔNG LẤY LẠI

`/ms/download-youtube-transcript` giữ nguyên văn cụm **`download sarikata YouTube dalam teks`** (vế `dalam teks`) trong section 6 đoạn 2. Trang này **không được dùng lại vế `dalam teks`** ở bất kỳ đâu — chỉ dùng `download sarikata youtube` trần hoặc kèm `fail`/`SRT`/`VTT`.

### ⚠️ QUYẾT ĐỊNH CHÉO TRANG CHO TƯƠNG LAI — `extract sarikata youtube`

Cụm `extract sarikata youtube` (0–10) sẽ dễ bị `/ms/youtube-transcript` giành khi làm sau này.

**Chốt: thuộc TRANG NÀY.** Lý do: `sarikata` = phụ đề, và `extract` ở đây là trích **fail sarikata** ra khỏi video — đúng việc trang này làm. Khi làm `/ms/youtube-transcript`, trang đó phải bám nhóm `transkrip`/`teks`/`tukar kepada teks`, không được lấy cụm này.

---

## Từ khóa chính

download sarikata youtube (0–10) ✅ *đã search* — **H1**

## Từ khóa đồng hạng

muat turun sarikata youtube (0–10) ✅ *đã search* — biến thể thuần Mã Lai, đặt ở conclusion H2 + quickAnswer

---

## Từ khóa phụ

### Nhóm download / muat turun (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download sarikata youtube | 0–10 | ✅ đã search *(KW chính)* |
| muat turun sarikata youtube | 0–10 | ✅ đã search |
| cara download sarikata youtube | 0–10 | ✅ đã search |
| cara muat turun sarikata youtube | 0–10 | ✅ đã search |
| download sarikata dari video youtube | 0–10 | ✅ đã search |
| download fail sarikata youtube | 0–10 | ✅ đã search |
| download sarikata youtube srt | 0–10 | ✅ đã search |
| extract sarikata youtube | 0–10 | ✅ đã search |

**8/8 keyword của danh sách ms đều đã search — không có dòng rác, không có cụm sai intent.**

### Dịch bổ sung (chỉ rải body, KHÔNG đặt ở title/h1/h2/description)

| Keyword | Nguồn |
| ------- | ----- |
| fail sarikata VTT | 🔄 dịch bổ sung (VTT file) |
| sarikata youtube percuma | 🔄 dịch bổ sung (free) |
| terjemah sarikata | 🔄 dịch bổ sung (translate subtitles) |
| sunting fail sarikata | 🔄 dịch bổ sung (edit subtitle file) |
| cap masa / bertimecode | 🔄 dịch bổ sung (timecode) |
| sarikata untuk youtube | 🔄 dịch bổ sung (subtitles for youtube) |

**Tỉ lệ: 8 keyword đã search / 6 cụm dịch bổ sung ≈ 57% đã search.**

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Mã Lai **cần fail sarikata để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn sarikata vào bản dựng.
- Đăng lại video lên kênh mình kèm sarikata mà không phải gõ lại.
- Dịch sarikata sang tiếng Mã Lai hoặc tiếng Anh rồi gắn lại.
- Sửa sarikata tự động của YouTube vốn hay sai với tiếng Mã Lai pha tiếng Anh.
- Đáp ứng yêu cầu tiếp cận cho người khiếm thính.

Họ kỳ vọng: tampal pautan là ra fail, chọn được SRT hay VTT, có cap masa từng dòng, mở sửa được, percuma, không cài extension.

### Khác biệt so với bản tiếng Anh

1. **`sarikata` là trục duy nhất.** Bản EN xen kẽ `subtitles` / `captions` để đỡ lặp; tiếng Mã Lai chỉ có `sarikata` (từ `subtitle` bị cấm vì trùng dạng Indonesia). Chống lặp bằng `fail sarikata` / `baris sarikata` / `cap masa` / `teks bermasa`.
2. **Song ngữ `download` / `muat turun`.** Người Mã Lai gõ cả hai; `download` là dạng vay mượn phổ biến hơn trong query, `muat turun` là dạng chuẩn. Dùng **cả hai** — `download` ở H1/title, `muat turun` ở H2 phụ và body.
3. **Volume toàn cụm rất thấp (0–10).** Không có cụm nào đủ mạnh để đè, nên phủ đều cả 8 biến thể thay vì dồn vào một cụm — khác bản ko (có cụm 1K–10K để dồn).
4. **Trang này là bên NHẬN keyword.** Bản EN không có vấn đề phân chia vì `transcript` và `subtitle` tách bạch tự nhiên. Tiếng Mã Lai cũng khá tách bạch (`transkrip` vs `sarikata`), nhưng trang đối xứng đã dùng `sarikata` một lần nên phải chốt bằng tay.

---

## Đối tượng người dùng

- Editor video, freelancer dựng phim (nạp SRT vào Premiere/Final Cut/Resolve)
- Người re-upload / tổng hợp video lên kênh riêng
- Người làm sarikata (dịch sub) cho khán giả Malaysia
- Marketer chạy nội dung đa ngôn ngữ (ms/en)
- Người làm nội dung tiếp cận cho người khiếm thính
- Người muốn sửa sarikata tự động sai của YouTube

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ms.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ms) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Download Sarikata YouTube | download sarikata youtube *(KW chính)* |
| — | **quickAnswer** | cara download sarikata youtube |
| 1 | Apa Itu Fail Sarikata Sebenarnya | download fail sarikata youtube, extract sarikata youtube |
| 2 | SRT atau VTT: Format Sarikata Mana Yang Patut Anda Download | download sarikata youtube srt |
| 3 | Cara Download Sarikata Daripada YouTube | cara download sarikata youtube, cara muat turun sarikata youtube |
| 4 | Apa Yang Boleh Anda Buat Dengan Fail Sarikata Yang Dimuat Turun | download sarikata dari video youtube |
| 5 | Muat Turun Sarikata Dalam Lebih 100 Bahasa | muat turun sarikata youtube *(+ nhấn tiếng Mã Lai)* |
| 6 | Sarikata, Transkrip atau Ringkasan? | *(3 internal link — chốt phân định)* |
| 7 | Soalan Lazim | long-tail + biến thể |
| — | **conclusion** | muat turun sarikata youtube, percuma |

### Ghi chú riêng cho bản ms (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là chỗ duy nhất được nhắc `transkrip` (thuộc trang kia).
- Section 1 đoạn 2 là **định nghĩa ranh giới của bản EN** (`transkrip` = chữ để đọc, `fail sarikata` = chữ chạy đè lên video). Dịch sát — đây là câu chống cannibalization mạnh nhất trang.
- Nỗi lo nhận dạng tiếng Mã Lai (và câu pha tiếng Anh) xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.

---

## 🛡️ Bảng chống trùng ms ↔ id

`/id/youtube-subtitle-downloader` là trang song sinh gần nhất (hai ngôn ngữ hiểu chéo được). Bắt buộc tách từ vựng:

| Khái niệm | ms — **DÙNG** | id — **CẤM trong ms.json** |
| --------- | ------------- | -------------------------- |
| phụ đề | `sarikata` | `subtitle` (dạng Indo trong nội dung) |
| tải xuống | `muat turun` / `download` | `unduh` |
| tệp | `fail` | `berkas` |
| miễn phí | `percuma` | `gratis` |
| có thể | `boleh` | `bisa` |
| chỉ / thôi | `sahaja` | `saja` |
| dán | `tampal` | `tempel` |
| liên kết | `pautan` | `tautan` |
| trình duyệt | `pelayar` | `peramban` |
| lựa chọn | `pilihan` | `opsi` |
| cài đặt (phần mềm) | `pemasangan` | `instalasi` |

Lưu ý: `download` vẫn được dùng trong ms.json vì đó **chính là keyword đã search** (`download sarikata youtube`) — dạng vay mượn này phổ biến ở cả hai thị trường, nhưng cặp `sarikata` + `fail` + `percuma` + `boleh` + `pautan` đủ để tách hoàn toàn hai bản.

---

## Không nên tối ưu cho các keyword

- **`download transkrip youtube` / `muat turun transkrip youtube`** → **/ms/download-youtube-transcript** (tài liệu để đọc/lưu/nộp). Chỉ được nhắc ở section 6.
- **`download sarikata youtube dalam teks`** → cụm trang đối xứng đang giữ, **không lấy lại**.
- `transkrip youtube` / `lihat transkrip youtube` → **/ms/youtube-transcript** (đọc trên màn hình, không tải fail).
- `ringkasan video youtube` → **/ms/youtube-video-summarizer**.
- **`download video youtube` / `muat turun video youtube` / `youtube downloader`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **fail sarikata**. Quy tắc: `download`/`muat turun` chỉ đi với `sarikata`/`fail`/`SRT`/`VTT`, **KHÔNG BAO GIỜ** với `video`.
- `cara buka sarikata youtube` / `tetapan sarikata` → **hướng dẫn bật phụ đề trong app**, không phải công cụ tải.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → /ms/youtube-transcript (đọc chữ thuần trên màn hình, không cap masa)
- → /ms/download-youtube-transcript (lưu chữ thành TXT/DOCX/PDF) — **đây là trang đối xứng, link quan trọng nhất**
- → /ms/youtube-video-summarizer (chỉ cần ý chính)

---

## Ghi chú kỹ thuật cho ms.json

- Xưng hô **"anda"**, nhất quán với các trang Mã Lai khác trong repo.
- Giữ nguyên Latin: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok**.
- Internal link section 6 giữ cú pháp markdown, path `/ms/...`.
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 = `intro` 1 + `items` **2**, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5/S6 = `content` 2, S7 `items` 8, conclusion `content` 2. **KHÔNG có `specs`.**
- Verify bằng `shape_check.py en.json ms.json` → phải in `ms.json -> True`, rồi grep xác nhận không dính từ Indo bị cấm.
