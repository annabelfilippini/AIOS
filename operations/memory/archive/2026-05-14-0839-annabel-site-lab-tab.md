---
date: 2026-05-14
time: 08:39
project: annabel-site
status: paused
next-session: Continue from the packed local HTML at `/Users/annabelfilippini/Downloads/Annabel Filippini (1).html`, where Lab now behaves like a separate hash tab instead of a homepage section.
---

# Session: Annabel Site - Lab Tab

## What we worked on

Annabel wanted the Lab area of her current personal site to describe and show visuals for projects she is working on.

Starting file:

- `/Users/annabelfilippini/Downloads/Annabel Filippini (1).html`

The file is a packed/exported single HTML page with a bundler manifest and JSON-encoded template. Edits need to modify the embedded `__bundler/template` JSON safely, not just append normal HTML outside the template.

## Decisions made

- **Lab should not live on the main homepage scroll.** Annabel clarified that the Lab content belongs on the Lab tab.
- **Keep this as one local HTML export for now.** The Lab tab is implemented as a hash-based view using `#lab`, not as a separate physical file.
- **The homepage default view should remain Home/About/Doorways only.** Lab content is hidden unless the URL hash is `#lab`.
- **Lab content should feel like a living project bench.** Project cards include short descriptions and self-contained CSS visuals, not external images.

## Projects included in Lab

- AI-OS + Annie
- Website Audit Studio
- Agency Audit Network
- Wayloft
- Spent
- Apartment Hunt
- Pickleball Portal

## Files changed

- `/Users/annabelfilippini/Downloads/Annabel Filippini (1).html`
  - Added Lab project content inside the bundled template.
  - Added CSS for Lab project cards and visual motifs.
  - Added hash-view behavior:
    - default page: Lab section hidden
    - `#lab`: homepage sections hidden, Lab section shown, nav remains fixed
  - Fixed a bundling issue by escaping the inline closing script tag as `<\/script>` inside the JSON template.

- `tools/site-edits/update-lab-section.mjs`
  - Utility script that inserts the first Lab section into the packed HTML template.

- `tools/site-edits/make-lab-tab-view.mjs`
  - Utility script that converts Lab from a normal homepage section into a hash-tab view.
  - Important implementation detail: when writing JSON back into `<script type="__bundler/template">`, escape `</script>` to avoid terminating the outer script tag early.

- Working copies created in repo root:
  - `Annabel Filippini lab-work.html`
  - `Annabel Filippini lab-tab-work.html`

## Verification performed

- Parsed the embedded `__bundler/template` JSON after edits.
- Started a local `python3 -m http.server 8765` preview because the in-app browser blocks raw `file://` navigation for automation.
- Verified:
  - default homepage URL renders with Lab hidden.
  - `#lab` URL applies `body.site-view--lab`.
  - Lab content becomes visible on the Lab tab.
  - About/hero wordmark are hidden on Lab view.
- Caught and fixed a browser-only export bug where an unescaped `</script>` inside the bundled JSON caused `Error unpacking: Unterminated string in JSON`.

## Open questions / next steps

1. Decide whether Lab should remain hash-based in the packed file or become a real standalone `lab.html` page when the site source is organized.
2. Refine project wording with Annabel's exact public positioning and any links/screenshots she wants included.
3. If continuing serious site work, find or create the durable source-of-truth site folder instead of repeatedly editing the packed Downloads export.

## System refinement candidates

- Create a small packed-HTML editing SOP or script for this export format:
  - read `__bundler/template`
  - `JSON.parse`
  - modify template
  - `JSON.stringify`
  - escape `</script>`
  - verify in browser
- For personal-site work, prefer a durable source folder over Downloads exports once Annabel is ready.
