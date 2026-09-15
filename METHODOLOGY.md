# Evaluation methodology

## Objective

Measure a complete Synthesa SDLC custom-harness campaign against the public
SWE-bench Pro task set using the official evaluator, while retaining the final
predictions, evaluator identity, results, and row-level provenance needed for
independent review.

## System boundary

Synthesa SDLC supplied the patch-production and campaign-control layer. Its
workflow represents unresolved requirements, failed checks, or missing evidence
as residual work and can route that work to deterministic mechanisms, a human,
or an external orchestrator. This campaign used the deterministic/model-free
path; no LLM chat trajectories are claimed.

The official SWE-bench Pro evaluator remained a separate measurement layer. The
final prediction set was executed locally in the official per-instance Docker
images using evaluator commit
`ca10a60a5fcae51e6948ffe1485d4153d421e6c5`.

## Campaign protocol

1. The campaign operated on all 731 public SWE-bench Pro tasks.
2. Candidate patches came from archived campaign work, current deterministic
   mechanisms, residual/manual construction, and explicitly disclosed public
   repository history or tests.
3. Candidate construction was adaptive. Local evaluator results were available
   during the campaign; seven final task rows followed a failed, byte-different
   candidate for the same task.
4. One non-empty final patch per task was assembled and frozen.
5. The frozen 731-patch file was evaluated in three disjoint execution
   partitions and merged into `eval_results.json`.
6. A second complete evaluation used the identical frozen prediction bytes.

The partition names `development`, `validation`, and `holdout` describe campaign
execution partitions. They do not turn this public-set campaign into an unseen
or private evaluation.

## Results

| Partition | Resolved | Tasks | Rate |
| --- | ---: | ---: | ---: |
| Development | 102 | 149 | 68.46% |
| Validation | 114 | 146 | 78.08% |
| Holdout execution partition | 354 | 436 | 81.19% |
| **Complete run** | **570** | **731** | **77.98%** |

The repeat resolved 569/731 tasks. The one-result difference occurred in the
holdout execution partition.

## Provenance reconstruction

The row-level ledger accounts for all 731 frozen prediction patches:

| Evidence class | Rows |
| --- | ---: |
| Archive-backed legacy trace | 148 |
| Current-campaign mechanism trace | 106 |
| Current-campaign residual/manual trace | 88 |
| Public-temporal repository trace | 371 |
| Public-temporal lineage with overwritten attempt receipt | 18 |

There are no wholly unaccounted rows. The last 18 rows retain a known pre-freeze
snapshot-batch origin but not an exact surviving attempt receipt, so they are
reported as lineage-only rather than content-matched acquisition traces.

Public repository history or public tests were used for 389 rows. That use is
part of the declared protocol, not described as held-out synthesis.

## Direct-answer comparison

A separate exact-answer comparison was produced after the final prediction
bytes had already been frozen. It identified 44 submitted patches equal to the
upstream production diff. The comparison was marked `GOLD_AIDED`, was excluded
from candidate eligibility, and did not produce or replace the frozen
predictions. Exact equality is retained as comparison evidence; it is not used
alone to infer how a patch was acquired.

## Interpretation

This package supports the claim:

> Synthesa SDLC resolved 570 of 731 SWE-bench Pro public tasks in a complete
> local run of the pinned official evaluator, with 569 resolved in a repeat of
> the same frozen predictions, under an adaptive open-material custom-harness
> protocol.

It does not support describing the number as one-shot pass@1, clean-room,
unseen-task, contamination-resistant, private-set, or organizer-certified.

## Known limitations

- Seven tasks contain same-task adaptation after a prior candidate failure.
- Public-temporal material was available for 389 rows.
- Eighteen rows have lineage evidence but no surviving exact attempt receipt.
- The repeat varied by one task.
- The study does not isolate causal uplift against an otherwise identical human
  or AI baseline.
