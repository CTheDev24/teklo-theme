# Custom Work attachments — 21 September 2026

Implemented on unpublished theme **196729798822**, `teklo-theme/dev`. No theme publication or paid upgrade occurred. Overall launch status remains **NOT READY**; this Custom Work test does not close the separate Trace order/proof/payment gates in REVIEW-PACKET.md.

## Applied changes

- Theme: Custom Work now embeds Jotform **262637916705061**, with an accessible iframe title, explicit provider/limits, and a direct new-tab fallback. Existing page layout and native contact form remain; turn off **Use Custom Work form with file uploads** to restore the latter. New setting defaults off for other section instances; enabled in `page.custom-work.json`.
- Preview: https://at3dshop.myshopify.com/pages/contact?view=custom-work&preview_theme_id=196729798822 . The menu uses this Contact page alternate template; `/pages/custom-work` is not an existing page.
- Jotform: required name/email/project description; optional organization/timing/budget/reference link/attachments. Allowed extensions: `pdf,jpg,jpeg,png,webp,heic,stl,3mf`. Maximum **5 files**, **10240 KB each**, verified by reopening field properties. Larger files can use the reference URL. Jotform account storage/submission limits still apply; no paid commitment was made.
- Jotform Google Drive integration: submission PDF and uploaded files, grouped by submission ID in **Teklo Studio / Teklo Studio — Custom Work**. Destination folder ID `1d5Mtfp_Pw-PJ6RgyLalptLcs7xteOUVi` inside supplied parent `1f2Luyf3tTrnFlJoT93uBee14vheETT_y`.
- Drive: with explicit merchant authorization, changed parent general access from **Anyone with the link / reader** to **Restricted**. Metadata now lists only the owner and `shared:false`. Destination was moved into the parent after restriction. Other child-folder settings were not individually changed.
- Both Jotform emails were disabled only for the authorized synthetic test, then restored immediately. Both menus subsequently showed **Disable**, confirming enabled state. Merchant notification uses the signed-in account's Apple relay; autoresponder uses submitted email. Receipt/relay forwarding is not verified.
- Thank-you copy simplified to “Thank you for reaching out to Teklo Studio” and “Your inquiry has been received.” Saved editor readback verified. No response-time or retention promise added.
- English fallback strings added consistently to existing locale files, matching the existing Custom Work localization approach. Non-English localization of this English Jotform is not complete.

## Test evidence

- One authorized synthetic submission **6658510023019737879**: `Teklo Upload Test`, reserved non-deliverable example email, explicitly marked synthetic/no fulfillment. Notification and autoresponder disabled before submit. Success page displayed “Your inquiry has been received.” No real customers contacted.
- Drive receipt verified in folder `1RkNu71RrmyMocNqHD3NbKiukQ5wfRzc1`: synthetic PDF **1397 bytes**, PNG **68 bytes**, STL **120 bytes**, 3MF **1124 bytes**, and generated inquiry PDF **71706 bytes**. All list as not shared. Small STL/3MF are transport fixtures, not certified printable models. Test artifacts are retained and labeled synthetic.
- Draft browser preview identified **teklo-theme/dev Draft**. Embedded form loaded; required name/email/project fields, optional attachments, allowed types/count/size and send control present. Direct fallback has the exact verified form URL, `_blank` and `noopener`.
- Controlled 390px and 360px CSS viewport checks: no horizontal page or embedded-body overflow. At 390px page width375/body314; at 360px page345/body284 (scrollbars consume remaining width). Blank embedded submission blocked with three required-field errors; no additional submission created. Auto-resize responded to validation and viewport changes. Desktop iframe resized to1657px. Viewport restored and clean draft preview left open.
- Theme Check: **0 errors, 10 warnings**: nine baseline warnings plus one new `RemoteAsset` warning for the official Jotform embed handler. The provider-hosted handler is needed for iframe resizing; only loaded with this form. No performance improvement claimed.
- Six existing offline Trace workflow unit tests pass; `git diff --check` passes. Shopify skill helper search failed network and validator lacked `@shopify/theme-check-common`; official Shopify settings docs and installed Theme Check used instead.
- First draft push saved new section code but dropped the enable setting before schema became available. Readback caught it; a second template push enabled it; browser verified the upload form.

## Limits and remaining review

Email delivery/Apple relay forwarding, Jotform quota exhaustion, large-file/count rejection, JPG/JPEG/WEBP/HEIC uploads, real iPhone/Android touch/file pickers, screen reader, 200% zoom and no-JavaScript behavior were not exercised. Four tested formats reached Drive; configuration alone is not a pass for other formats. Existing launch analytics/consent/performance and Trace post-payment tests remain open. Review the embedded provider appearance and verify merchant notification receipt before publication. No retention/deletion automation is asserted.

## Rollback

1. Theme editor > Custom Work section: turn **Use Custom Work form with file uploads** off; save on draft. This restores the original Shopify contact form (no attachments). Or restore the pre-change template setting `{}` and deploy only `templates/page.custom-work.json` to theme196729798822. No live publication required.
2. For complete code rollback, revert the Custom Work implementation commit and redeploy its theme files to the same unpublished ID. Preserve newer unrelated edits. Locale additions are inert while disabled.
3. If withdrawing the integration, remove the storefront entry point first, then disable the Google Drive integration on form262637916705061. Do not delete submissions/files; preserve data for merchant review. Emails should remain enabled unless the merchant decides to deactivate the form.
4. Destination can be moved back to My Drive (prior parent `0AHt41AMcOa1BUk9PVA`) without deleting files. Keep it Restricted. Restoring the parent's old public-link permission would expose inherited customer uploads: move sensitive contents out first and obtain explicit merchant authorization before broadening access. The requested security restriction should normally remain.

Source for Shopify checkbox setting semantics: https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings . Embed markup sourced from Jotform builder Publish > Embed > iFrame; unnecessary camera/microphone/geolocation/payment permissions and forced page scroll were omitted.