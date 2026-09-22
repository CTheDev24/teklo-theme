# Storefront verification — 21 September 2026

## Post-deployment controlled-width follow-up

Root recovered through the in-app browser after the Chrome failures recorded below. This supersedes only the width-testing limitation for these sampled interactions, not real-device/touch sign-off.

- Exact preview opened with `teklo-theme/dev Draft` bar. At 360×800, DOM `innerWidth` was 360 and document scroll width 345 (no observed horizontal overflow on homepage). Menu opened; Escape closed it and focus returned to Menu with `aria-expanded=false`.
- At 360px, visible Style/Route Color labels selected Nocturne and Match My Medal Color; rendered price was $174.95. Clicking Add to cart with blank Piece reference focused the invalid field and displayed `Please fill out this field.` Starting cart was independently empty.
- At 390×844, a fresh Gallery/Signal Orange product view accepted synthetic reference `QA-NEXT-390`. Add to cart opened the drawer with that exact property and $149.95. Increasing to 2 produced $299.90 subtotal, automatic 25OFF −$74.97 and $224.93 total. Reload retained two units and the reference. Removed only this synthetic line; final drawer explicitly showed `Your cart is empty` and Continue shopping. No checkout or form submission occurred.
- The first 360px cart attempt after opening the empty drawer unexpectedly navigated to the catalog, leaving cart empty. A fresh product view at 390px completed the successful add above. This may reflect an overlay/action timing issue; do not count the initial attempt as passed or infer a resolved cart bug.
- Screenshot at 390px showed readable item/options/reference and quantity controls in the drawer. Check out exists in its DOM, but preview-bar overlap/below-fold positioning and tool timeouts prevented a reliable visibility/scrolling pass. Checkout visibility and drawer scrolling remain required release tests.
- Default viewport restored. These were mouse/keyboard actions at controlled CSS widths, not touch, mobile OS keyboard, Safari/Android, 200% zoom or a full screen-reader pass. Image modal/Escape desktop evidence remains separate. No mobile performance or analytics receipt claim.

Read-only browser pass on the existing draft, before this branch's deployment. No cart mutation, customer submission, email, payment, configuration change or publication occurred in this subtask. Existing review packet and test evidence were read; no AGENTS.md was found in the worktree file inventory.

## Exact target and observed results

- Opened `https://at3dshop.myshopify.com/?preview_theme_id=196729798822`, redirected to `https://at3d.shop/`. Rendered page script explicitly identified `Shopify.theme` as name `teklo-theme/dev`, ID `196729798822`, role `unpublished`. Chrome viewport was 1295 × 767 CSS pixels.
- Homepage Shop points to `/collections/trace`; Trace, Explore Trace, Discover Trace and Customize Trace point to the intended product. Starting price reads **From $149.95 USD**. Header Trace navigation reached the product. No change to the cart was needed.
- Gallery / Signal Orange initially displayed **$149.95 USD**. Choosing Match My Medal Color retained Gallery and displayed **$174.95 USD**, variant `57452337496230`. Real-text description states current $25 delta. This verifies the product selection/price, not Gallery cart totals or discount behavior.
- Product image modal opened through “Open media 1 in modal.” Escape closed it and returned focus to the same trigger. Full screen-reader and focus-trap traversal were not exercised.
- `/collections/keep-it-organized?preview_theme_id=196729798822` showed **0 products** and **Browse available products**, linked to `/collections/all`, without blaming filters.
- Header search for synthetic query `teklo-qa-noresult-20260921` returned “No results found” with spelling/different-word guidance.
- Intentional `/pages/teklo-qa-missing-20260921?preview_theme_id=196729798822` returned 404 / Page not found / Continue shopping to `/collections/all`.

## Current gallery findings requiring action

The product now has **13 gallery images**. Every rendered thumbnail/modal alternative was the generic product title. This differs from the previous audit implementation's media set; previous alt-text corrections do not prove these replacement images are accessible. Images below were inspected visually through their actual rendered CDN URLs, not inferred from filenames.

| Gallery position / filename | Proposed concise alternative grounded in image | Content limitation or contradiction |
|---|---|---|
| 1 `Trace-Listing_Graphics_-_YOUR_TRACE.png` | Framed Gallery Trace sample with raised city buildings, orange route and personalized race poster. | Fine print says sample shown for styling/detail; final product ships in black shadow-box frame. |
| 2 `Trace-Listing_Graphics_-_WHAT_YOU_LL_RECEIVE.png` | Assembled Trace with black glazed shadow-box frame, custom race poster and mounted 3D race map. | No dimensions shown. |
| 4 `Trace-Listing_Graphics_-_Choose_Your_Style.png` | Gallery light finish and Nocturne dark finish shown side by side with orange routes. | Matches current finish options. |
| 5 `Choose_your_accent.png` | Route accent samples in Signal Orange, Pulse Pink, Volt Lime and Graphite/Stone on a Gallery map. | **Graphite/Stone is pictured but is not a selectable variant.** Current fourth option is Match My Medal Color. Do not disguise the discrepancy through alt text. |
| 6 `Trace-Listing_Graphics_-_YOUR_ROUTE_GIVEN_DIMENSION.png` | Close-up of raised light-colored city buildings and an orange race route in a Trace frame. | No specific measured dimensions asserted. |
| 7 `Trace-Listing_Graphics_-_SEE_THE_DEPTH.png` | Low-angle view of the raised city, elevated orange route and race poster inside a black frame. | Styling/detail sample fine print. |
| 8 `Trace-Listing_Graphics_-_HOW_IT_WORKS.png` | Trace ordering steps: choose options, send route, review proof, approve production and display artwork. | **Promises 8–10 days for production**, conflicting with unresolved older policy/production statements. Alt text alone cannot correct the graphic. |
| 9 `Trace-Listing_Graphics_-_SEND_US_YOUR_ROUTE.png` | Route submission options: GPX upload after checkout, public activity link or official race-course map; no passwords needed. | Post-checkout upload promise remains dependent on the full tested Trace workflow. Lists Strava, Garmin, COROS and Suunto. |
| 10 `Trace-Listing_Graphics_-_SEE_IT_BEFORE_WE_BUILD_IT.png` | Proof process: Teklo designs, customer checks route and custom details, then approves before production. | Does not identify delivery or approval channel; cannot close P0-03. |
| 11 `Trace-Listing_Graphics_-_Dimensions_Materials.png` | Diagram labels the frame as 12.5 inches wide, 15 inches high and 2.4 inches deep, and the 3D map as 8 by 10 inches. | These are **graphic assertions, not verified physical measurements**. Insert dimensions absent; contradicts page's “being confirmed” status. Hold until merchant measurement confirmation. |
| 12 `Trace-Listing_Graphics_-_QUESTIONS.png` | Questions about routes, GPX, customization and race courses; graphic directs customers to Etsy Messages. | **Explicit “MESSAGE US ON ETSY” remains**, a P0-03 regression in replacement media. Replace/hold this graphic; do not merely omit Etsy from alt. |

After browser recovery, the remaining photos were visually verified: image 3 (`6E225F15-750C-4835-9E81-9D11ECCD1564.jpg`) can use “Nocturne Houston 5K and Gallery Pennant 10K Trace samples displayed side by side in black frames.” Image 13 (`IMG-0423.png`) can use “Framed Gallery Pennant 10K Trace with raised city map and orange route displayed beside a plant.” All thirteen visual mappings were sent to the implementation agent for alt-only changes. Newly uploaded graphics are preserved for merchant review; their factual conflicts are not silently overwritten.

## Apps, analytics and consent

Rendered product script sources included Junip (`widgets.juniphq.com/v1/junip_shopify.js`), Hextom (`cdn.hextom.com/js/ultimatesalesboost.js` and `usb-productPageCore.js`), and Shopify web pixel `899285158`. Script URLs used shop alias `1zbzxv-pc.myshopify.com` for Junip/Hextom. This is an observation, not proof of incorrect configuration.

No LimeSpot script matched the inspected current script-source inventory. This does **not** prove it is disabled everywhere or resolve its app configuration. Retrieved warning/error sample was dominated by browser-extension MetaMask/AdBlock connection and listener warnings; those must not be attributed to the theme. No current LimeSpot warning was captured in that bounded sample.

No consent dialog appeared in the snapshots. Existing browser consent state and customer market were not reset or independently established. No analytics destination, event receipt, consent enforcement or purchase deduplication pass is claimed. Resolve these through Shopify pixel testing and destination diagnostics; do not introduce duplicate theme event emitters merely because current receipt is unverified.

## Limits

Browser control intermittently timed out, including navigation and one image inspection. Successful subsequent state checks underpin only the results explicitly recorded above. Browser viewport capability exists, but no override was applied to avoid interfering with parallel agents. No 360/390px, touch, iPhone/Android, 200% zoom, real keyboard appearance, performance/Core Web Vitals, checkout, email, form-success or post-payment test is claimed here. Nocturne/cart/quantity/persistence, sold-out variants and filtered collection zero-results were not re-exercised in this read-only pass.

## Controlled mobile attempt (same session follow-up)

After parallel desktop work finished, the browser viewport capability documentation was read. It supports width/height override only; no touch/device emulation API was exposed. A 360 x 800 override call returned successfully, but the new Chrome test tab failed with debugger-not-attached before the page could be inspected. Rebinding that tab also failed. The in-app-browser fallback reported unavailable. A fresh Chrome tab could be created; resetting the viewport then returned successfully before the following storefront navigation timed out. Its DOM read also timed out.

Consequently, neither an actual measured 360px viewport nor 390px interactions were verified. Mobile menu/focus, variants, zoom, cart drawer scrolling/checkout visibility, add/remove and empty-cart recovery remain untested in this follow-up. No cart mutation occurred. No responsive or touch pass is claimed. The temporary viewport override was reset through the supported API after obtaining a fresh tab. Retry these checks when the browser control connection is healthy; no theme defect can be inferred from these tool failures.
