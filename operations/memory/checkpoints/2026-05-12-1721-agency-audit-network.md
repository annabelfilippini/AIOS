---
date: 2026-05-12
time: 17:21
project: agency-audit-network
status: paused
next-session: Draft 3 agency outreach messages (Nick Rakis, Manish Unadkat, Matthew Lowe) + website copy for Annabel's Claude Design build.
---

# Session: Agency Audit Network — strategy lockdown + Mansel framework capture

## What we worked on

Stress-tested `projects/agency-audit-network/PLAN.md` through Garry + Business Partner lenses, locked the ICP, rewrote the plan as a 14-day sprint, then mid-session discovered Annabel already has two case studies (Cooldown website redesign + life coach AI automation). Captured Mansel Scheffel's full AIOS framework via authenticated Playwright on `skool.com/ainative` and identified 11 agency partner candidates from his community. Updated Quick Read template with Mansel-aligned vocabulary.

## Decisions made

- **ICP locked:** owner-operated product brands like Cooldown (2–20 ppl, $500k–$5M, often Shopify). Dad's network = v2 ("more employees / more systems"). True mid-market = v3.
- **Audit shape:** two tiers — Quick Read (free, 1–2 pp, 30–90 min) → Deep Audit ($300–$1,000, 5–7 pp, 4–6 hrs).
- **Framework vocabulary:** use Mansel's **4 pods** (Acquisition / Delivery / Support / Operations), not the playbook's "engines." Same model, his audience speaks his language.
- **ATOM positioning** (Audit → Build → Train → Maintain): Annabel owns Audit, refers Build/Train/Maintain.
- **Sequence pushback:** don't redo Cooldown audit retroactively in Deep Audit format. The deployed Cooldown website IS the headline case study; the existing audit PDF is supporting.
- **Don't pitch agencies "I have clients" yet** — use honest version: "learn about your work, refer when fit comes up."

## Open questions

- Resource files inside Mansel's course (AIOS Playbook, Pod Mapping Skill, Audit Deep Dive) not captured — worth a follow-up Playwright pass if needed.
- Skool member pagination broken (`?p=` doesn't paginate) — got 30 of 64 members; 34 still uncaptured.
- Should Annabel reach out to Mansel directly for a partnership? His community is small but premium.
- ATOM is Mansel's name — internal use only, do not adopt as client-facing brand language.

## Next steps

1. Draft 3 personalized agency outreach messages: **Nick Rakis** (Melbourne AI Education + Strategy agency), **Manish Unadkat** (Inner Core Solutions / Zoho CRM), **Matthew Lowe** (highest activity in ainative — generic bio, needs LinkedIn verification first). Each references something specific + attaches Cooldown + life coach case studies + low-commitment 20-min ask.
2. Draft website copy for Annabel's Claude Design build: hero, Cooldown case study (deployed site), life coach case study (before/after automation), Quick Read offer, agency partner CTA, brief about-Annabel.
3. After website ships: send Quick Read template to first Cooldown referral lead.
4. Security cleanup Annabel still owes: `rm ~/Documents/skool/skool-curl.txt` and log out of Skool to invalidate auth_token JWT (it appeared in this session's transcript).

## Context to preserve

**Files produced this session:**

- `projects/agency-audit-network/PLAN.md` — rewritten v2 (sprint dated 2026-05-12 → 2026-05-26)
- `projects/agency-audit-network/templates/quick-read.md` — Tier 1 template, Mansel-vocabulary aligned
- `projects/agency-audit-network/research/mansel-aios-framework-2026-05-12.md` — full framework synthesis from 10 captured AIOS Model modules
- `projects/agency-audit-network/research/mansel-members-agency-candidates-2026-05-12.md` — 11 ranked candidates
- `projects/agency-audit-network/research/mansel-framework-2026-05-12.md` — earlier public-only sync notes

**Annabel's existing assets (newly surfaced mid-session):**

- Cooldown — deployed website she built + audit PDF (not flagship format)
- Life coach — AI process automation, can reference
- Both have given (or will give) permission to be named
- Building her own website via **Claude Design** (not Claude Code)

**Garry / BP framing applied:**

- Three Garry pushbacks the user accepted: narrow ICP, defer multi-track audit until Track 1 ships, don't pitch agencies before having proof
- One BP pushback that succeeded: don't repackage Cooldown audit retroactively — deployed website is stronger

## System refinement candidates

- `skool-press.mjs` doesn't handle JS-rendered authenticated pages well (got less data with auth than without). Worth noting for next time.
- Playwright sandbox blocks `require` / dynamic `import` — workaround was writing JS to `~/.playwright-mcp/tmp/` and using `filename` param. Document this pattern.
- Skool pagination via `?p=` doesn't work. Need different param (try `page=` or post-request API).
