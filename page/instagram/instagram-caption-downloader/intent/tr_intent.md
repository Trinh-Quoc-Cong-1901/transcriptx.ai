🔥 TranscriptX – Instagram Caption Downloader (Turkish / tr)

URL:
/tr/instagram-caption-downloader

Intent chính:

Instagram açıklama indirme — gönderi açıklamasını ücretsiz indirme ve kopyalama

Trang này là **bản tiếng Thổ Nhĩ Kỳ** của trang Instagram Caption Downloader. Nhắm đến người dùng Thổ muốn lấy **açıklama** (phần mô tả do tác giả GÕ dưới bài đăng — chữ, hashtag, emoji, ngắt dòng) từ Instagram Gönderi, Reel hoặc Video — để sao chép, lưu, dịch, phân tích hoặc tái sử dụng.

Gộp toàn bộ intent đồng nghĩa **indirme / kopyalama / kaydetme / çıkarma** vì tất cả cho ra **cùng một kết quả**: açıklama Instagram → metin.

> ⚠️ **PHÂN ĐỊNH INTENT SỐNG CÒN: Açıklama ≠ Transkript.** Trang này lấy chữ tác giả **VIẾT** (açıklama, hashtag, emoji). Trang anh em `/tr/instagram-transcript` lấy chữ người ta **NÓI** trong video (seslendirme, konuşma). Section 2 của `en.json` tồn tại chính để phân định điều này — bản `tr` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau.

> ⚠️ **LỖI DỮ LIỆU trong `2_loc_kw.md` — keyword nguồn gõ THIẾU DẤU.** Section `## Turkish (tr)` có 12 keyword, tất cả band `0 – 10`, nhưng phần lớn bị mất dấu tiếng Thổ:
> - `acıklama` → chính tả đúng là **`açıklama`** (thiếu `ç`; nghịch lý là `ı` thì lại có, chứng tỏ đây là lỗi gõ chứ không phải biến thể)
> - `gonderi` → **`gönderi`** (thiếu `ö`)
> - `cıkarma` → **`çıkarma`** (thiếu `ç`)
> - `kopyalama`, `kaydetme`, `indirme`, `yazısı`, `linkten` → **đã đúng chính tả**, không cần sửa
>
> Đây là hệ quả thói quen gõ nhanh bàn phím mobile/ASCII của người Thổ, **không phải hai keyword khác nhau**.
>
> **Chiến lược xử lý:** trong intent này keyword luôn ghi ở **dạng đúng chính tả**. Trong `tr.json` viết **ĐÚNG DẤU 100%** — `açıklama`, `gönderi`, `çıkarma`, `ücretsiz`, `yapıştırın`, `İndirin`. Title / H1 / H2 / description **bắt buộc** dùng dạng có dấu chuẩn. **KHÔNG** cố tình nhét dạng không dấu (`acıklama`, `gonderi`, `cıkarma`) vào body: Google Thổ **chuẩn hóa dấu** (`acıklama` ≡ `açıklama`) nên cả hai dạng cùng khớp một truy vấn, trong khi viết sai dấu sẽ làm trang trông cẩu thả và hạ chất lượng cảm nhận. Khác hẳn bản `ar` (nơi biến thể hamza **phải** xuất hiện thật trong body).
>
> Lưu ý phụ: `ı` (i không chấm) và `İ` (I có chấm) là **hai chữ cái khác nhau**. Đầu câu phải viết `İndirin`, `İsterseniz`, `İçerik` — KHÔNG dùng `I`.

> ⚠️ **HAI TRỤC SONG SONG: `açıklama` (thuần Thổ) vs `caption` (mượn Anh).**
> - **`açıklama`** xuất hiện trong **9/12** keyword — trục áp đảo, là cách người Thổ thật sự gọi phần chữ dưới bài đăng.
> - **`caption`** chỉ có **2/12** (`instagram caption indir`, `instagram caption indirme`) — cách nói của giới creator/sosyal medya uzmanı quen thuật ngữ Anh.
> - **`yazı`** là trục thứ ba mỏng nhất, **1/12** (`instagram gönderi yazısı indirme`).
>
> **Phân bổ:** `açıklama` giữ **H1 + title + đa số H2**. `caption` **không được lên H1** (sẽ mất keyword chính) nhưng phải có mặt trong **tên công cụ ở H2 section 1** và **FAQ** để bắt nhóm creator. `yazı` rải body ở section 1 và section 4.

> ⚠️ **H1 GIỮ KHUNG `indirme` (đã chốt với người dùng).** Nhóm `kopyalama` đưa xuống **H2 section 5 + body**, giống hệt cách bản `de` dồn `text kopieren` vào section 5. Lý do: `indirme` khớp URL, khớp tên page type, và chiếm 9/12 keyword; `kopyalama` chỉ có 1 keyword riêng nên không đủ trọng số để đổi khung H1.

> ⛔ **CẢNH BÁO SAI LẦM ĐÃ XẢY RA:** "giữ khung `indirme`" **KHÔNG** có nghĩa là giữ nguyên tên tiếng Anh `Instagram Caption Downloader` làm H1. H1 để nguyên tiếng Anh sẽ bắt được **0 keyword đã search**. H1 đúng là **`Instagram Açıklama İndirme`** — trùng khít keyword chính. Đối chiếu bản `de`: H1 = `Instagram Caption herunterladen`, không phải `Instagram Caption Downloader`. Tên tiếng Anh chỉ được dùng làm **tên công cụ trong H2 section 1**, nơi bản EN vốn đã đặt tên tool.

---

## Từ khóa chính

**instagram açıklama indirme** (0–10) ✅ *đã search* *(nguồn ghi `instagram acıklama indirme`)*

Lý do chọn: là cụm ngắn nhất, đúng page type nhất, và là **gốc mở rộng của 5 keyword khác** trong danh sách (`gönderi açıklaması indirme`, `video açıklaması indirme`, `reels açıklaması indirme`, `linkten açıklama indirme`, `açıklama indir online`) — tức chi phối 6/12 danh sách. Trùng khít cấu trúc URL `/tr/instagram-caption-downloader`.

---

## Từ khóa phụ

### Nhóm İndirme / İndir (trục chính — khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram açıklama indirme | 0–10 | ✅ đã search *(KW chính; nguồn ghi `acıklama`)* |
| instagram gönderi açıklaması indirme | 0–10 | ✅ đã search *(nguồn ghi `gonderi acıklaması`)* |
| instagram video açıklaması indirme | 0–10 | ✅ đã search *(nguồn ghi `acıklaması`)* |
| instagram reels açıklaması indirme | 0–10 | ✅ đã search *(nguồn ghi `acıklaması`)* |
| instagram linkten açıklama indirme | 0–10 | ✅ đã search *(nguồn ghi `acıklama`)* |
| instagram açıklama indir online | 0–10 | ✅ đã search *(nguồn ghi `acıklama`)* |
| instagram gönderi yazısı indirme | 0–10 | ✅ đã search *(nguồn ghi `gonderi`)* |
| instagram caption indir | 0–10 | ✅ đã search |
| instagram caption indirme | 0–10 | ✅ đã search |

### Nhóm Kopyalama (dồn vào section 5 — theo quyết định giữ H1 `indirme`)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram açıklama kopyalama | 0–10 | ✅ đã search *(nguồn ghi `acıklama`)* |
| instagram hashtag kopyalama | — | 🔄 dịch bổ sung (keep the hashtag set) |
| instagram gönderi metni kopyalama | — | 🔄 dịch bổ sung (copy post text) |

### Nhóm Kaydetme (lưu lại)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram açıklama kaydetme | 0–10 | ✅ đã search *(nguồn ghi `acıklama`)* |
| instagram reels açıklaması kaydetme | — | 🔄 dịch bổ sung (save a Reels caption) |

### Nhóm Çıkarma (trích xuất)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram açıklama metni çıkarma | 0–10 | ✅ đã search *(nguồn ghi `acıklama metni cıkarma`)* |
| instagram gönderisinden metin çıkarma | — | 🔄 dịch bổ sung (extract text from a post) |

### Dịch bổ sung (chỉ rải trong body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| instagram caption downloader | — | 🔄 dịch bổ sung (tên công cụ, giữ Latin) |
| instagram açıklama çevirme | — | 🔄 dịch bổ sung (translate a caption) |
| uygulamasız instagram açıklama indirme | — | 🔄 dịch bổ sung (no install) |
| ücretsiz instagram açıklama indirme | — | 🔄 dịch bổ sung (free) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải trong body, **không** đặt vào title/H1.

---

## Search Intent

Người dùng Thổ thấy một açıklama Instagram hay (của mình hoặc của đối thủ) và muốn lấy nguyên văn phần chữ đó ra ngoài app — vì Instagram **không có nút kopyala** cho açıklama, và bôi đen trên điện thoại thì rất khó, hay dính nhầm chỗ.

Họ thường kỳ vọng:

- Chỉ cần **linki yapıştırmak** — dán link, không đăng nhập, không cài uygulama.
- Lấy **nguyên vẹn** hashtag, emoji và ngắt dòng — không bị gộp thành một cục.
- Chạy được với gönderi ảnh, Carousel, Reel và video.
- **Ücretsiz thật**, chạy được trên điện thoại.
- Kopyalayıp başka yere yapıştırmak — copy được ngay để dán sang chỗ khác (Notlar, içerik dokümanı, planlama aracı).

### Khác biệt so với bản tiếng Anh

1. **Tiếng Thổ không có từ vay mượn thống trị như bản EN.** Bản EN xoay quanh một từ duy nhất `caption`. Bản TR có **hai trục song song**: `açıklama` (thuần Thổ, 9/12) và `caption` (mượn Anh, 2/12). Không được chọn một bỏ một — `açıklama` giữ H1/title, `caption` bắt buộc xuất hiện ở H2 section 1 (tên công cụ) và trong FAQ.

2. **`downloader` không dịch được thành danh từ tự nhiên.** Tiếng Anh có `caption downloader` như một danh từ page-type. Tiếng Thổ phải chuyển thành **danh động từ `indirme`** (`açıklama indirme`) hoặc thêm `aracı` (`açıklama indirme aracı`). Đây chính là lý do H1 là `Instagram Açıklama İndirme` chứ không phải một danh từ ghép kiểu Anh.

3. **`indirme` đứng trần cực kỳ nguy hiểm ở TR.** Ở EN, `download` + Instagram vẫn còn mơ hồ nhưng SERP phân tách được. Ở TR, `instagram indirme` mặc định hiểu là **tải video/Reels**, và nhóm keyword đó có volume lớn hơn hẳn cụm này. Quy tắc dịch bắt buộc: **mọi `indirme` phải có tân ngữ** `açıklama` / `caption` / `metin` / `yazı` — tuyệt đối không để `video indirme` xuất hiện.

4. **Vấn đề dấu là đặc thù riêng của TR.** Không ngôn ngữ nào khác trong cụm này có keyword nguồn bị mất dấu (`acıklama`, `gonderi`, `cıkarma`). Xử lý: viết đúng dấu 100%, dựa vào cơ chế chuẩn hóa dấu của Google Thổ (xem cảnh báo đầu file).

5. **Cấu trúc câu tiếng Thổ đảo ngược động từ.** Câu mệnh lệnh ngắn kiểu EN ("Paste it into TranscriptX") phải thành dạng `-in/-ın` lịch sự với động từ về cuối (`TranscriptX'e yapıştırın`). Hậu tố cách sau tên riêng Latin dùng dấu nháy đơn: `TranscriptX'e`, `Instagram'da`, `Reel'den`, `Carousel'de`.

---

## Đối tượng người dùng

- Sosyal medya uzmanı / dijital pazarlamacı (phân tích açıklama đối thủ)
- İçerik üreticisi Thổ (lưu swipe file các açıklama hiệu quả)
- Ajans çalışanı làm báo cáo nội dung cho khách
- Freelancer quản lý tài khoản Instagram của khách
- Người muốn dịch açıklama tiếng nước ngoài
- Người lưu lại açıklama trước khi gönderi bị sửa/xóa
- E-ticaret satıcısı tái sử dụng mô tả sản phẩm giữa các gönderi

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, đúng 2 đoạn `conclusion`. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1: Instagram Açıklama İndirme** | **instagram açıklama indirme** *(KW chính)* |
| — | **quickAnswer** | instagram gönderi açıklaması indirme, instagram linkten açıklama indirme |
| 1 | Instagram Caption Downloader Aracı Ne Yapar? | instagram caption indirme, instagram video açıklaması indirme, instagram gönderi yazısı indirme |
| 2 | Açıklama mı Transkript mi: Hangisi Gerekli? | *(phân định + internal link `/tr/instagram-transcript`)* |
| 3 | Instagram Açıklaması Nasıl İndirilir? | instagram açıklama indirme, instagram linkten açıklama indirme, instagram açıklama metni çıkarma |
| 4 | İndirdiğiniz Açıklama ile Neler Yapabilirsiniz | instagram açıklama kaydetme, instagram reels açıklaması indirme, instagram açıklama çevirme 🔄 |
| 5 | **Instagram Açıklama Kopyalama — Hashtag, Emoji ve Biçim Korunur** | **instagram açıklama kopyalama**, instagram hashtag kopyalama 🔄 |
| 6 | Sıkça Sorulan Sorular | instagram açıklama indir online, instagram caption indir, instagram gönderi açıklaması indirme + long-tail |
| — | **conclusion** | instagram açıklama indirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

1. **Phân bổ hai trục theo section.** Trục `açıklama` chạy xuyên H1, section 3, 4, 5, conclusion. Trục `caption` chỉ đóng ở **H2 section 1** (đúng chỗ bản EN đặt tên công cụ: "What the Instagram Caption Downloader Does") và **FAQ 1** — đủ để bắt 2 keyword `caption` mà không làm loãng trục chính.
2. **Section 5 là van xả cho toàn bộ nhóm `kopyalama`.** Bản EN section này vốn đã nói "what you copy reads the same as what was on the post" — nên đưa `Açıklama Kopyalama` lên H2 ở đây là **bám đúng nghĩa gốc**, không phải nhét keyword. Đây là cách xử lý y hệt bản `de` (section 5 = `Instagram Text kopieren`).
3. **Section 2 giữ nguyên vai trò phân định Açıklama/Transkript.** Link nội bộ đổi thành `[Instagram Transkript](/tr/instagram-transcript)`. Cặp h3 phải đối xứng rõ: `yazılan` (được VIẾT) vs `söylenen` (được NÓI).
4. **`instagram açıklama metni çıkarma`** đặt nguyên cụm vào **step 3 của section 3** (bản EN: "The caption is extracted") — đúng chỗ, không cần thêm câu.
5. **`instagram açıklama kaydetme`** đặt vào **item 2 của section 4** (bản EN: "Save a caption before it changes"), **`instagram reels açıklaması indirme`** đặt vào **item 5** (hashtag set, nơi nhắc Reels) — mỗi item ôm một keyword.
6. **`instagram gönderi yazısı indirme`** rải trong **section 1 đoạn 3**, không lên H2 vì `açıklama` tự nhiên hơn ở heading.
7. **`instagram açıklama indir online`** gom vào **FAQ 8** (bản EN: "Can I download several captions?") — đúng chỗ nói về dùng online không giới hạn.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này:

- `instagram transkript` / `instagram video deşifre` / `reels yazıya çevirme` / `instagram videosunu yazıya çevirme` → **/tr/instagram-transcript** (chữ **NÓI**, không phải chữ **VIẾT**)
- `youtube transkript` / `youtube video yazıya çevirme` → **/tr/youtube-transcript**
- `tiktok transkript` / `tiktok video yazıya çevirme` → **/tr/tiktok-transcript**
- ⛔ **`instagram video indirme` / `instagram video indir` / `reels indirme` / `instagram indirme programı` → intent TẢI VIDEO.** Đây là **nhóm nhiễm nguy hiểm nhất của bản TR**, nguy hiểm hơn hẳn bản `de`: trong tiếng Thổ `indirme` **đứng trần mặc định được hiểu là tải video**, và nhóm keyword đó có volume lớn hơn cụm này nhiều lần, SERP toàn downloader video. Kéo vào sẽ làm lệch hoàn toàn page type.
  **Quy tắc dịch bắt buộc:** mọi lần xuất hiện của `indirme` / `indir` / `indirin` phải có **tân ngữ rõ ràng** — `açıklama indirme`, `caption indirme`, `açıklama metnini indirin`, `gönderi yazısını indirme`. **Không bao giờ** viết `videoyu indirin` hay để `indirme` lơ lửng không tân ngữ.
- `instagram biyografi kopyalama` / `instagram yorum kopyalama` → tuy gần `açıklama kopyalama` nhưng khác đối tượng, không tối ưu riêng
- `instagram altyazı indirme` → intent phụ đề video, không phải açıklama
- `instagram caption fikirleri` / `instagram açıklama örnekleri` → intent **sáng tác** caption, ngược hẳn intent trích xuất

---

## Internal linking

- ↔ /tr/instagram-transcript (khi user muốn chữ **NÓI** trong Reel/video thay vì açıklama viết) — **link quan trọng nhất**, nằm ở section 2
- → /tr/youtube-transcript, /tr/tiktok-transcript (cross-cluster)

---

## Ghi chú kỹ thuật cho tr.json

- `lang="tr"`, `dir="ltr"`.
- **Ký tự tiếng Thổ phải chuẩn trong toàn bộ file:** `ı` / `i`, `İ` / `I`, `ş`, `ç`, `ğ`, `ö`, `ü`. Đầu câu viết `İndirin`, `İçerik`, `İsterseniz` — KHÔNG dùng `I`. Không được để lọt bất kỳ dạng không dấu nào (`acıklama`, `gonderi`, `cıkarma`, `ucretsiz`, `yapistirin`).
- Giữ nguyên Latin, không dịch, không thêm dấu: **TranscriptX, Instagram, Reel, Reels, Carousel, hashtag, emoji**.
- Xưng hô **"siz"** nhất quán toàn trang (`yapıştırın`, `kopyalayın`, `indirin`, `ihtiyacınız`) — trang trọng, đồng bộ với `/tr/facebook-transcript` và `/tr/audio-to-text`.
- Hậu tố cách sau tên riêng Latin dùng dấu nháy đơn: `TranscriptX'e`, `Instagram'da`, `Instagram'ın`, `Reel'den`, `Carousel'de`.
- Internal link section 2 giữ nguyên cú pháp markdown, đổi path: `[Instagram Transkript](/tr/instagram-transcript)`.
- Cấu trúc JSON khớp 100% với `en.json`: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**; section 1 `content` 3, section 2 `intro` 1 + `items` 2, section 3 `steps` 4, section 4 `intro` 1 + `items` 5, section 5 `content` 3, section 6 `items` **8** (q/a); `conclusion` h2 + 2 đoạn.
