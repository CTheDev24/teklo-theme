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

## Homepage footer simplification — 22 September 2026

- Moved the existing philosophy section, including its maker seal and unchanged copy, from the homepage to the end of the Studio page.
- Removed the homepage Custom Work invitation; the existing navigation and upload-enabled Custom Work page remain the inquiry route.
- Removed the full-width Studio Notes section and enabled the native Shopify footer newsletter globally, labeled Studio Notes. Follow on Shop remains alongside it on desktop and below it on mobile.
- Updated only templates/index.json, templates/page.studio.json, sections/footer-group.json and assets/teklo-footer.css on unpublished theme 196729798822. Pulled back all four files and confirmed exact matches after newline normalization.

Validation: Theme Check has 0 errors and the same 10 baseline warnings in actual theme files (ignored review backup copies excluded). git diff --check passed. Browser verified the homepage ends at the Home Objects/Studio cards, exactly one newsletter email input, required email semantics, and philosophy appears exactly once on Studio. Desktop footer visually inspected. At controlled 390px and 360px widths, page scroll widths were 375px and 345px; email field bounds remained inside the viewport. No real-device/touch pass or newsletter delivery claim: no valid subscription was submitted. The attempted blank-submit browser action timed out, so native validation interaction is not marked passed.

Rollback: restore the four files from parent commit 4c977c0 (or revert the footer simplification commit), then push only those four files with --nodelete to theme 196729798822. Exact pre-deploy copies also remain locally in review/homepage-footer-before/. No Shopify-hosted policies, products, menus, apps, or email automation were changed.
