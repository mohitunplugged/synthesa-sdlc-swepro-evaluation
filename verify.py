#!/usr/bin/env python3
"""Verify the canonical 731-row entry and its disclosed composition."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {
    "predictions.json": "65004a641ecede9435d596ce7484811345f6885d91fd81b8f4c3a4f35c69002d",
    "eval_results.json": "e1f6652e681b47d93d63a5487117edbfdae1be83ee7b314486dbbb5128d24ddc",
    "evidence/source-campaign/predictions.json": "9541053225b56b9ace8d0738218ec1dec5d37d2409bbf8d93eb537423f0ba98f",
    "evidence/source-campaign/eval_results.json": "5b375ea4b465ee8a50e79c8d9fdc43e412781d31ccadd2e5ac0079d3f01080f8",
    "evidence/sealed-seven/candidate-predictions.json": "a760cdbe6f28ed61c72dacbbd095286e824bbd2c21267058c9cde590e12c2175",
    "evidence/sealed-seven/measurement/eval_results.json": "043a044b732273c6f14dc6702a20dcf58d964b1171503fffc3ea26921cb006ab",
}


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


for path, expected in EXPECTED_HASHES.items():
    actual = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    assert actual == expected, (path, actual, expected)

canonical_predictions = load("predictions.json")
canonical_results = load("eval_results.json")
source_predictions = load("evidence/source-campaign/predictions.json")
source_results = load("evidence/source-campaign/eval_results.json")
replacement_predictions = load("evidence/sealed-seven/candidate-predictions.json")
replacement_results = load("evidence/sealed-seven/measurement/eval_results.json")

replacement_by_id = {row["instance_id"]: row for row in replacement_predictions}
assert len(replacement_by_id) == 7
assert set(replacement_by_id) == set(replacement_results)

expected_predictions = [
    replacement_by_id.get(row["instance_id"], row) for row in source_predictions
]
expected_results = dict(source_results)
expected_results.update(replacement_results)

assert canonical_predictions == expected_predictions
assert canonical_results == expected_results
assert len(canonical_predictions) == 731
assert len({row["instance_id"] for row in canonical_predictions}) == 731
assert all(isinstance(row["patch"], str) and row["patch"] for row in canonical_predictions)
assert len(canonical_results) == 731
assert all(type(value) is bool for value in canonical_results.values())
assert sum(canonical_results.values()) == 567

print("verified canonical entry: 567 / 731 (77.56%)")
print("verified composition: 724 retained rows + 7 sealed replacement rows")
