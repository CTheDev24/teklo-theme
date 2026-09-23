# Additional Shop cart verification — 22 September 2026

Exact unpublished theme: teklo-theme/dev 196729798822, identified in preview bar. No payment, order, customer message or inventory change.

| Product / selected variant | Verified result |
|---|---|
| Boho / Clay/Off White, variant 46013813194918 | Visible label selection changed gallery/selected variant; added at $29.95. Existing Shopify selling settings permit this variant despite the reported negative inventory quantity. No inventory permission/policy was changed. |
| Birch / Black, Hanging Cord Included Yes, variant 56416312230054 | Price updated from $69.95 to $79.95; cart retained color and cord choice. |
| Luxar / White, 4-inch opening, variant 46200295620774 | Price updated to $24; cart retained color and size. |

Three-item cart total was $133.90 and survived reload. At controlled 360x844, drawer content scrolls and checkout geometry is top 781/bottom 828, left 46/right 345. Screenshot audit-2026-09-22/21-assortment-cart-360.png shows the Shopify preview bar overlapping the bottom; do not interpret it as a clean unobstructed checkout screenshot. This is desktop viewport emulation, not touch/real-device certification.

Increasing Luxar to two produced its $48 line total and $157.90 cart total. At 390px, removing Luxar returned $109.90, removing Birch returned $29.95, and removing Boho produced Your cart is empty. No discount appeared in these sampled baskets. Reset viewport afterward. All synthetic cart items removed.

Additional observations: Boho loaded an app-injected FREE Shipping on orders over $35 message and trust badges. Current Trace DOM with Hextom product-page script loaded showed no such free-shipping message; this is a sampled observation, not proof of all app targeting settings. Hextom's general threshold wording needs the same >=$35 correction as policies. Luxar recommendations include Torio, so the curated Shop collection does not globally restrict discovery. Long product names consume substantial drawer space but content remains scrollable.

Accessibility follow-up found encoded punctuation in generated cart control names: Birch reads literal &amp; and Luxar removal reads literal &quot;. Source uses translation interpolation followed by escape. Review escaping with Shopify translation behavior before changing it; retain safe HTML output. No screen-reader pass claimed.

Intermittent browser action timeouts were followed by fresh DOM checks before retry; eventual UI state, not attempted clicks, determined results. Checkout/actual rates/tax/payment/fulfillment remain untested because the store plan is Paused. Status remains NOT READY.
