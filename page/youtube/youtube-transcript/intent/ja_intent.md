🔥 TranscriptX – YouTube Transcript (Japanese / ja)

URL:
/ja/youtube-transcript

Intent chính:

youtube文字起こし / YouTube動画の文字起こしをオンラインで無料で取得する

Trang này nhắm đến người dùng nói tiếng Nhật muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán URL là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt với người dùng

> Trang này là **hub** nên **giữ trọn họ từ `文字起こし`** (`文字起こし`, `文字に起こす`, `トランスクリプト`), **và cả nhóm `テキスト抽出` / `テキスト化` / `からテキスト`**.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ **12 keyword** trong danh sách `## Japanese (ja)` đều thuộc về trang này, kể cả nhóm `youtube動画テキスト化` / `youtubeからテキスト` / `youtube字幕テキスト抽出` — vì các cụm đó **có chữ `youtube`**, nên không đụng trang generic `/ja/video-to-text`.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **Section 11 (`文字起こしをコピー・編集・翻訳・ダウンロード`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (`文字起こし` vs `字幕`) — chốt với `/ja/youtube-subtitle-downloader`.
- **FAQ 4** (`生成する` vs `抽出する`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — KIỂM TRA VÀ KẾT QUẢ

Đã rà section `## Japanese (ja)` trong `2_loc_kw.md` theo đúng tiền lệ của `intent/es_intent.md`:

| Loại lỗi | Có trong section `ja`? | Ghi chú |
| -------- | ---------------------- | ------- |
| `Keyword ideas` / `Keywords you provided` (nhãn giao diện công cụ search) | ❌ **Không có** | Lỗi export này xuất hiện ở `es`, `fr`, `vi` — section `ja` sạch. |
| `texttomp3` (TTS — intent NGƯỢC) | ❌ **Không có** | Xuất hiện ở `es` và `fr`. Section `ja` sạch. |
| Cụm garbled / sai chính tả | ❌ **Không có** | Cả 12 dòng đều là tiếng Nhật hợp lệ. |
| **Dấu cách thừa giữa morpheme** | ✅ **CÓ — cả 12/12 dòng** | Lỗi tokenizer khi export, xem bảng dưới. |

### ⚠️ Lỗi dấu cách thừa — lỗi duy nhất của section `ja`

Công cụ export đã **tách từ tiếng Nhật theo morpheme rồi chèn dấu cách**. `文字起こし` là **MỘT từ**, không phải `文字` + `起こし`. Tiếng Nhật **không dùng dấu cách giữa từ**. Nghiêm trọng nhất là `トラン スクリプト` — cắt đôi giữa một từ katakana.

| Dòng trong `2_loc_kw.md` (SAI) | Dạng đúng (dùng trong `ja.json`) | Volume |
| ------------------------------ | -------------------------------- | ------ |
| `youtube 文字 起こし` | `youtube文字起こし` | 1K – 10K |
| `youtube 動画 文字 起こし` | `youtube動画文字起こし` | 100 – 1K |
| `youtube 音声 文字 起こし` | `youtube音声文字起こし` | 100 – 1K |
| `youtube 文字 起こし サイト` | `youtube文字起こしサイト` | 100 – 1K |
| `youtube 文字 起こし ツール` | `youtube文字起こしツール` | 10 – 100 |
| `youtube 動画 テキスト 化` | `youtube動画テキスト化` | 10 – 100 |
| `youtube 文字 起こし 自動` | `youtube文字起こし自動` | 10 – 100 |
| `youtube 字幕 テキスト 抽出` | `youtube字幕テキスト抽出` | 0 – 10 |
| `youtube から テキスト` | `youtubeからテキスト` | 0 – 10 |
| `youtube トラン スクリプト` | `youtubeトランスクリプト` | 100 – 1K |
| `youtube 文字 起こし 無料` | `youtube文字起こし無料` | 100 – 1K |
| `youtube 動画 文字 に 起こす` | `youtube動画文字に起こす` | 0 – 10 |

> Trong file intent này ghi **dạng đúng**. Trong `ja.json` **viết liền tuyệt đối**, không một dấu cách nào giữa ký tự CJK. Kiểm bằng grep, kết quả phải = 0.

### 📊 Số keyword thực: **12 − 0 = 12**

Section `ja` là một trong số ít section **không dính rác keyword** — chỉ dính lỗi định dạng dấu cách.

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói, タイムスタンプ tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **取得 / get** — lấy 文字起こし có sẵn,
- **生成 / generate** — dựng 文字起こし từ audio khi video không có 字幕,
- **抽出 / extract** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

Kết quả trang này **luôn gọi là `文字起こし` hoặc `テキスト`** — **không bao giờ** gọi là `字幕`.

---

## Từ khóa chính

**youtube文字起こし (1K–10K)** ✅ *đã search* → **H1: `YouTube文字起こし`**

Đây là cụm mạnh nhất của tiếng Nhật ở trang này. Toàn bộ trang được xây quanh nó: xuất hiện ở `title`, `h1`, `ogTitle`, `schemaName`, H2 của S1 và S2, `conclusion.h2` và FAQ 1–2.

---

## Từ khóa phụ

### Nhóm `文字起こし` (trục chính — danh từ/động từ ghép)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube文字起こし | 1K–10K | ✅ đã search *(KW chính)* |
| youtube動画文字起こし | 100–1K | ✅ đã search |
| youtube音声文字起こし | 100–1K | ✅ đã search |
| youtube文字起こし無料 | 100–1K | ✅ đã search |
| youtube動画文字に起こす | 0–10 | ✅ đã search |

### Nhóm định danh công cụ (`サイト` / `ツール` / `自動`)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube文字起こしサイト | 100–1K | ✅ đã search |
| youtube文字起こしツール | 10–100 | ✅ đã search |
| youtube文字起こし自動 | 10–100 | ✅ đã search |

### Nhóm `テキスト` (chuyển đổi / trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube動画テキスト化 | 10–100 | ✅ đã search |
| youtube字幕テキスト抽出 | 0–10 | ✅ đã search |
| youtubeからテキスト | 0–10 | ✅ đã search |

### Nhóm katakana (từ mượn)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtubeトランスクリプト | 100–1K | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 話者分離 | — | 🔄 dịch bổ sung (speaker separation) |
| タイムスタンプ | — | 🔄 dịch bổ sung (timestamps) |
| 100言語以上 | — | 🔄 dịch bổ sung (100+ languages) |
| 登録不要 / 無料 | — | 🔄 dịch bổ sung (no sign-up / free) |
| 自動字幕 / 投稿者がつけた字幕 | — | 🔄 dịch bổ sung (auto-captions / creator captions) |
| 書き出し形式 | — | 🔄 dịch bổ sung (export formats) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng Nhật muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán URL YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu JA ⇄ EN rất nặng ở mảng học thuật và doanh nghiệp.
- Hoạt động **cả khi video không có 字幕** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (対談, パネルディスカッション).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Nhật chỉ có MỘT trục từ áp đảo, ngược với tiếng TBN có 3 họ song song.** `文字起こし` chiếm **9/12 keyword** trong danh sách, gồm cả cụm chính 1K–10K. Bản EN chia đều giữa `transcript` (danh từ) / `transcribe` (động từ) / `transcription`; tiếng Nhật gộp tất cả vào một danh từ ghép duy nhất. Hệ quả: **không cần đặt động từ làm H1** như bản `es` — H1 giữ đúng dạng danh từ `YouTube文字起こし`, khớp bản EN. Việc phủ keyword làm bằng **hậu tố** (`サイト`, `ツール`, `自動`, `無料`), không bằng cách đổi cấu trúc câu.

2. **Nhóm định danh công cụ (`サイト` / `ツール`) là intent riêng, bản EN không có.** `youtube文字起こしサイト` (100–1K) và `youtube文字起こしツール` (10–100) cho thấy người Nhật gõ thẳng "trang web/công cụ làm việc này" chứ không gõ "how to". Bản EN không có keyword nào dạng "youtube transcript site/tool" có volume. Phải cấp trọn **H2 của S4** (`YouTube文字起こしを自動生成するツール`) và rải `文字起こしサイト` trong body S4 — đây là chỗ duy nhất trong bài gọi TranscriptX bằng danh từ "サイト".

3. **Không có cụm "how to" có volume — ngược hẳn bản `es`.** Bản `es` có `como transcribir un video de youtube` đạt 1K–10K, phải cấp trọn H2 của S3. Tiếng Nhật **không có cụm `youtube文字起こし方法` / `やり方` nào trong danh sách**. Vì vậy S3 (`steps`) **không phải section mang keyword nặng** — chỉ dịch sát bản EN với H2 `YouTube動画を文字起こしする方法`, và `quickAnswer.question` cũng chỉ là câu hỏi tự nhiên, không gánh keyword riêng.

4. **`字幕` là bẫy cannibalization đặc thù của tiếng Nhật, không tồn tại ở bản EN.** Tiếng Anh phân biệt rõ `transcript` / `captions` / `subtitles`. Tiếng Nhật **gộp cả `captions` lẫn `subtitles` vào một từ `字幕`**, mà `字幕` lại thuộc trọn trang `/ja/youtube-subtitle-downloader`. Bản EN dùng `captions` ~6 chỗ mà không gặp rủi ro; bản `ja` phải có **quy tắc riêng** (xem mục dưới) để `字幕` không bao giờ leo lên heading và không bao giờ được dùng để gọi kết quả của trang này.

5. **`ダウンロード` phải kỷ luật hơn bản EN.** `youtube 動画 ダウンロード` trong tiếng Nhật là cụm khổng lồ, SERP toàn công cụ tải MP4. Kỷ luật cứng: `ダウンロード` / `保存` **chỉ** đi với `文字起こし` / `テキスト` / `ファイル`, **không bao giờ** với `動画`. Bản EN không chịu áp lực này ở cùng mức.

6. **`トランスクリプト` (katakana) là từ mượn có volume thật (100–1K) nhưng KHÔNG dùng làm từ chính.** Người Nhật có gõ nó, nhưng `文字起こし` mạnh hơn một bậc và tự nhiên hơn nhiều trong văn viết. Bản EN không có tình huống "hai cách gọi cùng một thứ, một bản địa một mượn". Xử lý: dùng `文字起こし` xuyên suốt, **không** ép `トランスクリプト` vào heading hay body — cụm này để trang tự bắt qua ngữ cảnh thương hiệu `TranscriptX` (bản thân tên thương hiệu đã là chuỗi Latin gần khớp).

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script để đưa vào dataset hoặc prompt)
- Nhân viên văn phòng Nhật cần 議事録 / tài liệu nội bộ từ video công khai
- Marketer đa ngôn ngữ JA ⇄ EN
- Người khiếm thính và người xem không bật được âm thanh

---

## ⚠️ Quy tắc dùng từ `字幕` (mục riêng — quan trọng nhất của bản ja)

Tiếng Nhật gộp `captions` và `subtitles` thành một từ `字幕`, trong khi `字幕` thuộc trọn về `/ja/youtube-subtitle-downloader`. Quy tắc:

### ✅ ĐƯỢC dùng `字幕` ở đúng 3 tình huống

1. **Nói về caption có sẵn của YouTube** — luôn có định ngữ, không bao giờ để trần:
   - `自動字幕` (auto-captions)
   - `投稿者がつけた字幕` (creator-added captions)
   - `字幕ボタン` (caption button)
   - `字幕がない動画` / `動画に字幕がなくても` (video has no captions)
2. **Trỏ sang trang phụ đề ở S11** — anchor `YouTube字幕ダウンローダー` + câu dẫn `字幕ファイルそのものが必要な場合`.
3. **FAQ 10** — câu hỏi so sánh `文字起こしと字幕は何が違いますか`. Đây là chốt phân định với trang phụ đề, bản EN cũng có đúng câu này.

### 🚫 CẤM tuyệt đối

- **`字幕` KHÔNG được xuất hiện trên bất kỳ `h1` / `h2` / `h3` nào.** Nếu lên heading, trang này sẽ tranh chấp trực tiếp với `/ja/youtube-subtitle-downloader`.
- **KHÔNG BAO GIỜ gọi kết quả của trang này là `字幕`.** Kết quả **luôn** là `文字起こし` hoặc `テキスト`.
- **KHÔNG dùng `字幕` để trần** khi nói về caption của YouTube — luôn thêm định ngữ (`自動`, `投稿者がつけた`).

### Vị trí `字幕` thực tế trong `ja.json` (đã kiểm)

| Vị trí | Cách dùng | Hợp lệ vì |
| ------ | --------- | --------- |
| S2 `specs` label `字幕がない動画` | caption có sẵn | Là `label`, KHÔNG phải heading |
| S4 `content[0]` `自動字幕` / `投稿者がつけた字幕` | caption có sẵn | Có định ngữ |
| S4 `content[1]` `字幕ボタン` | caption có sẵn | Có định ngữ |
| S4 `content[2]` `自動字幕` | caption có sẵn | Có định ngữ |
| S5 `content[0]` `すでに字幕がある場合` | caption có sẵn | Điều kiện, không phải kết quả |
| S8 `intro` + `items` | caption có sẵn của YouTube | Section so sánh |
| S10 `intro` `字幕がないこと自体は問題になりません` | caption có sẵn | Điều kiện |
| S11 `content[1]` `字幕ファイル` + anchor `YouTube字幕ダウンローダー` | link sang trang phụ đề | Chốt phân định |
| FAQ 3 `q` + `a` | `動画に字幕がなくても` | FAQ `q` KHÔNG phải heading; bản EN có đúng câu này |
| FAQ 8 `a` `字幕ファイル` | file phụ đề | Nói về SRT/VTT |
| FAQ 10 `q` + `a` | so sánh 文字起こし vs 字幕 | Chốt phân định, bản EN có đúng câu này |
| conclusion `content[0]` `既存の字幕から抽出` | caption có sẵn | Có định ngữ |

> Kiểm bắt buộc: `字幕` xuất hiện ở `h1`/`h2`/`h3`/`title`/`ogTitle` → phải **0 kết quả**. Ở `q` của FAQ 3 và FAQ 10 là **hợp lệ** (đúng bản EN, đúng tiền lệ FAQ 10 của bản pilot `es`).

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `ja.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** YouTube文字起こし | youtube文字起こし *(KW chính)* |
| — | **quickAnswer** | youtube文字起こし *(không có cụm "how to" riêng — xem Khác biệt #3)* |
| 1 | YouTube文字起こしとは？ | youtube文字起こし, youtube動画文字起こし |
| 2 | YouTube文字起こしの概要 *(`specs` × 10)* | youtube文字起こし |
| 3 | YouTube動画を文字起こしする方法 *(`steps` × 4)* | youtube動画文字起こし, youtube動画文字に起こす |
| 4 | YouTube文字起こしを自動生成するツール | youtube文字起こしツール, youtube文字起こしサイト, youtube文字起こし自動 |
| 5 | YouTube動画からテキストを抽出する | youtube字幕テキスト抽出, youtubeからテキスト, youtube動画テキスト化 |
| 6 | YouTube文字起こしの活用方法 *(`items` × 6)* | youtube動画文字起こし |
| 7 | あらゆる言語でYouTubeを文字起こし *(`content` × 2)* | youtube音声文字起こし, youtube文字起こし |
| 8 | TranscriptXとYouTube標準の文字起こしの比較 *(`items` × 2)* | youtube文字起こし自動 |
| 9 | 精度とそれを左右する要素 | *(E-E-A-T, không nhắm KW)* |
| 10 | YouTube文字起こしがうまくいかない場合 *(`items` × 5)* | youtube文字起こし |
| 11 | 文字起こしをコピー・編集・翻訳・ダウンロード | *(4 internal link — chốt phân định)* |
| 12 | よくある質問 *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion** *(3 đoạn)* | youtube文字起こし, youtube文字起こし無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- **S2 tái dùng đúng nhãn `specs` đã duyệt ở `/ja/video-to-text/ja.json`** khi nhãn trùng — **8/10 nhãn tái dùng nguyên văn**: `料金`, `アカウント登録`, `インストール`, `対応言語`, `話者分離`, `タイムスタンプ`, `対応デバイス`, `書き出し形式`. Hai nhãn mới riêng của trang này: **`入力`** (Input — URL video YouTube, thay cho `ファイルサイズ制限`/`対応形式` của trang upload file) và **`字幕がない動画`** (Works when the video has no captions).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại** — S4 giữ nhóm `ツール`/`サイト`/`自動`, S5 giữ nhóm `テキスト抽出`/`テキスト化`/`からテキスト`.
- **S8 là section so sánh** với 文字起こし tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. Đây là section dùng `字幕` dày nhất; tất cả đều nói về caption có sẵn của YouTube, không phải kết quả của TranscriptX.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào.
- **Kỷ luật `ダウンロード` / `保存`:** chỉ đi với `文字起こし` / `テキスト` / `ファイル` / `TXT、DOCX、PDF、SRT、VTT`. **Không bao giờ** viết `動画をダウンロード` — kể cả ở S3 bước 2 (bản EN nói "no file to download first" → dịch `先にダウンロードしておくファイルもありません`, giữ `ファイル`, không dùng `動画`).
- **Thể `です・ます` xuyên suốt**, kể cả trong `specs.value` dạng cụm danh từ (`無料`, `不要`, `対応` — đây là dạng bảng, chấp nhận thể ngắn, khớp `/ja/video-to-text/ja.json`).
- **Viết liền tuyệt đối, KHÔNG dấu cách giữa ký tự CJK.** Đây là lỗi duy nhất của danh sách keyword nguồn, tuyệt đối không mang vào `ja.json`.
- **Dấu câu:** dùng `、` và `。` kiểu Nhật. Danh sách format dùng `、` (`TXT、DOCX、PDF、SRT、VTT`), không dùng dấu phẩy Latin.
- Nhấn `無料` ở `title`, `description`, `hero.subtitle`, S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN, đồng thời phủ cụm `youtube文字起こし無料`.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`youtube文字起こしダウンロード` / `youtubeトランスクリプト保存`** → **`/ja/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`youtube字幕ダウンロード` / `youtube字幕抽出` / `youtube srt ダウンロード` / `youtube vtt`** → **`/ja/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). **Nhóm `字幕` để trần thuộc trọn về trang đó** — xem mục quy tắc `字幕` ở trên.
- **`youtube動画テキスト変換`**: giữ ở hub này — không còn trang riêng cho cách gọi "動画をテキストに". Cụm `youtube動画テキスト化` cũng giữ ở đây vì đúng intent 文字起こし.
- **`youtube要約` / `youtube動画要約` / `youtubeまとめ`** → **`/ja/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`動画文字起こし` / `動画テキスト変換` / `ビデオ文字起こし` / `mp4文字起こし`** (không có chữ `youtube`) → **`/ja/video-to-text`** — **đã hoàn thành**. Mọi cụm dùng ở trang này **bắt buộc phải có `youtube`** trong cụm.
- **`音声文字起こし` / `文字起こしアプリ`** (không có `youtube`) → **`/ja/audio-to-text`**. Lưu ý cụm `youtube音声文字起こし` (100–1K) **có** chữ `youtube` nên vẫn thuộc trang này.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`youtube動画ダウンロード` / `youtube mp4 変換` / `youtube保存` / `youtubeダウンロードサイト`** → **intent tải file video**, SERP toàn công cụ tải MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng: `ダウンロード`/`保存` không bao giờ đứng cạnh `動画`.

### Sai intent hoàn toàn

- **`texttomp3` và mọi cụm TTS** (`テキスト読み上げ`, `文章を音声に`, `音声合成`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. *(Cụm này không xuất hiện trong section `ja` nhưng có ở `es`/`fr` — nêu ra để giữ nguyên tắc.)*
- **`youtube字幕の出し方` / `youtube字幕設定`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Thứ tự và vai trò:

| Link | Anchor (ja) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/ja/download-youtube-transcript` | YouTube文字起こしダウンロード | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/ja/youtube-subtitle-downloader` | YouTube字幕ダウンローダー | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/ja/youtube-video-summarizer` | YouTube動画要約 | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho ja.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/ja/...)`, đổi path sang `/ja/`.
- Thuật ngữ khớp các trang ja đã duyệt (`/ja/video-to-text/ja.json`): `タイムスタンプ` (timestamps), `話者分離` (speaker separation), `ファイル` (file), `リンク` (link), `ブラウザ` (browser), `アカウント登録なし` / `登録不要` (no sign-up), `自動判別` (auto-detected), `書き出し` (export), `100言語以上` (100+ languages).
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ (`YouTube動画のURLを貼り付け...` / `文字起こしを取得`).
- **Kiểm tra bắt buộc trước khi bàn giao:**
  1. `python3 shape_check.py en.json ja.json` → phải in `ja.json -> True`.
  2. `grep -c '[ぁ-んァ-ヶ一-龯] [ぁ-んァ-ヶ一-龯]'` → **0** (không dấu cách giữa CJK).
  3. `grep -c '動画ダウンロード\|動画を保存\|動画をダウンロード'` → **0**.
  4. `字幕` trong `h1`/`h2`/`h3`/`title`/`ogTitle` → **0**. (Ở `q` của FAQ 3 và FAQ 10 là hợp lệ.)
  5. `grep -c 'texttomp3'` → **0**.
  6. 4 path internal link đúng `/ja/` prefix, đủ 4, không thừa không thiếu.
