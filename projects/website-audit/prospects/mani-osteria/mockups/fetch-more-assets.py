"""Fetch a second batch of Mani photography — TripAdvisor 1100/1200px shots (no Lena J watermarks)
plus Yelp photos we missed the first pass. Writes to mockups/assets/.
"""

import requests
from pathlib import Path

BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

# TripAdvisor 1100/1200px — different contributors, no "Photo by Lena J" watermarks
TA = {
    "ta-mani-1.jpg":       "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/11/1a/99/mani-osteria.jpg?w=1100&h=1100&s=1",
    "ta-mani-2.jpg":       "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/11/1a/9a/mani-osteria.jpg?w=1100&h=1100&s=1",
    "ta-mani-3.jpg":       "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/11/1a/9b/mani-osteria.jpg?w=1100&h=1100&s=1",
    "ta-mani-4.jpg":       "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/11/1a/9c/mani-osteria.jpg?w=1100&h=1100&s=1",
    "ta-mani-5.jpg":       "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/11/1a/9d/mani-osteria.jpg?w=1100&h=1100&s=1",
    "ta-interior.jpg":     "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/ad/f9/b5/interior.jpg?w=1200&h=1200&s=1",
    "ta-asparagus.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/ad/fd/7b/asparagus-appetizer.jpg?w=1200&h=1200&s=1",
    "ta-pizza.jpg":        "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/ad/fe/fb/pizza.jpg?w=1100&h=1100&s=1",
    "ta-margherita.jpg":   "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/93/46/8d/margherita.jpg?w=1100&h=1100&s=1",
    "ta-pepperoni.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/93/46/b4/pepperoni.jpg?w=1100&h=1100&s=1",
    "ta-squash-soup.jpg":  "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/c5/87/a6/butternut-squash-soup.jpg?w=1100&h=1100&s=1",
    "ta-caption-1.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/25/01/2d/75/caption.jpg?w=1200&h=1200&s=1",
    "ta-caption-2.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/25/01/2d/76/caption.jpg?w=1200&h=1200&s=1",
    "ta-caption-3.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/25/01/2d/77/caption.jpg?w=1200&h=1200&s=1",
    "ta-caption-4.jpg":    "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/d3/b0/f6/caption.jpg?w=1100&h=1100&s=1",
}

# Yelp photo IDs we haven't grabbed yet — from gallery scrape
YELP_NEW = {
    "yelp-new-1.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/-NM_xZIZ_tVaKbULpEVy1A/o.jpg",
    "yelp-new-2.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/2OQuQBR54F66jtlRndzJsA/o.jpg",
    "yelp-new-3.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/43kj9m4pji6Z0QM5L5NdrQ/o.jpg",
    "yelp-new-4.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/cEE5HuqlspnAISRy81crKQ/o.jpg",
    "yelp-new-5.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/CK6Ft6dfbIER6bReKaUZxA/o.jpg",
    "yelp-new-6.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/CS0_I7FtgnbcO3oPd_bmJg/o.jpg",
    "yelp-new-7.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/HpMUWHNRwbXb_tHe7KoALg/o.jpg",
    "yelp-new-8.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/IU6Z3DEiwbSHmqP4Me95FQ/o.jpg",
    "yelp-new-9.jpg":  "https://s3-media0.fl.yelpcdn.com/bphoto/joC7in52MrI5OW57FOuzXA/o.jpg",
    "yelp-new-10.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/JPoDDu3I8q55rNDMrNZisQ/o.jpg",
    "yelp-new-11.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/JZKmArw_kJydfqw7iTcrCg/o.jpg",
    "yelp-new-12.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/LCQcOXpyiHB6QlZ-HBIrqg/o.jpg",
    "yelp-new-13.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/LJscB4Lei-2m7anPJefnEg/o.jpg",
    "yelp-new-14.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/RhAZnreaYMvT5ZhC_b7urA/o.jpg",
    "yelp-new-15.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/vsNHqih2Q7oefK6OQasmtw/o.jpg",
    "yelp-new-16.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/X5cHdh_T2BKtK1qLM5L6Rg/o.jpg",
    "yelp-new-17.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/XDFXlyOuAq2qOXXqMDf-Ig/o.jpg",
    "yelp-new-18.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/3Kb8_Au5Si2y-3Ay063O-A/o.jpg",
    "yelp-new-19.jpg": "https://s3-media0.fl.yelpcdn.com/bphoto/fLn7kgZhmCDI8XoYOsNm1A/o.jpg",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36",
}


def download(name, url, referer):
    out = ASSETS / name
    if out.exists():
        print(f"  [skip] {name}")
        return
    headers = dict(HEADERS)
    headers["Referer"] = referer
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        out.write_bytes(r.content)
        print(f"  [ok]   {name} ({len(r.content)//1024}KB)")
    except Exception as e:
        print(f"  [FAIL] {name}: {type(e).__name__}: {e}")


print("=== TripAdvisor ===")
for name, url in TA.items():
    download(name, url, "https://www.tripadvisor.com/")

print("\n=== Yelp (new batch) ===")
for name, url in YELP_NEW.items():
    download(name, url, "https://www.yelp.com/")

print(f"\nTotal in assets/: {len(list(ASSETS.glob('*.jpg')))}")
