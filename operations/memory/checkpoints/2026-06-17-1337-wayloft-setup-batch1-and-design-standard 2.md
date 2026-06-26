---
date: 2026-06-17
time: 13:37
project: wayloft
status: in-progress
next-session: Build Batch 2 of the static design system, refined Today + full Earn, in projects/wayloft/design/screens.html. In Earn, make "watching" visibly drive the get-next-card pick (e.g. a "because you're watching United" reason chip). Then Batch 3 (Burn), Batch 4 (Mobile). Re-center the real app only after all screens are designed. Read ~/.claude/design.md before designing.
---

# Session: Wayloft Setup designed (Batch 1) + global design standard created

Continues from `2026-06-17-1300-wayloft-design-direction-a-chosen.md` (Direction A,
Editorial Cream squared, locked tokens live there).

## What we worked on

Chose to design the whole system in static HTML first, then rebuild the app once.
Built Batch 1 (Setup), took strong copy feedback from Annabel, and set up a global
design standard.

## Decisions made

**1. Path: full system in static HTML before code.** 4 batches:
1 Setup (done), 2 Today + Earn, 3 Burn + empty states, 4 Mobile + polish. Then one
clean re-center of `apps/web`.

**2. Batch 1 built and verified: Setup.** First-run (empty state) and full
(populated) at `projects/wayloft/design/screens.html`. Desktop copy:
`~/Desktop/wayloft-screens.html`. Browsable, jump-index, batches 2 to 4 marked soon.

**3. Strong copy rule from Annabel: kill all helper one-liner subtitles.** She
hates explanatory/reassuring subtitles under headings ("The cards you actually
carry.", "Unlocks once you add a card.", "Four quick things..."). Removed all of
them from screens.html. Headings now stand alone. Where a subtitle was explaining
mechanism, replaced it with self-evident UI (balances now show "updated Jun 14" /
"not set yet" stamps instead of a sentence). Saved as feedback memory
`no-helper-one-liners` and added to the global design standard.

**4. Product logic clarified with Annabel:**
- **Points balances** = manual entry in v1 (no bank-sync tool assumed). The
  "updated / not set yet" stamps make staleness visible. Later option: scrape from
  her logins (fragile).
- **Watching a program/route** drives three things: filters the Burn deals feed,
  tilts the Earn get-next-card recommendation toward cards that feed that program
  (watching United pushes Sapphire + United co-brands up), and preloads trip
  checks. Must be shown in the Earn design via a reason chip, not explained in copy.

**5. Global design standard created: `~/.claude/design.md`.** Project-agnostic
craft rules + Annabel's default taste (no one-liner subtitles, let UI show
function, serif display + grotesque body + mono figures, one restrained accent,
squared corners, real content, no dashes in copy). CLAUDE.md now has a Working
Style bullet: read `~/.claude/design.md` before designing any website or UI.

## Open questions — RESOLVED 2026-06-18

- **design.md placement: LEAVE at `~/.claude/design.md`.** Not moving into AI-OS.
- **Seats.aero data: SESSION-SCRAPE** (no Pro subscription). Follow the
  reddit-cli / ShopMy pattern: authenticated browser cookie, re-import when it
  expires. Scraper runs locally with Annabel's session, then writes results up.
- **Storage: SUPABASE** (not local-first). Note the interaction with the
  scrape decision: the scraper still runs locally (it needs Annabel's authed
  session — it can't be a pure Supabase serverless job), then pushes award data
  into Supabase. Supabase = storage + auth + cross-device sync; the scraper is a
  separate local/owned-box job that writes to it. Supabase is NOT yet configured
  (per stack rule) — standing it up is a re-center-phase task.

## Next steps

1. Batch 2: refined Today + full Earn (wallet coach + get-next-card with the
   watching reason chip). Verify in browser, update Desktop copy.
2. Batch 3: Burn (full deals feed + full trip check) + empty states.
3. Batch 4: Mobile views + polish.
4. Then re-center `apps/web` into Editorial Cream squared (see the 13:00
   checkpoint for the full re-center steps and locked tokens).

## Context to preserve

- Living spec: `projects/wayloft/design/screens.html`. Batch tracker:
  `projects/wayloft/design/in-progress.md`. Screenshots:
  `projects/wayloft/design/screenshots/`.
- Locked tokens and the re-center plan are in the 13:00 checkpoint.
- Annabel's real setup drives content: Chase Freedom Flex held, Sapphire is the
  next-card pick (unlocks transferability), watching United + partners and hotels.
