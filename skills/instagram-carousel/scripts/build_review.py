#!/usr/bin/env python3
"""Build a self-contained review.html with all slides embedded as base64.
Drops a copy on the Desktop per Annabel's global preference.

Reads inputs.yaml from the working folder. Pulls slide titles + notes from
the per-slide role mapping; renders any number of slides (3-8).
"""
from __future__ import annotations

import argparse
import base64
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


SLIDE_TITLES = {
    1: ("Hero — preventive frame", "Brand's preventive thesis in one line. Full-bleed photo with veiled headline bottom-left."),
    2: ("The why — founder origin", "Founder origin story + real number. Split right-photo + left text. Display word = the contradiction the brand resolves."),
    3: ("First visit — what makes it different", "Specific minutes. Full-bleed photo with display word top-left. Uses secondary serif by default."),
    4: ("Diagnostics — measurement", "What's tested, how long, how many readers. Split left-photo + right text. Display word = the time scale."),
    5: ("Philosophy — pull quote", "Brand's central line about relationship / care / philosophy. Full-bleed photo with literary italic quote. Uses secondary serif by default."),
    6: ("Sign-off — real low-friction CTA", "Real low-friction first step. Centered cream typography on dark-veiled photo, brand mark at base."),
}


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode("ascii")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", help="Path to inputs.yaml")
    ap.add_argument("--working-dir", default=None)
    args = ap.parse_args()

    inputs_path = Path(args.inputs).resolve()
    with open(inputs_path) as f:
        config = yaml.safe_load(f)

    brand = config["brand"]
    c = brand["colors"]
    cfg = config.get("config", {})
    caption = config.get("caption", {})

    working_dir = Path(args.working_dir).resolve() if args.working_dir else inputs_path.parent
    images_dir = working_dir / "images"
    slug = cfg.get("slug", "carousel")
    out_path = working_dir / "review.html"
    desktop_path = Path.home() / "Desktop" / f"{slug}-review.html"

    # Find rendered slides (numbers may be sparse if num_slides < 6)
    slide_pngs = sorted(images_dir.glob("slide-*.png"))
    if not slide_pngs:
        print(f"ERROR: no slide PNGs found in {images_dir}", file=sys.stderr)
        sys.exit(2)

    slide_nums = [int(p.stem.split("-")[1]) for p in slide_pngs]

    cards = []
    for n in slide_nums:
        img_b64 = b64(images_dir / f"slide-{n}.png")
        title, note = SLIDE_TITLES.get(n, (f"Slide {n}", ""))
        cards.append(f"""
        <article class="slide">
          <div class="slide-frame">
            <img alt="Slide {n}" src="data:image/png;base64,{img_b64}" />
          </div>
          <div class="meta">
            <div class="meta-row"><span class="num">{n:02d}</span><span class="title">{title}</span></div>
            <div class="note">{note}</div>
          </div>
        </article>""")
    cards_html = "\n".join(cards)

    body_paragraphs = ""
    if caption.get("body"):
        for para in caption["body"].strip().split("\n\n"):
            body_paragraphs += f"<p>{para.strip()}</p>\n"
    hashtags = caption.get("hashtags", "")

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{brand['name']} — Intro Carousel Review</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500;600&display=swap');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: {c['paper']}; color: {c['ink']}; font-family: 'Inter', sans-serif; }}
body {{ padding: 64px 48px 96px; max-width: 1280px; margin: 0 auto; }}
header {{ margin-bottom: 56px; padding-bottom: 32px; border-bottom: 1px solid {c['line']}; }}
.masthead {{
  display: flex; gap: 14px; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase;
  color: {c['muted']};
}}
.masthead .dot {{ color: {c['accent']}; }}
h1 {{
  font-family: 'Fraunces', Georgia, serif; font-weight: 400; font-size: 48px;
  color: {c['primary']}; text-align: center; margin: 24px 0 12px; letter-spacing: -0.01em;
}}
.lede {{
  text-align: center; font-family: 'Fraunces', serif; font-style: italic;
  font-size: 18px; color: {c['muted']}; max-width: 620px; margin: 0 auto; line-height: 1.5;
}}
.grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 48px 56px; margin-top: 48px; }}
.slide {{ display: flex; flex-direction: column; }}
.slide-frame {{
  width: 100%; aspect-ratio: 4 / 5; background: {c['cream']};
  box-shadow: 0 4px 30px rgba(22, 56, 32, 0.10), 0 1px 2px rgba(0,0,0,0.06); overflow: hidden;
}}
.slide-frame img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.meta {{ padding: 18px 4px 0; }}
.meta-row {{
  display: flex; gap: 14px; align-items: baseline;
  border-bottom: 1px solid {c['line']}; padding-bottom: 8px; margin-bottom: 10px;
}}
.num {{ font-family: 'Fraunces', serif; font-size: 32px; color: {c['accent']}; font-weight: 500; }}
.title {{ font-family: 'Fraunces', serif; font-size: 22px; color: {c['ink']}; font-weight: 500; }}
.note {{ font-size: 14px; line-height: 1.55; color: {c['ink']}; }}
.caption-block {{
  margin-top: 80px; background: {c['cream']}; padding: 36px 40px;
  border-left: 3px solid {c['accent']};
}}
.caption-block h2 {{
  font-family: 'Fraunces', serif; font-weight: 400; font-size: 22px;
  color: {c['primary']}; margin-bottom: 18px;
}}
.caption-block p {{ font-size: 15px; line-height: 1.65; color: {c['ink']}; margin-bottom: 12px; }}
.caption-block .tags {{ font-size: 13px; color: {c['muted']}; margin-top: 14px; }}
footer {{
  margin-top: 72px; padding-top: 32px; border-top: 1px solid {c['line']};
  text-align: center; font-size: 12px; color: {c['muted']}; letter-spacing: 0.08em;
}}
</style>
</head>
<body>
<header>
  <div class="masthead">
    <span>{brand['name']}</span><span class="dot">·</span>
    <span>Intro Carousel Review</span>
  </div>
  <h1>{brand['name']}</h1>
  <p class="lede">{len(slide_nums)}-slide Instagram intro carousel. Generated by health-brand-intro-carousel.</p>
</header>

<section class="grid">
{cards_html}
</section>

{f'<section class="caption-block"><h2>Suggested post caption</h2>{body_paragraphs}<p class="tags">{hashtags}</p></section>' if body_paragraphs else ''}

<footer>Generated by health-brand-intro-carousel</footer>
</body>
</html>"""

    out_path.write_text(html, encoding="utf-8")
    desktop_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_path, desktop_path)
    print(f"wrote {out_path} ({len(html)//1024} KB)")
    print(f"copied to {desktop_path}")


if __name__ == "__main__":
    main()
