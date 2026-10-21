🔥 TranscriptX – TikTok Caption Downloader (Portuguese / pt)

URL:
/pt/tiktok-caption-downloader

Intent chính:

Baixar legenda do TikTok dạng **arquivo de legenda sincronizada** (có timecode), miễn phí

Trang này nhắm đến người dùng nói tiếng Bồ Đào Nha (ưu tiên biến thể **pt-BR**) muốn **tải file phụ đề** của một video TikTok công khai — file có mốc thời gian từng dòng (`marcação de tempo`) — để gắn lại lên video khi repost, để dịch sang ngôn ngữ khác, hoặc để đáp ứng nhu cầu tiếp cận (`acessibilidade`).

---

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/pt/instagram-caption-downloader`.**
>
> Dù tên gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/pt/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (`descrição`, hashtag, emoji) | Lời **NÓI** trong video |
> | Kết quả | Đoạn text đọc được (`texto puro`) | **File phụ đề có timecode** (`arquivo de legenda sincronizada`) |
> | Nghĩa của `legenda` | caption viết dưới bài | **phụ đề khớp thời gian** |
> | SRT / VTT | **CẤM TUYỆT ĐỐI** | chính là sản phẩm |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram caption, `legenda` = chữ viết và mọi nhắc tới SRT/VTT bị cấm. **Ở trang này thì ngược lại.** Đừng áp nhầm quy tắc của trang kia.

---

## 🔴 MỤC QUAN TRỌNG NHẤT — Xử lý từ `legenda` ba nghĩa trong tiếng Bồ Đào Nha

**Đây là ngôn ngữ khó nhất của cặp trang này.** Tiếng Anh có hai từ tách bạch (`caption` vs `subtitle` vs bản dịch phim), tiếng Việt có `phụ đề` vs `mô tả`. Tiếng BĐN **dùng đúng một từ `legenda` cho cả ba nghĩa**:

| Nghĩa | Ví dụ ngoài đời | Trang nào dùng |
| ----- | --------------- | -------------- |
| 1. Chữ tác giả gõ dưới bài đăng (caption) | `a legenda do post no Instagram` | `/pt/instagram-caption-downloader` |
| 2. Phụ đề khớp thời gian chạy đè lên video (subtitle) | `legenda sincronizada`, `arquivo SRT` | **TRANG NÀY** |
| 3. Bản dịch lời thoại phim nước ngoài | `filme legendado` | không dùng |

Người tìm `legenda do tiktok` có thể đang nghĩ tới nghĩa 1 **hoặc** nghĩa 2. SERP nghiêng về nghĩa 2 (TikTok có tính năng auto-caption trên màn hình), nhưng ranh giới rất mỏng. **Nếu để `legenda` đứng trần, trang này sẽ đọc y hệt trang Instagram caption và Google sẽ trộn hai trang.**

### Quy tắc neo ngữ cảnh — BẮT BUỘC, áp cho MỌI lần xuất hiện

**Không bao giờ để `legenda` / `legendas` đứng trần.** Mỗi lần xuất hiện phải nằm trong một trong các khuôn sau:

| Khuôn được phép | Neo nghĩa bằng gì |
| --------------- | ----------------- |
| `arquivo de legenda` | neo bằng **định dạng file** — trang Instagram không bao giờ nói "arquivo de legenda" |
| `legenda sincronizada` / `legendas sincronizadas` | neo bằng **tính đồng bộ** |
| `legendas com marcação de tempo` | neo bằng **timecode** |
| `linha de legenda` / `linhas de legenda` | neo bằng **cấu trúc từng dòng** (caption viết dưới bài không có "dòng") |
| `legendas na tela` | neo bằng **vị trí hiển thị trên video** |
| `legenda automática do TikTok` | neo bằng **auto-caption của nền tảng** |
| `legendas de vídeo do TikTok` (keyword) | neo bằng mệnh đề liền kề nói tới `arquivo` / `marcação de tempo` |

Ngược lại, các khuôn của trang Instagram **bị cấm ở đây**: `legenda escrita`, `legenda do post`, `a descrição que o autor digitou`, `hashtags e emoji`, `copiar a legenda`.

### Đối chiếu trực tiếp với `/pt/instagram-caption-downloader`

| | Instagram caption (pt.json) | **Trang này (pt.json)** |
| --- | --- | --- |
| Cụm mở đầu | `tira a legenda de um post ... como texto puro` | `tira as legendas de vídeo do TikTok ... como arquivo` |
| Động từ chủ đạo | `copiar`, `salvar`, `puxar` | `baixar`, `montar`, `sincronizar` |
| Vật thể kết quả | `texto`, `descrição` | `arquivo de legenda`, `linha de legenda` |
| Thuộc tính nhấn | `hashtags, emoji, quebras de linha` | `marcação de tempo, hora de início e de fim` |

Tham chiếu giọng văn pt-BR: `/pt/instagram-transcript` đã dùng đúng cụm chuẩn `arquivo de legenda sincronizada` (section 6 + FAQ 9) — **lấy nguyên cụm đó làm chuẩn thuật ngữ cho trang này**, để cả cụm trang pt nhất quán.

---

> ⚠️ **PHÂN ĐỊNH VỚI `/pt/tiktok-transcript`: TRỤC LÀ TIMING, KHÔNG PHẢI VIẾT-VS-NÓI.**
>
> Cả hai trang đều lấy lời **NÓI** từ audio. Khác nhau ở **timing**:
> - Trang này → `arquivo de legenda sincronizada` (khớp thời gian, chạy đè lên video)
> - `/pt/tiktok-transcript` → `texto puro` (để đọc / copy, không timecode)
>
> Bản EN cài sẵn **3 chốt chặn** — giữ nguyên cả ba, dịch sát, **không rút gọn, không gộp**:
> 1. **Section 2** — cả section dành riêng để phân định, có internal link `[TikTok Transcript](/pt/tiktok-transcript)` ở item 2.
> 2. **FAQ 3** — "Qual a diferença entre a legenda do TikTok e a transcrição?"
> 3. **Section 1 đoạn 2** — câu giải thích vì sao trang này tách riêng khỏi trang transcript.

---

## Lưu ý riêng — CHỈ CÓ 3 KEYWORD

Danh sách `pt` trong `2_loc_kw.md` là một trong những danh sách **mỏng nhất** của toàn bộ dự án: chỉ **3 keyword**, trong đó chỉ 1 cụm ở band `10 – 100`, hai cụm còn lại `0 – 10`.

**Hệ quả về chiến lược:**

- **~30% nội dung** neo được vào keyword đã search (title, H1, description, quickAnswer, H2 section 3 & 5, conclusion, FAQ 1–3).
- **~70% còn lại là dịch bổ sung** — dịch tự nhiên từ bản EN, dùng biến thể pt-BR, **không** nhồi keyword.
- Không có cụm nào áp đảo để dồn lực → chiến lược là **phủ đủ 3 keyword ở vị trí neo**, phần còn lại ưu tiên **độ rõ nghĩa của `legenda`** hơn là mật độ keyword. Với trang này, neo ngữ cảnh quan trọng hơn keyword density.

---

## Từ khóa chính

**legenda do tiktok** (10–100) ✅ *đã search*

⚠️ Đây chính là cụm mơ hồ nhất. Bắt buộc phải đi kèm neo ngữ cảnh ở mọi vị trí: H1 dùng `Baixar Legenda do TikTok **em Arquivo**`, title dùng `— **Arquivo Sincronizado** Grátis`.

---

## Từ khóa phụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| legenda do tiktok | 10–100 | ✅ đã search *(KW chính)* |
| baixar legendas de video do tiktok | 0–10 | ✅ đã search |
| extrair legenda do tiktok | 0–10 | ✅ đã search |
| arquivo de legenda do tiktok | — | 🔄 dịch bổ sung *(subtitle file — cụm neo nghĩa chủ lực)* |
| legenda sincronizada do tiktok | — | 🔄 dịch bổ sung *(synced subtitles)* |
| legendas com marcação de tempo | — | 🔄 dịch bổ sung *(timed captions)* |
| baixar legenda do tiktok grátis | — | 🔄 dịch bổ sung *(free)* |
| como baixar legenda do tiktok | — | 🔄 dịch bổ sung *(how-to)* |
| salvar legenda do tiktok | — | 🔄 dịch bổ sung *(save)* |
| traduzir legenda do tiktok | — | 🔄 dịch bổ sung *(translate — khớp section 5)* |
| legendas na tela do tiktok | — | 🔄 dịch bổ sung *(on-screen captions)* |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

---

## Search Intent

Người dùng BĐN thấy một video TikTok và cần **file phụ đề** của nó — không phải để đọc, mà để **dùng lại**:

- Repost clip lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có `legendas na tela`.
- Dịch phụ đề sang tiếng BĐN (hoặc từ BĐN sang tiếng khác) rồi gắn lại.
- Sửa `legenda automática do TikTok` vốn hay sai chữ, sai dấu (`acento`) trong tiếng BĐN.
- Làm phụ đề cho người khiếm thính (`acessibilidade`).

Họ kỳ vọng:

- Dán link là ra file, không cần đăng nhập TikTok.
- File có **marcação de tempo từng dòng**, mở được bằng phần mềm dựng phim.
- Chạy được cả khi video gốc **không bật legenda na tela**.
- Sửa được chữ trong file trước khi dùng.
- Miễn phí.

### Khác biệt so với bản tiếng Anh

1. **EN có `captions` và `subtitles` là hai từ; pt chỉ có `legenda`.** Bản EN xen kẽ hai từ để chống lặp (`captions` ở H1, `subtitles` ở section 4). Bản pt không có lựa chọn đó → chống lặp bằng cách **đổi khuôn neo**: `arquivo de legenda` → `legenda sincronizada` → `legendas com marcação de tempo` → `linhas de legenda` → `legendas na tela`. Việc đổi khuôn vừa chống lặp vừa neo nghĩa — hai mục tiêu trong một.
2. **Bản pt phải chủ động dập nhiễm nghĩa "caption viết dưới bài".** Bản EN không có vấn đề này vì `caption` trên TikTok mặc định hiểu là chữ trên màn hình. Bản pt thì `legenda do tiktok` có thể bị đọc thành "descrição do post" → phải nói rõ **ngay từ H1 và câu đầu quickAnswer** rằng đây là **arquivo** có **marcação de tempo**, dựng từ **áudio**.
3. **Nỗi lo "legenda automática do TikTok sai tiếng BĐN" là điểm bán hàng riêng.** Auto-caption của TikTok nhận dạng tiếng BĐN hay mất `acento` và nuốt chữ. Bản EN chỉ nói "shaky auto-captions" chung chung — bản pt nhấn đúng nỗi đau này ở **section 4 item 3, trong đúng câu đã có sẵn**, không thêm câu.
4. **Biến thể pt-BR nhất quán:** `você` (không `tu`), `arquivo` (không `ficheiro`), `baixar` (không `descarregar`), `celular` (không `telemóvel`), `tela` (không `ecrã`). Đồng bộ với `/pt/instagram-transcript` và `/pt/instagram-caption-downloader` đã duyệt.
5. **`marcação de tempo` là thuật ngữ chủ đạo, không dùng `timecode` tiếng Anh.** Khác bản vi (giữ `timecode` làm từ mượn), người làm video BĐN dùng `marcação de tempo` / `sincronização` tự nhiên hơn.

---

## Đối tượng người dùng

- Người làm content re-upload / tổng hợp clip TikTok
- Editor video, freelancer dựng phim
- Người cross-post TikTok sang Reels / YouTube Shorts
- Người dịch phụ đề cho khán giả nói tiếng BĐN (Brasil + Portugal)
- Marketer chạy nội dung đa ngôn ngữ
- Người làm nội dung cho người khiếm thính
- Người muốn sửa `legenda automática` sai chính tả / mất dấu của TikTok

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `pt.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**.

| # | H2 (pt) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Baixar Legenda do TikTok em Arquivo | legenda do tiktok *(KW chính)* + neo `em arquivo` |
| — | **quickAnswer** | legenda do tiktok, baixar legendas de vídeo do tiktok |
| 1 | O Que o TikTok Caption Downloader Faz | baixar legendas de vídeo do tiktok, extrair legenda do tiktok |
| 2 | Legenda Sincronizada ou Transcrição: Do Que Você Precisa? | *(phân định + internal link `/pt/tiktok-transcript`)* |
| 3 | Como Baixar as Legendas de um Vídeo do TikTok | baixar legendas de video do tiktok |
| 4 | O Que Fazer Com o Arquivo de Legenda do TikTok Baixado | legendas na tela, arquivo de legenda *(dịch bổ sung)* |
| 5 | Baixar Legenda do TikTok em Mais de 100 Idiomas | legenda do tiktok, traduzir legenda do tiktok |
| 6 | Perguntas Frequentes | legenda do tiktok + long-tail |
| — | **conclusion** | baixar legenda do tiktok, grátis |

### Ghi chú riêng cho bản pt (KHÔNG tạo section mới)

- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho việc này. Dịch đủ 2 item, giữ link `[TikTok Transcript](/pt/tiktok-transcript)` ở item 2. H2 phải mở bằng `Legenda Sincronizada` (không phải `Legenda` trần) để trục timing lộ ra ngay ở mục lục.
- **FAQ 3** là chốt thứ hai — dịch sát, không rút gọn. Câu trả lời phải chứa cả `legenda sincronizada` lẫn `transcrição ... só as palavras, sem tempo`.
- **Section 1 đoạn 2** là chốt thứ ba — giữ nguyên logic "chính marcação de tempo là lý do trang này tách riêng".
- Nỗi lo `legenda automática` sai tiếng BĐN xử lý **trong câu đã có** ở section 4 item 3, không thêm câu mới.
- `extrair legenda do tiktok` chỉ dùng **một lần** trong section 1 (động từ `tira ... de dentro do clipe`), không đặt vào H2.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `transcrição de vídeo do tiktok` / `tiktok em texto` / `texto puro` như một sản phẩm → **/pt/tiktok-transcript** (text thuần, không timing). Ở đây `texto puro` **chỉ được nhắc để loại trừ**, không bao giờ như thứ trang này cung cấp.
- `legenda do post` / `descrição do post` / `legenda escrita` / `hashtags e emoji` → **/pt/instagram-caption-downloader** (chữ viết dưới bài, khác hẳn).
- `legenda do youtube` / `transcrição do youtube` → **/pt/youtube-transcript**.
- **Nhóm tải VIDEO — nguy hiểm nhất:** `baixar vídeo do tiktok`, `tiktok sem marca d'água`, `download de vídeo tiktok`, `salvar vídeo do tiktok`. SERP của nhóm này toàn video downloader. Trang này tải **file phụ đề**, không tải video.

> 🚫 **QUY TẮC CỨNG:** động từ `baixar` (và `download`, `salvar`) chỉ được đi với tân ngữ **`legenda`** / **`arquivo`** / **`legendas`** / **`texto`**. **KHÔNG BAO GIỜ** đi với **`vídeo`**. Chuỗi `baixar o vídeo`, `baixar vídeo`, `download do vídeo` không được xuất hiện ở bất kỳ đâu trong `pt.json`.

---

## Internal linking

- ↔ `/pt/tiktok-transcript` — khi user chỉ cần `texto puro` để đọc, không cần timing. **Link quan trọng nhất**, nằm ở **section 2 item 2** (dạng markdown), nhắc lại bằng tên (không link) ở **FAQ 3**.
- Liên hệ ngầm: `/pt/instagram-transcript` đã link ngược tới `/pt/tiktok-transcript` — giữ thuật ngữ `arquivo de legenda sincronizada` đồng nhất giữa các trang pt để cụm trang đọc như một hệ.

---

## Ghi chú kỹ thuật cho pt.json

- Xưng hô **`você`**, biến thể **pt-BR**: `arquivo`, `baixar`, `celular`, `tela`.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT**.
- Cấu trúc 1:1 với `en.json`: `seo` 6 keys · `hero` 4 · `quickAnswer` 2 · `sections` **6** · `conclusion` h2 + content 2.
  - S1 `content` **3** | S2 `intro` 1 + `items` 2 | S3 `steps` 4 | S4 `intro` 1 + `items` 5 | S5 `content` **2** | S6 `items` **8**.
- Internal link section 2 item 2 giữ cú pháp markdown: `[TikTok Transcript](/pt/tiktok-transcript)`.
- Tuyệt đối không để chuỗi **`baixar o vídeo`** / **`baixar vídeo`** xuất hiện.
- **Kiểm tra bắt buộc sau khi viết:** grep `legenda` và xác nhận **mọi lần xuất hiện đều có bổ ngữ neo nghĩa** theo bảng khuôn ở trên. Báo cáo số lần xuất hiện và số lần được neo.
