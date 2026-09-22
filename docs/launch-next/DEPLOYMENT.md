# Draft-theme deployment

Commit `51eacb058770211cde63f624f70523cc1f6ca6c7` theme files deployed on 21 September 2026 to **teklo-theme/dev**, theme **196729798822**, store `at3dshop.myshopify.com`. CLI theme list confirmed **unpublished** before deployment; push response again confirmed **unpublished**. The live theme remained `191513952422`. No publish command, theme configuration change or deletion was performed.

[Draft preview](https://at3dshop.myshopify.com?preview_theme_id=196729798822)

## Scope and verification

Only these 14 files were pulled, backed up and pushed with repeated `--only` flags and `--nodelete`:

- assets/product-form.js
- assets/teklo-custom-work.css
- sections/teklo-custom-work.liquid
- locales/pt-PT.json
- locales/ro.json
- locales/ru.json
- locales/sk.json
- locales/sl.json
- locales/sv.json
- locales/th.json
- locales/tr.json
- locales/vi.json
- locales/zh-CN.json
- locales/zh-TW.json

Before pushing, compared remote files with parent commit `918361f` (the dev baseline). The section matched. The other 13 remote files differed from that partial-sync baseline but matched the earlier committed `codex/fix/prelaunch-readiness` versions exactly after line-ending normalization. There were **no unexpected merchant edits**. In particular, the remote theme already contained the Trace validity guard and fallback translations: those repairs restore repository parity, not a newly fixed live behavior. New remote behavior is the section-unique iframe selector and keyboard focus styling.

Push completed successfully. An independent pull into `review/launch-next-readback/` verified **all 14 files byte-for-byte equal** to the deployed working files. Local readback hashes are in its `hashes.json`. This confirms deployment contents, not browser usability or checkout readiness.

## Rollback

Pre-deployment remote files are stored locally in ignored `review/launch-next-before/`. This is deliberately not included in the PR. Preserve that directory until final release acceptance. To roll back, first confirm the theme remains unpublished and no later merchant changes must be preserved; then from this checkout use:

```powershell
$files = @(
  'assets/product-form.js', 'assets/teklo-custom-work.css', 'sections/teklo-custom-work.liquid',
  'locales/pt-PT.json', 'locales/ro.json', 'locales/ru.json', 'locales/sk.json',
  'locales/sl.json', 'locales/sv.json', 'locales/th.json', 'locales/tr.json',
  'locales/vi.json', 'locales/zh-CN.json', 'locales/zh-TW.json'
)
$themeArgs = @('theme', 'push', '--store', 'at3dshop.myshopify.com', '--theme', '196729798822', '--path', 'review/launch-next-before', '--nodelete')
foreach ($file in $files) { $themeArgs += @('--only', $file) }
shopify @themeArgs
```

If that local backup is unavailable, reconstruct these 14 files from the earlier `codex/fix/prelaunch-readiness` branch, whose content was verified against the pre-deploy remote files, and compare before uploading. Do not use `918361f` for rollback because it lacks changes already present remotely. Shopify product-media rollback is separate and documented in `MEDIA-CHANGES.md`.

CLI calls used agent attribution `n:codex|v:desktop|p:openai` and `r:launch-next-20260921|i:theme-hardening`. Reference: [Shopify theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push).
