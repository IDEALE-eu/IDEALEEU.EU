import os
import json
import pytest

REQUIRED_FINDINGS = [
    "schema_ok",
    "brex_ok",
    "dmrl_ok",
    "references_ok",
    "issue_compat_ok",
]

@pytest.mark.smoke
def test_evidence_bundle_exists():
    p = os.getenv("EVIDENCE_PATH", "evidence/bundle.json")
    assert os.path.exists(p), f"missing evidence bundle at {p}"

def load_bundle(path="evidence/bundle.json"):
    with open(path) as f:
        return json.load(f)

def test_core_validators_pass():
    b = load_bundle()
    results = {v["name"]: v["result"] for v in b["validators"]}
    assert results.get("SchemaValidator") == "pass"
    assert results.get("BREXAgent") in {"pass","advisory"}
    assert results.get("DMRLChecker") == "pass"
    assert results.get("RefIntegrityAgent") == "pass"

def test_issue_compatibility_flag():
    b = load_bundle()
    flags = set(b.get("flags", []))
    assert "mixed_issues_blocked" not in flags

@pytest.mark.parametrize("audience", ["AVN","GEN","INT"])
def test_applicability_preview_exists(audience):
    path = f"evidence/previews/{audience}.json"
    assert os.path.exists(path), f"missing preview {path}"
