# Theme validation — next launch implementation

Validated 21 September 2026 on `codex/feature/launch-readiness-next`.

## Result

- `shopify theme check --path . --output json`: **0 errors, 10 warnings**, exit 0. Raw output: `review/theme-check-next.json`.
- `node --test review/test-product-form-validation.cjs`: **5 passing tests**. Covers invalid Trace references being stopped before cart mutation, valid references continuing, ordinary product behavior, and disabled purchasing.
- `node --check assets/product-form.js`: pass.
- `git diff --check`: pass (Git prints its configured LF/CRLF conversion notices).
- Locale preservation check: all **110 restored keys** equal the values committed on `codex/fix/prelaunch-readiness`; all other parsed locale values equal this branch's original HEAD.

## Partial-sync repairs

Restored three `templates.custom_work` upload keys and seven `teklo.launch` keys in each of: pt-PT, ro, ru, sk, sl, sv, th, tr, vi, zh-CN, zh-TW. These are the previously committed **English fallback values**, not newly translated copy. The missing keys caused MatchingTranslations errors before repair.

Restored the Trace form's explicit validity check, needed because the existing AJAX product form uses `novalidate`. Restored the Custom Work upload container/iframe responsive CSS. Added keyboard focus outlines and a section-specific iframe ID; the handler selector uses the same Shopify-generated `section.id` as the iframe. Shopify section IDs are platform-controlled identifiers, not customer-entered strings; the existing quoted attribute selector accommodates their normal hyphens and underscores. The standalone-form link remains visible if embedding or the remote resizing helper fails. No additional loading state or automatic submission was introduced.

## Remaining warnings

All ten warning types/locations were present in the first check before these repairs; **no new warnings** were introduced. The current baseline includes the existing Jotform RemoteAsset warning, so it is ten rather than the nine recorded before the upload integration.

| File:line | Check | Existing issue |
| --- | --- | --- |
| snippets/quick-order-product-row.liquid:1 | OrphanedSnippet | Snippet not referenced |
| sections/main-list-collections.liquid:20 | VariableName | `moduloResult` naming |
| sections/teklo-custom-work.liquid:54 | RemoteAsset | Official Jotform embed helper served remotely |
| sections/main-article.liquid:102 | VariableName | `anchorId` naming |
| sections/main-search.liquid:274 | UnusedAssign | `product_settings` unused |
| snippets/facets.liquid:865 | LiquidComplexity | Complexity 136 exceeds 120 |
| sections/main-product.liquid:745 | UnusedAssign | `seo_media` unused |
| sections/main-product.liquid:601 | UndefinedObject | `continue` unknown |
| layout/password.liquid:40 | UndefinedObject | `scheme_classes` unknown |
| layout/theme.liquid:84 | UndefinedObject | `scheme_classes` unknown |

## Tool and verification limitations

The Shopify skill's search helper failed with `fetch failed`; official Shopify product-form documentation was consulted as fallback. Its prescribed validation helper was attempted twice but cannot import its missing `@shopify/theme-check-common` package; the installed Shopify Theme Check CLI provided the validation above.

Node tests verify the submission handler gate using a stubbed browser validity result. They do not replace browser testing of native validation/focus, mobile layout, upload delivery, or payment. No deployment, customer communication, or browser submission was performed by this theme subtask.
