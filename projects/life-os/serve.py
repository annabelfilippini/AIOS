#!/usr/bin/env python3
"""
Life OS — one app, one server. Composes The Day (day-planner/planner.html) and
The Edit (style-feed/feed.html) into a single SPA with a top tab bar, at serve
time, so both modules stay canonical (The Day hand-authored, The Edit generated
by build_feed.py). No iframes: one document, shared in-page state.

How it works:
  - Both modules already share the same design tokens and have ZERO id overlap,
    so document.getElementById just works across the merged page.
  - The Edit's JS is IIFE-wrapped (no global leak); The Day is embed-aware via
    APPROOT (= #view-day when present), so its icon innerHTML reset and data-mtab
    only touch its own view.
  - The only collisions are CSS class names, fixed by scoping each module's CSS
    under its #view-* section (scope_css below).

Backends are reused wholesale from each project's own serve.py (calendar/email
for The Day; /feedback + /img proxy for The Edit), so this file adds no business
logic — just the shell + routing.

Run:  python3 serve.py [port]      (default 8800; opens the browser)
      python3 serve.py 8800 --no-open
      python3 serve.py --selfcheck (CSS scoper unit check, no server)
"""
import sys, pathlib, functools, threading, webbrowser, re, importlib.util

HERE = pathlib.Path(__file__).resolve().parent
PROJECTS = HERE.parent
DAY_HTML = PROJECTS / "day-planner" / "planner.html"
EDIT_HTML = PROJECTS / "style-feed" / "the-edit.html"


def _load(name, path):
    """Import a module from a path under a unique name (both projects ship a
    file literally named serve.py, so a plain `import serve` would alias them)."""
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


theday = _load("theday_serve", PROJECTS / "day-planner" / "serve.py")
theedit = _load("theedit_serve", PROJECTS / "style-feed" / "serve.py")


# ---- CSS scoping ------------------------------------------------------------
def _scope_one(s, sel):
    """Prefix a single selector so it only matches inside `sel`.
    body/html/:root (the standalone page root) become `sel` itself."""
    s = s.strip()
    if not s:
        return s
    if s in ("body", "html", ":root"):
        return sel
    for tag in ("body", "html"):
        # `body[...]`, `body .x`, `body>x` -> `#view .x`; but not `body2`/`bodyfoo`
        if s.startswith(tag) and (len(s) == len(tag) or not (s[len(tag)].isalnum() or s[len(tag)] in "-_")):
            return sel + s[len(tag):]
    return sel + " " + s


def scope_css(css, sel):
    """Scope a stylesheet under `sel`. Recurses into @media/@supports/@container;
    leaves @keyframes/@font-face/@page bodies untouched. Selector lists are split
    on commas (no commas inside [] or () in these files — ponytail: holds here)."""
    out = []
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            out.append(css[i:])
            break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        inner = css[j + 1:k - 1]
        if prelude.startswith("@"):
            name = prelude.split()[0].lower() if prelude.split() else ""
            if name in ("@media", "@supports", "@container"):
                out.append(prelude + "{" + scope_css(inner, sel) + "}")
            else:  # @keyframes/@font-face/@page: don't touch the inner rules
                out.append(prelude + "{" + inner + "}")
        else:
            sels = ",".join(_scope_one(s, sel) for s in prelude.split(","))
            out.append(sels + "{" + inner + "}")
        i = k
    return "".join(out)


# ---- SPA compose ------------------------------------------------------------
def _extract(html):
    style = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.S).group(1)
    return style, body


# All The Day's tokens (superset of The Edit's), hoisted so the shell chrome and
# both views inherit them. Kept verbatim from planner.html :root.
_TOKENS = (
    "--bg:#f3efe9;--card:#faf8f4;--ink:#1b1916;--accent:#3a352d;--muted:#7c756a;--line:#e0d9cd;--love:#b54b5a;"
    "--fn-focus:#3a352d;--fn-move:#7e8a6b;--fn-water:#7e95a3;--fn-social:#b54b5a;--fn-home:#7c756a;--fn-none:#a99f8f;"
    "--serif:'Cormorant Garamond',Georgia,serif;--sans:'Jost',system-ui,sans-serif;--r:6px;--topbar:46px"
)

_SHELL_CSS = """
html,body{margin:0;padding:0}
body{background:var(--bg);font-family:var(--sans);color:var(--ink);-webkit-font-smoothing:antialiased}
.los-top{position:sticky;top:0;z-index:200;height:var(--topbar);display:flex;align-items:center;gap:18px;padding:0 20px;background:var(--card);border-bottom:1px solid var(--line)}
.los-brand{font-family:var(--serif);font-weight:600;font-size:18px;letter-spacing:.16em;text-transform:uppercase}
.los-nav{display:flex;gap:4px}
.los-tab{border:0;background:transparent;font-family:var(--sans);font-weight:400;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);padding:8px 14px;border-radius:var(--r);cursor:pointer}
.los-tab:hover:not(:disabled){color:var(--ink)}
.los-tab.on{background:var(--accent);color:#fff}
.los-tab:disabled{opacity:.4;cursor:default}
.view[hidden]{display:none}
#view-day .app{height:calc(100vh - var(--topbar))}
/* The Edit is a centered scrolling column; offset its looks from the sticky topbar */
#view-edit .card{scroll-margin-top:calc(var(--topbar) + 10px)}
#view-edit .card.los-flash{animation:losflash 1.6s ease}
@keyframes losflash{0%{box-shadow:0 0 0 0 rgba(107,99,83,0)}18%{box-shadow:0 0 0 3px rgba(107,99,83,.5)}100%{box-shadow:0 0 0 0 rgba(107,99,83,0)}}
/* cross-module context banner: The Day -> "dressing for this event" -> The Edit */
#los-edit-banner{display:flex;align-items:center;gap:14px;margin:8px 0 0;padding:13px 18px;background:var(--accent);color:#faf8f4;border-radius:var(--r)}
#los-edit-banner .lb-txt{flex:1;font-family:var(--serif);font-size:18px;line-height:1.2}
#los-edit-banner .lb-txt b{font-weight:600}
#los-edit-banner .lb-kick{display:block;font-family:var(--sans);font-size:9px;font-weight:400;letter-spacing:.24em;text-transform:uppercase;opacity:.65;margin-bottom:3px}
#los-edit-banner .lb-x{flex:none;border:0;background:rgba(255,255,255,.16);color:#faf8f4;width:28px;height:28px;border-radius:50%;cursor:pointer;font-size:14px;line-height:1;display:grid;place-items:center}
#los-edit-banner .lb-x:hover{background:rgba(255,255,255,.3)}
@media(max-width:820px){#los-edit-banner .lb-txt{font-size:16px}}
"""

_ROUTER_JS = """
(function(){
  var tabs=[].slice.call(document.querySelectorAll('.los-tab'));
  var views={day:document.getElementById('view-day'),edit:document.getElementById('view-edit')};
  function show(v){
    if(!views[v])return;
    for(var k in views){views[k].hidden=(k!==v);}
    tabs.forEach(function(t){t.classList.toggle('on',t.dataset.view===v);});
    try{localStorage.setItem('los.view',v);}catch(e){}
    if(location.hash.slice(1)!==v){location.hash=v;}
  }
  tabs.forEach(function(t){if(!t.disabled)t.addEventListener('click',function(){show(t.dataset.view);});});
  var saved=null;try{saved=localStorage.getItem('los.view');}catch(e){}
  show(location.hash.slice(1)||saved||'day');
  window.addEventListener('hashchange',function(){var v=location.hash.slice(1);if(views[v])show(v);});

  /* ---- cross-module bus ---- The Day hands an event's occasion + context to
     The Edit, which scrolls to the matching look card and outlines it. The looks
     are tagged data-occ in the-edit.html; no other edits to that file. */
  function removeBanner(){var e=document.getElementById('los-edit-banner');if(e)e.remove();}
  function lookFor(occ){return document.querySelector('#view-edit .card[data-occ~=\\"'+occ+'\\"]');}
  function showBanner(ctx,anchor){
    removeBanner();
    var b=document.createElement('div');b.id='los-edit-banner';
    var title=(ctx&&ctx.title)?ctx.title:'your event';
    var time=(ctx&&ctx.time)?' · '+ctx.time:'';
    b.innerHTML='<div class="lb-txt"><span class="lb-kick">From The Day · dressing for</span><b>'+title+'</b>'+time+'</div><button class="lb-x" title="Clear">\\u2715</button>';
    anchor.parentNode.insertBefore(b,anchor);
    b.querySelector('.lb-x').onclick=removeBanner;
  }
  window.LifeOS={
    show:show,
    goToEdit:function(occ,ctx){
      show('edit');
      var card=lookFor(occ);
      var firstCard=document.querySelector('#view-edit .card');
      showBanner(ctx,card||firstCard);
      var target=card||document.querySelector('#view-edit header')||firstCard;
      try{
        if(card){card.classList.remove('los-flash');void card.offsetWidth;card.classList.add('los-flash');}
        if(target)target.scrollIntoView({behavior:'smooth',block:'start'});
        else window.scrollTo(0,0);
      }catch(e){}
    }
  };
})();
"""


def build_spa():
    day_style, day_body = _extract(DAY_HTML.read_text())
    edit_style, edit_body = _extract(EDIT_HTML.read_text())
    css = (":root{" + _TOKENS + "}" + _SHELL_CSS
           + scope_css(day_style, "#view-day")
           + scope_css(edit_style, "#view-edit"))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>Life OS</title>
<meta name="theme-color" content="#f3efe9" />
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header class="los-top">
  <span class="los-brand">Life OS</span>
  <nav class="los-nav">
    <button class="los-tab on" data-view="day" type="button">The Day</button>
    <button class="los-tab" data-view="edit" type="button">The Edit</button>
    <button class="los-tab" data-view="money" type="button" disabled title="Coming soon">Money</button>
  </nav>
</header>
<section id="view-day" class="view" data-mtab="day">{day_body}</section>
<section id="view-edit" class="view" hidden>{edit_body}</section>
<script>{_ROUTER_JS}</script>
</body>
</html>"""


# ---- server -----------------------------------------------------------------
class Handler(theday.Handler):  # inherits gate, /api/*, end_headers cookie, do_POST
    def _spa(self):
        html = build_spa().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def do_GET(self):
        if not self._gate():
            return
        route = self.path.split("?")[0]
        if route in ("/", "/index.html"):
            return self._spa()
        if route == "/feedback":
            data = (theedit.json.loads(theedit.FEEDBACK.read_text())
                    if theedit.FEEDBACK.exists() else {"liked": {}, "disliked": {}})
            return self._json(200, data)
        if route == "/img":
            return theedit.Handler._img(self)  # reuses The Edit's proxy + cache
        return super().do_GET()  # /api/calendar|emails|inbox + static (day-planner dir)

    def do_POST(self):
        if self.path.split("?")[0] == "/feedback":
            return theedit.Handler.do_POST(self)  # writes style-feed/data/feedback.json
        return super().do_POST()  # /api/inbox|event|draft|send


def _selfcheck():
    css = "body{margin:0} :root{--x:1} .row,.card{color:red} @media (max-width:9px){.row{color:blue} body{x:1}} @keyframes k{0%{x:1}100%{x:2}}"
    out = scope_css(css, "#v")
    assert "#v{margin:0}" in out, out
    assert "#v{--x:1}" in out, out
    assert "#v .row,#v .card{color:red}" in out, out
    assert "@media (max-width:9px){#v .row{color:blue}#v{x:1}}" in out, out
    assert "@keyframes k{0%{x:1}100%{x:2}}" in out, out  # untouched
    # real files compose without error
    html = build_spa()
    assert 'id="view-day"' in html and 'id="view-edit"' in html
    assert 'data-occ="vacation"' in html, "stylist Edit looks must be tagged for goToEdit"
    assert "@keyframes losflash" in html
    print("selfcheck OK")


if __name__ == "__main__":
    if "--selfcheck" in sys.argv:
        _selfcheck(); sys.exit(0)
    port = next((int(a) for a in sys.argv[1:] if a.isdigit()), 8800)
    url = f"http://localhost:{port}/"
    handler = functools.partial(Handler, directory=str(theday.ROOT))  # static from day-planner
    try:
        httpd = theday.Server(("127.0.0.1", port), handler)  # localhost only
    except OSError:
        print(f"Life OS already running. Opening {url}")
        webbrowser.open(url); sys.exit(0)
    print(f"\n  Life OS is live ->  {url}\n  The Day + The Edit, one app. Close this window to stop.\n")
    if "--no-open" not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
