# teklo-theme

Shopify theme development for Teklo.

## Closed-loop design review

`review/run-review-loop.ps1` alternates a write-enabled implementation agent, local `shopify theme check`, and an independent read-only reviewer. It stops on acceptance, missing/stale evidence, human judgment, a failed check, or after at most three iterations. It never commits, pushes, merges, publishes, connects checkout, or changes store data.

Prerequisites: check out `feature/*` or `codex/feature/*` (never main/master); install Codex CLI and Shopify CLI; and provide a safe local theme preview that needs no publish or checkout connection.

Validate without starting either CLI:

```powershell
pwsh -File review/run-review-loop.ps1 -ValidateOnly
```

Run the loop (optionally lower the limit with `-MaxIterations 1` or `2`):

```powershell
pwsh -File review/run-review-loop.ps1
```

Every pass must create fresh genuine screenshots at `review/evidence/current/desktop-1440x1000.png` (1440×1000) and `review/evidence/current/mobile-390x844.png` (390×844), with the changed area and context. The runner verifies freshness and PNG dimensions before Theme Check and review.

The schema-constrained reviewer result is written to `review/last-review.json`; `revise` becomes the next implementer's handoff, `accepted` ends successfully, and `human_review` stops immediately. Theme Check output goes to `review/theme-check.txt`. Prompts are separated in `review/prompts/`; the reviewer prompt forbids all mutation. The contract is `review/review.schema.json`.
