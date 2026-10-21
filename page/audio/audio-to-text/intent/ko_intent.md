🔥 TranscriptX – Audio to Text (Korean / ko)

URL:
/ko/audio-to-text

Intent chính:

음성 텍스트 변환 (무료 온라인)

Trang này là **bản tiếng Hàn của trang trụ (hub)** cụm Audio to Text. Nhắm đến người dùng Hàn Quốc đã có sẵn tệp âm thanh (녹음 파일, 음성 파일, MP3, 팟캐스트, 인터뷰...) và muốn chuyển nhanh thành văn bản.

Gộp toàn bộ intent đồng nghĩa **음성 / 녹음 / 오디오 + 텍스트 변환** vì tất cả cho ra **cùng một kết quả**: file âm thanh → văn bản.

> ⚠️ **Lưu ý cực kỳ quan trọng — lỗi khoảng trắng trong `2_loc_kw.md`:**
> Danh sách keyword tiếng Hàn trong `2_loc_kw.md` bị **chèn khoảng trắng sai giữa danh từ và trợ từ (조사)**. Tiếng Hàn **không bao giờ** tách trợ từ (`을/를`, `로/으로`, `이/가`, `에`) khỏi danh từ đứng trước.
>
> | Trong file (SAI) | Dạng đúng (dùng trong intent & ko.json) |
> | ---------------- | --------------------------------------- |
> | `음성 을 텍스트 로 변환` | `음성을 텍스트로 변환` |
> | `음성 을 글로 변환` | `음성을 글로 변환` |
>
> Toàn bộ file này và `ko.json` đã **sửa lại theo dạng đúng**. Nếu viết theo dạng sai, Google sẽ tokenize thành cụm vô nghĩa và người Hàn đọc sẽ thấy văn bản lỗi.

> 💡 **Ba cụm KW song song trong tiếng Hàn:** `음성` (giọng nói), `녹음` (bản ghi âm), `오디오` (audio) là **ba cụm độc lập, không phải biến thể của nhau** — người Hàn search cả ba với volume riêng biệt. Nội dung phải phủ **cả ba**, không được chỉ dùng `음성`.

---

## Từ khóa chính

음성 텍스트 변환 (1K–10K) ✅ *đã search*

---

## Từ khóa phụ

### Nhóm 음성 (giọng nói → text) — core

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 음성 파일 텍스트 변환 | 1K–10K | ✅ đã search |
| 음성을 텍스트로 변환 | 100–1K | ✅ đã search *(đã sửa khoảng trắng)* |
| 음성 텍스트 변환 무료 | 100–1K | ✅ đã search |
| 음성 텍스트 변환 사이트 | 100–1K | ✅ đã search |
| 음성 텍스트 변환 프로그램 | 10–100 | ✅ đã search |
| 음성을 글로 변환 | 10–100 | ✅ đã search *(đã sửa khoảng trắng)* |
| 음성 파일 텍스트 변환 무료 | — | 🔄 dịch bổ sung (audio file to text free) |
| 온라인 음성 텍스트 변환 | — | 🔄 dịch bổ sung (audio to text online) |
| 음성 인식 텍스트 변환 | — | 🔄 dịch bổ sung (speech recognition to text) |

### Nhóm 녹음 (bản ghi âm → text)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 녹음 파일 텍스트 변환 | 1K–10K | ✅ đã search |
| 녹음 텍스트 변환 | 1K–10K | ✅ đã search |
| 녹음 파일 텍스트 변환 무료 | — | 🔄 dịch bổ sung (transcribe recording free) |
| 인터뷰 녹음 텍스트 변환 | — | 🔄 dịch bổ sung (transcribe interview) |
| 회의 녹음 텍스트 변환 | — | 🔄 dịch bổ sung (transcribe meeting) |
| 강의 녹음 텍스트 변환 | — | 🔄 dịch bổ sung (transcribe lecture) |

### Nhóm 오디오 / 파일 형식 (audio & format)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 오디오 텍스트 변환 | 100–1K | ✅ đã search |
| 오디오 텍스트 변환 무료 | 10–100 | ✅ đã search |
| mp3 텍스트 변환 | 100–1K | ✅ đã search |
| 오디오 파일 텍스트 변환 | — | 🔄 dịch bổ sung (audio file to text) |
| 팟캐스트 텍스트 변환 | — | 🔄 dịch bổ sung (podcast to text) |
| 음성 텍스트 변환기 | — | 🔄 dịch bổ sung (audio to text converter) |

**Tổng:** 12 KW `✅ đã search` dùng được + 9 KW `🔄 dịch bổ sung`.

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, **được phép và nên** đặt vào title / H1 / H2 / meta. 🔄 *dịch bổ sung* = **chỉ rải trong body** để phủ ngữ nghĩa, **không** đặt vào title/H1/H2.

---

## Search Intent

Người dùng Hàn Quốc thường ĐÃ có sẵn tệp âm thanh (녹음 파일 từ 아이폰/갤럭시 음성 녹음, 회의 녹음, 강의 녹음, 인터뷰, 팟캐스트, MP3...) và muốn chuyển nhanh thành văn bản để đọc, tìm kiếm, ghi chú, trích dẫn hoặc lưu trữ.

Họ thường kỳ vọng:

- Tải file lên và nhận text ngay, **không cài phần mềm** (`프로그램 설치 없이` là kỳ vọng mạnh).
- **Miễn phí thật** — `무료` xuất hiện ở 2 keyword, cần nhấn rõ không có paywall.
- Nhận dạng tốt **tiếng Hàn**.
- Hỗ trợ MP3, WAV, M4A, AAC...
- Phân tách người nói (화자 분리) — quan trọng với 회의록.
- Xuất được nhiều định dạng.

### Khác biệt so với bản tiếng Anh

1. **Ba cụm 음성 / 녹음 / 오디오 phải phủ đều.** Bản EN chỉ có một trục "audio". Bản KO phải chủ động luân phiên ba từ này qua các section, nếu không sẽ mất trọn nhóm `녹음 * ` (1K–10K, ngang volume với KW chính).
2. **`사이트` và `프로그램` là hai intent tách bạch.** `음성 텍스트 변환 사이트` = tìm web tool; `음성 텍스트 변환 프로그램` = tìm phần mềm cài đặt. Section 4 phải trả lời **cả hai**: đây là 사이트, nên **không cần 프로그램**. Đây là góc bán hàng mạnh nhất cho thị trường KO.
3. **`무료` mạnh tương đương bản Ả Rập.** Cần lặp ở H1/meta/H2 section 4/conclusion.
4. **화자 분리 (speaker separation)** là điểm nhấn cho 회의록 문화 công sở Hàn — dùng đúng thuật ngữ `화자 분리`, không dịch vòng.
5. **Thể văn:** dùng `합니다`체 lịch sự chuẩn cho trang sản phẩm. Không dùng `해요`체 (quá thân mật) và không dùng `한다`체 (quá khô).

---

## Đối tượng người dùng

- Nhân viên văn phòng (회의 녹음 → 회의록)
- Sinh viên, nhà nghiên cứu (강의 녹음, 인터뷰 자료)
- Nhà báo / Phóng viên (인터뷰 녹취)
- Podcaster / YouTuber Hàn Quốc
- Người làm dịch vụ 녹취록 chuyên nghiệp
- Luật sư / Y tế (녹취록, 진료 기록)
- Người dùng AI cần đưa audio vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám đúng cấu trúc en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng **11 section** của `en.json`, cùng số đoạn văn, cùng số item, cùng số step, cùng **11 FAQ**. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 음성 텍스트 변환 | 음성 텍스트 변환 *(KW chính)* |
| — | **quickAnswer** | 음성 파일 텍스트 변환, 음성을 텍스트로 변환 |
| 1 | 음성 텍스트 변환이란? | 음성 텍스트 변환, 녹음 텍스트 변환 |
| 2 | 음성 텍스트 변환 한눈에 보기 | *(bảng thông số — 무료 / 100+ / 제한 없음)* |
| 3 | 음성 파일을 텍스트로 변환하는 방법 | 음성 파일 텍스트 변환, 음성을 텍스트로 변환 |
| 4 | 무료 음성 텍스트 변환 사이트 | 음성 텍스트 변환 무료, 음성 텍스트 변환 사이트, 음성 텍스트 변환 프로그램, 음성 텍스트 변환기 |
| 5 | 녹음 파일을 정확하게 텍스트로 변환 | 녹음 파일 텍스트 변환, 녹음 텍스트 변환, 음성을 글로 변환 |
| 6 | 지원 오디오 형식 | mp3 텍스트 변환, 오디오 텍스트 변환 |
| 7 | 변환할 수 있는 녹음 | 인터뷰 녹음 텍스트 변환, 회의 녹음 텍스트 변환, 강의 녹음 텍스트 변환, 팟캐스트 텍스트 변환 |
| 8 | 음성 텍스트 변환은 얼마나 정확한가요? | 음성 텍스트 변환, 음성 인식 텍스트 변환 |
| 9 | 100개 이상 언어의 음성 텍스트 변환 | 음성 텍스트 변환 *(+ nhấn tiếng Hàn)* |
| 10 | 다섯 가지 형식으로 내보내기 | *(internal link sang /ko/voice-to-text, /ko/youtube-transcript, /ko/tiktok-transcript)* |
| 11 | 자주 묻는 질문 | 오디오 텍스트 변환 무료, 오디오 파일 텍스트 변환 + long-tail |
| — | **conclusion** | 음성 텍스트 변환, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- Cụm `녹음` được dồn vào **section 5** và **section 7** (đúng chỗ bản EN nói về "transcribe" và "what you can transcribe") — không thêm section.
- Cụm `오디오` được dồn vào **section 6** (formats) và **FAQ** — nơi bản EN vốn đã nói về file/format.
- Intent `프로그램` được xử lý **trong section 4** bằng cách dịch câu "nothing to install" thành vế phủ định trực tiếp (`프로그램 설치 없이`), vừa bắt KW vừa không thêm câu.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `음성 받아쓰기` (10–100), `받아쓰기`, `음성 인식 받아쓰기`, `실시간 음성 인식`, `음성 메모 변환` → **/ko/voice-to-text** (ghi âm trực tiếp / đọc chính tả)
- `텍스트 음성 변환`, `TTS`, `글을 음성으로` → **trang Text-to-Speech (ngược intent)**
- `유튜브 자막 추출`, `유튜브 텍스트 변환` → **/ko/youtube-transcript**

> ⚠️ Cẩn thận: `음성 텍스트 변환` (đúng trang này) và `텍스트 음성 변환` (TTS — trang khác) chỉ khác thứ tự từ. Không được viết nhầm thứ tự ở bất kỳ đâu trong `ko.json`.

---

## Internal linking

- ↔ /ko/voice-to-text (khi user muốn ghi âm trực tiếp / 음성 메모 / 받아쓰기 thay vì file audio có sẵn)
- → /ko/youtube-transcript, /ko/tiktok-transcript (cross-cluster khi nguồn là video)

---

## Ghi chú kỹ thuật cho ko.json

- Thể văn: **`합니다`체** lịch sự chuẩn, xuyên suốt. Văn phong tự nhiên như người bản xứ viết, không dịch máy word-by-word.
- **Không chèn khoảng trắng trước trợ từ** (`을/를/로/이/가/에/의`). Đây là lỗi có sẵn trong `2_loc_kw.md`, đã sửa toàn bộ.
- Tên định dạng file (MP3, WAV, M4A, AAC, FLAC, OGG, TXT, DOCX, PDF, SRT, VTT) và tên thương hiệu (TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, iPhone, YouTube, TikTok) **giữ nguyên Latin**, không phiên âm sang Hangul.
- Số đếm dùng chữ số Latin (100+, 5).
- Internal link trong `sections[9]` giữ nguyên cú pháp markdown, đổi path sang `/ko/...`.
- Thuật ngữ chuẩn hoá: speaker separation → `화자 분리`; timestamps → `타임스탬프`; transcript → `변환된 텍스트` / `녹취록` (tuỳ ngữ cảnh); subtitles → `자막`.
