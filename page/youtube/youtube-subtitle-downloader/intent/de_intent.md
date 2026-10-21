🔥 TranscriptX – YouTube Subtitle Downloader (German / de)

URL:
/de/youtube-subtitle-downloader

Intent chính:

youtube untertitel herunterladen (SRT · VTT, kostenlos)

Trang này nhắm đến người dùng Đức muốn **tải file phụ đề có timecode** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại kèm phụ đề, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu tiếp cận (Barrierefreiheit).

---

## 🚨 CỤM YOUTUBE 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Trang này nằm ở vùng xung đột với `/de/download-youtube-transcript`. **Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **`Untertitel` (file phụ đề khớp giờ cho editor) → TRANG NÀY**
> **`Transkript` (tài liệu để đọc/lưu/nộp) → `/de/download-youtube-transcript`**

Căn cứ: bản EN section 1 đoạn 2 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### 🎉 Lợi thế riêng của tiếng Đức: phân định gần như miễn phí

- Bản **vi** phải hy sinh keyword mạnh nhất cho trang đối xứng vì chữ "phụ đề" bị dùng lẫn cho cả hai khái niệm.
- Bản **ko** phải chốt bằng tay vì `자막` bị kéo về cả hai phía.
- Tiếng Đức thì `Untertitel` và `Transkript` là **hai từ riêng biệt, người bản ngữ không nhầm**. Chỉ cần chọn đúng từ là ranh giới tự có.

**Kết quả kiểm trùng: 0 keyword trùng** giữa 9 keyword de của trang này (`Untertitel` ×8, `captions` ×1) và 11 keyword de của `/de/download-youtube-transcript` (`Transkript` ×9, `Transkription` ×1, `Text` ×2, `transcript` ×1).

**Trang này giữ `youtube untertitel herunterladen` (100 – 1K) làm H1** — cụm mạnh nhất, không phải nhường đi đâu.

### ⚠️ Ranh giới đã chốt ở trang đối xứng: `als Text` vs `als SRT`

Cụm `youtube untertitel als text herunterladen` (10–100) **có chứa `Untertitel` nhưng THUỘC TRANG KIA**, vì vế **`als Text`** neo rõ intent tài liệu để đọc.

Trang này giữ cụm song song `youtube untertitel als srt herunterladen` (0–10).

> **Ranh giới `als Text` (trang kia) vs `als SRT` (trang này) rất sạch. Trang này KHÔNG được lấy lại cụm `als Text`.**

---

## ⚠️ BẪY RIÊNG TIẾNG ĐỨC: bigram `Video herunterladen` do trật tự từ

Tiếng Đức đẩy động từ ra cuối mệnh đề, nên rất dễ vô tình sinh ra chuỗi `... YouTube-Video herunterladen` — **đúng bằng keyword của nhóm tải file mp4**, nhóm có volume rất lớn ở Đức và SERP toàn video downloader. Bản EN không gặp lỗi này vì trật tự SVO giữ động từ đứng trước tân ngữ.

Trong danh sách 9 keyword de của trang này có **1 cụm dính bẫy**:

| Keyword | Vấn đề | Cách viết an toàn |
| ------- | ------ | ----------------- |
| `untertitel aus youtube video herunterladen` (0–10) | Nếu viết thẳng theo trật tự Đức sẽ thành `... aus einem YouTube-Video herunterladen` → `Video` đứng liền trước `herunterladen` | Đảo tân ngữ ra sau: **`aus dem YouTube-Video die Untertitel heruntergeladen`** — `Untertitel` luôn đứng liền trước động từ |

**Quy tắc tuyệt đối:** `herunterladen` / `heruntergeladen` / `downloaden` chỉ được đi với `Untertitel` / `Untertiteldatei` / `Datei` / `SRT` / `VTT` đứng liền trước. **KHÔNG BAO GIỜ với `Video`.**

Verify: `grep -o "Video herunterladen" de.json | wc -l` phải = **0**. (Cùng lỗi từng xảy ra ở `/de/download-youtube-transcript`, đã ghi lại trong `intent/de_intent.md` của trang đó.)

---

## Lỗi dữ liệu trong file nguồn

Đã soát phần `## German (de)` của `2_loc_kw.md`:

- ❌ **Không có** dòng rác `Keyword ideas` / `Keywords you provided` (khác phần `## Vietnamese (vi)` có cả 2 dòng rác).
- ❌ **Không có** keyword trùng lặp trong nội bộ danh sách de.
- ❌ **Không có** keyword sai intent kiểu "tải VIDEO" hay "bật phụ đề".

**Số keyword thực: 9 dòng thô − 0 rác − 0 sai intent = 9 keyword, dùng được toàn bộ.**

---

## Từ khóa chính

**youtube untertitel herunterladen** (100 – 1K) ✅ *đã search*

Cụm mạnh nhất toàn danh sách de và là **lõi chung** của 5 cụm đuôi dài khác (`untertitel von youtube ...`, `untertitel youtube ...`, `youtube untertitel datei ...`, `youtube untertitel als srt ...`, `untertitel aus youtube video ...`). Neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm `herunterladen` (trục chính — 6 cụm)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube untertitel herunterladen | 100 – 1K | ✅ đã search *(KW chính — H1)* |
| untertitel von youtube herunterladen | 10 – 100 | ✅ đã search — neo ở H2 section 3 |
| untertitel youtube herunterladen | 10 – 100 | ✅ đã search — biến thể trật tự, phủ theo H1 |
| youtube untertitel datei herunterladen | 0 – 10 | ✅ đã search — neo ở step 4 (S3) |
| youtube untertitel als srt herunterladen | 0 – 10 | ✅ đã search — neo ở S2 mục SRT, **luôn giữ vế `als SRT`** |
| untertitel aus youtube video herunterladen | 0 – 10 | ✅ đã search — ⚠️ viết đảo trật tự, xem mục bẫy bigram |

### Nhóm danh từ công cụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube untertitel downloader | 10 – 100 | ✅ đã search — neo ở S1 đoạn 3 + FAQ 2 |

### Nhóm mượn tiếng Anh (người Đức hay gõ lẫn)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube captions herunterladen | 0 – 10 | ✅ đã search — neo ở FAQ 1 |
| untertitel downloaden youtube | 0 – 10 | ✅ đã search — `downloaden` dùng **đúng 1 lần** ở S3 step 3 |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| untertiteldatei bearbeiten | — | 🔄 dịch bổ sung (edit subtitle file) |
| youtube vtt herunterladen | — | 🔄 dịch bổ sung (VTT) |
| untertitel übersetzen | — | 🔄 dịch bổ sung (translate subtitles) |
| Zeitcode / Zeitstempel | — | 🔄 dịch bổ sung (timecode) |
| untertitel kostenlos herunterladen | — | 🔄 dịch bổ sung (free) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ Volume trang này (100 – 1K) ngang trang đối xứng. Không nhồi mật độ — chiến lược là **phủ đều 9 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Đức **cần file phụ đề để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn phụ đề vào bản dựng.
- Đăng lại video lên kênh mình kèm phụ đề mà không phải gõ lại.
- Dịch phụ đề sang ngôn ngữ khác rồi gắn lại (thị trường DACH hay làm sub đa ngôn ngữ).
- Sửa phụ đề tự động của YouTube vốn hay sai tên riêng.
- Đáp ứng yêu cầu Barrierefreiheit (BITV / EU Accessibility Act) — ở Đức đây là nghĩa vụ pháp lý, không phải tùy chọn.

Họ kỳ vọng: dán link là ra file, chọn được SRT hay VTT, có timecode từng dòng, mở sửa được, miễn phí, không cài extension.

### Khác biệt so với bản tiếng Anh

1. **Bẫy trật tự từ không tồn tại ở bản EN.** Tiếng Anh giữ động từ trước tân ngữ (`download subtitles from a YouTube video`) nên không bao giờ sinh chuỗi `video download`. Tiếng Đức đẩy động từ cuối câu → phải kiểm soát tân ngữ đứng liền trước `herunterladen` ở **mọi câu**. Xem mục bẫy bigram.

2. **Cặp `herunterladen` / `downloaden` cùng tồn tại.** Bản EN chỉ có một động từ `download`. Người Đức gõ cả hai. Xử lý: `herunterladen` là dạng chuẩn dùng xuyên suốt; `downloaden` dùng **đúng 1 lần** ở S3 (bám cụm `untertitel downloaden youtube`), nhiều hơn sẽ nghe như Denglisch bừa bãi.

3. **Danh từ ghép thay cho cụm giới từ.** Tiếng Đức gộp `Untertiteldatei`, `Untertitel-Format`, `YouTube-Video`, `Schnittprogramm` thành một từ. Mật độ keyword đọc tự nhiên hơn bản EN, nhưng phải giữ dấu gạch nối nhất quán ở `YouTube-Video` / `YouTube-Link`.

4. **`Untertitel` vs `Transkript` tách bạch tự nhiên — không cần kỹ thuật neo đẩy.** Bản EN có `subtitles` và `captions` dùng xen kẽ để đỡ lặp; tiếng Đức chỉ có một trục `Untertitel` (`Captions` chỉ là từ mượn dùng 1 lần ở FAQ). Chống lặp bằng cách đổi cấu trúc câu và xen `Untertiteldatei` / `Untertitel-Zeile` / `Zeitcode`.

5. **Nhấn Barrierefreiheit mạnh hơn bản EN.** Bản EN nói "often required"; ở Đức đây là nghĩa vụ pháp lý cụ thể — giữ đúng số câu nhưng chọn từ dứt khoát (`Pflicht, nicht Kür`).

---

## Đối tượng người dùng

- Video Editor, freelancer dựng phim (nạp SRT vào Premiere/Final Cut/Resolve)
- YouTuber / Content Creator re-upload video lên kênh riêng
- Người làm phụ đề (Untertitler) và dịch giả cho thị trường DACH
- Marketer chạy nội dung đa ngôn ngữ (DE → EN → FR)
- Người phụ trách Barrierefreiheit ở cơ quan, trường học, doanh nghiệp
- Người muốn sửa phụ đề tự động sai của YouTube

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `de.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (de) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube Untertitel herunterladen | youtube untertitel herunterladen *(KW chính)* |
| — | **quickAnswer** | untertitel aus youtube video herunterladen *(viết đảo trật tự)* |
| 1 | Was eine Untertiteldatei wirklich ist | youtube untertitel downloader, untertitel youtube herunterladen |
| 2 | SRT oder VTT: Welches Untertitel-Format herunterladen? | youtube untertitel als srt herunterladen |
| 3 | So lädst du Untertitel von YouTube herunter | untertitel von youtube herunterladen, untertitel downloaden youtube, youtube untertitel datei herunterladen |
| 4 | Was du mit einer heruntergeladenen Untertiteldatei machen kannst | untertitel aus youtube video herunterladen *(item 2)* |
| 5 | Untertitel in über 100 Sprachen herunterladen | youtube untertitel herunterladen *(+ nhấn tiếng Đức/Áo/Thụy Sĩ)* |
| 6 | Untertitel, Transkript oder Zusammenfassung? | *(3 internal link — chốt phân định)* |
| 7 | Häufige Fragen | youtube captions herunterladen, youtube untertitel downloader + long-tail |
| — | **conclusion** | youtube untertitel herunterladen, kostenlos |

### Ghi chú riêng cho bản de (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là chỗ duy nhất từ `Transkript` được phép xuất hiện ngoài S1 đoạn 2 và FAQ 5.
- **Section 1 đoạn 2 là câu chống cannibalization mạnh nhất trang** (`Transkript` = chữ để đọc, `Untertiteldatei` = chữ chạy đè lên video). Dịch sát, **không rút gọn**.
- `downloaden` dùng đúng **1 lần** ở S3 step 3. Mọi chỗ khác dùng `herunterladen`.
- `Captions` dùng đúng **1 lần** ở FAQ 1 (bám cụm `youtube captions herunterladen`).
- Nỗi lo nhận dạng tiếng Đức (giọng Áo / Thụy Sĩ) xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.
- **Không lấy lại cụm `youtube untertitel als text herunterladen`** — thuộc `/de/download-youtube-transcript`.

---

## Không nên tối ưu cho các keyword

- **`youtube transkript herunterladen` / `youtube transkript als txt herunterladen` / `youtube transkript pdf herunterladen` / `youtube untertitel als text herunterladen` / `youtube transkript exportieren`** → **/de/download-youtube-transcript** (tài liệu để đọc/lưu/nộp). Trang này không đặt `Transkript` vào `title` / `h1` / `h2`.
- `youtube transkript` / `youtube transkript anzeigen` / `youtube transkript kopieren` → **/de/youtube-transcript** (đọc và copy trên màn hình, không tải file).
- `youtube video zusammenfassen` / `youtube zusammenfassung` → **/de/youtube-video-summarizer**.
- **`youtube video herunterladen` / `youtube downloader` / `youtube mp4 herunterladen` / `youtube video downloaden`** → **intent tải VIDEO**, SERP toàn video downloader. Trang này tải **file phụ đề**. Quy tắc: `herunterladen` luôn phải có tân ngữ `Untertitel` / `Untertiteldatei` / `Datei` / `SRT` / `VTT` đứng liền trước, **không bao giờ `Video`** — kể cả dạng bigram do trật tự từ.
- **`untertitel einschalten` / `youtube untertitel aktivieren` / `untertitel anzeigen`** → **hướng dẫn bật phụ đề trong app YouTube**, không phải công cụ tải file. Intent hoàn toàn khác.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/de/youtube-transcript` (chỉ muốn đọc chữ thuần trên màn hình, không timecode)
- → `/de/download-youtube-transcript` (lưu chữ thành TXT/DOCX/PDF) — **đây là trang đối xứng, link quan trọng nhất**
- → `/de/youtube-video-summarizer` (chỉ cần ý chính, không cần từng dòng)

---

## Ghi chú kỹ thuật cho de.json

- Xưng hô **`du`** xuyên suốt, nhất quán với `/de/download-youtube-transcript` và `/de/video-to-text`. **Tuyệt đối không trộn `Sie`** (kể cả trong FAQ).
- Giữ nguyên Latin: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok**.
- Danh từ ghép giữ dấu gạch nối nhất quán: `YouTube-Video`, `YouTube-Link`, `Untertitel-Format`, `SRT-Datei`, `VTT-Datei`.
- Cấu trúc: **7 section**, **8 FAQ**, S1 = `content` 3, S2 = `intro` 1 + `items` **2**, S3 = `steps` 4, S4 = `intro` 1 + `items` 5, S5 = `content` 2, S6 = `content` 2, S7 = `items` 8, conclusion = `content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/de/...`.
- **Tuyệt đối không để chuỗi `Video herunterladen`, `Video heruntergeladen` hoặc `Video downloaden` xuất hiện.**
