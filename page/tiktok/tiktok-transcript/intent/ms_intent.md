🔥 TranscriptX – TikTok Transcript (Malay / ms)

URL:
/ms/tiktok-transcript

Intent chính:

Lấy lời nói trong video TikTok thành văn bản (transkrip) — miễn phí, dán link là xong

Trang này là **trang trụ (hub)** cụm TikTok Transcript bản tiếng Mã Lai. Nhắm đến người dùng Malaysia muốn lấy **lời nói** trong video TikTok thành **teks biasa để đọc / sao chép / nghiên cứu** — **không kèm mốc thời gian**.

Gộp toàn bộ intent đồng nghĩa **transkrip / tukar kepada teks / penjana transkrip** vì tất cả cho ra **cùng một kết quả**: video TikTok → teks.

> ⚠️ **Phân định với `/ms/tiktok-caption-downloader`: TIMING.** Cả hai trang đều lấy lời NÓI từ audio. Trang này ra **teks biasa để đọc**; trang kia ra **fail sarikata bertimecode** để lắp đè lên video khi repost. Bản EN cài sẵn 2 chốt chặn: **section 7 đoạn 2** (câu trỏ sang trang caption) và **FAQ 8** ("Can I download the TikTok transcript?" → được, nhưng nếu cần fail sarikata khớp giờ thì dùng công cụ kia). **Giữ nguyên cả hai, dịch sát, không rút gọn, không gộp.**

---

## 🚨 Quy tắc dùng `sarikata` — khác trang caption ra sao

`/ms/tiktok-caption-downloader` lấy **`sarikata` làm trục chính**: H1 là `Download Sarikata TikTok`, và từ này rải khắp title / H2 / FAQ. Nếu trang này cũng dùng `sarikata` thoải mái thì hai trang sẽ cannibalize nhau ngay ở SERP `sarikata tiktok`.

**Quy tắc chốt cho `ms.json` của trang này:**

| Tình huống | Được dùng `sarikata`? | Bắt buộc neo nghĩa |
| --- | --- | --- |
| Gọi **kết quả** của trang này | ❌ **KHÔNG** | Luôn gọi là `transkrip` hoặc `teks` |
| Nói về **caption tự động chạy trên màn hình TikTok** (ngữ cảnh phủ định: "video không có sẵn cũng chạy được") | ✅ có | `sarikata automatik pada skrin` / `sarikata pada skrin` |
| **Trỏ sang** `/ms/tiktok-caption-downloader` | ✅ có | `fail sarikata bertimecode` |
| Trong `title` / `h1` / `h2` / `seo.description` | ❌ **TUYỆT ĐỐI KHÔNG** | — |

Nói gọn: ở trang này `sarikata` **luôn là thứ của người khác** (của TikTok tự sinh, hoặc của trang caption), **không bao giờ là sản phẩm của TranscriptX trên trang này**. Sản phẩm ở đây tên là **`transkrip`**.

Vị trí `sarikata` được xuất hiện trong `ms.json` (đếm được, không phát sinh thêm):
- S2 spec "Berfungsi tanpa sarikata pada skrin"
- S4 đoạn 1 (`sarikata automatik pada skrin` — ngữ cảnh phủ định, đúng chỗ bản EN nói text dựng từ audio)
- S7 đoạn 2 (`fail sarikata bertimecode` + link sang trang caption)
- FAQ 4 (video không có sarikata trên màn hình vẫn chạy)
- FAQ 8 (chốt phân định, trỏ sang TikTok Caption Downloader)

---

## ⚠️ Lưu ý riêng bản ms

**1. Chỉ có 4 keyword đã search.** Ít hơn hẳn ko (13 KW) và ja (10 KW). Hệ quả:

- 4 KW đã search phải chiếm trọn các vị trí mạnh: `title`, `h1`, `h2` của S1/S2/S3/S4/S5, `conclusion`.
- Phần còn lại của body (~60%) là **dịch bổ sung** từ bản EN — bám sát ý bản EN, không bịa keyword không có volume.
- **Tỉ lệ ước tính: ~40% bề mặt trang neo vào 4 KW đã search, ~60% là dịch bổ sung rải body.**
- Vì `transkrip tiktok` và `transkrip video tiktok` **cùng 100–1K**, hai KW này gần như đồng nghĩa → dùng xen kẽ tự nhiên, không nhồi.

**2. Bảng chống trùng ms / id** (`/id/tiktok-transcript` làm song song, hai bản rất dễ trùng chữ):

| Ý | ✅ ms dùng | ❌ CẤM (dạng Indo) |
| --- | --- | --- |
| chuyển đổi | `tukar` | `mengubah` |
| trở thành | `kepada` / `bertukar kepada` | `menjadi` |
| miễn phí | `percuma` | `gratis` |
| có thể | `boleh` | `bisa` |
| chỉ | `sahaja` | `saja` |
| tải xuống | `muat turun` | `unduh` |
| tệp | `fail` | `berkas` |
| phụ đề | `sarikata` (đúng quy tắc trên) | `subtitle` |

**3. `download` / `muat turun` chỉ đi với `transkrip` / `teks` / `fail` — KHÔNG BAO GIỜ với `video`.** SERP của `download video tiktok` toàn downloader video, sai intent hoàn toàn.

**4. Xưng hô: `anda`.** Nhất quán với `/ms/instagram-transcript` và `/ms/tiktok-caption-downloader`.

---

## Từ khóa chính

`transkrip tiktok` (100–1K) ✅ *đã search* — **mạnh nhất, đưa lên H1 + title**

---

## Từ khóa phụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transkrip tiktok | 100–1K | ✅ đã search *(KW chính)* |
| transkrip video tiktok | 100–1K | ✅ đã search |
| tukar suara tiktok kepada teks | 0–10 | ✅ đã search |
| penjana transkrip tiktok | 0–10 | ✅ đã search |
| video tiktok kepada teks | — | 🔄 dịch bổ sung (video to text) |
| tukar tiktok kepada teks percuma | — | 🔄 dịch bổ sung (free) |
| transkripsi video tiktok | — | 🔄 dịch bổ sung (transcription) |
| mentranskrip video tiktok | — | 🔄 dịch bổ sung (transcribe) |
| muat turun transkrip tiktok | — | 🔄 dịch bổ sung (download transcript) |
| salin teks video tiktok | — | 🔄 dịch bổ sung (copy text) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, không đưa vào H1/title.

---

## Search Intent

Người dùng Malaysia xem một video TikTok ngắn và muốn **giữ lại lời nói** trong đó thành chữ — vì phần giá trị thường chỉ nằm ở một câu, và clip trôi rất nhanh khỏi trang For You.

Họ kỳ vọng:

- Dán link là ra chữ trong vài giây, không cần đăng nhập TikTok.
- Chạy được cả khi video **không có sarikata trên màn hình**.
- Nhận dạng tốt **tiếng Melayu**, kể cả câu **rojak** (Melayu trộn English) — rất phổ biến trên TikTok Malaysia.
- Sao chép được ngay phần hook để nghiên cứu hoặc viết lại.
- Miễn phí (`percuma`), không cài app.

### Khác biệt so với bản tiếng Anh

1. **Bản EN có 7 keyword phủ 3 nhóm intent (transcript / generator / video-to-text); bản ms chỉ có 4 KW và 2 KW mạnh nhất lại gần như đồng nghĩa.** Vì vậy H2 của S1/S2/S3 phải xoay quanh cùng một cụm `transkrip tiktok` mà không lặp máy móc — biến thể qua `transkrip video tiktok` và cách đặt câu, chứ không tách thành 3 nhóm intent riêng như EN.
2. **`sarikata` là ràng buộc riêng của bản ms.** Bản EN dùng "captions" thoải mái vì trang caption bản EN không cạnh tranh mạnh ở từ đó. Tiếng Mã Lai thì `sarikata` là trục chính của `/ms/tiktok-caption-downloader` → phải neo nghĩa mọi lần dùng (xem mục quy tắc ở trên).
3. **Phải chủ động chống trùng chữ với `/id/tiktok-transcript`.** Bản EN không có vấn đề này. Đây là ràng buộc riêng của cặp ms/id vì hai ngôn ngữ gần nhau đến mức Google dễ coi hai trang là bản sao — xem bảng ở trên.
4. **Ví dụ ngôn ngữ ở S4 đoạn 3 đổi.** Bản EN nêu Spanish / Indonesian. Bản ms nêu **Melayu** trước tiên (và giữ một ví dụ ngoại ngữ) để trả lời đúng nỗi lo "alat ni faham Melayu tak?".
5. **`percuma` phải hiện sớm.** Người tìm kiếm Malaysia lọc theo "percuma / tanpa daftar" ngay từ SERP; bản EN rải "free" đều hơn, bản ms đẩy lên `title` + `subtitle` + `conclusion`.

---

## Đối tượng người dùng

- Người xem TikTok muốn lưu tip / resepi trước khi clip trôi
- Content creator Malaysia nghiên cứu hook của video viral
- Marketer / social media phân tích clip đối thủ
- Học sinh, sinh viên
- Người học ngoại ngữ (đọc chậm lời nói nhanh của người bản xứ)
- Nhà báo / người viết cần trích dẫn chính xác lời creator
- Người tái sử dụng nội dung sang Reels / Shorts / blog

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ms.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng **8 `specs`** (khác trang Facebook/Instagram vốn có 10), đúng 4 `steps`, đúng **6 `items`** ở section 6, đúng **8 FAQ**.

| # | H2 (ms) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Transkrip TikTok | `transkrip tiktok` *(KW chính)* |
| — | **quickAnswer** | `transkrip video tiktok` |
| 1 | Apakah Itu Transkrip TikTok? | `transkrip tiktok`, `transkrip video tiktok` |
| 2 | Transkrip TikTok Sepintas Lalu | *(bảng 8 thông số)* |
| 3 | Cara Dapatkan Transkrip TikTok | `transkrip tiktok`, `transkrip video tiktok` |
| 4 | Penjana Transkrip TikTok | `penjana transkrip tiktok` + `sarikata automatik pada skrin` (neo nghĩa) |
| 5 | Tukar Video TikTok kepada Teks | `tukar suara tiktok kepada teks` |
| 6 | Kenapa Tukar TikTok Pendek kepada Teks? | *(intro + 6 items)* |
| 7 | Salin, Sunting, Terjemah atau Muat Turun | ⚠️ **chốt phân định 1** — `fail sarikata bertimecode` + link `/ms/tiktok-caption-downloader` + link `/ms/youtube-transcript` |
| 8 | Soalan Lazim | `transkrip tiktok percuma`, `penjana transkrip tiktok` + long-tail; ⚠️ **chốt phân định 2 ở FAQ 8** |
| — | **conclusion** | `transkrip tiktok`, `percuma` |

### Ghi chú riêng cho bản ms (KHÔNG tạo section mới)

- Sắc thái "alat ni faham Melayu tak?" xử lý **trong section 4 đoạn 3**, thay ví dụ ngôn ngữ của bản EN (Spanish / Indonesian) bằng ví dụ có **Melayu**. Không thêm câu.
- Sắc thái **rojak** (Melayu campur English) chỉ nhắc **một lần**, gọn, trong section 4 đoạn 3 — không mở thành ý mới, không thêm spec.
- Nỗi lo `sarikata` (người dùng tưởng công cụ chỉ lấy sarikata có sẵn) xử lý **trong section 4 đoạn 1** — bản EN vốn nói text dựng từ audio chứ không phụ thuộc caption. Đúng chỗ, không thêm câu.
- **Section 7 đoạn 2 và FAQ 8 là hai chốt phân định với trang caption** — dịch sát, không rút gọn, không gộp.
- S2 spec 6 dịch `Works without on-screen captions` → `Berfungsi tanpa sarikata pada skrin` (neo nghĩa "trên màn hình", không để trống nghĩa).

---

## Không nên tối ưu cho các keyword

Các keyword dưới đây thuộc landing page khác — KHÔNG dùng ở trang này để tránh cannibalization:

- **`download sarikata tiktok` / `sarikata tiktok` / `simpan sarikata tiktok` / `fail sarikata tiktok`** → **/ms/tiktok-caption-downloader** (fail bertimecode). Xem quy tắc neo nghĩa `sarikata` ở trên — trang này chỉ được nhắc khi trỏ đi.
- `transkrip youtube` / `sarikata youtube` → **/ms/youtube-transcript**
- `transkrip video instagram` / `transkrip reel instagram` → **/ms/instagram-transcript**
- **`download video tiktok` / `muat turun video tiktok` / `tiktok tanpa watermark` / `simpan video tiktok`** → **intent tải VIDEO**, SERP toàn downloader video. Trang này lấy **chữ**, không lấy file video. Quy tắc: `download` / `muat turun` chỉ được đi với `transkrip` / `teks` / `fail`, **không bao giờ** với `video`.

---

## Internal linking

- ↔ /ms/tiktok-caption-downloader (khi user cần `fail sarikata bertimecode` thay vì teks biasa) — **section 7 đoạn 2**, nhắc lại ở **FAQ 8**
- → /ms/youtube-transcript (cross-cluster, video dài) — cùng section 7 đoạn 2

Tổng: **đúng 2 internal link** trong `ms.json`, cả hai nằm ở section 7 đoạn 2.

---

## Ghi chú kỹ thuật cho ms.json

- Xưng hô **`anda`**, giọng văn nhất quán với `/ms/instagram-transcript` và `/ms/tiktok-caption-downloader`.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts**.
- Internal link section 7 giữ cú pháp markdown: `[TikTok Caption Downloader](/ms/tiktok-caption-downloader)`, `[YouTube Transcript](/ms/youtube-transcript)`.
- Cấu trúc: **8 section**, **8 `specs`**, 4 `steps`, **6 `items`** ở section 6, **8 FAQ**, section 7 = `content` 2 đoạn, `conclusion` = `content` 2 đoạn.
- Đếm đoạn: S1 `content` 3 | S2 `specs` 8 | S3 `steps` 4 | S4 `content` 3 | S5 `content` 2 | S6 `intro` 1 + `items` 6 | S7 `content` 2 | S8 `items` 8 | `conclusion` `content` 2.
- Kiểm tra trước khi giao: `python3 shape_check.py en.json ms.json` phải in `ms.json -> True`; grep xác nhận không có `mengubah` / `menjadi` / `gratis` / `bisa` / `saja` / `unduh` / `berkas` / `subtitle`.
