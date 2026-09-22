# Homepage corrections — 22 September 2026

Applied only to unpublished `teklo-theme/dev`, ID196729798822. Theme list and storefront preview bar verified the intended target; live theme191513952422 was not published or changed.

- Removed the introductory Trace and Purposeful Objects text columns using the section's new image/caption-only setting. Kept People, Places, Purpose in3D.
- Replaced its Trace photo with the existing active Modern Art Deco Wall Clock listing photo, product15295976439974. Visually inspected the blue ridged clock with houseplants; descriptive alt text added. Full image aspect ratio retained.
- Kept the neutral-green Trace product feature, specs, starting price and Customize Trace link.
- Removed the two graphic blocks below that feature and omitted their empty wrapper.

Changed files: templates/index.json, sections/teklo-introduction.liquid, assets/teklo-introduction.css, sections/teklo-trace-launch.liquid. Before deployment, all four remote files matched the branch after newline normalization. Backups are in ignored review/homepage-before/. Readback is in review/homepage-after/; all four match the deployed files after newline normalization.

Shopify initially stripped newly introduced template settings because template/schema were uploaded together. Reapplied only index.json after schema save; independent readback then matched and the browser confirmed both duplicate columns absent and the new clock image loaded.

Validation: Theme Check0errors/10existing theme warnings;93additional warnings came from ignored backup copies scanned under review/, not deployed theme files. No findings in changed files. The Liquid skill validator failed to load its bundled theme-check dependency; Shopify CLI Theme Check supplied validation. Desktop screenshot and accessibility tree verified the clock/caption, single Trace feature and removed lower photos. At390px and360px controlled viewport, no document horizontal overflow; image loaded. At360px clock bounds15–253px and caption277–330px fit. This is layout verification, not real-device/touch or full accessibility sign-off. Draft preview retained for merchant review.

Rollback: reconstruct these four files from parent commit a7ca2e7 or use review/homepage-before/ after checking for newer merchant edits. Push only these files with --nodelete to theme196729798822 while still unpublished, then pull back and verify. No Shopify product image asset was replaced/deleted; only its homepage selection changed. No product, policy, shipping, discount or app settings changed.
