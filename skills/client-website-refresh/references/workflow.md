# Website Refresh Workflow

This is the repeatable harness from the Vital Health process plus the earlier
website-audit pipeline. Keep it manual-first until a client type has worked more
than once.

## 0. Start Clean

- Read `AGENTS.md`, project `CLAUDE.md` or `AGENTS.md`, and exact memory recall.
- Work in `projects/<client-or-project>/`, not the AI-OS root.
- Keep prospect-specific artifacts inside that project folder.
- Create a short context file if the folder is new: client, URL, stakeholders,
  known tools, access status, current blockers, and review link.

## 1. Intake And Client Dislikes

Capture three layers before designing:

- Client says: direct quotes, specific dislikes, must-keep elements, business
  constraints, staff workflow complaints.
- Annabel says: taste notes, quality bar, what feels cheap, generic, wrong, or
  below standard.
- Reality says: outdated facts, broken links, mobile issues, missing trust,
  unclear CTA, SEO gaps, editability problems, backend confusion.

Do not translate vague client comments into a giant build. Ask enough questions
to separate public-site work from backend, admin, vendor, or operations work.

## 2. Audit The Current Website

Minimum audit for a real client refresh:

- Desktop and mobile screenshots of the current site.
- Current page list, nav, CTAs, forms, booking links, store links, portal links.
- Factual inventory: names, roles, addresses, phone, hours, services, pricing,
  testimonials, compliance-sensitive claims.
- Third-party reality check: Google Business Profile, reviews, booking/store
  tools, social profiles, vendor portals, current platform.
- Brand inventory: logo, fonts, colors, imagery, tone, strongest existing assets.
- Asset preservation list: which original images, fonts, section concepts, and
  brand details seem necessary to keep because they carry the client's identity
  or explain the service.
- Client-editability map: what must be editable by the client after launch.

For health, wellness, finance, legal, or other trust-sensitive sites, add a
claims matrix before mockup copy:

- Exact claim or testimonial.
- Where it appears.
- What it promises or implies.
- Source or approval status.
- Keep, soften, attribute, move, or remove.
- Who must sign off.

Use the older `projects/website-audit/.claude/commands/` pipeline as source
material when doing full scrape, SEO, AI discoverability, mockup, or outreach
work. The new harness does not replace that pipeline; it routes the higher-touch
client implementation lane.

## 3. Decide Architecture Before Building

Classify each thing the client wants:

- Public site: pages, services, trust, bios, resources, announcements, SEO.
- Client workflow: approvals, staff process, content updates, testimonials.
- Backend/vendor system: portal, checkout, EHR, scheduling, CRM, inventory.
- Compliance or sign-off: health claims, legal claims, refund policy, pricing.

Recommendation pattern from Vital Health:

- Use Webflow for editable public-site content when the client needs to update
  pages, bios, services, announcements, or resources without a developer.
- Keep existing patient portals, booking tools, stores, or vendor systems unless
  there is a strong reason to replace them.
- Describe backend work as coordination, setup, testing, or workflow mapping
  unless Annabel is genuinely building the backend.

## 4. Garry Scope Pass

Garry should answer:

- What is the real offer, and what is out of scope?
- What should be fixed price versus hourly?
- What discovery is needed before pricing backend/admin work?
- What client responsibilities and blockers need to be named early?
- What would make this proposal feel honest, premium, and not overpromised?

For implementation, Garry writes a concise handoff instead of prescribing code.

## 5. HTML Preview

Use an HTML/static preview when Annabel or the client needs to feel the redesign
before committing to the final platform.

Before building or polishing the preview, read
[html-preview-quality.md](html-preview-quality.md). Treat it as the quality gate
for static mockups.

For regulated or health-adjacent sites, do not write stronger claims in the
preview than the current site already makes. Prefer softer language or clearly
flagged placeholders until the claims matrix is approved.

Quality bar:

- Preserve the client's useful brand DNA while raising the taste level.
- Preserve necessary original imagery and fonts unless there is a clear reason
  to replace them. Do not swap in random stock or generic fonts by default.
- Choose a distinct art direction before coding. Avoid defaulting to blue/white
  SaaS, generic wellness cards, or a template rhythm.
- Use real facts only. If facts are missing, write soft copy or placeholders.
- Use actual assets where possible. Styled placeholders are acceptable when the
  client must provide headshots, testimonials, or policies.
- Build responsive desktop and mobile from the start.
- Do not render audit notes, diff labels, or "what changed" pills inside the
  mockup. The mockup should feel like the new website.
- Browser-check screenshots before sharing. If the first read is "AI generated,"
  keep polishing.

## 6. Business Partner QA

Business Partner checks:

- Site renders on desktop and mobile.
- Links, nav, booking, phone, email, forms, and portals are correct.
- Copy obeys Annabel's mechanics and current-person status.
- No placeholders are hidden from the handoff.
- No unsupported claims, especially health, legal, financial, or pricing claims.
- Editability tradeoffs are explicit.
- Review link is staging or preview unless live publish was approved.

For Webflow work, use `$webflow-rebuild-qa`.

## 7. Client-Editable Platform Build

When translating the preview into Webflow or another platform:

- Rebuild native sections in the platform where editability matters.
- Use CMS collections for repeatable client-owned content when useful: bios,
  services, resources, promotions, announcements, testimonials.
- Use custom code only for polish that should not be client-edited, such as
  reveal animation, minor nav behavior, or exact visual matching.
- Publish to staging first and QA the published site, not just the builder canvas.
- Keep a list of non-live blockers and explain them plainly.

## 8. Proposal And Next Steps

Use `$client-proposal-pdf` when the output should be a polished PDF.

The proposal should include:

- Review link or shipped work summary.
- Phase 1: what is already done or the fixed public-site scope.
- Phase 2: discovery-dependent backend/admin/workflow scope.
- Honest ranges, rate, hosting/subscription costs, and payment method.
- Client responsibilities and blockers.
- Optional add-ons only after the core scope is clear.
- Clear next steps, usually approval, meeting, missing assets, then launch.

## 9. Compound The Learning

After delivery, add the smallest durable improvement:

- A checkpoint if decisions or blockers should survive.
- A good or bad example if Annabel corrected a pattern.
- A project `CLAUDE.md` note if the project needs future routing.
- A skill reference update if the lesson generalizes across clients.
