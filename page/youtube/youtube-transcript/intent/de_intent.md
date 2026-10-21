🔥 TranscriptX – YouTube Transcript (German / de)

URL:
/de/youtube-transcript

Intent chính:

youtube transkript / YouTube Video transkribieren — lấy toàn văn lời nói của video YouTube dưới dạng chữ, online, miễn phí

Trang này nhắm đến người dùng nói tiếng Đức muốn **lấy toàn bộ nội dung nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán link là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này là **hub** nên **giữ trọn họ từ transcript**: `Transkript`, `transkribieren`, `Transkription`, **và cả nhóm `Text extrahieren` / `in Text umwandeln`**.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ 13 keyword trong danh sách `## German (de)` đều thuộc về trang này, kể cả `youtube video zu text`, `youtube video in text umwandeln`, `youtube in text umwandeln` — vì **tất cả đều có chữ `youtube`**, nên không đụng trang generic `/de/video-to-text`.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

- **Section 11 (`Kopieren, bearbeiten, übersetzen oder herunterladen`)** — chứa cả **4 internal link**, là chốt phân định chính. Dịch sát, không rút gọn, không bỏ vế nào.
- **FAQ 10** (`Transkript` vs `SRT/VTT`) — chốt với `/de/youtube-subtitle-downloader`.
- **FAQ 4** (`erstellen` vs `extrahieren`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một URL thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU HỆ THỐNG — ĐÃ KIỂM, SECTION `de` SẠCH

Đã kiểm section `## German (de)` trong `2_loc_kw.md` theo đúng tiền lệ bản `es` (bản `es` dính 4 dòng rác: `Keyword ideas`, `Keywords you provided`, `texttomp3`, `youtube subito texto`).

| Loại lỗi cần kiểm | Kết quả ở section `de` |
| ----------------- | ---------------------- |
| Dòng nhãn `Keyword ideas` | ❌ **không có** |
| Dòng nhãn `Keywords you provided` | ❌ **không có** |
| Cụm TTS `texttomp3` (intent ngược) | ❌ **không có** |
| Cụm garbled / sai chính tả | ❌ **không có** |

> ⚠️ Lỗi export hệ thống này có ở `## Spanish (es)`, `## French (fr)` và `## Vietnamese (vi)` của cùng file. Section `de` **không bị nhiễm** — không phải loại dòng nào.

### 📊 Số keyword thực: **13 / 13** (0 dòng bị loại)

---

## ⚠️ MỤC RIÊNG CHO BẢN DE: BẪY BIGRAM `Video herunterladen`

Đây là rủi ro **chỉ tiếng Đức mới có**, nặng hơn hẳn bản `es` (bản `es` chỉ phải tránh `descargar el video` — một cụm đứng liền nhau, dễ kiểm soát).

### Cơ chế gây lỗi

Tiếng Đức có **động từ tách được** (`herunter|laden`) cộng với **trật tự đẩy động từ về cuối mệnh đề** (mệnh đề phụ, câu có động từ tình thái, thể `zu`-Infinitiv). Hệ quả: danh từ `Video` bị đẩy ra sát ngay trước `herunterladen` và tạo ra bigram **`Video herunterladen`** — chính là intent tải file MP4 — **ngay cả trong câu không hề nói gì về việc tải video**.

Ví dụ câu vô hại nhưng sinh bigram sai:
- ✗ `…bevor du das Video herunterladen musst.`
- ✗ `…ohne dass du zuerst ein Video herunterladen musst.`

Cụm `youtube video herunterladen` trong tiếng Đức là cụm khổng lồ, SERP toàn downloader MP4. Một bigram lọt vào cũng đủ kéo trang lệch intent.

### Kỷ luật cứng đã áp

`herunterladen` / `Herunterladen` **chỉ được đi với** `Transkript`, `Text`, `Datei`. **Không bao giờ** với `Video`.

Bản EN câu S3 bước 2 nói *"no file to download first"* → dịch thành **`vorher auch keine Datei herunterladen`** (giữ `Datei`, tuyệt đối không dùng `Video`).

### Kết quả grep trên `de.json` (bắt buộc = 0 cả 3 dạng)

| Dạng | Số kết quả |
| ---- | ---------- |
| `Video herunterladen` | **0** ✅ |
| `Video heruntergeladen` | **0** ✅ |
| `Video downloaden` | **0** ✅ |

Toàn bộ 4 lần xuất hiện của `herunterlad*` trong `de.json`:
1. S3 bước 2 — `keine Datei herunterladen` ✅
2. S11 h2 — `Kopieren, bearbeiten, übersetzen oder herunterladen` (không có tân ngữ) ✅
3. S11 — `wenn das Herunterladen dein Hauptziel ist` (danh từ hóa, không tân ngữ) ✅
4. S11 — anchor `[YouTube Transkript herunterladen]` ✅ (đi với `Transkript`)

---

## ✅ LỢI THẾ RIÊNG CỦA TIẾNG ĐỨC: `Untertitel` ≠ `Transkript`

Khác hẳn tiếng Anh (`transcript` / `captions` / `subtitles` chồng lấn) và tiếng Tây Ban Nha (bản `es` phải dùng định ngữ `subtítulos automáticos` / `subtítulos del creador` để tránh nhập nhằng), tiếng Đức **tách bạch hoàn toàn**:

- `Transkript` = văn bản để đọc riêng — **kết quả của trang này**.
- `Untertitel` = chữ khớp giờ hiện lên khi phát — **thuộc trọn `/de/youtube-subtitle-downloader`**.

Vì tách bạch sẵn, bản `de` **không cần cơ chế định ngữ** như bản `es`. Chỉ cần kỷ luật vị trí:

**`Untertitel` KHÔNG được lên bất kỳ heading nào** (`h1` / `h2` / `h3` / `q`). Grep xác nhận: **0 hit trên heading** ✅.

Bốn chỗ duy nhất `Untertitel` xuất hiện, tất cả đều trong body hoặc nhãn spec:
1. **S2 spec label** `Funktioniert ohne Untertitel` — nhãn bảng thông số, không phải heading. Đây là dòng spec riêng của trang này (bản EN: *Works when the video has no captions*).
2. **S4** `automatisch erzeugte Untertitel sind oft fehlerhaft` — nói về auto-caption của YouTube, đúng ngữ cảnh.
3. **S11** `Brauchst du gezielt die Untertiteldatei` — câu trỏ sang `/de/youtube-subtitle-downloader`.
4. **FAQ 10** — câu trả lời phân định `Transkript` vs `Untertitel`, đồng thời gánh keyword `youtube untertitel als text`.

Ở mọi chỗ khác, kết quả của trang **luôn gọi là `Transkript` hoặc `Text`**.

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube tiếng Đức**: dán link video YouTube công khai → TranscriptX đọc phần âm thanh → trả về **toàn văn lời nói dưới dạng chữ** trong hơn 100 ngôn ngữ, tách từng người nói, `Zeitstempel` tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **holen / bekommen** — lấy `Transkript` có sẵn,
- **erstellen / generieren** — dựng `Transkript` từ âm thanh khi video không có textspur,
- **extrahieren / umwandeln** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

---

## Từ khóa chính

**youtube transkript (1K–10K)** ✅ *đã search* → **H1**

Đặt ở `title`, `h1`, `ogTitle`, `quickAnswer.question`, H2 của S1 / S2 / S10, `conclusion.h2` và FAQ 1–2.

**Lưu ý cấu trúc:** khác bản `es` (nơi động từ `transcribir` vượt danh từ nên phải đặt động từ làm H1), tiếng Đức có **danh từ `Transkript` và động từ `transkribieren` ngang bậc, cùng 1K–10K**. Vì vậy bản `de` **giữ nguyên cấu trúc danh từ của bản EN cho H1** (`YouTube Transkript`), và cấp trọn H2 của S3 cho động từ (`So kannst du ein YouTube Video transkribieren`).

---

## Từ khóa phụ

### Nhóm `Transkript` (danh từ — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript | 1K–10K | ✅ đã search *(KW chính)* |
| transkript von youtube video | 100–1K | ✅ đã search |
| youtube transkript erstellen | 100–1K | ✅ đã search |
| transkript erstellen youtube | 10–100 | ✅ đã search |

### Nhóm `transkribieren` / `Transkription` (động từ + kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video transkribieren | 1K–10K | ✅ đã search |
| youtube transkription | 100–1K | ✅ đã search |
| youtube video verschriftlichen | 0–10 | ✅ đã search |

### Nhóm `in Text umwandeln` / `zu Text` (chuyển đổi — bắt buộc có chữ `youtube`)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video in text umwandeln | 100–1K | ✅ đã search |
| youtube video zu text | 100–1K | ✅ đã search |
| youtube in text umwandeln | 10–100 | ✅ đã search |
| youtube gesprochenes in text umwandeln | 0–10 | ✅ đã search |

### Nhóm `extrahieren` (rút chữ ra)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube text extrahieren | 10–100 | ✅ đã search |
| youtube untertitel als text | 10–100 | ✅ đã search *(chỉ dùng ở FAQ 10 — xem mục `Untertitel`)* |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| Sprechertrennung | — | 🔄 dịch bổ sung (speaker separation) |
| Zeitstempel | — | 🔄 dịch bổ sung (timestamps) |
| über 100 Sprachen | — | 🔄 dịch bổ sung (100+ languages) |
| ohne Anmeldung / kostenlos | — | 🔄 dịch bổ sung (no sign-up / free) |
| Exportformate | — | 🔄 dịch bổ sung (export formats) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng Đức muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán link YouTube, không phải tải gì về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu DE ⇄ EN rất nặng trong môi trường học thuật và doanh nghiệp.
- Hoạt động **cả khi video không có `Untertitel`** — kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, `Podiumsdiskussion`).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Danh từ và động từ ngang bậc, không lệch như bản `es`.** Bản EN xoay quanh danh từ `transcript`. Bản `es` phải lật sang động từ vì `transcribir` (10K–100K) vượt `transcripción` (1K–10K). Tiếng Đức thì `youtube transkript` và `youtube video transkribieren` **cùng 1K–10K** — nên bản `de` giữ danh từ ở H1 như EN, nhưng **bắt buộc cấp một H2 riêng cho động từ** (S3), điều bản EN không phải làm vì tiếng Anh dùng chung một từ gốc.

2. **`Untertitel` và `Transkript` tách bạch hoàn toàn — lợi thế mà EN không có.** Trong tiếng Anh `transcript` / `captions` / `subtitles` chồng lấn nghĩa, nên bản EN phải giải thích khác biệt bằng cả một FAQ dài. Tiếng Đức tách sẵn ở tầng từ vựng, nên bản `de` chỉ cần **kỷ luật vị trí** (`Untertitel` không lên heading) thay vì cơ chế định ngữ như bản `es`. Đổi lại, `youtube untertitel als text` (10–100) là keyword thật, phải gánh ở FAQ 10 chứ không được bỏ.

3. **Bẫy bigram `Video herunterladen` do ngữ pháp, không do chọn từ.** Bản EN không có rủi ro này (tiếng Anh không tách động từ, không đẩy động từ cuối câu). Bản `es` có rủi ro tương tự nhưng nhẹ hơn vì `descargar el video` là cụm liền, viết ra là thấy. Tiếng Đức tạo bigram **một cách tự động** qua trật tự từ, kể cả khi người viết không hề nghĩ đến việc tải video. Đây là ràng buộc cấu trúc riêng, phải grep sau khi viết.

4. **Nhóm `in Text umwandeln` là 4 keyword độc lập, EN chỉ có một trục.** Tiếng Đức tách `in Text umwandeln`, `zu Text`, `Text extrahieren`, `verschriftlichen` thành các cụm có volume riêng. Bản EN gộp hết vào `extract` / `video to text`. Bản `de` phải rải đủ 4 biến thể qua S5 và S7 body — nhưng **mọi biến thể bắt buộc kèm chữ `YouTube`**, vì trang generic `/de/video-to-text` đã giữ cụm không có `youtube`.

5. **Danh từ ghép tiếng Đức thay đổi cách đặt H2.** `Exportformate`, `Sprechertrennung`, `Zeitstempel`, `Untertiteldatei` là một từ. H2 tiếng Đức vì thế ngắn hơn EN ở cùng lượng nghĩa, nhưng `title` và `description` lại dài hơn — phải cắt gọn `seo.description` xuống ~160 ký tự thay vì dịch nguyên câu EN.

---

## Đối tượng người dùng

- Sinh viên, `Studierende` (biến `Vorlesung`, khóa học online thành ghi chú ôn thi)
- Giảng viên, giáo viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, `Podiumsdiskussion` — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script cho dataset hoặc prompt)
- Marketer đa ngôn ngữ DE ⇄ EN
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `de.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (de) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Transkript | youtube transkript *(KW chính)* |
| — | **quickAnswer** | youtube transkript |
| 1 | Was ist ein YouTube Transkript? | youtube transkript, transkript von youtube video |
| 2 | YouTube Transkript auf einen Blick *(`specs` × 10)* | youtube transkript |
| 3 | So kannst du ein YouTube Video transkribieren *(`steps` × 4)* | youtube video transkribieren |
| 4 | YouTube Transkript erstellen | youtube transkript erstellen, transkript erstellen youtube |
| 5 | YouTube Text extrahieren | youtube text extrahieren, youtube video in text umwandeln, youtube video zu text |
| 6 | Wofür ein YouTube Transkript nützlich ist *(`items` × 6)* | transkript von youtube video |
| 7 | YouTube Transkription in jeder Sprache | youtube transkription, youtube gesprochenes in text umwandeln, youtube in text umwandeln, youtube video verschriftlichen |
| 8 | TranscriptX im Vergleich zum eingebauten Transkript von YouTube *(`items` × 2)* | youtube transkript |
| 9 | Genauigkeit und was sie beeinflusst | *(E-E-A-T, không nhắm KW)* |
| 10 | Wann ein YouTube Transkript nicht funktioniert *(`items` × 5)* | youtube transkript |
| 11 | Kopieren, bearbeiten, übersetzen oder herunterladen | *(4 internal link — chốt phân định)* |
| 12 | Häufige Fragen *(12 FAQ)* | long-tail + toàn bộ biến thể đã search + youtube untertitel als text *(FAQ 10)* |
| — | **conclusion** *(3 đoạn)* | youtube transkript, kostenlos |

### Ghi chú riêng cho bản de (KHÔNG tạo section mới)

- **S2 tái dùng đúng 8/10 nhãn `specs` đã duyệt ở `/de/video-to-text/de.json`**: `Preis`, `Konto erforderlich`, `Installation`, `Sprachen`, `Sprechertrennung`, `Zeitstempel`, `Exportformate`, `Geräte` — copy nguyên văn cả nhãn lẫn giá trị ở những dòng không phụ thuộc định dạng file. Hai nhãn riêng của trang này thay cho `Limit für Dateigröße` và `Unterstützte Formate` của trang kia: **`Eingabe`** (Input — link YouTube) và **`Funktioniert ohne Untertitel`** (Works when the video has no captions).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Dịch sát, **không gộp lại**, vì mỗi section giữ một họ keyword riêng: S4 giữ `Transkript erstellen`, S5 giữ `Text extrahieren` + `in Text umwandeln`.
- **S8 là section so sánh** với transcript tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. `h3` item 1 = `Das eingebaute Transkript von YouTube` (không dùng `Untertitel`).
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn.
- **FAQ 3 và FAQ 10 đã đổi cách đặt câu hỏi** so với dịch sát nghĩa đen, để giữ luật `Untertitel` không lên heading:
  - EN FAQ 3 *"…if the video has no captions?"* → **`…wenn YouTube keinen Text zum Video anbietet?`**
  - EN FAQ 10 *"…transcript and subtitles?"* → **`…zwischen einem YouTube Transkript und SRT- oder VTT-Dateien?`** (từ `Untertitel` chuyển vào phần trả lời, nơi nó gánh luôn keyword `youtube untertitel als text`).
- Xưng hô **`du`** nhất quán (`füge ein`, `kopiere`, `bearbeite`, `dein Ziel`) — khớp `/de/download-youtube-transcript/de.json`, `/de/youtube-subtitle-downloader/de.json`, `/de/youtube-video-summarizer/de.json`. **Không trộn `Sie`.**
- Nhấn `kostenlos` ở `title`, `hero.subtitle` (dạng `ohne Konto`), S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`youtube transkript herunterladen` / `youtube transkript download`** → **`/de/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`youtube untertitel herunterladen` / `youtube srt download` / `youtube untertitel extrahieren`** → **`/de/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). Nhóm `Untertitel` để trần thuộc trọn về trang đó.
- **`youtube video zu text`**: giữ ở hub này — không còn trang riêng cho cách gọi "Video zu Text". Cụm `youtube video zu text` và nhóm `in Text umwandeln` cũng giữ ở đây vì đúng intent transcript.
- **`youtube video zusammenfassen` / `youtube zusammenfassung` / `youtube video summarizer`** → **`/de/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`video in text umwandeln` / `video zu text` / `video transkribieren`** (không có chữ `youtube`) → **`/de/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `Text` dùng ở trang này **bắt buộc phải có `YouTube`** trong cụm.
- **`audio in text umwandeln` / `audio transkribieren`** (không có `youtube`) → **`/de/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`youtube video herunterladen` / `youtube downloader` / `youtube zu mp4` / `youtube video downloaden`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Kỷ luật cứng + kết quả grep đã nêu ở mục bẫy bigram phía trên.

### Sai intent hoàn toàn

- **`texttomp3` và mọi cụm TTS** (`Text zu Sprache`, `Text vorlesen lassen`, `Text in Audio umwandeln`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. *(Section `de` của `2_loc_kw.md` không dính cụm này, nhưng vẫn ghi để tránh về sau.)*
- **`untertitel bei youtube einschalten` / `youtube untertitel aktivieren`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Anchor khớp đúng tên các trang `de` anh em đã duyệt:

| Link | Anchor (de) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/de/download-youtube-transcript` | YouTube Transkript herunterladen | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/de/youtube-subtitle-downloader` | YouTube Subtitle Downloader | Cần đúng **`Untertiteldatei`** SRT/VTT khớp giờ |
| `/de/youtube-video-summarizer` | YouTube Video Summarizer | Chỉ cần **ý chính**, không cần toàn văn |

> Ba anchor tiếng Anh (`YouTube Subtitle Downloader`, `YouTube Video to Text`, `YouTube Video Summarizer`) **giữ nguyên có chủ ý** — đúng anchor mà `/de/download-youtube-transcript/de.json`, `/de/youtube-subtitle-downloader/de.json` và `/de/youtube-video-summarizer/de.json` đang dùng để trỏ chéo nhau. Đổi sang tiếng Đức sẽ vỡ tính nhất quán anchor của cả cụm.

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây (`[YouTube Transcript](/de/youtube-transcript)`).

---

## Ghi chú kỹ thuật cho de.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/de/...)`, path prefix `/de/`.
- Thuật ngữ khớp các trang `de` đã duyệt: `Zeitstempel` (timestamps), `Sprechertrennung` (speaker separation), `Datei` (file), `Link` (link), `Browser` (browser), `ohne Konto` / `ohne Anmeldung` (no sign-up), `automatisch erkannt` (auto-detected), `Exportformate` (export formats), `Geräte` (devices).
- Viết `YouTube Video`, `YouTube Transkript` **tách hai từ, viết hoa cả hai** (dạng thương hiệu, cũng là dạng người dùng gõ khi search) — không viết `YouTube-Video` có gạch nối, vì bigram gạch nối không khớp truy vấn.
- Dùng dấu nháy Đức `„…"` cho trích dẫn trong S11 — nhất quán với các trang `de` khác.
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ.
- **Kiểm tra bắt buộc trước khi bàn giao — đã chạy, tất cả PASS:**
  1. `python3 shape_check.py en.json de.json` → **`de.json -> True`** ✅
  2. `grep -io 'Video herunterladen\|Video heruntergeladen\|Video downloaden'` → **0** ✅
  3. `Untertitel` trên `h1`/`h2`/`h3`/`q` → **0 hit** ✅ *(chỉ có ở 1 nhãn `specs` + 3 chỗ body, đúng thiết kế)*
  4. 4 path internal link đúng prefix `/de/`, đủ 4, không thừa không thiếu ✅
