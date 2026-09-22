# Confirmed mailboxes and routing — 21 September 2026

Merchant confirmed support@teklostudio.com, orders@teklostudio.com and hello@teklostudio.com are actively monitored. No response-time commitment or sender-domain authentication evidence was supplied.

## Applied externally

- Trace form 262521531346047, Notification 1: orders@teklostudio.com, verified again after reload following testing.
- Custom Work form 262637916705061, Notification 1: hello@teklostudio.com, verified after save/reload in the preceding batch. Its customer autoresponder remains addressed to the submitted Email Address field. Trace has only Notification 1.
- Shopify Contact information: replaced contact@at3d.net with linked support@teklostudio.com.
- Shopify Shipping and Refund policies: replaced [support email] with linked support@teklostudio.com.
- Shopify Settings → General → Store contact details → Store email: sales@at3d.shop → support@teklostudio.com. This receives store messages; it is distinct from notification sender settings. Saving also updated the automated privacy policy contact. Automated policy remained enabled.

Independent Admin API readback confirms all four policy contacts and shop contactEmail now use support@. Contact, shipping and refund match the prepared bodies exactly except markup whitespace. Terms of service were not edited. Privacy was independently updated by the merchant during this work; its newer domain/template were preserved. Comparing privacy immediately before/after the store email change confirms only the email changed.

The shipping source editor virtualized its HTML. An initial save accidentally truncated the policy after section 4. It was immediately restored from the complete backup with the intended support substitution; full sections 1–8 and final paragraphs independently read back and matched. Use full rich-text iframe HTML, never CodeMirror visible innerText, for future edits.

## Email testing and newly discovered blocker

Merchant explicitly approved synthetic tests to orders@ and support@ and contact-only policy changes. Jotform Test Email was clicked twice, once with orders@ in the editor and once with a temporary unsaved support@ recipient. Merchant reported both arrived at the account's iCloud mailbox. These do **not** verify either Teklo mailbox. [Jotform documents that Test Email always targets the account email](https://www.jotform.com/answers/461950-test-email-sent-to-default-email-not-to-the-email-i-set-up). Temporary recipient was discarded by reload; persisted orders@ was verified. No account email changed.

A real form attempt used synthetic order TEKLO-TEST-20260921-NOT-AN-ORDER, piece TEST-DO-NOT-PRODUCE / 1, Gallery / Signal Orange, support@ as order email, and an explicitly fictional unavailable course. Notes prohibit research, proof, production, fulfillment or customer contact. Required category validation was exercised. Browser DOM reads did not reflect the email value reliably; a screenshot verified exactly support@ before the final attempt.

Submit opened **Preview Sign Document**, with electronic-signature legal acceptance and **Sign Document**. No signature or acceptance was made. No completed submission, orders@ delivery, proof delivery, written proof approval or production is claimed. Any retained partial test data must remain an unmatched synthetic order, never production work. Review this intake e-sign setting separately from later version-specific proof approval.

Support@ delivery remains unverified. Custom Work delivery to hello@ and customer autoresponder delivery also remain unverified. Existing Trace notification body still uses legacy Etsy labels and prototype piece fields 53/54; correction remains open. No paid order, real customer contact, payment or publication occurred.

## Rollback

- Policies: mailbox-policy-backup.json contains historical before bodies; mailbox-policy-readback.json records current saved bodies. Compare current content first and reverse only the targeted contact substitution. Do not restore the historical privacy body: merchant changed it independently. Keep automatic privacy enabled.
- Store email: restore sales@at3d.shop in General → Store contact details only if rolling back this contact routing; verify the automated privacy contact afterward. This does not restore or authenticate notification senders.
- Jotform recipients: Settings → Emails → Notification 1; restore original Apple private-relay recipient from the prior saved revision/account settings, save and reload. Private address is intentionally not copied into this repository. No template or sender changes were made during this test.
- No signature setting changed, no agreement signed, and no customer message was resent. Inspect partial synthetic data before any cleanup; do not delete real submissions.

Earlier connector write_legal_policies and automatic-review blocks were resolved for these specific contact-only writes by explicit merchant approval and authenticated Admin UI. P1-03 is partially fixed: monitored contacts and policy substitutions verified; delivery and response expectations remain open. P0-03 and overall **NOT READY** remain.

## Successful submission after approved signature removal

Merchant explicitly requested: remove intake signature; keep proof approval. Disabled Settings → Jotform Sign → Enable Jotform Sign Automation. Builder reported saved. A fresh public form retained all three acknowledgment checkboxes and the later written proof-approval requirement. The same clearly marked synthetic details then submitted successfully to the Thank You page without any signature step. Merchant confirmed the actual notification arrived at orders@teklostudio.com. This verifies one course-research-path submission and notification receipt; it does not verify GPX attachments, reply handling, two-piece reconciliation or proof delivery/approval.

That success page exposed an old Etsy/1–2-day promise. Replaced its paragraph, preserving formatting, with:

> Your submission is awaiting order and route verification. Submitting intake does not approve a design or start production. Missing or unclear details require clarification. Production requires written approval of the proof version for your piece; no response is not approval. For questions, contact orders@teklostudio.com and include your order number and piece reference.

Saved copy verified after builder reload. No duplicate submission was sent solely to re-render the new success copy. Original paragraph for targeted rollback: “We’ll review your information and route, then send your digital proof through Etsy Messages within 1–2 business days. Production will begin only after you approve the proof.” Restore only via explicit rollback review because it reintroduces an invalid channel/time promise. E-sign rollback is to re-enable Jotform Sign Automation; this restores the unwanted intake gate and is not recommended. Written approval remains a later operational gate; no proof was approved here.

The earlier signature-blocked result above is historical and superseded for intake completion. Support@ and hello@ delivery, customer autoresponder delivery and sender-domain authentication remain unverified. The synthetic completed entry is test evidence, never a production order. No deletion performed.
