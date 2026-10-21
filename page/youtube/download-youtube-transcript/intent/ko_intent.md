🔥 TranscriptX – Download YouTube Transcript (Korean / ko)

URL:
/ko/download-youtube-transcript

Intent chính:

Tải bản chép lời (스크립트 / 대본) của video YouTube về máy — TXT, DOCX, PDF, SRT — miễn phí

Trang này nhắm đến người dùng Hàn muốn **tải bản transcript của video YouTube xuống thiết bị** dưới dạng file — để đọc offline, lưu trữ, nộp bài, in ra, hoặc đưa vào công cụ khác. Khác hẳn với việc chỉ đọc transcript trên màn hình.

---

## 🚨 CỤM YOUTUBE CÓ 5 TRANG — ĐỌC PHẦN NÀY TRƯỚC

Repo có 5 trang YouTube dễ ăn thịt nhau. Đã kiểm tra chéo keyword toàn cụm:

| Cặp trang | Số keyword trùng |
| --------- | ---------------- |
| **`download-youtube-transcript` × `youtube-subtitle-downloader`** | **9** ⚠️ |
| `youtube-subtitle-downloader` × `youtube-transcript` | 1 |

Trang này nằm ở vùng xung đột thứ hai. **Quy tắc phân chia đã chốt — phân theo NGỮ NGHĨA TỪ:**

> **Từ mang nghĩa "phụ đề" (`자막`) → `/ko/youtube-subtitle-downloader`**
> **Từ mang nghĩa "bản chép lời" (`스크립트` / `대본` / `transcript`) → TRANG NÀY**

Căn cứ: bản EN section 6 tự định nghĩa ranh giới — *"if what you really need is a timed caption file for a video editor rather than a document, the YouTube Subtitle Downloader exports SRT and VTT instead"*. Trang này ra **tài liệu để đọc / lưu / nộp**; trang kia ra **file phụ đề khớp giờ cho phần mềm dựng phim**.

### Hệ quả cho bản ko: mất keyword mạnh nhất danh sách

`유튜브 자막 다운로드` (**1K – 10K**) là cụm mạnh nhất trong danh sách ko của trang này, **nhưng nó thuộc `/ko/youtube-subtitle-downloader`**. Xử lý bằng kỹ thuật **neo đẩy đi**: dùng **đúng 1 lần**, ở **section 6 đoạn 2**, ngay trong câu trỏ sang trang kia. Bắt được tín hiệu keyword nhưng đẩy traffic sai intent về đúng trang thay vì giữ lại rồi bounce. **Tuyệt đối không đặt vào title / H1 / H2.**

Đây là khác biệt lớn nhất so với bản vi: bản vi nhường 1 cụm, bản ko phải nhường **6 cụm** vì tiếng Hàn dùng `자막` cực rộng — người Hàn nói `자막` cho cả phụ đề khớp giờ lẫn bản chép lời thuần chữ.

### Bảng keyword NHƯỜNG cho `/ko/youtube-subtitle-downloader`

| Keyword | Volume | Lý do nhường |
| ------- | ------ | ------------ |
| `유튜브 자막 다운로드` | **1K – 10K** | ⚠️ Cụm `자막` lõi. **Neo đẩy đi 1 lần ở S6 đoạn 2.** |
| `유튜브 자막 저장` | 10 – 100 | `자막` + lưu → file phụ đề |
| `유튜브 자막 다운로드 무료` | 0 – 10 | biến thể của cụm lõi `자막` |
| `유튜브 영상 자막 텍스트 다운로드` | 0 – 10 | `자막` dẫn đầu ngữ nghĩa |
| `유튜브 자막 txt 다운로드` | 0 – 10 | `자막` dẫn đầu ngữ nghĩa |
| `유튜브 자막 추출 다운로드` | 0 – 10 | `자막 추출` là intent trích phụ đề có sẵn |

**Chỉ `유튜브 자막 다운로드` được xuất hiện, đúng 1 lần, ở S6 đoạn 2. 5 cụm còn lại KHÔNG xuất hiện ở bất cứ đâu trong `ko.json`.**

### Đếm keyword

**12 dòng thô − 6 cụm nhường = 6 cụm dùng làm trục chính.** Trong đó `youtube transcript 다운로드` và `유튜브 transcript 다운로드` là hai biến thể của cùng một cụm mượn tiếng Anh.

---

## Từ khóa chính

`유튜브 스크립트 다운로드` (**100 – 1K**) ✅ *đã search*

Đây là cụm mạnh nhất còn lại sau khi nhường toàn bộ nhóm `자막`. Nó cũng là **lõi chung** của `유튜브 스크립트 다운로드 방법`, nên neo vào đây thì đuôi dài tự phủ theo.

Cụm đồng hạng: `유튜브 대본 다운로드` (**100 – 1K**) — cùng volume, cùng intent. Xử lý như **KW chính thứ hai**: đặt ở H2 section 1 để cả hai cụm đều có heading riêng, tránh phải chọn một bỏ một.

---

## Từ khóa phụ

### Nhóm 스크립트 (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 스크립트 다운로드 | 100 – 1K | ✅ đã search *(KW chính)* |
| 유튜브 스크립트 다운로드 방법 | 0 – 10 | ✅ đã search |

### Nhóm 대본 (trục chính thứ hai)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 대본 다운로드 | 100 – 1K | ✅ đã search *(KW chính 2)* |

### Nhóm 텍스트 / transcript

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 영상 텍스트 다운로드 | 0 – 10 | ✅ đã search — `다운로드` gắn với `텍스트`, KHÔNG gắn với `영상` |
| youtube transcript 다운로드 | 0 – 10 | ✅ đã search |
| 유튜브 transcript 다운로드 | — | ✅ đã search (biến thể) |

### Nhóm 자막 — NHƯỜNG TRANG KHÁC

Xem bảng ở khối cảnh báo phía trên. Chỉ `유튜브 자막 다운로드` xuất hiện, đúng 1 lần, ở S6 đoạn 2.

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 유튜브 스크립트 파일로 저장 | — | 🔄 dịch bổ sung (save as file) |
| 유튜브 대본 PDF로 저장 | — | 🔄 dịch bổ sung (export PDF) |
| 유튜브 스크립트 DOCX 다운로드 | — | 🔄 dịch bổ sung (DOCX) |
| 오프라인 유튜브 대본 | — | 🔄 dịch bổ sung (offline) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

> ⚠️ Sau khi nhường nhóm `자막`, trần volume của trang tụt từ `1K – 10K` xuống `100 – 1K`. Không cố nhồi mật độ để bù — chiến lược là **phủ đều 6 cụm**, mỗi cụm một vị trí neo, và giữ ranh giới sạch với trang `자막`.

---

## Search Intent

Người dùng Hàn **đã biết mình muốn transcript** và đang ở bước tiếp theo: lấy nó thành **file trên máy**. Khác với người chỉ muốn đọc trên màn hình.

Họ kỳ vọng:

- Dán link là tải được ngay, không đăng nhập, không cài extension (người Hàn rất ngại cài chương trình lạ).
- **Chọn được định dạng** — TXT để dán đi chỗ khác, DOCX để sửa, PDF để nộp/in, SRT khi cần mốc thời gian.
- File mở được **offline**.
- Miễn phí, không giới hạn độ dài video.
- Nhận dạng tốt tiếng Hàn.

### Khác biệt so với bản tiếng Anh

1. **Phải nhường nguyên một nhóm 6 keyword cho trang khác.** Bản EN không có vấn đề này vì "transcript" và "subtitle" là hai từ tách bạch. Tiếng Hàn thì `자막` bị dùng lẫn cho cả hai, và tệ hơn bản vi ở chỗ `자막` chiếm luôn cụm volume cao nhất (1K–10K). Đây là ràng buộc riêng của bản ko — xem khối cảnh báo đầu file.
2. **Có HAI từ cho "transcript": `스크립트` và `대본`.** Bản EN chỉ có một. Cả hai đều 100–1K nên không được bỏ cụm nào — `스크립트` vào H1/title, `대본` vào H2 section 1. Sắc thái: `스크립트` nghiêng về bản ghi kỹ thuật/nội dung, `대본` nghiêng về kịch bản/lời thoại. Dùng `스크립트` khi nói về file và thao tác, `대본` khi nói về nội dung lời nói.
3. **Phải dập nhiễm intent tải VIDEO.** Cụm `유튜브 영상 다운로드` có volume rất lớn ở Hàn và SERP toàn downloader. Bản EN không gặp. Quy tắc cứng: `다운로드` chỉ được đứng cạnh `스크립트` / `대본` / `텍스트` / `파일`, **KHÔNG BAO GIỜ** cạnh `영상` / `동영상`.
4. **`transcript` giữ nguyên chữ Latin ở 2 cụm mượn.** Người dùng Hàn kỹ thuật hay gõ thẳng `transcript` — giữ đúng dạng `youtube transcript 다운로드` để bám keyword, không phiên âm sang `트랜스크립트`.
5. **Nhấn DOCX và PDF mạnh hơn bản EN.** Sinh viên và nhân viên văn phòng Hàn thường cần bản nộp được (보고서 / 과제).

---

## Đối tượng người dùng

- Sinh viên, học viên cao học (lưu 대본 bài giảng, phỏng vấn vào thư mục đề tài)
- Nhà báo (lưu lời phát biểu làm bằng chứng trước khi video bị gỡ)
- Nhân viên văn phòng (tải DOCX để làm 회의록 / 보고서)
- Người học ngoại ngữ (tải TXT đọc offline)
- Người làm phụ đề cần bản nháp có timecode (SRT)
- Người cần đưa transcript vào công cụ khác yêu cầu upload file

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng **7 section**, cùng số đoạn `content`, đúng 4 `items` ở S2, đúng 4 `steps` ở S3, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 유튜브 스크립트 다운로드 | 유튜브 스크립트 다운로드 *(KW chính)* |
| — | **quickAnswer** | 유튜브 스크립트 다운로드 방법 |
| 1 | 유튜브 대본 다운로드가 필요한 이유 | 유튜브 대본 다운로드 *(KW chính 2)*, 유튜브 스크립트 다운로드 |
| 2 | 어떤 형식으로 다운로드해야 할까요? | 유튜브 영상 텍스트 다운로드 *(mục TXT)*, DOCX / PDF / SRT |
| 3 | 유튜브 스크립트 다운로드 방법 | 유튜브 스크립트 다운로드 방법 |
| 4 | 화면의 글자가 아니라 파일이 필요할 때 | 유튜브 대본 다운로드, youtube transcript 다운로드 |
| 5 | 100개 이상 언어로 스크립트 다운로드 | 유튜브 transcript 다운로드 *(+ nhấn tiếng Hàn)* |
| 6 | 다른 도구가 더 알맞은 경우 | ⚠️ **유튜브 자막 다운로드 — đúng 1 lần, trong câu trỏ sang `/ko/youtube-subtitle-downloader`** + 2 link còn lại |
| 7 | 자주 묻는 질문 | 유튜브 스크립트 다운로드, 유튜브 대본 다운로드 + long-tail |
| — | **conclusion** | 유튜브 스크립트 다운로드, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây cũng là chỗ **duy nhất** cụm `유튜브 자막 다운로드` được xuất hiện, và nó phải nằm **trong chính câu trỏ sang `/ko/youtube-subtitle-downloader`**, không đứng riêng.
- Nỗi lo nhận dạng tiếng Hàn xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng Hàn — không thêm câu.
- `대본` và `스크립트` chia vai rõ: `스크립트` đi với thao tác/file (H1, S3, conclusion), `대본` đi với nội dung lời nói (S1, S4). Không trộn lẫn trong cùng một câu.
- Không dùng `트랜스크립트` phiên âm ở bất cứ đâu — giữ `transcript` dạng Latin khi cần bám 2 cụm mượn.

---

## Không nên tối ưu cho các keyword

- **`유튜브 자막 다운로드` / `유튜브 자막 저장` / `유튜브 자막 추출` / `유튜브 자막 txt 다운로드` / `유튜브 자막 다운로드 무료` / `유튜브 영상 자막 텍스트 다운로드`** → **/ko/youtube-subtitle-downloader** (file phụ đề khớp giờ cho editor). Xem quy tắc "đúng 1 lần" ở trên.
- `유튜브 스크립트 추출` / `유튜브 스크립트 보기` / `유튜브 대본 보기` → **/ko/youtube-transcript** (đọc và copy trên màn hình, không tải file).
- `유튜브 영상 요약` / `유튜브 요약` → **/ko/youtube-video-summarizer**.
- **`유튜브 영상 다운로드` / `유튜브 동영상 다운로드` / `유튜브 mp4 다운로드` / `유튜브 다운로더`** → **intent tải VIDEO**, SERP toàn downloader. Trang này tải **chữ**. Quy tắc cứng: `다운로드` không bao giờ đứng cạnh `영상` / `동영상`.
- `영상 텍스트 변환` (không có chữ 유튜브) → **/ko/video-to-text** (upload file từ máy, không dán link).

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/ko/youtube-transcript` (chỉ muốn đọc/copy trên màn hình, không cần file)
- → `/ko/youtube-subtitle-downloader` (cần file phụ đề khớp giờ cho phần mềm dựng phim) — **đây là link quan trọng nhất, cũng là chỗ neo cụm `유튜브 자막 다운로드`**
- → `/ko/youtube-video-summarizer` (chỉ cần ý chính, không cần toàn văn)

---

## Ghi chú kỹ thuật cho ko.json

- Thể văn: **합니다체** nhất quán toàn trang, giống `/ko/tiktok-transcript`. Không trộn 해요체.
- Giữ nguyên Latin: **TranscriptX, YouTube, TXT, DOCX, PDF, SRT, VTT, Word, Google Docs, Pages**. Riêng chữ **YouTube** trong body dùng dạng Hàn `유튜브` để bám keyword; dạng Latin `YouTube` chỉ giữ trong tên công cụ ở internal link và trong `seo.title`.
- Cấu trúc: **7 section**, **8 FAQ**, S1 `content` 3, S2 `intro` 1 + `items` 4, S3 `steps` 4, S4 `intro` 1 + `items` 5, S5 `content` 2, S6 `content` 2, S7 `items` 8, conclusion `content` 2. **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/ko/...`.
- Kiểm chính tả và **dấu cách**: viết `유튜브 스크립트 다운로드` (3 từ, 2 dấu cách), không viết dính cũng không thừa dấu cách. Danh sách nguồn có dòng bị chèn dấu cách sai — luôn ghi theo dạng chuẩn ở bảng trên.
- **Tuyệt đối không để chuỗi `영상 다운로드` hay `동영상 다운로드` xuất hiện.**
