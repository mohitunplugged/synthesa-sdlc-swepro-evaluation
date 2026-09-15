# Evidence and verification

## Historical campaign

| Artifact | Purpose | SHA-256 |
| --- | --- | --- |
| `predictions.json` | Frozen 731-patch prediction set | `9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f` |
| `eval_results.json` | Complete 570/731 result map | `5b375ea4b465ee8a50e79c8d9fdc43e412781d31ccadd2e5ac0079d3f01080f8` |
| `prediction-freeze.json` | Historical freeze manifest | `dcd6476940bcae86e75a33c8193eb9e97859f2991edfe55bbdcdaaf7fefd5e74` |
| `prediction-freeze-verification.json` | Historical freeze verification | `03fafd15f04e353eba42ea0184d758985dcab7690fccf29e032c521faf2ad587` |
| `prior-score-569.json` | Complete repeat result | `02cd1f0043a2a29adde66c49f0a5458ed09bff856715682a550c39678d21be87` |
| `provenance-reconstruction-v1.json` | 731-row provenance ledger | `c192a3ddd14eb0ec4cdf4687b4cc0024a8b8ed02ed66e55a364efe9158981bfc` |

Verify the historical result:

```bash
sha256sum predictions.json eval_results.json
python3 - <<'PY'
import json
results = json.load(open("eval_results.json", encoding="utf-8"))
assert len(results) == 731
assert all(type(value) is bool for value in results.values())
assert sum(results.values()) == 570
print("verified historical result: 570 / 731")
PY
```

## Seven-row confirmation

| Artifact | Purpose | SHA-256 |
| --- | --- | --- |
| `confirmation/candidate-predictions.json` | Seven frozen candidate patches | `a760cdbe6f28ed61c72dacbbd095286e824bbd2c21267058c9cde590e12c2175` |
| `confirmation/candidate-freeze.json` | 17-entry candidate evidence freeze | `2787ffb4e39f1d3972bf063908a8f6f8cd9f37aad351fed3cd6391107197fcbc` |
| `confirmation/candidate-freeze-verification.json` | Freeze verification | `9c8a63dca6e636029fbe8285e386d460602f776e78c965ab19d87dfb9b716246` |
| `confirmation/measurement/grade-spec.json` | Sealed official grade specification | `ee18132267ca1489c7bf946daf9623e068088b66ff6b5ccbff63238ba2cb4a30` |
| `confirmation/measurement/grade-execution.json` | Successful evaluator receipt | `df45618bc6432fb9f19162740b708f8e6f016c59601a8538f72c760139383741` |
| `confirmation/measurement/eval_results.json` | Complete 2/7 Boolean result map | `043a044b732273c6f14dc6702a20dcf58d964b1171503fffc3ea26921cb006ab` |
| `confirmation/measurement/grade-execution-failed-01.json` | Pre-task missing-dependency launcher failure | `07e0ce254b09228b3a513caecaff8a67f0e5a311b9b105b90a9e78cbf11ff651` |

Verify the confirmation result and candidate freeze:

```bash
sha256sum confirmation/candidate-predictions.json \
  confirmation/measurement/eval_results.json
python3 - <<'PY'
import hashlib, json, pathlib

root = pathlib.Path("confirmation")
freeze = json.load(open(root / "candidate-freeze.json", encoding="utf-8"))
for entry in freeze["entries"]:
    data = (root / entry["path"]).read_bytes()
    assert len(data) == entry["bytes"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"]

results = json.load(open(root / "measurement/eval_results.json", encoding="utf-8"))
assert len(results) == 7
assert sum(results.values()) == 2
print("verified seven-row confirmation: 2 / 7")
PY
```

See [`confirmation/README.md`](confirmation/README.md) for the per-row outcome
and claim boundary.

## Evaluator identity

- Repository: [`scaleapi/SWE-bench_Pro-os`](https://github.com/scaleapi/SWE-bench_Pro-os)
- Commit: `ca10a60a5fcae51e6948ffe1485d4153d421e6c5`
- Evaluator tree SHA-256: `bb5d4c5486be296e464e695df3747064aaa3bb197394bc6d39980634afec2034`
- Execution: local Docker using official per-instance images

Historical correction continuity remains available at
[`mohitunplugged/swepro-synthesa-v249-evidence`](https://github.com/mohitunplugged/swepro-synthesa-v249-evidence).
