# Confirmed mailboxes and routing

Merchant confirmed support@teklostudio.com, orders@teklostudio.com and hello@teklostudio.com exist and are actively monitored. No response-time commitment was supplied. Monitoring confirmation is not delivery/authentication evidence.

## Applied externally and verified after reload

- Trace form `262521531346047`, Notification 1: replaced the account's Apple private-relay recipient with `orders@teklostudio.com`.
- Custom Work form `262637916705061`, Notification 1: replaced the same account relay with `hello@teklostudio.com`.
- Existing Custom Work autoresponder remains addressed to the submitted Email Address field. Trace still has only Notification 1; no customer autoresponder created.
- Sender remains Jotform; no claim that the Teklo sender domain is authenticated. No test email, submission or customer message sent in this mailbox-routing follow-up.

Rollback: open each form's Settings → Emails → Notification 1, replace its single To recipient with the original account Apple private-relay address from the prior saved revision/account settings, save and reload. Original recipient is intentionally not duplicated in this repository. Email bodies and sender settings were not intentionally edited. Future submissions will use the new recipient; existing stored submissions were not resent.

## Prepared but not applied

`mailbox-policy-backup.json` contains exact before/after bodies for CONTACT_INFORMATION, PRIVACY_POLICY, REFUND_POLICY and SHIPPING_POLICY. The only textual substitution is `[support email]`, `contact@at3d.net` or `sales@at3d.shop` → `<a href="mailto:support@teklostudio.com">support@teklostudio.com</a>`. No return, cancellation, shipping, damage or retention term changes. The saved before bodies provide rollback, subject to checking for subsequent merchant edits.

Shopify returned access denied for CONTACT_INFORMATION and PRIVACY_POLICY because the connector lacks `write_legal_policies`. Automatic approval review rejected the REFUND_POLICY call because submitting the full policy includes unresolved substantive business/legal terms. SHIPPING_POLICY was not attempted after that rejection. None of these policies changed. Do not bypass the rejection through the UI without explicit approval of the exact contact-only replacements. Shopify shop contactEmail also remains `sales@at3d.shop`; it was read but not changed.

The review request asks for explicit permission for synthetic emails to orders@ and support@ and the exact contact-only policy replacements. Until answered, no send or policy write proceeds. Once approved, use authenticated Shopify Admin UI for policy edits if connector scope remains unavailable, then independently re-read all four bodies. Actual inbox receipt and reply matching still require evidence.

## Additional observation

The existing Trace notification body still labels the Shopify order fields as Etsy and includes hidden prototype piece fields 53/54 alongside the correct field 46. Routing is fixed, but the template needs a separate verified correction before workflow sign-off; no proof-delivery claim was introduced. Public intake labels remain Shopify.

P1-03 progresses from unknown monitored mailbox to merchant-confirmed addresses and configured Jotform routing. Public policy replacements and delivery remain open. P0-03 and overall NOT READY status are unchanged.

Readback note: Contact, refund and shipping bodies remained byte-for-byte unchanged after the blocked attempts. Privacy changed independently during the check: its site domain now reads teklostudio.com instead of at3d.shop, while sales@at3d.shop remains. Therefore the saved privacy before/after pair is a historical snapshot, not a safe whole-body payload for later use. Re-fetch and make only the targeted email substitution; preserve the newer domain and any other merchant edits.
