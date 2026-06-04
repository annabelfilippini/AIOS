"""Rebuild the menu body of all menu-* pages from menu-final.json.

Preserves the existing <header>, <footer>, hero section, and other-menus footer
of each page. Only the <section class="menu-body"> content is replaced so we get
clean rendering from fresh data without touching the page chrome.
"""

import json
import re
from html import escape
from pathlib import Path

BASE = Path(__file__).resolve().parent
MOCK_DIR = BASE / "mockups"
data = json.loads((BASE / "menu-final.json").read_text())
by_tab = data["by_tab"]
notes = data.get("notes", {})


def render_item(it):
    title = escape(it["title"])
    price = escape(it["price"])
    desc = escape(it["description"]) if it["description"] else ""
    return f'''<li class="menu-item" data-reveal>
  <div class="menu-item-row">
    <h3 class="menu-item-title">{title}</h3>
    <span class="menu-item-price">{price}</span>
  </div>
  {f'<p class="menu-item-desc">{desc}</p>' if desc else ''}
</li>'''


def render_items(items):
    return "\n".join(render_item(it) for it in items)


def group_by(items, field):
    groups = {}
    order = []
    for it in items:
        k = it[field]
        if k not in groups:
            order.append(k)
            groups[k] = []
        groups[k].append(it)
    return order, groups


def render_sections_by_section(items, section_label=None, section_title=None):
    """Group by `section` field, render each as its own block with <h2>."""
    order, groups = group_by(items, "section")
    blocks = []
    if section_label or section_title:
        blocks.append(f'''<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    {f'<span class="label">{escape(section_label)}</span>' if section_label else ''}
    {f'<h2>{escape(section_title)}</h2>' if section_title else ''}
  </div>
</div>''')
    for k in order:
        items_group = groups[k]
        # If all items share the same group, render subgroup headers too
        subgroup_order, subgroups = group_by(items_group, "group")
        if len(subgroup_order) > 1 or (len(subgroup_order) == 1 and subgroup_order[0]):
            sub_html = []
            for s in subgroup_order:
                header = f'<h3 class="menu-subgroup">{escape(s)}</h3>' if s else ''
                sub_html.append(f'''<div class="menu-subgroup-block" data-reveal-group>
  {header}
  <ul class="menu-items">
    {render_items(subgroups[s])}
  </ul>
</div>''')
            inner = "\n".join(sub_html)
        else:
            inner = f'<ul class="menu-items">{render_items(items_group)}</ul>'
        blocks.append(f'''<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <h2>{escape(k or "")}</h2>
  </div>
  {inner}
</div>''')
    return "\n".join(blocks)


def build_body_single_tab(tab):
    """Most pages render a single tab — LUNCH, DINNER, SUSHI, HAPPY HOUR, BEER."""
    items = by_tab[tab]
    return render_sections_by_section(items)


def build_body_cocktails():
    """Signature Cocktails + Spirit Free + Full Bar."""
    out = []
    out.append('''<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Signature Martinis and Cocktails</span>
    <h2>Signature Cocktails</h2>
  </div>
  <ul class="menu-items">
''' + render_items(by_tab["SIGNATURE COCKTAILS"]) + '''
  </ul>
</div>''')
    out.append('''<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Non-alcoholic</span>
    <h2>Spirit Free</h2>
  </div>
  <ul class="menu-items">
''' + render_items(by_tab["SPIRIT FREE"]) + '''
  </ul>
</div>''')
    out.append(f'''<div class="full-bar-block" data-reveal-group>
  <span class="label" data-reveal>Full Bar</span>
  <h2 data-reveal style="font-family: var(--display, 'Cormorant Garamond', serif); font-weight: 400; font-size: clamp(28px, 3vw, 36px); margin: 16px 0;">Full Bar</h2>
  <p class="prose" data-reveal>{escape(notes.get("spirits_replacement_text", ""))}</p>
</div>''')
    return "\n".join(out)


def build_body_wine():
    glass = by_tab["WINE BY THE GLASS"]
    bottle = by_tab["BOTTLED WINE"]
    # By-glass: grouped by section (BUBBLES/WHITE/RED)
    # Bottled: grouped by group (BUBBLES/WHITE/RED)
    def render_subgrouped(items, key):
        order, groups = group_by(items, key)
        html = []
        for k in order:
            header = f'<h3 class="menu-subgroup">{escape(k or "")}</h3>' if k else ''
            html.append(f'''<div class="menu-subgroup-block" data-reveal-group>
  {header}
  <ul class="menu-items">
    {render_items(groups[k])}
  </ul>
</div>''')
        return "\n".join(html)

    return f'''<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Poured Daily</span>
    <h2>By the Glass</h2>
    <p class="menu-section-note">Prices shown as glass / bottle.</p>
  </div>
  {render_subgrouped(glass, "section")}
</div>
<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Cellar</span>
    <h2>Bottled Wine</h2>
  </div>
  {render_subgrouped(bottle, "group")}
</div>'''


PAGE_BUILDERS = {
    "menu-lunch.html": lambda: build_body_single_tab("LUNCH"),
    "menu-dinner.html": lambda: build_body_single_tab("DINNER"),
    "menu-sushi.html": lambda: build_body_single_tab("SUSHI"),
    "menu-happy-hour.html": lambda: build_body_single_tab("HAPPY HOUR"),
    "menu-beer.html": lambda: build_body_single_tab("BEER"),
    "menu-cocktails.html": build_body_cocktails,
    "menu-wine.html": build_body_wine,
}


# Regex to replace the menu-body contents in existing pages.
BODY_RE = re.compile(
    r'(<section class="menu-body"[^>]*>\s*<div class="container">)(.*?)(</div>\s*</section>)',
    re.DOTALL,
)


for page_name, builder in PAGE_BUILDERS.items():
    path = MOCK_DIR / page_name
    if not path.exists():
        print(f"SKIP (missing): {page_name}")
        continue
    html = path.read_text()
    new_body = builder()
    replacement = r'\g<1>' + "\n" + new_body + "\n" + r'\g<3>'
    new_html, n = BODY_RE.subn(replacement, html)
    if n == 0:
        print(f"WARN: no menu-body found in {page_name}")
        continue
    path.write_text(new_html)
    print(f"Rebuilt {page_name} ({n} block replaced)")
