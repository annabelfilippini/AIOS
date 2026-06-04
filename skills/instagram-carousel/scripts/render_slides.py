#!/usr/bin/env python3
"""Render N instagram-carousel slides to 1080x1350 PNGs using Playwright.

Role-based renderer. inputs.yaml declares an ordered list of slides; each slide
names a role (hero, why, first_visit, diagnostics, pull_quote, cta, ...). Each
role has a render function in ROLE_RENDERERS. New role types are added by
writing a render function + registering it.

Two input schemas supported:

  NEW (preferred):
    slides:
      - role: hero
        copy: {line_1: "...", line_2_em: "...", line_3: "..."}
        photo: s1-hero.png        # optional; defaults to s{N}-{role}.png
      - role: why
        copy: {pre: "...", display: "...", sub: "..."}

  LEGACY (v5 brand-intro arc, auto-translated):
    copy:
      slide_1_hero: {...}
      slide_2_why: {...}
      ...
    config:
      num_slides: 6               # drop priority 4 → 5 → 3 if < 6

Usage:
    python render_slides.py /path/to/inputs.yaml [--working-dir /path/to/project]

Expects raw photos at <working-dir>/raw/<photo-filename>.png and writes:
  - <working-dir>/slides/slide-N.html
  - <working-dir>/images/slide-N.png
"""
from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path
from typing import Any, Callable

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CANVAS_W = 1080
CANVAS_H = 1350

# Legacy brand-intro arc — used by the schema shim to translate v5-style
# inputs.yaml (top-level copy.slide_N_* keys) into the role-based slides list.
# Drop priority for num_slides<6: 4 → 5 → 3. Slides 1, 2, 6 are non-negotiable.
LEGACY_INTRO_ARC = [
    ("hero",        "slide_1_hero",        "s1-hero.png"),
    ("why",         "slide_2_why",         "s2-philosophy.png"),
    ("first_visit", "slide_3_first_visit", "s3-first-visit.png"),
    ("diagnostics", "slide_4_diagnostics", "s4-diagnostics.png"),
    ("pull_quote",  "slide_5_pull_quote",  "s5-plan.png"),
    ("cta",         "slide_6_cta",         "s6-signoff.png"),
]
LEGACY_DROP_PRIORITY = ["diagnostics", "pull_quote", "first_visit"]


def img_data_uri(path: Path) -> str:
    b = base64.b64encode(path.read_bytes()).decode("ascii")
    suffix = path.suffix.lstrip(".").lower()
    mime = "image/png" if suffix == "png" else f"image/{suffix}"
    return f"data:{mime};base64,{b}"


def pagination(active: int, total: int) -> str:
    dots = []
    for i in range(1, total + 1):
        cls = "dot active" if i == active else "dot"
        dots.append(f'<span class="{cls}"></span>')
    return f'<div class="pagination">{"".join(dots)}</div>'


def base_styles(brand: dict[str, Any], fonts: dict[str, str]) -> str:
    c = brand["colors"]
    primary_serif = fonts.get("primary_serif", "Fraunces")
    secondary_serif = fonts.get("secondary_serif", "Cormorant Garamond")
    body_sans = fonts.get("body_sans", "Inter")
    font_import_parts = []
    if primary_serif == "Fraunces":
        font_import_parts.append("family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700")
    if secondary_serif == "Cormorant Garamond":
        font_import_parts.append("family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600")
    if body_sans == "Inter":
        font_import_parts.append("family=Inter:wght@300;400;500;600")
    font_import = "https://fonts.googleapis.com/css2?" + "&".join(font_import_parts) + "&display=swap"

    return f"""
    @import url('{font_import}');
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{ width: {CANVAS_W}px; height: {CANVAS_H}px; overflow: hidden; }}
    body {{
      font-family: '{body_sans}', sans-serif;
      color: {c['ink']};
      background: {c['cream']};
      position: relative;
    }}
    .canvas {{
      width: {CANVAS_W}px;
      height: {CANVAS_H}px;
      position: relative;
      overflow: hidden;
    }}
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
      background: {c['accent']};
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
    .veil {{ position: absolute; inset: 0; z-index: 2; }}
    .veil-soft-dark {{
      background: linear-gradient(180deg, rgba(22,56,32,0.32) 0%, rgba(22,56,32,0.12) 35%, rgba(22,56,32,0.42) 100%);
    }}
    .veil-soft-bottom {{
      background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(22,56,32,0.55) 100%);
    }}
    .h-display {{
      font-family: '{primary_serif}', Georgia, serif;
      font-weight: 400;
      font-style: normal;
      font-optical-sizing: auto;
      line-height: 1.06;
      letter-spacing: -0.01em;
    }}
    .hummingbird {{
      position: absolute;
      bottom: 78px;
      left: 0; right: 0;
      display: flex;
      justify-content: center;
      z-index: 4;
    }}
    .hummingbird img {{ width: 36px; height: auto; opacity: 0.9; }}
    """


def serif_for_slide(slide_n: int, fonts: dict[str, str], alt_slides: list[int]) -> str:
    """Returns primary or secondary serif font name based on alt_serif_slides config."""
    if slide_n in alt_slides:
        return fonts.get("secondary_serif", "Cormorant Garamond")
    return fonts.get("primary_serif", "Fraunces")


# ---------- role renderers ----------
# Uniform signature: (brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str
# `s` is the slide's own copy dict (NOT copy["slide_N_..."] — the legacy shim flattens that).
# `opts` is a dict for per-role extras (e.g. logo_uri for cta).

def render_hero(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    body_sans = fonts.get("body_sans", "Inter")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .s1-block {{
      position: absolute;
      bottom: 140px;
      left: 72px;
      right: 72px;
      z-index: 3;
    }}
    .s1-rule-h {{ width: 48px; height: 2px; background: {c['accent']}; margin-bottom: 28px; }}
    .s1-headline {{
      font-family: '{serif}', Georgia, serif;
      color: {c['cream']};
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
          <span>{s['line_1']}</span>
          <span><em>{s['line_2_em']}</em></span>
          <span>{s['line_3']}</span>
        </h1>
      </div>
      {pagination(position, total_slides)}
    </div></body></html>"""


def render_why(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    body_sans = fonts.get("body_sans", "Inter")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .canvas {{ background: {c['paper']}; }}
    .right-photo {{ position: absolute; top: 0; right: 0; width: 46%; height: 100%; object-fit: cover; z-index: 1; }}
    .left-block {{
      position: absolute; top: 0; left: 0;
      width: 54%; height: 100%;
      display: flex; flex-direction: column; justify-content: center;
      padding: 110px 72px 110px 88px; z-index: 3;
    }}
    .s2-pre {{
      font-family: '{serif}', serif;
      font-size: 24px; font-weight: 400; color: {c['ink']};
      max-width: 360px; line-height: 1.3; margin-bottom: 10px;
    }}
    .s2-display {{
      font-family: '{serif}', serif;
      font-style: italic; font-weight: 400; font-size: 110px;
      color: {c['primary']}; line-height: 0.92; letter-spacing: -0.02em;
    }}
    .s2-rule {{ width: 60px; height: 1px; background: {c['accent']}; margin: 36px 0 24px; }}
    .s2-sub {{ font-family: '{body_sans}'; font-size: 16px; line-height: 1.6; color: {c['muted']}; max-width: 360px; }}
    </style></head><body>
    <div class="canvas">
      <img class="right-photo" src="{bg_uri}" />
      <div class="left-block">
        <div class="s2-pre">{s['pre']}</div>
        <div class="s2-display">{s['display']}</div>
        <div class="s2-rule"></div>
        <p class="s2-sub">{s['sub']}</p>
      </div>
      {pagination(position, total_slides)}
    </div></body></html>"""


def render_first_visit(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    fallback = fonts.get("primary_serif", "Fraunces")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .s3-block {{ position: absolute; top: 180px; left: 88px; right: 88px; z-index: 3; }}
    .s3-display {{
      font-family: '{serif}', '{fallback}', serif;
      font-style: italic; font-weight: 500; font-size: 220px;
      color: {c['deep']}; line-height: 0.9; letter-spacing: -0.03em;
    }}
    .s3-after {{
      font-family: '{serif}', '{fallback}', serif;
      font-style: italic; font-weight: 400; font-size: 34px;
      color: {c['ink']}; margin-top: 16px; max-width: 460px; line-height: 1.22;
    }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="s3-block">
        <div class="s3-display">{s['display']}</div>
        <div class="s3-after">{s['after']}</div>
      </div>
      {pagination(position, total_slides)}
    </div></body></html>"""


def render_diagnostics(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    body_sans = fonts.get("body_sans", "Inter")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .canvas {{ background: {c['cream']}; }}
    .left-photo {{ position: absolute; top: 0; left: 0; width: 50%; height: 100%; object-fit: cover; z-index: 1; }}
    .right-block {{
      position: absolute; top: 0; right: 0;
      width: 50%; height: 100%;
      display: flex; flex-direction: column; justify-content: center;
      padding: 110px 88px 110px 64px; z-index: 3;
    }}
    .s4-pre {{ font-family: '{serif}', serif; font-size: 22px; color: {c['ink']}; margin-bottom: 6px; line-height: 1.3; }}
    .s4-display {{
      font-family: '{serif}', serif;
      font-style: italic; font-weight: 400; font-size: 116px;
      color: {c['primary']}; line-height: 0.92; letter-spacing: -0.02em;
    }}
    .s4-coda {{ font-family: '{serif}', serif; font-size: 26px; color: {c['ink']}; margin-top: 18px; line-height: 1.2; }}
    .s4-rule {{ width: 60px; height: 1px; background: {c['accent']}; margin: 32px 0 22px; }}
    .s4-sub {{ font-family: '{body_sans}'; font-size: 16px; line-height: 1.6; color: {c['muted']}; max-width: 360px; }}
    </style></head><body>
    <div class="canvas">
      <img class="left-photo" src="{bg_uri}" />
      <div class="right-block">
        <div class="s4-pre">{s['pre']}</div>
        <div class="s4-display">{s['display']}</div>
        <div class="s4-coda">{s['coda']}</div>
        <div class="s4-rule"></div>
        <p class="s4-sub">{s['sub']}</p>
      </div>
      {pagination(position, total_slides)}
    </div></body></html>"""


def render_pull_quote(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    fallback = fonts.get("primary_serif", "Fraunces")
    body_sans = fonts.get("body_sans", "Inter")
    attribution_html = ""
    if s.get("attribution_to_founder") and brand.get("founder_name"):
        attribution_html = f"""
        <div class="s5-attribution">
          <span class="rule"></span>
          <span class="text">{brand['founder_name']}</span>
        </div>"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .s5-block {{ position: absolute; top: 230px; left: 96px; right: 96px; z-index: 3; }}
    .s5-mark {{
      font-family: '{serif}', '{fallback}', serif;
      font-style: italic; font-weight: 500; font-size: 110px;
      color: {c['accent']}; line-height: 0.5; margin-bottom: 18px; letter-spacing: -0.03em;
    }}
    .s5-quote {{
      font-family: '{serif}', '{fallback}', serif;
      font-style: italic; font-weight: 500; font-size: 62px;
      color: {c['deep']}; line-height: 1.14; letter-spacing: -0.012em; max-width: 760px;
    }}
    .s5-quote .accent-word {{ color: {c['primary']}; }}
    .s5-attribution {{ margin-top: 36px; display: flex; align-items: center; gap: 16px; }}
    .s5-attribution .rule {{ width: 36px; height: 1px; background: {c['accent']}; }}
    .s5-attribution .text {{
      font-family: '{body_sans}'; font-size: 11px; color: {c['ink']};
      letter-spacing: 0.28em; text-transform: uppercase; font-weight: 500;
    }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="s5-block">
        <div class="s5-mark">&ldquo;</div>
        <div class="s5-quote">{s['quote_pre']} <span class="accent-word">{s['quote_accent']}</span> {s['quote_post']}</div>{attribution_html}
      </div>
      {pagination(position, total_slides)}
    </div></body></html>"""


def render_cta(brand, fonts, s, bg_uri, position, total_slides, alt_slides, opts) -> str:
    c = brand["colors"]
    serif = serif_for_slide(position, fonts, alt_slides)
    body_sans = fonts.get("body_sans", "Inter")
    logo_uri = opts.get("logo_uri", "")
    url = brand.get("cta_url", "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{base_styles(brand, fonts)}
    .s6-salute {{
      position: absolute; top: 88px; left: 0; right: 0; z-index: 5; text-align: center;
      font-family: '{serif}', serif; font-style: italic; font-weight: 300; font-size: 26px;
      color: {c['cream']}; letter-spacing: -0.005em;
    }}
    .s6-block {{ position: absolute; top: 200px; left: 88px; right: 88px; z-index: 3; text-align: center; }}
    .s6-pre {{
      font-family: '{body_sans}'; font-size: 11px; letter-spacing: 0.32em;
      text-transform: uppercase; color: {c['cream']}; opacity: 0.85; margin-bottom: 24px;
    }}
    .s6-pre::before, .s6-pre::after {{
      content: '·'; color: {c['accent']}; margin: 0 14px;
    }}
    .s6-display {{
      font-family: '{serif}', serif; font-style: italic; font-weight: 400; font-size: 132px;
      color: {c['cream']}; line-height: 0.92; letter-spacing: -0.025em;
    }}
    .s6-after {{
      font-family: '{serif}', serif; font-weight: 400; font-size: 32px;
      color: {c['cream']}; margin-top: 20px; line-height: 1.15;
    }}
    .s6-rule {{ width: 60px; height: 1px; background: {c['accent']}; margin: 32px auto 24px; }}
    .s6-url {{
      font-family: '{body_sans}'; font-size: 14px; font-weight: 500; color: {c['cream']};
      letter-spacing: 0.16em; text-transform: uppercase;
    }}
    .hummingbird {{ bottom: 100px; }}
    </style></head><body>
    <div class="canvas">
      <img class="photo-bg" src="{bg_uri}" />
      <div class="veil veil-soft-dark"></div>
      <div class="s6-salute">{s['salutation']}</div>
      <div class="s6-block">
        <div class="s6-pre">{s['pre']}</div>
        <div class="s6-display">{s['display']}</div>
        <div class="s6-after">{s['sub']}</div>
        <div class="s6-rule"></div>
        <div class="s6-url">{url}</div>
      </div>
      <div class="hummingbird"><img src="{logo_uri}" /></div>
      {pagination(position, total_slides)}
    </div></body></html>"""


# Role registry. Add new role types here as they ship.
ROLE_RENDERERS: dict[str, Callable] = {
    "hero":         render_hero,
    "why":          render_why,
    "first_visit":  render_first_visit,
    "diagnostics":  render_diagnostics,
    "pull_quote":   render_pull_quote,
    "cta":          render_cta,
}


def normalize_config(config: dict) -> dict:
    """Translate legacy v5 schema (top-level copy.slide_N_*) into the new slides[] list.

    Idempotent. If config already has a 'slides' list, returns it unchanged.
    """
    if "slides" in config and config["slides"]:
        return config

    legacy_copy = config.get("copy", {})
    if not any(k.startswith("slide_") for k in legacy_copy):
        # No legacy keys either — caller error
        print("ERROR: inputs.yaml has neither 'slides:' list nor legacy 'copy.slide_N_*' keys", file=sys.stderr)
        sys.exit(2)

    cfg = config.get("config", {})
    num_slides = cfg.get("num_slides", 6)

    # Decide which legacy roles to keep based on drop priority
    kept_roles = [r[0] for r in LEGACY_INTRO_ARC]
    if num_slides < 6:
        to_drop = LEGACY_DROP_PRIORITY[: 6 - num_slides]
        kept_roles = [r for r in kept_roles if r not in to_drop]

    slides = []
    for role, copy_key, default_photo in LEGACY_INTRO_ARC:
        if role not in kept_roles:
            continue
        if copy_key not in legacy_copy:
            print(f"ERROR: legacy schema missing copy.{copy_key}", file=sys.stderr)
            sys.exit(2)
        slides.append({
            "role": role,
            "copy": legacy_copy[copy_key],
            "photo": default_photo,
        })

    config["slides"] = slides
    return config


def resolve_photo_path(slide_spec: dict, position: int, raw_dir: Path) -> Path | None:
    """Find the raw photo for a slide. Order: explicit photo: field, s{N}-{role}.png, s{N}-*.png glob."""
    if slide_spec.get("photo"):
        candidate = raw_dir / slide_spec["photo"]
        if candidate.exists():
            return candidate
    role_default = raw_dir / f"s{position}-{slide_spec['role']}.png"
    if role_default.exists():
        return role_default
    matches = list(raw_dir.glob(f"s{position}-*.png"))
    if matches:
        return matches[0]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", help="Path to inputs.yaml")
    ap.add_argument("--working-dir", default=None, help="Project working folder (defaults to inputs.yaml's parent)")
    args = ap.parse_args()

    inputs_path = Path(args.inputs).resolve()
    if not inputs_path.exists():
        print(f"ERROR: inputs file not found: {inputs_path}", file=sys.stderr)
        sys.exit(2)

    with open(inputs_path) as f:
        config = yaml.safe_load(f)

    config = normalize_config(config)

    brand = config["brand"]
    fonts = config.get("fonts", {})
    slides = config["slides"]
    cfg = config.get("config", {})
    alt_serif_slides = cfg.get("alt_serif_slides", [3, 5])

    total_slides = len(slides)

    working_dir = Path(args.working_dir).resolve() if args.working_dir else inputs_path.parent
    slides_dir = working_dir / "slides"
    images_dir = working_dir / "images"
    raw_dir = working_dir / "raw"
    slides_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    # Resolve mark_path (brand mark for cta slide)
    mark_path_str = brand.get("mark_path", "")
    if mark_path_str:
        mark_path = (working_dir / mark_path_str).resolve() if not Path(mark_path_str).is_absolute() else Path(mark_path_str)
    else:
        mark_path = None

    # Validate roles + resolve photos
    raw_files = {}
    for idx, slide_spec in enumerate(slides, start=1):
        role = slide_spec.get("role")
        if role not in ROLE_RENDERERS:
            print(f"ERROR: slide {idx}: unknown role '{role}'. Known: {sorted(ROLE_RENDERERS)}", file=sys.stderr)
            sys.exit(2)
        photo = resolve_photo_path(slide_spec, idx, raw_dir)
        if photo is None:
            print(f"ERROR: slide {idx} ({role}): no raw photo found at {raw_dir}/s{idx}-*.png", file=sys.stderr)
            print("       Run scripts/generate_photos.py first.", file=sys.stderr)
            sys.exit(2)
        raw_files[idx] = photo

    bg_uris = {idx: img_data_uri(p) for idx, p in raw_files.items()}
    logo_uri = img_data_uri(mark_path) if mark_path and mark_path.exists() else ""

    # Render
    htmls = {}
    for idx, slide_spec in enumerate(slides, start=1):
        role = slide_spec["role"]
        renderer = ROLE_RENDERERS[role]
        opts = {"logo_uri": logo_uri}
        htmls[idx] = renderer(
            brand, fonts, slide_spec["copy"], bg_uris[idx],
            idx, total_slides, alt_serif_slides, opts,
        )

    for n, html in htmls.items():
        out = slides_dir / f"slide-{n}.html"
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {out.name} ({len(html)//1024} KB)")

    # Render to PNG via Playwright
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": CANVAS_W, "height": CANVAS_H}, device_scale_factor=1)
        for n in htmls:
            page = context.new_page()
            page.set_viewport_size({"width": CANVAS_W, "height": CANVAS_H})
            page.goto((slides_dir / f"slide-{n}.html").as_uri())
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(800)
            out_png = images_dir / f"slide-{n}.png"
            page.screenshot(path=str(out_png), full_page=False, omit_background=False,
                            clip={"x": 0, "y": 0, "width": CANVAS_W, "height": CANVAS_H})
            page.close()
            print(f"  rendered {out_png.name}")
        browser.close()

    print(f"\nDone. {len(htmls)} slides written to {images_dir}/")


if __name__ == "__main__":
    main()
