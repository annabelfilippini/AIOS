#!/usr/bin/env python3
"""Build a branded, self-contained pick-sheet of the FyM Instagram pull.
Photos + reel poster frames embedded as base64. Drops a copy on the Desktop.
"""
import json, glob, os, base64, subprocess, tempfile, html

SRC = "assets/web/photos/instagram"
OUT_PROJECT = "instagram-picksheet.html"
OUT_DESKTOP = os.path.expanduser("~/Desktop/fym-instagram-picksheet.html")
TMP = tempfile.mkdtemp()

def meta_for(media_file):
    j = media_file + ".json"
    if os.path.exists(j):
        return json.load(open(j))
    return {}

def b64_jpg(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

def thumb_photo(src, w=480):
    dst = os.path.join(TMP, os.path.basename(src) + ".thumb.jpg")
    subprocess.run(["sips", "--resampleWidth", str(w), "-s", "format", "jpeg",
                    src, "--out", dst],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dst if os.path.exists(dst) else src

def poster_reel(src, w=480):
    dst = os.path.join(TMP, os.path.basename(src) + ".poster.jpg")
    # grab a frame ~1s in, scale to width
    subprocess.run(["ffmpeg", "-y", "-ss", "1.0", "-i", src, "-vframes", "1",
                    "-vf", f"scale={w}:-1", dst],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not os.path.exists(dst):  # fallback to first frame
        subprocess.run(["ffmpeg", "-y", "-i", src, "-vframes", "1",
                        "-vf", f"scale={w}:-1", dst],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dst if os.path.exists(dst) else None

def cap_of(m):
    return (m.get("description") or "").strip()

# --- gather photos (carousel collapsed to its lead image, rest noted) ---
jpgs = sorted(glob.glob(os.path.join(SRC, "*.jpg")))
carousel_prefix = "3741303026574255418"
photos = []
carousel_imgs = [p for p in jpgs if os.path.basename(p).startswith(carousel_prefix)]
singles = [p for p in jpgs if not os.path.basename(p).startswith(carousel_prefix)]

# carousel: show all 7 as a group
for i, p in enumerate(carousel_imgs):
    m = meta_for(p)
    photos.append({"path": p, "cap": cap_of(m), "likes": m.get("like_count"),
                   "group": "Carousel (7 photos) — beach team / good mood",
                   "idx": i+1, "n": len(carousel_imgs)})
for p in singles:
    m = meta_for(p)
    photos.append({"path": p, "cap": cap_of(m), "likes": m.get("like_count"),
                   "group": None})

# --- gather reels ---
mp4s = sorted(glob.glob(os.path.join(SRC, "*.mp4")))
reels = []
for p in mp4s:
    m = meta_for(p)
    reels.append({"path": p, "cap": cap_of(m),
                  "w": m.get("width"), "h": m.get("height")})

def card(thumb_data, caption, badge, sub):
    cap = html.escape(caption[:240])
    return f"""
    <figure class="card">
      <div class="imgwrap"><img loading="lazy" src="{thumb_data}" alt=""></div>
      <figcaption>
        <span class="badge">{badge}</span>
        <p class="cap">{cap}</p>
        <p class="sub">{sub}</p>
      </figcaption>
    </figure>"""

photo_cards = []
print("Thumbnailing photos...")
for ph in photos:
    t = thumb_photo(ph["path"])
    data = b64_jpg(t)
    likes = f"♥ {ph['likes']}" if ph.get("likes") else ""
    if ph.get("group"):
        badge = f"PHOTO · {ph['idx']}/{ph['n']}"
        sub = f"{ph['group']} · {likes}"
    else:
        badge = "PHOTO"
        sub = f"{os.path.basename(ph['path'])} · {likes}"
    photo_cards.append(card(data, ph["cap"], badge, sub))

reel_cards = []
print("Extracting reel posters...")
for r in reels:
    poster = poster_reel(r["path"])
    if not poster:
        continue
    data = b64_jpg(poster)
    dim = f"{r['w']}×{r['h']}" if r.get("w") else ""
    sub = f"{os.path.basename(r['path'])} · {dim} · video"
    reel_cards.append(card(data, r["cap"], "REEL ▶", sub))

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Free your Mind — Instagram pull</title>
<style>
  :root {{
    --ivory:#f7f1e7; --ink:#2a2622; --terra:#c8794f; --teal:#2f6f6b;
    --line:#e3d8c7; --card:#fffdf9;
  }}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--ivory);color:var(--ink);
    font-family:'Inter',-apple-system,system-ui,sans-serif;line-height:1.5}}
  header{{padding:40px 32px 24px;border-bottom:1px solid var(--line)}}
  h1{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:32px;margin:0 0 6px}}
  header p{{margin:0;color:#6b6258;max-width:60ch}}
  .meta{{margin-top:14px;font-size:13px;color:var(--teal);font-weight:600;letter-spacing:.02em}}
  h2{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:22px;
    margin:36px 32px 4px;padding-top:20px}}
  .note{{margin:0 32px 16px;color:#6b6258;font-size:14px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));
    gap:18px;padding:8px 32px 40px}}
  .card{{margin:0;background:var(--card);border:1px solid var(--line);
    border-radius:2px;overflow:hidden;display:flex;flex-direction:column}}
  .imgwrap{{background:#ece3d4;aspect-ratio:4/5;overflow:hidden;display:flex;
    align-items:center;justify-content:center}}
  .imgwrap img{{width:100%;height:100%;object-fit:cover;display:block}}
  figcaption{{padding:10px 12px 14px}}
  .badge{{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.06em;
    color:#fff;background:var(--teal);padding:2px 8px;border-radius:2px}}
  .card .badge{{}}
  figcaption .cap{{margin:8px 0 4px;font-size:13px;color:var(--ink)}}
  figcaption .sub{{margin:0;font-size:11px;color:#9a9082;word-break:break-all}}
  .reel .badge{{background:var(--terra)}}
  footer{{padding:24px 32px 60px;color:#9a9082;font-size:12px;border-top:1px solid var(--line)}}
</style></head><body>
<header>
  <h1>Free your Mind — Instagram pull</h1>
  <p>Their real @free_your_mind_experience feed: {len(photos)} photos (incl. a 7-image carousel) and {len(reels)} reels, most recent 40 posts. Pick the ones you want on the site — reels can run as muted background video or I can pull a sharp still frame.</p>
  <p class="meta">Source: instagram.com/free_your_mind_experience · pulled via authenticated session</p>
</header>

<h2>Photos</h2>
<p class="note">The sunset surf shot (♥358) is their best-performing image by far.</p>
<div class="grid">{''.join(photo_cards)}</div>

<h2>Reels <span style="font-size:13px;color:#9a9082;font-weight:400">(poster frame shown — actual files are video)</span></h2>
<p class="note">Vertical action footage. Strong candidates for a muted hero background loop, like the Freeride site.</p>
<div class="grid reel">{''.join(c.replace('class="card"','class="card reel"') for c in reel_cards)}</div>

<footer>Generated pick-sheet · originals in projects/websites/freeyourmind-tarifa/assets/web/photos/instagram/</footer>
</body></html>"""

open(OUT_PROJECT, "w").write(HTML)
open(OUT_DESKTOP, "w").write(HTML)
size = len(HTML)/1024/1024
print(f"\nWrote {OUT_PROJECT} and {OUT_DESKTOP} ({size:.1f} MB)")
print(f"Photos: {len(photo_cards)} cards | Reels: {len(reel_cards)} cards")
