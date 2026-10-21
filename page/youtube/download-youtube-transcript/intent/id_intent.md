🔥 TranscriptX – Download YouTube Transcript (Indonesian / id)

URL:
/id/download-youtube-transcript

Intent chính:

Tải transcript video YouTube về thiết bị (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Indonesia muốn **tải bản transcript của video YouTube xuống máy** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcript trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/id/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **Từ mang nghĩa "phụ đề" (`subtitle` / `takarir` — file phụ đề khớp giờ cho editor) → `/id/youtube-subtitle-downloader`**
> **Từ mang nghĩa "bản chép lời" (`transkrip` / `teks` — tài liệu để đọc/lưu/nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 đã tự định nghĩa ranh giới — *"if what you really need is a timed caption file for a video editor rather than a document, the YouTube Subtitle Downloader exports SRT and VTT instead"*. Trang này ra **tài liệu**; trang kia ra **file phụ đề cho phần mềm dựng phim**.

### Kết quả kiểm trùng với `/id/youtube-subtitle-downloader`

Danh sách id của trang kia (6 keyword): `cara download subtitle youtube` (100–1K) · `download subtitle dari youtube` (100–1K) · `cara mengambil subtitle dari youtube` (10–100) · `ekstrak subtitle youtube` (10–100) · `cara download subtitle youtube di hp` (0–10) · `download subtitle youtube gratis` (0–10).

| Cặp keyword | Trạng thái | Xử lý |
| ----------- | ---------- | ----- |
| **Trùng nguyên văn** | **0 cặp** | — không có cụm nào lặp y hệt giữa hai danh sách |
| `download subtitle youtube jadi teks` (trang này) × cụm `subtitle` (trang kia) | ⚠️ **trùng lõi từ `subtitle`** | **Giữ ở trang này** — vế `jadi teks` neo rõ intent muốn văn bản để đọc, không phải file cho editor. Chỉ dùng ở **body S2, mục TXT**, luôn kèm nguyên vế `jadi teks`. |
| `download transkrip youtube gratis` (trang này) × `download subtitle youtube gratis` (trang kia) | ✅ không xung đột | khác head noun (`transkrip` vs `subtitle`) — mỗi trang giữ cụm của mình |
| `ambil transkrip video youtube` (trang này) × `cara mengambil subtitle dari youtube` (trang kia) | ✅ không xung đột | chung động từ `ambil` nhưng khác tân ngữ — tân ngữ mới là thứ phân định |
| `cara download subtitle youtube` (100–1K, **thuộc trang kia**) | ⚠️ **neo đẩy đi** | Dùng **đúng 1 lần**, ở **S6 đoạn 2**, ngay trong câu trỏ sang `/id/youtube-subtitle-downloader`. Bắt tín hiệu keyword nhưng đẩy traffic sai intent về đúng trang thay vì giữ lại rồi bounce. **Tuyệt đối không đặt vào title/H1/H2.** |

**Kết quả trang này luôn gọi là `transkrip` / `teks`.** Mọi chỗ buộc phải nhắc `subtitle` (mục SRT ở S2, và S6) đều neo bằng cụm **`file subtitle bertimecode`** để không cạnh tranh với trang kia.

---

## 🚫 CHỐNG TRÙNG VỚI `/ms/download-youtube-transcript` (làm song song)

Hai bản id và ms dùng chung nhiều gốc từ Mã Lai — nếu không phân biệt sẽ bị coi là duplicate content. Bảng chốt:

| Khái niệm | **id dùng (bắt buộc)** | **CẤM dùng (để dành cho ms)** |
| --------- | ---------------------- | ----------------------------- |
| tải xuống | `download` / `unduh` / `mengunduh` | ❌ `muat turun` |
| file | `file` | ❌ `fail` |
| miễn phí | `gratis` | ❌ `percuma` |
| có thể | `bisa` | ❌ `boleh` |
| chỉ / thôi | `saja` | ❌ `sahaja` |
| phụ đề | `subtitle` | ❌ `sarikata` |

Thêm: bản id chọn **`download`** làm dạng chính ở title/H1 (bám đúng keyword id volume cao nhất `download transkrip youtube`), còn bản ms nên neo `muat turun transkrip youtube` — đây là điểm tách rõ nhất ở vị trí SEO quan trọng nhất.

---

## ⚠️ LƯU Ý NGỮ NGHĨA RIÊNG CỦA TIẾNG INDO

Từ **`transkrip`** trong tiếng Indonesia còn có nghĩa **"bảng điểm học tập"** (transkrip nilai). Quy tắc: **luôn viết kèm `YouTube` hoặc `video`** — `transkrip YouTube`, `transkrip video YouTube`. Không bao giờ để `transkrip` đứng trơ ở title, H1, H2 hay meta description.

## 🚫 DẬP NHIỄM INTENT TẢI VIDEO

Nhóm `download video youtube` có volume **cực lớn** ở Indonesia và SERP toàn video downloader. Quy tắc tuyệt đối: **`download` / `unduh` chỉ được đi với `transkrip` / `teks` / `file`, KHÔNG BAO GIỜ với `video`.** Chuỗi `download video` và `unduh video` không được phép xuất hiện ở bất kỳ đâu trong `id.json`.

### Dòng rác trong file nguồn

Phần `## Indonesian (id)` **không có** dòng nhãn rác (`Keyword ideas` / `Keywords you provided`) như phần vi, và **không có keyword sai intent** nào cần loại.

**Số keyword thực: 10 dòng thô − 0 rác − 0 sai intent = 10 keyword, tất cả đều dùng được.** Trong đó 1 cụm (`download subtitle youtube jadi teks`) chỉ dùng hạn chế ở body.

---

## Từ khóa chính

**download transkrip youtube (100 – 1K)** ✅ *đã search*

Đây là cụm mạnh nhất trong danh sách và cũng là **lõi chung** của 3 cụm đuôi dài khác (`cara ...`, `... gratis`, `... txt`), nên neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm Transkrip (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download transkrip youtube | 100 – 1K | ✅ đã search *(KW chính)* |
| cara download transkrip youtube | 100 – 1K | ✅ đã search |
| download transkrip youtube gratis | 10 – 100 | ✅ đã search |
| unduh transkrip video youtube | 0 – 10 | ✅ đã search |
| cara mengunduh transkrip youtube | 0 – 10 | ✅ đã search |
| simpan transkrip youtube | 0 – 10 | ✅ đã search |
| download transkrip youtube txt | 0 – 10 | ✅ đã search |
| ambil transkrip video youtube | 0 – 10 | ✅ đã search |

### Nhóm Teks (thuần Indo)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download teks video youtube | 10 – 100 | ✅ đã search |

### Nhóm Subtitle — dùng HẠN CHẾ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download subtitle youtube jadi teks | 0 – 10 | ✅ đã search — chỉ ở body S2 (mục TXT), luôn kèm vế `jadi teks` |
| cara download subtitle youtube | 100 – 1K | ⚠️ **thuộc `/id/youtube-subtitle-downloader`** — đúng 1 lần ở S6 đoạn 2, trong câu trỏ đi |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| simpan transkrip youtube ke perangkat | — | 🔄 dịch bổ sung (save to device) |
| ekspor transkrip youtube ke PDF | — | 🔄 dịch bổ sung (export PDF) |
| download transkrip youtube docx | — | 🔄 dịch bổ sung (DOCX) |
| baca transkrip youtube offline | — | 🔄 dịch bổ sung (offline) |
| transkrip youtube dengan timestamp | — | 🔄 dịch bổ sung (timestamps) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ **Volume trang này thấp hơn hẳn `/id/video-to-text`.** Lý do: "download transkrip" là nhu cầu hẹp hơn "ubah video jadi teks". Không cố nhồi mật độ — chiến lược là **phủ đều 10 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Indonesia **đã biết mình muốn transcript** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài extension.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline** (băng thông ở nhiều vùng Indonesia còn hạn chế → offline là điểm bán mạnh).
- Miễn phí, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Indonesia.
- Làm được **trên điện thoại** — phần lớn người dùng Indonesia vào bằng mobile.

### Khác biệt so với bản tiếng Anh

1. **Phải chủ động nhường cụm `subtitle` cho trang khác.** Bản EN không có vấn đề này vì "transcript" và "subtitle" là hai từ tách bạch. Trong tiếng Indo, `subtitle` bị người dùng dùng lẫn cho cả file phụ đề lẫn văn bản để đọc — xem khối cảnh báo đầu file.
2. **Phải dập nhiễm intent tải VIDEO.** Nhóm `download video youtube` có volume khổng lồ ở Indonesia và SERP toàn downloader. Bản EN không gặp vấn đề này. Quy tắc: mọi chỗ `download`/`unduh` phải có tân ngữ `transkrip`/`teks`/`file`.
3. **Phải xử lý nghĩa kép của `transkrip` (= bảng điểm).** Bản EN không có. Luôn viết `transkrip YouTube` / `transkrip video YouTube`.
4. **Phải tách khỏi bản `ms` đang làm song song.** Bản EN không có ràng buộc này — xem bảng chống trùng id/ms ở trên.
5. **`download` giữ nguyên tiếng Anh làm dạng chính.** 5/10 keyword id dùng thẳng `download` chứ không phải `unduh` — đây là cách người Indonesia thực sự gõ. `unduh`/`mengunduh` dùng xen kẽ trong body cho tự nhiên và để phủ 2 keyword có dạng này.
6. **Nhấn offline + mobile mạnh hơn bản EN**, phù hợp thực tế kết nối và thiết bị ở Indonesia.

---

## Đối tượng người dùng

- Sinh viên, học sinh (lưu transkrip bài giảng, seminar vào thư mục môn học)
- Nghiên cứu sinh (lưu transkrip phỏng vấn, tọa đàm làm tư liệu trích dẫn)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX để làm biên bản, tài liệu nội bộ)
- Người học ngoại ngữ (tải TXT đọc offline)
- Content creator cần bản nháp có timecode (SRT)
- Người cần đưa transkrip vào công cụ khác yêu cầu upload file

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `id.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps` ở S3, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (id) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Download Transkrip YouTube | download transkrip youtube *(KW chính)* |
| — | **quickAnswer** | cara download transkrip youtube |
| 1 | Apa Gunanya Download Transkrip YouTube ke Perangkat Anda | download transkrip youtube, download teks video youtube |
| 2 | Format Mana yang Sebaiknya Anda Download? | download transkrip youtube txt, download subtitle youtube **jadi teks** *(mục TXT)*, `file subtitle bertimecode` *(mục SRT)* |
| 3 | Cara Download Transkrip YouTube | cara download transkrip youtube, cara mengunduh transkrip youtube, unduh transkrip video youtube |
| 4 | Ketika Anda Butuh Filenya, Bukan Sekadar Teks di Layar | simpan transkrip youtube, ambil transkrip video youtube |
| 5 | Download Transkrip YouTube dalam Lebih dari 100 Bahasa | download transkrip youtube gratis *(+ nhấn tiếng Indonesia)* |
| 6 | Kapan Alat Lain Lebih Cocok | ⚠️ **cara download subtitle youtube — đúng 1 lần, trong câu trỏ sang `/id/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | Pertanyaan yang Sering Diajukan | download transkrip youtube gratis, download transkrip youtube txt + long-tail |
| — | **conclusion** | download transkrip youtube, gratis |

### Ghi chú riêng cho bản id (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp. Đây cũng là chỗ **duy nhất** cụm `cara download subtitle youtube` được xuất hiện.
- Nỗi lo nhận dạng tiếng Indonesia xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Indonesia — **không thêm câu**.
- Chi tiết "mở được trên điện thoại" đã có sẵn trong step 4 và FAQ 5 của bản EN — chỉ cần dịch sát, **không thêm câu mới** để nhấn mobile.
- `unduh` / `mengunduh` rải ở S3, S4, S7 để phủ 2 keyword dạng này; `download` giữ ở title/H1/H2/S1/S2/S5/conclusion.

---

## Không nên tối ưu cho các keyword

- **`cara download subtitle youtube` / `download subtitle dari youtube` / `ekstrak subtitle youtube` / `cara mengambil subtitle dari youtube`** → **/id/youtube-subtitle-downloader** (file phụ đề khớp giờ cho editor). Xem quy tắc 1 lần ở trên.
- `transkrip youtube` / `lihat transkrip youtube` / `cara melihat transkrip youtube` → **/id/youtube-transcript** (đọc trên màn hình, không tải file).
- `ringkas video youtube` / `rangkuman video youtube` → **/id/youtube-video-summarizer**.
- **`download video youtube` / `download video youtube gratis` / `youtube downloader` / `download mp4 youtube` / `download video youtube di hp`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **chữ**. Quy tắc: `download`/`unduh` luôn phải có tân ngữ `transkrip`/`teks`/`file`.
- `transkrip nilai` / `cetak transkrip` → **nghĩa "bảng điểm"**, hoàn toàn khác intent.
- `ubah video jadi teks` (không có chữ youtube) → **/id/video-to-text** (upload file từ máy, không dán link).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/id/youtube-transcript` (chỉ muốn đọc/copy trên màn hình, không cần file)
- → `/id/youtube-subtitle-downloader` (cần file phụ đề khớp giờ cho phần mềm dựng phim) — **đây là link quan trọng nhất, cũng là chỗ neo cụm `cara download subtitle youtube`**
- → `/id/youtube-video-summarizer` (chỉ cần ý chính, không cần toàn văn)

---

## Ghi chú kỹ thuật cho id.json

- Xưng hô **"Anda"**, nhất quán với `/id/video-to-text` và các trang id khác trong repo.
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**. Từ **`download`** cũng giữ nguyên (bám keyword).
- Cấu trúc: **7 section**, **8 FAQ**, S1 = `content` 3 đoạn, S2 = `intro` 1 + `items` 4, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5 = `content` 2, S6 = `content` 2, S7 = `items` 8, `conclusion` = `content` 2. **Trang này KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/id/...`.
- **Tuyệt đối không để chuỗi `download video` hoặc `unduh video` xuất hiện.**
- **Tuyệt đối không để từ Mã Lai bị cấm xuất hiện:** `muat turun`, `fail`, `percuma`, `boleh`, `sahaja`, `sarikata`.
- `transkrip` không bao giờ đứng trơ ở vị trí SEO — luôn kèm `YouTube` / `video`.
