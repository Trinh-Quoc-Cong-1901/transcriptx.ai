🔥 TranscriptX – TikTok Caption Downloader (Indonesian / id)

URL:
/id/tiktok-caption-downloader

Intent chính:

Tải phụ đề TikTok về dạng file có timecode (miễn phí) — `download subtitle TikTok`

Trang này nhắm đến người dùng Indonesia muốn **tải file subtitle** của một video TikTok công khai — file có mốc thời gian từng dòng — để gắn lại lên clip khi đăng lại (repost), để dịch sang ngôn ngữ khác, hoặc để phục vụ người khiếm thính.

> 🚨 **ĐỌC KỸ TRƯỚC KHI DỊCH — TRANG NÀY KHÁC HẲN `/id/instagram-caption-downloader`.**
>
> Dù tên tiếng Anh gần giống nhau, hai trang làm hai việc hoàn toàn khác:
>
> | | `/id/instagram-caption-downloader` | **Trang này** |
> | --- | --- | --- |
> | Lấy gì | Chữ tác giả **GÕ** dưới bài (`caption`, `deskripsi`, hashtag, emoji) | Lời **NÓI** trong video |
> | Kết quả | Đoạn text đọc được | **File subtitle có timecode** |
> | Từ khóa trục | `caption` / `deskripsi` | `subtitle` / `teks bersinkron` |
> | Phân định với trang transcript | chữ viết ≠ chữ nói | **có timing ≠ không timing** |
>
> Ở trang Instagram, `caption` = chữ viết, tuyệt đối không được hiểu là phụ đề. **Ở trang này thì ngược lại: `subtitle` CHÍNH LÀ trục keyword.** Đừng áp nhầm quy tắc của trang kia.

> ⚠️ **Phân định với `/id/tiktok-transcript` — trục là TIMING, không phải viết-vs-nói.** Cả hai trang đều lấy lời NÓI từ audio. Khác nhau ở chỗ: trang này ra **file subtitle khớp thời gian** để chạy đè lên video; trang transcript ra **teks biasa** để đọc/copy. Bản EN cài sẵn 3 chốt chặn — **section 2** (cả section dành riêng để phân định, có internal link), **FAQ 3** ("What is the difference between TikTok captions and a transcript?"), và **section 1 đoạn 2**. Giữ nguyên cả ba, dịch sát, không rút gọn.

---

## 🚨 MỤC QUAN TRỌNG NHẤT — TRANG NÀY GẦN NHƯ 0 DỮ LIỆU KEYWORD

Đây là tình huống dữ liệu tệ nhất trong toàn bộ các bản localization của trang này.

### Tình trạng thực tế

Section `## Indonesian (id)` trong `2_loc_kw.md` **chỉ có đúng 1 dòng**:

```
download teks tiktok
```

- **Không có dòng volume** đi kèm (khác mọi ngôn ngữ khác trong file — kể cả `ms` cũng có `100 – 1K`).
- Chỉ 1 keyword duy nhất, so với `ko` 10 cụm, `fr` 11 cụm, `vi` 13 cụm.
- Nghĩa là: **không có cơ sở dữ liệu để chọn trục keyword.** Toàn bộ bản `id` là **dịch tự nhiên**, không phải tối ưu theo số liệu.

### Vấn đề riêng của cụm `download teks tiktok`

Cụm này **mơ hồ về intent**. Từ `teks` trong tiếng Indonesia là danh từ chung cho "chữ/văn bản", nó có thể mang hai nghĩa:

| Cách hiểu | Intent thật | Thuộc trang nào |
| --- | --- | --- |
| "tải chữ trong video TikTok về đọc" | transcript, teks biasa | ❌ `/id/tiktok-transcript` |
| "tải phần chữ (subtitle) của video TikTok" | subtitle file có timecode | ✅ trang này |

Nếu để cụm này đứng một mình làm H1, trang sẽ **ăn thịt `/id/tiktok-transcript`** — đúng cái lỗi mà 3 chốt chặn phân định ở trên sinh ra để ngăn.

### Hướng xử lý đã được người dùng chốt

1. ✅ **Vẫn dùng** `download teks tiktok` — đây là dữ liệu duy nhất có, bỏ đi thì trắng tay.
2. ✅ **Luôn neo ngữ cảnh subtitle**: mọi lần xuất hiện phải đi kèm mệnh đề làm rõ, kiểu `download teks TikTok dalam bentuk file subtitle bertimecode`. Không bao giờ để cụm trần.
3. ❌ **Không để nó đứng một mình làm H1.** H1 phải là cụm phụ đề rõ intent.
4. ✅ **H1 chốt: `Download Subtitle TikTok`** — dịch tự nhiên, rõ intent, khớp đúng thứ trang này trả ra.
5. ✅ Số lần xuất hiện của `download teks tiktok`: **tối đa 3 lần** (title/description, section 1 đoạn 1, FAQ 1) — mỗi lần đều có mệnh đề neo subtitle.

### 🔎 Khuyến nghị search bổ sung cho lần sau

Trước khi làm lại / tối ưu lại trang `id`, **cần search volume** các cụm sau — đây mới là trục intent đúng của trang:

| Cụm cần search | Lý do |
| --- | --- |
| `download subtitle tiktok` | ứng viên số 1 cho KW chính, khớp đúng intent |
| `cara download subtitle tiktok` | biến thể how-to, thường có volume cao ở Indonesia |
| `ekstrak subtitle tiktok` | biến thể "trích xuất", tương ứng `ekstrak sarikata tiktok` bên `ms` |
| `subtitle tiktok` | head term danh từ |
| `download subtitle video tiktok` | biến thể dài, có `video` |
| `simpan subtitle tiktok` | biến thể "lưu" |
| `download subtitle tiktok online` | biến thể online |

Có số liệu rồi thì đảo lại map H2 nếu cần. Hiện tại **map dưới đây dựa trên suy luận intent, không dựa trên volume.**

---

## 🛡️ Chống trùng với `/ms/tiktok-caption-downloader`

Bản `ms` đang được làm song song và dùng `sarikata` làm trục. Hai ngôn ngữ rất gần nhau, phải tách bạch từ vựng:

| Khái niệm | ✅ id dùng | ❌ Cấm (thuộc ms) |
| --- | --- | --- |
| phụ đề | `subtitle` | `sarikata` |
| tải về | `download` (+ `unduh` khi cần biến thể) | `muat turun` |
| tệp tin | `file` | `fail` |
| miễn phí | `gratis` | `percuma` |
| có thể | `bisa` (+ `dapat`) | `boleh` |
| chỉ, thôi | `saja` | `sahaja` |
| bạn | `Anda` | *(ms cũng dùng `anda` — phân biệt bằng 6 mục trên)* |
| dán | `tempel` | `tampal` |
| link | `link` | `pautan` |
| công cụ | `alat` | *(chung — không phải điểm phân biệt)* |
| công khai | `publik` | `awam` |

**Quy tắc grep sau khi viết xong:** `sarikata`, `muat turun`, `fail`, `percuma`, `boleh`, `sahaja`, `tampal`, `pautan`, `awam` phải = **0 hit** trong `id.json`.

---

## Từ khóa chính

**`download subtitle tiktok`** — ⚠️ **cụm dịch tự nhiên, CHƯA search, không có volume.**

Chọn vì: khớp chính xác thứ trang trả ra (file subtitle), tách bạch rõ với `/id/tiktok-transcript`, và là cách người Indonesia thực sự gọi việc này (`subtitle` là từ mượn đã phổ thông, dùng rộng hơn `takarir` vốn quá hàn lâm).

H1 chốt: **`Download Subtitle TikTok`**

---

## Từ khóa phụ

### Nhóm dữ liệu duy nhất có

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download teks tiktok | — *(file nguồn KHÔNG có dòng volume)* | ⚠️ đã có trong `2_loc_kw.md` nhưng **không có số liệu** — chỉ dùng kèm mệnh đề neo subtitle |

### Nhóm Tải / Lấy (trục chính)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| download subtitle tiktok | — | 🔄 dịch bổ sung *(KW chính — cần search)* |
| cara download subtitle tiktok | — | 🔄 dịch bổ sung (how to download) |
| download subtitle video tiktok | — | 🔄 dịch bổ sung (video subtitles) |
| download subtitle tiktok online | — | 🔄 dịch bổ sung (online) |
| download file subtitle tiktok | — | 🔄 dịch bổ sung (subtitle file) |
| unduh subtitle tiktok | — | 🔄 dịch bổ sung (biến thể chuẩn tiếng Indo của `download`) |

### Nhóm Danh từ (phủ head term)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| subtitle tiktok | — | 🔄 dịch bổ sung (tiktok subtitles) |
| subtitle video tiktok | — | 🔄 dịch bổ sung (tiktok video captions) |
| teks bersinkron tiktok | — | 🔄 dịch bổ sung (timed text) |

### Nhóm Dịch (khớp đúng section 5 của bản EN)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| terjemahkan subtitle tiktok | — | 🔄 dịch bổ sung (translate subtitles) |

### Dịch bổ sung khác (chỉ rải body)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| ekstrak subtitle tiktok | — | 🔄 dịch bổ sung (extract subtitles) |
| simpan subtitle tiktok | — | 🔄 dịch bổ sung (save subtitles) |
| subtitle tiktok gratis | — | 🔄 dịch bổ sung (free) |
| file SRT tiktok | — | 🔄 dịch bổ sung (SRT file) |

**Nguyên tắc dùng:** ✅ *đã search* = ưu tiên tuyệt đối — **trang này KHÔNG có cụm nào như vậy.** 🔄 *dịch bổ sung* = bình thường chỉ rải body, nhưng vì trang trắng dữ liệu nên **buộc phải để `download subtitle tiktok` lên title/H1**. Đây là ngoại lệ do tình huống dữ liệu, đã được duyệt.

> ⚠️ **Tóm lại: 0 cụm có volume, 1 cụm có mặt trong file nguồn nhưng mơ hồ.** Chiến lược: dịch tự nhiên bám sát bản EN, phủ đều 3 nhóm (tải / danh từ / dịch), và **ghi nợ một vòng search** cho lần tối ưu sau.

---

## Search Intent

Người dùng Indonesia thấy một video TikTok và cần **file subtitle** của nó — không phải để đọc, mà để **dùng lại**:

- Đăng lại clip (repost) lên TikTok của mình, hoặc cross-post sang Reels / Shorts, mà vẫn có subtitle.
- Dịch subtitle sang Bahasa Indonesia hoặc ngôn ngữ khác rồi gắn lại.
- Sửa lại subtitle tự động của TikTok vốn hay sai khi người nói trộn Bahasa với tiếng Anh hoặc dùng tiếng lóng.
- Làm subtitle cho người khiếm thính.

Họ kỳ vọng:

- Dán link là ra file, không cần đăng nhập TikTok.
- File có **timecode từng dòng**, mở được bằng phần mềm dựng phim (CapCut, Premiere).
- Chạy được cả khi video gốc **không bật subtitle**.
- Sửa được chữ trong file trước khi dùng.
- Miễn phí (`gratis`).

### Khác biệt so với bản tiếng Anh

1. **Bản EN xen kẽ `captions` / `subtitles` để chống lặp; bản id gần như chỉ có một từ dùng được là `subtitle`.** Tiếng Indonesia có `takarir` (thuật ngữ chuẩn KBBI cho subtitle) nhưng hầu như không ai search — dùng vào sẽ mất traffic. Vì vậy phải chống lặp bằng cách đổi cấu trúc câu và luân phiên `file subtitle` / `baris subtitle` / `teks bersinkron` / `teksnya`, chứ không đổi được từ gốc.
2. **Cụm `caption` phải bị hạn chế tối đa.** Ở Indonesia, `caption` được hiểu mặc định là **chữ viết dưới bài đăng** (đúng nghĩa trang Instagram), chứ không phải phụ đề. Bản EN dùng `caption` xuyên suốt; **bản id phải chuyển gần như toàn bộ sang `subtitle`**, nếu không sẽ tự đẩy mình vào cùng SERP với `/id/instagram-caption-downloader` và gây hiểu sai cho người dùng. Chỉ giữ `Caption` trong `schemaName` (tên riêng sản phẩm) và nhãn nút nếu cần.
3. **Rủi ro nhiễm intent "tải VIDEO TikTok" cao hơn hẳn mọi ngôn ngữ khác.** Indonesia là một trong những thị trường TikTok lớn nhất thế giới, và nhóm keyword `download video tiktok` / `tiktok tanpa watermark` / `snaptik` có volume khổng lồ. Nếu chuỗi `download video TikTok` xuất hiện trong bản dịch, Google sẽ hiểu nhầm trang là video downloader. **Quy tắc cứng: `download` / `unduh` chỉ được đi với `subtitle` / `file` / `teks`, tuyệt đối không đi với `video`.**
4. **Trang trắng dữ liệu keyword.** Các bản `vi`, `ko`, `fr` có 5–11 cụm đã search để neo. Bản `id` không có gì, nên độ ưu tiên chuyển từ "áp keyword" sang "dịch tự nhiên + phân định intent chuẩn xác", chờ vòng search bổ sung.
5. **`timecode`, `SRT`, `subtitle` giữ nguyên Latin.** Người làm video ở Indonesia dùng thẳng các từ này, không dịch. `bertimecode` là cách ghép tự nhiên (tiền tố `ber-` + từ mượn).

---

## Đối tượng người dùng

- Người làm content re-upload / tổng hợp clip TikTok
- Editor video, freelancer dựng phim (CapCut là công cụ phổ biến nhất ở Indonesia)
- Người cross-post TikTok sang Reels / YouTube Shorts
- Người dịch subtitle (sub) cho khán giả Indonesia
- Admin akun brand / olshop chạy nội dung đa ngôn ngữ
- Người làm nội dung cho người khiếm thính (`teman tuli`)
- Người muốn sửa subtitle tự động sai của TikTok, nhất là khi video trộn Bahasa với tiếng Anh

---

## Map H2 → keyword (bám ĐÚNG 6 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `id.json` phải dịch đúng **6 section** của `en.json`, cùng số đoạn `content`, đúng 2 `items` ở section 2, đúng 4 `steps`, đúng 5 `items` ở section 4, đúng **8 FAQ**. Keyword áp bằng **cách chọn từ ngữ khi dịch**.

| # | H2 (id) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** Download Subtitle TikTok | download subtitle tiktok *(KW chính, dịch tự nhiên)* |
| — | **quickAnswer** | cara download subtitle tiktok, file subtitle bertimecode |
| 1 | Apa yang Dilakukan Alat Download Subtitle TikTok Ini | download subtitle tiktok, **`download teks tiktok` + mệnh đề neo subtitle** |
| 2 | Subtitle atau Transkrip: Mana yang Anda Butuhkan? | *(phân định TIMING + internal link `/id/tiktok-transcript`)* |
| 3 | Cara Download Subtitle TikTok | cara download subtitle tiktok, download file subtitle tiktok |
| 4 | Apa yang Bisa Anda Lakukan dengan Subtitle TikTok yang Sudah Diunduh | subtitle tiktok, simpan subtitle tiktok |
| 5 | Download Subtitle TikTok dalam Lebih dari 100 Bahasa | terjemahkan subtitle tiktok |
| 6 | Pertanyaan yang Sering Diajukan | subtitle tiktok, ekstrak subtitle tiktok + long-tail |
| — | **conclusion** | download subtitle tiktok, gratis |

### Ghi chú riêng cho bản id (KHÔNG tạo section mới)

- **Section 2 là chốt phân định quan trọng nhất** — cả section dành riêng cho việc này, trục là **timing chứ không phải viết-vs-nói**. Dịch đủ 2 item, giữ link `[TikTok Transcript](/id/tiktok-transcript)` ở item 2.
- **FAQ 3** là chốt thứ hai (`Apa beda subtitle TikTok dengan transkrip?`) — dịch sát, không rút gọn, phải nói rõ transcript là **teks biasa** không có timing.
- **Section 1 đoạn 2** là chốt thứ ba — giữ nguyên lập luận "timing là lý do trang này tách riêng".
- Cụm `download teks tiktok` chỉ chạm ở **section 1 đoạn 1** và **FAQ 1**, luôn kèm mệnh đề `dalam bentuk file subtitle bertimecode`. Không thêm câu mới.
- Nỗi lo subtitle tự động sai (video trộn Bahasa + English) xử lý **trong câu đã có** ở section 4 item 3, không thêm câu mới.
- Không dùng `takarir` ở bất kỳ đâu — đúng thuật ngữ nhưng không ai search.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác hoặc sai intent — KHÔNG dùng ở trang này:

- `transkrip tiktok` / `ubah video tiktok jadi teks` / `teks biasa tiktok` → **/id/tiktok-transcript** (teks biasa để đọc, không có timing). Đây là ranh giới dễ vi phạm nhất vì cụm `download teks tiktok` nằm sát vạch.
- `download caption instagram` / `caption instagram` / `deskripsi instagram` → **/id/instagram-caption-downloader** (chữ viết dưới bài, khác hẳn)
- `transkrip youtube` / `subtitle youtube` → **/id/youtube-transcript**
- ⚠️ **`download video tiktok` / `tiktok tanpa watermark` / `download tiktok no wm` / `snaptik` / `ssstik`** → **intent tải VIDEO**, SERP toàn video downloader. Nhóm này **cực kỳ phổ biến ở Indonesia**, volume lớn hơn nhóm subtitle nhiều lần, nên rủi ro nhiễm rất cao.
  **Quy tắc cứng:** `download` / `unduh` chỉ được đi với `subtitle` / `file` / `teks`. Chuỗi `download video`, `unduh video`, `download TikTok tanpa watermark` phải = **0 hit**.
- `cara membuat subtitle di tiktok` / `cara menyalakan subtitle tiktok` → **hướng dẫn thao tác trong app TikTok**, không phải công cụ tải file về.

---

## Internal linking

- ↔ /id/tiktok-transcript (khi user chỉ cần teks biasa để đọc, không cần timing) — link quan trọng nhất, nằm ở **section 2 item 2**, nhắc lại ở **FAQ 3**
- ↔ /id/instagram-caption-downloader — *không* link trực tiếp từ trang này (khác intent hẳn), nhưng phải giữ từ vựng tách bạch để hai trang không cạnh tranh nhau

---

## Ghi chú kỹ thuật cho id.json

- Xưng hô **"Anda"**, nhất quán với `/id/instagram-transcript` và `/id/instagram-caption-downloader`.
- Giữ nguyên Latin: **TranscriptX, TikTok, Reel, Reels, Shorts, SRT, VTT, timecode, subtitle**.
- Cấu trúc: **6 section**, **8 FAQ**. S1 `content` **3 đoạn** | S2 `intro` 1 + `items` 2 | S3 `steps` 4 | S4 `intro` 1 + `items` 5 | S5 `content` **2 đoạn** | S6 `items` **8**. `conclusion` = h2 + content **2 đoạn**.
- Internal link section 2 item 2 giữ cú pháp markdown: `[TikTok Transcript](/id/tiktok-transcript)`.
- **Grep phải = 0:** `sarikata`, `muat turun`, `fail`, `percuma`, `boleh`, `sahaja`, `tampal`, `pautan`, `awam` (từ Mã Lai) — và `download video`, `unduh video`, `takarir`.
- Tránh lặp `subtitle` quá dày: luân phiên `file subtitle`, `baris subtitle`, `teks bersinkron`, `teksnya`, `subtitlenya`.
- Dùng `tempel` (dán), `publik` (công khai), `gratis` (miễn phí), `bisa` / `dapat` (có thể), `perangkat` (thiết bị).
