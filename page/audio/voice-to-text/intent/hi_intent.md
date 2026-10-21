🔥 TranscriptX – Voice to Text (Hindi / hi)

URL:
/hi/voice-to-text

Intent chính:

Convert Voice to Text Online Free (आवाज़ को टेक्स्ट में बदलें ऑनलाइन, फ्री)

Trang này nhắm đến người dùng Hindi muốn **nói ra là có chữ**: ghi âm trực tiếp trong trình duyệt để đọc chính tả (dictation / "बोल कर लिखना"), hoặc tải lên một bản ghi giọng nói (vॉइस मेमो, tin nhắn thoại, ghi âm cuộc họp trên điện thoại) rồi nhận về văn bản chỉnh sửa được.

Điểm phân biệt cốt lõi với /hi/audio-to-text: **xuất phát điểm là GIỌNG NÓI của chính người dùng** (nói ngay tại chỗ hoặc bản ghi họ tự tạo), không phải một file media có sẵn.

> ⚠️ **CẢNH BÁO PHÂN ĐỊNH — Voice ≠ Audio.** Trang anh em `/hi/audio-to-text` **đã publish và ĐÓNG BĂNG**, dùng chính chuỗi `ऑडियो को टेक्स्ट में बदलें` làm **title + H1**. Đây lại đúng là 1 trong 3 keyword Devanagari của trang Voice này. Để tránh keyword cannibalization: trang Voice **KHÔNG** đặt `ऑडियो को टेक्स्ट में बदलें` vào title/H1/H2 — thay vào đó dùng `आवाज़ को टेक्स्ट में बदलें` (voice) làm H1. Chuỗi `ऑडियो...` chỉ xuất hiện **1 lần trong body ở Section 9** (item so sánh), đúng chỗ dẫn link sang `/hi/audio-to-text`.

---

## Chiến lược Hinglish vs Devanagari (bám bản video-to-text/hi.json đã chốt)

Hindi có 2 tầng viết cho cùng intent: **Devanagari** (chữ Hindi chuẩn, đặt tầng hiển thị) và **Hinglish/Latin** (gõ Latin, người Ấn dùng khi search trên điện thoại). Repo đã chốt chiến lược 2 tầng ở `/hi/video-to-text`:

- **Tầng hiển thị (title/H1/mọi H2/H3/body/FAQ/conclusion) = Devanagari 100%.** Không để chuỗi Hinglish (Latin) lọt vào `hero` / `sections` / `conclusion`.
- **3 cụm Devanagari** đặt ở vị trí trọng số cao:
  - `आवाज़ को टेक्स्ट में बदलें` (voice to text) → **H1**, hero.button, quickAnswer.question, FAQ#1, conclusion.
  - `रिकॉर्डिंग को टेक्स्ट में लिखें` → **H2 Section 5** (biến thể tự nhiên: "आवाज़ रिकॉर्डिंग को टेक्स्ट में लिखें").
  - `ऑडियो को टेक्स्ट में बदलें` → **KHÔNG lên H1/H2** (nhường /hi/audio-to-text); chỉ 1 lần trong body Section 9 kèm internal link.
- **Tầng meta** (`description` / `ogDescription` / `schemaDescription`) chèn **nguyên văn 3 chuỗi Hinglish**:
  - `audio ko text me kaise badle` → description
  - `audio ko likhit me badalna` → description + schemaDescription
  - `bol kar likhne wala app` → ogDescription (và biến thể Devanagari "बोल कर लिखने वाला app" trong FAQ#4 để bắt intent dictation)

**Tỉ lệ search:** Chỉ có **6 keyword** trong `2_loc_kw.md` (3 Hinglish + 3 Devanagari), tất cả volume rất thấp (10–100 hoặc 0–10). Đây là bộ KW **mỏng**. Toàn bộ 6 KW đều được dùng đúng dạng gốc. Phần còn lại của nội dung là **dịch bổ sung** từ bản EN để phủ ngữ nghĩa (vॉइस मेमो, डिक्टेशन, स्पीकर लेबल, ट्रांसक्रिप्ट...).

> 🔎 **Khuyến nghị search bổ sung:** Vì bộ KW quá mỏng và volume thấp, nên chạy thêm keyword research cho các cụm Hindi/Hinglish tiềm năng: `voice typing hindi`, `awaz ko text me kaise badle`, `bol kar likhne wala`, `speech to text hindi`, `आवाज़ से टेक्स्ट`, `बोलकर टाइपिंग` — để xác nhận trục chính và bổ sung long-tail trước khi scale.

---

## Mô tả trang

TranscriptX Voice to Text (Hindi): ghi âm giọng nói trực tiếp trên trình duyệt hoặc tải lên bản ghi giọng nói, tự nhận diện ngôn ngữ trong 100+ ngôn ngữ, gán nhãn người nói, xuất TXT/DOCX/PDF/SRT/VTT. Miễn phí, không đăng ký, không cài đặt, không giới hạn thời lượng.

---

## Từ khóa chính

आवाज़ को टेक्स्ट में बदलें (Devanagari, voice to text) — **H1** *(0–10, dịch chuẩn cho intent Voice)*

Lưu ý: keyword volume cao hơn `audio ko text me kaise badle` (10–100) là **Hinglish** và chứa "audio" → chỉ dùng ở tầng meta, không dùng làm H1 (tránh chồng /hi/audio-to-text).

---

## Từ khóa phụ

| Keyword | Volume | Dạng | Nguồn |
| ------- | ------ | ---- | ----- |
| audio ko text me kaise badle | 10–100 | Hinglish | ✅ đã search — chèn vào `description` |
| bol kar likhne wala app | 10–100 | Hinglish | ✅ đã search — chèn vào `ogDescription` + Devanagari hoá trong FAQ#4 |
| ऑडियो को टेक्स्ट में बदलें | 10–100 | Devanagari | ✅ đã search — **nhường /hi/audio-to-text**, chỉ dùng body Section 9 |
| audio ko likhit me badalna | 0–10 | Hinglish | ✅ đã search — chèn vào `description` + `schemaDescription` |
| आवाज़ को टेक्स्ट में बदलें | 0–10 | Devanagari | ✅ đã search — **H1** + hero.button + quickAnswer + FAQ#1 + conclusion |
| रिकॉर्डिंग को टेक्स्ट में लिखें | 0–10 | Devanagari | ✅ đã search — **H2 Section 5** |

**Tổng: 6 keyword (3 Hinglish + 3 Devanagari), 100% dùng đúng dạng gốc.** Không có nhóm "dịch bổ sung" dạng KW rời — phần bổ sung nằm trong chọn từ khi dịch body.

---

## Search Intent

Người dùng Hindi tìm cụm này đang ở một trong hai trạng thái:

1. **Chưa có chữ, chỉ có ý trong đầu** — muốn nói ra để máy gõ hộ (dictation / voice typing / "बोल कर लिखना"): soạn email, ghi chú nhanh, viết nháp, hoặc người gõ phím chậm.
2. **Đã có bản ghi giọng nói** — vॉइस मेमो, tin nhắn thoại WhatsApp, ghi âm cuộc họp bằng điện thoại — muốn đọc lại dưới dạng chữ thay vì nghe lại.

Kỳ vọng: bấm là ghi âm ngay trên web (không cài app), nhận dạng tốt tiếng Hindi, miễn phí thật, không giới hạn thời lượng, không cần tài khoản, phân biệt người nói, xuất DOCX.

### Khác biệt so với bản tiếng Anh (≥3 điểm)

1. **Phân định Voice/Audio phải chủ động ở tầng chữ Devanagari.** Trong EN, "voice" và "audio" tách nhau tự nhiên. Trong Hindi, `ऑडियो` (audio) và `आवाज़` (voice) người dùng phổ thông dễ coi như đồng nghĩa. Vì `/hi/audio-to-text` đã chiếm `ऑडियो को टेक्स्ट में बदलें` làm H1, trang này phải **kiên quyết dùng `आवाज़`** ở mọi vị trí SEO trọng số cao.
2. **Chiến lược 2 tầng Hinglish/Devanagari** — bản EN không có. Meta layer phải nhồi Hinglish (Latin) vì người Ấn search bằng bàn phím Latin; display layer giữ Devanagari 100%.
3. **Dictation cần diễn đạt theo thói quen Ấn** — "बोल कर लिखना" / "बोलकर लिखवाना" (bol kar likhna) là cách nói tự nhiên, khớp Hinglish KW `bol kar likhne wala app`; thuật ngữ hàn lâm "श्रुतलेखन" bị tránh.
4. **Câu ngôn ngữ (Section 8) thêm nhắc "जिनमें हिंदी भी है"** — trấn an lo ngại "có nhận dạng tiếng Hindi không", giống cách vi.json thêm "trong đó có tiếng Việt". Không thêm câu/H2 mới, chỉ chọn từ khi dịch.

---

## Đối tượng người dùng

- Người bận rộn muốn nói thay vì gõ (email, ghi chú, nháp bài viết)
- Nhân viên văn phòng ghi âm cuộc họp bằng điện thoại
- Nhà báo / phóng viên ghi âm phỏng vấn tại hiện trường
- Sinh viên ghi âm bài giảng để chuyển thành vở ghi
- Content creator viết nháp bằng cách nói ra
- Người gõ phím Hindi chậm (gõ Devanagari/Latin trên điện thoại vốn khó), người khiếm khuyết vận động (accessibility)
- Người nhận nhiều tin nhắn thoại WhatsApp và muốn đọc thay vì nghe

---

## Map H2 → keyword (bám ĐÚNG 10 section của en.json)

> ⚠️ **KHÔNG thêm / bớt / gộp section.** `hi.json` dịch đúng 10 section, cùng số đoạn `content`, cùng số `steps` (4) / `items` (S6=6, S9=2) / `specs` (10), đúng **10 FAQ**. Keyword áp bằng **cách chọn từ khi dịch**, không thêm câu/H2.

| # | H2 (hi) | Keyword nhắm |
| - | ------- | ------------ |
| — | **H1:** आवाज़ को टेक्स्ट में बदलें | `आवाज़ को टेक्स्ट में बदलें` *(KW chính, Devanagari)* |
| — | **quickAnswer** | आवाज़ को टेक्स्ट में कैसे बदलें |
| 1 | आवाज़ को टेक्स्ट में बदलना क्या है? | आवाज़ को टेक्स्ट में बदलना |
| 2 | एक नज़र में वॉइस टू टेक्स्ट | *(bảng thông số — फ्री / 100+ भाषाएँ / कोई सीमा नहीं)* |
| 3 | आवाज़ को टेक्स्ट में कैसे बदलें | आवाज़ को टेक्स्ट में बदलें, ब्राउज़र में रिकॉर्ड |
| 4 | लाइव रिकॉर्ड करें या रिकॉर्डिंग अपलोड करें | ब्राउज़र में लाइव रिकॉर्ड, वॉइस मेमो अपलोड |
| 5 | आवाज़ रिकॉर्डिंग को टेक्स्ट में लिखें | `रिकॉर्डिंग को टेक्स्ट में लिखें` *(Devanagari KW)*, आवाज़ रिकॉर्डिंग ट्रांसक्रिप्ट |
| 6 | आप क्या-क्या टेक्स्ट में बदल सकते हैं | वॉइस मेमो, मीटिंग, इंटरव्यू, डिक्टेशन |
| 7 | डिक्टेशन के लिए वॉइस टू टेक्स्ट | बोलकर लिखवाना (bol kar likhna), वॉइस टाइपिंग |
| 8 | सटीकता और भाषाएँ | हिंदी नाम-पहचान, 100+ भाषाएँ |
| 9 | वॉइस टू टेक्स्ट या ऑडियो टू टेक्स्ट? | **1 lần** `ऑडियो को टेक्स्ट में बदलें` + internal link `/hi/audio-to-text`, `/hi/youtube-transcript` |
| 10 | अक्सर पूछे जाने वाले सवाल | आवाज़ को टेक्स्ट में फ्री, `बोल कर लिखने वाला app` (FAQ#4) + long-tail |
| — | **conclusion** | अपनी आवाज़ को फ्री में टेक्स्ट में बदलें |

### Ghi chú riêng cho bản hi (KHÔNG tạo section mới)

- 3 Hinglish chỉ ở meta; nếu lọt vào tầng hiển thị Devanagari sẽ bị coi là lỗi.
- `ऑडियो को टेक्स्ट में बदलें` chỉ 1 lần duy nhất — body Section 9, item 2, đúng chỗ dẫn sang trang audio-to-text.
- Lo ngại "nhận dạng tiếng Hindi" xử lý **bên trong Section 8**, không thêm câu.
- Nukta nhất quán: `ऑडियो, आवाज़, ज़्यादा, फ़ाइल, फ़ॉर्मैट, फ़ोन, फ़्री→फ्री`.
- Giữ Latin: TranscriptX, TXT, DOCX, PDF, SRT, VTT, MP3, ChatGPT, Claude, Gemini, YouTube, app.

---

## Không nên tối ưu cho các keyword

Thuộc landing page khác — KHÔNG dùng ở trang này ở vị trí SEO trọng số cao:

- `ऑडियो को टेक्स्ट में बदलें` (title/H1), `ऑडियो फ़ाइल को टेक्स्ट में`, `MP3 को टेक्स्ट`, `पॉडकास्ट ट्रांसक्राइब` → **/hi/audio-to-text (đã đóng băng, file có sẵn)**. Trang này chỉ nhắc 1 lần trong body kèm link.
- `वीडियो को टेक्स्ट में बदलें` → **/hi/video-to-text**
- `YouTube ट्रांसक्रिप्ट` / `वीडियो के सबटाइटल डाउनलोड` → **/hi/youtube-transcript**
- Nhóm **TTS ngược intent** (`टेक्स्ट को आवाज़ में बदलें`, `text to speech hindi`, `टेक्स्ट टू स्पीच`) → **trang Text-to-Speech**. Bộ KW Hindi ở `2_loc_kw.md` KHÔNG bị nhiễm TTS (khác bản vi), nhưng vẫn cấm tuyệt đối chuỗi "टेक्स्ट को आवाज़/स्पीच में".

---

## Internal linking

- → `/hi/audio-to-text` (khi người dùng đã có sẵn file media như podcast, MP3 — **1 link duy nhất** ở Section 9, item 2)
- → `/hi/youtube-transcript` (khi bản ghi thực chất là tiếng của một video — Section 9, item 2)
- ← nhận link ngược từ `/hi/audio-to-text` nếu trang đó có trỏ sang (kiểm tra khi rà internal link tổng thể).

Cả 2 link đều nằm ở Section 9 (index 8), đúng vị trí của bản EN (chỉ Section 9 có link trong en.json).

---

## Ghi chú kỹ thuật cho hi.json

- Cấu trúc JSON khớp 100% `en.json`: **10 section**, đúng số đoạn `content`, `steps` (S3=4), `items` (S6=6, S9=2, S10=10 FAQ), `specs` (S2=10), conclusion.content=2.
- **specs S2:** tái dùng nhãn của `/hi/audio-to-text/hi.json` cho đồng bộ (कीमत, अकाउंट ज़रूरी, इंस्टॉलेशन, भाषाएँ, स्पीकर की पहचान, टाइमस्टैम्प, एक्सपोर्ट फ़ॉर्मैट, डिवाइस). Hai nhãn KHÁC vì spec Voice ≠ Audio: `इनपुट` (Input, thay "फ़ाइल साइज़ की सीमा") và `रिकॉर्डिंग की लंबाई की सीमा` (Recording length limit).
- Internal link Section 9 giữ cú pháp markdown, path `/hi/`: `[ऑडियो टू टेक्स्ट](/hi/audio-to-text)`, `[YouTube ट्रांसक्रिप्ट](/hi/youtube-transcript)`.
- Xưng **आप**, văn phong tự nhiên. Không dịch máy word-by-word. Giữ nguyên ví dụ EN (voice memo lúc đi bộ, họp ghi trên điện thoại, tin nhắn thoại...).
- **Kiểm tra bắt buộc:**
  - `shape_check.py en.json hi.json` → `hi.json -> True`
  - grep 3 chuỗi Hinglish → chỉ hiện trong `seo.description/ogDescription/schemaDescription`, **0 hit** trong `hero`/`sections`/`conclusion`.
  - grep `/hi/audio-to-text` và `/hi/youtube-transcript` → mỗi cái 1 hit, đúng Section 9.
