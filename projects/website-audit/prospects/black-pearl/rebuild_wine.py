"""Rebuild menu-wine.html cleanly using the grouped Bottled Wine data."""

import json
from html import escape
from pathlib import Path

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / "menu-final.json").read_text())

def render_items(items):
    parts = []
    for it in items:
        title = escape(it["title"])
        price = escape(it["price"])
        desc = escape(it["description"]) if it["description"] else ""
        parts.append(f'''<li class="menu-item" data-reveal>
  <div class="menu-item-row">
    <h3 class="menu-item-title">{title}</h3>
    <span class="menu-item-price">{price}</span>
  </div>
  {f'<p class="menu-item-desc">{desc}</p>' if desc else ''}
</li>''')
    return "\n".join(parts)


def render_grouped(items, group_field):
    groups = {}
    order = []
    for it in items:
        k = it[group_field]
        if k not in groups:
            order.append(k)
            groups[k] = []
        groups[k].append(it)
    parts = []
    for k in order:
        label = f'<h3 class="menu-subgroup">{escape(k)}</h3>' if k else ''
        parts.append(f'''<div class="menu-subgroup-block" data-reveal-group>
  {label}
  <ul class="menu-items">
    {render_items(groups[k])}
  </ul>
</div>''')
    return "\n".join(parts)


by_tab = data["by_tab"]
glass = by_tab["WINE BY THE GLASS"]
bottle = by_tab["BOTTLED WINE"]

# Glass items are grouped by section field (BUBBLES/WHITE/RED)
glass_html = render_grouped(glass, "section")
# Bottle items are grouped by group field (BUBBLES/WHITE/RED)
bottle_html = render_grouped(bottle, "group")

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wine — Black Pearl Ann Arbor</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<!--#include-header-->
<main>
  <section class="hero hero-short" data-reveal-group>
    <div class="hero-bg" style="background-image:url('assets/img/Hamachi-Crudo-4.jpg');"></div>
    <div class="hero-content">
      <div class="hero-eyebrow" data-reveal>By the Glass &amp; Bottle</div>
      <h1 class="hero-title" data-reveal>Wine</h1>
    </div>
  </section>

  <section class="menu-intro" data-reveal-group>
    <div class="container narrow" style="text-align:center;">
      <p class="prose" data-reveal>A hand-picked list of old-world and new-world producers, balanced across bubbles, whites, and reds.</p>
    </div>
  </section>

  <section class="menu-body" data-reveal-group>
    <div class="container">
      <div class="menu-section" data-reveal-group>
        <div class="menu-section-head" data-reveal>
          <span class="label">Poured Daily</span>
          <h2>By the Glass</h2>
          <p class="menu-section-note">Prices shown as glass / bottle.</p>
        </div>
        {glass_html}
      </div>

      <div class="menu-section" data-reveal-group>
        <div class="menu-section-head" data-reveal>
          <span class="label">Cellar</span>
          <h2>Bottled Wine</h2>
        </div>
        {bottle_html}
      </div>
    </div>
  </section>

  <section class="other-menus" data-reveal-group>
    <div class="container narrow" style="text-align:center;">
      <span class="label" data-reveal>Explore</span>
      <h2 class="section-title" data-reveal style="font-size:clamp(28px,3.2vw,36px);">Other Menus</h2>
      <nav class="other-menus-nav" data-reveal>
        <a href="menu-dinner.html">Dinner</a>
        <a href="menu-lunch.html">Lunch</a>
        <a href="menu-sushi.html">Sushi</a>
        <a href="menu-happy-hour.html">Happy Hour</a>
        <a href="menu-cocktails.html">Cocktails</a>
        <a href="menu-beer.html">Beer</a>
      </nav>
    </div>
  </section>
</main>
<!--#include-footer-->
<script src="assets/js/main.js"></script>
</body>
</html>
'''

out = BASE / "mockups" / "menu-wine.html"
# Preserve header and footer from the existing file
existing = out.read_text()

# Extract header block (from <header> to </header>) and footer (<footer> to </footer>)
import re
header_match = re.search(r'<header.*?</header>', existing, re.DOTALL)
footer_match = re.search(r'<footer.*?</footer>', existing, re.DOTALL)
if header_match and footer_match:
    page = page.replace("<!--#include-header-->", header_match.group(0))
    page = page.replace("<!--#include-footer-->", footer_match.group(0))
else:
    print("WARN: could not extract header/footer from existing page")

out.write_text(page)
print(f"Wrote {out}")
print(f"Glass items rendered: {len(glass)}")
print(f"Bottle items rendered: {len(bottle)}")
