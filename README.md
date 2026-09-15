# Synthesa SDLC on SWE-bench Pro

This repository publishes the evidence for a complete, local evaluation of a
Synthesa-assisted software-engineering campaign on all 731 public SWE-bench Pro
tasks. It also records a sealed follow-up experiment on the seven rows whose
historical provenance was disputed.

## Results at a glance

| Evidence | Result | What it means |
| --- | ---: | --- |
| Historical complete campaign | 570 / 731 (77.98%) | Observed with the pinned official evaluator under an adaptive, open-material custom-harness protocol |
| Repeat of the same prediction bytes | 569 / 731 (77.84%) | Reproducibility range of the historical frozen submission |
| Historical subset after quarantining seven disputed rows | 565 / 724 (78.04%) | Conservative historical claim with the seven same-task-adaptation rows removed from both numerator and denominator |
| Sealed follow-up on the seven disputed rows | 2 / 7 (28.57%) | New, benchmark-informed Synthesa + Codex evidence; not a replacement leaderboard score |

The headline `570 / 731` is a real evaluator observation, but it is **not** a
clean-room, unseen-task, one-shot pass@1, or organizer-certified leaderboard
result. Public repository history or tests were available in the historical
campaign, and seven final rows followed an earlier failed candidate for the
same task.

## What the seven-row follow-up decided

The seven candidates were produced from frozen public task statements and
isolated exact-base repositories. Historical patch bytes, historical task-level
grader diagnostics, gold patches, future commits, public solution retrieval,
and hidden tests were excluded. All seven patches were frozen before one
official evaluator measurement.

The native Community product path produced explicit HOLDs but no patches for
these rows. A declared OpenAI Codex operator then created one fresh candidate
per row from the permitted public task/base evidence. The score therefore
belongs to the combined Synthesa-assisted workflow, not to autonomous
product-only patch generation.

Two rows passed:

- NodeBB plugin identifier validation.
- Element numeric-array resampling and rescaling.

Five rows failed:

- Element RoomHeader.
- Flipt deterministic export ordering.
- Flipt authentication configuration validation.
- Flipt configuration referential validation.
- Flipt cache initialization and `no-store` handling.

This does not reconstruct how the old patches were originally acquired. It does
remove the basis for presenting all seven historical selections as freshly
confirmed. We therefore quarantine them from the conservative historical
subset and report the follow-up separately.

## What this supports

The evidence supports a narrower, useful claim: Synthesa coordinated a large
repair campaign with explicit task state, residuals, frozen decisions,
provenance records, and evaluator separation. The product can route work to
deterministic mechanisms, humans, or AI agents; AI is not the verification
boundary.

This evaluation does not isolate causal productivity uplift, human-versus-AI
performance, cost savings, or unseen-task generalization. Those require a
separate controlled study.

## Evidence map

- [`submission.json`](submission.json) — machine-readable claims and results.
- [`METHODOLOGY.md`](METHODOLOGY.md) — historical and follow-up protocols.
- [`EVIDENCE.md`](EVIDENCE.md) — artifact hashes and verification commands.
- [`predictions.json`](predictions.json) and [`eval_results.json`](eval_results.json) — historical frozen submission and complete result map.
- [`confirmation/README.md`](confirmation/README.md) — seven-row follow-up and its sealed evidence.

Evaluator: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
at commit `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`, run locally with the official
per-instance Docker images.
