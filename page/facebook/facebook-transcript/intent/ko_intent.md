🔥 TranscriptX – Facebook Transcript (Korean / ko)

URL:
/ko/facebook-transcript

Intent chính:

페이스북 영상 텍스트 변환 (무료 온라인)

Trang này là **bản tiếng Hàn của trang trụ (hub)** cụm Facebook. Nhắm đến người dùng Hàn Quốc có một video Facebook (영상 게시물, 릴스, Watch, 페이스북 라이브 đã lưu, video trong 그룹/페이지) và muốn dán link để lấy toàn bộ lời nói thành văn bản — để đọc, tìm kiếm, sao chép, chỉnh sửa, trích dẫn hoặc lưu lại.

Gộp toàn bộ intent đồng nghĩa **텍스트 변환 / 텍스트 추출 / 받아쓰기** vì tất cả cho ra **cùng một kết quả**: video Facebook → 텍스트.

---

## ⚠️ Cảnh báo dữ liệu & ngôn ngữ (đọc trước khi viết ko.json)

### 1. Lỗi chèn dấu cách trong `2_loc_kw.md`

Danh sách keyword tiếng Hàn bị **chèn dấu cách sai** — artifact của công cụ search, KHÔNG phải cách viết thật. `페이스북` là **MỘT từ**, không bao giờ tách thành `페이스 북`. Trợ từ (`로/으로`) cũng không được tách khỏi danh từ.

| Trong file (SAI) | Dạng đúng (dùng trong intent & ko.json) |
| ---------------- | --------------------------------------- |
| `페이스 북 영상 자막 추출` | `페이스북 영상 자막 추출` |
| `페이스 북 동영상 텍스트 변환` | `페이스북 동영상 텍스트 변환` |
| `페이스 북 동영상 텍스트 로 변환` | `페이스북 동영상 텍스트로 변환` |
| `페이스 북 라이브 텍스트 변환` | `페이스북 라이브 텍스트 변환` |

> Toàn bộ file này và `ko.json` **ghi ở dạng đúng chính tả**. Viết theo dạng sai sẽ khiến Google tokenize thành cụm vô nghĩa và người Hàn đọc thấy văn bản lỗi.

### 2. Keyword cuối thiếu dòng volume

`페이스북 영상 음성 텍스트 변환` trong file gốc **thiếu dòng volume** (bị cắt ở cuối block ko). Keyword vẫn **hợp lệ và đã được search** — ghi Volume `—`, Nguồn `✅ đã search (thiếu volume trong file gốc)`.

### 3. `페이스북` (Hangul) vs `facebook` (Latin)

Danh sách có **cả hai dạng**: 12 keyword dùng `페이스북` Hangul, 1 keyword dùng `facebook` Latin (`facebook 영상 자막 추출`).

**Chiến lược phân bổ:**
- `페이스북` Hangul → `seo.title`, `hero.h1`, **toàn bộ H2**, văn xuôi body. Đây là dạng chiếm gần như toàn bộ volume.
- `Facebook` Latin → chỉ dùng khi **gọi tên tính năng chính thức** (`Facebook Live`, `Facebook Watch`) và trong `seo.description` / bảng `specs` để bắt biến thể Latin. **Không** đặt Latin vào H1/H2.

### 4. `영상` vs `동영상`

Cả hai đều xuất hiện trong danh sách đã search (7 keyword dùng `영상`, 4 keyword dùng `동영상`). Đây là **hai biến thể thật**, không được bỏ một cái.

**Chiến lược phân bổ:**
- `영상` (ngắn, phổ biến hơn, xuất hiện trong KW head + các modifier 무료/사이트/음성) → `seo.title`, `hero.h1`, H2 section 1, 3, 4, 6, 8.
- `동영상` (trang trọng hơn) → H2 **section 5** (`페이스북 동영상 텍스트로 변환`), bảng `specs`, và rải trong FAQ. Như vậy phủ trọn cả cụm `페이스북 동영상 텍스트 변환` mà không lặp thừa.

---

## 🚨 CẢNH BÁO INTENT QUAN TRỌNG — cụm `자막` KHÔNG phải intent chính

Danh sách ko nghiêng nặng về `자막` (phụ đề/subtitle): **5/13 keyword** thuộc nhóm này — `자막 추출` (×2), `자막 다운로드`, `릴스 자막 추출`, `자막 ai`. Đây là tỷ lệ cao nhất trong tất cả các ngôn ngữ của trang này (bản ar và es đều **không có** nhiễm intent).

**Vì sao lệch:** trang này tạo transcript **từ audio** (nhận dạng giọng nói), KHÔNG phải tải file phụ đề có sẵn. Người search cụm `자막` chia làm hai loại rất khác nhau:

| Keyword | Mức lệch | Phân tích | Xử lý |
| ------- | -------- | --------- | ----- |
| `페이스북 동영상 자막 다운로드` | 🔴 **Lệch nhất** | Intent rõ ràng là **tải file phụ đề đã tồn tại** (.srt) từ video. SERP là subtitle downloader / extension, page type hoàn toàn khác. Sản phẩm không có tính năng này. | **Không tối ưu.** Chỉ nhắc gián tiếp **1 lần trong section 7** khi nói về xuất SRT/VTT — vì đó là thứ TranscriptX thật sự làm được (tạo ra file phụ đề, không phải tải về file có sẵn). Cấm đưa vào title/H1/H2/FAQ question. |
| `페이스북 동영상 자막 ai` | 🟠 Lệch vừa | AI tạo phụ đề — gần với ta hơn (ta cũng dùng AI, cũng xuất SRT), nhưng vẫn là output "phụ đề" chứ không phải "transcript đọc được". | Body **section 4** (đoạn nói về AI + không cần caption). Không lên H2. |
| `페이스북 영상 자막 추출` | 🟡 Lệch nhẹ | Nhiều người Hàn dùng `자막 추출` như cách gọi dân dã cho "lấy chữ ra khỏi video" — trùng job với ta, nhưng chữ `추출` ngụ ý phụ đề **đã có sẵn**. | Body **section 1** và **section 4**. Không lên H1/H2 — thay bằng `텍스트 추출` (đúng intent, cùng động từ `추출`). |
| `facebook 영상 자막 추출` | 🟡 Lệch nhẹ | Như trên, thêm biến thể Latin. | Body **section 4** (1 lần, dạng Latin). |
| `페이스북 릴스 자막 추출` | 🟡 Lệch nhẹ | Đúng định dạng nội dung (Reels), sai động từ đích. | Body **item Reels của section 6**, viết lại thành `릴스 텍스트 추출` + nhắc `자막` một lần. |

**Kết luận:** cụm đúng intent chính là **`텍스트 변환` / `텍스트 추출` / `받아쓰기`** → đây là nhóm được ưu tiên cho `seo.title`, `hero.h1` và toàn bộ H2. **Không một keyword nhóm `자막` nào được lên title/H1/H2.**

---

## Từ khóa chính

페이스북 동영상 텍스트 변환 (0–10) ✅ *đã search*

*(Ghi chú: cụm thân `페이스북 영상 텍스트 변환` là **stem chung của 3 keyword đã search** — `페이스북 영상 텍스트 변환 무료`, `페이스북 영상 텍스트 변환 사이트`, `페이스북 영상 음성 텍스트 변환` — nên được dùng làm **dạng head trong `seo.title` và `hero.h1`**, còn dạng `동영상` được đặt nguyên cụm vào H2 section 5. Hai dạng bổ trợ nhau, không cạnh tranh.)*

---

## Từ khóa phụ

### Nhóm 텍스트 변환 (chuyển thành text — trục chính, ĐÚNG intent)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 페이스북 동영상 텍스트 변환 | 0–10 | ✅ đã search *(KW chính)* |
| 페이스북 동영상 텍스트로 변환 | 0–10 | ✅ đã search *(đã sửa dấu cách trợ từ)* |
| 페이스북 영상 텍스트 변환 무료 | 0–10 | ✅ đã search |
| 페이스북 영상 텍스트 변환 사이트 | 0–10 | ✅ đã search |
| 페이스북 영상 음성 텍스트 변환 | — | ✅ đã search (thiếu volume trong file gốc) |
| 페이스북 라이브 텍스트 변환 | 0–10 | ✅ đã search |
| 페이스북 영상 텍스트 변환 | — | 🔄 dịch bổ sung (stem chung, dạng head) |

### Nhóm 텍스트 추출 / 받아쓰기 (trích xuất & bóc băng — ĐÚNG intent)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 페이스북 영상 텍스트 추출 | 0–10 | ✅ đã search |
| 페이스북 영상 받아쓰기 | 0–10 | ✅ đã search |
| 페이스북 영상 녹취록 | — | 🔄 dịch bổ sung (Facebook video transcript) |
| 페이스북 영상 텍스트 변환 도구 | — | 🔄 dịch bổ sung (Facebook transcript tool) |
| 가입 없이 페이스북 영상 텍스트 변환 | — | 🔄 dịch bổ sung (no sign-up) |

### Nhóm định dạng nội dung Facebook (라이브 / 릴스)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 페이스북 라이브 텍스트 변환 | 0–10 | ✅ đã search |
| 페이스북 릴스 자막 추출 | 0–10 | ⚠️ đã search — **hạ xuống body** (nhóm 자막) |
| 페이스북 릴스 텍스트 추출 | — | 🔄 dịch bổ sung (dạng đúng intent thay thế) |

### Nhóm `자막` — ĐÃ SEARCH nhưng LỆCH INTENT, chỉ dùng body/FAQ

| Keyword | Volume | Nguồn | Vị trí cho phép |
| ------- | ------ | ----- | --------------- |
| 페이스북 영상 자막 추출 | 0–10 | ⚠️ đã search — hạ xuống body | section 1, section 4 |
| facebook 영상 자막 추출 | 0–10 | ⚠️ đã search — hạ xuống body | section 4 (dạng Latin) |
| 페이스북 동영상 자막 ai | 0–10 | ⚠️ đã search — hạ xuống body | section 4 |
| 페이스북 릴스 자막 추출 | 0–10 | ⚠️ đã search — hạ xuống body | section 6, item Reels |
| 페이스북 동영상 자막 다운로드 | 0–10 | ❌ **loại khỏi tối ưu** | chỉ nhắc gián tiếp ở section 7 (SRT/VTT) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, **được phép và nên** đặt vào `title` / `h1` / `h2` / `description`. ⚠️ *hạ xuống body* = đã search nhưng lệch intent, **chỉ rải trong body/FAQ**, cấm lên title/H1/H2. 🔄 *dịch bổ sung* = chỉ rải trong body để phủ ngữ nghĩa, không đặt vào title/H1.

---

## Search Intent

Người dùng Hàn Quốc có một video Facebook — thường là **페이스북 라이브 đã lưu** (웨비나, Q&A, 설교, 온라인 강의, 커뮤니티 모임), video trong 그룹/페이지, hoặc 릴스 — và muốn lấy nội dung lời nói thành 텍스트 để đọc, tìm kiếm, trích dẫn, ghi chú hoặc lưu trước khi bị xóa.

Họ thường kỳ vọng:

- Chỉ cần **dán link** (`링크만 붙여넣기`), không tải file, không cài `프로그램`.
- **Miễn phí thật** — `무료` có hẳn keyword riêng.
- Đây là một **웹사이트** dùng ngay trong trình duyệt — `사이트` cũng có keyword riêng.
- Chạy được cả khi video **không có 자막** sẵn (đây chính là điểm bán hàng để trả lời nhóm search `자막`).
- Nhận dạng tốt **tiếng Hàn**.
- Tách được nhiều người nói (`화자 분리`) — quan trọng với 라이브 / 인터뷰 / 좌담.
- Không cần đăng nhập Facebook, không cần app.

### Khác biệt so với bản tiếng Anh

1. **Nhiễm intent `자막` — bản EN hoàn toàn không có.** Bản EN chỉ nhắc "captions" như một điểm khác biệt kỹ thuật ở section 4. Bản ko có **5/13 keyword** thuộc cụm `자막`, tức gần 40% danh sách. Hệ quả: section 4 (`works without captions`) ở bản ko phải làm **hai việc cùng lúc** — vừa là điểm bán hàng, vừa là nơi thu hết lưu lượng `자막 추출` / `자막 ai` mà không để cụm này leo lên H1/H2 và làm lệch page type. Bản EN không cần cân nhắc này.
2. **`영상` và `동영상` là hai biến thể phải phủ song song.** Bản EN chỉ có một từ `video`. Bản ko phải luân phiên có chủ đích giữa `영상` (H1/title/đa số H2) và `동영상` (H2 section 5 + specs + FAQ), nếu không sẽ mất trọn 4 keyword nhóm `동영상`.
3. **`사이트` và `프로그램` là intent tách bạch (giống trang audio-to-text ko).** `페이스북 영상 텍스트 변환 사이트` = tìm web tool. Người Hàn mặc định nghĩ tác vụ này cần **cài phần mềm**, nên phải trả lời trực tiếp: đây là 사이트, `프로그램 설치 없이` dùng ngay. Bản EN chỉ nói nhẹ "nothing to install".
4. **`받아쓰기` là động từ bản địa không có tương đương trực tiếp trong EN.** Bản EN dùng `transcribe`; tiếng Hàn tách thành `텍스트 변환` (kỹ thuật/trung tính) và `받아쓰기` (bóc băng, đời thường). Phải dùng cả hai — `받아쓰기` đặt vào H2 section 3 hoặc 4, không được dịch chìm hết thành `변환`.
5. **`페이스북 라이브` nặng ký hơn `릴스` — ngược với bản es.** Bản es có `transcribir reel de facebook` (10–100) mạnh hơn Live. Bản ko thì `페이스북 라이브 텍스트 변환` là keyword đúng intent, còn Reels chỉ xuất hiện dưới dạng lệch (`릴스 자막 추출`). Nên item Live ở section 6 phải viết dày dặn hơn item Reels.

---

## Đối tượng người dùng

- Người xem **페이스북 라이브** (웨비나, Q&A 세션, 온라인 강의, 설교, 커뮤니티 모임)
- Admin **페이스북 그룹 / 페이지** Hàn Quốc
- 마케터 / 소셜 미디어 담당자
- 학생, 교사, 연구자 (강의·세미나 영상 정리)
- 기자 — cần trích dẫn chính xác phát biểu từ video Facebook
- 콘텐츠 크리에이터 tái sử dụng nội dung (릴스 → 블로그, 스레드, 뉴스레터)
- Người cần lưu nội dung video trước khi bị xóa
- 청각 장애인 hoặc người ở nơi không bật được tiếng

---

## Map H2 → keyword (bám ĐÚNG 9 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng 9 section của `en.json`, cùng số đoạn `content`, đúng 10 `specs`, đúng 4 `steps`, đúng 5 `items` ở section 6, đúng 9 FAQ, đúng 2 đoạn `conclusion`. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 페이스북 영상 텍스트 변환 | 페이스북 영상 텍스트 변환 *(stem chính; `페이스북 동영상 텍스트 변환` ở subtitle)* |
| — | **quickAnswer** | 페이스북 영상 텍스트 변환, 페이스북 영상 텍스트 추출 |
| 1 | 페이스북 영상 텍스트 변환이란? | 페이스북 영상 텍스트 변환, 페이스북 영상 텍스트 추출, `자막 추출` ⚠️ *(chỉ trong body đoạn 3)* |
| 2 | 페이스북 영상 텍스트 변환 한눈에 보기 | *(bảng thông số — 무료 / 100개 이상 언어 / 가입 불필요 / Facebook Latin)* |
| 3 | 페이스북 영상에서 텍스트를 추출하는 방법 | 페이스북 영상 텍스트 추출, 페이스북 영상 받아쓰기 |
| 4 | 자막 없이도 되는 페이스북 영상 AI 받아쓰기 | 페이스북 영상 받아쓰기, 페이스북 영상 음성 텍스트 변환 + ⚠️ `자막 추출`, `facebook 영상 자막 추출`, `동영상 자막 ai` *(body)* |
| 5 | 페이스북 동영상 텍스트로 변환 | 페이스북 동영상 텍스트로 변환, 페이스북 동영상 텍스트 변환 *(KW chính)* |
| 6 | 페이스북에서 텍스트로 바꿀 수 있는 영상 | 페이스북 라이브 텍스트 변환, ⚠️ 페이스북 릴스 자막 추출 *(item Reels, body)* |
| 7 | 복사, 편집, 번역, 다운로드 | *(internal link sang /ko/youtube-transcript, /ko/tiktok-transcript, /ko/audio-to-text; nhắc SRT/VTT — chạm nhẹ `자막 다운로드`)* |
| 8 | 정확도와 지원 언어 | 페이스북 영상 음성 텍스트 변환 *(+ nhấn tiếng Hàn)* |
| 9 | 자주 묻는 질문 | 페이스북 영상 텍스트 변환 무료, 페이스북 영상 텍스트 변환 사이트, 페이스북 영상 텍스트 변환 도구 🔄 + long-tail |
| — | **conclusion** | 페이스북 영상 텍스트 변환, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- **Section 4 là "van xả" của toàn bộ nhóm `자막`.** Bản EN vốn đã nói về "works without captions" — chỉ cần chọn từ khi dịch để cụm `자막 추출` / `자막 ai` xuất hiện tự nhiên trong đó. Không thêm câu, không thêm H2, không đưa `자막` lên H2.
- Keyword `페이스북 라이브 텍스트 변환` đặt vào **item số 1 của section 6** (Saved Facebook Live) — đúng chỗ, không cần section mới.
- Keyword `페이스북 릴스 자막 추출` đặt vào **item số 3 của section 6** (Reels), nhưng viết ưu tiên dạng đúng intent `릴스 텍스트 추출` và chỉ nhắc `자막` một lần trong cùng câu.
- Intent `프로그램` xử lý **trong section 2 (specs) và section 3 step 2** bằng vế phủ định trực tiếp (`설치할 프로그램 없이`) — vừa bắt KW vừa không thêm câu.
- `페이스북 영상 텍스트 변환 무료` và `... 사이트` gom vào **FAQ 1 và FAQ 2** — đúng chỗ bản EN đã có sẵn câu hỏi "for free" / "free generator".
- `페이스북 동영상 자막 다운로드` **không được đặt nguyên cụm ở bất kỳ đâu**. Chỉ để section 7 nói đúng sự thật: xuất SRT/VTT là **tạo** file phụ đề, không phải tải phụ đề có sẵn.
- Nỗi lo "công cụ có nhận dạng được tiếng Hàn không" xử lý **bên trong section 8** bằng cách thay ví dụ ngôn ngữ của bản EN (Spanish Live / Tagalog Reel) bằng ví dụ có tiếng Hàn — không thêm câu, không thêm H2.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `유튜브 영상 텍스트 변환` / `유튜브 자막 추출` / `유튜브 스크립트 추출` → **/ko/youtube-transcript**
- `틱톡 영상 텍스트 변환` / `틱톡 자막 추출` → **/ko/tiktok-transcript**
- `음성 텍스트 변환` / `녹음 파일 텍스트 변환` / `mp3 텍스트 변환` / `오디오 텍스트 변환` → **/ko/audio-to-text** (nguồn là **file âm thanh**, không phải video Facebook)
- `페이스북 영상 다운로드` / `페이스북 동영상 저장` / `페북 영상 다운` → intent **tải video**, KHÔNG phải transcript. Đây là nhóm nhiễm nguy hiểm nhất của cụm Facebook tiếng Hàn: volume rất lớn và SERP toàn downloader — kéo vào sẽ làm lệch page type.
- `텍스트 음성 변환` / `TTS` → **NGƯỢC intent**, thuộc trang Text-to-Speech. Cẩn thận thứ tự từ: `텍스트 변환` (đúng) vs `텍스트 음성 변환` (sai trang).
- `페이스북 동영상 자막 다운로드` → intent **tải file phụ đề có sẵn**, page type là subtitle downloader. Xem phân tích ở mục cảnh báo intent phía trên.

---

## Internal linking

- ↔ /ko/youtube-transcript, /ko/tiktok-transcript (cross-cluster: cùng nhu cầu transcript, nền tảng khác)
- → /ko/audio-to-text (khi user có file âm thanh thay vì video Facebook)

---

## Ghi chú kỹ thuật cho ko.json

- `lang="ko"`, `dir="ltr"`.
- **Thể văn: `합니다`체** lịch sự chuẩn, xuyên suốt — **nhất quán với `/ko/audio-to-text/ko.json`**. Không dùng `해요`체 (quá thân mật), không dùng `한다`체 (quá khô). Văn phong tự nhiên như người bản xứ viết, không dịch máy word-by-word.
- **Không chèn dấu cách sai:** `페이스북` (một từ), `텍스트로` (không tách trợ từ `로`). Lỗi này có sẵn trong `2_loc_kw.md`, đã sửa toàn bộ.
- Giữ nguyên Latin, không phiên âm: **TranscriptX, TXT, DOCX, PDF, SRT, VTT, URL**.
- Nền tảng: dùng **`페이스북`** Hangul trong H1/H2/văn xuôi (bám keyword đã search); giữ **`Facebook`** Latin khi gọi tên tính năng chính thức (`Facebook Live`, `Facebook Watch`) và trong `seo.description` + bảng `specs` để bắt biến thể Latin.
- `Reels` → **`릴스`** Hangul (bám keyword `페이스북 릴스 자막 추출`). `Live` → **`라이브`** Hangul (bám keyword `페이스북 라이브 텍스트 변환`), riêng tên tính năng đầy đủ giữ `Facebook Live`.
- Thuật ngữ chuẩn hoá: speaker separation → `화자 분리`; transcript → `변환된 텍스트` / `녹취록` (tuỳ ngữ cảnh); subtitles → `자막`; punctuation → `문장 부호`.
- Số đếm dùng chữ số Latin (100+, 5).
- Internal link trong `sections[6]` (section 7) giữ nguyên cú pháp markdown, đổi path: `[유튜브 영상 텍스트 변환](/ko/youtube-transcript)`, `[틱톡 영상 텍스트 변환](/ko/tiktok-transcript)`, `[음성 텍스트 변환](/ko/audio-to-text)`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, 9 sections, 10 specs, 4 steps, 5 items (section 6), 9 FAQ, `conclusion` h2 + 2 đoạn.
