---
date: 2026-06-17
time: 12:40
project: ideas / wellness-activity-finder
status: CONCEPT — brainstorm only, no build started. Waiting on Annabel to pick (a) pressure-test as product vs personal tool, or (b) scope v1 + build a clickable mockup. Claude recommends (b) and needs Annabel to name the launch city.
next-session: Map-based finder whose wedge is the compound query Google can't answer ("gym that ALSO has a sauna, 4.5+"). Decided: wellness-first (not activities), curated pre-enriched index for 1 city (not scrape-anywhere-live) for v1. The moat is the amenity-enrichment layer (LLM reads reviews + website → structured {sauna, steam, pool, cold-plunge, classes} profile), NOT the map UI (already built twice: Tarifa venue cards + Style Feed ranking). To resume: get Annabel's city + direction pick, then scope the v1 (one city, wellness, ~20-40 hand-picked venues, keyless OSM/Leaflet map, amenity checkboxes + min-rating slider) and build the mockup with seed data.
---

# Session: Wellness / activity finder — concept shaping

Brainstorm only. No files created, no prototype built. Annabel was riffing
("brain pumping out ideas"). Origin: she was traveling in Europe and wanted to
find a place to use a sauna that also had a gym, with a map + filter, ranked by
Google reviews. Explicitly tied it to the kitesurf "Google Map with an activity
finder" idea ([[2026-06-16-1240-kite-wind-watch-google-map-hero]]).

## The idea
A map-based finder where you filter by a combination of amenities/activities
plus a quality bar and get review-ranked results.
- Example query: "I'm in Paris, find a gym that also has a sauna, 4.5+ reviews."
- Map + filters + cards ranked by Google rating.
- Two possible framings she floated: **wellness** (gym + sauna + pool + cold
  plunge + steam) or **activity** (kite-surf rentals, etc., 4.5+).

## Key insights / what Claude argued
- **The wedge is the compound query Google can't answer.** Google stores "gym"
  as a type and stores the star rating, but does NOT store "has a sauna" as a
  structured field for gyms. So nobody can filter on it today. The moment the
  filter is an AND of 2+ amenities plus a quality bar, you're doing something
  Maps / TripAdvisor / ClassPass can't.
- **Easy part = the map UI; hard part = the data, and that's the moat.** Annabel
  has basically built the front end twice already (Tarifa venue cards w/
  photos+ratings+review links; Style Feed ranking UI). The valuable part is
  turning a raw place into a structured amenity profile
  `{sauna: yes, steam: yes, pool: no, cold-plunge: yes, classes: yes}` — Google
  won't hand that over, but it's exactly an LLM job (feed reviews + website text,
  ask "does this have a sauna?", get clean yes/no). That enrichment layer is what
  a competitor can't trivially copy.

## Decisions / recommendations
- **Wellness first, not activities.** It's the query Google truly can't do
  (amenity combinations), whereas "kite rental 4.5+" Google mostly *can* already
  do via search+sort. Also she personally wanted it, so she's the user. Activities
  reuse the same shell and can come later.
- **Curated index, not scrape-anywhere-live, for v1.** Live-scraping every gym in
  a city (hundreds of venues, each needing a website fetch + review read) is slow
  and runs up cost per search. Build a pre-enriched index for 1 city first; earn
  live-anywhere later.
- **Data source reality:** legit path is the **Google Places API (paid per call)**
  or **OpenStreetMap (free but sparse on amenities)**, NOT scraping Google
  directly. (Consistent with prior Tarifa note: Google Maps embed needs a paid key;
  shipped keyless OSM — see [[reference_venue_image_sourcing]].)
- **Ranking detail:** don't rank on raw stars. 4.9 with 12 reviews must not beat
  4.6 with 3,000. Use a minimum review count + a volume-weighted score.

## Proposed v1 (not yet approved)
One city, wellness only, ~20-40 hand-picked venues, each enriched with an amenity
checklist + rating + review count, on a keyless OSM/Leaflet map with amenity
checkboxes and a min-rating slider. Close to the Tarifa build, useful to Annabel
on her next trip, proves the enrichment idea before spending on live infra.

## Open questions / next decision
Claude offered two paths and recommended (b):
- (a) Pressure-test it as a real product vs a personal tool first (office-hours /
  Garry).
- (b) Scope the v1 and build a clickable mockup with seed data for one city.
Needs from Annabel: the launch **city**, and a yes on wellness-first.

## Related threads
Part of a cluster of map/discovery ideas: kite-wind-watch (kite conditions +
Google map hero), kitesurf-connect-app (rider/coach matching), Style Feed
(review-style ranking UI), and the Tarifa venue guide (the reusable venue-card +
map pattern this would generalize).
