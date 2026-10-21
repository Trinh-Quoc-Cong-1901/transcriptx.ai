🔥 TranscriptX – YouTube Video Summarizer (Japanese / ja)

URL:
/ja/youtube-video-summarizer

Intent chính:

Tóm tắt video YouTube bằng AI (miễn phí) — `YouTube要約`

Trang này nhắm đến người dùng Nhật muốn **nắm ý chính của một video YouTube mà không phải xem hết** — dán link, AI đọc toàn bộ nội dung rồi trả về bản tóm tắt ngắn gồm kết luận, các ý chính và chi tiết đáng nhớ.

---

## ✅ TRANG NÀY SẠCH XUNG ĐỘT VỚI 4 TRANG YOUTUBE KIA

Đã kiểm chéo toàn cụm 5 trang YouTube: **0 keyword trùng** với `youtube-transcript`, `download-youtube-transcript`, `youtube-subtitle-downloader` ở **cả 13 ngôn ngữ**.

Lý do: `要約` là intent tách bạch hoàn toàn — người tìm muốn **ý chính**, không phải **toàn văn** (`文字起こし`) hay **file phụ đề** (`字幕`). Không cần nhường hay neo đẩy đi cụm nào.

Ranh giới vẫn phải giữ trong nội dung — bản EN cài **3 chốt phân định**, bản ja dịch sát cả ba:

1. **S1 đoạn 3** — *"A transcript hands you every word; a summary decides which words were worth your time"* → `文字起こしは話された言葉をすべて渡します。要約はどの言葉が時間をかける価値があったのかを選び取ります。`
2. **FAQ 4** — *"What is the difference between a summary and a transcript?"* → `要約と文字起こしは何が違いますか？`
3. **S7** — đoạn 2 chứa cả **3 internal link**, dịch sát cả 3 vế.

Ngoài 3 chốt này, từ `文字起こし` **không được xuất hiện ở đâu khác**. Kết quả của trang này luôn gọi là `要約`.

---

## 🚨 LỖI DỮ LIỆU — DẤU CÁCH THỪA GIỮA MORPHEME

Danh sách `ja` trong `2_loc_kw.md` bị chèn **dấu cách giữa các morpheme** ở **cả 10/10 dòng**. Tiếng Nhật **không dùng dấu cách** — đây là lỗi định dạng của công cụ export, không phải cách người Nhật thực sự gõ.

| Dạng trong file (SAI) | Dạng đúng (dùng để viết `ja.json`) |
| --------------------- | ---------------------------------- |
| `youtube 要約` | `youtube要約` |
| `youtube 要約 ai` | `youtube要約ai` |
| `youtube 動画 要約` | `youtube動画要約` |
| `youtube 要約 サイト` | `youtube要約サイト` |
| `youtube 内容 要約` | `youtube内容要約` |
| `youtube 動画 要約 ツール` | `youtube動画要約ツール` |
| `動画 要約 youtube` | `動画要約youtube` |
| `youtube 動画 要約 無料` | `youtube動画要約無料` |
| `youtube 要約 自動` | `youtube要約自動` |
| `youtube url 要約` | `youtube url要約` |

**Quy tắc xử lý:** ghi dạng đúng (viết liền) trong bảng keyword ở dưới, và **`ja.json` tuyệt đối viết liền**. Ranh giới duy nhất được giữ dấu cách là giữa từ Latin và từ Latin (`youtube url`).

**Số keyword thực: 10 keyword** (danh sách `ja` **không** dính 2 dòng nhãn `Keyword ideas` / `Keywords you provided` như `fr` và `vi`, cũng không có keyword rác lệch intent). Chất lượng danh sách này tốt — **2 cụm đạt `1K – 10K`**, 3 cụm `100 – 1K`.

---

## Từ khóa chính

**youtube要約 (1K–10K)** ✅ *đã search*

Cụm mạnh nhất và là **lõi chung** của gần như toàn bộ danh sách (`...ai`, `...サイト`, `...自動`, `動画...`, `内容...`), nên neo vào đây thì các đuôi tự phủ theo.

---

## Từ khóa phụ

### Nhóm 要約 (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube要約 | 1K–10K | ✅ đã search *(KW chính)* |
| youtube動画要約 | 100–1K | ✅ đã search |
| youtube内容要約 | 100–1K | ✅ đã search |
| 動画要約youtube | 10–100 | ✅ đã search |

### Nhóm AI / Tự động

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube要約ai | 1K–10K | ✅ đã search |
| youtube要約自動 | 0–10 | ✅ đã search |

### Nhóm Công cụ / Site

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube要約サイト | 100–1K | ✅ đã search |
| youtube動画要約ツール | 10–100 | ✅ đã search |

### Nhóm Miễn phí / Thao tác

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube動画要約無料 | 0–10 | ✅ đã search |
| youtube url要約 | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 長い動画要約 | — | 🔄 dịch bổ sung (long video) |
| podcast要約 | — | 🔄 dịch bổ sung (podcast) |
| 動画の要点 | — | 🔄 dịch bổ sung (key points) |
| 講義動画要約 | — | 🔄 dịch bổ sung (lecture) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

---

## Search Intent

Người dùng Nhật gặp một video YouTube dài — bài giảng, podcast, buổi thuyết trình, review 20 phút — và muốn **biết nó nói gì trong một phút** để quyết định có đáng xem hết không.

Họ kỳ vọng:

- Dán link (`URL`) là ra tóm tắt trong vài giây, không đăng nhập.
- AI đọc **toàn bộ video**, không phải chỉ phần mô tả hay vài phút đầu.
- Tóm tắt đủ ngắn để đọc nhanh nhưng có **con số, tên riêng, khuyến nghị cụ thể**, không chung chung.
- Nhận dạng tốt tiếng Nhật, và tóm tắt được video tiếng Anh **thành tiếng Nhật**.
- Miễn phí, không giới hạn độ dài video.

### Khác biệt so với bản tiếng Anh

1. **Phải chuẩn hóa dấu cách trước khi viết.** Bản EN không có vấn đề này. 10/10 keyword ja trong `2_loc_kw.md` bị chèn dấu cách giữa morpheme — nếu bê nguyên vào `ja.json` thì text sẽ sai chính tả tiếng Nhật. Xem khối lỗi dữ liệu ở trên.
2. **`AI` là tín hiệu cực mạnh của thị trường Nhật.** Cụm `youtube要約ai` đạt `1K – 10K`, **ngang với keyword chính**. Bản EN không có keyword `ai` nào tương đương. Bắt buộc đưa `AI` vào `title`, `description` và **H2 section 3**.
3. **`サイト` mạnh hơn `ツール`.** Người Nhật tìm `youtube要約サイト` (`100 – 1K`) nhiều gấp mười lần `youtube動画要約ツール` (`10 – 100`) — họ muốn một **trang web dùng ngay trên trình duyệt**, không phải phần mềm cài đặt. Nhấn "chạy trong trình duyệt, không cần cài" mạnh hơn bản EN; ưu tiên `サイト` ở section 6, để `ツール` ở FAQ.
4. **`URL` là từ người Nhật gõ, không phải `リンク`.** Cụm `youtube url要約` có thật. Dùng `URL` ở `placeholder`, `quickAnswer` và step 1; `リンク` chỉ dùng xen kẽ chống lặp.
5. **Thể `です・ます` xuyên suốt.** Bản EN có giọng cụt, sắc, nhiều câu ngắn kiểu tuyên bố (*"That trade is the entire value"*). Tiếng Nhật giữ nguyên độ sắc của ý nhưng phải bọc trong thể lịch sự — chống dài dòng bằng cách cắt câu, không bằng cách bỏ `です・ます`.

---

## Đối tượng người dùng

- Sinh viên, người đang học (quyết định bài giảng có đáng xem hết không, biến ý chính thành ghi chú ôn tập)
- Người đi làm (nắm nội dung buổi thuyết trình, họp báo cáo kết quả, phỏng vấn trong ngành giữa các cuộc họp)
- Nghiên cứu viên (quét nhanh nhiều video để chọn ra vài cái đáng xem kỹ và trích dẫn)
- Content creator, marketer (rút thông điệp cốt lõi từ video dài để làm bài đăng, kịch bản)
- Người nghe podcast trên YouTube muốn nắm ý trước khi nghe
- Người học tiếng Anh muốn hiểu video tiếng Anh qua bản tóm tắt tiếng Nhật

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ja.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng 4 `steps`, đúng **4 `items`** ở S4 và S5, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube要約 | youtube要約 *(KW chính)* |
| — | **quickAnswer** | youtube動画要約, youtube url要約 |
| 1 | 要約で手に入るもの | youtube内容要約, youtube動画要約 *(+ chốt phân định với 文字起こし)* |
| 2 | 全部見るのではなく要約する理由 | 動画要約youtube |
| 3 | YouTube動画をAIで要約する方法 | youtube要約ai, youtube要約自動, youtube url要約 |
| 4 | よい要約に入っているもの | *(4 items — kết luận / ý chính / chi tiết cụ thể / mạch video)* |
| 5 | 要約が役に立つ人 | *(4 items — sinh viên / người đi làm / nghiên cứu / creator)* |
| 6 | 100を超える言語で動画を要約 | youtube要約サイト *(+ nhấn tiếng Nhật)* |
| 7 | 要約だけでは足りないとき | *(3 internal link — chốt phân định)* |
| 8 | よくある質問 | youtube動画要約無料, youtube動画要約ツール + long-tail |
| — | **conclusion** | youtube要約, 無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- **S1 đoạn 3, FAQ 4 và S7 là ba chốt phân định với trang transcript** — dịch sát, không rút gọn. Đây là ba chỗ **duy nhất** được nhắc `文字起こし` như một khái niệm đối lập.
- **Section 7 chứa cả 3 internal link** trong đoạn 2 — dịch sát cả ba vế, mỗi vế một lý do dùng khác nhau.
- Nỗi lo nhận dạng tiếng Nhật xử lý **trong section 6**: thay ví dụ ngôn ngữ của bản EN (German/Japanese) bằng ví dụ có **tiếng Nhật ở phía nhận** (video tiếng Anh → tóm tắt tiếng Nhật) — không thêm câu mới.
- Chống lặp `要約`: xen kẽ `要点` / `内容` / `まとめ` / `結論` / `かいつまむ`. Nhưng **tên gọi kết quả luôn là `要約`**.
- `動画` và `ビデオ`: dùng `動画` xuyên suốt (đúng cách người Nhật gõ và đúng keyword). `ビデオ` không dùng.

---

## Không nên tối ưu cho các keyword

- `youtube文字起こし` / `youtube文字起こし方法` → **/ja/youtube-transcript**
- `youtube文字起こしダウンロード` → **/ja/download-youtube-transcript**
- `youtube字幕ダウンロード` / `youtube字幕保存` → **/ja/youtube-subtitle-downloader**
- **`youtube動画ダウンロード` / `youtube保存`** → intent tải VIDEO, SERP toàn downloader. **Trang này không tải gì cả** — nó **đọc và tóm tắt**.
  **Quy tắc cứng:** tránh `ダウンロード` làm động từ chính; nếu buộc phải nhắc thì phải có tân ngữ rõ ràng (`文字起こし`/`テキスト`/`ファイル`). **Tuyệt đối không viết `動画ダウンロード`.**
- `文章要約` / `テキスト要約` / `記事要約` → intent tóm tắt **CHỮ** (văn bản, bài viết), không phải video — không thuộc trang này. Không đưa vào `title`/`h2`.

---

## Internal linking

Section 7 đoạn 2 chứa **cả 3 link**:

- → `/ja/youtube-transcript` (cần toàn văn `文字起こし`, không phải ý chính)
- → `/ja/download-youtube-transcript` (cần lưu toàn văn thành file)

---

## Ghi chú kỹ thuật cho ja.json

- Thể **です・ます** nhất quán toàn trang, đồng bộ với `../youtube-subtitle-downloader/ja.json`.
- Giữ nguyên Latin: **TranscriptX, YouTube, AI**. `URL` viết hoa Latin.
- **VIẾT LIỀN — KHÔNG dấu cách thừa** giữa các morpheme tiếng Nhật. Đây là lỗi phải chủ động sửa từ nguồn keyword.
- Dấu câu tiếng Nhật: `。`, `、`, `—` (em dash dùng như bản EN). Không dùng `,` `.` ASCII trong câu tiếng Nhật.
- Cấu trúc: **8 section**, **8 FAQ**, S4 và S5 = `intro` 1 + `items` **4**, S1/S2 = `content` 3, S6/S7 = `content` 2, S3 = `steps` 4, conclusion = `content` 2. **KHÔNG có `specs`.**
- Internal link section 7 giữ cú pháp markdown, đổi path sang `/ja/...`.
