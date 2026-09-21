# Applied external changes and rollback

All changes below are separate from theme commits. Theme rollback does not roll back Shopify product, collection, Files or Jotform changes.

## Theme

Before snapshot: `C:\Users\craig\Documents\teklo-theme\.worktrees\prelaunch-backup-196729798822` (full CLI pull). Branch base `bac9539` matches the inspected dev revision. Deployments used explicit unpublished theme 196729798822, `--nodelete` and changed-file lists. No publishing flag.

Restore only files changed by this PR from the snapshot to that same theme, after checking it is still unpublished. Include new `snippets/trace-piece-fields.liquid` only as an unused orphan if using nodelete, or remove it separately after reverting its call. Do not overwrite unrelated Theme Editor edits. Revert the PR commits in Git; do not force-reset dev. Shopify's GitHub integration may mirror draft-theme changes onto dev, so inspect dev before merging/reverting.

## Shopify product/content/media

- Trace ID `15807121490086`: vendor AllThings3DShop → Teklo Studio. Restore old vendor with productUpdate if rollback is needed.
- Trace description: replaced Etsy and unverified launch promises with explicit pre-launch hold, verified $25 price delta, semantic headings/lists, existing custom-return exclusion and cart/product gift-note instructions. Exact before HTML is in `before-product-15807121490086.json`; applied text in `applied-trace-description.html`. Restore `descriptionHtml` from the before snapshot only if intentionally restoring its documented defects. No existing order record/terms changed.
- No variant price, inventory, tax flag, shipping profile or discount changed. All eight original variant values are recorded in the before snapshot.
- Six graphic alt texts: see `applied-media-changes.json`. Restore originals (empty alt text) from before-product snapshot with fileUpdate, not by replacing image URLs.
- Detached product references for media `70354423939238` (dimensions), `70354423775398` (ordering) and `70354423808166` (proof). Shopify Files retained; no permanent file deletion. Rollback: fileUpdate each ID with `referencesToAdd: ["gid://shopify/Product/15807121490086"]`; restore original gallery ordering using the before snapshot. Never recreate duplicate images. Three remaining guide images have new alt text; held images retain new alt text too.
- Soft Face ID `15457467728038`: ACTIVE → DRAFT. Restore ACTIVE only after reviewing copied-specification risk; original snapshot provided. No image/price edits.
- Created manual collection `693016101030`, handle `trace`, containing only Trace. To roll back reversibly, remove Trace membership and unpublish the collection from Online Store; do not delete it. Revert Shop navigation first so it does not point to an empty assortment.
- Store display name: AllThings3DShop → Teklo Studio via General > Store contact details. Restore previous display name there if desired. Store email/phone/legal entity were not changed.

## Jotform

Form `262521531346047`, existing form and existing submission preserved. Before first edit revision: `6aa356ff636363c2f4a13c93`. Subsequent revision starts: `6ab1a767373162c31ec93720`, `6ab1a7cd626330e420482d11`, `6ab1a81a626330e42064fb7a`.

Applied: Shopify order wording; required order email/piece reference/unit/finish/accent; optional medal upload/color description; explicit no-response hold. Removed Etsy proof timing promises. Final builder reports route groups visible and GPX optional, finish time optional with OMIT guidance, and whole-number piece minimum 1. Verify actual public behavior before release. The first large edit returned a misleading partial-success result; subsequent smaller edits were verified for identity fields.

Rollback through Jotform revision history to the saved original revision, preserving submissions. If revision restore is unavailable, restore original order labels/introduction/acknowledgment and route visibility from the documented before state; archive newly added answers before removing fields. Never delete the form or submission. No email recipients, autoresponders, webhooks, retention settings or integrations were intentionally changed; their before/after configuration still requires inspection because the connector does not expose it.

## No changes applied

Billing/plan, payment activation/test mode, shipping rates/zones/taxes, discount 25OFF, support email addresses, policies, notification templates, app billing/installation/configuration, pixels/consent, DNS and retention/deletion automation. Prepared changes live in REVIEW-PACKET.md and order-confirmation-insert.liquid. Do not assume these are live.

## Homepage SEO rollback

Online Store > Preferences: restore title `AllThings3DShop | Custom 3D Printed Items - LED Signs, Vases and More` and description `Explore AllThings3DShop for unique 3D-printed items, from custom LED signs to modern vases and planters. Each piece is crafted with precision and creativity, perfect for home décor, gifts, and custom projects. Bring your ideas to life with our innovative 3D-printed designs!`. Social image unchanged.

Final public form observation: GPX upload has no required validation; finish time optional; all route fields visible. Piece number remains numeric with step any and no minimum despite requested positive-integer constraint. Treat it as untrusted input and hold invalid units during reconciliation. Latest edit starts at revision 6ab1a8fb3731626d9b35d7e6.
