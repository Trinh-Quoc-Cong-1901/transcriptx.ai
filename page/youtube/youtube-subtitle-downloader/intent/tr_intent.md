🔥 TranscriptX – YouTube Subtitle Downloader (Turkish / tr)

URL:
/tr/youtube-subtitle-downloader

Intent chính:

YouTube altyazı indirme (SRT · VTT, ücretsiz)

Trang này nhắm đến người dùng Thổ Nhĩ Kỳ muốn **tải file phụ đề có zaman kodu** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại video kèm phụ đề, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu erişilebilirlik (tiếp cận).

---

## 🚨 CỤM YOUTUBE 5 TRANG — TRANG NÀY LÀ BÊN **NHẬN** KEYWORD

Repo có 5 trang YouTube dễ ăn thịt nhau. Quy tắc phân chia **theo ngữ nghĩa từ** đã chốt từ khi làm `/tr/download-youtube-transcript`:

> **`altyazı` (file phụ đề khớp giờ cho editor) → TRANG NÀY**
> **`transkript` / `metin` (tài liệu để đọc/lưu/nộp) → `/tr/download-youtube-transcript`**

Căn cứ: bản EN section 1 đoạn 2 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Kết quả kiểm trùng thực tế (tr × tr)

Đã đối chiếu `## Turkish (tr)` của trang này (9 keyword) với `../download-youtube-transcript/2_loc_kw.md` (12 keyword).

**Số keyword trùng chuỗi chính xác: 0.** ✅ Tiếng Thổ tách bạch `altyazı` (phụ đề) và `transkript`/`metin` (bản chép lời), nên hai danh sách gần như không giao nhau — thuận lợi hơn hẳn bản `vi` và bản `ko`.

### Trang này ĐƯỢC NHẬN cụm mạnh nhất

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `youtube altyazı indirme` | **100 – 1K** | Cụm mạnh nhất. Trang `/tr/download-youtube-transcript` **đã nhường**, chỉ dùng đúng 1 lần ở S6 đoạn 2 trong câu trỏ sang đây, kèm neo `zaman kodlu altyazı dosyası`. **Trang này lấy làm H1 + title.** |

### Cụm KHÔNG được lấy lại

| Keyword | Thuộc về | Lý do |
| ------- | -------- | ----- |
| `youtube altyazı metin olarak indir` | `/tr/download-youtube-transcript` | Có vế **`metin olarak`** neo rõ là muốn văn bản để đọc, không phải file phụ đề cho editor. Trang đó đã dùng ở S2 (mục TXT). **Trang này tuyệt đối không viết chuỗi `metin olarak`.** |

---

## ⚠️ RỦI RO RIÊNG CỦA BẢN TR (1): `indirme` ĐỨNG TRẦN = TẢI VIDEO

Đây là rủi ro lớn nhất của bản Thổ và ở trang này còn nặng hơn trang đối xứng, vì H1 của trang **chính là** `YouTube Altyazı İndirme`.

Trong tiếng Thổ, `indirme` / `indir` đứng trần trong ngữ cảnh YouTube **mặc định được hiểu là TẢI VIDEO** (`youtube video indirme`, `youtube mp4 indir` — volume khổng lồ, SERP toàn downloader video). Nếu bản tr để lọt một cụm `video indirme` / `videoyu indir`, trang sẽ bắt sai intent và bounce sạch.

**Quy tắc cứng — không có ngoại lệ:**

> `indir` / `indirme` / `indirin` / `indirici` / `indirilir` **chỉ được đi kèm tân ngữ** `altyazı` / `altyazılar` / `altyazı dosyası` / `dosya` / `SRT` / `VTT`.
> **KHÔNG BAO GIỜ** đi kèm `video` / `videoyu`.

### 🔴 Xử lý keyword #2 `youtube video altyazı indirme` (100 – 1K)

Đây là ca khó nhất của bản tr. Keyword này **hợp lệ về intent** (tân ngữ là `altyazı`, chữ `video` chỉ bổ nghĩa), nhưng chuỗi thô của nó — `video altyazı indirme` — **khớp đúng pattern kiểm tra** `video[^.]{0,15}indir` (khoảng cách `video` → `indir` chỉ 9 ký tự).

**Quyết định: viết dạng giãn khoảng cách, giữ nguyên toàn bộ token của keyword.**

| Dạng | Khoảng cách `video`→`indir` | Grep | Dùng |
| ---- | -------------------------- | ---- | ---- |
| ❌ `youtube video altyazı indirme` | 9 ký tự | **DÍNH** | không dùng |
| ❌ `youtube video altyazısı indirme` | 11 ký tự | **DÍNH** | không dùng |
| ✅ `YouTube video altyazı dosyası indirme` | 17 ký tự | sạch | **S4 mục 2** |
| ✅ `bir YouTube videosunun altyazılarını ... indirin` | > 30 ký tự | sạch | hero, S1, FAQ 1 |

Dạng ✅ đầu tiên **gộp luôn keyword #3** `youtube altyazı dosyası indirme` (10–100) — một chuỗi phủ hai keyword. Đây là lợi ích phụ, không phải sự cố.

## ⚠️ RỦI RO RIÊNG CỦA BẢN TR (2): BẪY TỪ `indirger`

- ❌ **`indirger` / `indirgemek` / `indirgeme`** (nghĩa: rút gọn, giản lược) chứa nguyên chuỗi con `indir`. Nó vừa làm nhiễu mọi lệnh grep kiểm tra, vừa đọc nhập nhằng với "tải về".
- Chỗ dễ sa bẫy nhất: **S6, câu về Video Summarizer** — "tóm lược/rút gọn video" rất dễ bị viết thành `indirger`.
- **Bắt buộc dùng `özetler`** (hoặc `ana noktalarıyla verir`). Đã áp dụng trong `tr.json`.
- Các từ khác cần né vì lý do tương tự: `indirim` (giảm giá), `indirgenmiş`.

**Câu chốt an toàn của trang này** — hero + S1 đoạn 3: thứ tải về luôn được gọi thẳng là `altyazı dosyası`, không bao giờ là `video`.

---

## Chính tả dấu + số keyword thực

- Danh sách `## Turkish (tr)` **không có dòng rác** (`Keyword ideas` / `Keywords you provided` chỉ xuất hiện ở phần vi/ko).
- **Chính tả dấu Thổ trong file nguồn: ĐÚNG 100%.** Đã kiểm từng dòng: `altyazı` (ı), `nasıl indirilir` (ı), `çıkarma` (ç/ı), `indirici` (i), `ücretsiz` (ü), `dosyası` (ı).
- **Số keyword thực: 9 dòng thô − 0 rác − 0 sai intent = 9 keyword.** Tất cả 9 cụm đều dùng được và đều đã được neo trong `tr.json`.

⚠️ Phân biệt `ı` (không chấm) và `i` (có chấm) — sai một chữ là sai từ. `altyazı` KHÔNG phải `altyazi`; `nasıl` KHÔNG phải `nasil`; `çıkarma` KHÔNG phải `cikarma`. Chữ **i hoa** của tiếng Thổ có chấm: **`İndirme`**, KHÔNG phải `Indirme`.

---

## Từ khóa chính

**youtube altyazı indirme** (100 – 1K) ✅ *đã search*

Cụm mạnh nhất tuyệt đối trong danh sách tr, và cũng là **lõi chung** của 6 cụm đuôi dài khác (`... sitesi`, `... ücretsiz`, `youtube video altyazı indirme`, `youtube altyazı dosyası indirme`, `youtube srt altyazı indirme`, `youtube altyazı nasıl indirilir`). Neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm İndirme (trục chính)

| Keyword | Volume | Nguồn | Vị trí neo |
| ------- | ------ | ----- | ---------- |
| youtube altyazı indirme | 100–1K | ✅ đã search *(KW chính)* | title, H1, description, conclusion |
| youtube video altyazı indirme | 100–1K | ✅ đã search | S4 mục 2, dạng giãn `video altyazı dosyası indirme` |
| youtube altyazı dosyası indirme | 10–100 | ✅ đã search | S1 đoạn 3, S4 mục 2, FAQ 1 |
| youtube altyazı indirme sitesi | 10–100 | ✅ đã search | FAQ 2 |
| youtube srt altyazı indirme | 0–10 | ✅ đã search | S2 mục SRT |
| youtube altyazı nasıl indirilir | 0–10 | ✅ đã search | quickAnswer, H2 S3, S3 bước 4 |
| youtube altyazı indirme ücretsiz | 0–10 | ✅ đã search | S5 đoạn 2 (`... ücretsizdir`) |

### Nhóm Çıkarma / İndirici

| Keyword | Volume | Nguồn | Vị trí neo |
| ------- | ------ | ----- | ---------- |
| youtube altyazı çıkarma | 10–100 | ✅ đã search | H2 S1, S1 đoạn 3 |
| youtube altyazı indirici | 0–10 | ✅ đã search | FAQ 8 |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| zaman kodlu altyazı dosyası | — | 🔄 dịch bổ sung (timed caption file) |
| altyazı dosyası düzenleme | — | 🔄 dịch bổ sung (edit subtitle file) |
| altyazı çevirisi | — | 🔄 dịch bổ sung (translate subtitles) |
| youtube vtt indirme | — | 🔄 dịch bổ sung (VTT) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` hoặc body. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Thổ **cần file phụ đề để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn altyazı vào bản dựng.
- Đăng lại video lên kênh mình kèm altyazı mà không phải gõ lại.
- Dịch altyazı sang tiếng Thổ hoặc ngôn ngữ khác rồi gắn lại.
- Sửa altyazı tự động của YouTube vốn hay sai dấu tiếng Thổ.
- Đáp ứng yêu cầu erişilebilirlik cho người khiếm thính.

Họ kỳ vọng: dán link là ra file, chọn được SRT hay VTT, có zaman kodu từng dòng, mở sửa được bằng metin düzenleyici, ücretsiz, không cài eklenti.

### Khác biệt so với bản tiếng Anh

1. **`indirme` đứng trần bị hiểu là tải VIDEO — bản EN không gặp.** Trong tiếng Anh "download" trung tính; tiếng Thổ `youtube indirme` gần như luôn có nghĩa tải mp4. Đây là ràng buộc nặng nhất. Xem 2 mục rủi ro ở trên.
2. **`altyazı` là trục duy nhất, không có từ thứ hai.** Bản EN xoay vòng `subtitles` / `captions` để đỡ lặp; tiếng Thổ chỉ có `altyazı`. Chống lặp bằng cách đổi cấu trúc câu và xen kẽ `altyazı dosyası` / `altyazı satırı` / `zaman kodu` / `zaman damgası`.
3. **Trang này là bên NHẬN keyword.** Bản EN không có vấn đề phân chia. Bản tr thì `altyazı` bị kéo về cả hai phía (qua cụm `altyazı metin olarak indir`), nên phải chốt bằng tay.
4. **Nỗi lo dấu tiếng Thổ.** Nhiều công cụ altyazı làm hỏng `ı ş ğ ç ö ü` khi xuất SRT — mở trong Premiere ra ký tự lỗi. Bản EN không có mối lo này. Xử lý **trong S5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.
5. **`nasıl indirilir` là dạng câu hỏi bản địa mạnh.** Người Thổ gõ nguyên câu hỏi vào Google. Cấp hẳn H2 cho S3 + dùng ở quickAnswer.

---

## Đối tượng người dùng

- Video editor, freelancer dựng phim (nạp SRT vào Premiere / Final Cut / Resolve)
- Người re-upload / tổng hợp video lên kênh riêng
- Người làm phụ đề (çevirmen) cho khán giả Thổ
- Marketer chạy nội dung đa ngôn ngữ
- Người làm nội dung cho izleyici khiếm thính
- Người muốn sửa altyazı tự động sai dấu của YouTube

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2 (khác trang download-transcript vốn có 4), đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Altyazı İndirme | youtube altyazı indirme *(KW chính)* |
| — | **quickAnswer** | youtube altyazı nasıl indirilir |
| 1 | Altyazı Dosyası Aslında Nedir — YouTube Altyazı Çıkarma Ne Verir | youtube altyazı çıkarma, youtube altyazı dosyası indirme |
| 2 | SRT mi VTT mi: Hangi Altyazı Formatını İndirmeli | youtube srt altyazı indirme |
| 3 | YouTube'dan Altyazı Nasıl İndirilir | youtube altyazı nasıl indirilir |
| 4 | İndirdiğiniz Altyazı Dosyasıyla Neler Yapabilirsiniz | **youtube video altyazı indirme** *(dạng giãn)*, youtube altyazı dosyası indirme |
| 5 | 100'den Fazla Dilde Altyazı İndirme | youtube altyazı indirme ücretsiz *(+ nhấn dấu tiếng Thổ)* |
| 6 | Altyazı mı, Transkript mi, Özet mi? | *(3 internal link — chốt phân định)* |
| 7 | Sıkça Sorulan Sorular | youtube altyazı indirme sitesi, youtube altyazı indirici + long-tail |
| — | **conclusion** | youtube altyazı indirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là chỗ duy nhất `transkript` được nhắc như một sản phẩm của trang khác. Câu về Summarizer **bắt buộc dùng `özetler`, KHÔNG dùng `indirger`**.
- **Section 1 đoạn 2 là câu chống cannibalization mạnh nhất trang** — định nghĩa ranh giới `transkript` (chữ để đọc) vs `altyazı dosyası` (chữ chạy đè lên video, senkron kare kare). Dịch sát, không rút gọn.
- Nỗi lo dấu tiếng Thổ xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng liệt kê `ı, ş, ğ, ç, ü` — không thêm câu.
- Kết quả của trang **luôn gọi là `altyazı` / `altyazı dosyası`**. Từ `transkript` chỉ được xuất hiện ở **S1 đoạn 2, S6, FAQ 5** — đúng 3 chỗ, đều là chỗ so sánh ranh giới.

---

## Không nên tối ưu cho các keyword

- **`youtube transkript indirme` / `youtube transcript indir` / `youtube video metni indir` / `youtube deşifre metni indir` / `youtube altyazı metin olarak indir`** → **/tr/download-youtube-transcript** (tài liệu để đọc/lưu/nộp). Chỉ được nhắc ở S6.
- `youtube transkript görüntüleme` / `youtube transkript okuma` → **/tr/youtube-transcript** (đọc trên màn hình, không tải file).
- `youtube video özetleme` / `youtube video özeti` → **/tr/youtube-video-summarizer**.
- **`youtube video indirme` / `youtube mp4 indir` / `youtube indirici` / `youtube video indirme sitesi`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **file phụ đề**. Xem quy tắc cứng ở trên.
- `youtube altyazı ekleme` / `youtube altyazı açma` / `altyazı ayarları` → **hướng dẫn bật/thêm phụ đề trong YouTube Studio hoặc app**, không phải công cụ tải.
- `film altyazı indirme` / `dizi altyazı indirme` → **intent tải sub phim từ site sub**, không liên quan YouTube.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → /tr/youtube-transcript (đọc/copy chữ thuần trên màn hình, không zaman kodu)
- → /tr/download-youtube-transcript (lưu chữ thành TXT/DOCX/PDF) — **đây là trang đối xứng, link quan trọng nhất**
- → /tr/youtube-video-summarizer (chỉ cần ana noktalar)

---

## Ghi chú kỹ thuật cho tr.json

- Xưng hô **ngôi 2 số nhiều lịch sự (`-siniz` / `yapıştırın` / `seçin` / `indirin`)**, nhất quán với `/tr/download-youtube-transcript` và `/tr/video-to-text`.
- Giữ nguyên Latin: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok**.
- Dạng chuẩn của khái niệm: **`altyazı`** xuyên suốt. `transkript` chỉ 3 chỗ (S1 đ2, S6, FAQ 5).
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 = `intro` 1 + `items` **2**, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5 `content` 2, S6 `content` 2, S7 `items` 8, `conclusion.content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/tr/...`.
- **Chính tả ĐÚNG DẤU 100%**: `ı ş ğ ç ö ü` và chữ hoa `İ` (`İndirme`, `İndirdiğiniz`, `İndirmeli`).
- Dấu nháy đơn trước hậu tố của danh từ riêng: `TranscriptX'e`, `YouTube'dan`, `Resolve'a`, `VTT'yi`.
- **Tuyệt đối không để chuỗi `video indir` / `videoyu indir` / `video altyazı indir` / `indirger` xuất hiện.** Lệnh kiểm: `grep -nE "video[^.]{0,15}indir|indirger" tr.json` phải trả về rỗng.
