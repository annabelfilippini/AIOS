# Life OS

Annabel's personal life OS. One app that holds the parts of her she's put to
the side (fashion, day/to-dos, finances, investing) plus an agent that can
reason across all of it and act on her behalf.

This is the north star. Build toward it one daily-use module at a time.

## The end goal

A single personal life OS, not three separate apps. The value is the
**cross-module reasoning** no off-the-shelf app gives her: the thread between
modules.

> Friday dinner on the calendar (The Day) → suggested outfit (The Edit) →
> reminder to put it on the Amex because she's $40 from the dining credit
> (Wayloft / Money).

That calendar → wardrobe → card chain is the soul of the project. The unifying
asset is **her data**, not the model. The model is a swappable brain.

## Architecture (three layers)

1. **Shell** — one app, tabs: The Day, The Edit, Money. v0s of the first two
   already exist.
2. **Life-data layer** — the shared store underneath: calendar, wardrobe + taste,
   accounts + spending, eventually holdings. Every tab reads/writes here. This is
   what makes cross-module reasoning possible. Build it early even as simple files.
3. **Agent (the dial)** — one brain that reads across everything, swappable
   between GLM / Opus / a future local model via one config line
   (`MODEL_ENDPOINT`, `MODEL_KEY`, `MODEL_NAME`). Never hardcode a provider.

Most personal-app projects die because the tabs are built as separate islands.
The middle layer is what makes this compound.

## Build sequence (do NOT build it all at once)

Win condition: one module so useful she opens it every day, then accrete.

1. **The Day — the spine.** Daily return point, already wired to her real Google
   Calendar, and every cross-module trick keys off a calendar event. Status: good
   as-is (shipped 2026-06-23, phone access + mobile UI). She'll adjust as she sees fit.
2. **The Edit — the joy.** Already has momentum (style-feed). Bring it into the
   same shell next. First cross-module thread becomes possible here.
3. **Money / Wayloft — the depth.** Highest value, heaviest integration (real
   account data, card logic, investing). Last because it needs the shell + data
   layer proven first. Also where **private/local** actually earns its cost.
4. **Talking to other agents — the horizon.** Don't design for it now. A clean
   data layer + swappable brain lead there naturally.

## Model decision

- Build the dial. Run v1 on cloud (GLM via z.ai key, or the Opus already on Max).
- Cost savings and "un-takeable" barely matter at personal-app scale today.
- Privacy gets real once **Money** is in. That's the module where a local model
  earns its cost. The dial means that one module can run local while the rest
  stay cloud. See `~/.claude/projects/.../memory` notes on local vs cloud GLM.
- Keep the heavy model OUT of the hot path (don't call a big model on every
  Edit swipe; score by similarity, reserve the model for rich occasional tasks).
- Claude Code / Opus stays the workshop (builds the app), never inside the
  running product.

## The honest risk

Not technical. Scope and follow-through. A small life OS used every day beats a
grand one still being architected. Ship one daily-use module, then add.

## Existing pieces to draw from

- The Day: `projects/day-planner/` (`planner.html`, `serve.py`, Google Calendar
  auth, VPS phone access). Checkpoint: `2026-06-23-1054-day-planner-phone-access-mobile-ui.md`.
- The Edit: `projects/style-feed/` (`feed.html`, `quickchoose.html`,
  `style-profile.md`, taste ♥/✕ learning, ShopMy scraping).
- Money: `projects/wayloft/` (credit-card value engine).
- Shared design language: `projects/aios-dashboard/design-system` (cream /
  Cormorant / Jost), anchor = The Edit.

## Status

- **Batch 1 (done, 2026-06-25):** The Day + The Edit merged into one SPA shell.
  `serve.py` composes both canonical files at request time, scopes each module's
  CSS under `#view-day`/`#view-edit`, top tab bar + hash router. Run with
  `python3 serve.py` (port 8800; gated by THEDAY_KEY — open `/?k=<key>` once).

## Next

First **cross-module thread**: a calendar event (The Day) → suggested outfit
(The Edit), filtered by the event's occasion (The Edit already has work/casual/
going-out/vacation chips + per-card `data-occ`). That forces the shared data
layer into existence as simple JSON. Keep the model out of the hot path — filter
by existing data, no LLM per event. Then bring Money (Wayloft) in as view 3.
