🔥 TranscriptX – YouTube Transcript (Vietnamese / vi)

URL:
/vi/youtube-transcript

Intent chính:

chuyển video youtube thành văn bản / lấy transcript video YouTube online, miễn phí

Trang này nhắm đến người dùng Việt Nam muốn **lấy toàn bộ lời nói trong một video YouTube ra dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán link là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 💰 TRANG LỚN NHẤT VÀ GIÁ TRỊ CAO NHẤT CỦA TOÀN DỰ ÁN

Đây là landing page **lớn nhất** đã làm từ trước tới nay:

- **12 section** (gấp đôi mọi trang trước), trong đó có `specs` **10 dòng**, S6 **6 items**, S10 **5 items**, S8 **2 items**, S12 **12 FAQ**, `conclusion` **3 đoạn**.
- **4 internal link** ở section 11 — nhiều nhất dự án.
- Bản `es` của chính trang này là **PILOT đã duyệt**. Bản `vi` bám sát cấu trúc, độ sâu và giọng văn của bản pilot đó.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này là **hub** nên **giữ trọn họ từ `transcript`** (`transcript`, `lấy transcript`, `tạo transcript`, `gỡ băng`) **và cả nhóm `lấy / trích xuất chữ`** (`trích xuất văn bản từ video youtube`, `lấy nội dung video youtube thành văn bản`).

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ **16 keyword đúng intent** trong danh sách `## Vietnamese (vi)` đều thuộc về trang này, kể cả nhóm `chuyển video youtube thành văn bản` / `chuyển youtube sang text` / `video youtube sang văn bản` — vì các cụm đó **đều có chữ `youtube`**, nên không đụng trang generic `/vi/video-to-text`.

### ⚠️ Ngoại lệ: 2 cụm thuộc trang khác

| Cụm | Trang sở hữu | Trạng thái | Cách dùng ở trang này |
| --- | ------------ | ---------- | --------------------- |
| `tải phụ đề youtube` | `/vi/youtube-subtitle-downloader` | ✅ đã hoàn thành | **Chỉ ở S11**, trong câu trỏ sang trang đó (anchor `Công cụ tải phụ đề YouTube`) |
| `tải transcript youtube` | `/vi/download-youtube-transcript` | ✅ đã hoàn thành | **Chỉ ở S11**, trong câu trỏ sang trang đó (anchor `Tải transcript YouTube`) |

Ngoài S11, **không được** đưa hai cụm này vào `title`, `h1`, `h2`, `h3`, `q` hay body ở bất kỳ chỗ nào khác.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **Section 11 (`Sao chép, chỉnh sửa, dịch hoặc tải về`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (transcript vs file phụ đề SRT/VTT) — chốt với `/vi/youtube-subtitle-downloader`.
- **FAQ 4** (`tạo` vs `trích xuất`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — 2 DÒNG ĐÃ LOẠI

Danh sách `## Vietnamese (vi)` trong `2_loc_kw.md` có **18 dòng nhãn keyword**, trong đó **2 dòng là rác**. Cách xử lý theo đúng tiền lệ của bản `es` (mục lỗi dữ liệu riêng):

| Dòng | Volume | Lý do loại |
| ---- | ------ | ---------- |
| `Keyword ideas` | — | **Nhãn giao diện công cụ search**, không phải keyword. Bị copy nhầm khi export. |
| `Keywords you provided` | — | **Nhãn giao diện công cụ search**, không phải keyword. Cùng nguyên nhân. |

> ⚠️ Đây là **lỗi export hệ thống**, đã xuất hiện ở cả section `## Spanish (es)` và `## French (fr)` của cùng file.

### Đã kiểm thêm — bản `vi` KHÔNG dính:

- **`texttomp3`** (TTS, intent ngược) — ✅ **không có** trong section `vi`. Chỉ có ở `es` và `fr`.
- **Cụm garbled / lỗi chính tả** (kiểu `youtube subito texto` ở `es`) — ✅ **không có**. Cả 16 cụm còn lại đều là tiếng Việt chuẩn, có dấu, intent rõ ràng.

### 📊 Số keyword thực: **18 − 2 = 16**

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc phần âm thanh → trả về **toàn bộ lời nói dưới dạng văn bản** với hơn 100 ngôn ngữ, gán nhãn từng người nói, dấu thời gian tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **lấy / get** — lấy bản transcript có sẵn,
- **tạo / generate** — dựng bản transcript từ âm thanh khi video không có phụ đề,
- **trích xuất / extract** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

Kết quả trang này **luôn gọi là `bản transcript` hoặc `văn bản`** — **không bao giờ** gọi là `phụ đề`.

---

## Từ khóa chính

**chuyển video youtube thành văn bản (100–1K)** ✅ *đã search* → **H1**

Đây là cụm có volume cao nhất trong danh sách `vi`. Toàn bộ trang được xây quanh nó: xuất hiện ở `seo.title`, `hero.h1`, `ogTitle`, H2 của S2 và `conclusion.content[2]`.

---

## Từ khóa phụ

### Nhóm `chuyển … thành / sang văn bản` (trục chính — volume cao nhất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| chuyển video youtube thành văn bản | 100–1K | ✅ đã search *(KW chính)* |
| chuyển video youtube sang văn bản | 100–1K | ✅ đã search |
| chuyển video trên youtube thành văn bản | 10–100 | ✅ đã search |
| cách chuyển video youtube sang văn bản | 10–100 | ✅ đã search |
| chuyển âm thanh trên youtube thành văn bản | 10–100 | ✅ đã search |
| chuyển giọng nói youtube thành văn bản | 0–10 | ✅ đã search |
| chuyển youtube sang text | 10–100 | ✅ đã search |
| video youtube sang văn bản | 0–10 | ✅ đã search |

### Nhóm `transcript` (danh từ — trục thương hiệu của hub)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| lấy transcript youtube | 10–100 | ✅ đã search |
| tạo transcript từ video youtube | 10–100 | ✅ đã search |
| công cụ tạo transcript youtube | 0–10 | ✅ đã search |
| cách lấy transcript video youtube | 0–10 | ✅ đã search |

### Nhóm `lấy / trích xuất chữ`

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| trích xuất văn bản từ video youtube | 10–100 | ✅ đã search |
| lấy nội dung video youtube thành văn bản | 0–10 | ✅ đã search |
| lấy phụ đề youtube thành văn bản | 0–10 | ✅ đã search *(xem quy tắc `phụ đề` bên dưới)* |

### Nhóm nghề nghiệp

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| gỡ băng video youtube | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| gán nhãn từng người nói | — | 🔄 dịch bổ sung (speaker separation) |
| dấu thời gian | — | 🔄 dịch bổ sung (timestamps) |
| hơn 100 ngôn ngữ | — | 🔄 dịch bổ sung (100+ languages) |
| miễn phí / không cần đăng ký | — | 🔄 dịch bổ sung (free / no sign-up) |
| bản chữ thô | — | 🔄 dịch bổ sung (raw script) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## ⚠️ QUY TẮC DÙNG TỪ `phụ đề` — MỤC RIÊNG, BẮT BUỘC

Bản EN dùng `captions` ở khoảng **6 chỗ**. Tiếng Việt chỉ có **một từ** `phụ đề` gánh cả `captions` lẫn `subtitles`, nên phải đặt kỷ luật cứng:

### ✅ ĐƯỢC dùng `phụ đề` khi:

1. **Nói về phụ đề có sẵn của YouTube** — luôn có định ngữ, không để trần:
   - `phụ đề tự động` (auto-captions)
   - `phụ đề do người đăng thêm` (captions the creator added)
   - `nút phụ đề` (caption button)
2. **Trỏ sang `/vi/youtube-subtitle-downloader` ở S11** — anchor `Công cụ tải phụ đề YouTube`, và cụm `đúng file phụ đề`.
3. **FAQ 10** — câu trả lời giải thích phụ đề là chữ khớp giờ hiện lên khi phát video, lưu dạng SRT/VTT.
4. **Keyword `lấy phụ đề youtube thành văn bản`** — dùng **đúng một lần** ở S5, trong câu mô tả việc rút chữ ra từ phụ đề có sẵn. Đây là intent transcript (kết quả là **văn bản**), không phải intent tải file phụ đề.

### 🚫 KHÔNG được dùng `phụ đề` khi:

- **Gọi tên kết quả của trang này.** Kết quả **luôn** là `bản transcript` / `văn bản`. Không bao giờ viết "trang này cho bạn phụ đề".
- **Trên bất kỳ heading nào** — `h1`, `h2`, `h3`, `q` đều phải sạch từ `phụ đề`.
  - Vì thế **FAQ 3** (EN: *"Can I generate a transcript if the video has no captions?"*) được dịch thành **"Video chưa có sẵn bản chữ nào thì có tạo được transcript không?"** — giữ nguyên ý, đẩy từ `phụ đề` xuống phần `a`.
  - **FAQ 10** (EN: *"…transcript and subtitles?"*) được dịch thành **"Transcript YouTube khác gì với file SRT và VTT?"** — vừa sạch heading, vừa lấy thêm tín hiệu `SRT` / `VTT`.
- Nhãn `specs` **không phải heading**, nên dòng `Video chưa có phụ đề` được giữ (đối ứng `Works when the video has no captions` của EN).

### Kiểm tra bắt buộc

```
grep 'phụ đề' trên toàn bộ h1/h2/h3/q → phải rỗng
```

---

## Search Intent

Người dùng Việt Nam muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán link YouTube, không phải tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác — nhu cầu VI ⇄ EN rất nặng (video học thuật, khóa học nước ngoài).
- Hoạt động **cả khi video không có phụ đề** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, tọa đàm, podcast).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Việt không có một danh từ bản địa cho `transcript`, nên trục chính đổi sang cụm động từ `chuyển … thành văn bản`.** Bản EN xoay quanh danh từ `transcript` (`get / generate / extract a transcript`), và `youtube transcript` là cụm volume cao nhất. Ở tiếng Việt, cụm volume cao nhất lại là **`chuyển video youtube thành văn bản` (100–1K)**, còn `lấy transcript youtube` chỉ đạt 10–100. Vì vậy **H1 bản vi phải là cụm động từ** (`Chuyển video YouTube thành văn bản`), không phải bản dịch trực tiếp của "YouTube Transcript". Đây là thay đổi cấu trúc thật, không phải dịch sát nghĩa đen.

2. **Từ `transcript` được giữ nguyên dạng Latin, không dịch.** Người Việt gõ thẳng `transcript` khi search (`lấy transcript youtube`, `tạo transcript từ video youtube`, `công cụ tạo transcript youtube`) — không tồn tại một bản dịch nào có volume tương đương. Nhất quán với `/vi/video-to-text` và các trang vi đã duyệt: dùng **`bản transcript`** (danh từ ghép Việt + Latin). Bản EN không có vấn đề này.

3. **Tiếng Việt chỉ có MỘT từ `phụ đề` cho cả `captions` và `subtitles`.** Bản EN phân biệt được `captions` (chữ có sẵn của video) với `subtitles` (file khớp giờ) bằng hai từ riêng, nên viết thoải mái. Bản vi phải thêm định ngữ (`phụ đề tự động`, `phụ đề do người đăng thêm`) và cấm `phụ đề` trên heading — nếu không sẽ bị SERP hiểu nhầm là trang tải phụ đề và cannibalize `/vi/youtube-subtitle-downloader`. Xem mục quy tắc riêng ở trên.

4. **Rủi ro cannibalization ngược từ nhóm tải VIDEO là lớn nhất trong toàn bộ 13 ngôn ngữ.** `tải video youtube` ở Việt Nam có volume cực lớn và SERP toàn công cụ tải MP4. Kỷ luật cứng: từ `tải` **chỉ** được đi với `bản transcript` / `văn bản` / `file` / `phụ đề` (ở S11), **không bao giờ** với `video`. Kể cả S3 bước 2 (EN: *"no file to download first"*) → dịch thành `không có file nào phải tải về trước`, giữ chữ `file`, không dùng `video`. Bản EN không chịu áp lực này ở cùng mức.

5. **`gỡ băng` là thuật ngữ nghề nghiệp không có tương đương EN.** Đây là cách gọi của giới báo chí, thư ký, nghiên cứu Việt Nam cho việc chuyển audio thành chữ. Bản EN chỉ có một từ `transcribe`. Bản vi dùng **cả hai**: `gỡ băng` ở H2 của S7 và trong các câu mang giọng nghiệp vụ, `chuyển … thành văn bản` ở các câu hướng tới người dùng phổ thông.

6. **Nhóm `chuyển … thành văn bản` bắt buộc phải có chữ `youtube` mới được dùng.** Trang generic `/vi/video-to-text` đã hoàn thành và đang giữ `chuyển video thành văn bản`. Bản vi của trang này chỉ được dùng các biến thể **có `youtube`** trong cụm. Bản EN không có ràng buộc này vì trang EN tương ứng chia khác.

7. **Danh sách ngôn ngữ ví dụ ở S7 được bản địa hóa.** Bản EN liệt kê `English, Spanish, Hindi, Arabic, Japanese`. Bản vi đổi thành `tiếng Việt, tiếng Anh, tiếng Trung, tiếng Nhật, tiếng Hàn` — đúng nhóm ngôn ngữ mà người dùng Việt Nam thực sự cần gỡ băng.

---

## Đối tượng người dùng

- Học sinh, sinh viên, người học online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác, quen từ `gỡ băng`)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / bản tin)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần bản chữ thô để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ VI ⇄ EN
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `vi.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (vi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Chuyển video YouTube thành văn bản | chuyển video youtube thành văn bản *(KW chính)* |
| — | **quickAnswer** | cách lấy transcript video youtube, lấy transcript youtube |
| 1 | Transcript YouTube là gì? | lấy transcript youtube |
| 2 | Chuyển video YouTube thành văn bản – tổng quan nhanh *(`specs` × 10)* | chuyển video youtube thành văn bản |
| 3 | Cách chuyển video YouTube sang văn bản *(`steps` × 4)* | cách chuyển video youtube sang văn bản, chuyển video youtube sang văn bản |
| 4 | Công cụ tạo transcript YouTube | công cụ tạo transcript youtube, tạo transcript từ video youtube |
| 5 | Trích xuất văn bản từ video YouTube | trích xuất văn bản từ video youtube, chuyển youtube sang text, lấy phụ đề youtube thành văn bản |
| 6 | Dùng bản transcript YouTube để làm gì *(`items` × 6)* | lấy nội dung video youtube thành văn bản, chuyển video trên youtube thành văn bản |
| 7 | Gỡ băng video YouTube ở mọi ngôn ngữ | gỡ băng video youtube, chuyển âm thanh trên youtube thành văn bản, chuyển giọng nói youtube thành văn bản |
| 8 | TranscriptX so với transcript có sẵn của YouTube *(`items` × 2)* | *(so sánh — không nhắm KW mới)* |
| 9 | Độ chính xác và những yếu tố ảnh hưởng | *(E-E-A-T, không nhắm KW)* |
| 10 | Khi nào không lấy được transcript YouTube *(`items` × 5)* | lấy transcript youtube |
| 11 | Sao chép, chỉnh sửa, dịch hoặc tải về *(`content` × 2)* | *(4 internal link — chốt phân định)* |
| 12 | Câu hỏi thường gặp *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion** *(3 đoạn)* | lấy transcript youtube, chuyển video youtube thành văn bản, miễn phí |

### Ghi chú riêng cho bản vi (KHÔNG tạo section mới)

- **S2 tái dùng ĐÚNG các nhãn `specs` đã duyệt ở `/vi/video-to-text/vi.json`** khi nhãn trùng: `Chi phí`, `Yêu cầu tài khoản`, `Cài đặt`, `Ngôn ngữ`, `Phân biệt người nói`, `Dấu thời gian`, `Định dạng xuất`, `Thiết bị` — **8 nhãn dùng lại nguyên văn**. Hai nhãn mới riêng của trang này: **`Đầu vào`** (Input — link video YouTube) và **`Video chưa có phụ đề`** (Works when the video has no captions). Hai nhãn của trang generic không dùng ở đây (`Giới hạn dung lượng`, `Định dạng hỗ trợ`) vì đầu vào là link chứ không phải file.
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại**, vì mỗi section giữ một họ keyword riêng của tiếng Việt.
- **S8 là section so sánh** với transcript tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba. Gọi là `transcript có sẵn của YouTube`, **không** gọi là `phụ đề của YouTube`.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào. Đây là chỗ duy nhất hai cụm `tải transcript youtube` và `tải phụ đề youtube` được phép xuất hiện.
- **Kỷ luật chữ `tải`:** chỉ đi với `bản transcript` / `văn bản` / `file` / `phụ đề` (S11). **Không bao giờ** viết `tải video`. Kiểm tra: `grep 'tải video' vi.json` → phải rỗng.
- Xưng hô **`bạn`** — nhất quán với `/vi/video-to-text/vi.json` và các trang vi đã duyệt.
- Thuật ngữ khớp `/vi/video-to-text`: **`bản transcript`**, **`gán nhãn từng người nói`**, **`dấu thời gian`**, `trình duyệt`, `miễn phí`, `không cần đăng ký`, `tự động nhận diện`.
- Nhấn `miễn phí` ở `seo.title`, `hero.subtitle`, S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.
- `hero.placeholder` (`Dán link video YouTube...`) và `hero.button` (`Lấy transcript`) phải ngắn — dịch gọn, không thêm chữ.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`tải transcript youtube` / `download transcript youtube` / `tải bản transcript youtube`** → **`/vi/download-youtube-transcript`** *(đã hoàn thành)*. Trọng tâm là **tải file** TXT/DOCX/PDF/SRT. Trang này chỉ nhắc ở S11.
- **`tải phụ đề youtube` / `tải sub youtube` / `phụ đề srt youtube` / `trích xuất phụ đề youtube`** → **`/vi/youtube-subtitle-downloader`** *(đã hoàn thành)*. File phụ đề khớp giờ, dành cho người dựng phim. Nhóm `phụ đề` để trần thuộc trọn về trang đó.
- **`youtube video sang văn bản`**: giữ ở hub này — không còn trang riêng cho cách gọi "video sang văn bản". Các cụm `chuyển … video youtube … thành/sang văn bản` cũng giữ ở đây vì đúng intent transcript.
- **`tóm tắt video youtube` / `tóm tắt nội dung video youtube` / `công cụ tóm tắt youtube`** → **`/vi/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`chuyển video thành văn bản` / `video sang văn bản` / `chuyển video sang text`** (không có chữ `youtube`) → **`/vi/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `thành văn bản` dùng ở trang này **bắt buộc phải có `youtube`** trong cụm.
- **`chuyển audio thành văn bản` / `chuyển giọng nói thành văn bản`** (không có `youtube`) → **`/vi/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`tải video youtube` / `tải video youtube mp4` / `youtube sang mp4` / `tải nhạc youtube`** → **intent tải file video**, SERP ở Việt Nam toàn công cụ tải MP4/MP3, volume cực lớn. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng đã nêu ở trên: `grep 'tải video'` phải rỗng.

### Sai intent hoàn toàn

- **Mọi cụm TTS** (`chuyển văn bản thành giọng nói`, `đọc văn bản thành tiếng`, `text to speech tiếng Việt`, `texttomp3`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. *(Lưu ý: `texttomp3` xuất hiện ở section `es` và `fr` của `2_loc_kw.md` nhưng **không có** ở section `vi`.)*
- **`bật phụ đề youtube` / `cách bật phụ đề trên youtube`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link** — nhiều nhất dự án. Thứ tự và vai trò:

| Link | Anchor (vi) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/vi/download-youtube-transcript` | Tải transcript YouTube | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/vi/youtube-subtitle-downloader` | Công cụ tải phụ đề YouTube | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/vi/youtube-video-summarizer` | Công cụ tóm tắt video YouTube | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho vi.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`. Từ **`transcript`** cũng giữ nguyên dạng Latin, viết thường, thường đi kèm `bản` (`bản transcript`).
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/vi/...)`, đổi path sang `/vi/`.
- **Kiểm tra bắt buộc trước khi bàn giao:**
  1. `python3 shape_check.py en.json vi.json` → phải in `vi.json -> True`.
  2. `grep -c 'tải video' vi.json` → **0**.
  3. `grep 'phụ đề'` trên toàn bộ `h1` / `h2` / `h3` / `q` → **rỗng**.
  4. 4 path internal link đúng `/vi/` prefix, đủ 4, không thừa không thiếu.
  5. `grep -c 'texttomp3' vi.json` → **0**.
