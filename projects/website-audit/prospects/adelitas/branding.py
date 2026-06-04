"""Firecrawl branding pass for Adelitas. Scrapes /broadway (the real template;
root is a placeholder 'Location Picker' page with no design tokens)."""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent

TARGETS = [
    ("adelitas", "https://adelitasco.com/broadway"),
    ("la-dona", "https://ladonamezcaleria.com/"),
]

for name, url in TARGETS:
    print(f"\n=== {name} ({url}) ===")
    try:
        r = app.scrape(url, formats=["branding"], wait_for=3000)
        # Firecrawl returns branding in r.branding (pydantic) or dict.
        branding = getattr(r, "branding", None)
        if branding is None and isinstance(r, dict):
            branding = r.get("branding")
        if branding is None:
            # Some SDK versions: r.data.branding
            data = getattr(r, "data", None)
            if data is not None:
                branding = getattr(data, "branding", None)
        if hasattr(branding, "model_dump"):
            branding = branding.model_dump()
        print(json.dumps(branding, indent=2, default=str)[:800])
        out_path = BASE / ("branding.json" if name == "adelitas" else "branding-la-dona.json")
        out_path.write_text(json.dumps(branding, indent=2, default=str))
        print(f"  -> {out_path}")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        # Dump everything we can see for debugging
        try:
            print("  response keys:", list(vars(r).keys()) if 'r' in dir() else "no r")
        except Exception:
            pass
