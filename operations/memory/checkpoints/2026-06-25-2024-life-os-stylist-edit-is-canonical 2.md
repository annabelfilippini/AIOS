---
date: 2026-06-25 20:24
project: life-os
status: in-progress
type: checkpoint
slug: life-os-stylist-edit-is-canonical
---

# Life OS — stylist Edit is now THE Edit; hanger opens the matched look

## Where we landed
The three half-versions are now one. The Day (planner) + the **stylist** Edit
(calendar event → outfit from clothes she owns) are a single app, and the
per-event hanger on the planner opens the matching look in The Edit, outlined,
with a "dressing for <event>" banner above it. Verified in-browser end to end.

## What changed this session
- **Outfit affordance icon**: planner's per-event wear button was using
  `sparkles` (which already means "AI generate" on Structure-my-day + email
  draft) and `star` was taken by the Inbox "Starred" badge. Added a dedicated
  `hanger` icon and pointed the wear button at it.
  `projects/day-planner/planner.html:422` (icon), `:754` (use).
- **Stylist Edit is canonical and in-repo**: saved the page she approved
  ("This Week, From Your Closet") as `projects/style-feed/the-edit.html`
  (off the Desktop). Font unified to Cormorant Garamond. Each look card tagged
  `data-occ`: Airport & Travel=`vacation`, Family Pictures=`casual`,
  Alex's Birthday=`going-out`, Vail Daytime=`active casual`.
- **Shell composes the stylist Edit, not the old shopping feed**:
  `projects/life-os/serve.py` `EDIT_HTML` → `the-edit.html` (was `feed.html`).
- **Cross-module link rewritten** (serve.py `_ROUTER_JS` + `_SHELL_CSS`):
  `window.LifeOS.goToEdit(occ, ctx)` now finds the look via
  `#view-edit .card[data-occ~="occ"]`, scrolls to it, adds a `los-flash`
  outline (`@keyframes losflash`), and inserts the `#los-edit-banner` directly
  above that look. Replaced the old occbar-chip filtering. `--selfcheck` passes.

## How it runs / verifies
- `cd projects/life-os && python3 serve.py 8800 --no-open` (subclasses
  day-planner's Handler; reuses calendar/email/inbox + The Edit's /feedback,/img).
- Gate key (THEDAY_KEY in day-planner/.env): append `?k=<key>`.
- Selfcheck (no server): `python3 serve.py --selfcheck`.
- Verified: hanger on Airport(vacation) → Edit opens on "Airport & Travel",
  flashed, banner "From The Day · dressing for Airport · 10:45 AM" above it.
- Gotcha: changing only the URL `#hash` does NOT reload the page (stale DOM);
  hard-reload when re-testing after a serve.py edit.

## Known rough edge
The 4 looks are pinned to her REAL Jun 25–28 events (Airport, Pictures,
Birthday, Vail), so occasion matching is approximate. `vacation`→Airport and
`going-out`→Birthday are exact; a gym event (`active`, e.g. today's Strength)
maps to the closest casual look (Vail Daytime) since there's no athleisure look
in the set; `work` has no look → falls back to scrolling to top of The Edit.
Real fix later: generate a look per event, not per generic occasion.

## Cleanup still pending (blocked by safety classifier — Annabel to run)
Superseded proofs + unused feed, all safe to remove (feed.html regenerable via
build_feed.py; the rest are disposable):
```
rm "projects/life-os/life-os.html" \
   "projects/style-feed/lookbook.html" \
   "projects/style-feed/feed.html" \
   ~/Desktop/the-edit-this-week.html \
   ~/Desktop/life-os-preview.html
```

## Next
- Run the cleanup above.
- Decide: generate per-event looks (closes the rough edge) and/or build
  `style-feed/data/closet.json` so guessed staples (black Aritzia trouser, her
  jeans) persist across runs instead of being re-guessed.
