# Merchant policy decisions — 22 September 2026

This records merchant decisions and concrete proposed wording. It is not a claim that Shopify policies, rates, discounts, notifications or storage settings have changed. Applies prospectively; preserve existing order terms. Overall launch remains NOT READY.

## Confirmed decisions

- Trace production: 8–10 business days after written proof approval and complete usable intake. First-proof preparation time was not supplied.
- Damage reporting: 7 days after delivery. Keep damage/defect remedies distinct from change-of-mind exclusions; do not silently convert all defect remedies into a seven-day limitation.
- Custom-made change-of-mind returns remain excluded. Cancellation permitted until written approval; no cancellation once production starts. Changes may be allowed at seller discretion. Refund amount before approval and treatment of the approval-to-production interval need explicit resolution.
- Launch shipping: domestic US; standard and priority options. Exact territories, services and rates require configuration verification. Free shipping is a possible promotion, not yet approved or configured. Priority shipping does not inherently accelerate production.
- Merchant is the only intended human operator accessing routes/uploads. Services still store/process the data; do not publish an absolute claim that no provider has access.
- Customer-submitted files: merchant prefers deletion 14 days after delivery. Actual provider, local, trash and backup handling must be verified before an absolute deletion promise. Canceled/unfulfilled orders need a separate trigger.
- Intake and proof responses requested within 48 hours. Proposed separate clocks: order confirmation/intake instructions for intake; each proof delivery for proof feedback. Merchant requested refund after 10 days without a response, while asking whether a sent proof could be produced without approval. Recommendation: never produce without explicit written approval.
- Keep $25 medal-match upsell. Include Trace and medal matching in 25OFF relaunch promotion for no more than 30 days. Launch date/start/end and existing minimum-two-item condition remain to be settled; do not silently broaden to single-piece orders or restart an already-running promotion.

## Prepared customer copy

### Production and shipping (confirmed core; rates/coverage still gated)

> Trace is made to order. Production takes 8–10 business days after we receive complete, usable customization details and your written approval of the proof for your piece. The general 1–3-business-day processing window does not apply to Trace. Proof preparation and carrier transit are separate from production. Choosing priority shipping does not shorten production time.

Add domestic coverage and standard/priority checkout options only after actual shipping profiles are configured and tested. Do not advertise free shipping before the promotion is explicitly approved and configured. First-proof turnaround remains a missing operational commitment.

### Damage and returns

> Trace is custom-made and is not eligible for change-of-mind returns. This does not exclude the remedies for damaged or defective items described in our refund policy. Report shipping damage to support@teklostudio.com within 7 days after delivery and include your order number and photos of the item and packaging.

### Cancellation — proposed resolution of the approval/production gap

> You may cancel for a full refund before giving written approval of your proof. Written approval authorizes production, so cancellation is no longer guaranteed after approval. Once production starts, the order cannot be canceled. Requests for changes after approval may be considered at our discretion and must be accepted by us before they take effect.

The full-refund amount and treatment between approval and actual production are proposed, not yet merchant-confirmed. Keep any changes prospective.

### Response deadlines — proposal requiring confirmation

> Complete intake within 48 hours after receiving your order confirmation and intake instructions. Respond to each proof within 48 hours after it is sent. If details are missing or a proof remains unanswered, production stays on hold. No response is not approval. If we receive no response for 10 calendar days after the relevant intake request or proof message, we will cancel the unapproved order and issue a full refund.

Operational proposal: reminder at 48 hours, final reminder on day 7, manual cancellation/refund review on day 10. Each relevant request has its own clock; do not cancel ten days after purchase when the seller has not yet delivered the proof. An actual reply requiring clarification is not silence and must be handled individually. No timer, reminder or refund automation is implemented by this document.

### Route privacy — proposed operational scope

> Customer routes and uploads are used to prepare, proof and fulfill your order. The studio owner is the only authorized studio operator accessing these files. Our form and storage providers process them to provide their services. Private routes, activity links, course submissions, medal photos and personalization are excluded from the broad reuse permission for public feedback. Any marketing use requires separate permission.

Proposed deletion target: remove submitted files and route-bearing working/proof copies from active Jotform, Drive and local storage 14 days after delivery; for canceled orders, 14 days after cancellation. Keep minimal order, payment and approval records separately, without unnecessary raw routes. Explain provider backup limitations only after verifying them; never promise that every backup is purged at day 14 without evidence. Marketing permission, derived-copy scope and canceled-order trigger require confirmation. A manual deletion queue with completion evidence is acceptable; do not claim automation.

## Implementation map and rollback

- Shopify product, shipping/refund/terms policies and relevant graphics: align production/damage/cancellation copy. Snapshot current full bodies and graphics before writing. Reverse targeted changes only; do not overwrite later merchant edits or apply new terms retroactively.
- Shopify shipping profiles/markets: domestic coverage and standard/priority services; inspect current rates first. Snapshot destinations, rates and profile assignments for rollback. No free-shipping activation authorized yet.
- Shopify discount 25OFF: inspect current start/end, eligible products and minimum quantity before changes. Preserve original scope unless changed explicitly; enforce a maximum 30-day approved relaunch window. Snapshot original configuration for rollback.
- Jotform, order email, product and manual operations ledger: consistent separate response clocks and written approval requirement. Save prior templates/conditions and test through authorized destinations. Email wording is not an automation implementation.
- Jotform/Drive/local operations: verify sole studio operator access and provider processing, configure and exercise a deletion queue. Do not delete existing customer data or backups just to test this policy; use synthetic fixtures. Data deletion cannot be rolled back by a theme revert.

## Remaining concise decisions

1. First-proof turnaround after complete valid intake.
2. Full refund before approval; cancellation after approval but before production (proposed discretionary exception).
3. Separate 48-hour clocks, day-7 final reminder and day-10 full refund; no production without written approval.
4. US coverage (contiguous 48 vs all 50 states, DC, territories/APO/FPO), exact promo start/end, and whether 25OFF retains its existing two-item minimum.
5. Retention scope/canceled-order trigger and separate marketing permission as proposed, subject to provider verification.

## Approval and implementation follow-up

Merchant approved the proposed cancellation/refund, response-deadline and privacy wording, specified first proof within 48 hours after complete usable intake, and authorized implementation. The promotion's 30-day window starts on actual launch. Geographic answer was ambiguous and discount unit scope needs clarification; neither is inferred. Implementation status and exact external changes are in POLICY-IMPLEMENTATION.md, which supersedes the earlier staged-only status here.
