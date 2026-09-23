# Boho assortment and featured-brand follow-up — 22 September 2026

Applied directly to Shopify; no theme files or publication changed.

- Manual Shop collection 693062697126: replaced Torio (8425970794662) with Boho (8364700205222), position 4. Final order: Trace, Modern Art Deco clock, Birch light, Boho, Luxar. Torio remains a catalog product.
- P2-01 bounded fix: vendor changed from AllThings3DShop to Teklo Studio on Boho 8364700205222, clock 15295976439974, Birch 15295976341670 and Luxar 8425971941542. Trace was already Teklo Studio.
- Removed exactly ` Available now on Etsy, where artistry meets functionality.` from Boho description. Other product specifications preserved.

## Verification

Shopify readback confirms exactly five products in the intended order and all four vendor changes. Variant arrays (IDs, titles, prices and inventory quantities) match before/after exactly. Boho's default Pine Green/Off White storefront variant displays $29.95 and an enabled Add to cart button; zero reported stock was not treated as permission to alter inventory. No new checkout or fulfillment pass is claimed.

Dev theme 196729798822 preview shows five products, Boho replacing Torio, and Teklo Studio vendor text on all five cards. Screenshots: audit-2026-09-22/19-shop-boho-branding.png and 20-boho-shop-card.png. Admin readback verifies removal of the Etsy sentence. This is a content/configuration change; prior code tests were not rerun. NOT READY remains: checkout, full intake/proof workflow and mandatory release verification are still outstanding. P2-01 remains partial because policy branding and remaining metadata review are separate work.

## Exact rollback

Before snapshot: boho-branding-before.json. Verified after snapshot: boho-branding-after.json.

1. Add Torio 8425970794662 back to Shop collection 693062697126.
2. Remove only Boho's membership in that collection; do not delete/archive either product or remove unrelated memberships.
3. Move Torio to zero-based position 3. Confirm the prior five-product order from the before snapshot.
4. Restore vendor AllThings3DShop on the four IDs above only.
5. Restore Boho descriptionHtml from the before snapshot if reversing its Etsy-copy cleanup, after checking for intervening merchant edits.

Shopify content is shared across themes. Reverting this documentation commit does not reverse these Shopify changes. Discounts, prices, stock, handles, billing and theme publication were untouched.
