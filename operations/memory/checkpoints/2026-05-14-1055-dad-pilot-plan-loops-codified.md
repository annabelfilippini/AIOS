---
date: 2026-05-14
time: 10:55
project: agency-audit-network
status: complete
next-session: Annabel takes the dad-pilot plan + loops doc to her dad conversation. If he buys in, schedule the 60-min session to draft the five Dropbox markdown files (voice/ICP/business/offer/goals). Verify Granola plan pricing and Anthropic Team status before any spend.
---

# Session: Dad-pilot plan v1 written + closed-loop principles codified to global memory

## What we worked on

Continuation of morning's Mansel+Bo work. Annabel pushed for deeper synthesis: what to take from each, is Bo's education phase needed, where should company data live (Supabase vs Cloudflare vs Obsidian), Claude Code vs Cowork for employees. Scraped 4 more Mansel modules (Multiuser AIOS Designs, Cowork Setup, Supabase 101, Vercel 101) — most are video-only but Multiuser AIOS yielded the verbatim TLDR + the canonical architecture diagram. Web-fetched Anthropic's official Cowork docs + `anthropics/knowledge-work-plugins` repo. Verified Granola has no webhooks (polling required, Business plan ~$25/user/mo for transcript API). Spawned two Explore agents (initial Q1–Q7 mining, then a fresh-eyes tactical recomb) to extract verbatim guidance. Walked through the full live-brain architecture for Erica (marketing/sales, employee #1 at dad's company). Wrote a dad-shareable plan + a dedicated loops-explained doc. Codified the closed-loop thermostat principle + Bo/Mansel build rules into global memory.

## Decisions made

- **Mansel's federated architecture is the spine.** Per-laptop personal layer (skills/hooks/memory/CLAUDE.md) + Dropbox shared business context (5 markdown files) + Supabase shared state + Cloudflare for ingest plumbing. Documented in dad-pilot/plan-v1.
- **Cloudflare ≠ Supabase.** Supabase = storage. Cloudflare = edge compute / polling / webhook router. Both belong, different jobs.
- **Cowork is the employee tool, fork Anthropic's open-source plugins as starting point.** `github.com/anthropics/knowledge-work-plugins` — Sales/Marketing/Productivity plugins customize cleanly for Erica's role.
- **Skip notifications system for v1.** Gmail covers everything (Daily Brief = email, drafts sit in Gmail, errors = email). No Slack, no Telegram needed.
- **Build order locked: Daily Brief → email writer → LinkedIn writer → newsletter.** Daily Brief is the wedge (Bo + Mansel convergence). Slide-deck generation deprioritized.
- **Drafts only, never auto-send to clients.** Erica reviews everything.
- **Roles (Bo's framework): Dad = AI Founder, Erica = DRI for lead pipeline + brand voice, Annabel = Builder.**
- **One pod at a time.** Erica first, employee #2 not until her loop has been running 2+ weeks clean.
- **Three nested closed loops are the design backbone:** skill-level (days), workflow-level (weeks), brand-level (months). All three need measurement + comparison + adjustment.

## Open questions

- Granola Business ($25/user/mo) vs Enterprise ($35/user/mo) — which tier covers one user with transcript API? Verify with Granola sales.
- Does dad's company already have Anthropic Team / Cowork seats? Or do we need to add them?
- Beehiiv tier (existing subscription, depends on subscriber count) — Annabel to confirm with dad.
- Sensitive client data — should some calls/emails not flow into shared Supabase? Decide RLS policy in week 1 if yes.
- Does dad want to be AI Founder formally (i.e., learn enough to make judgment calls) or have Annabel own end-to-end? Decide in the conversation.

## Next steps

1. **Annabel takes plan-v1 + loops-explained docs to her dad.** Print or share; meant to be argued with.
2. **If yes: schedule 60-min "five Dropbox files" session** with dad. This is the highest-leverage hour before any code.
3. **Verify Granola plan + Anthropic Cowork status** before any spend.
4. **Set up Supabase + Cloudflare + Cowork accounts** (~3 hrs Annabel time).
5. **Week 1 build: Daily Brief skill end-to-end.** Proves the pipeline works.
6. *Deferred:* slide-deck generation, auto-send anything, employee #2, non-marketing/sales pods, dedicated CRM.

## Context to preserve

**New files this session:**

- `projects/agency-audit-network/dad-pilot/plan-v1-2026-05-14.md` — dad-shareable architecture + 4-week build plan + cost estimate + roles
- `projects/agency-audit-network/dad-pilot/loops-explained-2026-05-14.md` — three nested closed loops, Supabase schema, what's automated vs approved, compounding effect
- `projects/agency-audit-network/research/sources/mansel-ainative-2026-05-14/multiuser-architecture-diagram.png` — Mansel's canonical "Federated Personal, Shared Backbone" diagram
- Appended to `research/sources/mansel-ainative-2026-05-14/captured-module-bodies.md`: Multiuser AIOS Designs (gold), Cowork Setup, Supabase 101, Vercel 101 (last three are video-only stubs)

**New global memories** at `~/.claude/projects/-Users-annabelfilippini/memory/`:

- `feedback_closed_loop_thermostat.md` — the thermostat principle, 3 nested loops, measurement automated/judgment human. Apply across all projects.
- `feedback_ai_skill_build_principles.md` — 8 operator rules (test harness first, QDOAA before automate, one pod, Daily Brief first, federated architecture, three roles, context vs SOPs, silent failure watch).
- `reference_bo_mansel_aios_research.md` — pointer to all captured research files for verbatim quotes.
- MEMORY.md updated with 3 new index lines.

**Tactical findings worth keeping:**

- Granola: NO webhooks (on roadmap). Must poll API. Business plan required for transcript API. Granola has a public MCP server — Cowork can read native locally as alt path.
- Anthropic Cowork: 11 free open-source plugins on GitHub (Productivity, Sales, Customer Support, Product, Marketing, Legal, Finance, Data, Enterprise Search, Bio-Research, Plugin Mgmt). All forkable. Same plugin works in both Code and Cowork.
- Bo's verbatim test-harness example (for proposal-writing skill) captured for the email-writer rubric template.
- Bo's verbatim closed-loop sales example is literally what we're building for Erica.
- Mansel's silent-failure list: OAuth expiry, model updates, stale context, mystery edits. Mitigation: weekly volume-tracking via Daily Brief.

**Security cleanup completed:** `~/Documents/skool/skool-curl.rtf` deleted after capture (auth cookie file).

## System refinement candidates

- The "three nested loops on different time scales" framing (skill/days, workflow/weeks, brand/months) is a strong reusable explainer shape for any AI/automation framework. Annabel responded well to it — could become a template for client-facing audit deliverables.
- The output triple we produced — **dad-shareable plan + dedicated principle explainer + global memory codification** — is a good pattern when Annabel commits to a framework. Captures the practical (plan), the conceptual (loops), and the durable (memory) in one motion.
- The Mansel multi-user architecture diagram should probably be referenced visually in any future AnnabelFilippini.com audit deliverable — it's the canonical picture and Annabel didn't have it until today's scrape.
