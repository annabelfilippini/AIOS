# AIOS Starting Point Audit — what to expect

**Audience:** Tom
**Date:** 2026-05-14
**The skill you'll run:** `aios-starting-point-audit.md` (companion file in this folder)

## What this is

A Claude Code skill that runs on your laptop, reads your Obsidian vault and the four companies' public materials, and produces a structured starting point for Erica's working system: a normalized canon per company, a diagnostic across all four, a pilot recommendation, a deep dive on that pilot, and a setup checklist for the substrate (Anthropic Team plan, Supabase, Cloudflare, vault sync, editing surface for Josh).

The framework is Mansel Scheffel's AIOS audit (6-Layer Business Brain, 4 Pods, Friction Tags, QDOAA, Opportunity Matrix, Money Slide), applied to what you already have instead of a 50-question form.

**Closed loops are first-class.** Every Quick Win the audit recommends is staged as *heater* (ships first, no measurement) → *thermostat* (logging on, signal feeds back into the next execution). The skill specifies L1 / L2 / L3 loops per Quick Win — what gets measured on the day scale (per-draft engagement), the week scale (theme rollups, rule updates), and the month scale (proposed diffs against `voice.md` / `icp.md` / `offer.md`). A Quick Win without a thermostat plan doesn't make the slate. Reference: `loops-explained-2026-05-14.md` and the loops tab of the CFS pilot site.

## What you give it (~55 minutes total)

| Step | What you do | Time |
|---|---|---|
| 1 | Setup screenshare with Annabel — point the skill at your vault path, OAuth Gmail / Granola / LinkedIn, drop in the four URLs, list existing tool accounts and plan tiers, flag any folders or channels to exclude | ~20 min |
| 2 | Voice-memo Mansel's 7 discovery questions per company plus 1-3 gap questions the skill couldn't extract — solo, on your time, drop audio in `aios-audit/_run/voice-memos/<company>/` | ~15 min |
| 3 | Review screenshare with Annabel — walk the outputs together, mark anything wrong, lock | ~20 min |

No forms. No typed surveys. Two short calls and some voice memos.

## What lands in your vault when it's done

```
<vault>/
  canon/
    aih/_normalized/        ← founder identity (sparse — AIH is holding-co only)
    cfs/_normalized/        ← voice / icp / offer / business / goals + gaps + evidence
    falcon/_normalized/
    fsl/_normalized/
  aios-audit/
    diagnostic/             ← 6-Layer Brain scores, pod inventory, friction tags, AIOS-level rec per company
    pilot/<chosen>/         ← Step Cards, QDOAA pass, Opportunity Matrix, Money Slide
    setup/                  ← inventory, target architecture, checklist, editing-surface pick for Josh
    pilot-recommendation.md
    90-day-slate.md         ← 2-3 Quick Wins committed for the pilot company
    _run/                   ← pre-flight, gap questions, voice memos, decisions log
```

The `canon/<company>/_normalized/` files feed Layers 1-2 of the 6-Layer Brain. They are the editable surface Josh and every future hire touches.

## What the skill decides for you, what stays on you

**Skill decides (and shows its reasoning):**

- 6-Layer Brain scores 0-5 per company, with three evidence quotes per layer
- Loop-readiness score 0-3 per company (how mature the existing measurement / feedback is)
- Which pods are active in each company and where the friction lives
- AIOS-level recommendation per company (Personal / Team / Company / Cleanup-before-automation)
- Pilot company ranked by Mansel's priority formula (Impact × Confidence − Effort − Risk − Adoption gap − Data Readiness gap)
- Which pod in the pilot company gets the deep pass
- Which workflow inside that pod gets Step Cards + QDOAA
- Top 3 Quick Wins with Money Slide totals and L1/L2/L3 loop specs (heater ship date + thermostat close date for each)
- Loop substrate required (Supabase tables, Cloudflare crons, signal sources) consolidated across all Quick Wins
- Editing-surface recommendation for Josh (guided Obsidian / Notion mirror / shared docs)
- Setup checklist with monthly cost estimates

**Stays on you:**

- Approving the pilot pick on the review screenshare
- Approving spend before any paid service spins up
- Answering Mansel's 7 discovery questions per company by voice memo
- Confirming what's true and what's wrong on the review screenshare

## Per-company expectations

- **AIH** — light pass only (founder identity + holding-co structure). Likely Personal AIOS. ~1-2 voice memos.
- **CFS** — full pass. Pilot candidate. Likely Team AIOS. ~5-7 voice memos.
- **Falcon** — full pass. Other pilot candidate. Structurally similar to CFS, brand-distinct — whichever wins the pilot makes standing up the other one mostly a voice / brand swap, not a re-architecture. ~5-7 voice memos.
- **FSL** — full light pass + AIOS-level rec. Deep pass deferred to phase 2 — it's most different from the other three, and the skill will flag whether it's *Cleanup-before-automation* or just "pilot later." ~3-4 voice memos.

## Three decisions to make before Day 1

1. **Scan exclusions.** Vault folders, channels, accounts to skip. Default is the whole vault + Gmail sent + Granola + LinkedIn (personal + company pages).
2. **Personal LinkedIn and personal Gmail OK to scan?** Helps the Layer 1 (Identity) score and the voice extraction. If not, the skill works from company channels only — slightly less voice precision.
3. **Vault sync approach.** Obsidian Sync (~$8/user/mo, native) or cloud-folder sync (iCloud / Dropbox / Syncthing). The skill will recommend based on what's running on your laptops; flagging early so it's not a surprise in the setup checklist.

## What happens after

The 90-day slate becomes the build queue. `plan-v1-2026-05-14.md` (also in this folder) picks up from there — Week 1 stops being "draft the five canon files with you" because the audit will have produced them. Week 1 becomes "execute the setup checklist + ship the first Quick Win." Daily Brief is the wedge skill, Erica is the first DRI, you're the AI Founder, Annabel is the builder.

After the 90-day slate ships, the audit re-runs — 6-Layer scores update, the next pod gets the deep pass, the Opportunity Matrix advances. Mansel's framework is not a one-shot.

## How to run it

Once the three pre-Day-1 decisions are answered:

1. Open Claude Code on your laptop at the vault root.
2. Invoke the `aios-starting-point-audit.md` skill (drop it in your `.claude/skills/` or reference it directly).
3. Setup screenshare with Annabel kicks off Phase 0 — she walks the pre-flight questions with you on screen.
4. After Phase 0, the skill runs autonomously. You'll see updates in `aios-audit/_run/decisions.md` as it goes.
5. When it pauses for voice memos (Phase 4), it writes the prompts to `aios-audit/_run/gap-questions.md` and stops until you drop audio in.
6. After memos transcribe and slot, the skill writes the review summary and pings you to schedule the review screenshare.
