---
date: 2026-06-17
time: 15:15
project: wayloft
status: in-progress
next-session: Build Batch 3 (Burn) in projects/wayloft/design/screens.html — full deals feed where "watching" filters the feed (show a "watching United" filter state, not explained in copy), plus the full trip check. Add empty states for Burn. Then Batch 4 (Mobile). Re-center apps/web only after all screens are designed. Read ~/.claude/design.md before designing.
---

# Session: Wayloft Batch 2 designed (Today + Earn)

Continues from `2026-06-17-1337-wayloft-setup-batch1-and-design-standard.md`. Lane
is Editorial Cream squared (Direction A); locked tokens live in the 13:00
checkpoint.

## What we worked on

Built and verified Batch 2 of the static design system: three new screens added
to `projects/wayloft/design/screens.html` (sections 03, 04, 05). Desktop copy
refreshed at `~/Desktop/wayloft-screens.html`. Batch 2 ticked in `in-progress.md`.

## Decisions made

**1. Batch 2 = three screens, not two.** Annabel chose to build Today's first-run
(empty) state in addition to the full Today, matching how Setup got two screens.
So Batch 2 shipped: 03 Today first-run, 04 Today full, 05 Earn full.

**2. Reason chip = single outlined chip, no helper sentence.** On Earn
get-next-card the "watching drives the pick" link reads as one chip:
"because you watch United". No explanatory subtitle (stays on the no-helper-
one-liners rule). The get-next-card *why* line is real content (your 38,420
Chase points can't move until you add a Sapphire), not a tagline.

**3. Today layout = lead nudge + Watching + Wallet glance.** Full Today anchors
on one espresso lead nudge ("United transfer bonus is live. Move Chase points to
United at 30% extra. Ends Jun 30"), eyebrow "Because you watch United". Below:
two-column Watching (program + route rows, green/idle status dots, "moved"/
"seats" tags) and Wallet glance (read-only balances with updated/not-set stamps,
plus a "best card to use now → Open Earn" pointer).

**4. Earn = wallet coach + get-next-card, read as one argument.** Wallet coach
flags groceries (activate 5x this quarter, +6,000 pts) and shows dining/travel as
"no bonus card yet" — those muted rows deliberately set up why the next card
matters, so the screen reads top to bottom into the Sapphire recommendation.
United Explorer shown as a smaller runner-up so the pick doesn't look hard-coded.

## New CSS components added (reuse in Batch 3/4)

`.lead` (espresso anchor nudge) + `.lead.locked` (dashed empty variant);
`.wrow`/`.wsub` (watching status rows with `.dot`/`.dot.idle`); `.bal` (wallet
glance row); `.coach`/`.coach.ok` (wallet coach grid); `.tag.reason` (outlined
accent reason chip).

## Verification

Served the dir over `python3 -m http.server` and screenshotted via Playwright
(file:// is blocked in the browser MCP). All three screens render on-standard;
only console error was a harmless favicon 404. Screenshots in
`projects/wayloft/design/screenshots/`: `batch2-today-first`, `batch2-today-full`,
`batch2-earn`, `batch2-earn-runnerup`.

## Next steps

1. Batch 3: Burn — full deals feed (watching filters it; show the filter state in
   UI, e.g. a "watching United" filter pill, not in copy) + full trip check +
   Burn empty states.
2. Batch 4: Mobile views of key screens + final polish.
3. Then re-center `apps/web` into Editorial Cream squared (full re-center steps +
   locked tokens are in the 13:00 checkpoint).

## Context to preserve

- Living spec: `projects/wayloft/design/screens.html`. Tracker:
  `projects/wayloft/design/in-progress.md`. Design standard: `~/.claude/design.md`
  (read before designing).
- Real setup drives content: Chase Freedom Flex held, Sapphire is the next-card
  pick (unlocks transferability of 38,420 UR), watching United + Star Alliance +
  Hyatt/Marriott, routes NYC→Lisbon / NYC→London.
- Verify static screens via local http.server + Playwright; file:// is blocked.
