# The Day — Phone Access Runbook

Reach the planner from your iPhone anywhere (cellular or any WiFi), behind HTTPS + a private-link key.

## URL & login

- **Home-screen link (contains the key):**
  `https://planner.5-78-218-220.sslip.io/planner.html?k=<THEDAY_KEY>`
- **Auth = secret-link cookie**, NOT a password. The key lives in `.env`
  (`THEDAY_KEY=`, gitignored). Opening the `?k=` link sets a 1-year `tdk` cookie
  (Secure/HttpOnly) then redirects to the clean URL, so the home-screen app opens
  with no prompt (and re-auths invisibly from the link if the cookie is ever cleared).
- Basic auth was REMOVED (2026-06-23): iOS can't autofill the Basic Auth dialog in a
  standalone home-screen web app and re-prompted every cold launch. The gate now
  lives in `serve.py` `Handler._gate()`.
- **Rotate / revoke:** change `THEDAY_KEY` in `.env`, restart the agent
  (`launchctl kickstart -k gui/$(id -u)/com.annabel.theday`), hand out the new
  `?k=` link. Instantly logs out every device. Treat the link like a password.

## How it works (the chain)

```
iPhone → https://planner.5-78-218-220.sslip.io  (Let's Encrypt cert, TLS only)
       → Traefik (coolify-proxy) on Hetzner VPS 5.78.218.220   (no auth here anymore)
       → reverse SSH tunnel  VPS 172.17.0.1:8802 → Mac 127.0.0.1:8802
       → serve.py planner on the Mac (gates on the tdk cookie; Google login never leaves the Mac)
```

The Mac must be **awake and online** — there is no cloud copy of the app. The
VPS is only a relay; it never sees or stores calendar/email data.

## Pieces

1. **VPS sshd:** `GatewayPorts clientspecified` (backup at
   `/etc/ssh/sshd_config.bak.planner`). Lets the reverse tunnel bind the docker
   bridge IP so Traefik can reach it.
2. **Mac reverse tunnel:** launchd agent `com.annabel.theday.tunnel`
   (`~/Library/LaunchAgents/`, source copy in this folder). KeepAlive + self-heal,
   uses key `~/.ssh/id_ed25519`. Log: `~/Library/Logs/theday-tunnel.log`.
3. **Traefik route:** `/data/coolify/proxy/dynamic/planner.yaml` on the VPS —
   single router (Host rule) + `letsencrypt` TLS + service
   `http://host.docker.internal:8802`. NO auth middleware anymore (auth is the
   `tdk` cookie checked in `serve.py` `_gate()`). Traefik hot-reloads the dir.
   `_gate` lets `/apple-touch-icon.png` through unauthenticated so iOS can fetch
   the home-screen icon with no creds. Initial paint: `boot()` renders the
   calendar first, then loads inbox/emails async (email was the slow blocker).

## Home-screen app (PWA)

`planner.html` has `apple-mobile-web-app-capable`, `apple-mobile-web-app-title`
("The Day"), `theme-color`, and `<link rel="apple-touch-icon" href="apple-touch-icon.png">`
(branded 1024px cream calendar, generated with Pillow; source step in session
2026-06-23). Safari → Share → Add to Home Screen → opens full-screen, no chrome.
If the icon shows as a screenshot, iOS cached a pre-fix miss: delete the icon,
hard-reload the page in Safari, re-add (or Clear Safari website data).

## Local development / quick open

```sh
# Mac only: opens the live Morning Edit locally
cd ~/Documents/AI-OS/projects/day-planner
python3 serve.py --morning

# Same Wi-Fi phone preview (temporary; exposes the app to your LAN while running)
python3 serve.py --morning --lan
ipconfig getifaddr en0
# Then on iPhone: http://<that-ip>:8802/morning.html
```

By default `serve.py` binds to `127.0.0.1`, so `http://<Mac-IP>:8802/...` will NOT work unless you start it with `--lan`.

## Manage

```sh
# tunnel status / restart (Mac)
launchctl list | grep theday.tunnel
launchctl kickstart -k gui/$(id -u)/com.annabel.theday.tunnel
launchctl bootout   gui/$(id -u)/com.annabel.theday.tunnel   # disable

# end-to-end test from anywhere
curl -I -u annabel:PASSWORD https://planner.5-78-218-220.sslip.io/planner.html  # expect 200
curl -I https://planner.5-78-218-220.sslip.io/planner.html                      # expect 401

# change the password: regenerate hash and edit the users line in
#   /data/coolify/proxy/dynamic/planner.yaml   (Traefik reloads automatically)
htpasswd -nbB annabel 'NEWPASS'
```

## Undo / tear down

```sh
launchctl bootout gui/$(id -u)/com.annabel.theday.tunnel        # stop tunnel (Mac)
rm ~/Library/LaunchAgents/com.annabel.theday.tunnel.plist
ssh root@5.78.218.220 'rm /data/coolify/proxy/dynamic/planner.yaml'   # drop the route
# (optional) revert sshd: restore /etc/ssh/sshd_config.bak.planner then `systemctl reload ssh`
```

## Notes / gotchas

- Mac asleep = planner unreachable. To keep it always reachable, prevent sleep
  while plugged in (System Settings → Battery → keep awake on power).
- The planner can now **send** email (`/api/send`, `/api/draft`) — the password
  gate is what keeps that safe on the public internet. Do not remove it.
- If the OAuth consent screen for project `aj-bot-489823` is in "testing", the
  Google refresh token still expires ~7 days → re-run `auth_google.py` on the Mac.
- Port collision reminder: the `com.annabel.theday` launchd agent owns Mac port
  8802; the tunnel forwards to it. Don't `preview_start` on 8802.
