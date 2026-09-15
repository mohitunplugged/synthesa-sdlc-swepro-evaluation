# Synthesa SDLC on SWE-bench Pro

## 567 / 731 tasks resolved (77.56%)

This repository is the canonical public entry for a Synthesa-assisted campaign
over all 731 public SWE-bench Pro tasks. It contains one non-empty prediction
per task and one Boolean official-evaluator outcome per prediction.

| Scope | Resolved | Rate |
| --- | ---: | ---: |
| All public SWE-bench Pro tasks | **567 / 731** | **77.56%** |

The result is an **adaptive, open-material custom-harness evaluation**. It is
not an unseen-task, clean-room, one-shot pass@1, organizer-certified, or
official-leaderboard result.

## What was evaluated

Synthesa coordinated task state, requirements, residuals, evidence, candidate
freezing, and evaluator separation. Candidate implementation could be routed
to deterministic tooling, a human, or an AI coding operator. The official
SWE-bench Pro evaluator—not Synthesa or the operator—determined each outcome.

The canonical 731-row entry has two measurement components:

- 724 predictions and results retained from the frozen full campaign.
- Seven provenance-sensitive predictions independently regenerated from
  frozen public task statements and exact base repositories, sealed before
  grading, and then substituted by instance ID. Two of those seven passed.

The seven-row generation protocol excluded earlier patch bytes, earlier
task-level grader diagnostics, gold patches, future commits, public solution
retrieval, hidden tests, and cross-case feedback. Native Community flows
produced explicit HOLDs but no patches for those seven cases; a declared OpenAI
Codex operator created the replacement candidates from the permitted inputs.

The published result is therefore a reproducible composition of official
evaluator evidence, not a claim that all 731 rows were rerun together in one
new evaluator invocation.

## Evidence

- [`submission.json`](submission.json) — machine-readable result and claim
  boundary.
- [`predictions.json`](predictions.json) — canonical 731-row prediction set.
- [`eval_results.json`](eval_results.json) — canonical 731-row Boolean result
  map.
- [`submission-freeze.json`](submission-freeze.json) — content-addressed freeze
  for the canonical machine-readable artifacts.
- [`METHODOLOGY.md`](METHODOLOGY.md) — generation, substitution, and evaluation
  protocol.
- [`EVIDENCE.md`](EVIDENCE.md) — hashes and independent verification commands.
- [`evidence/sealed-seven/`](evidence/sealed-seven/) — sealed artifacts for the
  independently regenerated cohort.

Evaluator: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
at commit `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`, executed locally with the
official per-instance Docker images.

## Claim boundary

This evidence demonstrates a measured outcome for this disclosed workflow. It
does not by itself establish autonomous product-only patch generation, causal
productivity uplift, human-versus-AI superiority, cost savings, or
generalization to unseen tasks. Those require separate controlled studies.
