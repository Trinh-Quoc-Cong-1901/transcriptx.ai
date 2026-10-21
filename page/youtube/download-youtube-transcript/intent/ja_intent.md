🔥 TranscriptX – Download YouTube Transcript (Japanese / ja)

URL:
/ja/download-youtube-transcript

Intent chính:

Tải bản chép lời (文字起こし) của video YouTube về máy dưới dạng file (TXT, DOCX, PDF, SRT) — miễn phí

Trang này nhắm đến người dùng Nhật muốn **lưu bản 文字起こし của video YouTube xuống thiết bị thành file** — để đọc offline, lưu trữ, nộp/gửi, in ra, hoặc đưa vào công cụ khác. Khác với việc chỉ đọc transcript trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Đã kiểm chéo keyword toàn cụm. Với bản **ja**, trang này trùng **1 keyword** với `/ja/youtube-subtitle-downloader`:

| Keyword trùng | Volume | Trang sở hữu |
| ------------- | ------ | ------------ |
| `youtube字幕テキストダウンロード` | 10–100 | `/ja/youtube-subtitle-downloader` (nhưng có vế `テキスト` → dùng hạn chế ở trang này) |

**Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **Từ mang nghĩa "phụ đề" (`字幕`) → `/ja/youtube-subtitle-downloader`**
> **Từ mang nghĩa "bản chép lời" (`文字起こし` / `テキスト` / `transcript` / `トランスクリプト`) → TRANG NÀY**

Căn cứ ranh giới: bản EN section 6 đã tự định nghĩa — trang này ra **tài liệu để đọc / lưu / nộp**; trang kia ra **file phụ đề khớp giờ (SRT, VTT) cho phần mềm dựng phim**.

### Cách xử lý cụm `字幕テキスト`

Cụm `youtube字幕テキストダウンロード` (10–100) có vế **`テキスト`** neo rõ là người dùng muốn **văn bản để đọc**, không phải file phụ đề cho editor. Vì vậy:

- **Được dùng ở trang này**, nhưng **CHỈ trong body section 2 (mục TXT)**, và **luôn kèm vế `テキスト`**.
- **Tuyệt đối không đặt vào `title` / `h1` / bất kỳ `h2` nào.**
- Biến thể đảo trật tự `youtube字幕ダウンロードテキスト` (10–100) áp dụng **cùng một luật** — chỉ neo ở S2 mục TXT, không lên tiêu đề.
- Cụm `字幕` **thuần túy** (không có vế `テキスト`) thuộc hẳn `/ja/youtube-subtitle-downloader`, và ở trang này chỉ xuất hiện **đúng 1 lần** ở **S6 đoạn 2**, ngay trong câu trỏ sang trang kia (kỹ thuật neo đẩy đi).

---

## ⚠️ LỖI DỮ LIỆU TRONG `2_loc_kw.md`: DẤU CÁCH THỪA GIỮA MORPHEME

Danh sách keyword ja trong file nguồn bị **chèn dấu cách vào giữa các morpheme của cùng một từ**. Tiếng Nhật **không dùng dấu cách**, nên đây là lỗi của công cụ export, không phải cách người dùng thật gõ vào Google.

| Dạng SAI trong file nguồn | Dạng ĐÚNG (viết liền) |
| ------------------------- | --------------------- |
| `文字 起こし` | `文字起こし` ← **MỘT từ duy nhất** |
| `トラン スクリプト` | `トランスクリプト` |
| `youtube 文字 起こし ダウンロード` | `youtube文字起こしダウンロード` |
| `youtube 字幕 テキスト ダウンロード` | `youtube字幕テキストダウンロード` |
| `youtube 動画 テキスト 抽出 ダウンロード` | `youtube動画テキスト抽出ダウンロード` |
| `youtube 文字 起こし データ ダウンロード` | `youtube文字起こしデータダウンロード` |
| `日本 語` | `日本語` |

**Xử lý:** trong tài liệu intent này ghi ở dạng đúng (viết liền). Trong `ja.json` **viết liền hoàn toàn**, không được để lọt dấu cách thừa nào giữa các morpheme tiếng Nhật.

Ngoại lệ hợp lệ duy nhất: dấu cách quanh **chuỗi Latin** (ví dụ `YouTube transcript ダウンロード`, `youtube transcript download 日本語`), vì đó là ranh giới ngôn ngữ thật.

**Số keyword thực: 12 dòng, tất cả đều là keyword hợp lệ (không có dòng rác kiểu `Keyword ideas`).** Trong đó 2 cụm chứa `字幕` bị hạn chế vị trí → **10 cụm dùng làm trục chính tự do.**

---

## Từ khóa chính

**youtube文字起こしダウンロード (100 – 1K)** ✅ *đã search*

Đây là cụm mạnh nhất trong toàn bộ danh sách ja và cũng là **lõi chung** của 5 cụm đuôi dài khác (`youtube動画文字起こしダウンロード`, `youtube文字起こしtxtダウンロード`, `youtube文字起こし無料ダウンロード`, `youtube文字起こしデータダウンロード`, `youtube文字起こし保存`), nên neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm 文字起こし (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube文字起こしダウンロード | 100–1K | ✅ đã search *(KW chính)* |
| youtube文字起こし保存 | 10–100 | ✅ đã search |
| youtube動画文字起こしダウンロード | 0–10 | ✅ đã search |
| youtube文字起こしtxtダウンロード | 0–10 | ✅ đã search |
| youtube文字起こし無料ダウンロード | 0–10 | ✅ đã search |
| youtube文字起こしデータダウンロード | 0–10 | ✅ đã search |

### Nhóm トランスクリプト / transcript (từ mượn)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtubeトランスクリプトダウンロード | 10–100 | ✅ đã search |
| youtube transcript ダウンロード | 0–10 | ✅ đã search |
| youtube transcript download 日本語 | 0–10 | ✅ đã search |

### Nhóm テキスト抽出

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube動画テキスト抽出ダウンロード | 0–10 | ✅ đã search |

### Nhóm 字幕 — dùng HẠN CHẾ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube字幕テキストダウンロード | 10–100 | ✅ đã search — ⚠️ chỉ ở body S2 (mục TXT), luôn kèm vế `テキスト` |
| youtube字幕ダウンロードテキスト | 10–100 | ✅ đã search — ⚠️ cùng luật, biến thể đảo trật tự, cũng chỉ ở S2 |

**Tổng: 12/12 keyword đã search đều được áp dụng.**

### Dịch bổ sung (chỉ rải body, KHÔNG lên tiêu đề)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| YouTube文字起こしをPDFで保存 | — | 🔄 dịch bổ sung (PDF) |
| YouTube文字起こしDOCXダウンロード | — | 🔄 dịch bổ sung (DOCX) |
| YouTube文字起こしオフライン | — | 🔄 dịch bổ sung (offline) |
| YouTube文字起こしファイル保存 | — | 🔄 dịch bổ sung (save file) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ Volume cụm chính (100–1K) thấp hơn hẳn `/ja/video-to-text`. Lý do: "tải file 文字起こし" là nhu cầu hẹp hơn "chuyển video thành văn bản". Không cố nhồi mật độ — chiến lược là **phủ đều 12 cụm**, mỗi cụm một vị trí neo.

---

## Search Intent

Người dùng Nhật **đã biết mình muốn bản 文字起こし** và đang ở bước tiếp theo: lấy nó thành **file nằm trên máy**. Khác hẳn người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay — không đăng ký (会員登録不要), không cài extension (インストール不要).
- **Chọn được định dạng** — TXT để dán sang chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline**.
- Miễn phí (無料), không giới hạn độ dài video.
- Nhận dạng tốt **tiếng Nhật**, có phân tách người nói (話者ラベル).

### Khác biệt so với bản tiếng Anh

1. **Nguy cơ nhiễm intent "tải VIDEO" cao hơn hẳn bản EN.** Ở Nhật, nhóm `YouTube動画ダウンロード` / `YouTube保存` có volume rất lớn và SERP toàn công cụ tải mp4. Bản EN không gặp vấn đề này vì "transcript" tự nó đã tách bạch. Quy tắc cứng cho bản ja: **`ダウンロード` và `保存` chỉ được đi kèm `文字起こし` / `テキスト` / `ファイル`, KHÔNG BAO GIỜ đi kèm `動画`.** Khi cần dùng keyword `youtube動画文字起こしダウンロード`, viết dạng `YouTube動画の文字起こしをダウンロード` hoặc `YouTube動画文字起こしのダウンロード` — luôn có trợ từ tách để tân ngữ của "download" rõ ràng là **chữ**, không phải video.

2. **`字幕` bị dùng lẫn giữa hai nghĩa.** Bản EN có "transcript" vs "subtitle" tách bạch, còn tiếng Nhật `字幕` vừa chỉ phụ đề khớp giờ vừa được người dùng phổ thông dùng để chỉ "chữ trong video". Phải chủ động nhường `字幕` cho `/ja/youtube-subtitle-downloader`, chỉ giữ lại biến thể có vế `テキスト`. Xem khối cảnh báo đầu file.

3. **`文字起こし` là từ bản địa mạnh, không dùng từ mượn làm trục.** Ngược với bản vi (nơi `transcript` giữ nguyên tiếng Anh vì người Việt quen từ mượn), người Nhật gõ `文字起こし` áp đảo (6/12 keyword chứa cụm này, gồm cả cụm mạnh nhất). `トランスクリプト` chỉ 1 cụm ở mức 10–100 → dùng làm từ đồng nghĩa phụ, không lên H1.

4. **Thể văn `です・ます` bắt buộc.** Bản EN dùng giọng trực tiếp, cụt. Bản ja phải giữ thể lịch sự nhất quán với `/ja/video-to-text` — nhưng không rơi vào 敬語 nặng, giữ nhịp tự nhiên như văn hướng dẫn công cụ.

5. **Nhấn PDF/DOCX mạnh hơn bản EN.** Văn hóa văn phòng Nhật nặng về 資料 nộp/lưu hồ sơ, nên vế "file để nộp và lưu trữ" cần rõ hơn.

---

## Đối tượng người dùng

- Sinh viên, nghiên cứu sinh (lưu 文字起こし bài giảng, phỏng vấn vào thư mục đề tài)
- Nhân viên văn phòng (tải DOCX làm 議事録 / tài liệu nội bộ)
- Nhà báo, biên tập viên (giữ lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Người học ngoại ngữ (tải TXT đọc offline)
- Người làm phụ đề cần bản nháp có timecode (SRT)
- Người cần đưa 文字起こし vào công cụ khác yêu cầu upload file (dịch thuật, AI, hệ quản lý tài liệu)

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ja.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube文字起こしダウンロード | youtube文字起こしダウンロード *(KW chính)* |
| — | **quickAnswer** | youtube文字起こしダウンロード + cách làm |
| 1 | 文字起こしをダウンロードすると何ができるか | youtube文字起こしダウンロード, youtube文字起こしデータダウンロード, youtube動画テキスト抽出ダウンロード |
| 2 | どの形式でダウンロードすればいいか | youtube文字起こしtxtダウンロード, ⚠️ youtube字幕テキストダウンロード + youtube字幕ダウンロードテキスト *(chỉ ở mục TXT, luôn kèm vế `テキスト`)* |
| 3 | YouTube文字起こしをダウンロードする方法 | youtube文字起こしダウンロード, youtube動画文字起こしダウンロード *(dạng `YouTube動画の文字起こしをダウンロード`)* |
| 4 | テキストだけでなくファイルが必要なとき | youtube文字起こし保存, youtubeトランスクリプトダウンロード |
| 5 | 100言語以上の文字起こしをダウンロード | youtube文字起こし無料ダウンロード *(+ nhấn tiếng Nhật)*, youtube transcript download 日本語 |
| 6 | 別のツールが向いている場合 | ⚠️ `字幕` — **đúng 1 lần**, trong câu trỏ sang `/ja/youtube-subtitle-downloader` + 2 link còn lại |
| 7 | よくある質問 | youtube文字起こし無料ダウンロード, youtube文字起こしtxtダウンロード, YouTube transcript ダウンロード + long-tail |
| — | **conclusion** | youtube文字起こしダウンロード, 無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát **cả 3 vế**, không rút gọn, không gộp. Đây cũng là chỗ **duy nhất** từ `字幕` đứng một mình được phép xuất hiện.
- Nỗi lo nhận dạng **tiếng Nhật** xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Nhật — **không thêm câu**.
- `トランスクリプト` dùng **1 lần** ở S4 (bám keyword) và `YouTube transcript` dạng Latin **1 lần** ở FAQ. Dùng nhiều hơn sẽ loãng trục `文字起こし`.
- Cụm `字幕テキスト` chỉ nằm ở **S2 mục TXT**, đúng 1 câu, gói cả hai biến thể trật tự.
- Không dùng `動画をダウンロード` / `動画保存` ở bất kỳ đâu, kể cả trong câu phủ định.

---

## Không nên tối ưu cho các keyword

- **`youtube字幕ダウンロード` / `youtube字幕保存` / `youtube字幕srt` / `youtube字幕vtt`** → **/ja/youtube-subtitle-downloader** (file phụ đề khớp giờ cho phần mềm dựng phim). Chỉ nhắc `字幕` đúng 1 lần ở S6 trong câu trỏ đi.
- **`youtube文字起こし` / `youtube文字起こし表示` / `youtube文字起こし見る` / `youtubeスクリプト表示`** → **/ja/youtube-transcript** (đọc và copy trên màn hình, không tải file).
- **`youtube要約` / `youtube動画要約` / `youtubeまとめ`** → **/ja/youtube-video-summarizer**.
- 🚫 **NHÓM TẢI VIDEO — nguy hiểm nhất ở thị trường Nhật:** `YouTube動画ダウンロード`, `YouTube保存`, `YouTubeダウンロードmp4`, `YouTube動画保存アプリ`, `YouTube音声ダウンロード`. Volume rất lớn, SERP toàn công cụ tải video. Trang này chỉ tải **chữ**. Quy tắc: `ダウンロード`/`保存` luôn phải có tân ngữ `文字起こし` / `テキスト` / `ファイル`.
- **`動画文字起こし`** (không có chữ YouTube) → **/ja/video-to-text** (upload file từ máy, không dán link).
- **`YouTube字幕の付け方`** — hướng dẫn tự tạo phụ đề trong YouTube Studio, không phải công cụ tải.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/ja/youtube-transcript` — chỉ muốn đọc/copy trên màn hình, không cần file
- → `/ja/youtube-subtitle-downloader` — cần file **字幕** khớp giờ (SRT, VTT) cho phần mềm dựng phim — **link quan trọng nhất, cũng là chỗ neo duy nhất của từ `字幕`**
- → `/ja/youtube-video-summarizer` — chỉ cần ý chính, không cần toàn văn

---

## Ghi chú kỹ thuật cho ja.json

- Thể văn **です・ます**, nhất quán với `/ja/video-to-text`. Không dùng 敬語 nặng (`いたします`, `ございます`).
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**.
- **VIẾT LIỀN — không dấu cách thừa giữa morpheme tiếng Nhật.** Chỉ được có dấu cách ở ranh giới với chuỗi Latin.
- Dấu câu tiếng Nhật: `。` `、` `「」`. Dấu chấm giữa các format dùng `・` (ví dụ `TXT・DOCX・PDF・SRT`).
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 `intro` 1 + `items` 4, S3 `steps` 4, S4 `intro` 1 + `items` 5, S5 `content` 2, S6 `content` 2, S7 `items` 8, conclusion `content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/ja/...`.
- **Tuyệt đối không để chuỗi `動画をダウンロード` / `動画ダウンロード` / `動画を保存` xuất hiện.**
