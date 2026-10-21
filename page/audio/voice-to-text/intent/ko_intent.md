🔥 TranscriptX – Voice to Text (Korean / ko)

URL:
/ko/voice-to-text

Intent chính:

음성 받아쓰기 (브라우저에서 바로 녹음 · 무료)

Trang này là **bản tiếng Hàn của trang dictation / ghi âm trực tiếp** trong cụm Voice-Audio. Nhắm đến người dùng Hàn Quốc muốn **nói ra và nhận lại chữ**: ghi âm thẳng trong trình duyệt, đọc chính tả một bản nháp, hoặc chuyển 음성 메모 / 녹취 của chính mình thành văn bản.

Khác trang `/ko/audio-to-text` ở **điểm xuất phát**: trang kia bắt đầu từ **tệp âm thanh đã có sẵn** (MP3, 팟캐스트, 다운로드한 파일); trang này bắt đầu từ **giọng nói của chính người dùng** — vừa nói ra hoặc vừa ghi âm bằng điện thoại.

---

> ⚠️ **Lưu ý cực kỳ quan trọng — lỗi khoảng trắng trong `2_loc_kw.md`:**
> Danh sách keyword tiếng Hàn trong `2_loc_kw.md` bị **chèn khoảng trắng sai giữa danh từ và trợ từ (조사)**. Tiếng Hàn **không bao giờ** tách trợ từ (`을/를`, `로/으로`, `이/가`, `에`, `의`) khỏi danh từ đứng trước.
>
> | Trong file (SAI) | Dạng đúng (dùng trong intent & ko.json) |
> | ---------------- | --------------------------------------- |
> | `음성 을 텍스트 로 변환` | `음성을 텍스트로 변환` |
>
> Đây là keyword duy nhất trong section Korean bị lỗi khoảng trắng, nhưng nguyên tắc áp dụng cho **toàn bộ** `ko.json`: không bao giờ để khoảng trắng trước trợ từ. Nếu viết theo dạng sai, Google sẽ tokenize thành cụm vô nghĩa và người Hàn đọc sẽ thấy văn bản lỗi.

---

> 🚨 **CẢNH BÁO TRÙNG LẶP NẶNG với `/ko/audio-to-text` — ca khó nhất trong tất cả ngôn ngữ**
>
> Trang `/ko/audio-to-text` **đã hoàn thành và ĐÃ ĐÓNG BĂNG**. Hai trang trùng tới **8 keyword** — nhiều nhất trong mọi ngôn ngữ của dự án. Lý do: tiếng Hàn **không phân biệt** "voice" và "audio" ở tầng từ vựng thương mại — cả hai đều rơi về `음성`. Trong khi tiếng Anh có hai cụm riêng biệt (`voice to text` 100K–1M vs `audio to text`), tiếng Hàn chỉ có **một** cụm chủ đạo `음성 텍스트 변환`, và cụm đó đã thuộc về trang kia.
>
> **Hệ quả trực tiếp:**
> 1. Trang này **mất toàn bộ** nhóm KW volume cao (1K–10K). KW cao nhất còn dùng được chỉ là `음성 텍스트 추출` (100–1K).
> 2. **Phần lớn KW của trang này buộc phải là `🔄 dịch bổ sung`** — 13 KW bổ sung so với 7 KW đã search. Đây là tỷ lệ đảo ngược so với các ngôn ngữ khác. **Chấp nhận điều này** — thà phủ đúng ngữ nghĩa dictation với KW chưa có volume còn hơn ăn cắp KW của trang đã đóng băng và tạo cannibalization.
> 3. KW chính của trang này (`음성 받아쓰기`, 10–100) có volume **thấp hơn 100 lần** KW chính của trang kia. Đây là **lựa chọn có chủ đích**, không phải sai sót.
>
> **📌 KHUYẾN NGHỊ RESEARCH BỔ SUNG (ưu tiên cao):**
> Cụm `받아쓰기` / dictation trong tiếng Hàn **chưa được research đầy đủ** — `2_loc_kw.md` chỉ có đúng 1 keyword (`음성 받아쓰기`). Trước khi scale trang này, nên chạy thêm một vòng search volume cho:
> - `받아쓰기 프로그램`, `받아쓰기 사이트`, `음성 인식 받아쓰기`, `자동 받아쓰기`
> - `실시간 음성 텍스트 변환`, `실시간 자막`, `실시간 받아쓰기`
> - `음성 메모 텍스트 변환`, `음성 메모 변환`, `아이폰 음성 메모 텍스트`
> - `말로 입력`, `음성 입력`, `음성으로 글쓰기`, `음성 타이핑`
> - `회의록 자동 작성`, `녹취록 작성`, `강의 받아쓰기`
>
> Nhiều khả năng có KW volume **cao hơn** `음성 받아쓰기` đang ẩn trong cụm này (đặc biệt `음성 입력` và `회의록 자동 작성` — hai cụm rất phổ biến ở thị trường công sở Hàn). Nếu tìm được, **nên nâng KW chính của trang** ở vòng cập nhật sau.

---

> 💡 **Ba trục ngữ nghĩa của trang này (khác hẳn trang audio-to-text):**
> - `받아쓰기` — đọc chính tả / máy chép lại lời nói (**trục chính, độc quyền của trang này**)
> - `음성 입력` / `말로 입력` — nhập liệu bằng giọng nói thay bàn phím
> - `음성 메모` / `녹취` — ghi chú thoại của chính mình
>
> Trang audio-to-text sở hữu trục `파일` (파일 업로드, MP3, 팟캐스트). Trang này **tuyệt đối không** đi vào trục 파일.

---

## Từ khóa chính

**음성 받아쓰기** (10–100) ✅ *đã search*

> Trang `/ko/audio-to-text` **đã cố ý nhường lại** keyword này (xem `../audio-to-text/intent/ko_intent.md`, mục "Không nên tối ưu"). `받아쓰기` = dictation/chép chính tả — đúng intent trang này 100%.

---

## Từ khóa phụ

### Nhóm 받아쓰기 / 음성 인식 (dictation — trục chính, độc quyền)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 음성 받아쓰기 | 10–100 | ✅ đã search *(KW chính)* |
| 받아쓰기 | — | 🔄 dịch bổ sung (dictation) |
| 음성 인식 받아쓰기 | — | 🔄 dịch bổ sung (speech recognition dictation) |
| 자동 받아쓰기 | — | 🔄 dịch bổ sung (auto dictation) |
| 받아쓰기 사이트 | — | 🔄 dịch bổ sung (dictation site) |
| 음성 인식 | — | 🔄 dịch bổ sung (speech recognition) |

### Nhóm 음성 입력 / 말로 입력 (nhập liệu bằng giọng nói)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 음성 문자 변환 | 10–100 | ✅ đã search |
| 말로 입력 | — | 🔄 dịch bổ sung (type by speaking) |
| 음성 입력 | — | 🔄 dịch bổ sung (voice input) |
| 음성으로 글쓰기 | — | 🔄 dịch bổ sung (write by voice) |
| 음성 타이핑 | — | 🔄 dịch bổ sung (voice typing) |

### Nhóm 음성 메모 / 녹취 (ghi chú thoại của chính mình)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 음성 텍스트 추출 | 100–1K | ✅ đã search *(KW phụ mạnh nhất)* |
| 녹취 텍스트 변환 | 10–100 | ✅ đã search |
| 음성 자동 텍스트 변환 | 0–10 | ✅ đã search |
| 음성 메모 텍스트 변환 | — | 🔄 dịch bổ sung (voice memo to text) |
| 음성 메모 변환 | — | 🔄 dịch bổ sung (convert voice memo) |
| 녹취록 작성 | — | 🔄 dịch bổ sung (write up a transcript) |

### Nhóm 실시간 / 온라인 (thời gian thực & online — dùng dè dặt)

| Keyword | Volume | Nguồn |
| ------- | ------ | ----- |
| 녹음 텍스트 변환 온라인 | 0–10 | ✅ đã search |
| 음성 텍스트 변환 온라인 | 0–10 | ✅ đã search ⚠️ *chỉ dùng trong body — chứa cụm của trang kia* |
| 실시간 음성 텍스트 변환 | — | 🔄 dịch bổ sung (real-time voice to text) |
| 브라우저 음성 녹음 | — | 🔄 dịch bổ sung (record in browser) |

**Tổng:** **7 KW `✅ đã search`** dùng được + **13 KW `🔄 dịch bổ sung`**.

> ⚠️ Tỷ lệ 7/13 là **bất thường** so với các ngôn ngữ khác (thường 12/9). Nguyên nhân duy nhất là 8 KW volume cao đã bị `/ko/audio-to-text` chiếm. Xem khuyến nghị research bổ sung ở trên.

---

## 8 KW nhường cho /ko/audio-to-text

Trang `/ko/audio-to-text` **đã hoàn thành và đóng băng** — 8 keyword sau **KHÔNG được dùng làm KW chính, H1 hay H2** ở trang này:

| # | Keyword | Volume | Vai trò ở trang kia |
| - | ------- | ------ | ------------------- |
| 1 | `음성 텍스트 변환` | 1K–10K | **KW chính** của /ko/audio-to-text |
| 2 | `음성 파일 텍스트 변환` | 1K–10K | KW phụ #1, H2 section 3 |
| 3 | `녹음 파일 텍스트 변환` | 1K–10K | KW phụ, H2 section 5 |
| 4 | `녹음 텍스트 변환` | 1K–10K | KW phụ, H2 section 5 |
| 5 | `음성을 텍스트로 변환` | 100–1K | quickAnswer + section 3 *(đã sửa khoảng trắng)* |
| 6 | `음성 텍스트 변환 무료` | 100–1K | H2 section 4 |
| 7 | `음성 텍스트 변환 사이트` | 100–1K | H2 section 4 |
| 8 | `음성 텍스트 변환기` | 10–100 | section 4 |

> ✅ **Ngoại lệ đã được nhường lại:** `음성 받아쓰기` (10–100). Trang audio-to-text liệt kê nó ở mục "Không nên tối ưu → thuộc /ko/voice-to-text". Trang này **lấy làm KW chính**.

**Xử lý khi buộc phải nhắc KW trùng:** chỉ được nhắc **tối đa 1 lần trong body**, và **bắt buộc** kèm internal link sang `/ko/audio-to-text`. Vị trí duy nhất được phép: **section 9** (`음성 받아쓰기와 음성 파일 변환, 무엇을 쓸까요?`) — đúng chỗ bản EN vốn đã so sánh hai công cụ.

---

## Nguyên tắc dùng keyword

- ✅ *đã search* = ưu tiên tuyệt đối, **được phép và nên** đặt vào title / H1 / H2 / meta.
- 🔄 *dịch bổ sung* = **chỉ rải trong body** để phủ ngữ nghĩa, **không** đặt vào title/H1/H2.
- 🚫 8 KW ở bảng trên = **cấm hoàn toàn** ở title/H1/H2; body tối đa 1 lần + internal link.
- Với trang này, do KW đã search quá ít, **H2 được phép dùng KW `🔄 dịch bổ sung` mạnh** (`받아쓰기`, `음성 입력`, `음성 메모`) — vì nếu chỉ bám 7 KW đã search thì không đủ phủ 10 section. Đây là **ngoại lệ riêng cho ko**, không áp dụng cho ngôn ngữ khác.

---

## Search Intent

Người dùng Hàn Quốc vào trang này **chưa có văn bản, và cũng thường chưa có file**. Họ có **lời nói** — hoặc sắp nói ra, hoặc vừa ghi âm bằng 아이폰/갤럭시 음성 메모.

Ba tình huống điển hình:

1. **말로 입력** — Muốn viết nhanh (email, 보고서 초안, 메모) nhưng gõ chậm hơn nói. Cần nói ra và nhận lại chữ để sửa.
2. **음성 메모 정리** — Đã ghi âm một ý tưởng, một cuộc gọi, một buổi họp bằng điện thoại; giờ cần chuyển thành 텍스트 để tìm kiếm và lưu.
3. **실시간 받아쓰기** — Đang trong buổi họp/phỏng vấn, muốn ghi âm ngay trong trình duyệt và có 녹취록 lúc kết thúc.

Kỳ vọng của họ:

- **Ghi âm được ngay trên web**, không cần app (`앱 설치 없이`, `브라우저에서 바로`) — đây là điểm khác biệt lớn nhất so với trang audio-to-text.
- Nhận dạng **tiếng Hàn** tốt, kể cả khi nói nhanh.
- **화자 분리** cho 회의 / 인터뷰.
- Không giới hạn độ dài ghi âm.
- Miễn phí, không tài khoản.

### Khác biệt so với bản tiếng Anh

1. **Bản EN dựa vào sự phân biệt "voice" vs "audio" — tiếng Hàn KHÔNG có sự phân biệt đó.** Cả hai đều là `음성`. Vì vậy bản ko phải phân biệt bằng **hành động**, không bằng danh từ: trang này = `녹음하고 받아쓰기` (ghi âm rồi chép lại), trang kia = `파일을 올려 변환` (tải file lên rồi chuyển đổi). Xuyên suốt `ko.json`, mỗi khi bản EN nói "voice" theo nghĩa đối lập với "audio file", bản ko phải dịch thành **động từ/tình huống** (`직접 녹음한`, `말한 내용`, `직접 말해서`) chứ **không** thành `음성` trơ trọi — nếu không sẽ đè lên trang kia.
2. **`받아쓰기` là từ có sẵn trong đời sống Hàn Quốc** (vốn nghĩa là bài chính tả ở trường tiểu học), nên rất dễ hiểu và dễ nhớ. Nên dùng thẳng, không dịch vòng thành `구술 필기` (quá học thuật, không ai search).
3. **Section 7 (dictation) là section quan trọng nhất của bản ko** — trong bản EN nó chỉ là 1 trong 10 section, nhưng ở bản ko nó mang KW chính. Cần dịch kỹ nhất, dùng `받아쓰기` đậm đặc nhất ở đây.
4. **문화 công sở:** `회의록` (biên bản họp) là nhu cầu cực mạnh ở Hàn. Section 6 (items) là chỗ tự nhiên để nhấn `회의록`, `녹취록` mà không cần thêm câu.
5. **Thể văn:** `합니다`체 lịch sự chuẩn, đồng bộ với `../audio-to-text/ko.json`. Không `해요`체, không `한다`체.

---

## Đối tượng người dùng

- Nhân viên văn phòng cần **회의록** từ buổi họp vừa ghi âm
- Người viết nhiều (마케터, 기획자, 블로거) dùng **음성 입력** để viết nháp nhanh
- Sinh viên ghi âm **강의** rồi chuyển thành ghi chú ôn tập
- Nhà báo / researcher ghi âm **인터뷰** cần 녹취록 có 화자 분리
- Người dùng hay để lại **음성 메모** cho chính mình (ý tưởng, việc cần làm)
- Người gặp khó khăn khi gõ phím (**접근성** — 손목 통증, 시각 장애)
- Người dùng iPhone muốn chuyển 음성 메모 sang text mà không cài app

---

## Map H2 → keyword (bám đúng cấu trúc en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `ko.json` phải dịch đúng **10 section** của `en.json`, cùng số đoạn văn, cùng số item, cùng số step, cùng số dòng specs, cùng **10 FAQ**. Keyword được áp bằng **cách chọn từ ngữ khi dịch**, không bằng cách viết thêm câu hay thêm H2.

| # | H2 (ko) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** 음성 받아쓰기 | 음성 받아쓰기 *(KW chính)* |
| — | **quickAnswer** | 음성 받아쓰기, 음성 텍스트 추출 |
| 1 | 음성 받아쓰기란? | 음성 받아쓰기, 받아쓰기, 음성 인식 |
| 2 | 음성 받아쓰기 한눈에 보기 | *(bảng thông số — 무료 / 100+ / 제한 없음 / 브라우저 녹음)* |
| 3 | 음성을 받아쓰는 방법 | 음성 받아쓰기, 음성 텍스트 추출, 자동 받아쓰기 |
| 4 | 바로 녹음하거나 녹음 파일을 올리세요 | 브라우저 음성 녹음, 실시간 음성 텍스트 변환, 음성 메모 텍스트 변환 |
| 5 | 녹취를 텍스트로 옮기기 | 녹취 텍스트 변환, 녹취록 작성, 음성 텍스트 추출 |
| 6 | 텍스트로 바꿀 수 있는 것들 | 음성 메모 변환, 회의록, 녹취록 작성, 강의 |
| 7 | 받아쓰기로 글쓰기 ⭐ | **음성 받아쓰기**, 말로 입력, 음성 입력, 음성으로 글쓰기, 음성 타이핑 |
| 8 | 정확도와 지원 언어 | 음성 인식, 음성 문자 변환, 음성 자동 텍스트 변환 |
| 9 | 음성 받아쓰기와 음성 파일 변환, 무엇을 쓸까요? | 음성 받아쓰기 + **1 lần duy nhất** nhắc `음성 파일 텍스트 변환` kèm link `/ko/audio-to-text` |
| 10 | 자주 묻는 질문 | 녹음 텍스트 변환 온라인, 음성 텍스트 변환 온라인, 받아쓰기 사이트 + long-tail |
| — | **conclusion** | 음성 받아쓰기, 음성 텍스트 추출, 무료 |

### Ghi chú riêng cho bản ko (KHÔNG tạo section mới)

- **Section 7 là trọng tâm KW chính.** Bản EN gọi là "Voice to Text for Dictation" — bản ko dịch thẳng thành `받아쓰기로 글쓰기` và dồn toàn bộ cụm `말로 입력 / 음성 입력 / 음성 타이핑` vào đây. Không thêm câu, chỉ chọn từ khi dịch 3 đoạn có sẵn.
- **Section 4 giữ độc quyền cho trang này** — bản EN "Record Live or Upload a Recording" là điểm phân biệt mạnh nhất với `/ko/audio-to-text`. Nhấn `브라우저에서 바로 녹음` ngay đoạn đầu.
- **Section 9 là nơi duy nhất** được nhắc KW của trang kia. Bản EN vốn đã có internal link `[Audio to Text](/audio-to-text)` ở đây → đổi thành `/ko/audio-to-text`. Link `[YouTube Transcript](/youtube-transcript)` → `/ko/youtube-transcript`.
- **Cụm `녹취`** (bản ghi chính thức, hàm ý pháp lý/công việc) dồn vào **section 5** và **section 6** — đúng chỗ bản EN nói về transcribe recording. Không dùng ở section 7 (dictation không phải 녹취).
- **`음성 텍스트 변환 온라인`** (0–10) chỉ được xuất hiện **1 lần duy nhất trong FAQ**, vì nó chứa nguyên cụm KW chính của trang kia. Không đặt vào H2/title/meta.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — **KHÔNG** dùng ở title / H1 / H2 của trang này:

- `음성 텍스트 변환`, `음성 파일 텍스트 변환`, `녹음 파일 텍스트 변환`, `녹음 텍스트 변환`, `음성을 텍스트로 변환`, `음성 텍스트 변환 무료`, `음성 텍스트 변환 사이트`, `음성 텍스트 변환기` → **/ko/audio-to-text** *(8 KW đã đóng băng, xem bảng ở trên)*
- `mp3 텍스트 변환`, `오디오 텍스트 변환`, `팟캐스트 텍스트 변환`, `오디오 파일 텍스트 변환` → **/ko/audio-to-text** (trục file/format)
- `유튜브 자막 추출`, `유튜브 텍스트 변환`, `유튜브 자막 다운로드` → **/ko/youtube-transcript**
- `틱톡 자막`, `틱톡 텍스트 변환` → **/ko/tiktok-transcript**
- `동영상 텍스트 변환`, `영상 자막 추출` → **/ko/video-to-text**
- **`텍스트 음성 변환`, `TTS`, `글을 음성으로`, `음성 합성`, `AI 목소리` → trang Text-to-Speech (NGƯỢC intent hoàn toàn)**

> 🚨 **CẢNH BÁO THỨ TỰ TỪ — rà kỹ trước khi commit:**
> | Cụm | Nghĩa | Trang |
> | --- | ----- | ----- |
> | `음성` → `텍스트` (음성 텍스트 변환) | STT — giọng nói ra chữ | trang này & /ko/audio-to-text |
> | `텍스트` → `음성` (텍스트 음성 변환) | **TTS** — chữ ra giọng nói | **trang khác, ngược intent** |
>
> Hai cụm chỉ khác **thứ tự hai từ đầu**. Viết nhầm một lần là trang bị Google hiểu sai intent hoàn toàn. Sau khi viết xong `ko.json`, **grep `텍스트 음성`** để chắc chắn không xuất hiện.

---

## Internal linking

- ↔ **/ko/audio-to-text** — bắt buộc, đặt trong **section 9**. Ngữ cảnh: khi người dùng **đã có sẵn tệp âm thanh** (MP3, 팟캐스트, 다운로드한 인터뷰) thay vì tự ghi âm. Đây là link quan trọng nhất của trang, vừa điều hướng đúng intent vừa gửi tín hiệu phân vai rõ ràng cho Google giữa hai trang trùng lặp nặng.
- → **/ko/youtube-transcript** — trong section 9, khi nguồn thực chất là âm thanh của video.
- ← Nhận link ngược từ `/ko/audio-to-text` (section 10 của trang kia đã trỏ sang `/ko/voice-to-text`).

> 💡 Vì hai trang trùng 8 KW, **cặp internal link hai chiều này là biện pháp chống cannibalization quan trọng nhất**. Anchor text phải mô tả **sự khác biệt về điểm xuất phát**, không được dùng anchor chung chung kiểu `여기` hay `자세히 보기`.

---

## Ghi chú kỹ thuật cho ko.json

- Thể văn: **`합니다`체** lịch sự chuẩn, xuyên suốt. Văn phong tự nhiên như người bản xứ viết, không dịch máy word-by-word.
- **Không chèn khoảng trắng trước trợ từ** (`을/를/로/이/가/에/의`). Lỗi này có sẵn trong `2_loc_kw.md`, đã sửa toàn bộ.
- **Dịch 1:1 tuyệt đối:** đúng 10 sections, đúng 4 đoạn ở section 1, đúng 10 dòng specs ở section 2, đúng 4 steps ở section 3, đúng 3 đoạn ở section 4/5/7/8, đúng 6 items ở section 6, đúng 2 items ở section 9, đúng **10 FAQ**, đúng 2 đoạn conclusion.
- **KHÔNG đổi ví dụ trong bản EN** (voice memo dictated on a walk, ten-second reminder, hour-long discussion... giữ nguyên nội dung, chỉ dịch).
- Tên định dạng file (MP3, WAV, M4A, AAC, FLAC, OGG, TXT, DOCX, PDF, SRT, VTT) và tên thương hiệu (TranscriptX, ChatGPT, Claude, Gemini, Word, Google Docs, Pages, iPhone, YouTube, TikTok) **giữ nguyên Latin**, không phiên âm sang Hangul.
- Số đếm dùng chữ số Latin (100+, 10초, 1시간).
- Internal link trong `sections[8]` giữ nguyên cú pháp markdown, đổi path sang `/ko/audio-to-text` và `/ko/youtube-transcript`.
- Thuật ngữ chuẩn hoá: dictation → `받아쓰기`; speaker separation → `화자 분리`; timestamps → `타임스탬프`; transcript → `녹취록` / `변환된 텍스트` (tuỳ ngữ cảnh); voice memo → `음성 메모`; subtitles → `자막`; record live → `실시간 녹음` / `바로 녹음`.
