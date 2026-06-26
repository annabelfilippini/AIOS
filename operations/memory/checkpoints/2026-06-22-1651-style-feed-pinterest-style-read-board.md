---
date: 2026-06-22
time: 16:51
project: style-feed (personal shopping feed, "The Edit")
status: in-progress — UNHAPPY, needs direction
next-session: Annabel's last words were "checkpoint. everything looks bad." DO NOT keep
  iterating the board blind. FIRST clarify what "looks bad" means — two very different
  fixes: (A) the PAGE renders/looks bad (layout, the 3:4 object-fit COVER crop is cutting
  heads/full-body outfits off awkwardly, cream-on-cream tiles, too dense) → a presentation
  fix; or (B) the OUTFITS/curation are wrong / the whole static-board approach isn't landing
  → rethink the deliverable. Strong hypothesis it's at least partly (A): most pins are
  full-body shots and the card forces a 3:4 cover crop, so faces/shoes get chopped and it
  reads messy. Quick experiment for next session: change `.imgwrap` to object-fit:contain or
  a taller/auto aspect (masonry/Pinterest-style columns) so whole outfits show, rebuild, and
  ask if THAT was the problem before re-curating any images. Board builder + all assets:
  projects/style-feed/pinterest-board/build_board.py (run `python3 build_board.py`; writes
  board.html + ~/Desktop/the-edit-style-read.html, base64-embedded). Taste rules captured in
  projects/style-feed/taste-feedback.md (READ FIRST before any style work).
---

# Session: The Edit — Pinterest "style read" board as a live taste test

## What this was
Annabel doesn't love how the feed looks and wanted to pull Pinterest inspo into the mix for
work + everyday clothes. She has no pins of her own, so she set it as a TEST: "curate a
Pinterest board of what you think my style is; if you do a good job we'll build real
shoppable outfits + links." I can't post to her real Pinterest (no auth, external action),
so I built a self-contained branded HTML board (The Edit cream/Cormorant/Jost) with real
i.pinimg.com pins pulled via Firecrawl image search, base64-embedded, opened locally + copy
on Desktop. Four lanes: Everyday · Work · Workout · Going Out.

## Taste signal collected this session (saved to taste-feedback.md + memory
project_the_edit_taste_corrections)
- HATES red/burgundy (garments). LOVES black (incl. full all-black), blue, brown, grey,
  ecru/cream (her Zara shorts). A small RED accent in a shoe/bag is OK.
- Loose/relaxed pants only. NO capri/cropped leggings. Loves matching sets.
- WORK (from 5 ref pics): ivory/clean-neckline top + loose black/navy trouser + pointed
  flat; knit vest over white shirt; white top + black slit skirt; loose jeans + nice top;
  grey wool jacket / blazer-over-shoulder; brown suede bag + gold jewelry. Euro/Toteme/Row.
- EVERYDAY (from grid pics): fall-cozy + denim-heavy — oversized knits/cardigans (oatmeal,
  camel, brown, navy, grey, olive), WIDE blue jeans, tall tan/brown riding boots, brown
  loafers, gum-sole sneakers, suede jackets (tan/olive/brown), cream knit + white linen.
- WORKOUT brands she named: Set Active, Lululemon, Aritzia (sweatfleece/TNA), FP Movement.
  Neutral or all-black sets, no neon, no capri.
- Occasion read: she said GOING OUT and EVERYDAY were the ones I got least well at first.

## What got built (board v1 → v3)
- v1: my cold read (old-money/quiet-luxury, work+workout). She killed red, flares, capris.
- v2: recalibrated; added Everyday + Going Out lanes.
- v3: Work + Everyday rebuilt OUTFIT-BY-OUTFIT from her pasted reference pics; Workout pulled
  to her named brands. Key process win: I started Read-ing each downloaded pin image to
  verify before including it — caught many title/image mismatches (a going-out halter, cargo
  pants, a patterned slip dress, promo collages with text, hot-pink set, legwarmer Onitsuka).
  "Titles lie" is now a written rule in taste-feedback.md.

## The problem
After v3 she said: "checkpoint. everything looks bad." Ambiguous and unresolved — see
next-session. Did NOT diagnose whether it's the page presentation (likely the 3:4 cover-crop
chopping full-body outfits) or the curation/approach. Resist re-curating images until that's
settled.

## Files
- projects/style-feed/pinterest-board/build_board.py (builder; SECTIONS dict drives lanes)
- projects/style-feed/pinterest-board/img/ (downloaded pins)
- projects/style-feed/pinterest-board/board.html + ~/Desktop/the-edit-style-read.html (output)
- projects/style-feed/taste-feedback.md (durable hand-given taste rules — read first)
- memory: project_the_edit_taste_corrections.md

## Next steps
1. Ask what "looks bad" = page render/layout vs outfits/approach. (Lead with the layout fix
   hypothesis: try masonry / object-fit:contain so whole outfits show.)
2. If layout: rework card sizing to a Pinterest-style column masonry, rebuild, re-show.
3. If curation/approach: reconsider whether a static board is even the right deliverable, or
   pivot to building real shoppable outfits + links from the looks she already greenlit
   (the verified Work + Everyday + Workout tiles), which was the original payoff.
4. Going Out lane is still v2 (search-built, NOT eyeball-verified, no ref pics from her yet).
