# Trace private operations ledger — launch follow-up

Status: implemented and tested **offline only**. This is a manual operator tool, not a Shopify/Jotform integration, email service, authenticated approval portal, fulfillment system or launch sign-off. It records independently verified evidence. A boolean in an event is an operator attestation; this program cannot verify the sender or whether a message actually arrived.

## Run and private storage

From this checkout, use Python 3.10+:

```powershell
python -m unittest discover -s tests -v
python -m tools.trace_operations --help
python -m tools.trace_operations --root C:/PRIVATE_TRACE_LEDGER init --shop STORE --order IMMUTABLE_ORDER_ID --line IMMUTABLE_LINE_ID --unit 1 --quantity 2
```

`C:/PRIVATE_TRACE_LEDGER` is an example, not a configured or approved storage location. Choose an access-controlled private folder outside this repository and outside publicly shared/synced folders. The CLI refuses storage inside ordinary Git checkouts; it does not provision filesystem permissions, encryption, backups or retention. Volume-root Git markers are ignored. Never store real order events, proofs, routes or command output in this repository, PR or public logs.

Repeat `init` for unit 2 to get its independent piece ID. Reconcile each unit against the actual Shopify order/line, purchased quantity, order email and submitted piece reference first. Never accept a customer-entered order number as authentication. Quantity changes/refunds require operator reconciliation; this ledger does not track Shopify changes automatically.

The returned 64-character `piece_id` identifies the private JSON ledger. Read it before each edit:

```powershell
python -m tools.trace_operations --root C:/PRIVATE_TRACE_LEDGER show PIECE_ID
python -m tools.trace_operations --root C:/PRIVATE_TRACE_LEDGER apply PIECE_ID --expected-revision 0 --event C:/PRIVATE_EVENT_FOLDER/intake.json
python -m tools.trace_operations --root C:/PRIVATE_TRACE_LEDGER queue
```

Event files use UTF-8 JSON. Use a new stable event `id` for each real operation. Retry the identical event with the same ID after an uncertain result; it is applied once. A reused ID with changed evidence or a stale revision fails. `show` includes private intake/history; do not paste its output into public tickets.

## Events and evidence

Every event requires `id`, `type`, `at` (ISO date/time with timezone) and `evidence` (a private source reference, such as submission ID, retained message or operator review record). Preserve original evidence privately; the CLI records hashes of artifact bytes, not an archive of the artifacts. GPX/proof file paths should be absolute and accessible locally. No URL is fetched.

Synthetic intake example (replace only from verified order/submission data):

```json
{
  "id": "submission-SYNTHETIC-piece-1",
  "type": "intake",
  "at": "2026-09-21T20:00:00Z",
  "evidence": "synthetic-only",
  "verified_key": ["STORE", "IMMUTABLE_ORDER_ID", "IMMUTABLE_LINE_ID", 1],
  "data": {
    "runner": "Synthetic Runner",
    "race": "Synthetic Race",
    "date": "2026-09-21",
    "location": "Synthetic Location",
    "distance": "10K",
    "finish": "Nocturne",
    "accent": "Signal Orange",
    "route_method": "gpx",
    "route_source": "private submission attachment reference",
    "omit_finish_time": true
  }
}
```

Missing required values produce `NEEDS_INPUT`. Preserve long names without silent truncation; review the actual layout later. Use `finish_time` or explicitly set `omit_finish_time: true`.

| Event | Additional fields / operator action | Result |
|---|---|---|
| `intake` | Verified exact `verified_key` and `data` above. For `activity`, require `activity_url` with an HTTPS URL; for `course`, require `course_name`, `course_year`, `course_distance`, `course_location`; for `gpx`/`map`, require `route_source`. | Complete input → `AWAITING_ROUTE`; new intake clears old route/proof/approval. |
| `route` | `gpx_file`: private absolute GPX path; `source_verified: true`. Independently compare course/year/distance or activity to the submitted request and retain review evidence. | Structural GPX validation plus recorded verification → `AWAITING_PROOF`. Every source alternative must converge on accepted GPX; no automatic course lookup/conversion is claimed. |
| `proof` | `proof_file`: private absolute proof path; unique `version`; `layout_reviewed: true`; `color_confirmed: true`. Review spelling, long names, time/omission, course/crop, finish and medal color. | Stores proof hash, route hash and revision → `AWAITING_PROOF_DELIVERY`; clears any old delivery/approval. |
| `delivered` | Copy exact current `proof` object from `show`; `message_id`; `recipient_verified: true`. Evidence must independently demonstrate delivery to verified order contact. | `AWAITING_APPROVAL`. A send attempt or stored local file alone is insufficient evidence. |
| `approve` | Exact current `proof`, exact `verified_key`, `sender_verified: true`, and `text: "APPROVED FOR PRODUCTION"`. Preserve actual written reply identifying order, piece and proof version. | `APPROVED` for this exact piece/proof only. It does not start production. |
| `invalid_input`, `private_link`, `unavailable_course`, `color_unclear`, `correction` | Evidence identifies the specific problem/correction. | `NEEDS_INPUT`; route, proof, delivery and approval cleared, including previously approved work. Reconcile input and reverify route before proofing. |
| `no_response` | Record why customer input/approval is still awaited. | `HOLD_NO_RESPONSE`; no approval, automatic reminder, deadline, cancellation, refund or deletion. |
| `resume` | Record newly received reply or verified reason the nonresponse hold is resolved. | Restores prior waiting state. It does not supply missing input or approve a proof. |

A private activity link, unavailable course or ambiguous medal color needs clarification through a verified channel. Do not bypass the hold by asserting verification. A new proof or route invalidates earlier approval. The existing `CANVA_APPROVED` and map-generation human gates in Trace order operations remain independent and mandatory; this ledger does not write canonical `order.md` or supersede those gates.

## Persistence and recovery

One JSON file contains state plus append-only event receipts. Updates take a per-piece exclusive lock, compare the expected revision, write/fsync a temporary file, then replace the ledger atomically. Invalid events leave state unchanged. This supports a local single-machine operator workflow, not distributed multi-user/network-drive transactions or a tamper-proof audit log. Event evidence is trusted operator input.

If the process is interrupted, read the current ledger and retry the same event ID. A stale `.lock` can remain after a crash: verify no writer is running and back up the ledger before manually removing only that piece's lock. Do not remove an active lock. Maintain private backups according to the merchant-approved retention practice; no retention duration is invented here.

Rollback: stop using the CLI; no external services or Shopify settings were changed. Preserve privately stored records/evidence for reconciliation. Revert these code files if needed, without deleting order evidence or overwriting existing Trace order workspaces.

## Verification and remaining live work

Fourteen synthetic tests cover all four source paths, malformed/unsafe GPX, missing fields/finish time, long names, unit bounds, two pieces, exact proof revisions, delivery-before-approval, approval revocation, nonresponse holds, persistence/retries/revision conflicts, locked writes, private-path checks and CLI init/queue.

Not exercised: actual Shopify order matching, Jotform Trace submission/upload receipt, activity access/course conversion, real sender/domain authentication, email delivery/replies, live two-piece proof approval, payment/shipping/tax/refund, production or retention/deletion across providers. Custom Work attachment delivery does not prove these Trace paths. P0-03 remains open until the complete authorized test order is exercised with independently verified evidence.
