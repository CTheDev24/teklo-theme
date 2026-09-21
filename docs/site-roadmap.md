# Teklo storefront roadmap

Last updated: 2026-09-21

## Current implementation — 2026-09-21

The Studio Refresh uses a Trace-first homepage, split making-video hero, three-column introduction, maker-seal philosophy section, clean supplied photography and branding. Studio has three offering cards, selected projects and Around the Shop; the tent connector appears in its offering and project. Custom Work uses a native inquiry template. Final implementation and release status are maintained in studio-refresh-release.md.

Status: implemented in a development theme; Shopify rendering and automated checks pass. Browser visual/interaction QA is blocked by the local browser tool failing to initialize. Not approved for live publication. The historical acceptance notes below describe the August homepage, not this new revision.

Release preparation and outstanding assets are tracked in [studio-refresh-release.md](studio-refresh-release.md). The Custom Work preview uses the existing contact page with the alternate custom-work template; the dedicated custom-work page remains a release step. Sample project photos can be added later.

## Purpose

This document is the durable product roadmap for the Teklo storefront. It records the original direction, what is working now, what remains unfinished, and which ideas are proposed rather than approved.

Implementation-specific acceptance criteria belong in `review/design-brief.md`. This roadmap should remain higher-level and evolve as the studio, catalog, and content grow.

## Storefront vision

Teklo should feel like a small design studio with a shop, not a generic product marketplace. It should balance three jobs:

1. Sell design-led objects through familiar, trustworthy Shopify commerce.
2. Show how objects and one-off commissions are designed and made.
3. Build a recognizable studio identity through projects, experiments, and useful editorial content.

### Approved visual direction

- Warm off-white and black foundation
- Restrained sans-serif typography
- Generous editorial spacing
- Asymmetric product presentation
- Full-width campaign moments
- Commerce cues kept visually secondary
- Product and process photography as the main source of color
- Accessible, responsive, Shopify-native behavior

## Historical August site map (superseded by the September release notes)

### Homepage

Status: strong foundation; accepted in the real Shopify development preview.

Current structure:

1. Teklo overlay header
2. Video-ready hero and Shop Objects CTA
3. Selected Objects
4. Trace campaign story
5. Lighting campaign story
6. More From the Studio product collection
7. Made at Teklo process sequence
8. In Their Space, automatically collapsed while empty
9. Studio Notes newsletter
10. Shopify-native footer, localization, policies, payments, and Shop features

Completed behavior:

- One meaningful homepage H1
- Responsive desktop and mobile hero treatment
- Separate desktop and mobile Shopify video inputs
- Poster-first hero rendering and reduced-motion fallback
- Temporary desktop hero-video fallback asset
- Real Shopify collection, product, price, availability, and URL behavior
- Optional editorial product-card titles with authoritative product-title fallback
- Empty testimonial content does not create blank space
- Duplicate homepage footer newsletter is suppressed
- Configurable Teklo text identity in the homepage header and footer
- Keyboard focus treatment and responsive layout checks completed for the principal homepage actions

Known follow-ups:

- Replace the temporary hero video when approved final desktop and mobile files exist
- Confirm final mobile-video crop with a dedicated 9:16 asset
- Improve or replace product photography that does not match the studio direction
- Restore In Their Space only when real customer imagery and approved attribution exist
- Recheck cart behavior, assistive-technology output, and video performance before launch

### Catalog and collection pages

Status: Shopify-native foundation exists; no Teklo-specific design pass is documented.

Desired outcome:

- Clear browsing without losing the quiet editorial character
- Consistent product imagery and compact metadata
- Useful filtering and sorting only where the catalog warrants it
- Honest availability and pricing
- Strong mobile scanning and product selection

Questions for a future pass:

- Which collections are durable enough to feature in navigation?
- Should one-off work remain editorial-only, or can selected projects lead to inquiries?
- When does the catalog become large enough to justify collection-navigation cards?

### Product pages

Status: Shopify-native product templates exist; Teklo-specific content and layout requirements are not yet defined.

Proposed requirements:

- Strong image hierarchy and useful detail views
- Clear title, price, variant, availability, quantity, and cart behavior
- Concise product story followed by practical specifications
- Materials, dimensions, care, lead time, and customization only when factually supported
- Related objects that feel curated rather than algorithmically crowded
- Mobile purchase controls that remain easy to understand and operate
- No unsupported manufacturing, durability, sustainability, or sourcing claims

### Studio / About

Status: an existing About Us route is available, but its Teklo role and presentation have not been reviewed.

Proposed purpose:

- Explain who is behind Teklo
- Describe the relationship between design, digital fabrication, and hands-on finishing
- Connect the storefront to project work and the Made at Teklo process
- Provide a credible path for appropriate inquiries without overstating capabilities

### Contact

Status: an existing contact route is available; no dedicated review is documented.

Future review should confirm form accessibility, response expectations, spam handling, and whether project inquiries need structured fields.

### Cart and checkout handoff

Status: preserved as Shopify-native; no checkout customization is planned.

Required principles:

- Preserve Shopify cart, localization, payment, policy, and checkout behavior
- Keep cart access obvious from every template
- Avoid adding friction or unsupported urgency messaging
- Test variants, quantities, removal, empty cart, discounts, and mobile behavior before launch

## Proposed next feature: Studio Journal

Status: proposed and recommended; naming and scope require merchant approval before implementation.

### Why it fits

A project journal extends the approved studio positioning more naturally than adding more homepage merchandising. It provides a home for one-off work, experiments, commissions, lessons, and processes that may never become products.

Use Shopify's native blog and article system so authorship, publishing, article URLs, SEO fields, tags, and Theme Editor behavior remain maintainable.

### Recommended positioning

Working names:

- Studio Journal
- Projects
- Field Notes

Recommended default: **Studio Journal**, with individual entries treated as project stories rather than conventional marketing posts.

### First proposed article: ship-hull mold

The ship-hull mold is a strong opening story because it demonstrates practical problem solving and a one-off application of 3D printing.

Suggested article structure:

1. Project overview
2. The problem or requested outcome
3. Constraints and reference material
4. CAD or digital development
5. Print and mold-making approach
6. Iterations, tests, or failures worth showing
7. Finished mold and resulting use
8. What the project taught the studio

Content guardrails:

- Do not identify a client without permission
- Do not disclose confidential drawings, dimensions, or process details
- Do not imply certifications, engineering validation, or performance claims without evidence
- Clearly distinguish a mold, prototype, tooling aid, finished part, and production-ready component
- Use real project photography and facts rather than invented narrative

### Journal experience requirements

Journal index:

- Editorial lead story with restrained supporting cards
- Real article image, title, date, and optional short excerpt
- Useful tags only if they support genuine browsing
- Empty states that do not look broken
- Responsive image crops and keyboard-accessible article links

Article template:

- Strong project title and introduction
- Flexible wide, portrait, and paired media
- Readable long-form typography
- Descriptive captions and alt text
- Optional project facts such as type, year, material, or process
- Related entries or a simple return to Studio Journal
- Newsletter invitation only when it does not duplicate another prominent form

Homepage integration:

- Do not add a journal section until at least two credible entries exist, unless a single lead story is intentionally presented as a launch feature
- When ready, use a restrained Latest from the Studio section near Studio Notes
- Keep the homepage secondary to the objects and campaign storytelling

### Information needed before implementation

- Approved journal name
- Whether the ship-hull work can identify the client or project context
- Project date and concise factual summary
- Photographs, renders, diagrams, or video that may be published
- The actual workflow, constraints, iterations, result, and lessons
- Any confidential details that must be excluded
- Whether project inquiries should have a CTA and, if so, its confirmed destination

## Content and media backlog

Priority assets:

1. Final desktop hero video, approximately 16:9 and 6–10 seconds
2. Final mobile hero video, approximately 9:16 and 6–10 seconds
3. Stronger cohesive photography for weaker catalog cards
4. Real customer photography and approved testimonials for In Their Space
5. Ship-hull mold project media and factual notes
6. Studio portrait, workspace, or process imagery for the About page

For every asset, record ownership, permission to publish, alt-text intent, crop requirements, and whether it is final or temporary.

## Suggested delivery phases

### Phase 1 — Preserve and release the homepage foundation

Status: substantially complete.

- Finalize hero media
- Complete launch-level cart, keyboard, reduced-motion, and assistive-technology checks
- Confirm product photography and visible copy
- Keep the accepted homepage structure stable

### Phase 2 — Establish Studio Journal

Status: recommended next exploration.

- Approve journal name and content model
- Inventory ship-hull source material
- Design the journal index and article template
- Build with Shopify-native blog/article objects
- Publish only after real content is reviewed

### Phase 3 — Refine the commerce journey

Status: not yet scoped.

- Audit collection, search, product, and cart flows
- Define Teklo-specific product-information standards
- Improve templates with small reversible changes
- Test authoritative Shopify behavior across desktop and mobile

### Phase 4 — Complete the studio story

Status: not yet scoped.

- Refine About and Contact
- Decide whether project inquiries belong on the site
- Add In Their Space only with approved material
- Consider homepage journal integration once sufficient content exists

### Phase 5 — Launch readiness

Status: future.

- Content, link, SEO, accessibility, performance, analytics, policy, localization, and browser QA
- Confirm domain and visible business identity
- Review apps and third-party console warnings
- Document publishing and rollback procedure
- Obtain explicit merchant approval before publishing

## Ideas parking lot

These are possibilities, not commitments:

- Project inquiry form with carefully chosen qualifying fields
- Process taxonomy across articles, such as CAD, printing, tooling, finishing, and installation
- Limited-run or archive collection
- Project-to-product cross-links where genuinely relevant
- Downloadable care or installation guides
- Collection-navigation mosaic after the catalog has several meaningful collections
- Video or motion within journal articles when it adds explanatory value

## Decision log

- 2026-08-12: Approved the quiet editorial homepage direction and accepted its real-preview implementation.
- 2026-08-12: Kept In Their Space hidden until meaningful customer content exists.
- 2026-08-12: Made Studio Notes the sole prominent homepage newsletter form.
- 2026-08-13: Added a temporary hero video for review while retaining the still-image and reduced-motion fallback.
- 2026-08-13: Chose not to pursue a Tinker-style collection-card mosaic at the current catalog stage.
- 2026-08-13: Identified a project journal and the ship-hull mold as the strongest next content exploration.

## Roadmap maintenance

Update this document when a feature is approved, completed, deferred, or rejected. Add concrete implementation criteria to a separate brief rather than turning this roadmap into a task-level specification. Never mark proposed content as approved without a merchant decision.
