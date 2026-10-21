🔥 TranscriptX – Instagram Caption Downloader (Malay / ms)

URL:
/ms/instagram-caption-downloader

Intent chính:

download caption Instagram percuma — salin caption, deskripsi, hashtag dan emoji jadi teks

Trang này là **bản tiếng Mã Lai** của trang Instagram Caption Downloader. Nhắm đến người dùng Malaysia / Brunei / Singapore muốn lấy **caption** (phần chữ tác giả GÕ dưới bài đăng: deskripsi, hashtag, emoji, ngắt dòng) từ Instagram Post, Reel hoặc Video — để salin, simpan, terjemah, phân tích hoặc dùng lại.

Gộp toàn bộ intent đồng nghĩa **download / salin / copy / dapatkan / simpan** vì tất cả cho ra **cùng một kết quả**: caption Instagram → teks.

---

> ⚠️ **PHÂN ĐỊNH INTENT SỐNG CÒN: Caption ≠ Transkrip.** Trang này lấy chữ tác giả **VIẾT** (caption, deskripsi, hashtag, emoji). Trang anh em `/ms/instagram-transcript` lấy chữ người ta **NÓI** trong video (suara, voiceover, apa yang diperkatakan). Section 2 của `en.json` tồn tại chính để phân định điều này — bản `ms` phải giữ nguyên vai trò đó, không được làm mờ ranh giới, nếu không hai trang sẽ ăn thịt lẫn nhau.

> 🚨 **CẢNH BÁO LỚN NHẤT CỦA TRANG NÀY — TRÙNG 6/7 KEYWORD VỚI BẢN `/id/instagram-caption-downloader`**
>
> Danh sách ms và id ở trang này **trùng đúng 6/7 keyword, chỉ khác 1 từ duy nhất** (`dapatkan caption instagram` của ms vs `ambil caption instagram` của id). Đây là mức trùng **cao hơn hẳn** trang Facebook Transcript (nơi hai list còn khác nhau ở `tukar/mengubah`, `percuma/gratis`, `penjana/generator`...). Nghĩa là: **không thể dựa vào keyword để tách hai trang** — phải tách bằng **từ vựng thân bài + bối cảnh ví dụ**.
>
> **Bảng chống trùng bắt buộc:**
>
> | Ý nghĩa | ✅ ms (dùng trong `ms.json`) | ❌ id (CẤM xuất hiện trong `ms.json`) |
> | ------- | --------------------------- | ------------------------------------ |
> | miễn phí | **percuma** | gratis |
> | lấy / nhận | **dapatkan** *(là KW ms đã search)* | ambil *(là KW id đã search)* |
> | chuyển đổi | **tukar** | mengubah / ubah |
> | giới từ "thành" | **kepada** | menjadi / jadi |
> | bộ tạo / công cụ tạo | **penjana** | generator |
> | tải xuống (văn xuôi) | **muat turun** *(luôn kèm tân ngữ caption/teks)* | unduh |
> | tải lên | **muat naik** | unggah |
> | tệp | **fail** | berkas |
> | có thể | **boleh** | bisa |
> | chỉ | **sahaja** | saja |
> | trực tuyến (văn xuôi) | **dalam talian** | daring |
> | hỗ trợ | **menyokong** | mendukung |
> | thiết bị | **peranti** | perangkat |
> | xem | **tengok / lihat** *(ưu tiên `tengok` khẩu ngữ MY)* | lihat |
> | ứng dụng | **aplikasi** *(ok cả hai)* — nhưng câu chứa nó phải có từ ms khác | — |
>
> ⚠️ Các từ **trùng không tránh được**: `caption`, `instagram`, `download`, `link`, `salin`, `simpan`, `copy`, `deskripsi`, `hashtag`, `emoji`, `reel`, `online`. Đây đều là từ vay mượn / KW đã search, bắt buộc phải dùng. **Nguyên tắc bù trừ: mỗi câu chứa một trong các từ trùng đó phải có ít nhất một từ đặc trưng ms** (`percuma`, `boleh`, `anda`, `fail`, `sahaja`, `dapatkan`, `dalam talian`, `tengok`, `pautan`, `tampal`).
>
> ⚠️ **Tách thêm bằng bối cảnh.** Bản ms dùng ví dụ Malaysia: kandungan usahawan/peniaga online Malaysia, kedai IG, caption dwibahasa Melayu–English (code-switching), kempen raya/promosi, pengurus media sosial agensi tempatan. Bản id sẽ dùng bối cảnh Indonesia — không được dùng ví dụ trùng.

> ⚠️ **Lưu ý dữ liệu keyword ms: CHỈ CÓ 7 KEYWORD.** Đây là list ngắn nhất trong các ngôn ngữ của trang này (de 11, fr 12, pt 12). Hệ quả trực tiếp:
>
> - **Tỉ lệ: 7 KW đã search / ~10 KW dịch bổ sung** → khoảng **41% đã search / 59% dịch bổ sung**. Đây là tỉ lệ dịch bổ sung **cao bất thường**, cao hơn hẳn bản de.
> - Vì vậy: **7 KW đã search phải phủ kín toàn bộ `seo.title` / `h1` / 6 `h2` / `description`**, không được để trống chỗ nào cho KW dịch bổ sung ở cấp heading.
> - Nhóm dịch bổ sung **chỉ được rải trong body** (`content`, `steps`, `items`, FAQ answers).
> - Vì chỉ 7 KW, **không nhồi** — mật độ KW chính giữ ~0.8–1.2%, ưu tiên văn phong tự nhiên.

> ⚠️ **HAI KW MẠNH NHẤT ĐỀU LÀ INTENT COPY, NHƯNG H1 VẪN GIỮ KHUNG DOWNLOAD.** `salin caption instagram` (100–1K) và `cara copy caption instagram` (100–1K) là hai KW duy nhất vượt band 10–100 — cả hai đều là intent **copy**. Nhưng theo quyết định đã chốt với người dùng: **H1 giữ khung `download`** để khớp bản EN + URL `/ms/instagram-caption-downloader`. Nhóm `salin` / `copy` được cấp hẳn **H2 section 5 + body** — giống hệt cách bản `de` xử lý `instagram text kopieren`.

> 🚫 **LỖI ĐÃ TỪNG XẢY RA — TUYỆT ĐỐI TRÁNH.** Một agent trước đã hiểu "giữ khung download" thành "giữ nguyên tên tiếng Anh", đặt H1 = `Instagram Caption Downloader` → **bắt được 0 keyword tiếng Mã Lai**. H1 đúng phải dùng **đúng dạng chữ của KW đã search**: `Download Caption Instagram` (rút từ `cara download caption instagram` + `download caption instagram dari link`). So sánh với bản `de`: H1 = `Instagram Caption herunterladen` — dùng động từ Đức đã search, **không** để nguyên `Instagram Caption Downloader`. Cụm `Instagram Caption Downloader` chỉ được xuất hiện ở `schemaName` (tên sản phẩm) và **H2 section 1** (đúng như bản de), **không bao giờ** ở `h1`.

---

## Từ khóa chính

**download caption instagram** (10–100) ✅ *đã search* — dạng đầy đủ đã search: `cara download caption instagram`

> Đây là KW download có volume cao nhất trong list ms, và là KW duy nhất khớp cả **page type** (downloader) lẫn **URL**. Toàn bộ `seo.title` / `h1` / `conclusion` xây quanh cụm này.

## Từ khóa mạnh nhất theo volume (dùng ở H2 section 5, KHÔNG ở H1)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| salin caption instagram | 100–1K | ✅ đã search |
| cara copy caption instagram | 100–1K | ✅ đã search |

> Cả hai đều gấp ~10× KW chính về volume, nhưng đều là intent **copy**. Xử lý: giữ H1 download, dồn hai cụm này vào **H2 section 5** (chỗ bản EN vốn nói về "what you copy reads the same as what was on the post" — nên đây là **bám đúng nghĩa gốc**, không phải nhét keyword) + rải trong steps 4 và FAQ.

---

## Từ khóa phụ

### Nhóm Download (trục chính, khớp H1 + URL)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| cara download caption instagram | 10–100 | ✅ đã search *(KW chính)* |
| download deskripsi instagram | 10–100 | ✅ đã search |
| download caption instagram dari link | 0–10 | ✅ đã search |
| download caption video instagram | — | 🔄 dịch bổ sung (Instagram video caption download) |
| download caption reel instagram | — | 🔄 dịch bổ sung (Reel caption download) |
| download caption instagram online | — | 🔄 dịch bổ sung (caption download online) |
| download caption instagram percuma | — | 🔄 dịch bổ sung (free — ghép modifier `percuma`) |

### Nhóm Salin / Copy (volume cao nhất — dồn vào section 5)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| salin caption instagram | 100–1K | ✅ đã search |
| cara copy caption instagram | 100–1K | ✅ đã search |
| salin deskripsi instagram | — | 🔄 dịch bổ sung (copy the description) |
| salin hashtag instagram | — | 🔄 dịch bổ sung (keep the hashtag set) |

### Nhóm Dapatkan / Simpan (lấy về & lưu lại)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| dapatkan caption instagram | 0–10 | ✅ đã search *(điểm phân định duy nhất với id — id dùng `ambil`)* |
| simpan caption instagram | 0–10 | ✅ đã search |
| dapatkan teks caption instagram | — | 🔄 dịch bổ sung (get the caption text) |
| simpan deskripsi post instagram | — | 🔄 dịch bổ sung (save a post description) |
| simpan caption reel instagram | — | 🔄 dịch bổ sung (save a Reel caption) |

**Nguyên tắc dùng:**

- ✅ *đã search* = ưu tiên tuyệt đối, **chỉ nhóm này mới được đặt vào** `seo.title` / `h1` / `h2` / `description`.
- 🔄 *dịch bổ sung* = **chỉ rải trong body** (`content`, `steps`, `items`, FAQ answers). **Tuyệt đối không** đặt vào title/H1/H2.
- Tỉ lệ tổng: **7 đã search / 10 dịch bổ sung**.

---

## Search Intent

Người dùng Mã Lai thấy một caption Instagram hay — của mình, của kedai lain, của pesaing, hoặc của một creator — và muốn lấy nguyên văn phần chữ đó ra ngoài app. Lý do: Instagram **tiada butang salin caption**, và bôi đen (highlight) trên telefon thì rất khó, hay dính nhầm chỗ hoặc cắt mất khối hashtag ở cuối.

Họ thường kỳ vọng:

- Chỉ cần **tampal pautan** bài đăng, không log masuk.
- Lấy **utuh** hashtag, emoji và ngắt dòng — không bị gộp thành một cục chữ.
- Chạy được với Post ảnh, Carousel, Reel và Video.
- **Percuma thật**, tanpa pemasangan aplikasi.
- **Salin ngay** để tampal sang chỗ khác (nota, Google Docs, alat penjadualan).
- Chạy tốt **trên telefon** — Malaysia là thị trường mobile-first, hầu hết mở Instagram trong app.

### Khác biệt so với bản tiếng Anh

1. **Intent `salin`/`copy` mạnh gấp ~10× intent `download`.** Bản EN đóng khung là "downloader" và cụm download có volume thật (`instagram caption downloader` 10K–100K). Bản ms thì ngược: hai KW copy chiếm band 100–1K, KW download mạnh nhất chỉ 10–100. Đã xử lý bằng cách giữ H1 download (khớp URL + page type) nhưng cấp hẳn H2 section 5 cho nhóm `salin`/`copy`.
2. **`cara ...` (how-to) là dạng truy vấn chủ đạo, không phải danh từ công cụ.** 2/7 KW ms bắt đầu bằng `cara` (`cara copy caption instagram`, `cara download caption instagram`), trong khi bản EN thiên về danh từ công cụ (`instagram caption downloader`, `caption download instagram`). Hệ quả: **section 3 (how-to) và quickAnswer quan trọng hơn hẳn bản EN** — phải viết đúng dạng hướng dẫn từng bước, và H2 section 3 phải giữ nguyên chữ `Cara`.
3. **`deskripsi` là trục thứ hai thật sự, không phải từ đồng nghĩa phụ.** `download deskripsi instagram` đứng band 10–100, ngang KW chính. Người Malaysia gọi phần chữ dưới bài là `deskripsi` cũng nhiều như `caption` — phải dùng xen kẽ trong body, không chọn một bỏ một. (Giống hệt vai trò của `Beschreibung` trong bản de.)
4. **`download` giữ nguyên tiếng Anh trong KW, `muat turun` chỉ dùng trong văn xuôi.** Cả 3 KW download của ms đều viết chữ `download` (không phải `muat turun`) — code-switching Anh–Mã là chuẩn mực search ở Malaysia. Vì vậy: **áp KW thì giữ chữ `download`**, còn `muat turun` chỉ dùng để làm văn xuôi tự nhiên và **luôn phải kèm tân ngữ** `caption`/`deskripsi`/`teks`.
5. **List cực ngắn (7 KW) → phải dịch bổ sung nhiều hơn mọi bản khác.** Bản de có 11 KW phủ gần kín 6 H2; bản ms chỉ có 7, nên các long-tail (video caption, reel caption, online, percuma) đều là **dịch bổ sung** và chỉ được nằm trong body.
6. **Rủi ro trùng bản `id` cao hơn mọi trang khác trong dự án** (6/7 KW trùng). Bản EN không có vấn đề này. Xử lý bằng bảng từ vựng bắt buộc ở trên + bối cảnh ví dụ Malaysia.

---

## Đối tượng người dùng

- Pengurus media sosial / pemasar digital Malaysia (phân tích caption pesaing)
- Usahawan online / peniaga IG (kedai baju, makanan, kosmetik) lưu caption bán chạy
- Pencipta kandungan Malaysia (swipe file caption hiệu quả)
- Freelancer chạy Instagram cho khách hàng
- Người muốn **terjemah** caption tiếng nước ngoài sang bahasa Melayu
- Người lưu caption trước khi post bị sửa/xóa
- Nhân viên agensi làm laporan kandungan
- Người muốn giữ lại **set hashtag** của một post hiệu quả

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ms.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**, đúng 2 đoạn `conclusion`. Keyword áp bằng **cách chọn từ ngữ khi dịch**, không bằng viết thêm câu hay thêm H2.

| # | H2 (ms) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1: Download Caption Instagram** | **cara download caption instagram** *(KW chính; `percuma` + `salin` ở subtitle)* |
| — | **quickAnswer** | cara download caption instagram, download caption instagram dari link |
| 1 | Apa Yang Instagram Caption Downloader Ini Buat | cara download caption instagram, download deskripsi instagram 🔄 download caption video instagram |
| 2 | Caption atau Transkrip: Mana Satu Anda Perlukan? | *(phân định Caption/Transkrip + internal link `/ms/instagram-transcript`)* |
| 3 | Cara Download Caption Instagram | **cara download caption instagram**, download caption instagram dari link |
| 4 | Apa Yang Boleh Anda Buat Dengan Caption Yang Di-download | simpan caption instagram, dapatkan caption instagram |
| 5 | **Salin Caption Instagram — Hashtag, Emoji dan Format Kekal Utuh** | **salin caption instagram (100–1K)**, **cara copy caption instagram (100–1K)** |
| 6 | Soalan Lazim | download deskripsi instagram, dapatkan caption instagram, simpan caption instagram 🔄 + long-tail (`percuma`, `online`, `reel`) |
| — | **conclusion** | download caption instagram, percuma |

### Ghi chú riêng cho bản ms (KHÔNG tạo section mới)

1. **Section 5 là van xả cho toàn bộ nhóm `salin` / `copy`.** Đây là section duy nhất được đặt hai KW volume cao nhất lên H2. Bản EN section này vốn đã nói về giữ nguyên định dạng khi copy → đưa `Salin Caption Instagram` lên H2 là **bám đúng nghĩa gốc**. Cụm `cara copy caption instagram` áp ở **đoạn 2** của section (chỗ bản EN nói "what you copy reads the same as what was on the post"), giữ nguyên chữ `copy` tiếng Anh vì KW viết như vậy.
2. **Section 3 giữ nguyên chữ `Cara` ở H2** — đây là dạng truy vấn how-to chủ đạo của tiếng Mã Lai. `download caption instagram dari link` áp ở **step 2** (chỗ dán link).
3. **Section 2 giữ nguyên vai trò phân định Caption/Transkrip.** Internal link đổi thành `[Instagram Transcript](/ms/instagram-transcript)`. Item 1 = chữ VIẾT (caption/deskripsi/hashtag), item 2 = chữ NÓI (suara/voiceover). Không được làm mờ ranh giới này.
4. **Section 4** hứng nhóm lưu/lấy: `simpan caption instagram` ở item 2 (save before it changes), `dapatkan caption instagram` ở item 1 hoặc item 5. **`dapatkan` phải xuất hiện ít nhất 2 lần** trong toàn file — đây là **từ phân định duy nhất** với bản id, bỏ qua là mất điểm khác biệt lớn nhất.
5. **`deskripsi` xuất hiện tối thiểu 4 lần** (section 1, section 2 item 1, section 5, FAQ 1) để bắt `download deskripsi instagram` — KW band 10–100 ngang KW chính.
6. **Bối cảnh Malaysia** đặt ở **section 4 item 1** (study what works): thay ví dụ chung chung của bản EN bằng caption kedai/usahawan online Malaysia, caption dwibahasa Melayu–English. **Không thêm câu**, chỉ thay ví dụ bên trong câu có sẵn.
7. **FAQ 1** hứng `percuma` + `download deskripsi instagram`; **FAQ 3** hứng long-tail Reel/video; **FAQ 8** hứng `dapatkan`/`online`. Đúng chỗ bản EN đã có sẵn câu hỏi tương ứng.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng làm KW mục tiêu ở trang này:

- **transkrip instagram / transkrip reel instagram / tukar video instagram kepada teks** → **/ms/instagram-transcript** (chữ **NÓI**, không phải chữ **VIẾT**). Đây là ranh giới quan trọng nhất của trang.
- **transkrip video youtube / sari kata youtube** → **/ms/youtube-transcript**
- **transkrip video tiktok / tiktok ke teks** → **/ms/tiktok-transcript**
- **tukar audio kepada teks / transkrip audio / mp3 ke teks** → **/ms/audio-to-text**
- 🚨 **NHÓM TẢI VIDEO — nguy hiểm nhất:** **`muat turun video instagram`**, **`download video instagram`**, **`download reels`**, `muat turun reel instagram`, `instagram downloader`, `simpan video instagram`. Volume rất lớn và SERP **hoàn toàn là downloader video**. Trang này tải **CHỮ**, không tải video. Kéo nhóm này vào sẽ làm lệch page type và trang mất hẳn cơ hội xếp hạng cho cụm caption.
  > **Quy tắc dịch bắt buộc:** mọi chỗ có `download` hoặc `muat turun` **phải có tân ngữ** `caption` / `deskripsi` / `teks`. **KHÔNG BAO GIỜ** viết `muat turun video`, `download video`, `muat turun reel`, `download reel` đứng một mình. Kiểm tra bằng grep trước khi giao file.
- **muat turun gambar instagram / simpan foto instagram** → intent tải **ảnh**, cũng sai page type.
- **salin bio instagram / salin komen instagram** → tuy gần `salin caption instagram` nhưng khác đối tượng, không tối ưu riêng.
- **caption menarik untuk instagram / idea caption instagram** → intent **viết caption mới** (ý tưởng/mẫu caption), NGƯỢC hoàn toàn với intent trích xuất caption có sẵn. Nhóm này volume rất lớn ở Malaysia — tuyệt đối không chạm.
- **teks kepada suara** → NGƯỢC intent, thuộc trang Text-to-Speech.

---

## Internal linking

- ↔ `/ms/instagram-transcript` — **link quan trọng nhất**, nằm ở **section 2** (khi user muốn chữ NÓI trong Reel/Video thay vì caption viết). Anchor: `Instagram Transcript`.
- → `/ms/youtube-transcript`, `/ms/tiktok-transcript` (cross-cluster: cùng nhu cầu lấy text, nền tảng khác).
- → `/ms/audio-to-text` (khi user có **fail audio** thay vì post Instagram).
- ↔ `/id/instagram-caption-downloader` **chỉ qua hreflang**, KHÔNG internal link chéo ngôn ngữ trong body.

---

## Ghi chú kỹ thuật cho ms.json

- `lang="ms"`, `dir="ltr"`. Hreflang khai báo **cả `ms` và `id` riêng biệt** (`hreflang="ms"` / `hreflang="id"`), tuyệt đối không dùng chung một URL cho hai ngôn ngữ — đặc biệt quan trọng ở trang này vì 6/7 KW trùng.
- **Cấu trúc JSON khớp 100% với `en.json`**: `seo` 6 keys, `hero` 4 keys, `quickAnswer` 2 keys, **6 sections**, section 1 `content` 3 đoạn, section 2 `intro` 1 + `items` 2, section 3 `steps` 4, section 4 `intro` 1 + `items` 5, section 5 `content` 3 đoạn, section 6 `items` **8** (q/a), `conclusion` h2 + `content` 2 đoạn. Kiểm tra bằng script so sánh shape.
- **Giữ nguyên Latin, không dịch:** TranscriptX, Instagram, Reel, Reels, Carousel, hashtag, emoji, caption, URL, link.
- `caption` giữ nguyên chữ thường trong văn xuôi (từ vay mượn đã chuẩn hóa), viết hoa `Caption` chỉ khi ở đầu câu hoặc trong H1/H2.
- Xưng hô **"anda"** xuyên suốt — **nhất quán với `/ms/facebook-transcript`**. Không dùng "kamu" / "kau" / "awak".
- Internal link section 2 giữ cú pháp markdown: `[Instagram Transcript](/ms/instagram-transcript)`.
- **Danh sách từ Indonesia BỊ CẤM trong `ms.json`:** `gratis`, `ambil`, `mengubah`, `ubah` (nghĩa "đổi"), `generator`, `unduh`, `unggah`, `menjadi`, `jadi` (nghĩa "thành"), `bisa`, `saja`, `berkas`, `perangkat`, `daring`, `mendukung`.
- **Từ chuẩn ms phải dùng:** `tukar`, `kepada`, `percuma`, `dapatkan`, `penjana`, `boleh`, `sahaja`, `fail`, `dalam talian`, `muat turun`, `muat naik`, `peranti`, `menyokong`, `pautan` (link), `tampal` (paste), `salin` (copy), `sunting` (edit), `terjemah` (translate), `tengok` (xem), `utuh` (intact), `log masuk` (login), `pemasangan` (install), `akaun` (account), `awam` (public), `persendirian` (private).
- Kiểm tra cuối: `grep -iE 'gratis|ambil|mengubah|generator|unduh|unggah|menjadi|bisa|saja|berkas|perangkat|daring' ms.json` phải **không có kết quả** (lưu ý `saja` có thể lọt trong `sahaja` — dùng biên từ `\bsaja\b`).
