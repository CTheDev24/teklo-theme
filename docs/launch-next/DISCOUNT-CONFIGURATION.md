# Launch discount — one piece per order

Merchant clarification, 22 September 2026: **25% off one Trace piece per order**, including medal matching; launch window begins on the actual launch date and lasts 30 days. This is not a one-item order limit and not a once-per-customer rule.

## Verified result

Existing automatic 25OFF (1666621571238) remains EXPIRED. It still contains the old 25%-off-entire-order/minimum-two rule and must not be reactivated. An attempted inactive update to Trace-only, minimum one and discounted quantity one was rejected by Shopify: "discountOnQuantity field is only permitted with bxgy discounts." Independent readback confirms no change. Evidence: discount-scope-evidence-2026-09-22.json.

The native amount-off percentage rule cannot represent this cap. Do not substitute a fixed $37.49 saving: it would not equal 25% of the $174.95 medal variant. Do not substitute Buy X Get Y, restrict the cart to one item, or implement a browser-only discount.

Installed app inventory includes Hextom Sales Boost, AI Bundles & Upsells and AOV.ai Bundle. Their accessible documentation does not establish this exact single-unit automatic rule in the installed plans. The connector reports no Functions owned by its API client; that does not prove other installed apps have no Functions. Chrome app-settings inspection timed out, so existing app capability remains unverified.

## Concrete paid-app review

[Steppun Discount](https://apps.shopify.com/steppun-discount) explicitly supports percentage discounts capped by quantity, automatic discounts, product targeting and start/end schedules. Listing checked 22 September 2026: **USD6.99/month**, seven-day trial, recurring billing every30days. Not installed; no trial or subscription started. Listed access includes customer name/email, product/collection data, discounts, locations/Markets and store-owner contact data. Review actual consent and billing before authorizing.

Prepared configuration:
- Automatic campaign title: 25OFF.
- Eligibility: Trace product15807121490086, all eight variants, including Match My Medal Color; minimum one eligible unit.
- Benefit:25% off at most **one unit across the entire order**, including split cart lines and different personalization.
- Additional units remain full price; unrelated products receive no discount.
- No extra once-per-customer or order-quantity restriction.
- Keep inactive while preparing. Start at approved actual launch timestamp; end exactly30days later, with Shopify shop timezone shown in release record.
- Preserve current combination restrictions unless separately approved. No free-shipping promotion.
- For mixed-price Trace units, proposed deterministic selection is the highest-priced eligible unit (customer-favorable); verify and record app allocation behavior before activation. Do not silently claim a particular mixed-cart allocation until tested.

Only the app commitment requires merchant approval here. If an already-paid installed app proves capable of this exact rule, use it without a new commitment. A private custom Function is not a straightforward alternative on the current non-Plus store: Shopify documents custom-app Functions as Plus-only; public-app Functions are available across plans.

## Required activation tests — not yet run

| Cart | Expected discount |
|---|---|
| One $149.95 Trace | $37.49; merchandise $112.46 |
| One $174.95 medal Trace | $43.74; merchandise $131.21 |
| Two identical $149.95 units on one line | $37.49 total; merchandise $262.41 |
| Two identical units split by personalization | Same single $37.49 total |
| Two $174.95 medal units | $43.74 total; merchandise $306.16 |
| Mixed standard + medal | Exactly one unit discounted; allocation checked against chosen app rule |
| Trace plus another product | Only one Trace unit discounted |
| No Trace | No 25OFF |
| Before start / at expiry | No 25OFF |

Also verify discount stacking, cart edit/remove/re-add, accelerated checkout, tax/shipping unchanged by any theme trick, and midnight/timezone boundaries. Dollar examples assume USD current prices and Shopify cent rounding; checkout evidence is mandatory. No active promotion or checkout pass is claimed.

## Rollback

No discount mutation succeeded in this batch, so there is no configuration change to undo. Retain the expired legacy promotion. If a future app rule is introduced, deactivate that rule and independently confirm no 25OFF in one/two-piece carts; do not reactivate the old entire-order discount. Uninstalling an app does not by itself prove every discount is disabled; verify Admin and checkout separately.

Sources: [Shopify amount-off rules](https://help.shopify.com/en/manual/discounts/discount-types/percentage-fixed-amount), [Function availability](https://shopify.dev/docs/apps/build/functions), and the app listing above.
