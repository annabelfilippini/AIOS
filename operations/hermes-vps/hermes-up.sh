#!/usr/bin/env bash
# hermes-up — force an immediate restart of the Hermes SSH tunnels.
#
# Tunnels are normally kept alive AUTOMATICALLY by launchd (LaunchAgents
# com.aios.hermes.tunnels.fwd + .rev), which auto-restart them across Mac
# sleep/reboot. You rarely need this script. Use it only to force an
# instant restart instead of waiting ~10-40s for launchd's own retry.
#
# Usage:  hermes-up   (or double-click ~/Desktop/Start Hermes.command)
#
# If the launchd agents aren't installed, it falls back to starting the
# tunnels directly. To (re)install the agents, see operations/hermes-vps/README.md.

U=$(id -u)
VPS="root@5.78.218.220"
FWD=com.aios.hermes.tunnels.fwd
REV=com.aios.hermes.tunnels.rev

if launchctl list 2>/dev/null | grep -q "com.aios.hermes.tunnels"; then
  echo "Kicking launchd tunnel agents..."
  launchctl kickstart -k "gui/$U/$FWD" 2>/dev/null && echo "  ok  $FWD"
  launchctl kickstart -k "gui/$U/$REV" 2>/dev/null && echo "  ok  $REV"
else
  echo "launchd agents not installed — starting tunnels directly..."
  OPTS=(-f -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=3)
  pkill -f "ssh.*-L 3001:127.0.0.1:3000"   2>/dev/null
  pkill -f "ssh.*-L 9119:127.0.0.1:9119"   2>/dev/null
  pkill -f "ssh.*-R 11434:127.0.0.1:11434" 2>/dev/null
  sleep 1
  ssh "${OPTS[@]}" -L 3001:127.0.0.1:3000 -L 8642:127.0.0.1:8642 "$VPS" && echo "  ok  UI + gateway"
  ssh "${OPTS[@]}" -L 9119:127.0.0.1:9119 "$VPS"                        && echo "  ok  dashboard"
  ssh "${OPTS[@]}" -R 11434:127.0.0.1:11434 "$VPS"                      && echo "  ok  local model reverse"
fi

echo
echo "Waiting for tunnels to come up..."
for i in $(seq 1 10); do
  curl -s --max-time 4 localhost:8642/health 2>/dev/null | grep -q '"status": "ok"' && break
  sleep 2
done
if curl -s --max-time 5 localhost:8642/health 2>/dev/null | grep -q '"status": "ok"'; then
  echo "DONE - Hermes is up. Refresh the app."
else
  echo "WARN - gateway did not answer yet. Give it a few seconds, or check the VPS"
  echo "       (operations/hermes-vps/README.md -> 'Restart Remote Hermes')."
fi
