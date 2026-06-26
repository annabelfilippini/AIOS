---
date: 2026-06-26 15:05
project: day-planner
status: in-progress
type: checkpoint
slug: morning-edit-shipped-style-next
---

# Morning Edit shipped & wired; next session = make outfits use her real taste

## Where we landed
The Morning Edit (`projects/day-planner/morning.html`) was already built, committed,
and pushed by the prior Hermes session — nothing was lost. This session verified it
end to end against the live server and closed the remaining gaps. It now reads The
Day's live calendar/inbox/mail and The Edit's style data, on one gated server.
Verified in-browser: "Connected to The Day", Google Calendar live (9 events), 3
outfit cards, 0 broken images.

## What changed this session (all pushed to origin/main)
- **"Open The Edit" button + route** (`76d6504` chain): `serve.py` now serves
  `../style-feed/the-edit.html` at `/the-edit.html` (gated, self-contained), and
  morning.html has an "Open The Edit" pill. Relabeled "Open planner" → "Open The Day".
  Both directions of the bridge verified.
- **Refetch on reopen**: morning.html had no polling — it only fetched on first
  load, so reopening the PWA showed a stale view. Added
  `visibilitychange → loadAll()` (refetches all 4 endpoints on return).
- **Mail = recent inbox from real senders** (was the "emails not updating"
  complaint): `/api/emails` (`fetch_pressing_emails` in serve.py) was filtered to
  `is:unread OR is:starred` Primary, so it froze on a June 22 Venmo when nothing
  newer was unread. Changed query to `in:inbox category:primary` newest-first,
  dropping automated senders. Expanded `AUTOMATED_DOMAINS` (venmo/pge/walgreens/
  depop/cash.app/zelle/doordash/instacart) and the glued-localpart keyword check
  (customerservice/service/magiclink/automated/mailer). Stat relabeled
  "pressing mail" → "recent mail". Top of feed is now real people, today first.

## How it runs / verifies
- `cd projects/day-planner && python3 serve.py` (port 8802).
- Gate key = `THEDAY_KEY` in `projects/day-planner/.env`; append `?k=<key>` or
  the link JS auto-appends it to internal hrefs.
- Endpoints (need `X-Day-Key` header or `?k=`): `/api/calendar`, `/api/inbox`,
  `/api/emails`, `/api/style`, `/the-edit.html`.

## NEXT SESSION — the real ask: develop the outfits with her actual taste
She feels her style/preferences aren't being used, and she's right. The outfit
builder (`buildPieces()` / `outfitCopy()` / `banned()` in morning.html, ~line
146–176) is mostly **hardcoded regex keyword matching + canned fallback strings**.
It does NOT consume the rich taste signal that already exists:

- `projects/style-feed/taste-feedback.md` (65 lines) — hand-written per-occasion
  FORMULAS: everyday = relaxed shorts + cream sweater; going-out = sleek black,
  a little satin (Wilfred Martini halter); WORK = ivory clean-neck top + loose
  black/navy trouser + pointed flat; loves black/blue/brown/grey/ecru, matching
  sets; HATES red/burgundy, capri/cropped leggings.
- `projects/style-feed/data/feedback.json` — 278 liked / 334 disliked actual
  hearts/✕ (real learned signal, currently ignored by the builder).
- `projects/style-feed/data/purchases.json` (12 owned) + `style-profile.md` (numbers).
- `/api/style` already returns purchases, 160 topItems, 27 tasteRules — but
  morning.html only uses them as a regex pool, not as ranked taste.

Concrete plan to develop next time:
1. Make the outfit builder actually rank against `feedback.json` likes/dislikes
   and apply the per-occasion formulas from `taste-feedback.md` (not just the
   `banned()` regex). Owned pieces (purchases) should be preferred and labeled
   "Yours" vs guessed.
2. Per-occasion looks should match her stated formulas exactly (work/going-out/
   everyday/active/travel) rather than the generic fallback prose in `outfitCopy()`.
3. Consider generating outfits server-side from the style data (the bridge file
   the prior plan called for) so the logic isn't trapped in inline HTML JS.
4. The "known vs guessed" confidence label should reflect real owned-vs-inferred,
   driven by purchases.json + feedback matches.

Related memory: [[project_the_edit_taste_corrections]], [[project_day_planner]],
[[project_life_os]]. Note life-os already has a *stylist* Edit (calendar event →
outfit from owned clothes) at `projects/style-feed/the-edit.html` — next session
should reconcile morning.html's builder with that stylist approach rather than
duplicate it.
