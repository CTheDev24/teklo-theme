# Policy and launch-assortment configuration follow-up

Fresh Shopify reads on 22 September 2026: the store plan is Paused. This confirms P0-01 still requires merchant plan/payment activation and actual checkout tests.

## Policy branding: prepared, not applied

Four current policies contain AllThings3DShop: contact information, refund, shipping and terms. Exact pre-change bodies: policy-branding-before.json. Exact prepared input bodies: policy-branding-prepared.json. Each prepared change replaces only AllThings3DShop with Teklo Studio. Privacy already uses Teklo Studio and retains legal entity AllThings3D LLC; it is deliberately excluded.

The validated shopPolicyUpdate call on CONTACT_INFORMATION returned `Access denied for shopPolicyUpdate field. Required access: write_legal_policies access scope.` No policy changed; subsequent writes were not attempted. The connector's generic success message was not treated as success because its structured response contains access denial. Browser Admin is signed out, so that alternate route also requires merchant sign-in. No new app scope or security permission was requested silently.

When access is restored, reread each body before applying only the brand substitution; do not blindly overwrite intervening edits using a stale snapshot. Rollback after any future application is the inverse scoped substitution or restoring the exact before body after checking later changes. At present no rollback is needed because nothing was written.

## Shipping: fresh configuration evidence

All four additional Shop products (Boho, Modern Art Deco clock, Birch and Luxar), including every variant, are assigned to General profile. It has:

- Domestic US zone including territories and military-address regions, beyond the Trace-specific 50-state scope.
- Free Economy rate at total price greater than or equal to $35. The policy says over $35, so exactly $35 is a wording boundary discrepancy; use `orders of $35 or more` when correcting factual shipping copy.
- An unconditional $3 Economy option, plus USPS Ground Advantage, Priority Mail and Priority Mail Express.
- An International zone limited to 27 named countries; the blanket worldwide policy statement is broader than the configured zone. Exact countries are in launch-shipping-fresh-readback.json. An active zone is not proof of active market eligibility or a successful checkout rate.

Trace remains isolated in profile 105536815270, exactly eight variants, all 50 states plus DC, only Ground Advantage and Priority Mail active, with no free/flat rate. All queried connection pageInfo flags were false. Flat Rate profile contains no products. Shipping configuration was not changed in this follow-up.

Prepared factual wording for General shipping (requires policy write access): `For non-Trace products, available destinations, shipping services and charges are shown at checkout. Free Economy shipping is configured for eligible US orders of $35 or more. Trace has separate US-only shipping rates and is excluded from this offer.` Replace blanket worldwide wording in both shipping and terms with `International shipping for eligible non-Trace products is limited to supported destinations shown at checkout.` Do not infer a merchant decision to expand Trace shipping or remove existing general shipping zones.

Remaining verification: confirm intended launch scope for non-Trace products, active markets, package weight/dimensions and actual quotes for single/mixed baskets, Alaska/Hawaii/DC and excluded Trace destinations. Carrier configuration alone does not pass fulfillment testing. Existing generic processing/transit promises are not newly verified here. Status remains NOT READY.

