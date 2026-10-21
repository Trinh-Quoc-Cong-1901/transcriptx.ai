🔥 TranscriptX – TikTok Caption Downloader (Turkish / tr)

URL:
/tr/tiktok-caption-downloader

Intent chính:

Tải file phụ đề (altyazı dosyası) có timecode từ video TikTok — miễn phí

Trang này nhắm đến người dùng Thổ Nhĩ Kỳ muốn **tải altyazı dosyası** của một video TikTok công khai — file có mốc thời gian từng dòng — để gắn lại lên video khi đăng lại, để dịch sang ngôn ngữ khác, hoặc để phục vụ nhu cầu tiếp cận (erişilebilirlik).

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/tr/instagram-caption-downloader`.**
>
> Dù tên gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/tr/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (**açıklama**, hashtag, emoji) | Lời **NÓI** trong video |
> | Kết quả | Đoạn text đọc được | **Altyazı dosyası có timecode** |
> | Từ khóa trục | `açıklama` (indirme / kopyalama) | **`altyazı`** (indirme / kaydetme / dosyası) |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram, `altyazı` **bị hạ xuống body** vì caption ở đó là chữ viết → phải dùng `açıklama`. **Ở trang này thì ngược lại: `altyazı` CHÍNH LÀ keyword chính** — 6/7 keyword tiếng Thổ đều chứa `altyazı`. Đừng áp nhầm quy tắc của trang kia. Ở trang này, `açıklama` **không được** dùng theo nghĩa "caption".

> ⚠️ **Phân định với `/tr/tiktok-transcript` — trục TIMING, không phải viết-vs-nói.** Cả hai trang đều lấy lời NÓI từ audio. Khác nhau ở chỗ: trang này ra **altyazı dosyası khớp thời gian** để chạy đè lên video; trang kia ra **düz metin** để đọc/copy. Bản EN cài sẵn 3 chốt chặn — **section 2** (cả section dành riêng để phân định, có link), **FAQ 3** ("What is the difference between TikTok captions and a transcript?"), và **section 1 đoạn 2**. Giữ nguyên cả ba, dịch sát, không rút gọn.

---

## ⚠️ Lưu ý riêng cho bản tr

### 1. Lỗi chính tả trong file nguồn `2_loc_kw.md`

Danh sách `## Turkish (tr)` được ghi **không dấu** (kiểu gõ ASCII của công cụ keyword). Dạng đúng chính tả tiếng Thổ:

| Ghi trong `2_loc_kw.md` (SAI) | Dạng đúng (dùng trong `tr.json`) |
| ----------------------------- | -------------------------------- |
| tiktok altyazi indirme | tiktok **altyazı** indirme |
| tiktok video altyazi indirme | tiktok video **altyazı** indirme |
| tiktok altyazilarini indirme | tiktok **altyazılarını** indirme |
| tiktok altyazi nasil indirilir | tiktok **altyazı nasıl** indirilir |
| tiktok yazilari indirme | tiktok **yazıları** indirme |
| tiktok altyazi kaydetme | tiktok **altyazı** kaydetme |
| tiktok altyazi dosyasi indir | tiktok **altyazı dosyası** indir |

**Quy tắc:** ghi dạng ĐÚNG trong intent và trong `tr.json` (100% đúng dấu `ı/i`, `ş`, `ç`, `ğ`, `ö`, `ü`). Người Thổ gõ cả hai kiểu nhưng Google chuẩn hóa về dạng có dấu; viết sai dấu trong nội dung sẽ đọc như lỗi chính tả.

### 2. Volume phẳng 100% — không có tín hiệu xếp hạng

**7/7 keyword đều `0 – 10`.** Không có cụm nào áp đảo để dồn lực, cũng không có cụm nào bị nhiễm intent phải loại. Đây là danh sách sạch nhất trong các ngôn ngữ đã làm của trang này.

**Chiến lược chọn KW chính khi volume phẳng** — chọn theo hai tiêu chí thay cho volume:

1. **Độ tự nhiên** — cụm nào người Thổ thực sự gõ vào ô tìm kiếm.
2. **Độ phủ modifier** — cụm nào là *gốc* mà các cụm còn lại chỉ thêm bổ ngữ vào.

`tiktok altyazı indirme` thắng cả hai: nó là chuỗi ngắn nhất, và **4/6 keyword còn lại chứa `altyazı` chỉ là nó cộng thêm một modifier** (`video`, `-larını`, `nasıl`, `dosyası`). Neo vào cụm gốc thì các biến thể đuôi dài tự phủ theo. `tiktok altyazı dosyası indir` tuy khớp intent chính xác nhất (nói rõ "dosya") nhưng dài và ít tự nhiên hơn khi làm H1.

**Chiến lược tổng thể: phủ đều thay vì dồn head term.** Mỗi trong 3 nhóm (indirme / kaydetme / dosya) chiếm một vị trí neo riêng; phần còn lại là dịch tự nhiên.

---

## Từ khóa chính

**tiktok altyazı indirme** (0–10) ✅ *đã search*

---

## Từ khóa phụ

### Nhóm İndirme (trục chính — phủ head + modifier)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok altyazı indirme | 0–10 | ✅ đã search *(KW chính)* |
| tiktok video altyazı indirme | 0–10 | ✅ đã search |
| tiktok altyazılarını indirme | 0–10 | ✅ đã search |
| tiktok altyazı nasıl indirilir | 0–10 | ✅ đã search |
| tiktok yazıları indirme | 0–10 | ✅ đã search |
| tiktok altyazı indirme online | — | 🔄 dịch bổ sung (download online) |

### Nhóm Kaydetme (lưu về máy)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok altyazı kaydetme | 0–10 | ✅ đã search |
| tiktok altyazı çıkarma | — | 🔄 dịch bổ sung (extract subtitles) |

### Nhóm Dosya (nhấn mạnh "ra FILE" — chốt phân định với transcript)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| tiktok altyazı dosyası indir | 0–10 | ✅ đã search |
| tiktok altyazı dosyası | — | 🔄 dịch bổ sung (subtitle file) |
| zaman kodlu altyazı | — | 🔄 dịch bổ sung (timed subtitles) |
| tiktok SRT dosyası | — | 🔄 dịch bổ sung (SRT file) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối, phải xuất hiện trong `title` / `h1` / `h2` / `description`. 🔄 *dịch bổ sung* = chỉ rải body, **không** đặt vào title/H1.

> **7/7 keyword đã search đều được áp**, không loại cụm nào — vì không cụm nào lệch intent.

---

## Search Intent

Người dùng Thổ thấy một video TikTok và cần **altyazı dosyası** của nó — không phải để đọc, mà để **dùng lại**:

- Đăng lại clip (repost) lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có altyazı.
- Dịch altyazı sang tiếng Thổ hoặc ngôn ngữ khác rồi gắn lại.
- Sửa lại altyazı tự động của TikTok vốn hay sai với tiếng Thổ.
- Làm altyazı cho người khiếm thính (`işitme engelli`).

Họ kỳ vọng:

- Dán link là ra file, không cần đăng nhập TikTok.
- File có **zaman kodu từng dòng**, mở được bằng phần mềm dựng phim.
- Chạy được cả khi video gốc **không bật altyazı**.
- Sửa được chữ trong file trước khi dùng.
- Miễn phí, `kayıt yok, kurulum yok`.

### Khác biệt so với bản tiếng Anh

1. **Tiếng Thổ chỉ có một từ `altyazı` cho cả `captions` lẫn `subtitles`.** Bản EN xen kẽ hai từ để chống lặp (`captions` ở H1, `subtitles` ở section 4). Bản Thổ không có lựa chọn đó — phải chống lặp bằng cách đổi cấu trúc câu và dùng xen kẽ `altyazı dosyası` / `altyazı satırı` / `zaman kodlu metin`.
2. **`indirme` đứng trần là rủi ro intent lớn nhất của bản Thổ, không tồn tại ở bản EN.** Trong tiếng Thổ, `tiktok indirme` mặc định hiểu là **tải VIDEO** (SERP toàn downloader video, filigransız). Bản EN không gặp chuyện này vì "download" luôn đi kèm "captions". Bản Thổ phải cưỡng chế: mọi chỗ `indir`/`indirme` **bắt buộc** có tân ngữ `altyazı` / `altyazı dosyası` / `metin`.
3. **Cặp `altyazı` (trang này) vs `açıklama` (trang Instagram) phải giữ tách bạch tuyệt đối.** Người Thổ dùng `açıklama` cho chữ viết dưới bài, `altyazı` cho chữ chạy trên video. Bản EN dùng chung từ `caption` cho cả hai nên không có ranh giới này; bản Thổ có ranh giới rõ hơn cả bản gốc — và đó là lợi thế, phải khai thác chứ không được làm mờ.
4. **Nỗi lo "altyazı tự động của TikTok sai tiếng Thổ" là điểm bán hàng riêng.** Nhận dạng tiếng Thổ của TikTok hay hỏng ở hậu tố dính (`-lerini`, `-mıştır`) và ký tự `ı/i`, `ğ`, `ş`. Bản EN chỉ nói "shaky auto-captions" chung chung — bản Thổ nhấn đúng nỗi đau này ở section 4 item 3, **trong đúng câu đã có sẵn**.
5. **`zaman kodu` / `zaman kodlu` là cách nói chuẩn cho `timecode`.** Không dùng `timecode` nguyên tiếng Anh như bản Việt; giới làm video Thổ dùng `zaman kodu`. `SRT`, `VTT` thì giữ Latin.

---

## Đối tượng người dùng

- Người làm content re-upload / tổng hợp clip TikTok
- Video editor, freelancer dựng phim
- Người cross-post TikTok sang Reels / YouTube Shorts
- Người dịch altyazı cho khán giả Thổ
- Marketer chạy nội dung đa ngôn ngữ
- Người làm nội dung cho người khiếm thính (`işitme engelli`)
- Người muốn sửa altyazı tự động sai chính tả của TikTok

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `tr.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**.

| # | H2 (tr) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** TikTok Altyazı İndirme | tiktok altyazı indirme *(KW chính)* |
| — | **quickAnswer** | tiktok altyazı nasıl indirilir, tiktok altyazı indirme |
| 1 | TikTok Altyazı İndirme Aracı Ne Yapar? | tiktok altyazı indirme, tiktok video altyazı indirme |
| 2 | Altyazı mı Transkript mi: Hangisi Gerekli? | *(chốt phân định TIMING + internal link `/tr/tiktok-transcript`)* |
| 3 | TikTok Altyazıları Nasıl İndirilir? | tiktok altyazı nasıl indirilir, tiktok altyazılarını indirme |
| 4 | İndirdiğiniz TikTok Altyazılarıyla Neler Yapabilirsiniz | tiktok altyazı kaydetme, tiktok yazıları indirme |
| 5 | TikTok Altyazılarını 100'den Fazla Dilde İndirin | tiktok altyazı dosyası indir, tiktok altyazı indirme |
| 6 | Sıkça Sorulan Sorular | toàn bộ 7 KW + long-tail |
| — | **conclusion** | tiktok altyazı indirme, ücretsiz |

### Ghi chú riêng cho bản tr (KHÔNG tạo section mới)

- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho trục TIMING. Dịch đủ 2 item, giữ link `[TikTok Transkript](/tr/tiktok-transcript)` ở item 2. Từ khóa phân định phải là cặp **`zaman kodlu altyazı dosyası`** ↔ **`düz metin`**, không phải viết-vs-nói.
- **FAQ 3** là chốt thứ hai (`TikTok altyazıları ile transkript arasındaki fark nedir?`) — dịch sát, không rút gọn, nhắc lại tên công cụ `TikTok Transkript`.
- **Section 1 đoạn 2** là chốt thứ ba — câu "chính phần zaman kodu là lý do trang này tách riêng" phải giữ nguyên trọng lượng.
- `tiktok yazıları indirme` là cụm mờ nhất trong 7 KW (`yazı` có thể hiểu là chữ trên màn hình). Chỉ chạm **một lần** ở section 4, trong câu vốn đã nói về chữ hiện trên clip khi tắt tiếng — không thêm câu.
- Nỗi lo altyazı tự động sai tiếng Thổ xử lý **trong câu đã có** ở section 4 item 3, không thêm câu mới.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `tiktok transkript` / `tiktok videoyu yazıya çevirme` / `tiktok metne dönüştürme` → **/tr/tiktok-transcript** (**düz metin**, không có zaman kodu). Kéo vào đây sẽ ăn thịt trang kia.
- `instagram açıklama indirme` / `caption instagram` → **/tr/instagram-caption-downloader** (chữ tác giả GÕ dưới bài, khác hẳn)
- `youtube altyazı indirme` / `youtube transkript` → **/tr/youtube-transcript**
- 🚨 **Nhóm tải VIDEO — rủi ro cao nhất của bản Thổ:** `tiktok video indirme`, `tiktok filigransız indir`, `tiktok watermarksız indirme`, `tiktok video kaydetme`. SERP của các cụm này toàn công cụ tải video. Trang này tải **altyazı dosyası**, không tải video.
  > **Quy tắc cưỡng chế:** `indirme` / `indir` / `kaydetme` **chỉ được đi kèm** `altyazı` / `altyazı dosyası` / `metin`. **Không bao giờ** để chuỗi `video indirme`, `videoyu indir`, `video kaydetme` xuất hiện ở bất kỳ đâu trong `tr.json`.

---

## Internal linking

- ↔ /tr/tiktok-transcript (khi user chỉ cần düz metin để đọc, không cần zaman kodu) — link quan trọng nhất, nằm ở **section 2 item 2**, nhắc lại bằng tên (không link) ở **FAQ 3**

---

## Ghi chú kỹ thuật cho tr.json

- Xưng hô **ngôi thứ hai số nhiều lịch sự (`siz` — `yapıştırın`, `indirin`)**, nhất quán với các trang Thổ khác trong repo.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT**.
- Cấu trúc 1:1 với `en.json`: **6 section**, section 1 `content` **3 đoạn**, section 2 = `intro` 1 + `items` 2, section 3 = `steps` 4, section 4 = `intro` 1 + `items` 5, section 5 = `content` **2 đoạn**, section 6 = `items` **8 FAQ**, `conclusion` = h2 + `content` 2 đoạn.
- Internal link section 2 item 2 giữ cú pháp markdown: `[TikTok Transkript](/tr/tiktok-transcript)`.
- **Chính tả đúng dấu 100%:** phân biệt `ı` (không chấm) và `i` (có chấm) — `altyazı`, `nasıl`, `dosyası`, `yazıları`, `kaydı`; cùng `ş`, `ç`, `ğ`, `ö`, `ü`.
- Dấu nháy nối hậu tố cho danh từ riêng: `TranscriptX'e`, `TikTok'un`, `Reel'e`, `SRT'ye`.
- Tránh lặp `altyazı` quá dày: dùng xen kẽ `altyazı dosyası`, `altyazı satırı`, `zaman kodlu metin`, `dosya`.
