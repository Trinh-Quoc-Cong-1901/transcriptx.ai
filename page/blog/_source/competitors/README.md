# Phân tích đối thủ (sitemap) — cơ sở chọn chủ đề blog và tool page

Lấy ngày **2026-11-04**. Chỉ đọc danh sách URL trong sitemap của đối thủ, **không mở nội dung trang**. Chủ đề được gán bằng từ khoá trong URL nên số liệu là ước lượng: tin cột "Số đối thủ viết / có", đừng tin tuyệt đối cột "Tổng số bài" (Sonix, Rev có nhiều trang làm hàng loạt).

Đối thủ: Otter, Descript, Rev, Sonix, Trint, Notta, ElevenLabs, TurboScribe. **Happy Scribe chưa có** (sitemap trả 403).

## File

| File | Dùng để làm gì |
|---|---|
| `doi-thu-tong-hop-trang.xlsx` | **File chính.** Sheet **Blog kéo traffic**: 37 cụm bài × 8 đối thủ, TranscriptX đã đăng / đang viết / có trong kế hoạch / chưa có, ưu tiên P1–P3, slug đề xuất, tool page nhận traffic. Sheet **Tool page (đã sửa)**: loại trang nào mình đã có (đối chiếu `page/llms.txt`), loại nào chỉ cần thêm H2/FAQ, loại nào thật sự phải làm mới. Sheet **URL blog đối thủ theo cụm**: từng bài của đối thủ trong mỗi cụm. |
| `elevenlabs-sitemap-stt.xlsx` | Riêng ElevenLabs: tool page và blog về chép lời, trang STT theo ngôn ngữ. |
| `turboscribe-sitemap-stt.xlsx` | Riêng TurboScribe: landing `/l/`, `/learn/`, `free-*`, ý tưởng cho TranscriptX. |
| `urls/*.txt`, `urls/elevenlabs.tsv` | Danh sách URL tiếng Anh thô của từng đối thủ (mỗi dòng 1 URL). Dùng để grep. |
| `_scripts/` | Script tải sitemap và dựng lại các file Excel. |

## Cách dùng khi viết bài

**1. Chọn chủ đề tiếp theo:** mở `doi-thu-tong-hop-trang.xlsx` → sheet **Blog kéo traffic** → lọc cột *TranscriptX* = "Chưa có" hoặc "Có trong kế hoạch", ưu tiên P1. Lấy slug đề xuất → gửi danh sách keyword cho user tra volume (Bước 1 của skill `transcriptx-blog`).

**2. Xem đối thủ viết chủ đề đó thế nào (góc viết, H2 nên có):** grep slug trong `urls/`:
```bash
grep -h -i "interview" page/blog/_source/competitors/urls/*.txt | grep -E "/(blog|resources|learn|articles)/"
```
Tên slug của đối thủ cho biết họ chia nhỏ chủ đề ra sao (vd. `how-to-transcribe-an-interview-step-by-step`, `interview-transcription-tips`) → gợi ý H2/FAQ. Không chép nội dung, không link ra trang đối thủ.

**3. Trước khi làm tool page mới:** xem sheet **Tool page (đã sửa)**. Nếu cột *Việc cần làm* = "Đã có, thêm H2/FAQ" thì sửa trang đang có, không làm trang mới.

**4. Bài so sánh / alternative:** grep tên đối thủ (`grep -i "alternative\|-vs-" urls/turboscribe.txt`) để biết họ đang tự so với ai. Hồ sơ giá và tính năng vẫn phải lấy từ trang chính của đối thủ và ghi ngày kiểm tra (xem quy tắc trong `_blog_topics.md`).

## Cập nhật lại (khoảng mỗi quý)

```bash
cd page/blog/_source/competitors/_scripts
python3 fetch_sitemaps.py ../urls            # Otter, Descript, Rev, Sonix, Trint, Notta → ../urls/<site>.txt
python3 build_gap.py                         # đọc ../urls/ + ../../../_blog_topics.md, ghi ../doi-thu-tong-hop-trang.xlsx
```
- ElevenLabs (`urls/elevenlabs.tsv`) và TurboScribe (`urls/turboscribe.txt`) tải bằng sitemap `elevenlabs.io/sitemap.xml` và `turboscribe.com/__sitemap.xml`. `build_el_xlsx.py` / `build_tb_xlsx.py` nhận đường dẫn dữ liệu và file xuất qua tham số dòng lệnh.
- Bài mới: thư mục nào trong `page/blog/` có `kw.md` được tính là "Đang viết". Khi bài đã đăng, thêm slug vào `PUBLISHED` trong `build_gap.py`.
- Trang đối thủ chặn bot (403) thì bỏ qua, không vượt chặn.
