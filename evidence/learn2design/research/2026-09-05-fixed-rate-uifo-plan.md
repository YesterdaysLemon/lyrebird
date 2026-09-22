# Conditional fixed-rate UIFO diagnostic

Prepared without reading the active GPU outcomes or launching paid compute.
The active three-arm/twelve-run screen remains frozen and unchanged. This
separate four-run study now has two mutually exclusive prepared budget options, conditional on the
coordinator verifying that the complete additional allocation and cleanup fit
the remaining owner budget. It is not an automatic continuation.

## Question and frozen contrast

Would simply multiplying the retained Adam learning rates by four produce a
useful lead on fresh detector topologies? This is a low-cost control for the
idea that larger steps may be useful. It does not establish that constant
rates explain the adaptive arm's behavior on a different panel.

Both arms use the unchanged `BatchedRestartAdam`, population 8, random
initialization with the stock anchor, patience 600, optimizer seed **91**, and
the same public pre-clock warmup. The sole optimizer-setting difference is
the geometric learning-rate endpoints:

| Arm | Low rate | High rate |
| --- | ---: | ---: |
| `baseline` | 0.03 | 0.15 |
| `rate_4x` | 0.12 | 0.60 |

Each run receives **600 or 900 logged seconds**, selected solely by the frozen
cost rule below, on the same A100 80 GB device. Seeds,
initial arrays, topology identity and runtime must pair exactly within each
topology. There is no adaptive gain, new restart rule or polishing in either
arm. Both rate bounds and all other settings are fixed before outcomes.

## Untouched topology panel

The preparation step reads topology identities from existing checked-in
panels and generated `plan.json` files; it does not read result scores or
curves. It records hashes of the exclusion inputs. Starting from generator
seed 2026091501, it takes the first unseen D-readout topology and the first
unseen H-readout topology. The selected generator seeds are **2026091504 (D)**
and **2026091501 (H)**. Exact strings and descriptors are in the private plan.

Run order is D baseline, D rate_4x, H rate_4x, H baseline. Each worker is a
fresh isolated process; compilation cache reuse is allowed but optimizer
state never crosses workers. This is exact exclusion against known local
panels/plans, not an official-archive or hidden-panel exclusion claim.

## Scope, cost and completeness

The executable `BUDGET_CHOICES` map admits only these complete configurations:

| Choice | Seconds per run | Worker timeout | Internal session ceiling | Absolute rental ceiling | Reserved cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| `600s` | 600 | 800 s | 3,100 s | 55 min | $1.47 |
| `900s` | 900 | 1,080 s | 4,320 s | 75 min | $2.00 |

The owner-host supervisor must enforce the absolute ceiling from **rental
create intent to verified deletion**; setup, transfers and cleanup are
included, not added afterward. The hourly all-in offered rate must be at most
**$1.60**, including storage. At that ceiling, 75 minutes costs $2.00 and 55
minutes costs $1.4667, rounded upward to $1.47. The prior quoted $1.59 compute
plus approximately $0.00556/hour storage fits that ceiling, but the coordinator
must revalidate the actual offer and disk charges.

The frozen choice uses only the independently verified conservative final
allocation cost of the current study, called C:

1. Choose `900s` if **8.51 + C + 2.00 <= 14** (C <= $3.49).
2. Otherwise choose `600s` if **8.51 + C + 1.47 <= 14** (C <= $4.02).
3. Otherwise **do not launch** either option.

`select_budget` implements these inclusive boundaries using decimal
arithmetic. It does not verify the supplied cost or provision resources; the
coordinator owns that verification. No loss, rank, trajectory or rate-study
outcome enters the choice. Select one option only; the other remains
unexecuted. Use the actual verified completion/deletion interval and applicable
rates, not an estimate that assumes an unfinished study will finish cheaply.

The external deadline is the spending boundary. The runner checks that its
remaining internal envelope covers a full next-worker timeout before starting
it. Compilation or transfers can still consume the small margin; this plan
does not guarantee all four runs will finish. No shortened replacement run,
retry, extra seed, topology reroll or budget top-up is included. Preserve
partial artifacts and mark the diagnostic **inconclusive** unless all four
runs finish and pass the complete history audit.

## Evidence and interpretation

The worker keeps the established public `Objective.vmap_value_and_grad_aux`
logging path, saves full parameter/loss/feasibility NPZ histories, and records
the callback's finite-feasible minimum and captured initial-array hash.
The independent `tools.audit_fast_results.audit_run` implementation verifies
the actual NPZ histories against each JSON result, including initial arrays,
budgets, counts, times, runtime, source hashes and minima. Checkpoint
`best_loss` is checked as an unconstrained minimum; it is never substituted
for the feasible score.

The report provides both topology differences, their descriptive mean, run
counts, provenance and incumbent origins. With **two topology units**, there
is no promotion criterion, confirmation-unlocking test or permanent quality
rejection. Neither wins nor a mean difference imply a four-hour competition
gain. A positive result is a mechanism lead for a separately affordable fresh
comparison; a negative short result cannot rule out longer-budget usefulness.
The retained histories already demonstrate early/late ranking reversals.

## Implementation choice and commands

The historical `experiments/uifo_paired` runner was inspected first. Its
supported arms and per-arm settings are tied to prior and patience studies;
adding a rate arm would require changing those historical contracts. The new
`experiments/rate_screen.py` instead uses the stock optimizer directly and
reuses the independent NPZ auditing code. It does not refactor or modify the
active `fast_uifo_screen.py` or submitted optimizer.

Current prepared private artifacts (revision 3, both on the same untouched panel):

| Choice | Private directory | Plan SHA-256 | Bundle SHA-256 |
| --- | --- | --- | --- |
| `600s` | `artifacts/generated/rate-uifo-20260905-v3-600/` | `c5c315c78c78165a57e916fcc839e637a15600b33e50cc11dd4f97fb7ece1e90` | `331c3f2ea48d4a35e099a47e2b744cb310637a738e465433df8f1c3e2d6511db` |
| `900s` | `artifacts/generated/rate-uifo-20260905-v3-900/` | `edd1b64c014c92d2aa30bdd35b28cdc369366e5ea06ff188b51303e70601640a` | `6eb44880ebeae02de9b9b6db1ca5f1dcd7e546524cd0636d456c54505751eabe` |

Each directory contains `plan.json`, `source-bundle.zip` and `readiness.json`.
The nine-member bundles are 72,186 and 72,182 bytes, respectively. The readiness
receipts explicitly leave budget selection pending; both plans bind the same
source revision and record the superseded unexecuted revision-2 plan hash.

The archive contains only the new harness, independent auditor, unchanged
submission source, dependency declarations, frozen plan and empty package
initializers. It contains no official dataset, credentials or prior outcomes.

On an already authorized, source-verified rental, the coordinator can invoke:

```bash
uv run --frozen --group integration --group accelerator python -m experiments.rate_screen --run --plan plan.json --output results
uv run --frozen --group integration --group accelerator python -m experiments.rate_screen --analyze --output results
```

These commands do not provision hardware or install a spending backstop. The
provider supervisor and independent absolute cleanup watcher must already be
running. A nonzero worker/analyzer exit means incomplete evidence and cleanup,
not a reason to continue consuming credits.

### Operating-metadata-only preflight revision

Before any rate-study execution, the coordinator supplied two A100 worker
wall durations, 726.195 and 726.504 seconds, with about 127.5 seconds unscored
overhead per worker and roughly two minutes bootstrap. No new loss, rank,
trajectory or GPU outcome was accessed for this adjustment. These operating
measurements left the old 3,000-second session envelope and 780-second
next-worker reserve tight at the fourth launch. Revision 2 raises those to
3,100 and 800 seconds while preserving the **3,300-second external cap**.

At approximately 727 seconds per worker plus two minutes bootstrap, four runs
take about 3,028 seconds, leaving roughly 272 seconds of the external cap for
transfer and cleanup. This is an operating estimate, not a completion
guarantee; the external deadline and final combined-cost check remain binding.
The revised worker also requires a single MIG-disabled A100 reporting at
least **78,000 MiB**, and the analyzer checks the recorded hardware against
the same lower bound. Rate settings, seed, budgets per run, panel and order
remain unchanged. The two planned topologies were retained because the old
plan was unexecuted; no outcome-informed panel replacement occurred.

The old unexecuted plan and bundle remain byte-for-byte preserved at
`artifacts/generated/rate-uifo-20260905/`. Revision 2 is separately prepared at
`artifacts/generated/rate-uifo-20260905-v2/` and records the old plan hash as
`supersedes_unexecuted_plan_sha256`.

Revision 3 adds the deeper 900-second option before any rate-study outcome
exists. It preserves the two option-independent rate endpoints, population,
restart algorithm, seed 91, run order and untouched D/H panel, and changes
only the selected time/cost envelope. Both revision-1 and revision-2 bundles
were hash-verified unchanged. This is a choice of affordable physics depth,
not outcome-driven algorithm tuning or a second run after seeing the first.

## Unpaid verification

The forty rate-screen tests and twenty-five independent-auditor tests passed
(65 total). They check both complete frozen time configurations, exact cost
boundaries and rejected hybrid configurations, the exact two rate settings, public callback
feasibility behavior including a lower infeasible loss and a nonfinite value,
source-bound deterministic packaging, and deliberate history/provenance
corruptions. The real bundle's CLI imported from an isolated temporary
directory. GPU discovery and worker execution were mocked in the worker test;
no new UIFO objective, GPU comparison or candidate-performance result was run.
The active screen and original uploaded ZIP were not modified.
