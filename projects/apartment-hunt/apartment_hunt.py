"""Apartment hunt: pull SF rentals from Craigslist + Exa, dedupe, deliver digest.

Run modes:
  python apartment_hunt.py           # full run: scrape + write markdown archive
  python apartment_hunt.py --dry     # scrape + write markdown, skip seen-set update
  python apartment_hunt.py --reset   # clear seen-set (re-shows everything next run)
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlencode, urlparse, urlunparse

import requests
from dotenv import load_dotenv

# ---------- config ----------

ROOT = Path(__file__).resolve().parent
SEEN_PATH = ROOT / "seen_3br_sf_core.json"
DIGEST_PATH = ROOT / "digest_latest.md"
ARCHIVE_DIR = ROOT / "digests"

# Hunt criteria
MIN_PRICE = 3200
IDEAL_MAX_PRICE = 7500  # $2,500/person for 3 people
MAX_PRICE = 9000        # stretch ceiling for unusually good fits (raised from $8,250 on 2026-06-03)
MIN_BEDS = 3
MAX_BEDS = 3
MOVE_BY = dt.date(2026, 6, 15)

# Neighborhoods Annabel wants. Match against listing title/location text.
NEIGHBORHOODS = [
    "russian hill",
    "north beach",
    "hayes valley",
    "marina",
    "pacific heights",
    "cow hollow",
    "nob hill",
]

# Top priority — these float to the top of the digest.
PREFERRED_NEIGHBORHOODS = [
    "russian hill",
    "north beach",
]

# Acceptable fallback neighborhoods. Keep them visible, but below the core hunt.
FALLBACK_NEIGHBORHOODS = [
    "hayes valley",
    "marina",
    "pacific heights",
    "cow hollow",
    "nob hill",
]

# SF ZIP → neighborhood, restricted to the hoods Annabel cares about.
# Used to validate Exa results that don't repeat the neighborhood name in
# their title/snippet.
SF_TARGET_ZIPS = {
    "94133": "north beach",       # North Beach / Telegraph Hill / part of Russian Hill
    "94123": "marina",            # Marina / Cow Hollow
    "94115": "pacific heights",   # Pacific Heights / Lower Pac Heights / Japantown
    # Deliberately do not use 94109 or 94102 as positive ZIP fallbacks:
    # 94109 can be Russian Hill, Nob Hill, Polk Gulch, or Tenderloin; 94102 can
    # be Hayes Valley, Civic Center, or Tenderloin. Require an explicit
    # neighborhood label for those.
}

# Craigslist's location field is seller-typed but they overwhelmingly use these
# canonical labels. Match exactly — substring matching causes false positives
# like "outer mission" matching "mission" and "lower nob hill" sneaking in.
_CL_LOCATION_TO_HOOD: dict[str, str] = {
    "north beach": "north beach",
    "north beach / telegraph hill": "north beach",
    "telegraph hill": "north beach",
    "russian hill": "russian hill",
    "marina": "marina",
    "marina / cow hollow": "marina",
    "cow hollow": "cow hollow",
    "nob hill": "nob hill",
    "russian hill / nob hill": "nob hill",
    "pacific heights": "pacific heights",
    "lower pacific heights": "pacific heights",
    "pac hts": "pacific heights",
    "japantown": "pacific heights",
    "hayes valley": "hayes valley",
}

# Domains we explicitly DON'T want to whitelist for the open-web pass. Exa
# indexes well across the rental web — RentSFNow, Engel & Völkers, Movoto,
# Relisto, HomeFinder, Furnished Housing, etc. Whitelisting starves it. Just
# let it loose and filter on URL shape after.
REDDIT_DOMAINS = ["reddit.com"]

# Major aggregators that gate their search pages with anti-bot challenges
# (Cloudflare/F5). We can't direct-scrape them, but Exa often indexes their
# detail pages. Target each domain individually so Exa returns deep listing
# URLs we'd otherwise miss in the open-web sweep.
AGGREGATOR_DOMAINS = [
    "apartments.com",
    "apartmentfinder.com",
    "apartmentguide.com",
    "apartmenthomeliving.com",
    "apartmentlist.com",
    "avaloncommunities.com",
    "compass.com",
    "craigslist.org",
    "equityapartments.com",
    "forrent.com",
    "homefinder.com",
    "hotpads.com",
    "lovely.com",
    "padmapper.com",
    "redfin.com",
    "realtor.com",
    "rent.com",
    "rentable.co",
    "rentberry.com",
    "rentcafe.com",
    "renthop.com",
    "rentlingo.com",
    "rentometer.com",
    "rents.com",
    "rentsfnow.com",
    "sfcityrents.com",
    "trulia.com",
    "westside-rentals.com",
    "zillow.com",
    "zumper.com",
]

# Local/property-manager sources that often surface older SF buildings before
# aggregators do. These are queried through Exa rather than direct-scraped unless
# a site exposes a stable public listing page.
PROPERTY_MANAGER_DOMAINS = [
    "anchorrealtyinc.com",
    "brickandtimber.com",
    "chandlerproperties.com",
    "gaetanirealestate.com",
    "jwavro.com",
    "kinetic-re.com",
    "laphamcompany.com",
    "rentsfnow.com",
    "sfcityrents.com",
    "structureproperties.com",
    "trinitysf.com",
    "yeeproperties.com",
]

DIRECT_SOURCE_SEEDS = [
    # Direct-fetched sites. Only sites that actually return inventory in raw HTML
    # live here. Anti-bot-blocked + JS-only sites were migrated to FIRECRAWL_SEEDS
    # on 2026-06-03 (see notes/2026-06-03-firecrawl-source-rollout.md).
    # Zillow lives in its own paginated fetcher (fetch_zillow_firecrawl).
    ("apartmentguide.com", "https://www.apartmentguide.com/apartments/California/San-Francisco/3-beds-1z141xs/"),
    ("homefinder.com", "https://homefinder.com/rentals/CA/San-Francisco?beds=3"),
    ("redfin.com", "https://www.redfin.com/city/17151/CA/San-Francisco/apartments-for-rent/filter/property-type=apartment,min-beds=3,max-beds=3"),
    ("rentable.co", "https://www.rentable.co/san-francisco-ca?beds=3"),
    ("rentberry.com", "https://rentberry.com/apartments/s/san-francisco-ca/3-bed"),
    ("rentcafe.com", "https://www.rentcafe.com/3-bedroom-apartments-for-rent/us/ca/san-francisco/"),
    ("rentsfnow.com", "https://www.rentsfnow.com/apartments-for-rent/san-francisco/"),
    ("structureproperties.com", "https://structureproperties.com/available-rentals/"),
    # Broken sites kept commented out — re-enable if their URLs come back to life.
    # ("anchorrealtyinc.com", "https://www.anchorrealtyinc.com/vacancies"),  # DNS error
    # ("brickandtimber.com", "https://www.brickandtimber.com/apartments/"),  # 404
    # ("kinetic-re.com", "https://www.kinetic-re.com/rentals"),              # DNS error
    # ("laphamcompany.com", "https://www.laphamcompany.com/vacancies"),      # 404
]

CRAIGSLIST_BASE = "https://sfbay.craigslist.org/search/sfc/apa"
# Craigslist hard-blocks Python User-Agents (and their RSS feed) but serves HTML
# fine to a normal browser UA. Use a Safari string.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)


# ---------- data ----------

@dataclass
class Listing:
    source: str            # "craigslist", "exa", "exa-reddit"
    id: str                # stable dedup key
    title: str
    url: str
    price: int | None = None
    beds: int | None = None
    neighborhood: str | None = None
    posted: str | None = None    # ISO date string if known
    snippet: str = ""
    query_neighborhood: str | None = None  # the hood we searched for, even if title omits it

    def matches_neighborhood(self) -> str | None:
        # Craigslist: only trust the seller's location tag, and only if it's an
        # exact match to a known target label. The CL location field is
        # structured enough that substring matching just lets in noise.
        if self.source == "craigslist":
            if self.neighborhood:
                return _CL_LOCATION_TO_HOOD.get(self.neighborhood.strip().lower())
            return None
        # Exa: title/snippet may mention neighborhood loosely, plus we have ZIP fallback.
        haystack = f"{self.title} {self.neighborhood or ''} {self.snippet}".lower()
        for n in NEIGHBORHOODS:
            if n in haystack:
                return n
        return _zip_neighborhood(f"{self.title} {self.snippet}")

    def is_preferred(self) -> bool:
        match = self.matches_neighborhood()
        return match in PREFERRED_NEIGHBORHOODS if match else False

    def domain(self) -> str:
        m = re.search(r"https?://(?:www\.)?([^/]+)", self.url)
        return m.group(1) if m else "?"


@dataclass
class SourceReport:
    source: str
    url: str
    status: str
    listings: int = 0
    note: str = ""


# ---------- seen-set ----------

def load_seen() -> set[str]:
    if not SEEN_PATH.exists():
        return set()
    try:
        return set(json.loads(SEEN_PATH.read_text()))
    except json.JSONDecodeError:
        return set()


def save_seen(seen: set[str]) -> None:
    SEEN_PATH.write_text(json.dumps(sorted(seen), indent=2))


# ---------- craigslist ----------

_CL_LISTING_RE = re.compile(
    r'<li class="cl-static-search-result"[^>]*>\s*'
    r'<a href="(?P<url>[^"]+)">\s*'
    r'<div class="title">(?P<title>[^<]+)</div>\s*'
    r'<div class="details">\s*'
    r'<div class="price">(?P<price>[^<]*)</div>\s*'
    r'<div class="location">\s*(?P<location>[^<]*?)\s*</div>',
    re.DOTALL,
)


def fetch_craigslist() -> list[Listing]:
    """Pull listings from Craigslist's static (no-JS) HTML search results.

    Note: Craigslist's RSS feed is hard-blocked and their JS-rendered page is
    expensive to crawl. The static search results (rendered for non-JS clients)
    are returned in the HTML and contain title/url/price/location.
    """
    params = {
        "min_price": MIN_PRICE,
        "max_price": MAX_PRICE,
        "min_bedrooms": MIN_BEDS,
        "max_bedrooms": MAX_BEDS,
        "availabilityMode": 0,
    }
    url = f"{CRAIGSLIST_BASE}?{urlencode(params)}"
    resp = requests.get(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
            "Accept-Language": "en-US,en;q=0.9",
        },
        timeout=30,
    )
    resp.raise_for_status()
    html_text = resp.text

    out: list[Listing] = []
    for m in _CL_LISTING_RE.finditer(html_text):
        link = m.group("url").strip()
        title = html.unescape(m.group("title").strip())
        price_text = m.group("price").strip()
        location = html.unescape(m.group("location").strip())

        pid_match = re.search(r"/(\d{10,})\.html", link)
        listing_id = (
            f"cl-{pid_match.group(1)}"
            if pid_match
            else f"cl-{hashlib.sha1(link.encode()).hexdigest()[:12]}"
        )

        out.append(Listing(
            source="craigslist",
            id=listing_id,
            title=title,
            url=link,
            price=_parse_price(price_text) or _parse_price(title),
            beds=_parse_beds(title),  # often in title, e.g. "2br"
            neighborhood=location or None,
            posted=None,  # not present in static results; leave blank
            snippet="",
        ))
    return out


_PRICE_RE = re.compile(r"\$\s?([\d,]+)")
_BEDS_PATTERNS = [
    re.compile(r"\b(\d)\s*br\b", re.IGNORECASE),
    re.compile(r"\b(\d)\s*bd\b", re.IGNORECASE),
    re.compile(r"\b(\d)\s*bed(?:room)?s?\b", re.IGNORECASE),
]
_BED_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}
_BED_WORD_RE = re.compile(
    r"\b(one|two|three|four|five)\s+bed(?:room)?s?\b",
    re.IGNORECASE,
)


def _parse_price(title: str) -> int | None:
    m = _PRICE_RE.search(title)
    if not m:
        return None
    try:
        return int(m.group(1).replace(",", ""))
    except ValueError:
        return None


def _parse_beds(title: str) -> int | None:
    for pattern in _BEDS_PATTERNS:
        m = pattern.search(title)
        if m:
            return int(m.group(1))
    m = _BED_WORD_RE.search(title)
    if m:
        return _BED_WORDS[m.group(1).lower()]
    return None


# ---------- direct public sources ----------

_JSONLD_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
_HREF_RE = re.compile(
    r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
_SCRIPT_STYLE_RE = re.compile(
    r"<(script|style)\b[^>]*>.*?</\1>",
    re.IGNORECASE | re.DOTALL,
)
_TAG_RE = re.compile(r"<[^>]+>")
_SKIP_DIRECT_URL_RE = re.compile(
    r"(#|mailto:|tel:|javascript:|/privacy|/terms|/login|/sign[-_]?in|"
    r"/contact|/about|/blog|/careers|/press|/help|/sell|"
    r"\.(?:jpg|jpeg|png|gif|svg|webp|pdf|css|js)(?:\?|$))",
    re.IGNORECASE,
)


def fetch_direct_public_sources() -> tuple[list[Listing], list[SourceReport]]:
    """Fetch public search/vacancy pages and parse listing-looking records.

    This avoids logins, CAPTCHA handling, browser automation, and private
    sessions. Sites that return a block page or JS-only shell are recorded in
    the coverage report and still get Exa fallback coverage later.
    """
    listings: list[Listing] = []
    reports: list[SourceReport] = []

    for domain, url in DIRECT_SOURCE_SEEDS:
        source = f"direct:{domain}"
        try:
            resp = requests.get(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
                    "Accept-Language": "en-US,en;q=0.9",
                },
                timeout=30,
            )
        except requests.RequestException as exc:
            reports.append(SourceReport(source=source, url=url, status="error", note=str(exc)[:140]))
            continue

        if resp.status_code in {401, 403, 429}:
            reports.append(SourceReport(
                source=source,
                url=url,
                status="blocked",
                note=f"HTTP {resp.status_code}; kept Exa fallback only",
            ))
            time.sleep(0.2)
            continue
        if resp.status_code >= 400:
            reports.append(SourceReport(
                source=source,
                url=url,
                status="error",
                note=f"HTTP {resp.status_code}",
            ))
            time.sleep(0.2)
            continue

        html_text = resp.text
        parsed = _parse_direct_page(source, url, html_text)
        listings.extend(parsed)
        reports.append(SourceReport(
            source=source,
            url=url,
            status="ok",
            listings=len(parsed),
            note="parsed public page",
        ))
        time.sleep(0.2)

    return listings, reports


def _parse_direct_page(source: str, base_url: str, html_text: str) -> list[Listing]:
    out: list[Listing] = []
    seen_urls: set[str] = set()

    for ls in _parse_jsonld_listings(source, base_url, html_text):
        if ls.url not in seen_urls:
            seen_urls.add(ls.url)
            out.append(ls)

    for ls in _parse_anchor_listings(source, base_url, html_text):
        if ls.url not in seen_urls:
            seen_urls.add(ls.url)
            out.append(ls)

    return out


def _parse_jsonld_listings(source: str, base_url: str, html_text: str) -> list[Listing]:
    out: list[Listing] = []
    for m in _JSONLD_RE.finditer(html_text):
        raw = html.unescape(m.group(1).strip())
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue

        for node in _iter_json_nodes(data):
            if not isinstance(node, dict):
                continue
            url = _node_url(node)
            title = _node_text_value(node, "name") or _node_text_value(node, "headline")
            description = _node_text_value(node, "description")
            if not url or not (title or description):
                continue
            full_url = urljoin(base_url, url)
            text = _clean_text(" ".join(filter(None, [
                title,
                description,
                _node_text_value(node, "address"),
                _node_text_value(node, "offers"),
            ])))
            if not _RENTAL_HINTS.search(text):
                continue

            out.append(Listing(
                source=source,
                id=_url_listing_id(source, full_url),
                title=title or full_url,
                url=full_url,
                price=_price_from_jsonld(node) or _parse_price(text),
                beds=_parse_beds(text),
                neighborhood=None,
                posted=_node_text_value(node, "datePosted"),
                snippet=text[:500],
            ))
    return out


def _parse_anchor_listings(source: str, base_url: str, html_text: str) -> list[Listing]:
    out: list[Listing] = []
    for m in _HREF_RE.finditer(html_text):
        href = m.group(1).strip()
        if _SKIP_DIRECT_URL_RE.search(href):
            continue

        full_url = urljoin(base_url, html.unescape(href))
        parsed = urlparse(full_url)
        if parsed.scheme not in {"http", "https"}:
            continue
        if parsed.netloc and urlparse(base_url).netloc.replace("www.", "") not in parsed.netloc.replace("www.", ""):
            continue

        window_start = max(0, m.start() - 900)
        window_end = min(len(html_text), m.end() + 900)
        context = _clean_text(html_text[window_start:window_end])
        anchor_text = _clean_text(m.group(2))
        title = anchor_text or context[:140] or full_url
        haystack = f"{title} {context}"

        if not _RENTAL_HINTS.search(haystack):
            continue
        if _is_aggregator_url(full_url) and not _PRICE_RE.search(haystack):
            continue

        out.append(Listing(
            source=source,
            id=_url_listing_id(source, full_url),
            title=title[:180],
            url=full_url,
            price=_parse_price(haystack),
            beds=_parse_beds(haystack),
            neighborhood=None,
            posted=None,
            snippet=context[:500],
        ))
    return out


def _iter_json_nodes(data: object) -> Iterable[object]:
    if isinstance(data, list):
        for item in data:
            yield from _iter_json_nodes(item)
        return
    if not isinstance(data, dict):
        return

    yield data
    for key in ("@graph", "itemListElement", "mainEntity", "about", "offers"):
        value = data.get(key)
        if value is not None:
            yield from _iter_json_nodes(value)
    item = data.get("item")
    if isinstance(item, dict):
        yield from _iter_json_nodes(item)


def _node_url(node: dict) -> str | None:
    for key in ("url", "@id"):
        value = node.get(key)
        if isinstance(value, str):
            return value
    item = node.get("item")
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return _node_url(item)
    return None


def _node_text_value(node: object, key: str) -> str | None:
    if not isinstance(node, dict):
        return None
    value = node.get(key)
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        parts = [_node_text_value(item, key) or _flatten_json_text(item) for item in value]
        return " ".join(part for part in parts if part)
    if isinstance(value, dict):
        return _flatten_json_text(value)
    return None


def _flatten_json_text(value: object) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return " ".join(_flatten_json_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(_flatten_json_text(v) for v in value.values())
    return ""


def _price_from_jsonld(node: dict) -> int | None:
    offers = node.get("offers")
    if isinstance(offers, dict):
        for key in ("price", "lowPrice", "highPrice"):
            value = offers.get(key)
            if isinstance(value, (int, float)):
                return int(value)
            if isinstance(value, str):
                parsed = _parse_price(f"${value}") or _parse_price(value)
                if parsed:
                    return parsed
    return None


def _clean_text(raw: str) -> str:
    without_scripts = _SCRIPT_STYLE_RE.sub(" ", raw)
    without_tags = _TAG_RE.sub(" ", without_scripts)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def _url_listing_id(source: str, url: str) -> str:
    return f"{source}-{hashlib.sha1(_normalized_url(url).encode()).hexdigest()[:14]}"


def _normalized_url(url: str) -> str:
    parsed = urlparse(url)
    netloc = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.rstrip("/") or "/"
    return urlunparse((parsed.scheme.lower(), netloc, path, "", "", ""))


# ---------- exa ----------

def fetch_exa(api_key: str) -> list[Listing]:
    """Run a per-neighborhood neural sweep + a Reddit-specific sweep."""
    start_pub = (dt.date.today() - dt.timedelta(days=45)).isoformat()
    out: list[Listing] = []

    # Pass 1: open-web neural search per neighborhood.
    for n in NEIGHBORHOODS:
        q = (
            f"3 bedroom apartment for rent in {n.title()}, San Francisco "
            f"available now or June 2026, with monthly rent price and address"
        )
        out.extend(_exa_search(api_key, q, start_pub, n, source="exa", num_results=10))

    # Pass 2: Reddit sweep — people post sublets and rental leads on
    # r/sanfrancisco and r/AskSF that aggregators never see. Restrict to
    # user-thread URLs in keep().
    for n in NEIGHBORHOODS:
        q = (
            f"Reddit post: looking to sublet or rent out 3 bedroom apartment "
            f"in {n.title()}, San Francisco, June 2026, with rent and details"
        )
        out.extend(_exa_search(
            api_key, q, start_pub, n, source="exa-reddit",
            include_domains=REDDIT_DOMAINS, num_results=6,
        ))

    # Pass 3: per-aggregator sweep. Many sites gate their search pages, so we ask
    # Exa to return deep listing URLs from each domain. _is_aggregator_url drops
    # hub/category pages.
    target_phrase = (
        "Russian Hill, North Beach, Hayes Valley, Marina, or Pacific Heights, "
        "San Francisco"
    )
    for domain in AGGREGATOR_DOMAINS:
        q = (
            f"3 bedroom apartment for rent in {target_phrase} "
            f"with monthly rent price and address, available now"
        )
        out.extend(_exa_search(
            api_key, q, start_pub, "russian hill", source="exa-aggregator",
            include_domains=[domain], num_results=10,
        ))

    # Pass 4: local property manager sweep. These often list classic SF buildings
    # before or instead of aggregator feeds.
    for domain in PROPERTY_MANAGER_DOMAINS:
        q = (
            "3 bedroom apartment for rent in Russian Hill or North Beach, "
            "San Francisco, with monthly rent price and address"
        )
        out.extend(_exa_search(
            api_key, q, start_pub, "russian hill", source="exa-manager",
            include_domains=[domain], num_results=5,
        ))

    return out


def _exa_search(
    api_key: str,
    query: str,
    start_pub: str,
    query_hood: str,
    source: str,
    include_domains: list[str] | None = None,
    num_results: int = 8,
) -> list[Listing]:
    body: dict = {
        "query": query,
        "numResults": num_results,
        "useAutoprompt": True,
        "type": "neural",
        "startPublishedDate": start_pub,
        "contents": {
            "text": {"maxCharacters": 800},
            "highlights": {"numSentences": 2, "highlightsPerUrl": 1},
        },
    }
    if include_domains:
        body["includeDomains"] = include_domains

    try:
        resp = requests.post(
            "https://api.exa.ai/search",
            headers={"x-api-key": api_key, "content-type": "application/json"},
            json=body,
            timeout=30,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        print(f"  exa query failed ({query!r}): {exc}", file=sys.stderr)
        return []

    out: list[Listing] = []
    for r in resp.json().get("results", []):
        url = r.get("url", "")
        if not url or _is_aggregator_url(url):
            continue
        listing_id = f"{source}-{hashlib.sha1(url.encode()).hexdigest()[:14]}"

        title = html.unescape((r.get("title") or url).strip())
        text = (r.get("text") or "").strip()
        highlights = " ".join(r.get("highlights") or [])
        snippet = (highlights or text)[:500]
        snippet = re.sub(r"\s+", " ", snippet)

        out.append(Listing(
            source=source,
            id=listing_id,
            title=title,
            url=url,
            price=_parse_price(f"{title} {text}"),
            beds=_parse_beds(f"{title} {text}"),
            neighborhood=None,
            posted=r.get("publishedDate"),
            snippet=snippet,
            query_neighborhood=query_hood,
        ))
    time.sleep(0.15)
    return out


# Patterns that indicate Exa returned a category/index page, not a real listing.
_AGGREGATOR_PATTERNS = re.compile(
    r"/(\d+-bedroom-apartments-for-rent|apartments-for-rent|"
    r"apartments_for_rent|houses-for-rent|condos-for-rent|"
    r"rentals?/?$|search/?|browse/?|category/|tag/|topics?/|floorplans?/?)",
    re.IGNORECASE,
)

# URL paths that mean "for sale" rather than rental.
_FOR_SALE_PATTERNS = re.compile(
    r"/(homes?-for-sale|for-sale|homes-for-sale-details|sales?/|listings?/sale)",
    re.IGNORECASE,
)

# Titles like "Marina District Apartments" without a specific address are hub pages.
_HUB_TITLE_PATTERNS = re.compile(
    r"(^\s*\d+\s+(apartments|rentals|homes)\s+for\s+rent|"
    r"apartments\s+for\s+rent\s+\|\s+san\s+francisco|"
    r"apartments\s+for\s+rent\s+in\s+san\s+francisco)",
    re.IGNORECASE,
)

# Sale-style prices: 6+ digit dollar amounts ($500,000+). Real SF rents top out
# in the low tens of thousands per month even at the high end.
_SALE_PRICE_RE = re.compile(r"\$\s?[1-9]\d{0,2},\d{3},\d{3}|\$\s?[1-9]\d{2},\d{3}")


def _is_aggregator_url(url: str) -> bool:
    """True for category/index/search pages that aren't a single listing."""
    if _AGGREGATOR_PATTERNS.search(url):
        return True
    if _FOR_SALE_PATTERNS.search(url):
        return True
    # Highrises.com / similar: /apartments/{Neighborhood-Name_City_State} = hub
    if re.search(r"/apartments/[A-Z][a-z]+-?\w*_[A-Z]", url):
        return True
    if "zillow.com" in url and "/homedetails/" not in url and "/b/" not in url:
        return True
    if "apartments.com" in url and url.rstrip("/").count("/") < 4:
        return True
    return False


# ---------- firecrawl-routed sources ----------
#
# Sites that either anti-bot block our direct fetch (403/429) or serve a
# JS-only React shell with no inventory in the raw HTML. We route them
# through Firecrawl's /v1/scrape with structured JSON extraction (LLM-based)
# instead of writing a custom parser per site.
#
# Cost per call: roughly 5-10 Firecrawl credits per site for extraction +
# JS rendering. 21 sites/day ≈ 150 credits/day ≈ 4,500/month.
#
# Each entry corresponds to a sensible "SF 3BR rentals" landing URL. The
# Firecrawl schema below tells the LLM what fields to pull, so the same
# extraction logic works across all 21 layouts without site-specific code.

FIRECRAWL_SEEDS = [
    # Anti-bot blocked aggregators (return 403/429 on direct fetch).
    ("apartments.com", "https://www.apartments.com/san-francisco-ca/3-bedrooms/"),
    ("apartmentfinder.com", "https://www.apartmentfinder.com/California/San-Francisco-Apartments/3-Bedrooms"),
    ("apartmenthomeliving.com", "https://www.apartmenthomeliving.com/san-francisco-ca/apartments-for-rent/3-bedroom"),
    ("apartmentlist.com", "https://www.apartmentlist.com/ca/san-francisco?beds=3"),
    ("equityapartments.com", "https://www.equityapartments.com/san-francisco-apartments"),
    ("forrent.com", "https://www.forrent.com/find/CA/metro-San+Francisco/San+Francisco/beds-3"),
    ("hotpads.com", "https://hotpads.com/san-francisco-ca/3-bedroom-apartments-for-rent"),
    ("realtor.com", "https://www.realtor.com/apartments/San-Francisco_CA/beds-3"),
    # renthop.com dropped 2026-06-03: their search URL returns NYC inventory (no real SF coverage).
    ("trulia.com", "https://www.trulia.com/for_rent/San_Francisco,CA/3p_beds/"),
    # JS-only aggregators (return 200 but raw HTML has no listings).
    ("avaloncommunities.com", "https://www.avaloncommunities.com/california/san-francisco-apartments"),
    ("compass.com", "https://www.compass.com/for-rent/san-francisco-ca/3-bedrooms/"),
    ("padmapper.com", "https://www.padmapper.com/apartments/san-francisco-ca/3-beds"),
    ("rent.com", "https://www.rent.com/california/san-francisco-apartments/3-bedroom"),
    ("zumper.com", "https://www.zumper.com/apartments-for-rent/san-francisco-ca/3-beds"),
    # SF property managers (JS-only listing widgets).
    ("chandlerproperties.com", "https://chandlerproperties.com/"),
    ("gaetanirealestate.com", "https://www.gaetanirealestate.com/vacancies"),
    ("jwavro.com", "https://www.jwavro.com/rentals.php"),
    ("sfcityrents.com", "https://www.sfcityrents.com/"),
    ("trinitysf.com", "https://www.trinitysf.com/"),
    ("yeeproperties.com", "https://www.yeeproperties.com/vacancies"),
]

# Firecrawl LLM extraction schema. Same shape every site is normalized into.
_FIRECRAWL_LISTING_SCHEMA = {
    "type": "object",
    "properties": {
        "listings": {
            "type": "array",
            "description": (
                "Rental apartment listings shown on this page. Include only items "
                "that look like real for-rent units with a monthly price; skip "
                "ads, neighborhood hub pages, navigation links, and for-sale items."
            ),
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Listing title or property name"},
                    "url": {"type": "string", "description": "Detail-page URL (absolute or relative)"},
                    "price_per_month": {
                        "type": "number",
                        "description": "Monthly rent in USD as a number (no $ or commas)",
                    },
                    "bedrooms": {"type": "number", "description": "Bedroom count"},
                    "address": {"type": "string", "description": "Street address if shown"},
                    "neighborhood": {"type": "string", "description": "Neighborhood name if shown"},
                },
                "required": ["title", "url"],
            },
        },
    },
    "required": ["listings"],
}


def fetch_firecrawl_sources(api_key: str) -> tuple[list[Listing], list[SourceReport]]:
    """Pull rentals from JS-only / anti-bot-blocked sites via Firecrawl structured extract."""
    listings: list[Listing] = []
    reports: list[SourceReport] = []

    for domain, url in FIRECRAWL_SEEDS:
        source = f"firecrawl:{domain}"
        try:
            resp = requests.post(
                "https://api.firecrawl.dev/v1/scrape",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "url": url,
                    "formats": ["json"],
                    "jsonOptions": {"schema": _FIRECRAWL_LISTING_SCHEMA},
                    "waitFor": 5000,
                    "timeout": 90000,   # Firecrawl-side timeout (ms); some aggregators are slow
                },
                timeout=180,
            )
        except requests.RequestException as exc:
            reports.append(SourceReport(source=source, url=url, status="error", note=str(exc)[:140]))
            continue

        if resp.status_code != 200:
            reports.append(SourceReport(
                source=source, url=url, status="error",
                note=f"firecrawl HTTP {resp.status_code}: {resp.text[:120]}",
            ))
            continue

        payload = resp.json()
        if not payload.get("success"):
            reports.append(SourceReport(
                source=source, url=url, status="error",
                note=f"firecrawl error: {str(payload.get('error', ''))[:140]}",
            ))
            continue

        data = (payload.get("data") or {}).get("json") or {}
        raw_items = data.get("listings") or []

        parsed: list[Listing] = []
        for item in raw_items:
            if not isinstance(item, dict):
                continue
            detail_url = (item.get("url") or "").strip()
            if not detail_url:
                continue
            if detail_url.startswith("/"):
                detail_url = urljoin(url, detail_url)
            if not detail_url.startswith("http"):
                continue

            title_raw = item.get("title") or item.get("address") or detail_url
            address = (item.get("address") or "").strip()
            hood = (item.get("neighborhood") or "").strip()

            price = item.get("price_per_month")
            if isinstance(price, str):
                price = _parse_price(price)
            price_int = int(price) if isinstance(price, (int, float)) else None
            # LLM uses -1 / 0 as a "no price shown" sentinel — treat as unknown.
            if price_int is not None and price_int <= 0:
                price_int = None

            beds_raw = item.get("bedrooms")
            beds_int = None
            if isinstance(beds_raw, (int, float)):
                beds_int = int(beds_raw)
            elif isinstance(beds_raw, str):
                m = re.search(r"\d+", beds_raw)
                if m:
                    beds_int = int(m.group())

            snippet = " | ".join(p for p in [address, hood] if p)[:500]

            parsed.append(Listing(
                source=source,
                id=_url_listing_id(source, detail_url),
                title=str(title_raw)[:180],
                url=detail_url,
                price=price_int,
                beds=beds_int,
                neighborhood=address or hood or None,
                posted=None,
                snippet=snippet,
            ))

        listings.extend(parsed)
        reports.append(SourceReport(
            source=source, url=url, status="ok", listings=len(parsed),
            note="firecrawl rendered + json schema extracted",
        ))
        time.sleep(0.1)

    return listings, reports


# ---------- zillow (via firecrawl) ----------
#
# Direct-fetching Zillow returns 403 (PerimeterX). Firecrawl handles JS
# rendering + rotating residential proxies, so we route Zillow through their
# /v1/scrape endpoint and parse the __NEXT_DATA__ JSON blob that Zillow embeds
# on every search results page. Costs ~1 Firecrawl credit per URL fetched.
#
# Gated on FIRECRAWL_API_KEY; if missing, we skip with a warning (same way Exa
# would be skipped if EXA_API_KEY were missing, except Exa is currently
# required). Falls back gracefully — Zillow detail pages are still indexed by
# Exa, so a Firecrawl outage doesn't blind the whole pipeline.

ZILLOW_RENTAL_URL = "https://www.zillow.com/san-francisco-ca/rentals/"

_ZILLOW_NEXT_DATA_RE = re.compile(
    r'<script[^>]+id=["\']__NEXT_DATA__["\'][^>]*>(.*?)</script>',
    re.DOTALL,
)


ZILLOW_MAX_PAGES = 3  # Zillow returns ~40 listings/page; 3 pages covers SF 3BR rental inventory


def fetch_zillow_firecrawl(api_key: str) -> tuple[list[Listing], SourceReport]:
    """Pull SF rentals from Zillow via Firecrawl, paginated across ZILLOW_MAX_PAGES."""
    all_listings: list[Listing] = []
    seen_ids: set[str] = set()
    pages_fetched = 0
    errors: list[str] = []

    for page in range(1, ZILLOW_MAX_PAGES + 1):
        page_listings, error = _fetch_zillow_page(api_key, page)
        pages_fetched += 1
        if error:
            errors.append(f"page {page}: {error}")
            # Don't bail on a single page failure — try the next page.
            continue
        new_count = 0
        for ls in page_listings:
            if ls.id in seen_ids:
                continue
            seen_ids.add(ls.id)
            all_listings.append(ls)
            new_count += 1
        # If a page returns nothing new, we're past the end of results — stop.
        if new_count == 0 and page > 1:
            break

    note_bits = [
        f"firecrawl rendered + __NEXT_DATA__ parsed across {pages_fetched} page(s)",
    ]
    if errors:
        note_bits.append(f"errors: {'; '.join(errors)[:200]}")

    status = "ok" if all_listings else ("error" if errors else "ok")
    return all_listings, SourceReport(
        source="zillow",
        url=ZILLOW_RENTAL_URL,
        status=status,
        listings=len(all_listings),
        note=" | ".join(note_bits),
    )


def _fetch_zillow_page(api_key: str, page: int) -> tuple[list[Listing], str | None]:
    """Fetch a single page of Zillow SF rentals. Returns (listings, error_msg)."""
    # Zillow uses an opaque searchQueryState query param to encode filters and
    # pagination. We pre-filter on price/beds server-side so we don't waste
    # credits on listings that would be dropped anyway. mapBounds covers SF proper.
    search_state = {
        "pagination": {"currentPage": page} if page > 1 else {},
        "usersSearchTerm": "San Francisco, CA",
        "mapBounds": {
            "west": -122.5183,
            "east": -122.3551,
            "south": 37.7080,
            "north": 37.8324,
        },
        "isMapVisible": False,
        "filterState": {
            "fr": {"value": True},     # for rent
            "fsba": {"value": False},  # exclude for-sale-by-agent
            "fsbo": {"value": False},  # exclude for-sale-by-owner
            "nc": {"value": False},    # exclude new construction
            "cmsn": {"value": False},
            "auc": {"value": False},
            "fore": {"value": False},
            "mp": {"min": MIN_PRICE, "max": MAX_PRICE},
            "beds": {"min": MIN_BEDS, "max": MAX_BEDS},
        },
        "isListVisible": True,
    }
    from urllib.parse import quote  # local import keeps top-of-file diff small
    full_url = f"{ZILLOW_RENTAL_URL}?searchQueryState={quote(json.dumps(search_state))}"

    try:
        resp = requests.post(
            "https://api.firecrawl.dev/v1/scrape",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "url": full_url,
                "formats": ["rawHtml"],
                "waitFor": 3000,  # let the React app paint __NEXT_DATA__
            },
            timeout=90,
        )
    except requests.RequestException as exc:
        return [], str(exc)[:140]

    if resp.status_code != 200:
        return [], f"firecrawl HTTP {resp.status_code}: {resp.text[:120]}"

    payload = resp.json()
    if not payload.get("success"):
        return [], f"firecrawl error: {str(payload.get('error', ''))[:140]}"

    html_text = (payload.get("data") or {}).get("rawHtml") or ""
    if not html_text:
        return [], "empty rawHtml"

    return _parse_zillow_html(html_text), None


def _parse_zillow_html(html_text: str) -> list[Listing]:
    """Extract listings from Zillow's __NEXT_DATA__ JSON blob.

    Zillow's structure (as of 2026): props.pageProps.searchPageState.cat1
    .searchResults.listResults — array of dicts with zpid/detailUrl/address/
    price/beds. This schema has shifted before and will shift again; on any
    parse miss we return [] and let the source report show 0 listings so it's
    visible in coverage.
    """
    m = _ZILLOW_NEXT_DATA_RE.search(html_text)
    if not m:
        return []
    try:
        data = json.loads(html.unescape(m.group(1)))
    except json.JSONDecodeError:
        return []

    cur = data
    for key in ("props", "pageProps", "searchPageState", "cat1", "searchResults", "listResults"):
        if not isinstance(cur, dict):
            return []
        cur = cur.get(key)
        if cur is None:
            return []
    if not isinstance(cur, list):
        return []

    out: list[Listing] = []
    for node in cur:
        if not isinstance(node, dict):
            continue
        detail_url = node.get("detailUrl") or node.get("hdpUrl")
        if not detail_url:
            continue
        if detail_url.startswith("/"):
            detail_url = f"https://www.zillow.com{detail_url}"

        zpid = node.get("zpid") or node.get("id")
        address = node.get("address") or ""
        status_text = node.get("statusText") or ""
        title = address or status_text or detail_url

        price = None
        price_raw = node.get("unformattedPrice") or node.get("price")
        if isinstance(price_raw, (int, float)):
            price = int(price_raw)
        elif isinstance(price_raw, str):
            price = _parse_price(price_raw)

        beds = None
        beds_raw = node.get("beds")
        if isinstance(beds_raw, (int, float)):
            beds = int(beds_raw)

        # Stuff the full address into both `neighborhood` (for the digest
        # display) and the snippet (so matches_neighborhood() can find a SF
        # ZIP or neighborhood string in the haystack).
        snippet_parts = [address, status_text]
        var_data = node.get("variableData")
        if isinstance(var_data, dict):
            vd_text = var_data.get("text")
            if isinstance(vd_text, str):
                snippet_parts.append(vd_text)
        snippet = " | ".join(p for p in snippet_parts if p)[:500]

        listing_id = (
            f"zillow-{zpid}"
            if zpid
            else f"zillow-{hashlib.sha1(detail_url.encode()).hexdigest()[:12]}"
        )

        out.append(Listing(
            source="zillow",
            id=listing_id,
            title=title[:180],
            url=detail_url,
            price=price,
            beds=beds,
            neighborhood=address or None,
            posted=None,
            snippet=snippet,
        ))
    return out


# ---------- filtering ----------

_ZIP_RE = re.compile(r"\b(94\d{3})\b")
_CA_ZIP_RE = re.compile(r"\b(9\d{4})\b")


def _zip_neighborhood(text: str) -> str | None:
    """Return the target neighborhood if the text contains a target SF ZIP."""
    for m in _ZIP_RE.finditer(text):
        hood = SF_TARGET_ZIPS.get(m.group(1))
        if hood:
            return hood
    return None


def _has_nontarget_sf_zip(text: str) -> bool:
    """True if text contains an SF ZIP that's NOT in our target list — strong
    signal the listing is somewhere else in SF."""
    for m in _ZIP_RE.finditer(text):
        if m.group(1) not in SF_TARGET_ZIPS:
            return True
    return False


def _has_non_sf_zip(text: str) -> bool:
    """True if the result names a California ZIP outside San Francisco."""
    for m in _CA_ZIP_RE.finditer(text):
        if not m.group(1).startswith("941"):
            return True
    return False


_STALE_MARKERS = re.compile(
    r"\b(rented|leased|deposit taken|off market|no longer available|"
    r"property is no longer|unavailable|wait[\s-]?list|waitlist)\b",
    re.IGNORECASE,
)

_BLOCKED_LOCATION_MARKERS = re.compile(
    r"\b(tenderloin|tendernob|tender\s+nob|lower\s+nob(?:\s+hill)?|"
    r"polk\s+gulch|civic\s+center|south\s+beach)\b",
    re.IGNORECASE,
)

# Domains that appear in Exa results but aren't useful for SF rentals.
_BANNED_DOMAINS = {
    "thirdhome.com", "api.thirdhome.com",
    "airbnb.com", "vrbo.com", "homeaway.com", "vacasa.com",
    "hometogo.com", "booking.com", "hotels.com",
    "business.reddit.com",  # Reddit's corporate marketing, not user posts
    "redditinc.com",
    "loopnet.com",  # commercial real estate
    "crexi.com",   # commercial
}

# Indicator phrases that a snippet/title is actually about a rental listing.
_RENTAL_HINTS = re.compile(
    r"(\$\d[\d,]+|/mo\b|per month|for rent|to rent|available\s+\w+ \d|"
    r"\d\s*bed(room)?s?|\d\s*br\b|\d\s*bd\b|"
    r"sublet|sublease|lease starts|lease available|move[- ]in)",
    re.IGNORECASE,
)


def keep(listing: Listing) -> bool:
    """Filter by price, beds, neighborhood, staleness, and 'is this actually a rental listing?'"""
    haystack = f"{listing.title} {listing.neighborhood or ''} {listing.snippet}"
    matched_hood = listing.matches_neighborhood()
    if _BLOCKED_LOCATION_MARKERS.search(haystack):
        return False
    if _STALE_MARKERS.search(haystack):
        return False
    if listing.domain() in _BANNED_DOMAINS:
        return False
    if _has_non_sf_zip(haystack):
        return False
    # Sale-price formatting in the snippet ($XXX,XXX or $X,XXX,XXX) → for-sale, not rent.
    if _SALE_PRICE_RE.search(haystack):
        return False
    # Title is a generic hub like "12 Apartments for Rent in Marina"
    if _HUB_TITLE_PATTERNS.search(listing.title):
        return False
    if listing.price is not None:
        if listing.price < MIN_PRICE or listing.price > MAX_PRICE:
            return False
    if listing.beds is not None:
        if listing.beds < MIN_BEDS or listing.beds > MAX_BEDS:
            return False

    # Search/direct/firecrawl results need to actually look like a rental
    # listing, not a generic page.
    if (
        listing.source.startswith("exa")
        or listing.source.startswith("direct:")
        or listing.source.startswith("firecrawl:")
    ):
        if not _RENTAL_HINTS.search(haystack):
            return False
        if listing.beds is None:
            return False
        # Reddit-source results must be a user post, not a corporate page.
        if listing.source == "exa-reddit" and "/r/" not in listing.url:
            return False

    # If the text shows an SF ZIP outside our target list, it's elsewhere in SF — drop.
    if _has_nontarget_sf_zip(haystack) and _zip_neighborhood(haystack) is None and matched_hood is None:
        return False

    # Require either a literal neighborhood match or a target ZIP.
    if matched_hood is None:
        return False
    return True


# ---------- digest ----------

def render_markdown(
    new: list[Listing],
    total_seen: int,
    coverage_reports: list[SourceReport] | None = None,
) -> str:
    today = dt.date.today().isoformat()
    lines = [f"# Apartment hunt — {today}", ""]
    lines.append(
        f"**Criteria:** {f'{MIN_BEDS}BR' if MIN_BEDS == MAX_BEDS else f'{MIN_BEDS}-{MAX_BEDS}BR'}"
        f" · ideal <= ${IDEAL_MAX_PRICE:,} "
        f"(${IDEAL_MAX_PRICE // 3:,}/person) · stretch <= ${MAX_PRICE:,} · "
        f"move by {MOVE_BY.isoformat()}"
    )
    lines.append(
        f"**Top priority:** {', '.join(n.title() for n in PREFERRED_NEIGHBORHOODS)}  ·  "
        f"**Fallback:** {', '.join(n.title() for n in FALLBACK_NEIGHBORHOODS)}  ·  "
        f"**Hard no:** Tenderloin / TenderNob / Lower Nob / Polk Gulch / Civic Center"
    )
    lines.append("")
    if not new:
        lines.append("_No new listings since last run._")
        lines.append("")
        lines.append(f"_(Tracking {total_seen} listings total.)_")
        _render_coverage(lines, coverage_reports or [])
        return "\n".join(lines)

    preferred = [ls for ls in new if ls.is_preferred()]
    other = [ls for ls in new if not ls.is_preferred()]

    summary_bits = []
    if preferred:
        summary_bits.append(f"**{len(preferred)} in Russian Hill / North Beach**")
    if other:
        summary_bits.append(f"{len(other)} in fallback neighborhoods")
    lines.append(" · ".join(summary_bits))
    lines.append("")

    if preferred:
        lines.append("## Top picks — Russian Hill & North Beach")
        lines.append("")
        _render_listings(lines, preferred)

    if other:
        lines.append("## Fallback neighborhoods")
        lines.append("")
        _render_listings(lines, other)

    lines.append(f"_(Tracking {total_seen} listings total.)_")
    _render_coverage(lines, coverage_reports or [])
    return "\n".join(lines)


def _render_listings(lines: list[str], listings: list[Listing]) -> None:
    for ls in sorted(listings, key=lambda x: (_neighborhood_rank(x), x.price or 99999)):
        price = f"${ls.price:,}" if ls.price else "price n/a"
        if ls.price is not None and ls.price > IDEAL_MAX_PRICE:
            price += " stretch"
        beds = f"{ls.beds}BR" if ls.beds else "?BR"
        # For Craigslist, show the raw location the seller typed. For Exa, show
        # the matched canonical neighborhood.
        if ls.source == "craigslist" and ls.neighborhood:
            hood_label = ls.neighborhood
        else:
            hood_label = (ls.matches_neighborhood() or ls.neighborhood or "?").title()
        source_tag = f" _[{ls.source} · {ls.domain()}]_"
        lines.append(f"- **[{ls.title}]({ls.url})**{source_tag}")
        lines.append(f"  · {price} · {beds} · {hood_label}")
        if ls.snippet:
            lines.append(f"  · _{ls.snippet[:220]}_")
        lines.append("")


def _render_coverage(lines: list[str], reports: list[SourceReport]) -> None:
    if not reports:
        return

    ok = sum(1 for report in reports if report.status == "ok")
    blocked = sum(1 for report in reports if report.status == "blocked")
    errors = len(reports) - ok - blocked

    lines.append("")
    lines.append("## Direct source coverage")
    lines.append("")
    lines.append(
        f"Checked {len(reports)} public source pages directly: "
        f"{ok} reachable, {blocked} blocked/rate-limited, {errors} errored."
    )
    lines.append("Sites with 0 parsed candidates may still be JS-only, empty, or covered through Exa.")
    lines.append("")

    for report in reports:
        label = report.source.removeprefix("direct:")
        count = f"{report.listings} raw candidate{'s' if report.listings != 1 else ''}"
        note = f" — {report.note}" if report.note else ""
        lines.append(f"- **{label}**: {report.status}, {count}{note}")
    lines.append("")


def _neighborhood_rank(ls: Listing) -> int:
    match = ls.matches_neighborhood()
    order = {
        "russian hill": 0,
        "north beach": 1,
        "hayes valley": 2,
        "marina": 3,
        "pacific heights": 4,
    }
    return order.get(match or "", 99)


def _dedupe_key(ls: Listing) -> str:
    if ls.source == "craigslist":
        return ls.id
    return _normalized_url(ls.url)


# ---------- main ----------

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="write markdown but do not update seen-set")
    parser.add_argument("--reset", action="store_true", help="clear seen-set and exit")
    args = parser.parse_args()

    if args.reset:
        if SEEN_PATH.exists():
            SEEN_PATH.unlink()
        print("seen-set cleared.")
        return 0

    # Load env from project dir.
    load_dotenv(ROOT / ".env")

    exa_key = os.environ.get("EXA_API_KEY")
    firecrawl_key = os.environ.get("FIRECRAWL_API_KEY")

    if not exa_key:
        print("ERROR: set EXA_API_KEY in .env", file=sys.stderr)
        return 1

    print("Fetching Craigslist…")
    cl = fetch_craigslist()
    print(f"  {len(cl)} raw listings")

    print("Fetching direct public sources…")
    direct, coverage_reports = fetch_direct_public_sources()
    print(f"  {len(direct)} raw listing candidates")
    print(f"  {len(coverage_reports)} direct source pages checked")

    firecrawl_routed: list[Listing] = []
    if firecrawl_key:
        print(f"Fetching {len(FIRECRAWL_SEEDS)} JS-only / blocked sources via Firecrawl…")
        firecrawl_routed, fc_reports = fetch_firecrawl_sources(firecrawl_key)
        print(f"  {len(firecrawl_routed)} raw listing candidates")
        coverage_reports.extend(fc_reports)
    else:
        print(f"Skipping {len(FIRECRAWL_SEEDS)} Firecrawl-routed sources: FIRECRAWL_API_KEY not set in .env")
        for domain, url in FIRECRAWL_SEEDS:
            coverage_reports.append(SourceReport(
                source=f"firecrawl:{domain}",
                url=url,
                status="skipped",
                note="FIRECRAWL_API_KEY not configured",
            ))

    print("Fetching Exa…")
    exa = fetch_exa(exa_key)
    print(f"  {len(exa)} raw listings")

    zillow: list[Listing] = []
    if firecrawl_key:
        print("Fetching Zillow via Firecrawl…")
        zillow, zillow_report = fetch_zillow_firecrawl(firecrawl_key)
        print(f"  {len(zillow)} raw listings ({zillow_report.status}: {zillow_report.note})")
        coverage_reports.append(zillow_report)
    else:
        print("Skipping Zillow: FIRECRAWL_API_KEY not set in .env")
        coverage_reports.append(SourceReport(
            source="zillow",
            url=ZILLOW_RENTAL_URL,
            status="skipped",
            note="FIRECRAWL_API_KEY not configured",
        ))

    all_listings = cl + direct + firecrawl_routed + exa + zillow

    # Dedup within this run (Exa often surfaces the same URL across queries).
    by_id: dict[str, Listing] = {}
    for ls in all_listings:
        by_id.setdefault(_dedupe_key(ls), ls)
    deduped = list(by_id.values())

    # Apply criteria filter.
    matched = [ls for ls in deduped if keep(ls)]
    print(f"  {len(matched)} match criteria (post-filter)")

    # Diff against seen.
    seen = load_seen()
    new = [ls for ls in matched if ls.id not in seen]
    print(f"  {len(new)} new since last run")

    # Render + write digest.
    md = render_markdown(new, total_seen=len(seen) + len(new), coverage_reports=coverage_reports)
    DIGEST_PATH.write_text(md)
    print(f"Wrote {DIGEST_PATH}")

    if args.dry:
        # Dry runs only update digest_latest.md, NEVER the dated archive — otherwise an
        # ad-hoc dry run clobbers the morning cron's archived digest for the same date.
        print("--dry: skipping seen-set update and dated archive")
    else:
        # Archive a dated copy from real (non-dry) runs only.
        ARCHIVE_DIR.mkdir(exist_ok=True)
        (ARCHIVE_DIR / f"{dt.date.today().isoformat()}.md").write_text(md)
        seen.update(ls.id for ls in matched)
        save_seen(seen)
        print(f"Updated seen-set at {SEEN_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
