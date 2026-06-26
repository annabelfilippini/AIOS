#!/usr/bin/env python3
"""Per-event taste engine for The Edit.

Given a calendar event title + Annabel's closet, produce a styled look from
what she owns, ranked by her real taste. Works for ANY event, not just the
hand-pinned four. The formulas below are her hand-given taste from
taste-feedback.md; the closet is data/closet.json.

Pure / no deps. Run `python3 style_engine.py` for the self-check.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLOSET_PATH = ROOT / "data" / "closet.json"

# Colors she loves (taste-feedback.md) → rank up; hates → exclude outright.
LOVED_TONES = {"black", "blue", "navy", "brown", "grey", "gray", "ecru", "cream",
               "white", "satin", "birch"}
BANNED_TONES = {"red", "burgundy", "maroon"}
BANNED_TEXT = re.compile(
    r"cardigan|burgundy|maroon|\bred\b|capri|cropped legging|neon|bright pink|rainbow",
    re.I)


def occasion_of(title):
    """Map an event title to an occasion lane, or None if it doesn't drive an
    outfit (a finance reminder, a bill, an admin task). None events get no card."""
    t = (title or "").lower()
    if re.search(r"dinner|drinks|date night|\bdate\b|party|wedding|cocktail|\bbar\b|"
                 r"birthday|\bbday\b|night out|formal|reservation|gala|concert", t):
        return "going-out"
    if re.search(r"flight|airport|\btrip\b|vacation|hotel|resort|travel|packing|"
                 r"getaway|vail|\bski\b", t):
        return "vacation"
    if re.search(r"gym|strength|lift|barre|pilates|yoga|\brun\b|bike|cycle|swim|"
                 r"workout|hike|tennis|core|spin|legs|glutes|upper body|stretch", t):
        return "active"
    if re.search(r"work|meeting|call with|client|interview|presentation|zoom|"
                 r"webflow|office|deadline|sync|1:1|class", t):
        return "work"
    if re.search(r"coffee|lunch|brunch|errand|grocery|grocer|shopping|market|"
                 r"museum|gallery|walk|family|picture|photo|park|friend|hang|"
                 r"breakfast|appointment|haircut|nails|drop off|pick up", t):
        return "casual"
    return None  # money due, bills, admin → no outfit


# Per-occasion formulas (her words, taste-feedback.md). Each slot names the
# closet slot to fill, tones to prefer, and the fallback label + brand to show
# when nothing she owns matches (a "My guess" piece driven by the style rule).
FORMULAS = {
    "going-out": {
        "title": "Quiet going-out",
        "note": "Sleek and a little satin, not sparkly. Black or ivory top, "
                "relaxed dark trouser, gold jewelry.",
        "elevate": "Your Wilfred Martini satin halter with the black trousers "
                   "is the sleeker all-black version.",
        "slots": [
            {"slot": "top", "prefer": ["black", "satin", "white"],
             "fallback": ("White lace or black satin top", "The Edit")},
            {"slot": "bottom", "prefer": ["black"],
             "fallback": ("Loose black trousers", "My guess")},
            {"slot": "shoe", "prefer": ["black", "birch", "grey"],
             "fallback": ("Pointed flat or low heel", "Style rule")},
        ],
    },
    "work": {
        "title": "Polished but not stiff",
        "note": "Ivory clean-neckline top, loose black or navy trousers, "
                "pointed flat. European minimal: Toteme / The Row / Frankie Shop.",
        "elevate": "Brown suede bag and belt, delicate gold jewelry, short grey "
                   "wool jacket over the shoulder.",
        "slots": [
            {"slot": "top", "prefer": ["white", "cream", "ecru"],
             "fallback": ("Ivory clean-neckline top", "Style rule")},
            {"slot": "bottom", "prefer": ["black", "navy"],
             "fallback": ("Loose black or navy trousers", "Style rule")},
            {"slot": "shoe", "prefer": ["black", "brown", "birch"],
             "fallback": ("Pointed flat or loafer", "Style rule")},
            {"slot": "layer", "prefer": ["grey", "navy"],
             "fallback": ("Short grey wool jacket or blazer", "Style rule")},
        ],
    },
    "active": {
        "title": "Pilates-to-coffee neutral set",
        "note": "Neutral or all-black set, full-length only. Clean enough to "
                "wear after class.",
        "elevate": "Grey half-zip, New Balance, a cap. Keep it neutral, no neon.",
        "slots": [
            {"slot": "top", "prefer": ["black", "navy", "cream", "white"],
             "fallback": ("Neutral fitted tank", "Style rule")},
            {"slot": "bottom", "prefer": ["black", "navy", "cream"],
             "fallback": ("Full-length leggings or sweat-set", "Style rule")},
            {"slot": "shoe", "prefer": ["grey", "white"],
             "fallback": ("Clean sneaker", "Style rule")},
            {"slot": "layer", "prefer": ["grey", "white"],
             "fallback": ("Grey half-zip or cloud hoodie", "Style rule")},
        ],
    },
    "vacation": {
        "title": "Soft travel uniform",
        "note": "White top, relaxed denim or ecru bottom, cloud hoodie, clean "
                "sneakers. Comfortable without looking like airport pajamas.",
        "elevate": "A Dairy Boy cap and gold hoops. Swap to ecru shorts if you'd "
                   "rather not fly in denim.",
        "slots": [
            {"slot": "top", "prefer": ["white", "cream"],
             "fallback": ("White easy top", "The Edit")},
            {"slot": "bottom", "prefer": ["blue", "denim", "ecru"],
             "fallback": ("Relaxed denim or ecru shorts", "Style rule")},
            {"slot": "layer", "prefer": ["white", "grey"],
             "fallback": ("Cloud hoodie or light jacket", "Yours / guess")},
            {"slot": "shoe", "prefer": ["grey", "birch", "white"],
             "fallback": ("Mexico 66 or easy sneaker", "Style rule")},
        ],
    },
    "casual": {
        "title": "Cream, denim, brown leather",
        "note": "Soft cream top, wide denim or ecru shorts, structured light "
                "layer, gold jewelry. Easy and lived-in, not fussy.",
        "elevate": "Brown leather bag and tall cognac boots warm it up in fall.",
        "slots": [
            {"slot": "top", "prefer": ["cream", "white", "ecru"],
             "fallback": ("Soft cream top", "Style rule")},
            {"slot": "bottom", "prefer": ["blue", "denim", "ecru"],
             "fallback": ("Wide denim or ecru shorts", "Style rule")},
            {"slot": "shoe", "prefer": ["birch", "grey", "brown"],
             "fallback": ("Mexico 66 or gum-sole sneaker", "Style rule")},
        ],
    },
}


def load_closet(path=CLOSET_PATH):
    data = json.loads(Path(path).read_text())
    return data.get("pieces", []) if isinstance(data, dict) else []


def _banned(piece):
    text = f"{piece.get('name','')} {piece.get('brand','')} {piece.get('color','')}".lower()
    if BANNED_TEXT.search(text):
        return True
    return any(t in BANNED_TONES for t in piece.get("tones", []))


def _score(piece, occ, prefer):
    """Higher = better fit for this slot. None means disqualified."""
    if _banned(piece):
        return None
    s = 0.0
    if occ in piece.get("occ", []):
        s += 3
    if piece.get("owned"):
        s += 2
    tones = set(piece.get("tones", []))
    if tones & set(prefer):
        s += 4  # matches the formula's preferred tone for this slot
    s += len(tones & LOVED_TONES) * 0.5
    if not piece.get("img"):
        s -= 1  # prefer a piece we can actually show
    return s


def _pick(closet, occ, slotdef, used):
    candidates = [p for p in closet if p.get("slot") == slotdef["slot"]
                  and p.get("id") not in used]
    best, best_s = None, None
    for p in candidates:
        sc = _score(p, occ, slotdef["prefer"])
        if sc is None:
            continue
        if best_s is None or sc > best_s:
            best, best_s = p, sc
    return best


def build_look(event, closet, occ=None):
    """event: {'t': title, 's': 'HH:MM', 'allDay': bool, ...} (or a plain title).
    Returns a structured look ready to render."""
    title = event.get("t") if isinstance(event, dict) else event
    occ = occ or occasion_of(title)
    formula = FORMULAS.get(occ, FORMULAS["casual"])
    used, pieces = set(), []
    for slotdef in formula["slots"]:
        p = _pick(closet, occ, slotdef, used)
        if p:
            used.add(p["id"])
            pieces.append({
                "slot": slotdef["slot"], "name": p["name"], "brand": p.get("brand", ""),
                "color": p.get("color", ""), "img": p.get("img"),
                "owned": bool(p.get("owned")), "source": p.get("source"),
            })
        else:
            label, brand = slotdef["fallback"]
            pieces.append({"slot": slotdef["slot"], "name": label, "brand": brand,
                           "color": "", "img": None, "owned": False, "guess": True})
    owned_n = sum(1 for p in pieces if p["owned"])
    ev = event if isinstance(event, dict) else {}
    return {
        "occasion": occ,
        "event": title,
        "title": formula["title"],
        "note": formula["note"],
        "elevate": formula["elevate"],
        "pieces": pieces,
        "confidence": "owned" if owned_n >= len(pieces) - 1 else
                      "mixed" if owned_n else "guess",
        "start": ev.get("s"), "day": ev.get("day"), "allDay": ev.get("allDay"),
    }


def build_week(events, closet):
    """One look per occasion lane — you wear one outfit per occasion type. Each
    look carries `events`, the list of that lane's event titles (so the weekly
    Edit can head a card by lane and list its events). Calendar order; non-dress
    events (money due, admin) get no card."""
    looks, by_lane = [], {}
    for e in events:
        title = e.get("t") if isinstance(e, dict) else e
        occ = occasion_of(title)
        if occ is None:
            continue
        if occ not in by_lane:
            look = build_look(e, closet, occ)
            look["events"] = []
            by_lane[occ] = look
            looks.append(look)
        if title not in by_lane[occ]["events"]:  # dedupe recurring entries
            by_lane[occ]["events"].append(title)
    return looks


def demo():
    closet = load_closet()
    assert closet, "closet.json is empty"

    # Occasion detection covers her real lanes + calendar shorthand.
    assert occasion_of("Alex's Birthday dinner") == "going-out"
    assert occasion_of("Alex bday") == "going-out"
    assert occasion_of("Flight to Vail") == "vacation"
    assert occasion_of("Strength training") == "active"
    assert occasion_of("Client meeting") == "work"
    assert occasion_of("Coffee with mom") == "casual"
    # Non-dress events get no card (was wrongly producing a casual look).
    assert occasion_of("CHASE MONEY DUE") is None
    assert occasion_of("Rent due") is None
    assert build_week([{"t": "CHASE MONEY DUE"}], closet) == []

    # build_week collapses a day to one look per lane and lists each lane's
    # events. Two coffees + one dinner: 2 looks; casual look lists both coffees.
    day = [{"t": "Coffee with mom"}, {"t": "Coffee with Sara"}, {"t": "Dinner date"}]
    wk = build_week(day, closet)
    assert len(wk) == 2
    casual = next(l for l in wk if l["occasion"] == "casual")
    assert casual["events"] == ["Coffee with mom", "Coffee with Sara"]

    # Going-out picks a sleek black/satin top she owns, never red.
    look = build_look("Dinner reservation", closet)
    assert look["occasion"] == "going-out"
    top = next(p for p in look["pieces"] if p["slot"] == "top")
    assert top["owned"], "should pull an owned going-out top"
    assert all("red" not in (p.get("color", "").lower()) for p in look["pieces"])

    # Work fills the trouser slot even though she owns no work trouser → guess,
    # but the ivory top should come from her closet.
    work = build_look("Webflow client call", closet)
    wtop = next(p for p in work["pieces"] if p["slot"] == "top")
    assert wtop["owned"], "owns an ivory/white top for work"

    # Every look fills every formula slot, no piece reused within a look.
    for occ in FORMULAS:
        lk = build_look("x", closet, occ)
        ids = [p["name"] for p in lk["pieces"]]
        assert len(lk["pieces"]) == len(FORMULAS[occ]["slots"])
        assert len(ids) == len(set(ids)), f"duplicate piece in {occ}"

    print("style_engine self-check OK —",
          {occ: build_look("x", closet, occ)["confidence"] for occ in FORMULAS})


if __name__ == "__main__":
    demo()
