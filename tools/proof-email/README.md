# Trace proof email

Open `tools/proof-email/index.html` in a browser on the computer holding your order workspace and proof. Keep `index.html`, `app.js` and `core.js` together. No server, account, installation or API key is needed.

1. Choose that piece's canonical `order.md`. Existing order/customer/race/style/accent fields fill automatically. This is a local-file import, not a live Shopify lookup. Corrected workspace values remain authoritative.
2. Check the customer email against the actual Shopify order. Enter the exact piece reference and unit number if absent from the record. Never infer a recipient from the runner's name.
3. Drop the finished PNG/JPEG/PDF proof(s), enter a version such as `v1`, and review the populated email. Multiple attachments are allowed for the same piece/version; use separate emails for different pieces.
4. Check the review box and select **Download email + proofs**. The `.eml` contains the personalized text and the actual attachment bytes. No remote proof URL is needed.
5. Open it in your mail app. Confirm **From: orders@teklostudio.com**, the recipient, piece/version and attachment contents. Send manually. The From header does not authenticate or configure the account.

The file asks compatible mail apps to open it as an unsent draft. Outlook/Apple Mail editing behavior must be tested in the merchant's exact version; no client-specific pass is claimed. If it opens read-only, start a new message, use **Copy email text**, transfer To/Subject to their respective fields and attach the original proofs manually. Microsoft documents opening EML files in new Outlook: https://support.microsoft.com/en-us/outlook/mail/open-eml-msg-and-oft-files-in-new-outlook-and-outlook-on-the-web.

## Approval and follow-up

The email includes the order, piece reference, unit and proof version in its subject and asks the customer to reply with the exact **APPROVED FOR PRODUCTION** phrase identifying those same details, or to request changes. It includes the 48-hour response window and approved 8–10-business-day production timing, with transit separate and silence never approval.

Generating/downloading an email does **not** record delivery, start the response clock, mark approval, alter `order.md`, or modify the operations ledger. After independently verifying actual delivery, record the exact sent proof/version/hash and message receipt using the existing ledger's `proof`/`delivered` events. After verifying the written reply, record `approve`. A revised proof needs a new version and new approval. Existing Canva/map gates remain unchanged.

The browser does not connect to Shopify, Jotform, Outlook or Apple Mail. Details stay in memory; closing/reloading clears them. Downloaded EML files and clipboard text contain customer information, and EML attachments contain proof/route data: keep them with the private order records and include copies in the existing deletion review. Never commit customer order files or generated emails to Git. No reminder, refund or deletion automation is introduced.

## Validation boundaries

Core tests cover canonical-record parsing, duplicate/ambiguous fields, recipient/header validation, Unicode content, exact piece/version approval identity, and MIME attachment contents/type/size checks. Synthetic records only. Browser visual/drop interaction and mail-client draft opening/delivery require the merchant-side test; browser automation refused the local file URL. No alternate route around that browser restriction was attempted.

Rollback: remove or stop using these local files; no external settings were changed. Preserve any already-sent proof records and customer approvals. This tool does not supersede the overall NOT READY launch status.
