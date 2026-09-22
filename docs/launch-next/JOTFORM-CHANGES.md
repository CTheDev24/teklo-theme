# Trace intake changes — 21 September 2026

Form: https://form.jotform.com/262521531346047. These are external Jotform changes, not effects of a theme commit. No submission or email was sent in this follow-up.

## Applied and read back

- Condition 1 formerly compared the route choice with `MISSING FIELD`. It now requires `Upload your route file` when the selected value is `Upload my activity file — Best accuracy`.
- Condition 5 referenced a deleted source and a deleted target. Disabled it (not deleted). Other conditions retained.
- Original piece-number question 46 remains the visible required number field with minimum 1. Its help now reads: `Use 1 for the first piece with this reference, 2 for the second, and so on. Enter a whole number; we check it against your order quantity before preparing a proof.` Placeholder: `e.g., 1`.
- Two replacement-field experiments did not enforce integers in the public form. Question 53 (`Piece number (legacy numeric)`) and question 54 (`Piece number (unused text validation)`) are hidden and optional. Original question 46 and existing submission data were preserved. Do not map an integration to 53/54.

## Verification and limits

Public form reload shows only the original required piece-number control. Earlier minimum validation rejected zero, but decimals remained accepted. Numeric short-text validation also accepted 1.5 in the observed blur check; it was not left as the live replacement. Whole-number and purchased-quantity reconciliation remain a mandatory operator check; the offline ledger rejects invalid units. No browser integer-enforcement pass is claimed.

Selecting each of the four route methods changed Jotform's `validate[required]` class to the corresponding fields: GPX input 21; activity link 22; course year 24, distance 26 and details 27; map upload 28. The GPX requirement is removed for alternatives. Native `required` remains on field 26 even while its Jotform required class is removed. End-to-end successful alternative submissions still require testing; class switching alone does not prove submission acceptance or storage delivery.

No live Trace upload receipt, notification delivery, sender authentication, two-piece reconciliation, proof delivery/reply or post-payment flow was exercised. Existing Custom Work synthetic upload evidence is separate.

## Rollback

In the builder Settings → Conditions, restore condition 1 to the saved earlier revision if needed; re-enable condition 5 only when restoring its missing fields, since it is invalid otherwise. A form revision immediately after the condition repairs and before field experiments was `6ab1e8c46364645a82cbcbfd`. Review revision contents before restoring because a whole-form restore could overwrite later merchant edits.

For a targeted rollback, retain original question 46 required/visible with minimum 1; recover its prior sublabel from revision history and restore placeholder `Submit once per physical piece. For quantity 2 with the same reference, use 1 then 2.` Keep 53/54 hidden and optional to preserve history. No email toggles, recipients or storage permissions were changed by this follow-up.

## Integration and notification inspection

The Trace Google Drive panel opened a new-integration wizard, not a configured destination. An existing authorized Google account was available. Its mapping screen offered a new folder name, optional per-submission subfolders, PDF selection and upload-field selection; no existing folder-ID selector was visible. Canceled and explicitly discarded this unsaved wizard. Custom Work's completed connection does not establish a Trace connection.

Merchant configuration identifies Trace's accepted-GPX folder as `1oGVT9Z8OO9Ss2EDM4W99DxRb8bJhONUR`, direct files only, filename `firstname_ordernumber.gpx`. Do not silently create a new similarly named destination, recurse into subfolders or repurpose the separate Custom Work folder. The observed wizard does not demonstrate that direct-folder contract or per-piece naming. Exact remaining implementation is to map upload field 21 to a verified private staging destination, prove receipt, then reconcile order/line/unit and promote accepted GPX into the approved direct folder; photos/maps and submission PDFs need separate private staging and must not masquerade as accepted GPX. Existing order-only filenames cannot alone authenticate or distinguish multiple pieces. No storage automation is claimed here.

Emails panel listed only `Notification 1`, from Jotform to the account's Apple private-relay address. No customer autoresponder was listed in the inspected panel. Delivery/monitoring of that relay was not tested. Prepared customer acknowledgment must use the confirmed support/proof channel and exact per-piece reference; the setup blocker is verified sender/recipient and storage reconciliation, not a missing Jotform login. No setting was changed in this inspection.
