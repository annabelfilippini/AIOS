"""SEO research for Hop Alley: autocomplete + pytrends + DIY AnswerThePublic."""
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "seo"
OUT.mkdir(exist_ok=True)

KEYWORDS = [
    # Branded
    "hop alley",
    "hop alley denver",
    # Category
    "chinese restaurant denver",
    "sichuan restaurant denver",
    "michelin restaurants denver",
    "michelin bib gourmand denver",
    # Intent
    "best chinese food denver",
    "chef's counter denver",
    "upscale chinese denver",
    "chinese tasting menu denver",
]


def autocomplete(query: str) -> list[str]:
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={urllib.parse.quote(query)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read().decode("utf-8"))
        return data[1] if len(data) > 1 else []
    except Exception as e:
        return [f"ERROR: {e}"]


def run_autocomplete_all():
    results = {}
    for kw in KEYWORDS:
        suggs = autocomplete(kw)
        results[kw] = suggs
        print(f"  {kw}: {len(suggs)} suggestions")
        time.sleep(0.4)
    (OUT / "autocomplete.json").write_text(json.dumps(results, indent=2))
    print(f"Wrote {OUT / 'autocomplete.json'}")
    return results


def run_diy_atp():
    """DIY AnswerThePublic — question + segment + comparison prefixes for core terms."""
    seeds = [
        "chinese food denver",
        "sichuan denver",
        "hop alley",
        "michelin denver",
    ]
    prefixes = {
        "questions": ["how to", "what is", "is ", "why is", "where is", "when is"],
        "segments": [" for kids", " for date night", " for groups", " for birthday", " vegan"],
        "comparisons": [" vs ", " or ", " near me", " reservations", " menu"],
    }
    results = {}
    for seed in seeds:
        results[seed] = {}
        for bucket, plist in prefixes.items():
            bucket_out = {}
            for p in plist:
                q = f"{p}{seed}" if p.endswith(" ") or p.startswith(" ") is False else f"{seed}{p}"
                # Question prefixes precede the seed; segments/comparisons follow.
                if bucket == "questions":
                    q = f"{p} {seed}".strip()
                else:
                    q = f"{seed}{p}"
                suggs = autocomplete(q)
                bucket_out[q] = suggs
                time.sleep(0.4)
            results[seed][bucket] = bucket_out
        print(f"  {seed}: queried {sum(len(p) for p in prefixes.values())} prefixes")
    (OUT / "diy_atp.json").write_text(json.dumps(results, indent=2))
    print(f"Wrote {OUT / 'diy_atp.json'}")
    return results


def run_trends():
    from pytrends.request import TrendReq
    pytrends = TrendReq(hl="en-US", tz=360, timeout=(10, 25))
    # One build_payload — batching keeps rate-limit exposure minimal
    terms = ["hop alley", "chinese food denver", "sichuan denver"]
    pytrends.build_payload(terms, timeframe="today 12-m", geo="US")
    iot = pytrends.interest_over_time()
    by_region = pytrends.interest_by_region(resolution="REGION", inc_low_vol=False)

    iot_out = iot.reset_index().to_dict(orient="records") if not iot.empty else []
    # Region: top 10 for each term
    region_out = {}
    if not by_region.empty:
        for term in terms:
            if term in by_region.columns:
                top10 = by_region[term].sort_values(ascending=False).head(10)
                region_out[term] = {state: int(val) for state, val in top10.items()}

    # Monthly summary for iot
    summary = {}
    if iot_out:
        for term in terms:
            vals = [row.get(term, 0) for row in iot_out if isinstance(row.get(term), (int, float))]
            if vals:
                summary[term] = {
                    "min": min(vals),
                    "max": max(vals),
                    "avg": round(sum(vals) / len(vals), 1),
                    "latest": vals[-1] if vals else None,
                }

    out = {"terms": terms, "interest_over_time": iot_out, "top_regions": region_out, "summary": summary}
    (OUT / "trends.json").write_text(json.dumps(out, indent=2, default=str))
    print(f"Wrote {OUT / 'trends.json'}")
    return out


if __name__ == "__main__":
    print("== 1. Google Autocomplete ==")
    run_autocomplete_all()

    print("\n== 2. DIY AnswerThePublic ==")
    run_diy_atp()

    print("\n== 3. Google Trends (pytrends) ==")
    try:
        run_trends()
    except Exception as e:
        print(f"Trends failed: {e}")
        (OUT / "trends_error.txt").write_text(str(e))
