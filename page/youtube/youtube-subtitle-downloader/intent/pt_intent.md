🔥 TranscriptX – YouTube Subtitle Downloader (Portuguese / pt)

URL:
/pt/youtube-subtitle-downloader

Intent chính:

Baixar legendas do YouTube (SRT · VTT, grátis)

Trang này nhắm đến người dùng nói tiếng Bồ Đào Nha (ưu tiên biến thể **pt-BR**) muốn **tải file phụ đề có marcação de tempo** từ video YouTube — SRT hoặc VTT — để nạp vào phần mềm dựng phim, đăng lại video kèm legenda, dịch sang ngôn ngữ khác, hoặc đáp ứng yêu cầu acessibilidade.

---

## 🚨 CỤM YOUTUBE 5 TRANG — TRANG NÀY LÀ BÊN **NHẬN** TOÀN BỘ NHÓM `legenda`

Repo có 5 trang YouTube dễ ăn thịt nhau. Quy tắc phân chia **theo ngữ nghĩa từ**, đã chốt từ khi làm `/pt/download-youtube-transcript`:

> **`legenda` mang nghĩa phụ đề khớp giờ → TRANG NÀY**
> **`transcrição` (tài liệu để đọc / lưu / nộp) → `/pt/download-youtube-transcript`**

Căn cứ: bản EN section 1 tự định nghĩa ranh giới — *"A transcript is text you read on its own; a subtitle file is text built to run alongside video, synced frame by frame to the speech."*

### Trang này nhận trọn nhóm `legenda` mà trang đối xứng đã nhường

| Keyword | Volume | Ghi chú |
| ------- | ------ | ------- |
| `baixar legendas do youtube` | **1K – 10K** | Cụm mạnh nhất cả cụm 5 trang. `/pt/download-youtube-transcript` đã **bỏ hoàn toàn**, không đặt vào title/H1/H2 dù mạnh gấp 10 lần KW chính của trang đó. **Trang này lấy làm H1.** |
| `extrair legendas do youtube` | 100 – 1K | Trang kia không dùng |
| `baixar legenda de video do youtube` | 100 – 1K | Trang kia không dùng |
| `download de legendas youtube` | 10 – 100 | Trang kia không dùng |
| `baixar arquivo de legenda youtube` | 0 – 10 | Trang kia không dùng |
| `baixar legenda youtube srt` | 0 – 10 | Trang kia không dùng |

**Kết quả: bản pt của trang này mạnh hơn hẳn trang đối xứng** (`1K – 10K` vs `100 – 1K`). Đó là phân bổ đúng theo dữ liệu — người Brasil gõ `legenda` nhiều hơn gõ `transcrição`.

### Cụm duy nhất KHÔNG lấy

`baixar legenda do youtube em texto` (0–10) **thuộc `/pt/download-youtube-transcript`**, vì vế **`em texto`** neo rõ là muốn văn bản để đọc, không phải file phụ đề cho editor. Trang này không được dùng khuôn `legenda ... em texto`.

---

## 🔴 MỤC RIÊNG — `legenda` Ở TRANG NÀY LÀ TRỤC CHÍNH, NGƯỢC VỚI TRANG ĐỐI XỨNG

**Đây là điểm dễ làm sai nhất của cặp trang này.** Tiếng Anh tách bạch `transcript` vs `subtitle`; tiếng BĐN **dùng chung đúng một từ `legenda` cho cả hai nghĩa**.

| Trang | Vai trò của từ `legenda` | Số lần được dùng |
| ----- | ------------------------ | ---------------- |
| `/pt/download-youtube-transcript` | **Bị hạn chế nghiêm ngặt** — chỉ 3 vị trí, luôn phải neo (`em texto`, `arquivo de legenda sincronizada`). Cấm ở title/description/h1/h2/conclusion. | đúng 3 |
| **TRANG NÀY** | **Trục chính, không giới hạn** — sản phẩm của trang đúng là file phụ đề. Xuất hiện ở title, h1, nhiều h2, conclusion. | tự do |

### Quy tắc cứng để giữ nhất quán hai chiều

> **Sản phẩm của trang này LUÔN gọi là `legenda` / `arquivo de legenda`. Sản phẩm của trang kia LUÔN gọi là `transcrição`.**

Khi trang này buộc phải nhắc tới trang kia — **3 vị trí duy nhất** — phải gọi rõ là `transcrição`, **tuyệt đối không được gọi là `legenda`**:

| Vị trí | Khuôn bắt buộc | Vì sao |
| ------ | -------------- | ------ |
| **S1 đoạn 2** | `Uma transcrição é um texto que você lê por conta própria` | Câu định nghĩa ranh giới — chống cannibalization mạnh nhất trang |
| **S6 đoạn 2** | `[Transcrição do YouTube](/pt/youtube-transcript)` + `[Baixar Transcrição do YouTube](/pt/download-youtube-transcript)` | Chốt phân định 3 trang anh em |
| **FAQ 5** | `Qual a diferença entre legenda e transcrição?` | Câu hỏi tách nghĩa trực diện |

Cụm chuẩn hóa toàn hệ trang pt: **`arquivo de legenda sincronizada`** (đã chốt ở `/pt/tiktok-caption-downloader`). Trang này được dùng cả dạng ngắn `arquivo de legenda`, vì ở đây không có nguy cơ lẫn nghĩa — cả trang nói về đúng thứ đó.

---

## ⚠️ Lỗi dữ liệu trong `2_loc_kw.md` (section pt)

| Dòng nguồn | Vấn đề | Xử lý |
| ---------- | ------ | ----- |
| `baixar legenda de video do youtube` | thiếu dấu: `video` → đúng chính tả là `vídeo` | Giữ keyword để tra cứu; trong body **viết đúng dấu** `vídeo` |
| `baixar legendas youtube gratis` | thiếu dấu: `gratis` → đúng chính tả là `grátis` | Body viết `grátis` |

Đây là dạng người dùng gõ không dấu trên bàn phím, Google đã gộp về biến thể có dấu.

> ✅ **Danh sách pt của trang này sạch** — **10/10 keyword đúng intent phụ đề**, không dòng rác, không cụm sai intent, không cụm tải VIDEO. Khác hẳn bản `vi` (có 2 dòng rác `Keyword ideas` / `Keywords you provided` + 4 cụm sai intent tải video).

**Số keyword thực dùng: 10/10.**

---

## Từ khóa chính

**baixar legendas do youtube** (1K–10K) ✅ *đã search*

Cụm mạnh nhất toàn cụm 5 trang YouTube bản pt, và cũng là **lõi chung** của 4 cụm đuôi dài khác (`como ...`, `... online`, `... grátis`, `... de vídeo`), nên neo vào đây thì các đuôi dài tự phủ theo.

---

## Từ khóa phụ

### Nhóm `baixar` / `download` (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| baixar legendas do youtube | 1K–10K | ✅ đã search *(KW chính)* |
| como baixar legendas do youtube | 100–1K | ✅ đã search |
| baixar legenda de vídeo do youtube | 100–1K | ✅ đã search |
| baixar legendas do youtube online | 10–100 | ✅ đã search |
| download de legendas youtube | 10–100 | ✅ đã search |
| baixar arquivo de legenda youtube | 0–10 | ✅ đã search |
| baixar legenda youtube srt | 0–10 | ✅ đã search |
| baixar legendas youtube grátis | 0–10 | ✅ đã search |

### Nhóm `extrair` (trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| extrair legendas do youtube | 100–1K | ✅ đã search |
| como extrair legendas do youtube | 10–100 | ✅ đã search |

### Dịch bổ sung (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| legenda em VTT | — | 🔄 dịch bổ sung *(VTT)* |
| traduzir legenda | — | 🔄 dịch bổ sung *(translate subtitles)* |
| editar arquivo de legenda | — | 🔄 dịch bổ sung *(edit subtitle file)* |
| marcação de tempo | — | 🔄 dịch bổ sung *(timecode — cụm đã chuẩn hóa toàn hệ trang pt)* |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

---

## Search Intent

Người dùng BĐN **cần file legenda để làm việc tiếp**, không phải để đọc:

- Nạp SRT vào Premiere / Final Cut / DaVinci Resolve để gắn legenda vào bản dựng.
- Đăng lại vídeo lên kênh mình kèm legenda mà không phải gõ lại.
- Dịch legenda sang tiếng Bồ Đào Nha hoặc ngôn ngữ khác rồi gắn lại.
- Sửa legenda tự động của YouTube vốn hay sai tên riêng và acento.
- Đáp ứng yêu cầu acessibilidade cho người khiếm thính.

Họ kỳ vọng: cola o link là ra arquivo, chọn được SRT hay VTT, có marcação de tempo từng dòng, mở sửa được, grátis, không cài extensão, chạy online ngay trên navegador.

### Khác biệt so với bản tiếng Anh

1. **`legenda` là trục duy nhất, không có từ thứ hai.** Bản EN có `subtitles` và `captions` dùng xen kẽ để đỡ lặp; tiếng BĐN chỉ có `legenda`. Phải chống lặp bằng cách đổi cấu trúc câu và dùng `arquivo de legenda` / `linha de legenda` / `marcação de tempo` xen kẽ.
2. **Trang này là bên NHẬN keyword, ngược chiều hoàn toàn với trang đối xứng.** Bản EN không có vấn đề phân chia — `transcript` và `subtitle` tách bạch tự nhiên. Tiếng BĐN thì `legenda` bị kéo về cả hai phía, nên phải chốt bằng tay. Xem hai khối cảnh báo đầu file.
3. **Nhóm `extrair` mạnh bất thường.** `extrair legendas do youtube` đạt `100 – 1K` và `como extrair legendas do youtube` thêm `10 – 100`. Bản EN không có động từ "extract" nào có volume tương đương. Phải cấp hẳn vế H2 section 1 cho nó.
4. **Phải dập nhiễm intent tải VIDEO.** Cụm `baixar vídeo do youtube` có volume khổng lồ ở Brasil và SERP toàn video downloader. Quy tắc: `baixar` chỉ đi với `legenda` / `arquivo` / `SRT` / `VTT`, **KHÔNG BAO GIỜ** với `vídeo`.
5. **Biến thể pt-BR nhất quán:** `você` (không `tu`), `arquivo` (không `ficheiro`), `baixar` (không `descarregar`), `celular` (không `telemóvel`), `tela` (không `ecrã`), `grátis`. Đồng bộ với `/pt/download-youtube-transcript`, `/pt/video-to-text`, `/pt/tiktok-caption-downloader` đã duyệt.

---

## Đối tượng người dùng

- Editor de vídeo, freelancer dựng phim (nạp SRT vào Premiere/Final Cut/Resolve)
- Người re-upload / tổng hợp vídeo lên kênh riêng
- Người làm legenda (dịch sub) cho khán giả Brasil và Portugal
- Marketer chạy nội dung đa ngôn ngữ trên Instagram / TikTok
- Người làm nội dung cho người khiếm thính (acessibilidade)
- Người muốn sửa legenda automática sai của YouTube

---

## Map H2 → keyword (bám ĐÚNG 7 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `pt.json` phải dịch đúng **7 section**, đúng **2 `items`** ở S2 (khác trang download-transcript vốn có 4), đúng 4 `steps`, đúng 5 `items` ở S4, đúng **8 FAQ**, **3 internal link**. **Trang này KHÔNG có `specs`.**

| # | H2 (pt) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Baixar Legendas do YouTube | baixar legendas do youtube *(KW chính)* |
| — | **quickAnswer** | como baixar legendas do youtube |
| 1 | O Que É de Fato um Arquivo de Legenda | extrair legendas do youtube, baixar arquivo de legenda youtube |
| 2 | SRT ou VTT: Qual Formato de Legenda Baixar | baixar legenda youtube srt |
| 3 | Como Baixar Legendas do YouTube | como baixar legendas do youtube, baixar legendas do youtube online, download de legendas youtube |
| 4 | O Que Fazer com o Arquivo de Legenda Baixado | baixar legenda de vídeo do youtube, baixar arquivo de legenda youtube |
| 5 | Baixe Legendas em Mais de 100 Idiomas | baixar legendas youtube grátis *(+ nhấn tiếng BĐN)* |
| 6 | Legenda, Transcrição ou Resumo? | *(3 internal link — chốt phân định)* |
| 7 | Perguntas Frequentes | como extrair legendas do youtube, baixar legendas do youtube online + long-tail |
| — | **conclusion** | baixar legendas do youtube, grátis |

### Ghi chú riêng cho bản pt (KHÔNG tạo section mới)

- **Section 6 là chốt phân định với 3 trang anh em** — dịch sát cả 3 vế, không rút gọn, không gộp. Đây là chỗ duy nhất được nhắc `transcrição` như một sản phẩm (thuộc trang kia), và phải gọi đúng tên đó, không được gọi là `legenda`.
- **Section 1 đoạn 2 là định nghĩa ranh giới của bản EN** (`transcript` = chữ để đọc; `subtitle file` = chữ chạy đè lên vídeo, khớp từng khung hình). **Dịch sát, không rút gọn** — đây là câu chống cannibalization mạnh nhất trang, và là câu đối xứng ngược với quy tắc neo của `/pt/download-youtube-transcript`.
- **S1 đoạn 3** là chỗ nhồi `extrair legendas do youtube` + `baixar arquivo de legenda youtube` (tương ứng vế "YouTube captions downloader" của bản EN).
- Nỗi lo nhận dạng tiếng BĐN xử lý **trong section 5**, thay ví dụ ngôn ngữ của bản EN bằng ví dụ có tiếng BĐN — không thêm câu.
- FAQ 5 giữ nguyên vai câu tách nghĩa `legenda` vs `transcrição` — đây là FAQ quan trọng nhất của bản pt, quan trọng hơn hẳn bản EN.

---

## Không nên tối ưu cho các keyword

- **`baixar transcrição do youtube` / `baixar transcrição de vídeo do youtube` / `baixar legenda do youtube em texto` / `download transcrição youtube`** → **/pt/download-youtube-transcript** (tài liệu để đọc / lưu / nộp, TXT · DOCX · PDF). Chỉ được nhắc ở section 6.
- `transcrição do youtube` / `ver transcrição do youtube` / `pegar transcrição do youtube` → **/pt/youtube-transcript** (đọc trên tela, không tải arquivo).
- `resumir vídeo do youtube` / `resumo de vídeo do youtube` → **/pt/youtube-video-summarizer**.
- **`baixar vídeo do youtube` / `baixar vídeo do youtube com legenda` / `youtube downloader` / `baixar mp4 do youtube`** → **intent tải VIDEO**, volume khổng lồ ở Brasil, SERP toàn downloader. Trang này tải **arquivo de legenda**. Quy tắc: `baixar` chỉ đi với `legenda` / `arquivo` / `SRT` / `VTT`, **không bao giờ** với `vídeo`.
- **`ativar legendas no youtube` / `como ativar legenda automática` / `como fazer legenda no youtube`** → **hướng dẫn thao tác trong app / YouTube Studio**, không phải công cụ tải file. Người gõ cụm này chỉ muốn bật CC khi xem, không muốn arquivo.

---

## Internal linking

Section 6 đoạn 2 chứa **cả 3 link**:

- → `/pt/youtube-transcript` (chỉ muốn đọc chữ thuần trên tela, không marcação de tempo)
- → `/pt/download-youtube-transcript` (lưu chữ thành TXT/DOCX/PDF) — **đây là trang đối xứng, link quan trọng nhất, và là chỗ trả traffic sai intent về đúng chỗ**
- → `/pt/youtube-video-summarizer` (chỉ cần ý chính)

---

## Ghi chú kỹ thuật cho pt.json

- Xưng hô **`você`**, biến thể **pt-BR**: `arquivo`, `baixar`, `celular`, `tela`, `grátis`, `marcação de tempo`.
- Giữ nguyên Latin: **TranscriptX, YouTube, SRT, VTT, Premiere, Final Cut, DaVinci Resolve, HTML5, TXT, DOCX, PDF, Instagram, TikTok**.
- **Viết đúng chính tả và đủ dấu** (`vídeo`, `grátis`, `áudio`, `idioma`) — kể cả khi keyword nguồn viết thiếu dấu.
- Cấu trúc 1:1 với `en.json`: `seo` 6 keys · `hero` 4 · `quickAnswer` 2 · `sections` **7** · `conclusion` h2 + content 2.
  - S1 `content` **3** | S2 `intro` 1 + `items` **2** | S3 `steps` **4** | S4 `intro` 1 + `items` **5** | S5 `content` **2** | S6 `content` **2** | S7 `items` **8**.
  - **KHÔNG có `specs`.**
- Internal link S6 giữ cú pháp markdown, đổi path sang `/pt/...`.
- **Tuyệt đối không để chuỗi `baixar o vídeo` / `baixar vídeo` / `download do vídeo` xuất hiện.**
- **Kiểm tra bắt buộc sau khi viết:** grep `transcri` và xác nhận từ này **chỉ xuất hiện** ở S1 đoạn 2, S6 đoạn 2, FAQ 5 (và trong tên thương hiệu `TranscriptX`) — không được rò rỉ sang chỗ khác.
