"""Google Trends via pytrends.

Pulls interest_over_time (12mo) + interest_by_region for category-level queries.
pytrends 429s after ~2 requests, so we prioritize the 3 most strategic comparisons.
"""
import json
import time
from pathlib import Path

from pytrends.request import TrendReq

BASE = Path(__file__).resolve().parent
OUT = BASE / "trends.json"

# One build_payload only to avoid 429. Max 5 terms.
# Strategic comparison: Adelitas's own category terms side by side.
TERMS = [
    "Mexican restaurant Denver",
    "Michoacan food Denver",
    "mezcal bar Denver",
    "best Mexican food Denver",
    "tequila Denver",
]


def run():
    pytrends = TrendReq(hl="en-US", tz=360)
    out = {"terms": TERMS, "timeframe": "today 12-m", "geo": "US"}

    print(f"Building payload for: {TERMS}")
    pytrends.build_payload(TERMS, timeframe="today 12-m", geo="US")

    print("Fetching interest_over_time...")
    iot = pytrends.interest_over_time()
    if not iot.empty:
        iot = iot.drop(columns=["isPartial"], errors="ignore")
        out["interest_over_time"] = {
            "dates": [d.strftime("%Y-%m-%d") for d in iot.index],
            "values": {t: iot[t].tolist() for t in TERMS if t in iot.columns},
        }
        out["summary_iot"] = {
            t: {
                "mean": round(iot[t].mean(), 1),
                "max": int(iot[t].max()),
                "min": int(iot[t].min()),
                "peak_date": iot[t].idxmax().strftime("%Y-%m-%d"),
            }
            for t in TERMS
            if t in iot.columns
        }

    time.sleep(2)

    print("Fetching interest_by_region (STATE)...")
    try:
        ibr = pytrends.interest_by_region(resolution="REGION", inc_low_vol=True)
        if not ibr.empty:
            top_by_term = {}
            for t in TERMS:
                if t in ibr.columns:
                    top = ibr[t].sort_values(ascending=False).head(10)
                    top_by_term[t] = {k: int(v) for k, v in top.items()}
            out["top_states"] = top_by_term
    except Exception as e:
        out["top_states_error"] = str(e)

    time.sleep(2)

    print("Fetching interest_by_region (Denver metros)...")
    try:
        ibr_metro = pytrends.interest_by_region(resolution="DMA", inc_low_vol=False)
        if not ibr_metro.empty:
            denver_row = ibr_metro[ibr_metro.index.str.contains("Denver", case=False, na=False)]
            if not denver_row.empty:
                out["denver_dma"] = {
                    t: int(denver_row[t].iloc[0]) for t in TERMS if t in denver_row.columns
                }
    except Exception as e:
        out["denver_dma_error"] = str(e)

    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUT}")
    if "summary_iot" in out:
        for t, s in out["summary_iot"].items():
            print(f"  {t}: mean={s['mean']} peak={s['max']} on {s['peak_date']}")


if __name__ == "__main__":
    run()
