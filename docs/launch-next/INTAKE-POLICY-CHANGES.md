# Trace intake policy implementation — 2026-09-22

External app: Jotform form `262521531346047`, **Complete Your Trace**. These changes are saved in Jotform, not deployed by a theme commit. Merchant expressly approved the policy choices and implementation on September 22.

## Applied: paragraph field 52

Before:

> Missing details, invalid route files, private activity links, unavailable courses, or unclear medal colors require clarification. No response is not approval. Production stays on hold until details and route are verified and written approval identifies the proof version and piece.

After:

> Submit one intake per piece within 48 hours of receiving your order confirmation and intake instructions. We send your first proof to your order email within 48 hours after receiving complete, usable intake. Reply within 48 hours of each proof email with changes or written approval identifying the piece and proof version.
>
> Missing details, invalid route files, private activity links, unavailable courses, or unclear medal colors require clarification. Production stays on hold until the details and route are verified and you approve the proof in writing. Silence never counts as approval.
>
> For an unanswered intake, clarification or proof request, we send a reminder at 48 hours and a final reminder on day 7. After 10 calendar days without a response to that request, an unapproved order is canceled and fully refunded.
>
> You may cancel for a full refund before written proof approval. After approval but before production, cancellation is at our discretion. Orders cannot be canceled once production starts; changes are at our discretion. Production takes 8–10 business days after complete intake and written approval. Shipping transit time is additional.
>
> Questions or corrections? Email orders@teklostudio.com with your order number and piece reference.

## Applied: thank-you page body paragraph

Kept the existing heading, image, typography, wrapper and layout. Only replaced the body paragraph, adding paragraph breaks.

Before:

> Your submission is awaiting order and route verification. Submitting intake does not approve a design or start production. Missing or unclear details require clarification. Production requires written approval of the proof version for your piece; no response is not approval. For questions, contact orders@teklostudio.com and include your order number and piece reference.

After:

> Your submission is awaiting order and route verification. We send your first proof to your order email within 48 hours after receiving complete, usable intake. Please reply within 48 hours of each proof email with changes or written approval identifying the piece and proof version. Missing or unclear details require clarification. Submitting intake does not approve a design or start production; silence never counts as approval.
>
> For an unanswered intake, clarification or proof request, we send a reminder at 48 hours and a final reminder on day 7. After 10 calendar days without a response to that request, an unapproved order is canceled and fully refunded. Production takes 8–10 business days after complete intake and written approval; shipping transit time is additional.
>
> For questions or corrections, contact orders@teklostudio.com and include your order number and piece reference.

## Verification and limitations

- Jotform displayed **All changes saved** after both edits. Reloaded the page and independently reread the saved thank-you text and field 52.
- No fields, IDs, conditions, required flags, route options, uploads or acknowledgment checkboxes were changed. No signature field was added; Sign settings still offered **+ Add Signature Field**. The previously disabled signature flow was not changed.
- Notification 1 remains addressed to `orders@teklostudio.com`, confirmed after reload. No submissions, test emails, customer messages or refunds were sent.
- Notification HTML still has the legacy labels **Etsy order number** and **Name used on the Etsy order**, plus two legacy piece-number rows. An attempted source-editor correction did not visibly take effect; it was discarded by reloading without saving. Follow-up should replace those two labels with Shopify while preserving substitution tokens and the recipient. These labels are internal notification content, not public intake labels.
- This is published form guidance, **not proof of scheduled reminders, refund automation, proof delivery or approval completion**. The merchant must operate the stated schedule until an integration is built and verified. No new automation was created or represented as functioning.
- Retention/privacy text was deliberately not added: provider deletion and backup behavior still require validation.

## Rollback

Open `https://www.jotform.com/build/262521531346047`. Edit existing paragraph field 52 and replace its body with the exact Before paragraph above; blur the editor and wait for All changes saved. In Settings → Thank You Page, replace only the body paragraph with the exact Before text, preserving the wrapper, heading, images and styles. Reload each surface and verify the restored copy. Do not restore the entire form revision, which could revert unrelated fixes or fields. Retain applicable terms for existing orders; rollback is not authorization to alter their terms retroactively.
