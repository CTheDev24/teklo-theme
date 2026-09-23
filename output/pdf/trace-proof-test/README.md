# Synthetic proof delivery test packet

TEST ONLY. These files do not represent a Shopify order and must never start production, fulfillment, refunds or customer messaging. All runner/race/route data is fictional. The three emails are unsent drafts addressed to the merchant's support@teklostudio.com mailbox, from orders@teklostudio.com. Nothing has been sent.

## Files

- piece-a-v1.eml: TEST-A, unit 1, v1, Gallery/Signal Orange, finish time 00:41:13.
- piece-b-v1.eml: TEST-B, unit 1, v1, Nocturne/Volt Lime, explicit finish-time omission.
- piece-a-v2.eml: revised TEST-A runner name and proof v2; requires separate new approval.
- Matching PDFs, plain-text email fallbacks and synthetic order.md imports are included.
- manifest.json records expected recipient, piece/unit/version, attachment SHA-256 and exact approval phrase.

## Merchant email-client verification still required

1. Open the two v1 EML files in your chosen mail app. Verify they are editable unsent drafts, From is your configured orders@ account, To is your own support@ mailbox, and each PDF opens correctly. If EML opens read-only, create a message manually using the matching email.txt and PDF.
2. Send only to your own test mailbox. Confirm actual receipt there, including sender/reply address and the two distinct attachments/subjects. Save message identifiers privately; a Sent entry alone is not delivery evidence.
3. Reply to TEST-A v1 with a correction request for the runner name. Reply to TEST-B v1 with its exact approval phrase from that email. Confirm TEST-B approval does not approve TEST-A.
4. Send TEST-A v2 after verifying its changed name and version. Reply with v2's exact phrase. A late v1 approval must not release v2. Keep these records separate from real orders and do not enter them into a production queue.
5. Report app/version, draft-edit result, each actual receipt and reply match. The agent can then record only the evidence actually exercised. Do not claim a completed Shopify order, intake upload, automated deadline or payment/refund test from this email-only exercise.

No timers are started by opening/downloading this packet. The real workflow still requires verified order matching and recorded delivery/approval evidence. These tests do not activate Shopify checkout.

## Agent-side checks completed

All three PDFs rendered and visually inspected: clear TEST label, distinct piece/version/details and no clipping. Poppler emitted fallback-font warnings, but rendered pages are readable. EMLs generated using the actual tools/proof-email/core.js. Independent Python MIME parsing verified exact recipient, X-Unsent, one PDF attachment with matching SHA-256, and exact Unicode approval text for all three. An initial checker used the Windows default text encoding for the JSON manifest; rerunning with explicit UTF-8 resolved that checker-only mismatch. No email generator change was needed. Mail-client opening, sending, receipt and reply verification remain untested.
