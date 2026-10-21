🔥 TranscriptX – Download YouTube Transcript (Turkish / tr)

URL:
/tr/download-youtube-transcript

Intent chính:

Tải transcript video YouTube về máy (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Thổ Nhĩ Kỳ muốn **tải bản transcript của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcript trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/tr/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **`altyazı` (file phụ đề khớp giờ cho editor) → `/tr/youtube-subtitle-downloader`**
> **`transkript` / `metin` (tài liệu để đọc/lưu/nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 đã tự định nghĩa ranh giới — trang này ra **tài liệu để đọc/lưu/nộp**; trang kia ra **file phụ đề cho phần mềm dựng phim**.

### Kết quả kiểm trùng thực tế (tr × tr)

Đã đối chiếu `## Turkish (tr)` của trang này (12 keyword) với `../youtube-subtitle-downloader/2_loc_kw.md` (9 keyword).

| Danh sách | Cụm |
| --------- | --- |
| `/tr/youtube-subtitle-downloader` | youtube altyazı indirme (100–1K) · youtube video altyazı indirme (100–1K) · youtube altyazı dosyası indirme · youtube altyazı indirme sitesi · youtube altyazı çıkarma · youtube altyazı indirici · youtube srt altyazı indirme · youtube altyazı nasıl indirilir · youtube altyazı indirme ücretsiz |
| Trang này | 11 cụm `transkript`/`metin`/`transcript` + **1 cụm chứa `altyazı`** |

**Số keyword trùng chuỗi chính xác: 0.** ✅ Bản tr may mắn hơn bản vi — tiếng Thổ tách bạch `altyazı` (phụ đề) và `transkript`/`metin` (bản chép lời), nên hai danh sách gần như không giao nhau.

**Trùng CỤM NGỮ NGHĨA: 1 cụm.**

| Keyword | Volume | Xử lý |
| ------- | ------ | ----- |
| `youtube altyazı metin olarak indir` | 0–10 | ✅ **GIỮ LẠI** — có vế **`metin olarak`** neo rõ là muốn văn bản để đọc, không phải file phụ đề cho editor. Y hệt ngoại lệ `tải phụ đề youtube dạng text` của bản vi. Dùng ở body **S2 (mục TXT)**, luôn kèm nguyên vế `metin olarak`. |

### Neo đẩy đi

Cụm mạnh nhất của trang kia — `youtube altyazı indirme` (**100–1K**) — không nằm trong danh sách trang này nhưng vẫn là tín hiệu lớn. Dùng kỹ thuật **neo đẩy đi**: xuất hiện **đúng 1 lần**, ở **S6 đoạn 2**, ngay trong câu trỏ sang `/tr/youtube-subtitle-downloader`. **Tuyệt đối không đặt vào title/H1/H2.**

**Quy tắc neo `altyazı`:** mọi chỗ buộc phải nhắc `altyazı` (mục SRT ở S2, và S6) đều phải viết đủ **`zaman kodlu altyazı dosyası`** — không để `altyazı` đứng trần, tránh trang bị Google đọc nhầm thành trang phụ đề.

---

## ⚠️ RỦI RO RIÊNG CỦA BẢN TR: `indirme` ĐỨNG TRẦN = TẢI VIDEO

Đây là **rủi ro lớn nhất** của bản Thổ, vì trang này vốn nói về "download".

Trong tiếng Thổ, `indirme` / `indir` đứng trần trong ngữ cảnh YouTube **mặc định được hiểu là TẢI VIDEO** (`youtube video indirme`, `youtube mp4 indir` — volume khổng lồ, SERP toàn downloader video). Nếu bản tr để lọt một cụm `video indirme` / `videoyu indir`, trang sẽ bắt sai intent và bounce sạch.

**Quy tắc cứng — không có ngoại lệ:**

> `indir` / `indirme` / `indirin` / `iner` **chỉ được đi kèm tân ngữ** `transkript` / `metin` / `dosya` / `TXT` / `DOCX` / `PDF` / `SRT`.
> **KHÔNG BAO GIỜ** đi kèm `video` / `videoyu` / `videoyu indir`.

Cụm hợp lệ: `youtube video transkript indir` — tân ngữ là **`transkript`**, chữ `video` chỉ bổ nghĩa cho `transkript`. Hợp lệ.

**Bẫy từ vựng cần tránh:**

- ❌ `indirger` / `indirgemek` (rút gọn, giản lược) — chứa chuỗi con `indir`, làm nhiễu grep kiểm tra và đọc nhập nhằng. Ở **S6 câu về Summarizer** phải dùng **`özetler`**, không dùng `indirger`.
- ❌ `videoyu indirin`, `video indirme sitesi`, `video indirici`.
- ✅ Câu chốt an toàn ở S1 đoạn 3: *"Videonun kendisi YouTube'da kalır; cihazınıza inen şey yalnızca metindir."* — nói thẳng thứ tải về là **chữ**, không phải video.

---

## Lỗi dữ liệu trong file nguồn + số keyword thực

- Danh sách `## Turkish (tr)` **không có dòng rác** (`Keyword ideas` / `Keywords you provided` chỉ xuất hiện ở phần vi/ko).
- **Chính tả dấu Thổ trong file nguồn: ĐÚNG 100%.** Đã kiểm từng dòng: `nasıl indirilir` (ı), `deşifre` (ş), `altyazı` (ı), `ücretsiz` (ü), `yazıya dökülmüş` (ı/ö/ü/ş). Không phải sửa dòng nào.
- **Số keyword thực: 12 dòng thô − 0 rác − 0 sai intent = 12 keyword.** Trong đó 1 cụm (`youtube altyazı metin olarak indir`) dùng hạn chế ở body → **12 cụm dùng được, 11 cụm làm trục chính.**

⚠️ Lưu ý phân biệt `ı` (không chấm) và `i` (có chấm) — viết sai một chữ là sai từ. `nasıl` KHÔNG phải `nasil`; `altyazı` KHÔNG phải `altyazi`; `yazıya` KHÔNG phải `yaziya`.

---

## Từ khóa chính

**youtube transkript indirme** (100–1K) ✅ *đã search*

Cụm mạnh nhất tuyệt đối trong danh sách tr, và cũng là **lõi chung** của 6 cụm đuôi dài khác (`... nasıl indirilir`, `... txt indir`, `... ücretsiz indir`, `youtube video transkript indir`, `youtube transkript kaydet`, `youtube transcript indir`). Neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm Transkript (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript indirme | 100–1K | ✅ đã search *(KW chính)* |
| youtube transcript indir | 10–100 | ✅ đã search *(dạng Latin, người Thổ hay gõ)* |
| youtube transkript nasıl indirilir | 10–100 | ✅ đã search |
| youtube video transkript indir | 0–10 | ✅ đã search |
| youtube transkript txt indir | 0–10 | ✅ đã search |
| youtube transkript kaydet | 0–10 | ✅ đã search |
| youtube transkript ücretsiz indir | 0–10 | ✅ đã search |
| download youtube transcript türkçe | 0–10 | ✅ đã search *(mixed query)* |

### Nhóm Metin / Deşifre (thuần Thổ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video metni indir | 0–10 | ✅ đã search |
| youtube deşifre metni indir | 0–10 | ✅ đã search |
| youtube video yazıya dökülmüş metni indir | 0–10 | ✅ đã search |

### Nhóm Altyazı — dùng HẠN CHẾ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube altyazı metin olarak indir | 0–10 | ✅ đã search — chỉ ở body S2 (mục TXT), luôn kèm nguyên vế `metin olarak` |
| youtube altyazı indirme | 100–1K | ⚠️ **thuộc `/tr/youtube-subtitle-downloader`** — đúng 1 lần ở S6 đoạn 2, trong câu trỏ đi, kèm neo `zaman kodlu altyazı dosyası` |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transkripti cihaza kaydetmek | — | 🔄 dịch bổ sung (save to device) |
| youtube transkript pdf indir | — | 🔄 dịch bổ sung (PDF) |
| youtube transkript docx indir | — | 🔄 dịch bổ sung (DOCX) |
| transkripti çevrimdışı okumak | — | 🔄 dịch bổ sung (offline) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` hoặc body. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ **Volume trang này thấp hơn hẳn `/tr/video-to-text`.** Lý do: "tải transcript" là nhu cầu hẹp hơn "chuyển video thành văn bản". Không cố nhồi mật độ — chiến lược là **phủ đều 12 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Thổ **đã biết mình muốn transkript** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài eklenti (tiện ích).
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **çevrimdışı** (offline).
- Miễn phí, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Thổ, ra đúng dấu `ı ş ğ ç ö ü`.

### Khác biệt so với bản tiếng Anh

1. **`indirme` đứng trần bị hiểu là tải VIDEO — bản EN không gặp.** Trong tiếng Anh "download" trung tính, còn tiếng Thổ thì `youtube indirme` gần như luôn có nghĩa tải mp4. Đây là ràng buộc nặng nhất của bản tr: mọi động từ `indir` phải có tân ngữ `transkript`/`metin`/`dosya`. Xem mục cảnh báo riêng ở trên.
2. **Phải chủ động nhường cụm `altyazı` cho trang anh em.** Bản EN có "transcript" và "subtitle" tách bạch nên không cần luật; bản tr phải neo `zaman kodlu altyazı dosyası` mỗi lần buộc nhắc, và chỉ đẩy đi 1 lần ở S6.
3. **Song song `transkript` (Thổ hoá) và `transcript` (Latin).** Người dùng Thổ gõ cả hai dạng (`youtube transcript indir` đạt 10–100). Bản EN chỉ có một dạng. Xử lý: dùng `transkript` làm dạng chuẩn xuyên suốt, cho dạng Latin xuất hiện **đúng 1 lần** ở S1 đoạn 3 như cách người dùng thật hay gõ.
4. **Nhấn nỗi lo dấu tiếng Thổ.** Nhiều công cụ deşifre làm hỏng `ı ş ğ ç ö ü` khi xuất file. Bản EN không có mối lo này. Xử lý **trong S5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ tiếng Thổ — không thêm câu.
5. **Nhấn DOCX mạnh hơn bản EN.** Sinh viên và nhân viên văn phòng Thổ thường cần bản Word để nộp bài / làm tutanak (biên bản).

---

## Đối tượng người dùng

- Sinh viên, nghiên cứu sinh (lưu transkript bài giảng, phỏng vấn vào thư mục đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX để làm tutanak / tài liệu nội bộ)
- Người học ngoại ngữ (tải TXT đọc çevrimdışı)
- Người làm phụ đề cần bản nháp có timecode (SRT)
- Người cần đưa transkript vào công cụ khác yêu cầu upload file

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Transkript İndirme | youtube transkript indirme *(KW chính)* |
| — | **quickAnswer** | youtube transkript nasıl indirilir |
| 1 | Transkripti İndirmek Size Ne Kazandırır | youtube transkript indirme, youtube video metni indir, deşifre metni, yazıya dökülmüş, **youtube transcript indir** *(dạng Latin, 1 lần)* |
| 2 | Hangi Formatı İndirmelisiniz? | youtube transkript txt indir, **youtube altyazı metin olarak indir** *(mục TXT)*, `zaman kodlu altyazı dosyası` *(mục SRT)* |
| 3 | YouTube Transkripti Nasıl İndirilir | youtube transkript nasıl indirilir, youtube video transkript indir |
| 4 | Sadece Metin Değil, Dosyanın Kendisi Gerektiğinde | youtube transkript kaydet, transkripti çevrimdışı okumak |
| 5 | 100'den Fazla Dilde Transkript İndirme | youtube transkript ücretsiz indir, download youtube transcript türkçe *(+ nhấn dấu tiếng Thổ)* |
| 6 | Başka Bir Araç Daha Uygun Olduğunda | ⚠️ **youtube altyazı indirme — đúng 1 lần, trong câu trỏ sang `/tr/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | Sıkça Sorulan Sorular | youtube transkript ücretsiz indir, youtube transkript txt indir + long-tail |
| — | **conclusion** | youtube transkript indirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây cũng là chỗ duy nhất cụm `youtube altyazı indirme` được xuất hiện, và phải kèm neo `zaman kodlu altyazı dosyası`.
- **S6 câu về Summarizer bắt buộc dùng `özetler`, KHÔNG dùng `indirger`** — xem mục rủi ro `indirme` ở trên.
- Nỗi lo dấu tiếng Thổ xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ tiếng Thổ (liệt kê `ı, ş, ğ, ç, ü`) — không thêm câu.
- `deşifre metni` và `yazıya dökülmüş metin` gộp vào **1 câu duy nhất ở S1 đoạn 2** làm từ giải thích cho `transkript`. Rải nhiều hơn sẽ nghe nặng và lệch giọng người dùng thật.
- Dạng Latin `transcript` dùng **đúng 1 lần** (S1 đoạn 3). Nhiều hơn sẽ loãng dạng chuẩn `transkript`.

---

## Không nên tối ưu cho các keyword

- **`youtube altyazı indirme` / `youtube altyazı dosyası indirme` / `youtube srt altyazı indirme` / `youtube altyazı çıkarma` / `youtube altyazı indirici`** → **/tr/youtube-subtitle-downloader** (file phụ đề khớp giờ cho editor). Xem quy tắc 1 lần ở trên.
- `youtube transkript` / `youtube transkript görüntüleme` / `youtube transkript okuma` → **/tr/youtube-transcript** (đọc trên màn hình, không tải file).
- `youtube video özetleme` / `youtube video özeti` → **/tr/youtube-video-summarizer**.
- **`youtube video indirme` / `youtube mp4 indir` / `youtube indirici` / `youtube video indirme sitesi`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **chữ**. Quy tắc: `indir` luôn phải có tân ngữ `transkript`/`metin`/`dosya`.
- `youtube altyazı ekleme` / `youtube altyazı oluşturma` → **hướng dẫn thao tác trong YouTube Studio**, không phải công cụ tải.
- `video yazıya çevirme` (không có chữ youtube) → **/tr/video-to-text** (upload file từ máy, không dán link).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → /tr/youtube-transcript (chỉ muốn đọc/copy trên màn hình, không cần file)
- → /tr/youtube-subtitle-downloader (cần `zaman kodlu altyazı dosyası` cho phần mềm dựng phim) — **đây là link quan trọng nhất, cũng là chỗ neo cụm `youtube altyazı indirme`**
- → /tr/youtube-video-summarizer (chỉ cần ý chính, không cần toàn văn)

---

## Ghi chú kỹ thuật cho tr.json

- Xưng hô **ngôi 2 số nhiều lịch sự (`-siniz` / `yapıştırın` / `seçin`)**, nhất quán với `/tr/video-to-text`.
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- Dạng chuẩn của khái niệm: **`transkript`** (Thổ hoá). Dạng Latin `transcript` chỉ 1 lần ở S1.
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 = `intro` 1 + `items` 4, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5 `content` 2, S6 `content` 2, S7 `items` 8, `conclusion.content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/tr/...`.
- **Chính tả ĐÚNG DẤU 100%**: `ı ş ğ ç ö ü` và chữ hoa `İ` (chữ i hoa của tiếng Thổ có chấm — `İndirme`, KHÔNG phải `Indirme`).
- Dấu nháy đơn trước hậu tố của danh từ riêng: `TranscriptX'e`, `YouTube'da`, `DOCX'tir`.
- **Tuyệt đối không để chuỗi `video indir` / `videoyu indir` / `indirger` xuất hiện.**
