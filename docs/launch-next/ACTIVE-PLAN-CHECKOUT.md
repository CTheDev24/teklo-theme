# Active-plan checkout verification — 22 September 2026

Merchant restored an active selling plan. Fresh Shopify shop.plan.publicDisplayName now returns **Basic**, superseding earlier Paused observations.

On exact draft theme 196729798822, selected Race Day / Nocturne / Match My Medal Color (variant 57452337627302), quantity 1, piece reference TEKLO-TEST-PLAN-ACTIVE. Add to cart succeeded at $174.95. Check out opened Shopify Checkout rather than the prior store-not-set-up error. The checkout summary retained all variant labels and the piece reference, subtotal $174.95, with no discount shown. Screenshot: audit-2026-09-22/24-checkout-active-plan.png.

Contact, delivery, shipping-method and payment sections loaded. Card, Shop Pay and PayPal choices were rendered, plus express wallets. This does not establish that a payment method is activated correctly or in test mode. No visible test-mode indicator was observed. Wallet iframe wording Sandbox describes the embedded wallet surface and was not treated as proof of gateway test mode.

No email, address or card details entered; Pay now was not clicked. Shipping required an address; no rates or taxes verified. Requested merchant confirmation of test gateway and authorized shipping address. Returned to cart, removed only the synthetic item and verified Your cart is empty. No order, charge, refund, notification or fulfillment was created.

Checkout's country selector offered France, Germany, Spain, Sweden, Switzerland, United Kingdom and United States. That selector is not evidence that Trace ships internationally; its separate profile and actual address-dependent quotes must still enforce US scope. Email marketing was prechecked in the sampled checkout; no contact was entered or subscription created. Consent behavior remains an explicit audit gate.

P0-01 disposition: plan rejection resolved and checkout entry tested; full acceptance remains open for test shipping/tax/payment, order email and refund. Overall NOT READY remains because the full intake/proof and other mandatory gates remain incomplete. No theme publication or configuration mutation performed by the agent; merchant owns the billing change. No code rollback is needed for this evidence-only follow-up.
