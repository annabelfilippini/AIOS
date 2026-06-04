"""Collect every Black Pearl image URL from scraped markdown/HTML and download locally.

Images go to prospects/black-pearl/mockups/assets/img/.
Produces a manifest: mockups/assets/img/manifest.json mapping original URL -> local filename + caption.
"""

import hashlib
import json
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parent
SCRAPE_DIR = BASE / "scrape"
IMG_DIR = BASE / "mockups" / "assets" / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST = IMG_DIR / "manifest.json"

# Additional known pages (full site HTML) we should scan for image URLs
extra_htmls = [
    BASE / "scrape" / "menu-raw.html",
]

def harvest_urls():
    urls = {}  # url -> caption guess
    # Markdown images: ![alt](url)
    md_img_pat = re.compile(r'!\[([^\]]*)\]\((https?://[^\s\)]+)\)')
    for md in SCRAPE_DIR.glob("*.md"):
        text = md.read_text()
        for alt, url in md_img_pat.findall(text):
            if "squarespace-cdn.com" in url or "blackpearl" in url:
                if url not in urls:
                    urls[url] = alt or md.stem
    # HTML pages
    for html_path in extra_htmls:
        if not html_path.exists():
            continue
        text = html_path.read_text()
        for m in re.finditer(r'(https?://images\.squarespace-cdn\.com/[^"\s\)]+)', text):
            u = m.group(1)
            if u not in urls:
                urls[u] = ""
    return urls


def normalize(url: str) -> str:
    """Strip trailing format tokens and get a cleaner URL for filename derivation."""
    # Squarespace URLs end with ?format=... — we'll ask for a decent size
    return url.split("?")[0]


def download(url, dest: Path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        dest.write_bytes(data)
        return len(data)
    except Exception as e:
        print(f"  ERROR {type(e).__name__}: {e} — {url}")
        return 0


urls = harvest_urls()
print(f"Harvested {len(urls)} image URLs")

manifest = {}
for url, caption in urls.items():
    clean = normalize(url)
    # Prefer a reasonable Squarespace size
    request_url = url
    if "squarespace-cdn.com" in url and "?format" not in url:
        request_url = url + "?format=2500w"
    name = Path(urlparse(clean).path).name
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-") or hashlib.md5(url.encode()).hexdigest()[:10]
    # ensure extension
    if "." not in stem:
        stem += ".jpg"
    dest = IMG_DIR / stem
    if dest.exists():
        print(f"  [skip exists] {stem}")
        manifest[url] = {"file": stem, "caption": caption, "bytes": dest.stat().st_size}
        continue
    size = download(request_url, dest)
    if size:
        print(f"  {stem}: {size//1024}KB — {caption[:60]}")
        manifest[url] = {"file": stem, "caption": caption, "bytes": size}

MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
print(f"\nWrote {MANIFEST}")
print(f"Downloaded {sum(1 for v in manifest.values() if v['bytes'] > 0)} images to {IMG_DIR}")
