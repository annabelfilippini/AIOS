"""Raw HTML analysis for Frita Batidos — meta, JSON-LD, headings, alt audit, third-party scripts."""

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen
from html.parser import HTMLParser

BASE = Path(__file__).resolve().parent

TARGETS = [
    ("frita-batidos", "homepage-main", "https://fritabatidos.com/"),
    ("frita-batidos", "ann-arbor-home", "https://fritabatidos.com/ann-arbor"),
    ("frita-batidos", "ann-arbor-food", "https://fritabatidos.com/ann-arbor/food"),
    ("frita-batidos", "ann-arbor-chef", "https://fritabatidos.com/ann-arbor/chef"),
    ("frita-batidos", "ann-arbor-philosophy", "https://fritabatidos.com/ann-arbor/philosophy"),
    ("frita-batidos", "ann-arbor-praise", "https://fritabatidos.com/ann-arbor/praise"),
    ("frita-batidos", "ann-arbor-contact", "https://fritabatidos.com/ann-arbor/contact"),
    ("frita-batidos", "detroit-home", "https://fritabatidos.com/detroit"),
]


def fetch(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (audit-scrape)"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


class Analyzer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {"title": None, "description": None, "robots": None, "viewport": None, "og": {}, "twitter": {}, "canonical": None}
        self.headings = []
        self.images = []
        self.scripts = []
        self.jsonld = []
        self._in_title = False
        self._title_buf = []
        self._in_jsonld = False
        self._jsonld_buf = []
        self._heading_tag = None
        self._heading_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = a.get("name", "").lower()
            prop = a.get("property", "").lower()
            content = a.get("content", "")
            if name == "description":
                self.meta["description"] = content
            elif name == "robots":
                self.meta["robots"] = content
            elif name == "viewport":
                self.meta["viewport"] = content
            elif prop.startswith("og:"):
                self.meta["og"][prop] = content
            elif name.startswith("twitter:"):
                self.meta["twitter"][name] = content
        elif tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading_tag = tag
            self._heading_buf = []
        elif tag == "img":
            self.images.append({
                "src": a.get("src", ""),
                "alt": a.get("alt"),
                "loading": a.get("loading"),
                "width": a.get("width"),
                "height": a.get("height"),
            })
        elif tag == "script":
            if a.get("type") == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []
            elif a.get("src"):
                self.scripts.append(a["src"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.meta["title"] = "".join(self._title_buf).strip()
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._heading_tag == tag:
            text = " ".join("".join(self._heading_buf).split())
            self.headings.append({"tag": tag, "text": text})
            self._heading_tag = None
        elif tag == "script" and self._in_jsonld:
            raw = "".join(self._jsonld_buf).strip()
            self._in_jsonld = False
            try:
                self.jsonld.append(json.loads(raw))
            except Exception:
                self.jsonld.append({"_raw": raw[:500], "_error": "parse-failed"})

    def handle_data(self, data):
        if self._in_title:
            self._title_buf.append(data)
        if self._in_jsonld:
            self._jsonld_buf.append(data)
        if self._heading_tag:
            self._heading_buf.append(data)


def classify_script(src):
    patterns = [
        ("Google Tag Manager", r"googletagmanager\.com"),
        ("Google Analytics", r"google-analytics\.com|gtag/js"),
        ("Facebook Pixel", r"connect\.facebook\.net|fbevents"),
        ("Klaviyo", r"klaviyo"),
        ("Shopify", r"cdn\.shopify"),
        ("Toast", r"toasttab|toast"),
        ("Squarespace", r"squarespace|sqsp"),
        ("WordPress", r"wp-content|wp-includes"),
        ("Wix", r"wix|parastorage"),
        ("Jotform", r"jotform"),
        ("Tawk", r"tawk"),
        ("Hotjar", r"hotjar"),
        ("Cloudflare", r"cloudflare"),
        ("jQuery", r"jquery"),
        ("Stripe", r"stripe\.com|js\.stripe"),
        ("Mailchimp", r"mailchimp"),
        ("Reserve / Resy / OpenTable / Tock", r"resy|opentable|tock\.com|sevenrooms|exploretock"),
    ]
    for label, pat in patterns:
        if re.search(pat, src, re.I):
            return label
    return None


def analyze(site, page, url):
    print(f"\n--- {site}/{page} ({url}) ---")
    try:
        html = fetch(url)
    except Exception as e:
        print(f"  fetch failed: {e}")
        return {"site": site, "page": page, "url": url, "error": str(e)}

    a = Analyzer()
    a.feed(html)

    images = a.images
    total = len(images)
    empty_alt = sum(1 for i in images if i.get("alt") == "")
    missing_alt = sum(1 for i in images if i.get("alt") is None)
    generic_alt = sum(1 for i in images if i.get("alt") and i["alt"].lower().strip() in {"image", "photo", "picture", "img", "icon", ""})
    lazy = sum(1 for i in images if i.get("loading") == "lazy")

    third_party = {}
    for s in a.scripts:
        label = classify_script(s)
        if label:
            third_party.setdefault(label, []).append(s)

    result = {
        "site": site,
        "page": page,
        "url": url,
        "html_bytes": len(html),
        "meta": a.meta,
        "headings": {
            "count_by_level": {t: sum(1 for h in a.headings if h["tag"] == t) for t in ("h1", "h2", "h3", "h4", "h5", "h6")},
            "h1_texts": [h["text"] for h in a.headings if h["tag"] == "h1"],
            "total": len(a.headings),
            "hierarchy": [{"tag": h["tag"], "text": h["text"][:100]} for h in a.headings[:60]],
        },
        "images": {
            "total": total,
            "empty_alt": empty_alt,
            "missing_alt": missing_alt,
            "generic_alt": generic_alt,
            "lazy_loaded": lazy,
        },
        "scripts": {
            "total_external": len(a.scripts),
            "third_party": {k: len(v) for k, v in third_party.items()},
            "third_party_samples": {k: v[:2] for k, v in third_party.items()},
        },
        "jsonld": {
            "count": len(a.jsonld),
            "types": [item.get("@type") if isinstance(item, dict) else "?" for item in a.jsonld],
            "samples": a.jsonld[:3],
        },
    }

    print(f"  title: {a.meta['title']}")
    print(f"  description: {(a.meta['description'] or '')[:100]}")
    print(f"  h1 count: {result['headings']['count_by_level']['h1']}  h1s: {result['headings']['h1_texts']}")
    print(f"  images: {total} (missing-alt={missing_alt}, empty-alt={empty_alt}, generic-alt={generic_alt}, lazy={lazy})")
    print(f"  scripts: {len(a.scripts)} external, third-party: {list(third_party.keys())}")
    print(f"  JSON-LD blocks: {len(a.jsonld)}  types: {result['jsonld']['types']}")
    print(f"  canonical: {a.meta['canonical']}")
    return result


all_results = []
for site, page, url in TARGETS:
    all_results.append(analyze(site, page, url))

out = BASE / "scrape" / "raw-html-analysis.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(all_results, indent=2, default=str))
print(f"\n=> {out}")
