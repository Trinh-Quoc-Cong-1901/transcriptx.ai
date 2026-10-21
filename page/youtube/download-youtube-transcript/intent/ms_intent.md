🔥 TranscriptX – Download YouTube Transcript (Malay / ms)

URL:
/ms/download-youtube-transcript

Intent chính:

Tải transkrip video YouTube về máy (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Malaysia muốn **tải bản transkrip của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transkrip trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/ms/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt cho bản ms — phân theo NGỮ NGHĨA TỪ:**

> **`sarikata` (file phụ đề khớp giờ cho phần mềm dựng phim) → `/ms/youtube-subtitle-downloader`**
> **`transkrip` / `teks` (tài liệu để đọc / lưu / nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 đã tự vạch ranh giới — trang kia xuất *"a timed caption file for a video editor"*, trang này xuất *"a document"*.

### Kết quả kiểm trùng với `/ms/youtube-subtitle-downloader`

Danh sách ms của trang kia (8 cụm): `download sarikata youtube`, `cara download sarikata youtube`, `muat turun sarikata youtube`, `download sarikata dari video youtube`, `download fail sarikata youtube`, `download sarikata youtube srt`, `cara muat turun sarikata youtube`, `extract sarikata youtube`.

| Kiểm tra | Kết quả |
| -------- | ------- |
| Trùng **tuyệt đối** (chuỗi giống hệt) | **0 cụm** ✅ |
| Trùng **cụm gốc** (chứa `sarikata youtube`) | **1 cụm** ⚠️ — `download sarikata youtube dalam teks` (0–10) |

Bản ms **may mắn hơn bản vi**: cụm mạnh nhất của trang này là `download transkrip youtube` (**100 – 1K**) — mang từ `transkrip`, **thuộc đúng trang này**, không phải nhường đi. Bản vi phải nhường `tải phụ đề youtube` (100–1K) cho trang kia.

### Xử lý cụm trùng duy nhất

`download sarikata youtube dalam teks` (0–10) mang lõi `download sarikata youtube` → **thuộc `/ms/youtube-subtitle-downloader`**. Xử lý bằng kỹ thuật **neo đẩy đi**: dùng **đúng 1 lần**, ở **section 6 đoạn 2**, ngay bên trong câu trỏ sang trang kia. Bắt được tín hiệu keyword nhưng đẩy traffic sai intent về đúng trang thay vì giữ lại rồi bounce.

**Tuyệt đối không đặt vào `title` / `h1` / bất kỳ `h2` nào.**

### Quy tắc neo khi buộc phải nhắc `sarikata`

Kết quả của trang này **luôn gọi là `transkrip`/`teks`**. Chỉ có **2 chỗ** được nhắc `sarikata`, và phải neo rõ nó là thứ của trang khác:

| Vị trí | Cách neo bắt buộc |
| ------ | ----------------- |
| S2 — mục SRT | `fail sarikata bertimecode` (nói về việc *làm ra* sarikata, không phải kết quả trang này) |
| S6 đoạn 2 | `fail sarikata bertimecode` + cụm neo đẩy đi, trong câu trỏ sang `/ms/youtube-subtitle-downloader` |

---

## 🇲🇾🆚🇮🇩 BẢNG CHỐNG TRÙNG ms ↔ id

`/id/download-youtube-transcript` đang làm song song với cùng bộ nội dung nguồn. Hai bản **bắt buộc** khác nhau ở lớp từ vựng:

| Khái niệm | ✅ ms DÙNG | ❌ ms CẤM (là dạng id) |
| --------- | ---------- | --------------------- |
| tải xuống | `muat turun` / `download` | `unduh`, `mengunduh` |
| tập tin | `fail` | `berkas` |
| miễn phí | `percuma` | `gratis` |
| có thể | `boleh` | `bisa` |
| chỉ / thôi | `sahaja` | `saja` (đứng độc lập) |
| dán | `tampal` | `tempel` |
| liên kết | `pautan` | `tautan` |
| phụ đề | `sarikata` | `subtitle`, `takarir` |

Ghi chú grep: `sahaja` chứa chuỗi con `saja` — khi kiểm phải dùng biên từ (`\bsaja\b`), không grep thô.

Khác biệt cấu trúc bổ sung: ms giữ dạng `boleh anda`/`yang` chuẩn văn viết Malaysia, xưng **`anda`**; bản id thường xưng `Anda` viết hoa và dùng cấu trúc `bisa Anda`.

---

## Dòng dữ liệu nguồn

Phần `## Malay (ms)` của `2_loc_kw.md` sạch — **không có dòng rác** kiểu `Keyword ideas` / `Keywords you provided` (bản vi có 2 dòng rác), và **không có cụm sai intent tải VIDEO** (bản vi phải loại 4 cụm).

**Số keyword thực: 10 dòng thô − 0 rác − 0 sai intent = 10 keyword.** Trong đó **1 cụm nhường trang khác** → **9 cụm dùng làm trục chính.**

---

## Từ khóa chính

**download transkrip youtube** (100 – 1K) ✅ *đã search*

Đây là cụm mạnh nhất trong toàn bộ danh sách ms và nó mang từ `transkrip` → thuộc đúng trang này. Người Malaysia dùng lẫn từ mượn `download` và từ chuẩn `muat turun`; cụm có `download` volume gấp ~10 lần. Chiến lược: **`download transkrip YouTube` vào `title`/`h1`**, còn `muat turun` phủ dày ở body và các H2 để bắt trọn nhóm biến thể chuẩn.

---

## Từ khóa phụ

### Nhóm Transkrip (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download transkrip youtube | 100–1K | ✅ đã search *(KW chính)* |
| muat turun transkrip youtube | 0–10 | ✅ đã search |
| cara muat turun transkrip youtube | 0–10 | ✅ đã search |
| muat turun transkrip video youtube | 0–10 | ✅ đã search |
| muat turun transkrip youtube txt | 0–10 | ✅ đã search |
| muat turun transkrip youtube percuma | 0–10 | ✅ đã search |
| simpan transkrip youtube | 0–10 | ✅ đã search |
| ambil transkrip video youtube | 0–10 | ✅ đã search |

### Nhóm Teks (thuần Mã Lai)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| muat turun teks video youtube | 0–10 | ✅ đã search |

### Nhóm Sarikata — nhường trang khác

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download sarikata youtube dalam teks | 0–10 | ⚠️ **thuộc `/ms/youtube-subtitle-downloader`** — đúng 1 lần ở S6 đoạn 2, trong câu trỏ đi |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| muat turun transkrip youtube ke peranti | — | 🔄 dịch bổ sung (save to device) |
| eksport transkrip youtube ke PDF | — | 🔄 dịch bổ sung (export PDF) |
| muat turun transkrip youtube DOCX | — | 🔄 dịch bổ sung (DOCX) |
| simpan transkrip youtube untuk luar talian | — | 🔄 dịch bổ sung (offline) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ Volume trang này thấp — 9/10 cụm ở mức 0–10. Không nhồi mật độ. Chiến lược là **phủ đều 9 cụm**, mỗi cụm một vị trí neo duy nhất.

---

## Search Intent

Người dùng Malaysia **đã biết mình muốn transkrip** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Tampal pautan là tải được ngay, không đăng nhập, không cài extension.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **luar talian** (offline).
- `Percuma`, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Mã Lai, kể cả video trộn Mã Lai – Anh.

### Khác biệt so với bản tiếng Anh

1. **Phải chủ động nhường cụm `sarikata` cho trang khác.** Bản EN không gặp vấn đề này vì "transcript" và "subtitle" là hai từ tách bạch, còn tiếng Mã Lai thì `sarikata` bị dân dụng dùng lẫn cho cả hai loại kết quả. Đây là ràng buộc riêng của bản ms — xem khối cảnh báo đầu file.
2. **Phải song hành hai lớp từ `download` ↔ `muat turun`.** Bản EN chỉ có một động từ "download". Tiếng Mã Lai có từ mượn (volume cao, dân dụng) và từ chuẩn (volume thấp, chuẩn chính tả). Bản ms phải neo cả hai — `download` ở title/h1, `muat turun` ở H2 và body — mà không đọc thành lặp từ.
3. **Phải chống trùng với bản id ở lớp từ vựng.** Bản EN không có trang anh em cùng ngữ hệ. Tiếng Mã Lai và tiếng Indonesia gần như đọc hiểu chéo được, nên nếu không cưỡng chế bảng từ vựng ở trên thì hai bản sẽ giống nhau tới mức Google gộp — xem bảng chống trùng.
4. **`transkrip` giữ dạng bản địa hóa, không giữ nguyên `transcript` tiếng Anh.** Khác bản vi (nơi 7/9 keyword giữ nguyên từ mượn `transcript`), toàn bộ 9 cụm ms đều viết `transkrip`. Không được để chuỗi `transcript` trần trong body.
5. **Nhấn DOCX và PDF mạnh hơn bản EN.** Sinh viên và nhân viên văn phòng Malaysia thường cần bản Word để nộp hoặc bản PDF để lưu hồ sơ.

---

## Đối tượng người dùng

- Pelajar và mahasiswa (lưu transkrip bài giảng, phỏng vấn vào thư mục đề tài)
- Pensyarah / giáo viên (soạn tài liệu từ video bài giảng)
- Wartawan / nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX làm biên bản, tài liệu nội bộ)
- Người học ngoại ngữ (tải TXT đọc luar talian)
- Người cần đưa transkrip vào công cụ khác yêu cầu upload file
- Người làm nghiên cứu cần kho tư liệu tìm kiếm được

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ms.json` phải dịch đúng **7 section**, cùng số đoạn: S1 `content` 3 · S2 `intro` 1 + `items` 4 · S3 `steps` 4 · S4 `intro` 1 + `items` 5 · S5 `content` 2 · S6 `content` 2 · S7 `items` **8 FAQ** · `conclusion` `content` 2. **3 internal link.** **Trang này KHÔNG có `specs`.**

| # | H2 (ms) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Download Transkrip YouTube | download transkrip youtube *(KW chính)* |
| — | **quickAnswer** | cara muat turun transkrip youtube |
| 1 | Apa Yang Anda Dapat Apabila Muat Turun Transkrip | download transkrip youtube, muat turun teks video youtube |
| 2 | Format Mana Yang Patut Anda Muat Turun? | muat turun transkrip youtube txt *(mục TXT)*, `fail sarikata bertimecode` *(mục SRT — neo)* |
| 3 | Cara Muat Turun Transkrip YouTube | cara muat turun transkrip youtube, muat turun transkrip video youtube |
| 4 | Bila Anda Perlukan Failnya, Bukan Sekadar Teks | simpan transkrip youtube, ambil transkrip video youtube |
| 5 | Muat Turun Transkrip Dalam Lebih 100 Bahasa | muat turun transkrip youtube percuma *(+ nhấn bahasa Melayu)* |
| 6 | Bila Alat Lain Lebih Sesuai | ⚠️ **download sarikata youtube dalam teks — đúng 1 lần, trong câu trỏ sang `/ms/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | Soalan Lazim | muat turun transkrip youtube percuma, muat turun transkrip youtube txt + long-tail |
| — | **conclusion** | download transkrip youtube, percuma |

### Ghi chú riêng cho bản ms (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp. Đây cũng là chỗ **duy nhất** cụm `download sarikata youtube dalam teks` được xuất hiện.
- **Nỗi lo nhận dạng tiếng Mã Lai xử lý trong section 5** — thay ví dụ ngôn ngữ của bản EN bằng ví dụ có `bahasa Melayu`, **không thêm câu**.
- **`download` và `muat turun` chia vai rõ:** `download` neo ở `title` / `ogTitle` / `h1` / `conclusion.h2` (bám KW chính 100–1K); `muat turun` phủ H2 của S1/S2/S3/S5 và toàn bộ body. Không trộn hai từ trong cùng một câu.
- **`muat turun` / `download` chỉ đi với `transkrip` / `teks` / `fail`.** TUYỆT ĐỐI không bao giờ đi với `video` — sẽ nhiễm intent tải file MP4.
- `sarikata` xuất hiện **đúng 2 lần** trong cả file: S2 mục SRT và S6 đoạn 2, cả hai đều neo `fail sarikata bertimecode`.

---

## Không nên tối ưu cho các keyword

- **`download sarikata youtube` / `muat turun sarikata youtube` / `download sarikata youtube srt` / `extract sarikata youtube` / `download fail sarikata youtube`** → **/ms/youtube-subtitle-downloader** (file phụ đề khớp giờ cho editor). Xem quy tắc 1 lần ở trên.
- `transkrip youtube` / `lihat transkrip youtube` / `dapatkan transkrip youtube` → **/ms/youtube-transcript** (đọc trên màn hình, không tải file).
- `ringkasan video youtube` / `rumusan video youtube` → **/ms/youtube-video-summarizer**.
- **Nhóm tải VIDEO — nhiễm intent nặng nhất:** `download video youtube`, `muat turun video youtube`, `youtube downloader`, `download mp4 youtube`, `download video youtube bersarikata`. SERP toàn downloader video. Trang này tải **chữ**. Quy tắc cưỡng chế: mọi chỗ `muat turun`/`download` phải có tân ngữ `transkrip` / `teks` / `fail`.
- `tukar video kepada teks` (không có chữ youtube) → **/ms/video-to-text** (muat naik file từ máy, không tampal pautan).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**, đúng thứ tự bản EN:

- → `/ms/youtube-transcript` — chỉ muốn đọc / salin trên màn hình, không cần file
- → `/ms/youtube-subtitle-downloader` — cần `fail sarikata bertimecode` cho phần mềm dựng phim — **link quan trọng nhất, cũng là chỗ neo cụm đẩy đi `download sarikata youtube dalam teks`**
- → `/ms/youtube-video-summarizer` — chỉ cần ý chính, không cần toàn văn

Giữ nguyên cú pháp markdown `[Tên](/ms/path)` như bản EN, chỉ đổi path sang `/ms/...`.

---

## Ghi chú kỹ thuật cho ms.json

- Xưng hô **`anda`** (thường, không viết hoa giữa câu), nhất quán với `/ms/video-to-text`.
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- Cấu trúc **1:1 với `en.json`** — không thêm/bớt section, câu hay FAQ. **KHÔNG có `specs`.**
- Bảng từ cấm (dạng Indonesia) phải grep sạch: `unduh`, `berkas`, `gratis`, `bisa`, `\bsaja\b`, `subtitle`, `tempel`, `tautan`.
- Chuỗi `transcript` (dạng Anh) không được xuất hiện trong body — chỉ tồn tại bên trong tên riêng **TranscriptX** và tên công cụ `[YouTube Transcript]`.
- Chuỗi `muat turun video` / `download video` **tuyệt đối không được xuất hiện**.
