# Evaluation methodology

## Historical 731-task campaign

The historical campaign processed every public SWE-bench Pro task and froze one
non-empty patch per task. The frozen prediction bytes were measured twice with
the official evaluator: 570/731 and 569/731.

It was an adaptive, open-material custom-harness evaluation:

- Public task materials were used.
- Public repository history or public tests were available for 389 rows.
- Local evaluator outcomes were available during parts of candidate production.
- Seven final selections followed an earlier, byte-different failed candidate
  for that same task.
- The execution partitions named development, validation, and holdout were
  campaign partitions; they were not private or unseen benchmark partitions.

The row-level reconstruction accounts for all 731 prediction rows. Exact
acquisition traces survive for 713; 18 retain lineage but no exact attempt
receipt. These facts make the historical evaluator outcome reproducible, but do
not make it a clean-room or leaderboard-comparable pass@1 result.

The product is architecturally AI-optional. This evidence does not establish
that every historical patch was generated without AI, so no model-free patch
generation claim is made here.

## Seven-row confirmation

The follow-up cohort was selected post hoc because these were the seven rows
with a prior same-task failure before historical final selection. It was not an
unseen sample.

Before candidate generation, the experiment froze:

1. The seven public task projections.
2. Exact base commits materialized from digest-identified official images.
3. The Synthesa Community package and its runtime audit.
4. A protocol forbidding gold data, historical patch bytes, historical
   task-level grader diagnostics, future commits, public solution retrieval,
   hidden tests, and cross-task outcome learning.

Each task used an isolated repository and product state. The native product path
ended in recorded HOLDs and produced zero patches. After preserving those
outcomes, a declared OpenAI Codex operator implemented one candidate per task
using only the frozen task statement and exact base tree. This is reported as a
benchmark-informed Synthesa-assisted workflow.

All seven final patches and the combined prediction file were sealed under
candidate freeze root
`18768cf89b430bcb0fbaaa3e6eaf98d05c686e5988ed92fc61bdacf96da98ff0`
before grading. The official evaluator was then run once across all seven
candidates with four local workers.

The first launcher attempt exited in 0.06 seconds because the host Python lacked
`pandas`; it loaded no task and produced no result. After installing the
evaluator dependency, the identical sealed grade specification was resumed.
No candidate changed. The completed measurement resolved 2/7 tasks.

## Interpretation

Supported historical statement:

> The frozen historical submission resolved 570 of 731 public SWE-bench Pro
> tasks in one complete official-evaluator run and 569 in a repeat, under an
> adaptive open-material custom-harness protocol.

Supported conservative statement:

> Removing the seven same-task-adaptation rows yields 565 resolved tasks among
> 724 retained historical rows. This remains open-material; it is not a
> clean-room result.

Supported follow-up statement:

> A sealed, benchmark-informed Synthesa + Codex reconstruction resolved 2 of the
> seven disputed rows. The native product-only path produced HOLDs, not patches.

Unsupported descriptions include one-shot pass@1, unseen-task generalization,
contamination resistance, organizer certification, autonomous product-only
570/731, or causal productivity uplift.
