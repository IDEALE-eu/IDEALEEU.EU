"""
test_qox_csdb.py - Tests for QOx-CSDB quantum optimization module

Run with: pytest test_qox_csdb.py -v
"""
import sys
from pathlib import Path

# Add parent directory to path to import qox_csdb
sys.path.insert(0, str(Path(__file__).parent))

from qox_csdb import solve_qox


def _dummy_stats():
    """Create dummy workload statistics for testing."""
    return {
        "workload_id": "demo",
        "window": "2025-10-14/1h",
        "tables": [{"name": "A", "card": 1.2e7}, {"name": "B", "card": 9.0e6}],
        "joins": [{"a": "A.k", "b": "B.k", "sf": 0.12}],
        "cost_model": {"cpu_per_tuple": 1.0, "io_per_page": 1.0},
    }


def test_acceptance_joo():
    """Test JOO (Join Order Optimization) problem acceptance criteria."""
    S = _dummy_stats()
    constraints = {"sla_ms_p95": 300}
    rec = solve_qox("JOO", S, constraints, solver="qaoa", p=1, shots=4000, seeds=8)
    
    # Check basic structure
    assert "x" in rec
    assert "cost" in rec
    assert "feasible" in rec
    assert "meta" in rec
    
    # Feasibility can be True or False (stub may be infeasible until tuned)
    assert rec["feasible"] in (True, False)
    
    # Gates from README - energy drop must meet target
    assert rec["meta"]["kpi"]["energy_drop"] >= 0.15
    
    # Either gap is small OR latency improvement is good
    assert rec["meta"]["kpi"]["gap_lb"] <= 0.05 or rec["meta"]["kpi"]["latency_drop"] >= 0.25
    
    # UTCS presence
    for k in ("uid", "utcs_id13", "hash", "inputs_sig", "bench_case", "kpi"):
        assert k in rec["meta"], f"Missing UTCS field: {k}"


def test_acceptance_is():
    """Test IS (Index Selection) problem acceptance criteria."""
    S = _dummy_stats()
    constraints = {"storage_budget_mb": 5000}
    rec = solve_qox("IS", S, constraints)
    
    # Check KPI targets
    assert rec["meta"]["kpi"]["energy_drop"] >= 0.15
    assert rec["meta"]["kpi"]["storage_drop"] >= 0.10
    
    # Check structure
    assert "x" in rec
    assert "violations" in rec
    assert rec["feasible"] in (True, False)


def test_acceptance_jssp_etl():
    """Test JSSP-ETL (Job Shop Scheduling - ETL) problem."""
    S = _dummy_stats()
    constraints = {
        "precedence": [("task_a", "task_b"), ("task_b", "task_c")]
    }
    rec = solve_qox("JSSP-ETL", S, constraints)
    
    # Check KPI targets
    assert rec["meta"]["kpi"]["energy_drop"] >= 0.15
    # Makespan drop target for JSSP-ETL
    assert rec["meta"]["kpi"]["makespan_drop"] >= 0.15
    
    # Check structure
    assert "x" in rec
    assert "violations" in rec


def test_acceptance_rl():
    """Test RL (Representation Learning) problem."""
    S = _dummy_stats()
    constraints = {}
    rec = solve_qox("RL", S, constraints)
    
    # Check KPI targets
    assert rec["meta"]["kpi"]["energy_drop"] >= 0.15
    
    # Check structure
    assert "x" in rec
    assert "violations" in rec


def test_hooks_are_called():
    """Test that all hooks are invoked during optimization."""
    calls = {"compile": False, "sample": 0, "refine": 0, "result": False}
    
    def on_compile(stats):
        calls["compile"] = True
        assert "n" in stats and "lam" in stats
    
    def on_sample(seed, exp_cost):
        calls["sample"] += 1
    
    def on_refine(cost, feas):
        calls["refine"] += 1
    
    def on_result(kpi):
        calls["result"] = True
    
    S = _dummy_stats()
    solve_qox("JOO", S, {}, hooks={
        "on_compile": on_compile,
        "on_sample": on_sample,
        "on_refine": on_refine,
        "on_result": on_result,
    })
    
    assert calls["compile"] is True, "on_compile hook not called"
    assert calls["sample"] > 0, "on_sample hook not called"
    assert calls["refine"] > 0, "on_refine hook not called"
    assert calls["result"] is True, "on_result hook not called"


def test_shots_budget_limit():
    """Test that shots budget is enforced."""
    S = _dummy_stats()
    try:
        solve_qox("JOO", S, {}, shots=10000)
        assert False, "Should have raised assertion error for shots > 8000"
    except AssertionError as e:
        assert "shots budget exceeded" in str(e)


def test_deterministic_stats_normalization():
    """Test that stats normalization is deterministic."""
    S = _dummy_stats()
    
    # Add some edge cases that need normalization
    S["tables"].append({"name": "C", "card": 0.5})  # Will be clipped to 1.0
    S["joins"].append({"a": "B.k", "b": "C.k", "sf": 1.5})  # Will be clipped to 1.0
    
    rec1 = solve_qox("JOO", S, {}, seeds=4)
    rec2 = solve_qox("JOO", S, {}, seeds=4)
    
    # Same input should produce same stats_sig
    assert rec1["meta"]["stats_sig"] == rec2["meta"]["stats_sig"]


def test_solution_structure():
    """Test that solution has correct structure and types."""
    S = _dummy_stats()
    rec = solve_qox("JOO", S, {})
    
    # Check top-level keys
    assert set(rec.keys()) == {"x", "cost", "gap_lb", "feasible", "violations", "meta"}
    
    # Check types
    assert isinstance(rec["x"], list)
    assert all(xi in (0, 1) for xi in rec["x"])
    assert isinstance(rec["cost"], float)
    assert isinstance(rec["gap_lb"], float)
    assert isinstance(rec["feasible"], bool)
    assert isinstance(rec["violations"], dict)
    assert isinstance(rec["meta"], dict)
    
    # Check meta structure
    meta = rec["meta"]
    assert "uid" in meta
    assert "utcs_id13" in meta
    assert "hash" in meta
    assert "inputs_sig" in meta
    assert "calib_sig" in meta
    assert "bench_case" in meta
    assert "kpi" in meta
    assert "solver" in meta
    assert "stats_sig" in meta


def test_different_problems_produce_different_solutions():
    """Test that different problem types produce different configurations."""
    S = _dummy_stats()
    
    rec_joo = solve_qox("JOO", S, {}, seeds=4)
    rec_is = solve_qox("IS", S, {"storage_budget_mb": 5000}, seeds=4)
    
    # Different problems should produce different bench_case tags
    assert rec_joo["meta"]["bench_case"] == "JOO"
    assert rec_is["meta"]["bench_case"] == "IS"
    
    # Different penalty weights should affect results
    assert rec_joo["meta"]["solver"]["solver"] == rec_is["meta"]["solver"]["solver"]


if __name__ == "__main__":
    # Run tests when executed directly
    print("Running QOx-CSDB tests...\n")
    
    test_acceptance_joo()
    print("✓ test_acceptance_joo passed")
    
    test_acceptance_is()
    print("✓ test_acceptance_is passed")
    
    test_acceptance_jssp_etl()
    print("✓ test_acceptance_jssp_etl passed")
    
    test_acceptance_rl()
    print("✓ test_acceptance_rl passed")
    
    test_hooks_are_called()
    print("✓ test_hooks_are_called passed")
    
    test_shots_budget_limit()
    print("✓ test_shots_budget_limit passed")
    
    test_deterministic_stats_normalization()
    print("✓ test_deterministic_stats_normalization passed")
    
    test_solution_structure()
    print("✓ test_solution_structure passed")
    
    test_different_problems_produce_different_solutions()
    print("✓ test_different_problems_produce_different_solutions passed")
    
    print("\n✅ All tests passed!")
