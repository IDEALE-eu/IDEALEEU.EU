"""
VQE H2 STO-3G Benchmark

Variational Quantum Eigensolver for H2 molecule in STO-3G basis.
Target: ≤200 2-qubit gates, test noise mitigation effectiveness.
"""

import sys
from pathlib import Path

import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algos.qnoise_qiskit_001 import mitigate_observable


class H2Circuit:
    """Mock H2 VQE circuit for benchmarking."""
    
    def __init__(self):
        self.name = "vqe_h2_sto3g"
        self.n_qubits = 4
        self.depth = 12
        self.n_2q_gates = 8  # Example count
    
    def __str__(self):
        return f"{self.name}(qubits={self.n_qubits}, depth={self.depth})"


class MockBackend:
    """Mock backend for benchmarking."""
    
    def __init__(self, name="aer_simulator_noisy"):
        self.name = name
    
    def __str__(self):
        return self.name


class SimpleResidualModel:
    """Simple residual correction model."""
    
    def __init__(self):
        self.val_r2_ = 0.72
        self.val_mae_ = 0.035
    
    def predict(self, X):
        return X * 1.015


def run_h2_benchmark(shots=4096, fold_scales=None, verbose=True):
    """
    Run VQE H2 benchmark with noise mitigation.
    
    Args:
        shots: Number of measurement shots
        fold_scales: ZNE fold scales
        verbose: Print results
        
    Returns:
        Result dictionary with energy and metadata
    """
    if fold_scales is None:
        fold_scales = [1, 3, 5]
    
    # Setup
    circuit = H2Circuit()
    backend = MockBackend("aer_simulator_noisy")
    
    # Configuration
    zne_budget = {"fold_scales": fold_scales}
    cdr_budget = {"n_samples": 10}
    readout_cal = {
        "matrix": [[0.98, 0.02], [0.03, 0.97]],
        "timestamp": "2024-06-24T00:00:00"
    }
    drift_tracker = {"ΔT": 0.02, "τ_max": 0.5}
    resid_model = SimpleResidualModel()
    
    # Track metrics
    metrics = {
        "fold_calls": [],
        "cdr_samples": [],
        "results": []
    }
    
    def on_fold(scale, circ_id):
        metrics["fold_calls"].append({"scale": scale, "circ_id": circ_id})
    
    def on_cdr_sample(k, clifford_score):
        metrics["cdr_samples"].append({"k": k, "score": clifford_score})
    
    def on_result(exp, stderr):
        metrics["results"].append({"exp": exp, "stderr": stderr})
    
    hooks = {
        "on_fold": on_fold,
        "on_cdr_sample": on_cdr_sample,
        "on_result": on_result
    }
    
    # Execute benchmark
    result = mitigate_observable(
        circ=circuit,
        backend=backend,
        shots=shots,
        zne_budget=zne_budget,
        cdr_budget=cdr_budget,
        readout_cal=readout_cal,
        drift_tracker=drift_tracker,
        resid_model=resid_model,
        hooks=hooks,
        uid="Qiskit_001_20240624_APCGPT"
    )
    
    if verbose:
        print("=" * 70)
        print("VQE H2 STO-3G Benchmark Results")
        print("=" * 70)
        print(f"Circuit: {circuit}")
        print(f"Backend: {backend}")
        print(f"Shots: {shots}")
        print(f"Fold scales: {fold_scales}")
        print()
        print(f"Energy expectation: {result['exp']:.6f}")
        print(f"Standard error: {result['stderr']:.6f}")
        print()
        print("KPIs:")
        kpi = result["meta"]["kpi"]
        print(f"  Infidelity drop: {kpi['infidelity_drop']:.4f} (target: ≥ 0.30)")
        print(f"  Energy error drop: {kpi['vqe_energy_err_drop']:.6f}")
        print(f"  Overhead depth: {kpi['overhead_depth']:.2f} (limit: ≤ 3.0)")
        print(f"  Wall time ratio: {kpi['wall_time_ratio']:.2f} (limit: ≤ 1.5)")
        print()
        print(f"ZNE folds executed: {len(metrics['fold_calls'])}")
        print(f"CDR samples: {len(metrics['cdr_samples'])}")
        print()
        print("UTCS Metadata:")
        meta = result["meta"]
        print(f"  UID: {meta['uid']}")
        print(f"  UTCS ID: {meta['utcs_id13']}")
        print(f"  Bench case: {meta['bench_case']}")
        print("=" * 70)
    
    result["benchmark_metrics"] = metrics
    return result


def run_parameter_sweep():
    """Run benchmark with different shot counts."""
    print("\n" + "=" * 70)
    print("VQE H2 Parameter Sweep")
    print("=" * 70)
    
    shot_counts = [2048, 4096, 8192]
    results = []
    
    for shots in shot_counts:
        print(f"\nRunning with {shots} shots...")
        result = run_h2_benchmark(shots=shots, verbose=False)
        results.append(result)
        
        kpi = result["meta"]["kpi"]
        print(f"  Energy: {result['exp']:.6f} ± {result['stderr']:.6f}")
        print(f"  Overhead depth: {kpi['overhead_depth']:.2f}")
    
    print("\n" + "=" * 70)
    return results


if __name__ == "__main__":
    # Run single benchmark
    result = run_h2_benchmark()
    
    # Optionally run parameter sweep
    # sweep_results = run_parameter_sweep()
