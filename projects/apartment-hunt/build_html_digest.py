"""Build a self-contained HTML digest of current 3BR matches.

Runs the full scrape pipeline, applies the existing filter, and renders a
clickable HTML page. Writes two copies:
  - projects/apartment-hunt/digest_latest.html
  - ~/Desktop/apartment-hunt-3br-{YYYY-MM-DD}.html

Usage:
  .venv/bin/python build_html_digest.py
"""

from __future__ import annotations

import datetime as dt
import html as html_mod
import os
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from apartment_hunt import (  # noqa: E402
    fetch_craigslist,
    fetch_direct_public_sources,
    fetch_exa,
    fetch_zillow_firecrawl,
    keep,
    _dedupe_key,
    PREFERRED_NEIGHBORHOODS,
    FALLBACK_NEIGHBORHOODS,
    MIN_PRICE,
    IDEAL_MAX_PRICE,
    MAX_PRICE,
    MIN_BEDS,
    MAX_BEDS,
    MOVE_BY,
)


def main() -> int:
    load_dotenv(ROOT / ".env")
    exa_key = os.environ.get("EXA_API_KEY")
    firecrawl_key = os.environ.get("FIRECRAWL_API_KEY")
    if not exa_key:
        print("ERROR: EXA_API_KEY missing", file=sys.stderr)
        return 1

    print("Fetching all sources…")
    cl = fetch_craigslist()
    direct, _ = fetch_direct_public_sources()
    exa = fetch_exa(exa_key)
    zillow = []
    if firecrawl_key:
        zillow, _zr = fetch_zillow_firecrawl(firecrawl_key)

    # Dedupe.
    by_id: dict = {}
    for ls in cl + direct + exa + zillow:
        by_id.setdefault(_dedupe_key(ls), ls)
    deduped = list(by_id.values())
    matched = [ls for ls in deduped if keep(ls)]
    print(f"  {len(matched)} matched")

    # Sort: preferred neighborhoods first, then by price.
    def sort_key(ls):
        hood = ls.matches_neighborhood() or 'zzz'
        pref = 0 if hood in PREFERRED_NEIGHBORHOODS else 1
        return (pref, ls.price or 99999)

    matched.sort(key=sort_key)

    today = dt.date.today().isoformat()
    bed_label = f"{MIN_BEDS}BR" if MIN_BEDS == MAX_BEDS else f"{MIN_BEDS}-{MAX_BEDS}BR"
    html = build_html(matched, today, bed_label)

    # Write to project.
    out_project = ROOT / "digest_latest.html"
    out_project.write_text(html)
    print(f"Wrote {out_project}")

    # Mirror to Desktop.
    desktop = Path.home() / "Desktop" / f"apartment-hunt-3br-{today}.html"
    desktop.write_text(html)
    print(f"Wrote {desktop}")

    return 0


def build_html(matched, today, bed_label):
    pref_listings = [ls for ls in matched if (ls.matches_neighborhood() or '') in PREFERRED_NEIGHBORHOODS]
    fallback_listings = [ls for ls in matched if (ls.matches_neighborhood() or '') in FALLBACK_NEIGHBORHOODS]

    parts = []
    parts.append(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SF 3BR rentals · {today}</title>
<style>
  :root {{
    --ink: #1a1a1a;
    --muted: #6a6a6a;
    --accent: #2a5e8c;
    --bg: #faf8f4;
    --card: #ffffff;
    --line: #e5e0d6;
    --pill-pref: #2a5e8c;
    --pill-fallback: #8c6d2a;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
    background: var(--bg);
    color: var(--ink);
    margin: 0;
    padding: 40px 24px 80px;
    line-height: 1.5;
  }}
  .wrap {{ max-width: 880px; margin: 0 auto; }}
  header {{ margin-bottom: 32px; }}
  h1 {{
    font-size: 28px;
    font-weight: 600;
    margin: 0 0 8px;
    letter-spacing: -0.01em;
  }}
  .meta {{
    color: var(--muted);
    font-size: 14px;
  }}
  .meta strong {{ color: var(--ink); }}
  h2 {{
    font-size: 18px;
    font-weight: 600;
    margin: 40px 0 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--line);
  }}
  .count {{
    color: var(--muted);
    font-weight: 400;
    font-size: 14px;
    margin-left: 8px;
  }}
  .card {{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 20px 22px;
    margin-bottom: 14px;
    display: flex;
    gap: 20px;
    align-items: flex-start;
    justify-content: space-between;
  }}
  .card-body {{ flex: 1; min-width: 0; }}
  .card-title {{
    font-size: 16px;
    font-weight: 600;
    margin: 0 0 6px;
    color: var(--ink);
    text-decoration: none;
    display: inline-block;
  }}
  .card-title:hover {{ color: var(--accent); text-decoration: underline; }}
  .card-meta {{
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    font-size: 13px;
    color: var(--muted);
    margin-top: 8px;
  }}
  .price {{
    color: var(--ink);
    font-weight: 600;
  }}
  .pill {{
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: white;
    background: var(--pill-pref);
  }}
  .pill.fallback {{ background: var(--pill-fallback); }}
  .pill.outline {{
    background: transparent;
    color: var(--muted);
    border: 1px solid var(--line);
  }}
  .source {{
    font-size: 12px;
    color: var(--muted);
    margin-top: 4px;
  }}
  .button {{
    display: inline-block;
    background: var(--accent);
    color: white;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 6px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .button:hover {{ background: #1a4060; }}
  .empty {{
    color: var(--muted);
    font-style: italic;
    padding: 20px;
    text-align: center;
    border: 1px dashed var(--line);
    border-radius: 8px;
  }}
  footer {{
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 12px;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>SF apartments for rent — {today}</h1>
  <div class="meta">
    <strong>Criteria:</strong> {bed_label} ·
    ideal &le; ${IDEAL_MAX_PRICE:,} (${IDEAL_MAX_PRICE // 3:,}/person) ·
    stretch &le; ${MAX_PRICE:,} ·
    move by {MOVE_BY.isoformat()}
  </div>
  <div class="meta">
    <strong>Top priority:</strong> {', '.join(n.title() for n in PREFERRED_NEIGHBORHOODS)} &nbsp;·&nbsp;
    <strong>Fallback:</strong> {', '.join(n.title() for n in FALLBACK_NEIGHBORHOODS)}
  </div>
</header>
""")

    parts.append(f'<h2>Top picks <span class="count">· Russian Hill &amp; North Beach · {len(pref_listings)} listing{"" if len(pref_listings) == 1 else "s"}</span></h2>')
    parts.append(render_cards(pref_listings, preferred=True))

    parts.append(f'<h2>Fallback neighborhoods <span class="count">· {len(fallback_listings)} listing{"" if len(fallback_listings) == 1 else "s"}</span></h2>')
    parts.append(render_cards(fallback_listings, preferred=False))

    total = len(pref_listings) + len(fallback_listings)
    parts.append(f"""<footer>
  Generated {today} · {total} listing{"" if total == 1 else "s"} match {bed_label} criteria across all sources today.
  <br>Sources: Craigslist · 33 aggregator/property-manager pages · Exa neural search · Zillow (Firecrawl).
</footer>
</div>
</body>
</html>""")

    return "".join(parts)


def render_cards(listings, preferred):
    if not listings:
        return '<div class="empty">No matches in this category today.</div>'

    cards = []
    for ls in listings:
        title = html_mod.escape(ls.title)
        url = html_mod.escape(ls.url, quote=True)
        hood = (ls.matches_neighborhood() or '?').title()
        source = html_mod.escape(ls.source)
        domain = html_mod.escape(ls.domain())

        if ls.price is not None:
            stretch = " stretch" if ls.price > IDEAL_MAX_PRICE else ""
            price_str = f'<span class="price">${ls.price:,}</span>/mo{stretch}'
        else:
            price_str = '<span class="price">$?</span>'

        if ls.beds is not None:
            beds_str = f"{ls.beds}BR"
        else:
            beds_str = "?BR"

        pill_class = "pill" if preferred else "pill fallback"
        pill_label = hood

        cards.append(f"""
<div class="card">
  <div class="card-body">
    <a class="card-title" href="{url}" target="_blank" rel="noopener">{title}</a>
    <div class="card-meta">
      {price_str}
      <span>{beds_str}</span>
      <span class="{pill_class}">{pill_label}</span>
      <span class="pill outline">{source}</span>
    </div>
    <div class="source">{domain}</div>
  </div>
  <a class="button" href="{url}" target="_blank" rel="noopener">View listing &rarr;</a>
</div>
""")
    return "".join(cards)


if __name__ == "__main__":
    sys.exit(main())
