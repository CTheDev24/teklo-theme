# Teklo homepage design brief

## Goal

Create a quiet, premium editorial storefront for design-led 3D-printed objects. The homepage should feel like a small design studio and catalog, not a default Shopify product grid.

## Visual principles

- Warm off-white and black remain the dominant palette; product imagery supplies color.
- Use generous whitespace, restrained typography, and clear editorial pacing.
- Alternate quiet product storytelling with strong full-width campaign moments.
- Keep commerce cues useful but visually secondary.
- Preserve accessibility, responsive behavior, Theme Editor control, and Shopify-native functionality.

## Current iteration: homepage refinement after Shopify preview audit

### Live-preview rejection from iteration 1

The local fixture produced a false positive. In the real Shopify preview, the product cards still inherit a dark gray/black native card content background, product metadata remains visually heavy, and both the section's left edge and `View all objects ->` are clipped outside the viewport. Treat the real Shopify preview as authoritative over the fixture. Fix the native Publisher card cascade and page-width/grid geometry; do not merely update the fixture.

Implement these changes in priority order:

1. Redesign **More From the Studio** as a calm editorial catalog. Remove black caption panels; use clean media on the cream ground; place a short, restrained product title and price beneath each image; prevent title/price collisions; use consistent image ratios and comfortable gutters; keep the staggered editorial rhythm; and ensure `View all objects ->` is fully visible and aligned with the section grid.
2. Keep real Shopify product and collection links, prices, availability, collection selection, and Theme Editor controls intact. Short display titles may be configurable editorial overrides, but must never replace or mutate Shopify product titles or SEO data.
3. Configure homepage CTA defaults where the destination is unambiguous: `Shop objects` and `View all objects` go to `/collections/all`; `Explore the studio` and `Inside the studio` go to the appropriate existing studio/about page when it exists locally. Leave ambiguous campaign links configurable rather than inventing destinations.
4. Improve the homepage header hierarchy so the storefront name does not compete with the hero headline. Do not create a new logo or perform a broad header redesign.
5. Preserve the strongest current moments: hero composition, Selected Objects spacing, the corrected Trace image and editorial treatment, distinct Lighting campaign, Made at Teklo narrative, and Studio Notes.
6. Keep the missing `FINISH` process media as an explicit honest placeholder until a real or approved image is supplied. Do not reuse another process image or fabricate unsupported product/process claims.

## Shopify preview audit evidence

- `review/audit-current/01-hero-desktop.png`
- `review/audit-current/02-selected-objects.png`
- `review/audit-current/03-trace-lighting.png`
- `review/audit-current/04-more-from-studio.png`
- `review/audit-current/05-process.png`

## Acceptance criteria

- Desktop and mobile screenshots are present in `review/evidence/current/` and show the changed area plus its surrounding context.
- No equal-card, heavy-bottom, default-Shopify-grid treatment remains in More From the Studio.
- Product titles do not dominate or wrap awkwardly at the target viewport widths.
- Product name, price, and collection navigation remain understandable and keyboard accessible.
- No black metadata panel appears below or over product imagery in the Teklo presentation.
- No gray metadata panel or inherited card color-scheme background appears below or over product imagery in the real Shopify preview.
- Product title and price never overlap, collide, or clip at 1440 x 1000 or 390 x 844.
- `View all objects ->` remains entirely inside the content area at both viewports.
- The heading, first product, and `View all objects ->` all share a visible left content edge; none begins outside the viewport.
- Theme Editor merchants can select the collection and control the relevant content.
- Live Shopify product URLs, prices, availability, and collection behavior remain authoritative.
- Homepage CTA links use valid local destinations when those destinations are known; no knowingly disabled primary homepage CTA remains.
- The storefront name remains legible but subordinate to the hero headline.
- The Trace section uses the supplied route-art image and Lighting uses its distinct lamp image.
- FORM, MAKE, and SEND show their approved process assets; FINISH remains visibly honest when no approved asset exists.
- The change does not regress the header, hero, Trace, process, newsletter, footer, cart, product links, or reduced-motion behavior.
- `shopify theme check` completes without new warnings attributable to the change.

## Review viewports

- Desktop: 1440 x 1000
- Mobile: 390 x 844

## Scope guardrails

- Work on a feature branch only.
- Never publish, push, merge, change store data, or connect checkout during the loop.
- Prefer isolated `teklo-*` sections/assets and small, reversible edits.
- Treat any screenshot reference as evidence, not as permission to copy third-party assets or branding.
