---
date: 2026-06-13
time: 15:54
project: websites / system + freeride-tarifa
status: done
next-session: Built the 3-layer website doc system (global design.md + per-project design.md + NEW content.md facts layer), a process CLAUDE.md at projects/websites/, a _template/ to copy for new sites, and a Stop hook (~/.claude/hooks/update-design-docs.sh) that nags to update design.md/content.md when site CODE changed but the docs didn't. THEN populated the first real example: freeride-tarifa/content.md (business basics, full lesson + rental price tables, IKO roadmap, the 21-venue Tarifa guide with Google ratings, source log), with verified/recheck/unconfirmed flags. Next: populate content.md for the other active projects (vital-health-review next) by copying _template/ and filling facts the same way. ACTION FOR ANNABEL: confirm with Free Ride whether homepage names "Oleg" (instructor) and "Leah" (rider) are real people or replace them (no-invented-people rule); both are flagged [unconfirmed] in content.md so they can't ship as fact. NOTE: vital-health-review/media/design.md is intentional (their social-media design guidelines) — leave it, not a stray.
---

# Session: Website design.md / content.md doc system + update hook + freeride content.md

## What we worked on

Annabel wants a repeatable "take any website and redo it" setup (kitesurf,
restaurant, hotel, etc.) governed by a global design.md plus per-project design
files, like CLAUDE.md but for website design. She asked to (1) document how the
process works in a CLAUDE.md, and (2) add a hook that enforces updating each
project's design.md + content.md (and the global one if needed) when working on
a site. Discovered the global design.md and freeride design.md already existed
and are strong, so this was about adding the missing layers + wiring, not a
rewrite. Then built the first real content.md as a worked example.

## The system (three layers)

1. `projects/websites/design.md` — GLOBAL taste + standards (already existed,
   514 lines, left intact; only added a short "layer 1 of three" preamble
   pointer).
2. `projects/websites/<project>/design.md` — BRAND direction + iteration log.
3. `projects/websites/<project>/content.md` — NEW. Verified FACTS layer. Source
   of truth that keeps the build from inventing things. Split test: "would it
   change between two clients?" yes = project level, no = global.

## Files created / changed

- NEW projects/websites/CLAUDE.md — process doc / system outline (router style:
  3 layers, read order, split test, start-a-new-site, build-from-content.md,
  keep-docs-current). Auto-loads when working under projects/websites/.
- NEW projects/websites/_template/design.md — fill-in brand-brief skeleton.
- NEW projects/websites/_template/content.md — verified-facts skeleton with
  status legend ([verified]/[recheck]/[unconfirmed]), source log, no-invented-
  bios guardrail.
- EDIT projects/websites/design.md — added a 6-line preamble naming the 3
  layers. Body untouched.
- NEW ~/.claude/hooks/update-design-docs.sh — Stop hook.
- EDIT ~/.claude/settings.json — registered the hook FIRST in the Stop list.
- NEW projects/websites/freeride-tarifa/content.md — first real example (below).
- EDIT projects/websites/freeride-tarifa/design.md — iteration-log entry noting
  facts now live in content.md.

## Hook behavior (update-design-docs.sh)

Modeled on reflect-on-session.sh (transcript-gated, .state marker, once per
session, decision:block). If real SITE CODE changed (.html/.css/.js/.ts/.jsx/
.vue/.astro/.svelte/.liquid) but NO project design.md/content.md was updated this
session -> block with a reminder to update design.md (dated iteration entry) +
content.md, and promote to global design.md if a preference is universal. Self-
suppressing: silent on non-website sessions, silent when docs were already
updated, with an explicit "say so in one line and stop" escape hatch. Editing
only research .md notes does NOT trigger it. Verified with 3 synthetic
transcripts (fires / silent / silent); settings.json re-validated with jq.

## freeride-tarifa/content.md (first worked example)

Facts pulled from the as-built pages (index/lessons/rent/tarifa.html, June 2026),
NOT from memory. Captured: founded 2016, WhatsApp +34 601 655 993,
freeridetarifa.com, IKO certified, max 4 students/instructor, FR/EN/ES, the three
beaches (Los Lances/Valdevaqueros/Balneario), 300+ wind days; full lesson price
tables (Group/Couple/Semi-private/Private x 1-5 days) + IKO roadmap; full rental
pricing (packs, boards, full packs, rescue cards, level check) + rider
requirements; the 21-venue Tarifa guide across 5 categories with Google ratings,
review counts, and map-query strings; a source log.

- Flags: prices = [recheck] (live site, June 2026); all Google ratings/review
  counts = [recheck] (captured 2026-06-11); kite-camp specifics = [unconfirmed].
- KEY FINDING: homepage draft names "Oleg, kite instructor" and "Leah, from Lake
  Constance" — unclear if real or invented during the build. Both flagged
  [unconfirmed]; needs Annabel to confirm with Free Ride (no-invented-people
  rule). Coach "Amaury" appears inside a real-looking Google review, likelier
  genuine.

## Notes / open

- content.md was deliberately NOT auto-populated from memory for any project;
  freeride was built from its real as-built pages. Same approach for the rest.
- Global design.md was not rewritten; it already encodes "no weird phrases,"
  image-vetting/licensing, and fact-checking rules.
- vital-health-review/media/design.md confirmed intentional (social-media design
  guidelines), not an artifact. Do not move it.
