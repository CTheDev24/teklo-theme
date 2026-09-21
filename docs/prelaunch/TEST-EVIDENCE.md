# Verification evidence — 21 September 2026

**NOT READY.** Results below separate observed behavior from untested integrations.

## Automated checks

- Shopify Theme Check: baseline and final each 0 errors / 9 warnings; no new warnings. Local JSON reports are ignored machine artifacts in review/.
- Python unittest: 6 tests pass. Covers GPX malformed/empty/nonfinite/DTD rejection; all four source methods require a verified route; immutable per-piece identity/unit bounds; finish-time omission; invalid/private/unavailable/color holds; current proof delivery and written approval; revision invalidation; no-response never approves. This is an offline gate library, not a deployed service or authenticated receipt adapter.
- node --check assets/product-form.js: pass.
- Existing review/verify-studio-refresh.cjs attempted: its drawer/navigation unit portion passed; remote rendering assertions could not target the authenticated draft. Anonymous fetch with preview_theme_id returned the live Dawn theme and failed the split-hero assertion. This is a test-environment limitation, not a draft-theme pass. Script now accepts an explicit preview theme parameter and expects the corrected dimension placeholder; run against an authenticated local theme renderer before release.
- Skill validation helper unavailable because @shopify/theme-check-common is missing; installed Shopify CLI Theme Check used instead.

## Browser observations on exact draft 196729798822

- Preview bar identified teklo-theme/dev, Draft. Homepage Customize Trace, Shop collection route, product route and From $149.95 USD observed.
- Controlled desktop Chrome and narrow CSS viewport of 390px exercised. Requested 360px override still reported 390px after browser minimum/zoom behavior; **360px was not achieved**. No real touch, iPhone Safari, Android Chrome, virtual keyboard or 200% zoom pass is claimed.
- Mobile menu initially painted behind hero content. Added isolated hero stacking context; screenshot confirmed solid menu above hero. Menu open/close and focus returning to Menu observed; complete keyboard/screen-reader matrix outstanding.
- Nocturne and Match My Medal Color selected through visible labels; $174.95 displayed. Blank Piece reference stopped add with native required feedback. Two synthetic references QA-20260921-A/B added separately with gift notes; separate cart lines persisted after reload. Existing 25OFF applied at quantity two: $87.47 discount, $262.43 total. Both test lines removed; Your cart is empty verified. No order or customer was created.
- Checkout reproduced “This store isn’t set up to receive orders yet.” No payment/address entry, order email, intake receipt, proof delivery, approval reply, refund or fulfillment was exercised.
- Empty Keep It Organized showed Browse available products with no filter blame. Catalog maximum $1 showed 0 of 10 and remove-filter guidance. Nonsense search showed spelling/query guidance. Intentional 404 showed Continue shopping. Empty cart recovery present.
- Store display name read back as Teklo Studio through API. Home title and meta description read back from rendered DOM; canonical remains https://at3d.shop/.
- Product real-text h2 headings, $25 current delta, prelaunch status, return-policy link and new graphic alt text observed. Conflicting images absent from gallery.

## Configuration and intake

- Shopify plan remains Pause and Build. Payments screen says Shopify Payments is not processing transactions until plan selection; PayPal setup incomplete. No settings changed.
- General shipping profile covers all products; Flat Rate has zero products. General: domestic US free Economy at $35+, $3 Economy and calculated USPS; international carrier options with warning that 21 countries require inclusion in markets. These are configuration observations, not verified checkout rates or worldwide coverage.
- Notifications sender sales@at3d.shop reports Email domain authentication Needs setup. Customer notification templates accessible. No delivery or monitored mailbox verified. Order-confirmation insert prepared, not installed. No recipient or DNS change.
- Existing Jotform submission preserved, not inspected. Public form now exposes Shopify identity, required email/reference/unit/finish/accent, optional medal evidence, all four route paths and explicit hold/no-response text. Final GPX upload has no required validation; finish time optional. Piece number still has step any/no minimum despite multiple builder requests: operator must reject invalid unit against Shopify quantity; UI constraint remains release work. No real route or customer data submitted. Upload/storage/notification success NOT tested.
- Existing app inventory read; app settings, automation execution, pixel receipt, consent accept/decline and purchase deduplication NOT verified. No app disabled/uninstalled. No LCP/INP/CLS or performance improvement claim.

## Required remaining acceptance tests

Full 360/390 touch/device/zoom and screen-reader checks; Gallery cart, sold-out/unavailable options, cart quantity/stock boundaries, image modal, forms success/receipt/newsletter duplicates, analytics event receipt and consent, real mobile performance. Original audit passes are not silently promoted to new regression passes. Execute paid-plan-dependent test-mode order through refund and per-piece intake/proof approval after approved facts, sender and test destination are available.
