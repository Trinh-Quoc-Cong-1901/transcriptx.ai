🔥 TranscriptX – TikTok Transcript (Turkish / tr)

URL:
/tr/tiktok-transcript

Intent chính:

TikTok videosundaki konuşmayı ücretsiz olarak yazıya çevirme

Trang này là **trang trụ (hub)** cụm TikTok Transcript bản tiếng Thổ. Nhắm đến người dùng Thổ muốn lấy **lời nói** trong video TikTok thành **düz metin để đọc / sao chép / nghiên cứu** — không kèm mốc thời gian.

Gộp toàn bộ intent đồng nghĩa **sesi yazıya çevirme / videoyu metne çevirme / metne dönüştürme / metin çıkarma / yazıya dökme** vì tất cả cho ra **cùng một kết quả**: video TikTok → metin.

> ⚠️ **Phân định với `/tr/tiktok-caption-downloader`: TIMING.** Cả hai trang đều lấy lời NÓI từ audio. Trang này ra **düz metin để đọc** (`transkript`); trang kia ra **zaman kodlu altyazı dosyası** để chạy đè lên video. Bản EN cài sẵn 2 chốt chặn: **section 7 đoạn 2** (link sang trang caption) và **FAQ 8** ("Can I download the TikTok transcript?" → có, nhưng nếu cần file altyazı khớp giờ thì dùng công cụ kia). Giữ nguyên cả hai, dịch sát, không rút gọn, không gộp.

> 🚨 **QUY TẮC DÙNG `altyazı` Ở TRANG NÀY — KHÁC HẲN TRANG CAPTION.**
>
> Ở `/tr/tiktok-caption-downloader`, `altyazı` là **trục chính** (nằm ở H1, title, button, conclusion). Ở trang này, `altyazı` **KHÔNG BAO GIỜ là tên gọi của kết quả**.
>
> | Ngữ cảnh | Cách viết ở trang này | Ghi chú |
> | --- | --- | --- |
> | Kết quả trang này trả về | `transkript` / `metin` | ✅ mặc định, dùng khắp nơi |
> | Chữ tự động hiện trên màn hình video | `ekranda beliren otomatik altyazı`, `ekranda altyazı` | ⚠️ luôn neo bằng `ekran…` |
> | File có timecode (thuộc trang kia) | `zaman kodlu altyazı dosyası` | ⚠️ luôn neo bằng `zaman kodlu` + `dosya` |
> | `altyazı` đứng trần | ❌ CẤM | dễ bị hiểu là trang caption |
>
> `altyazı` chỉ được xuất hiện ở **4 chỗ**: section 2 (spec "Ekranda altyazı olmadan çalışır"), section 4 đoạn 1, section 7 đoạn 2 (câu trỏ đi), FAQ 4 + FAQ 8. Tất cả đều đã neo nghĩa. Tuyệt đối không đặt vào `title` / `h1` / bất kỳ `h2` nào.

> ⚠️ **`indirme` đứng trần trong tiếng Thổ mặc định hiểu là TẢI VIDEO.** SERP của `tiktok video indirme` / `filigransız indir` toàn là video downloader — sai intent hoàn toàn. Quy tắc cứng: `indir` / `indirme` **chỉ được đi kèm** `transkript` / `metin` / `dosya`, **KHÔNG BAO GIỜ** đi với `video`.

> ✅ **Kiểm chính tả dấu ở nguồn `2_loc_kw.md`.** Khác bản Hàn (bị chèn dấu cách thừa), **cả 11 keyword tiếng Thổ ở nguồn đều viết ĐÚNG**, không phải sửa. Bảng dưới ghi nguyên dạng nguồn. Điểm cần canh khi viết `tr.json`: `ı` vs `i` (`yazıya`, `çıkarma`, `dökme` — không phải `yaziya`/`cikarma`), `ç` (`çevirme`), `ö`/`ü`/`ş` (`dönüştürme`), `Ç` hoa trong H2 (`Çevirme`, không phải `Cevirme`).

---

## Từ khóa chính

tiktok sesi yazıya çevirme (10–100) ✅ *đã search*

Chọn làm KW chính vì: (1) volume cao nhất trong 11 keyword; (2) chữ **`sesi`** tự nó neo đúng cơ chế của trang — text dựng **từ audio**, không phụ thuộc altyazı có sẵn; (3) không chứa `altyazı` nên không đụng trang caption; (4) không chứa `video indirme` nên không rơi vào intent tải video.

---

## Từ khóa phụ

### Nhóm yazıya çevirme / dökme (trục chính — đưa lời nói thành chữ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok sesi yazıya çevirme | 10–100 | ✅ đã search *(KW chính)* |
| tiktok video yazıya çevirme | 0–10 | ✅ đã search |
| tiktok videoyu yazıya dökme | 0–10 | ✅ đã search |
| tiktok yazıya dökme | 0–10 | ✅ đã search |
| tiktok video yazıya çevirme ücretsiz | 0–10 | ✅ đã search |

### Nhóm metne çevirme / dönüştürme (chuyển đổi)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok videoyu metne çevirme | 0–10 | ✅ đã search |
| tiktok video metne dönüştürme | 0–10 | ✅ đã search |
| tiktok metne çevirme | 0–10 | ✅ đã search |

### Nhóm metin çıkarma / kopyalama (bóc chữ ra + công cụ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok videodan metin çıkarma | 0–10 | ✅ đã search |
| tiktok metin çıkarma aracı | 0–10 | ✅ đã search |
| tiktok video metin kopyalama | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H1/H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok transkript | — | 🔄 dịch bổ sung (transcript) |
| tiktok transkript oluşturucu | — | 🔄 dịch bổ sung (generator) |
| tiktok metin çıkarma sitesi | — | 🔄 dịch bổ sung (tool site) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Thổ xem một video TikTok ngắn và muốn **giữ lại lời nói** trong đó thành chữ — vì phần giá trị thường chỉ nằm ở một câu, và clip trôi rất nhanh khỏi tab **Senin İçin**.

Họ kỳ vọng:

- Dán link là ra chữ trong vài giây, không cần đăng nhập TikTok.
- Chạy được cả khi video **không có chữ trên màn hình** (`ekranda altyazı yok`).
- Nhận dạng tốt **tiếng Thổ** — nhất là hậu tố dính và các chữ `ı/i`, `ğ`, `ş` mà auto-caption của TikTok hay sai.
- Sao chép được ngay phần kanca (hook) để nghiên cứu hoặc viết lại.
- Miễn phí, không cài app.

### Khác biệt so với bản tiếng Anh

1. **Trục chính là `ses` (audio), không phải `transcript`.** Bản EN xoay quanh danh từ "transcript". Tiếng Thổ không có danh từ đó ở dạng phổ biến trong search — người ta gõ **động từ**: `yazıya çevirme`, `metne dönüştürme`, `yazıya dökme`. Nên H1 phải là cụm động từ `TikTok Sesi Yazıya Çevirme`, và `transkript` chỉ đóng vai từ giải thích trong body.
2. **Tiếng Thổ có 3 trục song song cho cùng một hành động: `yazıya çevirme` / `metne dönüştürme` / `metin çıkarma`.** Bản EN gộp hết vào "transcript / generate / convert". Mỗi trục tiếng Thổ có keyword riêng nên phải phân bổ ra 3 section khác nhau (S3–S4–S5) thay vì chọn một.
3. **Phải chủ động nhường toàn bộ từ `altyazı` cho trang caption.** Bản EN không có vấn đề này vì "caption" và "transcript" là hai từ khác hẳn. Tiếng Thổ chỉ có một từ `altyazı` phủ cả hai nghĩa → phải neo nghĩa mọi lần dùng. Xem khối quy tắc ở đầu file.
4. **Phải chủ động tránh intent tải video.** `indirme` trong tiếng Thổ mặc định = tải video, SERP toàn downloader. Bản EN không gặp rủi ro này vì "download transcript" đã tự đủ rõ.
5. **Ví dụ ngôn ngữ ở section 4 đoạn 3 đổi để có tiếng Thổ.** Bản EN nêu Spanish/Indonesian; bản tr thêm Türkçe lên đầu để trả lời nỗi lo "có nhận dạng tiếng Thổ không". Không thêm câu mới.

---

## Đối tượng người dùng

- Người xem TikTok muốn lưu mẹo / công thức trước khi clip trôi mất
- Content creator Thổ nghiên cứu kanca (hook) của video viral
- Marketer phân tích clip đối thủ
- Người học ngoại ngữ (đọc chậm lời nói nhanh của người bản xứ)
- Nhà báo / người viết cần trích dẫn chính xác
- Người tái sử dụng nội dung sang Reel / Shorts / blog

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng **8 `specs`** (khác trang Facebook/Instagram vốn có 10), đúng 4 `steps`, đúng **6 `items`** ở section 6, đúng **8 FAQ**, đúng **2 internal link**.

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** TikTok Sesi Yazıya Çevirme | tiktok sesi yazıya çevirme *(KW chính)* |
| — | **quickAnswer** | tiktok video yazıya çevirme |
| 1 | TikTok Transkripti Nedir? | tiktok sesi yazıya çevirme, tiktok metne çevirme |
| 2 | Bir Bakışta TikTok Sesi Yazıya Çevirme | *(bảng 8 thông số)* |
| 3 | TikTok Sesi Yazıya Nasıl Çevrilir? | tiktok videoyu yazıya dökme, tiktok video metin kopyalama |
| 4 | TikTok Metin Çıkarma Aracı | tiktok metin çıkarma aracı, tiktok videodan metin çıkarma, tiktok sesi yazıya çevirme |
| 5 | TikTok Videoyu Metne Çevirme | tiktok videoyu metne çevirme, tiktok video metne dönüştürme, tiktok videoyu yazıya dökme |
| 6 | Kısa Bir TikTok'u Neden Yazıya Dökmeli? | tiktok yazıya dökme *(intro + 6 items)* |
| 7 | Kopyalayın, Düzenleyin, Çevirin veya İndirin | tiktok video yazıya çevirme ücretsiz + ⚠️ **2 link: `/tr/tiktok-caption-downloader`, `/tr/youtube-transcript`** |
| 8 | Sıkça Sorulan Sorular | tiktok video metne dönüştürme, tiktok metin çıkarma aracı + long-tail |
| — | **conclusion** | tiktok sesi yazıya çevirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

- Sắc thái `çıkarma` (dễ bị hiểu là bóc file có sẵn) xử lý **trong section 4** — bản EN vốn nói text được dựng từ audio chứ không phụ thuộc caption. Không thêm câu.
- Nỗi lo "có nhận dạng tiếng Thổ không" xử lý **trong section 4 đoạn 3** và **FAQ 5**, chỉ đổi ví dụ ngôn ngữ. Không thêm câu.
- **Section 7 đoạn 2 và FAQ 8 là hai chốt phân định với trang caption** — dịch sát, giữ nguyên cấu trúc "có, tải được transkript / nhưng nếu cần `zaman kodlu altyazı dosyası` thì sang trang kia".
- Section 6 item 4 dùng `Reel` / `Shorts` giữ nguyên Latin, nhất quán với trang caption tr.

---

## Không nên tối ưu cho các keyword

- **`tiktok altyazı indirme` / `tiktok altyazı dosyası` / `tiktok altyazı indir`** → **/tr/tiktok-caption-downloader** (zaman kodlu altyazı dosyası). Trang này KHÔNG nhắm bất kỳ keyword nào chứa `altyazı`; từ `altyazı` chỉ xuất hiện đã neo nghĩa, và đúng 1 lần ở section 7 trong chính câu trỏ sang trang kia.
- `youtube transkript` / `youtube altyazı indirme` → **/tr/youtube-transcript**
- `instagram video transkript` / `instagram videodan metin çıkarma` → **/tr/instagram-transcript**
- `instagram açıklama indirme` → **/tr/instagram-caption-downloader** (chữ VIẾT dưới bài)
- **`tiktok video indirme` / `tiktok filigransız indir` / `tiktok video indir`** → **intent tải VIDEO**, SERP toàn downloader, không phải nhu cầu văn bản. Trang này lấy **chữ**. Quy tắc: `indir`/`indirme` chỉ đi với `transkript` / `metin` / `dosya`, **không bao giờ** với `video`.

---

## Internal linking

- ↔ /tr/tiktok-caption-downloader (khi user cần `zaman kodlu altyazı dosyası` thay vì düz metin) — **section 7 đoạn 2**, nhắc lại ở **FAQ 8**
- → /tr/youtube-transcript (cross-cluster, video dài) — cùng section 7

---

## Ghi chú kỹ thuật cho tr.json

- Giọng văn: ngôi **siz** (`yapıştırın`, `okuyun`), câu mệnh lệnh ngắn — nhất quán với `/tr/instagram-transcript` và `/tr/tiktok-caption-downloader`.
- Giữ nguyên Latin: **TranscriptX**, **TikTok**, **Reel**, **Shorts**. Dấu nháy trước hậu tố tên riêng: `TranscriptX'e`, `TikTok'un`, `Reel'e`.
- **Chính tả ĐÚNG DẤU 100%**: `ı` / `i`, `ş`, `ç`, `ğ`, `ö`, `ü`. Canh kỹ: `yazıya`, `çevirme`, `dökme`, `çıkarma`, `dönüştürme`, `düzenleyin`, `ücretsiz`, `içerik`.
- Gọi hook là **`kanca`** (đồng bộ với `/tr/instagram-transcript` tr).
- Gọi For You page là **`Senin İçin akışı`**.
- Internal link section 7 giữ cú pháp markdown: `[TikTok Altyazı İndirme](/tr/tiktok-caption-downloader)`, `[YouTube Transkript](/tr/youtube-transcript)`.
- Cấu trúc: **8 section**, **8 `specs`**, 4 `steps`, **6 `items`** ở section 6, **8 FAQ**, section 7 = `content` 2 đoạn, conclusion = `content` 2 đoạn.
