# Kế hoạch triển khai backlink cho TranscriptX.ai

Ngày lập: 2026-10-11
Nguồn: 10 file phân tích backlink đối thủ trong thư mục `bacnklink/`.

---

## 1. Tóm tắt nhanh

| Đối thủ | Link thật | Kênh chính | Học được gì |
|---|---:|---|---|
| wayin.ai | ~250 | Trang free tool, blog dữ liệu, guest post, skill cho AI agent, ~75 directory | Mô hình chuẩn để học theo |
| transcriptly.org | ~55 | Directory (nhiều trang Trung Quốc), Lemmy, đăng lại bài lên dev.to | Directory và cộng đồng |
| proactor.ai | ~36 | Newsletter AI, blog trích dẫn, directory | Newsletter |
| transcribex.io | ~24 | Báo công nghệ Trung Quốc, Black Friday, Homebrew | Chỉ hợp với app desktop |
| transcript365.com | ~13 | Chrome extension, API, Claude skill | Extension và GitHub |
| vocascript.com | ~7 | Chrome extension, ManyScripts | Trang so sánh |
| transcribeyt.com | ~6 | PeerPush, MCP directory, domain cũ | MCP directory |
| scribesnap.ai | 5 | Product Hunt | — |
| transcriptx.xyz | 1 | Playbook về Claude connector | Trùng tên thương hiệu, cần theo dõi |
| ytmp3.gg | ~30 | Bài "top YouTube to MP3" (Hàn, Pháp, Đài Loan) | Ngách gần, ưu tiên thấp |

**Kết luận:** Trừ Wayin, ngách này hầu như chưa ai làm link building nghiêm túc. Làm đủ Giai đoạn 1 và 2 dưới đây là TranscriptX vượt 8/9 đối thủ.

**Lợi thế riêng của TranscriptX:** Bạn đã có MCP server, Claude/ChatGPT connector, API và loạt trang tool theo nền tảng (YouTube, TikTok, Instagram, Facebook). Đây chính là các kênh mạnh nhất của Wayin, transcript365 và transcribeyt. Bạn không cần xây thêm sản phẩm, chỉ cần đi đăng ký và outreach.

**Không làm:** link farm, PBN, comment spam trên blog Wix hay forum không liên quan, mua domain hết hạn để redirect, link từ trang crack (cracked.sx, macked.app). Khoảng 600 link spam của các đối thủ đều thuộc nhóm này.

---

## 2. Ưu tiên số 1: nguồn đã link cho nhiều đối thủ

Trang nào đã link cho 2 đối thủ trở lên thì gần như chắc chắn sẽ nhận thêm TranscriptX. Nên làm nhóm này trước.

| Nguồn | Số đối thủ có link | Cách lấy link |
|---|---:|---|
| allaiapp.com | 4 | Tự submit |
| ai-hunt.tech | 3 | Tự động có khi launch Product Hunt |
| thejoai.com | 3 | Tự submit |
| captapi.com | 3 | Outreach: blog viết về transcript Instagram, TikTok |
| crxcheck.com | 3 | Tự động có khi có Chrome extension |
| manyscripts.com | 2 | **Outreach quan trọng nhất**: họ có loạt bài "best [nền tảng] video transcript generators" |
| shorttranscript.com | 2 | Outreach để được thêm vào trang `/alternatives/` |
| skillget.dev | 2 | Tự động có khi đưa skill hoặc MCP lên GitHub |
| dev.to | 2 | Tự đăng bài |
| grokipedia.com | 2 | Có tự nhiên khi bài blog dạng dữ liệu được trích dẫn |
| blog.lunote.ai, tinrec.com | 2 | Outreach: blog viết về transcript YouTube |
| extscope.org, extensionauditor.com, extwise.com, chromewebstore | 2 | Tự động có khi có Chrome extension |
| aipure.ai, i10x.ai, toolany.com, showmebest.ai, aideckly.com, aicatalog.com.ua, askmatchbox.com, aistage.net, uselumen.ai, hau.xyz, indiepa.ge, promoteproject.com, launches.uicomet.com, alternativeai.tools, aixies.com, aimostall.com, ailookup.dev, easyai.indevs.in, catalgo.de, neura.market | 2 | Tự submit vào directory |

---

## 3. Lộ trình triển khai

### Giai đoạn 1 (tuần 1–2): Nhóm tự submit, không cần xin

**A. Launch platform** (đăng một lần, các trang khác tự lấy lại dữ liệu)
- [ ] Product Hunt: tự động có link từ ai-hunt.tech, sheepnav.com, aisynkit.com
- [ ] PeerPush (peerpush.com): link mạnh nhất của transcribeyt, AS 24
- [ ] Indiepa.ge, SideProjectors, launches.uicomet.com, startupfa.st, shipybara.com, innolope.com

**B. MCP và AI agent directory** (kênh mới, ít cạnh tranh, rất hợp với TranscriptX)
- [ ] mcprating.io (transcribeyt có link từ đây)
- [ ] Đưa MCP server lên GitHub, có README rõ ràng và link về transcriptx.ai
- [ ] skillget.dev, skillhub.club, clawhub.ai (Wayin có skill ở đây)
- [ ] Các MCP directory khác: Smithery, mcp.so, Glama, PulseMCP, awesome-mcp-servers trên GitHub (gửi PR)
- [ ] Template n8n: n8nworkflows.xyz, n8nworkflow.com (Wayin có 2 template)
- [ ] Plugin Obsidian (nếu làm): obsidianstats.com, plugins.semiautonomous.org

**C. AI directory**: submit 40–50 trang trong tuần đầu. Danh sách đã lọc từ các đối thủ:

*Nhóm quốc tế:*
aipure.ai · toolify.ai · topai.tools · aitoptools.com · aitools.fyi · i10x.ai · dokeyai.com · aiwith.me · bai.tools · aiparabellum.com · toolhunt.io · thejoai.com · allaiapp.com · aixies.com · aimostall.com · ailookup.dev · alternativeai.tools · showmebest.ai · twelve.tools · tyy.ai · aiseekertools.com · aimatch.pro · aideckly.com · aicatalog.com.ua · toolany.com · sharefast.co · listedai.co · seektool.ai · 5app.ai · askmatchbox.com · aistage.net · uselumen.ai · mostpopularaitools.com · chatgate.ai · rightaichoice.com · novatools.ai · omnitools.ai · aiforest.app · whatsthatai.com · tooldix.com · toolverto.com · aitoolhub.co · aitoolex.com · aiproductlist.net · ainexfinder.com · aimyflow.com · allaitoollist.com · anyai.tools · bestaifor.me · clipsradar.com · aiproductleaderboard.com · aimarketly.com · aivitamin.org · getaitool.in · one9founders.com · bocal.online · polaris7.io · uwarp.design · neura.market · promoteproject.com · semfirms.com · appsfor.us · apprank.io · easyai.indevs.in · catalgo.de

*Nhóm Trung Quốc và châu Á* (ít đối thủ để ý, transcriptly lấy được nhiều link từ đây):
ainavtool.com · toolradarai.com · xiaomulu.com · ainavdir.com · aitntnews.com · yizhan.club · agent996.com · global.php.cn · 1ai.net · ranking.junai.ai (Hàn)

**D. Trang dữ liệu doanh nghiệp và affiliate**
- [ ] getlatka.com, affiliateprogram.app (nếu có chương trình affiliate), saas1to10.com

### Giai đoạn 2 (tuần 2–4): Outreach xin link (ưu tiên cao nhất)

Đây là những trang **đã viết về đối thủ**. Gửi email đề nghị thêm TranscriptX vào bài.

**Trang so sánh và "best tools" về transcript** (đúng chủ đề nhất):

| Trang | Bài đang nhắc đối thủ | Đề xuất |
|---|---|---|
| manyscripts.com | best Facebook, LinkedIn video transcript generators | Xin vào các bài YouTube, TikTok, Instagram, Facebook |
| shorttranscript.com | /alternatives/transcript365, /alternatives/wayin | Xin trang /alternatives/transcriptx hoặc thêm vào bài sẵn có |
| captapi.com | blog Instagram reel transcript, TikTok transcript | Đề xuất thêm TranscriptX vào danh sách |
| blog.lunote.ai | how-to-get-a-transcript-from-a-youtube-video | Đề xuất thêm vào bài |
| transclipper.ai | how-to-generate-transcripts-from-instagram-videos | Như trên |
| tokify.net | top tool tạo transcript TikTok 2026 | Như trên |
| transcriptr.ai, whisperai.com | blog về transcript và podcast | Như trên |
| novascribe.ai | best transcription software 2026 | Như trên |
| speaknotes.io, otio.ai, vomo.ai | blog về summary, transcript | Như trên |
| sky-scribe.com, hazeclips.com | blog về transcript và caption | Như trên |
| iemlabs.com | summarized transcripts of YouTube podcasts | Như trên |
| t-applicada.blogspot.com | công cụ miễn phí trích xuất transcript | Như trên |

**Trang "best AI video summarizer / YouTube tools"** (Wayin có mặt, TranscriptX có trang `/youtube-video-summarizer`):
educba.com/ai-video-summarizer · classlecture.ai · adviserry.com · startwebtools.com · embed.klap.app · atlasworkspace.ai · ai-explorer.io · techloy.com · aijourn.com · techbullion.com · xyzeo.com/blog/best-ai-tools-for-youtube · plainenglish.io · digitalcitizen.life · appsgeyser.com · toolsbuddy.io · aiapps.com · thedatascientist.com

**Trang "best meeting assistant / transcription"** (từ proactor):
cirface.com/blog/best-ai-meeting-assistant · kingy.ai · testingcatalog.com · tavus.io

**Trang về Claude connector / MCP:**
- attentionfactory.io/playbooks/five-claude-connectors: trang này đang link cho transcriptx.xyz (trùng tên). Liên hệ để giới thiệu TranscriptX.ai connector, và kiểm tra họ có nhầm hai thương hiệu không.
- claude-updates.com, somyanayak.com, milleemd.com: viết về Claude skill và workflow.
- windowsreport.com (bài về workflow API), ai-primer.com, blankdot.ai.

**Mẫu email outreach (tiếng Anh):**

```
Subject: Quick addition to your "<tên bài>" list

Hi <tên>,

I read your post "<tên bài>" — really useful breakdown, especially the part on <chi tiết cụ thể>.

I'm <tên> from TranscriptX.ai. We're a free transcript tool for YouTube, TikTok,
Instagram and Facebook, and we also ship an MCP server / Claude connector so people
can transcribe videos straight inside Claude or ChatGPT. That's something none of
the tools in your list currently offer.

Would you consider adding us? Happy to send a free Pro account so you can test it,
or provide a screenshot / short description in your format.

Link: https://transcriptx.ai/<trang tool phù hợp>

Thanks either way!
<chữ ký>
```

Mẹo: trỏ link về đúng trang tool liên quan (vd. bài TikTok thì trỏ về `/tiktok-transcript-generator`), không trỏ về trang chủ. Sau 5–7 ngày không có phản hồi thì gửi follow-up một lần.

### Giai đoạn 3 (tháng 2): Content tự kéo link (chiến lược của Wayin)

Không cần outreach, nhưng đây là nguồn link bền vững nhất.

- [ ] **Blog dạng dữ liệu tra cứu**: "Instagram video length limit 2026", "TikTok video length limit", "Twitter/X video length limit", "Reels dimensions", "YouTube Shorts length". Wayin được Grokipedia, Mallary, Narrareach, Supabird trích dẫn nhờ các bài này.
- [ ] **Bài "best tools"**: "best free YouTube transcript tools", "best TikTok transcript generators"… Đây là dạng được trích dẫn nhiều nhất.
- [ ] **Trang alternative**: `/alternatives/wayin`, `/alternatives/transcript365`, `/alternatives/tactiq`… để bắt người dùng đang tìm đối thủ.
- [ ] **Bài kỹ thuật đăng lại** lên dev.to, Medium, Hashnode, có canonical về blog gốc. Ví dụ: "How YouTube auto-captions work", "Build a YouTube transcript MCP server". Transcriptly lấy link mạnh nhất từ cách này.

### Giai đoạn 4 (tháng 2–3): Mở rộng kênh

- [ ] **Chrome extension** cho từng nền tảng (YouTube, Instagram, TikTok, Facebook). Mỗi extension mang về 3–5 link tự động: Chrome Web Store, crxcheck, extscope, extensionauditor, extwise.
- [ ] **Newsletter AI**: gửi tin cho Ben's Bites, The Unwind AI, AI Marketing School, Aloa Byte-sized, Horizon AI, Daily Bite, các newsletter beehiiv về AI. Có tin mới nhất (vd. ra mắt connector) thì cơ hội cao.
- [ ] **Cộng đồng**: trả lời có giá trị thật trên Reddit (r/youtube, r/podcasting, r/ClaudeAI, r/mcp, r/selfhosted) và Lemmy. Không spam link.
- [ ] **Guest post / sponsored** (nếu có ngân sách): Windows Report, MSPowerUser, TechBullion, AI Journal, Techloy, Coruzant, Nerdbot. Wayin dùng nhóm này. Nên dùng rel="sponsored" cho đúng hướng dẫn của Google.
- [ ] **Deal season**: Black Friday thì gửi tin cho các trang tổng hợp deal (blackfridaydeals.directory, neura.market).

---

## 4. KPI theo dõi

| Mốc | Mục tiêu |
|---|---|
| Hết tuần 2 | 40+ directory, Product Hunt, PeerPush, 5+ MCP directory |
| Hết tháng 1 | 60+ referring domain thật, 50 email outreach đã gửi, 5–10 link từ outreach |
| Hết tháng 3 | 120+ referring domain thật, 10+ link editorial (bài viết), 5 bài blog dữ liệu đã đăng |

Theo dõi trong file Excel `TranscriptX_SEO_Strategy.xlsx` hoặc một sheet riêng, với các cột: Nguồn · URL · Loại (directory/outreach/tự động) · Ngày gửi · Trạng thái · Link đã lên · Anchor · Trang đích.

---

## 5. Lưu ý về thương hiệu "TranscriptX"

transcriptx.xyz dùng cùng tên. Họ chưa mạnh (1 link thật), nhưng nên:
- Ở mọi directory, ghi rõ tên **TranscriptX.ai** và domain đầy đủ.
- Kiểm tra định kỳ xem có trang nào nhầm link sang transcriptx.xyz thì liên hệ sửa lại.
