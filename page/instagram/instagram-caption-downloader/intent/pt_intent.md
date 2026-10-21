🔥 TranscriptX – Instagram Caption Downloader (Portuguese / pt)

URL:
/pt/instagram-caption-downloader

Intent chính:

Baixar e copiar a legenda do Instagram grátis

Trang này là **bản tiếng Bồ Đào Nha** của trang Instagram Caption Downloader. Nhắm đến người dùng nói tiếng Bồ (chủ yếu Brazil) muốn lấy **legenda / descrição** (phần chữ mà tác giả **GÕ** dưới bài đăng) từ Instagram Post, Reel hoặc Video — để copiar, salvar, traduzir, phân tích hoặc tái sử dụng.

Gộp toàn bộ intent đồng nghĩa **baixar / copiar / extrair / salvar** vì tất cả cho ra **cùng một kết quả**: legenda do Instagram → texto.

> ⚠️ **PHÂN ĐỊNH INTENT SỐNG CÒN: Legenda (caption) ≠ Transcrição.** Trang này lấy chữ tác giả **VIẾT** dưới bài (descrição, hashtags, emoji, quebras de linha). Trang anh em `/pt/instagram-transcript` lấy chữ người ta **NÓI** trong video (voz, narração, áudio). Section 2 của `en.json` tồn tại **chính để phân định điều này** — bản `pt` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau.

> ⚠️ **RỦI RO ĐẶC THÙ CỦA TIẾNG BỒ: `legenda` có HAI NGHĨA.**
> 1. **Caption Instagram** — phần chữ dưới bài đăng. ← *đây là trang này*
> 2. **Phụ đề video (subtitle/SRT)** — chữ chạy dưới màn hình phim, chính là nghĩa trong `baixar legenda de filme`, `legenda srt`, `legendas automáticas`.
>
> Đây là nguồn nhiễm intent **thật và nguy hiểm nhất** của bản pt, vì cả hai nghĩa dùng chung một từ và cùng đi với động từ `baixar`. Cách xử lý bắt buộc:
> - **Luôn neo `legenda` vào Instagram và vào hành vi VIẾT.** Mọi lần xuất hiện ở `title` / `h1` / `h2` / `description` phải là `legenda do Instagram` / `legenda de um post` / `legenda de Reels` — **không bao giờ** để `legenda` đứng trần một mình.
> - **Định nghĩa sớm và dứt khoát.** Ngay đoạn 1 của section 1 phải nói rõ: legenda ở đây là *a descrição que o autor escreveu embaixo do post* — **không phải** *legenda de vídeo / arquivo de legenda*. Câu này vừa dập nhiễm intent phụ đề, vừa phục vụ luôn việc phân định với transcript.
> - **Tuyệt đối cấm** các từ `SRT`, `VTT`, `legenda automática`, `sincronizar`, `baixar legenda de filme` xuất hiện ở bất kỳ đâu trong `pt.json`. Chỉ cần một chữ `SRT` là kéo về nhóm truy vấn phụ đề phim, vốn có volume lớn hơn nhiều và sẽ nuốt chủ đề của trang.
>
> **Ghi chú phân bổ `legenda` vs `descrição`:**
> - `legenda` = từ khóa chủ lực (cả 2 KW top band đều dùng nó) → dùng ở `title`, `h1`, `h2` section 3 và 5, `conclusion`.
> - `descrição` = từ đồng nghĩa bản địa, có 2 KW riêng (`baixar descricao do instagram`, `copiar descricao do instagram`) → dùng để **giảm mật độ `legenda`** và làm rõ nghĩa. Đặt trong body section 1, section 4, section 5, FAQ.
> - Nguyên tắc thực dụng: chỗ nào có nguy cơ đọc nhầm sang "phụ đề", thay bằng `descrição` hoặc `texto da legenda`.

> ⚠️ **Quyết định đã chốt: H1 GIỮ KHUNG `baixar`.** Bản pt là ca **thuận lợi nhất** trong toàn bộ 14 ngôn ngữ: `baixar legenda do instagram` và `copiar legenda do instagram` **hòa nhau ở cùng band 100 – 1K** — không ngôn ngữ nào khác có chuyện download và copy cân bằng như vậy (de nghiêng hẳn về `kopieren`, id/ms nghiêng về `salin`, ja/ko nghiêng về copy). Vì hòa, không cần đánh đổi: **H1 dùng `baixar`** (khớp EN + khớp URL `-downloader`), còn `copiar legenda do instagram` được cấp **H2 section 5 với trọng số đầy đủ** — đúng mẫu `de.json` section 5.

> ⚠️ **Cảnh báo chính tả: dữ liệu keyword được gõ KHÔNG DẤU** (`descricao`, `publicacao`, `video`). Nội dung phải viết **đúng chính tả có dấu** (`descrição`, `publicação`, `vídeo`) vì Google chuẩn hóa dấu cho tiếng Bồ. Không cần nhét dạng không dấu vào body.

> ⚠️ **Giới từ `do`.** Người Brazil nói `legenda do Instagram` (có `do`), không nói *"legenda Instagram"*. Mọi H1/H2 phải giữ `do`.

---

## Từ khóa chính

**baixar legenda do instagram** (100 – 1K) ✅ *đã search*

## Từ khóa đồng hạng (dùng ở H2 section 5, KHÔNG ở H1)

**copiar legenda do instagram** (100 – 1K) ✅ *đã search* — xem quyết định đã chốt ở trên

---

## Từ khóa phụ

### Nhóm Baixar (trục chính, khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| baixar legenda do instagram | 100 – 1K | ✅ đã search *(KW chính)* |
| baixar descricao do instagram | 0 – 10 | ✅ đã search |
| baixar legenda de video instagram | 0 – 10 | ✅ đã search |
| como baixar a legenda de um post instagram | 0 – 10 | ✅ đã search |
| baixar legenda instagram online | 0 – 10 | ✅ đã search |
| baixar legenda de reels instagram | 0 – 10 | ✅ đã search |
| baixar legenda do instagram pelo link | 0 – 10 | ✅ đã search |
| baixar texto de publicacao instagram | 0 – 10 | ✅ đã search |

### Nhóm Copiar (đồng hạng volume — dồn vào section 5)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| copiar legenda do instagram | 100 – 1K | ✅ đã search |
| copiar descricao do instagram | 0 – 10 | ✅ đã search |

### Nhóm Extrair / Salvar

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| extrair legenda do instagram | 0 – 10 | ✅ đã search |
| salvar legenda do instagram | 0 – 10 | ✅ đã search |

### Dịch bổ sung (chỉ rải trong body, KHÔNG vào title/H1/H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram caption downloader | — | 🔄 dịch bổ sung (tên công cụ, giữ Latin) |
| copiar hashtags do instagram | — | 🔄 dịch bổ sung (keep the hashtag set) |
| baixar legenda do instagram sem cadastro | — | 🔄 dịch bổ sung (no sign-up) |
| copiar legenda de carrossel do instagram | — | 🔄 dịch bổ sung (carousel) |

**Tổng: 12 KW ✅ đã search + 4 KW 🔄 dịch bổ sung.**

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, chỉ những KW này mới được đặt vào `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body/FAQ để phủ ngữ nghĩa.

---

## Search Intent

Người dùng Brazil/Bồ Đào Nha thấy một legenda Instagram hay — của mình hoặc của đối thủ — và muốn lấy nguyên văn phần chữ đó ra ngoài app, vì Instagram **không có nút copiar legenda**, và bôi đen trên celular thì rất khó, hay dính nhầm chỗ hoặc mở nhầm menu.

Họ thường kỳ vọng:

- Chỉ cần **colar o link** do post, không cần đăng nhập Instagram.
- Lấy **nguyên vẹn** hashtags, emoji và quebras de linha — không bị gộp thành một cục chữ.
- Chạy được với post ảnh, carrossel, Reel và vídeo.
- **Grátis thật**, không cài app, không cadastro.
- Copiar được ngay để colar sang chỗ khác (planilha, doc, ferramenta de agendamento).
- Chạy tốt trên **celular** — thị trường BR mobile-first, và đây chính là nơi việc copy thủ công đau nhất.

### Khác biệt so với bản tiếng Anh

1. **`copiar` mạnh ngang `baixar` — bản EN không có chuyện này.** Bản EN đóng khung dứt khoát là "downloader" và cụm download chiếm hết volume (`instagram caption downloader` 10K–100K). Bản pt thì **hai động từ hòa nhau ở cùng band 100 – 1K**. Hệ quả: không được coi `copiar` là từ đồng nghĩa phụ để dịch qua loa — nó là một trục riêng, phải được cấp H2 section 5 và xuất hiện tự nhiên trong quickAnswer, steps, FAQ. Đây là điểm khác biệt lớn nhất so với EN.

2. **`legenda` là từ đa nghĩa — bản EN không có rủi ro tương đương.** Tiếng Anh `caption` cũng có nghĩa phụ đề nhưng người Anh ngữ dùng `subtitles` cho phụ đề, nên `caption` gần như luôn hiểu là caption mạng xã hội. Tiếng Bồ dùng **cùng một từ `legenda`** cho cả hai. Vì vậy bản pt **bắt buộc phải làm thêm một việc mà bản EN không cần**: định nghĩa `legenda` ngay đoạn đầu và luôn neo nó vào `do Instagram`. Xem khối cảnh báo phía trên.

3. **Không có từ mượn "caption" trong keyword pt.** Khác bản de (nơi `Caption` mượn Anh và `Bildunterschrift` thuần Đức chạy song song, cả hai đều có keyword riêng), người Brazil **không gõ** `caption instagram` — 12/12 keyword đều dùng `legenda` hoặc `descrição`. Do đó chữ "Caption" chỉ được phép xuất hiện trong **tên riêng công cụ** (`Instagram Caption Downloader`), không dùng như danh từ chung trong câu tiếng Bồ.

4. **`descrição` là trục thứ ba thật sự, không phải biến thể văn phong.** Có 2 keyword riêng (`baixar descricao`, `copiar descricao`) — đúng cấu trúc đối xứng với cặp `legenda`. Người Brazil gọi phần chữ dưới bài là `descrição` cũng nhiều như `legenda`, và `descrição` **không mang nghĩa phụ đề** — nên nó vừa bắt keyword vừa là công cụ khử nhiễm. Phải dùng xen kẽ chứ không chọn một.

5. **`baixar` cần tân ngữ chặt hơn hẳn bản EN.** Trong tiếng Anh "download the caption" khó bị hiểu nhầm. Trong tiếng Bồ, `baixar do Instagram` mà thiếu tân ngữ sẽ rơi thẳng vào cụm **tải VIDEO** (`baixar vídeo do Instagram`, `baixar Reels`) — nhóm keyword có volume lớn hơn nhiều lần và SERP toàn video downloader. Quy tắc dịch cứng: mọi `baixar` phải kèm `legenda` / `descrição` / `texto`.

---

## Đối tượng người dùng

- Social media manager / profissional de marketing (phân tích legenda đối thủ)
- Criador de conteúdo Brazil (lưu swipe file các legenda hiệu quả)
- Freelancer quản lý Instagram cho khách
- Người muốn traduzir legenda tiếng nước ngoài
- Người muốn salvar legenda trước khi post bị sửa hoặc xóa
- Nhân viên agência làm relatório de conteúdo
- Người bán hàng chép lại descrição sản phẩm từ post

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `pt.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (pt) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Baixar Legenda do Instagram | baixar legenda do instagram *(KW chính)* |
| — | **quickAnswer** | como baixar a legenda de um post instagram, copiar legenda do instagram |
| 1 | O Que o Instagram Caption Downloader Faz | baixar legenda do instagram, baixar legenda de video instagram, baixar descricao do instagram |
| 2 | Legenda ou Transcrição: Do Que Você Precisa? | *(phân định VIẾT/NÓI + internal link `/pt/instagram-transcript`)* |
| 3 | Como Baixar a Legenda de um Post do Instagram | como baixar a legenda de um post instagram, baixar legenda do instagram pelo link |
| 4 | O Que Fazer Com Uma Legenda Baixada | salvar legenda do instagram, baixar legenda de reels instagram, baixar texto de publicacao instagram |
| 5 | **Copiar Legenda do Instagram – Hashtags, Emoji e Formatação Intactos** | **copiar legenda do instagram (100 – 1K)**, copiar descricao do instagram |
| 6 | Perguntas Frequentes | baixar legenda instagram online, extrair legenda do instagram, baixar descricao do instagram + long-tail |
| — | **conclusion** | baixar legenda do instagram, grátis |

### Ghi chú riêng cho bản pt (KHÔNG tạo section mới)

- **Section 5 là van xả cho toàn bộ nhóm `copiar`.** Bản EN section này vốn đã nói về "what you copy reads the same as what was on the post" — nên đưa `Copiar Legenda do Instagram` lên H2 ở đây là **bám đúng nghĩa gốc**, không phải nhét keyword. Vì `copiar` đồng hạng volume với `baixar`, section này được đối xử ngang H1 về mức đầu tư câu chữ.
- **Section 1 đoạn 1 gánh nhiệm vụ khử nhiễm `legenda`.** Bản EN đoạn này đã định nghĩa caption = "the description the creator wrote under the post... not the spoken audio". Bản pt giữ nguyên cấu trúc câu đó nhưng chọn từ sao cho đồng thời loại luôn nghĩa phụ đề — nói rõ là *o que o autor escreveu embaixo do post*. Không thêm câu.
- **Section 2 giữ nguyên vai trò phân định Legenda/Transcrição.** Internal link đổi thành `[Instagram Transcript](/pt/instagram-transcript)`.
- `descrição` xuất hiện tối thiểu 4 lần trong body (section 1, section 4, section 5, FAQ) để bắt nhóm keyword `descricao` và giảm mật độ `legenda`.
- `baixar legenda de reels instagram` đặt vào **item cuối section 4** (Keep the hashtag set) hoặc item "salvar" — đúng chỗ tự nhiên, không cần section mới.
- Kỳ vọng mobile-first (dùng trên **celular**) xử lý **bên trong section 1 đoạn 2 và section 3 step 1** bằng cách chọn từ, không thêm câu.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `transcrição do Instagram` / `transcrever Reels` / `transcrever vídeo do Instagram` → **/pt/instagram-transcript** (chữ **NÓI**, không phải chữ **VIẾT**). Ranh giới sống còn của cụm.
- `transcrever vídeo do YouTube` / `transcrição do YouTube` / `legenda do YouTube em texto` → **/pt/youtube-transcript**
- `transcrever vídeo do TikTok` / `transcrição do TikTok` → **/pt/tiktok-transcript**
- **Nhóm tải VIDEO** — `baixar vídeo do Instagram` / `baixar Reels` / `baixar Reels do Instagram` / `downloader de Reels` / `salvar vídeo do Instagram` → intent **tải file video**, SERP toàn video downloader. Đây là nhóm nhiễm nguy hiểm nhất về volume: trang này tải **chữ**, không tải video. **Quy tắc dịch cứng: mọi `baixar` phải có tân ngữ `legenda` / `descrição` / `texto`, KHÔNG BAO GIỜ `baixar vídeo` hay `baixar Reels`.** Khi cần nói về Reel, viết `a legenda de um Reel`, không viết `baixar Reel`.
- **Nhóm phụ đề (nghĩa thứ hai của `legenda`)** — `baixar legenda de filme` / `legenda srt` / `baixar legenda de série` / `legendas automáticas` / `gerador de legendas` / `sincronizar legenda` → intent **phụ đề video**, hoàn toàn khác. Volume lớn hơn trang này nhiều lần nên nếu để lọt sẽ nuốt chủ đề. **Cấm tuyệt đối các chữ `SRT`, `VTT`, `sincronizar`, `legenda automática` trong `pt.json`.** Mọi `legenda` phải neo vào `do Instagram` / `do post` / `de um Reel`.
- `copiar bio do Instagram` / `copiar comentários do Instagram` → gần `copiar legenda` nhưng khác đối tượng, không tối ưu riêng
- `texto para voz` / `converter texto em áudio` → ngược intent hoàn toàn

---

## Internal linking

- ↔ **/pt/instagram-transcript** — **link quan trọng nhất**, nằm ở **section 2**. Đây là van chuyển hướng cho người dùng thực ra cần chữ **NÓI** trong Reel/vídeo thay vì legenda viết. Không có link này, section 2 mất tác dụng và hai trang sẽ cạnh tranh nhau.
- → /pt/youtube-transcript, /pt/tiktok-transcript (cross-cluster)

---

## Ghi chú kỹ thuật cho pt.json

- **Biến thể: pt-BR.** Nhất quán với `/pt/facebook-transcript`. `lang="pt-BR"`, hreflang `pt`.
- Từ vựng bắt buộc: **você** (không *tu*), **arquivo** (không *ficheiro*), **baixar** (không *descarregar*), **celular** (không *telemóvel*), **tela** (không *ecrã*), **grátis / gratuito** (không *de graça*).
- Câu mệnh lệnh dùng imperativo do *você*: **Cole / Copie / Abra / Toque / Salve / Traduza**, không dùng dạng *Cola / Copia* của pt-PT.
- Dấu tiếng Bồ chuẩn tuyệt đối: **legenda, descrição, vídeo, publicação, grátis, você, formatação, tradução**.
- Luôn dùng **`legenda do Instagram`** (có giới từ `do`), không viết *"legenda Instagram"*.
- Giữ nguyên Latin, không dịch: **TranscriptX, Instagram, Reel, Reels, Carousel, hashtags, emoji**.
  - `Carousel` giữ nguyên theo yêu cầu (người BR cũng nói *carrossel*, nhưng bản này thống nhất giữ Latin như các bản ngôn ngữ khác của trang).
  - `hashtags` và `emoji` viết **chữ thường** khi nằm trong câu tiếng Bồ (khác tiếng Đức phải viết hoa).
- **KHÔNG** dùng `SRT`, `VTT`, `legenda automática`, `sincronizar` ở bất kỳ đâu — xem mục nhiễm intent phụ đề.
- Internal link section 2 giữ cú pháp markdown: `[Instagram Transcript](/pt/instagram-transcript)`.
- Cấu trúc khớp 100% `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**, `conclusion` (h2 + content 2 đoạn).
  - Section 1: `content` 3 | Section 2: `intro` 1 + `items` 2 | Section 3: `steps` 4 | Section 4: `intro` 1 + `items` 5 | Section 5: `content` 3 | Section 6: `items` **8** (q/a)
