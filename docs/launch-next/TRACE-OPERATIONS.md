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

## Approved deadlines and manual queue (22 September 2026)

The queue now reports due dates; **nothing sends email, cancels/refunds an order, deletes a file, or starts production automatically**. An operator must run and reconcile it daily against Shopify, Jotform and the mailbox. Existing pieces have no invented request dates: record evidence-backed scheduling events before relying on their queue. Shopify cancellation/refund applies to the real order/affected lines, not independently to each unit; reconcile multi-piece orders and payments before taking action.

Use `queue --at 2026-09-23T00:00:00Z` for a deterministic report, or omit `--at` for current time. Times require a timezone, and the queue displays UTC. Deadlines are elapsed calendar hours/days, including weekends. Event timestamps cannot precede the last recorded event; `usable_at` can separately identify the earlier actual receipt of complete usable intake. Do not postpone that timestamp to the time an operator reviewed it.

Additional events use the same evidence, event ID, expected revision and private persistence rules:

| Event | Required additional evidence/fields | Queue behavior |
|---|---|---|
| `input_requested` | `request_id` of the actual sent instructions/clarification; `request_kind` is `intake` or `clarification`; `at` is the actual request time. | Response due in 48 hours, reminder at 48 hours, final reminder at day 7, manual cancellation/full-refund review at day 10 without a response. Cannot silently replace an unanswered request. |
| `customer_replied` | Current exact `request_id`; independently verify the customer's reply. | Stops that request's nonresponse clock. Does not approve a proof or resolve invalid input. Record a new clarification request if needed. |
| `intake_usable` | `usable_at` is when complete usable inputs became available; `complete_usable_verified: true`; complete intake and independently verified route must already exist. | First proof due 48 hours after `usable_at`. Cannot reset/extend this clock. |
| `delivered` (existing proof-delivery event) | Existing exact proof and verified delivery evidence. | Records first proof delivery and starts a new 48-hour response deadline for this proof, with its `message_id` as request ID. Later proof versions get their own response clock. |
| `reminder_sent` | Current `request_id`; `stage` is `48h` or `day7`; evidence of actual manual reminder. | Suppresses only that recorded reminder stage. Rejects early/duplicate stages. Does not restart the 10-day clock. |
| `approve` (existing event) | Existing version-specific written approval requirements. | Clears the current response deadline. Silence never supplies approval. |
| `item_delivered` | Carrier/customer delivery evidence and actual delivery timestamp; written approval must exist. | Customer-file deletion review due 14 days after item delivery; this is distinct from digital proof `delivered`. |
| `cancelled_refunded` | Evidence of completed cancellation and full refund; `full_refund_verified: true`. | Closes this piece, blocks further production workflow and schedules deletion 14 days after cancellation. Merely reaching day 10 never records a refund. |
| `files_deleted` | `deletion_verified: true`; `checked_locations` exactly `jotform`, `drive`, `local`, `working_files`, `proofs`, `backups`; independent deletion/reconciliation evidence. | Marks manual deletion review complete. It does not remove any file. Do not attest complete deletion if provider backups still conflict with the published policy. |

At day 10, the queue presents cancellation/refund review instead of stale reminder tasks. Verify that no reply arrived outside the ledger before cancellation. Missing/invalid input and no-response states continue to prevent production. After approval but before production, cancellation remains a seller decision; after production begins, the published cancellation restriction applies. The ledger has no production-start or financial integration and cannot decide eligibility by itself.

Deletion scope includes customer-submitted files, raw routes, route-bearing working files, proofs, copies and relevant backups. The private ledger receipts can themselves contain personal data and private route references. Review/purge or minimize those records and temporary event files too, retaining only necessary transaction, approval, refund and deletion records without the route files. This tool does not perform minimization, determine legal recordkeeping requirements, provision sole-operator access or verify provider deletion/backup behavior. No unconditional cross-provider deletion guarantee is established by a queue entry.

Rollback: stop the queue or revert the deadline code; no external actions are reversed. Back up private ledgers under the approved retention rules before reverting. New `policy` metadata and event receipts must be preserved for reconciliation; older code does not recognize the new scheduling events. Actual sent messages, refunds, cancellations and deleted files require separate provider-specific handling and cannot be undone by a Git revert.

Verification: 22 synthetic tests pass, including exact 48-hour/day-7/day-10 boundaries, timezone conversion, first-proof clock preservation, reply/re-request behavior, verified proof delivery and approval, delivery/cancellation deletion deadlines, storage-check requirements, chronological/early reminder rejection, and the original 14 workflow/persistence tests. No live reminder, refund, deletion or proof response was exercised by these tests.

Proof reminder safeguards: re-sending the same proof is a reminder, not a new response window. Delivered proof versions and artifact hashes are remembered; reuse of either cannot restart the clock. A genuinely changed proof must have a new version and artifact. Pending intake/clarification requests require a recorded reply before proof delivery can replace their timer. Deletion completion timestamps cannot precede closure. These safeguards have three additional synthetic regression tests. Legacy records without delivered-proof history must be reconciled before using new scheduling events; no past delivery dates are inferred.
