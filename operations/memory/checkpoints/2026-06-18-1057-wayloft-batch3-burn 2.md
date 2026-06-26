---
date: 2026-06-18
time: 10:57
project: wayloft
status: in-progress
next-session: Build Batch 4 (Mobile) in projects/wayloft/design/screens.html — mobile views of the key screens (Today, Earn, Burn deals, Burn trip check) + final polish. Then re-center apps/web into Editorial Cream squared (full re-center steps + locked tokens are in the 2026-06-17-1300 checkpoint). Read ~/.claude/design.md before designing.
supersedes: 2026-06-17-1515-wayloft-batch2-today-earn.md
---

# Session: Wayloft Batch 3 designed (Burn) + plain-language preference recorded

Continues from `2026-06-17-1515-wayloft-batch2-today-earn.md`. Lane is Editorial
Cream squared (Direction A); locked tokens in the 13:00 checkpoint.

## What shipped

Built and verified Batch 3: three Burn screens added to
`projects/wayloft/design/screens.html` (sections 06, 07, 08). Desktop copy
refreshed at `~/Desktop/wayloft-screens.html`. Batch 3 ticked in `in-progress.md`.

- **06 Burn first-run (empty)** — `.emptybox` "No trips checked yet", a real
  status stamp "Watching 4 programs · 2 routes" (status, not a helper subtitle),
  Check a trip / Browse deals CTAs.
- **07 Burn deals feed** — filter state shown in UI not copy: `.filterbar` of
  `.fchip` pills (United active w/ dot + counts, Star Alliance, Hyatt, All).
  Feed of `.deal` rows (badge + route/opportunity + price + tag). Gated deals
  carry a muted `.tag.lock` ("needs Sapphire") that points back to Earn.
- **08 Burn trip check** — the core decision surface. `.tripin` set-value inputs,
  then a three-way `.compare`: Pay cash $720 / Points today (`.opt.dead` Locked,
  0 transferable) / The smart path (`.opt.pick` crowned "Best", 35,000 + $80,
  2.1¢/pt, saves $640). Verdict banner reuses `.lead` → "See the path → Earn".

## Key decision

**Trip check shows the real situation, not an aspirational one.** Annabel chose
this: points are genuinely locked (Freedom Flex only, UR can't transfer), so the
points column reads Locked and the smart path is gated behind the Sapphire. This
makes Burn and Earn point at each other and read as one coherent argument, same
as Earn was built.

## New CSS components (reuse in Batch 4)

`.filterbar`/`.fchip` (+ `.on`, `.dot`, `.ct` count); `.deal` (+ `.badge`,
`.ttl`, `.price`); `.tag.lock` (muted gated variant); `.tripin`/`.ti`
(set-value inputs); `.compare`/`.opt` (+ `.opt.dead`, `.opt.pick`, `.crown`);
`.cpp` (green mono cents-per-point readout).

## Verification

Served the dir over `python3 -m http.server 8809` and screenshotted via
Playwright (file:// blocked). All three render on-standard; only console error is
the harmless favicon 404. Screenshots in `projects/wayloft/design/screenshots/`:
`batch3-burn-first`, `batch3-burn-deals`, `batch3-burn-tripcheck`.
Note: the Playwright MCP chrome profile was locked by a stale process at first;
`pkill -f ms-playwright-mcp/<profile>` then re-navigate cleared it.

## Also this session

Recorded a communication preference in `~/.claude/CLAUDE.md` (Working Style):
when introducing an unfamiliar concept/tool/tradeoff, explain it in plain
language the first time, before jargon, without being asked. Triggered by
Annabel liking how the Earn/Burn "locked points" mechanic was explained.

## Next steps

1. Batch 4: Mobile views of key screens (Today, Earn, Burn deals, Burn trip
   check) + final polish. Verify in browser, refresh Desktop copy.
2. Then re-center `apps/web` into Editorial Cream squared (steps + locked tokens
   in the 2026-06-17-1300 checkpoint).

## Context to preserve

- Living spec: `projects/wayloft/design/screens.html`. Tracker:
  `projects/wayloft/design/in-progress.md`. Design standard: `~/.claude/design.md`.
- Real setup drives content: Freedom Flex held, 38,420 Chase UR locked (no
  transfer-partner card), Sapphire is the next-card unlock, watching United /
  Star Alliance / Hyatt / Marriott, routes NYC→Lisbon / NYC→London.
- Verify static screens via local http.server + Playwright; file:// is blocked.
