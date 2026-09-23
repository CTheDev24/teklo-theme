# Trace intake purchase handoff — 22 September 2026

P0-03 partial implementation: the Trace purchase form now exposes the existing enabled public intake https://form.jotform.com/262521531346047 in a new tab. Instructions require one submission per piece after ordering, using order number, order email and the cart piece reference; they list GPX, public activity link, official course and course-map alternatives. Proof instructions explain reply-based, version-specific written approval and production hold. The pre-launch warning remains because checkout and the complete proof workflow are not verified.

This change does not install an order-confirmation email, send proofs, verify delivery or close P0-03. The user previously confirmed actual Trace test receipt at orders@; this run freshly verified enabled form state and visible order/piece fields and route options without submitting customer data.

Changed theme files: snippets/trace-piece-fields.liquid and 31 storefront locale files. New text uses English fallback, consistent with the existing Teklo launch strings; no translated-copy sign-off is claimed. Existing required piece reference and gift note fields remain intact.

Validation: official Shopify documentation search completed. The skill's bundled validate.mjs failed to start because @shopify/theme-check-common is absent. Installed Shopify Theme Check completed with zero errors and ten baseline warnings in actual theme files (review backups excluded). Remote before copies of all 32 changed files matched pre-edit Git HEAD after newline normalization. Deploy only those files with --nodelete to unpublished theme 196729798822.

Rollback: local ignored review/homepage-handoff-before contains exact remote before files. Restore only the changed snippet and matching 31 storefront locale files to theme 196729798822 with explicit --only arguments and --nodelete, checking for intervening merchant edits. Alternatively revert this commit and deploy only its theme changes. No Shopify product, policy, notification, app, billing or published-theme setting was changed.

Remaining P0-03 work: purchase/order-email consistency, actual two-piece receipt and reconciliation, missing/invalid/private/unavailable route handling, version-specific proof delivery and approval, reminders/nonresponse/refund execution, outdated Etsy graphic and test order after merchant plan/payment activation. Status remains NOT READY.

Deployment completed successfully to unpublished teklo-theme/dev 196729798822. Fresh rendered product DOM confirms the exact public form URL and new intake instructions. The five product-form validation checks pass (empty/invalid/valid reference, ordinary product and unavailable product). git diff --check passes after newline normalization.
