---
date: 2026-06-14
time: 19:45
project: hermes / local-model
status: delivered & verified — SSH tunnels now auto-persist via launchd; self-heal tested
next-session: DONE — the recurring "Hermes unavailable / app won't open" problem is fixed. Two macOS LaunchAgents now keep the Mac<->VPS SSH tunnels alive and auto-restart them across sleep/reboot (verified self-heal: killed a tunnel, launchd respawned it in ~14s). This closes the long-standing #1 open item (tunnel persistence) from the 2026-06-14-1318 and -1920 checkpoints. Remaining optional items: pin Hermes auxiliary helpers to local for zero-cloud; tiny always-on VPS model for laptop-closed Telegram; native `hermes desktop` Electron app (she currently uses the PWA "Hermes Workspace"; Hermes is NOT installed on the Mac, which is why `hermes desktop` doesn't exist there).
---

# Session: Hermes tunnels made persistent with launchd

## Problem (recurring all session)

The Mac<->VPS SSH tunnels were manual (`ssh -f`) and died on sleep/reboot,
repeatedly breaking the Workspace PWA ("Hermes unavailable" / "won't open"),
Telegram->local, and the local model. Hit 3+ times today.

## Fix delivered

Two user LaunchAgents in `~/Library/LaunchAgents/` (source copies in
`operations/hermes-vps/`):

- `com.aios.hermes.tunnels.fwd` — `-L 3001:3000` (UI), `-L 8642` (gateway),
  `-L 9119` (dashboard)
- `com.aios.hermes.tunnels.rev` — `-R 11434` (Mac Ollama -> VPS, local model)

Split into two agents so a reverse-tunnel hiccup can't take down the app's
forward tunnels. Each runs FOREGROUND `ssh -N` (no `-f`) so launchd supervises
the real ssh process; `KeepAlive=true` + `ServerAliveInterval=30`/`CountMax=3` +
`ExitOnForwardFailure=yes` + `ConnectTimeout=15` + `ThrottleInterval` 10/15.
Auth: passphrase-less `~/.ssh/id_ed25519` (verified passphrase-less, perms 600),
so launchd needs no ssh-agent/keychain.

## Verified

- Bootstrapped both via `launchctl bootstrap gui/$(id -u) <plist>`; both show in
  `launchctl list` with exit code 0; all four ports UP.
- SELF-HEAL: `kill -9` the fwd ssh -> ports DOWN -> launchd respawned it ~14s
  later (new PID) -> ports UP -> gateway `{"status":"ok"}` through the new tunnel.
- Exactly one ssh per tunnel (no duplicates).

## Tooling updated

- `operations/hermes-vps/hermes-up.sh` rewritten: now `launchctl kickstart -k`
  the agents (force restart) instead of spawning parallel `ssh -f` tunnels;
  falls back to direct tunnels if agents aren't installed. Desktop
  "Start Hermes.command" still calls it.
- `operations/hermes-vps/README.md`: new "Tunnel Persistence (launchd)" section
  (status/kickstart/bootout/bootstrap commands, logs at
  `~/Library/Logs/hermes-tunnels-{fwd,rev}.log`); "Restore Local Access" reframed
  (launchd primary, hermes-up = force-restart).

## Manage cheat-sheet

- Status: `launchctl list | grep aios.hermes`
- Force restart: `hermes-up` (or `launchctl kickstart -k gui/$(id -u)/com.aios.hermes.tunnels.fwd`)
- Disable: `launchctl bootout gui/$(id -u)/com.aios.hermes.tunnels.fwd` (+ `.rev`)
- Reinstall: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.aios.hermes.tunnels.fwd.plist`
