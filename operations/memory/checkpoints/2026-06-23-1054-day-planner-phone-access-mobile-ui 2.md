---
date: 2026-06-23
time: 10:54
project: day-planner ("The Day")
status: SHIPPED — planner reachable on her phone (anywhere), mobile UI rebuilt, home-screen app, password swapped for a self-healing private link.
---

# Session: The Day — phone access + mobile UI + home-screen app

## Why
Annabel wanted her planner (calendar + to-dos + pressing email) on her phone,
always available, ideally a home-screen app and a lock-screen glance.

## What shipped
- **Anywhere access** via her existing Hetzner VPS (`5.78.218.220`, runs Coolify
  + Traefik). Chain: iPhone → Traefik (TLS, Let's Encrypt) → reverse SSH tunnel
  `VPS 172.17.0.1:8802 → Mac 127.0.0.1:8802` → `serve.py`. App stays on the Mac;
  VPS is only a relay. URL `https://planner.5-78-218-220.sslip.io/planner.html`.
  - VPS sshd `GatewayPorts clientspecified` (backup `sshd_config.bak.planner`).
  - Mac launchd tunnel `com.annabel.theday.tunnel` (KeepAlive/self-heal, source
    plist in project). Traefik route `/data/coolify/proxy/dynamic/planner.yaml`.
  - **Mac must be awake** (no cloud copy).
- **Mobile UI** (responsive, all under `@media (max-width:760px)`; desktop
  3-column untouched): three desktop columns become Day / To-dos / Mail bottom
  tabs (Day default), pull-up Inbox tray on Day, single-tap event edit, branded.
- **Time-proportional timeline**: removed the `.tl-line` connector; `.gap` spacers
  size to free time (`min*0.55`px).
- **Home-screen app (PWA)**: apple-mobile-web-app meta + `apple-touch-icon.png`
  (1024px cream calendar, Pillow-drawn). Opens full-screen.
- **Auth swapped basic-auth → private-link cookie** (iOS couldn't autofill the
  Basic Auth dialog in standalone PWA, re-prompted every launch + slow).
  `serve.py Handler._gate()` authorizes via tdk cookie OR `X-Day-Key` header OR
  `?k=<THEDAY_KEY>` (key in `.env`). Link sets a 1yr Secure/HttpOnly cookie (no
  redirect). Page stashes key in localStorage + `fetch` wrapper attaches header →
  saves work even if iOS drops the cookie. Traefik basicAuth removed.
- **Speed**: `boot()` paints calendar first, defers inbox/emails.
- Lock-screen glance: she chose Apple's native Calendar widget (events only,
  works Mac-off, reads her Google Calendar). Steps given; nothing to build.

## Operate
- Edit `planner.html`/`serve.py` on the Mac → live instantly (no-store + tunnel).
  After `serve.py` changes: `launchctl kickstart -k gui/$(id -u)/com.annabel.theday`.
- Home-screen link: `…/planner.html?k=YKdiWKT97K277mDIUKvAjrIyGW11H8f_`.
- Rotate key: change `THEDAY_KEY` in `projects/day-planner/.env`, restart agent.
- Runbook: `projects/day-planner/PHONE-ACCESS.md`.

## Still open
- Annabel must **re-add the home-screen icon from the `?k=` link** (old cached
  PWA had no key → "can't add events"; the self-heal + re-add fixes it).
- Offered but not done: Scriptable lock-screen widget (events + to-dos in her
  cream/serif style, needs Mac awake); set Mac to stay awake on power.
