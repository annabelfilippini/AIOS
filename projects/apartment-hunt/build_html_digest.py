"""Build a self-contained HTML digest of current matches for a city.

Runs the full scrape pipeline, applies the existing filter, and renders a
clickable HTML page styled to the Editorial Cream design system. Writes:
  - projects/apartment-hunt/digest_<city>_latest.html
  - ~/Desktop/apartment-hunt-<city>-{YYYY-MM-DD}.html

Usage:
  .venv/bin/python build_html_digest.py            # San Francisco (default)
  .venv/bin/python build_html_digest.py --city denver
"""

from __future__ import annotations

import argparse
import datetime as dt
import html as html_mod
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import apartment_hunt as ah  # noqa: E402
import profiles  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--city", default="sf", choices=sorted(profiles.PROFILES),
        help="which city profile to render (default: sf)",
    )
    args = parser.parse_args()
    ah.apply_profile(profiles.get_profile(args.city))

    load_dotenv(ROOT / ".env")
    exa_key = os.environ.get("EXA_API_KEY")
    firecrawl_key = os.environ.get("FIRECRAWL_API_KEY")
    if not exa_key:
        print("ERROR: EXA_API_KEY missing", file=sys.stderr)
        return 1

    print(f"City: {ah.CITY_LABEL}")
    print("Fetching all sources…")
    cl = ah.fetch_craigslist()
    direct, _ = ah.fetch_direct_public_sources()
    exa = ah.fetch_exa(exa_key)
    reddit, reddit_reports = ah.fetch_reddit()
    for r in reddit_reports:
        print(f"  reddit {r.source}: {r.status} ({r.note})")
    firecrawl_routed = []
    zillow = []
    if firecrawl_key:
        firecrawl_routed, _fr = ah.fetch_firecrawl_sources(firecrawl_key)
        zillow, _zr = ah.fetch_zillow_firecrawl(firecrawl_key)

    matched = filter_and_sort(
        cl + direct + firecrawl_routed + exa + zillow + reddit, firecrawl_key
    )
    print(f"  {len(matched)} matched")

    today = dt.date.today().isoformat()
    html = build_html(matched, today)

    out_project = ROOT / f"digest_{ah.ACTIVE_PROFILE.key}_latest.html"
    out_project.write_text(html)
    print(f"Wrote {out_project}")

    desktop = Path.home() / "Desktop" / f"apartment-hunt-{ah.ACTIVE_PROFILE.key}-{today}.html"
    desktop.write_text(html)
    print(f"Wrote {desktop}")
    return 0


def filter_and_sort(listings, firecrawl_key=None):
    """Dedupe, (optionally enrich detail pages,) keep, and sort.

    Sort order: priority hoods first, then garage-confirmed first, then hood
    rank, then price — so the houses you most want float to the top of each
    section and you never have to click through to learn there's no garage."""
    by_id = {}
    for ls in listings:
        by_id.setdefault(ah._dedupe_key(ls), ls)
    deduped = list(by_id.values())

    if ah.ENRICH_DETAILS and firecrawl_key:
        basic = [ls for ls in deduped if ah.keep_basic(ls)]
        print(f"  {len(basic)} candidates pass basic filter")
        ah.enrich_candidates(firecrawl_key, basic)
        matched = [ls for ls in basic if ah.keep(ls)]
    else:
        matched = [ls for ls in deduped if ah.keep(ls)]

    # Cross-source collapse: same street address from two sites (Zillow +
    # Highrises, or "238 Harrison" vs "238 N Harrison") becomes one card with the
    # garage signal merged. Runs after enrichment so garage_status is populated.
    before = len(matched)
    matched = ah.collapse_by_address(matched)
    if len(matched) != before:
        print(f"  collapsed {before} → {len(matched)} after cross-source address dedup")

    pref = set(ah.PREFERRED_NEIGHBORHOODS)
    matched.sort(key=lambda ls: (
        0 if (ls.matches_neighborhood() or "") in pref else 1,
        0 if ls.garage_status == "confirmed" else 1,
        ah._neighborhood_rank(ls),
        -len(ls.feature_matches()),
        ls.price or 99999,
    ))
    return matched


def _bucket(matched):
    """Split into (preferred, fallback, other). Nothing is dropped."""
    pref_set = set(ah.PREFERRED_NEIGHBORHOODS)
    fb_set = set(ah.FALLBACK_NEIGHBORHOODS)
    preferred, fallback, other = [], [], []
    for ls in matched:
        hood = ls.matches_neighborhood() or ""
        if hood in pref_set:
            preferred.append(ls)
        elif hood in fb_set:
            fallback.append(ls)
        else:
            other.append(ls)
    return preferred, fallback, other


# --------------------------------------------------------------------------- #
# Rendering — Editorial Cream design system.
# --------------------------------------------------------------------------- #

_STYLE = """
:root {
  --bg: #f4f0e6;
  --card: #fbf9f3;
  --ink: #211e1a;
  --muted: #8a8276;
  --line: #e3dbcb;
  --accent: #9a7b3f;          /* brass, the single accent */
  --serif: "Cormorant Garamond", Georgia, "Times New Roman", serif;
  --sans: "Jost", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  --mono: ui-monospace, "SF Mono", "SFMono-Regular", Menlo, Consolas, monospace;
}
* { box-sizing: border-box; }
body {
  font-family: var(--sans);
  background: var(--bg);
  color: var(--ink);
  margin: 0;
  padding: 64px 24px 96px;
  line-height: 1.5;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 800px; margin: 0 auto; }

header { margin-bottom: 8px; }
.eyebrow {
  font-family: var(--sans);
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 10px;
}
h1 {
  font-family: var(--serif);
  font-weight: 600;
  font-size: 46px;
  line-height: 1.05;
  letter-spacing: -0.01em;
  margin: 0 0 16px;
}
.criteria {
  font-size: 13.5px;
  color: var(--muted);
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  align-items: baseline;
}
.criteria .fig { font-family: var(--mono); color: var(--ink); font-size: 12.5px; }
.criteria .sep { color: var(--line); }
.rule { height: 1px; background: var(--line); margin: 28px 0 0; }

h2 {
  font-family: var(--serif);
  font-weight: 600;
  font-size: 27px;
  letter-spacing: -0.01em;
  margin: 44px 0 4px;
  display: flex;
  align-items: baseline;
  gap: 12px;
}
h2 .count {
  font-family: var(--mono);
  font-size: 12px;
  font-weight: 400;
  color: var(--muted);
  letter-spacing: 0;
}
.section-rule { height: 1px; background: var(--line); margin: 12px 0 22px; }

.card {
  background: var(--card);
  border: 1px solid var(--line);
  padding: 20px 22px;
  margin-bottom: 12px;
  display: flex;
  gap: 20px;
  align-items: flex-start;
  justify-content: space-between;
}
.card-body { flex: 1; min-width: 0; }
.card-title {
  font-family: var(--serif);
  font-size: 22px;
  font-weight: 600;
  line-height: 1.2;
  color: var(--ink);
  text-decoration: none;
}
.card-title:hover { color: var(--accent); }
.card-meta {
  display: flex;
  gap: 8px 16px;
  flex-wrap: wrap;
  align-items: center;
  margin-top: 12px;
  font-size: 13px;
  color: var(--muted);
}
.price { font-family: var(--mono); font-size: 14px; color: var(--ink); font-weight: 500; }
.price .stretch {
  font-family: var(--sans);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-left: 6px;
}
.beds { font-family: var(--mono); font-size: 13px; color: var(--ink); }
.tag {
  font-family: var(--sans);
  font-size: 10.5px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 3px 9px;
  border: 1px solid var(--ink);
  color: var(--ink);
  background: transparent;
}
.tag.hood { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.tag.src { border-color: var(--line); color: var(--muted); }
.tag.feat { border-color: var(--accent); color: var(--accent); text-transform: none; letter-spacing: 0.02em; }
/* Garage is the make-or-break feature, so it gets a filled, high-contrast badge. */
.tag.garage-yes { background: #2f5d3a; color: #f4f0e6; border-color: #2f5d3a; text-transform: none; letter-spacing: 0.02em; }
.tag.garage-no { border-color: #b04a3a; color: #b04a3a; text-transform: none; letter-spacing: 0.02em; }
.tag.garage-unverified { border-color: var(--line); color: var(--muted); text-transform: none; letter-spacing: 0.02em; }
.baths, .sqft { font-family: var(--mono); font-size: 13px; color: var(--ink); }
.domain { font-family: var(--mono); font-size: 11.5px; color: var(--muted); margin-top: 9px; }
.view {
  font-family: var(--sans);
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--accent);
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 0;
  padding-top: 6px;
}
.view:hover { color: var(--ink); }
.empty {
  color: var(--muted);
  font-style: italic;
  padding: 22px 0;
  font-family: var(--serif);
  font-size: 18px;
}
footer {
  margin-top: 64px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 12px;
}
footer .fig { font-family: var(--mono); color: var(--ink); }
"""


def build_html(matched, today):
    bed_label = f"{ah.MIN_BEDS}BR" if ah.MIN_BEDS == ah.MAX_BEDS else f"{ah.MIN_BEDS}-{ah.MAX_BEDS}BR"
    preferred, fallback, other = _bucket(matched)
    has_priority = bool(ah.PREFERRED_NEIGHBORHOODS)

    type_label = ah.LISTING_NOUN if ah.LISTING_NOUN != "apartment" else None
    crit_bits = [f'<span class="fig">{bed_label}</span>']
    if type_label:
        crit_bits.append(f'<span class="fig">{html_mod.escape(type_label)}</span>')
    # Budget doesn't matter when the ceiling is set absurdly high.
    if ah.MAX_PRICE >= 50000:
        crit_bits.append("budget: any")
    elif ah.IDEAL_MAX_PRICE == ah.MAX_PRICE:
        crit_bits.append(f'&le; <span class="fig">${ah.MAX_PRICE:,}</span>/mo')
    else:
        per_person = ah.IDEAL_MAX_PRICE // ah.NUM_PEOPLE
        crit_bits.append(
            f'ideal &le; <span class="fig">${ah.IDEAL_MAX_PRICE:,}</span> '
            f'(<span class="fig">${per_person:,}</span>/person)'
        )
        crit_bits.append(f'stretch &le; <span class="fig">${ah.MAX_PRICE:,}</span>')
    want = [label for label, _ in ah.PREFERRED_KEYWORDS if label != ah.LISTING_NOUN]
    if want:
        crit_bits.append("want " + ", ".join(want))
    if ah.MOVE_BY:
        crit_bits.append(f'move by <span class="fig">{ah.MOVE_BY.isoformat()}</span>')
    if has_priority:
        crit_bits.append(
            "priority "
            + ", ".join(n.title() for n in ah.PREFERRED_NEIGHBORHOODS)
        )
    else:
        crit_bits.append(f"{ah.CITY_LABEL} metro-wide")
    criteria = '<span class="sep">·</span>'.join(crit_bits)

    parts = [f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_mod.escape(ah.CITY_LABEL)} {bed_label} rentals · {today}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<style>{_STYLE}</style>
</head>
<body>
<div class="wrap">
<header>
  <p class="eyebrow">Apartment hunt · {today}</p>
  <h1>{html_mod.escape(ah.CITY_LABEL)} {bed_label} rentals</h1>
  <div class="criteria">{criteria}</div>
</header>
<div class="rule"></div>
"""]

    if has_priority:
        pref_title = " & ".join(n.title() for n in ah.PREFERRED_NEIGHBORHOODS)
        parts.append(_section(f"Top picks", f"{pref_title}", preferred, hood_filled=True))
        parts.append(_section("Fallback neighborhoods", "", fallback, hood_filled=False))
        if other:
            parts.append(_section("Elsewhere in the city", "", other, hood_filled=False))
    else:
        parts.append(_section(f"{ah.CITY_LABEL} {bed_label}", "", other or fallback or preferred, hood_filled=False))

    total = len(matched)
    garage_yes = sum(1 for ls in matched if ls.garage_status == "confirmed")
    garage_line = ""
    if ah.ENRICH_DETAILS and total:
        garage_line = (
            f'<span class="fig">{garage_yes}</span> of <span class="fig">{total}</span> '
            f"have a confirmed garage (read from the full listing page).<br>"
        )
    parts.append(f"""<footer>
  <span class="fig">{total}</span> listing{"" if total == 1 else "s"} match {bed_label} criteria across all sources today.<br>
  {garage_line}Sources: Craigslist, direct aggregator and property-manager pages, institutional SFH landlords, FRBO / by-owner sites, Reddit owner-direct posts, Zillow, plus per-listing detail-page enrichment.
</footer>
</div>
</body>
</html>""")
    return "".join(parts)


def _section(title, subtitle_count, listings, hood_filled):
    label = f' <span class="count">{subtitle_count} · {len(listings)}</span>' if subtitle_count \
        else f' <span class="count">{len(listings)}</span>'
    head = f'<h2>{html_mod.escape(title)}{label}</h2><div class="section-rule"></div>'
    if not listings:
        return head + '<div class="empty">Nothing here today.</div>'
    return head + "".join(_card(ls, hood_filled) for ls in listings)


def _card(ls, hood_filled):
    title = html_mod.escape(ls.title)
    url = html_mod.escape(ls.url, quote=True)
    source = html_mod.escape(ls.source)
    domain = html_mod.escape(ls.domain())

    if ls.price is not None:
        stretch = '<span class="stretch">stretch</span>' if ls.price > ah.IDEAL_MAX_PRICE else ""
        price_html = f'<span class="price">${ls.price:,}/mo{stretch}</span>'
    else:
        price_html = '<span class="price">price n/a</span>'

    beds_html = f'<span class="beds">{ls.beds}BR</span>' if ls.beds is not None else '<span class="beds">?BR</span>'
    baths_html = ""
    if ls.bathrooms is not None:
        bath_label = f"{ls.bathrooms:g}BA"
        baths_html = f'<span class="baths">{bath_label}</span>'
    sqft_html = f'<span class="sqft">{ls.sqft:,} sqft</span>' if ls.sqft else ""

    # Garage badge — the feature Annabel most cares about. Driven by the detail
    # page we read, not a keyword guess: confirmed / none found / unverified.
    if ls.garage_status == "confirmed":
        garage_html = '<span class="tag garage-yes">&check; garage</span>'
    elif ls.garage_status == "none found":
        garage_html = '<span class="tag garage-no">no garage found</span>'
    elif ah.ENRICH_DETAILS:
        garage_html = '<span class="tag garage-unverified">garage unverified</span>'
    else:
        garage_html = ""
    office_html = '<span class="tag feat">&check; office</span>' if ls.has_office else ""

    # Craigslist shows the raw seller location; everything else shows the matched hood.
    if ls.source == "craigslist" and ls.neighborhood:
        hood = ls.neighborhood
    else:
        hood = ls.matches_neighborhood() or ""
    hood_tag = ""
    if hood:
        cls = "tag hood" if hood_filled else "tag"
        hood_tag = f'<span class="{cls}">{html_mod.escape(hood.title())}</span>'

    # Garage / office / baths now come from the enriched page; keep only the
    # soft keyword features the enrichment doesn't cover (e.g. open floor plan).
    _authoritative = {"house", "garage", "office", "2 bath"}
    feat_tags = "".join(
        f'<span class="tag feat">&check; {html_mod.escape(f)}</span>'
        for f in ls.feature_matches() if f not in _authoritative
    )

    return f"""
<div class="card">
  <div class="card-body">
    <a class="card-title" href="{url}" target="_blank" rel="noopener">{title}</a>
    <div class="card-meta">
      {price_html}
      {beds_html}
      {baths_html}
      {sqft_html}
      {hood_tag}
      {garage_html}
      {office_html}
      {feat_tags}
      <span class="tag src">{source}</span>
    </div>
    <div class="domain">{domain}</div>
  </div>
  <a class="view" href="{url}" target="_blank" rel="noopener">View &nearr;</a>
</div>
"""


if __name__ == "__main__":
    sys.exit(main())
