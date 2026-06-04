"""Second facts pass — Yelp biz page + Michigan Daily article for review quotes and press."""
import os, json, time, requests
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent
FACTS = BASE / "facts"

SOURCES = [
    ("yelp-biz", "https://www.yelp.com/biz/amers-delicatessen-ann-arbor"),
    ("mich-daily", "https://www.michigandaily.com/arts/amers-delicatessen-a-university-of-michigan-students-home-base/"),
    ("tripadvisor", "https://www.tripadvisor.com/Restaurant_Review-g29556-d416898-Reviews-Amer_s_Deli-Ann_Arbor_Michigan.html"),
]

results = {}
for name, url in SOURCES:
    print(f"\n[{name}] {url}")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=5000)
        md = r.markdown or ""
        ok = len(md) > 500
        suffix = "" if ok else "-WEAK"
        (FACTS / f"{name}{suffix}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars {'OK' if ok else 'WEAK'}")
        if r.screenshot:
            resp = requests.get(r.screenshot, timeout=60)
            (FACTS / f"{name}-full.png").write_bytes(resp.content)
        results[name] = {"url": url, "ok": ok, "chars": len(md)}
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        results[name] = {"url": url, "ok": False, "error": str(e)}
    time.sleep(0.5)

summary_path = FACTS / "deep-summary.json"
summary_path.write_text(json.dumps(results, indent=2, default=str))
print(f"\nDone. Summary: {summary_path}")
