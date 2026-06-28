---
date: 2026-06-28
time: 12:58
project: stoop
status: in-progress
next-session: Pick a deferred item — recommend #2 hood-tag the NEIGHBORS teaser stubs (no backend) to make the feed feel real
---

# Session: Stoop — stand-creation now asks for a neighborhood + photo copy cleanup

Follows `2026-06-28-1234-stoop-batch3-hood-filter-role-home.md`. All work in the single
file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## What we worked on
Bug Annabel hit: creating a stand never asked for a neighborhood — it silently
defaulted to country-club. Plus a copy cleanup on the photo step.

## What shipped
**Neighborhood step on stand creation.** Root cause: the geo picker (`view-neighborhood`,
"Where's your stand?") only ran on the front-door role-card path (`chooseRole`). Every
in-feed CTA jumped straight to `go('onboard')`, skipping it, so the stand inherited
`account.hoods[0]` or `'country-club'`.
- New `startStand()` helper (near `chooseRole`, ~line 608): always routes through the
  geo picker as a seller, pre-selecting the current hood (`pickedHoods=[account.hoods[0]]`)
  so a returning seller just confirms with one tap ("This is my spot →").
- Wired all three creation CTAs to it: home hero "Start my own stand" (line 343),
  add-stand card (line 686), `mk-add` "Set up your stand" (line 873). The `go('onboard','edit')`
  Edit button and internal `!profile` guards left alone (they shouldn't re-pick).
- Note: dropped an earlier short-circuit (seller-with-hood → skip geo) because it was
  exactly why Annabel never saw the step while testing as an existing seller.

**Copy cleanup.** Photo step: removed the helper subtitle ("A picture of you doing your
thing, like Delaney out on the field…") and renamed the h2 from "Your photo" to
"Profile picture". One clean label, no helper one-liner.

## Decisions made
- Stand creation always shows the neighborhood step (pre-filled), rather than skipping
  it for returning sellers. Matches Annabel's expectation that creating a stand asks where.

## Open questions
- None new. Prior empty-feed UX question still open (just-CTA vs "invite a neighbor" prompt).

## Next steps (deferred, none picked)
- **#2 Hood-tag the NEIGHBORS teaser stubs** (Mateo/Priya) — no-backend, makes the feed
  show >1 stand. Recommended next move.
- **#1 Multi-stand feed** — single profile slot → multi-stand; needs a backend.
- **#3 Parent view** — approve-orders / see-the-money rail; not built; project doc calls
  it load-bearing.
- Richer empty-feed state; real SMS/backend confirmations; per-week "copy to next 4 weeks".

## Context to preserve
- Could not drive the live preview this session: port 8762 and the Playwright browser
  were both held by another chat. Verified via `node` script-parse (clean) + static trace
  of `startStand` → `initGeo` → `renderHoods` (pre-selected hood reveals the geo-go button).
  Annabel should hard-refresh (Cmd+Shift+R) if the change doesn't appear — browser cache
  is the remaining suspect.
- Data model unchanged: `account={role,hoods:[],contact?,name?}` in `stoop-account-v1`;
  one `profile` in `stoop-profile-v2`. `selMode==='one'` = seller (single hood).

## System refinement candidates
- None this session.
