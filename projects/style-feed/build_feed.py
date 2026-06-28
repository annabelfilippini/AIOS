#!/usr/bin/env python3
"""
STYLE FEED — build script (v1: + creators, + heart/✕ taste learning).

Reads raw ShopMy storefront pulls (one per creator), strips out non-apparel,
scores each item against Annabel's taste, merges cross-creator co-signs, and
emits a single self-contained feed.html.

THREE scoring inputs:
  1) Text heuristics over brand + title (liked brands, fabrics/cuts, loud prints).
  2) COLOUR read straight from the product photo (mean + high-percentile
     saturation of the garment). Old-money-neutral == low saturation, so this
     promotes white/cream/grey/black/beige and demotes loud/colourful pieces.
  3) LEARNED feedback from Annabel's hearts/✕ (data/feedback.json, exported from
     the feed). Liked brands/categories/colours get boosted, disliked ones
     penalised, exact dislikes dropped, exact likes pinned high. Inert until a
     feedback.json exists.

In the browser, every heart/✕ also re-ranks the feed live (localStorage), so it
adapts instantly without a rebuild. Price no longer gates anything (Annabel:
price doesn't matter for now); it's still displayed.

Colour metrics are cached to data/color_cache.json so re-runs are instant.
"""

import os, json, re, html, pathlib, shutil, io, base64, datetime, urllib.request, urllib.parse, concurrent.futures
import numpy as np
from PIL import Image

ROOT = pathlib.Path("/Users/annabelfilippini/Documents/AI-OS/projects/style-feed")
RAW = ROOT / "data" / "raw"
CACHE = ROOT / "data" / "color_cache.json"
VCACHE = ROOT / "data" / "vision_cache.json"
FEEDBACK = ROOT / "data" / "feedback.json"
SRC = ROOT / "data" / "sources"

# ---- proxied image hosts ----------------------------------------------------
# Stores whose image CDN is behind Cloudflare bot management (403 to plain
# fetches and to Anthropic's by-URL vision fetch). For these we (a) pull bytes
# with a real Chrome TLS fingerprint via curl_cffi at build time for colour +
# vision, and (b) rewrite the card <img src> to the serve.py /img proxy so the
# browser loads them too. Keep this in sync with serve.py PROXY_HOSTS.
PROXY_HOSTS = {"assets.aritzia.com"}
NEW_DAYS = 7   # an item stamped first_seen within this many days gets a NEW badge
_curl = None
def needs_proxy(url):
    return urllib.parse.urlparse(url or "").netloc in PROXY_HOSTS

def fetch_bytes(url):
    """Image bytes for build-time analysis. curl_cffi (Chrome fingerprint) for
    Cloudflare-fronted hosts, plain urllib otherwise."""
    global _curl
    if needs_proxy(url):
        if _curl is None:
            from curl_cffi import requests as _r
            _curl = _r
        r = _curl.get(url, impersonate="chrome120", timeout=20)
        if r.status_code != 200:
            raise RuntimeError(f"proxy fetch {r.status_code}")
        return r.content
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=15).read()

def proxied_src(url):
    """Card <img src>: route Cloudflare-fronted hosts through serve.py /img."""
    return f"/img?u={urllib.parse.quote(url, safe='')}" if needs_proxy(url) else url

def as_jpg_url(url):
    """Force a Cloudinary URL to emit JPEG (Anthropic vision rejects AVIF, which
    Aritzia's f_auto serves to a Chrome fingerprint)."""
    if "/upload/" not in url:
        return url
    if "f_auto" in url:
        return url.replace("f_auto", "f_jpg")
    head, tail = url.split("/upload/", 1)
    return f"{head}/upload/f_jpg/{tail}"

# ---- env + AI-vision config -------------------------------------------------
def _load_env():
    envf = ROOT / ".env"
    if not envf.exists():
        return
    for line in envf.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

_load_env()
# Vision tagging runs only when a key is present; without it the build falls
# back to the old saturation heuristic so a keyless rebuild still works.
VISION_ON = bool(os.environ.get("ANTHROPIC_API_KEY")) and os.environ.get("STYLE_FEED_NO_VISION") != "1"
VISION_MODEL = os.environ.get("STYLE_FEED_VISION_MODEL", "claude-opus-4-8")  # env override; haiku to cut cost
SILHOUETTES = ["fitted", "relaxed", "oversized", "wide-leg", "straight", "cropped",
               "tailored", "a-line", "flowy", "structured", "bodycon", "other"]
FORMALITIES = ["loungewear", "casual", "smart-casual", "formal", "evening"]
PATTERNS = ["solid", "stripe", "check", "floral", "print", "textured", "embellished", "colorblock"]
# Borrowed from The Yes's deeper per-item taxonomy: one swipe should teach many
# garment dimensions, not just cut. "na" = doesn't apply (shoes/bags have no
# neckline, etc.) so the model never penalises a missing axis.
NECKLINES = ["crew", "v-neck", "scoop", "boat", "collared", "halter", "square",
             "cowl", "turtleneck", "strapless", "off-shoulder", "other", "na"]
SLEEVES = ["sleeveless", "cap", "short", "three-quarter", "long", "puff", "strappy", "other", "na"]
LENGTHS = ["cropped", "hip", "tunic", "knee", "midi", "maxi", "mini", "full-length", "other", "na"]
FABRICS = ["cotton", "linen", "silk", "wool", "cashmere", "knit", "denim", "leather",
           "satin", "synthetic", "other"]
DRAPES = ["structured", "tailored", "fluid", "flowy", "stiff", "clingy", "other"]
# Back detail — the only axis the front-facing neckline tag can't capture. "na"
# covers "back not shown in the photo" AND "not a top/dress", so the existing
# "na"-is-skipped logic in scoring handles both without rewarding non-signal.
BACKS = ["open-back", "low-back", "cutout-back", "tie-back", "halter", "closed", "na"]
VISION_SCHEMA = {
    "type": "object",
    "properties": {
        "garment": {"type": "boolean"},
        "primary_color": {"type": "string"},
        "neutral": {"type": "number"},
        "silhouette": {"type": "string", "enum": SILHOUETTES},
        "formality": {"type": "string", "enum": FORMALITIES},
        "oldmoney": {"type": "number"},
        "pattern": {"type": "string", "enum": PATTERNS},
        "neckline": {"type": "string", "enum": NECKLINES},
        "sleeve": {"type": "string", "enum": SLEEVES},
        "length": {"type": "string", "enum": LENGTHS},
        "fabric": {"type": "string", "enum": FABRICS},
        "drape": {"type": "string", "enum": DRAPES},
        "back": {"type": "string", "enum": BACKS},
    },
    "required": ["garment", "primary_color", "neutral", "silhouette", "formality",
                 "oldmoney", "pattern", "neckline", "sleeve", "length", "fabric", "drape", "back"],
    "additionalProperties": False,
}
VISION_PROMPT = (
    "Tag this single fashion product photo for a personal style feed. Look only at the main item. "
    "Return: garment (true if a wearable garment/shoe/bag is clearly the subject, false if it's "
    "packaging, a flatlay, or unclear); primary_color (one or two words, the dominant colour of the "
    "item, e.g. 'cream', 'navy', 'chocolate brown'); neutral (0.0-1.0 — how quiet the palette is: "
    "1.0 = white/cream/grey/black/beige/navy, 0.0 = bright saturated colour); silhouette (overall "
    "cut); formality; oldmoney (0.0-1.0 — how much it reads as understated quiet-luxury / old-money "
    "vs trendy or loud); pattern; neckline; sleeve (sleeve length/type); length (overall length of "
    "the garment); fabric (best guess at primary material from the photo); drape (how the cloth "
    "hangs — structured/tailored vs fluid/flowy vs clingy); back (the back of a top/dress IF the "
    "photo shows it: open-back/low-back/cutout-back/tie-back/halter, or 'closed' for a normal full "
    "back — return 'na' if the back is not visible in the photo or the item is not a top/dress). For "
    "any axis that does not apply to the item (e.g. neckline/sleeve/length on a shoe or bag), return "
    "'na'. Judge from the photo, not from assumptions."
)

# ---- back-detail backfill (cheap, targeted) ---------------------------------
# Items tagged before the `back` axis existed are re-checked with one tiny
# question on a cheap model — only for garments where a back matters — rather
# than re-running the full Opus vision pass on the whole catalogue.
BACK_MODEL = os.environ.get("STYLE_FEED_BACK_MODEL", "claude-haiku-4-5")
BACK_SCHEMA = {"type": "object", "properties": {"back": {"type": "string", "enum": BACKS}},
               "required": ["back"], "additionalProperties": False}
BACK_PROMPT = (
    "Look at the BACK of this top or dress, only if the photo shows it. Classify the back: "
    "open-back (large bare-back opening), low-back (scooped low but not fully open), cutout-back "
    "(one or more cut-out openings), tie-back (laces/ties across the back), halter (ties at the neck "
    "leaving the upper back bare), closed (ordinary full back). Return 'na' if the back is not "
    "visible in the photo, or the item is not a top or dress. Judge only from the photo."
)

# All sources read from data/sources/*.json (stable, repo-local). Re-pull a
# creator's ShopMy storefront into that file to refresh; never point back at
# ephemeral .claude tool-result paths (they get cleaned and break the build).
SOURCES = [
    ("Brigette Pheloung", str(SRC / "brigettepheloung.json")),
    ("Paige Lorenze",     str(SRC / "paigelorenze.json")),
    ("Abby Catlin",       str(SRC / "abbycatlin.json")),
    ("Carly Riordan",     str(SRC / "carlyriordan.json")),
    ("Grace Atwood",      str(SRC / "graceatwood.json")),
    ("Merritt Beck",      str(SRC / "merrittbeck.json")),
    ("Mary Lawless Lee",  str(SRC / "marylawlesslee.json")),
]

# Brand catalogs (data/brands/*.json, same shape as sources). Unlike creator
# storefronts these are full catalogs and mostly off-taste, so they're trimmed at
# build time to the top BRAND_KEEP per brand that clear BRAND_MIN_SCORE — only the
# pieces that score as Annabel's taste survive into the feed.
BRANDS_DIR = ROOT / "data" / "brands"
BRANDS = [
    ("Dairy Boy",      str(BRANDS_DIR / "dairyboy.json")),
    ("Revolve",        str(BRANDS_DIR / "revolve.json")),
    ("Zara",           str(BRANDS_DIR / "zara.json")),
    ("Anthropologie",  str(BRANDS_DIR / "anthropologie.json")),
    ("Abercrombie",    str(BRANDS_DIR / "abercrombie.json")),
    ("Aritzia",        str(BRANDS_DIR / "aritzia.json")),
    ("Lululemon",      str(BRANDS_DIR / "lululemon.json")),
    ("Reformation",    str(BRANDS_DIR / "reformation.json")),
]
BRAND_KEEP = 24          # max items surfaced per brand catalog
BRAND_MIN_SCORE = 56     # a brand item must clear this taste score to show

# ---- taste vocabulary -------------------------------------------------------
# Non-apparel buckets. cats_of() (apparel nouns) is checked FIRST in classify(),
# so a "Powder Blue Sweater" or "Tea Length Dress" stays apparel; only items with
# no apparel noun fall through to beauty/home, and anything left over is dropped.
BEAUTY = re.compile(r"\b(serum|lipstick|mascara|foundation|concealer|blush|bronzer|highlighter|"
    r"eyeliner|eyeshadow|brow gel|lash|perfume|fragrance|cologne|eau de|shampoo|conditioner|"
    r"deodorant|cleanser|moisturiz|moisturis|sunscreen|spf|nail polish|skincare|toner|primer|"
    r"retinol|hyaluronic|exfoliant|self.?tan|body wash|hand cream|face cream|lotion|"
    r"sheet mask|face mask|lip balm|lip gloss|lip oil|setting spray|setting powder|cuticle|makeup)", re.I)
HOME = re.compile(r"\b(candle|diffuser|pillow|cushion|throw blanket|blanket|duvet|comforter|sheets?|"
    r"towel|nightstand|dresser|drawer|rug|lamp|vase|mug|bowl|platter|serving tray|tray|"
    r"organizer|organiser|dispenser|soap|picture frame|mirror|bedding|coaster|napkin|"
    r"curtain|basket|hanger|storage)", re.I)
KEEP = re.compile(r"\b(dress|gown|top|shirt|blouse|tank|tee|t-shirt|sweater|sweatshirt|knit|"
    r"cardigan|blazer|jacket|coat|trench|parka|pant|trouser|jean|denim|short|skort|skirt|set\b|"
    r"romper|jumpsuit|vest|shoe|sandal|heel|flat|loafer|boot|sneaker|mule|clog|bag|tote|purse|"
    r"clutch|crossbody|pochette|satchel|hobo|belt|scarf|sunglass|hat|cap\b|cashmere|robe|bikini|"
    r"swim|one piece|legging|capri|bralette|corset|slip|gloves|wrap|bandana|earring|bodysuit|pump|pant)", re.I)
OLDMONEY = re.compile(r"\b(cashmere|wool|merino|linen|silk|poplin|trench|blazer|tailored|"
    r"pleated|knit|loafer|ballet|trouser|midi|slip|button|oxford|cable|ribbed|boucle|tweed|"
    r"collared|cardigan|wide.?leg|straight.?leg|barrel|halter)", re.I)
LOUD = re.compile(r"\b(sequin|neon|rhinestone|leopard|zebra|snake|cutout|cut.?out|crystal|"
    r"glitter|rainbow|stripe|floral|print|metallic|fringe|feather|appliqu|western|paillette)", re.I)
LIKED_BRANDS = {b.lower() for b in [
    "The Row","Reformation","The Frankie Shop","Dairy Boy","Sezane","Sézane","Aritzia","Free People",
    "Anthropologie","Levi's","GRLFRND","AGOLDE","Tory Burch","Toteme","Totême","Khaite","Vince",
    "Everlane","Jenni Kayne","Posse","Faithfull","DISSH","Quince","Madewell","Abercrombie","Wilfred",
    "Babaton","J.Crew","Banana Republic","Nordstrom","Revolve","Lululemon","Varley","Alo","Set Active",
    "Djerf Avenue","With Jean","Sir","Aje","Staud","Mango","COS","Arket","Loulou Studio",
    "LESET","Réalisation Par","Realisation Par","Sunday Best","Vitamin A","Hunza G","Margaux","Christopher Esber"]}

# coarse category tags, used for taste learning (one source of truth, embedded in
# cards). Plural-aware (\bpants? etc.) so "Pants"/"Boots"/"Loafers" tag correctly.
CAT_PATTERNS = [
    ("dress",     r"\b(dress(?:es)?|gowns?)\b"),
    ("top",       r"\b(tops?(?!\s*handle)|blouses?|shirts?|tanks?|tees?|t-shirts?|bodysuits?|bralettes?|corsets?|camis?|halters?)\b"),
    ("knit",      r"\b(sweaters?|knits?|cardigans?|cashmere|jumpers?)\b"),
    ("outerwear", r"\b(blazers?|jackets?|coats?|trench(?:es)?|parkas?|vests?)\b"),
    ("bottom",    r"\b(pants?|trousers?|jeans|shorts|skirts?|skort|leggings?|capris?|culottes?)\b"),
    ("bag",       r"\b(bags?|totes?|purses?|clutch(?:es)?|crossbody|pochettes?|satchels?|hobos?)\b"),
    ("shoe",      r"\b(shoes?|sandals?|heels?|loafers?|boots?|sneakers?|mules?|clogs?|ballet|flats)\b"),
    ("accessory", r"\b(belts?|scarf|scarves|sunglass(?:es)?|hats?|caps?|gloves?|bandanas?|earrings?|necklaces?)\b"),
    ("swim",      r"\b(bikinis?|swimsuits?|swimwear|one piece)\b"),
]

def cats_of(text):
    return [name for name, pat in CAT_PATTERNS if re.search(pat, text, re.I)]

def classify(brand, title):
    """Return a category list, or None to drop. Apparel nouns win first (protects
    e.g. cream-coloured or tea-length clothing), then beauty, then home, then
    apparel-ish leftovers (wrap/robe/set); food/tech/supplements fall through.
    Categorises on the TITLE only, so a brand like "Joe's Jeans" can't tag a
    sweater as a bottom."""
    text = title
    # Standalone bras are underwear, not feed pieces. Keep bralettes/bandeaus
    # (worn as tops), sports bras (activewear), and swim/bikini tops.
    if re.search(r"\bbras?\b", text, re.I) and not re.search(
            r"bralette|bandeau|swim|bikini|sports? ?bra", text, re.I):
        return None
    # Hosiery / shapewear / socks are basics, not "cute clothes" discovery — and
    # "Control-Top ... Tights" was leaking into Tops (the "Top" in "Control-Top").
    if re.search(r"\b(tights?|hosiery|stockings?|nylons?|shapewear|control[- ]?top|socks?)\b",
                 text, re.I):
        return None
    # Underwear (thong/brief/boy-short/g-string sets). Guard the shoe sense of
    # "thong" (thong sandals/heels) so real footwear is never dropped.
    if re.search(r"\b(thongs?|briefs?|boy ?shorts?|g[- ]?strings?)\b", text, re.I) and not \
            re.search(r"sandal|heel|mule|flat|slide|flip|wedge|bag|case", text, re.I):
        return None
    # Loungewear / sleepwear gets its OWN category (and tab) so cute PJ sets
    # (Dairy Boy, Eberjey, ...) don't clutter Tops/Bottoms. Checked before the
    # apparel nouns, since "Sleep Pant"/"Pajama Set" otherwise read as bottom/top.
    if re.search(r"\b(pajamas?|pyjamas?|pjs?|nightgowns?|nightshirts?|nighti?es?|loungewear|"
                 r"sleep\s?(?:set|pant|short|shirt|tee|top|wear|dress|cami|romper|tank|suit)|"
                 r"robes?)\b", text, re.I):
        return ["loungewear"]
    cats = cats_of(text)
    if cats:
        # Swim is its own category: a bikini/swim top is swimwear, not a "top".
        if "swim" in cats:
            return ["swim"]
        # A dress/gown is a one-piece: descriptive words (shirt/tank/halter/corset/
        # scarf-print) don't make it a top or accessory. "dress" is the sole category
        # — UNLESS it's an adjective (dress shirt/pants), where the other garment wins.
        if "dress" in cats:
            if re.search(r"\bdress(?:es)?[\s-]+(shirt|pant|trouser|short|skirt|shoe|"
                         r"boot|sandal|sneaker|loafer|coat|jacket|blazer|sock)\b", text, re.I):
                cats = [c for c in cats if c != "dress"]
            else:
                return ["dress"]
        return cats
    if BEAUTY.search(text): return ["beauty"]
    if HOME.search(text): return ["home"]
    if KEEP.search(text): return ["other"]
    return None

# ---- helpers ----------------------------------------------------------------
def load_products(path):
    raw = json.load(open(path))
    txt = raw[0]["text"] if isinstance(raw, list) else raw
    obj = json.loads(txt) if isinstance(txt, str) else txt
    return obj["json"]["products"]

def price_val(s):
    if not s: return None
    m = re.search(r"(\d[\d,]*\.?\d*)", s)
    return float(m.group(1).replace(",", "")) if m else None

color_cache = json.load(open(CACHE)) if CACHE.exists() else {}

def colorfulness(url):
    """0 = greyscale/neutral, ~1 = vivid. Reads the garment, ignores white bg."""
    if url in color_cache: return color_cache[url]
    val = None
    try:
        raw = fetch_bytes(as_jpg_url(url) if needs_proxy(url) else url)  # PIL can't decode AVIF
        im = Image.open(io.BytesIO(raw)).convert("RGB"); im.thumbnail((90, 90))
        hsv = np.asarray(im.convert("HSV")).astype(float)
        h, w, _ = hsv.shape
        hsv = hsv[int(h*.18):int(h*.82), int(w*.18):int(w*.82)]      # center crop
        S = hsv[..., 1] / 255.0; V = hsv[..., 2] / 255.0
        fg = ~((V > .90) & (S < .10))                                # drop white bg
        Sf = S[fg] if fg.sum() > 20 else S.ravel()
        val = round(min(1.0, float(.6*Sf.mean() + .4*np.percentile(Sf, 90))), 4)
    except Exception:
        val = None
    color_cache[url] = val
    return val

# ---- retailer-link resolver (ShopMy product link -> real product page) ------
# The stored productUrl is a shopmy.us page. ShopMy's public product API
# (apiv3, no auth) returns the actual retailer URL, so we swap each card's href
# to the real shop. Cached to data/link_cache.json; falls back to the ShopMy
# link for anything that won't resolve.
LINK_CACHE = ROOT / "data" / "link_cache.json"
link_cache = json.load(open(LINK_CACHE)) if LINK_CACHE.exists() else {}
_API_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/148.0.0.0 Safari/537.36"

def resolve_link(product_url):
    """shopmy.us/shop/product/<id> -> retailer product URL (US), or None."""
    if not product_url: return None
    if product_url in link_cache: return link_cache[product_url]
    out = None
    m = re.search(r"/product/(\d+)", product_url)
    if m:
        pid = m.group(1)
        cur = re.search(r"Curator_id=(\d+)", product_url)
        api = f"https://apiv3.shopmy.us/api/v2/Products/{pid}?countryCode=US"
        if cur: api += f"&Curator_id={cur.group(1)}"
        try:
            req = urllib.request.Request(api, headers={
                "User-Agent": _API_UA, "Accept": "application/json",
                "Origin": "https://shopmy.us", "Referer": "https://shopmy.us/"})
            data = json.loads(urllib.request.urlopen(req, timeout=20).read())
            prod = data.get("product") or {}
            for ln in (prod.get("links") or []):
                st = (ln.get("url_data") or {}).get("urlStem") or ""
                if re.search(r"\b(uk|france|fr|de|eu|au|ca|us-uk)/", st):   # skip country mirrors
                    continue
                if ln.get("link"): out = ln["link"]; break
            if not out:
                links = prod.get("links") or []
                out = (links[0].get("link") if links else None) or prod.get("fallbackUrl")
        except Exception:
            out = None
    link_cache[product_url] = out
    return out

def text_score(p):
    brand = (p.get("brand") or "").strip(); title = (p.get("title") or "").strip()
    text = f"{brand} {title}"; why, s = [], 50
    om = OLDMONEY.findall(text)
    if om: s += min(20, 8*len(set(w.lower() for w in om))); why.append(f"Quiet-luxury cut ({om[0].lower()})")
    if brand.lower() in LIKED_BRANDS: s += 16; why.append(f"Brand you like ({brand})")
    if LOUD.search(text): s -= 12; why.append("Pattern/print noted")
    return s, why

def color_adjust(c, why):
    if c is None: return 0
    if c < .14: why.insert(0, "Reads neutral in the photo"); return 28
    if c < .22: why.insert(0, "Mostly neutral tones"); return 16
    if c < .32: return 4
    if c > .55: why.append("Too colourful for your palette"); return -34
    if c > .45: why.append("A bit bold for you"); return -20
    if c > .37: return -9
    return 0

# ---- AI-vision tags (silhouette / palette / formality, cached) --------------
vision_cache = json.load(open(VCACHE)) if VCACHE.exists() else {}
_aclient = None
def _anthropic():
    global _aclient
    if _aclient is None:
        import anthropic
        _aclient = anthropic.Anthropic()
    return _aclient

def vision_tag(url):
    """One Claude vision call per image → structured garment tags. Cached to
    data/vision_cache.json so re-runs are instant. Returns None on failure."""
    if url in vision_cache:
        return vision_cache[url]
    val = None
    try:
        # Cloudflare-fronted hosts 403 Anthropic's by-URL fetch, so send those as
        # base64 (bytes pulled with the Chrome fingerprint); everything else by URL.
        if needs_proxy(url):
            b = fetch_bytes(as_jpg_url(url))
            src = {"type": "base64", "media_type": "image/jpeg", "data": base64.b64encode(b).decode()}
        else:
            src = {"type": "url", "url": url}
        resp = _anthropic().messages.create(
            model=VISION_MODEL, max_tokens=400,
            output_config={"format": {"type": "json_schema", "schema": VISION_SCHEMA}},
            messages=[{"role": "user", "content": [
                {"type": "image", "source": src},
                {"type": "text", "text": VISION_PROMPT},
            ]}],
        )
        txt = next(b.text for b in resp.content if b.type == "text")
        val = json.loads(txt)
    except Exception:
        val = None
    vision_cache[url] = val
    return val

def back_tag(url):
    """One cheap vision call → the `back` axis only. Used to backfill items tagged
    before the axis existed. Returns a BACKS value or None on failure."""
    try:
        if needs_proxy(url):
            b = fetch_bytes(as_jpg_url(url))
            src = {"type": "base64", "media_type": "image/jpeg", "data": base64.b64encode(b).decode()}
        else:
            src = {"type": "url", "url": url}
        resp = _anthropic().messages.create(
            model=BACK_MODEL, max_tokens=60,
            output_config={"format": {"type": "json_schema", "schema": BACK_SCHEMA}},
            messages=[{"role": "user", "content": [
                {"type": "image", "source": src},
                {"type": "text", "text": BACK_PROMPT},
            ]}],
        )
        txt = next(b.text for b in resp.content if b.type == "text")
        return json.loads(txt).get("back")
    except Exception:
        return None

# Categorical vision axes and their match weights, shared by the server scorer
# and (mirrored) the in-browser rerank. Each tuple is (like_cap, like_per_count,
# dislike_cap, dislike_per_count). "na" never scores — it just means the axis
# doesn't apply to that item. Pattern is handled separately (asymmetric).
VIS_CATS = ["silhouette", "formality", "neckline", "sleeve", "length", "fabric", "drape", "back"]
VIS_WEIGHTS = {
    "silhouette": (14, 7, 12, 6),
    "formality":  (8, 4, 8, 4),
    "neckline":   (6, 3, 6, 3),
    "sleeve":     (6, 3, 6, 3),
    "length":     (6, 3, 6, 3),
    "fabric":     (8, 4, 8, 4),
    "drape":      (6, 3, 6, 3),
    "back":       (10, 5, 6, 3),   # asymmetric reward: a distinctive back is a strong "more like this"
}

# ---- recency weighting ------------------------------------------------------
# Taste evolves, so a recent swipe should outweigh an old one. Each like/✕ in
# feedback.json carries a `ts` (YYYY-MM-DD); its influence decays with a 45-day
# half-life: today=1.0, 45d ago=0.5, 90d ago=0.25. Legacy records were backfilled
# to a baseline date, so they still count, just less than fresh swipes over time.
RECENCY_HALF_LIFE = 45.0
_TODAY = datetime.date.today()
_TS_BASELINE = "2026-06-17"
def recency_w(rec):
    ts = (rec or {}).get("ts") or _TS_BASELINE
    try:
        d = datetime.date.fromisoformat(str(ts)[:10])
        age = max(0, (_TODAY - d).days)
        return 0.5 ** (age / RECENCY_HALF_LIFE)
    except Exception:
        return 0.5

def _vision_signals(records, pool):
    """Recency-weighted centroid of one swipe set's vision tags: per-axis category
    weight-sums (incl. pattern) + weighted-mean neutral/oldmoney. `records` is the
    liked/disliked dict (id -> record-with-ts)."""
    counts = {f: {} for f in VIS_CATS + ["pattern"]}
    neu, om, wsum = [], [], []
    for it in pool:
        rec = records.get(it["id"]) if isinstance(records, dict) else None
        if rec is not None and it.get("vision"):
            w = recency_w(rec) * float(rec.get("weight", 1.0) or 1.0)
            v = it["vision"]
            for f in counts:
                val = v.get(f)
                if val and val != "na":
                    counts[f][val] = counts[f].get(val, 0) + w
            try:
                neu.append(float(v["neutral"]) * w); om.append(float(v["oldmoney"]) * w); wsum.append(w)
            except (TypeError, ValueError): pass
    tw = sum(wsum)
    return (counts,
            (sum(neu) / tw if tw else None),
            (sum(om) / tw if tw else None))

# ---- learned feedback (from hearts/✕ exported to data/feedback.json) --------
fb = json.load(open(FEEDBACK)) if FEEDBACK.exists() else {}
liked = fb.get("liked", {}) or {}
disliked = fb.get("disliked", {}) or {}

# ---- Nuuly taste signal (worn rentals + saved closet) -----------------------
# Annabel's Nuuly history is strong real-world taste signal: a worn rental beats
# a feed heart (she paid to wear it a month); a closet save is about a normal
# like. tools/nuuly-cli pulls these to data/nuuly.json. We fold them in as
# synthetic, recency-weighted "likes" that feed the BRAND / CATEGORY / COLOUR
# signal — NOT the vision centroid (these items aren't in the scraped pool) and
# NOT the buy feed (they're rentals, not shoppable here). Per Annabel: rental
# ~1.75x a like, closet = a normal like. Rentals carry their real rental date so
# recency applies; closet has no date, so it sits at the legacy baseline.
NUULY = ROOT / "data" / "nuuly.json"
NUULY_RENTAL_WEIGHT = 2.0
NUULY_CLOSET_WEIGHT = 1.25
nuuly_likes = {}
nuuly_pool = []          # {id, img, vision} — Nuuly's own pool (not in the scraped feed)
n_nuuly_rental = n_nuuly_closet = 0
if NUULY.exists():
    _nu = json.load(open(NUULY))
    def _nu_record(x, weight, ts):
        cats = classify((x.get("brand") or ""), (x.get("name") or "")) or []
        return {"brand": (x.get("brand") or "").strip(), "cats": " ".join(cats),
                "ts": ts, "weight": weight, "src": x.get("signal")}
    for x in (_nu.get("rental_history") or []):
        nid = "nuuly:" + str(x.get("id"))
        nuuly_likes[nid] = _nu_record(x, NUULY_RENTAL_WEIGHT, x.get("date") or _TS_BASELINE)
        nuuly_pool.append({"id": nid, "img": (x.get("img") or "").strip()})
        n_nuuly_rental += 1
    for x in (_nu.get("closet") or []):
        nid = "nuuly:" + str(x.get("id"))
        if nid in nuuly_likes:            # already rented → keep the stronger rental vote
            continue
        nuuly_likes[nid] = _nu_record(x, NUULY_CLOSET_WEIGHT, _TS_BASELINE)
        nuuly_pool.append({"id": nid, "img": (x.get("img") or "").strip()})
        n_nuuly_closet += 1

# Email purchases = the STRONGEST owned signal. She paid for + kept these, so a
# purchase outweighs a rental, and the real order date means a fresh buy (this
# month's Zara shorts) dominates recency. Folded into the SAME owned pool as Nuuly
# so all the centroid / vision / base-prior machinery picks them up for free; only
# the weight and the why-string differ. `purchase_brands` lets nuuly_adjust say
# "you recently bought X" instead of the Nuuly phrasing for these brands.
PURCHASES = ROOT / "data" / "purchases.json"
PURCHASE_WEIGHT = 2.5
n_purchase = 0
purchase_brands = set()
if PURCHASES.exists():
    for x in (json.load(open(PURCHASES)).get("purchases") or []):
        pid = "buy:" + str(x.get("id"))
        if pid in nuuly_likes:
            continue
        nuuly_likes[pid] = _nu_record(x, PURCHASE_WEIGHT, x.get("date") or _TS_BASELINE)
        nuuly_pool.append({"id": pid, "img": (x.get("img") or "").strip()})
        b = (x.get("brand") or "").lower().strip()
        if b:
            purchase_brands.add(b)
        n_purchase += 1

# Taste signal = real swipes + Nuuly. `liked` stays PURE (real swipes only) for
# exact-match pinning, the buy feed, and the profile love-count; `taste_liked`
# is the merged set that drives the brand/category/colour signal.
taste_liked = {**nuuly_likes, **liked}

# ---- manual taste overrides (Annabel can edit data/style-overrides.json) -----
# A direct lever on top of learned taste: "boost" terms (brand or word) lift any
# matching item; "hide" terms bury it. Case-insensitive substring match on brand
# + title. Lets her correct the model by hand when it's wrong, no swiping needed.
OVERRIDES = ROOT / "data" / "style-overrides.json"
if not OVERRIDES.exists():
    json.dump({"boost": [], "hide": []}, open(OVERRIDES, "w"), indent=2)
_ov = json.load(open(OVERRIDES))
OV_BOOST = [t.lower() for t in (_ov.get("boost") or []) if t.strip()]
OV_HIDE  = [t.lower() for t in (_ov.get("hide")  or []) if t.strip()]
def override_adjust(it):
    text = (it["brand"] + " " + it["title"]).lower()
    if any(t in text for t in OV_HIDE):  return -100, "Hidden by your override"
    if any(t in text for t in OV_BOOST): return  30,  "Boosted by your override"
    return 0, None

def _signals(d):
    """Recency-weighted brand/category weight-sums + weighted colour mean."""
    brands, cats, cols, colw = {}, {}, [], []
    for v in d.values():
        w = recency_w(v) * float(v.get("weight", 1.0) or 1.0)
        b = (v.get("brand") or "").lower().strip()
        if b: brands[b] = brands.get(b, 0) + w
        for c in (v.get("cats") or "").split():
            cats[c] = cats.get(c, 0) + w
        try:
            cv = v.get("c")
            if cv not in (None, ""): cols.append(float(cv) * w); colw.append(w)
        except (TypeError, ValueError):
            pass
    return brands, cats, cols, colw

L_brand, L_cat, L_col, L_colw = _signals(taste_liked)
D_brand, D_cat, D_col, _ = _signals(disliked)
_lcm = sum(L_col) / sum(L_colw) if L_colw else None

# Nuuly as a STATIC taste prior baked into the cold `base` score. Both browser
# views (quick-choose + feed) re-rank live from `base` + the live swipe profile
# they recompute from localStorage — they can't see Nuuly (it isn't a swipe), so
# the Nuuly signal would never reach the ranking Annabel sees unless it lives in
# `base`. It's a fixed prior, not live feedback, so baking it in is correct: her
# swipes still layer on top and can flip it. Positive-only (a worn rental/closet
# save is interest, never a dislike). Drawn from nuuly_likes ALONE so real-swipe
# feedback stays out of base (the browser owns that, live).
N_brand, N_cat, N_col, N_colw = _signals(nuuly_likes)
_ncm = sum(N_col) / sum(N_colw) if N_colw else None
def nuuly_adjust(it):
    if not nuuly_likes: return 0, None
    b = it["brand"].lower(); cats = it.get("cats", [])
    adj = 0.0; why = None
    nb = N_brand.get(b, 0)
    if nb > 0:
        adj += min(14, 7 * nb)
        why = (f"You recently bought {it['brand']}" if b in purchase_brands
               else f"You wear {it['brand']} on Nuuly")
    net = sum(N_cat.get(c, 0) for c in cats)
    if net > 0: adj += min(10, 3 * net)
    c = it.get("colorfulness")
    if c is not None and _ncm is not None and abs(c - _ncm) < .08: adj += 4
    return round(adj), why

def feedback_adjust(it):
    why, adj = None, 0
    b = it["brand"].lower(); cats = it.get("cats", [])
    nb = L_brand.get(b, 0) - D_brand.get(b, 0)   # net, recency-weighted brand signal
    if nb > 0:   adj += min(11, 7 * nb); why = f"You like {it['brand']}"
    elif nb < 0: adj += max(-15, 9 * nb); why = f"Not your usual {it['brand']}"
    net = sum(L_cat.get(c, 0) for c in cats) - sum(D_cat.get(c, 0) for c in cats)
    adj += max(-14, min(12, (6 if net < 0 else 4) * net))
    for c in cats:                       # a category she (recently) only ever passes on
        if D_cat.get(c, 0) >= 1.5 and L_cat.get(c, 0) < 0.4:
            adj -= 20; why = "You keep passing these"
    c = it.get("colorfulness")
    if c is not None and _lcm is not None and abs(c - _lcm) < .08: adj += 6
    return round(adj), why

# ---- build: filter + merge --------------------------------------------------
merged = {}; dropped_cat = 0
def _ingest(name, path, is_brand):
    """Load one source/brand file and merge its products into `merged`. Tracks
    creator backing and brand backing separately so brand catalogs can be
    trimmed later while creator-picked items are always kept."""
    global dropped_cat
    prods = load_products(path)
    RAW.mkdir(parents=True, exist_ok=True)
    json.dump(prods, open(RAW/(re.sub(r"\W+","",name.lower())+".json"),"w"), indent=2)
    for p in prods:
        title=(p.get("title") or "").strip(); brand=(p.get("brand") or "").strip(); img=(p.get("imageUrl") or "").strip()
        if not title or not img: continue
        cats = classify(brand, title)
        if cats is None: dropped_cat += 1; continue
        key = re.sub(r"\W+","",f"{brand}{title}".lower())[:60]
        if key in merged:
            (merged[key]["brands"] if is_brand else merged[key]["creators"]).add(name)
        else:
            s, why = text_score(p)
            merged[key] = {**p, "id":key, "brand":brand, "title":title, "imageUrl":img,
                           "tscore":s, "why":why, "cats":cats,
                           "creators": (set() if is_brand else {name}),
                           "brands":   ({name} if is_brand else set())}

for creator, path in SOURCES: _ingest(creator, path, False)
for brand, path in BRANDS:    _ingest(brand, path, True)

# ---- image-only sources: her Pinterest inspiration + her closet -------------
# These aren't titled retail products, so they bypass title-classify. Pinterest
# pins are whole LOOKS (own "inspiration" cat, vision-tagged in the normal pass).
# Closet pieces already carry tags (data/closet.json), so they skip the vision API
# and map straight in. Both render + react like any card, so a ♥/✕ on them trains
# the SAME feedback.json the morning debrief reads.
def _add_look(key, img, *, cats, source, title="", price="", url="", brand="", tags=None):
    if not img or key in merged: return False
    s, why = text_score({"brand": brand, "title": title})
    merged[key] = {"id": key, "brand": brand, "title": title, "imageUrl": img,
                   "price": price, "productUrl": url, "tscore": s, "why": why,
                   "cats": cats, "creators": {source}, "brands": set(),
                   "_tags": tags}          # reapplied after the vision pass (which nulls vision)
    return True

PINT = ROOT / "data" / "pinterest" / "clothes.json"
n_pins = sum(_add_look("pin_" + str(p.get("id", "")), (p.get("img") or "").strip(),
                       cats=["inspiration"], source="Pinterest",
                       title=(p.get("title") or "").strip(), url=(p.get("link") or ""))
             for p in (json.load(open(PINT)) if PINT.exists() else []))

# closet slot -> feed category; items get their category tab AND a "closet" tab
SLOT_CAT = {"top": "top", "knit": "knit", "sweater": "knit", "bottom": "bottom",
            "pant": "bottom", "jean": "bottom", "skirt": "bottom", "dress": "dress",
            "outerwear": "outerwear", "jacket": "outerwear", "coat": "outerwear",
            "shoe": "shoe", "bag": "bag", "accessory": "accessory", "swim": "swim"}
def _closet_vision(t):                      # her short tag keys -> the vision schema card() reads
    if not t: return None
    return {"garment": True, "silhouette": t.get("sil"), "length": t.get("len"),
            "fabric": t.get("fab"), "drape": t.get("drp"), "formality": t.get("form"),
            "neutral": t.get("neut"), "oldmoney": t.get("om")}
CLOSET = ROOT / "data" / "closet.json"
_cj = json.load(open(CLOSET)) if CLOSET.exists() else {}
n_closet = sum(_add_look("closet_" + str(p.get("id") or i), (p.get("img") or "").strip(),
                         cats=[SLOT_CAT.get((p.get("slot") or "").lower(), "top"), "closet"],
                         source="Closet", title=(p.get("name") or "").strip(),
                         brand=(p.get("brand") or "").strip(), tags=_closet_vision(p.get("tags")))
               for i, p in enumerate(_cj.get("pieces") or []))
print(f"image-only sources: pinterest={n_pins}  closet={n_closet}")

items = list(merged.values())

# drop products whose photo is shared by another product: the source scrape
# sometimes pins one image to several titles (a lazy-load mismatch), e.g. a
# "Mini Dress" showing leggings. The title<->image pairing can't be trusted, so
# drop all of them rather than show a wrong picture.
_imgc = {}
for it in items: _imgc[it["imageUrl"]] = _imgc.get(it["imageUrl"], 0) + 1
dropped_dupe_img = sum(1 for it in items if _imgc[it["imageUrl"]] > 1)
items = [it for it in items if _imgc[it["imageUrl"]] == 1]

# ---- colour pass (threaded, cached) — also the image-load / broken check ----
urls = [it["imageUrl"] for it in items]
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
    list(ex.map(colorfulness, urls))
json.dump(color_cache, open(CACHE,"w"))
for it in items:
    it["colorfulness"] = color_cache.get(it["imageUrl"])
    it["vision"] = None

# Only keep pieces whose image actually loads (failed fetch == blocked hotlink),
# then vision-tag the survivors — no point spending a vision call on a dead image.
broken = [it for it in items if it["colorfulness"] is None]
items = [it for it in items if it["colorfulness"] is not None]

# ---- AI-vision pass (threaded, cached) — wearables only ---------------------
# Beauty/home stay on the saturation heuristic; silhouette is meaningless there.
vision_targets = [it for it in items if "beauty" not in it["cats"] and "home" not in it["cats"]]
n_vision = 0
if VISION_ON and vision_targets:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        list(ex.map(vision_tag, [it["imageUrl"] for it in vision_targets]))
    json.dump(vision_cache, open(VCACHE, "w"))
    for it in vision_targets:
        it["vision"] = vision_cache.get(it["imageUrl"])
    n_vision = sum(1 for it in vision_targets if it.get("vision"))

# closet pieces ship their own tags — restore them over the null the color pass set.
for it in items:
    if it.get("_tags"): it["vision"] = it["_tags"]

# Back-detail backfill: items vision-tagged before the `back` axis existed lack it.
# Only tops/dresses/knits/outerwear are worth checking (a back is meaningless on a
# shoe/bag/trouser). One cheap call each, merged into the vision cache so it's a
# one-time cost — subsequent builds and new items (tagged by the main pass) skip it.
BACK_CATS = {"top", "dress", "knit", "outerwear"}
back_targets = [it for it in vision_targets
                if it.get("vision") and it["vision"].get("garment", True)
                and it["vision"].get("back") in (None, "")
                and any(c in BACK_CATS for c in it["cats"])]
n_back = 0
if VISION_ON and back_targets:
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        tags = list(ex.map(back_tag, [it["imageUrl"] for it in back_targets]))
    for it, tag in zip(back_targets, tags):
        if tag:
            it["vision"]["back"] = tag
            vision_cache[it["imageUrl"]]["back"] = tag   # persist into the cache entry
            n_back += 1
    json.dump(vision_cache, open(VCACHE, "w"))

# Vision-tag the Nuuly items in their OWN pool (they aren't in the scraped feed)
# so her worn rentals + closet shape the VISION centroid — silhouette, formality,
# fabric, neckline, drape, palette — the richest taste signal, not just brand.
# scene7 images hotlink and nuuly-cli forces ?fmt=jpeg, so vision_tag fetches by
# URL; cached in vision_cache.json by URL, so this is a one-time cost.
n_nuuly_vision = 0
if VISION_ON and nuuly_pool:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        list(ex.map(vision_tag, [p["img"] for p in nuuly_pool if p.get("img")]))
    json.dump(vision_cache, open(VCACHE, "w"))
    for p in nuuly_pool:
        p["vision"] = vision_cache.get(p["img"])
    n_nuuly_vision = sum(1 for p in nuuly_pool if p.get("vision"))

# Recency-weighted centroids of what she's swiped, in vision space. Nuuly is
# folded into the LIKED centroid (one combined call over swipes + Nuuly's pool,
# weighted by each record's rental/closet weight) so the server score + the style
# profile reflect her real-world vision taste, not just her swipes.
Lcounts, Lneu, Lom = _vision_signals({**liked, **nuuly_likes}, items + nuuly_pool)
Dcounts, Dneu, Dom = _vision_signals(disliked, items)

# Nuuly-ONLY vision centroid + a positive-only prior baked into `base` (the cold
# score both browsers re-rank on). The merge above only reaches the server score;
# `base` is where the ranking Annabel actually sees is built, and the browser
# can't recompute Nuuly (it isn't a localStorage swipe), so it must live here.
# Dialed back (0.6x, capped) so it nudges rather than swamping her 292 real swipes.
Ncounts, Nneu, Nom = _vision_signals(nuuly_likes, nuuly_pool)
# Per-axis weight totals → the prior rewards how TYPICAL an item is of her Nuuly
# taste (the centroid SHARE on each axis), not just "shares any common value".
# A raw capped reward saturates (a dense 147-item centroid maxes every axis), so
# the boost would be a near-flat shift that doesn't re-rank. Share-weighting makes
# it discriminate: relaxed+knit+midi (her Nuuly modes) scores high, bodycon+satin
# +mini scores low. lc is the axis's importance (silhouette > neckline).
_Ntot = {f: sum(Ncounts[f].values()) for f in VIS_WEIGHTS}
NUULY_VIS_SCALE, NUULY_VIS_CAP = 0.8, 24
def nuuly_vision_adjust(it):
    if not nuuly_pool: return 0
    v = it.get("vision")
    if not v or not v.get("garment", True): return 0
    adj = 0.0
    for f, (lc, _lpc, _dc, _dpc) in VIS_WEIGHTS.items():
        val = v.get(f); tot = _Ntot.get(f, 0)
        if not val or val == "na" or not tot: continue
        adj += lc * (Ncounts[f].get(val, 0) / tot)    # axis importance × Nuuly-typicality
    if Nneu is not None:
        try: adj += 5 * (1 - 2 * abs(float(v["neutral"]) - Nneu))   # palette proximity, ±5
        except (TypeError, ValueError): pass
    return round(min(NUULY_VIS_CAP, adj * NUULY_VIS_SCALE))

def vision_adjust(it):
    """Score an item against the liked centroid across all categorical axes
    (cut, formality, neckline, sleeve, length, fabric, drape) + pattern +
    quiet-luxury and palette alignment. Replaces saturation for tagged
    wearables."""
    v = it.get("vision")
    if not v or not v.get("garment", True):
        return 0, None
    adj = 0.0; why = None
    for f, (lc, lpc, dc, dpc) in VIS_WEIGHTS.items():
        val = v.get(f)
        if not val or val == "na": continue
        lk, dk = Lcounts[f].get(val, 0), Dcounts[f].get(val, 0)
        if lk:
            adj += min(lc, lpc * lk)
            if f == "back" and val not in ("closed", "na") and why is None:
                why = f"{val.replace('-', ' ')}, like the pieces you save"
            elif f == "silhouette" and why is None:
                why = f"{val.replace('-', ' ')} cut, like your saved pieces"
        if dk: adj -= min(dc, dpc * dk)
    p = v.get("pattern")                                    # asymmetric: only penalise
    if p and p != "na" and Dcounts["pattern"].get(p) and not Lcounts["pattern"].get(p): adj -= 8
    try: adj += 10 * (float(v["oldmoney"]) - 0.5)          # quiet-luxury reward, ±5
    except (TypeError, ValueError): pass
    if Lneu is not None:
        try: adj += 5 * (1 - 2 * abs(float(v["neutral"]) - Lneu))   # palette proximity, ±5
        except (TypeError, ValueError): pass
    if why is None and adj > 6: why = "Quiet, neutral palette like your taste"
    return round(adj), why

for it in items:
    if it.get("vision"):
        va, vwhy = vision_adjust(it)
        it["score"] = max(0, min(100, it["tscore"] + va))
        if vwhy: it["why"].insert(0, vwhy)
    else:
        it["score"] = max(0, min(100, it["tscore"] + color_adjust(it["colorfulness"], it["why"])))
    srcs = it["creators"] | it["brands"]
    if len(srcs) >= 2:
        it["score"] = min(100, it["score"] + 14)
        it["why"].insert(0, "Co-signed by " + " + ".join(sorted(srcs)))

# Cold, feedback-independent baseline emitted as data-base for the in-browser
# live rerank. The browser recomputes the feedback + centroid terms on top of
# this from the live swipe state, so taste adapts on every heart/✕ with no
# rebuild (see SCRIPT). Only the terms that don't depend on liked/disliked sets
# belong here: tscore, the quiet-luxury (oldmoney) reward, colour for untagged
# items, and the co-sign bonus.
for it in items:
    v = it.get("vision")
    if v and v.get("garment", True):
        cold = 0.0
        try: cold += 10 * (float(v["oldmoney"]) - 0.5)
        except (TypeError, ValueError): pass
        b = max(0, min(100, it["tscore"] + round(cold)))
    elif v:
        b = max(0, min(100, it["tscore"]))
    else:
        b = max(0, min(100, it["tscore"] + color_adjust(it["colorfulness"], [])))
    if len(it["creators"] | it["brands"]) >= 2:
        b = min(100, b + 14)
    na, nawhy = nuuly_adjust(it)
    nva = nuuly_vision_adjust(it)
    if na or nva:
        b = max(0, min(100, b + na + nva))
        if nawhy: it["why"].append(nawhy)
    it["base"] = b

# ---- NUULY tuning probe (NUULY_PROBE=1) -------------------------------------
# Confirms the Nuuly prior still DISCRIMINATES (on-taste >> off-taste) and hasn't
# re-saturated at the cap after a knob change. Two synthetic archetypes: her Nuuly
# mode (relaxed knit, neutral) vs off-taste (bodycon satin, vivid). Run before and
# after any NUULY_* edit; the on-vs-off GAP must stay wide and cap-hit % stay low.
if os.environ.get("NUULY_PROBE"):
    def _probe_item(brand, cats, colorf, vis):
        return {"brand": brand, "cats": cats, "colorfulness": colorf, "vision": vis}
    _on = _probe_item("Reformation", ["top"], (_ncm or .25), {
        "garment": True, "silhouette": "relaxed", "formality": "casual",
        "neckline": "crew", "sleeve": "long", "length": "midi", "fabric": "knit",
        "drape": "fluid", "back": "closed", "neutral": (Nneu or .8)})
    _off = _probe_item("Naked Wardrobe", ["dress"], 0.85, {
        "garment": True, "silhouette": "bodycon", "formality": "going-out",
        "neckline": "halter", "sleeve": "sleeveless", "length": "mini",
        "fabric": "satin", "drape": "structured", "back": "open", "neutral": 0.15})
    on_na, _ = nuuly_adjust(_on); on_nva = nuuly_vision_adjust(_on)
    off_na, _ = nuuly_adjust(_off); off_nva = nuuly_vision_adjust(_off)
    _nvas = [nuuly_vision_adjust(it) for it in items if it.get("vision")]
    _atcap = sum(1 for x in _nvas if x >= NUULY_VIS_CAP)
    _mean = sum(_nvas) / len(_nvas) if _nvas else 0
    print(f"[NUULY PROBE] SCALE={NUULY_VIS_SCALE} CAP={NUULY_VIS_CAP} "
          f"RENTAL_W={NUULY_RENTAL_WEIGHT}")
    print(f"  ON  (relaxed knit) : brand+cat={on_na:+d}  vision={on_nva:+d}  "
          f"total Nuuly lift={on_na+on_nva:+d}")
    print(f"  OFF (bodycon satin): brand+cat={off_na:+d}  vision={off_nva:+d}  "
          f"total Nuuly lift={off_na+off_nva:+d}")
    print(f"  GAP (on - off vision) = {on_nva-off_nva:+d}   "
          f"(wider = more discrimination)")
    print(f"  saturation: {_atcap}/{len(_nvas)} ({100*_atcap/max(1,len(_nvas)):.0f}%) "
          f"at cap; mean vision lift = {_mean:.1f}")
    import sys as _sys; _sys.exit(0)

# apply learned feedback: adjust, pin exact likes, drop exact dislikes
if liked or disliked:
    for it in items:
        fa, fwhy = feedback_adjust(it)
        if fa: it["score"] = max(0, min(100, it["score"] + fa))
        if fwhy: it["why"].insert(0, fwhy)
    for it in items:
        if it["id"] in liked:
            it["score"] = min(100, it["score"] + 16); it["why"].insert(0, "You loved this")

# manual overrides last, so they win over learned taste
if OV_BOOST or OV_HIDE:
    for it in items:
        oa, owhy = override_adjust(it)
        if oa:
            it["score"] = max(0, min(100, it["score"] + oa))
            if owhy: it["why"].insert(0, owhy)

items.sort(key=lambda x: x["score"], reverse=True)

# ---- curate brand catalogs --------------------------------------------------
# Creator items are hand-picked → keep all. Brand-catalog items are a full,
# mostly off-taste catalog → keep only the top BRAND_KEEP per brand that also
# clear BRAND_MIN_SCORE, i.e. only the pieces that score as her taste.
from collections import defaultdict
_bkept = defaultdict(int); _curated = []; _bdropped = 0
for it in items:                              # already score-sorted desc
    if it["creators"]:                        # any real creator backing → keep
        _curated.append(it); continue
    b = next(iter(it["brands"]), None)
    if b is None:
        _curated.append(it); continue
    if it["score"] >= BRAND_MIN_SCORE and _bkept[b] < BRAND_KEEP:
        _bkept[b] += 1; _curated.append(it)
    else:
        _bdropped += 1
items = _curated

# ---- retailer-link pass (threaded, cached) ----------------------------------
prod_urls = [it.get("productUrl") for it in items if it.get("productUrl")]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    list(ex.map(resolve_link, prod_urls))
json.dump(link_cache, open(LINK_CACHE, "w"))
for it in items:
    it["shopUrl"] = link_cache.get(it.get("productUrl")) or it.get("productUrl")
n_links = sum(1 for it in items if link_cache.get(it.get("productUrl")))

# ---- render -----------------------------------------------------------------
_TODAY = datetime.date.today()
def _is_new(it):
    """True if first_seen is set and within NEW_DAYS. Legacy items (no first_seen,
    e.g. the original brand catalogs) are never flagged."""
    fs = it.get("first_seen")
    if not fs:
        return False
    try:
        return (_TODAY - datetime.date.fromisoformat(str(fs)[:10])).days <= NEW_DAYS
    except ValueError:
        return False

# ---- occasion / use-case tags ----------------------------------------------
# Orthogonal to garment category (what it IS): occasion answers WHEN you'd wear
# it, so the feed can answer "show me work clothes". Derived from the AI vision
# formality axis (primary signal) + fabric/silhouette + title keywords + brand.
# An item can carry several (a tailored trouser is work + casual). Athleisure
# brands and active keywords force "active" and block "work".
ATHLEISURE = {"lululemon", "alo", "alo yoga", "varley", "set active", "vuori",
              "beyond yoga", "outdoor voices", "bandier"}
ACTIVE_RE = re.compile(r"\b(legging|sports? ?bra|bike ?short|yoga|jogger|sweatpant|"
    r"track ?(?:pant|suit)|tennis|golf|active|athletic|workout|gym|run(?:ning)?|crew sock|"
    r"scrunch|performance|seamless|ribbed tank|sports? top)\b", re.I)
# Dresses that bare the shoulders / hang on thin straps are occasion/evening pieces,
# never workwear — used to keep sundresses and slip dresses out of the "work" bucket.
NOT_WORK_DRESS = re.compile(r"\bstrapless|spaghetti|\bcami\b|slip dress|sun ?dress|nap dress|tube\b", re.I)
# Sleepwear is loungewear, not an occasion — and print words ("Tennis Club" PJs)
# must not pull it into Active. Sleepwear gets no occasion bucket at all.
SLEEP_RE = re.compile(r"\b(?:pajamas?|pyjamas?|pj|sleep ?(?:set|wear|shirt|pant|short|gown|tee)?|"
    r"nightgowns?|nighties?|nightshirts?|loungewear)\b", re.I)
WORK_RE = re.compile(r"\b(blazer|trouser|tailored|suit|slack|button.?up|button.?down|"
    r"oxford|poplin|sheath|pencil|ponte|crepe|loafer|pump|collared|cardigan|waistcoat|"
    r"wide.?leg|straight.?leg|column|midi skirt|knit (?:top|polo|vest))\b", re.I)
GOINGOUT_RE = re.compile(r"\b(slip dress|mini dress|sequin|satin|corset|bodycon|cocktail|"
    r"going.?out|party|halter|cut.?out|cutout|backless|strapless|bustier|stiletto|gown|"
    r"bustier|rhinestone|metallic)\b", re.I)
VACATION_RE = re.compile(r"\b(linen|crochet|cover.?up|coverup|resort|beach|raffia|straw|"
    r"kaftan|caftan|sarong|cabana|vacation|sundress|espadrille|poolside|eyelet|gauze)\b", re.I)
CASUAL_RE = re.compile(r"\b(jean|denim|tee|t-shirt|sweater|sweatshirt|sneaker|flat|short|"
    r"cargo|chino|henley|flannel|everyday|relaxed|fleece|hoodie|crew(?:neck)?)\b", re.I)

def occasions_of(it):
    """Return the use-case buckets this item fits, from the small fixed set
    [work, casual, going-out, active, vacation]. Empty is allowed."""
    title = it.get("title", "")
    brand = (it.get("brand") or "").lower()
    cats = it.get("cats", [])
    v = it.get("vision") or {}
    form = v.get("formality") if v.get("garment", True) else None
    fab, sil = v.get("fabric"), v.get("silhouette")
    if SLEEP_RE.search(title):                               # PJs/sleepwear: no occasion
        return []
    neck, slv = v.get("neckline"), v.get("sleeve")
    occ = set()
    # Active = athletic only. Loungewear/PJs are NOT active (that was putting sleep
    # sets in the Active bucket), so don't trigger on the loungewear formality.
    is_active = brand in ATHLEISURE or bool(ACTIVE_RE.search(title))
    if is_active:
        occ.add("active")
    if "swim" not in cats and not is_active:                  # work: dressy, not gym, not pool
        bare_dress = "dress" in cats and (
            neck in ("strapless", "off-shoulder", "halter") or slv == "strappy"
            or NOT_WORK_DRESS.search(title))
        if not bare_dress and (form in ("smart-casual", "formal") or WORK_RE.search(title)):
            occ.add("work")
    # Going out: dressy occasion-wear. Swimwear is never going-out even though the
    # tagger reads swimsuits as "bodycon", so exclude swim and only let bodycon
    # imply going-out for actual dresses.
    if "swim" not in cats and (form in ("formal", "evening")
            or GOINGOUT_RE.search(title) or (sil == "bodycon" and "dress" in cats)):
        occ.add("going-out")
    if "swim" in cats or fab == "linen" or VACATION_RE.search(title):
        occ.add("vacation")
    if form in ("casual", "smart-casual") or CASUAL_RE.search(title):
        occ.add("casual")
    return sorted(occ)

# ---- styling pass: "goes with / more like your new <purchase>" --------------
# Annabel's actual ask: don't just rank by taste — when she buys something, surface
# things that COMPLETE THE OUTFIT around it (a top + sandals for her new Zara
# shorts) and MORE LIKE IT (other casual summer shorts). Driven by the specific
# recent purchases, not the aggregate centroid, so the reason is concrete and the
# boost is fresh. Same-category match => "more like"; complementary category with a
# compatible occasion + palette => "goes with". One reason per item, recency-scaled.
COMPLEMENT = {
    "bottom":    {"top", "knit", "outerwear", "shoe", "bag", "accessory"},
    "top":       {"bottom", "outerwear", "shoe", "bag", "accessory"},
    "knit":      {"bottom", "outerwear", "shoe", "bag", "accessory"},
    "dress":     {"outerwear", "shoe", "bag", "accessory"},
    "outerwear": {"top", "knit", "bottom", "dress", "shoe", "bag"},
    "shoe":      {"bottom", "top", "dress", "knit", "bag"},
    "bag":       {"bottom", "top", "dress", "knit", "shoe"},
    "accessory": {"bottom", "top", "dress", "knit", "shoe"},
    "swim":      {"outerwear", "bag", "accessory", "shoe"},
}
_pool_vision = {p["id"]: p.get("vision") for p in nuuly_pool}
recent_buys = []
if PURCHASES.exists():
    for x in (json.load(open(PURCHASES)).get("purchases") or []):
        try:
            age = (_TODAY - datetime.date.fromisoformat((x.get("date") or "")[:10])).days
        except ValueError:
            continue
        if age > 90:                       # only genuinely recent buys earn "your new X"
            continue
        bcats = set(classify((x.get("brand") or ""), (x.get("name") or "")) or [])
        bvis = _pool_vision.get("buy:" + str(x.get("id"))) or {}
        bocc = set(occasions_of({"title": x.get("name", ""), "brand": x.get("brand", ""),
                                 "cats": list(bcats), "vision": bvis}))
        recent_buys.append({"brand": (x.get("brand") or "").strip(), "name": (x.get("name") or "").strip(),
                            "cats": bcats, "occ": bocc, "neut": bvis.get("neutral"),
                            "w": 0.5 ** (age / 45.0)})
    recent_buys.sort(key=lambda b: b["w"], reverse=True)

def _palette_close(it, b):
    """0..1 palette closeness (neutral axis); None when either side is untagged."""
    n1, n2 = (it.get("vision") or {}).get("neutral"), b.get("neut")
    try:
        return max(0.0, 1 - abs(float(n1) - float(n2)))
    except (TypeError, ValueError):
        return None

# Only the few freshest buys earn styling callouts, so the feed isn't blanketed.
_STYLE_BUYS = recent_buys[:6]

def styling_match(it):
    """Strongest recent-buy styling tie: (kind, label, weight, score) or None.
    'more' = same category + close palette (another piece like the one she bought).
    'goes' = complementary category + a SHARED occasion + close palette + on-taste
    (something to wear with it). 'goes' is gated hard so it stays a real suggestion."""
    icats = set(it.get("cats", []))
    if not icats:
        return None
    iocc = set(occasions_of(it))
    best = None
    for b in _STYLE_BUYS:
        pc = _palette_close(it, b)
        if icats & b["cats"]:                              # same category → more like this
            if pc is not None and pc < 0.6:                # tagged but off-palette → skip
                continue
            sc = ((pc if pc is not None else 0.7) + 0.35) * b["w"] * 1.4
            cand = ("more", b, sc)
        elif (iocc & b["occ"] and (pc is None or pc >= 0.75)
              and it.get("base", it["score"]) >= 58        # only pair on-taste pieces
              and any(ic in COMPLEMENT.get(bc, ()) for bc in b["cats"] for ic in icats)):
            sc = (pc if pc is not None else 0.82) * b["w"]
            cand = ("goes", b, sc)
        else:
            continue
        if best is None or cand[2] > best[2]:
            best = cand
    if best is None:
        return None
    kind, b, sc = best
    return kind, f"{b['brand']} {b['name'].lower()}".strip(), b["w"], sc

# Collect candidates, then tag only the strongest per kind so callouts stay curated.
# "goes with" is the headline ask (what to pair with a new buy), so it gets its own
# reserved budget rather than being crowded out by the higher-scoring "more like".
GOES_CAP, MORE_CAP = 110, 80
_cands = []
if _STYLE_BUYS:
    for it in items:
        m = styling_match(it)
        if m:
            _cands.append((it, *m))
_cands.sort(key=lambda c: c[4], reverse=True)
# Spread callouts across the different recent buys (and, for "goes with", across
# categories) so the feed shows pairings for several purchases — not 28 cardigans
# for one pair of shorts.
from collections import Counter as _Counter
_kept, _seen_goes, _seen_more = [], 0, 0
_goes_label, _goes_label_cat, _more_label = _Counter(), _Counter(), _Counter()
for it, kind, label, w, sc in _cands:
    if kind == "goes":
        cat = (it.get("cats") or ["?"])[0]
        if (_seen_goes < GOES_CAP and _goes_label[label] < 24
                and _goes_label_cat[(label, cat)] < 8):
            _kept.append((it, kind, label, w, sc)); _seen_goes += 1
            _goes_label[label] += 1; _goes_label_cat[(label, cat)] += 1
    elif _seen_more < MORE_CAP and _more_label[label] < 24:
        _kept.append((it, kind, label, w, sc)); _seen_more += 1
        _more_label[label] += 1
n_styled = n_goes = 0
for it, kind, label, w, sc in _kept:
    boost = round((6 if kind == "more" else 5) * w)
    if not boost:
        continue
    it["base"] = max(0, min(100, it.get("base", it["score"]) + boost))
    it["score"] = max(0, min(100, it["score"] + boost))
    reason = (f"More like your new {label}" if kind == "more"
              else f"Goes with your new {label}")
    if it["why"] and it["why"][0] == "You loved this":
        it["why"].insert(1, reason)                        # never bury an exact love
    else:
        it["why"].insert(0, reason)
    n_styled += 1
    n_goes += (kind == "goes")
if n_styled:
    items.sort(key=lambda x: x["score"], reverse=True)     # re-sort: boosts changed order
print(f"styling: {n_styled} items tagged ({n_goes} 'goes with', {n_styled - n_goes} 'more like') "
      f"from {len(_STYLE_BUYS)} recent buys")

def card(it):
    creators = " · ".join(sorted(it["creators"] | it["brands"]))
    why = it["why"][0] if it["why"] else "Matches your saved style"
    cats = " ".join(it.get("cats", []))
    c = it.get("colorfulness")
    cval = "" if c is None else c
    url = html.escape(it.get("shopUrl") or it.get("productUrl") or "#")
    # vision tags → card dataset, so the in-browser rerank can match cut + palette
    # live (mirrors vision_adjust). Empty when the image wasn't vision-tagged.
    v = it.get("vision") or {}
    is_garment = v.get("garment", True)
    def vtag(key):                       # blank for non-garments and "na" axes
        val = v.get(key, "") if is_garment else ""
        return html.escape("" if val in (None, "na") else val)
    sil, form = vtag("silhouette"), vtag("formality")
    neck, slv, length = vtag("neckline"), vtag("sleeve"), vtag("length")
    fab, drp, bk = vtag("fabric"), vtag("drape"), vtag("back")
    neut = v.get("neutral", "");  neut = "" if neut in (None, "") else round(float(neut), 3)
    om = v.get("oldmoney", "");   om = "" if om in (None, "") else round(float(om), 3)
    new_flag = _is_new(it)
    occ = html.escape(" ".join(occasions_of(it)))
    return f"""
    <article class="card" data-id="{html.escape(it['id'])}" data-brand="{html.escape(it['brand'].lower())}" data-creators="{html.escape(creators)}" data-cats="{html.escape(cats)}" data-occ="{occ}" data-new="{1 if new_flag else 0}" data-c="{cval}" data-sil="{sil}" data-form="{form}" data-neck="{neck}" data-slv="{slv}" data-len="{length}" data-fab="{fab}" data-drp="{drp}" data-bk="{bk}" data-neut="{neut}" data-om="{om}" data-score="{it['score']}" data-base="{it.get('base', it['score'])}">
      <div class="imgwrap">
        {'<span class="badge-new">New</span>' if new_flag else ''}
        <a class="imglink" href="{url}" target="_blank" rel="noopener"><img src="{html.escape(proxied_src(it['imageUrl']))}" alt="" loading="lazy"></a>
        <div class="acts">
          <button class="act dislike" type="button" data-act="dislike" aria-label="Not for me">&#10005;</button>
          <button class="act like" type="button" data-act="like" aria-label="Love it">&#9829;</button>
        </div>
      </div>
      <a class="meta" href="{url}" target="_blank" rel="noopener">
        <div class="row"><span class="brand">{html.escape(it['brand'])}</span></div>
        <div class="title">{html.escape(it['title'])}</div>
        <div class="price">{html.escape(it.get('price') or '—')}</div>
        <div class="why">{html.escape(why)}</div>
        <div class="src">{html.escape(creators)}</div>
      </a>
    </article>"""

cards = "\n".join(card(it) for it in items)

# ---- quick-choose data export ----------------------------------------------
# The bucket-first "quick choose" page (quickchoose.html) is hand-authored and
# data-driven: it loads this JSON, buckets items by occasion/category, and shows
# a one-at-a-time deck so Annabel decides fast instead of scrolling. Every field
# mirrors the data-* attrs the feed's card() emits, so a swipe there writes the
# SAME meta record under the SAME localStorage key ('theedit:v1') and POSTs to
# the SAME /feedback endpoint — the two views share one taste loop.
def _qc_item(it):
    v = it.get("vision") or {}
    is_garment = v.get("garment", True)
    def vtag(key):
        val = v.get(key, "") if is_garment else ""
        return "" if val in (None, "na") else val
    c = it.get("colorfulness")
    neut = v.get("neutral", "");  neut = "" if neut in (None, "") else round(float(neut), 3)
    om = v.get("oldmoney", "");   om = "" if om in (None, "") else round(float(om), 3)
    return {
        "id": it["id"],
        "brand": it["brand"],
        "title": it["title"],
        "price": it.get("price") or "",
        "img": proxied_src(it["imageUrl"]),
        "url": it.get("shopUrl") or it.get("productUrl") or "#",
        "score": it["score"],
        "base": it.get("base", it["score"]),
        "cats": it.get("cats", []),
        "occ": occasions_of(it),
        "why": it["why"][0] if it["why"] else "Matches your saved style",
        "new": 1 if _is_new(it) else 0,
        "creators": " · ".join(sorted(it["creators"] | it["brands"])),
        # meta mirror for info()/centroid learning
        "brand_l": it["brand"].lower(),
        "c": "" if c is None else c,
        "neut": neut, "om": om,
        "sil": vtag("silhouette"), "form": vtag("formality"),
        "neck": vtag("neckline"), "slv": vtag("sleeve"), "len": vtag("length"),
        "fab": vtag("fabric"), "drp": vtag("drape"), "bk": vtag("back"),
    }

_QC_SKIP = {"home", "beauty", "loungewear"}   # not outfit-buy buckets
_qc_items = [_qc_item(it) for it in items
             if not (_QC_SKIP & set(it.get("cats", [])))]
json.dump(_qc_items, open(ROOT / "data" / "items.json", "w"), indent=1)
print(f"  quick-choose: wrote {len(_qc_items)} items to data/items.json")

# ---- style-profile.md: a readable, regenerated mirror of learned taste -------
# So Annabel can SEE what the system currently believes her taste is, and watch
# it evolve. Recency-weighted, plus a "lately" view (last 21 days) vs the rest so
# a genuine shift is visible. Hand corrections go in data/style-overrides.json.
def _emit_style_profile():
    def topw(weights, n=8):
        return sorted(((k, v) for k, v in weights.items()), key=lambda kv: -kv[1])[:n]
    def axis_top(counts, axis, n=4):
        return topw(counts.get(axis, {}), n)
    def recent_brands(records, days):
        cut = _TODAY - datetime.timedelta(days=days)
        w = {}
        for r in records.values():
            try:
                if datetime.date.fromisoformat(str(r.get("ts", _TS_BASELINE))[:10]) >= cut:
                    b = (r.get("brand") or "").strip()
                    if b: w[b] = w.get(b, 0) + 1
            except Exception: pass
        return topw(w, 6)
    L = "".join(
        ["# The Edit — Style Profile\n\n",
         f"_Auto-generated {_TODAY.isoformat()} from {len(liked)} loves + {len(disliked)} passes._\n",
         "_This file is regenerated on every build. To correct the model by hand, "
         "edit `data/style-overrides.json` (boost / hide lists)._\n\n",
         "## Palette\n",
         f"- Neutrality lean: **{(Lneu if Lneu is not None else 0):.2f}** "
         "(1.0 = all white/cream/grey/black/navy, 0 = saturated colour)\n",
         f"- Quiet-luxury (old-money) lean of loves: **{(Lom if Lom is not None else 0):.2f}**\n\n",
         "## What you reach for (recency-weighted)\n",
         "**Top brands**\n",
         *[f"- {b} ({w:.1f})\n" for b, w in topw(L_brand)],
         "\n**Silhouettes** — " + ", ".join(f"{k} ({v:.1f})" for k, v in axis_top(Lcounts, "silhouette")) + "\n\n",
         "**Formality** — " + ", ".join(f"{k} ({v:.1f})" for k, v in axis_top(Lcounts, "formality")) + "\n\n",
         "**Fabrics** — " + ", ".join(f"{k} ({v:.1f})" for k, v in axis_top(Lcounts, "fabric")) + "\n\n",
         "## Lately (last 21 days)\n",
         "Brands you've been saving most recently:\n",
         *([f"- {b} ({c})\n" for b, c in recent_brands(liked, 21)] or ["- (no swipes in the last 21 days)\n"]),
         "\n## Recently bought (email orders)\n",
         f"_{n_purchase} items from order confirmations (weight {PURCHASE_WEIGHT:g}x — the strongest owned "
         "signal), newest first. These pull the feed toward what you're actually buying right now._\n",
         *([f"- {x.get('brand')} — {x.get('name')} ({x.get('date')})\n"
            for x in sorted((json.load(open(PURCHASES)).get("purchases") or []),
                            key=lambda r: r.get("date") or "", reverse=True)]
           if PURCHASES.exists() else ["- (no purchase data)\n"]),
         "\n## From Nuuly (worn rentals + closet)\n",
         f"_{n_nuuly_rental} worn rentals (weight {NUULY_RENTAL_WEIGHT:g}x) + {n_nuuly_closet} closet saves, "
         "folded into your brand & category taste._\n",
         *([f"- {b} ({w:.1f})\n" for b, w in topw(_signals({k: v for k, v in nuuly_likes.items()
                                                             if not k.startswith('buy:')})[0], 8)]
           or ["- (no Nuuly data — run nuuly-cli pull)\n"]),
         "\n## What you pass on\n",
         "**Brands** — " + (", ".join(b for b, _ in topw(D_brand, 6)) or "none yet") + "\n\n",
         "**Silhouettes** — " + (", ".join(f"{k}" for k, _ in axis_top(Dcounts, "silhouette")) or "none yet") + "\n",
        ])
    (ROOT / "style-profile.md").write_text(L)
    print("  wrote style-profile.md")
_emit_style_profile()

STYLE = '''
:root{--bg:#f3efe9;--ink:#1b1916;--muted:#7c756a;--line:#e0d9cd;--card:#faf8f4;--accent:#3a352d;--love:#b54b5a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Jost',system-ui,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased;display:flex;align-items:flex-start}
.side{position:sticky;top:0;height:100vh;flex:0 0 212px;width:212px;border-right:1px solid var(--line);background:var(--card);display:flex;flex-direction:column;padding:28px 16px 18px}
.side .mark{font-family:'Cormorant Garamond',serif;font-size:23px;letter-spacing:.16em;text-transform:uppercase;text-align:center;margin-bottom:3px}
.side .tag{font-size:9px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);text-align:center;margin-bottom:24px}
.side nav{display:flex;flex-direction:column;gap:1px;overflow-y:auto}
.tab{appearance:none;border:none;background:none;font-family:inherit;cursor:pointer;text-align:left;display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 12px;border-radius:8px;color:var(--muted);font-size:11.5px;letter-spacing:.15em;text-transform:uppercase}
.tab:hover{background:var(--bg);color:var(--ink)}
.tab.on{background:var(--accent);color:#fff}
.tab .n{font-size:10px;opacity:.6;font-variant-numeric:tabular-nums}
.tab.love{margin-top:10px;color:var(--love)}
.tab.love.on{background:var(--love);color:#fff}
.side-foot{margin-top:auto;padding-top:16px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:9px}
.toggle{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:6px;cursor:pointer}
.mini{appearance:none;border:1px solid var(--line);background:var(--bg);font-family:inherit;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);padding:7px 10px;border-radius:6px;cursor:pointer}
.mini:hover{color:var(--ink);border-color:var(--muted)}
main{flex:1;min-width:0}
.m-head{padding:42px 30px 22px;border-bottom:1px solid var(--line)}
.kicker{font-size:10px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);margin-bottom:11px}
.m-head h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(34px,5vw,60px);margin:0;letter-spacing:.01em}
.count{color:var(--muted);font-size:11px;letter-spacing:.2em;text-transform:uppercase;margin-top:12px}
.occbar{display:flex;flex-wrap:wrap;gap:8px;padding:20px 30px 0}
.chip{appearance:none;border:1px solid var(--line);background:var(--card);font-family:inherit;font-weight:300;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);padding:8px 15px;border-radius:999px;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:background .2s,color .2s,border-color .2s}
.chip:hover{color:var(--ink);border-color:var(--muted)}
.chip.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.chip .n{font-size:9px;opacity:.55;font-variant-numeric:tabular-nums}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:28px 24px;padding:26px 30px 90px}
.card{text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:transform .35s ease,opacity .3s ease}
.card:hover{transform:translateY(-4px)}
.card[hidden]{display:none!important}
.card.out{opacity:0;transform:scale(.92) translateY(10px)}
.imgwrap{position:relative;aspect-ratio:3/4;background:var(--card);overflow:hidden;border:1px solid var(--line);transition:border-color .25s ease}
.imglink{display:block;width:100%;height:100%}
.imgwrap img{width:100%;height:100%;object-fit:cover;mix-blend-mode:multiply;transition:transform .6s ease}
.card:hover .imgwrap img{transform:scale(1.04)}
.badge-new{position:absolute;top:10px;left:10px;z-index:2;background:var(--accent);color:#fff;font-size:9px;letter-spacing:.22em;text-transform:uppercase;padding:4px 8px;line-height:1}
.acts{position:absolute;left:0;right:0;bottom:12px;display:flex;justify-content:center;gap:16px;opacity:0;transition:opacity .25s ease;pointer-events:none}
.card:hover .acts{opacity:1;pointer-events:auto}
@media (hover:none){.acts{opacity:1;pointer-events:auto}}
.act{width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:rgba(250,248,244,.94);backdrop-filter:blur(6px);cursor:pointer;font-size:16px;line-height:1;display:grid;place-items:center;color:var(--ink);box-shadow:0 4px 14px rgba(0,0,0,.12);transition:transform .15s ease,background .2s,color .2s,border-color .2s}
.act:hover{transform:scale(1.09)}
.act.like{color:var(--love)}
.card.is-liked .act.like{background:var(--love);color:#fff;border-color:var(--love)}
.card.is-liked .imgwrap{border-color:var(--love)}
.card.is-disliked .act.dislike{background:var(--ink);color:#fff;border-color:var(--ink)}
.card.is-disliked{opacity:.5}
.meta{padding:14px 2px 0;text-decoration:none;color:inherit}
.row{display:flex;justify-content:space-between;align-items:baseline}
.brand{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink)}
.score{font-family:'Cormorant Garamond',serif;font-size:16px;color:var(--muted)}
.title{font-family:'Cormorant Garamond',serif;font-size:19px;line-height:1.25;margin:5px 0 6px}
.price{font-size:13px;letter-spacing:.04em;color:var(--ink)}
.why{color:var(--accent);font-style:italic;margin-top:9px;line-height:1.4;font-family:'Cormorant Garamond',serif;font-size:14px}
.src{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-top:7px}
.empty{text-align:center;color:var(--muted);padding:70px 20px;font-family:'Cormorant Garamond',serif;font-size:22px;font-style:italic}
@media (max-width:820px){
  body{flex-direction:column}
  .side{height:auto;width:auto;flex:none;flex-direction:row;align-items:center;gap:8px;overflow-x:auto;padding:10px 12px;border-right:none;border-bottom:1px solid var(--line);z-index:20}
  .side .mark,.side .tag{display:none}
  .side nav{flex-direction:row;gap:4px}
  .tab{white-space:nowrap;padding:8px 12px}
  .tab.love{margin-top:0}
  .side-foot{margin:0 0 0 auto;flex-direction:row;align-items:center;border-top:none;padding-top:0;gap:8px}
  .m-head{padding:26px 18px 16px}
  .occbar{padding:16px 16px 0;flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .chip{white-space:nowrap}
  .grid{padding:20px 16px 70px}
}
'''

SCRIPT = '''
(function(){
  // Retry images that fail transiently (e.g. ERR_NETWORK_CHANGED, CDN drops on a
  // burst of ~800 requests). A failed <img> never re-fetches on its own, leaving a
  // permanent broken thumbnail. Refetch the SAME url (no query mutation, so signed
  // CDN urls stay valid) up to 3x with backoff.
  document.addEventListener('error', function(e){
    var img=e.target;
    if(!img || img.tagName!=='IMG') return;
    var n=img._retry||0; if(n>=3) return; img._retry=n+1;
    var src=img.src;
    setTimeout(function(){ img.src=''; img.src=src; }, 500*(n+1));
  }, true);
  var KEY='theedit:v1';
  var grid=document.getElementById('grid');
  var cards=Array.prototype.slice.call(grid.querySelectorAll('.card'));
  var TAB_CATS = __TAB_CATS__;
  // categorical vision axes with their like/dislike weights, as
  // [datasetKey, likeCap, likePer, dislikeCap, dislikePer] — mirrors VIS_WEIGHTS
  // in build_feed.py. Used both to snapshot saved likes and to score the LIVE
  // rerank below.
  var VCATS=[['sil',14,7,12,6],['form',8,4,8,4],['neck',6,3,6,3],['slv',6,3,6,3],['len',6,3,6,3],['fab',8,4,8,4],['drp',6,3,6,3],['bk',10,5,6,3]];
  var tabEls=Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var chipEls=Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var state=load(); var view='all'; var occ='all'; var showDismissed=false;

  function load(){ try{var s=JSON.parse(localStorage.getItem(KEY)); return (s&&s.liked)?s:{liked:{},disliked:{}};}catch(e){return {liked:{},disliked:{}};} }
  function save(){ try{localStorage.setItem(KEY, JSON.stringify(state));}catch(e){} push(); }
  function push(){ try{ fetch('/feedback',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(state)}).catch(function(){}); }catch(e){} }
  function hydrate(cb){
    try{
      fetch('/feedback').then(function(r){return r.ok?r.json():null;}).then(function(disk){
        if(disk){
          ['liked','disliked'].forEach(function(side){ var d=disk[side]||{}; Object.keys(d).forEach(function(id){ if(!state.liked[id]&&!state.disliked[id]) state[side][id]=d[id]; }); });
          try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){} push();
        }
        cb();
      }).catch(function(){ cb(); });
    }catch(e){ cb(); }
  }
  // info() snapshots the card's tags onto the saved like/dislike, so the live
  // taste profile can be rebuilt from state alone (no item lookup needed).
  function info(card){ var o={brand:card.dataset.brand||'',creators:card.dataset.creators||'',c:card.dataset.c||'',cats:card.dataset.cats||'',neut:card.dataset.neut||'',om:card.dataset.om||'',ts:new Date().toISOString().slice(0,10)}; VCATS.forEach(function(f){o[f[0]]=card.dataset[f[0]]||'';}); return o; }
  function catsOf(card){ return (card.dataset.cats||'').split(' ').filter(Boolean); }
  function occOf(card){ return (card.dataset.occ||'').split(' ').filter(Boolean); }
  function matchOcc(card,o){ return o==='all' || occOf(card).indexOf(o)>=0; }

  // ---- live rerank: every heart/✕ reshapes the order, no rebuild ------------
  // buildProfile() turns the saved swipes into liked/disliked centroids;
  // liveScore() adds the feedback + vision-centroid terms (mirroring
  // feedback_adjust + vision_adjust in build_feed.py) on top of each card's
  // cold data-base. rerank() re-sorts the grid. This is the whole point of the
  // page: taste compounds as you curate, with zero server round-trip.
  function buildProfile(){
    var P={Lb:{},Db:{},Lc:{},Dc:{},Lv:{},Dv:{},_Lcol:[],_nu:[],cm:null,Lneu:null};
    function add(side,o){
      var bset=side==='L'?P.Lb:P.Db, cset=side==='L'?P.Lc:P.Dc, vset=side==='L'?P.Lv:P.Dv;
      var b=(o.brand||'').toLowerCase().trim(); if(b) bset[b]=(bset[b]||0)+1;
      (o.cats||'').split(' ').filter(Boolean).forEach(function(c){ cset[c]=(cset[c]||0)+1; });
      var cv=parseFloat(o.c); if(side==='L'&&!isNaN(cv)) P._Lcol.push(cv);
      VCATS.forEach(function(f){ var v=o[f[0]]; if(v&&v!=='na'){ if(!vset[f[0]])vset[f[0]]={}; vset[f[0]][v]=(vset[f[0]][v]||0)+1; } });
      if(side==='L'){ var nu=parseFloat(o.neut); if(!isNaN(nu)) P._nu.push(nu); }
    }
    Object.keys(state.liked).forEach(function(id){ add('L', state.liked[id]||{}); });
    Object.keys(state.disliked).forEach(function(id){ add('D', state.disliked[id]||{}); });
    if(P._Lcol.length) P.cm=P._Lcol.reduce(function(a,b){return a+b;},0)/P._Lcol.length;
    if(P._nu.length) P.Lneu=P._nu.reduce(function(a,b){return a+b;},0)/P._nu.length;
    return P;
  }
  function liveScore(card,P){
    // d = fit to what she's HEARTED (brand + category + cut/palette + neutrality),
    // computed the same way the server does. base = the cold catalogue score.
    var base=parseFloat(card.dataset.base); if(isNaN(base)) base=parseFloat(card.dataset.score)||0;
    var b=card.dataset.brand||'', cats=catsOf(card), i, d=0, pos=0;
    var nb=(P.Lb[b]||0)-(P.Db[b]||0);
    if(nb){ d+=nb>0?Math.min(11,7*nb):Math.max(-15,9*nb); if(nb>0)pos++; }
    var net=0; for(i=0;i<cats.length;i++){ net+=(P.Lc[cats[i]]||0)-(P.Dc[cats[i]]||0); }
    d+=Math.max(-14, Math.min(12, (net<0?6:4)*net)); if(net>0)pos++;
    for(i=0;i<cats.length;i++){ if((P.Dc[cats[i]]||0)>=2 && !(P.Lc[cats[i]]||0)) d-=20; }
    var cv=parseFloat(card.dataset.c);
    if(!isNaN(cv) && P.cm!=null && Math.abs(cv-P.cm)<0.08){ d+=6; pos++; }
    for(i=0;i<VCATS.length;i++){
      var k=VCATS[i][0], val=card.dataset[k]; if(!val||val==='na') continue;
      var lk=(P.Lv[k]&&P.Lv[k][val])||0, dk=(P.Dv[k]&&P.Dv[k][val])||0;
      if(lk){ d+=Math.min(VCATS[i][1], VCATS[i][2]*lk); pos++; }
      if(dk) d-=Math.min(VCATS[i][3], VCATS[i][4]*dk);
    }
    var nu=parseFloat(card.dataset.neut);
    if(!isNaN(nu) && P.Lneu!=null) d+=5*(1-2*Math.abs(nu-P.Lneu));
    // Knee-length and a-line are clear losers in her hearts but still ride brand +
    // category into the top; demote them hard so they fall out of the feed.
    if(card.dataset.len==='knee') d-=8;
    if(card.dataset.sil==='a-line') d-=10;
    // Stash fit so shouldShow() can DROP anything that doesn't lean toward her
    // hearts (her rule: "no point keeping things I don't like").
    card.__fit=d; card.__pos=pos;
    // Cold start (barely curated): keep the catalogue order so the feed isn't empty.
    var nLiked=Object.keys(state.liked).length;
    if(nLiked<8) return base+d;
    // She's curated. Re-curate to LOOK LIKE her hearts: fit dominates, base is only
    // a faint tiebreaker.
    if(pos===0) d-=12;
    return d*3 + base*0.12;
  }
  var ACC_CAP=12;  // accessories are low-signal and flood the feed; show only the top few
  function rerank(){
    var P=buildProfile(), arr=cards.slice();
    arr.forEach(function(c){ c.__s=liveScore(c,P); });
    arr.sort(function(a,b){ return b.__s-a.__s; });
    // Cap accessories: keep the top ACC_CAP un-reacted ones, hide the rest so
    // clothing leads instead of 70 sunglasses/necklaces.
    var accSeen=0;
    arr.forEach(function(c){ c.__capped=false;
      var id=c.dataset.id;
      if(!state.liked[id] && !state.disliked[id] && catsOf(c).indexOf('accessory')>=0){
        accSeen++; if(accSeen>ACC_CAP) c.__capped=true;
      }
    });
    var frag=document.createDocumentFragment();
    arr.forEach(function(c){ frag.appendChild(c); });
    grid.appendChild(frag);
  }
  function inTab(card,v){
    if(v==='new') return card.dataset.new==='1';
    var c=catsOf(card);
    if(v==='all') return c.indexOf('home')<0 && c.indexOf('beauty')<0;
    var want=TAB_CATS[v]; if(!want) return true;
    for(var i=0;i<c.length;i++){ if(want.indexOf(c[i])>=0) return true; }
    return false;
  }
  // passesFit: does this option lean toward what she's hearted? Her rule is "no
  // point keeping things I don't like", so once she's curated we DROP anything
  // with non-positive fit. Her own Closet/Inspiration are always exempt.
  function passesFit(card){
    if(showDismissed) return true;
    var c=catsOf(card); if(c.indexOf('closet')>=0||c.indexOf('inspiration')>=0) return true;
    if(Object.keys(state.liked).length<8) return true;
    if(card.__capped) return false;                    // accessory overflow
    var nu=parseFloat(card.dataset.neut);              // loud prints/brights — she's a neutral.
    if(!isNaN(nu) && nu<0.3) return false;             // cut CONFIRMED-loud only; keep un-tagged
    return card.__fit!=null && card.__fit>0;
  }
  function shouldShow(card){
    var id=card.dataset.id;
    if(view==='loved') return !!state.liked[id];
    if(state.liked[id]) return false;
    if(state.disliked[id] && !showDismissed) return false;
    if(!inTab(card,view) || !matchOcc(card,occ)) return false;
    return passesFit(card);
  }
  function applyView(){
    rerank();   // taste first, then visibility — order reflects the latest swipe
    var shown=0, counts={}, occCounts={};
    tabEls.forEach(function(t){ counts[t.dataset.view]=0; });
    chipEls.forEach(function(c){ occCounts[c.dataset.occ]=0; });
    counts['loved']=Object.keys(state.liked).length;
    cards.forEach(function(card){
      var id=card.dataset.id;
      card.classList.toggle('is-liked',!!state.liked[id]);
      card.classList.toggle('is-disliked',!!state.disliked[id]);
      var show=shouldShow(card); card.hidden=!show; if(show)shown++;
      if(state.liked[id]) return;
      if(state.disliked[id] && !showDismissed) return;
      if(!passesFit(card)) return;   // hidden options don't inflate tab/chip counts
      // tab counts respect the selected occasion; chip counts respect the selected tab
      tabEls.forEach(function(t){ var v=t.dataset.view; if(v==='loved')return; if(inTab(card,v)&&matchOcc(card,occ)) counts[v]++; });
      chipEls.forEach(function(c){ var o=c.dataset.occ; if(o==='all')return; if(inTab(card,view)&&matchOcc(card,o)) occCounts[o]++; });
    });
    tabEls.forEach(function(t){ var el=t.querySelector('.n'); if(el) el.textContent=counts[t.dataset.view]||0; });
    chipEls.forEach(function(c){ var el=c.querySelector('.n'); if(el&&c.dataset.occ!=='all') el.textContent=occCounts[c.dataset.occ]||0; });
    document.getElementById('occbar').hidden=(view==='loved');
    var hid=cards.filter(function(c){ var id=c.dataset.id; if(state.liked[id])return false;
      var cc=catsOf(c); if(cc.indexOf('home')>=0||cc.indexOf('beauty')>=0)return false;
      var ex=cc.indexOf('closet')>=0||cc.indexOf('inspiration')>=0;
      if(state.disliked[id]) return true;
      if(ex || Object.keys(state.liked).length<8) return false;
      var nu=parseFloat(c.dataset.neut);
      return c.__capped || (!isNaN(nu)&&nu<0.3) || c.__fit==null || c.__fit<=0; }).length;
    document.getElementById('nNope').textContent=hid;
    var active=tabEls.filter(function(t){return t.dataset.view===view;})[0];
    document.getElementById('viewTitle').textContent=active?active.querySelector('.lbl').textContent:'All';
    document.getElementById('count').textContent=shown+(shown===1?' piece':' pieces');
    var e=document.getElementById('empty');
    e.textContent=(view==='loved')?'Nothing saved yet. Tap the heart on pieces you love.':(view==='new')?'No new arrivals right now.':'Nothing left in this category.';
    e.hidden=shown>0;
  }
  function toggle(card,kind){
    var id=card.dataset.id, other=(kind==='liked')?'disliked':'liked';
    if(state[kind][id]){ delete state[kind][id]; }
    else { state[kind][id]=info(card); delete state[other][id]; }
    save();
    if(!shouldShow(card)){   // heart or x both clear the piece from this view
      card.classList.add('out');
      setTimeout(function(){ card.classList.remove('out'); applyView(); },300);
    } else { applyView(); }
  }
  grid.addEventListener('click',function(e){
    var btn=e.target.closest('.act'); if(!btn)return;
    e.preventDefault(); e.stopPropagation();
    toggle(btn.closest('.card'), btn.dataset.act==='like'?'liked':'disliked');
  });
  tabEls.forEach(function(t){
    t.addEventListener('click',function(){ view=t.dataset.view; tabEls.forEach(function(x){x.classList.toggle('on',x===t);}); applyView(); try{window.scrollTo({top:0,behavior:'smooth'});}catch(e){window.scrollTo(0,0);} });
  });
  chipEls.forEach(function(c){
    c.addEventListener('click',function(){ occ=c.dataset.occ; chipEls.forEach(function(x){x.classList.toggle('on',x===c);}); applyView(); try{window.scrollTo({top:0,behavior:'smooth'});}catch(e){window.scrollTo(0,0);} });
  });
  var sd=document.getElementById('showDismissed');
  sd.addEventListener('change',function(){ showDismissed=sd.checked; applyView(); });
  document.getElementById('export').addEventListener('click',function(){
    var blob=new Blob([JSON.stringify(state,null,2)],{type:'application/json'});
    var a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='feedback.json';
    document.body.appendChild(a); a.click(); a.remove(); setTimeout(function(){URL.revokeObjectURL(a.href);},1000);
  });
  var rb=document.getElementById('reset');
  rb.addEventListener('click',function(){ if(confirm('Clear all your likes and dislikes?')){ state={liked:{},disliked:{}}; save(); showDismissed=false; sd.checked=false; view='all'; occ='all'; tabEls.forEach(function(x){x.classList.toggle('on',x.dataset.view==='all');}); chipEls.forEach(function(x){x.classList.toggle('on',x.dataset.occ==='all');}); applyView(); } });
  hydrate(function(){ applyView(); });
})();
'''

# ---- sidebar tabs -----------------------------------------------------------
present = set()
for it in items: present.update(it["cats"])
TAB_DEFS = [
    ("all",         "All",         None),
    ("new",         "New",         "new"),
    ("closet",      "My Closet",   ["closet"]),
    ("inspiration", "Inspiration", ["inspiration"]),
    ("tops",        "Tops",        ["top", "knit"]),
    ("bottoms",     "Bottoms",     ["bottom"]),
    ("dresses",     "Dresses",     ["dress"]),
    ("outerwear",   "Outerwear",   ["outerwear"]),
    ("shoes",       "Shoes",       ["shoe"]),
    ("bags",        "Bags",        ["bag"]),
    ("accessories", "Accessories", ["accessory"]),
    ("swim",        "Swim",        ["swim"]),
    ("loungewear",  "Loungewear",  ["loungewear"]),
    ("home",        "Home",        ["home"]),
    ("beauty",      "Beauty",      ["beauty"]),
    ("loved",       "Loved",       "loved"),
]
has_new = any(_is_new(it) for it in items)
def _present(c):
    if c == "new": return has_new          # hide the New tab when nothing is fresh
    return c is None or c == "loved" or any(x in present for x in c)
tabs = [t for t in TAB_DEFS if _present(t[2])]
tab_cats = {k: c for k, lbl, c in tabs if isinstance(c, list)}

def tab_btn(key, label, cats):
    cls = "tab" + (" love" if key == "loved" else "") + (" on" if key == "all" else "")
    return (f'    <button class="{cls}" data-view="{key}" type="button">'
            f'<span class="lbl">{html.escape(label)}</span><span class="n">0</span></button>')
nav = "\n".join(tab_btn(*t) for t in tabs)

# ---- occasion chips (use-case cross-filter, orthogonal to category tabs) -----
OCC_DEFS = [("all", "All"), ("work", "Work"), ("casual", "Casual"),
            ("going-out", "Going out"), ("active", "Active"), ("vacation", "Vacation")]
occ_present = set()
for it in items:
    occ_present.update(occasions_of(it))
occ_chips = [(k, l) for k, l in OCC_DEFS if k == "all" or k in occ_present]

def occ_chip(key, label):
    cls = "chip" + (" on" if key == "all" else "")
    n = "" if key == "all" else '<span class="n"></span>'
    return (f'    <button class="{cls}" data-occ="{key}" type="button">'
            f'<span class="lbl">{html.escape(label)}</span>{n}</button>')
occbar = '  <div class="occbar" id="occbar">\n' + "\n".join(occ_chip(*c) for c in occ_chips) + '\n  </div>\n'

SCRIPT = SCRIPT.replace("__TAB_CATS__", json.dumps(tab_cats))
wearable = sum(1 for it in items if "home" not in it["cats"] and "beauty" not in it["cats"])

side_html = (
    '<aside class="side">\n'
    '  <div class="mark">The Edit</div>\n'
    '  <div class="tag">for Annabel</div>\n'
    '  <nav>\n' + nav + '\n  </nav>\n'
    '  <div class="side-foot">\n'
    '    <label class="toggle"><input type="checkbox" id="showDismissed"> show everything (<span id="nNope">0</span> hidden)</label>\n'
    '    <button class="mini" id="export" type="button">Export taste</button>\n'
    '    <button class="mini" id="reset" type="button">Reset</button>\n'
    '  </div>\n'
    '</aside>\n'
)
main_html = (
    '<main>\n'
    '  <div class="m-head">\n'
    '    <div class="kicker">What the people you follow are buying, tuned to you</div>\n'
    '    <h1 id="viewTitle">All</h1>\n'
    f'    <div class="count" id="count">{wearable} pieces</div>\n'
    '  </div>\n'
    + occbar +
    '  <div class="grid" id="grid">\n' + cards + '\n  </div>\n'
    '  <div class="empty" id="empty" hidden></div>\n'
    '</main>\n'
)

page = (
    '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    '<title>The Edit</title>\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">\n'
    '<style>' + STYLE + '</style></head>\n<body>\n'
    + side_html + main_html
    + '<script>' + SCRIPT + '</script>\n'
    + '</body></html>'
)

(ROOT/"feed.html").write_text(page, encoding="utf-8")
shutil.copy(ROOT/"feed.html", "/Users/annabelfilippini/Desktop/the-edit-feed.html")

n_home = sum(1 for it in items if "home" in it["cats"])
n_beauty = sum(1 for it in items if "beauty" in it["cats"])
print(f"creators={len(SOURCES)}  items={len(items)}  wearable={wearable}  home={n_home}  beauty={n_beauty}  dropped={dropped_cat}  dupe_img={dropped_dupe_img}  broken={len(broken)}")
print(f"brands={len(BRANDS)}  brand_kept={dict(_bkept)}  brand_dropped={_bdropped}")
print(f"vision: {'ON' if VISION_ON else 'OFF (no key — saturation fallback)'}  tagged={n_vision}/{len(vision_targets)} wearables  model={VISION_MODEL}")
print(f"nuuly: {n_nuuly_rental} rental + {n_nuuly_closet} closet → {len(nuuly_pool)} pool, vision-tagged {n_nuuly_vision}/{len(nuuly_pool)}")
print(f"purchases: {n_purchase} email orders (weight {PURCHASE_WEIGHT:g}x) folded into owned pool")
print(f"back-axis backfill: {n_back}/{len(back_targets)} tops/dresses tagged  model={BACK_MODEL}")
print(f"retailer links resolved: {n_links}/{len(items)}  (rest fall back to ShopMy)")
if VISION_ON and (Lcounts["silhouette"] or Dcounts["silhouette"]):
    print(f"  liked silhouettes={dict(sorted(Lcounts['silhouette'].items(), key=lambda x:-x[1]))}  liked fabrics={dict(sorted(Lcounts['fabric'].items(), key=lambda x:-x[1]))}  liked oldmoney≈{round(Lom,2) if Lom else None}  neutral≈{round(Lneu,2) if Lneu else None}")
if liked or disliked:
    print(f"feedback applied: liked={len(liked)} disliked={len(disliked)}")
print("tabs:", [t[1] for t in tabs])
print("TOP 8:")
for it in items[:8]:
    print(f"  {it['score']:>3}  {','.join(it['cats']):<14}  {it['brand']} | {it['title'][:38]}")
