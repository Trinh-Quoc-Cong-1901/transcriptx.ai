"""Expand sitemap indexes recursively and save URL lists per site (URLs only, no page content)."""
import gzip, re, sys, urllib.request, json, os
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
OUT = sys.argv[1]
SITES = {
    "otter": ["https://otter.ai/sitemap.xml"],
    "descript": ["https://www.descript.com/sitemap.xml", "https://www.descript.com/sitemap-index.xml"],
    "rev": ["https://www.rev.com/sitemap.xml"],
    "sonix": ["https://static.sonix.ai/sitemaps/sitemap.xml.gz", "https://sonix.ai/resources/sitemap_index.xml"],
    "happyscribe": ["https://www.happyscribe.com/sitemap.xml"],
    "trint": ["https://trint.com/sitemap.xml"],
    "notta": ["https://www.notta.ai/sitemap-0.xml", "https://www.notta.ai/brain/sitemap.xml", "https://www.notta.ai/robots.txt"],
}
# skip localized copies: /de/, /fr/, /es-ES/ ...
LOCALE = re.compile(r"^https?://[^/]+/(?:[a-z]{2}(?:[-_][A-Za-z]{2,4})?)(?:/|$)")
KEEP_2 = {"ai", "go", "my", "tv", "vs"}  # 2-letter segments that are not locales

def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = urllib.request.urlopen(req, timeout=40).read()
        if url.endswith(".gz") or data[:2] == b"\x1f\x8b":
            data = gzip.decompress(data)
        return data.decode("utf-8", "replace")
    except Exception as e:
        return f"__ERR__ {e}"

def is_locale(u):
    m = LOCALE.match(u)
    if not m:
        return False
    seg = u.split("/")[3].lower()
    return seg[:2] not in KEEP_2 or "-" in seg or "_" in seg

def crawl(site, seeds):
    seen, urls, errs, queue = set(), set(), [], list(seeds)
    while queue and len(seen) < 400:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        txt = get(sm)
        if txt.startswith("__ERR__") or "<html" in txt[:500].lower():
            errs.append(f"{sm}: {txt[:80]}")
            continue
        if sm.endswith("robots.txt"):
            queue += [l.split(":", 1)[1].strip() for l in txt.splitlines() if l.lower().startswith("sitemap:")]
            continue
        locs = re.findall(r"<loc>\s*(?:<!\[CDATA\[)?([^<\]]+)", txt)
        if "<sitemapindex" in txt:
            for l in locs:
                l = l.strip()
                if not is_locale(l.replace("/sitemap", "/x/sitemap")) or True:
                    queue.append(l)
        else:
            for l in locs:
                l = l.strip()
                if not is_locale(l):
                    urls.add(l)
    return site, sorted(urls), errs, len(seen)

with ThreadPoolExecutor(7) as ex:
    for site, urls, errs, n in ex.map(lambda kv: crawl(*kv), SITES.items()):
        with open(os.path.join(OUT, f"{site}.txt"), "w") as f:
            f.write("\n".join(urls))
        print(f"{site}: {len(urls)} urls from {n} sitemaps; errors {len(errs)}")
        for e in errs[:4]:
            print("   ", e)
