# Teklo pre-launch implementation — 21 September 2026

**Status: NOT READY.** This is an implemented draft with explicit remaining gates, not a launch approval. No theme publication, paid commitment, payment activation, real-card charge, customer contact or order fulfillment occurred.

Branch: `codex/fix/prelaunch-readiness`, based on `origin/dev` at `bac9539`.
Target: unpublished `teklo-theme/dev`, **196729798822**. The similarly named theme and live theme were not substituted.
Preview: https://at3dshop.myshopify.com/?preview_theme_id=196729798822
Product: https://at3dshop.myshopify.com/products/personalized-3d-race-map-custom-gpx-running-wall-art-marathon-finisher-gift?preview_theme_id=196729798822
Collection: https://at3dshop.myshopify.com/collections/trace?preview_theme_id=196729798822

## Findings matrix

| ID | Owner | Implemented and evidence | Remaining disposition |
|---|---|---|---|
| P0-01 | Shopify billing/payments | Revalidated Pause and Build through connected Shopify. No paid or payment settings changed. | **Necessary human review:** active selling plan, gateway/test mode and launch markets. Checkout/payment/shipping/tax/confirmation/refund cannot pass on the paused plan. |
| P0-02 | Theme + Shopify collection | Created manual Trace collection 693016101030 with launch product only. Shop links there; Trace, Explore and Discover link to product. Customize Trace and live minimum price rendered ($149.95 USD). | **Fixed/tested** homepage navigation/price; final release review remains. |
| P0-03 | Theme + Jotform + notifications + operations | Product form captures visible per-piece reference and gift note; client validation runs before add. Two distinct references produce two cart lines. Existing form 262521531346047 now uses Shopify order identity and adds required email/reference/unit/finish/accent, medal input and explicit nonresponse hold. Offline route/proof gate and tests supplied. Etsy copy removed from Shopify description. | **Partial, blocked by integration verification:** Jotform receipt/upload and notifications not exercised; no verified sender/inbox/test recipient; Admin access recovered; sender sales@at3d.shop shows domain authentication Needs setup. Public GPX upload is now optional and all route alternatives visible; piece-number integer restriction did not persist despite builder success. Full workflow NOT passed. Launch copy and notification insert staged. |
| P1-01 | Shopify content/pricing | All eight variants read: six standard $149.95; Gallery and Nocturne medal-match $174.95. Description now states currently configured $25 before discounts. Variant prices unchanged. Browser Nocturne medal price/cart verified. | **Fixed factual conflict; pricing-intent review** still needed, including 25OFF. Gallery cart and remaining graphics not fully retested. |
| P1-02 | Shopify policies/shipping | Re-read policies; 7/14-day conflict and generic processing rules confirmed. General profile covers all products; Flat Rate has zero products. General has US Economy free at $35+, $3 Economy, and carrier rates; international zone warns 21 countries need a market. These settings do not prove checkout eligibility or worldwide service. Unverified production promises removed from pre-launch description and conflicting ordering/proof graphics detached. | **Staged necessary review:** explicit Trace production exception, proof window, damage window, rates/destinations and free-shipping eligibility. No shipping rates changed. |
| P1-03 | Shopify policies + mailbox | Placeholder and two different mailboxes confirmed. Product has direct native Contact link without promising a monitored address or response time. | **Staged necessary review:** choose and verify support inbox/test destination, then replace placeholders and standardize routes. No email receipt claimed. |
| P1-04 | Shopify content/policy | Product now marks custom-made change-of-mind exclusion from existing refund policy and links it; distinguishes policy coverage for damage/defects; states no retroactive change to existing orders. | **Partial; staged necessary review:** cancellation before/after approval still requires merchant decision. |
| P1-05 | Shopify content + theme | Conflicting measurements removed from homepage specs and pre-launch product text; dimension graphic detached, not deleted. | **Staged necessary review:** actual exterior width/height/depth, insert and raised-map size must be measured. No physical dimensions invented. |
| P1-06 | Policies + Jotform/Drive | Removed inaccessible retention-policy claim from product. No retention period or deletion automation invented. Existing Google Drive direct-folder contract inspected. | **Staged necessary review:** actual access, retention/deletion practice, terms exclusion and intake notice; apply/verify across Jotform, Drive, local files and proof copies. |
| P1-07 | Shopify product | Soft Face 15457467728038 set DRAFT; copied description preserved in backup. Excluded from Trace collection. | **Fixed by removal from sale**, specifications required before reactivation. |
| P2-01 | Shopify settings/content | Trace vendor and store display name changed to Teklo Studio; home title/description updated to Trace-focused copy; handles preserved. | **Partial:** social share image crop and remaining catalog vendor/SEO review deferred; no blanket vendor edits. Exact applied SEO values below. Other product vendors not blanket-changed. |
| P2-02 | Shopify media/content | Six graphics received meaningful alt text; new product description has h2 headings and real lists. Three conflicting graphics detached pending replacement. | **Implemented**, screen-reader interaction and final image/content consistency remain release tests. |
| P2-03 | Theme | Empty collection uses all_products_count to distinguish no inventory from filtered no-results, with Browse available products action. Existing filter-removal branch retained. | **Implemented**, final browser checks recorded in TEST-EVIDENCE.md. |
| P2-04 | External apps | App inventory inspected: Klaviyo, Hextom, Junip, Flow, Zapier and upsell apps present. No relevant app embed in theme settings; scripts cannot safely be disabled by theme code alone. | **Deferred/blocked:** app owner configuration and necessity review; app settings and event destinations were not verified. No uninstall or billing commitment. Mobile performance/analytics sign-off outstanding. |

## One consolidated review packet

Only the following require judgment or unavailable access. Do not treat the draft as launch-ready after approving copy alone.

1. **Paid selling plan and payments:** choose an active plan in Shopify; confirm gateway, test mode, currency and intended launch markets. Then run a test-mode order using an approved test identity/destination. No real card is necessary. Verify rates/tax, payment, confirmation, intake, proof/approval, cancellation/refund and inventory restoration.
2. **Mailbox and operations:** complete sender domain authentication (Shopify reports Needs setup), then confirm a monitored support/proof mailbox and an authorized test recipient (configured shop email is sales@at3d.shop; Contact policy says contact@at3d.net; neither has been receipt-tested). Choose a response expectation only after staffing is confirmed. Recommended operational behavior: manual proof delivery to the verified order email until automation is demonstrated, with each message identifying order, piece and proof revision. Do not enable staged email text until delivery/reply evidence is captured.
3. **Physical facts:** supply measured exterior frame width × height × depth, poster/insert dimensions and raised-map dimensions. Existing competing figures are evidence of ambiguity, not a basis for selecting a measurement. Confirm any photographed medal is a styling prop versus included item before revising imagery.
4. **Commercial/policy choices:** retain the current $25 medal delta or explicitly authorize $29 (then set only the two medal variants to $178.95, leaving six standard variants at $149.95). Decide whether active automatic discount 25OFF (ID 1666621571238, 25% entire order, minimum quantity two) applies to Trace/medal matching. Recommended interim action: keep all existing prices/discounts until confirmed. Confirm proof turnaround; whether existing 10–14 business days after approval is operationally accurate; one damage-reporting window (existing product promised 14, policies say 7); supported destinations; free-shipping eligibility/exclusions; cancellation before/after approval. Preserve earlier order terms.
5. **Route data:** identify who can access files, actual service providers, retention trigger/period, backup deletion limits and deletion-request route. Approve the narrow exclusion below from broad submission reuse. No new retention duration is proposed as an established practice.
6. **Final release:** review draft PR/content, repaired mobile menu, full browser/device matrix, app selection, analytics consent/event receipt and mobile performance. Publish only after these gates and purchasing/intake tests pass.

## Exact prepared copy/configuration (NOT deployed)

### Shop and home SEO (text applied; social image staged)

- Shop display name: `Teklo Studio` (billing/legal entity remains separate).
- Home page title: `Teklo Studio | Trace Personalized Race Artwork`.
- Home description: `Discover Trace by Teklo Studio: personalized dimensional race artwork in Gallery and Nocturne finishes. Explore the studio and custom design work.`
- Social image: use existing Trace lead photograph from `before-product-15807121490086.json`; verify crop and approve preview. Keep current product handles/canonicals.

### Shipping exception, pending capability confirmation

> Trace is made to order. Its production time begins after complete, usable route information and written approval of the identified proof. The general 1–3 business-day processing statement does not apply to Trace. Proof preparation, production and carrier transit are separate stages. [CONFIRMED PROOF WINDOW]. [CONFIRMED PRODUCTION WINDOW] after written approval. [CONFIRMED TRANSIT/RATE/DESTINATION RULE]. [EXPLICIT FREE-SHIPPING ELIGIBILITY].

### Damage/cancellation/support, pending business approval

> Report transit damage within [ONE APPROVED WINDOW] of delivery through [VERIFIED CONTACT ROUTE]. Include photos of the artwork, carton, packaging and shipping label. Keep packaging until the issue is resolved.

> Trace is custom-made and is not eligible for change-of-mind returns. This does not exclude the remedies for damaged or defective items described in our refund policy. Before proof approval: [APPROVED CANCELLATION RULE]. After proof approval: [APPROVED CANCELLATION RULE]. These terms apply to orders placed on or after [EFFECTIVE DATE]; earlier order terms remain unchanged.

Replace each `[support email]` only after mailbox verification. Use `<a href="mailto:VERIFIED_ADDRESS">VERIFIED_ADDRESS</a>` in shipping/refund/contact policies. Contact page and Trace: `Questions about your order or route? Contact [VERIFIED_ADDRESS]. [CONFIRMED RESPONSE EXPECTATION].` Bracketed values are internal review tokens, never customer copy.

### Route policy and submission-terms exclusion, pending practice review

> Private route files, activity links, course submissions, medal photos and order personalization submitted for fulfillment are excluded from the broad reuse permission for general feedback and public submissions. They may be used to prepare, proof and fulfill the ordered artwork, subject to the route-data notice.

Route-data notice must enumerate Jotform intake, Drive transfer, local production/proof files, authorized access, purpose, precise-location sensitivity, deletion contact, retention trigger/duration and backup limitations. Fill from actual practice; do not promise automatic deletion until configured and tested. Link this notice from Trace and intake before inviting route upload.

### Full launch handoff text, pending end-to-end test

> After payment, complete one [Trace intake form](https://form.jotform.com/262521531346047) for each physical piece. Use your Shopify order number, order email, piece reference and unit number. Supply a GPX file, accessible activity link, official-course details or course map. A submitted form is not production approval. We will deliver the identified proof to [VERIFIED ORDER-EMAIL CHANNEL]. Check the route, spelling, layout, finish and accent. Reply with the order, piece reference/unit and proof version plus “APPROVED FOR PRODUCTION,” or send one consolidated correction request. Missing/invalid input, inaccessible links, uncertain courses or colors require clarification; no response keeps production on hold. [CONFIRMED FOLLOW-UP/CANCELLATION RULE].

Use the same approved text next to the purchase button, in the product description, the order confirmation and intake acknowledgment. `order-confirmation-insert.liquid` is prepared but NOT installed.

## Smallest remaining rollout backlog

1. Approve facts and terms; authenticate the sender domain and verify mailbox/test recipient.
2. Finish and test Jotform upload/receipt and private per-piece reconciliation, proof sending/replies and nonresponse queue; install tested order-email insert. Offline tests alone cannot close P0-03.
3. Activate the chosen plan and payment test mode; exercise full order/shipping/tax/refund flow and verify discount scope.
4. Apply approved policies/SEO, replace held graphics and configure app/pixel requirements.
5. Finish device/accessibility/analytics/performance tests, review PR, merge to dev, separately approve publication.

## Approval-review rejection

Automatic approval review rejected the first partial product-description update because it retained unverified Etsy intake/proof and route-policy promises. It was not bypassed. A safer complete pre-launch description, removing those promises and disclosing the unresolved workflow, subsequently succeeded. The full launch wording remains staged for the factual/business gates above.

## Configuration verification addendum

Shopify Payments explicitly reports it is not processing transactions until a plan is selected. PayPal setup is incomplete. Neither was activated. Admin access recovered after the initial 500; it is not a blanket access blocker. No customer or test email was sent. General profile settings advertise US Economy free for orders $35+, $3 Economy, USPS services and international carrier services, but 21 international countries are outside enabled markets. Checkout verification remains required before claiming eligibility.

Shopify GitHub integration mirrored draft uploads onto dev during this task. The implementation branch retains its own commits and reconciles those sync commits; the PR explains which changes are already mirrored. No direct git push to dev occurred.
