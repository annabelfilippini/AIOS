---
date: 2026-05-14
time: 15:30
project: agency-audit-network
status: complete
next-session: Wait for Tom's reply to the WhatsApp + audit-intake doc. If yes, answer his three pre-Day-1 decisions (scan exclusions, personal LinkedIn/Gmail, vault sync approach) and kick off Day 1 of intake. If pushback, iterate the doc. Either way, the Cowork-references in `plan-v1-2026-05-14.md` cost table need a small bump (1 seat → 5-seat Team-plan block) before the build kickoff.
---

# Session: Dad-pilot audit intake doc written, ready to send to Tom

## What we worked on

Worked through Annabel's question on Dropbox vs Supabase vs Cloudflare for Tom's setup, then quickly expanded scope as the real picture emerged: Tom has 4 companies under one entity (AIH = holding, CFS + Falcon = similar/distinct brand, FSL = most different), all employees cross-company, and his canon today lives in an Obsidian vault, not Dropbox. No Supabase, no Cloudflare. He wants the audit to look his system over and produce structure — not fill out a 50-question form himself.

Wrote the audit intake doc at `projects/agency-audit-network/dad-pilot/audit-intake-2026-05-14.md` over multiple iterations. Confirmed via claude.com/pricing that the "Team plan" Tom mentioned is the Anthropic pricing tier ($20/seat annual, $25/seat monthly, 5-150 seat range, includes both Cowork and Claude Code on one bill). Reverted a brief Claude-Teams-vs-Cowork detour. Drafted a WhatsApp version for Annabel to send alongside the doc.

## Decisions made

- **Obsidian vault stays as the canon layer** (replacing the original Dropbox plan). Architecture diagram boxes swap "Dropbox" → "Shared Obsidian Vault (synced)", everything else identical.
- **One vault parent, per-company subfolders, NOT four separate Dropboxes/vaults.** Voice isolation enforced at the skill layer (`company=cfs` parameter, project boundaries), not at the storage layer.
- **One Supabase + `company_id NOT NULL` on every row** for clean per-company isolation in operational data.
- **Cowork stays as the employee AI surface** (Tom was talking about the Team *pricing tier* in Cowork, not the separate Claude Teams web product). Annabel uses Claude Code as builder.
- **Audit scope expanded from "canon extraction" to "full system diagnosis + canon + setup plan."** Now produces 7 deliverables: system inventory, target architecture, per-company normalized canon (5 files each), setup checklist, employee onboarding template, pilot recommendation, build order.
- **Tom's gap-question burden: ~5 voice memos per company across 6 categories.** No typing. Total time from Tom: ~35 min across 3 days.
- **Pilot will be CFS or Falcon** (similar shape, more material). FSL deferred. AIH gets a light scan only.

## Open questions

1. **Anthropic Team plan 5-seat minimum** — is it hard or soft? Worth a quick Anthropic sales ping before signing. If hard, monthly cost starts at ~$180-225/mo (1 Premium seat for Annabel-as-builder + 4 standard).
2. **Tom's three pre-Day-1 decisions** — scan exclusions, personal LinkedIn/Gmail OK to scan, vault sync approach (Obsidian Sync $8/user/mo vs cloud-folder sync). Waiting on his reply.
3. **`plan-v1-2026-05-14.md` cost table needs updating** from "1 seat @ $30/mo" to "5-seat Team block @ ~$180/mo." Not blocking Tom's reply.
4. **How Annabel actually executes the autonomous scans** — Gmail/Granola/LinkedIn OAuth flows in the doc imply infrastructure that isn't built yet. For v1 with one client (Tom), manual extraction via Claude Code is fine; productizing later.

## Next steps

1. **Annabel sends the WhatsApp + the doc link to Tom.**
2. **Wait for his reply.** If yes + answers the three decisions, kick off Day 1 (vault access, OAuth, URLs, account list).
3. **Before Day 1:** verify Anthropic Team plan 5-seat minimum with sales; pick vault sync mechanism based on Tom's preference.
4. **After audit completes:** update `plan-v1-2026-05-14.md` cost table, swap any remaining Dropbox refs in plan-v1 to Obsidian.
5. **Productization signal:** the audit-intake doc structure is the v0 of the actual self-serve audit product Annabel is building. Worth re-reading after Tom's run to extract the template.

## Context to preserve

**Files written/updated this session:**
- `projects/agency-audit-network/dad-pilot/audit-intake-2026-05-14.md` — main artifact, ready to send to Tom (~200 lines, dad-readable)

**Key architecture clarifications worth not losing:**
- Litmus test for what goes where: *Will a human edit this directly?* → vault (Obsidian). *Is this a log of something that happened?* → Supabase. *Is this only running because a schedule fired?* → Cloudflare.
- Per-company isolation enforced 3 ways: skill-layer `company` parameter, vault folder permissions, Supabase `company_id NOT NULL`. Storage separation (4 vaults) was rejected — wrong tool for the job.
- Blotato sits *downstream* of drafts (publishing-distribution layer), not in the canon/data stack.
- Anthropic Team plan = pricing tier covering both Cowork + Claude Code. Different from the standalone "Claude Teams" web-only product.

**Companies (worth remembering for future sessions):**
- AIH — holding company, light operational footprint, skip for pilot
- CFS — pilot candidate, similar to Falcon
- Falcon — pilot candidate, similar to CFS but distinct brand
- FSL — most different, deferred to phase 2

## System refinement candidates

- The **audit-intake doc structure** (one-paragraph summary → 35-min table → autonomous scans → 7 deliverables → step-by-step flow → per-company expectations → pilot logic → guarantees → timeline → pre-Day-1 decisions) is a reusable template for the self-serve AIOS Starting Point Audit product. Worth extracting into `research/templates/` after Tom's run validates it.
- The **"read what they already have, only ask for genuine gaps" framing** is the real differentiator vs every other Skool-style audit form. Worth codifying as a global feedback memory — applies to any future intake or onboarding flow Annabel designs.
- Confirmed pattern: when Tom (or any non-technical stakeholder) is the reader, **voice memos beat forms by a lot.** Worth a global memory.
