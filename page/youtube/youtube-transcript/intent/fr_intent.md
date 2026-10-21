🔥 TranscriptX – YouTube Transcript (French / fr)

URL:
/fr/youtube-transcript

Intent chính:

transcrire une vidéo YouTube / obtenir la transcription d'une vidéo YouTube en ligne, gratuitement

Trang này nhắm đến người dùng nói tiếng Pháp muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán link là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này là **hub** nên **giữ trọn họ từ `transcription` / `transcrire`**, **và cả nhóm `extraire le texte` / `en texte`**.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ **11 keyword đúng intent** trong danh sách `## French (fr)` đều thuộc về trang này, kể cả nhóm `convertir video youtube en texte` / `video youtube en texte` / `youtube en texte` — vì các cụm đó **có chữ `youtube`**, nên không đụng trang generic `/fr/video-to-text`.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **Section 11 (`Copier, modifier, traduire ou télécharger`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (`transcription` vs `sous-titres`) — chốt với `/fr/youtube-subtitle-downloader`.
- **FAQ 4** (`générer` vs `extraire`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — 4 DÒNG ĐÃ LOẠI

Danh sách `## French (fr)` trong `2_loc_kw.md` có **15 dòng nhãn keyword**, trong đó **4 dòng là rác hoặc sai intent**. Section `fr` dính **cả 3 loại lỗi** đã ghi nhận ở bản pilot `es`:

| Dòng | Volume | Lý do loại |
| ---- | ------ | ---------- |
| `Keyword ideas` | — | **Nhãn giao diện công cụ search**, không phải keyword. Bị copy nhầm khi export. |
| `Keywords you provided` | — | **Nhãn giao diện công cụ search**, không phải keyword. Cùng nguyên nhân. |
| `texttomp3` | 10 – 100 | **Công cụ text-to-MP3 (TTS)** — biến chữ thành giọng nói. **Intent ngược hoàn toàn** với trang này (biến giọng nói thành chữ). Tuyệt đối không tối ưu. Dòng này lặp lại y hệt ở section `es` với cùng volume. |
| `texta youtube` | 10 – 100 | **Cụm garbled.** `texta` không tồn tại trong tiếng Pháp — nhiều khả năng là lỗi OCR/typo của `texte` hoặc rác từ cùng đợt export đã sinh ra `texttomp3`. Không có intent xác định. Tương đương `youtube subito texto` bên `es`. |

> ⚠️ Hai dòng `Keyword ideas` / `Keywords you provided` xuất hiện ở cả `es`, `fr` và `vi` — đây là **lỗi export hệ thống**, phải loại ở mọi ngôn ngữ.

### 📊 Số keyword thực: **15 − 4 = 11**

---

## 📌 QUY TẮC DÙNG TỪ `sous-titres` (mục riêng — bắt buộc)

Đây là quy tắc quan trọng nhất của bản `fr`, vì `sous-titres` là từ dễ tràn sang trang `/fr/youtube-subtitle-downloader` nhất.

**1. Kết quả của trang này LUÔN gọi là `transcription` hoặc `texte`.** Không bao giờ gọi kết quả là `sous-titres`.

**2. `sous-titres` chỉ được dùng trong 3 vai trò:**

| Vai trò | Vị trí trong `fr.json` | Cách viết |
| ------- | ---------------------- | --------- |
| Caption có sẵn của YouTube / của người đăng | S2 (`specs` label), S4, S5, S8, S10 `intro`, FAQ 3, FAQ 4, `conclusion` | Có định ngữ: **`sous-titres automatiques`**, **`sous-titres du créateur`**, hoặc trong mệnh đề phủ định (`la vidéo n'a pas de sous-titres`) |
| Trỏ sang trang phụ đề | S11 — anchor `Téléchargeur de sous-titres YouTube` | Để trần, đúng 1 lần |
| Câu hỏi so sánh / phủ định trong FAQ | FAQ 3 (phủ định), FAQ 10 (so sánh) | Bám đúng bản EN — pilot `es` đã làm y hệt |

**3. `sous-titres` TUYỆT ĐỐI không xuất hiện trong `h1`, bất kỳ `h2` nào, hay bất kỳ `h3` nào.** Đã verify: 31 heading, 0 heading chứa `sous-titre`.

**4. Hệ quả cho S5:** bản EN đặt H2 là `YouTube Transcript Extractor`. Bản `fr` **không** dịch thành *"Extracteur de sous-titres YouTube"* (sẽ đụng trang subtitle) mà thành **`Extraire le texte d'une vidéo YouTube`** — vừa đúng ranh giới, vừa khớp keyword đã search `extraire le texte d une video youtube`.

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói, horodatages tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **obtenir / récupérer** — lấy transcription có sẵn,
- **générer** — dựng transcription từ audio khi video không có sous-titres,
- **extraire** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

---

## Từ khóa chính

**transcrire une video youtube (100–1K)** ✅ *đã search* → **H1**

Đây là cụm đứng đầu bậc volume cao nhất của tiếng Pháp trong danh sách (100–1K), và là cụm **duy nhất ở bậc đó thuộc trọn họ từ `transcrire`** — họ từ mà trang hub này giữ. Toàn bộ trang được xây quanh nó: xuất hiện ở `title`, `h1`, `ogTitle`, H2 của S2 và S3, `conclusion.h2` và `conclusion.content[2]`.

> Lưu ý phân bậc: tiếng Pháp **không có cụm nào vượt bậc 100–1K** (khác `es` có cụm 10K–100K). Bốn cụm cùng đứng bậc 100–1K là `transcrire une video youtube`, `convertir video youtube en texte`, `transcrire youtube en texte`, `video youtube en texte`. Chọn `transcrire une video youtube` làm KW chính vì nó **đúng họ từ trang hub giữ**; ba cụm còn lại được cấp H2 riêng ở S5 và S7 nên không mất giá trị.

---

## Từ khóa phụ

### Nhóm `transcrire` (động từ — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcrire une video youtube | 100–1K | ✅ đã search *(KW chính)* |
| transcrire youtube en texte | 100–1K | ✅ đã search |
| comment transcrire une video youtube | 10–100 | ✅ đã search |

### Nhóm `transcription` (danh từ — kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcription automatique youtube | 10–100 | ✅ đã search |
| recuperer la transcription youtube | 0–10 | ✅ đã search |
| obtenir la transcription d une video youtube | 0–10 | ✅ đã search |
| generateur de transcription youtube | 0–10 | ✅ đã search |

### Nhóm `en texte` / `extraire` (chuyển đổi + rút chữ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| convertir video youtube en texte | 100–1K | ✅ đã search |
| video youtube en texte | 100–1K | ✅ đã search |
| extraire le texte d une video youtube | 10–100 | ✅ đã search |
| youtube en texte | 10–100 | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| séparation des locuteurs | — | 🔄 dịch bổ sung (speaker separation) |
| horodatages | — | 🔄 dịch bổ sung (timestamps) |
| plus de 100 langues | — | 🔄 dịch bổ sung (100+ languages) |
| sans inscription / gratuit | — | 🔄 dịch bổ sung (no sign-up / free) |
| extracteur de script YouTube | — | 🔄 dịch bổ sung (youtube script extractor) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng Pháp muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán link YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu FR ⇄ EN rất nặng.
- Hoạt động **cả khi video không có sous-titres** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, bàn tròn).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Không có cụm nào áp đảo — volume tiếng Pháp phẳng, phải trải đều thay vì dồn.** Bản EN có `youtube transcript` ở bậc 1M–10M, áp đảo tuyệt đối mọi biến thể, nên toàn trang có thể dồn vào một cụm duy nhất. Tiếng Pháp có **4 cụm cùng đứng bậc 100–1K** và không cụm nào vượt lên. Hệ quả cấu trúc: không được nhồi `transcrire une vidéo YouTube` vào mọi H2 như bản EN nhồi `YouTube Transcript`; phải **cấp H2 riêng cho từng cụm** — `transcrire` giữ H1 + S2 + S3, `convertir … en texte` / `vidéo YouTube en texte` giữ S5, `transcrire YouTube en texte` giữ S7.

2. **Tiếng Pháp tách `transcrire` (động từ) và `transcription` (danh từ) thành hai họ có volume độc lập, tiếng Anh chỉ có một trục danh từ.** Bản EN xoay quanh danh từ `transcript` (`get/generate/extract a transcript`), động từ `transcribe` chỉ là biến thể. Tiếng Pháp thì `transcrire` mạnh hơn hẳn `transcription` ở bậc volume (100–1K so với 10–100 và 0–10). Vì vậy bản `fr` **đặt động từ làm H1** (`Transcrire une vidéo YouTube`) thay vì danh từ như EN — thay đổi cấu trúc thật, không phải dịch sát nghĩa đen. Danh từ `transcription` được giữ ở S1, S4, S10 và `conclusion`.

3. **`extract` của EN phải tách làm hai trong tiếng Pháp, và không được dịch bằng `sous-titres`.** Bản EN đặt H2 `YouTube Transcript Extractor` — một danh từ tác nhân gọn. Tiếng Pháp `extracteur` gần như không có volume, còn cụm thật người dùng gõ là **động từ** `extraire le texte d une video youtube` (10–100). Thêm nữa, dịch `extractor` thành *"extracteur de sous-titres"* sẽ đâm thẳng vào `/fr/youtube-subtitle-downloader`. Nên H2 của S5 phải là **`Extraire le texte d'une vidéo YouTube`**, và `extracteur` chỉ còn nằm trong body ở dạng `extracteur de script YouTube`.

4. **Cụm `comment` là intent riêng có volume thật.** `comment transcrire une video youtube` đạt 10–100 — một bậc rõ ràng. Bản EN không có "how to" nào tách bạch tương đương. Phải cấp trọn H2 của **section 3** (steps) và `quickAnswer.question`.

5. **Rủi ro cannibalization ngược từ nhóm tải VIDEO.** `télécharger une vidéo YouTube` trong tiếng Pháp là cụm khổng lồ, SERP toàn downloader MP4. Kỷ luật cứng: `télécharger` **chỉ** đi với `transcription` / `texte` / `fichier`, **không bao giờ** với `vidéo`. Bản EN không chịu áp lực này ở cùng mức.

6. **Nhóm `en texte` phải có chữ `youtube` mới được dùng.** Trang generic `/fr/video-to-text` đã hoàn thành và đang giữ `convertir une vidéo en texte` / `transcription vidéo en texte`. Bản `fr` của trang này chỉ được dùng các biến thể **có `youtube`** (`convertir video youtube en texte`, `video youtube en texte`, `youtube en texte`, `transcrire youtube en texte`). Bản EN không có ràng buộc này.

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến bài giảng, MOOC thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ FR ⇄ EN, thị trường Pháp / Bỉ / Thụy Sĩ / Québec / Bắc Phi Pháp ngữ
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `fr.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (fr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Transcrire une vidéo YouTube | transcrire une video youtube *(KW chính)* |
| — | **quickAnswer** | comment transcrire une video youtube |
| 1 | Qu'est-ce qu'une transcription YouTube ? | recuperer la transcription youtube, obtenir la transcription d une video youtube |
| 2 | Transcrire une vidéo YouTube en un coup d'œil *(`specs` × 10)* | transcrire une video youtube |
| 3 | Comment transcrire une vidéo YouTube *(`steps` × 4)* | comment transcrire une video youtube |
| 4 | Générateur de transcription YouTube | generateur de transcription youtube, transcription automatique youtube |
| 5 | Extraire le texte d'une vidéo YouTube | extraire le texte d une video youtube, convertir video youtube en texte, video youtube en texte, youtube en texte |
| 6 | À quoi sert une transcription YouTube *(`items` × 6)* | transcription youtube (rải body) |
| 7 | Transcrire YouTube en texte dans toutes les langues | transcrire youtube en texte |
| 8 | TranscriptX face à la transcription intégrée de YouTube *(`items` × 2)* | transcription automatique youtube |
| 9 | La précision et ce qui l'influence | *(E-E-A-T, không nhắm KW)* |
| 10 | Quand une transcription YouTube peut ne pas fonctionner *(`items` × 5)* | transcription youtube |
| 11 | Copier, modifier, traduire ou télécharger | *(4 internal link — chốt phân định)* |
| 12 | Questions fréquentes *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion** *(3 đoạn)* | obtenir la transcription d une video youtube, transcrire une video youtube, gratuit |

### Ghi chú riêng cho bản fr (KHÔNG tạo section mới)

- **S2 tái dùng đúng nhãn `specs` đã duyệt ở `/fr/video-to-text/fr.json`** khi nhãn trùng, chỉ đổi giá trị cho hợp YouTube: `Prix`, `Compte requis`, `Installation`, `Langues`, `Séparation des locuteurs`, `Horodatages`, `Formats d'export`, `Appareils`. Hai nhãn mới riêng của trang này: **`Entrée`** (Input — lien vidéo YouTube) và **`Fonctionne sans sous-titres automatiques`** (Works when the video has no captions).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại**, vì mỗi section giữ một họ keyword riêng của tiếng Pháp.
- **S8 là section so sánh** với transcription tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. H3 item 1 là `La transcription intégrée de YouTube`, **không** dùng `sous-titres`.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào.
- **Kỷ luật `télécharger`:** chỉ đi với `transcription` / `texte` / `fichier` / `TXT, DOCX, PDF, SRT, VTT`. **Không bao giờ** viết `télécharger la vidéo`. Cụ thể:
  - S3 bước 2 (EN: "no file to download first") → **`aucun fichier à télécharger au préalable`** — giữ `fichier`, không dùng `vidéo`.
  - S11 (EN: "if downloading is your main goal") → **`si votre objectif principal est de récupérer un fichier`** — dùng `récupérer un fichier` thay vì lặp `télécharger` sát cạnh `vidéo`.
- Xưng hô **`vous`** (`collez`, `copiez`, `modifiez`, `votre appareil`) — nhất quán với `/fr/video-to-text/fr.json`.
- Trong body viết **có dấu đầy đủ** (`vidéo`, `transcription automatique`); keyword không dấu trong `2_loc_kw.md` (`video`, `transcrire une video youtube`) chỉ là dạng người dùng gõ, Google khớp cả hai.
- Dùng **`modifier`** cho "edit" (không dùng `éditer`, vốn nghĩa là "xuất bản" trong tiếng Pháp chuẩn) — nhất quán với các trang fr đã duyệt.
- Nhấn `gratuit` / `gratuitement` ở `title`, `hero.subtitle` (qua `sans compte`), S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.
- Dùng guillemets Pháp **« … »** cho trích dẫn trong S11 (`« vidéo en texte »`).

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`télécharger transcription youtube` / `télécharger transcript youtube`** → **`/fr/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`télécharger sous-titres youtube` / `sous-titres srt youtube` / `extraire les sous-titres youtube`** → **`/fr/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho monteur). Nhóm `sous-titres` để trần thuộc trọn về trang đó.
- **`youtube vidéo en texte`**: giữ ở hub này — không còn trang riêng cho cách gọi "vidéo en texte". Các cụm `convertir video youtube en texte` / `video youtube en texte` / `youtube en texte` cũng giữ ở đây vì đúng intent transcript.
- **`résumer une vidéo youtube` / `résumé vidéo youtube` / `résumeur youtube`** → **`/fr/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`convertir une vidéo en texte` / `vidéo en texte` / `transcription vidéo` / `transcripteur vidéo`** (không có chữ `youtube`) → **`/fr/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `en texte` dùng ở trang này **bắt buộc phải có `youtube`** trong cụm.
- **`audio en texte` / `transcrire un audio`** (không có `youtube`) → **`/fr/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`télécharger une vidéo youtube` / `youtube mp4` / `convertisseur youtube mp4` / `télécharger youtube gratuit`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng đã nêu ở trên.

### Sai intent hoàn toàn

- **`texttomp3` và mọi cụm TTS** (`texte en voix`, `convertir texte en audio`, `synthèse vocale`, `lire un texte à voix haute`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. Đã loại khỏi danh sách keyword ở mục lỗi dữ liệu.
- **`texta youtube`** → cụm garbled, không có intent. Đã loại.
- **`activer les sous-titres sur youtube` / `mettre les sous-titres youtube`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Thứ tự và vai trò:

| Link | Anchor (fr) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/fr/download-youtube-transcript` | Télécharger une transcription YouTube | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/fr/youtube-subtitle-downloader` | Téléchargeur de sous-titres YouTube | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/fr/youtube-video-summarizer` | Résumeur de vidéos YouTube | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho fr.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/fr/...)`, đổi path sang `/fr/`.
- Thuật ngữ khớp các trang fr đã duyệt: `horodatages` (timestamps), `séparation des locuteurs` (speaker separation), `fichier` (file), `lien` (link), `navigateur` (browser), `sans inscription` (no sign-up), `détectées automatiquement` (auto-detected), `modifier` (edit).
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ.
- **Kiểm tra bắt buộc trước khi bàn giao — ĐÃ CHẠY, TẤT CẢ PASS:**
  1. `python3 shape_check.py en.json fr.json` → in **`fr.json -> True`** ✅
  2. `grep -oi 'télécharg[^.]\{0,45\}vidéo' fr.json` → **0 kết quả** ✅
  3. `grep -c 'texttomp3' fr.json` → **0** ✅
  4. `sous-titres` trong heading: quét 31 heading (`h1` + 12 `h2` + toàn bộ `h3` + `conclusion.h2`) → **0** ✅
  5. 4 path internal link đúng `/fr/` prefix, đủ 4, không thừa không thiếu ✅
