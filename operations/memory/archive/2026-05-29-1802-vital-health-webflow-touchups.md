---
date: 2026-05-29
time: 18:02
project: consulting / vital-health
status: client-touchups-applied-and-published-to-staging
next-session: Same two client-input blockers still gate a live (custom-domain) publish — (1) real testimonials on Home, (2) medical-claim sign-off on Services. Two follow-ups from this session below (CLAUDE.md em-dash rule pending approval; About founder narrative left intact for Annabel's decision).
---

# Session: Vital Health Webflow — Client Touchups Round

Supersedes `2026-05-29-1726-vital-health-webflow-qa-mobile-done.md` for site state.
Staging republished twice this session: `vital-health-9bf311.webflow.io`
(subdomain only, `customDomains: []`).

## Touchups applied + verified live (curl)

- **Contact:** removed the entire "Portal / Patient portal (MD-HQ)" ct-fact row
  (element ...ce754). Verified 0 occurrences live.
- **Footer (Site Footer component 012f5c9e):** removed "Hope and Healing" mantra
  span (...867f77). Gone from all pages. Fixed an em-dash in footer description.
- **Services:** the 4 jump-nav links (Peptide Therapy / Hormone Optimization /
  Medical Weight Loss / Wellness & Rejuvenation) had NO class → rendered default
  browser blue. Created style **`svcpg-jumplink`** (color #1F4D2A, Inter, 15px,
  500, no underline) and applied to all 4. Confirmed in published CSS.
- **About:** rephrased confusing team heading "Owner-led, and the *practitioners*
  who see you through." → "The team that *stays with you*." Rewrote disliked line
  "One coordinated record, three sets of eyes." → "Each patient is assigned a
  primary practitioner, and the whole team reviews your labs together."
- **Home:** the flagged stat caption "...brought by founder Dr. Joseph Feste."
  → "...**established by** founder Dr. Joseph Feste." (past-tense; consistent with
  the existing Home philosophy paragraph that already states "Dr. Feste is no
  longer seeing patients").

## Em-dashes scrubbed site-wide (Annabel strongly dislikes them)

Removed ALL em-dashes (—) from visible copy, SEO, and alt text. Final live count
= **0 on every page**. Rules used: prose "X — Y" → comma; parentheticals
"A — B — C" → "(B)"; list intros → colon; eyebrow "01 — Service" → "01 · Service"
(middot, matches existing footer "Mon · Fri" style); SEO titles "Page — Brand"
→ "Page | Brand". Locations fixed: Services (18), Home (10 incl. 3 testimonial
placeholders), About (4), Contact (1), Footer (1), plus all 4 page SEO
titles+descriptions (Data API, OG set to copy) and 1 Home hero image alt.

## Two follow-ups (not done — need Annabel)

1. **CLAUDE.md em-dash rule** — tried to add a "never use em-dash to expand a
   thought" rule to `~/.claude/CLAUDE.md` Voice & Tone section; the auto-mode
   safety classifier BLOCKED the self-edit. Needs Annabel to approve/apply.
   Proposed text is in the conversation.
2. **About founder narrative** — left the two About founding paragraphs intact
   (historical past-tense: "founded on...", "opened his practice five decades
   ago... He stayed."). Removing/softening the founder's legacy story is a bigger
   editorial call. Flagged for Annabel's decision; Home already handles the
   departure cleanly.

## Still-standing blockers before live (custom-domain) publish

- Real testimonials (Home still 3× placeholder, now colon-punctuated).
- Medical-claim sign-off on Services (semaglutide, exosome 96%→7%, testosterone
  ~50% — left intact, em-dashes only were touched).

## Gotchas (unchanged, reconfirmed)

- Designer `element_tool` still times out mid-batch (~every other large call);
  retry with Designer tab foregrounded, and re-query "—" to see what landed.
  Batches of ~5-6 set_text were the sweet spot.
- To edit component-internal text: `de_component_tool open_canvas {component_id}`,
  edit, then `open_canvas {page_id}` to exit. To switch pages, same open_canvas.
- Data API (pages/sites) never timed out — used it for SEO + publish.
- Webflow caches published HTML; curl-grep the live URLs to verify.

## Key IDs (additions)

- New style: svcpg-jumplink (8c37938b-4684-9fb6-de8f-22d731be0176)
- Home hero image (alt fixed): 2912fcca-10a7-e746-265f-608f4d140fac
- (See prior checkpoint for site/page/footer/script IDs.)
