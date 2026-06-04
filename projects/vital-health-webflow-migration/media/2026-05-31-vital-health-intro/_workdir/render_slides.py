#!/usr/bin/env python3
"""Render 6 Vital Health intro-carousel slides to 1080x1350 PNGs using Playwright.

Reads slide HTMLs from slides/ and outputs to images/. The slide HTMLs are
self-contained (CSS inline, image embedded as base64 file:// reference) so
Chromium renders each at exact 1080x1350.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "slides"
IMAGES_DIR = ROOT / "images"
RAW_DIR = ROOT / "raw"
# Project root = ROOT.parent.parent (ROOT is media/<dated-folder>/)
PROJECT_ROOT = ROOT.parent.parent
LOGO_PATH = PROJECT_ROOT / "logo-options" / "bird-filled-deep-forest.png"

CANVAS_W = 1080
CANVAS_H = 1350

COLORS = {
    "cream": "#F5EFE0",
    "paper": "#FBF7EC",
    "primary": "#1F4D2A",
    "deep_forest": "#163820",
    "accent": "#C9A04A",
    "ink": "#2A2A26",
    "muted": "#7A776B",
    "line": "#DED3B8",
}

MASTHEAD = '<span>AUSTIN, TEXAS</span><span class="dot">·</span><span>INTEGRATIVE MEDICINE</span><span class="dot">·</span><span>EST. 2010</span>'


def img_data_uri(path: Path) -> str:
    b = base64.b64encode(path.read_bytes()).decode("ascii")
    suffix = path.suffix.lstrip(".").lower()
    mime = "image/png" if suffix == "png" else f"image/{suffix}"
    return f"data:{mime};base64,{b}"


def pagination(active: int, total: int = 6) -> str:
    dots = []
    for i in range(1, total + 1):
        cls = "dot active" if i == active else "dot"
        dots.append(f'<span class="{cls}"></span>')
    return f'<div class="pagination">{"".join(dots)}</div>'


def base_styles() -> str:
    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=Inter:wght@300;400;500;600&display=swap');
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{ width: {CANVAS_W}px; height: {CANVAS_H}px; overflow: hidden; }}
    body {{
      font-family: 'Inter', sans-serif;
      color: {COLORS['ink']};
      background: {COLORS['cream']};
      position: relative;
    }}
    .canvas {{
      width: {CANVAS_W}px;
      height: {CANVAS_H}px;
      position: relative;
      overflow: hidden;
    }}
    .masthead {{
      position: absolute;
      top: 32px;
      left: 0; right: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 14px;
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      z-index: 5;
    }}
    .masthead .dot {{ color: {COLORS['accent']}; }}
    .pagination {{
      position: absolute;
      bottom: 32px;
      left: 0; right: 0;
      display: flex;
      justify-content: center;
      gap: 8px;
      z-index: 5;
    }}
    .pagination .dot {{
      width: 6px; height: 6px;
      border-radius: 50%;
      background: rgba(0,0,0,0.18);
    }}
    .pagination .dot.active {{
      background: {COLORS['accent']};
      width: 18px;
      border-radius: 3px;
    }}
    .photo-bg {{
      position: absolute;
      inset: 0;
      width: 100%; height: 100%;
      object-fit: cover;
      z-index: 1;
    }}
    .veil {{
      position: absolute;
      inset: 0;
      z-index: 2;
    }}
    .veil-soft-dark {{
      background: linear-gradient(180deg, rgba(22,56,32,0.32) 0%, rgba(22,56,32,0.12) 35%, rgba(22,56,32,0.42) 100%);
    }}
    .veil-soft-bottom {{
      background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(22,56,32,0.55) 100%);
    }}
    .content {{
      position: absolute;
      inset: 0;
      z-index: 3;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 96px 88px;
    }}
    .h-display {{
      font-family: 'Fraunces', Georgia, serif;
      font-weight: 400;
      font-style: normal;
      font-optical-sizing: auto;
      line-height: 1.06;
      letter-spacing: -0.01em;
    }}
    .gold-rule-v {{
      width: 1px;
      background: {COLORS['accent']};
      margin: 22px auto;
    }}
    .gold-rule-h {{
      height: 1px;
      background: {COLORS['accent']};
      margin: 18px 0;
    }}
    .small-caps {{
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.24em;
      text-transform: uppercase;
    }}
    .hummingbird {{
      position: absolute;
      bottom: 78px;
      left: 0; right: 0;
      display: flex;
      justify-content: center;
      z-index: 4;
    }}
    .hummingbird img {{
      width: 36px; height: auto; opacity: 0.9;
    }}
    /* Corner brand mark — solid white hummingbird silhouette, top-right of
       every slide. Soft drop-shadow keeps it legible on bright skies. */
    .brand-mark {{
      position: absolute;
      top: 36px;
      right: 36px;
      z-index: 6;
      width: 56px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .brand-mark img {{
      width: 56px;
      height: auto;
      filter: drop-shadow(0 0 6px rgba(245, 239, 224, 0.55))
              drop-shadow(0 1px 3px rgba(245, 239, 224, 0.45));
    }}
    """


# ---------- per-slide layouts ----------


def slide_1(bg_uri: str, logo_uri: str) -> str:
    # Bottom-left anchored headline, no masthead, no subline. "catches" italic for whimsy.
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .s1-kicker {{
      position: absolute;
      top: 56px; left: 72px;
      z-index: 5;
      color: {COLORS['cream']};
      font-family: 'Inter';
      font-size: 11px;
      letter-spacing: 0.32em;
      font-weight: 500;
      text-transform: uppercase;
      opacity: 0.85;
    }}
    .s1-kicker::before {{
      content: '';
      display: inline-block;
      width: 26px; height: 1px;
      background: {COLORS['accent']};
      vertical-align: middle;
      margin-right: 14px;
    }}
    .s1-block {{
      position: absolute;
      bottom: 140px;
      left: 72px;
      right: 72px;
      z-index: 3;
    }}
    .s1-rule-h {{
      width: 48px; height: 2px;
      background: {COLORS['accent']};
      margin-bottom: 28px;
    }}
    .s1-headline {{
      color: {COLORS['cream']};
      font-size: 72px;
      text-align: left;
      line-height: 1.02;
      letter-spacing: -0.012em;
      max-width: 880px;
    }}
    .s1-headline span {{ display: block; }}
    .s1-headline em {{ font-style: italic; font-weight: 300; }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="veil veil-soft-bottom"></div>
      <div class="s1-block">
        <div class="s1-rule-h"></div>
        <h1 class="h-display s1-headline">
          <span>Medicine that</span>
          <span><em>catches it</em></span>
          <span>before it catches you.</span>
        </h1>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(1)}
    </div></body></html>"""


def slide_2(bg_uri: str, logo_uri: str) -> str:
    # Magazine chapter feel — "01 / WHY" kicker, oversized italic "preventable."
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .canvas {{ background: {COLORS['paper']}; }}
    .right-photo {{
      position: absolute;
      top: 0; right: 0;
      width: 46%; height: 100%;
      object-fit: cover;
      z-index: 1;
    }}
    .left-block {{
      position: absolute;
      top: 0; left: 0;
      width: 54%; height: 100%;
      display: flex; flex-direction: column;
      justify-content: center;
      padding: 110px 72px 110px 88px;
      z-index: 3;
    }}
    .s2-kicker {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin-bottom: 32px;
      font-family: 'Inter';
      font-size: 11px;
      color: {COLORS['muted']};
      letter-spacing: 0.28em;
      text-transform: uppercase;
    }}
    .s2-kicker .num {{
      font-family: 'Fraunces';
      font-style: italic;
      font-size: 28px;
      font-weight: 400;
      color: {COLORS['accent']};
      letter-spacing: 0;
      text-transform: none;
      line-height: 1;
    }}
    .s2-pre {{
      font-family: 'Fraunces', serif;
      font-size: 24px;
      font-weight: 400;
      color: {COLORS['ink']};
      max-width: 360px;
      line-height: 1.3;
      margin-bottom: 10px;
    }}
    .s2-display {{
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-weight: 400;
      font-size: 110px;
      color: {COLORS['primary']};
      line-height: 0.92;
      letter-spacing: -0.02em;
    }}
    .s2-rule {{ width: 60px; height: 1px; background: {COLORS['accent']}; margin: 36px 0 24px; }}
    .s2-sub {{ font-family: 'Inter'; font-size: 16px; line-height: 1.6; color: {COLORS['muted']}; max-width: 360px; }}
    </style></head><body>
    <div class="canvas">
      <img class="right-photo" src="{bg_uri}" />
      <div class="left-block">
        <div class="s2-pre">Most emergencies are</div>
        <div class="s2-display">preventable.</div>
        <div class="s2-rule"></div>
        <p class="s2-sub">Dr. Swett spent twenty-three years in the ER watching it happen. Vital Health was the answer.</p>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(2)}
    </div></body></html>"""


def slide_3(bg_uri: str, logo_uri: str) -> str:
    # "Ninety." set as oversized italic display upper-left; smaller serif beneath.
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .s3-kicker {{
      position: absolute;
      top: 56px; right: 72px;
      z-index: 5;
      font-family: 'Inter';
      font-size: 11px;
      color: {COLORS['muted']};
      letter-spacing: 0.32em;
      font-weight: 500;
      text-transform: uppercase;
    }}
    .s3-kicker::after {{
      content: '';
      display: inline-block;
      width: 26px; height: 1px;
      background: {COLORS['accent']};
      vertical-align: middle;
      margin-left: 14px;
    }}
    .s3-block {{
      position: absolute;
      top: 180px;
      left: 88px;
      right: 88px;
      z-index: 3;
    }}
    .s3-display {{
      font-family: 'Cormorant Garamond', 'Fraunces', serif;
      font-style: italic;
      font-weight: 500;
      font-size: 220px;
      color: {COLORS['deep_forest']};
      line-height: 0.9;
      letter-spacing: -0.03em;
    }}
    .s3-after {{
      font-family: 'Cormorant Garamond', 'Fraunces', serif;
      font-style: italic;
      font-weight: 400;
      font-size: 34px;
      color: {COLORS['ink']};
      margin-top: 16px;
      max-width: 460px;
      line-height: 1.22;
    }}
    .s3-sub-block {{
      position: absolute;
      bottom: 130px;
      left: 88px;
      right: 88px;
      z-index: 3;
    }}
    .s3-rule {{ width: 44px; height: 1px; background: {COLORS['accent']}; margin-bottom: 14px; }}
    .s3-sub {{
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-weight: 300;
      font-size: 22px;
      color: {COLORS['ink']};
      max-width: 600px;
      line-height: 1.4;
    }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="s3-block">
        <div class="s3-display">Ninety.</div>
        <div class="s3-after">minutes to read your story before we write any of it.</div>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(3)}
    </div></body></html>"""


def slide_4(bg_uri: str, logo_uri: str) -> str:
    # Photo swaps to LEFT (asymmetry vs slide 2). Big italic "Weeks." then smaller "not minutes."
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .canvas {{ background: {COLORS['cream']}; }}
    .left-photo {{
      position: absolute;
      top: 0; left: 0;
      width: 50%; height: 100%;
      object-fit: cover;
      z-index: 1;
    }}
    .right-block {{
      position: absolute;
      top: 0; right: 0;
      width: 50%; height: 100%;
      display: flex; flex-direction: column;
      justify-content: center;
      padding: 110px 88px 110px 64px;
      z-index: 3;
    }}
    .s4-kicker {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin-bottom: 36px;
      font-family: 'Inter';
      font-size: 11px;
      color: {COLORS['muted']};
      letter-spacing: 0.28em;
      text-transform: uppercase;
    }}
    .s4-kicker .num {{
      font-family: 'Fraunces';
      font-style: italic;
      font-size: 28px;
      font-weight: 400;
      color: {COLORS['accent']};
      letter-spacing: 0;
      text-transform: none;
      line-height: 1;
    }}
    .s4-pre {{
      font-family: 'Fraunces', serif;
      font-size: 22px;
      color: {COLORS['ink']};
      margin-bottom: 6px;
      line-height: 1.3;
    }}
    .s4-display {{
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-weight: 400;
      font-size: 116px;
      color: {COLORS['primary']};
      line-height: 0.92;
      letter-spacing: -0.02em;
    }}
    .s4-coda {{
      font-family: 'Fraunces', serif;
      font-size: 26px;
      color: {COLORS['ink']};
      margin-top: 18px;
      line-height: 1.2;
    }}
    .s4-rule {{ width: 60px; height: 1px; background: {COLORS['accent']}; margin: 32px 0 22px; }}
    .s4-sub {{ font-family: 'Inter'; font-size: 16px; line-height: 1.6; color: {COLORS['muted']}; max-width: 360px; }}
    </style></head><body>
    <div class="canvas">
      <img class="left-photo" src="{bg_uri}" />
      <div class="right-block">
        <div class="s4-pre">Your workup takes</div>
        <div class="s4-display">weeks.</div>
        <div class="s4-coda">Not minutes.</div>
        <div class="s4-rule"></div>
        <p class="s4-sub">Comprehensive labs, four sets of eyes, one coordinated record.</p>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(4)}
    </div></body></html>"""


def slide_5(bg_uri: str, logo_uri: str) -> str:
    # Pull-quote treatment. No masthead. Big italic Fraunces with quotation marks,
    # tiny attribution beneath a gold rule. Magazine pull-quote rhythm.
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .s5-block {{
      position: absolute;
      top: 230px;
      left: 96px;
      right: 96px;
      z-index: 3;
    }}
    .s5-mark {{
      font-family: 'Cormorant Garamond', 'Fraunces', serif;
      font-style: italic;
      font-weight: 500;
      font-size: 110px;
      color: {COLORS['accent']};
      line-height: 0.5;
      margin-bottom: 18px;
      letter-spacing: -0.03em;
    }}
    .s5-quote {{
      font-family: 'Cormorant Garamond', 'Fraunces', serif;
      font-style: italic;
      font-weight: 500;
      font-size: 62px;
      color: {COLORS['deep_forest']};
      line-height: 1.14;
      letter-spacing: -0.012em;
      max-width: 760px;
    }}
    .s5-quote .accent-word {{
      color: {COLORS['primary']};
    }}
    .s5-attribution {{
      margin-top: 36px;
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .s5-attribution .rule {{
      width: 36px; height: 1px; background: {COLORS['accent']};
    }}
    .s5-attribution .text {{
      font-family: 'Inter';
      font-size: 11px;
      color: {COLORS['ink']};
      letter-spacing: 0.28em;
      text-transform: uppercase;
      font-weight: 500;
    }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="s5-block">
        <div class="s5-mark">&ldquo;</div>
        <div class="s5-quote">Care here reads more like <span class="accent-word">a relationship</span> than an appointment.</div>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(5)}
    </div></body></html>"""


def slide_6(bg_uri: str, logo_uri: str) -> str:
    # No masthead (kills slide-1 duplication pattern). Salutation up top, big CTA
    # mid-upper, URL only (no "Austin, TX" — that's redundant with the brand).
    # Hummingbird mark just above bottom edge.
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles()}
    .s6-salute {{
      position: absolute;
      top: 88px; left: 0; right: 0;
      z-index: 5;
      text-align: center;
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-weight: 300;
      font-size: 26px;
      color: {COLORS['cream']};
      letter-spacing: -0.005em;
    }}
    .s6-block {{
      position: absolute;
      top: 200px; left: 88px; right: 88px;
      z-index: 3;
      text-align: center;
    }}
    .s6-pre {{
      font-family: 'Inter';
      font-size: 11px;
      letter-spacing: 0.32em;
      text-transform: uppercase;
      color: {COLORS['cream']};
      opacity: 0.85;
      margin-bottom: 24px;
    }}
    .s6-pre::before, .s6-pre::after {{
      content: '·';
      color: {COLORS['accent']};
      margin: 0 14px;
    }}
    .s6-display {{
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-weight: 400;
      font-size: 132px;
      color: {COLORS['cream']};
      line-height: 0.92;
      letter-spacing: -0.025em;
    }}
    .s6-after {{
      font-family: 'Fraunces', serif;
      font-weight: 400;
      font-size: 32px;
      color: {COLORS['cream']};
      margin-top: 20px;
      line-height: 1.15;
    }}
    .s6-rule {{ width: 60px; height: 1px; background: {COLORS['accent']}; margin: 32px auto 24px; }}
    .s6-url {{
      font-family: 'Inter';
      font-size: 14px;
      font-weight: 500;
      color: {COLORS['cream']};
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }}
    .hummingbird {{ bottom: 100px; }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="veil veil-soft-dark"></div>
      <div class="s6-salute">Begin here.</div>
      <div class="s6-block">
        <div class="s6-pre">A first step</div>
        <div class="s6-display">Free.</div>
        <div class="s6-after">Thirty minutes. No cost. Just a fit conversation.</div>
        <div class="s6-rule"></div>
        <div class="s6-url">vitalhealthaustin.com</div>
      </div>
      <div class="brand-mark"><img src="{logo_uri}" /></div>
      {pagination(6)}
    </div></body></html>"""


def main():
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    raw_files = {
        1: RAW_DIR / "s1-hero.png",
        2: RAW_DIR / "s2-philosophy.png",
        3: RAW_DIR / "s3-first-visit.png",
        4: RAW_DIR / "s4-diagnostics.png",
        5: RAW_DIR / "s5-plan.png",
        6: RAW_DIR / "s6-signoff.png",
    }
    missing = [n for n, p in raw_files.items() if not p.exists()]
    if missing:
        print(f"ERROR: missing raw images for slides {missing}", file=sys.stderr)
        sys.exit(2)

    bg_uris = {n: img_data_uri(p) for n, p in raw_files.items()}
    logo_uri = img_data_uri(LOGO_PATH)

    htmls = {
        1: slide_1(bg_uris[1], logo_uri),
        2: slide_2(bg_uris[2], logo_uri),
        3: slide_3(bg_uris[3], logo_uri),
        4: slide_4(bg_uris[4], logo_uri),
        5: slide_5(bg_uris[5], logo_uri),
        6: slide_6(bg_uris[6], logo_uri),
    }
    for n, html in htmls.items():
        out = SLIDES_DIR / f"slide-{n}.html"
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {out.name} ({len(html)//1024} KB)")

    # Render to PNG via Playwright
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": CANVAS_W, "height": CANVAS_H}, device_scale_factor=1)
        for n in range(1, 7):
            page = context.new_page()
            page.set_viewport_size({"width": CANVAS_W, "height": CANVAS_H})
            page.goto((SLIDES_DIR / f"slide-{n}.html").as_uri())
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(800)  # let webfonts settle
            out_png = IMAGES_DIR / f"slide-{n}.png"
            page.screenshot(path=str(out_png), full_page=False, omit_background=False,
                            clip={"x": 0, "y": 0, "width": CANVAS_W, "height": CANVAS_H})
            page.close()
            print(f"  rendered {out_png.name}")
        browser.close()

    print(f"\nDone. {len(htmls)} slides written to {IMAGES_DIR}/")


if __name__ == "__main__":
    main()
