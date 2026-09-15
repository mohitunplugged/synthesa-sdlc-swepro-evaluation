# Evaluation methodology

## Classification

This is an adaptive, open-material, custom-harness evaluation on all 731 public
SWE-bench Pro tasks. It is published as one canonical entry containing exactly
one non-empty patch and one Boolean result for every benchmark instance.

It is not submitted as a clean-room evaluation, unseen-task test, one-shot
pass@1 result, or organizer-certified leaderboard entry.

## Candidate generation

Synthesa supplied the workflow layer: task state, requirements, residuals,
evidence handling, candidate freezing, and evaluator separation. Depending on
the task, implementation could involve deterministic tools, humans, or AI
coding operators. The evidence does not support a model-free or autonomous
product-only claim for the complete candidate set.

Public task materials were available throughout the campaign. The provenance
ledger classifies 371 rows as content-matched traces that used a later public
repository state or its tests. Another 18 rows retain public-temporal lineage
but no longer have the exact attempt trace, for 389 public-temporal rows in
total. Local evaluator outcomes were also available during parts of candidate
development. The labels `development`, `validation`, and `holdout` in source
receipts are campaign execution partitions; they are not private or unseen
benchmark partitions.

## Canonical entry assembly

The published candidate set was assembled deterministically by instance ID:

1. Retain 724 predictions and their Boolean results from the frozen full
   campaign.
2. Independently regenerate the seven rows selected for stricter provenance
   controls.
3. Seal all seven replacement patches before grading.
4. Evaluate the sealed replacements with the pinned official evaluator.
5. Substitute the seven predictions and results by exact instance ID.
6. Verify 731 unique predictions, 731 Boolean results, and exactly seven
   substitutions.

The retained component resolves 565 of 724 tasks. The sealed replacement
component resolves 2 of 7. Their disjoint union resolves 567 of 731 tasks.

This is a composite measurement: the 724 retained results come from the
complete pinned official-evaluator campaign, while the seven substituted
results come from the sealed cohort's pinned official-evaluator execution. The
731 canonical rows were not rerun together in one new evaluator invocation.

## Stricter protocol for the seven substituted rows

Before replacement candidate generation, the following were frozen:

1. The seven public task projections.
2. Exact base commits materialized from digest-identified official images.
3. The Synthesa Community package and runtime audit.
4. A protocol excluding gold data, earlier patch bytes, earlier task-level
   grader diagnostics, future commits, public solution retrieval, hidden tests,
   and cross-case outcome learning.

Every task used isolated repository and product state. Native Community flows
ended in recorded HOLDs or intake limitations and produced zero patches. After
those outcomes were preserved, a declared OpenAI Codex operator created one
candidate per task using only the permitted task statement and exact base tree.

All seven patches were sealed under candidate freeze root
`18768cf89b430bcb0fbaaa3e6eaf98d05c686e5988ed92fc61bdacf96da98ff0`
before the official evaluator was invoked. The evaluator resolved 2 of 7.

An initial launcher attempt exited after 0.06 seconds because the host Python
environment lacked `pandas`; it loaded no task and returned no task feedback.
After installing the missing evaluator dependency, the identical sealed grade
specification was executed. No candidate changed. Both receipts are retained.

## Evaluator

- Repository: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
- Commit: `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`
- Evaluator tree SHA-256: `bb5d4c5486be296e464e695df3747064aaa3bb197394bc6d39980634afec2034`
- Execution: local Docker with official per-instance images

## Supported interpretation

> Under the disclosed adaptive, open-material custom harness, the canonical
> Synthesa-assisted entry resolved 567 of 731 public SWE-bench Pro tasks as
> measured by the pinned official evaluator.

Unsupported descriptions include one-shot pass@1, unseen-task generalization,
contamination resistance, organizer certification, autonomous product-only
567/731, or causal productivity uplift.
