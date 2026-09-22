# Policy implementation — 22 September 2026

## Applied and verified

- Shopify Trace product 15807121490086: approved 48-hour first-proof preparation after complete usable intake, 8–10 business-day production after written approval, separate 48-hour response clocks, 48-hour/day-7 reminders, day-10 unapproved-order full refund, cancellation boundaries and seven-calendar-day shipping-damage reporting. Existing order terms preserved. Product retains pre-launch NOT READY disclosure; no proof automation claim. API readback exactly matches prepared HTML.
- Shopify refund policy: prospective Trace exception with approved cancellation, response and damage terms; original general return provisions preserved. Admin UI saved; independent API readback matches prepared HTML except a TinyMCE link metadata attribute. Complete original content retained.
- Jotform: intake paragraph and success-page copy saved/reloaded. See INTAKE-POLICY-CHANGES.md. Notifications remain orders@. No new submission/email sent this turn.
- Discount 25OFF, AutomaticNode/1666621571238: old active, unlimited-duration, minimum-two-item promotion deactivated pending actual launch. Readback EXPIRED, endsAt 2026-09-22T05:24:16Z; original startsAt 2025-02-22T04:37:05Z, original endsAt null. No launch clock started. Existing 25% and minimum-two scope remain in the inactive record until clarified/configured.
- Local manual operations: deadline queue with fixed first-proof clock, separate request/proof clocks, reminders, cancellation/refund review and delivery/cancellation +14-day deletion checklist. No automated email, refund, cancellation, deletion or production. 22 synthetic tests pass.

- Shopify shipping policy: saved complete Trace exception for 48-hour first proof, 8–10-business-day production, seven-day shipping damage, domestic-only launch and no assumed free-shipping promotion; original general sections retained. Independent normalized text readback exactly matches approved body.
- Shopify Terms: saved prospective Trace cancellation/response rules and narrow private-route exclusion from broad submission reuse; sole studio operator/provider processing distinction and separate marketing permission. Independent readback matches approved body apart from editor metadata.

## Prepared, not applied

- Exact applied policy bodies are refund_policy-approved.html, shipping_policy-approved.html and terms_of_service-approved.html, with before/after JSON backup. Connector lacks write_legal_policies; authenticated Admin UI ultimately recovered and all three writes completed. No new login is required for those completed edits. Automated privacy body was preserved.
- Privacy/retention: merchant approved sole studio operator, separate marketing permission, 14-day active-file/route-bearing-copy target after delivery or cancellation. Provider storage/trash/backups and actual deletion have not been verified. Keep automatic Shopify privacy enabled. Do not publish an unconditional provider deletion guarantee. Manual queue supports review, not actual provider deletion.
- Order confirmation insert updated to the approved timelines/cancellation terms, still staged, not installed. End-to-end Shopify notification delivery remains a test gate.
- Shipping configuration: Trace remains in General profile 93564829862 with Domestic and International zones. Existing domestic method names are Economy, usps, Economy; names alone do not prove standard/priority rates or services. Empty Flat Rate profile 93565550758 has usps/Standard methods. Exact geography, prices/services and checkout behavior must be established before moving Trace or promising configured options. No profile changed.
- Promotion: merchant approved 25OFF for a single-piece purchase and a maximum 30-day window beginning on actual launch. Clarification pending whether discount covers all eligible pieces or only one per order. Do not infer a launch date or activate today. Configure start at release timestamp and end exactly 30 days later, then test one/two pieces and medal matching before launch.
- Automated return/cancellation rules: Admin currently shows Default rules, 14-day returns, no cancellation rules. Written Trace policy does not configure self-serve returns or approval-aware cancellation. Inspect available per-product rules before enabling such self-service; do not claim alignment from this text change alone.

## Rollback

- Product/refund/shipping/terms: use policy-implementation-backup-2026-09-22.json before values, but first compare current content and preserve intervening merchant edits. Revert only this batch's changes; never change earlier customers' terms retroactively.
- Discount: original record was ACTIVE, startsAt 2025-02-22T04:37:05Z, endsAt null, 25% entire order/minimum quantity2. Restoring those dates/activation restores the old promotion, so do so only if intentionally rolling back launch timing. Do not automatically reactivate on a code revert.
- Jotform: targeted before text and rollback in INTAKE-POLICY-CHANGES.md. Do not restore whole form revisions.
- Queue: revert local code or stop using it; preserve private ledger receipts and reconcile new policy metadata. No provider actions are undone. No existing customer files were deleted.

## Validation and remaining gates

GraphQL operations validated before execution; product exact readback and full refund readback verified. Shipping/terms full text readback confirmed. Discount EXPIRED confirmed. Python22 tests and diff whitespace check pass. No theme files changed in this batch, so no theme deployment or new Theme Check result is claimed; prior0-error/10-warning baseline remains historical. No paid plan, payment, real-card charge, theme publication or customer contact occurred. Real proof delivery/approval, scheduled reminders, actual refund, provider deletion, shipping checkout and final release checks remain untested. Overall **NOT READY**.
