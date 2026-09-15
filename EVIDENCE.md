# Evidence and verification

## Primary artifacts

[`submission.json`](submission.json) is the machine-readable entry point for
the result, protocol classification, evaluator identity, and provenance scope.

| Artifact | Purpose | SHA-256 |
| --- | --- | --- |
| `predictions.json` | Frozen 731-patch prediction set | `9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f` |
| `eval_results.json` | Complete 570/731 result map | `5b375ea4b465ee8a50e79c8d9fdc43e412781d31ccadd2e5ac0079d3f01080f8` |
| `prediction-freeze.json` | Frozen prediction manifest | `dcd6476940bcae86e75a33c8193eb9e97859f2991edfe55bbdcdaaf7fefd5e74` |
| `prediction-freeze-verification.json` | Freeze verification result | `03fafd15f04e353eba42ea0184d758985dcab7690fccf29e032c521faf2ad587` |
| `prior-score-569.json` | Complete repeat result | `02cd1f0043a2a29adde66c49f0a5458ed09bff856715682a550c39678d21be87` |
| `provenance-reconstruction-v1.json` | 731-row provenance ledger | `c192a3ddd14eb0ec4cdf4687b4cc0024a8b8ed02ed66e55a364efe9158981bfc` |

The provenance ledger carries reconstruction root:

`005f51f80866ab4a2cf0d4c0e4344486801fd74308e01583e1d5cf1932a277d4`

## Partition artifacts

Each execution partition includes a grade specification, execution receipt, and
rooted score summary.

| Partition | Specification | Execution | Score |
| --- | --- | --- | --- |
| Development | `development-grade-spec.json` | `development-grade-execution.json` | `development-score.json` |
| Validation | `validation-grade-spec.json` | `validation-grade-execution.json` | `validation-score.json` |
| Holdout execution partition | `holdout-grade-spec.json` | `holdout-grade-execution.json` | `holdout-score.json` |

## Quick verification

Verify the two central artifact hashes:

```bash
sha256sum predictions.json eval_results.json
```

Verify the result count and that every recorded value is Boolean:

```bash
python3 - <<'PY'
import json

with open("eval_results.json", encoding="utf-8") as handle:
    results = json.load(handle)

assert len(results) == 731
assert all(type(value) is bool for value in results.values())
assert sum(results.values()) == 570
print("verified: 570 / 731")
PY
```

Verify the prediction cardinality, non-empty patches, recorded freeze status,
and the prediction file's inclusion in the 37-entry freeze manifest:

```bash
python3 - <<'PY'
import json

with open("predictions.json", encoding="utf-8") as handle:
    predictions = json.load(handle)
with open("prediction-freeze.json", encoding="utf-8") as handle:
    freeze = json.load(handle)
with open("prediction-freeze-verification.json", encoding="utf-8") as handle:
    verification = json.load(handle)

assert len(predictions) == 731
assert all(isinstance(row["patch"], str) and row["patch"] for row in predictions)
assert any(
    entry["sha256"]
    == "9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f"
    for entry in freeze["entries"]
)
assert verification["entries_verified"] == len(freeze["entries"]) == 37
assert verification["verified"] is True
print("verified: 731 non-empty predictions in the verified freeze manifest")
PY
```

## Historical continuity

The earlier publication and its complete correction history remain preserved at
[`mohitunplugged/swepro-synthesa-v249-evidence`](https://github.com/mohitunplugged/swepro-synthesa-v249-evidence).
This fresh package does not rewrite that history. It excludes the earlier
manifest and post-hoc policy audit because both contained superseded
methodology classifications; the row-level reconstruction is the current
provenance evidence.
