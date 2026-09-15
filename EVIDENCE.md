# Evidence and verification

## Canonical public entry

| Artifact | Purpose | SHA-256 |
| --- | --- | --- |
| `predictions.json` | Canonical 731-row candidate set | `65004a641ecede9435d596ce7484811345f6885d91fd81b8f4c3a4f35c69002d` |
| `eval_results.json` | Canonical 731-row Boolean result map | `e1f6652e681b47d93d63a5487117edbfdae1be83ee7b314486dbbb5128d24ddc` |
| `submission.json` | Machine-readable claim and result | `bf1aaf2c8f03c6371872b1f85873571441c3c8ae2a0b711cf72206d73bb5ba2c` |
| `measurement-components.json` | Exact instance-ID composition rule | `c560bc1e8e1ffbd01f4d7ede4b78d854153bc1aaeccaaa0d42a48444ecf3581d` |
| `submission-freeze.json` | Four-artifact canonical freeze | `0a078004ba49bf895abd6da6282f4daa73f5a74cceb9b64ba5e2bfea2e6cebeb` |
| `submission-freeze-verification.json` | Freeze verification receipt | `aba7b2a6076f82cb5d40ab0112aba1f710e26e70e75e7330d03dd5b4df5e5181` |

Run the independent verifier:

```bash
python3 verify.py
```

It checks artifact hashes, reconstructs the canonical prediction and result
files from the two disjoint measurement components, verifies exactly seven
substitutions, and asserts 567 Boolean passes among 731 unique non-empty
predictions.

The canonical freeze root is
`f53895875f60cb99354c936d09de6d96a033c9de5610efd58ed41482152bf30a`.

## Measurement components

| Component artifact | Purpose | SHA-256 |
| --- | --- | --- |
| `evidence/source-campaign/predictions.json` | Frozen source set from which 724 rows are retained | `9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f` |
| `evidence/source-campaign/eval_results.json` | Complete source result map | `5b375ea4b465ee8a50e79c8d9fdc43e412781d31ccadd2e5ac0079d3f01080f8` |
| `evidence/sealed-seven/candidate-predictions.json` | Seven sealed replacement candidates | `a760cdbe6f28ed61c72dacbbd095286e824bbd2c21267058c9cde590e12c2175` |
| `evidence/sealed-seven/candidate-freeze.json` | Seventeen-entry replacement evidence freeze | `2787ffb4e39f1d3972bf063908a8f6f8cd9f37aad351fed3cd6391107197fcbc` |
| `evidence/sealed-seven/candidate-freeze-verification.json` | Candidate freeze verification | `9c8a63dca6e636029fbe8285e386d460602f776e78c965ab19d87dfb9b716246` |
| `evidence/sealed-seven/measurement/grade-spec.json` | Sealed official grade specification | `ee18132267ca1489c7bf946daf9623e068088b66ff6b5ccbff63238ba2cb4a30` |
| `evidence/sealed-seven/measurement/grade-execution.json` | Successful evaluator receipt | `df45618bc6432fb9f19162740b708f8e6f016c59601a8538f72c760139383741` |
| `evidence/sealed-seven/measurement/eval_results.json` | Complete seven-row Boolean result map | `043a044b732273c6f14dc6702a20dcf58d964b1171503fffc3ea26921cb006ab` |
| `evidence/sealed-seven/measurement/grade-execution-failed-01.json` | Pre-task dependency failure receipt | `07e0ce254b09228b3a513caecaff8a67f0e5a311b9b105b90a9e78cbf11ff651` |

The seven replacement candidates were sealed under freeze root
`18768cf89b430bcb0fbaaa3e6eaf98d05c686e5988ed92fc61bdacf96da98ff0`
before grading.

## Evaluator identity

- Repository: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
- Commit: `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`
- Evaluator tree SHA-256: `bb5d4c5486be296e464e695df3747064aaa3bb197394bc6d39980634afec2034`
- Execution: local Docker using official per-instance images

The evaluator receipts measure both components. No claim is made that the
canonical 731-row composition was executed as one new monolithic evaluator
run.
