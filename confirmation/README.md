# Seven-row confirmation

This directory contains the sealed follow-up experiment for the seven
historical rows whose final patch followed an earlier failed candidate for that
same task.

## Result

| Task | Historical final | Fresh confirmation |
| --- | ---: | ---: |
| NodeBB plugin identifier validation | Pass | **Pass** |
| Element RoomHeader | Pass | Fail |
| Element array utilities | Pass | **Pass** |
| Flipt export ordering | Pass | Fail |
| Flipt authentication validation | Pass | Fail |
| Flipt referential validation | Fail | Fail |
| Flipt cache initialization / no-store | Fail | Fail |
| **Total** | **5 / 7** | **2 / 7** |

## Boundary

- Cohort: post-hoc, exactly the seven disputed rows.
- Inputs: frozen public task statements, isolated exact-base trees, and the
  frozen benchmark-informed Community package.
- Excluded: historical patch bytes, historical task-level grader diagnostics,
  gold data, future commits, public solution retrieval, and hidden tests.
- Product-only outcome: zero patches; native runs stopped at explicit HOLDs or
  intake limitations.
- Candidate owner: combined Synthesa workflow plus declared OpenAI Codex
  operator.
- Selection: one candidate per task; all seven frozen before grading.
- Measurement: one completed official-evaluator run, 2/7.
- Comparison: not unseen, not leaderboard pass@1, and not evidence of autonomous
  product-only patch generation.

The evaluator launcher first exited before loading any task because its host
Python lacked `pandas`. The dependency was installed and the identical sealed
grade specification was resumed. Both receipts are retained under
[`measurement/`](measurement/).

## Core artifacts

- [`candidate-generation-disclosure.json`](candidate-generation-disclosure.json)
- [`candidate-manifest.json`](candidate-manifest.json)
- [`candidate-predictions.json`](candidate-predictions.json)
- [`candidate-freeze.json`](candidate-freeze.json)
- [`candidate-freeze-verification.json`](candidate-freeze-verification.json)
- [`measurement/grade-spec.json`](measurement/grade-spec.json)
- [`measurement/grade-execution.json`](measurement/grade-execution.json)
- [`measurement/eval_results.json`](measurement/eval_results.json)

The candidate freeze root is
`18768cf89b430bcb0fbaaa3e6eaf98d05c686e5988ed92fc61bdacf96da98ff0`.
