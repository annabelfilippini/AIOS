---
date: 2026-06-22
time: 16:50
project: websites / freeyourmind-tarifa
status: DONE — brand-true homepage built from FyM's real identity, approved ("this is epic"), refined, and DEPLOYED live to https://freeyourmind-tarifa.vercel.app/ (public, no login wall). Reusable method saved into the client-website-refresh skill + memory.
next-session: Build the inner pages (Lessons, Camps, Stay, Contact) in the brand-true system, matching the homepage. Then resolve the confirm-before-launch list before pointing any custom domain.
supersedes: 2026-06-22-1620-freeyourmind-tarifa-brand-true-draft.md
---

# Session: Free Your Mind — brand-true homepage built, refined & deployed

## The pivot (Annabel's idea, on a walk)

She was making generic-to-her sites for businesses full of personality — pouring
the client's photos + copy into HER house lane (Fraunces/espresso/coral), i.e.
her taste with their content, not their brand. New method: full audit of all the
client's channels, then build FROM their real identity.

## What got built

1. **Brand audit** (Firecrawl `branding` extract of freeyourmindexperience.com +
   read their logo + About page; IG already pulled). FyM's real brand: bright
   yellow `#F8EC1E` + cyan `#4DC0E2` + magenta `#CC3366`, Urbanist + Barlow,
   rounded pills, paint-splatter logo; voice is mindful ("feel the wind, let go of
   the noise", conscious tourism). A **duality**: loud playful surface over a calm
   soulful core. Founder Tanja Rosenkranz; team Lilli/Ingo/Gonzalo/Cris/Wiebke/
   Andrea; camps Tarifa/Conil/Dakhla/Essaouira/Sri Lanka; base Los Lances Norte.
2. **Direction fork asked** → Annabel chose **the duality**.
3. **Built** the brand-true homepage (their tokens, their copy, the loud/calm
   rhythm). Kept the old espresso draft for comparison.
4. **Refinements she asked for:**
   - All SENTENCE headings replaced with plain noun titles (she hates sentence
     titles, even the client's own — rule sharpened in global Ship Gate + memory).
     Now: "Learn to kitesurf in Tarifa", "Lessons, camps & rentals", "Why Free
     Your Mind", "About Free Your Mind", "Kitesurfing in Tarifa", "Book your
     session".
   - Three offerings side by side (equal cards, CTAs bottom-aligned).
   - Hero: two buttons only, "No wind, no pay" pill moved BELOW them, ✦ star
     removed.
   - "book me in" removed everywhere → **"Message us on WhatsApp"** + secondary
     **"Offerings"**.
5. **Deployed to Vercel** (she said "this is epic, push to vercel"):
   **https://freeyourmind-tarifa.vercel.app/** — verified live, desktop + mobile,
   13 images load, 0 broken, console clean.

## File / deploy structure

- **`index.html`** = the brand-true page (served at `/`). Live homepage.
- **`index-espresso.html`** = the old espresso comparison (preserved).
- **`index-brand.html`** = identical copy of the brand page (kept; docs name it).
- 5 hero/section images that lived in `.vercelignore`d `instagram/`+`raw/` were
  copied into `assets/web/photos/site/` (hero-foil, lessons-instructor,
  wing-rider, soul-sunset, tarifa-coast) and repointed → deploy is self-contained
  (2.4M). Vercel served physical index.html over a `/` rewrite, hence the rename.
- Server: launch.json `fym-tarifa` (python http :8849, serves the project).

## Reusable method saved (she wants to recreate for other companies)

- New skill reference: `~/.claude/skills/client-website-refresh/references/brand-dna-audit.md`
  (full recipe: channel audit, Firecrawl `branding`, logo read, one-fork question,
  plain-title headings, Vercel deploy gotchas). Wired into the skill's operating
  loop (step 4) + references list.
- Memory: `feedback-client-site-from-their-brand` (+ MEMORY.md line). Sharpened
  `feedback-no-invented-headings` (plain titles, never sentences) too.
- To rerun: invoke `/client-website-refresh` — it now leads with the brand audit.

## Confirm before launch (fine for *.vercel.app pitch; not for a custom domain)

Review-quote permission; full team roster + roles; current contact email
(freeyourmindexperience.com vs old kitesurf-tarifa-spain.com); prices still routed
to WhatsApp.
