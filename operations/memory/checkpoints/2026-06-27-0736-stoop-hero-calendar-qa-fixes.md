---
date: 2026-06-27 07:36
project: stoop
status: in-progress
type: checkpoint
slug: stoop-hero-calendar-qa-fixes
---

# Stoop — Delaney page layout QA: calendar overlap, about width, hero ring

Follows `2026-06-26-2115-stoop-delaney-page-real-identity-and-photo.md`. Same v1
file (`projects/stoop/cousin-lacrosse.html`). Annabel reported three layout
defects from phone screenshots; all three fixed and QA'd live. Reviewed in her
real browser, she approved ("this looks good").

## What was broken (root causes, not symptoms)
1. **Request bar overlapped the bottom calendar week.** Root cause was NOT the
   reqbar (the prior "make it static" fix was treating a symptom). The real bug:
   `.cell{aspect-ratio:1/.74}` on `repeat(7,1fr)` grid items rendered the cells
   ~88px taller than the `.month` grid box, so the last row (28/29/30) overflowed
   *below* the box and the reqbar drew on top of it. Measured: cellOverflow 88px,
   reqbar top above last-cell bottom.
2. **About section didn't fill the space / half-width divider line.**
   `.about{max-width:620px}` left-aligned, so the `border-top` divider and text
   only covered the left ~half on wide views; dead space on the right.
3. **Hero ring + center-line looked "weird on top," not centered.** The field
   center-line + face-off ring were pinned to the hero's vertical middle
   (`top:50%`) while the avatar sat at the top — visually disconnected.

## Fixes (all in cousin-lacrosse.html `<style>`)
- `.cell`: removed `aspect-ratio:1/.74` → `min-height:50px`. Deterministic row
  height, grid box wraps its rows, overflow gone. (ponytail comment in source.)
- `.about`: removed `max-width:620px`; added `.about p{max-width:60ch}` so the
  divider spans full width and mobile fills edge-to-edge, while desktop lines
  stay a readable measure.
- `.hero-line`: moved from `top:50%` to `top:96px` (hero padding-top 44 + half
  the 104px avatar = avatar center); ring `::after` enlarged 62px→150px and
  re-centered so it frames the avatar like a face-off circle. **Hardcoded to the
  104px avatar size — recompute `top` if the avatar is resized** (a noted comment
  + relevant because "bump avatar larger" is still pending).

## Verified
preview MCP server `stoop` on port 8762 (added to `.claude/launch.json`),
`projects/stoop/cousin-lacrosse.html`. Mobile 375 + desktop 1280: cellOverflow
0, reqbar 18px below last row, avatar center 98px, about full-width, no console
errors (favicon 404 only, historically). Annabel opened it in her real browser.

## Decided this session: NEXT = make "Request a lesson" actually send (Option A)
Laid out the fork and Annabel implicitly accepted the framing by saving here.
The page LOOKS done but is still a demo in two ways: (1) **"Request this lesson"
goes nowhere** — the modal just swaps to a fake "Request sent!" view, no real
send; this is the load-bearing v1 promise ("routes to her parent"). (2)
availability is hardcoded Tue/Thu/Sat.

**Recommended next = Option A: make the request genuinely land.** Lazy/backendless
plan: the "Send request" button opens a pre-filled `mailto:`/`sms:` to Delaney's
parent with the picked time + kid name + contact + note. Turns the page from demo
into a real shareable link ("prove the link first" thesis). **BLOCKER before
building: need the destination from Annabel** — parent's email, a phone number
for SMS, or both. Not yet provided.

Deferred (v2+, do not start before A): availability editor (`?edit=1`), builder
flow (5 questions → page), parent dashboard, the hyperlocal feed,
theme-follows-visitor (needs a backend; localStorage is per-browser).

Still concept/preview stage. Avatar is still the full-motion action crop; tighter
face/upper-body re-crop + larger size both still offered, still undecided.
