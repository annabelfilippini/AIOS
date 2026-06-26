---
date: 2026-06-14
time: 13:18
project: hermes / local-model
status: delivered & working — local model + Hermes 0.16.0 + PWA app all done; main open item is tunnel persistence
next-session: DONE this session: local Qwen3 wired into Hermes as `local`/`local-fast` (tested end-to-end), Hermes upgraded 0.15.1->0.16.0 on the VPS (config survived migration), and the Workspace installed as a PWA on the Mac (chrome-less app window with the agent bar — Annabel's chosen "widget"; native Electron widget deferred by choice). ONE real durability gap: all SSH tunnels (reverse 11434 for Ollama; forward 3001/8642/9119 for UI/gateway/dashboard) are MANUAL and die on reboot/sleep, which breaks the PWA, Telegram->local, and VPS-CLI->local paths (raw `ollama run` on the Mac still works offline). Next if asked: install launchd LaunchAgents on the Mac to auto-restart the tunnels (key ~/.ssh/id_ed25519). Optional: keep the local model warm (Ollama keep_alive) to avoid ~80s cold loads.
---

# Session: Local model (Ollama + Qwen3) wired into Hermes as the `local` agent

## Why

After the "frontier model could get banned" idea (Greg Isenberg video), Annabel
wanted a local-model fallback: one Hermes agent that uses a free local model
instead of the cloud default, for (a) running things cheaply and (b) insurance
if cloud models (OpenAI/Claude) become unavailable. Goal was ONE agent on local,
not converting the whole Hermes setup.

## Architecture (important)

- Hermes runs on the Hetzner VPS (`root@5.78.218.220`), default model `gpt-5.5`
  via `openai-codex`. NOT on the Mac.
- The local model runs on the Mac (MacBook Pro M4 Pro, 24GB unified, 16-core GPU)
  via Ollama.
- A reverse SSH tunnel exposes the Mac's Ollama to the VPS so a Hermes agent can
  reach it: `ssh -R 11434:127.0.0.1:11434` (Mac -> VPS).
- Flow for the local agent: phone/SSH -> VPS (Hermes) -> reverse tunnel -> Mac
  (Ollama/Qwen3) -> back. So Hermes paths need internet (they cross the VPS);
  only raw `ollama run` on the Mac is fully offline.

## What was set up

Mac (via Homebrew):

- Installed Ollama (v0.30.8), running as `brew services` (homebrew.mxcl.ollama).
  Plist already includes OLLAMA_FLASH_ATTENTION=1 + OLLAMA_KV_CACHE_TYPE=q8_0.
- Pulled `qwen3:8b` (5.2GB) and `qwen3:14b` (9.3GB).
- Created 64K-context variants (Modelfile `PARAMETER num_ctx 65536`, reuses
  blobs): `qwen3-64k:8b`, `qwen3-64k:14b`. Ollama caps actual context at Qwen3's
  native 40960, which is fine for short tasks.

VPS (Hermes config `/root/.hermes/config.yaml`, backed up to
`config.yaml.bak.local-model-setup`), all via `hermes config set`:

- `model_aliases.local`      = qwen3-64k:14b, provider custom, base_url
  <http://127.0.0.1:11434/v1>, context_length 65536, reasoning_effort none
- `model_aliases.local-fast` = same but qwen3-64k:8b
- `providers.local` = base_url loopback + per-model context_length 65536 (clears
  Hermes's 64K floor; scoped to the local endpoint, leaves gpt-5.5 untouched)
- `model.ollama_num_ctx` = 65536 (global; only applies to local Ollama endpoints)

## Key gotchas learned (Hermes + Ollama)

- Hermes requires a model with >=64K context. Qwen3 reports 40960, so it refuses
  unless you override. The override that WORKS is per-model under the provider:
  `providers.<name>.models.<model>.context_length` (matched by base_url). An
  alias-level `context_length` did NOT take effect.
- For a loopback `base_url`, Hermes auto-trusts it, needs NO api_key, and
  auto-detects API mode. `provider: custom` is the type for OpenAI-compatible
  local endpoints (confirmed in Hermes' own ollama test).
- Qwen3 "thinking" mode was the latency killer: ~8s of hidden reasoning even for
  a 3-word reply. Fix: `reasoning_effort: none` on the alias (Hermes sends it
  top-level to local endpoints). Dropped per-call latency from 33-54s to ~8s.
- Ollama loads at 4096 ctx by default and reloads per call if num_ctx mismatches
  (slow). Baking `num_ctx` into a Modelfile variant makes it load once.

## Performance (tested)

- Raw Ollama on the Mac (think off): sub-second to ~1s.
- Via Hermes (`hermes -m local-fast`, warm, think off): ~8s/turn (dominated by
  Hermes's agent prompt + CLI startup, not the model). Cold model load 15-130s.

## How to use it (command cheat-sheet)

- Telegram (your agent, switch the brain to local):
    /model local          -> Qwen3 14B on the Mac (quality)
    /model local-fast     -> Qwen3 8B on the Mac (faster/cheaper)
    (switch back with /model and pick gpt-5.5)
- VPS CLI: `hermes -m local -z "..."`  (or `-m local-fast`)
- Fully offline, raw model on the Mac (no VPS, no internet):
    `ollama run qwen3:8b "..."`   (or qwen3:14b)
- Restart tunnel if local paths stop working (run on the Mac):
    `ssh -f -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -R 11434:127.0.0.1:11434 root@5.78.218.220`
- Health checks:
    Mac:  `ollama ps`  /  `ollama list`
    VPS:  `ssh root@5.78.218.220 'curl -s localhost:11434/api/version'` (should
          return a version if the tunnel is up)

## Cost / connectivity model

- `local` / `local-fast` = free local inference, does NOT use OpenAI/Claude subs.
- Cloud subscription is only spent on the default model (gpt-5.5).
- Hermes local paths still need internet (route via VPS + tunnel). Only raw
  `ollama run` on the Mac is truly offline.
- Footnote: some Hermes auxiliary helpers (title-gen, compression) are
  `provider: auto` and may still touch the cloud default; not yet pinned to local.

## Update 2026-06-14 (~19:45): Hermes upgraded 0.15.1 -> 0.16.0

- Ran `hermes update --backup --yes` on the VPS (was 1179 commits behind main).
  Stopped gateway first, ran in a detached tmux `hermes-update`, restarted after.
- Pre-update full backup: `/root/hermes-backup-pre-update-20260614.zip` (88MB,
  restore with `hermes import`). Code rollback commit: `fe709a421`.
- Config migration reported "Configuration is up to date" — local-model aliases
  and `providers.local` overrides SURVIVED intact, re-tested working end-to-end
  on 0.16.0 (cold load ~80s for the 64k variant, warm ~8s).
- Gateway + dashboard restarted (tmux `hermes` / `hermes-dashboard`); health
  `{"status":"ok","version":"0.16.0"}`. Telegram should auto-reconnect.
- Cold-load latency note: the Mac evicts the model after idle; consider a longer
  Ollama keep_alive to keep `local`/`local-fast` warm.

## Delivered this session (final state, Annabel signed off "this looks good")

- Local model usable 3 ways: `/model local` (Telegram), `hermes -m local` (VPS
  CLI), `ollama run qwen3:8b` (fully offline on the Mac).
- Hermes upgraded to 0.16.0; gateway healthy; Telegram back online.
- Workspace installed as a PWA on the Mac (Chrome -> address-bar install). It's a
  chrome-less app window with the agent bar at the bottom — the chosen "floating
  widget" for now. Pin via Dock icon -> Options -> Keep in Dock. PWA loads
  localhost:3001, so it needs the forward tunnel up.
- Native Electron desktop widget was offered and DECLINED (more work + uncertain
  remote-backend wiring); the PWA is the accepted substitute.

## Open items

1. Tunnel persistence (launchd) — the one real durability gap, and Annabel said
   "no that's ok" for now. ALL tunnels are manual (reverse 11434 Ollama; forward
   3001/8642/9119 UI/gateway/dashboard) and die on reboot/sleep. Until done, after
   a reboot she must re-run the tunnel commands (see cheat-sheet above) or the
   PWA / Telegram->local / CLI->local paths break. Raw `ollama run` still works.
2. (Optional) Keep the local model warm via Ollama keep_alive — avoids ~80s cold loads.
3. (Deferred by choice) Native desktop widget — install Hermes+Node on the Mac,
   `hermes desktop` to build the Electron app, wire to the VPS gateway.
4. (Optional) Pin Hermes auxiliary helpers to local for guaranteed zero-cloud.
5. (Optional) Tiny always-on model on the VPS for laptop-closed Telegram insurance.
6. (Optional) Dedicated standalone `local` profile vs the current `/model local` switch.
