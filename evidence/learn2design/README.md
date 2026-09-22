# Learn2Design: fixed-rate diagnostic evidence

This public snapshot accompanies “Larger steps in detector optimization.”
Original development commit: `1747af93d167e15720cd66b5d1f662eaa48ea299`.
The original project is https://github.com/YesterdaysLemon/learn2design.

- [Result and limits](research/2026-09-05-fixed-rate-uifo-results.md)
- [Frozen plan](research/2026-09-05-fixed-rate-uifo-plan.md)
- [Download the public evidence archive](https://lyrebird.alirezaafshan.com/papers/fixed-rate-optimization/evidence.zip)

Archive size: 23,994,813 bytes. SHA-256: `c5d5b69e2f19eeb0bd9d36e1d7381bf9a740919e28d3d36cd561ca0d4181e2b9`.

The archive contains four generated-topology NPZ histories and JSON records,
the frozen plan, audited analysis, budget prefixes, summary, paired CSV, and
the original nine-member source bundle. It excludes rental/provider records
and any official competition dataset. The source bundle includes the runner,
independent history auditor, unchanged optimizer source, and dependencies.
Its own source provenance is recorded in the frozen plan. The history auditor
uses a restricted NumPy decoder; do not load arbitrary pickle files unsafely.

Fresh replay on September 22, 2026 verified all four histories and reproduced
the mean paired feasible-loss difference -1.6138125667514436. This remains a
two-topology, one-seed diagnostic and is not a public leaderboard score.
Source software retains its original project license and dependency licenses.
