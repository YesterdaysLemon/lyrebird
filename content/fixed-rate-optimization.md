# Fixed 4x Adam-rate UIFO diagnostic

Date: 2026-09-05 UTC

## Result

The four-run diagnostic completed and passed local Objective-checkpoint
replay. Fixed 4x learning rates beat the stock rates on both fresh topologies:
mean feasible loss was **2.208027348** versus baseline **3.821839915**, with a
mean paired difference of **-1.613812567**. This is a useful two-topology
mechanism lead. There was no promotion criterion at n=2, and no optimizer was
uploaded or assigned a new public score.

The replacement rental was deleted and cleanup verified. Its conservative
cost bound is **$1.37**; an earlier provider failure before container creation
adds **$0.14**. Including the two preceding studies, the combined conservative
bound is **$13.78**, below the $14 ceiling. These are allocation-time bounds,
not settled provider invoices.

## Frozen comparison and endpoints

The [prepared plan](2026-09-05-fixed-rate-uifo-plan.md) selected the 600-second
option solely from the preceding study's verified conservative cost. Both
arms use the unchanged `BatchedRestartAdam`, optimizer seed **91**, population
8, stock anchor plus paired random starts, patience 600 and the same public
pre-clock warmup. The sole optimizer-setting change is geometric learning-rate
endpoints **0.03--0.15** versus **0.12--0.60**. There is no adaptive gain,
polishing, new restart rule or extra evaluation mechanism.

The D/H panel remained untouched through all preparatory revisions and the
failed provider start. Generator seeds are 2026091504 and 2026091501; topology
identity, initial-array hashes and runtime pair exactly within each block.
Known local panels/plans were excluded by exact identity. No official-archive
or hidden-panel exclusion is claimed.

| Topology | Baseline | Fixed 4x rates | 4x minus baseline |
| --- | ---: | ---: | ---: |
| 1 (D) | 3.541691990 | **1.367611327** | -2.174080663 |
| 2 (H) | 4.101987839 | **3.048443369** | -1.053544470 |
| Mean | 3.821839915 | **2.208027348** | **-1.613812567** |

All **four runs** returned finite feasible results within their 600-second
logged budgets, totaling **15,640 evaluations**. The run order was D baseline,
D rate_4x, H rate_4x, H baseline. Each worker had fresh process and optimizer
state; only compilation was cached. There was no scored retry, substituted
topology or source change.

## Evaluation matching, prefixes and population activity

| Arm | Evaluations | Mean evaluations per logged second | Mean finite-feasible fraction |
| --- | ---: | ---: | ---: |
| Baseline | 7,792 | 6.4984 | 59.73% |
| Fixed 4x rates | 7,848 | 6.5453 | 49.63% |

The final minima are unchanged when each pair is truncated to its last common
evaluation count: **3,904** for topology 1 and **3,888** for topology 2. The
observed endpoint lead therefore persists after matching evaluations. The
4x arm produced a smaller feasible-point fraction, showing that more feasible
evaluations alone are not the explanation for its better minimum.

| Replayed logged prefix | Baseline mean | Fixed 4x mean |
| --- | ---: | ---: |
| 150 s | 4.309412328 | 4.255287931 |
| 300 s | 4.245789772 | 2.943473531 |
| 450 s | 3.911687584 | 2.328010974 |
| 600 s | 3.821839915 | 2.208027348 |

These prefixes reuse the same four histories; they are not extra independent
experiments. The panel mean already favored 4x at 150 seconds, but most of the
gap appeared later. The 4x final minima first occurred at **592.74 seconds**
on topology 1 and **248.15 seconds** on topology 2. Baseline final minima first
occurred at 570.77 and 371.51 seconds.

The winning 4x points came from non-anchor lanes **6 and 7**, respectively
(zero-based indexing). Each 4x run had incumbent improvements from five
different lane positions. This diagnostic exercised population exploration,
rather than only the common anchor trajectory seen in some earlier short CPU
checks. It does not establish how the same lanes or rates behave on new seeds.

## Limits on interpretation

This experiment has two topology units and one paired optimizer seed per unit.
It provides neither a calibrated significance claim nor an estimate of
within-topology seed variability. The settings are deliberately simple, but
the physics trajectories remain sensitive to numerical and stochastic
variation. Relevant longer-budget comparisons and fresh topologies/seeds are
still needed before promotion.

**Do not rank fixed 4x rates directly against sign-adaptive Adam from the
preceding study.** Those results used different topologies, optimizer seeds
and a different GPU driver. Their absolute means are not a paired comparison.
This diagnostic also cannot determine whether constant larger steps explain
the adaptive arm's earlier gain; that requires comparing them on a common
fresh panel with matched budgets.

The result is at **600 seconds**, not the competition's four-hour budget.
It is not a public-leaderboard score, an estimate of hidden-score improvement,
or authorization to submit or spend further. The retained package remains
unchanged.

## Provider failure, replacement and cleanup

The first host repeatedly reported a missing Docker layer while trying to
create its container. It never created a usable container, started the
experiment or logged a physics evaluation. Its initialization log and
`failed-start-cost.json` are preserved under
`artifacts/generated/rate-uifo-20260905-v3-600/rental/`. Cleanup was verified at
**2026-09-05 03:28:53.9914814 UTC**. The 308.678137-second conservative
allocation interval contributes the separately recorded **$0.14** bound.

The coordinator copied the same frozen plan and source bundle to a replacement
host. Their bytes and source-member hashes match the previously prepared
artifacts. This was a replacement of failed infrastructure before physics,
not a retry of an unfavorable scored run. All four scored runs then completed
once, and cleanup was verified at **2026-09-05 04:21:26.265421 UTC**.

The replacement interval from create intent through verified deletion was
**3,069.808788 seconds**, within its 55-minute ceiling. At the conservative
all-in hourly bound of $1.60, the rounded bound is **$1.37**. Worker wall time
totaled **2,818.06 seconds**; per-run overhead outside logged search ranged
from **52.10 to 164.63 seconds**. The failed first allocation is charged
separately rather than hidden inside the replacement deadline.

The final combined bounds are:

| Allocation | Conservative bound |
| --- | ---: |
| Prior H100 study | $8.51 |
| Continuous-explorer A100 study | $3.76 |
| Failed rate-study provider start | $0.14 |
| Completed replacement rate study | $1.37 |
| Total | **$13.78** |

The coordinator verified an empty pod inventory and zero current compute
spend per hour after cleanup. Both local state receipts record
`cleanup_verified=true`. Provider-ledger reconciliation remains separate from
these conservative allocation bounds and does not require keeping hardware
running.

## Runtime and evidence artifacts

The four workers reported **NVIDIA A100-SXM4-80GB**, 81,920 MiB, MIG Disabled,
driver **580.159.04**, Python 3.12.13, JAX 0.9.0.1, dfbench 0.3.3 and x64
enabled. The independent history auditor verifies the saved Objective NPZ
losses, feasibility, counts, timestamps, initial parameters, source/runtime
pairing and minima against JSON. In particular, unconstrained checkpoint
`best_loss` is never substituted for the finite-feasible score. The coordinator's
local replay passed all four runs and reproduced the GPU report.

- Plan SHA-256:
  `c5c315c78c78165a57e916fcc839e637a15600b33e50cc11dd4f97fb7ece1e90`.
- Frozen source-bundle SHA-256:
  `331c3f2ea48d4a35e099a47e2b744cb310637a738e465433df8f1c3e2d6511db`.
- Local audited analysis SHA-256:
  `2acb653e12aabc8285b793a9db078c7d85265eb14390ecbfb7f672b3a5aa6c5b`.

Raw and derived results are under
`artifacts/generated/rate-uifo-20260905-v3-600-host2/results/`:

- `analysis.json`: four-run NPZ replay, paired differences and explicit
  no-promotion/no-quality-rejection status.
- `final-comparison.csv`: endpoint, evaluation count, timing, feasible fraction,
  common-evaluation minimum and incumbent-lane details.
- `budget-ladder.json`: all four time prefixes and matched-evaluation results.
- `progress-time.png` and `progress-evaluations.png`: complete two-topology plots.
- `final-data-summary.json` and `derived-artifacts-manifest.json`: aggregate
  data, verification results and derived-file hashes.

The existing plotting and prefix tools generated these artifacts. All four
plotted minima match the audited endpoints, and both rendered figures were
visually inspected. Generated histories and figures remain outside Git. This
completed comparison changed no frozen optimizer source or uploaded package.

The 47-member evidence archive is 24,176,132 bytes, SHA-256
`9a5bafb65bac9687f7557c64172fc47c5319b617ccef45344064c8571aa43f98`.
ZIP integrity, every member hash, and an identical second local copy under
`learn2design-runpod-results/rate-uifo-20260905/` were verified. The archive
includes the provider-startup failure receipts separately from the four
completed scientific runs.


## Public evidence release

For this Lyrebird edition, the four generated-topology histories, JSON records, frozen plan, independent replay analysis, and original nine-member source bundle are available in the [evidence archive](/papers/fixed-rate-optimization/evidence.zip). Rental records and official competition data are excluded. Archive SHA-256: `c5d5b69e2f19eeb0bd9d36e1d7381bf9a740919e28d3d36cd561ca0d4181e2b9`. The original project and its license remain the source of the optimizer code.
