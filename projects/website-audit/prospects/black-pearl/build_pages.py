#!/usr/bin/env python3
"""
Build Black Pearl mockup HTML pages from menu-final.json + verified facts.
Generates: menus.html, menu-*.html (7), about.html, private-events.html, reservations.html
Reuses header/footer from index.html pattern.
"""
import json, os, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MOCKUPS = ROOT / "mockups"

with open(ROOT / "menu-final.json") as f:
    menu = json.load(f)

HEADER_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>

<header class="site-header{hdr_class}" data-nav>
  <div class="container">
    <a href="index.html" class="wordmark">Black Pearl</a>
    <nav class="nav" aria-label="Primary">
      <a href="menus.html" class="nav-link"{nav_menus}>Menus</a>
      <a href="private-events.html" class="nav-link"{nav_greenhouse}>Greenhouse</a>
      <a href="about.html" class="nav-link"{nav_about}>About</a>
      <a href="reservations.html" class="nav-link"{nav_contact}>Contact</a>
    </nav>
    <a href="https://resy.com/cities/ann-arbor-mi/venues/black-pearl-ann-arbor" target="_blank" rel="noopener" class="nav-reserve">Reserve</a>
    <button class="menu-toggle" data-menu-toggle aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<nav class="mobile-menu" data-menu aria-label="Mobile">
  <a href="menus.html">Menus</a>
  <a href="private-events.html">Greenhouse</a>
  <a href="about.html">About</a>
  <a href="reservations.html">Contact</a>
  <a class="btn mobile-reserve" href="https://resy.com/cities/ann-arbor-mi/venues/black-pearl-ann-arbor" target="_blank" rel="noopener">Reserve</a>
</nav>
"""

FOOTER_TPL = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-wordmark">Black Pearl</div>
        <p>302 South Main Street<br>Ann Arbor, MI 48104</p>
        <p><a href="tel:+17342220400">(734) 222-0400</a></p>
        <p><a href="mailto:info@blackpearlannarbor.com">info@blackpearlannarbor.com</a></p>
      </div>
      <div class="footer-col">
        <h4>Hours</h4>
        <p>Mon &ndash; Thu &nbsp; 5 &ndash; 10 PM</p>
        <p>Fri &ndash; Sat &nbsp; 4 &ndash; 11 PM</p>
        <p>Sunday &nbsp; 5 &ndash; 9 PM</p>
        <p style="margin-top:10px;font-style:italic;opacity:0.7;">Bar service ends 1 hour after kitchen close</p>
      </div>
      <div class="footer-col">
        <h4>Visit</h4>
        <a href="https://resy.com/cities/ann-arbor-mi/venues/black-pearl-ann-arbor" target="_blank" rel="noopener">Reservations</a>
        <a href="https://order.toasttab.com/online/black-pearl-ann-arbor-302-south-main-street" target="_blank" rel="noopener">Takeout</a>
        <a href="https://www.doordash.com/business/626310/" target="_blank" rel="noopener">Delivery</a>
        <a href="https://www.toasttab.com/black-pearl-ann-arbor-302-south-main-street/giftcards" target="_blank" rel="noopener">Gift Cards</a>
        <a href="private-events.html">Private Events</a>
      </div>
    </div>
    <div class="footer-copy">&copy; 2026 Black Pearl Ann Arbor · Downtown Ann Arbor since 2008</div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

def header(title, desc, current, dark=False):
    cur = {
        'menus': ' aria-current="page"' if current == 'menus' else '',
        'greenhouse': ' aria-current="page"' if current == 'greenhouse' else '',
        'about': ' aria-current="page"' if current == 'about' else '',
        'contact': ' aria-current="page"' if current == 'contact' else '',
    }
    return HEADER_TPL.format(
        title=html.escape(title),
        desc=html.escape(desc),
        hdr_class=' site-header--dark' if dark else '',
        nav_menus=cur['menus'],
        nav_greenhouse=cur['greenhouse'],
        nav_about=cur['about'],
        nav_contact=cur['contact'],
    )

def hero_short(title, bg_image, eyebrow=None, medium=False):
    size_cls = 'hero hero-medium' if medium else 'hero hero-short'
    eb = f'<div class="hero-eyebrow" data-reveal>{html.escape(eyebrow)}</div>' if eyebrow else ''
    return f"""
<section class="{size_cls}" data-reveal-group>
  <div class="hero-bg" style="background-image:url('assets/img/{bg_image}');"></div>
  <div class="hero-content">
    {eb}
    <h1 class="hero-title" data-reveal>{html.escape(title)}</h1>
  </div>
</section>
"""

def render_price(price):
    if price == "MKT":
        return '<span class="menu-item-price is-mkt">MKT</span>'
    return f'<span class="menu-item-price">{html.escape(price)}</span>'

def _clean_title(raw):
    """Strip trailing 'n/a' / 'N/A' artifacts that leaked in from menu-parse
    of the Spirit Free section. The site should never display these markers."""
    import re as _re
    cleaned = _re.sub(r'\s+n/?a\.?\s*$', '', raw, flags=_re.IGNORECASE).strip()
    return cleaned

def render_menu_item(item):
    title = html.escape(_clean_title(item['title']))
    desc = item.get('description') or ''
    price = item['price']
    if not price:
        raise ValueError(f"Empty price for {item['title']}")
    # Banner row (happy hour header)
    if price == "----------":
        return f"""<li class="menu-item menu-item--banner">
  <div class="menu-item-row">
    <span class="menu-item-title">{title}</span>
    <span class="menu-item-price">&nbsp;</span>
  </div>
  <p class="menu-item-desc">{html.escape(desc)}</p>
</li>"""
    desc_html = f'<p class="menu-item-desc">{html.escape(desc)}</p>' if desc else ''
    return f"""<li class="menu-item" data-reveal>
  <div class="menu-item-row">
    <h3 class="menu-item-title">{title}</h3>
    {render_price(price)}
  </div>
  {desc_html}
</li>"""

def render_menu_sections(items, skip_section_heads=False, tab_name=None):
    """Render menu sections.

    If skip_section_heads, only render item rows (used when a parent head already
    introduces the group).

    If tab_name is provided and a section's name equals the tab name
    (case-insensitive), that section's heading is suppressed — the tab-level
    hero/heading already labels the group, so rendering an identical <h2>
    creates a visible duplicate.
    """
    sections = []
    current = None
    for it in items:
        sec = it.get('section') or 'MENU'
        if current is None or current['name'] != sec:
            current = {'name': sec, 'items': []}
            sections.append(current)
        current['items'].append(it)

    out = []
    for sec in sections:
        rows = "\n".join(render_menu_item(it) for it in sec['items'])
        # Suppress the section head when its name duplicates the tab name
        suppress_head = skip_section_heads or (
            tab_name is not None and sec['name'].strip().upper() == tab_name.strip().upper()
        )
        if suppress_head:
            out.append(f"""<ul class="menu-items" data-reveal-group>
    {rows}
  </ul>""")
        else:
            out.append(f"""<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <h2>{html.escape(sec['name'])}</h2>
  </div>
  <ul class="menu-items">
    {rows}
  </ul>
</div>""")
    return "\n".join(out)

MENU_PAGE_META = {
    "LUNCH": {
        "file": "menu-lunch.html",
        "title": "Lunch Menu — Black Pearl Ann Arbor",
        "desc": "Lunch at Black Pearl, Wednesday through Sunday from 11am to 2:30pm. Sushi, seafood, and chef-driven midday plates in downtown Ann Arbor.",
        "hero_title": "Lunch",
        "hero_eyebrow": "Wed – Sun · 11:00 AM – 2:30 PM",
        "hero_img": "Featuring-the-fries---low-res-1.jpeg",
        "intro": "A refined midday menu featuring sushi, seafood, and chef-driven favorites. Lunch service begins May 6.",
    },
    "DINNER": {
        "file": "menu-dinner.html",
        "title": "Dinner Menu — Black Pearl Ann Arbor",
        "desc": "Seasonal dinner menu at Black Pearl — contemporary American plates, scallops, short rib, and chef's weekly cuts.",
        "hero_title": "Dinner",
        "hero_eyebrow": "Seasonal Selections",
        "hero_img": "_MG_7056.jpg",
        "intro": "Contemporary American plates built around seafood, sushi, and the week's best ingredients. Served nightly.",
    },
    "SUSHI": {
        "file": "menu-sushi.html",
        "title": "Sushi Menu — Black Pearl Ann Arbor",
        "desc": "Sushi menu at Black Pearl — rolls and temaki prepared by Chef Jae Myoung.",
        "hero_title": "Sushi",
        "hero_eyebrow": "From Chef Jae Myoung",
        "hero_img": "Sushi-8.jpg",
        "intro": "Classic rolls and house creations from our sushi bar. Fish is hand-selected daily.",
    },
    "HAPPY HOUR": {
        "file": "menu-happy-hour.html",
        "title": "Happy Hour — Black Pearl Ann Arbor",
        "desc": "Happy hour at the Black Pearl bar: Monday through Thursday 5–6 PM and Friday–Saturday 4–5 PM.",
        "hero_title": "Happy Hour",
        "hero_eyebrow": "At the Bar",
        "hero_img": "cocktails-low-res-1.jpg",
        "intro": "Weekday winds-down at the bar. Small plates, sushi, and a short list of cocktails, wine, and beer.",
    },
    "SIGNATURE COCKTAILS": {
        "file": "menu-cocktails.html",
        "title": "Cocktails — Black Pearl Ann Arbor",
        "desc": "Signature cocktails, spirit-free drinks, and a full bar at Black Pearl Ann Arbor.",
        "hero_title": "Cocktails",
        "hero_eyebrow": "Signature & Spirit-Free",
        "hero_img": "cocktails-low-res-1.jpg",
        "intro": "Signature martinis and cocktails, spirit-free options, and a full bar of vodka, gin, rum, tequila, mezcal, whiskey, scotch, brandy, cognac, and liqueurs.",
    },
    "WINE BY THE GLASS": {
        "file": "menu-wine.html",
        "title": "Wine Menu — Black Pearl Ann Arbor",
        "desc": "Wine by the glass and bottled wine selections at Black Pearl Ann Arbor.",
        "hero_title": "Wine",
        "hero_eyebrow": "By the Glass & Bottle",
        "hero_img": "Hamachi-Crudo-4.jpg",
        "intro": "A hand-picked list of old-world and new-world producers, balanced across bubbles, whites, and reds.",
    },
    "BEER": {
        "file": "menu-beer.html",
        "title": "Beer Menu — Black Pearl Ann Arbor",
        "desc": "Bottled beer menu at Black Pearl Ann Arbor — local, domestic, and non-alcoholic selections.",
        "hero_title": "Beer",
        "hero_eyebrow": "Bottled Selections",
        "hero_img": "_MG_7056.jpg",
        "intro": "Michigan favorites alongside a rotating list of stouts, IPAs, lagers, and non-alcoholic pours.",
    },
}

# Explore links shared across all menu pages
MENU_EXPLORE_LINKS = [
    ("menu-dinner.html", "Dinner"),
    ("menu-lunch.html", "Lunch"),
    ("menu-sushi.html", "Sushi"),
    ("menu-happy-hour.html", "Happy Hour"),
    ("menu-cocktails.html", "Cocktails"),
    ("menu-wine.html", "Wine"),
    ("menu-beer.html", "Beer"),
]

def explore_links(current_file):
    items = "\n".join(
        f'    <a href="{href}">{html.escape(label)}</a>'
        for href, label in MENU_EXPLORE_LINKS
        if href != current_file
    )
    return f"""
<section class="menu-explore" data-reveal-group>
  <div class="container">
    <div class="section-label" data-reveal style="justify-content:center;">Explore</div>
    <h2 class="section-title" data-reveal style="font-size:clamp(28px,3.2vw,36px);">Other Menus</h2>
    <div class="menu-explore-links" data-reveal>
{items}
    </div>
  </div>
</section>
"""

def build_menu_page(tab_key):
    meta = MENU_PAGE_META[tab_key]
    page_title = meta['title']
    hero = hero_short(meta['hero_title'], meta['hero_img'], eyebrow=meta['hero_eyebrow'])

    if tab_key == "SIGNATURE COCKTAILS":
        # Combine Signature + Spirit Free + Full Bar paragraph
        body_parts = []
        body_parts.append(render_menu_sections(menu['by_tab']['SIGNATURE COCKTAILS'], tab_name='SIGNATURE COCKTAILS'))
        body_parts.append(render_menu_sections(menu['by_tab']['SPIRIT FREE'], tab_name='SPIRIT FREE'))
        # Full bar callout
        spirits_text = menu['notes']['spirits_replacement_text']
        body_parts.append(f"""
<div class="full-bar" data-reveal>
  <h2>Full Bar</h2>
  <p>{html.escape(spirits_text)}</p>
</div>""")
        body = "\n".join(body_parts)
    elif tab_key == "WINE BY THE GLASS":
        # Combine Glass + Bottled
        body_parts = []
        # Glass
        body_parts.append(f"""<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Wine by the Glass &amp; Bottle</span>
    <h2>By the Glass</h2>
  </div>
</div>""")
        body_parts.append(render_menu_sections(menu['by_tab']['WINE BY THE GLASS'], tab_name='WINE BY THE GLASS'))
        # Bottled
        body_parts.append(f"""<div class="menu-section" data-reveal-group>
  <div class="menu-section-head" data-reveal>
    <span class="label">Cellar</span>
    <h2>Bottled Wine</h2>
  </div>
</div>""")
        # tab_name='BOTTLED WINE' suppresses the duplicate auto-heading since
        # every item in this tab has section='BOTTLED WINE' (same as tab)
        body_parts.append(render_menu_sections(menu['by_tab']['BOTTLED WINE'], tab_name='BOTTLED WINE'))
        body = "\n".join(body_parts)
    else:
        body = render_menu_sections(menu['by_tab'][tab_key], tab_name=tab_key)

    html_out = (
        header(page_title, meta['desc'], current='menus')
        + hero
        + f"""
<section class="menu-intro" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <p class="prose" data-reveal>{meta['intro']}</p>
  </div>
</section>
<section class="menu-body" data-reveal-group>
  <div class="container">
    {body}
  </div>
</section>
"""
        + explore_links(meta['file'])
        + FOOTER_TPL
    )
    (MOCKUPS / meta['file']).write_text(html_out)
    return meta['file']


def build_menus_index():
    cards = []
    for href, label in MENU_EXPLORE_LINKS:
        # pick a representative image
        img_map = {
            "menu-dinner.html": ("_MG_7056.jpg", "Seasonal mains, sushi, and chef-driven plates."),
            "menu-lunch.html": ("Featuring-the-fries---low-res-1.jpeg", "Refined midday, Wed–Sun. Begins May 6."),
            "menu-sushi.html": ("Sushi-8.jpg", "Rolls and temaki from Chef Jae."),
            "menu-happy-hour.html": ("cocktails-low-res-1.jpg", "Mon–Thu 5–6 PM · Fri–Sat 4–5 PM at the bar."),
            "menu-cocktails.html": ("cocktails-low-res-1.jpg", "Signature, spirit-free, and a full bar."),
            "menu-wine.html": ("Hamachi-Crudo-4.jpg", "By the glass and bottled selections."),
            "menu-beer.html": ("_MG_7056.jpg", "Michigan bottles and rotating guests."),
        }
        img, desc = img_map[href]
        cards.append(f"""<a href="{href}" class="menu-card" data-reveal>
  <div class="menu-card-img" style="background-image:url('assets/img/{img}');"></div>
  <div class="menu-card-body">
    <h3 class="menu-card-title">{html.escape(label)}</h3>
    <p class="menu-card-desc">{html.escape(desc)}</p>
    <span class="menu-card-cta">View Menu →</span>
  </div>
</a>""")

    body = (
        header("Menus — Black Pearl Ann Arbor", "All Black Pearl menus: dinner, lunch, sushi, happy hour, cocktails, wine, beer.", current='menus')
        + hero_short("Menus", "Hamachi-Crudo-4.jpg", eyebrow="A Table for Every Evening")
        + f"""
<section class="section" data-reveal-group>
  <div class="container">
    <div class="container narrow" style="text-align:center;">
      <p class="prose" data-reveal>Every table at Black Pearl begins with the same ingredients list &mdash; the produce market, the day's catch, the bar. Where the evening goes is up to you.</p>
    </div>
    <div class="menu-cards">
      {''.join(cards)}
    </div>
  </div>
</section>
"""
        + FOOTER_TPL
    )
    (MOCKUPS / "menus.html").write_text(body)


def build_about():
    team = [
        {
            "name": "Harry Cohen",
            "role": "Owner",
            "portrait": "Harry-Headshot.jpg",
            "bio": "Harry Cohen is a psychologist, author, and co owner of The Black Pearl since 2008. Leveraging his experience coaching executives on leadership, customer service, and personal development, he created the Black Pearl to practice the principles he espouses. He is committed to cultivating an atmosphere where staff and guests feel warmly welcomed and served. His vision was to create a unique and accessible gathering place where friends, family, and strangers can come together to be uplifted by delicious food, exceptional service, and a beautiful ambiance.",
            "links": [
                ("https://bethesunnotthesalt.com/", "bethesunnotthesalt.com"),
                ("https://www.amazon.com/Secrets-Obvious-Guide-Balanced-Living/dp/0741413698", "Secrets of the Obvious: A Guide for Balanced Living"),
                ("https://www.amazon.com/Sun-Not-Salt-Harry-Cohen/dp/0578412225", "Be the Sun, Not the Salt"),
            ],
        },
        {
            "name": "Jan Z. Cohen",
            "role": "Owner",
            "portrait": "Jan-Headshot.jpg",
            "bio": "Jan uses her artistic sensibilities to make the overall vibe of Black Pearl a beautiful, warm, inviting, and uplifting place for customers and staff alike. The unique ambience of Black Pearl is one of the reasons people love to hang out there and Jan is forever looking for ways to enhance that experience for everyone.",
            "links": [],
        },
        {
            "name": "Jake Doyal",
            "role": "Owner / Operator",
            "portrait": "Jake-headshot-2024-2.jpg",
            "bio": "He exemplifies what amazing hospitality looks like. There is no job too large or small for Jake to take on. When the pandemic closed his former restaurant on Main Street, he joined the team at the Pearl and became a partner and GM in 2021. His regular customers followed him to his new home for a reason. He truly cares. Under his leadership, the Black Pearl continues to stretch the boundaries of operational excellence and unreasonable hospitality.",
            "links": [],
        },
        {
            "name": "Anthony DeChavez",
            "role": "Executive Chef",
            "portrait": "tony-headshot-website.jpg",
            "bio": "Tony has over 10 years of experience in the restaurant industry. He graduated from Schoolcraft in 2014 and has traveled and cooked in France, Chicago, and worked with several renowned chefs including Stephanie Izard and Jimmy Bannos Jr. Tony is excited to offer the city of Ann Arbor contemporary interpretations of classic seafood — uniting time tested plates that have brought smiles to our customers with new blends of flavors and techniques that are waiting to be explored.",
            "links": [],
        },
        {
            "name": "Jae Myoung",
            "role": "Sushi Chef",
            "portrait": "_MG_0646.JPEG",
            "bio": "Jae is a dedicated sushi chef with over six years of experience in crafting authentic and innovative Japanese cuisine. A graduate of the Culinary Arts program at Schoolcraft College, Jae blends professional expertise and a passion for creative sushi which he inherited from his father, also a sushi chef. Passionate about quality and detail, he is committed to delivering exceptional sushi experiences that leave a lasting impression.",
            "links": [],
        },
    ]

    cards = []
    for m in team:
        links_html = ""
        if m['links']:
            link_items = "\n      ".join(
                f'<a class="inline-link" href="{href}" target="_blank" rel="noopener">{html.escape(label)}</a>'
                for href, label in m['links']
            )
            links_html = f'<div class="team-links">\n      {link_items}\n    </div>'
        cards.append(f"""<div class="team-member" data-reveal>
  <div class="team-portrait" style="background-image:url('assets/img/{m['portrait']}');"></div>
  <h3 class="team-name">{html.escape(m['name'])}</h3>
  <p class="team-role">{html.escape(m['role'])}</p>
  <p class="team-bio">{html.escape(m['bio'])}</p>
  {links_html}
</div>""")

    body = (
        header("About — Black Pearl Ann Arbor", "Meet the team behind Black Pearl Ann Arbor — Harry and Jan Cohen, Jake Doyal, Chef Tony DeChavez, and Sushi Chef Jae Myoung.", current='about')
        + hero_short("About", "Sushi-8.jpg", eyebrow="Our People")
        + f"""
<section class="section" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <div class="section-label" data-reveal style="justify-content:center;">The Team</div>
    <h2 class="section-title" data-reveal>The people behind the Pearl</h2>
    <p class="prose" data-reveal style="margin-top:28px;">We opened the doors in 2008 with a simple goal: create a place where friends, family, and strangers gather over good food and honest hospitality. Every member of this team is part of keeping that true.</p>
  </div>
  <div class="container">
    <div class="team-grid">
      {''.join(cards)}
    </div>
  </div>
</section>
"""
        + FOOTER_TPL
    )
    (MOCKUPS / "about.html").write_text(body)


def build_private_events():
    body = (
        header("Private Events — Black Pearl Ann Arbor", "Host your next private event in Black Pearl's soundproof 44-seat dining room — business meetings, rehearsal dinners, showers, and full-restaurant buyouts in downtown Ann Arbor.", current='greenhouse')
        + hero_short("Private Events", "LONG-ROAD-8710_1_1-min.jpg", eyebrow="The Greenhouse", medium=True)
        + """
<section class="section" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <div class="section-label" data-reveal style="justify-content:center;">A Room of Your Own</div>
    <h2 class="section-title" data-reveal>Host at Black Pearl</h2>
    <p class="prose" data-reveal style="margin-top:28px;">
      Our private, soundproof dining room is built to host everything from a quiet board dinner to a full-restaurant wedding buyout. Gourmet seafood and steaks, a private bar, and a menu tailored to your guests.
    </p>
  </div>
  <div class="container">
    <div class="facts-panel">
      <div data-reveal>
        <h3>The Space</h3>
        <ul>
          <li>Private, soundproof dining room</li>
          <li>600 sq ft customizable floor plan</li>
          <li>Seating for up to 44 guests</li>
          <li>80" flat screen television with surround sound</li>
          <li>Private bar</li>
          <li>Videoconferencing</li>
          <li>Direct HDMI, Chromecast, and Apple AirPlay</li>
          <li>Vegetarian, vegan, and allergen-free options</li>
        </ul>
      </div>
      <div data-reveal>
        <h3>Ideal For</h3>
        <ul>
          <li>Business meetings</li>
          <li>Board dinners and luncheons</li>
          <li>Anniversaries</li>
          <li>Birthday parties</li>
          <li>Rehearsal dinners</li>
          <li>Baby and wedding showers</li>
          <li>Networking events</li>
          <li>Wine tastings</li>
          <li>Social gatherings</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="dark-strip" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <div class="section-label" data-reveal style="justify-content:center;">Full Buyout</div>
    <h2 class="section-title" data-reveal style="color:#F5EEE0;">The Restaurant, The Room, The Patio</h2>
    <p class="prose" data-reveal style="color:rgba(245,238,224,0.88); margin-top:28px;">
      For a larger reception, social, or corporate event, we offer an exclusive buyout of the restaurant, private dining room, and patio. Available seven days a week and bookable up to one year in advance.
    </p>
  </div>
</section>

<section class="section" data-reveal-group>
  <div class="container">
    <p class="compliance" data-reveal>
      Using a U of M P-card, or need an AdvaMed or PharMa-compliant menu? We know the guidelines and will build something to your budget.
    </p>
    <div class="inquire-block" data-reveal>
      <div class="section-label" style="justify-content:center;margin-bottom:14px;">Inquire</div>
      <h3>Sydney McGee</h3>
      <p>Private Event Coordinator · <a class="inline-link" href="tel:+17343532991">(734) 353-2991</a> · <a class="inline-link" href="mailto:sydney@blackpearlannarbor.com">sydney@blackpearlannarbor.com</a></p>
      <a href="https://theblackpearl.tripleseat.com/party_request/24138" target="_blank" rel="noopener" class="btn">Inquire About Your Event</a>
    </div>
  </div>
</section>
"""
        + FOOTER_TPL
    )
    (MOCKUPS / "private-events.html").write_text(body)


def build_reservations():
    body = (
        header("Reservations & Contact — Black Pearl Ann Arbor", "Make a reservation, order takeout or delivery, and find hours for Black Pearl Ann Arbor. 302 South Main Street · (734) 222-0400.", current='contact')
        + hero_short("Visit", "20190424-545A5312.jpg", eyebrow="302 South Main Street, Ann Arbor")
        + """
<section class="section" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <div class="section-label" data-reveal style="justify-content:center;">How to Join Us</div>
    <h2 class="section-title" data-reveal>Reserve, order, or call</h2>
    <p class="prose" data-reveal style="margin-top:24px; font-size:clamp(18px,1.4vw,22px);">The simplest way to hold a table is Resy. The kitchen is reachable by phone during service for curbside and carryout.</p>
  </div>
  <div class="container">
    <div class="reserve-grid">
      <a href="https://resy.com/cities/ann-arbor-mi/venues/black-pearl-ann-arbor" target="_blank" rel="noopener" class="reserve-card" data-reveal>
        <span class="label">Resy</span>
        <h3>Reserve</h3>
        <p>Hold a table online through our Resy page.</p>
        <span class="btn btn-brass">Make a Reservation</span>
      </a>
      <a href="https://order.toasttab.com/online/black-pearl-ann-arbor-302-south-main-street" target="_blank" rel="noopener" class="reserve-card" data-reveal>
        <span class="label">Toast</span>
        <h3>Pickup</h3>
        <p>Curbside and in-store pickup during hours of service.</p>
        <span class="btn btn-brass">Order for Pickup</span>
      </a>
      <a href="https://www.doordash.com/business/626310/" target="_blank" rel="noopener" class="reserve-card" data-reveal>
        <span class="label">DoorDash</span>
        <h3>Delivery</h3>
        <p>Door-to-door delivery through DoorDash.</p>
        <span class="btn btn-brass">Order Delivery</span>
      </a>
      <a href="https://www.toasttab.com/black-pearl-ann-arbor-302-south-main-street/giftcards" target="_blank" rel="noopener" class="reserve-card" data-reveal>
        <span class="label">Toast</span>
        <h3>Gift Cards</h3>
        <p>Digital gift cards redeemable in-restaurant.</p>
        <span class="btn btn-brass">Send a Gift Card</span>
      </a>
    </div>
    <div class="phone-large" data-reveal-group>
      <span class="label" data-reveal>Or call us</span>
      <a href="tel:+17342220400" data-reveal>(734) 222-0400</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;" data-reveal-group>
  <div class="container narrow" style="text-align:center;">
    <div class="section-label" data-reveal style="justify-content:center;">Hours</div>
    <h2 class="section-title" data-reveal>Seasonal Kitchen Hours</h2>
    <ul class="hours-list" data-reveal>
      <li><span>Monday &ndash; Thursday</span><span>5 – 10 PM</span></li>
      <li><span>Friday &ndash; Saturday</span><span>4 – 11 PM</span></li>
      <li><span>Sunday</span><span>5 – 9 PM</span></li>
    </ul>
    <p class="hours-note" data-reveal>Bar service ends one hour after the kitchen closes. Seasonal hours &mdash; confirm by phone.</p>
    <p class="hours-note" data-reveal style="margin-top:8px;">Happy Hour: Mon &ndash; Thu 5 &ndash; 6 PM · Fri &ndash; Sat 4 &ndash; 5 PM (bar only)</p>
    <p class="hours-note" data-reveal style="margin-top:28px;">Lunch service begins May 6 · Wed &ndash; Sun 11 AM &ndash; 2:30 PM</p>
  </div>
</section>
"""
        + FOOTER_TPL
    )
    (MOCKUPS / "reservations.html").write_text(body)


def main():
    # Build all menu pages
    for tab in ["LUNCH", "DINNER", "SUSHI", "HAPPY HOUR", "SIGNATURE COCKTAILS", "WINE BY THE GLASS", "BEER"]:
        out = build_menu_page(tab)
        print(f"  wrote {out}")

    build_menus_index()
    print("  wrote menus.html")
    build_about()
    print("  wrote about.html")
    build_private_events()
    print("  wrote private-events.html")
    build_reservations()
    print("  wrote reservations.html")

    # quick sanity — count items
    total = sum(len(v) for v in menu['by_tab'].values())
    print(f"\nTotal menu items in JSON: {total}")

if __name__ == "__main__":
    main()
