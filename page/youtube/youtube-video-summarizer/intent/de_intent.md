🔥 TranscriptX – YouTube Video Summarizer (German / de)

URL:
/de/youtube-video-summarizer

Intent chính:

YouTube Video zusammenfassen — bằng KI, miễn phí

Trang này nhắm đến người dùng nói tiếng Đức muốn **nắm ý chính của một video YouTube mà không phải xem hết** — dán link, KI đọc toàn bộ nội dung rồi trả về một bản tóm tắt ngắn gồm kết luận, các ý chính và những chi tiết cụ thể đáng nhớ.

---

## ✅ TRANG NÀY SẠCH XUNG ĐỘT VỚI 4 TRANG YOUTUBE KIA

Đã kiểm chéo toàn cụm 5 trang YouTube: **0 keyword trùng** với `youtube-transcript`, `download-youtube-transcript`, `youtube-subtitle-downloader` — ở **cả 13 ngôn ngữ**, bao gồm `de`.

Lý do: `zusammenfassen` là intent tách bạch hoàn toàn — người tìm muốn **ý chính**, không phải **toàn văn**. Không cần nhường hay neo đẩy đi cụm nào, khác hẳn cặp `download-transcript` ↔ `subtitle-downloader`.

**Ba chốt phân định phải giữ trong nội dung:**

1. **S1 đoạn 3** — bản EN: *"A transcript hands you every word; a summary decides which words were worth your time"*. Bản de dịch sát (`Ein Transkript reicht dir jedes einzelne Wort; eine Zusammenfassung entscheidet, welche Wörter deine Zeit wert waren`). Đây là chỗ duy nhất trong body được nhắc `Transkript` như một khái niệm đối lập.
2. **FAQ 4** — bản EN: *"What is the difference between a summary and a transcript?"*. Giữ nguyên câu hỏi đối lập, không đổi thành câu khác.
3. **S7** — chứa cả **3 internal link**, dịch sát cả 3 vế để mỗi link có lý do tồn tại rõ ràng.

Ngoài ba chỗ trên, từ `Transkript` không xuất hiện. Từ **`Untertitel` tuyệt đối không được dùng** — nó thuộc `/de/youtube-subtitle-downloader`.

---

## ⚠️ MỤC RIÊNG: BẪY BIGRAM `Video herunterladen` (đặc thù tiếng Đức)

Trang này **không tải gì cả** — nó **đọc và tóm tắt**. Nhưng tiếng Đức có một cái bẫy mà các ngôn ngữ khác trong dự án không có:

**Động từ tách được (trennbare Verben) và cấu trúc đẩy động từ về cuối mệnh đề** khiến tân ngữ `Video` bị đặt sát ngay trước `herunterladen`, tạo ra bigram `Video herunterladen` **một cách vô tình**, ngay cả khi ý câu hoàn toàn không nói về việc tải video. Ví dụ những câu rất tự nhiên nhưng phải loại bỏ:

- ❌ `…ohne das Video herunterladen zu müssen`
- ❌ `…wenn du das Video heruntergeladen hast`
- ❌ `…statt das Video downloaden zu müssen`

Mọi câu trên đều sinh đúng cụm mà SERP của nhóm **YouTube-Video-Downloader** đang chiếm. Ba dạng phải bằng **0**:

| Dạng cần grep | Yêu cầu |
| ------------- | ------- |
| `Video herunterladen` | = 0 |
| `Video heruntergeladen` | = 0 |
| `Video downloaden` | = 0 |

**Quy tắc viết:** tránh `herunterladen` làm động từ chính. Nếu buộc phải nhắc thì tân ngữ phải là `Transkript` hoặc `Datei`, không bao giờ là `Video`. Trong `de.json`, `herunterladen` chỉ xuất hiện **đúng một lần** — trong anchor text của internal link `[YouTube Transkript herunterladen](/de/download-youtube-transcript)` ở S7, nơi tân ngữ là `Transkript`.

Kết quả của trang này luôn gọi là **`Zusammenfassung`**, không bao giờ gọi là `Download` hay `Datei`.

---

## Lỗi dữ liệu trong `2_loc_kw.md` section `## German (de)`

Đã rà soát toàn bộ khối `## German (de)`:

- **Không có** dòng rác nhãn công cụ `Keyword ideas` / `Keywords you provided` (khác khối `fr` và `vi` — cả hai đều dính nhãn, riêng `vi` còn dính 8 cụm Minecraft).
- **Không có** keyword trùng lặp.
- **Không có** keyword sai intent. Cả 10 dòng đều là intent "tóm tắt video YouTube", không lẫn cụm tìm nội dung để xem, không lẫn cụm tải video.

**Số keyword thực: 10 − 0 nhãn − 0 trùng − 0 sai intent = 10 keyword.** Khối dữ liệu sạch, ngang chất lượng khối `es`.

> ⚠️ **Lưu ý về trần volume:** cụm mạnh nhất chỉ đạt `100 – 1K`, thấp hơn hẳn `es` (`10K – 100K`) và `vi` (`1K – 10K`). Thị trường Đức cho intent này nhỏ hơn nhiều, hoặc người Đức đang tìm bằng tiếng Anh (`youtube summarizer`). Không vì thế mà giảm độ sâu nội dung — nhưng đừng kỳ vọng traffic ngang các bản kia.

---

## Từ khóa chính

**youtube video zusammenfassen (100–1K)** ✅ *đã search*

Chọn dạng động từ làm KW chính vì: (a) khớp trực tiếp với hành động của công cụ, (b) là **lõi chung** của 4 cụm đuôi dài khác (`… ki`, `… kostenlos`, `… online`, `… lassen`), nên neo vào đây thì các đuôi tự phủ theo.

Cụm `youtube video zusammenfassen ki` cùng đạt `100 – 1K` và được xử lý như **KW chính thứ hai**, neo ở `title` + **H2 section 3**.

---

## Từ khóa phụ

### Nhóm `zusammenfassen` — trục động từ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video zusammenfassen | 100–1K | ✅ đã search *(KW chính)* |
| youtube video zusammenfassen kostenlos | 10–100 | ✅ đã search |
| youtube video zusammenfassen lassen | 10–100 | ✅ đã search |
| youtube zusammenfassen | 10–100 | ✅ đã search |
| youtube video zusammenfassen online | 0–10 | ✅ đã search |

### Nhóm `Zusammenfassung` — trục danh từ (kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video zusammenfassung | 10–100 | ✅ đã search |
| video zusammenfassung youtube | 0–10 | ✅ đã search |

### Nhóm KI / Công cụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube video zusammenfassen ki | 100–1K | ✅ đã search *(KW chính thứ hai)* |
| youtube zusammenfassung ki | 10–100 | ✅ đã search |
| youtube zusammenfassung tool | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| langes Video zusammenfassen | — | 🔄 dịch bổ sung (long video) |
| Podcast zusammenfassen | — | 🔄 dịch bổ sung (podcast) |
| Kernpunkte eines Videos | — | 🔄 dịch bổ sung (key points) |
| Vorlesung zusammenfassen | — | 🔄 dịch bổ sung (lecture) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng nói tiếng Đức gặp một video YouTube dài — Vorlesung, Podcast, Vortrag, Test 20 phút — và muốn **biết nó nói gì trong một phút** để quyết định có đáng xem hết không.

Họ kỳ vọng:

- Dán link là ra tóm tắt trong vài giây, không đăng nhập, không cài đặt.
- KI đọc **toàn bộ video**, không phải chỉ phần mô tả hay vài phút đầu.
- Bản tóm tắt đủ ngắn để đọc nhanh nhưng có **con số, tên riêng, khuyến nghị cụ thể**, không chung chung.
- Nhận dạng tốt tiếng Đức, kể cả giọng Áo và Thụy Sĩ.
- Miễn phí, không giới hạn độ dài video.
- Rõ ràng về quyền riêng tư và việc không cần tài khoản — thị trường Đức nhạy cảm hơn hẳn với chuyện đăng ký.

### Khác biệt so với bản tiếng Anh

1. **`KI` chứ không phải `AI`.** Và tín hiệu KI ở tiếng Đức **mạnh bất thường**: `youtube video zusammenfassen ki` đạt `100 – 1K`, **ngang chính KW chính**. Không ngôn ngữ nào khác trong dự án có cụm KI/AI ngang bằng KW chính như vậy (`es` chỉ `10 – 100`, `vi` `100 – 1K` nhưng dưới cụm chính một bậc). Vì thế `KI` phải vào `title` và **H2 section 3**, không được để chìm trong body.
2. **Cụm `zusammenfassen lassen` là dạng truy vấn riêng của tiếng Đức, bản EN không có tương đương.** Người Đức gõ *"video zusammenfassen **lassen**"* — cấu trúc sai khiến, nghĩa là "để cho ai/cái gì tóm tắt hộ". Nó phản ánh đúng mối quan hệ người dùng ↔ công cụ. Phải xuất hiện nguyên dạng ít nhất một lần trong body (đặt ở **S2 đoạn 2**) và một lần ở `ogDescription`.
3. **Bẫy bigram `Video herunterladen` do động từ tách được** — xem mục riêng phía trên. Đây là rủi ro kỹ thuật **chỉ tiếng Đức mới có**, bản EN/es/vi không cần grep loại này.
4. **Tiếng Đức có sẵn cặp động từ ↔ danh từ (`zusammenfassen` / `Zusammenfassung`) để luân phiên**, giống `es` (`resumir` / `resumen`) và khác `vi` (chỉ một từ `tóm tắt`). Đây là lợi thế chống lặp: mỗi lần luân phiên đều rơi vào một trong hai trục keyword. **Không** thay bằng `verdichten` / `komprimieren` / `kürzen` ở vị trí quan trọng — lệch keyword, chỉ dùng làm biến thể phụ trong body.
5. **Trần volume thấp hơn hẳn.** `es` có 2 cụm `10K – 100K`, `vi` có 1 cụm `1K – 10K`; `de` cao nhất chỉ `100 – 1K`. Hệ quả về chiến thuật: không có cụm nào đủ mạnh để "một mình gánh trang", nên phải phủ **rộng** cả 10 cụm thay vì dồn toàn lực vào một điểm neo duy nhất như bản `es`.
6. **Danh từ viết hoa.** `Zusammenfassung`, `Kernpunkte`, `Transkript`, `Video` luôn viết hoa theo chính tả Đức — kể cả khi keyword search ở dạng thường. Không hạ chữ thường trong body để "khớp keyword"; công cụ tìm kiếm chuẩn hóa chữ hoa/thường.

---

## Đối tượng người dùng

- Studierende và người đang học (quyết định một `Vorlesung` hay tutorial có đáng xem hết không, biến ý chính thành ghi chú ôn tập)
- Berufstätige (nắm nội dung `Vortrag`, hội thảo, phỏng vấn trong ngành giữa các cuộc họp)
- Người nghiên cứu (quét nhanh một loạt video để chọn ra vài cái đáng xem kỹ và trích dẫn)
- Content creator, marketer (rút thông điệp cốt lõi từ video dài để làm bài đăng, kịch bản)
- Người nghe podcast trên YouTube muốn nắm ý trước khi nghe trọn

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `de.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng 4 `steps`, đúng **4 `items`** ở S4 và S5, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (de) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Video zusammenfassen | youtube video zusammenfassen *(KW chính)* |
| — | **title** | youtube video zusammenfassen + ki + kostenlos |
| — | **description** | youtube video zusammenfassung *(trục danh từ)* |
| — | **schemaName** | youtube zusammenfassung tool |
| — | **quickAnswer** | youtube video zusammenfassen *(dạng câu hỏi "Wie kann ich…")* |
| 1 | Was dir eine Video-Zusammenfassung gibt | youtube video zusammenfassung, youtube zusammenfassung tool *(+ chốt phân định với Transkript)* |
| 2 | Warum zusammenfassen statt alles ansehen | youtube video zusammenfassen lassen |
| 3 | So kannst du ein YouTube Video mit KI zusammenfassen | youtube video zusammenfassen ki *(KW chính thứ hai)* |
| 4 | Was in einer guten Zusammenfassung steht | *(4 items — Kernaussage / Kernpunkte / konkrete Details / Aufbau)* |
| 5 | Für wen sich Zusammenfassungen lohnen | *(4 items — Studierende / Berufstätige / Recherchierende / Creator)* |
| 6 | Videos in über 100 Sprachen zusammenfassen | youtube video zusammenfassen online, youtube zusammenfassung ki *(+ nhấn tiếng Đức, Áo, Thụy Sĩ)* |
| 7 | Wenn du mehr brauchst als die Zusammenfassung | *(3 internal link — chốt phân định)* |
| 8 | Häufige Fragen | youtube video zusammenfassen kostenlos + long-tail |
| — | **conclusion** | youtube video zusammenfassen kostenlos, youtube zusammenfassen |

### Ghi chú riêng cho bản de (KHÔNG tạo section mới)

- **S1 đoạn 3 và FAQ 4 là hai chốt phân định với trang transcript** — dịch sát, không rút gọn. Đây là chỗ duy nhất được nhắc `Transkript` như khái niệm đối lập (cùng với S7).
- **S7 là chốt thứ ba**, chứa cả 3 internal link — dịch sát cả 3 vế.
- **Luân phiên `zusammenfassen` / `Zusammenfassung` có chủ đích.** Mỗi đoạn nên chạm ít nhất một trong hai dạng.
- **`zusammenfassen lassen` đặt ở S2 đoạn 2** — đây là chỗ hợp ngữ cảnh nhất (người dùng "để công cụ tóm tắt hộ" rồi quyết định có xem tiếp không). Không nhồi vào H1.
- **`KI` xuất hiện tối thiểu 4 lần**: `title`, `H2 S3`, `step 2 của S3`, `S1 đoạn 2`. Luôn viết hoa hai chữ `KI`, không `AI`, không `A.I.`.
- Nỗi lo nhận dạng tiếng Đức xử lý **trong S6**, thay ví dụ ngôn ngữ của bản EN (German/Japanese) bằng ví dụ có tiếng Đức + biến thể Áo/Thụy Sĩ — không thêm câu.
- **Tuyệt đối không dùng `Untertitel`** ở bất kỳ vị trí nào. Nếu cần nói về chữ chạy theo video thì… không cần — trang này không có ngữ cảnh đó.

---

## Không nên tối ưu cho các keyword

- `youtube transkript` / `transkript erstellen youtube` → **/de/youtube-transcript**
- `youtube transkript herunterladen` → **/de/download-youtube-transcript**
- `youtube untertitel herunterladen` / `srt vtt untertitel` → **/de/youtube-subtitle-downloader**. Từ **`Untertitel` bị cấm hoàn toàn trên trang này.**
- **`youtube video herunterladen` / `youtube video downloaden`** → intent tải VIDEO, SERP toàn downloader. **Trang này không tải gì cả** — nó **đọc và tóm tắt**. Quy tắc: tránh `herunterladen` làm động từ chính; nếu buộc phải nhắc thì tân ngữ phải là `Transkript` / `Datei`. **Xem mục bẫy bigram phía trên — đây là rủi ro số một của bản de.**
- `text zusammenfassen` / `artikel zusammenfassen` / `pdf zusammenfassen` → intent tóm tắt **CHỮ** (dán đoạn văn vào), không phải video. SERP là các công cụ text summarizer, khác hẳn. Không thuộc trang này.

---

## Internal linking

Section 7 đoạn 2 chứa **cả 3 link**:

- → /de/youtube-transcript (cần toàn văn, không phải ý chính)
- → /de/download-youtube-transcript (cần lưu toàn văn thành file)

---

## Ghi chú kỹ thuật cho de.json

- Xưng hô **`du`** (`füge ein`, `bekommst`, `brauchst`), nhất quán với `../youtube-subtitle-downloader/de.json`. **Không trộn `Sie`** ở bất kỳ đâu, kể cả FAQ.
- Giữ nguyên Latin: **TranscriptX, YouTube, KI**. Tên tool trong internal link giữ nguyên tiếng Anh (`YouTube Transcript`, `YouTube Video to Text`) đúng như `../youtube-subtitle-downloader/de.json`.
- Dùng `ß` chuẩn Đức (không đổi sang `ss` kiểu Thụy Sĩ).
- Cấu trúc: **8 section**, **8 FAQ**, S4 và S5 = `intro` 1 + `items` **4**, S1/S2 = `content` 3, S3 = `steps` 4, S6/S7 = `content` 2, conclusion = `content` 2. **KHÔNG có `specs`.**
- Internal link S7 giữ cú pháp markdown, đổi path sang `/de/...`.
- **Verify bắt buộc trước khi bàn giao:** shape check với `en.json` phải `True`; grep `Video herunterladen` / `Video heruntergeladen` / `Video downloaden` / `Untertitel` đều phải **= 0**.
