# Synthesa SDLC on SWE-bench Pro

Synthesa SDLC is a custom software-engineering harness that turns unresolved
requirements, failed checks, and missing evidence into explicit next actions.
Those actions can be completed by deterministic automation, a human engineer,
or an AI coding agent while the same verification and provenance controls stay
in place.

In a complete local evaluation of all **731 SWE-bench Pro public tasks**, a
frozen Synthesa prediction set resolved **570 tasks (77.98%)** using the pinned
official evaluator and official per-task Docker images. A second complete run
of the same prediction bytes resolved **569 tasks (77.84%)**.

## Result

| Measurement | Resolved | Rate |
| --- | ---: | ---: |
| Complete evaluation | 570 / 731 | 77.98% |
| Independent repeat, same predictions | 569 / 731 | 77.84% |
| Observed repeat range | 569–570 / 731 | 77.84–77.98% |

The frozen prediction file contains one non-empty patch for every task and
has SHA-256:

`9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f`

## What the harness demonstrated

- **Complete campaign execution:** 731 tasks were carried through to one frozen
  final patch per task.
- **Generator independence:** the campaign used a deterministic/model-free
  control path; the residual, evidence, and verification model does not require
  an LLM.
- **Reproducible measurement:** the same prediction bytes produced 569 and 570
  resolved tasks across two complete evaluator runs.
- **Independent verification:** prediction production was separated from the
  pinned official evaluator and its per-task environments.
- **Auditable provenance:** every prediction row is represented in a
  machine-readable reconstruction, including 18 rows where only lineage—not an
  exact attempt receipt—survived.

## Evaluation protocol

This was an **adaptive, open-material custom-harness evaluation**. Public task
materials and public repository history or tests were available to parts of the
campaign. In seven tasks, a different candidate for the same task had failed a
local official-evaluator run before the final frozen candidate was produced or
selected.

The result is therefore a legitimate measurement of this custom harness under
that protocol. It is **not** presented as one-shot pass@1, unseen-task
generalization, or an organizer-certified SWE-bench Pro leaderboard result.
See [METHODOLOGY.md](METHODOLOGY.md) for the full boundary.

## Why this is relevant to product evaluation

The result shows that Synthesa can coordinate and verify a large software-change
campaign without making AI the trust boundary. The same workflow can accept
candidate work from humans or AI systems while retaining explicit residuals,
frozen decisions, evaluator separation, and replayable evidence.

This package establishes the harness result. Causal claims about engineering
time, cost, quality, human productivity, or AI uplift require a separately
controlled with/without-Synthesa study.

## Evidence

- [`submission.json`](submission.json) — machine-readable result and protocol
  classification
- [`predictions.json`](predictions.json) — all 731 frozen patches
- [`eval_results.json`](eval_results.json) — 731 Boolean evaluator outcomes
- [`prediction-freeze.json`](prediction-freeze.json) and
  [`prediction-freeze-verification.json`](prediction-freeze-verification.json)
  — prediction freeze and verification
- [`provenance-reconstruction-v1.json`](provenance-reconstruction-v1.json) —
  row-level acquisition and chronology evidence
- [`prior-score-569.json`](prior-score-569.json) — complete repeat result
- [`EVIDENCE.md`](EVIDENCE.md) — artifact map, hashes, and verification commands

## Evaluator identity

- Evaluator repository: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
- Evaluator commit: `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`
- Evaluator SHA-256: `bb5d4c5486be296e464e695df3747064aaa3bb197394bc6d39980634afec2034`
- Execution environment: local Docker with the official per-instance images

The evidence is published for technical review by benchmark maintainers,
customers, investors, and engineering teams evaluating Synthesa SDLC.
