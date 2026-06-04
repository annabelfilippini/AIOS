"""Google Autocomplete runner for SEO research.

Hits suggestqueries.google.com with firefox client, collects suggestions
per keyword + DIY AnswerThePublic prefixes. Writes JSON to autocomplete.json.
"""
import json
import time
import urllib.parse
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parent
OUT = BASE / "autocomplete.json"

KEYWORDS = [
    "Adelitas Denver",
    "La Dona mezcaleria Denver",
    "Chef Silvia Andaya",
    "Mexican restaurant Denver",
    "Michoacan food Denver",
    "mezcal bar Denver",
    "family owned Mexican restaurant Denver",
    "best Mexican food Denver",
    "Mexican restaurant Denver reservations",
    "tequila dinner Denver",
]

QUESTION_PREFIXES = ["how to", "what is", "where is", "is", "why is", "when does"]
SEGMENT_SUFFIXES = ["for kids", "for families", "for groups", "for date night",
                    "for birthday", "near me"]
COMPARISON_SUFFIXES = ["vs", "or"]


def fetch(query: str) -> list[str]:
    url = (
        "https://suggestqueries.google.com/complete/search"
        f"?client=firefox&q={urllib.parse.quote(query)}"
    )
    r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    data = r.json()
    return data[1] if len(data) > 1 else []


def run():
    out = {"keywords": {}, "questions": {}, "segments": {}, "comparisons": {}}

    for kw in KEYWORDS:
        out["keywords"][kw] = fetch(kw)
        time.sleep(0.5)

    # DIY AnswerThePublic — only on the top 3 category/intent keywords
    focus_kws = [
        "Adelitas",
        "Michoacan food Denver",
        "mezcal bar Denver",
        "best Mexican food Denver",
    ]
    for kw in focus_kws:
        out["questions"][kw] = {}
        for pfx in QUESTION_PREFIXES:
            q = f"{pfx} {kw}"
            out["questions"][kw][pfx] = fetch(q)
            time.sleep(0.4)
        out["segments"][kw] = {}
        for sfx in SEGMENT_SUFFIXES:
            q = f"{kw} {sfx}"
            out["segments"][kw][sfx] = fetch(q)
            time.sleep(0.4)
        out["comparisons"][kw] = {}
        for sfx in COMPARISON_SUFFIXES:
            q = f"{kw} {sfx}"
            out["comparisons"][kw][sfx] = fetch(q)
            time.sleep(0.4)

    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(f"Keywords: {sum(len(v) for v in out['keywords'].values())} total suggestions")
    print(f"Questions: {sum(len(v) for pfx in out['questions'].values() for v in pfx.values())}")
    print(f"Segments: {sum(len(v) for pfx in out['segments'].values() for v in pfx.values())}")
    print(f"Comparisons: {sum(len(v) for pfx in out['comparisons'].values() for v in pfx.values())}")


if __name__ == "__main__":
    run()
