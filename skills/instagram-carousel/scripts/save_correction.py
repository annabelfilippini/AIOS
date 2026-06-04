#!/usr/bin/env python3
"""
save_correction.py — called by the listen-for-corrections.sh UserPromptSubmit hook.

Reads the hook payload (JSON) on stdin. If the user prompt matches one of the
aggressive correction patterns, appends a structured entry to the universal
style file (references/style.md) under the inferred category and emits a
one-line system-reminder on stdout (which Claude Code adds to the model context).

Layer-3 routing (writing brand-specific corrections to
<project>/media/brand_context/carousel-direction.md) is planned for Batch 2b. Current
behaviour: everything lands in style.md.

Silent (exit 0, no stdout) when nothing matches. Never blocks — exit 0 always.

Manual mode for smoke tests:
    python3 save_correction.py --text "don't use cinematic photography" --dry-run
    python3 save_correction.py --text "the font is too generic"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
PREFS = SKILL_ROOT / "references" / "style.md"

# ---------------------------------------------------------------------------
# Trigger patterns — err aggressive. Deletion is cheap, missing is forever.
# ---------------------------------------------------------------------------
# Each pattern is a compiled, case-insensitive regex. A prompt matches if ANY
# of these fire. Keep additions liberal; refine via deletions, not by adding
# negative lookaheads here.
TRIGGER_PATTERNS = [
    r"\bdon'?t (like|want|use|do|need|show)\b",
    r"\bi do not (like|want|use|do|need)\b",
    r"\b(stop|quit) (doing|using|showing)\b",
    r"\bnever (use|do|show|put|include|write)\b",
    r"\bavoid\b",
    r"\btoo (much|many|big|small|loud|busy|bright|dark|polished|generic|"
    r"formal|casual|cheesy|corporate|salesy|stiff|safe|wordy|tight|tall|wide|"
    r"long|short|hyped?|aggressive|soft|bold|thin|heavy|light)\b",
    r"\b(less|more) (polished|formal|busy|corporate|generic|cheesy|cluttered|"
    r"hyped?|warm|human|specific|concrete|real|natural|quiet|loud|soft|bold)\b",
    r"\b(change|swap|replace|fix|kill|drop|cut|remove|delete|redo) (the|that|this|out)\b",
    r"\bthat'?s (wrong|off|bad|not right|not it|too much|ugly|generic|cheesy|"
    r"salesy|weird|forced|fake|stiff|boring|flat)\b",
    r"\b(i )?hate (the|this|that|how|when)\b",
    r"\bnot (a fan|right|working|it|the vibe|quite right|loving|feeling|sure about)\b",
    r"\b(wrong|off|bad) (font|color|colour|tone|word|image|photo|crop|layout|logo|caption|copy|headline|sub|cta|spacing)\b",
    r"\bmake it (less|more|warmer|cooler|softer|tighter|simpler|smaller|larger|quieter|louder|bolder|cleaner|sharper|brighter|darker|shorter|longer)\b",
    r"\b(sounds|reads|feels) (ai|robotic|fake|generic|stiff|corporate|cheesy|salesy|forced|flat|chatgpt)\b",
    r"\bthe (font|color|colour|copy|headline|image|photo|crop|layout|logo|caption|spacing|tone|voice|cta|sub|subline|background|veil|word|line) (is|looks|feels|reads|sounds)\b",
    # softer but still useful
    r"\b(rather|prefer|would prefer|i'?d rather|i would rather) (we |to )?(have|use|see|do|show|write|swap|drop)\b",
    r"\binstead of\b",
    r"\bredo\b",
    r"\bregenerate\b",
    r"\bdrop the\b",
    r"\bkill the\b",
]
_TRIGGER_RE = re.compile("|".join(TRIGGER_PATTERNS), re.IGNORECASE)

# ---------------------------------------------------------------------------
# Category inference — keyword → existing style.md section header.
# Order matters: TEXT-ON-PHOTO LEGIBILITY before Layout, Voice before Copy.
# ---------------------------------------------------------------------------
CATEGORY_RULES = [
    ("TEXT-ON-PHOTO LEGIBILITY (highest priority — caught TWICE)", [
        r"\billegib", r"\bleg(i|a)b", r"\bunreadable", r"\bcontrast (with|on|against)",
        r"\bveil", r"\bplate", r"\btext (on|over) (the )?(photo|image|background)",
        r"\bcan'?t read", r"\bhard to read",
    ]),
    ("Typography", [
        r"\bfont", r"\bserif", r"\bitalic", r"\btype(face)?", r"\bkerning",
        r"\bweight", r"\bfraunces", r"\bcormorant", r"\binter\b",
        r"\bdisplay (type|face|font)", r"\bbody (sans|serif|type|font)",
        r"\bdash(es)?\b", r"\bhyphen", r"\bpunctuation",
    ]),
    ("Photography", [
        r"\bphoto", r"\bimage", r"\blight(ing)?", r"\bcolor( palette|s)?\b",
        r"\bcolour", r"\bpalette", r"\bcrop", r"\bframe", r"\bshot",
        r"\bcomposition", r"\bbackground", r"\bforeground", r"\bsubject",
        r"\bgender", r"\bage\b", r"\bperson", r"\bface", r"\bhand",
        r"\bbotanical", r"\bstill[- ]life", r"\bcinematic", r"\bdocumentary",
        r"\beditorial", r"\bstock\b", r"\bgeneric (image|photo)",
        r"\bbrand( ?ed)? photo", r"\bgpt-image", r"\bmidjourney",
    ]),
    ("Layout / Composition", [
        r"\blayout", r"\balignment", r"\bplace(ment)?\b", r"\bslide \d",
        r"\bhierarchy", r"\bbalance", r"\bwhitespace", r"\bwhite[- ]space",
        r"\bmargin", r"\bpadding", r"\bgrid", r"\bsplit", r"\bfull[- ]bleed",
        r"\bcenter(ed)?", r"\bleft|\bright", r"\btop|\bbottom",
        r"\bposition", r"\barrangement",
    ]),
    ("Voice", [
        r"\bvoice", r"\btone", r"\bsound", r"\breads (like|as)",
        r"\bhype", r"\bsalesy", r"\bcorporate", r"\bcheesy", r"\bgeneric",
        r"\bplain", r"\bquiet", r"\bconfident", r"\bdirect",
        r"\bmarketing[- ]speak", r"\bbuzz(word)?", r"\bfeels ai",
    ]),
    ("Copy", [
        r"\bcopy\b", r"\bword(s|ing)?\b", r"\bheadline", r"\bsub(line|head)",
        r"\bcaption", r"\bsentence", r"\bclaim", r"\bcta\b", r"\bcall to action",
        r"\bhashtag", r"\bquote", r"\bemoji", r"\bphrase", r"\btagline",
    ]),
]

# Negative-only patterns → "Don't do this" if no category matched
DONT_HINTS = [
    r"\b(never|don'?t|stop|avoid|kill|drop|cut|remove|delete) (use|do|show|put|include|write|the|this|that)\b",
]
_DONT_RE = re.compile("|".join(DONT_HINTS), re.IGNORECASE)


def infer_category(text: str) -> str:
    """Return the section header (without leading '## ') that fits the text."""
    for header, patterns in CATEGORY_RULES:
        compiled = re.compile("|".join(patterns), re.IGNORECASE)
        if compiled.search(text):
            return header
    if _DONT_RE.search(text):
        return "Don't do this"
    return "Uncategorized"


def format_entry(text: str, source: str, today: str) -> str:
    """Build a style.md entry block from the verbatim prompt."""
    # Heuristic one-line rule: take the first sentence-ish, lowercase the
    # leading word for imperative feel, strip trailing punctuation.
    first = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0].strip()
    if len(first) > 180:
        first = first[:180].rsplit(" ", 1)[0] + "…"
    quote = text.strip().replace("\n", " ").replace('"', "'")
    if len(quote) > 280:
        quote = quote[:280].rsplit(" ", 1)[0] + "…"
    return (
        f"\n- **[{today}] {first}**\n"
        f"  Source: {source}\n"
        f'  Quote: "{quote}"\n'
        f"  Applies to: all (recategorize next run if wrong)\n"
    )


def append_under_category(prefs_path: Path, category: str, entry: str) -> None:
    """Insert entry at the end of the named category section in style.md."""
    if not prefs_path.exists():
        prefs_path.parent.mkdir(parents=True, exist_ok=True)
        prefs_path.write_text(f"# Preferences\n\n## {category}\n{entry}", encoding="utf-8")
        return

    text = prefs_path.read_text(encoding="utf-8")
    header = f"## {category}"

    if header not in text:
        # Append a fresh section at end of file
        if not text.endswith("\n"):
            text += "\n"
        text += f"\n{header}\n{entry}"
        prefs_path.write_text(text, encoding="utf-8")
        return

    # Find the section, append at its end (just before the next "## " or EOF)
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    inserted = False
    while i < len(lines):
        out.append(lines[i])
        if not inserted and lines[i].rstrip() == header:
            # Walk forward until the next "## " or EOF
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                out.append(lines[j])
                j += 1
            # Strip trailing blank lines before our insert, then add entry
            while out and out[-1].strip() == "":
                out.pop()
            out.append("\n")
            out.append(entry.lstrip("\n"))
            out.append("\n")
            inserted = True
            i = j
            continue
        i += 1
    prefs_path.write_text("".join(out), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Append a correction to style.md")
    p.add_argument("--text", help="Manual mode: skip stdin, use this string as the prompt")
    p.add_argument("--source", default="hook (UserPromptSubmit)", help="Source label for the entry")
    p.add_argument("--dry-run", action="store_true", help="Print the would-be entry, don't write")
    p.add_argument("--force", action="store_true", help="Skip pattern match; always log")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.text is not None:
        prompt = args.text
        source = args.source
    else:
        try:
            payload = json.load(sys.stdin)
        except json.JSONDecodeError:
            # Hook fired but stdin wasn't JSON — silent no-op.
            return 0
        prompt = payload.get("prompt", "") or ""
        cwd = payload.get("cwd", "")
        source = f"hook (UserPromptSubmit) — cwd: {cwd}" if cwd else args.source

    if not prompt.strip():
        return 0

    if not args.force and not _TRIGGER_RE.search(prompt):
        return 0  # silent no-match

    category = infer_category(prompt)
    today = os.environ.get("AIOS_TODAY") or date.today().isoformat()
    entry = format_entry(prompt, source, today)

    if args.dry_run:
        print(f"--- DRY RUN ---\nCategory: {category}\nEntry:{entry}")
        return 0

    append_under_category(PREFS, category, entry)

    # System reminder back to Claude so the model knows the rule was captured.
    # UserPromptSubmit hooks' stdout is prepended to the user prompt as context.
    print(
        f"[instagram-carousel hook] correction logged → "
        f"references/style.md § {category}. "
        f"Don't restate it; just apply it going forward."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
