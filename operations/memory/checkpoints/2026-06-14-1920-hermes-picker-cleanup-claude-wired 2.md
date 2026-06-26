---
date: 2026-06-14
time: 19:20
project: hermes / local-model
status: delivered & verified — LIBRARY hidden, Claude wired (direct Anthropic key), all tested end-to-end
next-session: DONE: (1) trimmed + then fully hid the "LIBRARY" (raw local Ollama) group from the Workspace model picker via a source patch; (2) wired Claude via a direct Anthropic API key with claude/claude-opus aliases. ONE open thread: now that the Anthropic key is active, the picker may surface an ANTHROPIC provider group (raw Claude variants) and possibly OPENAI-API — offered to hide those raw groups too (same patch pattern) so she just uses the aliases; awaiting her look after refresh. Also still-open from prior checkpoints: SSH tunnel persistence via launchd (tunnels die on Mac sleep; `hermes-up` / Desktop "Start Hermes.command" is the manual fix).
---

# Session: Hermes picker cleanup + Claude wired

## What was asked

"Hide library" (the confusing LIBRARY group in the model picker) and "wire Claude into Hermes."

## Done & verified

1. **LIBRARY hidden.** The picker listed the loopback `local` Ollama provider as a
   "LIBRARY" group duplicating the local/local-fast aliases.
   - First trimmed `providers.local.models` from 4 -> 2 (removed the plain
     `qwen3:8b`/`qwen3:14b` footguns; picker is config-driven, confirmed).
   - Then fully hid it via a source patch: drop the `local` provider row in
     `hermes_cli/inventory.py:build_models_payload` (the chokepoint used by the
     Workspace `tui_gateway`, the dashboard `web_server`, and the CLI). Verified
     payload now returns `[openai-codex, nous, anthropic, openai-api]`, no `local`.
   - `providers.local` STAYS in config — it supplies the 64k context_length
     override the aliases require (empirically proven: removing it breaks
     local/local-fast with "context window below the minimum 64,000").
   - Patch is lost on `hermes update`. Re-apply script saved:
     `/root/.hermes/aios-patches/hide-local-picker.py` (idempotent) and
     `operations/hermes-vps/hide-local-picker.py` (source of truth); documented
     in `operations/hermes-vps/README.md`.
2. **Claude wired (direct Anthropic key).** Chosen over Nous credits (her Nous
   balance was $0). Added `ANTHROPIC_API_KEY` to `/root/.hermes/.env` (clean
   newline for python-dotenv). Added aliases `claude` -> claude-sonnet-4-6,
   `claude-opus` -> claude-opus-4-8. Tested: direct call, both aliases, all OK.
   After gateway restart, `anthropic` shows `auth=True` in the picker payload.
   Billed by Anthropic pay-per-token (separate from her OpenAI sub / free local).

## Key mechanics learned (Hermes 0.16.0)

- The picker is built by `inventory.build_models_payload` -> `list_authenticated_providers`.
  The web UI ALSO renders an ALIAS group from `config.yaml model_aliases` (so
  aliases DO appear in the picker — earlier note was from a scrolled screenshot).
- The web frontend CURATES which models per provider it shows (e.g. nous shows
  just "hermes-agent", not all 25 catalog models). So exact web rendering of the
  new ANTHROPIC group can't be predicted from the payload alone — hence the open
  thread to confirm visually.
- Config/.env edits require a gateway restart to take effect in the running
  Workspace; the CLI reflects them immediately (fresh process).
- Process layout: tmux `hermes` = `pnpm start:all` = concurrently(`hermes gateway
  run` [8642], `pnpm dev`/vite [3000]); tmux `hermes-dashboard` [9119].

## Backups created (on VPS)

- `config.yaml.bak.hide-library`, `config.yaml.bak.trim`, `config.yaml.bak.claude`
- `inventory.py.bak.aios` (pre-patch original)

## Security note

She pasted a live, funded Anthropic API key into chat (now in this transcript and
in tool-call history). It is stored on the VPS and working. If she wants, she can
rotate it anytime at console.anthropic.com — not required, just hygiene.

## Open

1. Confirm the ANTHROPIC / OPENAI-API raw provider groups aren't re-cluttering the
   picker after refresh; if so, extend the hide patch to those too (keep Claude on
   the aliases). Offered, awaiting her look.
2. Tunnel persistence via launchd (carried over; tunnels die on sleep).
