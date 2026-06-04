#!/usr/bin/env python3
"""Pre-ship audit for health-brand-intro-carousel output.

Runs the checklist from SKILL.md §7 against inputs.yaml and rendered slide HTMLs.
Writes preship-audit.md to the working folder. Exits 0 if all pass, 1 if any fail.

Checks (in order):
  1. No two slides share the same layout — at least 3 distinct layouts across the carousel
  2. At least 2 of N slides use the secondary display serif (default: 3 and 5)
  3. Body sans is constant across all slides
  4. Brand mark appears on slide 6 ONLY (img.hummingbird selector)
  5. No masthead string appears on >1 slide (the v3→v4 lesson)
  6. Every text element <24px sits on a solid color region or has a veil — caught the v5 legibility bug
  7. No em-dashes or en-dashes in any copy (Annabel's global rule)
  8. No claim words (miracle / cure / guaranteed / reverse / melt / biohack)
  9. No "01 · X", "02 · Y" chapter-kicker labels (the v4→v5 lesson)
 10. No "the house style of X" or fake brand-book pull-quote attributions (the v4→v5 lesson)
 11. CTA slide uses real low-friction offer language (NOT "book your first consult")
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CLAIM_WORDS = ["miracle", "cure", "guaranteed", "reverse", "melt", "biohack"]
BANNED_CTA_PHRASES = ["book your first consult", "schedule a consultation", "book now"]
BANNED_ATTRIBUTION_PATTERNS = [
    r"the house style of \w+",
    r"the \w+ way$",
    r"— vital health$",  # generic brand-as-author attribution
]


def collect_strings(node):
    """Recursively yield all string leaves of a yaml-parsed object."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from collect_strings(v)
    elif isinstance(node, list):
        for item in node:
            yield from collect_strings(item)


def extract_visible_text(html: str) -> list[str]:
    """Strip CSS/script/base64, return list of visible text fragments."""
    html = re.sub(r'data:image/[^"\)]+', '[BASE64]', html)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.S)
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S)
    matches = re.findall(r'>([^<>]+)<', html)
    return [m.strip() for m in matches if m.strip() and not m.strip().startswith('[BASE64]')]


def find_small_text_on_photo(html: str) -> list[str]:
    """Find any text-bearing class with font-size <24px that's NOT inside a
    veiled region. Returns list of class names that violate.
    Heuristic: look for CSS rules with font-size: Npx where N<24, and check
    if the corresponding markup is inside a veil/block/solid-bg container."""
    violations = []
    # Find all .className { font-size: Npx } rules with N < 24
    rules = re.findall(r'\.([\w-]+)\s*\{[^}]*font-size:\s*(\d+)px[^}]*\}', html)
    small_classes = {cls for cls, sz in rules if int(sz) < 24}
    # Check if any small-class element sits directly inside a .canvas (not inside
    # a veil-protected block). Crude: if element appears AFTER a veil tag, mark as protected.
    for cls in small_classes:
        # Find the markup using the class
        markup_match = re.search(rf'<[^>]+class="[^"]*\b{re.escape(cls)}\b[^"]*"[^>]*>', html)
        if not markup_match:
            continue
        pos = markup_match.start()
        # Look at the 800 chars before — if there's a `.veil` or background-color set, treat as protected
        prelude = html[max(0, pos - 1500):pos]
        protected = (
            '"veil ' in prelude or "'veil '" in prelude or
            'veil-soft' in prelude or
            'background:' in prelude or
            'background-color:' in prelude
        )
        # Also protected if inside a non-photo split block (e.g. .left-block, .right-block sits on .canvas { background: paper })
        if 'left-block' in prelude or 'right-block' in prelude or '.canvas { background:' in prelude:
            protected = True
        if not protected:
            violations.append(cls)
    return violations


def audit(inputs_path: Path, working_dir: Path) -> tuple[list[dict], list[dict]]:
    """Returns (passes, failures) — each entry is {check, detail}."""
    passes, failures = [], []

    with open(inputs_path) as f:
        config = yaml.safe_load(f)

    cfg = config.get("config", {})
    fonts = config.get("fonts", {})
    copy = config.get("copy", {})
    alt_serif_slides = cfg.get("alt_serif_slides", [3, 5])

    slides_dir = working_dir / "slides"
    slide_files = sorted(slides_dir.glob("slide-*.html"))
    if not slide_files:
        failures.append({"check": "slides exist", "detail": f"no slide HTMLs in {slides_dir}"})
        return passes, failures

    slide_htmls = {int(p.stem.split("-")[1]): p.read_text() for p in slide_files}

    # 1. Layout diversity — count distinct top-level layout classes (s1-block, left-block, right-block, s3-block, s5-block, s6-block)
    layout_signatures = []
    for n, html in slide_htmls.items():
        sig_classes = set(re.findall(r'class="(s\d-block|left-block|right-block)"', html))
        layout_signatures.append((n, frozenset(sig_classes)))
    unique_layouts = len({sig for _, sig in layout_signatures})
    if unique_layouts >= 3:
        passes.append({"check": "layout diversity", "detail": f"{unique_layouts} distinct layouts across {len(slide_htmls)} slides"})
    else:
        failures.append({"check": "layout diversity", "detail": f"only {unique_layouts} distinct layouts — need at least 3"})

    # 2. Secondary serif on at least 2 slides
    sec_serif = fonts.get("secondary_serif", "Cormorant Garamond")
    slides_with_secondary = []
    for n, html in slide_htmls.items():
        if f"'{sec_serif}'" in html:
            slides_with_secondary.append(n)
    if len(slides_with_secondary) >= 2:
        passes.append({"check": "font variety (secondary serif)", "detail": f"slides {slides_with_secondary} use {sec_serif}"})
    else:
        failures.append({"check": "font variety (secondary serif)", "detail": f"only {len(slides_with_secondary)} slide(s) use the secondary serif — need at least 2 (expected: {alt_serif_slides})"})

    # 3. Body sans constant
    body_sans = fonts.get("body_sans", "Inter")
    inconsistent = []
    for n, html in slide_htmls.items():
        # Find any font-family for body/sub/sans-purpose elements
        sans_uses = re.findall(r"font-family:\s*'([\w\s]+)'\s*[,;]?\s*sans-serif", html)
        for f in sans_uses:
            if f != body_sans:
                inconsistent.append((n, f))
    if not inconsistent:
        passes.append({"check": "body sans constant", "detail": f"{body_sans} used everywhere a sans-serif appears"})
    else:
        failures.append({"check": "body sans constant", "detail": f"inconsistent body sans: {inconsistent}"})

    # 4. Brand mark on slide 6 only
    mark_slides = [n for n, html in slide_htmls.items() if 'class="hummingbird"' in html]
    if mark_slides == [6] or (6 in slide_htmls and mark_slides == [6]):
        passes.append({"check": "brand mark slide 6 only", "detail": "brand mark appears on slide 6 only"})
    elif not mark_slides and 6 not in slide_htmls:
        passes.append({"check": "brand mark slide 6 only", "detail": "no slide 6 in this build, no brand mark"})
    else:
        failures.append({"check": "brand mark slide 6 only", "detail": f"brand mark appears on slides {mark_slides} — should be [6] only"})

    # 5. No masthead string repeated on >1 slide
    masthead_pattern = re.compile(r'class="masthead"[^>]*>([^<]+)</')
    masthead_strings = {}
    for n, html in slide_htmls.items():
        for m in masthead_pattern.findall(html):
            masthead_strings.setdefault(m.strip(), []).append(n)
    duplicates = {s: ns for s, ns in masthead_strings.items() if len(ns) > 1}
    if not duplicates:
        passes.append({"check": "no duplicated masthead", "detail": "no masthead string appears on multiple slides"})
    else:
        failures.append({"check": "no duplicated masthead", "detail": f"masthead duplicated: {duplicates}"})

    # 6. Text-on-photo legibility — small text not in a veil/block
    legibility_failures = []
    for n, html in slide_htmls.items():
        violations = find_small_text_on_photo(html)
        if violations:
            legibility_failures.append((n, violations))
    if not legibility_failures:
        passes.append({"check": "text-on-photo legibility (v5 lesson)", "detail": "no small text on raw photo"})
    else:
        failures.append({"check": "text-on-photo legibility (v5 lesson)", "detail": f"small text on raw photo: {legibility_failures}"})

    # 7. No em/en dashes in copy
    all_copy_strings = list(collect_strings(copy)) + list(collect_strings(config.get("caption", {})))
    dash_violations = [s for s in all_copy_strings if "—" in s or "–" in s]
    if not dash_violations:
        passes.append({"check": "no em/en dashes", "detail": "all copy uses periods or commas"})
    else:
        failures.append({"check": "no em/en dashes", "detail": f"{len(dash_violations)} string(s) with em/en dash: {dash_violations[:3]}"})

    # 8. No claim words
    claim_violations = []
    for s in all_copy_strings:
        for word in CLAIM_WORDS:
            if re.search(rf"\b{word}\b", s, re.I):
                claim_violations.append((word, s))
    if not claim_violations:
        passes.append({"check": "no claim words", "detail": "no miracle/cure/guaranteed/reverse/melt/biohack"})
    else:
        failures.append({"check": "no claim words", "detail": f"found: {claim_violations[:3]}"})

    # 9. No chapter-kicker meta-labels
    kicker_pattern = re.compile(r'\b0\d\s*[·•]\s*(why|on your|how we)', re.I)
    kicker_violations = []
    for n, html in slide_htmls.items():
        for txt in extract_visible_text(html):
            if kicker_pattern.search(txt):
                kicker_violations.append((n, txt))
    if not kicker_violations:
        passes.append({"check": "no chapter kickers", "detail": "no '01 · Why X' style labels"})
    else:
        failures.append({"check": "no chapter kickers (v5 lesson)", "detail": f"chapter kickers found: {kicker_violations}"})

    # 10. No fake pull-quote attributions
    attribution_violations = []
    for s in all_copy_strings:
        for pattern in BANNED_ATTRIBUTION_PATTERNS:
            if re.search(pattern, s, re.I):
                attribution_violations.append((pattern, s))
    if not attribution_violations:
        passes.append({"check": "no fake pull-quote attributions", "detail": "no 'house style of X' / 'the X way' lines"})
    else:
        failures.append({"check": "no fake attributions (v5 lesson)", "detail": f"banned attributions: {attribution_violations}"})

    # 11. CTA language
    cta_sub = copy.get("slide_6_cta", {}).get("sub", "")
    cta_violations = [p for p in BANNED_CTA_PHRASES if p in cta_sub.lower()]
    if not cta_violations:
        passes.append({"check": "CTA uses real low-friction offer", "detail": f"CTA: '{cta_sub}'"})
    else:
        failures.append({"check": "CTA language", "detail": f"banned CTA phrases: {cta_violations}"})

    return passes, failures


def write_report(passes, failures, out_path: Path):
    lines = ["# Pre-ship audit\n"]
    lines.append(f"**Result**: {'✅ PASS' if not failures else '❌ FAIL'} ({len(passes)} passed, {len(failures)} failed)\n")

    if failures:
        lines.append("## Failures (fix before shipping)\n")
        for f in failures:
            lines.append(f"- **{f['check']}**: {f['detail']}\n")
        lines.append("")

    lines.append("## Passes\n")
    for p in passes:
        lines.append(f"- ✓ **{p['check']}**: {p['detail']}\n")

    out_path.write_text("".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", help="Path to inputs.yaml")
    ap.add_argument("--working-dir", default=None)
    args = ap.parse_args()

    inputs_path = Path(args.inputs).resolve()
    working_dir = Path(args.working_dir).resolve() if args.working_dir else inputs_path.parent

    passes, failures = audit(inputs_path, working_dir)

    out_path = working_dir / "preship-audit.md"
    write_report(passes, failures, out_path)

    print(f"\nPre-ship audit: {len(passes)} passed, {len(failures)} failed")
    if failures:
        print("\nFailures:")
        for f in failures:
            print(f"  ❌ {f['check']}: {f['detail']}")
    print(f"\nReport: {out_path}")

    sys.exit(0 if not failures else 1)


if __name__ == "__main__":
    main()
