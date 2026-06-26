---
date: 2026-06-25
time: 18:30
project: life-os (new north-star project)
status: VISION SET — life OS project doc created; GLM/local question resolved into a "swappable model dial" decision. Next session: combine The Day + The Edit into one shell.
---

# Session: Life OS vision + GLM/local decision

## Why
Annabel started by trying to get GLM (z.ai) working in Claude Code and couldn't
figure out why she still had Opus. That unspooled into the real question: she
wants to build a personal life OS, and was trying to decide local vs cloud GLM.

## What we figured out (the GLM/local reality)
- Her screenshot config was never saved anywhere Claude Code reads; her shell
  also had `ANTHROPIC_BASE_URL=api.anthropic.com` (injected by Claude Desktop)
  which would override settings.json anyway. We briefly wrote the corrected env
  block (key in `ANTHROPIC_AUTH_TOKEN`, not `ANTHROPIC_API_KEY`), verified
  `glm-5.2` works live via `api.z.ai/api/anthropic`, then **reverted it** at her
  request. settings.json is back to Opus/Max.
- z.ai key (works): `f4e5663c80ab425fb85c2a915b45ed0b.nZ11oWgGGB6ETVkt`.
- **GLM 5.2 is 756B params. It does NOT run on her Mac.** The famous "Opus-level"
  GLM only runs in the cloud or on data-center hardware. A laptop/Mac Mini could
  only run a much smaller, dumber variant. Confirmed by 3 YouTube reviews (Claire
  Vo, Nate Herk, Greg Isenberg/Amir) — ALL of them rent it via z.ai/OpenRouter,
  none run it locally. Even full GLM is ~4 pts behind Opus (62% vs 69%).
- The hype = (1) ~5x cheaper than Opus, (2) open weights = can't be permanently
  killed like Fable was. Both are about cloud + insurance, not laptop-local.
- For HER personal-app scale: cost savings negligible, and private/offline/
  un-takeable ONLY come from local (out of reach for good GLM). So GLM buys
  little over Opus for v1.

## The decision
**Make the model a swappable dial, not a dependency.** One config
(`MODEL_ENDPOINT`, `MODEL_KEY`, `MODEL_NAME`); never hardcode a provider. Run v1
on cloud (GLM or Opus). Revisit local only for the Money module later, where
sensitive financial data justifies the cost. "Fusion/chaining" = cheap model for
routine, Opus for hard reasoning.

## The real vision (north star)
A personal **life OS**: one app, tabs for The Day / The Edit / Money, a shared
life-data layer underneath, and one agent that reasons across all of it. The
magic is cross-module: calendar event → outfit → which card to use. Doc written
to `projects/life-os/README.md`.

Build sequence: The Day (spine, already good) → The Edit (joy, has momentum) →
Money/Wayloft (depth, where local/private matters) → agent-to-agent (horizon).
Risk is scope/follow-through, not capability. Ship one daily-use module, accrete.

## Decided this session
- The Day is good as-is; she'll tweak it herself as she sees fit.
- **Next session: start combining The Day + The Edit into one shell** with a
  shared data layer, starting from The Day as the spine.

## Next session — start here
1. Read `projects/life-os/README.md`.
2. Look at how `projects/day-planner/planner.html` and
   `projects/style-feed/feed.html` (+ `quickchoose.html`) are structured.
3. Plan the shared shell: tabs + shared data layer, The Day as spine. Don't
   rebuild The Day; bring The Edit alongside it.
