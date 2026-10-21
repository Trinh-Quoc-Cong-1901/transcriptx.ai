🔥 TranscriptX – TikTok Caption Downloader (Spanish / es)

URL:
/es/tiktok-caption-downloader

Intent chính:

Descargar subtítulos de TikTok en archivo con marcas de tiempo (gratis)

Trang này nhắm đến người dùng nói tiếng Tây Ban Nha muốn **tải file phụ đề** (`archivo de subtítulos`) của một video TikTok công khai — file có mốc thời gian từng dòng — để gắn lại lên video khi đăng lại, để dịch sang ngôn ngữ khác, hoặc để đáp ứng nhu cầu tiếp cận (accesibilidad).

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/es/instagram-caption-downloader`.**
>
> Dù tên gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/es/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (`caption`, `descripción`, hashtag, emoji) | Lời **NÓI** trong video |
> | Kết quả | Đoạn text đọc được | **`archivo de subtítulos` có timecode** |
> | Từ chủ đạo | `caption` / `descripción` / `pie de foto` | **`subtítulos`** |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram, `subtítulos` chỉ là **intent lân cận** dùng thưa trong body vì caption ở đó là chữ viết. **Ở trang này thì ngược lại: `subtitulos de tiktok` CHÍNH LÀ keyword chính, có volume.** Đừng áp nhầm quy tắc của trang kia.

> ⚠️ **Phân định với `/es/tiktok-transcript` — trục TIMING, không phải viết-vs-nói.** Cả hai trang đều lấy lời NÓI từ audio. Khác nhau ở **timing**: trang này ra **`archivo de subtítulos` khớp thời gian** để chạy đè lên video; trang transcript ra **`texto plano`** để đọc/copy. Bản EN cài sẵn 3 chốt chặn — **section 2** (cả section dành riêng để phân định, có internal link), **FAQ 3** ("What is the difference between TikTok captions and a transcript?"), và **section 1 đoạn 2**. Giữ nguyên cả ba, dịch sát, không rút gọn, không gộp.

---

## ⚠️ Lưu ý riêng cho bản es — dữ liệu keyword MỎNG NHẤT trong các trang đã làm

`2_loc_kw.md` section `## Spanish (es)` **chỉ có đúng 2 keyword**:

| Keyword | Volume |
| ------- | ------ |
| subtitulos de tiktok | 10 – 100 |
| subtitulos de tiktok en archivo | 0 – 10 |

So sánh: `fr` có 11 keyword, `ko` có 10, `tr` có 7. Bản `es` chỉ có 2 → **tỉ lệ dịch bổ sung rất cao: khoảng 2/12 ≈ 17% đã search, ~83% là dịch bổ sung**. Hệ quả về chiến lược:

- **Không có cụm nào để dồn lực.** Cả hai keyword đều xoay quanh đúng một head term `subtítulos de TikTok`. Trục nội dung phải neo chặt vào head term này ở `title` / `h1` / `h2` / `description`, phần còn lại dịch tự nhiên theo bản EN.
- **Nhóm động từ `descargar` KHÔNG có dữ liệu search** — không có `descargar subtitulos de tiktok` trong danh sách. Nhưng đây là landing page của một công cụ tải, nên `descargar` vẫn phải xuất hiện; xếp nó là 🔄 *dịch bổ sung* và luôn đi kèm tân ngữ an toàn (xem `## Không nên tối ưu`).
- **Keyword thứ hai `subtitulos de tiktok en archivo` chứa chữ `archivo` — đó chính là điểm phân định của trang này** với `/es/tiktok-transcript`. Từ `archivo` vừa là keyword vừa là lập luận phân định. Đặt nó ở **H2 section 4**.

### `subtítulos` vs `caption` phân vai thế nào

| Từ | Vai trên trang này |
| --- | --- |
| `subtítulos` | **Từ chủ đạo.** Là keyword chính. Dùng ở title, h1, mọi h2 cần neo, xuyên suốt body. |
| `archivo de subtítulos` | Biến thể neo keyword phụ + là bằng chứng phân định với transcript. |
| `caption` | **Gần như không dùng.** Tiếng TBN mượn `caption` cho chữ viết dưới bài (đúng ngữ cảnh trang Instagram). Ở đây dùng nó sẽ kéo nhầm intent. Chỉ chấp nhận trong cụm `subtítulos automáticos` khi nói về tính năng auto-caption của TikTok — và ngay cả chỗ đó vẫn dịch là `subtítulos automáticos`, không viết `caption`. **Grep `caption` trong `es.json` phải = 0.** |
| `transcripción` / `texto plano` | Chỉ xuất hiện ở section 2, FAQ 3 và section 1 đoạn 2, để **đẩy** user sang trang kia — không phải để tối ưu. |

---

## Từ khóa chính

subtitulos de tiktok (10–100) ✅ *đã search* → viết có dấu: **subtítulos de TikTok**

---

## Từ khóa phụ

### Nhóm Danh từ (trục chính — phủ head term)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| subtitulos de tiktok | 10–100 | ✅ đã search *(KW chính)* |
| subtitulos de tiktok en archivo | 0–10 | ✅ đã search *(neo H2 section 4)* |
| subtítulos de un video de TikTok | — | 🔄 dịch bổ sung (tiktok video captions) |
| subtítulos en TikTok | — | 🔄 dịch bổ sung (captions on tiktok) |

### Nhóm Tải / Lấy (dịch bổ sung — không có data)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| descargar subtítulos de TikTok | — | 🔄 dịch bổ sung (tiktok subtitles download) |
| descargar los subtítulos en un archivo | — | 🔄 dịch bổ sung (subtitle file download) |
| bajar subtítulos de TikTok | — | 🔄 dịch bổ sung (biến thể LatAm, dùng tối đa 1 lần) |
| guardar los subtítulos | — | 🔄 dịch bổ sung (save subtitles) |
| extraer subtítulos de TikTok | — | 🔄 dịch bổ sung (extract subtitles) |

### Nhóm Dịch / Đa ngôn ngữ (khớp đúng section 5 của bản EN)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| traducir subtítulos de TikTok | — | 🔄 dịch bổ sung (translate captions) |
| subtítulos de TikTok en más de 100 idiomas | — | 🔄 dịch bổ sung |

### Dịch bổ sung khác (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| subtítulos gratis | — | 🔄 dịch bổ sung (free) |
| archivo SRT de TikTok | — | 🔄 dịch bổ sung (SRT file) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

> ⚠️ **Chỉ 2/12 keyword có dữ liệu thật.** Không được bịa volume cho nhóm 🔄. Chiến lược: neo cứng head term `subtítulos de TikTok` ở mọi vị trí quan trọng, để phần dịch bổ sung phủ đuôi dài một cách tự nhiên.

---

## Search Intent

Người dùng nói tiếng TBN thấy một video TikTok và cần **file phụ đề** của nó — không phải để đọc, mà để **dùng lại**:

- Đăng lại clip (repost) lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có subtítulos.
- Dịch subtítulos sang tiếng TBN hoặc ngôn ngữ khác rồi gắn lại (thị trường es trải dài Tây Ban Nha + LatAm, nhu cầu dịch rất cao).
- Sửa lại subtítulos tự động của TikTok vốn hay sai dấu, sai chính tả.
- Làm subtítulos cho người khiếm thính.

Họ kỳ vọng:

- Dán link là ra **archivo**, không cần đăng nhập TikTok.
- File có **marcas de tiempo** từng dòng, mở được bằng phần mềm dựng phim.
- Chạy được cả khi video gốc **không bật subtítulos**.
- Sửa được chữ trong file trước khi dùng.
- Gratis.

### Khác biệt so với bản tiếng Anh

1. **Tiếng TBN chỉ có một từ `subtítulos` cho cả `captions` lẫn `subtitles`.** Bản EN dùng hai từ xen kẽ để đỡ lặp (`captions` ở H1, `subtitles` ở section 4). Bản es không có lựa chọn đó — chống lặp bằng cách đổi cấu trúc câu và luân phiên `subtítulos` / `archivo de subtítulos` / `líneas de subtítulos` / `las líneas` / `el archivo`.
2. **`caption` là từ bị cấm ở đây nhưng lại là từ chủ đạo ở trang Instagram cùng tên.** Bản EN không gặp mâu thuẫn này vì `caption` trong tiếng Anh mang cả hai nghĩa. Bản es phải chủ động chọn `subtítulos` và giữ grep `caption` = 0 để hai landing page không ăn thịt nhau.
3. **Dữ liệu keyword mỏng hơn hẳn mọi bản khác (2 keyword).** Bản EN có 6 keyword để trải đều 6 section; bản es phải lặp lại cùng một head term ở nhiều vị trí neo mà không được để văn bản nghe như nhồi từ khóa — nên phần lớn nội dung là dịch bám sát EN, keyword áp bằng cách chọn từ khi dịch chứ không thêm cụm.
4. **`archivo` được nâng cấp từ chi tiết kỹ thuật thành lập luận phân định.** Ở bản EN, "file" chỉ là danh từ mô tả kết quả. Ở bản es, `archivo` nằm trong chính keyword đã search (`subtitulos de tiktok en archivo`), nên nó vừa gánh SEO vừa gánh việc tách trang này khỏi `/es/tiktok-transcript`. Đặt ở H2 section 4.
5. **Xưng `tú`, `video` viết không dấu**, đồng bộ với `/es/instagram-transcript` và `/es/instagram-caption-downloader` trong repo.

---

## Đối tượng người dùng

- Người làm content re-upload / tổng hợp clip TikTok ở Tây Ban Nha và Mỹ Latinh
- Editor video, freelancer dựng phim
- Người cross-post TikTok sang Reels / YouTube Shorts
- Người dịch subtítulos (ES ↔ EN, ES ↔ PT) cho khán giả nói tiếng TBN
- Marketer chạy nội dung đa ngôn ngữ cho thị trường LatAm
- Người làm nội dung cho người khiếm thính
- Người muốn sửa subtítulos tự động sai dấu của TikTok

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `es.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**.

| # | H2 (es) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Descargar subtítulos de TikTok | subtitulos de tiktok *(KW chính)* |
| — | **quickAnswer** | subtitulos de tiktok, descargar subtítulos |
| 1 | Qué hace este descargador de subtítulos de TikTok | subtitulos de tiktok, subtítulos de un video de TikTok |
| 2 | ¿Subtítulos o transcripción? Cuál necesitas | *(phân định + internal link `/es/tiktok-transcript`)* |
| 3 | Cómo descargar los subtítulos de TikTok | descargar subtítulos de TikTok |
| 4 | Qué puedes hacer con los subtítulos de TikTok en archivo | **subtitulos de tiktok en archivo** *(neo KW phụ đã search)* |
| 5 | Subtítulos de TikTok en más de 100 idiomas | traducir subtítulos de TikTok |
| 6 | Preguntas frecuentes | subtitulos de tiktok + long-tail |
| — | **conclusion** | descargar subtítulos de TikTok, gratis |

### Ghi chú riêng cho bản es (KHÔNG tạo section mới)

- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho việc này. Dịch đủ 2 item, giữ link `[TikTok Transcript](/es/tiktok-transcript)` ở item 2. Lập luận phải là **timing**, không phải viết-vs-nói.
- **FAQ 3** là chốt thứ hai (`¿Cuál es la diferencia entre los subtítulos de TikTok y una transcripción?`) — dịch sát, không rút gọn, giữ nguyên cả hai vế và lời khuyên chọn công cụ.
- **Section 1 đoạn 2** là chốt thứ ba — đoạn giải thích "timing là lý do trang này tách riêng". Không được gộp vào đoạn 1 hay đoạn 3.
- `subtitulos de tiktok en archivo` chỉ neo **một lần ở H2 section 4**; trong body của section đó dùng `el archivo`, `un archivo de subtítulos` để tránh lặp cứng.
- Nỗi lo subtítulos tự động sai dấu xử lý **trong câu đã có** ở section 4 item 3, không thêm câu mới.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `transcripcion de tiktok` / `pasar tiktok a texto` / `texto de un video de tiktok` → **/es/tiktok-transcript** (**texto plano**, không timing). Chỉ được nhắc để đẩy user sang đó, không tối ưu.
- `caption de instagram` / `descripción de instagram` / `pie de foto` → **/es/instagram-caption-downloader** (chữ viết dưới bài, khác hẳn). Grep `caption` trong `es.json` phải = 0.
- `subtitulos de youtube` / `transcripcion de youtube` → **/es/youtube-transcript**
- **Nhóm tải VIDEO — nguy hiểm nhất:** `descargar video de tiktok`, `tiktok sin marca de agua`, `descargar tiktok`, `guardar video de tiktok` → SERP toàn downloader video. Trang này tải **archivo de subtítulos**, KHÔNG tải video.
  - **Quy tắc cứng:** `descargar` / `bajar` / `guardar` chỉ được đi với tân ngữ **`subtítulos`** / **`archivo`** / **`texto`** / **`las líneas`**. **KHÔNG BAO GIỜ** đi với **`video`**.
  - Cụ thể: các chuỗi `descargar el video`, `descargar un video`, `descargar video`, `bajar el video`, `guardar el video` phải **không xuất hiện** ở bất kỳ đâu trong `es.json`.
  - Khi cần nói "video TikTok", dùng làm bổ ngữ sau danh từ subtítulos: `los subtítulos de un video de TikTok` — hợp lệ, vì tân ngữ của `descargar` vẫn là `subtítulos`.
- `como poner subtitulos en tiktok` / `activar subtitulos tiktok` → **hướng dẫn thao tác trong app**, không phải công cụ tải file.

---

## Internal linking

- ↔ /es/tiktok-transcript (khi user chỉ cần `texto plano` để đọc, không cần timing) — link quan trọng nhất, nằm ở **section 2 item 2**, nhắc lại (không link) ở **FAQ 3**
- ↔ /es/instagram-caption-downloader — **KHÔNG link chéo**: hai trang khác intent hoàn toàn, link chéo sẽ làm nhiễu tín hiệu.

---

## Ghi chú kỹ thuật cho es.json

- Xưng hô **`tú`** (tuteo), nhất quán với các trang es khác trong repo. Dùng `pega`, `copia`, `guarda`, `puedes`.
- **`video` viết không dấu** (biến thể LatAm) — không dùng `vídeo`.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT**.
- Cấu trúc: **6 section**, **8 FAQ**. seo 6 keys · hero 4 · quickAnswer 2. S1 `content` **3** | S2 `intro` 1 + `items` 2 | S3 `steps` 4 | S4 `intro` 1 + `items` 5 | S5 `content` **2** | S6 `items` **8** | conclusion h2 + `content` **2**.
- Internal link section 2 giữ cú pháp markdown: `[TikTok Transcript](/es/tiktok-transcript)`.
- **Grep `caption` = 0.** **Grep `descargar video` / `descargar el video` / `descargar un video` = 0.**
- Tránh lặp `subtítulos` quá dày: luân phiên `archivo de subtítulos`, `líneas de subtítulos`, `las líneas`, `el archivo`, `los subtítulos`.
- `marcas de tiempo` dùng ở câu giải thích đầu tiên; sau đó chuyển sang `tiempo de inicio y de fin`, `sincronizados`, `el tiempo` cho tự nhiên.
