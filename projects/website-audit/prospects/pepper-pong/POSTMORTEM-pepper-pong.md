# Postmortem: Pepper Pong Walkthrough (April 13–14, 2026)

The first end-to-end run of the website-audit pipeline. Walkthrough #1 of 1 (per Ras Mic methodology — nail the manual process, then create/refine skills from the run).

## What we built

Two HTML deliverables (`homepage-redesign.html` + `dashboard-preview.html`) plus the full audit narrative (`audit-client.html`) and a landing page (`index.html`), all deployed as a branded portal. Total: 4 HTML files linked from one shareable URL. Covers every audit finding via annotated fixes (orange FIX / green NEW / blue SIGNATURE tags).

## Day 1 (hand-built): what it cost

Approach: Claude hand-wrote every line of HTML/CSS in the main session.

- Homepage v1: **1,242 lines** across multiple iterations (comparison card, redesign v1, v2 adjustments, photo swaps, asset debugging)
- Dashboard v1: **1,174 lines** (editorial layout redesign, opportunity bars killed, AI scan hero added, keyword accent-bar list)
- Associated work: 10 scratchpad entries across the day, Obsidian design-inspo lookups, image sourcing + resizing

Estimated Claude token usage for the redesign + dashboard portion: **~450–550K tokens** (conservative; counting iterative CSS work and asset debugging).

## Day 2 (Stitch pipeline): what it cost

Approach: Firecrawl branding pass → Stitch generates layout → agent ports to final HTML with real assets + motion → bb-quality QA.

- Firecrawl: 1 credit (branding format on pepperpong.com)
- Stitch generations/edits: 6 total (homepage initial gen, homepage v2 regen, nav edit, promo-bar edit, dashboard gen, separate QA verification)
- Agent rebuild (general-purpose, handled BOTH files in one run): **~177K tokens, 15min duration**
- Main-session orchestration: read v1 references for copy specs, write Stitch prompts, spawn + brief agents — **~60-80K tokens estimated** (prompt writing + state checking + two agent briefings)

Estimated Day 2 total Claude usage: **~100–140K tokens**.

## The unlock

Hand-building is O(output_line_count). Conducting the pipeline is O(instruction_size). A 1,000-line mockup takes ~10x more tokens to write than to orchestrate if someone else writes it.

Stitch handles the layout at a fixed per-screen cost. Agent rebuilds handle the mechanical port at ~10–15K tokens per file. Main-session Claude only writes prompts, reviews output, and conducts QA — it never touches a `<div>`.

**Structural cost per prospect:**
- Day 1 approach: ~500K tokens, 2 sessions spread across a day.
- Day 2 approach: ~100K tokens, one focused session.
- **~5x reduction**, more at higher volumes (skills compound).

## Kill gate check-in

Per BB strategy evaluation (2026-04-12): 20 personalized audits in 2 weeks = viable. <3 conversations = kill. With the pipeline now shipped:

- **Realistic throughput per day:** 2–3 prospects end-to-end (manual prospect selection + outreach stays the rate limiter, not Claude usage).
- **20-prospect target over 2 weeks** is now feasible without usage panic — it's ~10 total sessions of pipeline work.
- **Cooldown response** (Apr 9, pre-pipeline) was the first canary — positive. Next signal: pitch Pepper Pong + outreach via warm channels. If that converts at even 20%, the unit economics work.

## Key learnings captured this session

1. **Stitch paraphrases unfenced copy.** Every verbatim string (customer quotes, step labels, headlines) must be wrapped in triple-backticks with `DO NOT REWRITE`. This eliminated ~70% of iteration overhead when applied to the dashboard.
2. **Stitch stacks duplicate nav bars on edits.** Always follow generation with a cleanup edit: "Remove any duplicate headers or nav bars — exactly one nav above the hero."
3. **Stitch outputs no motion.** Phase B always wires back: marquee scroll, UGC `<video autoplay>`, scan-line animation, hover states.
4. **Stitch's trends chart is unreliable.** Data point dots don't land on the line. Always port v1's SVG verbatim.
5. **Stitch's font enum is limited.** No Gotham/Proxima. Metropolis ≈ Gotham, DM Sans ≈ Proxima, Space Grotesk ≈ modern geometric. Phase B swaps to real stack via `@font-face`.
6. **Agent QA > Claude QA.** The bb-quality agent caught invented customer quotes, duplicate nav bars, and paraphrased step labels. Claude eyeballing would have shipped those.
7. **Homepage + dashboard need separate Stitch design systems.** Homepage = bold brand (Metropolis, ROUND_FULL, VIBRANT). Dashboard = editorial (all-Inter, ROUND_EIGHT, NEUTRAL).

## Next prospect

**Goal:** Run the updated skills end-to-end on a warm Ann Arbor or Denver lead. Target: total time under 2 hours, total Claude usage under 100K tokens.

Success criteria:
- Phase B agent delegation enforced by new hook (no main-session HTML editing)
- Skill template produces a first-pass Stitch output that's ≥90% correct (vs. today's ~80% on Pepper Pong, which required manual iteration)
- bb-quality agent catches any remaining paraphrasing before human review
- End-to-end: prospect scrape → audit → Stitch → agent rebuild → Vercel deploy → outreach draft, in one session

If prospect #2 exceeds 2 hours or 100K tokens, the skill needs another iteration before scaling. If it comes in under, the pipeline is ready for cadence (2–3 prospects/day).

## Kill signal for the pipeline itself (meta)

If the hook fires on Edit/Write in `prospects/*/mockups/*.html` more than 2 times per prospect, the skill isn't enforcing delegation strongly enough. Iterate the skill until Claude's first instinct is "spawn an agent," not "open the file."
