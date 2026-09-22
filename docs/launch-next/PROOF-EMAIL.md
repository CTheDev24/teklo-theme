# Proof-email implementation — 22 September 2026

Implemented a local reusable draft generator at `tools/proof-email/index.html`. Load a canonical order.md, confirm the exact piece/unit, drop the finished proof/render and enter its version. Customer, order, race, finish and accent values populate from the record. Required absent values must be supplied; no order lookup or recipient inference is claimed.

Output: personalized plain-text email preview plus unsent multipart EML with PNG/JPEG/PDF attachments. Includes version-specific written approval text, approved48-hour response window,8–10-business-day production terms and nonresponse/cancellation wording. Uses orders@teklostudio.com in From/Reply-To; actual sending-account authentication remains separate.

No Shopify, Jotform, email-provider or theme configuration changed. Nothing was sent. No delivery/approval/reminder/production state is changed. Discounts remain disabled. No paid app is needed for this local tool.

Core and UI-state unit tests cover canonical import (including backtick-wrapped values), duplicates, missing values, recipient/header validation, attachment bytes and type/size rules, exact approval identity, changing order/recipient, stale review prevention and invalid replacement proofs. These are not visual browser or mail-client tests. Browser automation rejected the local file URL; no workaround was attempted. The merchant still needs to open a synthetic draft in the chosen Apple Mail/Outlook version, inspect attachments and exercise authorized delivery/reply matching.

The order-confirmation insert remains a separate staged Shopify notification change. This proof tool does not install it or make the complete Trace workflow ready.

Rollback: stop using/remove the local generator; external settings need no rollback. Preserve already-sent proof and approval evidence. Keep generated customer emails, attachments, downloads and clipboard copies out of Git and within the existing private-file handling/deletion process.
