🔥 TranscriptX – YouTube Transcript (Turkish / tr)

URL:
/tr/youtube-transcript

Intent chính:

youtube transkript / lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản (transkript), online, miễn phí

Trang này nhắm đến người dùng nói tiếng Thổ Nhĩ Kỳ muốn **lấy toàn bộ lời nói trong một video YouTube dưới dạng văn bản** — để đọc, tìm kiếm, sao chép, sửa, dịch hoặc xuất file. Dán URL là ra chữ, không cần tài khoản, không cài phần mềm.

---

## 🚨 CỤM YOUTUBE 5 TRANG — QUY TẮC PHÂN CHIA

Repo có 5 trang YouTube. Trang này là **trang trụ (hub)** của cả cụm và **giữ trọn họ từ `transkript` / `metin`** (transcript / text). Ranh giới với các trang anh em được cài sẵn trong nội dung, tập trung ở **Section 11**:

| Trang anh em | Đường dẫn | Giữ cụm gì |
| ------------ | --------- | ---------- |
| Tải transcript (file) | `/tr/download-youtube-transcript` | Trọng tâm **tải file** TXT/DOCX/PDF/SRT |
| Tải phụ đề | `/tr/youtube-subtitle-downloader` | File **altyazı** SRT/VTT khớp giờ, cho editor |
| Tóm tắt video | `/tr/youtube-video-summarizer` | Chỉ **ý chính**, không phải toàn văn |

> Trang này là **hub** nên giữ trọn: `transkript` (danh từ chính, loanword), `deşifre` (đồng nghĩa native), **và cả nhóm rút chữ `metin çıkarma` / `metin alma` / `yazı hâline getirme`**. Kết quả trang **luôn gọi là `transkript` hoặc `metin`**, không bao giờ gọi là `altyazı`.

Ranh giới nằm ở **S11** (`Kopyalayın, Düzenleyin, Çevirin veya Kaydedin`) — chứa **cả 4 internal link** và là chốt phân định duy nhất trong toàn trang. Đây cũng là chỗ duy nhất từ `altyazı` được dùng để trỏ sang trang phụ đề.

---

## 🚫 LỖI DỮ LIỆU + SỐ KEYWORD THỰC

Đã kiểm section `## Turkish (tr)` trong `2_loc_kw.md`:

- **KHÔNG** có dòng rác giao diện (`Keyword ideas` / `Keywords you provided`).
- **KHÔNG** có `texttomp3` hay cụm TTS sai intent.
- **KHÔNG** có dòng garbled/lỗi chính tả (khác `es` có `youtube subito texto`).

### 📊 Số keyword thực: **6** — nhưng chỉ **1 cụm có volume thật**

| Tình trạng | Số cụm |
| ---------- | ------ |
| ✅ đã search, volume ≥ 1K | **1** (`youtube transkript`, 1K–10K) |
| ✅ đã search, volume 10–100 | 1 (`youtube deşifre`) |
| ✅ đã search, volume 0–10 | 4 |

Đây là ngôn ngữ **nghèo keyword nhất** trong số các bản đã làm của trang này (so với `es` có 14 cụm). 5/6 cụm gần như không có volume — trang buộc phải **dồn toàn bộ sức mạnh vào một hub term `youtube transkript`** và phủ semantic bằng thân bài, thay vì trải đều nhiều cụm mạnh như `es`.

> ⚠️ **Khuyến nghị search bổ sung** trước khi coi danh sách là hoàn chỉnh: các biến thể có volume tiềm năng chưa xuất hiện trong danh sách — `youtube transkript indir` (tải), `youtube transkript çıkarma`, `youtube video metne çevirme`, `youtube altyazı indir`, `youtube deşifre programı`, `video yazıya dökme`. Cần chạy volume để xác định cụm nào thuộc trang này, cụm nào thuộc trang tải/phụ đề.

---

## ⚠️ MỤC RIÊNG: RỦI RO `indir` ĐỨNG TRẦN = TẢI VIDEO, VÀ BẪY `indirger`

Trong tiếng Thổ, **`indir-`** là động từ "tải xuống". Rủi ro cannibalization: nếu `indir` đứng cạnh `video`, người dùng và Google hiểu là **tải file video MP4** — đúng intent của downloader video, **ngược** với trang này (chỉ ra chữ).

**Kỷ luật cứng (đã được tuân thủ trong `tr.json`):**
- `indir` **chỉ** đi với `transkript` / `altyazı` / `metin` / `TXT, DOCX, PDF, SRT, VTT`.
- **Không bao giờ** viết `videoyu indir` / `video indirme`.
- Đã kiểm: `grep video…indir` → **0 kết quả**. Hai chỗ dùng `İndir` đều là anchor text: `[YouTube Transkript İndirme]` và `[YouTube Altyazı İndirici]` — cả hai gắn với `transkript` / `altyazı`, không gắn `video`. ✅

**Bẫy `indirger`:** động từ `indirgemek` (= giản lược / quy về) trông giống `indir-` nhưng **nghĩa hoàn toàn khác**, dễ lọt vào bản dịch gây tối nghĩa. Đã kiểm: `grep indirge|indirger` → **0 kết quả**. ✅ Khi làm các bản khác của trang này cần giữ nguyên rào chắn này.

> Lưu ý phụ: các từ Thổ như `sizindir`, `metindir` (kết thúc bằng hậu tố `-dir`) chứa chuỗi "indir" nhưng **không phải** động từ tải — đừng nhầm khi grep thô.

---

## ⚠️ MỤC RIÊNG: QUY TẮC DÙNG `altyazı`

Trong tiếng Thổ, **`altyazı`** = phụ đề / caption (một từ dùng cho cả hai). Trang này phải phân định rõ:

- `altyazı` **chỉ** dùng để chỉ **caption có sẵn của YouTube** — phụ đề người đăng thêm, hoặc phụ đề tự động của YouTube (thứ mà công cụ *chiết xuất* hoặc *thay thế*). Xuất hiện ở S1-spec (`Altyazısı olmayan videolarda çalışır mı`), S4 (video không có altyazı → dựng từ audio), S5 (`altyazı metin çıkarma`), S8 (so sánh với panel altyazı của YouTube), S10, FAQ.
- **Kết quả của trang luôn gọi là `transkript` hoặc `metin`** — không bao giờ gọi output là `altyazı`.
- `altyazı` **đứng trần** với vai trò "file phụ đề để tải" chỉ được dùng ở **S11** (link sang `/tr/youtube-subtitle-downloader`, anchor `YouTube Altyazı İndirici`) và **FAQ 9** (câu hỏi so sánh `transkript` vs `altyazı`). Đó là hai chỗ duy nhất trỏ sang trang phụ đề.

Đã kiểm: `altyazı` xuất hiện ~24 lần, luôn ở vai trò caption/phụ đề, không lần nào bị dùng để gọi tên kết quả trang. ✅

---

## Mô tả trang

Landing page công cụ, **trang trụ của cụm YouTube**: dán link video YouTube công khai → TranscriptX đọc audio → trả về **toàn bộ lời nói dưới dạng văn bản (`transkript`)** trong hơn 100 ngôn ngữ, tách từng người nói (`konuşmacı ayrımı`), zaman damgası (timestamp) tùy chọn.

Trang gộp **ba intent đồng nghĩa** vì cùng cho ra một kết quả:
- **almak / get** — lấy transkript có sẵn (`YouTube'dan metin alma`),
- **oluşturmak / generate** — dựng transkript từ audio khi video không có altyazı (`transkript oluşturma`),
- **çıkarmak / extract** — rút chữ ra khỏi video (`altyazı metin çıkarma`).

Gộp để tránh cannibalization và dồn toàn bộ sức mạnh vào một URL duy nhất.

---

## Từ khóa chính

**youtube transkript (1K–10K)** ✅ *đã search* → **H1** (`YouTube Transkript`)

Đây là cụm có volume cao nhất — và gần như là cụm duy nhất có volume đáng kể của bản tr. Toàn bộ trang được xây quanh nó: xuất hiện ở `seo.title`, `h1`, `ogTitle`, `quickAnswer.question`, H2 của S1 / S2 / S3, `conclusion.h2` và FAQ 1.

---

## Từ khóa phụ

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| youtube transkript | 1K–10K | ✅ đã search *(KW chính)* |
| youtube deşifre | 10–100 | ✅ đã search |
| youtube altyazi metin cikarma | 0–10 | ✅ đã search |
| youtube video yazi haline getirme | 0–10 | ✅ đã search |
| youtube transkript olusturma | 0–10 | ✅ đã search |
| youtube den metin alma | 0–10 | ✅ đã search |

### Dịch bổ sung (chỉ rải body, KHÔNG lên H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| konuşmacı ayrımı | — | 🔄 dịch bổ sung (speaker separation) |
| zaman damgası | — | 🔄 dịch bổ sung (timestamps) |
| 100'den fazla dil | — | 🔄 dịch bổ sung (100+ languages) |
| üyelik yok / ücretsiz | — | 🔄 dịch bổ sung (no sign-up / free) |
| YouTube betik çıkarma | — | 🔄 dịch bổ sung (youtube script extractor) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên, phải xuất hiện trong `title` / `h1` / `h2` / `description` / FAQ. 🔄 *dịch bổ sung* = chỉ rải body cho tự nhiên.

---

## Search Intent

Người dùng tiếng Thổ muốn **lấy chữ ra khỏi một video YouTube** để làm việc tiếp với nó. Họ kỳ vọng:

- Chỉ dán URL YouTube, không tải video về trước.
- Ra chữ trong vài giây, đọc ngay trên màn hình.
- Sao chép toàn bộ hoặc một câu trích dẫn.
- Sửa được chữ ngay tại chỗ (sửa tên riêng, bỏ từ đệm).
- Dịch sang ngôn ngữ khác (nhu cầu TR ⇄ EN).
- Hoạt động **cả khi video không có altyazı** — đây là kỳ vọng phân biệt lớn nhất.
- Tách được ai nói câu nào (phỏng vấn, bàn tròn).
- Xuất file khi cần (TXT, DOCX, PDF, SRT, VTT).
- Miễn phí, không đăng ký, không cài đặt, chạy được trên điện thoại.

### Khác biệt so với bản tiếng Anh

1. **`transkript` là loanword và giữ ngôi vương, nhưng có đối thủ native `deşifre`.** Bản EN chỉ có một trục danh từ `transcript`. Tiếng Thổ có **hai từ chỉ kết quả**: `transkript` (mượn từ, volume 1K–10K, làm H1) và `deşifre` (thuật ngữ native, 10–100). Không được dịch cả hai về một từ — `deşifre` phải giữ trọn H2 của **S7** (`Her Dilde YouTube Deşifre`) để phủ cụm đó, còn `transkript` phủ phần còn lại.

2. **Ngôn ngữ chắp dính (agglutinative) trải intent rút chữ thành nhiều cụm động-danh khác nhau.** Bản EN gói get/generate/extract quanh một danh từ. Tiếng Thổ tách thành các cụm bề mặt riêng biệt: `metin alma` (lấy chữ — S5), `metin çıkarma` (chiết chữ — S5), `yazı hâline getirme` (đưa về dạng chữ — S6 intro), `transkript oluşturma` (dựng transkript — S4). Mỗi cụm là một keyword riêng, phải rải đúng section thay vì gộp về một từ.

3. **Cực kỳ nghèo volume so với EN/es.** Chỉ 1/6 cụm có volume ≥ 1K; 5 cụm còn lại 0–100. Bản EN và es dựa vào nhiều cụm mạnh song song; bản tr **phải dồn tất cả vào hub `youtube transkript`** và dùng thân bài phủ semantic. Đây là khác biệt chiến lược, không chỉ dịch.

4. **`altyazı` là một từ cho cả caption lẫn subtitle — EN tách `caption` và `subtitle`.** Bản EN phân biệt hai khái niệm bằng hai từ; tiếng Thổ chỉ có `altyazı`, nên phải phân định bằng **văn cảnh và định ngữ** (caption có sẵn vs file phụ đề để tải), không bằng cách đổi từ. Đây là gánh nặng phân định riêng của bản tr.

5. **Xưng hô trang trọng `siz`, không phải `sen`.** Bản EN trung tính (`you`). Bản tr chọn ngôi **`siz`** — mệnh lệnh dạng số nhiều/lịch sự (`yapıştırın`, `kopyalayın`, `açın`, `düzenleyin`) — đúng chuẩn tông web tiếng Thổ. (Đối chiếu: bản es chọn `tú` thân mật; bản tr chọn trang trọng.)

6. **Rào chắn `indir` + bẫy `indirger` là vấn đề riêng của tiếng Thổ** (xem mục riêng ở trên) — bản EN không chịu áp lực hình thái này.

---

## Đối tượng người dùng

- Sinh viên, học viên online (biến bài giảng, khóa học thành ghi chú ôn thi)
- Giáo viên, giảng viên soạn tài liệu từ video
- Nhà nghiên cứu, nhà báo (phỏng vấn, podcast, tọa đàm — cần trích dẫn chính xác)
- Content creator, blogger, SEO writer (biến 1 video thành bài viết / newsletter)
- YouTuber tái sử dụng nội dung của chính mình
- Developer / AI Engineer / Data Analyst (cần raw script để đưa vào dataset hoặc prompt)
- Marketer đa ngôn ngữ TR ⇄ EN
- Người khiếm thính và người xem không bật được âm thanh

---

## Map H2 → keyword (bám ĐÚNG 12 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section, câu, FAQ.** `tr.json` dịch đúng **12 section**, đúng **10 `specs`** ở S2, **4 `steps`** ở S3, **6 `items`** ở S6, **2 `items`** ở S8, **5 `items`** ở S10, **12 FAQ** ở S12, **3 đoạn** ở `conclusion`, **4 internal link** ở S11. Keyword áp bằng **cách chọn từ khi dịch**, không bằng cách thêm câu.

| # | H2 thực trong tr.json | Keyword nhắm |
| - | --------------------- | ------------ |
| — | **H1:** YouTube Transkript | youtube transkript *(KW chính)* |
| — | **quickAnswer:** YouTube transkript nasıl alınır? | youtube transkript (biến thể "nasıl") |
| 1 | YouTube Transkript Nedir? | youtube transkript |
| 2 | Bir Bakışta YouTube Transkript *(`specs` × 10)* | youtube transkript |
| 3 | YouTube Videosundan Transkript Nasıl Alınır? *(`steps` × 4)* | youtube transkript, youtube den metin alma |
| 4 | YouTube Transkript Oluşturma | youtube transkript olusturma |
| 5 | YouTube'dan Metin Alma ve Metin Çıkarma | youtube den metin alma, youtube altyazi metin cikarma |
| 6 | YouTube Transkriptini Nerelerde Kullanabilirsiniz *(`intro` 1 + `items` × 6)* | youtube video yazi haline getirme *(intro: "videoyu yazı hâline getirme")* |
| 7 | Her Dilde YouTube Deşifre | youtube deşifre |
| 8 | TranscriptX ile YouTube'un Yerleşik Transkripti *(`items` × 2)* | youtube transkript (so sánh) |
| 9 | Doğruluk ve Onu Etkileyen Etkenler | *(E-E-A-T, không nhắm KW)* |
| 10 | YouTube Transkript Ne Zaman Çalışmayabilir *(`intro` 1 + `items` × 5)* | youtube transkript |
| 11 | Kopyalayın, Düzenleyin, Çevirin veya Kaydedin *(`content` 2)* | *(4 internal link — chốt phân định)* |
| 12 | Sıkça Sorulan Sorular *(12 FAQ)* | long-tail + toàn bộ biến thể đã search |
| — | **conclusion:** YouTube Transkriptinizi Ücretsiz Alın *(3 đoạn)* | youtube transkript, ücretsiz |

**Cả 6 keyword đều có chỗ đứng:** `youtube transkript` (H1 + S1/S2/S3/S8/S10 + title + conclusion), `youtube transkript olusturma` (S4), `youtube den metin alma` + `youtube altyazi metin cikarma` (S5), `youtube video yazi haline getirme` (S6 intro), `youtube deşifre` (S7). ✅

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

- **S4 và S5 là hai section gộp intent** (generator + extractor). Bản EN cài chúng để một URL rank được cả ba cụm. Dịch sát, **không gộp hai section lại**, vì mỗi section giữ một họ keyword riêng của tiếng Thổ (`oluşturma` vs `metin alma / çıkarma`).
- **S7 giữ trọn `deşifre`** — đây là section duy nhất phủ cụm native `youtube deşifre` (10–100). Không thay `deşifre` bằng `transkript` trong H2 này.
- **S8 là section so sánh** với transkript panel tích hợp của YouTube — dịch sát, giữ **đúng 2 items**, không thêm vế thứ ba.
- **S11 chứa cả 4 internal link trong `content[1]`** — dịch sát cả 4 vế, không rút gọn, không bỏ vế nào. Đây là chỗ duy nhất `altyazı` (để trần, vai trò file) được dùng để trỏ sang trang phụ đề.
- **Xử lý `altyazı`:** kết quả trang **luôn** là `transkript` / `metin`. Khi bản EN nói `captions` (phụ đề người đăng / phụ đề tự động), dịch thành `altyazı` **có định ngữ** (`altyazısı olmayan`, `otomatik altyazılar`, `YouTube'un altyazıladığı`). `altyazı` để trần với vai trò "file phụ đề" chỉ ở **S11** và **FAQ 9**.
- **Kỷ luật `indir`:** chỉ đi với `transkript` / `altyazı` / `metin` / `TXT, DOCX, PDF, SRT, VTT`. **Không bao giờ** viết `videoyu indir`. Ở S3 bước 2 bản EN nói "no file to download first" → dịch giữ `dosya`, không dùng `video`.
- **Bẫy `indirger`:** không được để `indirgemek` (giản lược) lọt vào bản dịch — đã kiểm 0 kết quả.
- Xưng hô **`siz`** nhất quán (`yapıştırın`, `kopyalayın`, `düzenleyin`, `cihazınız`).
- Nhấn `ücretsiz` ở `title`, `hero.subtitle`, S1 đoạn cuối, FAQ 2 và `conclusion` — đúng vị trí bản EN.

---

## Không nên tối ưu cho các keyword

### 4 trang YouTube anh em

- **`youtube transkript indir` / `youtube transkript indirme`** → **`/tr/download-youtube-transcript`** (trọng tâm là **tải file** TXT/DOCX/PDF/SRT). Trang này chỉ nhắc ở S11.
- **`youtube altyazı indir` / `youtube altyazı indirici` / `srt altyazı youtube`** → **`/tr/youtube-subtitle-downloader`** (file phụ đề khớp giờ, dành cho editor). Nhóm `altyazı` để trần thuộc trọn về trang đó.
- **`youtube video metne çevirme` / `youtube video yazıya çevirme`**: giữ ở hub này — không còn trang riêng cho cách gọi "video metne çevirme".
- **`youtube video özetleme` / `youtube özet` / `video özetleyici`** → **`/tr/youtube-video-summarizer`** (chỉ ý chính, không phải toàn văn).

### Nhóm intent tải VIDEO — cannibalization nguy hiểm nhất

- **`youtube video indir` / `youtube mp4 indir` / `youtube indirme` (đứng trần)** → **intent tải file video**, SERP toàn downloader MP4. Trang này **không tải video**, chỉ ra chữ. Quy tắc `indir` đã nêu ở mục riêng.

### Sai intent hoàn toàn

- **`texttomp3` và mọi cụm TTS** (`metni sese çevirme`, `sesli okuma`) → **intent NGƯỢC**: biến chữ thành giọng nói. Trang này biến giọng nói thành chữ. (Không xuất hiện trong danh sách tr — đã kiểm.)
- **`youtube'da altyazı açma` / `youtube altyazı ayarları`** → hướng dẫn bật nút CC trong app YouTube, không phải công cụ.

---

## Internal linking

**Section 11, `content[1]`** chứa **cả 4 link**. Thứ tự và vai trò (khớp `tr.json`):

| Link | Anchor (tr) | Khi nào người dùng cần |
| ---- | ----------- | ---------------------- |
| `/tr/download-youtube-transcript` | YouTube Transkript İndirme | Mục tiêu chính là **tải file** TXT/DOCX/PDF/SRT |
| `/tr/youtube-subtitle-downloader` | YouTube Altyazı İndirici | Cần đúng **file phụ đề** SRT/VTT khớp giờ |
| `/tr/youtube-video-summarizer` | YouTube Video Özetleyici | Chỉ cần **ý chính**, không cần toàn văn |

Trang trụ link xuống cả 4 trang con; cả 4 trang con link ngược về đây. Đã kiểm: đủ 4 path, đúng prefix `/tr/`. ✅

---

## Ghi chú kỹ thuật cho tr.json

- Cấu trúc **1:1 với `en.json`**:
  `seo` 7 khóa · `hero` 4 khóa · `quickAnswer` 2 khóa · **12 section** ·
  S1 `content` **3** · S2 `specs` **10** · S3 `steps` **4** · S4 `content` **3** · S5 `content` **2** ·
  S6 `intro` **1** + `items` **6** · S7 `content` **2** · S8 `intro` **1** + `items` **2** ·
  S9 `content` **3** · S10 `intro` **1** + `items` **5** · S11 `content` **2** · S12 `items` **12** ·
  `conclusion.content` **3**.
- Giữ nguyên Latin, **không dịch**: `TranscriptX`, `YouTube`, `TXT`, `DOCX`, `PDF`, `SRT`, `VTT`, `Word`, `Google Docs`, `Pages`, `ChatGPT`, `Claude`, `Gemini`.
- Internal link ở S11 giữ **cú pháp markdown** `[anchor](/tr/...)`, path prefix `/tr/`.
- Thuật ngữ nhất quán: `transkript` (transcript), `deşifre` (transcription — native, chỉ S7), `metin` (text), `altyazı` (caption/subtitle — có định ngữ), `zaman damgası` (timestamp), `konuşmacı ayrımı` (speaker separation), `dosya` (file), `bağlantı` / `enlace→bağlantı` (link), `tarayıcı` (browser), `üyelik yok` (no sign-up), `otomatik olarak algılanır` (auto-detected).
- Xưng hô **`siz`** (mệnh lệnh số nhiều/lịch sự) — nhất quán toàn trang.
- `hero.placeholder` (`YouTube video bağlantısını yapıştırın...`) và `hero.button` (`Transkript Al`) ngắn gọn.
- **Kiểm tra trước khi bàn giao:**
  1. `python3 shape_check.py en.json tr.json` → phải in `tr.json -> True`.
  2. `grep -oE 'video[^.]{0,30}indir|indir[^.]{0,30}video' tr.json` → **0 kết quả**. ✅ (đã kiểm)
  3. `grep -c 'indirge\|indirger' tr.json` → **0**. ✅ (đã kiểm)
  4. `grep -c 'texttomp3' tr.json` → **0**. ✅ (đã kiểm)
  5. 4 path internal link đúng `/tr/` prefix, đủ 4, không thừa không thiếu. ✅ (đã kiểm)
