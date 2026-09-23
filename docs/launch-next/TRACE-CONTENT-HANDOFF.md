# Trace product handoff and conflicting graphics — 22 September 2026

Applied directly to Shopify product 15807121490086. No theme publication or notification change.

Description now links the existing enabled intake form, identifies order/email/reference/unit matching, includes GPX/public-link/course-details/course-map alternatives, explicitly permits finish-time omission, and describes email proof corrections/written approval by piece and version. Existing approved deadlines, prices, return/cancellation terms and pre-launch/measurement warnings are preserved. This publishes the intended manual process; it does not establish automated delivery or close the end-to-end verification gate.

Three conflicting graphics were detached using fileUpdate.referencesToRemove for this product only. Files were not deleted or overwritten:

| Media ID | Prior position (one-based) | Reason |
|---|---|---|
| 70404128309414 | 5 | Graphite/Stone shown although not a configured purchase option; medal-match missing |
| 70401314750630 | 11 | Measurement claims are not yet verified; conflicts with measurement warning |
| 70401314717862 | 12 | Directs Shopify customers to Etsy Messages |

Fresh variant image read before detachment returned null for all eight variants, so no assigned variant image was cleared. Fresh product readback confirms the other ten images retain their order, description matches the intended HTML exactly, and variant IDs/titles/prices/inventory match the before snapshot. Rendered dev product shows the new heading/intake link and zero image elements using the three detached sources. The original accent and dimensions graphics were visually inspected from their existing Shopify CDN URLs; Etsy graphic inspected in the saved audit capture matching the current source.

Before: trace-content-handoff-before.json. After: trace-content-handoff-after.json. These snapshots contain exact public product copy, media URLs/IDs/order and variant values.

## Rollback

Restore descriptionHtml from the before snapshot only after checking for intervening merchant edits. Reattach each retained file using fileUpdate with its MediaImage ID and referencesToAdd: [gid://shopify/Product/15807121490086]. Restore gallery order using the full before-snapshot media sequence (productReorderMedia or Admin drag ordering); just reattaching appends files and is not a complete order rollback. Do not delete/re-upload originals. No variant-image assignments need restoration because all were null. Code/documentation reverts do not undo Shopify content.

## Remaining gates

P0-03 is partially improved: purchase and description intake links exist and the Etsy-only graphic is absent. Order-confirmation installation requires the currently signed-out Admin session; actual two-piece delivery, proof approval and post-payment tests remain open. P1-05 still needs verified exterior/insert/map measurements; removing an unverified graphic is not measurement verification. Accent replacements need verified samples matching configured variants. Status remains NOT READY. No paid commitment, payment, customer message or theme publication occurred.
