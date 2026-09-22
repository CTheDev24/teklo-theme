# Trace shipping configuration — 22 September 2026

Status: **implemented and configuration readback verified; checkout rates not yet tested**. Related audit: P1-02; P0-01 still prevents end-to-end purchase sign-off.

## Applied in Shopify

Created shipping profile **Trace — US launch**, ID `gid://shopify/DeliveryProfile/105536815270`, and moved all eight variants of Trace product `15807121490086` into it. No other product was moved.

- Destination: US, all 50 states plus District of Columbia. Alaska and Hawaii explicitly included. Territories, freely associated states and military-address regions AA/AE/AP are excluded; no international zone.
- Origins: existing AT3D Warehouse `75230838950` and TX Warehouse `73954164902`, retained from Trace's previous General profile.
- Standard option: existing USPS **Ground Advantage** carrier-calculated service.
- Priority option: existing USPS **Priority Mail** carrier-calculated service.
- Existing active USPS carrier `67078586534`; fixed fee $0 USD, percentage markup 0%; automatic addition of new carrier services disabled.
- Priority Mail Express, First Class Mail and Media Mail disabled in this Trace profile.
- No flat rate, free-shipping threshold or free-shipping promotion was added. Trace no longer inherits General's free Economy rate for orders ≥$35 or unconditional $3 Economy rate.

This is Shopify configuration, not a theme setting. It applies across storefront themes. No theme was published and no plan or paid service was purchased.

## Evidence

Before: `shipping-configuration-backup-2026-09-22.json` preserves both original profiles, the inspected service/price/condition data, all eight Trace variant IDs and exact create input.

After: `shipping-configuration-readback-2026-09-22.json` records a fresh query after successful creation (no user errors):

- Trace profile contains exactly one product and all eight Trace variants.
- Its sole zone contains exactly 51 region codes (50 states + DC), US only.
- Only Ground Advantage and Priority Mail services are active.
- General profile location groups/zones/rates are byte-for-byte unchanged in query data.
- General profile's remaining product records/inspected variant records are unchanged.
- Empty Flat Rate profile is byte-for-byte unchanged.

Profile, product assignment, location, zone and method connection pagination is complete. Unrelated product variant lists in snapshots are explicitly sampled first 10; Trace's eight variants are complete. No unrelated variant changes were requested or performed.

Admin schema inspected before query and mutation; both passed connector GraphQL validation. Skill CLI mutation validation passed. Skill documentation search could not fetch; schema plus validated connector operation provided the implementation contract. Initial broad read exceeded query-cost limit and was reduced before any mutation.

## Remaining verification

Carrier configuration does not prove a quoted price or service availability for a particular package/address. After selling-plan/payment test setup, test standard and priority rates for contiguous US, Alaska, Hawaii and DC; reject Canada, Puerto Rico and military-region addresses for Trace. Test one piece, two pieces, and mixed carts containing a General-profile product. Confirm no unintended free shipping or combined-rate behavior. Check package dimensions/weight and inventory-origin allocation against measured packing facts before signing off rate accuracy; no physical values were invented or changed here.

Carrier service names are retained; no guaranteed transit time was introduced. Priority shipping does not shorten the approved 8–10-business-day production period.

## Rollback

1. In Shopify Settings → Shipping and delivery, open **Trace — US launch** (profile `105536815270`).
2. Remove only the eight Trace variants from this custom profile (or use `deliveryProfileUpdate` with `variantsToDissociate` containing the eight IDs in the backup). Shopify returns dissociated variants to the General profile.
3. Requery profiles and verify Trace is back in General with all eight variants; other assignments and all General/Flat Rate rates remain unchanged.
4. Leave the now-empty Trace profile as a reversible record, or delete it only after confirming it is empty.
5. This rollback restores inherited international and free-≥$35 Economy rates, so it also restores the known launch-policy mismatch. Do not mark shipping ready after rollback without resolving that mismatch.

Reverting the repository commit alone does not undo this Shopify change.

Source reference: [Shopify deliveryProfileCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/deliveryProfileCreate) and [DeliveryParticipant](https://shopify.dev/docs/api/admin-graphql/latest/objects/DeliveryParticipant).
