# Sealed seven-row replacement cohort

This directory contains the evidence for the seven rows regenerated under the
entry's stricter provenance protocol. These rows are a component of the
canonical 731-task result, not a separate public submission.

## Outcomes

| Task | Official evaluator outcome |
| --- | ---: |
| NodeBB plugin identifier validation | **Pass** |
| Element RoomHeader | Fail |
| Element numeric-array utilities | **Pass** |
| Flipt deterministic export ordering | Fail |
| Flipt authentication validation | Fail |
| Flipt referential validation | Fail |
| Flipt cache initialization / `no-store` | Fail |
| **Total** | **2 / 7** |

## Protocol boundary

- Inputs: frozen public task statements, isolated exact-base trees, and the
  frozen benchmark-informed Community package.
- Excluded: earlier patch bytes, earlier task-level grader diagnostics, gold
  data, future commits, public solution retrieval, hidden tests, and cross-case
  outcome learning.
- Native product outcome: zero patches; runs stopped at explicit HOLDs or
  intake limitations.
- Candidate owner: Synthesa-assisted workflow plus a declared OpenAI Codex
  operator.
- Selection: one candidate per task, with all seven frozen before grading.
- Measurement: one completed pinned official-evaluator execution resolving
  2/7.

The evaluator launcher initially exited before loading a task because its host
Python environment lacked `pandas`. The missing dependency was installed and
the identical sealed grade specification was executed. No candidate changed,
and both receipts are retained under [`measurement/`](measurement/).

## Core artifacts

- [`candidate-generation-disclosure.json`](candidate-generation-disclosure.json)
- [`candidate-manifest.json`](candidate-manifest.json)
- [`candidate-predictions.json`](candidate-predictions.json)
- [`candidate-freeze.json`](candidate-freeze.json)
- [`candidate-freeze-verification.json`](candidate-freeze-verification.json)
- [`measurement/grade-spec.json`](measurement/grade-spec.json)
- [`measurement/grade-execution.json`](measurement/grade-execution.json)
- [`measurement/eval_results.json`](measurement/eval_results.json)

Candidate freeze root:
`18768cf89b430bcb0fbaaa3e6eaf98d05c686e5988ed92fc61bdacf96da98ff0`.
