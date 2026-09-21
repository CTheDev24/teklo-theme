# Studio refresh — review and release

Updated 2026-09-21. Branch: `codex/feature/studio-refresh`. Target: `dev`.

## Review

- Homepage: https://at3dshop.myshopify.com/?preview_theme_id=196729798822
- Studio: https://at3dshop.myshopify.com/pages/about-us?view=studio&preview_theme_id=196729798822
- Custom Work: https://at3dshop.myshopify.com/pages/contact?view=custom-work&preview_theme_id=196729798822

The changes are uploaded to unpublished `teklo-theme/dev` (196729798822). Shopify's GitHub integration also synced the uploaded theme into `dev`. The live theme has not been published or modified.

## Final implementation

- Trace-first homepage with split making-video hero, thin-rule eyebrow, three-column introduction, large Trace card, clean product photography, Home Objects introduction, maker-seal philosophy section, newsletter and Custom Work invitation. Other product listings are disabled.
- Supplied Teklo/Trace logos and maker seal. Trace images are clean Shopify Files photographs, with specifications rendered as page text: 12.5 × 15 × 2.4 inch wooden frame, 8 × 10 inch map, custom race poster, Gallery/Nocturne finishes.
- Three-part Studio page: curated objects/design and fabrication/experiments; selected projects; Around the Shop. Tent-pole connector photo appears in the fabrication card and its project entry. Professional-work project remains disabled pending details.
- Native Custom Work contact form with accessible labels, optional timing/budget/reference fields and project proof blocks. No message was submitted.
- Native search, cart, localization and mobile drawer retained. Video controls respect reduced motion, visibility, user pause and Theme Editor lifecycle.
- New interface strings have English fallbacks in all storefront locale files; merchant translations remain a release task.

## Verification

- Installed Shopify Theme Check: zero errors and nine existing warnings. The bundled skill validator cannot load its missing dependency; installed CLI validation was used.
- `node review/verify-studio-refresh.cjs`: six integration groups passed, including homepage content, two Studio connector placements, native contact form structure, catalog/product/search/cart rendering and served assets. Set `TEKLO_PREVIEW_URL` to an authenticated development renderer if port 9293 is unavailable.
- Navigation/media JavaScript syntax checks passed. Earlier controller checks covered drawer closure, pause persistence, breakpoints, reduced motion, document visibility and cleanup.
- Browser visual and keyboard verification remains blocked: CUA fails before navigation with a missing kernel-assets path. HTTP checks do not establish visual acceptance.

## Before live publication

1. Review desktop/tablet/mobile layouts, image crops, focus behavior, menu/video controls and newsletter in a working browser.
2. Assign dedicated Studio and Custom Work pages and update navigation when ready; current links use alternate templates on existing About Us and Contact pages.
3. Configure a real Trace product when available. No Trace product was returned by Shopify search, so its CTA currently opens an inquiry.
4. Add remaining project photographs, professional-project details and optional workshop/setup content.
5. Verify inquiry delivery with an authorized test message, and verify cart/checkout handoff. No transaction or message delivery has been tested.
6. Translate new fallback strings before a non-English release and approve the content before publishing.

## Photo mapping

Shopify Files originals remain the source of truth. Homepage: BB61BA2B (intro), 425BD1ED (main), DD2233B2 and 23C2B695 (supporting views). Studio: A122129A (Trace), 9A8B0F62 (connector in both locations). Full filenames are recorded in the templates. Downloaded review copies are excluded from version control.
