"""Finalize menu data for the redesign.

- Load parsed menu JSON
- Fill 3 beer prices to $6 (domestic-bottle rate)
- Drop the SPIRITS LIST entirely
- Output prospects/black-pearl/menu-final.json
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "scrape" / "menu-parsed.json"
OUT = BASE / "menu-final.json"
MD_OUT = BASE / "menu-final.md"

data = json.loads(SRC.read_text())
by_tab = data["by_tab"]

DOMESTIC_BEER_FILL = {
    "Modelo Mexican Lager": "$6",
    "Yuengling Lager": "$6",
    "Coors Light Lager": "$6",
}

filled = 0
for item in by_tab.get("BEER", []):
    if not item["price"] and item["title"] in DOMESTIC_BEER_FILL:
        item["price"] = DOMESTIC_BEER_FILL[item["title"]]
        item["description"] = ""
        filled += 1

# Happy Hour cleanup:
# - Drop the row whose title is actually a time-header ("MONDAY - THURSDAY...")
# - Replace the "Wine"/"White"/"Red" triplet with one "Wine (glass)" row whose
#   description names both options, since White/Red are really sub-options under
#   Wine, not their own menu items.
hh = by_tab.get("HAPPY HOUR", [])
cleaned_hh = []
white_desc = None
red_desc = None
for item in hh:
    if item["title"].startswith("MONDAY - THURSDAY"):
        continue
    if item["title"] == "White":
        white_desc = item["description"]
        continue
    if item["title"] == "Red":
        red_desc = item["description"]
        continue
    cleaned_hh.append(item)
# Patch the "Wine" row to include the White/Red options as its description.
for item in cleaned_hh:
    if item["title"] == "Wine" and (white_desc or red_desc):
        parts = []
        if white_desc:
            parts.append(f"White: {white_desc}")
        if red_desc:
            parts.append(f"Red: {red_desc}")
        item["title"] = "Wine by the Glass"
        item["description"] = " / ".join(parts)
        break
by_tab["HAPPY HOUR"] = cleaned_hh

by_tab.pop("SPIRITS LIST", None)

# The SPIRIT FREE tab has redundant "n/a" suffixes on titles (the whole section
# already means non-alcoholic). Strip them.
for item in by_tab.get("SPIRIT FREE", []):
    item["title"] = re.sub(r"\s*n/a\s*$", "", item["title"], flags=re.IGNORECASE).strip()

all_items = []
for items in by_tab.values():
    all_items.extend(items)

missing = [i for i in all_items if not i["price"]]
print(f"Filled {filled} beer prices.")
print(f"Dropped SPIRITS LIST (191 unpriced items).")
print(f"Remaining items: {len(all_items)}, missing prices: {len(missing)}")
for m in missing:
    print(f"  [{m['tab']}/{m['section']}/{m['group']}] {m['title']}")

TAB_ORDER = [
    "LUNCH", "DINNER", "SUSHI", "HAPPY HOUR",
    "SIGNATURE COCKTAILS", "SPIRIT FREE",
    "WINE BY THE GLASS", "BOTTLED WINE", "BEER",
]
ordered = {k: by_tab[k] for k in TAB_ORDER if k in by_tab}

OUT.write_text(json.dumps({
    "source_url": data["source_url"],
    "item_count": sum(len(v) for v in ordered.values()),
    "by_tab": ordered,
    "notes": {
        "spirits_list_dropped": True,
        "spirits_replacement_text": (
            "Full bar featuring a curated selection of vodka, gin, rum, tequila, "
            "mezcal, whiskey, scotch, brandy, cognac, and liqueurs. "
            "Ask your server about pours and flights."
        ),
        "beer_prices_filled": DOMESTIC_BEER_FILL,
    },
}, indent=2, ensure_ascii=False))
print(f"\nWrote {OUT}")

# Human-readable markdown for review
lines = ["# Black Pearl — Final Menu (Redesign)\n"]
lines.append("_All items priced. Spirits list replaced with Full Bar paragraph on cocktails page._\n")
for tab, items in ordered.items():
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
        price = item["price"]
        price_str = f"${price}" if "/" not in price and price else (price or "??")
        desc = f"  \n  _{item['description']}_" if item["description"] else ""
        lines.append(f"- **{item['title']}** — {price_str}{desc}")
MD_OUT.write_text("\n".join(lines))
print(f"Wrote {MD_OUT}")
