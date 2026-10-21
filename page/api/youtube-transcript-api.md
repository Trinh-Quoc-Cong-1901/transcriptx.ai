<!--
SEO
- URL: /api/youtube-transcript
- Title (≤60): YouTube Transcript API – Captions + AI Fallback | TranscriptX
- Meta: Get any YouTube transcript with one API call. 100+ languages, timestamps, speaker labels, SRT/VTT export, and AI transcription when a video has no captions.
- Keyword chính: youtube transcript api
- Keyword phụ: youtube captions api, youtube subtitles api, youtube video to text api, youtube transcript api python, youtube transcript api javascript, youtube transcript api blocked
- Schema: WebAPI + FAQPage + BreadcrumbList
- Breadcrumb: Home › API › Speech to Text › YouTube Transcript API

CẦN DEV XÁC NHẬN TRƯỚC KHI ĐĂNG (code là ví dụ, các giá trị này đang là giả định):
- Base URL `https://api.transcriptx.ai/v1`, header `Authorization: Bearer`
- Tên endpoint `POST /transcribe`, `GET /transcripts/{id}`, `GET /transcripts/{id}/export`
- Tên tham số và field response, các mã lỗi
- Free tier (100 request/tháng), rate limit (60 request/phút), cách tính credit
- URL MCP server cho Cursor / Claude Code
Thông tin đã là thật (lấy từ transcriptx.ai và connector TranscriptX đang chạy):
100+ ngôn ngữ tự nhận diện, gắn nhãn người nói, bật/tắt timestamp, xuất TXT/DOCX/PDF/SRT/VTT,
không xử lý video private/unlisted/cần đăng nhập, hỗ trợ YouTube/TikTok/Facebook/Instagram/Vimeo/X/LinkedIn/Twitch/Dailymotion/Reddit,
các tool MCP: transcribe, upload_file, get_transcript, list_sessions, get_session.
-->

# YouTube Transcript API

Get the transcript of any public YouTube video with one HTTP request. TranscriptX returns the video's captions when they exist. When they don't, it transcribes the audio with AI, so every public video gives you text back.

```bash
curl -X POST https://api.transcriptx.ai/v1/transcribe \
  -H "Authorization: Bearer $TRANSCRIPTX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

[Get a free API key](#) · [Open the playground](#) · [Full API reference](#)

**What you get**

- **Captions, with AI as backup.** Uploaded and auto-generated captions come back in about a second. Videos without captions are transcribed from the audio.
- **100+ languages.** The language is detected automatically, or you can name the one you want.
- **Timestamps on every segment**, plus **speaker labels** for interviews, podcasts and panels.
- **Export formats:** JSON, plain text, SRT and VTT from the API. DOCX and PDF are available in the web app.
- **One API for every source.** The same endpoint takes TikTok, Instagram, Facebook, X, Vimeo, LinkedIn, Twitch, Dailymotion and Reddit links, plus audio and video files.
- **No proxies to run.** Requests come from our infrastructure, so you never see YouTube's IP blocks.

---

## Quickstart

You'll have a transcript in under five minutes.

### 1. Get your API key

1. Sign in at [transcriptx.ai](https://transcriptx.ai) and open **Dashboard → API keys**.
2. Click **Create key** and copy it. It starts with `tx_live_` and is shown only once.
3. Store it in an environment variable. Don't put it in your code:

```bash
# macOS / Linux
export TRANSCRIPTX_API_KEY="tx_live_xxxxxxxxxxxxxxxx"

# Windows (PowerShell)
$env:TRANSCRIPTX_API_KEY="tx_live_xxxxxxxxxxxxxxxx"
```

The free plan includes **100 requests per month** and needs no credit card.

### 2. Send your first request

Pick your language. Each example below is a complete file that you can save and run.

#### cURL

```bash
curl -X POST https://api.transcriptx.ai/v1/transcribe \
  -H "Authorization: Bearer $TRANSCRIPTX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "timestamps": true
  }'
```

#### Python

Install the only dependency:

```bash
pip install requests
```

Save this as `transcript.py`:

```python
import os
import time
import requests

API_KEY = os.environ["TRANSCRIPTX_API_KEY"]
BASE_URL = "https://api.transcriptx.ai/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def get_transcript(video_url, **options):
    """Request a transcript and wait until it is ready."""
    response = requests.post(
        f"{BASE_URL}/transcribe",
        headers=HEADERS,
        json={"url": video_url, **options},
        timeout=60,
    )
    response.raise_for_status()
    job = response.json()

    # Videos with captions return "completed" right away.
    # Videos without captions are transcribed by AI, so poll until done.
    while job["status"] in ("queued", "processing"):
        time.sleep(3)
        response = requests.get(
            f"{BASE_URL}/transcripts/{job['id']}", headers=HEADERS, timeout=30
        )
        response.raise_for_status()
        job = response.json()

    if job["status"] == "failed":
        raise RuntimeError(job["error"]["message"])
    return job


if __name__ == "__main__":
    result = get_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    print(f"Title:    {result['source']['title']}")
    print(f"Language: {result['language']}")
    print(f"Method:   {result['method']}")  # "captions" or "ai"
    print()
    for seg in result["segments"]:
        print(f"[{seg['start']:>7.2f}s] {seg['text']}")
```

Run it:

```bash
python transcript.py
```

#### JavaScript (Node.js 18+)

No packages needed, because Node 18 has `fetch` built in. Save this as `transcript.mjs`:

```javascript
const API_KEY = process.env.TRANSCRIPTX_API_KEY;
const BASE_URL = "https://api.transcriptx.ai/v1";
const headers = {
  Authorization: `Bearer ${API_KEY}`,
  "Content-Type": "application/json",
};

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getTranscript(videoUrl, options = {}) {
  let res = await fetch(`${BASE_URL}/transcribe`, {
    method: "POST",
    headers,
    body: JSON.stringify({ url: videoUrl, ...options }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  let job = await res.json();

  // Poll while the AI fallback is transcribing the audio.
  while (job.status === "queued" || job.status === "processing") {
    await sleep(3000);
    res = await fetch(`${BASE_URL}/transcripts/${job.id}`, { headers });
    if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
    job = await res.json();
  }

  if (job.status === "failed") throw new Error(job.error.message);
  return job;
}

const result = await getTranscript("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
console.log(`${result.source.title} (${result.language}, via ${result.method})\n`);
for (const seg of result.segments) {
  console.log(`[${seg.start.toFixed(2)}s] ${seg.text}`);
}
```

Run it:

```bash
node transcript.mjs
```

### 3. Read the response

```json
{
  "id": "trx_8f3k2m9q",
  "status": "completed",
  "method": "captions",
  "language": "en",
  "source": {
    "platform": "youtube",
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "video_id": "dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Video)",
    "duration": 213
  },
  "segments": [
    { "start": 18.64, "end": 21.88, "speaker": null, "text": "We're no strangers to love" },
    { "start": 22.64, "end": 26.92, "speaker": null, "text": "You know the rules and so do I" }
  ],
  "text": "We're no strangers to love You know the rules and so do I ...",
  "created_at": "2026-10-08T09:12:44Z"
}
```

| Field | Type | Description |
|---|---|---|
| `id` | string | Transcript ID. Use it to poll, export or fetch the transcript again later. |
| `status` | string | `queued`, `processing`, `completed` or `failed`. |
| `method` | string | `captions` if YouTube captions were used, `ai` if the audio was transcribed. |
| `language` | string | ISO 639-1 code of the transcript language. |
| `source` | object | Platform, URL, video ID, title and duration in seconds. |
| `segments` | array | Timed lines with `start` and `end` in seconds, plus `speaker` and `text`. |
| `text` | string | The full transcript as one string, ready to send to an LLM. |

---

## Request parameters

`POST /v1/transcribe`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | string | **required** | A YouTube link in any form: `watch?v=`, `youtu.be/`, `/shorts/`, `/live/` or `/embed/`. |
| `language` | string | auto | The transcript language you want, for example `en`, `vi` or `ja`. If the video has captions in that language, those are used. Otherwise the AI transcribes the audio in that language. |
| `mode` | string | `auto` | `auto` uses captions first and AI as backup. `captions` returns captions only and fails if there are none. `ai` always transcribes the audio, which is useful when auto-captions are poor. |
| `timestamps` | boolean | `true` | Set to `false` to receive only `text` without segments. |
| `speaker_labels` | boolean | `false` | Labels each segment with `Speaker 1`, `Speaker 2` and so on. This forces `mode: ai`. |

**Which mode should I use?**

- Building a chatbot or RAG index? Keep `auto`. It's fast, and every video returns text.
- Need the exact wording the creator approved? Use `captions`.
- Transcribing interviews or podcasts? Use `ai` with `speaker_labels: true`.

---

## Export as SRT, VTT or plain text

Every completed transcript can be downloaded as a subtitle or text file:

```bash
curl "https://api.transcriptx.ai/v1/transcripts/trx_8f3k2m9q/export?format=srt" \
  -H "Authorization: Bearer $TRANSCRIPTX_API_KEY" \
  -o video.srt
```

`format` accepts `srt`, `vtt` or `txt`. The output looks like this:

```
1
00:00:18,640 --> 00:00:21,880
We're no strangers to love

2
00:00:22,640 --> 00:00:26,920
You know the rules and so do I
```

---

## Batch: transcribe many videos

This script reads a list of URLs and writes one `.srt` file per video. It runs four requests at a time, which stays well under the rate limit. Save it as `batch.py`, put your links in `videos.txt` (one per line), then run `python batch.py`.

```python
import os
from concurrent.futures import ThreadPoolExecutor

import requests

from transcript import BASE_URL, HEADERS, get_transcript


def save_srt(video_url):
    job = get_transcript(video_url)
    srt = requests.get(
        f"{BASE_URL}/transcripts/{job['id']}/export",
        headers=HEADERS,
        params={"format": "srt"},
        timeout=30,
    )
    srt.raise_for_status()
    filename = f"out/{job['source']['video_id']}.srt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(srt.text)
    return filename


os.makedirs("out", exist_ok=True)
with open("videos.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

with ThreadPoolExecutor(max_workers=4) as pool:
    for url, result in zip(urls, pool.map(save_srt, urls)):
        print(f"✓ {url} → {result}")
```

---

## Use it with AI agents (MCP)

TranscriptX runs an MCP server, so Claude and other MCP clients can fetch transcripts without any code. Your agent gets these tools:

| Tool | What it does |
|---|---|
| `transcribe` | Transcribe a link from YouTube, TikTok, Instagram, X, a podcast, a direct media URL, or a shared Google Drive, Dropbox or OneDrive file. |
| `upload_file` | Transcribe an audio or video file from the user's device. |
| `get_transcript` | Get a finished transcript, or check its progress, by ID. |
| `list_sessions` / `get_session` | Browse and reopen transcripts saved in the user's library. |

**Claude (claude.ai and Claude Desktop):** open **Settings → Connectors**, add **TranscriptX**, and sign in. Then ask *"Summarize this video: https://youtu.be/…"*.

**Cursor, Claude Code and other MCP clients:** add the server to your MCP config:

```json
{
  "mcpServers": {
    "transcriptx": {
      "url": "https://mcp.transcriptx.ai/mcp"
    }
  }
}
```

---

## Errors

Every error returns the same JSON shape:

```json
{
  "error": {
    "code": "video_private",
    "message": "This video is private or requires sign-in."
  }
}
```

| HTTP | `code` | What it means / what to do |
|---|---|---|
| 400 | `invalid_url` | The link isn't a YouTube video URL. Check for typos or a stripped `v=` parameter. |
| 401 | `invalid_api_key` | The key is missing or wrong. Check the `Authorization: Bearer` header. |
| 402 | `insufficient_credits` | Your plan's quota is used up. Upgrade, or wait for the monthly reset. |
| 403 | `video_private` | The video is private, unlisted, members-only or age-restricted behind a login. Only public videos can be transcribed. |
| 404 | `no_captions` | Returned only with `mode: captions` when the video has no captions. Retry with `mode: auto`. |
| 404 | `video_not_found` | The video was deleted or the ID doesn't exist. |
| 429 | `rate_limited` | Too many requests. Wait for the number of seconds in the `Retry-After` header. |
| 5xx | `server_error` | Temporary problem on our side. Retry with backoff. Credits are not charged for failed requests. |

**Handling 429 in Python:**

```python
import time
import requests


def post_with_retry(url, max_retries=5, **kwargs):
    for attempt in range(max_retries):
        r = requests.post(url, **kwargs)
        if r.status_code != 429:
            return r
        time.sleep(int(r.headers.get("Retry-After", 2 ** attempt)))
    r.raise_for_status()
```

---

## Rate limits and pricing

| Plan | Requests | Rate limit |
|---|---|---|
| Free | 100 / month, no card | 10 requests / minute |
| Paid | From your plan quota | 60 requests / minute |

- A request answered from **captions** costs 1 credit.
- A request that uses the **AI fallback** is billed per minute of audio.
- Failed requests are free.

See [API pricing](#) for current plans.

---

## Why not just use the `youtube-transcript-api` Python library?

The open-source [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) works well on a laptop. In production it usually breaks in one of three ways:

1. **IP blocks.** YouTube blocks most cloud server IPs (AWS, GCP, Azure, Vercel). Your code works locally and then raises `RequestBlocked` or `IpBlocked` once deployed. Fixing it means paying for rotating residential proxies.
2. **Videos with no captions.** The library can only read existing captions. Many Shorts and new uploads have none, so you get `TranscriptsDisabled` or `NoTranscriptFound`.
3. **YouTube-only.** TikTok, Instagram Reels and podcast links need separate tools.

TranscriptX handles all three behind one endpoint. Switching usually takes about five lines of code:

```python
# Before
from youtube_transcript_api import YouTubeTranscriptApi
segments = YouTubeTranscriptApi().fetch("dQw4w9WgXcQ")

# After
from transcript import get_transcript
segments = get_transcript("https://youtu.be/dQw4w9WgXcQ")["segments"]
```

---

## What developers build with it

- **RAG and chatbots:** index a channel's videos and answer questions with cited timestamps.
- **Video summaries:** send `text` to an LLM for summaries, chapters or key takeaways.
- **Subtitles:** export SRT/VTT and translate them into other languages.
- **Content repurposing:** turn videos into blog posts, newsletters or social threads.
- **Research and monitoring:** search what was said across hundreds of videos.

---

## FAQ

**What happens if a video has no captions?**
With the default `mode: auto`, TranscriptX downloads the audio and transcribes it with AI. The response has `"method": "ai"`, and you get text either way.

**Which languages are supported?**
100+ languages, detected automatically. Pass `language` to request a specific one.

**Do I need a YouTube Data API key or OAuth?**
No. You only need your TranscriptX API key. YouTube's official `captions.download` endpoint only works for videos you own. TranscriptX works for any public video.

**Can I get transcripts of private or unlisted videos?**
No. Only public videos can be transcribed. Private, unlisted and login-only videos return `403 video_private`.

**Does it work with YouTube Shorts and live streams?**
Yes for Shorts. Finished live streams work like normal videos. Streams that are still live can be transcribed once they end.

**Can I pass a video ID instead of a URL?**
Yes. `"url": "dQw4w9WgXcQ"` is accepted and treated as a YouTube video.

**How long does a request take?**
Videos with captions return in about 1 second. AI transcription usually takes a fraction of the video's length. Poll `GET /v1/transcripts/{id}` every 3 seconds.

**Is there a free tier?**
Yes. 100 requests per month, no credit card required.

**Is it legal to fetch YouTube transcripts?**
TranscriptX only accesses publicly available videos. How you use the text, for example republishing it, is your responsibility under copyright law and YouTube's terms.

---

## More TranscriptX APIs

- [Speech to Text API](#): one API for any file or link
- [Video to Text API](#) · [Audio to Text API](#)
- [MP3 to Text API](#) · [MP4 to Text API](#) · [WAV to Text API](#)
- [TikTok Transcript API](#) · [Instagram Reels Transcript API](#)
- Prefer no code? Use the free [YouTube Transcript tool](/youtube-transcript/)

---

### Start building

Create a free API key and get your first transcript in under five minutes. 100 free requests every month, no card required.

[Get your free API key →](#)
