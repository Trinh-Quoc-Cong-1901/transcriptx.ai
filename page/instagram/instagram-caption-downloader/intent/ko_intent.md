🔥 TranscriptX – Instagram Caption Downloader (Korean / ko)

URL:
/ko/instagram-caption-downloader

Intent chính:

인스타그램 캡션 다운로드 (무료 온라인 · 복사)

Trang này là **bản tiếng Hàn** của trang Instagram Caption Downloader. Nhắm đến người dùng Hàn Quốc muốn lấy **캡션 / 설명** (phần chữ do tác giả **GÕ** dưới bài đăng) từ Instagram 게시물, 릴스 hoặc 동영상 — để sao chép (`복사`), lưu (`저장`), dịch, phân tích hoặc tái sử dụng.

Gộp toàn bộ intent đồng nghĩa **다운로드 / 복사 / 저장 / 추출 / 가져오기** vì tất cả cho ra **cùng một kết quả**: caption Instagram → 텍스트.

---

## ⚠️ Cảnh báo dữ liệu & ngôn ngữ (đọc trước khi viết ko.json)

### 1. Lỗi chèn dấu cách trong `2_loc_kw.md`

Danh sách keyword tiếng Hàn trong file nguồn bị **chèn dấu cách sai** — artifact của công cụ search, KHÔNG phải cách viết thật của người Hàn. `인스타` là **MỘT từ**, `인스타그램` là **MỘT từ**, `가져오기` là **MỘT từ**.

| Trong file (SAI) | Dạng đúng (dùng trong intent & ko.json) |
| ---------------- | --------------------------------------- |
| `인스 타 캡션 복사` | `인스타 캡션 복사` |
| `인스 타 그램 캡션 다운로드` | `인스타그램 캡션 다운로드` |
| `인스 타 그램 게시물 설명 저장` | `인스타그램 게시물 설명 저장` |
| `인스 타 동영상 캡션 다운로드` | `인스타 동영상 캡션 다운로드` |
| `인스 타 캡션 추출` | `인스타 캡션 추출` |
| `인스 타 그램 캡션 다운로더` | `인스타그램 캡션 다운로더` |
| `인스 타 릴스 캡션 다운로드` | `인스타 릴스 캡션 다운로드` |
| `인스 타 캡션 텍스트 복사` | `인스타 캡션 텍스트 복사` |
| `인스 타 그램 설명 다운로드` | `인스타그램 설명 다운로드` |
| `인스 타 링크 캡션 가져 오기` | `인스타 링크 캡션 가져오기` |
| `인스 타 캡션 온라인 다운로드` | `인스타 캡션 온라인 다운로드` |
| `인스 타 그램 게시물 텍스트 저장` | `인스타그램 게시물 텍스트 저장` |

> Toàn bộ file này và `ko.json` **ghi ở dạng đúng chính tả**. Viết theo dạng sai sẽ khiến Google tokenize thành cụm vô nghĩa và người Hàn đọc thấy văn bản lỗi. Xử lý y hệt cách đã làm ở `/ko/facebook-transcript` (`페이스 북` → `페이스북`).

### 2. ⚠️ PHÂN ĐỊNH INTENT SỐNG CÒN: Caption ≠ Transcript

Trang này lấy chữ tác giả **VIẾT** (`캡션`, `설명`, `해시태그`, `이모지`). Trang anh em `/ko/instagram-transcript` lấy chữ người ta **NÓI** trong video (`음성`, `말한 내용`, `텍스트 변환`). Section 2 của `en.json` tồn tại **chính để phân định điều này** — bản `ko` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau.

> 🚨 **RIÊNG TIẾNG HÀN: TUYỆT ĐỐI KHÔNG DÙNG `자막` ĐỂ CHỈ CAPTION.**
> `자막` trong tiếng Hàn nghĩa là **phụ đề video** (subtitle) — thuộc intent hoàn toàn khác (`자막 추출`, `자막 다운로드`, page type = subtitle downloader). Người Hàn search `인스타 자막` là đang tìm phụ đề trong video, **không phải** phần chữ dưới bài. Dùng `자막` ở trang này sẽ:
> - kéo sai traffic (người muốn phụ đề, bounce ngay),
> - làm Google hiểu nhầm page type,
> - và cạnh tranh trực tiếp với `/ko/instagram-transcript`.
>
> Đáng chú ý: **cả 12 keyword đã search của cụm ko trang này đều KHÔNG chứa `자막`** — chỉ có `캡션`, `설명`, `텍스트`. Đây là bằng chứng dữ liệu rằng người Hàn phân biệt rất rõ hai khái niệm. Bám theo dữ liệu: chỉ dùng `캡션` / `설명` / `텍스트`.

### 3. `인스타` (viết tắt) vs `인스타그램` (đầy đủ)

Danh sách có **cả hai dạng**: 7 keyword dùng `인스타` (gồm cả KW mạnh nhất), 5 keyword dùng `인스타그램`. Đây là **hai biến thể thật**, không được bỏ một cái.

**Chiến lược phân bổ:**
- `인스타그램` (đầy đủ, trang trọng, khớp tên thương hiệu) → `seo.title`, **`hero.h1`**, H2 section 1, H2 section 3, `conclusion.h2`. Đây là dạng an toàn cho SEO thương hiệu và khớp URL Latin `instagram`.
- `인스타` (viết tắt, khẩu ngữ, chiếm KW volume cao nhất `인스타 캡션 복사`) → **H2 section 5** (van xả nhóm `복사`), body section 4, và rải trong FAQ. Đây là cách người Hàn thật sự gõ khi search.
- Trong cùng một đoạn văn nên luân phiên tự nhiên, không lặp cứng một dạng.

### 4. `캡션` vs `설명`

Danh sách có **cả hai**: 8 keyword dùng `캡션`, 2 keyword dùng `설명` (`인스타그램 게시물 설명 저장`, `인스타그램 설명 다운로드`), 2 keyword dùng `텍스트` (`인스타 캡션 텍스트 복사`, `인스타그램 게시물 텍스트 저장`).

**Chiến lược phân bổ:**
- `캡션` (mượn Anh, là cách gọi phổ biến nhất trong giới creator Hàn) → trục chính: title, H1, đa số H2.
- `설명` (thuần Hàn, "phần mô tả") → **section 4 item "저장"** và **FAQ** — phủ trọn 2 keyword nhóm `설명` mà không làm loãng trục `캡션`. Dùng tối thiểu 3 lần trong body.
- `텍스트` → dùng làm từ nối tự nhiên khi nói về kết quả đầu ra (`텍스트로 복사`, `텍스트 저장`), phủ 2 keyword nhóm `텍스트`.
- Ba từ này **bổ trợ**, không cạnh tranh — người Hàn dùng lẫn lộn cả ba khi nói về cùng một thứ.

---

## Từ khóa chính

인스타그램 캡션 다운로드 (0–10) ✅ *đã search*

*(Đây là KW đóng khung page type, khớp EN `instagram caption downloader` + URL `/ko/instagram-caption-downloader`. Dùng nguyên cụm ở `seo.title` và **`hero.h1`**.)*

> ⚠️ **BẮT BUỘC: H1 phải là keyword tiếng Hàn đã search, KHÔNG được để nguyên tên tiếng Anh "Instagram Caption Downloader".** H1 để tiếng Anh sẽ bắt được **0 keyword** trong 12 KW đã search của cụm ko. So sánh: bản `de` H1 = `Instagram Caption herunterladen` (đã dịch động từ), bản `ko` H1 = **`인스타그램 캡션 다운로드`**.

---

## Từ khóa mạnh nhất theo volume (dùng ở H2, KHÔNG ở H1)

인스타 캡션 복사 (10–100) ✅ *đã search*

> ⚠️ Đây là keyword **duy nhất vượt band `0–10`**; 11 keyword còn lại đều `0–10`. Nhưng intent của nó là **COPY**, không phải **DOWNLOAD** — trong khi page type, URL và bản EN đều đóng khung `downloader`.
>
> **Quyết định đã chốt với người dùng: H1 GIỮ KHUNG `다운로드`.** Nhóm `복사` đưa xuống **H2 section 5 + body** — đúng chỗ bản EN vốn đã nói về "what you copy reads the same as what was on the post". Xem `de.json` section 5 làm mẫu (bản de xử lý y hệt với `instagram text kopieren` 100–1K).
>
> Cách này giữ được cả hai: page type chính xác ở H1, còn trọng số SEO của cụm `복사` được cấp hẳn một H2 riêng.

---

## Từ khóa phụ

### Nhóm 다운로드 (trục chính — khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 인스타그램 캡션 다운로드 | 0–10 | ✅ đã search *(KW chính)* |
| 인스타 동영상 캡션 다운로드 | 0–10 | ✅ đã search |
| 인스타 릴스 캡션 다운로드 | 0–10 | ✅ đã search |
| 인스타그램 설명 다운로드 | 0–10 | ✅ đã search |
| 인스타 캡션 온라인 다운로드 | 0–10 | ✅ đã search |
| 인스타그램 캡션 다운로더 | 0–10 | ✅ đã search *(dạng danh từ — tên công cụ)* |

### Nhóm 복사 (volume cao nhất — dồn vào section 5)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 인스타 캡션 복사 | 10–100 | ✅ đã search *(KW mạnh nhất — H2 section 5)* |
| 인스타 캡션 텍스트 복사 | 0–10 | ✅ đã search |

### Nhóm 저장 (lưu lại)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 인스타그램 게시물 설명 저장 | 0–10 | ✅ đã search |
| 인스타그램 게시물 텍스트 저장 | 0–10 | ✅ đã search |

### Nhóm 추출 / 가져오기 (trích xuất từ link)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 인스타 캡션 추출 | 0–10 | ✅ đã search |
| 인스타 링크 캡션 가져오기 | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải trong body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 인스타 해시태그 복사 | — | 🔄 dịch bổ sung (keep the hashtag set) |
| 인스타그램 캡션 무료 다운로드 | — | 🔄 dịch bổ sung (free) |
| 앱 없이 인스타 캡션 복사 | — | 🔄 dịch bổ sung (no install) |
| 인스타그램 캡션 번역 | — | 🔄 dịch bổ sung (translate a caption) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải trong body, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Hàn Quốc thấy một caption Instagram hay (của mình hoặc của đối thủ) và muốn lấy nguyên văn phần chữ đó ra ngoài app — vì Instagram **không có nút copy caption**, và bôi đen trên điện thoại thì rất khó, hay dính nhầm chỗ hoặc dính cả comment.

Họ thường kỳ vọng:

- Chỉ cần **dán link** (`링크만 붙여넣기`), không đăng nhập Instagram.
- Lấy **nguyên vẹn** `해시태그`, `이모지` và ngắt dòng — không bị gộp thành một cục.
- Chạy được với 사진 게시물, 캐러셀, 릴스 và 동영상.
- **Miễn phí** (`무료`), không cài `앱`.
- **Copy được ngay** để dán sang chỗ khác — đây là kỳ vọng mạnh nhất, phản ánh qua KW `인스타 캡션 복사` (10–100).

### Khác biệt so với bản tiếng Anh

1. **Intent `복사` mạnh hơn `다운로드` — ngược hoàn toàn với bản EN.** Bản EN đóng khung là "downloader" và cụm download có volume thật (`instagram caption downloader` 10K–100K). Bản ko thì ngược: `인스타 캡션 복사` một mình chiếm band 10–100, còn **mọi cụm `다운로드` đều 0–10**. Lý do văn hóa: người Hàn không nghĩ caption là thứ "tải về" (`다운로드` gợi liên tưởng tải file/video), mà là thứ "chép ra" (`복사`). Đã xử lý bằng cách giữ H1 `다운로드` (khớp page type + URL) nhưng cấp hẳn H2 section 5 cho `복사`.
2. **Rủi ro `자막` — bản EN hoàn toàn không có.** Tiếng Anh "caption" đa nghĩa nhưng ở ngữ cảnh Instagram thì rõ ràng là phần chữ dưới bài. Tiếng Hàn tách bạch hẳn: `캡션` = chữ dưới bài, `자막` = phụ đề video. Bản ko phải **chủ động cấm** `자막` — một rủi ro bản EN không hề có, và là lý do section 2 ở bản ko quan trọng hơn cả bản EN.
3. **`인스타` và `인스타그램` là hai biến thể phải phủ song song.** Bản EN chỉ có một từ `Instagram`. Bản ko phải luân phiên có chủ đích giữa `인스타그램` (H1/title/H2 chính) và `인스타` (H2 section 5 + body + FAQ), nếu không sẽ mất trọn 7 keyword nhóm viết tắt — trong đó có cả KW mạnh nhất.
4. **`설명` là trục thứ hai, không phải từ đồng nghĩa phụ.** Bản EN dùng "caption" và "description" gần như thay thế nhau tự do. Bản ko có 2 keyword riêng cho `설명` (`게시물 설명 저장`, `설명 다운로드`) — phải dùng xen kẽ có chủ đích chứ không chọn một.
5. **Nhóm `저장` tách bạch khỏi `다운로드`.** Người Hàn phân biệt `다운로드` (tải về máy) với `저장` (lưu lại để dùng sau). Bản EN gộp cả hai vào "download"/"save". Bản ko phải cho `저장` một chỗ đứng riêng — đặt vào section 4 (item "lưu caption trước khi bị sửa"), đúng nghĩa gốc.

---

## Đối tượng người dùng

- 소셜 미디어 마케터 / 담당자 (phân tích caption đối thủ)
- 인스타그램 콘텐츠 크리에이터 Hàn Quốc (lưu swipe file caption hiệu quả)
- 프리랜서 làm Instagram cho khách hàng
- 쇼핑몰 / 브랜드 운영자 (nghiên cứu caption bán hàng)
- Người muốn dịch caption tiếng nước ngoài sang tiếng Hàn
- Người lưu lại caption trước khi bài bị sửa/xóa
- 대행사 직원 làm báo cáo nội dung
- 해시태그 리서치 하는 사람 (lấy nguyên bộ hashtag)

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, đúng 2 đoạn `conclusion`. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1: 인스타그램 캡션 다운로드** | 인스타그램 캡션 다운로드 *(KW chính — BẮT BUỘC tiếng Hàn, không để "Instagram Caption Downloader")* |
| — | **quickAnswer** | 인스타그램 캡션 다운로드, 인스타 링크 캡션 가져오기 |
| 1 | 인스타그램 캡션 다운로더로 할 수 있는 일 | 인스타그램 캡션 다운로더, 인스타 동영상 캡션 다운로드, 인스타 캡션 추출 |
| 2 | 캡션과 음성 텍스트, 무엇이 필요하신가요? | *(phân định Caption/Transcript + internal link `/ko/instagram-transcript`. **Cấm dùng `자막`** — dùng `음성 텍스트` / `말한 내용`)* |
| 3 | 인스타그램 캡션 다운로드 하는 방법 | 인스타그램 캡션 다운로드, 인스타 링크 캡션 가져오기 |
| 4 | 다운로드한 캡션으로 할 수 있는 일 | 인스타그램 게시물 설명 저장, 인스타그램 게시물 텍스트 저장, 인스타 릴스 캡션 다운로드 |
| 5 | **인스타 캡션 복사 — 해시태그, 이모지, 줄바꿈까지 그대로** | **인스타 캡션 복사 (10–100)**, 인스타 캡션 텍스트 복사 |
| 6 | 자주 묻는 질문 | 인스타그램 설명 다운로드, 인스타 캡션 온라인 다운로드, 인스타 캡션 추출 + long-tail |
| — | **conclusion** | 인스타그램 캡션 다운로드, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- **Section 5 là "van xả" của toàn bộ nhóm `복사`.** Bản EN section này vốn đã nói về "what you copy reads the same as what was on the post" — nên đưa `인스타 캡션 복사` lên H2 ở đây là **bám đúng nghĩa gốc**, không phải nhét keyword. Đây là mẫu đã duyệt ở `de.json` section 5.
- **Section 2 giữ nguyên vai trò phân định Caption/Transcript**, nhưng H2 và body **không được chứa `자막`**. Diễn đạt bằng `음성 텍스트`, `말한 내용`, `영상 속 말소리`. Internal link: `[Instagram 음성 텍스트 변환](/ko/instagram-transcript)`.
- `설명` xuất hiện tối thiểu 3 lần trong body (section 1, section 4, FAQ) để bắt 2 keyword nhóm `설명`.
- `인스타` (viết tắt) xuất hiện tối thiểu 3 lần — H2 section 5 + body section 4 + FAQ — để bắt nhóm KW viết tắt, trong đó có KW mạnh nhất.
- `인스타 릴스 캡션 다운로드` đặt vào **section 4 item cuối (giữ bộ hashtag)** hoặc item "tái sử dụng", giống cách `de.json` đặt `instagram reels caption speichern`.
- `인스타 캡션 온라인 다운로드` và `인스타그램 설명 다운로드` gom vào **FAQ 1** — đúng chỗ bản EN đã có sẵn câu hỏi "for free".
- **Không thêm câu, không thêm H2, không thêm FAQ.** Mọi keyword phải nằm gọn trong khung 6 section có sẵn.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `인스타그램 영상 텍스트 변환` / `인스타 릴스 음성 텍스트` / `인스타 자막 추출` → **/ko/instagram-transcript** (chữ **NÓI**, không phải chữ **VIẾT**)
- `유튜브 영상 텍스트 변환` / `유튜브 자막 추출` → **/ko/youtube-transcript**
- `틱톡 영상 텍스트 변환` / `틱톡 자막 추출` → **/ko/tiktok-transcript**
- 🔴 **`인스타 영상 다운로드` / `인스타 동영상 저장` / `릴스 다운로드` / `인스타 사진 저장` → intent TẢI VIDEO/ẢNH, KHÔNG phải tải chữ.** Đây là **nhóm nhiễm nguy hiểm nhất** của cụm Instagram tiếng Hàn: volume rất lớn và SERP toàn video downloader. Trang này tải **chữ**, không tải video.
  > **Quy tắc dịch bắt buộc:** mọi chỗ dùng `다운로드` hoặc `저장` **phải luôn có tân ngữ** `캡션` / `설명` / `텍스트`. Viết `캡션 다운로드`, `설명 저장`, `텍스트 저장` — **không bao giờ** viết `영상 다운로드`, `동영상 저장`, hay `다운로드` đứng trơ một mình.
- `인스타 자막` (mọi biến thể) → xem cảnh báo mục 2 phía trên. `자막` = phụ đề video, sai page type.
- `인스타 프로필 복사` / `인스타 댓글 복사` → tuy gần `인스타 캡션 복사` nhưng khác đối tượng, không tối ưu riêng.

---

## Internal linking

- ↔ **/ko/instagram-transcript** (khi user muốn chữ **NÓI** trong 릴스/동영상 thay vì caption viết) — đây là link **quan trọng nhất**, nằm ở section 2, item thứ 2
- → /ko/youtube-transcript, /ko/tiktok-transcript (cross-cluster: cùng nhu cầu lấy text, nền tảng khác)

---

## Ghi chú kỹ thuật cho ko.json

- `lang="ko"`, `dir="ltr"`.
- **Thể văn: `합니다`체** lịch sự chuẩn, xuyên suốt — **nhất quán với `/ko/facebook-transcript/ko.json`**. Không dùng `해요`체 (quá thân mật), không dùng `한다`체 (quá khô). Văn phong tự nhiên như người Hàn viết, không dịch máy word-by-word.
- **Không chèn dấu cách sai:** `인스타그램` (một từ), `인스타` (một từ), `가져오기` (một từ), `해시태그` (một từ). Lỗi này có sẵn trong `2_loc_kw.md`, đã sửa toàn bộ.
- Giữ nguyên Latin, không phiên âm: **TranscriptX, Instagram, URL**.
- Nền tảng: dùng **`인스타그램`** / **`인스타`** Hangul trong H1/H2/văn xuôi (bám keyword đã search); giữ **`Instagram`** Latin trong `seo.description`, `schemaName`, `schemaDescription` và tên link nội bộ để bắt biến thể Latin.
- Thuật ngữ chuẩn hoá: Reel/Reels → **`릴스`**; Carousel → **`캐러셀`**; hashtag → **`해시태그`**; emoji → **`이모지`**; line break → **`줄바꿈`**; caption → **`캡션`**; description → **`설명`**.
- 🚫 **`자막` bị cấm hoàn toàn trong file này.** Nói về chữ NÓI thì dùng `음성 텍스트`, `말한 내용`, `영상 속 말소리`.
- Internal link section 2 giữ nguyên cú pháp markdown, đổi path: `[Instagram 음성 텍스트 변환](/ko/instagram-transcript)`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**, section 1 = `content` 3, section 2 = `intro` 1 + `items` 2, section 3 = `steps` 4, section 4 = `intro` 1 + `items` 5, section 5 = `content` 3, section 6 = `items` **8** (q/a), `conclusion` = h2 + `content` 2 đoạn.
