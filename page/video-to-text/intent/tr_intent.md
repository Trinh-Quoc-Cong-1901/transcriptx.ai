🔥 TranscriptX – Video to Text (Turkish / tr)

URL:
/tr/video-to-text

Intent chính:

video yazıya çevirme — ücretsiz online, dosya yükleyerek

Trang này là **trang trụ (hub)** cụm Video to Text bản tiếng Thổ Nhĩ Kỳ. Nhắm đến người dùng Thổ đã **có sẵn file video trong máy** (MP4, MOV, AVI, MKV, WebM, bản ghi Zoom/Teams/Meet, screen recording, footage máy quay) và muốn lấy **lời nói bên trong video** ra thành văn bản để đọc, tìm kiếm, trích dẫn, làm biên bản hoặc làm phụ đề.

Gộp toàn bộ intent đồng nghĩa **yazıya çevirme / metne çevirme / metne dönüştürme / deşifre / metin çıkarma / yazıya dökme** vì tất cả cho ra **cùng một kết quả**: file video → văn bản.

> ⚠️ **Phân định với `/tr/audio-to-text`: LOẠI FILE.** Trang này nhận **video dosyası** (MP4, MOV, AVI, MKV, WebM); trang kia nhận **ses dosyası** (MP3, WAV, M4A...). Kiểm tra dữ liệu: **0 keyword trùng nhau** giữa hai danh sách TR — mọi keyword của trang này đều bắt đầu bằng `video` / `videoyu` / `videodan` / `videodaki` / `mp4`, còn trang kia bằng `ses` / `sesi` / `mp3`. Người dùng Thổ tự tách rất sạch, không cần chèn thêm câu phân định. Chốt chặn duy nhất nằm ở **section 10 đoạn 3** (link sang `/tr/audio-to-text`).

> ⚠️ **Phân định với các trang nền tảng: FILE vs LINK.** Trang này để **dosya yükleme** (tải file lên từ máy); các trang `/tr/youtube-transcript`, `/tr/tiktok-transcript`, `/tr/instagram-transcript` để **bağlantı yapıştırma** (dán link). Cùng ở **section 10 đoạn 3** có link sang cả ba. Tổng cộng **4 internal link** — nhiều nhất trong các trang đã làm.

> 🚨 **Rủi ro `indirme` — quy tắc cứng của bản tiếng Thổ.**
> Trong tiếng Thổ, `video indirme` đứng trần **mặc định được hiểu là TẢI VIDEO VỀ MÁY** (intent video downloader, hoàn toàn khác trang này). Nếu để `indir` / `indirme` đứng cạnh `video`, Google sẽ đọc trang là công cụ tải video.
> - `indir` / `indirme` **chỉ** được đi với `transkript` / `metin` / `dosya` / tên định dạng (`TXT, DOCX, PDF, SRT, VTT olarak indirin`).
> - **KHÔNG BAO GIỜ** viết `video indir`, `videoyu indirin`, `video indirme`, kể cả khi bản EN dùng "download".
> - Khi bản EN nói về nạp file lên → luôn dùng **`yükleme` / `yükleyin`**.
> - Ba chỗ bản EN dùng "download" theo nghĩa khác đã được viết lại: S3 bước 4 (giữ `indirin` vì đi với định dạng TXT/DOCX/…), S4 đoạn 3 ("nothing to download" → `kurulacak bir şey ... yoktur`), quickAnswer ("nothing to download onto your device" → `kurmanıza gerek kalmaz`). S6 (MP4, AVI/MKV) và S7 item 6 bản EN nhắc "downloads / downloaded video" → dịch thành `paylaşılan` / `arşivlenmiş` / `saklanan`, tuyệt đối không dùng `indirilen video`.

> 🚨 **Rủi ro OCR — chốt nguồn là ÂM THANH.**
> Keyword `videodan metin çıkarma` (100–1K) đọc mộc trong tiếng Thổ có thể hiểu là **trích chữ hiển thị trên màn hình (OCR)** — một intent hoàn toàn khác. Trang này lấy **videodaki konuşma** (lời nói).
> - Dữ liệu may mắn có sẵn cụm chốt: **`videodaki sesi yazıya çevirme` (100–1K)** — nói rõ nguồn là **ses của video**.
> - Cụm này được dùng ở **section 5** và **section 8** để khóa ngữ nghĩa "nguồn = âm thanh", đúng như cách bản `es` dùng nhóm `audio de video` / `voz de video`.
> - `videodan metin çıkarma` chỉ được đặt ở **FAQ 9** (vị trí đã có ngữ cảnh "konuşma" bao quanh), không đặt ở H1/H2/title.

> ⚠️ **`altyazı` (phụ đề) bị giới hạn phạm vi.** Kết quả của trang này luôn được gọi là `transkript` / `metin`, KHÔNG gọi là `altyazı`. Từ `altyazı` chỉ xuất hiện ở **section 10 đoạn 2** và **FAQ 8** — đúng chỗ nói về xuất **SRT/VTT**. Lý do: `altyazı` kéo về intent "video'ya altyazı ekleme" (gắn phụ đề vào video), trang này không làm việc đó.

> ⚠️ **Lỗi dữ liệu trong `2_loc_kw.md`, mục `## Turkish (tr)`.**
> - **Không có** dòng rác `Keyword ideas` hay `Keywords you provided` trong khối TR (khác các khối de / es / fr / vi vốn bị nhiễm).
> - **Không có** keyword trùng lặp (khác khối es có `desgrabador video online` lặp 2 lần).
> - Số keyword thực: **14** — đúng bằng số dòng đếm thô. Khối dữ liệu TR sạch.
> - Chính tả dấu trong nguồn đã kiểm từng dòng: `yazıya` (`ı` không chấm), `çevirme`, `dönüştürme`, `deşifre`, `videodaki`, `çıkarma`, `ücretsiz`, `dökme` — tất cả đều đúng, dùng nguyên văn được.
> - Cảnh báo volume: **2 keyword ở band `0 – 10`** (`video yazıya çevirme ücretsiz`, `video yazıya çevirme programı`) là nhiễu — chỉ rải body, không hy sinh title/H1 cho chúng.

---

## Từ khóa chính

**video yazıya çevirme** (1K – 10K) ✅ *đã search*

Lý do chọn: band cao nhất, ngắn nhất, là **lõi chung** mà 3 keyword khác mở rộng từ nó (`... ücretsiz`, `... programı`, `videodan ...`), và đúng intent hub nhất — không khóa vào một định dạng hay một nền tảng nào. Đặt ở `hero.h1`, `seo.title`, H2 section 1.

## Từ khóa đồng hạng

**videoyu metne çevirme** (1K – 10K) ✅ *đã search*

Cùng band với KW chính. Đây là **biến thể song song bắt buộc phủ** — giống hệt tình huống `yazıya çevirme` vs `metne çevirme` ở `/tr/audio-to-text`: `yazıya çevirme` là cụm phổ thông, `metne çevirme` là cụm kỹ thuật hơn, cả hai đều có volume thật. Không được chọn một bỏ một. Đặt nguyên văn ở `seo.description` và H2 section 5.

---

## Từ khóa phụ

### Nhóm `yazıya çevirme` (trục phổ thông — trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video yazıya çevirme | 1K – 10K | ✅ đã search *(KW chính)* |
| videodan yazıya çevirme | 10 – 100 | ✅ đã search |
| videodaki sesi yazıya çevirme | 100 – 1K | ✅ đã search *(cụm chốt chống OCR)* |
| mp4 yazıya çevirme | 10 – 100 | ✅ đã search |
| video yazıya dökme | 10 – 100 | ✅ đã search |
| video yazıya çevirme ücretsiz | 0 – 10 ⚠️ *rất thấp* | ✅ đã search |
| video yazıya çevirme programı | 0 – 10 ⚠️ *rất thấp* | ✅ đã search |

### Nhóm `metne çevirme` / `metne dönüştürme` (trục kỹ thuật — phải phủ song song)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| videoyu metne çevirme | 1K – 10K | ✅ đã search *(KW đồng hạng)* |
| video metne dönüştürme | 100 – 1K | ✅ đã search |
| video metne çevirme ücretsiz | 100 – 1K | ✅ đã search |
| videoyu metne çevirme online | 10 – 100 | ✅ đã search |

### Nhóm `deşifre` / `transkript` (thuật ngữ nghề)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video deşifre | 10 – 100 | ✅ đã search |
| video transkript | 100 – 1K | ✅ đã search |

### Nhóm `çıkarma` (trích xuất — cẩn thận OCR)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| videodan metin çıkarma | 100 – 1K | ✅ đã search ⚠️ *chỉ dùng ở FAQ 9, phải có ngữ cảnh `konuşma` bao quanh* |

### Dịch bổ sung (chỉ rải body, KHÔNG đặt title/H1/H2)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| video deşifre metni | — | 🔄 dịch bổ sung (video transcript) |
| toplantı kaydını yazıya çevirme | — | 🔄 dịch bổ sung (transcribe meeting recording) |
| ekran kaydını yazıya çevirme | — | 🔄 dịch bổ sung (transcribe screen recording) |
| webinar deşifre | — | 🔄 dịch bổ sung (transcribe webinar) |
| ders kaydını metne çevirme | — | 🔄 dịch bổ sung (transcribe lecture) |
| video metne çevirme aracı | — | 🔄 dịch bổ sung (video to text tool) |

**Nguyên tắc dùng:**
- ✅ *đã search* = ưu tiên tuyệt đối, được phép đặt ở `title` / `h1` / `h2` / `description`.
- ⚠️ *0 – 10* = đã search nhưng volume gần 0 → **chỉ rải body**, không hy sinh câu chữ.
- 🔄 *dịch bổ sung* = chưa có dữ liệu volume, **chỉ rải body** để phủ ngữ nghĩa.

---

## Search Intent

Người dùng Thổ **đã có file video trong tay** — bản ghi Zoom/Teams/Meet, screen recording bài hướng dẫn, webinar, ders kaydı, footage phỏng vấn quay bằng máy quay hoặc điện thoại — và muốn lấy phần lời nói ra thành chữ.

Họ kỳ vọng:

- **Tải file lên là chạy** (`yükle`), không cài phần mềm — dù họ vẫn gõ từ `program`.
- **Không giới hạn dung lượng / thời lượng** — bản ghi họp 2–3 tiếng là chuyện thường.
- Hỗ trợ nhiều định dạng: MP4, MOV, AVI, MKV, WebM.
- Phân biệt được **nhiều người nói** (quan trọng nhất với toplantı / röportaj).
- **Hỗ trợ tốt tiếng Thổ** — mối lo cố hữu của thị trường TR, nhiều công cụ chỉ chạy tốt tiếng Anh.
- **Ücretsiz thật** — `ücretsiz` xuất hiện trong 2 keyword.
- Xuất được nhiều định dạng, đặc biệt **DOCX** để làm tài liệu và **SRT** để làm phụ đề.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Thổ search bằng CỤM ĐỘNG TỪ, không phải danh từ.** Bản EN có danh từ head cực mạnh: `video to text`, `video transcriber`, `video transcript generator`. Tiếng Thổ **không có một danh từ head nào có volume** — toàn bộ 14 keyword đều là cụm danh động từ (`-me` / `-ma`): `çevirme`, `dönüştürme`, `dökme`, `çıkarma`. Hệ quả: H1 và mọi H2 phải là **hành động** (`Video Yazıya Çevirme`), không được dịch danh từ hóa kiểu `Video Metin Dönüştürücü`. Đây là khác biệt cấu trúc lớn nhất so với bản EN/ES.
2. **Hai biến thể song song `yazıya` vs `metne`, volume ngang nhau (1K–10K).** Bản EN chỉ có một cụm `video to text`. Bản dịch phải luân phiên cả hai một cách tự nhiên theo section, không được chỉ dùng một.
3. **`deşifre` là intent nghề nghiệp độc lập, không phải từ đồng nghĩa phụ.** Dịch vụ deşifre là một ngành có thật ở TR (thư ký, pháp lý, báo chí). Bản EN không có tương đương — chỗ bản EN nói "transcribe accurately" thì bản TR lấy `deşifre` làm trục H2 section 5.
4. **Rủi ro `indirme` không tồn tại trong bản EN.** "Download the transcript" trong tiếng Anh không hề mơ hồ; `video indirme` trong tiếng Thổ thì mơ hồ nghiêm trọng (cả một ngành video downloader chiếm SERP). Phải xử lý riêng — xem mục 🚨 ở trên.
5. **Rủi ro OCR cũng không tồn tại rõ ở bản EN.** "Extract text from video" tiếng Anh thường vẫn hiểu là transcript; `videodan metin çıkarma` tiếng Thổ dễ trượt sang OCR hơn. Cụm `videodaki sesi yazıya çevirme` là công cụ chốt.
6. **Volume tổng thể thấp hơn nhiều so với EN/ES/PT.** Band cao nhất của TR là 1K–10K, trong khi ES đạt 10K–100K. Chiến lược: **phủ rộng long-tail** thay vì dồn lực vào một head keyword.

---

## Đối tượng người dùng

- Nhân viên văn phòng, trợ lý (toplantı kaydı — bản ghi Zoom/Teams/Meet → tutanak)
- Nhà báo, phóng viên (röportaj quay hình → bóc băng)
- Giáo viên, sinh viên (ders kaydı, bài giảng ghi hình)
- Người làm khóa học online, tài liệu nội bộ (ekran kaydı → dokümantasyon)
- Người làm dịch vụ **deşifre** chuyên nghiệp (ngành có sẵn ở TR)
- Luật sư, ngành pháp lý (bản ghi phiên họp cần văn bản chính thức)
- Content creator, marketer (webinar → bài viết, altyazı)
- Người cần đưa nội dung video vào ChatGPT / Claude / Gemini

---

## Map H2 → keyword (bám ĐÚNG 11 section)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **11 section**, cùng số đoạn `content`, đúng **10 `specs`**, đúng **4 `steps`**, section 6 = `intro` 1 + `items` 4, section 7 = `intro` 1 + `items` 6, đúng **10 FAQ** (khác `/tr/audio-to-text` vốn có 11). Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu.

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Video Yazıya Çevirme | video yazıya çevirme *(KW chính)* |
| — | **quickAnswer** | video yazıya çevirme, video transkript |
| 1 | Video Yazıya Çevirme Nedir? | video yazıya çevirme, video transkript, video yazıya dökme |
| 2 | Bir Bakışta Video Yazıya Çevirme | *(bảng 10 thông số — ücretsiz / sınırsız / 100+ dil)* |
| 3 | Video Dosyasını Yazıya Çevirme Nasıl Yapılır? | videodan yazıya çevirme, video dosyası yükleme |
| 4 | Ücretsiz Video Metne Çevirme Aracı | video metne çevirme ücretsiz, video yazıya çevirme programı, videoyu metne çevirme online, video yazıya çevirme ücretsiz |
| 5 | Videoyu Metne Çevirme ve Video Deşifre | **videoyu metne çevirme**, video deşifre, videodaki sesi yazıya çevirme |
| 6 | Desteklenen Video Formatları | mp4 yazıya çevirme *(MP4, MOV, AVI, MKV, WebM)* |
| 7 | Neleri Yazıya Çevirebilirsiniz | toplantı kaydını yazıya çevirme, ekran kaydını yazıya çevirme, webinar deşifre, ders kaydını metne çevirme |
| 8 | Video Yazıya Çevirme Ne Kadar Doğru? | videodaki sesi yazıya çevirme *(chốt nguồn = âm thanh)* |
| 9 | 100'den Fazla Dilde Video Metne Dönüştürme | video metne dönüştürme *(+ nhấn tiếng Thổ)* |
| 10 | Metninizi Beş Formatta Dışa Aktarın | *(altyazı SRT/VTT + **4 internal link**: /tr/audio-to-text, /tr/youtube-transcript, /tr/tiktok-transcript, /tr/instagram-transcript)* |
| 11 | Sıkça Sorulan Sorular | video yazıya çevirme ücretsiz, videodan metin çıkarma, videoyu metne çevirme online, mp4 yazıya çevirme + long-tail |
| — | **conclusion** | video yazıya çevirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

1. **Phủ hai biến thể theo section.** Section 1, 3, 7, 8 chạy trục `yazıya çevirme`; section 4, 5, 9 chạy trục `metne çevirme` / `metne dönüştürme`. Cách chia này phủ đủ cả hai band 1K–10K mà không cần thêm section nào.
2. **`video yazıya çevirme programı` và `videoyu metne çevirme online`** (volume thấp) được chèn vào **section 4** bằng cách dịch câu "Plenty of video transcribers let you upload..." theo hướng nói về `program` và `online araç` — cách người Thổ thực sự gọi công cụ web. Không thêm câu.
3. **`video yazıya dökme`** đặt ở **section 1 đoạn 1** — chỗ bản EN mô tả hành động "typing what you hear", đúng sắc thái "chép ra giấy" của `dökme`.
4. **`videodaki sesi yazıya çevirme`** dùng **đúng 2 lần**: section 5 đoạn 2 và section 8 đoạn 2. Đây là hai chỗ bản EN nói về việc rút audio ra và về chất lượng thu âm — ngữ cảnh tự nhiên nhất để chốt nguồn là âm thanh, đồng thời chống nhiễm OCR.
5. **Nỗi lo tiếng Thổ** xử lý **trong section 9**, thay ví dụ ngôn ngữ của bản EN (German / Vietnamese) bằng ví dụ có tiếng Thổ — giữ nguyên số câu.
6. **`transkript`** dùng làm danh từ chỉ kết quả xuyên suốt (thay cho `transcript` của bản EN), qua đó phủ KW `video transkript` một cách tự nhiên mà không cần câu riêng.
7. **Section 3 bước 1** bản EN có "or paste a link to the video" — giữ nguyên 1 mệnh đề, nhưng KHÔNG mở rộng thành đoạn, vì trục của trang này là `dosya yükleme`; phần link thuộc các trang nền tảng.

---

## Không nên tối ưu cho các keyword

- `ses yazıya çevirme` / `ses metne çevirme` / `ses kaydını yazıya çevirme` / `mp3 yazıya çevirme` / `ses deşifre` → **/tr/audio-to-text** (file âm thanh). Dữ liệu đã tự tách sạch (0 keyword trùng), chỉ cần không chủ động kéo về.
- `youtube video yazıya çevirme` / `tiktok video yazıya çevirme` / `instagram video yazıya çevirme` → **các trang nền tảng riêng** (dán link, không upload file).
- 🚨 **`video indirme` / `video indirici` / `mp4 indirme` / `videoyu mp3 yapma`** → **intent xử lý/tải FILE video**, không phải lấy chữ. Quy tắc cứng: `indir` / `indirme` chỉ đi với `transkript` / `metin` / `dosya` / tên định dạng, **không bao giờ** với `video`.
- 🚨 **`görüntüden metin okuma` / `resimden yazı çıkarma` / `OCR`** → **intent đọc chữ TRÊN màn hình**, khác hẳn. Trang này lấy **videodaki konuşma**. Cụm `videodaki sesi yazıya çevirme` ở S5/S8 là chốt phân định.
- `videoya altyazı ekleme` / `altyazı yapma` → intent **gắn** phụ đề vào video; trang này chỉ **xuất** file SRT/VTT (section 10 + FAQ 8), không gắn hộ. `altyazı` vì thế bị giới hạn đúng 2 chỗ đó.
- `metni sese çevirme` / `yazıyı sese dönüştürme` → **ngược intent (TTS)**.

---

## Internal linking

Section 10 đoạn 3 chứa **cả 4 link**:

- → `/tr/audio-to-text` — khi nguồn là **ses dosyası** thay vì video dosyası *(phân định LOẠI FILE)*
- → `/tr/youtube-transcript` — khi video nằm trên YouTube, **bağlantı yapıştırma** thay vì yükleme
- → `/tr/tiktok-transcript` — như trên, TikTok
- → `/tr/instagram-transcript` — như trên, Instagram

Ba link sau cùng đóng vai trò **phân định FILE vs LINK** trong một câu duy nhất.

---

## Ghi chú kỹ thuật cho tr.json

- `lang="tr"`, `dir="ltr"`.
- **Ký tự tiếng Thổ phải chuẩn 100%:** `ı` (i không chấm), `İ` (I có chấm), `ş`, `ğ`, `ç`, `ö`, `ü`. Đặc biệt `İ` viết hoa đầu câu/đầu tiêu đề (`İnceleyin`, `İsimleri`, `İki`) — **KHÔNG** dùng `I`. Và `yazıya` luôn là `ı`, không phải `i`.
- Xưng hô **"siz"** (`yükleyin`, `dışa aktarın`, `ihtiyacınız`) — nhất quán với `/tr/audio-to-text`.
- Hậu tố cách sau tên riêng / số Latin dùng dấu nháy đơn: `TranscriptX'e`, `MP4'ü`, `ChatGPT'ye`, `100'den`, `Zoom'da`.
- **Nhãn `specs` copy Y NGUYÊN 10 chuỗi từ `/tr/audio-to-text/tr.json`** — không tự dịch lại: `Ücret` / `Hesap gerekli mi` / `Kurulum` / `Dosya boyutu sınırı` / `Kabul edilen formatlar` / `Diller` / `Konuşmacı ayrımı` / `Zaman damgaları` / `Dışa aktarma formatları` / `Cihazlar`. Chỉ đổi **giá trị** của `Kabul edilen formatlar` sang định dạng video (`MP4, MOV, AVI, MKV, WebM ve daha fazlası`).
- Giữ nguyên Latin, không dịch, không thêm dấu: **MP4, MOV, AVI, MKV, WebM, TXT, DOCX, PDF, SRT, VTT** và thương hiệu **TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, Zoom, Teams, Meet, QuickTime, iPhone, iPad, YouTube, TikTok, Instagram**.
- Cấu trúc: **11 section**, **10 `specs`**, **4 `steps`**, S6 = `intro` 1 + `items` 4, S7 = `intro` 1 + `items` 6, **10 FAQ**, `conclusion.content` 2 đoạn.
- Internal link ở `sections[9]` giữ cú pháp markdown: `[Ses Yazıya Çevirme](/tr/audio-to-text)`, `[YouTube Transkript](/tr/youtube-transcript)`, `[TikTok Transkript](/tr/tiktok-transcript)`, `[Instagram Transkript](/tr/instagram-transcript)`.
- Số đếm dùng chữ số Latin (100+, 5).
- **Kiểm tra cuối trước khi giao:** grep chuỗi `video indir`, `videoyu indir`, `video indirme` phải trả về **0 kết quả**.
