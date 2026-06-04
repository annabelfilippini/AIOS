"""Firecrawl branding scrape for Hop Alley. Saves colors/fonts/logos as JSON.

Tries native `branding` format first; falls back to extracting from rawHtml + CSS
if the format is unavailable in the installed SDK.
"""

import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent
URL = "https://hopalleydenver.com/"
OUT = BASE / "branding.json"


def _to_dict(obj):
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, dict):
        return obj
    try:
        return {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    except TypeError:
        return obj


def try_native_branding():
    print("Attempting native `branding` format...")
    try:
        r = app.scrape(URL, formats=["branding"], wait_for=3000)
    except Exception as e:
        print(f"  native branding errored: {type(e).__name__}: {e}")
        return None

    # Look for a branding attribute or dict key
    branding = None
    for attr in ("branding", "brand"):
        if hasattr(r, attr):
            branding = getattr(r, attr)
            break
    if branding is None and isinstance(r, dict):
        branding = r.get("branding") or r.get("brand")

    branding = _to_dict(branding)
    if branding:
        print(f"  native branding OK ({len(str(branding))} chars)")
        return branding

    # Dump whole response for inspection — SDKs vary
    dump = _to_dict(r)
    print(f"  no `branding` attr on response; keys: {list(dump.keys()) if isinstance(dump, dict) else type(dump)}")
    return None


def fallback_from_css():
    """Pull colors, fonts, logo URLs out of raw HTML + inline/linked CSS."""
    print("\nFalling back to rawHtml extraction...")
    r = app.scrape(URL, formats=["rawHtml", "html", "links"], wait_for=3000)
    html = getattr(r, "rawHtml", None) or getattr(r, "raw_html", None) or getattr(r, "html", "") or ""
    links = getattr(r, "links", []) or []

    # Colors — hex + rgb from all style/CSS content
    hex_colors = set(re.findall(r"#[0-9A-Fa-f]{6}\b", html))
    rgb_colors = set(re.findall(r"rgba?\([^)]+\)", html))

    # Fonts — font-family declarations
    font_families = set()
    for m in re.findall(r"font-family\s*:\s*([^;\"'}]+)", html, re.IGNORECASE):
        font_families.add(m.strip())
    # Google fonts links
    google_fonts = re.findall(r"fonts\.googleapis\.com/css2?\?family=([^\"'&]+)", html)

    # Logos — images containing "logo" in src/alt
    logo_urls = set()
    for m in re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']*logo[^"\']*)["\']', html, re.IGNORECASE):
        logo_urls.add(m)
    for m in re.findall(r'<img[^>]+alt=["\'][^"\']*logo[^"\']*["\'][^>]*(?:src|data-src)=["\']([^"\']+)["\']', html, re.IGNORECASE):
        logo_urls.add(m)
    # Favicon
    favicons = re.findall(r'<link[^>]+rel=["\'][^"\']*icon[^"\']*["\'][^>]*href=["\']([^"\']+)["\']', html, re.IGNORECASE)

    return {
        "source": "fallback:rawHtml+regex",
        "url": URL,
        "colors": {
            "hex": sorted(hex_colors),
            "rgb": sorted(rgb_colors),
        },
        "fonts": {
            "font_families": sorted(font_families),
            "google_fonts": sorted(set(google_fonts)),
        },
        "logos": sorted(logo_urls),
        "favicons": sorted(set(favicons)),
        "links_sample": links[:20] if isinstance(links, list) else [],
    }


def main():
    native = try_native_branding()
    if native:
        payload = {"source": "firecrawl:branding", "url": URL, "branding": native}
    else:
        payload = fallback_from_css()
    OUT.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\nWrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
