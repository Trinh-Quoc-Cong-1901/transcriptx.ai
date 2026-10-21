🔥 TranscriptX – YouTube Subtitle Downloader (Japanese / ja)

URL:
/ja/youtube-subtitle-downloader

Intent chính:

YouTube字幕ダウンロード (SRT · VTT, 無料)

Trang này nhắm đến người dùng Nhật muốn **tải file phụ đề có timecode** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại kèm phụ đề, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu tiếp cận (accessibility).

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA

Repo có 5 trang YouTube. Đã kiểm chéo keyword toàn cụm. Quy tắc phân chia **theo ngữ nghĩa từ**:

> **`字幕` (file phụ đề khớp giờ, dành cho editor / player) → TRANG NÀY**
> **`文字起こし` / `テキスト` (tài liệu để đọc / lưu / nộp) → `/ja/download-youtube-transcript`**

Căn cứ: bản EN section 1 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Trang này giữ cụm mạnh nhất

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `youtube字幕ダウンロード` | **1K – 10K** | Cụm mạnh nhất cả cụm 5 trang. **Trang này lấy làm H1.** |

### ⚠️ CỤM TRÙNG ĐÃ NHƯỜNG — `youtube字幕テキストダウンロード`

Cụm `youtube字幕テキストダウンロード` (**10 – 100**) nằm trong danh sách của **cả trang này lẫn `/ja/download-youtube-transcript`**.

**Chốt: thuộc `/ja/download-youtube-transcript`.** Trang đó **đã giữ** cụm này rồi — dùng ở body S2, mục TXT (vế `テキスト` neo intent "văn bản để đọc", đúng trục của trang kia).

> **Trang này KHÔNG được lấy lại cụm đó.** Không viết `字幕テキスト` ở bất kỳ đâu trong `ja.json` của trang này — tránh hai trang tranh nhau cùng một SERP. Trang này chỉ nói `字幕ファイル`, không nói `字幕テキスト`.

### ⚠️ LỖI DỮ LIỆU trong `2_loc_kw.md` — dấu cách thừa giữa morpheme

Danh sách `## Japanese (ja)` trong `2_loc_kw.md` ghi keyword **có dấu cách chen giữa các morpheme**, ví dụ `youtube 字幕 ダウンロード`, `youtube 字幕 ファイル ダウンロード`, `youtube 字幕 srt ダウンロード`.

Đây là **artifact của công cụ export keyword**, không phải chính tả tiếng Nhật. Tiếng Nhật **không dùng dấu cách giữa từ**.

Lưu ý thêm về ranh giới từ (để hiểu đúng dữ liệu, không phải để viết có dấu cách):
- `字幕` và `ダウンロード` đúng là **hai từ riêng** ghép lại thành danh từ ghép → viết liền `字幕ダウンロード`.
- `文字起こし` là **MỘT từ duy nhất** (`文字` + `起こし` là một động danh từ cố định) → tuyệt đối không tách thành `文字 起こし`.

**Dạng đúng để viết trong `ja.json` (viết liền, không dấu cách):**

| Ghi trong `2_loc_kw.md` (sai) | Dạng đúng dùng trong `ja.json` |
| ----------------------------- | ------------------------------ |
| `youtube 字幕 ダウンロード` | `YouTube字幕ダウンロード` |
| `youtube 字幕 抽出` | `YouTube字幕抽出` |
| `youtube 字幕 ダウンロード サイト` | `YouTube字幕ダウンロードサイト` |
| `youtube 動画 字幕 ダウンロード` | `YouTube動画字幕ダウンロード` |
| `youtube 字幕 srt ダウンロード` | `YouTube字幕SRTダウンロード` |
| `youtube 字幕 ファイル ダウンロード` | `YouTube字幕ファイルダウンロード` |
| `youtube 字幕 保存` | `YouTube字幕保存` |
| `youtube 字幕 ダウンロード 方法` | `YouTube字幕ダウンロード方法` |
| `youtube 字幕 ダウンロード 無料` | `YouTube字幕ダウンロード無料` |
| `youtube 字幕 テキスト ダウンロード` | ❌ **KHÔNG DÙNG** — đã nhường trang kia |

---

## Từ khóa chính

YouTube字幕ダウンロード (1K–10K) ✅ *đã search*

---

## Từ khóa phụ

### Nhóm ダウンロード (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| YouTube字幕ダウンロード | 1K–10K | ✅ đã search *(KW chính)* |
| YouTube動画字幕ダウンロード | 10–100 | ✅ đã search |
| YouTube字幕SRTダウンロード | 10–100 | ✅ đã search |
| YouTube字幕ファイルダウンロード | 10–100 | ✅ đã search |
| YouTube字幕ダウンロードサイト | 10–100 | ✅ đã search |
| YouTube字幕ダウンロード方法 | 0–10 | ✅ đã search |
| YouTube字幕ダウンロード無料 | 0–10 | ✅ đã search |

### Nhóm 抽出 / 保存

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| YouTube字幕抽出 | 100–1K | ✅ đã search |
| YouTube字幕保存 | 10–100 | ✅ đã search |

### Đã nhường trang đối xứng — KHÔNG dùng

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| YouTube字幕テキストダウンロード | 10–100 | ❌ đã giữ ở `/ja/download-youtube-transcript` (S2 mục TXT) |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| YouTube VTTダウンロード | — | 🔄 dịch bổ sung (VTT) |
| 字幕翻訳 | — | 🔄 dịch bổ sung (translate subtitles) |
| 字幕ファイル編集 | — | 🔄 dịch bổ sung (edit subtitle file) |
| タイムコード | — | 🔄 dịch bổ sung (timecode) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Nhật **cần file phụ đề để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn phụ đề vào bản dựng.
- Đăng lại video lên kênh mình kèm phụ đề mà không phải gõ lại.
- Dịch phụ đề sang tiếng Nhật hoặc ngôn ngữ khác rồi gắn lại.
- Sửa phụ đề tự động của YouTube vốn hay sai (đặc biệt tên riêng, kanji đồng âm).
- Đáp ứng yêu cầu tiếp cận cho người khiếm thính.

Họ kỳ vọng: dán link là ra file, chọn được SRT hay VTT, có timecode từng dòng, mở sửa được, miễn phí, không cài extension.

### Khác biệt so với bản tiếng Anh

1. **`字幕` là trục duy nhất, không có từ thứ hai.** Bản EN xoay vòng `subtitles` / `captions` để đỡ lặp; tiếng Nhật chỉ có `字幕` (từ `キャプション` gần như không ai search). Phải chống lặp bằng cách đổi cấu trúc câu và xen `字幕ファイル` / `字幕の行` / `タイムコード`.
2. **Trang này phải nhường 1 cụm cho trang đối xứng.** Bản EN không có vấn đề này — `transcript` và `subtitle` tách bạch tự nhiên. Tiếng Nhật thì `youtube字幕テキストダウンロード` đứng chân hai bên, đã chốt nhường cho `/ja/download-youtube-transcript`. Xem khối cảnh báo đầu file.
3. **Nhóm `抽出` mạnh hơn tương ứng bản EN.** `YouTube字幕抽出` đạt `100 – 1K` — bản EN không có động từ "extract" nào có volume đáng kể. Phải đưa vào H2 section 1.
4. **Dữ liệu keyword tiếng Nhật bị nhiễu dấu cách.** Bản EN vốn có dấu cách nên không có vấn đề; bản ja phải chuẩn hóa lại toàn bộ trước khi viết. Xem mục lỗi dữ liệu ở trên.
5. **Nỗi lo nhận dạng tiếng Nhật.** Người Nhật hay nghi ngờ độ chính xác của nhận dạng giọng nói tiếng Nhật (kanji, tên riêng). Xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu mới.

---

## Đối tượng người dùng

- Editor video, freelancer dựng phim (nạp SRT vào Premiere/Final Cut/Resolve)
- Người re-upload / tổng hợp video lên kênh riêng
- Người làm phụ đề (dịch sub) cho khán giả Nhật
- Marketer chạy nội dung đa ngôn ngữ
- Người làm nội dung cho người khiếm thính (bắt buộc theo yêu cầu tiếp cận)
- Người muốn sửa phụ đề tự động sai của YouTube

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ja.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2, đúng **4 `steps`** ở S3, đúng **5 `items`** ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube字幕ダウンロード | YouTube字幕ダウンロード *(KW chính)* |
| — | **quickAnswer** | YouTube字幕ダウンロード方法 |
| 1 | 字幕ファイルとは何か — YouTube字幕抽出で得られるもの | YouTube字幕抽出, YouTube字幕ファイルダウンロード |
| 2 | SRTとVTT、どちらの字幕形式でダウンロードするか | YouTube字幕SRTダウンロード |
| 3 | YouTubeから字幕をダウンロードする方法 | YouTube字幕ダウンロード方法 |
| 4 | ダウンロードした字幕ファイルでできること | YouTube動画字幕ダウンロード, YouTube字幕保存 |
| 5 | 100言語以上で字幕をダウンロード | YouTube字幕ダウンロード無料 *(+ nhấn tiếng Nhật)* |
| 6 | 字幕、文字起こし、要約 — どれが必要か？ | *(3 internal link — chốt phân định)* |
| 7 | よくある質問 | YouTube字幕ダウンロードサイト + long-tail |
| — | **conclusion** | YouTube字幕ダウンロード, 無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là **một trong hai chỗ duy nhất** được nhắc `文字起こし` (thuộc trang kia).
- **Section 1 đoạn 2 là định nghĩa ranh giới của bản EN** (`transcript` = chữ để đọc, `subtitle file` = chữ chạy đè lên video). **Dịch sát, không rút gọn** — đây là câu chống cannibalization mạnh nhất trang.
- `文字起こし` **chỉ được xuất hiện ở S1 đoạn 2, S6 và FAQ 5.** Ngoài ba chỗ đó, kết quả của trang này luôn gọi là `字幕` / `字幕ファイル`.
- **Không bao giờ viết `字幕テキスト`** — cụm đó đã nhường trang đối xứng.
- Nỗi lo nhận dạng tiếng Nhật xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN — không thêm câu.

---

## Không nên tối ưu cho các keyword

- **`YouTube文字起こしダウンロード` / `YouTube字幕テキストダウンロード` / `YouTube transcript ダウンロード`** → **/ja/download-youtube-transcript** (tài liệu để đọc/lưu/nộp). Chỉ được nhắc ở section 6.
- **`YouTube文字起こし` / `YouTube字幕表示`** (đọc trên màn hình, không tải file) → **/ja/youtube-transcript**.
- **`YouTube動画要約`** → **/ja/youtube-video-summarizer**.
- **`YouTube動画ダウンロード` / `YouTube MP4ダウンロード` / `YouTubeダウンローダー`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **file phụ đề**. Quy tắc: `ダウンロード` / `保存` chỉ đi với `字幕` / `字幕ファイル` / `SRT` / `VTT`, **KHÔNG BAO GIỜ** với `動画`.
- **`YouTube字幕をオンにする` / `YouTube字幕設定`** → **hướng dẫn bật phụ đề trong app**, không phải công cụ tải file.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/ja/youtube-transcript` (đọc chữ thuần trên màn hình, không timecode)
- → `/ja/download-youtube-transcript` (lưu chữ thành TXT/DOCX/PDF) — **đây là trang đối xứng, link quan trọng nhất**
- → `/ja/youtube-video-summarizer` (chỉ cần ý chính)

---

## Ghi chú kỹ thuật cho ja.json

- Thể văn **です・ます**, nhất quán với các trang Nhật khác trong repo.
- Giữ nguyên Latin: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok**.
- **Viết liền, KHÔNG chèn dấu cách thừa** giữa morpheme (`YouTube字幕ダウンロード`, không phải `YouTube 字幕 ダウンロード`).
- Dùng dấu câu Nhật: `。` `、` `「」`; dùng `・` khi liệt kê format (`SRT・VTT`).
- Internal link section 6 giữ cú pháp markdown, đổi path sang `/ja/...`.
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 `intro` 1 + `items` **2**, S3 `steps` 4, S4 `intro` 1 + `items` 5, S5 `content` 2, S6 `content` 2, S7 `items` 8, conclusion `content` 2. **KHÔNG có `specs`.**
