#!/usr/bin/env python3
"""Kite Wind Watch — hourly wind alerter.

Two triggers, matched to the dashboard's accuracy:
  1. FORECAST — a blended Open-Meteo forecast (Best Match + NOAA HRRR + GFS,
     averaged hour by hour) shows gusts at/above the threshold inside the
     lookahead window.
  2. LIVE NOW — the nearest real station (Synoptic if a token is configured,
     else NWS) is *currently* blowing at/above the threshold (daylight only).

Sends one consolidated Telegram + macOS alert, including the real current
reading for context. De-dupes: a forecast day pings once per spot (re-pings if
the peak climbs); a "blowing now" pings once per spot per day.

Read-only, Python stdlib only.

Operate:
  python3 scraper/wind_alert.py          # normal run (sends if windy)
  python3 scraper/wind_alert.py --dry    # print, never send, ignore state
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# ---- settings (chosen by Annabel) ----
GUST_THRESHOLD_KN = 18      # gusts at/above this = "very windy"
LOOKAHEAD_HOURS = 48        # how far ahead to look
RIDE_START_HOUR = 6         # only count daylight-ish hours (local)
RIDE_END_HOUR = 21
REALERT_RISE_KN = 3         # re-ping a day only if peak climbs this much
TZ = "America/Denver"
DENVER = ZoneInfo(TZ)       # forecast times are Denver-local; reason in Denver
                            # time regardless of the server's clock (VPS = UTC)

HOME = os.path.expanduser("~")
HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_JS = os.path.join(HERE, "..", "config.js")
STATE_DIR = os.path.join(HOME, ".local", "share", "kite-wind-watch")
STATE_FILE = os.path.join(STATE_DIR, "alert_state.json")
TELEGRAM_ENV = os.path.join(HOME, ".claude", "channels", "telegram", ".env")
TELEGRAM_CHAT_ID = "8519804405"


def _load_local_env():
    """On a server (no Mac config), load TELEGRAM_BOT_TOKEN / SYNOPTIC_TOKEN from
    a .env sitting next to this script. No-op on the Mac (file absent)."""
    p = os.path.join(HERE, ".env")
    if not os.path.exists(p):
        return
    try:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except Exception:  # noqa: BLE001
        pass


_load_local_env()

# Blended forecast models (endpoint, Open-Meteo model id). None = Best Match.
OM_MODELS = [
    ("https://api.open-meteo.com/v1/forecast", None),            # Best Match
    ("https://api.open-meteo.com/v1/gfs", "ncep_hrrr_conus"),     # NOAA HRRR (3km)
    ("https://api.open-meteo.com/v1/gfs", "gfs_global"),          # NOAA GFS
]

# ---- tracked spots (mirrors index.html SPOTS) ----
SPOTS = [
    {"name": "Aurora Reservoir",        "region": "Denver Front Range",       "lat": 39.61,   "lon": -104.66},
    {"name": "Cherry Creek Reservoir",  "region": "Denver Front Range",       "lat": 39.638,  "lon": -104.8501},
    {"name": "Chatfield Reservoir",     "region": "Denver Front Range",       "lat": 39.5475, "lon": -105.0669},
    {"name": "Union Reservoir",         "region": "Longmont · Front Range",   "lat": 40.1797, "lon": -105.0383},
    {"name": "Boyd Lake",               "region": "Loveland · Front Range",   "lat": 40.4402, "lon": -105.0362},
    {"name": "Lake Dillon",             "region": "Colorado mountains",       "lat": 39.6173, "lon": -106.0558},
    {"name": "Pueblo Reservoir",        "region": "Southern Colorado",        "lat": 38.2674, "lon": -104.7382},
    {"name": "Lake McConaughy",         "region": "Nebraska · driveable",     "lat": 41.245,  "lon": -101.808},
    {"name": "Lake Hattie Reservoir",   "region": "Wyoming · Laramie (Dad)",  "lat": 41.2435, "lon": -105.9285},
    {"name": "Twin Buttes Lake",        "region": "Wyoming · Laramie (Dad)",  "lat": 41.2387, "lon": -105.8622},
    {"name": "Williams Fork Reservoir", "region": "Colorado · Grand Co (Dad)","lat": 40.0178, "lon": -106.2116},
]

COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


def log(msg):
    print(f"{datetime.now():%Y-%m-%d %H:%M} {msg}", flush=True)


def deg_to_compass(deg):
    if deg is None:
        return "?"
    return COMPASS[int((deg / 22.5) + 0.5) % 16]


def get_json(url, headers=None):
    h = headers or {"Accept": "application/json", "User-Agent": "kite-wind-watch/1.0"}
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def read_synoptic_token():
    try:
        with open(CONFIG_JS) as f:
            m = re.search(r'synopticToken:\s*"([^"]+)"', f.read())
        if m:
            tok = m.group(1).strip()
            if tok and not tok.startswith("PASTE_"):
                return tok
    except Exception:  # noqa: BLE001
        pass
    env = (os.environ.get("SYNOPTIC_TOKEN") or "").strip()
    return env or None


def kn_from(value, unit):
    if value is None:
        return None
    u = unit or ""
    if "km_h" in u or "km/h" in u:
        return value * 0.539957
    if "m_s" in u or "m/s" in u:
        return value * 1.94384
    return value


# ---------- blended forecast ----------
def _fetch_model(spot, endpoint, model):
    params = {
        "latitude": spot["lat"],
        "longitude": spot["lon"],
        "hourly": "wind_speed_10m,wind_gusts_10m,wind_direction_10m",
        "wind_speed_unit": "kn",
        "timezone": TZ,
        "forecast_days": 3,
    }
    if model:
        params["models"] = model
    url = endpoint + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            return get_json(url, headers={"User-Agent": "kite-wind-watch/1.0"}).get("hourly", {})
        except Exception:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
    return None


def fetch_forecast(spot):
    """Blend the models: average gust/wind per timestamp across whichever return."""
    agg = {}
    got = False
    for endpoint, model in OM_MODELS:
        h = _fetch_model(spot, endpoint, model)
        if not h:
            continue
        got = True
        times = h.get("time", [])
        gusts = h.get("wind_gusts_10m", [])
        winds = h.get("wind_speed_10m", [])
        dirs = h.get("wind_direction_10m", [])
        for i, t in enumerate(times):
            slot = agg.setdefault(t, {"g": [], "w": [], "d": []})
            if i < len(gusts) and gusts[i] is not None:
                slot["g"].append(gusts[i])
            if i < len(winds) and winds[i] is not None:
                slot["w"].append(winds[i])
            if i < len(dirs) and dirs[i] is not None:
                slot["d"].append(dirs[i])
    if not got:
        log(f"  forecast fetch failed for {spot['name']}")
        return []
    out = []
    for t in sorted(agg):
        s = agg[t]
        out.append({
            "dt": datetime.fromisoformat(t),
            "wind": sum(s["w"]) / len(s["w"]) if s["w"] else None,
            "gust": sum(s["g"]) / len(s["g"]) if s["g"] else None,
            "dir": s["d"][0] if s["d"] else None,
            "models": len(s["g"]),
        })
    return out


def find_windy_window(hours, now):
    cutoff = now + timedelta(hours=LOOKAHEAD_HOURS)
    best = None
    for h in hours:
        if h["dt"] < now or h["dt"] > cutoff:
            continue
        if not (RIDE_START_HOUR <= h["dt"].hour <= RIDE_END_HOUR):
            continue
        if h["gust"] is None or h["gust"] < GUST_THRESHOLD_KN:
            continue
        if best is None or h["gust"] > best["gust"]:
            best = h
    return best


# ---------- live observations ----------
def fetch_nws_live(spot):
    try:
        pt = get_json(f"https://api.weather.gov/points/{spot['lat']},{spot['lon']}",
                      headers={"Accept": "application/geo+json", "User-Agent": "kite-wind-watch/1.0"})
        st_url = pt.get("properties", {}).get("observationStations")
        if not st_url:
            return None
        sd = get_json(st_url, headers={"Accept": "application/geo+json", "User-Agent": "kite-wind-watch/1.0"})
        for f in (sd.get("features", []) or [])[:5]:
            sid = f["properties"]["stationIdentifier"]
            try:
                od = get_json(f"https://api.weather.gov/stations/{sid}/observations/latest",
                              headers={"Accept": "application/geo+json", "User-Agent": "kite-wind-watch/1.0"})
            except Exception:  # noqa: BLE001
                continue
            p = od.get("properties", {})
            ws = p.get("windSpeed") or {}
            wind = kn_from(ws.get("value"), ws.get("unitCode"))
            if wind is None:
                continue
            wg = p.get("windGust") or {}
            wd = p.get("windDirection") or {}
            return {"wind": wind, "gust": kn_from(wg.get("value"), wg.get("unitCode")),
                    "dir": wd.get("value"), "station": sid, "source": "NWS"}
    except Exception as e:  # noqa: BLE001
        log(f"  NWS live failed {spot['name']}: {e}")
    return None


def fetch_synoptic_live(spot, token):
    if not token:
        return None
    try:
        url = ("https://api.synopticdata.com/v2/stations/latest?token=" + urllib.parse.quote(token)
               + f"&radius={spot['lat']},{spot['lon']},30&limit=1"
               + "&vars=wind_speed,wind_gust,wind_direction&units=speed|kts&within=120&obtimezone=utc")
        d = get_json(url)
        st = d.get("STATION") or []
        if not st:
            return None
        o = st[0].get("OBSERVATIONS", {})
        sp = (o.get("wind_speed_value_1") or {}).get("value")
        if sp is None:
            return None
        return {"wind": sp, "gust": (o.get("wind_gust_value_1") or {}).get("value"),
                "dir": (o.get("wind_direction_value_1") or {}).get("value"),
                "station": st[0].get("STID", "stn"), "source": "Synoptic"}
    except Exception as e:  # noqa: BLE001
        log(f"  Synoptic live failed {spot['name']}: {e}")
    return None


def fetch_live(spot, token):
    # prefer Synoptic (denser/closer) when a token is set, else NWS
    return fetch_synoptic_live(spot, token) or fetch_nws_live(spot)


def live_speed(live):
    if not live:
        return None
    return live.get("gust") if live.get("gust") is not None else live.get("wind")


# ---------- state / sending ----------
def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def save_state(state):
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def read_bot_token():
    try:
        with open(TELEGRAM_ENV) as f:
            for line in f:
                line = line.strip()
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    return line.split("=", 1)[1].strip()
    except Exception:  # noqa: BLE001
        pass
    env = (os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
    return env or None


def send_telegram(text):
    token = read_bot_token()
    if not token:
        log("  no telegram token — skipping send")
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "true",
    }).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=payload), timeout=20) as r:
            ok = json.load(r).get("ok", False)
            log(f"  telegram send ok={ok}")
            return ok
    except Exception as e:  # noqa: BLE001
        log(f"  telegram send failed: {e}")
        return False


def disp_speed(r):
    return max(r.get("gust") or 0, r.get("live_speed") or 0)


def send_macos_notification(fresh):
    if sys.platform != "darwin":
        return False  # no desktop notifications on the server; Telegram covers it

    def ascii_clean(s):
        return s.encode("ascii", "ignore").decode().strip()

    top = fresh[0]
    now_count = sum(1 for r in fresh if r.get("live_windy"))
    title = ascii_clean(f"Wind alert - {len(fresh)} spot(s) 18kn+" + (f" - {now_count} blowing NOW" if now_count else ""))
    subtitle = ascii_clean(f"Top: {top['spot']['name']} {disp_speed(top)}kn")
    body = ascii_clean(", ".join(
        f"{r['spot']['name']} {disp_speed(r)}kn" + (" NOW" if r.get("live_windy") else "")
        for r in fresh[:5]))
    script = (
        f'display notification {json.dumps(body)} '
        f'with title {json.dumps(title)} subtitle {json.dumps(subtitle)} '
        f'sound name "Submarine"'
    )
    try:
        r = subprocess.run(["osascript", "-e", script], timeout=10, capture_output=True, text=True)
        if r.returncode != 0:
            log(f"  macOS notification error: {r.stderr.strip()}")
            return False
        log("  macOS notification posted")
        return True
    except Exception as e:  # noqa: BLE001
        log(f"  macOS notification failed: {e}")
        return False


def main():
    dry = "--dry" in sys.argv
    now = datetime.now(DENVER).replace(tzinfo=None)  # naive Denver, matches forecast dt
    daytime = RIDE_START_HOUR <= now.hour <= RIDE_END_HOUR
    token = read_synoptic_token()
    log(f"Wind check — {GUST_THRESHOLD_KN}kn gusts, next {LOOKAHEAD_HOURS}h, {len(SPOTS)} spots, "
        f"blended forecast + live ({'Synoptic+NWS' if token else 'NWS'})" + (" [DRY]" if dry else ""))

    state = {} if dry else load_state()
    today_key = f"{now:%Y-%m-%d}"
    candidates = []

    for spot in SPOTS:
        hours = fetch_forecast(spot)
        peak = find_windy_window(hours, now) if hours else None
        live = fetch_live(spot, token)
        lspd = live_speed(live)
        live_windy = bool(daytime and lspd is not None and lspd >= GUST_THRESHOLD_KN)

        if not peak and not live_windy:
            continue
        rec = {"spot": spot, "live": live}
        if peak:
            rec["peak"] = peak
            rec["gust"] = round(peak["gust"])
            rec["day"] = f"{peak['dt']:%Y-%m-%d}"
        if live_windy:
            rec["live_windy"] = True
            rec["live_speed"] = round(lspd)
        candidates.append(rec)
        log(f"  {spot['name']}: "
            + (f"forecast {rec.get('gust')}kn @ {peak['dt']:%a %H:%M}; " if peak else "")
            + (f"NOW {rec.get('live_speed')}kn" if live_windy else (f"now {round(lspd)}kn" if lspd else "no live")))

    # de-dupe forecast (per spot per windy day) and live (per spot per day)
    fresh = []
    for r in candidates:
        is_fresh = False
        if r.get("peak"):
            key = f"f|{r['spot']['name']}|{r['day']}"
            prev = state.get(key)
            if prev is None or r["gust"] >= prev + REALERT_RISE_KN:
                is_fresh = True
            state[key] = max(r["gust"], prev or 0)
        if r.get("live_windy"):
            key = f"l|{r['spot']['name']}|{today_key}"
            if key not in state:
                is_fresh = True
            state[key] = r["live_speed"]
        if is_fresh:
            fresh.append(r)

    state = {k: v for k, v in state.items() if k == "_last_run" or k.split("|")[-1] >= today_key}
    state["_last_run"] = f"{now:%Y-%m-%d %H:%M}"

    if not fresh:
        log(f"  nothing new to alert ({len(candidates)} windy, all already sent)")
        if not dry:
            save_state(state)
        return

    fresh.sort(key=disp_speed, reverse=True)
    lines = ["🪁 *Wind alert* — 18kn+ (blended HRRR/GFS forecast + live stations):", ""]
    for r in fresh:
        s = r["spot"]
        head = f"• *{s['name']}*"
        if r.get("live_windy"):
            head += f" — 🟢 *BLOWING NOW {r['live_speed']}kn*"
        lines.append(head)
        if r.get("peak"):
            p = r["peak"]
            when = f"{p['dt']:%a %-I%p}".replace("AM", "am").replace("PM", "pm")
            lines.append(f"   forecast peak {r['gust']}kn gusts {when} ({deg_to_compass(p['dir'])})")
        if r.get("live") and not r.get("live_windy"):
            lv = r["live"]
            sp = lv.get("gust") or lv.get("wind")
            if sp is not None:
                lines.append(f"   now {round(sp)}kn {deg_to_compass(lv.get('dir'))} · {lv['source']} {lv['station']}")
        lines.append(f"   _{s['region']}_")
    lines += ["", "First screen, not a launch decision — check the dashboard before you load up."]
    msg = "\n".join(lines)

    if dry:
        log("DRY — would send:")
        print("\n" + msg + "\n")
        return

    tg_ok = send_telegram(msg)
    mac_ok = send_macos_notification(fresh)
    if tg_ok or mac_ok:
        save_state(state)
        log(f"  alerted {len(fresh)} spot(s) (telegram={tg_ok}, macos={mac_ok})")
    else:
        log("  all channels failed — state NOT saved (will retry next run)")


if __name__ == "__main__":
    main()
