# Brief + bài hoàn chỉnh: medical transcription

Theo mẫu `page/blog/template_blog.md`. Mục 1–10 là cài đặt và ghi chú (tiếng Việt), mục 11 là bài viết tiếng Anh, sẵn sàng tạo bài trên CMS. Thân bài **chỉ dùng chữ** (bảng, danh sách, mẫu transcript thay cho ảnh chụp màn hình). Ảnh bìa / ảnh share nằm trong `images/`.

---

## 1. Từ khóa chính

```
Keyword: medical transcription
```

Volume (Keyword Planner, user gửi 2026-11-06): 10N–100N.

⚠️ Trang tool `/medical-transcription/` nhắm **"medical transcription software"** (ý định dùng ngay, H1 "AI Medical Transcription Software"). Bài blog nhắm cụm gốc **"medical transcription"** với ý định **tìm hiểu** ("what is it", so sánh scribe, chi phí dịch vụ), rồi dẫn traffic về trang tool. Không dùng "medical transcription software" làm H2 trong bài.

## 2. Danh sách từ khóa phụ

```
* medical transcription what is it          1N–10N
* medical transcription vs medical scribe   10–100
* medical scribe vs medical transcriptionist 10–100
* medical transcription cost per line       10–100
  medical transcribe                        10N–100N
  medical transcription services            1N–10N
  healthcare transcription services         1N–10N
  medical transcription companies           100–1N
  medical dictation                         100–1N
  ai medical transcription                  100–1N   (chỉ 1 lần, link về trang tool)
  radiology transcription                   100–1N
  radiology terms medical transcription     10–100
  medical speech to text                    100–1N
```

Không dùng: soap note generator (TranscriptX không tự viết SOAP), medical scribe software, radiology dictation systems, radiology typing, các biến thể tìm việc (jobs, remote, certification, course). Dragon chỉ dùng trong bài so sánh riêng "Best Medical Dictation Software".

## 3. Góc nhìn và thông điệp chính

```
Góc: SERP "medical transcription" toàn trang bán dịch vụ người chép và trang tuyển việc. Không ai giải thích gọn
medical transcription bây giờ chạy thế nào khi đã có AI: ai đọc, ai chép, ai soát, khác medical scribe ở đâu,
dịch vụ tính tiền theo dòng là sao. Bài trả lời thẳng các câu đó, rồi chỉ cách tự làm bản nháp AI và soát
những chỗ nguy hiểm (tên thuốc đọc giống nhau, liều/đơn vị, trái/phải, câu phủ định). Nói thật về HIPAA.
```

## 4. Tool TranscriptX muốn dẫn tới

```
Tool: medical-transcription
```

⚠️ `medical-transcription` chưa có trong danh sách tool của CMS. Trang `/medical-transcription/` phải lên web trước khi đăng bài; nếu CMS chưa có slug này thì khối tool tạm dùng `audio-to-text`, link trong bài vẫn trỏ `/medical-transcription/`.

## 5. Chuyên mục (topic)

```
Topic: guides
```

## 6. Loại bài

```
Loại: explainer + how-to   (phần các bước dùng khối steps → HowTo schema)
```

## 7. Ảnh chụp màn hình

```
Thân bài không dùng ảnh (tối ưu bằng chữ như bài finance, user yêu cầu 2026-11-06).
Thay ảnh bằng: 1 mẫu transcript (khối code), 1 bảng soát lỗi y khoa, 1 bảng transcription vs scribe, 1 bảng các cách làm.

Ảnh share (1 ảnh duy nhất, không chèn vào thân bài):
  images/what-is-medical-transcription-share.png   2400×1260 PNG → dùng cho cả ô "Ảnh bìa" và og:image (Facebook, Zalo, X, LinkedIn, Slack)
Alt: "Celexa or Celebrex? A dictated medical note transcribed in TranscriptX with timestamps"
```

## 8. Ngôn ngữ

```
Ngôn ngữ gốc: en
Dịch thêm: (chỉ dịch khi user duyệt bản EN)
```

## 9. Đăng bài

```
Đăng: draft
```

## 10. Ghi chú thêm

- **Tác giả:** Tori Trinh. **Người duyệt:** TranscriptX Team.
- **Mục lục:** bật tự động (lấy từ H2/H3).
- **Excerpt** (EN, 200 ký tự):
  ```
  What medical transcription is, how it works now that AI does the first draft, how it differs from a medical scribe, how services charge per line, and what to check before a medical transcript is used.
  ```
- **Ảnh bìa / share:** hook kiểu thumbnail YouTube. Kicker "Dictated note" + chữ lớn **"Celexa"** + cam **"or Celebrex?"** (cặp thuốc tên đọc giống nhau, có trong danh sách sound-alike phổ biến). Hình: màn hình transcript thật sau khi Record (`_source/record/recording-transcript-result.png`), giữ nguyên giao diện và timestamp, chỉ thay chữ thành một ghi chú khám bệnh đọc chính tả (bịa, không có bệnh nhân thật, có nhắc Celexa) để ảnh khớp chủ đề. Script: `_source/_tools/build_cover_medical.py`.
- **Được nói (user xác nhận 2026-11-06):** TranscriptX dùng speech model đã train cho thuật ngữ y khoa, tên thuốc, liều; cả Free và Pro. Được dùng chữ "accurate". Không nêu tên đối tác model.
- **Không được nói:** không HIPAA / BAA / SOC 2; không % chính xác; không "best / most accurate"; không tích hợp EHR; không tự viết SOAP note; không bot vào cuộc khám; không viết Summary/Mind map như đã có; không ghi giá/credit/dung lượng (link `/pricing/`); nhận diện người nói + Speak live = **Pro**; không nêu giá dịch vụ theo dòng (chỉ nói cách tính).
- **Nguồn số liệu:** "about four hours to type one hour of audio" từ trang Pricing (`_source/pricing/`).
- **Cần kiểm chứng:**
  - TranscriptX có ký BAA không (bài đang viết "does not claim HIPAA compliance").
  - Câu quyền riêng tư (tự xoá file upload, không train AI, xoá dữ liệu bất cứ lúc nào) lấy từ `/interview-transcription/`.
  - Chuẩn ghi liều thuốc trong mục "How Accurate…": danh sách "Do Not Use" của The Joint Commission (U, IU, Q.D., Q.O.D., số 0 ở cuối, thiếu số 0 ở đầu, MS/MSO4/MgSO4) và khuyến nghị của ISMP. Kiến thức chung, viết ở mức phổ biến, không trích nguyên văn.
  - Kiến thức ngành: "line" thường tính 65 ký tự kể cả dấu cách; quy trình MT/speech recognition editing; ambient AI scribe. Đây là kiến thức chung, cách tính dòng khác nhau theo hợp đồng.
- **Link nội bộ:** `/medical-transcription/` (chính), `/interview-transcription/`, `/real-time-speech-to-text/`, `/blog/how-long-to-transcribe-1-hour-of-audio/`, `/pricing/`, `/privacy-policy/`.

---

## 11. Bài viết

**Slug**
```
what-is-medical-transcription
```

**Công cụ chính / Chủ đề / Thẻ:** Medical Transcription (tạm: Audio to Text) / Guides / medical, dictation, healthcare transcription

# What Is Medical Transcription and How Does It Work?

**Lede:** Learn who dictates, who types and who checks a medical transcript today, how it differs from a medical scribe, and how to make a safe first draft with AI.

> **Quick answer:** Medical transcription turns spoken healthcare recordings, such as dictated visit notes, radiology reports and patient interviews, into written text. Today it usually starts with an AI draft: upload or dictate the recording in [TranscriptX Medical Transcription](/medical-transcription/), which is trained on medical terminology, then check drug names, doses, sides and negatives against the audio before use.

Medical transcription used to mean one thing: a doctor dictated into a recorder, and a trained medical transcriptionist typed it up. That still happens, but most of the typing has moved to speech recognition. The human part has moved from typing to checking.

This guide explains what medical transcription covers, the three ways it is done now, how it compares with a medical scribe, how medical transcription services charge, and which words you must check before a transcript goes anywhere.

## What Does Medical Transcription Mean?

Medical transcription is the process of turning spoken medical information into a written document. To medical transcribe a recording is to write out what was said, word for word or in a set report format, so it can be read, edited, filed and searched.

The recordings usually come from:

- **Dictated notes and letters:** visit notes, referral letters, discharge summaries and operative notes, dictated after the appointment.
- **Radiology and pathology dictations:** reports read aloud while the specialist looks at the images or slides.
- **Patient and expert interviews:** qualitative research, case studies and audits.
- **Lectures and meetings:** grand rounds, teaching sessions, case conferences and medical webinars.
- **Health content:** medical podcasts and patient education videos that need text or captions.

The person who does the work is a **medical transcriptionist** (often now called a healthcare documentation specialist). Their job is less about typing speed and more about knowing medical terms, drug names, abbreviations and report formats well enough to spot what is wrong.

## How Does Medical Transcription Work Today?

There are three common workflows. The difference is who makes the first draft and who checks it.

| Workflow | First draft | Who checks it | Typical use |
|---|---|---|---|
| Traditional transcription | A medical transcriptionist types from the audio | The transcriptionist, then the clinician signs | Complex dictations, organizations with an existing service |
| Speech recognition + editing | Software turns the dictation into text | A transcriptionist edits it, or the clinician edits it directly | Most dictation today, including radiology |
| AI draft you review yourself | An AI tool trained on medical terms, such as TranscriptX | You, against the recording | Notes, research interviews, lectures, talks |

The second and third rows are what people mean by **medical speech to text**. The speech recognition part is fast. The value is in the checking, because a fluent sentence with one wrong drug name is worse than an obvious typo.

### Medical Dictation vs Medical Transcription

**Medical dictation** is the speaking part: the clinician says the note out loud. **Medical transcription** is the writing part: turning that dictation into text. With live speech recognition, the two happen at the same time and the words appear while you talk.

## How to Transcribe a Medical Recording with AI

You can make a first draft yourself in a few minutes. TranscriptX uses a speech model trained on medical terminology, including drug names, doses and clinical language, so the draft starts close to right. The checking step is still the one that matters.

1. **Add the recording.** Open [Medical Transcription](/medical-transcription/) and click **Upload** to pick a file from your device, Google Drive, Dropbox or OneDrive. For a lecture or talk already online, paste the video link. To dictate a note now, click **Record** and keep the page open while you speak.
2. **Get the transcript.** TranscriptX detects the language and writes out the recording as paragraphs, each with a timestamp.
3. **Check it against the audio.** Play the recording beside the text and click **Edit** to correct drug names, doses, sides and negatives. Use the **Notes** tab for follow-ups or to draft your note in your own format.
4. **Copy or download.** Click **Copy** to paste the text into your note or document, or click the download button next to it to save it as .docx, .pdf or .txt.

On the [Pro plan](/pricing/), TranscriptX also labels speakers in interviews and consultations, and [Speak live](/real-time-speech-to-text/) shows the words as you dictate.

Typing one hour of audio by hand takes about four hours. With an AI draft, most of that time goes into checking instead. See [how long it takes to transcribe one hour of audio](/blog/how-long-to-transcribe-1-hour-of-audio/) for the full comparison.

## What a Medical Transcript Looks Like

A dictated note becomes useful when it has a short header and clear sections. Here is a format you can copy. The patient details are made up.

```
Document:   Clinic visit note (dictated)
Date:       2026-11-06
Dictated by: Dr. A. Example, Internal Medicine
Source:     recording-2026-11-06-0915.webm

[00:00] Patient is a 54-year-old seen for follow-up of hypertension.
        Denies chest pain or shortness of breath.
[00:21] Current medications: lisinopril 10 mg by mouth once daily.
        Blood pressure today 138 over 86.
[00:45] Assessment: hypertension, improving.
        Plan: continue lisinopril 10 mg by mouth once daily,
        recheck blood pressure in 3 months.
```

Keep the timestamps while you review. When a word looks wrong, the timestamp takes you straight to the moment in the recording.

## How Accurate Is AI Medical Transcription?

Accuracy depends on two things: a speech model that knows medical language, and a recording it can hear clearly. General speech-to-text is trained mostly on everyday speech, so it tends to turn rare drug names into common words. TranscriptX uses a speech model trained on medical terminology, including drug names, doses and clinical language, on both the Free and Pro plans.

The model does its part; good dictation habits do the rest:

- **Use a quiet room and a close microphone.** Background noise and a phone held at arm's length cause more errors than any medical term.
- **Spell rare or new drug names** the first time you say them, especially brand names that sound like others.
- **Say every dose in full:** drug, strength, unit, route and frequency, for example "lisinopril ten milligrams by mouth once daily".
- **Say units as words.** "Micrograms" and "milligrams" are clearer than "mcg" and "mg" when spoken.
- **Say "point" for decimals** and pause between numbers, for example "zero point five milligrams".
- **Avoid abbreviations you wouldn't write.** Say "once daily", not "q.d.", and "units", not "U".

### How Should Doses Be Written in a Medical Transcript?

Write each medication in the same order every time, using the format clinicians and pharmacists expect:

| Part | Example |
|---|---|
| Drug name | Lisinopril |
| Strength and unit | 10 mg |
| Route | by mouth |
| Frequency | once daily |
| Duration or quantity, if given | for 30 days |

When you review the transcript, also apply the safe-writing rules most hospitals follow, based on The Joint Commission's "Do Not Use" list and ISMP recommendations:

- **No trailing zero:** write 5 mg, not 5.0 mg, which can be misread as 50 mg.
- **Always a leading zero:** write 0.5 mg, not .5 mg, which can be misread as 5 mg.
- **Write "units" in full,** not "U" or "IU", which can be misread as 0 or IV.
- **Write "daily" and "every other day" in full,** not "Q.D." or "Q.O.D.".
- **Write the drug name in full,** not "MS" or "MSO4", which can mean morphine or magnesium sulfate.

The transcript records what was said, so never change a dose to what you think it should be. If a dose sounds wrong, flag it for the clinician who dictated it.

## Radiology Transcription and Medical Terms to Double-Check

Even with a model trained on medical terms, a careful review is part of the standard. In medical and radiology transcription, the risk sits in a small set of words that sound alike or are easy to drop. Give each of these a second listen:

| What to check | Example | Why it matters |
|---|---|---|
| Drug names that sound alike | Celexa / Celebrex, hydroxyzine / hydralazine | A different drug, not a typo |
| Doses and units | 15 / 50, mg / mcg | A tenfold or thousandfold difference |
| Frequency | "twice daily" / "twice weekly" | Changes how the drug is taken |
| Left and right | left kidney / right kidney | Wrong side on a finding or procedure |
| Negatives | "no fracture" / "fracture" | One short word flips the finding |
| Measurements | 1.5 cm / 15 mm / 5 cm | Changes size, follow-up or staging |
| Abbreviations | MS, HTN, qd | Some have more than one meaning |
| Names and numbers | patient name, date of birth, lab values | Wrong person or wrong result |

For radiology terms in medical transcription, also check anatomy words that sound alike (ileum and ilium, perineal and peroneal) and every measurement against the images. The radiologist still reviews and signs the report.

## Medical Transcription vs Medical Scribe: What's the Difference?

A medical transcriptionist works **from a recording, after the visit**. A medical scribe works **during the visit**, writing the note in the health record while the clinician talks with the patient. Ambient AI scribes do the same with software that listens in the room and drafts the note.

| | Medical transcriptionist | Medical scribe |
|---|---|---|
| When | After the visit, from a recording | During the visit, live |
| Where | Remote, from audio files | In the room, or remote over video |
| Output | A transcript or formatted report | A note entered in the health record |
| Who speaks | The clinician dictates for the record | The clinician talks with the patient |
| AI version | Speech recognition + editing | Ambient AI scribe connected to the record |

In short, medical scribe vs medical transcriptionist comes down to timing. If you already have a recording, you need transcription. If you want the note written while the visit happens, you need a scribe.

## Medical Transcription Services: How Do They Charge?

Medical transcription services and companies usually bill in one of two ways:

- **Per line.** A line is often defined as a set number of characters, commonly 65, including spaces. Check how your contract counts lines, because headers, spaces and blank lines may or may not count.
- **Per audio minute.** You pay for the length of the recording, whatever the length of the text.

Price also depends on turnaround time, audio quality, the specialty and whether the service formats the report into your template. Healthcare transcription services that handle patient data in the United States are also expected to sign a Business Associate Agreement under HIPAA.

A service makes sense when you need someone else to check the text, or a high volume of formatted reports. For notes, research interviews, lectures and talks, an AI draft you review yourself is often enough and much faster.

## Is Medical Transcription Safe for Patient Data?

Recordings that identify patients are protected health information in many countries, so the tool matters.

- **Check your organization's policy** on which tools may handle patient data.
- **Know the tool's status.** TranscriptX does not claim HIPAA compliance. If you need a HIPAA-compliant service with a signed Business Associate Agreement, use one that provides it.
- **Remove identifiers when you can.** Dictate without names and dates of birth, or remove them before uploading.
- **Get consent** before recording a consultation or interview.

TranscriptX deletes uploaded files automatically, does not use your recordings or transcripts to train AI models, and lets you delete transcripts at any time. See the [Privacy Policy](/privacy-policy/). Lectures, talks and de-identified research interviews are the easy place to start.

## Frequently Asked Questions

### Is medical transcription being replaced by AI?

The typing is. Speech recognition now makes most first drafts, and the work has shifted to editing and checking, which still needs someone who knows medical terms.

### How accurate is TranscriptX with drug names and doses?

TranscriptX uses a speech model trained on medical terminology, so it recognizes drug names, doses and clinical terms that general speech-to-text often gets wrong. On a clear recording you get accurate text; check doses and rare names against the audio before the note is signed.

### How long does it take to transcribe one hour of medical audio?

Typing it by hand takes about four hours. An AI draft takes seconds to minutes, plus the time you spend checking it.

### Can I try AI medical transcription for free?

Yes. TranscriptX is free every day, and you can try it without an account. Speaker labels and Speak live are on the [Pro plan](/pricing/).

### Is TranscriptX HIPAA compliant?

No, TranscriptX does not claim HIPAA compliance. For recordings with patient identifiers, follow your organization's rules or remove the identifiers before uploading.

### Can TranscriptX write a SOAP note from the transcript?

No. It gives you the transcript with timestamps. You can write your SOAP note in the Notes tab beside it and copy it into your record.

### Does TranscriptX join telehealth or Zoom calls?

No. Record the session with consent, then upload the recording file afterwards.

## Start Your First Medical Transcription

A safe medical transcript comes from a clear recording, a fast first draft and a careful check of every drug, dose, side and negative. Let AI do the typing, keep the timestamps so every word can be traced back to the audio, and spend your time on the checking.

Upload a dictation, interview or lecture to [Medical Transcription](/medical-transcription/), or press **Record** and dictate. For research interviews, see [Interview Transcription](/interview-transcription/).

**CTA → tool:** `medical-transcription` (tạm `audio-to-text`) · text: "Transcribe your first dictation"

### SEO

**Meta title** (51)
```
What Is Medical Transcription? How It Works with AI
```

**Meta description** (144)
```
Medical transcription explained: how it works with AI, medical transcription vs medical scribe, how services charge per line, and what to check.
```

**Focus keyword**
```
medical transcription
```

**Secondary keywords**
```
medical transcription what is it
medical transcribe
medical transcription vs medical scribe
medical scribe vs medical transcriptionist
medical transcription cost per line
medical transcription services
healthcare transcription services
medical transcription companies
medical dictation
ai medical transcription
radiology transcription
radiology terms medical transcription
medical speech to text
medical transcriptionist
```
