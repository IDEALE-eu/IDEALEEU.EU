import os
import json
import pytest

def test_dual_approval_enforced():
    p = os.getenv("APPROVAL_LOG", "evidence/approvals.json")
    assert os.path.exists(p), "missing approvals log"
    with open(p) as f:
        approvals = json.load(f)
    for rec in approvals:
        assert rec.get("count", 0) >= 2, f"insufficient approvals for {rec.get('object_id')}"
        users = set(a["user"] for a in rec.get("approvals", []))
        assert len(users) >= 2, "approvals must be from distinct users"

def test_classification_respected():
    p = os.getenv("ACCESS_DECISIONS", "evidence/access_decisions.json")
    if not os.path.exists(p):
        pytest.skip("no access decisions evidence")
    with open(p) as f:
        decisions = json.load(f)
    for d in decisions:
        if d["object"]["classification"] > d["actor"].get("clearance", 0):
            assert d["outcome"] == "deny"
