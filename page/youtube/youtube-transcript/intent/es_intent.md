🔥 TranscriptX – YouTube Transcript (Spanish / es)

URL:
/es/youtube-transcript

Intent chính:

transcribir video de youtube / obtener la transcripción de YouTube online, gratis

Trang này nhắm đến người dùng nói tiếng Tây Ban Nha muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán URL là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 💰 TRANG LỚN NHẤT VÀ GIÁ TRỊ CAO NHẤT CỦA TOÀN DỰ ÁN

Đây là landing page **lớn nhất** đã làm từ trước tới nay:

- **12 section** (gấp đôi mọi trang trước), trong đó có `specs` **10 dòng**, S6 **6 items**, S10 **5 items**, S8 **2 items**, S12 **12 FAQ**, `conclusion` **3 đoạn**.
- **4 internal link** ở section 11 — nhiều nhất dự án.
- Cụm chính `transcribir video de youtube` đạt **10K – 100K**, là **cụm mạnh nhất toàn bộ dự án tiếng Tây Ban Nha**, cộng thêm **6 cụm bậc 1K – 10K**.

Vì khối lượng volume dồn vào đây lớn hơn hẳn các trang khác, bản `es` này được làm **PILOT** — 12 ngôn ngữ còn lại của trang sẽ dùng bản này làm bài mẫu về cấu trúc intent, cách chia nhóm keyword và cách xử lý ranh giới cụm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm. Đã kiểm chéo keyword toàn bộ 5 trang:

| Cặp trang | Số cụm trùng |
| --------- | ------------ |
| `download-youtube-transcript` × `youtube-subtitle-downloader` | 9 *(đã xử lý xong ở vòng trước)* |

### Quyết định đã chốt với người dùng

> Trang này là **hub** nên **giữ trọn họ từ transcript**: `transcripción`, `transcribir`, `transcript`, **và cả nhóm `extraer` / `sacar texto`**.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ 14 keyword đúng intent trong danh sách `## Spanish (es)` đều thuộc về trang này, kể cả nhóm `convertir video de youtube a texto` / `youtube a texto` / `pasar video de youtube a texto` — vì các cụm đó **có chữ `youtube`**, nên không đụng trang generic `/es/video-to-text`.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **Section 11 (`Copiar, editar, traducir o descargar`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (`transcripción` vs `subtítulos`) — chốt với `/es/youtube-subtitle-downloader`.
- **FAQ 4** (`generar` vs `extraer`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — 4 DÒNG ĐÃ LOẠI

Danh sách `## Spanish (es)` trong `2_loc_kw.md` có **18 dòng nhãn keyword**, trong đó **4 dòng là rác hoặc sai intent**. Cách xử lý theo đúng tiền lệ của `/es/youtube-video-summarizer/intent/vi_intent.md` (trang đó cũng dính nhiễm dữ liệu và ghi thành mục riêng):

| Dòng | Volume | Lý do loại |
| ---- | ------ | ---------- |
| `Keyword ideas` | — | **Nhãn giao diện công cụ search**, không phải keyword. Bị copy nhầm khi export. |
| `Keywords you provided` | — | **Nhãn giao diện công cụ search**, không phải keyword. Cùng nguyên nhân. |
| `texttomp3` | 10 – 100 | **Công cụ text-to-MP3 (TTS)** — biến chữ thành giọng nói. **Intent ngược hoàn toàn** với trang này (biến giọng nói thành chữ). Tuyệt đối không tối ưu. |
| `youtube subito texto` | 10 – 100 | **Lỗi chính tả / garbled.** Không phải tiếng Tây Ban Nha chuẩn (`subito` không tồn tại trong ngữ cảnh này; có thể là lỗi OCR của `subtítulo` hoặc lẫn tiếng Ý). Không có intent xác định. |

> ⚠️ Hai dòng `Keyword ideas` / `Keywords you provided` cũng xuất hiện ở section `## French (fr)` và `## Vietnamese (vi)` của cùng file — đây là **lỗi export hệ thống**, cần loại ở mọi ngôn ngữ khi làm 12 bản còn lại. Dòng `texttomp3` cũng lặp lại ở `fr` với đúng volume 10 – 100.

### 📊 Số keyword thực: **18 − 4 = 14**

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói, marcas de tiempo tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **obtener / get** — lấy transcripción có sẵn,
- **generar / generate** — dựng transcripción từ audio khi video không có subtítulos,
- **extraer / sacar** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

Kết quả trang này **luôn gọi là `transcripción` hoặc `texto`** — **không bao giờ** gọi là `subtítulos`.

---

## Từ khóa chính

**transcribir video de youtube (10K–100K)** ✅ *đã search* → **H1**

Đây là cụm có volume cao nhất toàn dự án. Toàn bộ trang được xây quanh nó: xuất hiện ở `title`, `h1`, `ogTitle`, H2 của S2 và S3, `conclusion.h2` và FAQ 1.

---

## Từ khóa phụ

### Nhóm `transcribir` (động từ — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcribir video de youtube | 10K–100K | ✅ đã search *(KW chính)* |
| transcribir youtube | 1K–10K | ✅ đã search |
| como transcribir un video de youtube | 1K–10K | ✅ đã search |
| transcribir audio de youtube a texto | 100–1K | ✅ đã search |

### Nhóm `transcripción` (danh từ — kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcripcion de youtube | 1K–10K | ✅ đã search |
| transcripcion de video de youtube | 1K–10K | ✅ đã search |
| transcripcion automatica youtube | 10–100 | ✅ đã search |
| obtener transcripcion de youtube | 0–10 | ✅ đã search |

### Nhóm `extraer` / `sacar` (rút chữ ra)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| sacar texto de un video de youtube | 1K–10K | ✅ đã search |
| extraer texto de youtube | 100–1K | ✅ đã search |

### Nhóm `a texto` (chuyển đổi)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| convertir video de youtube a texto | 1K–10K | ✅ đã search |
| youtube a texto | 1K–10K | ✅ đã search |
| pasar video de youtube a texto | 100–1K | ✅ đã search |

### Nhóm `generador`

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| generador de transcripciones de youtube | 100–1K | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| separación de hablantes | — | 🔄 dịch bổ sung (speaker separation) |
| marcas de tiempo | — | 🔄 dịch bổ sung (timestamps) |
| más de 100 idiomas | — | 🔄 dịch bổ sung (100+ languages) |
| sin registro / gratis | — | 🔄 dịch bổ sung (no sign-up / free) |
| extractor de guiones de YouTube | — | 🔄 dịch bổ sung (youtube script extractor) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng Tây Ban Nha muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán URL YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu ES ⇄ EN rất nặng ở Mỹ Latinh.
- Hoạt động **cả khi video không có subtítulos** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, bàn tròn).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Tiếng TBN có 3 họ từ song song, tiếng Anh chỉ có 1 trục.** Bản EN xoay quanh danh từ `transcript` là chính (`get/generate/extract a transcript`). Tiếng TBN chia thành **ba họ có volume độc lập và gần ngang nhau**: `transcribir` (động từ, 10K–100K), `transcripción` (danh từ, 1K–10K), và nhóm `sacar/extraer/convertir/pasar … a texto` (cộng lại vượt 3K–30K). Không được dịch tất cả về một từ — phải cấp section riêng: `transcribir` giữ H1 + S3 + S7, `transcripción` giữ S1 + S4 + conclusion, nhóm `a texto` giữ S5.

2. **Động từ trong tiếng TBN mạnh hơn danh từ, ngược hoàn toàn với EN.** `transcribir video de youtube` (10K–100K) vượt `transcripcion de youtube` (1K–10K) một bậc rưỡi. Trong khi bản EN đặt danh từ `YouTube Transcript` làm H1, bản es **phải đặt động từ làm H1** (`Transcribir video de YouTube`). Đây là thay đổi cấu trúc thật, không phải dịch sát nghĩa đen.

3. **Cụm `cómo` là intent riêng có volume thật.** `como transcribir un video de youtube` đạt **1K–10K** — ngang hàng các cụm chính. Bản EN không có "how to" nào có volume tương đương. Phải cấp trọn H2 của **section 3** (steps) và `quickAnswer.question`.

4. **`sacar texto` là cách nói đời thường không có tương đương EN.** `sacar texto de un video de youtube` đạt **1K–10K** — cao hơn hẳn `extraer texto de youtube` (100–1K) vốn là từ trang trọng. Bản EN chỉ có một từ `extract`. Bản es phải dùng **cả hai**: `sacar` trong H2 section 5 và body (giọng đời thường, đúng cách người dùng gõ), `extraer` trong câu kỹ thuật hướng tới developer/researcher.

5. **Rủi ro cannibalization ngược từ nhóm tải VIDEO.** `descargar video de youtube` trong tiếng TBN là cụm khổng lồ, SERP toàn downloader MP4. Kỷ luật cứng: `descargar` **chỉ** đi với `transcripción` / `texto` / `archivo`, **không bao giờ** với `video`. Bản EN không chịu áp lực này ở cùng mức vì "download a video" không cạnh tranh mạnh bằng.

6. **Nhóm `a texto` phải có chữ `youtube` mới được dùng.** Trang generic `/es/video-to-text` đã hoàn thành và đang giữ `convertir video a texto` / `video a texto`. Bản es của trang này chỉ được dùng các biến thể **có `de youtube`** (`convertir video de youtube a texto`, `youtube a texto`, `pasar video de youtube a texto`). Bản EN không có ràng buộc này vì trang EN tương ứng chia khác.

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ ES ⇄ EN ⇄ PT
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `es.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (es) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Transcribir video de YouTube | transcribir video de youtube *(KW chính)* |
| — | **quickAnswer** | como transcribir un video de youtube |
| 1 | ¿Qué es una transcripción de YouTube? | transcripcion de youtube, transcripcion de video de youtube |
| 2 | Transcribir video de YouTube en resumen *(`specs` × 10)* | transcribir video de youtube |
| 3 | Cómo transcribir un video de YouTube *(`steps` × 4)* | como transcribir un video de youtube |
| 4 | Generador de transcripciones de YouTube | generador de transcripciones de youtube, transcripcion automatica youtube |
| 5 | Sacar el texto de un video de YouTube | sacar texto de un video de youtube, extraer texto de youtube, youtube a texto |
| 6 | Para qué sirve una transcripción de YouTube *(`items` × 6)* | transcripcion de video de youtube, pasar video de youtube a texto |
| 7 | Transcribir YouTube en cualquier idioma | transcribir youtube, transcribir audio de youtube a texto |
| 8 | TranscriptX frente a la transcripción integrada de YouTube *(`items` × 2)* | transcripcion automatica youtube |
| 9 | La precisión y qué la afecta | *(E-E-A-T, không nhắm KW)* |
| 10 | Cuándo puede no funcionar una transcripción de YouTube *(`items` × 5)* | transcripcion de youtube |
| 11 | Copiar, editar, traducir o descargar | *(4 internal link — chốt phân định)* |
| 12 | Preguntas frecuentes *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion** *(3 đoạn)* | obtener transcripcion de youtube, transcribir video de youtube, gratis |

### Ghi chú riêng cho bản es (KHÔNG tạo section mới)

- **S2 tái dùng đúng 10 nhãn `specs` đã duyệt ở `/es/video-to-text/es.json`** khi nhãn trùng, chỉ đổi giá trị cho hợp YouTube: `Precio`, `Cuenta necesaria`, `Instalación`, `Idiomas`, `Separación de hablantes`, `Marcas de tiempo`, `Formatos de exportación`, `Dispositivos`. Hai nhãn mới riêng của trang này: `Entrada` (Input — URL video YouTube) và `Funciona sin subtítulos` (Works when the video has no captions).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại**, vì mỗi section giữ một họ keyword riêng của tiếng TBN.
- **S8 là section so sánh** với transcripción tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào. Đây là chỗ duy nhất từ `subtítulos` được dùng để trỏ sang trang phụ đề.
- **Xử lý từ `subtítulos`:** kết quả trang này **luôn** là `transcripción` / `texto`. Khi bản EN nói `captions` (subtítulos của người đăng video / subtítulos tự động của YouTube), dịch thành **`subtítulos automáticos`** hoặc **`subtítulos del creador`** — có định ngữ, không bao giờ để trần. Từ `subtítulos` **để trần** chỉ xuất hiện ở **S11** (link sang `/es/youtube-subtitle-downloader`) và **FAQ 10** (câu hỏi so sánh transcripción vs subtítulos). Đó là hai chỗ duy nhất.
- **Kỷ luật `descargar`:** chỉ đi với `transcripción` / `texto` / `archivo` / `TXT, DOCX, PDF, SRT, VTT`. **Không bao giờ** viết `descargar el video` — kể cả trong S3 bước 1 (bản EN nói "no file to download first" → dịch thành `no hay ningún archivo que descargar antes`, giữ `archivo`, không dùng `video`).
- Xưng hô **`tú`** (`pega`, `copia`, `edita`, `tu dispositivo`) — nhất quán với `/es/youtube-subtitle-downloader/es.json` và `/es/video-to-text/es.json`.
- **`video` viết không dấu** (dạng Mỹ Latinh, cũng là dạng người dùng gõ khi search) — nhất quán toàn bộ các trang es.
- Trong body viết **có dấu đầy đủ** (`transcripción`, `automática`); keyword không dấu trong `2_loc_kw.md` chỉ là dạng người dùng gõ, Google khớp cả hai.
- Nhấn `gratis` ở `title`, `hero.subtitle`, S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`descargar transcripcion de youtube` / `bajar transcripcion youtube` / `descargar transcript youtube`** → **`/es/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`descargar subtitulos de youtube` / `subtitulos srt youtube` / `extraer subtitulos de youtube`** → **`/es/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). Nhóm `subtítulos` để trần thuộc trọn về trang đó.
- **`youtube video a texto`**: giữ ở hub này — không còn trang riêng cho cách gọi "video a texto". Các cụm `convertir/pasar … de youtube a texto` cũng giữ ở đây vì đúng intent transcript.
- **`resumir video de youtube` / `resumen de video de youtube` / `resumidor de youtube`** → **`/es/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`convertir video a texto` / `video a texto` / `transcribir video` / `transcriptor de video`** (không có chữ `youtube`) → **`/es/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `a texto` dùng ở trang này **bắt buộc phải có `youtube`** trong cụm.
- **`audio a texto` / `transcribir audio`** (không có `youtube`) → **`/es/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`descargar video de youtube` / `descargar youtube mp4` / `bajar videos de youtube gratis` / `youtube a mp4`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng đã nêu ở trên.

### Sai intent hoàn toàn

- **`texttomp3` và mọi cụm TTS** (`texto a voz`, `convertir texto a audio`, `leer texto en voz alta`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. Đã loại khỏi danh sách keyword ở mục lỗi dữ liệu.
- **`activar subtitulos en youtube` / `poner subtitulos en youtube`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link** — nhiều nhất dự án. Thứ tự và vai trò:

| Link | Anchor (es) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/es/download-youtube-transcript` | Descargar transcripción de YouTube | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/es/youtube-subtitle-downloader` | Descargador de subtítulos de YouTube | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/es/youtube-video-summarizer` | Resumidor de videos de YouTube | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho es.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/es/...)`, đổi path sang `/es/`.
- Thuật ngữ khớp các trang es đã duyệt: `marcas de tiempo` (timestamps), `separación de hablantes` (speaker separation), `archivo` (file), `enlace` (link), `navegador` (browser), `sin registro` (no sign-up), `detectado automáticamente` (auto-detected).
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ.
- **Kiểm tra bắt buộc trước khi bàn giao:**
  1. `python3 shape_check.py en.json es.json` → phải in `es.json -> True`.
  2. `grep -o 'descargar[^.]\{0,40\}video'` → **0 kết quả**.
  3. `grep -c 'texttomp3'` → **0**.
  4. 4 path internal link đúng `/es/` prefix, đủ 4, không thừa không thiếu.
