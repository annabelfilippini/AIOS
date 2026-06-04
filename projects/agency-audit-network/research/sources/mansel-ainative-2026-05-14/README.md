# Mansel Scheffel / AI Native (ainative) — full classroom structure capture

Captured: 2026-05-14
Source: authenticated scrape of `https://www.skool.com/ainative` (shared account with Tom Filippini)
Community now branded: **AI Transformation Academy** (still at the `/ainative` slug)
Founder: Mansel Scheffel
Price: tracked separately in skool press output
Captured by: targeted curl fetcher (`/tmp/ainative-sweep.mjs` series) — script preserved in `/tmp` if a re-run is needed.

## What's in this folder

- **`module-tree.txt`** — Human-readable hierarchy of all 123 module entries across the 4 paid courses Annabel has access to. Each module shows whether it has a video, written guide(s), or both. *Start here.*
- **`module-catalog.json`** — Same data structured, with IDs, slugs, parent paths.
- **`resources-catalog.json`** — Every written guide / blueprint attached to a module, with file_id and content type. *48 resource files. Their bodies were not captured — see "What's missing" below.*
- **`attention-residuals-post.json`** — The body of the community post Annabel sent (turned out to be a 465-char Mansel update about Moonshot AI's residual-attention paper, not a deep module).

## What's new since the 2026-05-13 capture

The 5/13 `mansel-audit-structure-check-2026-05-13.md` only had a partial title sample. Today's capture is complete, and several things have changed:

1. **Entire new course: "Vibe Coding & Agentic Workflows"** — 40+ modules across 6 levels (Foundations, Agentic Toolkit, Context + Prompt Engineering, Frameworks Overview, Web App Toolkit, Security). Did not exist on 5/13. This is Mansel's attempt to teach the implementation skills downstream of the AIOS framework.
2. **AIOS Model now has 19 modules** (5/13 only captured ~6 titles). New visible modules include "AIOS Security", "Monitoring", "AIOS Failover", "Github Automation".
3. **AIOS Model module 6.5** ("Automating AIOS Onboarding") — wasn't captured 5/13. Bundles `onboard-skill-refactored`, `pod-mapper`, and `offer-engine` zips. This is Mansel's own audit/onboarding plug-in pack.
4. **Blueprint Library expanded** — now has 18 entries vs. earlier mention of "Context Audit" alone. Includes GTM OS, Content OS, App-building ATLAS v3, Daily Brief, AI SEO/GEO, Frontend Website Builder, Proposal Generator, Call Digest, Meeting Prep, Slide Generator, AI News Monitor, Playwright Automated Testing, Gamma Slides, Ultimate AI Memory System.
5. **One-Person AI Transformation Phase 1, module 6 "Framework - Audit / AI Readiness"** confirmed to have a Notion-page guide + knowledge base + content whiteboard attached. *This is Mansel's actual audit framework artifact* — the one we should request from him directly or capture via authenticated browser.

## The audit-relevant modules (Mansel's own audit material)

Five modules across two courses contain Mansel's audit framework:

| Course | Module | Materials |
|--------|--------|-----------|
| One-Person AI Transformation | Phase 1 / 6. **Framework - Audit / AI Readiness** | Audit Notion Page + Knowledge Base (markdown) + Content Whiteboard (SVG) |
| The AIOS Model | 14. **AIOS Consulting Playbook** | `aios-consultant-playbook.html` + **Audit Deep Dive** guide |
| The AIOS Model | 6.5. **Automating AIOS Onboarding** | `onboard-skill-refactored.zip`, `pod-mapper.zip`, `offer-engine.zip`, onboarding-automation HTML |
| The AIOS Model | 11. **AIOS Security** | `security-audit.zip` + security-audit HTML |
| Blueprint Library | **Context Audit** | `context-audit.zip` |

The five together represent Mansel's full audit IP. The next session should focus on actually capturing the *body* of these specific resources.

## What's missing (and why)

**48 attached resource files (HTML guides + ZIP plug-in packs) returned 403** when fetched directly from `assets.skool.com/f/<file_id>`. Skool serves them via signed URLs that are minted at module-view time by Skool's frontend JS. To capture the bodies, the next pass needs to:

1. Use authenticated **Playwright** to navigate to each module page
2. Wait for the JS to render the resource download links (which by then carry a signed token)
3. Extract the signed URL from the DOM
4. Fetch each signed URL within the same session

This is the same pattern the 2026-05-12 capture used to get module body content. The 5/12 note "Playwright sandbox blocks `require` / dynamic `import` — workaround was writing JS to `~/.playwright-mcp/tmp/`" still applies.

**Video lessons** are 90%+ of the course content but were not transcribed — Skool serves them via Mux with playback tokens, and transcribing the audio is a separate pipeline. The module titles + the attached HTML guides cover the conceptual skeleton; the videos add Mansel's tactical narration.

## Why module titles + structure alone are still valuable

Even without bodies, the structure tells us:

- **Mansel's pedagogical order** — how he sequences a learner from concept → implementation → consulting
- **What he sells** as standalone blueprints (the Blueprint Library is the productization layer)
- **What's automatable** — modules tagged with `.zip` attachments are pre-built skill/plug-in packs ready to deploy
- **What's coming** — "Level 6 - coming soon" in Vibe Coding tells us his roadmap

Combined with the 2026-05-12 framework synthesis (pods + ATOM + 4 engines, captured via Playwright), Annabel has Mansel's conceptual model AND his course architecture. The unrecovered piece is the verbatim language inside each guide, which Mansel writes himself and which would be helpful but is not strictly necessary to design Annabel's own audit.

## Security note

`~/Documents/skool/skool-curl.txt` will be deleted after this run. The auth token inside expires anyway and was exposed via prior session transcripts.
