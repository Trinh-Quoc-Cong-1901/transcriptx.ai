🔥 TranscriptX – YouTube Transcript (Portuguese / pt)

URL:
/pt/youtube-transcript

Intent chính:

transcrever vídeo do YouTube / lấy transcrição của video YouTube online, miễn phí

Trang này nhắm đến người dùng nói tiếng Bồ Đào Nha (chủ yếu **pt-BR**) muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán link là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA ĐÃ CHỐT

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm.

### Quyết định đã chốt

> Trang này là **hub** nên **giữ trọn họ từ transcript**: `transcrição`, `transcrever`, `transcript`, **và cả nhóm `extrair` / `tirar texto`**.

### ✅ Hệ quả thực tế: trang này KHÔNG phải nhường cụm nào

Toàn bộ 13 keyword đúng intent trong danh sách `## Portuguese (pt)` đều thuộc về trang này, kể cả nhóm `converter vídeo do youtube em texto` / `youtube para texto` / `transformar vídeo do youtube em texto` — vì các cụm đó **có chữ `youtube`**, nên không đụng trang generic `/pt/video-to-text`.

### Nhưng vẫn phải giữ ranh giới TRONG NỘI DUNG

Bản EN đã cài sẵn các chốt phân định, **dịch sát, không rút gọn, không gộp**:

- **Section 11 (`Copiar, editar, traduzir ou baixar`)** — chứa cả **4 internal link**, là chốt phân định chính.
- **FAQ 10** (`transcrição` vs `legendas`) — chốt với `/pt/youtube-subtitle-downloader`.
- **FAQ 4** (`gerar` vs `extrair`) — chốt nội bộ, giữ hai intent generator/extractor trong cùng một trang thay vì tách trang.

---

## 🚫 LỖI DỮ LIỆU — ĐÃ KIỂM, KHÔNG CÓ DÒNG NÀO PHẢI LOẠI

Đã kiểm section `## Portuguese (pt)` trong `2_loc_kw.md` theo đúng checklist đã dùng cho bản `es`:

| Loại lỗi cần tìm | Kết quả ở section `pt` |
| ---------------- | ---------------------- |
| Dòng nhãn `Keyword ideas` | ❌ **không có** |
| Dòng nhãn `Keywords you provided` | ❌ **không có** |
| Cụm `texttomp3` (công cụ TTS — intent NGƯỢC) | ❌ **không có** |
| Cụm garbled / sai chính tả không phải tiếng BĐN chuẩn | ❌ **không có** |

> ⚠️ Lỗi export hệ thống này **có thật** nhưng chỉ nhiễm vào các section `## Spanish (es)`, `## French (fr)` và `## Vietnamese (vi)` của cùng file. Section `pt` **sạch hoàn toàn** — 13/13 dòng đều là keyword tiếng BĐN hợp lệ, đúng intent transcript.

### 📊 Số keyword thực: **13 − 0 = 13**

Toàn bộ 13 keyword đều dùng được, không phải loại dòng nào.

---

## 🔤 QUY TẮC DÙNG TỪ `legenda` — MỤC RIÊNG

Đây là điểm khó nhất của bản `pt`. Bản EN dùng `captions` ở khoảng **6 chỗ**, và tiếng Anh phân biệt được `captions` (chữ hiện khi phát) với `subtitles` (phụ đề dịch). **Tiếng Bồ Đào Nha chỉ có một từ: `legenda`** — gộp cả hai nghĩa. Nếu dịch thẳng, trang sẽ tự cạnh tranh với `/pt/youtube-subtitle-downloader`.

Áp dụng đúng quy tắc đã chốt ở bản `es`:

| Tình huống | Cách viết ở `pt.json` |
| ---------- | --------------------- |
| **Kết quả mà trang này tạo ra** | **LUÔN** là `transcrição` hoặc `texto`. **Tuyệt đối không** gọi là `legenda`. |
| Bản EN nói `captions` (chữ của video, do người đăng thêm hoặc YouTube tự tạo) | Thêm định ngữ: **`legendas automáticas`** hoặc **`legendas do criador`**. Không bao giờ để trần. |
| `legenda` **để trần** | Chỉ ở **S11** (anchor trỏ sang trang phụ đề) và **FAQ 10** (câu hỏi so sánh `transcrição` vs `legendas`). Hai chỗ duy nhất. |

### Kết quả kiểm thực tế trên `pt.json`

- **H1 / 12 H2 / conclusion.h2:** 0 chỗ chứa `legenda`.
- **Toàn bộ H3** (4 `steps` + 6 + 2 + 5 `items`): 0 chỗ chứa `legenda`.
- **12 FAQ `q`:** chỉ **1** chỗ chứa — đúng **FAQ 10**, là câu so sánh được phép.
- FAQ 3 (bản EN: *"Can I generate a transcript if the video has no captions?"*) đã được viết lại thành **"E se o vídeo não tiver transcrição automática do YouTube?"** để không đưa `legenda` lên heading, vẫn giữ nguyên intent `gerador` và giữ nguyên câu trả lời.
- Nhãn spec S2: **`Funciona sem legendas automáticas`** — có định ngữ, đúng quy tắc (nhãn spec không phải heading).

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc áudio → trả về **toàn bộ lời nói dưới dạng văn bản** trong hơn 100 ngôn ngữ, tách từng người nói, marcações de tempo tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **pegar / obter / get** — lấy transcrição có sẵn,
- **gerar / generate** — dựng transcrição từ áudio khi video không có legendas do criador,
- **extrair / tirar** — rút chữ ra khỏi video.

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

---

## Từ khóa chính

**transcrever video do youtube (1K–10K)** ✅ *đã search* → **H1**

Đây là cụm có volume cao nhất của tiếng BĐN trong danh sách. Toàn bộ trang xây quanh nó: xuất hiện ở `title`, `h1`, `ogTitle`, H2 của S2, H2 của S3 (dạng `como`), và `conclusion.content[2]`.

---

## Từ khóa phụ

### Nhóm `transcrever` (động từ — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcrever video do youtube | 1K–10K | ✅ đã search *(KW chính)* |
| como transcrever um video do youtube | 1K–10K | ✅ đã search |
| transcrever audio do youtube em texto | 10–100 | ✅ đã search |

### Nhóm `transcrição` (danh từ — kết quả)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transcricao de video do youtube | 1K–10K | ✅ đã search |
| transcricao do youtube | 100–1K | ✅ đã search |
| pegar transcricao do youtube | 0–10 | ✅ đã search |
| transcricao automatica youtube | 0–10 | ✅ đã search |

### Nhóm `em texto` / `para texto` (chuyển đổi)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| transformar video do youtube em texto | 100–1K | ✅ đã search |
| converter video do youtube em texto | 100–1K | ✅ đã search |
| youtube para texto | 100–1K | ✅ đã search |
| video do youtube em texto | 100–1K | ✅ đã search |

### Nhóm `extrair` (rút chữ ra)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| extrair texto de video do youtube | 100–1K | ✅ đã search |

### Nhóm `gerador`

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| gerador de transcricao do youtube | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| separação de falantes | — | 🔄 dịch bổ sung (speaker separation) |
| marcações de tempo | — | 🔄 dịch bổ sung (timestamps) |
| mais de 100 idiomas | — | 🔄 dịch bổ sung (100+ languages) |
| sem cadastro / grátis | — | 🔄 dịch bổ sung (no sign-up / free) |
| extrator de roteiros do YouTube | — | 🔄 dịch bổ sung (youtube script extractor) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng BĐN muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán link YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ vício de linguagem).
- Dịch sang ngôn ngữ khác — nhu cầu PT ⇄ EN rất nặng ở Brazil.
- Hoạt động **cả khi video không có legendas do criador** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, mesa-redonda).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên celular.

### Khác biệt so với bản tiếng Anh

1. **Tiếng BĐN chỉ có MỘT từ `legenda` cho cả `captions` lẫn `subtitles`.** Bản EN tách được hai khái niệm nên viết `captions` thoải mái ở 6 chỗ mà không đụng trang phụ đề. Bản `pt` không có xa xỉ đó: nếu dịch thẳng, trang này sẽ tự cạnh tranh với `/pt/youtube-subtitle-downloader`. Phải xử lý bằng **định ngữ bắt buộc** (`legendas automáticas` / `legendas do criador`) và giới hạn `legenda` trần vào đúng 2 chỗ. Đây là ràng buộc nặng nhất của bản `pt`, bản EN hoàn toàn không có.

2. **Động từ mạnh hơn danh từ, ngược với EN.** `transcrever video do youtube` (1K–10K) và `como transcrever um video do youtube` (1K–10K) đứng ngang hoặc trên `transcricao do youtube` (100–1K). Bản EN đặt danh từ `YouTube Transcript` làm H1; bản `pt` **phải đặt động từ làm H1** (`Transcrever Vídeo do YouTube`). Đây là thay đổi cấu trúc thật, không phải dịch nghĩa đen.

3. **Nhóm `em texto` phân mảnh thành 4 động từ riêng, EN chỉ có một cụm `video to text`.** Tiếng BĐN có `transformar … em texto`, `converter … em texto`, `youtube para texto`, `vídeo do youtube em texto` — mỗi cụm 100–1K, cộng lại vượt cả cụm chính. Không được dịch tất cả về một cách nói; phải rải đủ **cả bốn biến thể** trong S5 và S7 thay vì lặp một cụm.

4. **Cụm `como` là intent riêng có volume thật.** `como transcrever um video do youtube` đạt **1K–10K** — ngang cụm chính. Bản EN không có "how to" nào có volume tương đương. Phải cấp trọn H2 của **section 3** (steps) và `quickAnswer.question`.

5. **Rủi ro cannibalization ngược từ nhóm tải VIDEO.** `baixar vídeo do youtube` trong tiếng BĐN là cụm khổng lồ, SERP toàn downloader MP4. Kỷ luật cứng: `baixar` **chỉ** đi với `transcrição` / `texto` / `arquivo`, **không bao giờ** với `vídeo`. Bản EN không chịu áp lực này ở cùng mức.

6. **Chuẩn pt-BR chứ không phải pt-PT.** Volume tập trung ở Brazil, nên dùng `você` (không phải `tu`), `arquivo` (không phải `ficheiro`), `baixar` (không phải `descarregar`), `celular` (không phải `telemóvel`), `tela` (không phải `ecrã`). Bản EN trung lập vùng miền, bản `pt` phải chọn dứt khoát.

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến aula, curso thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (entrevista, podcast, mesa-redonda — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần roteiro bruto để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ PT ⇄ EN ⇄ ES
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `pt.json` phải dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 (pt) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Transcrever Vídeo do YouTube | transcrever video do youtube *(KW chính)* |
| — | **quickAnswer** | como transcrever um video do youtube |
| 1 | O que é uma transcrição do YouTube? | transcricao do youtube, transcricao de video do youtube |
| 2 | Transcrever vídeo do YouTube em resumo *(`specs` × 10)* | transcrever video do youtube |
| 3 | Como transcrever um vídeo do YouTube *(`steps` × 4)* | como transcrever um video do youtube |
| 4 | Gerador de transcrição do YouTube | gerador de transcricao do youtube, transcricao automatica youtube |
| 5 | Extrair texto de vídeo do YouTube | extrair texto de video do youtube, converter video do youtube em texto, transformar video do youtube em texto |
| 6 | Para que serve uma transcrição do YouTube *(`items` × 6)* | transcricao de video do youtube |
| 7 | Transcrever o YouTube em qualquer idioma | transcrever audio do youtube em texto, transcricao do youtube |
| 8 | TranscriptX frente à transcrição integrada do YouTube *(`items` × 2)* | transcricao automatica youtube |
| 9 | A precisão e o que afeta ela | *(E-E-A-T, không nhắm KW)* |
| 10 | Quando a transcrição do YouTube pode não funcionar *(`items` × 5)* | transcricao do youtube |
| 11 | Copiar, editar, traduzir ou baixar | *(4 internal link — chốt phân định)* |
| 12 | Perguntas frequentes *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion** *(3 đoạn)* | pegar transcricao do youtube, transcrever video do youtube, grátis |

### Ghi chú riêng cho bản pt (KHÔNG tạo section mới)

- **S2 tái dùng ĐÚNG 8 nhãn `specs` đã duyệt ở `/pt/video-to-text/pt.json`**, chỉ đổi giá trị cho hợp YouTube: `Preço`, `Conta necessária`, `Instalação`, `Idiomas`, `Separação de falantes`, `Marcações de tempo`, `Formatos de exportação`, `Dispositivos`. Hai nhãn mới riêng của trang này thay cho `Limite de tamanho` / `Formatos aceitos` của trang generic: **`Entrada`** (Input — link video YouTube) và **`Funciona sem legendas automáticas`** (Works when the video has no captions).
- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại**, vì mỗi section giữ một họ keyword riêng của tiếng BĐN.
- **S5 gánh nhóm `em texto`:** trong 2 đoạn phải rải đủ `extrair texto de vídeo do YouTube`, `converter vídeo do YouTube em texto`, `transformar vídeo do YouTube em texto` — ba biến thể, không lặp một cụm ba lần.
- **S8 là section so sánh** với transcrição tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào. Đây là chỗ duy nhất trong body từ `legenda` được dùng trần, để trỏ sang trang phụ đề.
- **Kỷ luật `baixar`:** chỉ đi với `transcrição` / `texto` / `arquivo` / `TXT, DOCX, PDF, SRT, VTT`. **Không bao giờ** viết `baixar o vídeo` — kể cả ở S3 bước 2 (bản EN nói "no file to download first" → dịch thành `nem arquivo para baixar antes`, giữ `arquivo`, không dùng `vídeo`).
- Xưng hô **`você`** (`cole`, `copie`, `edite`, `seu`) — chuẩn pt-BR, nhất quán với `/pt/video-to-text/pt.json`.
- **`vídeo` viết CÓ dấu** trong body (chuẩn chính tả BĐN); keyword không dấu trong `2_loc_kw.md` chỉ là dạng người dùng gõ, Google khớp cả hai.
- Nhấn `grátis` ở `title`, `hero.subtitle` (gián tiếp), S1 đoạn cuối, FAQ 2 và `conclusion.h2` — đúng vị trí bản EN.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`baixar transcricao do youtube` / `download transcricao youtube`** → **`/pt/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`baixar legendas do youtube` / `legenda srt youtube` / `extrair legendas do youtube`** → **`/pt/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). Nhóm `legenda` để trần thuộc trọn về trang đó.
- **`youtube video em texto`**: giữ ở hub này — không còn trang riêng cho cách gọi "video em texto". Các cụm `converter/transformar … do youtube em texto` cũng giữ ở đây vì đúng intent transcript.
- **`resumir video do youtube` / `resumo de video do youtube` / `resumidor de youtube`** → **`/pt/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Trang generic

- **`converter video em texto` / `video em texto` / `transcrever video` / `transcritor de video`** (không có chữ `youtube`) → **`/pt/video-to-text`** — **đã hoàn thành**. Mọi cụm nhóm `em texto` dùng ở trang này **bắt buộc phải có `youtube`** trong cụm.
- **`audio em texto` / `transcrever audio`** (không có `youtube`) → **`/pt/audio-to-text`**.

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`baixar video do youtube` / `baixar youtube mp4` / `download video youtube gratis` / `youtube para mp4`** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc cứng đã nêu ở trên.

### Sai intent hoàn toàn — nhóm TTS

- **`texttomp3` và mọi cụm TTS** (`texto para voz`, `converter texto em audio`, `ler texto em voz alta`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. *(Section `pt` của `2_loc_kw.md` không dính cụm này — nhưng `es` và `fr` thì có, nên vẫn ghi lại để cảnh giác.)*
- **`ativar legendas no youtube` / `como colocar legenda no youtube`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Thứ tự và vai trò:

| Link | Anchor (pt) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/pt/download-youtube-transcript` | Baixar Transcrição do YouTube | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/pt/youtube-subtitle-downloader` | Baixador de Legendas do YouTube | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/pt/youtube-video-summarizer` | Resumidor de Vídeos do YouTube | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây.

---

## Ghi chú kỹ thuật cho pt.json

- Cấu trúc **1:1 với `en.json`**, không sai một phần tử:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/pt/...)`, đổi path sang `/pt/`.
- Thuật ngữ khớp `/pt/video-to-text/pt.json` đã duyệt: `marcações de tempo` (timestamps), `separação de falantes` (speaker separation), `arquivo` (file), `link` (link), `navegador` (browser), `sem cadastro` (no sign-up), `detectados automaticamente` (auto-detected), `celular` (mobile).
- `hero.placeholder` và `hero.button` phải ngắn — dịch gọn, không thêm chữ.
- **Kiểm tra bắt buộc trước khi bàn giao — ĐÃ CHẠY, ĐẠT:**
  1. `python3 shape_check.py en.json pt.json` → in `pt.json -> True` ✅
  2. `grep -o 'baixar[^.]\{0,40\}vídeo'` → **0 kết quả** ✅
  3. `legenda` trên H1 / H2 / H3 → **0 kết quả**; trên FAQ `q` → **đúng 1** (FAQ 10, câu so sánh được phép) ✅
  4. `grep -c 'texttomp3'` → **0** ✅
  5. 4 path internal link đúng `/pt/` prefix, đủ 4, không thừa không thiếu ✅
