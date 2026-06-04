"""Pull real hours/phone/reviews for Adelitas from OpenTable + Yelp via Firecrawl."""
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])
BASE = Path(__file__).resolve().parent / "facts"
BASE.mkdir(exist_ok=True)

TARGETS = [
    ("opentable-broadway", "https://www.opentable.com/r/adelitas-cocina-y-cantina-denver"),
    ("yelp-broadway", "https://www.yelp.com/biz/adelitas-cocina-y-cantina-denver"),
    ("yelp-edgewater", "https://www.yelp.com/biz/adelitas-cocina-y-cantina-edgewater"),
    ("google-broadway-search", "https://www.google.com/search?q=adelitas+cocina+y+cantina+denver+broadway+hours"),
    ("google-edgewater-search", "https://www.google.com/search?q=adelitas+cocina+y+cantina+edgewater+hours+phone"),
]

for name, url in TARGETS:
    print(f"\n=== {name} ===\n{url}")
    try:
        r = app.scrape(url, formats=["markdown"], wait_for=4000)
        md = r.markdown or ""
        (BASE / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  {len(md)} chars")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
