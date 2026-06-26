#!/usr/bin/env python3
"""Kite Wind Watch — Reddit spot-discovery scraper (kitesurfing only).

Reads FULL Reddit threads (post + every comment) for the Colorado + Wyoming
region and mines them for KITESURFING / kiteboarding spots — water kiting only.
Snowkiting, wingfoiling, eFoil and other random foil sports are filtered out.
Surfaces not just the spots Annabel named but every water-kite spot people
actually talk about, ranked by how many threads mention it.

How it gets the data:
  This is a thin orchestrator over **reddit-cli** (tools/reddit-cli), which uses
  Annabel's authenticated browser session to read Reddit. We went this route
  because Reddit 403s anonymous .json, Firecrawl refuses to scrape threads, a
  headless browser is network-blocked, and the official API's app-creation form
  is currently bugged. reddit-cli (the skool-pp-cli authenticated-cookie pattern)
  is the working path. See its agent-context for details.

Flow:
  1. `reddit-cli sync` across the kite/foil subs (searching geo terms) and the
     geo subs (searching sport terms) -> local SQLite mirror of threads+comments.
  2. `reddit-cli export` that mirror as JSON.
  3. Tag known spots, discover unknown ones, and write data/discourse.{json,js}
     for the dashboard's "What people are saying" panel.

  Use --no-sync to re-mine the existing mirror without hitting Reddit again.

Standard library only — no pip install. reddit-cli must have a valid session
(`reddit-cli doctor`); if not, this keeps existing data rather than wiping it.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DATA = PROJECT / "data"
AIOS_ROOT = PROJECT.parents[2]                      # .../AI-OS
REDDIT_CLI = os.environ.get("REDDIT_CLI") or str(
    AIOS_ROOT / "tools" / "reddit-cli" / "reddit-cli")

# --- tunables ----------------------------------------------------------------
MAX_POSTS = 24                  # threads kept in the dashboard panel
SYNC_LIMIT_SPORT = 30           # threads per sport-sub search
SYNC_LIMIT_GEO = 20             # threads per geo-sub search

# --- where the kitesurf + regional crowd talks -------------------------------
# Kitesurfing only — no snowkiting / wingfoil / efoil subs.
SPORT_SUBS = ["Kiteboarding", "kitesurfing"]
GEO_SUBS = ["Colorado", "Wyoming", "Denver", "boulder", "ColoradoSprings",
            "FortCollins", "Nebraska"]
ALL_SUBS = SPORT_SUBS + GEO_SUBS
# In sport subs, search for the region; in regional subs, search for the sport.
GEO_TERMS = ('Colorado OR Wyoming OR Denver OR Boulder OR "Front Range" '
             'OR Laramie OR Cheyenne OR Nebraska')
SPORT_TERMS = 'kitesurf OR kiteboard OR kiteboarding OR kitesurfing OR kiting'

# --- spot tagging ------------------------------------------------------------
# Known spots: name -> (regex over text, display "where"). Extend freely; the
# discovery extractor below finds the ones we haven't listed here yet.
SPOT_META = {
    "Lake McConaughy":         (r"mcconaughy|\blake mac\b",        "Nebraska high plains"),
    "Lake Dillon":             (r"\bdillon\b",                      "Colorado mountains"),
    "Lake Hattie":             (r"\bhattie\b",                      "Wyoming (Laramie)"),
    "Twin Buttes Lake":        (r"twin buttes",                     "Wyoming (Laramie)"),
    "Williams Fork Reservoir": (r"williams fork",                   "Colorado mountains"),
    "Cherry Creek Reservoir":  (r"cherry creek",                    "Denver"),
    "Aurora Reservoir":        (r"aurora reservoir|aurora res\b",   "Denver"),
    "Chatfield Reservoir":     (r"chatfield",                       "Denver"),
    "Union Reservoir":         (r"union reservoir",                 "Longmont"),
    "Boyd Lake":               (r"\bboyd\b",                        "Loveland"),
    "Pueblo Reservoir":        (r"\bpueblo\b",                      "Southern Colorado"),
    "Standley Lake":           (r"standley",                        "Denver (Westminster)"),
    "Sloan Lake":              (r"sloan",                           "Denver (in city)"),
    "Georgetown Lake":         (r"georgetown lake|georgetown res",  "Colorado mountains"),
    # newly confirmed from discovery scans:
    "Big Soda Lake":           (r"big soda lake|soda lakes?",       "Lakewood (Denver)"),
    "Horsetooth Reservoir":    (r"horsetooth",                      "Fort Collins"),
    "Carter Lake":             (r"carter lake",                     "Loveland"),
    "Boulder Reservoir":       (r"boulder reservoir|boulder res\b", "Boulder"),
    # (snowkite-only spots removed — this tracks water kitesurfing only)
}
SPOT_RX = {name: re.compile(pat, re.I) for name, (pat, _) in SPOT_META.items()}

# Spots already selectable in the dashboard (so "new finds" can be badged).
KNOWN_SPOTS = {
    "Aurora Reservoir", "Cherry Creek Reservoir", "Chatfield Reservoir",
    "Union Reservoir", "Boyd Lake", "Lake Dillon", "Pueblo Reservoir",
    "Lake McConaughy",
}
DAD_SPOTS = ["Lake Hattie", "Twin Buttes Lake", "Williams Fork Reservoir"]
DAD_RX = {
    "Lake Hattie": re.compile(r"\bhattie\b", re.I),
    "Twin Buttes Lake": re.compile(r"twin buttes", re.I),
    "Williams Fork Reservoir": re.compile(r"williams fork", re.I),
}

# Kitesurfing only — require a real sport compound, NOT bare "kite"/"kiting".
# (Bare "kite" pulls in toy-kite threads, music lineups, UFO posts, etc.)
KITE_RX = re.compile(
    r"kitesurf|kite ?surf|kiteboard|kite ?board|kiteboarding|kitefoil|kite ?foil",
    re.I)
# Snowkiting / ice kiting / wingfoil / efoil get dropped — see filtering below.
SNOW_RX = re.compile(
    r"snow ?kite|snowkit|ice ?kite|wing ?foil|wingfoil|winging|e-?foil", re.I)
# A snow/wing term in the TITLE means the thread is about that sport — drop it
# outright even if it name-drops a lake.
SNOW_TITLE_RX = re.compile(r"snow ?kite|snowkit|ice ?kite|wing ?foil|wingfoil|e-?foil", re.I)
WATER_RX = re.compile(
    r"kitesurf|kiteboard|reservoir|\blake\b|water|summer|launch|beach", re.I)
GEO_RX = re.compile(
    r"colorado|wyoming|denver|boulder|fort collins|laramie|cheyenne|"
    r"front range|colorado springs|pueblo|loveland|longmont|nebraska|"
    r"\bco\b|\bwy\b|summit county|steamboat|windsor|mcconaughy", re.I)

# Discovery: pull candidate place names out of free text. Matches both
# "<Name> Reservoir/Lake/Pass/Dam" and "Lake <Name>".
PLACE_SUFFIX_RX = re.compile(
    r"\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2})\s+"
    r"(Reservoir|Lake|Res|Ponds?|Pass|Dam)\b")
PLACE_LAKE_PREFIX_RX = re.compile(r"\bLake\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)\b")
# Things the suffix regex catches that are not kite spots.
PLACE_STOPWORDS = {
    "salt lake", "great lakes", "the lake", "this lake", "that lake",
    "a lake", "lake city", "lake the", "crater lake", "finger lakes",
    "mountain lake", "the res", "the dam", "the pass", "mountain pass",
    "the reservoir", "any lake", "some lake", "every lake", "small lake",
    "big lake", "local lake", "nearest lake", "nearby lake", "home lake",
    "the ponds", "open lake", "good lake", "best lake", "main lake",
}
# Leading words that mean the regex grabbed a sentence fragment, not a place.
NAME_STOPWORDS = {
    "kite", "kiteboarding", "kiteboard", "kitesurf", "kitesurfing", "snowkite",
    "snowkiting", "wingfoil", "winging", "foil", "foiling", "kitefoil",
    "the", "any", "this", "that", "some", "every", "a", "an", "my", "your",
    "our", "his", "her", "their", "good", "best", "big", "small", "local",
    "main", "open", "nearest", "nearby", "home", "great", "finger", "mountain",
    "crater", "salt", "what", "where", "which", "another", "other", "new",
}


# --- reddit-cli orchestration ------------------------------------------------
def run_rcli(args, capture=True):
    return subprocess.run([sys.executable, REDDIT_CLI] + args,
                          capture_output=capture, text=True)


def rcli_session_ok():
    r = run_rcli(["doctor", "--json"])
    try:
        return json.loads(r.stdout or "{}").get("ok") is True
    except json.JSONDecodeError:
        return False


def do_sync():
    print("Syncing kite/foil subs (searching the region)…")
    run_rcli(["sync", "-r", ",".join(SPORT_SUBS), "-q", GEO_TERMS,
              "--limit", str(SYNC_LIMIT_SPORT), "--time", "all",
              "--max-comments", "150", "--json"], capture=False)
    print("Syncing regional subs (searching the sport)…")
    run_rcli(["sync", "-r", ",".join(GEO_SUBS), "-q", SPORT_TERMS,
              "--limit", str(SYNC_LIMIT_GEO), "--time", "all",
              "--max-comments", "120", "--json"], capture=False)


def load_candidates():
    """Pull the mirror as candidate threads with full comment text."""
    r = run_rcli(["export", "-r", ",".join(ALL_SUBS), "--json"])
    try:
        data = json.loads(r.stdout or "{}")
    except json.JSONDecodeError:
        print("! could not parse reddit-cli export output", file=sys.stderr)
        return []
    cands = []
    for p in data.get("posts", []):
        comments = [c.get("body", "") for c in p.get("comments", [])]
        cands.append({
            "id": p.get("id"),
            "subreddit": p.get("subreddit") or "reddit",
            "url": "https://www.reddit.com" + (p.get("permalink") or ""),
            "title": p.get("title") or "",
            "selftext": p.get("selftext") or "",
            "snippet": (p.get("selftext") or "")[:200],
            "score": p.get("score", 0),
            "num_comments": p.get("num_comments", 0),
            "created": p.get("created_utc") or p.get("created") or 0,
            "comments": comments,
        })
    return cands


# --- analysis ----------------------------------------------------------------
def tag_spots(text):
    return [name for name, rx in SPOT_RX.items() if rx.search(text)]


def relevance(text, spots):
    if spots:
        return "high"
    if GEO_RX.search(text) and KITE_RX.search(text):
        return "high"
    if KITE_RX.search(text):
        return "medium"
    return "low"


def discover_spots(text, counter, samples, threads_seen, thread_key):
    """Pull unknown place names from text and tally them per-thread."""
    known_lower = {n.lower() for n in SPOT_META}
    found = set()
    for m in PLACE_SUFFIX_RX.finditer(text):
        phrase = f"{m.group(1)} {m.group(2)}".strip()
        found.add(re.sub(r"\bRes\b", "Reservoir", phrase))
    for m in PLACE_LAKE_PREFIX_RX.finditer(text):
        found.add(f"Lake {m.group(1)}")
    for name in found:
        key = name.lower()
        if key in PLACE_STOPWORDS or key in known_lower:
            continue
        if key.split()[0] in NAME_STOPWORDS:
            continue  # regex grabbed a sentence fragment, not a place name
        if any(rx.search(name) for rx in SPOT_RX.values()):
            continue  # already a known spot under a different spelling
        if thread_key in threads_seen.setdefault(key, set()):
            continue  # count a spot once per thread
        threads_seen[key].add(thread_key)
        counter[name] = counter.get(name, 0) + 1
        if name not in samples:
            pos = text.lower().find(key)
            snippet = text[max(0, pos - 60):pos + 80].strip()
            samples[name] = re.sub(r"\s+", " ", snippet)[:160]


def region_guess(text):
    t = text.lower()
    # Colorado *River* spots (Havasu, Mohave, Parker) are AZ/NV, not local.
    if any(w in t for w in ("havasu", "mohave", "colorado river", "arizona",
                            "nevada", "las vegas")):
        return "Arizona / Nevada (far)"
    if "wyoming" in t or "laramie" in t or "cheyenne" in t:
        return "Wyoming"
    if "nebraska" in t or "mcconaughy" in t:
        return "Nebraska"
    if "utah" in t or "strawberry" in t or "salt lake" in t:
        return "Utah"
    if any(w in t for w in ("denver", "boulder", "front range", "fort collins",
                            "pueblo", "steamboat", "loveland", "longmont")):
        return "Colorado"
    if "colorado" in t:
        return "Colorado"
    return "Colorado / Wyoming region"


# --- main --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Kite Wind Watch Reddit spot scraper")
    ap.add_argument("--no-sync", action="store_true",
                    help="skip reddit-cli sync; re-mine the existing mirror only")
    args = ap.parse_args()

    if not os.path.exists(REDDIT_CLI):
        print(f"ERROR: reddit-cli not found at {REDDIT_CLI}. Set $REDDIT_CLI or "
              "build tools/reddit-cli.", file=sys.stderr)
        return 2

    if not args.no_sync:
        if not rcli_session_ok():
            print("reddit-cli session not ready (cookie expired?). Re-capture "
                  "with `reddit-cli auth import`, then retry. Keeping existing "
                  "data — not overwriting.", file=sys.stderr)
            return 1
        do_sync()

    candidates = load_candidates()
    if not candidates:
        print("No threads in the mirror. Run a sync first (drop --no-sync). "
              "Keeping existing data — not overwriting.", file=sys.stderr)
        return 1

    # ---- analyse -----------------------------------------------------------
    spot_counts, spot_sample = {}, {}
    disc_counts, disc_sample, disc_threads = {}, {}, {}
    posts_out = []
    for c in candidates:
        full = " ".join([c["title"], c["selftext"],
                         " ".join(c["comments"])]).strip()
        if not full:
            continue
        if not KITE_RX.search(full):
            continue
        # Kitesurfing only: a snow/wing term in the title => that sport => drop.
        if SNOW_TITLE_RX.search(c["title"]):
            continue
        # Also drop snow/wing threads that lack any water-kite context.
        if SNOW_RX.search(full) and not WATER_RX.search(full):
            continue
        spots = tag_spots(full)
        rel = relevance(full, spots)
        if rel == "low":
            continue
        for s in spots:
            spot_counts[s] = spot_counts.get(s, 0) + 1
            spot_sample.setdefault(s, c["snippet"] or full[:160])
        discover_spots(full, disc_counts, disc_sample, disc_threads, c["id"])
        posts_out.append({
            "title": c["title"] or c["url"],
            "subreddit": "r/" + c["subreddit"],
            "url": c["url"],
            "snippet": c["snippet"] or full[:200],
            "spots": spots,
            "relevance": rel,
            "score": c["score"],
            "num_comments": c["num_comments"],
            "created": c["created"],
            "read_full": bool(c["comments"]),
        })

    posts_out.sort(key=lambda p: (p["relevance"] != "high",
                                  -len(p["spots"]), -(p["num_comments"] or 0)))
    posts_out = posts_out[:MAX_POSTS]

    # known-spot aggregation (for the chip row)
    spots_out = []
    for name, n in sorted(spot_counts.items(), key=lambda kv: -kv[1]):
        where = SPOT_META.get(name, ("", "Colorado / Wyoming"))[1]
        spots_out.append({
            "name": name, "where": where, "mentions": n,
            "known": name in KNOWN_SPOTS,
            "dad": name in DAD_SPOTS,
            "blurb": (spot_sample.get(name, "") or "")[:160],
        })

    # NEW spots the dashboard doesn't track yet, ranked by thread mentions
    discovered_out = []
    for name, n in sorted(disc_counts.items(), key=lambda kv: -kv[1]):
        if n < 2 and not GEO_RX.search(disc_sample.get(name, "")):
            continue  # weak single mention with no regional anchor — skip
        discovered_out.append({
            "name": name, "mentions": n,
            "region_guess": region_guess(disc_sample.get(name, "")),
            "quote": disc_sample.get(name, ""),
        })
    discovered_out = discovered_out[:20]

    # dad-spot status (reads comment bodies, so a buried mention still counts)
    alltext = " ".join(" ".join([c["title"], c["selftext"],
                                 " ".join(c["comments"])]) for c in candidates)
    dad_out = []
    for name in DAD_SPOTS:
        hit = DAD_RX[name].search(alltext)
        dad_out.append({
            "name": "Lake Hattie Reservoir" if name == "Lake Hattie" else name,
            "status": "chatter" if hit else "quiet",
            "note": ("Riders are talking about it on Reddit." if hit
                     else "No Reddit chatter surfaced yet. Likely a local / "
                          "word-of-mouth spot."),
        })

    threads_read = sum(1 for c in candidates if c["comments"])
    out = {
        "generated_at": date.today().isoformat(),
        "source": "Reddit (full threads via reddit-cli)",
        "region": "Colorado + Wyoming (and driveable neighbours)",
        "subreddits": ALL_SUBS,
        "threads_found": len(candidates),
        "threads_read_full": threads_read,
        "note": "Regenerated by scraper/scrape_reddit.py (reads full comment "
                "trees via reddit-cli).",
        "spots": spots_out,
        "discovered_spots": discovered_out,
        "dad_spots": dad_out,
        "posts": posts_out,
    }

    if not posts_out:
        print("No kite-relevant posts after filtering. Keeping existing data — "
              "not overwriting.", file=sys.stderr)
        return 1

    DATA.mkdir(exist_ok=True)
    (DATA / "discourse.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False))
    (DATA / "discourse.js").write_text(
        "// Auto-generated by scraper/scrape_reddit.py — do not hand-edit.\n"
        "window.KWW_DISCOURSE = "
        + json.dumps(out, indent=2, ensure_ascii=False) + ";\n")
    print(f"\nWrote {len(posts_out)} posts, {len(spots_out)} known spots, "
          f"{len(discovered_out)} NEW discovered spots "
          f"(mined {threads_read} full threads) -> data/discourse.{{json,js}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
