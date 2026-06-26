---
date: 2026-06-14
time: 14:30
project: hermes / local-model
status: diagnosed — root cause found, working fix given (use /model in chat); no code change made
next-session: Local-model backend is 100% healthy (verified end-to-end). The app's web model picker is the problem: it does NOT hot-swap the running chat. If Annabel wants the picker itself to work, options are (a) watch her screen to see which picker she opens, (b) make `local` show up properly / pin a reliable in-chat swap, or (c) just standardize on typing `/model local` / `/model local-fast`. Still-open infra item from the 13:18 checkpoint: tunnels are manual and die on reboot/sleep — install launchd LaunchAgents (key ~/.ssh/id_ed25519) for durability.
---

# Session: Why "click local in the Hermes app doesn't switch models" — diagnosed

## The question

Annabel: in the Hermes app she has the option to switch to the local model, but
clicking "local" doesn't switch the model. Why?

## Verdict

The local model and all infrastructure are fine. The bug is in the **web model
picker's apply path** — it does not hot-swap the currently running chat.

## What was verified (all green, 2026-06-14)

- Ollama running on the Mac with all 4 models (qwen3:8b/14b, qwen3-64k:8b/14b).
- All SSH tunnels UP: reverse 11434 (Ollama→VPS), forward 3001/8642/9119.
- VPS reaches the Mac's Ollama through the tunnel (`curl localhost:11434/api/version`
  → `{"version":"0.30.8"}`, lists all models).
- Hermes 0.16.0 healthy on the VPS (`root@5.78.218.220`).
- `model_aliases.local`/`local-fast` and `providers.local` intact in
  `/root/.hermes/config.yaml`; `model.default` still `gpt-5.5`.
- **End-to-end proof:** `hermes -m local-fast -z "...PONG"` → returned `PONG`.
- `switch_model()` resolves BOTH `qwen3-64k:14b --provider local` (what the UI
  sends) AND the `local` alias to the loopback endpoint, success=True.

## Root cause (web UI, not infra)

From the 0.16.0 web bundle (`web_dist/assets/index-*.js`) + `web_server.py`:

- The picker is built by `inventory.build_models_payload()` and lists the `local`
  **provider's raw models** (qwen3-64k:14b etc.), authenticated=True — NOT the
  tuned `model_aliases` (`local`/`local-fast`, which carry `reasoning_effort:none`).
- Two apply paths, neither switches the live chat:
  1. "Set as default" → `POST /api/model/set` → `set_model_assignment`, whose own
     docstring says *"applies to NEW sessions only; the running chat is not
     affected"*. (Confirmed: `model.default` is still `gpt-5.5`, so this path
     never persisted.)
  2. In-chat hot-swap (gateway RPC `config.set` w/ `session_id`, or `i()` command
     injection of `/model <model> --provider <provider>`) → only fires with a
     live gateway session bound; otherwise it's a silent no-op.

## Fix given to Annabel

- Type in the chat: `/model local` (14B, quality) or `/model local-fast` (8B,
  faster — warm right now). Proven path; also faster than the picker because the
  aliases disable Qwen3 "thinking".
- Heads-up: first message after switching to a cold model = ~60–130s load on the
  Mac (can look like "nothing happened").

## Open items

1. Make the picker itself reliable (or surface the aliases in it) — optional;
   `/model` works today.
2. Tunnel persistence via launchd — still REQUIRED for durable access (carried
   over from the 13:18 checkpoint; not done).

## Note

This session exposed upstream OAuth tokens in `/root/.hermes/auth.json` in tool
output (Nous JWT, OpenAI ChatGPT OAuth for <annabelflip1@gmail.com>). Not reused or
transmitted. Consider rotating if that output was logged anywhere shared.
