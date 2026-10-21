🔥 TranscriptX – Voice to Text (Japanese / ja)

URL:
/ja/voice-to-text

Intent chính:

ボイスメモ・録音した音声を文字起こしする（音声入力・音声認識）

Trang này là **bản tiếng Nhật của trang Voice to Text**. Nhắm đến người dùng Nhật muốn **nói trực tiếp vào trình duyệt** (音声入力 / 口述) hoặc **chuyển bản ghi âm của chính mình** (ボイスメモ, 会議の録音, インタビューの録音) thành văn bản.

Điểm phân biệt với `/ja/audio-to-text`: trang kia bắt đầu từ **tệp âm thanh có sẵn** (MP3, podcast, file tải về); trang này bắt đầu từ **giọng nói của người dùng** — ghi âm trực tiếp hoặc ボイスメモ do chính họ thu.

> ⚠️ **VẤN ĐỀ KHOẢNG TRẮNG TRONG KEYWORD TIẾNG NHẬT — BẮT BUỘC XỬ LÝ**
>
> Trong `2_loc_kw.md`, toàn bộ keyword tiếng Nhật bị công cụ export chèn khoảng trắng sai giữa các morpheme, ví dụ `ボイスメモ 文字 起こし`, `録音 を 文字 起こし`, `音声 認識 テキスト`.
> **Tiếng Nhật KHÔNG dùng khoảng trắng giữa từ.** Keyword thật là `ボイスメモ文字起こし`, `録音を文字起こし`, `音声認識テキスト`.
> Khi viết vào file intent này và khi dùng trong `ja.json`, **phải bỏ hết khoảng trắng thừa**. Để nguyên khoảng trắng thì chuỗi không khớp truy vấn thật của người dùng Nhật và trông như dịch máy.
>
> Lỗi dữ liệu khác đã kiểm tra trong section `## Japanese (ja)`:
> 1. `音声 文字 化` (100–1K) **xuất hiện 2 lần trùng lặp** (dòng 234 và 242) → chỉ tính 1 lần.
> 2. Không có dòng nào bị dính 2 keyword hay mất volume trong section `ja` của file này (khác với vấn đề đã gặp ở nhánh audio-to-text).
> 3. Section `ja` **không có keyword text-to-speech** (`テキスト読み上げ`), nên không cần loại bỏ.

### Bảng đối chiếu KW đã sửa khoảng trắng

| Chuỗi lỗi trong `2_loc_kw.md` | Keyword đúng |
| ----------------------------- | ------------ |
| `ボイスメモ 文字 起こし` | `ボイスメモ文字起こし` |
| `録音 を 文字 起こし` | `録音を文字起こし` |
| `録音 文字 起こし アプリ` | `録音文字起こしアプリ` |
| `録音 テキスト 化` | `録音テキスト化` |
| `文字 起こし ブラウザ` | `文字起こしブラウザ` |
| `音声 認識 テキスト` | `音声認識テキスト` |
| `音声 文字 化` | `音声文字化` |
| `音声 文字 起こし` | `音声文字起こし` *(nhường trang khác)* |
| `音声 データ 文字 起こし` | `音声データ文字起こし` *(nhường trang khác)* |
| `音声 を テキスト に 変換` | `音声をテキストに変換` *(nhường trang khác)* |
| `音声 テキスト 変換` | `音声テキスト変換` *(nhường trang khác)* |
| `音声 文字 起こし 無料` | `音声文字起こし無料` *(nhường trang khác)* |
| `文字 起こし 音声 ファイル` | `文字起こし音声ファイル` *(nhường trang khác)* |
| `音声 テキスト 変換 無料` | `音声テキスト変換無料` *(nhường trang khác)* |
| `音声 文字 起こし オンライン` | `音声文字起こしオンライン` *(nhường trang khác)* |

---

## Từ khóa chính

ボイスメモ文字起こし (10K–100K) ✅ *đã search*

> Đây là keyword volume cao nhất **còn khả dụng** sau khi `音声文字起こし` bị `/ja/audio-to-text` chiếm. Nó nằm chính xác trên trục riêng của trang này: **giọng nói / bản ghi âm cá nhân**, không phải tệp media tải về. `ボイスメモ` là từ người Nhật dùng hằng ngày (app Voice Memos trên iPhone), gắn liền với hành vi "nói rồi muốn ra chữ".
>
> Phải có trong title, H1, meta description và lặp lại đều trong body.

---

## Từ khóa phụ

### Nhóm 録音 (bản ghi âm của chính người dùng) — trục chính

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 録音文字起こしアプリ | 1K–10K | ✅ đã search |
| 録音を文字起こし | 100–1K | ✅ đã search |
| 録音テキスト化 | 10–100 | ✅ đã search |
| 録音した音声を文字起こし | — | 🔄 dịch bổ sung (transcribe a recording) |
| ボイスレコーダー文字起こし | — | 🔄 dịch bổ sung (voice recorder to text) |
| 会議録音文字起こし | — | 🔄 dịch bổ sung (recorded meeting) |
| インタビュー録音文字起こし | — | 🔄 dịch bổ sung (recorded interview) |

### Nhóm 音声入力・音声認識 (nói trực tiếp / đọc chính tả) — trục phụ mạnh

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 音声認識テキスト | 10–100 | ✅ đã search |
| 音声文字化 | 100–1K | ✅ đã search |
| 音声入力 | — | 🔄 dịch bổ sung (voice input — từ nội địa mạnh) |
| 音声認識 | — | 🔄 dịch bổ sung (speech recognition) |
| 口述筆記 | — | 🔄 dịch bổ sung (dictation) |
| 話した内容をテキスト化 | — | 🔄 dịch bổ sung (spoken words to text) |
| 声を文字にする | — | 🔄 dịch bổ sung (voice to text, cách nói thường ngày) |

### Nhóm Browser / Realtime

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 文字起こしブラウザ | 100–1K | ✅ đã search |
| リアルタイム文字起こし | — | 🔄 dịch bổ sung (record live in browser) |
| ブラウザで録音 | — | 🔄 dịch bổ sung (record straight into the browser) |

**Nguyên tắc dùng KW:**

- ✅ *đã search* = ưu tiên tuyệt đối. `ボイスメモ文字起こし` bắt buộc ở title / H1 / meta. `録音文字起こしアプリ`, `録音を文字起こし`, `文字起こしブラウザ`, `音声認識テキスト` được đặt vào H2/H3 hoặc câu mở đầu section.
- 🔄 *dịch bổ sung* = **chỉ rải trong body**, không đặt vào title / H1 / H2.
- Mật độ: mỗi section chỉ nhắm 1–2 keyword, không nhồi.

---

## KW nhường cho /ja/audio-to-text

Trang `/ja/audio-to-text` **đã hoàn thành và ĐÃ ĐÓNG BĂNG**. Các keyword dưới đây thuộc quyền trang đó — **KHÔNG dùng làm KW chính, KHÔNG đặt vào title / H1 / H2 / meta của trang này**:

| Keyword | Volume | Lý do nhường |
| ------- | ------ | ------------ |
| 音声文字起こし | 10K–100K | KW chính của /ja/audio-to-text |
| 音声文字起こし無料 | 1K–10K | biến thể 無料 của KW chính trang kia |
| 音声データ文字起こし | 1K–10K | "dữ liệu âm thanh" = tệp có sẵn, không phải giọng nói |
| 文字起こし音声ファイル | 100–1K | trục 音声ファイル文字起こし của trang kia |
| 音声をテキストに変換 | 100–1K | đã nằm bảng KW của trang kia |
| 音声テキスト変換 | 100–1K | đồng nghĩa 音声文字変換 của trang kia |
| 音声テキスト変換無料 | 10–100 | đã nằm bảng KW của trang kia |
| 音声文字起こしオンライン | 10–100 | đã nằm bảng KW của trang kia |

**Tổng: 8 keyword nhường.**

Xử lý khi buộc phải nhắc: `文字起こし` là thuật ngữ trung tâm thị trường Nhật nên không thể tránh hoàn toàn — nhưng chỉ dùng ở dạng **ghép với 録音 / ボイスメモ / 音声入力** (`録音を文字起こし`, `ボイスメモ文字起こし`), **không** dùng cụm trần `音声文字起こし`. Cụm `音声ファイル` chỉ xuất hiện **1 lần duy nhất** trong section 9 (so sánh 2 công cụ), kèm internal link sang `/ja/audio-to-text`.

---

## Search Intent

Người dùng Nhật vào trang này thường ở một trong hai tình huống:

1. **Chưa có văn bản, muốn nói ra chữ** — cần 音声入力 / 口述筆記: soạn nháp email, ghi ý tưởng, viết note khi đang đi lại. Kỳ vọng: bấm nút là ghi âm được ngay trên trình duyệt, không cài app.
2. **Đã có bản ghi âm của chính mình** — ボイスメモ trên iPhone, băng ghi âm cuộc họp, ghi âm phỏng vấn. Kỳ vọng: tải lên và ra 議事録 / bản trích dẫn có 話者分離.

Kỳ vọng chung:

- `インストール不要` / `アプリ不要` — chạy thẳng trên trình duyệt (khớp KW `文字起こしブラウザ`).
- `無料` và `登録不要`.
- `録音時間の制限なし` — ghi âm dài không bị cắt.
- `話者分離` cho 議事録 và インタビュー.
- `精度` — người dùng Nhật rất nhạy chất lượng nhận dạng.

### Khác biệt so với bản tiếng Anh

1. **`ボイスメモ` thay vì "voice memo" chung chung.** Ở Nhật `ボイスメモ` gắn trực tiếp với app mặc định trên iPhone và là hành vi phổ biến nhất tạo ra file giọng nói. Đây là điểm neo mạnh hơn bản EN.
2. **`音声入力` là một khái niệm nội địa độc lập**, không phải bản dịch của "voice to text". Người Nhật đã quen 音声入力 trên smartphone / Google ドキュメント. Dùng từ này để bắt intent "nói thay vì gõ" trong section 7 (Dictation).
3. **議事録 là use-case số 1**, mạnh hơn podcast/interview như thị trường Anh–Mỹ. Section 6 mục "Meetings and calls" phải dùng từ `議事録`.
4. **Ranh giới với trang audio-to-text phải rõ hơn bản EN.** Bản EN có thể dùng "audio" và "voice" lẫn nhau; bản JA phải kỷ luật: trang này = `録音`/`ボイスメモ`/`音声入力`, trang kia = `音声ファイル`.
5. **Không dùng khoảng trắng** — xem cảnh báo đầu file.
6. Văn phong: thể `です・ます` lịch sự chuẩn trang sản phẩm; tránh 体言止め dày đặc kiểu quảng cáo.

---

## Đối tượng người dùng

- Nhân viên văn phòng ghi âm cuộc họp bằng điện thoại rồi cần làm 議事録
- Người dùng iPhone có nhiều ボイスメモ chưa nghe lại
- Nhà báo / biên tập viên ghi âm phỏng vấn
- Người viết lách muốn 口述筆記 bản nháp thay vì gõ
- Sinh viên ghi âm bài giảng, ゼミ
- Người gõ phím chậm hoặc có khó khăn vận động (アクセシビリティ)
- Người dùng cần đưa nội dung nói vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám đúng cấu trúc en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ja.json` phải dịch đúng **10 section** của `en.json`, cùng số đoạn văn, cùng số step, cùng số item, cùng số spec, cùng **10 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (ja) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** ボイスメモ文字起こし・音声入力 | ボイスメモ文字起こし *(KW chính)*, 音声入力 |
| — | **quickAnswer** | ボイスメモ文字起こし, 録音を文字起こし |
| 1 | ボイスメモ文字起こしとは？ | ボイスメモ文字起こし, 音声文字化, 声を文字にする |
| 2 | 音声入力・録音文字起こしの概要 | *(bảng thông số — 無料 / 録音時間制限なし / 100言語以上)* |
| 3 | 録音を文字起こしする方法 | 録音を文字起こし, 文字起こしブラウザ |
| 4 | ブラウザで録音するか、録音データをアップロードするか | 文字起こしブラウザ, リアルタイム文字起こし, ブラウザで録音 |
| 5 | 録音した音声を文字起こしする | 録音した音声を文字起こし, 録音テキスト化, ボイスレコーダー文字起こし |
| 6 | テキストにできる音声の種類 | 会議録音文字起こし *(議事録)*, インタビュー録音文字起こし, 録音文字起こしアプリ |
| 7 | 音声入力で口述筆記する | 音声入力, 口述筆記, 話した内容をテキスト化 |
| 8 | 認識精度と対応言語 | 音声認識テキスト, 音声認識 |
| 9 | 音声入力と音声ファイルの文字起こし、どちらを使う？ | ボイスメモ文字起こし + *(1 lần duy nhất nhắc 音声ファイル kèm internal link /ja/audio-to-text, /ja/youtube-transcript)* |
| 10 | よくある質問 | 録音文字起こしアプリ, 録音テキスト化, 音声認識テキスト + long-tail |
| — | **conclusion** | ボイスメモ文字起こし, 音声入力, 無料 |

### Ghi chú riêng cho bản ja (KHÔNG tạo section mới)

- Section 6 mục "Meetings and calls" dịch bằng `会議・通話の録音` và nhấn `議事録` để bắt intent nội địa.
- Section 6 mục "Voice memos and notes" là chỗ đặt `ボイスメモ` đậm nhất sau H1.
- Section 9 là chỗ **duy nhất** được nhắc `音声ファイル` — bắt buộc kèm internal link sang `/ja/audio-to-text`.
- FAQ số 10 (so sánh voice to text vs audio to text) nhắc lại ranh giới nhưng **không** đặt link thứ hai, giữ đúng cấu trúc EN (EN cũng không có link trong FAQ).

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- テキスト読み上げ / 文章を音声に変換 / 音声合成 → **trang Text-to-Speech (ngược intent)**
- 音声文字起こし / 文字起こし無料 / 音声ファイル文字起こし / mp3文字起こし / 音声をテキストに変換 / 文字起こし音声 → **/ja/audio-to-text (đã đóng băng)**
- YouTube文字起こし / 動画文字起こし → **/ja/youtube-transcript**
- TikTok文字起こし → **/ja/tiktok-transcript**

---

## Internal linking

- ↔ /ja/audio-to-text (khi người dùng có sẵn 音声ファイル như podcast / MP3 thay vì bản ghi giọng nói của chính họ) — đặt trong section 9
- → /ja/youtube-transcript (khi nguồn thực chất là âm thanh của video) — đặt trong section 9

---

## Ghi chú kỹ thuật cho ja.json

- **Tuyệt đối không chèn khoảng trắng vào keyword tiếng Nhật.** Khoảng trắng trong `2_loc_kw.md` là lỗi export, không phải chính tả.
- Cấu trúc JSON phải **giống hệt** `en.json`: 10 section, 10 spec, 4 step, 6 item ở section 6, 2 item ở section 9, 10 FAQ, 2 đoạn conclusion.
- Không đổi ví dụ trong bản EN (10 giây / 1 tiếng, email, report, article... giữ nguyên ý).
- Giữ nguyên Latin: MP3, WAV, M4A, AAC, FLAC, OGG, TXT, DOCX, PDF, SRT, VTT, TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, iPhone, YouTube, TikTok.
- Số đếm dùng chữ số Latin (100+, 4).
- Dấu câu dùng `。`, `、` chuẩn Nhật; không dùng `,` `.` phương Tây.
- Internal link giữ cú pháp markdown và đổi sang prefix `/ja/`: `[音声文字起こし](/ja/audio-to-text)`, `[YouTube文字起こし](/ja/youtube-transcript)`.
- Thể văn: `です・ます` thống nhất toàn trang.
