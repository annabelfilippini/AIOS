"""Parse Black Pearl menu HTML into structured JSON with every item + price.

Uses BeautifulSoup for correct nested-span handling. The menu page has
<div aria-label="TABNAME"> blocks (LUNCH, DINNER, SUSHI, HAPPY HOUR,
SIGNATURE COCKTAILS, SPIRIT FREE, BEER, WINE BY THE GLASS, BOTTLED WINE,
SPIRITS LIST). Within each tab:
  .menu-section > .menu-section-header > .menu-section-title
  .menu-section > .menu-items > .menu-item >
    .menu-item-title
    .menu-item-description
    .menu-item-price-top or .menu-item-price-bottom
"""

import json
import re
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup  # type: ignore

BASE = Path(__file__).resolve().parent
HTML_PATH = BASE / "scrape" / "menu-raw.html"
OUT_PATH = BASE / "scrape" / "menu-parsed.json"
MD_PATH = BASE / "scrape" / "menu-parsed.md"

URL = "https://www.blackpearlannarbor.com/menu"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")
HTML_PATH.write_text(html)

soup = BeautifulSoup(html, "html.parser")

TAB_NAMES = [
    "LUNCH", "DINNER", "SUSHI", "HAPPY HOUR", "SIGNATURE COCKTAILS",
    "SPIRIT FREE", "BEER", "WINE BY THE GLASS", "BOTTLED WINE", "SPIRITS LIST",
]

LEGEND_TITLES = {
    "GF: Gluten Free by Nature", "V: Vegetarian", "VV: Vegan",
    "White", "Red", "BUBBLES", "WHITE", "RED",
}


def clean_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s


def price_from_node(node) -> str:
    """Render a price node like <span class="currency-sign">$</span>16 / <span>$</span>50 as '$16 / $50'."""
    if node is None:
        return ""
    # Get raw text but preserve $ sign explicitly
    text = node.get_text(separator="")
    text = clean_text(text)
    # BS4 get_text joined nested spans → gives us "$16" or "$12 / $50" directly
    text = re.sub(r"\s*/\s*", " / ", text)
    return text


by_tab = {}
all_items = []

# Items whose title is an all-caps wine category are actually sub-group headers,
# not items. Capture them as group labels for following rows.
SUBGROUP_LABELS = {"BUBBLES", "WHITE", "RED"}

for tab in TAB_NAMES:
    tab_root = soup.find(attrs={"aria-label": tab})
    if not tab_root:
        continue
    by_tab[tab] = []
    for section in tab_root.select(".menu-section"):
        section_title_el = section.select_one(".menu-section-title")
        section_title = clean_text(section_title_el.get_text()) if section_title_el else None
        current_subgroup = None
        for group_block in (section.select(".menu-group") or [section]):
            group_title_el = group_block.select_one(".menu-group-title") if group_block is not section else None
            group_title = clean_text(group_title_el.get_text()) if group_title_el else None
            for item in group_block.select(".menu-item"):
                title_el = item.select_one(".menu-item-title")
                if not title_el:
                    continue
                title = clean_text(title_el.get_text())
                if not title:
                    continue
                # GF/V/VV legend rows are always filtered.
                ALWAYS_DROP = {"GF: Gluten Free by Nature", "V: Vegetarian", "VV: Vegan"}
                if title in ALWAYS_DROP:
                    continue
                # All-caps wine categories (BUBBLES/WHITE/RED) are sub-group
                # headers — capture and continue.
                if title in SUBGROUP_LABELS:
                    current_subgroup = title
                    continue
                # Mixed-case "White"/"Red" only exist as items in HAPPY HOUR.
                CONTEXT_DROP = {"White", "Red"}
                if title in CONTEXT_DROP and tab != "HAPPY HOUR":
                    continue
                desc_el = item.select_one(".menu-item-description")
                desc_preview = clean_text(desc_el.get_text()) if desc_el else ""
                price_el_preview = item.select_one(".menu-item-price-top") or item.select_one(".menu-item-price-bottom")
                price_preview = price_from_node(price_el_preview)
                desc = desc_preview
                price = price_preview
                rec = {
                    "tab": tab,
                    "section": section_title,
                    "group": group_title or current_subgroup,
                    "title": title,
                    "description": desc,
                    "price": price,
                }
                by_tab[tab].append(rec)
                all_items.append(rec)

print(f"Total items parsed: {len(all_items)}")
for tab in TAB_NAMES:
    items = by_tab.get(tab, [])
    missing = [i for i in items if not i["price"] or i["price"] == "$"]
    print(f"  {tab}: {len(items)} items, {len(missing)} missing price")

missing = [i for i in all_items if not i["price"] or i["price"] == "$"]
print(f"\nTotal missing prices: {len(missing)}")
for i in missing[:30]:
    print(f"  [{i['tab']}/{i['section']}/{i['group']}] {i['title']} | price={i['price']!r}")

OUT_PATH.write_text(json.dumps({
    "source_url": URL,
    "item_count": len(all_items),
    "by_tab": by_tab,
    "missing_prices": [{"tab": i["tab"], "section": i["section"], "group": i["group"], "title": i["title"]} for i in missing],
}, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT_PATH}")

lines = ["# Black Pearl — Full Menu (Parsed)\n"]
for tab in TAB_NAMES:
    items = by_tab.get(tab, [])
    if not items:
        continue
    lines.append(f"\n## {tab}\n")
    cur_section = None
    cur_group = None
    for item in items:
        if item["section"] != cur_section:
            cur_section = item["section"]
            if cur_section:
                lines.append(f"\n### {cur_section}\n")
        if item["group"] != cur_group:
            cur_group = item["group"]
            if cur_group:
                lines.append(f"\n**{cur_group}**\n")
        price = item["price"] or "*(no price listed)*"
        desc = f"  \n  {item['description']}" if item["description"] else ""
        lines.append(f"- **{item['title']}** — {price}{desc}")
MD_PATH.write_text("\n".join(lines))
print(f"Wrote {MD_PATH}")
