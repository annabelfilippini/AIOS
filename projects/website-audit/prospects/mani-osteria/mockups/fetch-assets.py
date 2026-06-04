"""Download Mani Osteria photography to mockups/assets/ for the redesign mockup.

Sources: Yelp biz page (public photos) + Mani's own WP CDN (tomatoes, crostini, cocktails).
All images are Mani's — we're using their existing assets, not stock.
"""

import requests
from pathlib import Path

BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

# Yelp CDN — public food/interior photos from Mani's Yelp page
YELP = {
    "hero-pizza-puttanesca.jpg":   "https://s3-media0.fl.yelpcdn.com/bphoto/7hgtuK296VT_0goS-rK_Pg/o.jpg",
    "dining-room.jpg":             "https://s3-media0.fl.yelpcdn.com/bphoto/EUcectmb-4IAbjVN5I5kgQ/o.jpg",
    "arancini.jpg":                "https://s3-media0.fl.yelpcdn.com/bphoto/d01RhZycXBPD9RKnzRjR5w/o.jpg",
    "puttanesca-alt.jpg":          "https://s3-media0.fl.yelpcdn.com/bphoto/pARQTBfsTqGPi2QuqVntqQ/o.jpg",
    "carbonara.jpg":               "https://s3-media0.fl.yelpcdn.com/bphoto/O1oPcEHADvZccIX3AfiMNA/o.jpg",
    "gelato.jpg":                  "https://s3-media0.fl.yelpcdn.com/bphoto/3IOEg--I6nSN0JOjLIh_Qw/o.jpg",
    "interior-1.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/BZXLzFD2pMm3o6URBqYPJw/o.jpg",
    "interior-2.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/v9fDK5rDYbhV6oom0r05og/o.jpg",
    "interior-3.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/F1XMbhhpmJTLGQAm5wyOPQ/o.jpg",
    "interior-4.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/7-8nYWZl47bPHg2U7jNtlA/o.jpg",
    "outside-1.jpg":               "https://s3-media0.fl.yelpcdn.com/bphoto/UeAKNxf66FzQULF7zNn76w/o.jpg",
    "outside-2.jpg":               "https://s3-media0.fl.yelpcdn.com/bphoto/mhlXbJ64s9ZUwPdzIVUa2Q/o.jpg",
    "ann-arbor-classic.jpg":       "https://s3-media0.fl.yelpcdn.com/bphoto/WkONHtG7oAZu5c05l62mbg/o.jpg",
    "pickled-tomatoes.jpg":        "https://s3-media0.fl.yelpcdn.com/bphoto/i2XJD1oVc7fJBBSfdz6H7g/o.jpg",
    "red-onion-pistachio.jpg":     "https://s3-media0.fl.yelpcdn.com/bphoto/BaJ8dDC-wE-MMEPDoTHYLw/o.jpg",
    "caesar-salad.jpg":            "https://s3-media0.fl.yelpcdn.com/bphoto/ej8Ek70_SjU010B-qMh3iQ/o.jpg",
    "margherita.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/XmNXPuXKRy-yOiJRp82A9Q/o.jpg",
    "tartufo.jpg":                 "https://s3-media0.fl.yelpcdn.com/bphoto/7Qetcsf6V-ShQyQ57NygVA/o.jpg",
    "pork-belly.jpg":              "https://s3-media0.fl.yelpcdn.com/bphoto/ReSQY6QUJ-i0L9xCIFVvlw/o.jpg",
    "arugula-prosciutto.jpg":      "https://s3-media0.fl.yelpcdn.com/bphoto/MnfkA_p7GtWsdBgULjz0dA/o.jpg",
    "vodka-pasta.jpg":             "https://s3-media0.fl.yelpcdn.com/bphoto/8OLE54g4JWhyZR4d9iR53A/o.jpg",
    "whipped-ricotta.jpg":         "https://s3-media0.fl.yelpcdn.com/bphoto/eL6Jbz5Ie4HRRJ7Md42bmw/o.jpg",
    "charred-octopus.jpg":         "https://s3-media0.fl.yelpcdn.com/bphoto/CxZU7qmcFyWQXvMfiHks6A/o.jpg",
    "shrimp-scampi.jpg":           "https://s3-media0.fl.yelpcdn.com/bphoto/dvGj-6VWd9BdYeWPBQk9dQ/o.jpg",
}

# Mani's own WP CDN
MANI = {
    "mani-tomatoes.jpg":  "https://maniosteria.com/wp-content/uploads/sites/2/2022/02/man_thumbnail_tomatoes_100121.jpg",
    "mani-crostini.jpg":  "https://maniosteria.com/wp-content/uploads/sites/2/2022/02/man_thumbnail_crostini_112921.jpg",
    "mani-cocktails.jpg": "https://maniosteria.com/wp-content/uploads/sites/2/2022/02/man_thumbnail_cocktails_020422.jpg",
    "mani-collage.jpg":   "https://maniosteria.com/wp-content/uploads/sites/2/2022/02/man_thumbnail_collage01_0204_02-1.jpg",
    "mani-image1.jpg":    "https://maniosteria.com/wp-content/uploads/sites/2/2021/08/image1-1-compressed.jpg",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36",
    "Referer": "https://www.yelp.com/",
}


def download(name, url, referer=None):
    out = ASSETS / name
    if out.exists():
        print(f"  [skip] {name} ({out.stat().st_size//1024}KB)")
        return
    headers = dict(HEADERS)
    if referer:
        headers["Referer"] = referer
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        out.write_bytes(r.content)
        print(f"  [ok]   {name} ({len(r.content)//1024}KB)")
    except Exception as e:
        print(f"  [FAIL] {name}: {type(e).__name__}: {e}")


print("=== Yelp ===")
for name, url in YELP.items():
    download(name, url, referer="https://www.yelp.com/")

print("\n=== Mani WP CDN ===")
for name, url in MANI.items():
    download(name, url, referer="https://maniosteria.com/")

print(f"\n=== Done. {len(list(ASSETS.glob('*.jpg')))} files in {ASSETS} ===")
