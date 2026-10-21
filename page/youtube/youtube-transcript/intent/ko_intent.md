🔥 TranscriptX – YouTube Transcript (Korean / ko)

URL:
/ko/youtube-transcript

Intent chính:

유튜브 스크립트 / 유튜브 스크립트 추출 — lấy toàn bộ lời nói trong video YouTube dưới dạng văn bản, online, miễn phí

Trang này nhắm đến người dùng Hàn Quốc muốn **lấy toàn bộ nội dung nói trong một video YouTube dưới dạng chữ** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán URL là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này là **hub** nên **giữ trọn họ từ `스크립트` / `대본`**, cộng thêm nhóm `텍스트 추출` / `텍스트 변환`.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ nhóm `유튜브 영상 텍스트 변환` / `유튜브 음성 텍스트 변환` / `유튜브 텍스트 추출` đều **có chữ `유튜브`**, nên không đụng trang generic `/ko/video-to-text`. Trang này giữ hết.

### ⚠️ NGOẠI LỆ DUY NHẤT — `유튜브 자막 추출` KHÔNG thuộc trang này

Cụm `유튜브 자막 추출` (**1K – 10K**) tuy có trong danh sách `## Korean (ko)` nhưng **đã được chốt thuộc `/ko/youtube-subtitle-downloader`** khi làm trang đó — ghi rõ ở mục "QUYẾT ĐỊNH CHÉO TRANG CHO TƯƠNG LAI" trong `../youtube-subtitle-downloader/intent/ko_intent.md`.

Lý do: `자막` = phụ đề, `추출` ở đây là trích **file phụ đề** ra khỏi video — đúng việc trang subtitle làm. Trang này phải bám nhóm `스크립트` / `대본` / `텍스트 변환`.

**Cách xử lý trong `ko.json`:** dùng **đúng 1 lần**, ở **S11**, trong câu trỏ sang `/ko/youtube-subtitle-downloader` — kỹ thuật "neo đẩy đi" (mention có chủ đích rồi chuyển link luôn, để Google hiểu trang này biết cụm đó nhưng không tranh). **KHÔNG** đặt ở `title`, `h1`, bất kỳ `h2`/`h3` nào, hay `description`.

### Vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **S11 (`복사, 편집, 번역 또는 다운로드`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (`스크립트` vs `자막`) — chốt với `/ko/youtube-subtitle-downloader`.
- **FAQ 4** (생성 vs 추출) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — ĐÃ KIỂM SECTION `## Korean (ko)`

Đã kiểm đủ 4 loại lỗi hệ thống từng gặp ở `es` / `fr` / `vi`:

| Loại lỗi | Kết quả kiểm |
| -------- | ------------ |
| Dòng nhãn `Keyword ideas` | ❌ **không có** trong section ko |
| Dòng nhãn `Keywords you provided` | ❌ **không có** trong section ko |
| Cụm `texttomp3` (TTS — intent ngược) | ❌ **không có** trong section ko |
| Cụm garbled / sai chính tả | ❌ **không có** |
| **Dấu cách thừa** | ⚠️ **CÓ 1 dòng** |

### ⚠️ Dòng có dấu cách thừa

| Dòng trong file | Dạng đúng | Volume |
| --------------- | --------- | ------ |
| `유튜브 트랜 스크립트` | **`유튜브 트랜스크립트`** | 10 – 100 |

`트랜스크립트` là phiên âm của "transcript", viết **liền một từ**. Dấu cách giữa `트랜` và `스크립트` là lỗi tokenizer khi export (cùng loại lỗi với section `## Japanese (ja)`: `youtube 文字 起こし`). Khi viết body dùng **dạng đúng, không dấu cách**.

> ℹ️ Lưu ý: `유튜브` là **một từ**, luôn viết liền. Toàn bộ danh sách ko đều đúng ở điểm này.

### 📊 Số keyword thực

- Tổng dòng keyword trong section `## Korean (ko)`: **11**
- Loại bỏ do lỗi dữ liệu: **0**
- **Số keyword thực: 11**
- Trong đó **nhường `/ko/youtube-subtitle-downloader`: 1** (`유튜브 자막 추출`)
- **→ Keyword dùng cho trang này: 10**

---

## 🔤 MỤC RIÊNG — QUY TẮC DÙNG TỪ `자막`

Đây là quyết định thuật ngữ quan trọng nhất của bản ko, vì tiếng Hàn có **hai từ tách bạch rất rõ** mà tiếng Anh gộp chung:

| Tiếng Hàn | Nghĩa | Dùng cho |
| --------- | ----- | -------- |
| **`스크립트` / `대본`** | bản chữ của lời nói, đọc độc lập | **Kết quả của trang này — LUÔN LUÔN** |
| **`자막`** | phụ đề khớp giờ hiện trên video | **Đầu vào có sẵn của YouTube**, hoặc trỏ sang trang subtitle |

### Quy tắc cứng

1. **Kết quả trang này không bao giờ gọi là `자막`.** Luôn là `스크립트`, `대본` hoặc `텍스트`.
2. **`자막` chỉ được dùng khi nói về caption có sẵn của YouTube** — và phải có **định ngữ** để rõ nghĩa:
   - `자동 자막` (auto-captions)
   - `제작자가 넣은 자막` (captions the creator added)
   - `자막이 없는 영상` / `자막 트랙` (nói về sự vắng mặt của caption)
3. **`자막` để trần** chỉ xuất hiện ở:
   - **S11** — câu trỏ sang `/ko/youtube-subtitle-downloader` (`자막 파일`, `유튜브 자막 다운로더`, `유튜브 자막 추출`)
   - **FAQ 8** (`자막 파일` — khi bật timestamp để xuất SRT/VTT)
   - **FAQ 10** — câu hỏi so sánh `스크립트` vs `자막`
4. **Không heading nào chứa `자막`.** Đã grep xác nhận trên toàn bộ 31 heading (`h1` + 12 `h2` + 4 `h3` steps + 13 `h3` items + `conclusion.h2`) → **0 kết quả**.

Bản EN dùng `captions` ở ~6 chỗ; bản ko dịch thành `자막` có định ngữ ở S2 (nhãn `자막 없는 영상`), S4 (2 lần), S8 (2 lần), S10 (`자막 트랙`), FAQ 3, FAQ 4.

### Kỷ luật `다운로드` / `저장`

`다운로드` và `저장` **chỉ đi với** `스크립트` / `대본` / `텍스트` / `파일`. **Không bao giờ** đi với `영상` / `동영상`.

Rủi ro: `유튜브 영상 다운로드` là cụm khổng lồ ở Hàn Quốc, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. S3 bước 2 bản EN nói "no file to download first" → dịch `먼저 받아 둘 파일도 없습니다`, giữ `파일`, tuyệt đối không dùng `영상`. Grep `영상 다운로드` → **0**.

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói (`화자 분리`), timestamp (`타임스탬프`) tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **받기 / get** — lấy スクリプト có sẵn,
- **생성 / generate** — dựng scripts từ audio khi video không có `자막`,
- **추출 / extract** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

---

## Từ khóa chính

**유튜브 스크립트 (1K–10K)** ✅ *đã search* → **H1**

Toàn bộ trang xây quanh cụm này: xuất hiện ở `title`, `h1`, `ogTitle`, H2 của S1 và S2, `conclusion.h2` và FAQ 2.

---

## Từ khóa phụ

### Nhóm `스크립트` (trục chính — danh từ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 스크립트 | 1K–10K | ✅ đã search *(KW chính)* |
| 유튜브 스크립트 추출 | 1K–10K | ✅ đã search |
| 유튜브 영상 스크립트 | 100–1K | ✅ đã search |
| 유튜브 스크립트 따기 | 100–1K | ✅ đã search |
| 유튜브 트랜스크립트 | 10–100 | ✅ đã search *(sửa dấu cách thừa)* |

### Nhóm `대본` (đồng nghĩa dân dã của 스크립트)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 대본 추출 | 1K–10K | ✅ đã search |

### Nhóm `텍스트` (chuyển đổi / trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 텍스트 추출 | 100–1K | ✅ đã search |
| 유튜브 음성 텍스트 변환 | 100–1K | ✅ đã search |
| 유튜브 영상 텍스트 변환 | 10–100 | ✅ đã search |
| 유튜브 영상 글로 변환 | — *(không ghi volume)* | ✅ đã search |

### ⛔ Nhóm NHƯỜNG TRANG KHÁC

| Keyword | Volume | Nhường cho | Cách xử lý ở trang này |
| ------- | ------ | ---------- | ---------------------- |
| 유튜브 자막 추출 | 1K–10K | `/ko/youtube-subtitle-downloader` | Dùng **đúng 1 lần** ở S11 trong câu trỏ link — "neo đẩy đi". Không lên heading. |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 화자 분리 | — | 🔄 dịch bổ sung (speaker separation) |
| 타임스탬프 | — | 🔄 dịch bổ sung (timestamps) |
| 100개 이상 언어 | — | 🔄 dịch bổ sung (100+ languages) |
| 무료 / 가입 불필요 | — | 🔄 dịch bổ sung (free / no sign-up) |
| 유튜브 스크립트 생성기 | — | 🔄 dịch bổ sung (youtube transcript generator) |
| 유튜브 영상 스크립트 생성기 | — | 🔄 dịch bổ sung (youtube video transcript generator) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng Hàn Quốc muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán URL YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu KO ⇄ EN rất nặng (học tiếng Anh qua YouTube là một use case lớn ở Hàn).
- Hoạt động **cả khi video không có `자막`** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, tọa đàm).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Hàn tách bạch `스크립트` và `자막`, tiếng Anh gộp vào `transcript`/`captions` một cách mờ hơn.** Trong tiếng Anh, "transcript" và "captions" chồng lấn về ngữ nghĩa và người dùng thường gõ lẫn lộn. Tiếng Hàn thì **hai từ này là hai thế giới riêng**: `자막` gắn chặt với hình ảnh chữ chạy dưới video, `스크립트` gắn với văn bản đọc rời. Chính vì thế cụm `유튜브 자막 추출` (1K–10K) **phải nhường** cho trang subtitle, còn bản EN không có ranh giới sạch tương đương. Đây là khác biệt cấu trúc lớn nhất của bản ko.

2. **Tiếng Hàn có hai từ đồng nghĩa cạnh tranh cho "transcript": `스크립트` và `대본`.** Bản EN chỉ có một trục duy nhất `transcript`. Bản ko phải phục vụ cả hai vì `유튜브 대본 추출` đạt **1K–10K**, ngang với `유튜브 스크립트`. Xử lý: `스크립트` giữ H1 + phần lớn heading (từ phổ biến hơn, sát tiếng Anh); `대본` được cấp một câu riêng ở **S5** (`유튜브 대본 추출`) và rải trong body. Không dịch cả hai về một từ.

3. **`추출` (trích xuất) mạnh bất thường trong tiếng Hàn.** Có tới **4/10 keyword** dùng động từ `추출`: `유튜브 스크립트 추출` (1K–10K), `유튜브 대본 추출` (1K–10K), `유튜브 텍스트 추출` (100–1K), cộng cụm nhường đi `유튜브 자막 추출`. Bản EN chỉ có một cụm `youtube transcript extractor` ở bậc thấp hơn nhiều so với cụm chính. Hệ quả: **S5 phải lấy trọn H2 cho `유튜브 스크립트 추출`** và nhồi cả `유튜브 텍스트 추출` + `유튜브 대본 추출` vào `content[1]` — nặng hơn hẳn vai trò của S5 trong bản EN.

4. **`따기` là cách nói đời thường không có tương đương EN.** `유튜브 스크립트 따기` (100–1K) dùng động từ `따다` — nghĩa gốc là "hái, ngắt", giọng rất thân mật, đúng cách người Hàn gõ khi tìm công cụ. Bản EN không có gì tương ứng (`get a transcript` trung tính). Xử lý: cấp cho **H2 của S3** (`유튜브 영상 스크립트 따는 방법`) và `quickAnswer.question`, nơi giọng hướng dẫn cho phép văn phong đời thường.

5. **Nhóm `텍스트 변환` phải có chữ `유튜브` mới được dùng.** Trang generic `/ko/video-to-text` đã hoàn thành và đang giữ `영상 텍스트 변환` / `동영상 텍스트 추출`. Bản ko của trang này chỉ được dùng biến thể **có `유튜브`** (`유튜브 음성 텍스트 변환`, `유튜브 영상 텍스트 변환`, `유튜브 텍스트 추출`). Bản EN không chịu ràng buộc này.

6. **Rủi ro cannibalization ngược từ nhóm tải VIDEO nặng hơn EN.** `유튜브 영상 다운로드` / `유튜브 다운로드` ở Hàn Quốc là cụm khổng lồ, SERP toàn downloader MP4. Kỷ luật cứng: `다운로드`/`저장` chỉ đi với `스크립트`/`대본`/`텍스트`/`파일`. Bản EN không chịu áp lực này ở cùng mức.

7. **Thể văn.** Bản EN dùng giọng trung tính, câu ngắn. Bản ko dùng **합니다체** nhất quán toàn trang (trang trọng nhưng thân thiện, đúng chuẩn landing page công cụ Hàn Quốc), câu mệnh lệnh dùng `-세요` / `-면 됩니다`.

---

## Đối tượng người dùng

- Học sinh, sinh viên, người học online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Người học tiếng Anh qua video YouTube (nhu cầu rất lớn ở Hàn Quốc — cần script để đối chiếu)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ KO ⇄ EN ⇄ JA
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `ko.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 유튜브 스크립트 | 유튜브 스크립트 *(KW chính)* |
| — | **quickAnswer:** 유튜브 스크립트는 어떻게 따나요? | 유튜브 스크립트 따기 |
| 1 | 유튜브 스크립트란 무엇인가요? | 유튜브 스크립트, 유튜브 영상 스크립트 |
| 2 | 유튜브 스크립트 한눈에 보기 *(`specs` × 10)* | 유튜브 스크립트 |
| 3 | 유튜브 영상 스크립트 따는 방법 *(`steps` × 4)* | 유튜브 스크립트 따기, 유튜브 영상 스크립트 |
| 4 | 유튜브 스크립트 생성기 | 유튜브 스크립트 생성기, 유튜브 영상 스크립트 생성기 |
| 5 | 유튜브 스크립트 추출 | 유튜브 스크립트 추출, 유튜브 텍스트 추출, 유튜브 대본 추출 |
| 6 | 유튜브 스크립트 활용법 *(`items` × 6)* | 유튜브 스크립트, 유튜브 영상 스크립트 |
| 7 | 모든 언어로 유튜브 음성 텍스트 변환 | 유튜브 음성 텍스트 변환, 유튜브 영상 텍스트 변환, 유튜브 영상 스크립트 |
| 8 | TranscriptX와 유튜브 기본 스크립트 비교 *(`items` × 2)* | 유튜브 스크립트 *(so sánh với 자동 자막)* |
| 9 | 정확도와 정확도를 좌우하는 요소 | *(E-E-A-T, không nhắm KW)* |
| 10 | 유튜브 스크립트가 만들어지지 않는 경우 *(`items` × 5)* | 유튜브 스크립트 |
| 11 | 복사, 편집, 번역 또는 다운로드 | *(4 internal link — chốt phân định + neo `유튜브 자막 추출`)* |
| 12 | 자주 묻는 질문 *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion:** 무료로 유튜브 스크립트 받기 *(3 đoạn)* | 유튜브 스크립트, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- **S2 tái dùng đúng 8/10 nhãn `specs` đã duyệt ở `/ko/video-to-text/ko.json`**: `가격`, `계정 필요 여부`, `설치`, `언어`, `화자 분리`, `타임스탬프`, `지원 기기`, `내보내기 형식` — nguyên văn, không đổi chữ. Hai nhãn mới riêng của trang này: **`입력`** (Input — URL video YouTube) và **`자막 없는 영상`** (Works when the video has no captions). Hai nhãn của `/ko/video-to-text` **không dùng ở đây** vì không áp dụng: `파일 용량 제한`, `지원 형식` (trang này nhận URL chứ không nhận file).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại** — S4 giữ họ `생성기`, S5 giữ họ `추출` vốn là nhóm mạnh nhất của tiếng Hàn.
- **S8 là section so sánh** với 스크립트 tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. H3 item 1 là `유튜브 기본 스크립트` (KHÔNG dùng `자막` trên heading), nhưng body của nó được phép nói `제작자가 자막을 넣은 영상에만 존재합니다` vì đó đúng là mô tả cơ chế của YouTube.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào. Đây cũng là chỗ **duy nhất** cụm `유튜브 자막 추출` được phép xuất hiện.
- Thể **합니다체** nhất quán; câu hướng dẫn dùng `-세요` / `-면 됩니다`. Không trộn 해요체 hay 반말.
- Viết đúng chính tả, **không dấu cách thừa**: `유튜브` (một từ), `트랜스크립트` (một từ), `타임스탬프`, `화자 분리`, `텍스트`.
- Nhấn `무료` ở `title`, `hero.subtitle`, S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`유튜브 자막 추출` / `유튜브 자막 다운로드` / `유튜브 자막 저장` / `유튜브 srt 다운로드`** → **`/ko/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). Toàn bộ họ `자막` để trần thuộc trọn về trang đó. Trang này chỉ neo `유튜브 자막 추출` **1 lần** ở S11 rồi đẩy link đi.
- **`유튜브 스크립트 다운로드` / `유튜브 대본 다운로드` / `유튜브 스크립트 저장`** → **`/ko/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`유튜브 영상 텍스트 변환`**: giữ ở hub này (body S7) — không còn trang riêng cho cách gọi "영상을 텍스트로".
- **`유튜브 영상 요약` / `유튜브 요약기` / `유튜브 영상 요약 사이트`** → **`/ko/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`영상 텍스트 변환` / `동영상 텍스트 추출` / `비디오 텍스트 변환`** (không có chữ `유튜브`) → **`/ko/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `텍스트 변환` dùng ở trang này **bắt buộc phải có `유튜브`**.
- **`음성 텍스트 변환` / `녹음 텍스트 변환`** (không có `유튜브`) → **`/ko/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`유튜브 영상 다운로드` / `유튜브 다운로드` / `유튜브 mp4 변환` / `유튜브 저장`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Grep `영상 다운로드` phải = **0**.

### Sai intent hoàn toàn

- **Mọi cụm TTS** (`텍스트 음성 변환`, `글자 음성으로`, `텍스트를 음성으로`, `texttomp3`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ.
- **`유튜브 자막 켜기` / `유튜브 자막 설정`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link** — nhiều nhất dự án. Thứ tự và vai trò:

| Link | Anchor (ko) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/ko/download-youtube-transcript` | 유튜브 스크립트 다운로드 | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/ko/youtube-subtitle-downloader` | 유튜브 자막 다운로더 | Cần đúng **file phụ đề** SRT/VTT khớp giờ — **đồng thời là nơi neo `유튜브 자막 추출`** |
| `/ko/youtube-video-summarizer` | 유튜브 영상 요약기 | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho ko.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
  - ⚠️ Trong body tiếng Hàn dùng `유튜브` (Hangul) khi là keyword; giữ `YouTube` dạng Latin khi là tên thương hiệu trong ngữ cảnh kỹ thuật. `ko.json` dùng `유튜브` xuyên suốt để khớp keyword.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/ko/...)`, đổi path sang `/ko/`.
- Thuật ngữ khớp các trang ko đã duyệt (`/ko/video-to-text`, `/ko/youtube-subtitle-downloader`): `타임스탬프` (timestamps), `화자 분리` (speaker separation), `파일` (file), `링크` (link), `브라우저` (browser), `가입 불필요` / `계정 필요 없음` (no sign-up), `자동 감지` (auto-detected), `내보내기` (export).
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ.
- **Kiểm tra bắt buộc trước khi bàn giao — ĐÃ CHẠY, ĐỀU PASS:**
  1. `python3 shape_check.py en.json ko.json` → **`ko.json -> True`** ✅
  2. `grep -c '영상 다운로드'` → **0** ✅
  3. `grep -o '유튜브 자막 추출' | wc -l` → **1** ✅ *(đúng 1 lần, ở S11)*
  4. `자막` trên heading (31 heading) → **0** ✅
  5. `grep -c 'texttomp3'` → **0** ✅
  6. 4 path internal link đúng `/ko/` prefix, đủ 4, không thừa không thiếu ✅
