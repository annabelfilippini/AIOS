#!/usr/bin/env python3
"""Build a single self-contained review.html with all 6 carousel slides embedded
as base64. Drops a copy on the Desktop per Annabel's global preference."""
import base64
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
OUT = ROOT / "review.html"
DESKTOP = Path.home() / "Desktop" / "vh-intro-carousel-review.html"
LOGO = ROOT.parent.parent / "logo-options" / "bird-filled-deep-forest.png"

COLORS = {
    "cream": "#F5EFE0", "paper": "#FBF7EC", "primary": "#1F4D2A",
    "accent": "#C9A04A", "ink": "#2A2A26", "muted": "#7A776B", "line": "#DED3B8",
}

SLIDE_NOTES = [
    ("Hero — preventive frame", "carousel-hero-human-touch", "Woman at sunlit window with tea, Austin trees beyond. 'Medicine that catches it before it catches you' — the preventive thesis of the practice in one line."),
    ("The why — Julie's ER insight", "forest-emphasis-word + botanical-still-life", "Most emergencies were preventable. Dr. Swett spent 23 years in the ER watching it happen, then built Vital Health. Growing herbs on a sunlit windowsill anchor the 'alive, preventive' visual."),
    ("First visit — long-form consult", "carousel-artifact-ui (styled still-life)", "Ninety-minute first visit. Tea, folded intake card, rosemary, leafy shadow on bright cream. The one paper slide of the carousel. Pulls from 'long enough to read your story before we write any of it.'"),
    ("Diagnostics — measurement", "botanical-still-life", "Measurement that takes weeks, not minutes. Four sets of eyes, one coordinated record. Direct language from the website's about page. Bright amber bottle + marble + leaves."),
    ("Care relationship — loud", "carousel-loud-stat (re-cast as the brand's central line)", "Care that reads more like a relationship. Older man walking through Austin wildflowers toward the downtown skyline. The carousel's masculine slide and the preventive-care lived experience."),
    ("Sign-off — free 30-min call", "carousel-signoff-cta", "Woman walking into the sunlit clinic reception. 'Start with a free thirty-minute call' — the actual first step Vital Health offers, per the website."),
]


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode("ascii")


def main():
    imgs = {n: b64(IMAGES / f"slide-{n}.png") for n in range(1, 7)}
    logo_b64 = b64(LOGO)
    cards = []
    for n in range(1, 7):
        title, move, note = SLIDE_NOTES[n - 1]
        cards.append(f"""
        <article class="slide">
          <div class="slide-frame">
            <img alt="Slide {n}" src="data:image/png;base64,{imgs[n]}" />
          </div>
          <div class="meta">
            <div class="meta-row"><span class="num">{n:02d}</span><span class="title">{title}</span></div>
            <div class="move">Move: <code>{move}</code></div>
            <div class="note">{note}</div>
          </div>
        </article>""")
    cards_html = "\n".join(cards)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Vital Health — Intro Carousel — Review</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500;600&display=swap');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: {COLORS['paper']}; color: {COLORS['ink']}; font-family: 'Inter', sans-serif; }}
body {{ padding: 64px 48px 96px; max-width: 1280px; margin: 0 auto; }}
header {{ margin-bottom: 56px; padding-bottom: 32px; border-bottom: 1px solid {COLORS['line']}; }}
.header-row {{
  display: flex; gap: 18px; align-items: center; justify-content: center;
}}
.header-row .bird {{
  width: 42px; height: 42px; display: block;
}}
.header-row .wordmark {{
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 400;
  font-size: 34px;
  color: {COLORS['primary']};
  letter-spacing: -0.005em;
  line-height: 1;
}}
.summary {{
  margin-top: 36px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  font-size: 13px;
  color: {COLORS['muted']};
}}
.summary .card {{
  background: {COLORS['cream']};
  padding: 14px 16px;
  border-left: 2px solid {COLORS['accent']};
}}
.summary .card strong {{ display: block; color: {COLORS['ink']}; font-weight: 600; margin-bottom: 4px; font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; }}
.grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px 56px;
  margin-top: 48px;
}}
.slide {{
  display: flex;
  flex-direction: column;
}}
.slide-frame {{
  width: 100%;
  aspect-ratio: 4 / 5;
  background: {COLORS['cream']};
  box-shadow: 0 4px 30px rgba(22, 56, 32, 0.10), 0 1px 2px rgba(0,0,0,0.06);
  overflow: hidden;
}}
.slide-frame img {{
  width: 100%; height: 100%; object-fit: cover; display: block;
}}
.meta {{ padding: 18px 4px 0; }}
.meta-row {{
  display: flex; gap: 14px; align-items: baseline;
  border-bottom: 1px solid {COLORS['line']};
  padding-bottom: 8px;
  margin-bottom: 10px;
}}
.num {{
  font-family: 'Fraunces', serif;
  font-size: 32px;
  color: {COLORS['accent']};
  font-weight: 500;
}}
.title {{
  font-family: 'Fraunces', serif;
  font-size: 22px;
  color: {COLORS['ink']};
  font-weight: 500;
}}
.move {{ font-size: 12px; color: {COLORS['muted']}; margin-bottom: 8px; letter-spacing: 0.04em; }}
.move code {{
  background: {COLORS['cream']};
  padding: 2px 6px;
  color: {COLORS['primary']};
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
}}
.note {{ font-size: 14px; line-height: 1.55; color: {COLORS['ink']}; }}
footer {{
  margin-top: 72px;
  padding-top: 32px;
  border-top: 1px solid {COLORS['line']};
  text-align: center;
  font-size: 12px;
  color: {COLORS['muted']};
  letter-spacing: 0.08em;
}}
footer .accent {{ color: {COLORS['accent']}; }}
.caption-block {{
  margin-top: 80px;
  background: {COLORS['cream']};
  padding: 36px 40px;
  border-left: 3px solid {COLORS['accent']};
}}
.caption-block h2 {{
  font-family: 'Fraunces', serif;
  font-weight: 400;
  font-size: 22px;
  color: {COLORS['primary']};
  margin-bottom: 18px;
}}
.caption-block p {{ font-size: 15px; line-height: 1.65; color: {COLORS['ink']}; margin-bottom: 12px; }}
.caption-block .tags {{ font-size: 13px; color: {COLORS['muted']}; margin-top: 14px; }}
</style>
</head>
<body>
<header>
  <div class="header-row">
    <img class="bird" alt="" src="data:image/png;base64,{logo_b64}" />
    <span class="wordmark">Vital Health Instagram</span>
  </div>
  <div class="summary">
    <div class="card"><strong>Brand</strong>Vital Health · Integrative Medicine · Austin, TX</div>
    <div class="card"><strong>Format</strong>Instagram carousel · 6 slides · 1080×1350 · 4:5</div>
    <div class="card"><strong>Pipeline</strong>gpt-image-1 photos + brand-token HTML chrome + Playwright composite</div>
  </div>
</header>

<section class="grid">
{cards_html}
</section>

<section class="caption-block">
  <h2>Suggested post caption</h2>
  <p>Dr. Julie Swett spent twenty-three years working the ER in Austin. She kept seeing the same pattern. Most of what came through the door was not random. It was the late chapter of something that could have been caught much earlier.</p>
  <p>That is why she built Vital Health. Ninety-minute first visits. Comprehensive labs that take weeks to read, not minutes. Four practitioners, one coordinated record, four sets of eyes on every chart. Care here reads more like a relationship than an appointment.</p>
  <p>If you want to know whether we are the right fit, the first step is a free thirty-minute call. <strong>vitalhealthaustin.com</strong>.</p>
  <p class="tags">#integrativemedicine · #preventivemedicine · #functionalmedicine · #austintx · #austinhealth</p>
</section>

<footer>
  Generated <span class="accent">·</span> 2026-05-31 <span class="accent">·</span> /Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/
</footer>
</body>
</html>"""

    OUT.write_text(html, encoding="utf-8")
    DESKTOP.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUT, DESKTOP)
    print(f"wrote {OUT} ({len(html)//1024} KB)")
    print(f"copied to {DESKTOP}")


if __name__ == "__main__":
    main()
