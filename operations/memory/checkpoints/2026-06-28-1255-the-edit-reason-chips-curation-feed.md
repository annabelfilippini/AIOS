---
date: 2026-06-28 12:55
project: style-feed
status: in-progress
type: checkpoint
slug: the-edit-reason-chips-curation-feed
---

# The Edit — why-chips on ✕, reason-aware re-rank, curation feed un-hidden

## What happened this session
Annabel felt the feed "wasn't picking up her taste." Diagnosed why, then shipped
reason capture + made the feed usable for active curation. All in
`projects/style-feed/build_feed.py` (the SCRIPT/STYLE strings that generate
feed.html). Served by `serve.py` on 8801.

### Diagnosis (the real problem)
- I CAN see everything: `data/feedback.json` (gitignored — that's why she couldn't
  find it; it's local-only, never on GitHub). ~399♥/444✕ at session start.
- Tags barely separate her taste: **41% of hearts have a tag-for-tag twin in her ✕s**.
  Per-axis the strongest "signal" is whether a field is BLANK (noise). Her profile
  lists the SAME brands (j.crew/zara/dairy boy/tuckernuck) and "relaxed" on BOTH the
  reach-for and pass-on lists. Taste lives in the gestalt, not single coarse tags.
- Only clean tag signal: **open/tie-back wins, closed-back loses** (83♥/152✕).

### Shipped
1. **Why-chips on ✕** — a dark toast slides up when she ✕s a card:
   colour · shape/fit · too dressy · too plain · cheap-looking · not me. Tap →
   writes `reason` onto the disliked record (rides along to feedback.json; serve.py
   stores the whole record so no server change). Auto-hide **8s** (was 5; 5 was too
   short to think). Ignoring it still counts the ✕.
2. **Reason-aware re-rank** in `buildProfile`/`liveScore`: P.rx collects reasons →
   too dressy demotes evening/formal/smart-casual; colour demotes by (1-neut);
   shape demotes that silhouette; cheap demotes that brand. Chip tap calls
   `applyView()` so the feed reshapes on the spot. Lives in the LIVE layer
   (re-derived from saved reasons each load) so it survives nightly rebuilds.
3. **Un-hid the curation feed** — `passesFit` was dropping every un-swiped item with
   `__fit<=0` (only 12 visible!). Changed final `return` to `true`: show ALL
   un-swiped, ranked best-first. Kept accessory cap + loud-color (neut<0.3) cut.
   **Feed went 12 → 108 visible.** With "show everything" OFF, an ✕ removes forever.

Verified live (playwright, DOM reads): toast+6 chips present, ✕ hides the card,
"too dressy" tap stored reason="too dressy" and sank dressy items to the bottom.

## ⚠️ Data integrity note (I caused drift)
Driving the feed in the **automated** browser repeatedly merged its stale
localStorage into `data/feedback.json` (app's "localStorage-wins" hydrate→push).
Counts wobbled 399/444 → 410/433 → 400/443. Restored to session-start
(md5 `b79eaddc05c2b28debbae0be248ad8a1`, **400♥/443✕, 1 reason**) and cleared the
automated browser's localStorage. **True original (399/444) is not perfectly
recoverable** — only her own browser's localStorage is ground truth. On her next
load in HER browser it will heal the file. NEVER drive this feed via automation again.

## State / how to run
- Server is UP: `http://localhost:8801/feed.html` (started fresh end of session).
- `cd projects/style-feed && python3 serve.py` (port 8801).
- feedback.json: 400♥/443✕ (md5 above). feed.html rebuilt from it (build only READS
  the file; md5 unchanged after `python3 build_feed.py`).

## Open / next
- **She should open the feed in her OWN browser**, "show everything" OFF, and curate.
  Reasons start teaching once she logs ~30-50.
- Offered: show the handful of items that disagree between disk and her browser so she
  can spot-check the drift. Not done yet.
- Still open from prior: **RED slips through** (browser has colorfulness `c`, not hue);
  real fix = hard red/burgundy ban server-side (`style_engine.py:29` knows hated colors).
- Optional: fold reasons into the cold `base` (build_feed.py) so cold-start order also
  reflects them; bake "tailored = hard no" into taste-feedback.md.

Related: [[2026-06-28-1225-the-edit-full-catalogue-curated]],
[[project_style_feed]], [[project_the_edit_taste_corrections]], [[project_life_os]].
