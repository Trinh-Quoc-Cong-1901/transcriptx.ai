🔥 TranscriptX – Video to Text (Korean / ko)

URL:
/ko/video-to-text

Intent chính:

영상 텍스트 추출 (동영상 음성 → 텍스트, 무료 온라인)

Trang này là **trang trụ (hub)** cụm Video to Text bản tiếng Hàn. Nhắm đến người dùng Hàn đã **có sẵn file video** (MP4, MOV, bản ghi Zoom/Teams, 화면 녹화, 촬영본) và muốn lấy phần **lời nói bên trong video** ra thành chữ.

Gộp toàn bộ intent đồng nghĩa **추출 / 변환 / 텍스트화** vì tất cả cho ra **cùng một kết quả**: file video → text.

> ⚠️ **Phân định với `/ko/audio-to-text`: LOẠI FILE.** Trang này nhận **영상 파일** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **음성 파일** (MP3, WAV, M4A...). Kiểm tra dữ liệu: **0 keyword trùng nhau** giữa hai danh sách ko — người dùng Hàn tự tách rất sạch (`영상`/`동영상`/`비디오` vs `음성`/`녹음`/`오디오`). Chốt chặn nằm ở **section 10 đoạn 3** (link sang `/ko/audio-to-text`). Không chủ động kéo keyword nhóm audio về đây.

> ⚠️ **Phân định với các trang nền tảng: FILE vs LINK.** Trang này để **파일 업로드** từ máy; các trang `/ko/youtube-transcript`, `/ko/tiktok-transcript`, `/ko/instagram-transcript` để **링크 붙여넣기**. Cùng **section 10 đoạn 3** chứa cả ba link đó — tổng cộng **4 internal link**, nhiều nhất trong các trang đã làm.

> 🚨 **RỦI RO RIÊNG CỦA BẢN KO: NHIỄM OCR.**
> Keyword mạnh nhất `영상 텍스트 추출` đọc mộc **có thể hiểu thành hai nghĩa**:
> 1. lấy **lời nói** trong video ra thành chữ ← đúng trang này;
> 2. lấy **chữ hiển thị trên màn hình** (하드코딩 자막, 화면 속 글자) ra ← đó là **OCR**, không phải sản phẩm này.
> Tiếng Anh không có mơ hồ này vì "transcribe" đã hàm ý âm thanh. Tiếng Hàn `추출` thì trung tính.
>
> **Cách chốt (không thêm section nào):** dùng nhóm keyword có `음성` để khoá nguồn là âm thanh — `동영상 음성 텍스트 변환` (100–1K) và `영상 음성 텍스트 변환` (10–100). Cụ thể:
> - **Section 5** (H2 = `동영상 음성 텍스트 변환을 정확하게`) — nói thẳng công cụ xử lý **영상 속 음성**.
> - **Section 8** (đoạn 2) — `영상 음성 텍스트 변환` đặt nguyên văn, gắn với chất lượng **âm thanh** (소음, 울림, 억양) → tự khắc loại nghĩa OCR.
> - **Section 3 bước 2** — mô tả `영상에서 음성을 분리해` trước khi nhận dạng.
> - **Hero subtitle + quickAnswer** — nêu `영상 속 말소리` ngay từ trên màn hình đầu.
> Ngoài 4 vị trí đó thì để keyword `영상 텍스트 추출` chạy tự nhiên, không cần giải thích lại.

> ⚠️ **Lỗi dữ liệu trong `2_loc_kw.md` (block `## Korean (ko)`).**
> - Số keyword thực: **16**, không có dòng rác `Keyword ideas` (khác block de/es/fr/vi), không có trùng lặp.
> - **Lỗi khoảng trắng trước trợ từ (조사):** dòng `영상 텍스트 로 바꾸기` bị tách `로` khỏi `텍스트`. Dạng đúng: **`영상 텍스트로 바꾸기`** (tự nhiên nhất là `영상을 텍스트로 바꾸기`). Tiếng Hàn **không bao giờ** tách trợ từ (`을/를`, `로/으로`, `이/가`, `에`) khỏi danh từ đứng trước.
> - Cùng loại lỗi ở trang anh em (`음성 을 텍스트 로 변환` → `음성을 텍스트로 변환`) — đã kiểm tra, block ko của trang này **chỉ dính 1 dòng** nêu trên.
> - Toàn bộ intent này và `ko.json` viết theo **dạng đúng**. Viết theo dạng sai thì Google tokenize thành cụm vô nghĩa và người Hàn đọc thấy văn bản lỗi.

---

## Từ khóa chính

영상 텍스트 추출 (100–1K) ✅ *đã search*

Là cụm có volume cao nhất trong 16 keyword, và là **lõi chung** của nhóm `추출`. Đặt nguyên văn ở **H1**, `seo.title`, `ogTitle`, H2 section 8 và conclusion.

---

## Từ khóa phụ

### Nhóm 추출 (trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 영상 텍스트 추출 | 100–1K | ✅ đã search *(KW chính)* |
| 영상 스크립트 추출 | 100–1K | ✅ đã search |
| 동영상 자막 추출 | 100–1K | ✅ đã search *(chỉ dùng ở S10 + FAQ 8)* |

### Nhóm 변환 (chuyển đổi)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 동영상 음성 텍스트 변환 | 100–1K | ✅ đã search *(chốt chặn OCR)* |
| 영상 텍스트 변환 | 10–100 | ✅ đã search |
| 동영상 텍스트 변환 | 10–100 | ✅ đã search |
| 영상 음성 텍스트 변환 | 10–100 | ✅ đã search *(chốt chặn OCR)* |
| 비디오 텍스트 변환 | 10–100 | ✅ đã search |
| 동영상 텍스트 변환 사이트 | 10–100 | ✅ đã search |
| 동영상 텍스트 변환 무료 | 10–100 | ✅ đã search |
| mp4 텍스트 변환 | 10–100 | ✅ đã search |
| 영상 텍스트 변환 무료 | 0–10 | ✅ đã search |
| 영상 텍스트 변환 프로그램 | 0–10 | ✅ đã search |
| 영상 자막 텍스트 변환 | 0–10 | ✅ đã search *(chỉ dùng ở S10)* |
| 동영상 텍스트 변환 온라인 | 0–10 | ✅ đã search |

### Nhóm 텍스트화 / khẩu ngữ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 영상 텍스트로 바꾸기 | 0–10 | ✅ đã search *(đã sửa khoảng trắng)* |
| 영상 텍스트화 | — | 🔄 dịch bổ sung (video to text) |
| 화면 녹화 텍스트 변환 | — | 🔄 dịch bổ sung (screen recording) |
| 회의 영상 텍스트 변환 | — | 🔄 dịch bổ sung (meeting recording) |
| 강의 영상 텍스트 변환 | — | 🔄 dịch bổ sung (lecture video) |
| 영상 녹취록 | — | 🔄 dịch bổ sung (video transcript) |

**Tổng: 16 KW `✅ đã search` (dùng hết 16) + 5 KW `🔄 dịch bổ sung`.**

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, được phép và nên đặt vào `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = **chỉ rải body**.

---

## Search Intent

Người dùng Hàn **đã có file video trong tay** — bản ghi Zoom/Teams/Meet, 화면 녹화, 웨비나, 강의 영상, 인터뷰 촬영본 — và muốn lấy phần lời nói ra thành chữ để đọc, tìm kiếm, trích dẫn, làm 회의록 hoặc làm tài liệu.

Họ kỳ vọng:

- Tải file lên là chạy, **프로그램 설치 없이** (kỳ vọng rất mạnh ở thị trường KO).
- **Không giới hạn dung lượng / thời lượng** — bản ghi họp 2–3 tiếng là chuyện thường.
- **화자 분리** — quan trọng nhất với văn hoá 회의록 công sở Hàn.
- **무료 thật** — `무료` xuất hiện ở 2 keyword riêng.
- Nhận dạng tiếng Hàn tốt.
- Xuất được **DOCX** (làm tài liệu) và **SRT** (làm 자막).

### Khác biệt so với bản tiếng Anh

1. **Ba cụm `영상` / `동영상` / `비디오` là ba trục riêng, không phải biến thể tuỳ ý.** `영상` và `동영상` đều có volume thật và phải phủ đều; `비디오` chỉ có 1 keyword nên dùng đúng 1–2 lần (S6 + FAQ). Bản EN chỉ có một trục "video".
2. **Mơ hồ OCR không tồn tại ở bản EN.** `추출` trung tính về nguồn, nên phải chủ động khoá bằng nhóm `음성` — xem mục 🚨 ở trên. Đây là khác biệt lớn nhất của bản ko.
3. **`사이트` / `프로그램` / `온라인` là ba intent tách bạch.** `동영상 텍스트 변환 사이트` = tìm web tool; `영상 텍스트 변환 프로그램` = tìm phần mềm cài đặt; `동영상 텍스트 변환 온라인` = nhấn chạy trên web. **Section 4 phải trả lời cả ba**: đây là 사이트 chạy 온라인, nên **không cần 프로그램**. Bản EN gộp chung vào "no install".
4. **`자막` là keyword có volume (100–1K) nhưng KHÔNG phải kết quả của trang này.** Bản EN nói "subtitles" thoải mái; bản ko phải giới hạn `자막` vào đúng **S10 + FAQ 8** (chỗ nói xuất SRT/VTT). Ở mọi chỗ khác kết quả gọi là `텍스트` / `대본` / `스크립트`.
5. **Nỗi lo nhận dạng tiếng Hàn** xử lý trong **section 9**, thay ví dụ ngôn ngữ của bản EN (German/Vietnamese) bằng ví dụ có tiếng Hàn — không thêm câu.

---

## Đối tượng người dùng

- Nhân viên văn phòng (Zoom/Teams/Meet 녹화 → 회의록)
- Người làm 사내 교육 / 매뉴얼 (화면 녹화 → 문서)
- Giáo viên, sinh viên (강의 영상)
- Nhà báo, phóng viên (인터뷰 촬영본 녹취)
- Marketer, content creator (웨비나 → 아티클)
- Người làm 자막 (xuất SRT/VTT)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng **11 section**, đúng **10 `specs`**, đúng **4 `steps`**, S6 = `intro` 1 + `items` 4, S7 = `intro` 1 + `items` 6, đúng **10 FAQ** (khác trang audio-to-text vốn có 11), `conclusion.content` 2 đoạn. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách viết thêm câu.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 영상 텍스트 추출 | 영상 텍스트 추출 *(KW chính)* |
| — | **quickAnswer** | 동영상 텍스트 변환, 영상 텍스트로 바꾸기 |
| 1 | 영상 텍스트 추출이란? | 영상 텍스트 추출, 영상 스크립트 추출, 영상 텍스트 변환 |
| 2 | 영상 텍스트 추출 한눈에 보기 | *(bảng 10 thông số — 무료 / 제한 없음 / 100개 이상)* |
| 3 | 영상 파일을 텍스트로 변환하는 방법 | 동영상 텍스트 변환, 영상 텍스트로 바꾸기 *(bước 2 chốt nguồn `음성`)* |
| 4 | 무료 동영상 텍스트 변환 사이트 | 동영상 텍스트 변환 사이트, 동영상 텍스트 변환 무료, 영상 텍스트 변환 무료, 영상 텍스트 변환 프로그램, 동영상 텍스트 변환 온라인 |
| 5 | 동영상 음성 텍스트 변환을 정확하게 | **동영상 음성 텍스트 변환** *(chốt OCR #1)*, 영상 녹취록 |
| 6 | 지원 영상 형식 | mp4 텍스트 변환, 비디오 텍스트 변환 |
| 7 | 텍스트로 바꿀 수 있는 영상 | 회의 영상 텍스트 변환, 화면 녹화 텍스트 변환, 강의 영상 텍스트 변환 |
| 8 | 영상 텍스트 추출은 얼마나 정확한가요? | 영상 텍스트 추출, **영상 음성 텍스트 변환** *(chốt OCR #2)* |
| 9 | 100개 이상 언어의 영상 텍스트 변환 | 영상 텍스트 변환 *(+ nhấn tiếng Hàn)* |
| 10 | 다섯 가지 형식으로 내보내기 | 동영상 자막 추출, 영상 자막 텍스트 변환 + *(4 internal link)* |
| 11 | 자주 묻는 질문 | 영상 스크립트 추출, 비디오 텍스트 변환, 영상 텍스트 변환 무료 + long-tail |
| — | **conclusion** | 영상 텍스트 추출, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- Cụm `자막` xuất hiện **đúng 2 chỗ**: **S10 đoạn 2** (`동영상 자막 추출` + `영상 자막 텍스트 변환`, nơi bản EN nói về SRT/VTT) và **FAQ 8** (câu hỏi về subtitles). Mọi chỗ khác kết quả gọi là `텍스트` / `대본` / `스크립트`.
- Intent `프로그램` xử lý **trong S4** bằng cách dịch "no desktop app to install" thành vế phủ định trực tiếp (`영상 텍스트 변환 프로그램을 따로 설치할 필요가 없습니다`) — vừa bắt KW vừa không thêm câu.
- `비디오` chỉ dùng **2 lần**: S6 (intro formats) và FAQ 2 — vì chỉ có 1 keyword, dùng nhiều sẽ lệch giọng (người Hàn viết `영상`/`동영상` là chính).
- `영상 텍스트로 바꾸기` (dạng đã sửa khoảng trắng) đặt ở **quickAnswer** và **S3 tiêu đề bước 1 area** — dạng động từ, hợp văn hướng dẫn.

---

## Không nên tối ưu cho các keyword

- `음성 텍스트 변환`, `녹음 파일 텍스트 변환`, `오디오 텍스트 변환`, `mp3 텍스트 변환` → **/ko/audio-to-text** (file âm thanh). Dữ liệu đã tự tách sạch (0 trùng), chỉ cần không chủ động kéo về. Lưu ý: `동영상 음성 텍스트 변환` **thuộc trang này** vì có `동영상` — không nhầm với `음성 텍스트 변환` trơn.
- `유튜브 자막 추출` / `유튜브 텍스트 변환` → **/ko/youtube-transcript**; `틱톡` → `/ko/tiktok-transcript`; `인스타` → `/ko/instagram-transcript` (dán link, không upload file).
- **`영상 다운로드` / `동영상 저장` / `mp4 변환기` / `영상 압축`** → **intent xử lý FILE video**, không phải lấy chữ. Quy tắc cứng: `다운로드` / `저장` chỉ đi với `텍스트` / `대본` / `파일`, **KHÔNG BAO GIỜ** với `영상` / `동영상`.
- `이미지 텍스트 추출` / `사진 글자 인식` / `OCR` → **intent đọc chữ TRÊN màn hình**. Trang này lấy **영상 속 음성**. Xem mục 🚨.
- `영상에 자막 넣기` / `자막 삽입` → intent gắn phụ đề vào video; trang này chỉ **xuất file SRT/VTT** (S10 + FAQ 8), không gắn hộ.
- `텍스트 음성 변환` / `TTS` → ngược intent, trang khác.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link**:

- → `/ko/audio-to-text` (khi nguồn là **음성 파일** thay vì **영상 파일**)
- → `/ko/youtube-transcript`, `/ko/tiktok-transcript`, `/ko/instagram-transcript` (khi video nằm trên nền tảng — **링크 붙여넣기** thay vì **파일 업로드**)

---

## Ghi chú kỹ thuật cho ko.json

- Thể văn: **`합니다`체** lịch sự chuẩn, xuyên suốt — nhất quán với `/ko/audio-to-text`. Không dùng `해요`체, không dùng `한다`체.
- **Không chèn khoảng trắng trước trợ từ** (`을/를/로/이/가/에/의`) — lỗi có sẵn trong `2_loc_kw.md`, đã sửa toàn bộ.
- **Nhãn `specs` copy y nguyên 10 chuỗi từ `/ko/audio-to-text/ko.json`**: `가격` / `계정 필요 여부` / `설치` / `파일 용량 제한` / `지원 형식` / `언어` / `화자 분리` / `타임스탬프` / `내보내기 형식` / `지원 기기`. Chỉ đổi **giá trị** của `지원 형식` sang định dạng video (MP4, MOV, AVI, MKV, WebM 외 다수).
- Thuật ngữ chuẩn hoá (khớp trang anh em): speaker separation → `화자 분리`; timestamps → `타임스탬프`; transcript → `변환된 텍스트` / `대본` / `녹취록`; subtitles → `자막` (chỉ S10 + FAQ 8).
- Giữ nguyên Latin, không phiên âm Hangul: **MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT**; **TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad**.
- Số đếm dùng chữ số Latin (100개 이상, 5가지).
- Internal link trong `sections[9].content[2]` giữ cú pháp markdown, path `/ko/...`.
