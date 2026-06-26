---
date: 2026-06-07
time: 19:58
project: vital-health-webflow-review
status: in-progress
next-session: Reload Codex so the newly added Webflow MCP server loads, then use Webflow MCP tools to apply the Vital Health review changes and publish staging only.
---

# Session: Vital Health Webflow MCP connected, Codex reload needed

## What we worked on

- Continued from the Vital Health Webflow change inventory and blocked-push checkpoint.
- Confirmed the official Webflow MCP endpoint from Webflow docs:
  `https://mcp.webflow.com/mcp`.
- Added Webflow MCP to `~/.codex/config.toml`:

  ```toml
  [mcp_servers.webflow]
  url = "https://mcp.webflow.com/mcp"
  ```

- Annabel opened the Vital Health Webflow Designer and launched the Webflow MCP Bridge App.
- Screenshot confirmed the Bridge App says `Connected to the MCP server`.
- Checked tool discovery and MCP resources in the current Codex session.

## Decisions made

- The Webflow side is connected correctly.
- The current Codex session cannot call Webflow yet because MCP tools are loaded at session startup, and `mcp__webflow__...` did not hot-load after editing config.
- Do not publish yet. CLI can publish staging, but content edits still need Webflow MCP Designer tools.
- Keep the Webflow Designer tab and Bridge App open if possible while reloading/restarting Codex.

## Open questions

- After Codex reloads, whether Webflow OAuth will need an additional authorization prompt in Codex.
- Whether to include `/shop` in the client review push, since current staging `/shop` is `404` and the local Shop page is a concept with backend/compliance blockers.

## Next steps

1. Restart/reload Codex or start a new Codex session in the same `AI-OS` workspace.
2. Confirm the Webflow MCP tools appear, likely as an `mcp__webflow__...` namespace.
3. If prompted, authorize Webflow MCP for the Vital Health site.
4. Keep or reopen the Webflow Designer and MCP Bridge App for Vital Health.
5. Apply native Webflow edits from:
   `projects/websites/vital-health-review/webflow-change-inventory-2026-06-07.md`.
6. Publish to `.webflow.io` staging only.
7. QA desktop/mobile, anchors, stale-copy search, map link, patient portal, console, and horizontal overflow.

## Context to preserve

- Local review preview was running at `http://127.0.0.1:8765/home-review.html`.
- Current staging still matched the old `*-source.html` files before this checkpoint.
- Webflow site ID: `6a15e6f364922623e13946da`.
- Page IDs:
  - Home: `6a15e6f464922623e139470e`
  - Services: `6a15f430cbd0f7ef0469e27f`
  - About: `6a19b8b56de372b248e55901`
  - Contact: `6a19bf5c98546d4f3a53d97a`
- Designer launch URL from prior checkpoints:
  `https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99`

## System refinement candidates

- Add a Webflow MCP reload reminder to the Webflow workflow: after editing MCP config, restart Codex before trying tool discovery.
- Add a preflight step that checks both sides: Codex tool namespace available and Webflow Bridge App connected.
