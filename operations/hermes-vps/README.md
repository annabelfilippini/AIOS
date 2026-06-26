# Hermes VPS Runbook

Hermes runs on the Hetzner VPS at `root@5.78.218.220`.

## Current Layout

- VPS Hermes workspace: `/root/hermes-workspace`
- VPS AI-OS workspace: `/root/AI-OS`
- Hermes config and runtime data: `/root/.hermes`
- Workspace UI: remote `3000`, local tunnel `3001`
- Gateway API: remote/local `8642`
- Dashboard: remote/local `9119`

## Check Status

```sh
ssh -o BatchMode=yes root@5.78.218.220 pgrep -af hermes
ssh -o BatchMode=yes root@5.78.218.220 ss -ltnp
ssh -o BatchMode=yes root@5.78.218.220 tmux list-sessions
ssh -o BatchMode=yes root@5.78.218.220 hermes status
```

Expected remote listeners:

- `0.0.0.0:3000` for the workspace UI
- `127.0.0.1:8642` for the gateway
- `127.0.0.1:9119` for the dashboard

## Restore Local Access

**Tunnels auto-restart via launchd** (see "Tunnel Persistence" below) — they
recover on their own across sleep/reboot, usually within ~10-40s. If the app
shows "Hermes unavailable" and you don't want to wait, force an immediate
restart: run `hermes-up` (alias in `~/.zshrc`) or double-click
`~/Desktop/Start Hermes.command` (both kick the launchd agents).

Manual equivalent:

```sh
ssh -f -N -L 3001:127.0.0.1:3000 -L 8642:127.0.0.1:8642 root@5.78.218.220
ssh -f -N -L 9119:127.0.0.1:9119 root@5.78.218.220
ssh -f -N -R 11434:127.0.0.1:11434 root@5.78.218.220   # local model (Mac Ollama -> VPS)
```

Verify locally:

```sh
curl -I --max-time 6 http://127.0.0.1:3001
curl -sS --max-time 6 http://127.0.0.1:8642/health
curl -sS --max-time 6 http://127.0.0.1:9119
```

## Tunnel Persistence (launchd)

Two LaunchAgents keep the tunnels alive and auto-restart them across Mac
sleep/reboot (replaces the old manual `ssh -f` approach). Self-heal verified:
killing a tunnel ssh respawns it in ~10-15s.

- `com.aios.hermes.tunnels.fwd` — forwards 3001->3000 (UI), 8642 (gateway), 9119 (dashboard)
- `com.aios.hermes.tunnels.rev` — reverse 11434 (Mac Ollama -> VPS, local model)

Plists live in `~/Library/LaunchAgents/` (source copies in this folder). They use
the passphrase-less key `~/.ssh/id_ed25519`, `KeepAlive=true`, and SSH keepalives,
so a dropped tunnel is detected and respawned automatically. Logs:
`~/Library/Logs/hermes-tunnels-fwd.log` / `-rev.log`.

```sh
launchctl list | grep aios.hermes                                      # status (PID + last exit)
launchctl kickstart -k gui/$(id -u)/com.aios.hermes.tunnels.fwd        # force restart (or: hermes-up)
launchctl bootout   gui/$(id -u)/com.aios.hermes.tunnels.fwd           # stop/disable
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.aios.hermes.tunnels.fwd.plist  # (re)install
```

After editing a plist, `bootout` then `bootstrap` it. To restore from the repo
copies, cp them into `~/Library/LaunchAgents/` first. (Same commands for `.rev`.)

## Restart Remote Hermes

Hermes currently runs in tmux sessions named `hermes` and `hermes-dashboard`.
Attach first if you need to inspect live output:

```sh
ssh root@5.78.218.220
tmux attach -t hermes
tmux attach -t hermes-dashboard
```

If the remote processes are down, restart them from the VPS:

```sh
cd /root/hermes-workspace
tmux new-session -d -s hermes 'pnpm start:all'
tmux new-session -d -s hermes-dashboard 'hermes dashboard --no-open --skip-build'
```

Smoke-test model auth:

```sh
ssh -o BatchMode=yes root@5.78.218.220 "hermes --ignore-rules -z 'Reply exactly: hermes smoke ok'"
```

## Model Picker Patch (hide the local / "LIBRARY" group)

The Workspace model picker otherwise lists the loopback `local` Ollama provider
as its own "LIBRARY" group, duplicating the tuned `local` / `local-fast`
aliases. We patch `hermes_cli/inventory.py:build_models_payload` to drop that
provider row. `providers.local` STAYS in `config.yaml` because it supplies the
64k `context_length` override the aliases need (removing it breaks them with a
"context window below the minimum 64,000" error).

The patch is overwritten by `hermes update`. Re-apply + restart after any update:

```sh
ssh root@5.78.218.220 'python3 /root/.hermes/aios-patches/hide-local-picker.py'
ssh root@5.78.218.220 'tmux kill-session -t hermes; cd /root/hermes-workspace && tmux new-session -d -s hermes "pnpm start:all"'
```

Script source of truth: `operations/hermes-vps/hide-local-picker.py` (idempotent;
exits non-zero without writing if Hermes internals change and the anchor is
gone). Config backups from this work: `config.yaml.bak.hide-library`,
`config.yaml.bak.trim`; original file at `inventory.py.bak.aios`.
