🔥 TranscriptX – TikTok Caption Downloader (French / fr)

URL:
/fr/tiktok-caption-downloader

Intent chính:

Télécharger les sous-titres TikTok dưới dạng file có timecode (miễn phí)

Trang này nhắm đến người dùng Pháp muốn **tải file sous-titres** của một video TikTok công khai — file có mốc thời gian từng dòng — để gắn lại lên video khi republier, để dịch sang ngôn ngữ khác, hoặc để đáp ứng nhu cầu accessibilité.

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/fr/instagram-caption-downloader`.**
>
> Dù tên gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/fr/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (`légende`, hashtag, emoji) | Lời **NÓI** trong video |
> | Kết quả | Đoạn text đọc được | **File `sous-titres` có timecode** |
> | Từ khóa trục | `légende` | `sous-titres` |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram, từ **`sous-titre` bị cấm tuyệt đối** (grep = 0) vì caption ở đó là chữ viết — trang đó dùng `légende` 44 lần. **Ở trang này thì ngược lại: `sous-titres` CHÍNH LÀ keyword chính** — 11/11 keyword tiếng Pháp đều chứa cụm `sous titres`. Đừng áp nhầm quy tắc của trang kia.

> ⚠️ **Phân định với `/fr/tiktok-transcript` — trục TIMING, KHÔNG phải viết-vs-nói.** Cả hai trang đều lấy lời NÓI từ audio. Khác nhau ở chỗ: trang này ra **fichier de sous-titres synchronisé** để chạy đè lên video; trang transcript ra **texte brut** để đọc/copy. Bản EN cài sẵn 3 chốt chặn — **section 2** (cả section dành riêng để phân định, có internal link), **FAQ 3** ("What is the difference between TikTok captions and a transcript?"), và **section 1 đoạn 2**. Giữ nguyên cả ba, dịch sát, không rút gọn.

---

## 🚫 Quyết định riêng của bản fr: CẤM HOÀN TOÀN từ `légende`

**`grep -c "légende" fr.json` phải bằng 0.**

Lý do: `légende` là từ trục của `/fr/instagram-caption-downloader` (nơi nó nghĩa là *chú thích tác giả gõ dưới bài*). Nếu trang này cũng dùng `légende` để dịch `captions`, Google sẽ thấy hai trang cùng site tranh nhau một cụm mà thực chất phục vụ hai intent hoàn toàn khác → cannibalization + nhiễu ngữ nghĩa cho chính người đọc Pháp (họ hiểu `légende` là chữ viết, không phải chữ chạy trên video).

Giải pháp: **mọi lần bản EN dùng `caption` hoặc `subtitle` đều dịch thành `sous-titres`** (hoặc biến thể chống lặp bên dưới). Tiếng Pháp vốn không phân biệt caption/subtitle như tiếng Anh trong bối cảnh video ngắn — `sous-titres` phủ cả hai, và đó cũng đúng là từ người Pháp gõ vào Google.

### Chống lặp `sous-titres` (vì chỉ có một từ cho hai khái niệm EN)

Bản EN xen kẽ `captions` / `subtitles` để đỡ lặp. Bản fr không có lựa chọn đó, phải chống lặp bằng biến thể cấu trúc:
`fichier de sous-titres` · `lignes de sous-titres` · `sous-titrage` · `texte synchronisé` · `le fichier` · `sous-titrer` (động từ).

### Biến thể số ít / số nhiều đều có keyword

`telecharger sous titre tiktok` (số ít, 10–100) và `telecharger sous titres tiktok` (số nhiều, 0–10) là **hai keyword riêng biệt và cụm SỐ ÍT có volume cao hơn**. Vì thế bản fr cố ý để tồn tại cả hai dạng: dạng số nhiều `les sous-titres` làm trục chính (đúng ngữ pháp Pháp), nhưng có ít nhất một chỗ dùng dạng số ít tự nhiên (`un fichier de sous-titre`… → thực tế dùng `chaque ligne de sous-titre`, `une piste de sous-titre`) để phủ luôn biến thể singulier mà không viết sai chính tả.

---

## Từ khóa chính

telecharger sous titre tiktok (10–100) ✅ *đã search* → viết đúng chính tả: **télécharger les sous-titres TikTok**

Đồng hạng: `sous titres tiktok` (10–100) ✅ — head term danh từ, dùng làm neo cho H2 section 4/5.

---

## Từ khóa phụ

### Nhóm Télécharger (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| telecharger sous titre tiktok | 10–100 | ✅ đã search *(KW chính)* |
| telecharger sous titres tiktok | 0–10 | ✅ đã search |
| telecharger les sous titres d une video tiktok | 0–10 | ✅ đã search |
| comment telecharger les sous titres tiktok | 0–10 | ✅ đã search *(dùng cho quickAnswer + FAQ 1)* |
| telecharger sous titres tiktok en ligne | 0–10 | ✅ đã search |
| telecharger le texte d une video tiktok | 0–10 | ⚠️ đã search nhưng **hạ trọng số** — xem ghi chú |

### Nhóm Extraire / Récupérer

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| extraire les sous titres tiktok | 0–10 | ✅ đã search |
| recuperer sous titres tiktok | 0–10 | ✅ đã search |

### Nhóm Enregistrer

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| enregistrer sous titres tiktok | 0–10 | ✅ đã search |

### Nhóm Fichier / Danh từ (phủ head term)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| sous titres tiktok | 10–100 | ✅ đã search |
| sous titres tiktok fichier | 0–10 | ✅ đã search → viết thành `fichier de sous-titres TikTok` |
| sous-titres de vidéo TikTok | — | 🔄 dịch bổ sung (tiktok video captions) |
| fichier SRT TikTok | — | 🔄 dịch bổ sung (SRT file) |
| traduire les sous-titres TikTok | — | 🔄 dịch bổ sung (translate subtitles) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

> ⚠️ **Ghi chú về `telecharger le texte d une video tiktok`.** Cụm này nằm sát intent transcript (`texte` = texte brut). Chỉ dùng **một lần duy nhất**, trong section 2 item 1 hoặc section 1, và **luôn kèm bổ ngữ `synchronisé` / `avec les temps`** để không kéo nhầm truy vấn của `/fr/tiktok-transcript` về đây. Không đặt vào title/H1/H2.

> ⚠️ **11/11 keyword đều chứa `sous titres`, và chỉ 2 cụm đạt 10–100.** Không có cụm nào áp đảo. Chiến lược: **phủ đều 4 nhóm động từ** (télécharger / extraire / récupérer / enregistrer), mỗi nhóm chiếm ít nhất một vị trí neo trong body, `télécharger` giữ title + H1 + conclusion.

---

## Search Intent

Người dùng Pháp thấy một video TikTok và cần **fichier de sous-titres** của nó — không phải để đọc, mà để **dùng lại**:

- Republier clip lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có sous-titres.
- Traduire sous-titres sang tiếng Pháp hoặc ngôn ngữ khác rồi gắn lại.
- Sửa lại sous-titres automatiques của TikTok vốn hay sai accent, sai liaison.
- Làm sous-titrage cho người sourd et malentendant.

Họ kỳ vọng:

- Coller un lien là ra file, không cần đăng nhập TikTok.
- File có **timecode từng dòng**, mở được bằng logiciel de montage.
- Chạy được cả khi video gốc **không bật sous-titres**.
- Sửa được chữ trong file trước khi dùng.
- Gratuit, en ligne, sans inscription.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Pháp chỉ có một từ `sous-titres` cho cả `captions` lẫn `subtitles`.** Bản EN dùng hai từ xen kẽ để đỡ lặp (`captions` ở H1, `subtitles` ở section 4). Bản fr phải chống lặp bằng biến thể cấu trúc (`fichier de sous-titres`, `lignes de sous-titres`, `sous-titrage`, động từ `sous-titrer`) chứ không đổi được từ vựng.
2. **Bản fr phải chủ động tránh `légende`, bản EN không có ràng buộc này.** Đây là ràng buộc SEO nội bộ site (tránh ăn thịt `/fr/instagram-caption-downloader`), không phải vấn đề dịch thuật. Bản EN dùng `captions` thoải mái vì trang Instagram EN dùng `caption` theo nghĩa khác nhưng không đụng `subtitle`.
3. **Volume tiếng Pháp thấp hơn EN hai bậc** (10–100 so với 1K–10K). Vì thế bản fr không dồn lực vào một cụm head duy nhất mà rải đều 4 nhóm động từ — mỗi truy vấn long-tail đều có một câu khớp gần đúng, thay vì tối ưu dày một cụm như bản EN làm với `tiktok caption downloader`.
4. **Nỗi lo `sous-titres automatiques` sai tiếng Pháp là điểm bán hàng riêng.** Auto-caption của TikTok nuốt accent (é/è), sai élision và liaison trong tiếng Pháp nói nhanh. Bản EN chỉ nói `shaky auto-captions` chung chung — bản fr nhấn đúng nỗi đau này ở section 4 item 3, **trong đúng câu đã có sẵn**, không thêm câu.
5. **Xưng hô `vous`**, nhất quán với `/fr/instagram-transcript` và các trang Pháp khác trong repo. Bản EN dùng `you` trung tính.

---

## Đối tượng người dùng

- Créateurs de contenu re-upload / compilation clip TikTok
- Monteurs vidéo, freelances en montage
- Người cross-post TikTok sang Reels / YouTube Shorts
- Traducteurs / sous-titreurs làm sub cho khán giả Pháp ngữ
- Community managers chạy nội dung đa ngôn ngữ
- Người làm nội dung accessible cho người sourd et malentendant
- Người muốn sửa sous-titres automatiques sai accent của TikTok

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `fr.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content` (S1 = 3, S5 = 2), đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, `conclusion` 2 đoạn. Keyword áp bằng **cách chọn từ ngữ khi dịch**.

| # | H2 (fr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Télécharger les sous-titres TikTok | telecharger sous titre tiktok *(KW chính)* |
| — | **quickAnswer** | comment telecharger les sous titres tiktok |
| 1 | Ce que fait cet outil de téléchargement de sous-titres TikTok | telecharger sous titres tiktok, sous titres tiktok |
| 2 | Sous-titres ou transcription : de quoi avez-vous besoin ? | *(phân định TIMING + internal link `/fr/tiktok-transcript`)* |
| 3 | Comment télécharger les sous-titres d'une vidéo TikTok | comment telecharger les sous titres tiktok, telecharger les sous titres d une video tiktok |
| 4 | Ce que vous pouvez faire avec un fichier de sous-titres TikTok | sous titres tiktok fichier, sous titres tiktok |
| 5 | Télécharger les sous-titres TikTok en plus de 100 langues | traduire les sous-titres tiktok, sous titres tiktok |
| 6 | Questions fréquentes | sous titres tiktok + long-tail (extraire / récupérer / enregistrer) |
| — | **conclusion** | telecharger sous titre tiktok, gratuit |

### Ghi chú riêng cho bản fr (KHÔNG tạo section mới)

- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho trục TIMING. Dịch đủ 2 item, giữ link `[TikTok Transcript](/fr/tiktok-transcript)` ở item 2. Item 1 = "khi chữ chạy trên video → sous-titres", item 2 = "khi chỉ cần đọc → texte brut".
- **FAQ 3** là chốt thứ hai (`Quelle différence entre les sous-titres TikTok et une transcription ?`) — dịch sát, không rút gọn, nhắc lại tên công cụ TikTok Transcript.
- **Section 1 đoạn 2** là chốt thứ ba — câu giải thích "chính timing là lý do trang này tách riêng khỏi trang transcript". Giữ nguyên độ dài.
- Nhóm động từ `extraire` / `récupérer` / `enregistrer` được rải vào **section 1 đoạn 1**, **section 3 step 4**, và **FAQ**, trong các câu vốn đã có — không thêm câu mới.
- Nỗi lo sous-titres automatiques sai accent xử lý **trong câu đã có** ở section 4 item 3.
- `telecharger le texte d une video tiktok` chỉ chạm **một lần**, ở section 2 item 1, luôn kèm `synchronisé`.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `transcription tiktok` / `convertir une video tiktok en texte` / `texte d'une video tiktok` (không kèm bổ ngữ synchronisé) → **/fr/tiktok-transcript** (texte brut, không timing). Đây là trang anh em gần nhất, dễ ăn thịt nhau nhất.
- `légende instagram` / `telecharger legende instagram` → **/fr/instagram-caption-downloader** (légende écrite tác giả gõ dưới bài, khác hẳn). Từ `légende` **cấm xuất hiện** trong `fr.json` này.
- `sous titres youtube` / `transcription youtube` → **/fr/youtube-transcript**
- **Nhóm tải VIDEO** — `télécharger vidéo tiktok`, `telecharger tiktok sans filigrane`, `tiktok sans watermark`, `enregistrer video tiktok` → **intent tải VIDEO**, SERP toàn downloader vidéo. Trang này tải **fichier de sous-titres**, không tải video.
  > **Quy tắc cứng:** động từ `télécharger` / `enregistrer` chỉ được đi với tân ngữ `sous-titres` / `fichier` / `texte`, **KHÔNG BAO GIỜ** với `vidéo`. Chuỗi `télécharger la vidéo`, `télécharger une vidéo`, `enregistrer la vidéo` không được phép xuất hiện ở bất kỳ đâu trong `fr.json`.
- `activer les sous-titres sur tiktok` / `mettre des sous-titres sur tiktok` → hướng dẫn thao tác trong app, không phải công cụ tải file.

---

## Internal linking

- ↔ /fr/tiktok-transcript (khi user chỉ cần texte brut để đọc, không cần timing) — link quan trọng nhất, nằm ở **section 2 item 2**, nhắc lại bằng tên (không link) ở **FAQ 3**
- Trang này là điểm đến ngược lại của `/fr/instagram-transcript` (vốn đã link sang `/fr/tiktok-transcript`)

---

## Ghi chú kỹ thuật cho fr.json

- Xưng hô **`vous`**, nhất quán với `/fr/instagram-transcript` và các trang Pháp khác trong repo.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT**.
- Cấu trúc: **6 section**, **8 FAQ**; section 1 = `content` **3 đoạn**; section 2 = `intro` 1 + `items` 2; section 3 = `steps` 4; section 4 = `intro` 1 + `items` 5; section 5 = `content` **2 đoạn**; `conclusion` = h2 + `content` 2 đoạn.
- Internal link section 2 item 2 giữ cú pháp markdown: `[TikTok Transcript](/fr/tiktok-transcript)`.
- **Kiểm tra bắt buộc trước khi giao:** `grep -c "légende" fr.json` → phải bằng **0**.
- **Kiểm tra bắt buộc:** không có chuỗi `télécharger la vidéo` / `télécharger une vidéo` / `enregistrer la vidéo`.
- Tránh lặp `sous-titres` quá dày: dùng xen kẽ `fichier de sous-titres`, `lignes de sous-titres`, `sous-titrage`, `le fichier`, động từ `sous-titrer`.
- Dùng dấu nháy đơn cong `'` (apostrophe typographique) nhất quán như `/fr/instagram-transcript`.
- Espace insécable trước `?` và `:` không bắt buộc trong JSON — dùng espace thường như file Instagram fr đã làm.
