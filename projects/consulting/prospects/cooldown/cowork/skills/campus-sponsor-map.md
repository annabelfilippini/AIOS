# /campus-sponsor-map

**When to use:** When cooldown is launching or relaunching a college chapter and needs a local sponsor target list, activation angles, and draft-ready sponsor inputs.

**Owner:** Anya for launches, Bailey for sponsor relationship decisions

**How to use:** Use this before chapter outreach starts. It creates the sponsor map for one campus at a time, then hands off the best targets into `/sponsor-research` or `/sponsor-outreach`.

---

## Prompt to paste

```
/campus-sponsor-map

Campus / city:
[e.g., "University of Michigan / Ann Arbor"]

Launch status:
[new launch, relaunch, likely returning, date set, date TBD]

Launch date:
[date or "TBD"]

What we know:
[chapter leader, expected turnout, run day/time, starting location, existing sponsor interest, any warm intros. Leave unknowns blank.]

Sponsor categories to include:
[optional. Default: running stores, coffee, smoothie/juice, fitness studios, recovery/wellness, local food, campus-friendly national brands, apparel/printers.]

Sponsor categories to avoid:
[optional. Default for campus: alcohol, gambling, weight-loss/diet products, anything that would make a student chapter feel unsafe or off-brand.]

Build the campus sponsor map. Use this exact structure:

1. CAMPUS LAUNCH SNAPSHOT
   3 bullets. What is known, what is missing, and what the sponsor moment is likely to be.

2. BEST-FIT SPONSOR CATEGORIES
   5-7 categories. For each:
   - Why it fits cooldown:
   - Best ask:
   - What makes a brand in this category a "yes":

3. TARGET LIST
   10-15 prospects grouped by category.
   For each prospect:
   - Name:
   - Category:
   - Why they might fit:
   - Contact path to verify:
   - Activation idea:
   - Priority: high / medium / low

4. WARM INTRO ANGLES
   3-5 possible warm paths: Fleet Feet, campus orgs, chapter leader network, local studios, local creators, existing recurring sponsors, or Bailey's network.

5. FIRST-WAVE OUTREACH PLAN
   A 2-week sequence:
   - Day 1:
   - Day 3:
   - Day 7:
   - Day 10:
   Keep it practical and manual-review friendly. No auto-sending.

6. DRAFT-READY INPUTS
   Give the top 5 prospects as paste-ready `/sponsor-outreach mode=chapter-launch` inputs:

   Chapter / city:
   Launch date:
   Sponsor:
   Contact:
   Ask:
   Prior relationship:

7. WHAT TO CONFIRM BEFORE EMAILING
   Missing date, route, expected turnout, leader name, correct contact, partner category risk, or sponsor exclusivity questions.

CRITICAL:
- If browsing is available, use public research and cite or label source paths. If browsing is not available, make this a research plan and mark targets as `[research needed]`.
- Do not invent contacts, addresses, sponsor interest, or prior relationships.
- Campus sponsors should feel useful to the students showing up, not like a brand slapped on a launch.
- Avoid alcohol-first sponsor ideas for college launches unless Bailey explicitly asks.
- The output should help Anya start outreach this week.
```

---

## Notes

- Use this one campus at a time. Ten campuses in one prompt will create generic lists.
- If a warm partner already exists, such as Fleet Feet for Ann Arbor, treat that as the first anchor and build outward from it.
- Use `/sponsor-research` on the top 3-5 prospects before drafting if the contact path or fit is uncertain.
- Use `/sponsor-outreach mode=chapter-launch batch=true` for recurring sponsors once the launch date and chapter details are confirmed.

## What this saves

Anya has not started campus outreach yet, and cooldown is aiming at 10 college launches this fall. This skill creates the first-pass sponsor list and outreach sequence in **20-30 minutes per campus** instead of rebuilding the approach from scratch each time.
