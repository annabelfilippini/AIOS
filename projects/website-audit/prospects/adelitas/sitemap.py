"""Crawl all sitemaps for adelitasco.com and ladonamezcaleria.com. Produce full URL inventory."""

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parent

SITES = [
    ("adelitas", "https://adelitasco.com"),
    ("la-dona", "https://ladonamezcaleria.com"),
]


def fetch(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", errors="replace"), r.status
    except Exception as e:
        return None, f"ERR: {e}"


def extract_urls(xml):
    return re.findall(r"<loc>([^<]+)</loc>", xml or "")


inventory = {}
for site, root in SITES:
    print(f"\n=== {site} ({root}) ===")
    urls_seen = set()

    # robots.txt
    robots_body, _ = fetch(f"{root}/robots.txt")
    if robots_body:
        sitemap_lines = [line.split(":", 1)[1].strip() for line in robots_body.splitlines() if line.lower().startswith("sitemap:")]
    else:
        sitemap_lines = []

    # Direct /sitemap.xml
    for sm in [f"{root}/sitemap.xml"] + sitemap_lines:
        body, status = fetch(sm)
        if body is None:
            print(f"  [{status}] {sm}")
            continue
        found = extract_urls(body)
        print(f"  [{len(found)}] {sm}")
        for u in found:
            if u.endswith(".xml"):
                child_body, _ = fetch(u)
                child_found = extract_urls(child_body)
                print(f"    child [{len(child_found)}] {u}")
                urls_seen.update(child_found)
            else:
                urls_seen.add(u)

    inventory[site] = sorted(urls_seen)
    print(f"  total unique URLs: {len(urls_seen)}")
    print(f"  robots.txt: {'present' if robots_body else 'missing'}")


out = BASE / "scrape" / "url-inventory.json"
out.write_text(json.dumps(inventory, indent=2))
print(f"\n=> {out}")

# Group by pattern for Adelitas
adl = inventory.get("adelitas", [])
categories = {"core": [], "seo_doorway": [], "other": []}
CORE = {"/", "/broadway", "/edgewater", "/catering", "/qr-code-menu", "/event", "/tequilas-family-mexican-restaurant"}
for u in adl:
    path = u.replace("https://adelitasco.com", "") or "/"
    if path in CORE:
        categories["core"].append(u)
    elif any(k in path for k in ["best-", "mezcal-", "tequila-", "top-", "brunch-", "breakfast-", "happy-hour", "margaritas", "tacos", "delivery", "cocktail"]):
        categories["seo_doorway"].append(u)
    else:
        categories["other"].append(u)

print("\nAdelitas URL categorization:")
for k, v in categories.items():
    print(f"  {k}: {len(v)}")
    for u in v:
        print(f"    {u}")

cats_out = BASE / "scrape" / "url-categorized.json"
cats_out.write_text(json.dumps(categories, indent=2))
print(f"\n=> {cats_out}")
