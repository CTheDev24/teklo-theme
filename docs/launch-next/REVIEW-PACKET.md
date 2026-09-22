# Next launch implementation — 21 September 2026

**NOT READY.** Purchasing, complete Trace intake/proof delivery, business facts and mandatory release tests remain open. Nothing was published and no paid commitment, payment activation, real-card charge or customer communication was made in this follow-up.

Branch `codex/feature/launch-readiness-next`, based on `origin/dev` at `918361f`. This batch follows [draft PR 2](https://github.com/CTheDev24/teklo-theme/pull/2); it does not imply that PR was merged. Target is only unpublished `teklo-theme/dev`, ID **196729798822**.

[Draft preview](https://at3dshop.myshopify.com/?preview_theme_id=196729798822) · [Trace preview](https://at3dshop.myshopify.com/products/personalized-3d-race-map-custom-gpx-running-wall-art-marathon-finisher-gift?preview_theme_id=196729798822) · [Custom Work preview](https://at3dshop.myshopify.com/pages/contact?view=custom-work&preview_theme_id=196729798822)

## Policy implementation update — 22 September

See [merchant decisions and prepared copy](POLICY-DECISIONS.md). Merchant selected 8–10 business days production, 7-day damage reporting, domestic US launch shipping, a 14-day post-delivery file deletion target, the current $25 medal upsell and a maximum 30-day relaunch discount. Cancellation/refund boundaries, response clocks, actual storage deletion and exact shipping/discount configuration still need the limited clarifications recorded there. Merchant subsequently approved the proposed cancellation/refund, response and privacy scope, a 48-hour first proof, and a launch-date-based 30-day promotion. Product/refund/Jotform terms are now applied; manual deadline queue has 22 passing tests. The old unlimited 25OFF is deactivated pending launch. Shipping/terms policy saves subsequently completed and were read back. Actual shipping coverage/services, exact discount unit scope and provider deletion remain open. See [implementation evidence and rollback](POLICY-IMPLEMENTATION.md). This supersedes older decision requests below.

## Implementation and findings matrix

Mailbox follow-up: merchant confirmed all three Teklo mailboxes are monitored. Trace routing is orders@; Custom Work is hello@. Four policy contact sections and Shopify store email now use support@, independently read back. Test Email delivered to the account's iCloud address, not the configured recipients. Merchant approved removing the unexpected intake e-signature gate. A fresh synthetic submission succeeded and merchant confirmed notification receipt at orders@. The obsolete Etsy/time promise on the success page was corrected and saved. Later proof approval remains required. See [current mailbox configuration](MAILBOX-CONFIGURATION.md) for evidence and rollback.

All audit IDs are retained. Status distinguishes current work from inherited fixes and unresolved decisions.

| ID | Owner | Current result and remaining disposition |
|---|---|---|
| P0-01 | Shopify billing/payments | **Staged for necessary human review.** Fresh shop read still reports Pause and Build. Active plan/payment test configuration requires merchant action. Shipping, tax, payment, confirmation and refund untested. |
| P0-02 | Theme/collection | **Fixed/tested, inherited.** Exact draft routes Shop to Trace collection and Trace actions to product; From $149.95 visible. Reverified desktop. |
| P0-03 | Theme/Jotform/operations/notifications | **Partially implemented; mandatory live gate open.** Restored pre-cart validity check; repaired obsolete form condition; added persistent per-piece offline ledger. Full upload/reconciliation/email-proof/approval and nonresponse operations are not exercised. Newly replaced gallery image again says Etsy; hold/replace before launch. |
| P1-01 | Product content/pricing | **Factual text fixed; intent staged.** Fresh eight variants retain $149.95 standard/$174.95 medal. $25 delta matches text and Gallery selection. Merchant approved the $25 surcharge and relaunch discount. Old unlimited 25OFF is now inactive; final unit scope and launch-timestamp activation remain gated. |
| P1-02 | Policies/shipping/content | **Partially implemented.** Merchant approved 48-hour first proof, 8–10 business-day production and 7-day damage reporting; product/refund/intake copy applied. Shipping exception saved and independently verified; actual domestic services/coverage and checkout remain unverified. |
| P1-03 | Policies/mailbox | **Partially fixed/tested.** Monitored mailboxes confirmed; contact, shipping, refund and automated privacy contacts now support@. Full policy readback verified contact-only changes. Trace notification receipt at orders@ confirmed by merchant; support@/hello@ delivery and response expectations remain open. |
| P1-04 | Product/policy | **Approved and implemented in product/refund/intake.** Full refund before approval; discretionary cancellation after approval before production; none once production starts. Earlier orders retain prior terms. Shopify self-service rules are separate and not verified. |
| P1-05 | Product/theme/media | **Staged for measured facts.** Text withheld conflicting dimensions, but replacement graphic asserts frame 12.5×15×2.4 and map 8×10. These are not measurement evidence. Confirm exterior/insert/map and update together. |
| P1-06 | Policy/intake/storage | **Approved target; provider verification open.** Sole studio operator, separate marketing permission, 14-day deletion target after delivery/cancellation approved. Manual deletion queue implemented; actual provider/backup deletion untested. Terms reuse exclusion saved and independently verified; automated privacy body preserved. |
| P1-07 | Shopify product | **Inherited fixed by DRAFT status.** Soft Face remains excluded from launch in prior evidence; no reactivation performed. Verified specifications required before return to sale. |
| P2-01 | Shop/product SEO | **Partial inherited fix; bounded remainder deferred.** Teklo Studio vendor verified on Trace. Shop/home SEO already corrected in prior batch; catalog-wide vendor and social-image crop review not completed here. Handles retained. |
| P2-02 | Shopify media/content | **Fixed/tested media metadata.** All 13 current images now have visually grounded alt text, applied and independently read back. Earlier alt work did not cover replacement media. Logical description headings retained; full screen-reader sign-off pending. |
| P2-03 | Theme | **Fixed/tested, inherited.** Actually empty collection gives Browse available products; desktop reverified without misleading filter advice. |
| P2-04 | External apps | **Deferred with reason.** Current sampled scripts include Junip/Hextom; no LimeSpot in sampled inventory. Necessity/settings and analytics destination not established, so no uninstall or speculative event emitters. No measured performance improvement claimed. |

## Evidence and exact change records

- [Theme checks](THEME-VALIDATION.md): Theme Check 0 errors/10 baseline warnings; 5 handler tests; 110 restored fallback keys in 11 locales. Design preserved.
- [Trace operations](TRACE-OPERATIONS.md): 14 offline synthetic tests, four route alternatives, two pieces, invalid GPX, missing inputs, proof version/hash, delivery-before-approval, corrections and no-response holds. This is a manual evidence ledger, not functioning email/Shopify automation.
- [Storefront checks](STOREFRONT-VERIFICATION.md): precise browser results and device limitations. Distinguish checks before deployment from later deployed checks.
- [Shopify media changes and rollback](MEDIA-CHANGES.md): exact media IDs, new alternatives, validated mutation inputs, blank-alt rollback. Full prior product snapshot: `trace-product-before.json`.
- [Jotform changes and rollback](JOTFORM-CHANGES.md): conditions, original field preserved, unsuccessful integer-field prototypes hidden. No Trace submission/email sent.
- [Deployment and rollback](DEPLOYMENT.md): all 14 scoped files independently pulled back byte-for-byte. Remote already had the earlier validation/locale fixes; this batch repairs Git parity and adds unique iframe IDs/focus styling.
- [Custom Work evidence](CUSTOM-WORK-UPLOADS.md): prior authorized synthetic PDF/photo/STL/3MF upload and private Drive receipt; email delivery remains unverified. The temporary email-disable permission was used for that test and restored, not reused here.
- [Prior packet](PRIOR-REVIEW-PACKET.md): historical applied configuration and exact staged policy/notification copy. Its earlier media set/status is superseded by current media and storefront records. It is not a current all-pass assertion.

## Consolidated human review

1. **Billing/payment:** select the intended active plan and payment test mode, launch markets and authorized test identity/address. Then exercise order → shipping/tax/payment → confirmation → intake → proof/approval → cancellation/refund. No real card is requested.
2. **Support/proof channel:** monitored mailboxes and test destinations are confirmed. The intake e-signature gate was removed with explicit approval and orders@ receipt passed for one synthetic submission. Test support@, hello@ and customer autoresponder delivery separately (the template Test Email button targets the account address). Verify sender-domain authentication and actual response/follow-up expectations. Proposed initial operation is manual proof delivery to the verified order contact with order, line/piece and proof revision; do not install the prepared order-email insert until delivery and reply matching pass.
3. **Product facts/graphics:** measure exterior frame, insert and map; confirm accent assortment. Replace the Etsy graphic and reconcile 8–10 versus older 10–14-day claims against real capacity. Current Graphite/Stone graphic conflicts with available variants. These graphics are preserved for review, not approved for launch.
4. **Commercial/policy decisions:** retain current $25 medal delta unless explicitly choosing $29 (which would make medal variants $178.95 at unchanged base price). Confirm automatic 25OFF eligibility. Choose one damage window, proof/production timing, cancellation rules, destinations and free-shipping eligibility. Exact proposed wording with internal placeholders is in the prior packet; none of those placeholders should be published.
5. **Route privacy:** confirm authorized people/providers, retention trigger and duration, deletion request route and backup limits across Jotform, Drive, local routes and proofs. Proposed terms exclusion: private route files, activity links, course submissions, medal photos and personalization used for fulfillment are excluded from broad reuse rights for public feedback. Publish only after actual practice is confirmed and configured.
6. **Final release review:** PR, final content, mobile/keyboard/screen reader, consent/event receipt/purchase deduplication and measured mobile performance. Review and publication are separate gates.

## Smallest remaining rollout backlog

1. Resolve the five merchant fact/configuration groups above; apply reviewed copy and graphic corrections.
2. Finish live Trace integration receipt/reconciliation and authorized two-piece proof delivery/approval tests, including missing/invalid/private/unavailable routes and no response. Native form integer enforcement remains unresolved; mandatory operator unit validation is implemented.
3. Install and test the prepared order-confirmation handoff using the verified channel, then complete payment/shipping/tax/refund test after plan activation.
4. Complete device/accessibility, analytics consent/receipt and mobile performance evidence; choose app configuration based on actual launch needs.
5. Final code/content review and merge to dev; publication only on separate explicit release approval.

## Rollback boundaries

Revert this batch's code commit through normal review and redeploy only its changed theme files to the same unpublished theme. Do not restore an entire theme or overwrite unrelated merchant edits. Deployment record contains remote before/after evidence. Code reverts do not undo Shopify media, Jotform settings, policies, notifications, billing or Drive sharing: use their explicit records separately. Stop the offline ledger tool without deleting private order evidence. No public release rollback is needed because no publication occurred.
