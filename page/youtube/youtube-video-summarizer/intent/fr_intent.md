🔥 TranscriptX – YouTube Video Summarizer (French / fr)

URL:
/fr/youtube-video-summarizer

Intent chính:

Résumer une vidéo YouTube avec l'IA (gratuit)

Trang này nhắm đến người dùng Pháp muốn **nắm ý chính của một video YouTube mà không phải xem hết** — dán link, IA đọc toàn bộ nội dung rồi trả về một `résumé` ngắn gồm kết luận, các ý chính và chi tiết cụ thể đáng nhớ.

Khác với **/fr/youtube-transcript**, trang này không hiển thị toàn văn mà **rút gọn nội dung** và **tiết kiệm thời gian**. Kết quả của trang luôn được gọi là `résumé`, không bao giờ là `transcription` (trừ 3 chốt phân định) và tuyệt đối không phải `sous-titres`.

---

## ✅ TRANG NÀY SẠCH XUNG ĐỘT VỚI 4 TRANG YOUTUBE KIA

Đã kiểm chéo toàn cụm 5 trang YouTube ở bản `fr`: **0 keyword trùng** với `youtube-transcript`, `download-youtube-transcript`, `youtube-subtitle-downloader`.

Lý do: trục từ vựng của trang này là **`résumé` / `résumer`**, còn 4 trang kia chạy trên trục **`transcription` / `sous-titres` / `texte`**. Hai trục không giao nhau ở bất kỳ cụm nào — đây là intent tách bạch hoàn toàn, **không phải nhường cụm nào cho trang anh em**, khác hẳn cặp `download-transcript` ↔ `subtitle-downloader`.

### 3 chốt phân định phải dịch sát (bản EN đã cài sẵn)

| Chốt | Vị trí | Vai trò |
| ---- | ------ | ------- |
| 1 | **S1 đoạn 3** — *"A transcript hands you every word; a summary decides which words were worth your time"* | Phân định `résumé` vs `transcription` ngay trong section đầu |
| 2 | **FAQ 4** — *"What is the difference between a summary and a transcript?"* | Trả lời thẳng câu hỏi phân định, đẩy user cần toàn văn sang trang transcript |
| 3 | **S7 đoạn 2** — chứa cả **3 internal link** | Điều hướng 3 nhu cầu sâu hơn sang 3 trang anh em |

Ngoài 3 chốt này, từ `transcription` **không được xuất hiện ở bất kỳ chỗ nào khác** trong `fr.json`.

---

## 🚨 LỖI DỮ LIỆU — 1 KEYWORD LẠC INTENT

Danh sách `fr` trong `2_loc_kw.md` bị lẫn **1 keyword hoàn toàn lạc intent**, nằm ngay dưới nhãn `Keyword ideas`:

| Keyword rác | Volume | Vì sao loại |
| ----------- | ------ | ----------- |
| video cv youtube | 10–100 | Đây là **CV vidéo** (video hồ sơ xin việc đăng lên YouTube), không liên quan gì tới công cụ tóm tắt |

**Nguyên nhân suy đoán:** đồng âm `resume`. Trong tiếng Anh `resume` = CV, trong tiếng Pháp `résumé` = bản tóm tắt. Công cụ search kéo seed `resume video youtube` (không dấu) và trả về cả cụm thuộc ngữ nghĩa "CV vidéo". Đây cũng là lý do phải **luôn viết có dấu `résumé` / `résumer`** trong nội dung — bỏ dấu sẽ trôi sang SERP tuyển dụng.

Cộng 2 dòng rác `Keyword ideas` / `Keywords you provided` (nhãn công cụ, không phải keyword).

**Số keyword thực: 12 entry − 1 lạc intent = 11 keyword.**

> So với bản `vi` (8 cụm rác Minecraft), bản `fr` sạch hơn nhiều — chỉ 1 cụm nhiễm. Nhưng phổ volume yếu: 1 cụm `1K – 10K`, 1 cụm `100 – 1K`, còn lại phần lớn `0 – 10`. Nên search bổ sung quanh `résumer une vidéo`, `résumé automatique`, `IA résumé vidéo`.

---

## Từ khóa chính

résumé vidéo YouTube — `resume video youtube` (1K–10K) ✅ *đã search*

Cụm mạnh nhất trong toàn bộ danh sách `fr` và là **lõi danh từ** mà 3 cụm đuôi dài khác bám vào (`résumé automatique ...`, `outil résumé ...`, và bản động từ `résumer ...`). Neo vào đây thì cả nhánh `résumer` tự phủ theo nhờ cùng gốc từ.

---

## Từ khóa phụ

### Nhóm `résumé` (danh từ — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| resume video youtube | 1K–10K | ✅ đã search *(KW chính)* |
| resume automatique video youtube | 0–10 | ✅ đã search |
| outil resume video youtube | 0–10 | ✅ đã search |

### Nhóm `résumer` (động từ)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| resumer une video youtube | 100–1K | ✅ đã search |
| resumer video youtube | 10–100 | ✅ đã search |
| resumer youtube | 10–100 | ✅ đã search |
| comment resumer une video youtube | 0–10 | ✅ đã search |
| resumer une video youtube gratuit | 0–10 | ✅ đã search |
| resumer une video youtube en ligne | 0–10 | ✅ đã search |

### Nhóm IA

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| resumer une video youtube avec ia | 0–10 | ✅ đã search |
| resumer video youtube ia | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| résumer une vidéo longue | — | 🔄 dịch bổ sung (long video) |
| résumer un podcast YouTube | — | 🔄 dịch bổ sung (podcast) |
| points clés d'une vidéo | — | 🔄 dịch bổ sung (key points) |
| résumer un cours en vidéo | — | 🔄 dịch bổ sung (lecture) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body.

⚠️ Keyword trong danh sách gốc viết **không dấu** (`resume`, `resumer`) vì đó là cách người dùng gõ. Trong nội dung **luôn viết có dấu** (`résumé`, `résumer`) — Google khớp cả hai, còn bỏ dấu thì lệch sang ngữ nghĩa CV.

---

## Search Intent

Người dùng Pháp gặp một video YouTube dài — cours, podcast, conférence, test sản phẩm 20 phút — và muốn **biết nó nói gì trong một phút** để quyết định có đáng xem hết không.

Họ kỳ vọng:

- Dán link là ra `résumé` trong vài giây, không tạo tài khoản.
- IA đọc **toàn bộ video**, không phải chỉ phần mô tả hay vài phút đầu.
- Bản tóm tắt đủ ngắn để đọc nhanh nhưng có **con số, tên riêng, khuyến nghị cụ thể**.
- Hỗ trợ tốt tiếng Pháp và các thứ tiếng khác.
- Miễn phí, không giới hạn độ dài video.

### Khác biệt so với bản tiếng Anh

1. **Phải loại cụm `video cv youtube` và luôn giữ dấu.** Bản EN không có vấn đề đồng âm này. Tiếng Pháp `résumé` (tóm tắt) và tiếng Anh `resume` (CV) trùng mặt chữ khi bỏ dấu — đây là rủi ro riêng của bản `fr`, xem khối lỗi dữ liệu ở trên.
2. **Có sẵn cặp danh từ / động từ, không lo lặp từ.** Bản EN xen kẽ `summary` / `summarize`; tiếng Pháp có đúng cặp tương ứng `résumé` / `résumer`, cộng thêm `synthèse`, `l'essentiel`, `les points clés`, `l'idée principale` để đổi giọng. Thuận lợi hơn bản `vi` (chỉ có một từ `tóm tắt`).
3. **Nhánh động từ mạnh hơn nhánh danh từ ở đuôi dài.** 6/11 cụm là `résumer ...`, chỉ 3 cụm là `résumé ...`. Vì thế H1 dùng danh từ (bám KW chính `1K – 10K`), còn **H2 của S3 và S2 phải dùng động từ** để phủ nhánh còn lại.
4. **`avec l'IA` là tín hiệu rõ nhưng volume thấp.** Khác bản `vi` (`bằng ai` đạt `100 – 1K`), bản `fr` chỉ `0 – 10`. Vẫn đưa `IA` vào `title` và H2 của S3, nhưng **không hy sinh cụm chính** để nhét IA.
5. **Rào chắn từ vựng chặt hơn.** Bản `fr` phải tránh `télécharger` làm động từ chính (đụng `/fr/download-youtube-transcript`) và cấm tuyệt đối `sous-titres` (thuộc `/fr/youtube-subtitle-downloader`). Bản EN không cần rào này vì các trang anh em EN đã tách rõ bằng cấu trúc URL.

---

## Đối tượng người dùng

- Étudiants (quyết định một `cours` hay `tutoriel` có đáng bỏ ra một tiếng không, biến ý chính thành ghi chú ôn tập)
- Người đi làm (nắm nội dung một `conférence`, một buổi công bố kết quả hay một cuộc phỏng vấn trong ngành giữa các cuộc họp)
- Chercheurs (quét nhanh một loạt video để chọn ra vài cái đáng xem kỹ và trích dẫn)
- Créateurs, marketers (rút thông điệp cốt lõi từ video dài để làm bài đăng, kịch bản)
- Người nghe podcast trên YouTube muốn nắm ý trước khi nghe

---

## Map H2 → keyword (bám ĐÚNG 8 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `fr.json` phải dịch đúng **8 section**, cùng số đoạn `content`, đúng 4 `steps`, đúng **4 `items`** ở S4 và S5, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (fr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Résumé de vidéo YouTube | resume video youtube *(KW chính)* |
| — | **quickAnswer** | comment resumer une video youtube |
| 1 | Ce que le résumé d'une vidéo vous apporte | resume video youtube, resumer youtube *(+ chốt phân định 1)* |
| 2 | Pourquoi résumer une vidéo YouTube plutôt que la regarder en entier | resumer une video youtube, resumer video youtube |
| 3 | Comment résumer une vidéo YouTube avec l'IA | comment resumer une video youtube, resumer une video youtube avec ia, resumer video youtube ia |
| 4 | Ce que contient un bon résumé | *(4 items — l'essentiel / points clés / détails concrets / structure)* |
| 5 | À qui servent les résumés | *(4 items — étudiants / pros / chercheurs / créateurs)* |
| 6 | Résumer des vidéos dans plus de 100 langues | resumer une video youtube en ligne *(+ nhấn tiếng Pháp)* |
| 7 | Quand le résumé ne suffit pas | *(3 internal link — chốt phân định 3)* |
| 8 | Questions fréquentes | resumer une video youtube gratuit, outil resume video youtube, resume automatique video youtube *(+ chốt phân định 2 ở FAQ 4)* |
| — | **conclusion** | resume video youtube, gratuit |

### Ghi chú riêng cho bản fr (KHÔNG tạo section mới)

- **S1 đoạn 3 và FAQ 4 là hai chốt phân định với trang transcript** — dịch sát, không rút gọn. Đây là hai chỗ duy nhất trong thân bài được nhắc `transcription` như khái niệm đối lập.
- **S7 là chốt thứ ba**, chứa cả 3 internal link — dịch sát cả 3 vế, mỗi vế giữ đúng nhu cầu riêng (toàn văn / lưu thành file / chữ thuần).
- **Ví dụ ngôn ngữ ở S6:** thay `German / Japanese` của bản EN bằng ví dụ có **tiếng Pháp** làm đích đến (video tiếng Anh hoặc tiếng Nhật → `résumé` tiếng Pháp) — đổi ví dụ, **không thêm câu**.
- **Xưng `vous` xuyên suốt**, nhất quán với `/fr/youtube-subtitle-downloader`.
- **Không dùng `télécharger` làm động từ chính.** Chỉ được xuất hiện khi có tân ngữ `transcription` / `fichier` — tức là trong S7 (anchor internal link). Tuyệt đối không `télécharger la vidéo`.
- **Cấm `sous-titres`** ở mọi vị trí, kể cả anchor text.

---

## Không nên tối ưu cho các keyword

### Thuộc 4 trang YouTube anh em

- `transcription youtube` / `obtenir la transcription youtube` → **/fr/youtube-transcript**
- `télécharger transcription youtube` → **/fr/download-youtube-transcript**
- `télécharger sous-titres youtube` / `extraire les sous-titres` → **/fr/youtube-subtitle-downloader**

### Nhóm tải VIDEO (không thuộc trang nào)

- `télécharger une vidéo youtube`, `telecharger video youtube mp4`, `convertisseur youtube` → intent tải **VIDEO**, SERP toàn downloader. Trang này **không tải gì cả** — nó **đọc và tóm tắt**.

### Nhóm tóm tắt CHỮ (lạc định dạng)

- `résumer un texte` / `résumer un article` / `résumé automatique de texte` → intent tóm tắt **văn bản**, không phải video. Không thuộc trang này.

### Lạc intent hoàn toàn

- `video cv youtube` → CV vidéo / hồ sơ xin việc. Xem khối lỗi dữ liệu.

---

## Internal linking

Section 7 đoạn 2 chứa **cả 3 link**:

- → `/fr/youtube-transcript` (cần toàn văn từng chữ, không phải ý chính)
- → `/fr/download-youtube-transcript` (cần lưu toàn văn thành file để giữ lại)

Không có link nào trỏ tới `/fr/youtube-subtitle-downloader` — đúng như bản EN.

---

## Ghi chú kỹ thuật cho fr.json

- Cấu trúc **1:1 với `en.json`**: 8 section, 8 FAQ, S1 `content` 3, S2 `content` 3, S3 `steps` 4, S4 `intro` 1 + `items` 4, S5 `intro` 1 + `items` 4, S6 `content` 2, S7 `content` 2, S8 `items` 8, `conclusion.content` 2. **KHÔNG có `specs`.**
- Giữ nguyên Latin: **TranscriptX, YouTube, IA**.
- Xưng hô **`vous`**, thể lịch sự, nhất quán toàn trang.
- Internal link section 7 giữ cú pháp markdown `[anchor](/fr/...)`.
- Luôn viết có dấu: `résumé`, `résumer`, `résumés`.
- Kiểm cuối: `grep -c "sous-titre" fr.json` phải bằng **0**.
