🔥 TranscriptX – Facebook Transcript (Japanese / ja)

URL:
/ja/facebook-transcript

Intent chính:

Facebook動画文字起こし（無料・オンライン）

Trang này là **bản tiếng Nhật của trang trụ (hub)** cụm Facebook. Nhắm đến người dùng Nhật có một video Facebook (bài đăng video, リール, Watch, bản Facebook Live đã lưu, video trong group/page) và muốn dán link để lấy toàn bộ lời nói thành văn bản — để đọc, tìm kiếm, sao chép, chỉnh sửa, trích dẫn hoặc lưu lại.

Gộp toàn bộ intent đồng nghĩa **文字起こし / テキスト化 / テキスト変換** vì tất cả cho ra **cùng một kết quả**: video Facebook → văn bản.

> ⚠️ **LỖI DỮ LIỆU 1 — KHOẢNG TRẮNG TRONG KEYWORD TIẾNG NHẬT (BẮT BUỘC XỬ LÝ)**
>
> Trong `2_loc_kw.md`, mọi keyword tiếng Nhật đều bị công cụ search chèn khoảng trắng sai giữa các morpheme, ví dụ `facebook 動画 文字 起こし`, `フェイス ブック 動画 文字 起こし`.
> **Tiếng Nhật KHÔNG dùng khoảng trắng giữa từ.** `文字起こし` là **MỘT từ**, không phải `文字` + `起こし`. Keyword thật là `facebook動画文字起こし`, `フェイスブック動画文字起こし`.
> Trong bảng dưới đây và trong `ja.json`, **toàn bộ keyword được ghi ở dạng viết đúng, đã bỏ hết khoảng trắng thừa**. Nếu để nguyên khoảng trắng, chuỗi sẽ không khớp truy vấn thật của người dùng và trông như dịch máy.

> ⚠️ **LỖI DỮ LIỆU 2 — KEYWORD CUỐI THIẾU DÒNG VOLUME**
>
> Dòng cuối của section `## Japanese (ja)` là `facebook 動画 文字 起こし ツール` nhưng **không có dòng volume theo sau** (file gốc bị cắt). Đây vẫn là **keyword hợp lệ, đúng intent** — ghi Volume `—`, Nguồn `✅ đã search (thiếu volume trong file gốc)`. Không được loại bỏ chỉ vì thiếu số liệu.

> ⚠️ **LỖI DỮ LIỆU 3 — `facebook` Latin vs `フェイスブック` katakana**
>
> Danh sách có **cả hai dạng**: 11/12 keyword viết `facebook` bằng chữ Latin, chỉ 1 keyword dùng katakana `フェイスブック動画文字起こし`.
> Đây là thực tế gõ phím tiếng Nhật: người dùng Nhật **gõ tên nền tảng nước ngoài bằng Latin** (không cần chuyển IME), nên dạng Latin chiếm gần hết truy vấn. Katakana chỉ xuất hiện khi người dùng gõ toàn câu bằng IME tiếng Nhật.
>
> **Chiến lược áp dụng:**
> - **`Facebook` Latin** dùng cho `seo.title`, `hero.h1`, **toàn bộ H2**, `description`, `ogTitle` — bám dạng chiếm đa số volume. Viết hoa chữ F (`Facebook`) vì đó là tên riêng; Google normalize hoa/thường nên không mất khớp với `facebook` thường.
> - **`フェイスブック` katakana** phải xuất hiện **2–3 lần trong body** (section 1, section 5 hoặc FAQ) để bắt biến thể katakana. **KHÔNG** đưa katakana vào title/H1/H2 — sẽ làm loãng dạng Latin mạnh hơn.
> - Không dùng `FB` viết tắt ở bất kỳ đâu — không có volume.

> ✅ **Không có nhiễm intent trong danh sách đã search.** Toàn bộ 12 keyword tiếng Nhật đều đúng intent video Facebook → 文字起こし/テキスト. **Không loại keyword nào trong danh sách.** Riêng `facebook動画字幕テキスト` là **intent lân cận** (phụ đề) — giữ lại nhưng bị giới hạn vị trí, xem ghi chú bên dưới.

---

## Từ khóa chính

facebook動画文字起こし (0–10) ✅ *đã search*

> `文字起こし` là **thuật ngữ trung tâm của thị trường Nhật** — một danh từ nghiệp vụ độc lập (có cả ngành dịch vụ 文字起こし代行), không phải bản dịch tạm của "transcribe". Nó xuất hiện trong **9/12 keyword** của danh sách. Đây là **trục chính** của toàn trang: phải có trong `seo.title`, `hero.h1`, `description` và lặp lại đều trong body. Các biến thể `テキスト化` / `テキスト変換` chỉ là nhánh phụ.

---

## Từ khóa phụ

### Nhóm Core 文字起こし (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook動画文字起こし | 0–10 | ✅ đã search *(KW chính)* |
| facebook動画文字起こし無料 | 0–10 | ✅ đã search |
| フェイスブック動画文字起こし | 0–10 | ✅ đã search *(biến thể katakana — chỉ dùng body)* |
| Facebook動画の文字起こし方法 | — | 🔄 dịch bổ sung (how to transcribe a Facebook video) |

### Nhóm テキスト化 / テキスト変換 (chuyển đổi — tương ứng "facebook video to text")

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook動画テキスト化 | 0–10 | ✅ đã search |
| facebook動画テキスト変換 | 0–10 | ✅ đã search |
| facebook動画音声テキスト化 | 0–10 | ✅ đã search |
| Facebook動画をテキストに変換 | — | 🔄 dịch bổ sung (biến thể dạng câu) |

### Nhóm Định dạng nội dung Facebook (Live / Reels)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebookライブ文字起こし | 0–10 | ✅ đã search |
| facebookリール文字起こし | 0–10 | ✅ đã search |
| Facebookライブ配信の文字起こし | — | 🔄 dịch bổ sung (saved Live) |

### Nhóm Công cụ / AI / Site

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook動画文字起こしAI | 0–10 | ✅ đã search |
| facebook動画文字起こしサイト | 0–10 | ✅ đã search |
| facebook動画文字起こしツール | — | ✅ đã search *(thiếu volume trong file gốc)* |
| 無料文字起こしツール | — | 🔄 dịch bổ sung (free tool) |
| 登録不要 / インストール不要 | — | 🔄 dịch bổ sung (no sign-up / no install) |

### Nhóm intent lân cận (giữ — CHỈ body/FAQ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| facebook動画字幕テキスト | 0–10 | ✅ đã search — ⚠️ **KHÔNG vào title/H1/H2** |

> ⚠️ **Xử lý `字幕`:** đây là intent **lân cận**, không phải intent trang này. Người tìm `字幕` có thể đang muốn *bật/tải phụ đề*, không phải lấy transcript. Giữ keyword để phủ ngữ nghĩa nhưng **chỉ đặt trong body** — cụ thể: section 4 (nói về việc công cụ chạy được cả khi video không có 字幕), section 7 (khi nói về xuất SRT/VTT), FAQ 5 (câu hỏi "video không có phụ đề thì sao"). **Tuyệt đối không** đưa `字幕` vào `seo.title`, `hero.h1` hay bất kỳ `h2` nào — sẽ làm lệch page type sang trang phụ đề.

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải trong body để phủ ngữ nghĩa, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Nhật có một video Facebook — thường là **Facebook Live đã lưu** (ウェビナー, 説明会, オンライン講座, 自治体・団体の配信), video trong グループ / ページ, hoặc リール — và muốn lấy nội dung lời nói thành văn bản để đọc, tìm kiếm, trích dẫn, làm 議事録/メモ hoặc lưu trước khi bị xóa.

Họ thường kỳ vọng:

- Chỉ cần **dán link (URLを貼るだけ)**, không tải file, không cài app.
- **Miễn phí thật** — `無料` có hẳn keyword riêng, là modifier mạnh nhất của thị trường Nhật sau `文字起こし`.
- **Không cần đăng ký** (`登録不要`) và **không cần cài đặt** (`インストール不要`) — đây là kỳ vọng mặc định, không phải điểm cộng.
- Chạy được cả khi video **không có 字幕** sẵn.
- **Độ chính xác cao (`精度`)** — người dùng Nhật nhạy cảm với chất lượng hơn hầu hết thị trường khác; đây là yếu tố quyết định ở lại hay thoát.
- Nhận dạng tốt **tiếng Nhật** (nhiều công cụ nước ngoài chỉ chạy tốt tiếng Anh) — nỗi lo lớn nhất.
- **話者分離** (tách người nói) — quan trọng với Live / 対談 / インタビュー.

### Khác biệt so với bản tiếng Anh

1. **`文字起こし` là danh từ nghiệp vụ độc lập, không phải bản dịch của "transcribe".** Ở Nhật đây là cả một ngành dịch vụ (文字起こし代行) với quy chuẩn riêng. Vì vậy nó là **trục chính xuyên suốt trang** — xuất hiện trong 9/12 keyword — chứ không phải một nhóm keyword phụ như "transcribe" ở bản EN. Bản EN chia đều giữa `transcript` (danh từ) và `transcribe` (động từ); bản JA gần như chỉ có một dạng danh từ hóa duy nhất.
2. **`無料` mạnh hơn "free" của bản EN.** Bản EN chỉ có 1 FAQ nói về free; bản JA cần `無料` xuất hiện ở `seo.title`, `hero.h1` subtitle, section 4, FAQ 1–2 và conclusion — vì có hẳn keyword `facebook動画文字起こし無料`.
3. **Nhóm "công cụ" (ツール / サイト / AI) có 3 keyword riêng — bản EN chỉ có `facebook transcript generator` + `facebook transcript ai`.** Người Nhật tìm kiếm theo **loại công cụ** (`〜ツール`, `〜サイト`) nhiều hơn theo hành động. Section 4 phải nói rõ đây là một **ツール／サイト** chạy trên trình duyệt, không chỉ là "generator".
4. **Không có keyword dạng câu hỏi/động từ ("how to...").** Bản EN có `transcribe facebook video` dạng động từ; tiếng Nhật hoàn toàn dùng cụm danh từ ghép. Khi dịch H2 số 3 phải dùng dạng `〜する方法` chứ không dịch máy thành câu mệnh lệnh.
5. **Vấn đề `facebook` Latin vs `フェイスブック` katakana** không tồn tại ở bản EN — xem cảnh báo đầu file.
6. **Văn phong:** thể `です・ます` lịch sự chuẩn cho trang sản phẩm (nhất quán với `/ja/audio-to-text`); tránh 体言止め dày đặc kiểu quảng cáo và tránh 命令形 thô.

---

## Đối tượng người dùng

- Người xem **Facebookライブ配信** (ウェビナー, 説明会, Q&A, オンライン講座, 自治体の配信)
- Admin グループ / Facebookページ
- Marketing / SNS運用担当者
- Học sinh, sinh viên, nhà nghiên cứu (講義・セミナーの録画配信)
- Nhà báo / biên tập viên cần trích dẫn phát biểu chính xác từ video Facebook
- Content creator tái sử dụng nội dung (リール → 記事, X投稿, ブログ)
- Người làm dịch vụ 文字起こし代行
- Người cần lưu nội dung video trước khi bị xóa
- Người khiếm thính hoặc ở nơi không bật được tiếng (電車内など)

---

## Map H2 → keyword (bám ĐÚNG 9 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ja.json` phải dịch đúng 9 section của `en.json`, cùng số đoạn `content`, đúng 10 `specs`, đúng 4 `steps`, đúng 5 `items` ở section 6, đúng 9 FAQ, đúng 2 đoạn `conclusion`. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Facebook動画文字起こし | facebook動画文字起こし *(KW chính; `無料` ở subtitle)* |
| — | **quickAnswer** | Facebook動画の文字起こし方法 🔄, facebook動画文字起こし |
| 1 | Facebook動画文字起こしとは？ | facebook動画文字起こし, facebook動画テキスト化 *(+ `フェイスブック` katakana 1 lần)* |
| 2 | Facebook動画文字起こしの概要 | *(bảng thông số — 無料 / 100言語以上 / 登録不要 / インストール不要)* |
| 3 | Facebook動画を文字起こしする方法 | Facebook動画の文字起こし方法 🔄, facebook動画文字起こし |
| 4 | 字幕なしでも使えるFacebook動画文字起こしAIツール | facebook動画文字起こしAI, facebook動画文字起こしツール, facebook動画文字起こしサイト, facebook動画音声テキスト化, facebook動画字幕テキスト *(chỉ trong body)* |
| 5 | Facebook動画をテキスト化する | facebook動画テキスト化, facebook動画テキスト変換 *(+ `フェイスブック` katakana 1 lần)* |
| 6 | Facebookで文字起こしできる動画の種類 | facebookライブ文字起こし *(item 1)*, facebookリール文字起こし *(item 3)* |
| 7 | コピー・編集・翻訳・ダウンロード | *(internal link sang /ja/youtube-transcript, /ja/tiktok-transcript, /ja/audio-to-text; nhắc SRT/VTT = 字幕ファイル)* |
| 8 | 精度と対応言語 | facebook動画文字起こし *(+ nhấn 日本語の精度)* |
| 9 | よくある質問 | facebook動画文字起こし無料, facebook動画文字起こしサイト, facebook動画字幕テキスト + long-tail |
| — | **conclusion** | facebook動画文字起こし, 無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- Nỗi lo **"công cụ có nhận dạng được tiếng Nhật không"** xử lý **bên trong section 8** bằng cách thay ví dụ ngôn ngữ của bản EN (Spanish Live / Tagalog Reel) bằng ví dụ có **tiếng Nhật** và ngôn ngữ khác — không thêm câu, không thêm H2.
- Keyword `facebookライブ文字起こし` đặt vào **item số 1 của section 6** (Saved Facebook Live) — đúng chỗ, không cần section mới.
- Keyword `facebookリール文字起こし` đặt vào **item số 3 của section 6** (Reels), viết nguyên cụm.
- Keyword `facebook動画音声テキスト化` đặt trong **section 4** (chỗ bản EN nói "builds the text from the audio itself") — đúng ngữ cảnh "âm thanh → text".
- Keyword `facebook動画字幕テキスト` chỉ xuất hiện ở **section 4** (video không có 字幕 vẫn chạy được), **section 7** (SRT/VTT là 字幕ファイル) và **FAQ 5**. **KHÔNG** vào H2.
- Biến thể katakana `フェイスブック` chèn **2–3 lần**: một lần ở **section 1**, một lần ở **section 5**, tối đa một lần ở **FAQ 7** (câu hỏi về Facebookアカウント). Không nhiều hơn — sẽ đọc như lặp thừa.
- `facebook動画文字起こしサイト` và `facebook動画文字起こし無料` gom vào **FAQ 1 và FAQ 2** — đúng chỗ bản EN đã có sẵn câu hỏi "for free" / "free generator".
- Bản EN section 1 có câu meta về "getting the transcript / generating with AI / converting to text đều là một" — dịch thành `文字起こし・テキスト化・テキスト変換` để gom 3 nhóm keyword trong đúng một câu đã có sẵn.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- YouTube文字起こし / YouTube動画テキスト化 / YouTube字幕テキスト → **/ja/youtube-transcript**
- TikTok文字起こし / TikTok動画テキスト化 → **/ja/tiktok-transcript**
- 音声文字起こし / 音声ファイル文字起こし / mp3文字起こし / 録音文字起こし / 文字起こしツール *(dạng chung không có Facebook)* → **/ja/audio-to-text** (nguồn là **file âm thanh**, không phải video Facebook)
- テキスト読み上げ / 音声合成 → **NGƯỢC intent**, thuộc trang Text-to-Speech
- **facebook動画ダウンロード / フェイスブック動画保存 / facebook動画ダウンロードサイト** → intent **tải video**, KHÔNG phải transcript. Đây là nhóm nhiễm nguy hiểm nhất của cụm Facebook tiếng Nhật vì volume lớn hơn hẳn và SERP hoàn toàn là downloader — kéo vào sẽ làm lệch page type.
- facebook字幕ダウンロード / 動画に字幕をつける → intent **tạo/tải phụ đề**, chỉ được nhắc trong body khi nói về xuất SRT/VTT, không tối ưu ở cấp H1/H2

---

## Internal linking

- ↔ /ja/youtube-transcript, /ja/tiktok-transcript (cross-cluster: cùng nhu cầu 文字起こし, nền tảng khác)
- → /ja/audio-to-text (khi user có **file âm thanh** thay vì video Facebook)

---

## Ghi chú kỹ thuật cho ja.json

- `lang="ja"`, `dir="ltr"`.
- **Tuyệt đối không chèn khoảng trắng vào keyword tiếng Nhật.** Khoảng trắng trong `2_loc_kw.md` là lỗi export của công cụ search, không phải chính tả.
- Giữ nguyên Latin, không katakana hóa: **TranscriptX, TXT, DOCX, PDF, SRT, VTT, Facebook, URL**.
- Theo cách người Nhật thực sự gọi: **リール** (Reels — katakana, đúng theo keyword `facebookリール文字起こし`), **ライブ配信** hoặc **Facebookライブ** (Live — đúng theo keyword `facebookライブ文字起こし`), **Watch** giữ Latin (tên tính năng chính thức, ít dùng trong hội thoại).
- `Facebook` viết hoa chữ F trong nội dung; katakana `フェイスブック` chỉ 2–3 lần trong body như ghi chú trên.
- Số đếm dùng chữ số Latin (100+, 5).
- Dấu câu dùng `。`, `、` chuẩn Nhật; không dùng `,` `.` phương Tây. Dấu `・` cho liệt kê ngắn (TXT・DOCX・PDF・SRT・VTT).
- Internal link trong `sections[6]` (section 7) giữ nguyên cú pháp markdown, đổi path: `[YouTube文字起こし](/ja/youtube-transcript)`, `[TikTok文字起こし](/ja/tiktok-transcript)`, `[音声文字起こし](/ja/audio-to-text)`.
- **Thể văn: `です・ます` thống nhất toàn trang** — nhất quán với `/ja/audio-to-text/ja.json` đã duyệt. Không trộn `である`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, 9 sections, 10 specs, 4 steps, 5 items (section 6), 9 FAQ, `conclusion` h2 + 2 đoạn.
