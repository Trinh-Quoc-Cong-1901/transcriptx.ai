🔥 TranscriptX – Download YouTube Transcript (French / fr)

URL:
/fr/download-youtube-transcript

Intent chính:

Tải transcription video YouTube về máy (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Pháp muốn **tải bản transcription của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcription trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/fr/youtube-subtitle-downloader`.

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **`sous-titres` (file phụ đề khớp giờ cho editor) → `/fr/youtube-subtitle-downloader`**
> **`transcription` / `transcript` (tài liệu để đọc/lưu/nộp) → TRANG NÀY**

Căn cứ: bản EN section 6 đã tự định nghĩa ranh giới — *"if what you really need is a timed caption file for a video editor rather than a document, the YouTube Subtitle Downloader exports SRT and VTT instead"*. Trang này ra **tài liệu để đọc/lưu/nộp**; trang kia ra **file phụ đề cho phần mềm dựng phim**.

### Kết quả kiểm trùng với `../youtube-subtitle-downloader/2_loc_kw.md` (phần `## French (fr)`)

| Keyword trang này | Keyword trang kia | Mức trùng | Xử lý |
| ----------------- | ----------------- | --------- | ----- |
| `télécharger sous titres youtube en texte` (0–10) | `telecharger sous titres youtube` (100–1K) | ⚠️ **gần trùng — cùng head `sous-titres`** | **GIỮ LẠI** — có vế `en texte` neo rõ là muốn văn bản để đọc. Dùng ở body S2 (mục TXT), luôn kèm vế `en texte` |
| `récupérer transcription youtube` (10–100) | `recuperer sous titres youtube` (0–10) | ✅ khác head (`transcription` vs `sous-titres`) | Dùng tự do ở trang này |
| 9 keyword còn lại | — | ✅ không trùng | Dùng tự do |

**Trùng tuyệt đối: 0 cặp. Gần trùng: 1 cặp.** Bản fr sạch hơn hẳn bản vi, vì tiếng Pháp tách bạch tự nhiên `sous-titres` (phụ đề) và `transcription` (bản chép lời) — không có hiện tượng một từ dùng lẫn cho cả hai như `phụ đề` trong tiếng Việt.

### Neo đẩy đi (push-away anchor)

`télécharger les sous-titres YouTube` (~100–1K ở trang kia) là cụm mạnh nhưng **thuộc `/fr/youtube-subtitle-downloader`**. Xử lý: dùng **đúng 1 lần**, ở **section 6 đoạn 2**, ngay trong câu trỏ sang trang kia. Bắt tín hiệu keyword nhưng đẩy traffic sai intent về đúng trang thay vì giữ lại rồi bounce.

**Tuyệt đối không đặt `sous-titres` vào `title` / `h1` / `h2` / `description`.**

---

## ⚠️ MỤC RIÊNG: QUY TẮC DÙNG TỪ `sous-titres` TRONG BẢN fr

1. **Kết quả của trang này LUÔN gọi là `transcription` hoặc `texte`** — không bao giờ gọi là `sous-titres`. Người dùng tải về một *tài liệu*, không phải một *file phụ đề*.
2. Từ `sous-titres` chỉ được xuất hiện **đúng 2 chỗ** trong `fr.json`:
   - **S2, mục SRT** — buộc phải nhắc vì SRT vốn là định dạng phụ đề. Phải neo bằng cụm đầy đủ **`fichier de sous-titres synchronisés`** và đóng khung là *một trong bốn định dạng xuất*, không phải sản phẩm chính.
   - **S6 đoạn 2** — câu trỏ sang `/fr/youtube-subtitle-downloader`. Cũng neo bằng **`fichier de sous-titres synchronisés`**. Đây là chỗ duy nhất bắt tín hiệu cụm `télécharger les sous-titres YouTube`.
3. Cụm keyword `télécharger sous titres youtube en texte` được dùng ở **S2 mục TXT**, nhưng viết ở dạng có vế `en texte` (`télécharger les sous-titres YouTube en texte`) — vế này neo rõ intent "muốn chữ để đọc", không phải file cho editor.
4. **Không đặt `sous-titres` vào bất kỳ FAQ nào.** Bản EN có FAQ nhắc caption; bản fr giữ nguyên số FAQ (8) nhưng chuyển sang nói về `horodatages` / `SRT` thay vì `sous-titres`.

---

## 🚫 Kiểm lỗi dữ liệu nguồn

Đã rà phần `## French (fr)` của `2_loc_kw.md`:

- **KHÔNG có** dòng rác `Keyword ideas` / `Keywords you provided` (khác bản vi — bản vi dính 2 dòng này).
- **KHÔNG có** keyword hỏng, keyword lặp, hay keyword sai intent tải VIDEO.
- Keyword trong file viết **không dấu và không gạch nối** (`telecharger`, `sous titres`) — đây là dạng chuẩn hoá của công cụ search. Khi viết content phải dùng **chính tả đúng có dấu**: `télécharger`, `sous-titres`. Google khớp cả hai dạng.

**Số keyword thực: 11 dòng thô − 0 rác − 0 sai intent = 11 keyword.** Trong đó 1 cụm (`télécharger sous titres youtube en texte`) dùng hạn chế → **10 cụm dùng làm trục chính + 1 cụm neo hạn chế**.

---

## Từ khóa chính

**télécharger transcription youtube (100–1K)** ✅ *đã search*

Cụm mạnh nhất và cũng là **lõi chung** của 5 cụm đuôi dài khác (`... vidéo`, `... txt`, `... pdf`, `... gratuit`, và biến thể `transcript`), nên neo vào đây thì các đuôi dài tự phủ theo.

**H1 chốt: `Télécharger une transcription YouTube`** — giữ đủ 3 token `télécharger` + `transcription` + `YouTube` liền kề, và vẫn đúng ngữ pháp Pháp (`télécharger transcription youtube` trần trụi là sai ngữ pháp, không dùng được làm H1).

---

## Từ khóa phụ

### Nhóm Transcription (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| télécharger transcription youtube | 100–1K | ✅ đã search *(KW chính)* |
| récupérer transcription youtube | 10–100 | ✅ đã search |
| télécharger transcription vidéo youtube | 10–100 | ✅ đã search |
| exporter transcription youtube | 10–100 | ✅ đã search |
| enregistrer transcription youtube | 0–10 | ✅ đã search |
| télécharger transcript youtube | 0–10 | ✅ đã search *(biến thể mượn tiếng Anh)* |

### Nhóm Định dạng (đuôi dài)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| télécharger transcription youtube txt | 0–10 | ✅ đã search |
| télécharger transcription youtube pdf | 0–10 | ✅ đã search |
| télécharger transcription youtube gratuit | 0–10 | ✅ đã search |

### Nhóm Texte (thuần Pháp)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| télécharger le texte d'une vidéo youtube | 0–10 | ✅ đã search |

### Nhóm Sous-titres — dùng HẠN CHẾ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| télécharger sous titres youtube en texte | 0–10 | ✅ đã search — chỉ ở body S2 (mục TXT), luôn kèm vế `en texte` |
| télécharger les sous-titres youtube | 100–1K | ⚠️ **thuộc `/fr/youtube-subtitle-downloader`** — đúng 1 lần ở S6 đoạn 2, trong câu trỏ đi |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| télécharger transcription youtube en DOCX | — | 🔄 dịch bổ sung (DOCX) |
| enregistrer transcription youtube hors ligne | — | 🔄 dịch bổ sung (offline) |
| transcription youtube sans inscription | — | 🔄 dịch bổ sung (no sign-up) |
| télécharger transcription youtube sur mobile | — | 🔄 dịch bổ sung (device) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ **Volume trang này thấp hơn hẳn `/fr/video-to-text`.** Lý do: "télécharger une transcription" là nhu cầu hẹp hơn "convertir vidéo en texte". Không cố nhồi mật độ — chiến lược là **phủ đều 10 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Pháp **đã biết mình muốn transcription** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài extension.
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **hors ligne**.
- Miễn phí (`gratuit`), không giới hạn độ dài video.
- Nhận dạng tốt tiếng Pháp.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Pháp có 4 động từ cạnh tranh cho cùng một hành động.** Bản EN chỉ có `download`; bản fr có `télécharger` (100–1K), `récupérer` (10–100), `exporter` (10–100), `enregistrer` (0–10) — cả 4 đều là keyword riêng có volume. Phải phân bổ đều thay vì lặp `télécharger` khắp nơi: `télécharger` ở H1/title/S1/S3, `exporter` ở S7 (FAQ), `enregistrer` ở S4, `récupérer` ở S4/S5. Bản EN không có bài toán này.
2. **`transcription` là từ chuẩn, `transcript` chỉ là biến thể mượn yếu.** Ngược với bản vi (nơi `transcript` mượn tiếng Anh lại là dạng phổ biến nhất, 7/9 keyword). Ở fr, 8/11 keyword dùng `transcription`, chỉ 1 dùng `transcript`. → Toàn bài dùng `transcription`; `transcript` chỉ xuất hiện **1 lần** ở S1 như từ đồng nghĩa mượn.
3. **Ranh giới `sous-titres` / `transcription` rõ ràng sẵn trong tiếng Pháp**, nên không mất keyword mạnh như bản vi (bản vi phải nhường hẳn `tải phụ đề youtube` 100–1K). Bản fr giữ trọn cụm chính `télécharger transcription youtube` 100–1K. Đây là bản dịch **thuận lợi nhất** trong cụm 5 trang.
4. **Phải dập nhiễm intent tải VIDEO.** `télécharger vidéo youtube` có volume cực lớn ở Pháp và SERP toàn downloader. Quy tắc cứng: `télécharger` chỉ đi với `transcription` / `texte` / `fichier`, **KHÔNG BAO GIỜ với `vidéo`**. Câu "télécharger la transcription d'une vidéo YouTube" hợp lệ (tân ngữ là `transcription`), câu "télécharger une vidéo" thì không.
5. **Nhấn PDF mạnh hơn bản EN.** `télécharger transcription youtube pdf` là keyword riêng có thật; người dùng Pháp (sinh viên, hành chính) thường cần bản PDF để nộp/lưu hồ sơ.

---

## Đối tượng người dùng

- Sinh viên, nghiên cứu sinh (lưu transcription bài giảng, phỏng vấn vào thư mục đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX để làm tài liệu nội bộ, compte rendu)
- Người học ngoại ngữ (tải TXT đọc hors ligne)
- Người làm phụ đề cần bản nháp có timecode (SRT)
- Người cần đưa transcription vào công cụ khác yêu cầu upload file

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `fr.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (fr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Télécharger une transcription YouTube | télécharger transcription youtube *(KW chính)* |
| — | **quickAnswer** | comment télécharger une transcription youtube |
| 1 | Ce que le téléchargement d'une transcription vous apporte | télécharger transcription youtube, télécharger le texte d'une vidéo youtube, *transcript* (1 lần) |
| 2 | Quel format télécharger ? | télécharger transcription youtube txt *(TXT)*, télécharger sous titres youtube **en texte** *(TXT)*, télécharger transcription youtube pdf *(PDF)*, `fichier de sous-titres synchronisés` *(SRT — neo bắt buộc)* |
| 3 | Comment télécharger une transcription YouTube | télécharger transcription vidéo youtube, récupérer transcription youtube |
| 4 | Quand il vous faut le fichier, pas seulement le texte | enregistrer transcription youtube, récupérer transcription youtube |
| 5 | Télécharger des transcriptions dans plus de 100 langues | télécharger transcription youtube gratuit *(+ nhấn tiếng Pháp)* |
| 6 | Quand un autre outil convient mieux | ⚠️ **télécharger les sous-titres YouTube — đúng 1 lần, trong câu trỏ sang `/fr/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | Questions fréquentes | exporter transcription youtube, télécharger transcription youtube txt / pdf / gratuit + long-tail |
| — | **conclusion** | télécharger transcription youtube, gratuit |

### Ghi chú riêng cho bản fr (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp. Đây cũng là chỗ duy nhất cụm `télécharger les sous-titres YouTube` được xuất hiện, và phải neo bằng `fichier de sous-titres synchronisés`.
- Nỗi lo nhận dạng tiếng Pháp xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Pháp — **không thêm câu**.
- Từ `transcript` (mượn tiếng Anh) dùng đúng **1 lần** ở S1 làm từ đồng nghĩa. Nhiều hơn sẽ nghe như dịch máy.
- 4 động từ (`télécharger` / `récupérer` / `exporter` / `enregistrer`) phân bổ theo bảng map ở trên — không dồn hết vào `télécharger`.
- **Không để chuỗi `télécharger une vidéo` / `télécharger la vidéo` xuất hiện ở bất kỳ đâu.**

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`télécharger sous-titres youtube` / `telecharger sous titre youtube srt` / `extraire les sous titres youtube` / `telecharger fichier sous titres youtube`** → **/fr/youtube-subtitle-downloader** (file phụ đề khớp giờ cho editor). Xem quy tắc 1 lần ở trên.
- `transcription youtube` / `lire transcription youtube` / `obtenir transcription youtube` → **/fr/youtube-transcript** (đọc trên màn hình, không tải file).
- `résumer une vidéo youtube` / `résumé vidéo youtube` → **/fr/youtube-video-summarizer**.

### Nhóm tải VIDEO — loại tuyệt đối

- **`télécharger vidéo youtube` / `télécharger une vidéo youtube gratuitement` / `youtube downloader` / `télécharger mp4 youtube` / `télécharger vidéo youtube avec sous-titres`** → **intent tải VIDEO (file mp4)**, SERP toàn downloader video. Trang này tải **chữ**.
  Quy tắc cứng: `télécharger` luôn phải có tân ngữ `transcription` / `texte` / `fichier`.
- `ajouter des sous-titres sur youtube` / `créer des sous-titres youtube` → **hướng dẫn thao tác trong YouTube Studio** cho creator, không phải công cụ tải.
- `convertir vidéo en texte` (không có chữ youtube) → **/fr/video-to-text** (upload file từ máy, không dán link).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/fr/youtube-transcript` (chỉ muốn đọc/copy trên màn hình, không cần file)
- → `/fr/youtube-subtitle-downloader` (cần `fichier de sous-titres synchronisés` cho phần mềm dựng phim) — **đây là link quan trọng nhất, cũng là chỗ neo cụm `télécharger les sous-titres YouTube`**
- → `/fr/youtube-video-summarizer` (chỉ cần ý chính, không cần toàn văn)

---

## Ghi chú kỹ thuật cho fr.json

- Xưng hô **"vous"**, nhất quán với `/fr/video-to-text` và các trang Pháp khác trong repo.
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- Cấu trúc 1:1 với `en.json`: **7 section**, **8 FAQ**, S1 `content` 3 · S2 `intro` 1 + `items` 4 · S3 `steps` 4 · S4 `intro` 1 + `items` 5 · S5 `content` 2 · S6 `content` 2 · S7 `items` 8 · `conclusion.content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/fr/...`.
- Dùng dấu cách không ngắt trước `?` và `:` theo chuẩn typo Pháp là **không bắt buộc** — giữ nhất quán với `/fr/video-to-text` (có dùng ` ?`).
- **Tuyệt đối không để chuỗi `télécharger une vidéo` / `télécharger la vidéo` xuất hiện.**
- **Tuyệt đối không gọi kết quả trang này là `sous-titres`** — luôn là `transcription` hoặc `texte`.
