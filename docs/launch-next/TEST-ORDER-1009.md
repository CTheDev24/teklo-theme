# Test order #1009 and shipping-discount correction

22 September 2026, America/Chicago. Exact unpublished theme 196729798822; no publication.

## Verified checkout outcome

Merchant activated Basic, confirmed Shopify Payments test mode, and supplied an authorized Chandler, Arizona apartment address. The street/unit are deliberately omitted from repository evidence.

- Order #1009, Shopify ID 13000741421222; confirmation 2I4UD5A6X.
- Shopify independently reports test=true, PAID, UNFULFILLED, no fulfillments.
- Two distinct quantity-one lines: TEKLO-TEST-A, Gallery/Signal Orange, $149.95; TEKLO-TEST-B, Nocturne/Match My Medal Color, $174.95.
- Line-item references and separate test gift notes survived into Shopify customAttributes. The order-level DO NOT PRODUCE/FULFILL/BUY LABEL note also persisted.
- Subtotal $324.90; Priority Mail $8.07; total $332.97 USD. Ground Advantage also quoted $8.25 for the same two-piece basket/address. No general free-shipping threshold applied after the discount fix below.
- Order totalTax is $0.00. This records Shopify's calculation; merchant tax registrations/settings and tax correctness are not signed off. Other states, non-US exclusions and mixed-product baskets remain untested.
- Shopify Payments AUTHORIZATION 14746189398182 and CAPTURE 14746189562022 both SUCCESS and test=true, each $332.97. Only Shopify's published synthetic Visa 4242 number was used; no real card or express wallet used.
- On-screen confirmation showed support@teklostudio.com. Marketing and saved-account opt-ins were left off. Actual order-confirmation mailbox receipt and Trace intake instructions are awaiting merchant verification; the thank-you screen is not email evidence.

The order completed once. It remains an unfulfilled test; do not produce or buy labels. A preview-bar overlay initially covered the cart drawer checkout control. Hiding that preview-only bar allowed normal navigation; no theme change was needed. Browser accessibility snapshots omitted the email value, so it was corrected and verified visually before submission; final Shopify order contact is exactly support@teklostudio.com.

## Applied Shopify correction: old automatic free shipping

Checkout revealed FREESHIPPING reducing both USPS rates to zero, despite the instruction to keep discounts disabled. Fresh discountNodes query identified the one active rule:

- ID gid://shopify/DiscountAutomaticNode/1648508928166
- Type DiscountAutomaticFreeShipping, title FREESHIPPING
- Before: ACTIVE, startsAt 2024-12-20T01:30:02Z, endsAt null.
- Applied discountAutomaticDeactivate; no user errors. After: EXPIRED, unchanged startsAt, endsAt 2026-09-23T04:15:13Z.
- Fresh active-discount query returned zero nodes with hasNextPage=false. Reloaded checkout showed Priority $8.07 / Ground $8.25 with no FREESHIPPING allocation.

Rollback only if merchant later explicitly requests the promotion: inspect the retained rule and intervening changes, then reactivate this exact rule in Shopify Discounts (or restore its prior endsAt=null using the appropriate validated update). This would restore the undesired shipping promotion, so it is not a launch step. Rule was not deleted; its other configuration was not edited. Reverting documentation cannot undo this Shopify change. Existing General-profile free Economy rate is a separate shipping rate, not this discount, and was not changed.

## Agent cancellation attempt: blocked; merchant subsequently canceled

Full cancellation/refund/restock with notice to the same merchant test mailbox was prepared for only #1009. First attempt failed automatic approval review because of a usage limit and explicitly did not execute. After the merchant said Continue, a fresh read confirmed test=true, cancelledAt=null, PAID/UNFULFILLED. Retry was refused by the Shopify connector safety policy: order cancellation/capture operations are restricted because they can move funds and trigger irreversible refund, restocking and notification changes. No alternate tool was used to bypass that restriction.

The read immediately after the blocked attempt showed only successful test AUTHORIZATION/CAPTURE and PAID/UNFULFILLED. This historical state is superseded by the merchant cancellation below.

Merchant confirmed cancellation with refund and restock selected. Independent Shopify read confirms cancelledAt **2026-09-23T04:29:00Z** (22 September locally), no fulfillment, and refund **1204504559782**. Both line items (37408769147046 / TEKLO-TEST-B and 37408769179814 / TEKLO-TEST-A), quantity one each, report restockType=CANCEL and restocked=true.

The refund transaction is **test=true, REFUND, PENDING, $332.97 USD** through shopify_payments. A second read after 20 seconds confirms the same pending transaction; totalRefundedSet remains $0 and displayFinancialStatus remains PAID. This is processing, not a failed or completed refund. Do not submit another refund or cancellation. Recheck this same order/refund until a terminal result is known; require SUCCESS and the expected full amount before marking the refund test passed. Cancellation and restocking have passed independently of the pending financial result.

## Remaining acceptance

P0-01: old plan rejection resolved; two-piece checkout and simulated capture passed for one Arizona destination. Cancellation and both restocks are verified; refund completion, actual confirmation delivery, other launch destinations and tax configuration remain open. P0-03: order/piece properties passed, but no intake or proof approval was performed for #1009. The full workflow and production-release controls remain unsigned off. Overall NOT READY.

Test mode is still merchant-controlled and has not been turned off by the agent. Turn it off before accepting real orders after the test campaign and release review are complete.
