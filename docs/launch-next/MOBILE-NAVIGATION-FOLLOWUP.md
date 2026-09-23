# Controlled mobile navigation and inquiry checks — 22 September 2026

Exact unpublished teklo-theme/dev 196729798822 identified by preview bar. Browser viewport overridden to 390×844 and 360×800, then reset. This is desktop Chromium at controlled widths, not iPhone Safari, Android Chrome or touch emulation.

## Results

- At both widths: Menu opened; four launch links visible; Tab entered Shop; Escape closed the drawer and returned focus to Menu. Read-only DOM check after the closing animation confirmed details.open=false and active element aria-label=Menu. At 360 px, Shop's focus outline was visually visible.
- Homepage width: innerWidth 390/document scrollWidth 375, then 360/345 (desktop scrollbar accounts for the difference). No horizontal page overflow in these sampled states.
- At 390 px: Start a Conversation expanded, displaying file types/count/size and a direct form fallback. Embedded Jotform loaded the current Custom Work form. Tab from the disclosure reached the fallback; next Tab entered First Name in the iframe. Inquiry collapsed successfully after switching to 360 px.
- Embedded form at 390 px measured 345 px wide with left edge 15 px. Visual inspection shows readable wrapped labels and fields inside the page. It has a separate internal scrollbar; this is an observed behavior, not a touch-usability pass.
- Screenshots: audit-2026-09-22/22-custom-work-390.png and 23-menu-360.png. Shopify's preview bar remains visible and overlays the viewport bottom.

## Limits

No form submitted, no file uploaded and no customer email sent. No screen reader, on-screen keyboard, pinch/200% zoom, touch interaction, image zoom, complete cart/checkout at these widths, or performance measurement exercised in this check. Earlier cart evidence remains separately scoped. No new mobile-complete or READY claim.

Two Playwright locator clicks timed out at the browser-control layer without opening the menu. Documented accessible-element click succeeded; screenshots and final DOM state establish actual behavior. These tool timeouts are not classified as storefront menu failures. Accessibility state captured immediately during closing animation briefly retained expanded=true; the later DOM check confirmed closed state and returned focus.

This follow-up changes evidence only. There is no theme/configuration mutation to roll back.
