---
date: 2026-06-25 19:58
project: life-os
status: in-progress
type: checkpoint
slug: life-os-edit-into-planner
---

# Life OS — wire The Edit into the live planner (next build)

## Where we landed
Annabel's north star reconfirmed: **The Day (planner) and The Edit are one app.**
The Edit pivoted this session from a shopping feed into a **stylist**: calendar +
closet + taste → today's outfit, with shopping demoted to an optional "to elevate"
nudge. She does NOT want to photograph her closet; the system infers/guesses.

## Decided this session
- The Edit = stylist, not store. Loop: **calendar event → outfit from clothes she
  owns**, each look pinned to a real event.
- **Stop asking questions.** She wants best-guess judgment: if a piece isn't on
  file, guess a real product from her brands (Aritzia, AGOLDE, Zara, Nuuly stack)
  and label it as a guess. Corrections refine the engine over time.
- Guessed pieces shown with a "my guess" tag; confirmed-owned shown with "yours".

## What got built (proofs, not the final form)
- `projects/style-feed/lookbook.html` — 4 looks for her real Jun 25–28 calendar,
  built from owned pieces + 2 labeled guesses (Aritzia Effortless Pant black,
  AGOLDE Low Rise Loose).
- `projects/life-os/life-os.html` — **standalone** shell, two tabs (The Day / The
  Edit), outfit chip on each event → jumps to matching look + flashes it. This was
  the throwaway proof the link works. Verified: tabs switch, 17 imgs load, 0 broken.

## THE ACTUAL NEXT TASK (what she asked for)
Graft the Edit link **into the real `projects/day-planner/planner.html`** (the live
app talking to `serve.py`), NOT maintain a second file. life-os.html is disposable.

Mechanism (confirmed feasible):
- planner.html builds each event row in JS (template around `planner.html:746`,
  `html+=\`<div class="row"...\``). Add a per-event outfit affordance there.
- Clicking it opens The Edit as an **in-app panel** (slide-over or 2nd tab) scrolled
  to the look matched to that event (match by title/time → look id).
- The Edit panel reuses planner design tokens (already shared:
  `--serif:Cormorant Garamond`, `--bg:#f3efe9`, `--card:#faf8f4`, fn-color dots).
- Data: Nuuly box via `tools/nuuly-cli` (current box = most recent rental order
  date; this week = 6 white/ivory tops, pulled 2026-06-25), `style-feed/data/
  purchases.json`, taste in `style-feed/taste-feedback.md`.

## Design note / open decision
- **Don't reuse the star icon** for outfits — star already = starred/important in
  the Inbox. Use a distinct mark (hanger / outfit dot) on events.
- Open: where Edit-guessed staples (black Aritzia trouser, her jeans) should persist
  so the same guess sticks across runs → propose a small `style-feed/data/
  closet.json` for staples that never came through email. Not built yet.

## Data sources confirmed working
- Nuuly: `nuuly-cli doctor` ok; current box order date 2026-06-11 (6 tops).
- Aritzia images 403 to curl (Cloudflare) but render fine in-browser — verify via
  playwright naturalWidth, not curl.
- scene7 (Nuuly), static.zara.net, agolde.com CDN, goat/farfetch all hotlink.

## Current 6 Nuuly tops (this week)
Free People Forevermore LS (white, her fave), Madewell Leah 60's (white),
Anthropologie ruched asymmetric tee (white), Zemeta Bell Lace (white),
Dolan flutter lace (ivory), Native Youth Broderie back-tie (white).
