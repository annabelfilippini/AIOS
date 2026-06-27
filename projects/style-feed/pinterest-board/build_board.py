#!/usr/bin/env python3
"""Build a curated 'style read' board for The Edit.
Downloads real Pinterest pins, embeds them base64, outputs a branded board page.
v2 — recalibrated from Annabel's direct feedback (2026-06-22):
  - KILL red/burgundy, flared trousers, capri leggings
  - palette: black, blue, brown, grey + ecru/cream (her Zara shorts)
  - loves: all-black outfits, loose pants, matching sets
  - brands: Aritzia sets, Lululemon sets, Free People (simpler pieces)
  - add the two lanes v1 missed: Everyday/Casual + Going Out
"""
import base64, os, urllib.request, sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(HERE, "img")
os.makedirs(IMGDIR, exist_ok=True)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# (slug, url, title, why)
SECTIONS = {
"Everyday": ("your fall everyday, from your pics: oversized knits, wide blue jeans, tall boots, loafers.", [
    ("37d21c98ef10d897802c03898d9b10fd", "https://i.pinimg.com/736x/37/d2/1c/37d21c98ef10d897802c03898d9b10fd.jpg",
     "Oversized knit + wide blue jeans", "Your exact everyday: cozy sweater, wide blue jean, coffee in hand."),
    ("89b229441e89b74b68e37f517a95bdc4", "https://i.pinimg.com/736x/89/b2/29/89b229441e89b74b68e37f517a95bdc4.jpg",
     "Cable knit + tan chelsea boots", "Cream cable knit, light jeans, tan boots. Peak fall-cozy."),
    ("02812fa6110f639ea6b3692b987be2e6", "https://i.pinimg.com/736x/02/81/2f/02812fa6110f639ea6b3692b987be2e6.jpg",
     "Camel cardigan + white tee + jeans", "Cardigan over a white tee, straight jeans, a flat. The uniform."),
    ("d7e979e53baca0aa7e940287180f741c", "https://i.pinimg.com/736x/d7/e9/79/d7e979e53baca0aa7e940287180f741c.jpg",
     "Brown cardigan + denim shirt + loafers", "Chocolate cardigan, chambray, brown loafers. So you."),
    ("d150b26994758ebc27e0b2b88f7794e8", "https://i.pinimg.com/736x/d1/50/b2/d150b26994758ebc27e0b2b88f7794e8.jpg",
     "Tunic sweater + tall cognac boots", "Long sweater, tall riding boots. The boot look from your pics."),
    ("af36e9296408ce416cccab819d95c668", "https://i.pinimg.com/736x/af/36/e9/af36e9296408ce416cccab819d95c668.jpg",
     "Grey sweater + tailored shorts", "Your shorts-and-sweater everyday, the cooler-weather cut."),
]),
"Work": ("your references, read back: clean tops, knit vests, loose trousers, a sleek skirt.", [
    ("0dd8611e2df28da53a3d1dfc51245589", "https://i.pinimg.com/736x/0d/d8/61/0dd8611e2df28da53a3d1dfc51245589.jpg",
     "Sleek knit top + column skirt", "Clean, tonal, elevated. Your skirt pic, nailed."),
    ("53d620711d06864a80623c5eb4e17183", "https://i.pinimg.com/736x/53/d6/20/53d620711d06864a80623c5eb4e17183.jpg",
     "Knit vest + white shirt + black trousers", "The vest-over-shirt layering from your third pic, exactly."),
    ("b8cc02b867d6eb1c76c8c0f87f8b49aa", "https://i.pinimg.com/736x/b8/cc/02/b8cc02b867d6eb1c76c8c0f87f8b49aa.jpg",
     "Cricket vest + loafers", "Preppy-soft, cream and navy, polished but easy."),
    ("bf120e78425bd9f834e7aae0bc0a4382", "https://i.pinimg.com/736x/bf/12/0e/bf120e78425bd9f834e7aae0bc0a4382.jpg",
     "White shirt + black slit skirt", "Your fourth pic: crisp top, sleek slit skirt, a heel."),
    ("3d7b1bb583abd92d3bb1117bd44b0292", "https://i.pinimg.com/736x/3d/7b/1b/3d7b1bb583abd92d3bb1117bd44b0292.jpg",
     "Breton stripe + loose black trousers", "Stripes you already wear, with the loose black trouser."),
    ("e26455f4bfb81e167d8cc4c30445e47f", "https://i.pinimg.com/736x/e2/64/55/e26455f4bfb81e167d8cc4c30445e47f.jpg",
     "White tee + loose grey trousers", "Your second pic's energy: easy jacket, wide trouser, flat."),
    ("2209d4619042934c8e76fb7680ada67e", "https://i.pinimg.com/736x/22/09/d4/2209d4619042934c8e76fb7680ada67e.jpg",
     "Tee + black maxi skirt", "The casual way to wear the long skirt."),
    ("eab74083ce521258f2c2b056c2dc59a8", "https://i.pinimg.com/736x/ea/b7/40/eab74083ce521258f2c2b056c2dc59a8.jpg",
     "Long grey coat over the basics", "The grey-jacket look from your pics, in a longer line."),
]),
"Workout": ("sets in neutral + black. set active / lululemon / aritzia / fp movement energy.", [
    ("55da19f974d78fd4e0b2e35f94d7d0c7", "https://i.pinimg.com/736x/55/da/19/55da19f974d78fd4e0b2e35f94d7d0c7.jpg",
     "Cream sweat set + New Balance", "Matching cream set, the Aritzia sweatfleece feeling."),
    ("abc8c08addd4378be0ced2dc7b324ad9", "https://i.pinimg.com/736x/ab/c8/c0/abc8c08addd4378be0ced2dc7b324ad9.jpg",
     "Neutral leggings + zip hoodie", "Clean-girl set: mushroom leggings, grey half-zip, NB. Set Active energy."),
    ("d391235dda5e528d7fe18244db7f52a0", "https://i.pinimg.com/736x/d3/91/23/d391235dda5e528d7fe18244db7f52a0.jpg",
     "All-black jacket + leggings", "Full black, sleek. The Lululemon all-black you like."),
    ("bb7aa1a7cc8e17c42876dac953e43cd6", "https://i.pinimg.com/736x/bb/7a/a1/bb7aa1a7cc8e17c42876dac953e43cd6.jpg",
     "Beige Pilates set + jacket", "Tonal sports set with a throw-on jacket. Pilates-to-coffee."),
    ("f3ee70def91e08c62c6b94fff215e7ca", "https://i.pinimg.com/736x/f3/ee/70/f3ee70def91e08c62c6b94fff215e7ca.jpg",
     "Cozy grey knit set", "Soft knit two-piece for the low-key days."),
]),
"Going out": ("you said I missed this. black, sleek, a little satin. your halter energy.", [
    ("f4a83581c597e8faf2a7f594d8cbb779", "https://i.pinimg.com/736x/f4/a8/35/f4a83581c597e8faf2a7f594d8cbb779.jpg",
     "Black satin midi + pumps", "Sleek, minimal, all-black. The grown-up going-out look."),
    ("1b9e104e31940ffc624019c295c2fd36", "https://i.pinimg.com/736x/1b/9e/10/1b9e104e31940ffc624019c295c2fd36.jpg",
     "Satin skirt + heels", "Satin separates, the same fabric as your Wilfred halter."),
    ("8f5807035c0e5ae081cac2e704dda649", "https://i.pinimg.com/736x/8f/58/07/8f5807035c0e5ae081cac2e704dda649.jpg",
     "Black satin plunge, dressed", "A going-out piece that still reads clean, not costume."),
    ("cd26c6643a8263e0d083472691a7850e", "https://i.pinimg.com/736x/cd/26/c6/cd26c6643a8263e0d083472691a7850e.jpg",
     "Elegant dinner look", "Date-night / dinner, understated and elevated."),
    ("7a9e76dd3a849abef6fb5958e9742bee", "https://i.pinimg.com/736x/7a/9e/76/7a9e76dd3a849abef6fb5958e9742bee.jpg",
     "Night-out, minimal", "Going out without trying too hard. Sleek over sparkly."),
    ("9dc41fd965fd0c60cde6b800c5c48e9a", "https://i.pinimg.com/736x/9d/c4/1f/9dc41fd965fd0c60cde6b800c5c48e9a.jpg",
     "Simple evening dress", "One clean black dress, let it do the work."),
]),
}

def fetch(slug, url):
    path = os.path.join(IMGDIR, slug + ".jpg")
    if not os.path.exists(path) or os.path.getsize(path) < 1500:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://www.pinterest.com/"})
        try:
            data = urllib.request.urlopen(req, timeout=30).read()
            with open(path, "wb") as f:
                f.write(data)
        except Exception as e:
            print(f"  FAIL {slug}: {e}", file=sys.stderr); return None
    size = os.path.getsize(path)
    if size < 1500:
        print(f"  TINY {slug}: {size}b", file=sys.stderr); return None
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    print(f"  ok   {slug}: {size//1024}kb")
    return f"data:image/jpeg;base64,{b64}"

def tile(item):
    slug, url, title, why = item
    src = fetch(slug, url)
    if not src: return ""
    return f"""<figure class="card"><div class="imgwrap"><img loading="lazy" src="{src}" alt="{title}"></div>
      <figcaption><div class="title">{title}</div><div class="why">{why}</div></figcaption></figure>"""

sec_html = ""
for name, (note, items) in SECTIONS.items():
    print(f"{name}:")
    grid = "\n".join(t for t in (tile(i) for i in items) if t)
    sec_html += f"""<section class="sec"><div class="sechead"><h2>{name}</h2><span class="note">{note}</span></div>
    <div class="grid">{grid}</div></section>\n"""

HTML = f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Edit · Style Read v2</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f3efe9;--ink:#1b1916;--muted:#7c756a;--line:#e0d9cd;--card:#faf8f4;--accent:#3a352d;--love:#b54b5a}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:'Jost',system-ui,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1120px;margin:0 auto;padding:46px 26px 90px}}
header{{text-align:center;margin-bottom:8px}}
.mark{{font-family:'Cormorant Garamond',serif;font-size:26px;letter-spacing:.24em;text-transform:uppercase}}
.kicker{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-top:10px}}
.lede{{max-width:660px;margin:18px auto 0;text-align:center;font-family:'Cormorant Garamond',serif;font-size:21px;line-height:1.45;color:var(--accent)}}
.lede em{{font-style:italic;color:var(--love)}}
.changed{{max-width:660px;margin:16px auto 0;text-align:center;font-size:12.5px;letter-spacing:.02em;color:var(--muted);line-height:1.7}}
.sec{{margin-top:50px}}
.sechead{{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:24px;flex-wrap:wrap}}
.sechead h2{{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:30px;margin:0}}
.sechead .note{{font-size:13px;color:var(--muted)}}
.grid{{column-width:230px;column-gap:20px}}
.card{{margin:0 0 20px;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;break-inside:avoid;display:inline-block;width:100%}}
.imgwrap{{display:block;width:100%;background:#ece6dc}}
.imgwrap img{{width:100%;height:auto;display:block}}
figcaption{{padding:13px 14px 16px}}
.title{{font-family:'Cormorant Garamond',serif;font-size:19px;line-height:1.15;margin:0 0 4px}}
.why{{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:14px;line-height:1.3;color:var(--love);margin:0}}
footer{{margin-top:64px;text-align:center;font-size:13px;color:var(--muted);line-height:1.7}}
footer .q{{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:18px;color:var(--accent)}}
</style></head>
<body><div class="wrap">
<header>
  <div class="mark">The Edit</div>
  <div class="kicker">A Style Read · v3 · built from your reference pics</div>
  <p class="lede">All four lanes now read back from the pictures you sent. Work and Everyday rebuilt outfit-by-outfit from your screenshots; Workout pulled to your brands. <em>Every pin here I actually looked at first.</em></p>
  <p class="changed">FROM YOUR PICS — <b>Work</b>: ivory tops, knit vests, slit skirt, loose trousers &nbsp;·&nbsp; <b>Everyday</b>: oversized knits, wide blue jeans, tall boots, loafers &nbsp;·&nbsp; <b>Workout</b>: neutral + black sets (Set Active / Lululemon / Aritzia / FP Movement)</p>
</header>
{sec_html}
<footer>
  <p class="q">Warmer?</p>
  <p>Same drill: which tiles are dead-on, which are still off, what's missing.<br>
  When the read holds, I turn it into real shoppable outfits with links.</p>
</footer>
</div></body></html>"""

OUT = os.path.join(HERE, "board.html")
open(OUT, "w").write(HTML)
DESK = os.path.expanduser("~/Desktop/the-edit-style-read.html")
open(DESK, "w").write(HTML)
print(f"\nWrote {OUT}\nWrote {DESK}\nSize: {len(HTML)//1024}kb")
