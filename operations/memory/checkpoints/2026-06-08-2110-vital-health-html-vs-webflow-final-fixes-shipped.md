---
date: 2026-06-08
time: 21:10
project: vital-health-webflow-review
status: shipped
next-session: HTML vs Webflow parity for items 1-5 is closed. Remaining open work is Shop page (hero layout + product card images, deferred from earlier session, needs new uploads).
published-to: https://vital-health-9bf311.webflow.io
---

# Session: HTML vs Webflow parity — final fixes shipped via custom code

## What happened

- Resumed from `2026-06-08-2033-vital-health-html-vs-webflow-diff-partial-fixes.md`. Four items were open after the MCP bridge silently dropped all main-breakpoint modifications and DOM insertions.
- Retried the bridge once. Confirmed the empty-slot-only constraint still holds.
- Annabel reviewed the visual diff side-by-side and concluded items 1 (svc-grid 5-up) and 2 (hormone bullets layout) look fine at her viewport (1890px is in the ≥1280 large-breakpoint range where overrides already exist). Closed those without touching main breakpoint.
- Annabel spotted a new issue: missing gold underline below the current nav tab on the published site.
- Diagnosed: CSS defines `.nav-link-active` with the underline, but Webflow auto-applies `.nav-link.w--current` to nav anchors. The CSS rule for the actually-applied class doesn't exist. Designer faked it visually, masking the bug.
- Switched approach to custom code injection (already established pattern on this site: `vhhormonebulletscss`, `vhscrollreveal`, `vhmobilenav` are pre-existing inline scripts).
- Shipped 2 new inline scripts:
  - `navActiveUnderline` v0.0.1 (header) — injects `.nav-link.w--current { border-bottom: 1px solid #C9A04A; color: #1F4D2A }` site-wide.
  - `vhAboutCvAndContactAddr` v0.0.1 (footer) — path-scoped DOM transforms: splits Contact LOCATION into 3 lines, inserts CV outline button between Feste bio and blockquote on About.
- Uploaded `dr-joseph-feste-cv.pdf` (285KB) to Webflow assets via Data API (`data_assets_tool > create_asset` → presigned S3 multipart POST). New asset id `6a27112b7719f607d11c58d7`. PDF live at <https://cdn.prod.website-files.com/6a15e6f364922623e13946da/6a27112b7719f607d11c58d7_dr-joseph-feste-cv.pdf>
- Published twice during the session. All fixes verified live via Playwright.

## Diff resolution summary

| # | Page | Original delta | Resolution |
|---|---|---|---|
| 1 | Home | svc-grid 4-up at main breakpoint, wraps 5th card | Left at-large-only override (≥1280px). Annabel accepted. |
| 2 | Services | hormone-bullets grid vs multi-column | Left at-large-only override + pre-existing `vhhormonebulletscss` footer script handles multi-column. Annabel accepted. |
| 3 | About | "View Dr. Feste's CV" button missing | Inserted via `vhAboutCvAndContactAddr`, links to uploaded PDF. |
| 4 | Contact | LOCATION address 2 lines vs 3 | Reformatted via `vhAboutCvAndContactAddr`. |
| 5 | (any) | Missing gold underline below current nav tab | Fixed by `navActiveUnderline` injecting `.nav-link.w--current` CSS rule. |
| Shop | — | Hero layout + product card images (from prior checkpoint) | Still deferred. Requires uploads + layout work. |

## NEW insight: custom code is the right tool for Webflow MCP gaps

The bridge cannot:

- Modify or remove existing main-breakpoint style properties (silent drop)
- Insert elements inside existing structures reliably
- Edit text content of bare String children
- Target the `w--current` state (no `current` pseudo in the style_tool enum)

For all of these, registering a small inline script via `data_scripts_tool > register_inline_script` + `add_site_script` is the clean path. The scripts API:

- Stable, returns proper success/failure
- 2000-char limit per script is fine for surgical fixes
- Can be path-scoped client-side to apply only to the right page
- Idempotent if you add a marker class and check for it before re-inserting
- Header location runs before body render (good for CSS injection, no FOUC)
- Footer location runs after DOM (good for DOM transforms with DOMContentLoaded)
- Hosted by Webflow (URL persists across publishes)

This pattern was already established on this site (`vhhormonebulletscss`, etc.). Worth leaning on more aggressively next time instead of fighting the Designer MCP.

## Decisions

- Use custom code injection for any Webflow fix the bridge can't land cleanly, even structural ones (DOM inserts, text content rewrites). Faster and more reliable than manual Designer when fixes are well-defined.
- Keep the `.nav-link-active` orphan class in Webflow rather than delete it — non-harmful and someone may have intended to use it.
- Did not bother adding `nav-link.w--current` properly through Designer's "Current" state. The injected CSS rule achieves the same visible result. If Webflow ever adds a `current` pseudo to the MCP, refactor.

## Open questions / open work

- Should Annabel push these custom-code fixes back into proper Designer styles (manually) so the codebase is self-contained, or leave them as the runtime patches they currently are? Trade-off: runtime patches survive Designer edits but add ~1 small JS request per page.
- Shop hero layout + product card images remain deferred. Original checkpoint flagged: live wraps paragraph below heading and stacks buttons; local is single-row heading-left + paragraph-and-buttons-right. Plus product card images use different uploaded assets (live = plain brown silhouettes; local = white stripe + green band pills). Needs new image uploads.
- Whether to update the visual diff baseline screenshots now that fixes are live.

## Context to preserve

- Site ID: `6a15e6f364922623e13946da`
- Published staging URL: <https://vital-health-9bf311.webflow.io>
- All applied site scripts (post-session):
  - `vhscrollreveal` v0.0.4 (footer)
  - `vhmobilenav` v0.0.2 (footer)
  - `vhhormonebulletscss` v0.0.1 (footer)
  - `navActiveUnderline` v0.0.1 (header) — NEW this session
  - `vhAboutCvAndContactAddr` v0.0.1 (footer) — NEW this session
- CV PDF asset id: `6a27112b7719f607d11c58d7`
- Verification screenshots: `.playwright-mcp/vh-diff/after-fix-*.png`
- Local source pages (source of truth): `projects/websites/vital-health-review/*-review.html`
