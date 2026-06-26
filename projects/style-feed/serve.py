#!/usr/bin/env python3
"""
The Edit — tiny local server so the feed's hearts/x reach disk (and Claude).

Serves the static feed and accepts the browser's swipe state at POST /feedback,
writing it to data/feedback.json. build_feed.py reads that file on rebuild to
bake Annabel's taste into the ranking, and Claude can read it directly. GET
/feedback returns the saved state so a fresh browser re-hydrates her taste.

Run:  python3 serve.py [port]            (opens the browser; default port 8801)
      python3 serve.py 8801 --no-open    (no browser; used by the preview)
Stop: close this window / Ctrl-C.
"""
import http.server, socketserver, json, sys, pathlib, webbrowser, threading, functools
from urllib.parse import urlparse, parse_qs

ROOT = pathlib.Path(__file__).resolve().parent
FEEDBACK = ROOT / "data" / "feedback.json"
PORT = next((int(a) for a in sys.argv[1:] if a.isdigit()), 8801)

# ---- image proxy ------------------------------------------------------------
# Some stores (Aritzia) front their image CDN with Cloudflare bot management, so
# the browser hotlinking the real URL gets a 403. We launder those — and only
# those — through here: serve.py fetches server-side with a real Chrome TLS
# fingerprint (curl_cffi) and streams the bytes back. Nothing is stored on disk;
# a small in-memory cache just avoids re-fetching the same image each rerender.
# build_feed.py rewrites image src to /img?u=<url> for these hosts only.
PROXY_HOSTS = {"assets.aritzia.com"}        # extend as more Cloudflare stores appear
_IMG_CACHE = {}                              # url -> (content_type, bytes)
_IMG_CACHE_MAX = 600
_curl = None
def _curl_get(url):
    global _curl
    if _curl is None:
        from curl_cffi import requests as _r
        _curl = _r
    return _curl.get(url, impersonate="chrome120", timeout=20)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")  # dodge stale-cache trap
        super().end_headers()

    def _json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        route = self.path.split("?")[0]
        if route == "/feedback":
            data = json.loads(FEEDBACK.read_text()) if FEEDBACK.exists() else {"liked": {}, "disliked": {}}
            return self._json(200, data)
        if route == "/img":
            return self._img()
        return super().do_GET()

    def _img(self):
        """Stream a Cloudflare-protected store image (allowlisted hosts only)."""
        u = parse_qs(urlparse(self.path).query).get("u", [""])[0]
        host = urlparse(u).netloc
        if not u or host not in PROXY_HOSTS:                 # SSRF guard
            return self.send_error(400, "host not proxyable")
        hit = _IMG_CACHE.get(u)
        if hit is None:
            try:
                r = _curl_get(u)
                if r.status_code != 200:
                    return self.send_error(502, f"upstream {r.status_code}")
                hit = (r.headers.get("content-type", "image/jpeg"), r.content)
                if len(_IMG_CACHE) >= _IMG_CACHE_MAX:
                    _IMG_CACHE.pop(next(iter(_IMG_CACHE)))    # cheap FIFO evict
                _IMG_CACHE[u] = hit
            except Exception as e:
                return self.send_error(502, str(e))
        ctype, body = hit
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()                                   # adds no-store; server cache covers refetch
        self.wfile.write(body)

    def do_POST(self):
        if self.path.split("?")[0] != "/feedback":
            return self.send_error(404)
        try:
            n = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(n) or b"{}")
            out = {"liked": data.get("liked", {}) or {}, "disliked": data.get("disliked", {}) or {}}
            FEEDBACK.parent.mkdir(parents=True, exist_ok=True)
            tmp = FEEDBACK.with_suffix(".tmp")
            tmp.write_text(json.dumps(out, indent=2))
            tmp.replace(FEEDBACK)  # atomic
            print(f"  saved feedback: {len(out['liked'])} loved, {len(out['disliked'])} passed")
            return self._json(200, {"ok": True, "liked": len(out["liked"]), "disliked": len(out["disliked"])})
        except Exception as e:
            return self.send_error(500, str(e))

    def log_message(self, *a):
        pass


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    url = f"http://localhost:{PORT}/feed.html"
    handler = functools.partial(Handler, directory=str(ROOT))
    try:
        httpd = Server(("", PORT), handler)
    except OSError:
        print(f"The Edit is already running. Opening {url}")
        webbrowser.open(url)
        sys.exit(0)
    print(f"\n  The Edit is live ->  {url}\n  Your hearts/x save to {FEEDBACK}\n  Close this window to stop.\n")
    if "--no-open" not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
