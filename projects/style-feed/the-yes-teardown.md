# The Yes — teardown + what to borrow for The Edit

The closest product ever built to The Edit was **The Yes** (Julie Bornstein,
ex-COO Stitch Fix / ex-Sephora / ex-Nordstrom). Launched 2020, acquired by
Pinterest June 2022, shut down as a standalone product. Nobody is currently
shipping this exact product, so The Yes is the reference, not a platform to fork.

This doc records how it worked and what is worth copying into `build_feed.py`.

## How The Yes worked

Modeled explicitly on Pandora's Music Genome Project. Two-step taxonomy:

1. **Human stylists seed it** — fashion experts define the attributes and
   hand-label a core set. "We had to build the most extensive taxonomy that
   exists in fashion."
2. **Computer vision + ML extend it** — ~**500 attributes per item**, applied
   across the full catalog and learned per shopper.

Personalization loop:

- **Onboarding quiz** — brand, price, color, style, size, fit captured up front
  (cold-start signal).
- **Yes/No on every item** — fed a *per-user ML model* that re-ranked the feed
  continuously ("always re-ranking as it learns better what a person likes").
- **Pop quizzes** — periodic optional questions surfaced *while browsing* to
  refine the model when it was uncertain (active learning, not just passive).
- **YES Lists** — liked items saved into a structured wishlist.

The differentiator was the **depth of the per-item attribute vector**, not the
swipe UI. One "yes" taught the model about fabric, neckline, hem, drape,
formality, fit-on-body, era — many dimensions per tap.

## The Edit vs The Yes (current state)

What The Edit already does (`build_feed.py`):

- brand (liked list + learned), color/neutrality (saturation + vision),
  silhouette (12), formality (5), pattern (8), custom "old-money" axis.
- live re-rank on every heart/✕ (localStorage + `/feedback`), cross-creator
  co-sign boost, vision centroid of liked vs disliked.

What The Edit has that The Yes did NOT:

- **Creator co-sign.** The Edit ranks *what specific people Annabel follows
  bought*, not a whole catalog. Stronger taste prior than any quiz. Lean in.

What The Yes had that The Edit does not, ranked by payoff:

1. **Wider per-item attribute vector.** Add neckline, sleeve, length, fabric,
   drape to `VISION_SCHEMA`. One "yes" should teach ~12 dimensions, not ~5.
   Lowest-effort, highest-payoff change — it's a schema + prompt edit, and the
   browser `affinity()`/`learn()` already generalize over `data-*` tags.
2. **Cold-start onboarding quiz.** Replace the hardcoded `LIKED_BRANDS` seed
   with a 10–15 card first-run yes/no that builds the initial centroid. Reuses
   the existing swipe machinery.
3. **Active learning / pop-quiz.** When an item's score sits in the uncertain
   middle band, surface it deliberately and weight that swipe higher. The Edit
   currently only learns passively.

## Not worth copying

- Size/fit modeling — personal single-user feed, not multi-body fulfillment.
- Price sensitivity — Annabel has explicitly de-prioritized price.
- 500 attributes — overkill for one user; ~12 well-chosen ones capture most of
  the signal.

## Sources

- TechCrunch (2020) — taxonomy, 500 dimensions, Pandora analogy:
  https://techcrunch.com/2020/05/20/former-stitch-fix-coo-julie-bornstein-just-took-the-wraps-off-her-app-only-e-commerce-startup-the-yes/
- Marie Claire — how the quiz + yes/no loop worked:
  https://www.marieclaire.com/fashion/a33003972/the-yes-shopping-app-julie-bornstein/
- Pinterest newsroom — acquisition / shutdown:
  https://newsroom.pinterest.com/news/pinterest-to-acquire-the-yes-an-ai-powered-shopping-platform-for-fashion/
