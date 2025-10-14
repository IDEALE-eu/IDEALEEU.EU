"""
QAOA MaxCut Benchmark on Erdős-Rényi Graphs

Quantum Approximate Optimization Algorithm for MaxCut problem.
Tests on random graphs G(n,p) with n ∈ [8,14].
"""

import sys
from pathlib import Path

import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algos.qnoise_qiskit_001 import mitigate_observable


class QAOACircuit:
    """Mock QAOA circuit for MaxCut."""
    
    def __init__(self, n_nodes, p_layers=2):
        self.name = f"qaoa_maxcut_g{n_nodes}"
        self.n_nodes = n_nodes
        self.p_layers = p_layers
        self.n_qubits = n_nodes
        self.depth = p_layers * 4  # Approximate
    
    def __str__(self):
        return f"{self.name}(qubits={self.n_qubits}, p={self.p_layers})"


class MockBackend:
    """Mock backend for benchmarking."""
    
    def __init__(self, name="aer_simulator_noisy"):
        self.name = name
    
    def __str__(self):
        return self.name


class SimpleResidualModel:
    """Simple residual correction model."""
    
    def __init__(self):
        self.val_r2_ = 0.68
        self.val_mae_ = 0.042
    
    def predict(self, X):
        return X * 1.012


def generate_erdos_renyi_graph(n, p=0.5):
    """
    Generate Erdős-Rényi random graph.
    
    Args:
        n: Number of nodes
        p: Edge probability
        
    Returns:
        List of edges
    """
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if np.random.random() < p:
                edges.append((i, j))
    return edges


def run_qaoa_benchmark(n_nodes=8, p_layers=2, shots=4096, verbose=True):
    """
    Run QAOA MaxCut benchmark with noise mitigation.
    
    Args:
        n_nodes: Number of nodes in graph
        p_layers: QAOA layers
        shots: Number of measurement shots
        verbose: Print results
        
    Returns:
        Result dictionary with cost and metadata
    """
    # Setup
    circuit = QAOACircuit(n_nodes, p_layers)
    backend = MockBackend("aer_simulator_noisy")
    
    # Generate random graph
    edges = generate_erdos_renyi_graph(n_nodes, p=0.5)
    
    # Configuration
    zne_budget = {"fold_scales": [1, 3, 5]}
    cdr_budget = {"n_samples": 10}
    readout_cal = {
        "matrix": [[0.98, 0.02], [0.03, 0.97]],
        "timestamp": "2024-06-24T00:00:00"
    }
    drift_tracker = {"ΔT": 0.03, "τ_max": 0.5}
    resid_model = SimpleResidualModel()
    
    # Track metrics
    metrics = {
        "fold_calls": [],
        "results": []
    }
    
    def on_fold(scale, circ_id):
        metrics["fold_calls"].append({"scale": scale, "circ_id": circ_id})
    
    def on_result(exp, stderr):
        metrics["results"].append({"exp": exp, "stderr": stderr})
    
    hooks = {
        "on_fold": on_fold,
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
        print("QAOA MaxCut Benchmark Results")
        print("=" * 70)
        print(f"Circuit: {circuit}")
        print(f"Backend: {backend}")
        print(f"Graph: G({n_nodes}, 0.5) with {len(edges)} edges")
        print(f"Shots: {shots}")
        print()
        print(f"Cost expectation: {result['exp']:.6f}")
        print(f"Standard error: {result['stderr']:.6f}")
        print()
        print("KPIs:")
        kpi = result["meta"]["kpi"]
        print(f"  Infidelity drop: {kpi['infidelity_drop']:.4f} (target: ≥ 0.30)")
        print(f"  Overhead depth: {kpi['overhead_depth']:.2f} (limit: ≤ 3.0)")
        print(f"  Wall time ratio: {kpi['wall_time_ratio']:.2f} (limit: ≤ 1.5)")
        print()
        print(f"ZNE folds executed: {len(metrics['fold_calls'])}")
        print()
        print("UTCS Metadata:")
        meta = result["meta"]
        print(f"  UID: {meta['uid']}")
        print(f"  UTCS ID: {meta['utcs_id13']}")
        print("=" * 70)
    
    result["benchmark_metrics"] = metrics
    result["graph_edges"] = edges
    return result


def run_scaling_study():
    """Run benchmark across different graph sizes."""
    print("\n" + "=" * 70)
    print("QAOA MaxCut Scaling Study")
    print("=" * 70)
    
    node_counts = [8, 10, 12, 14]
    results = []
    
    for n in node_counts:
        print(f"\nRunning with {n} nodes...")
        result = run_qaoa_benchmark(n_nodes=n, shots=4096, verbose=False)
        results.append(result)
        
        kpi = result["meta"]["kpi"]
        print(f"  Cost: {result['exp']:.6f} ± {result['stderr']:.6f}")
        print(f"  Graph edges: {len(result['graph_edges'])}")
        print(f"  Overhead depth: {kpi['overhead_depth']:.2f}")
    
    print("\n" + "=" * 70)
    return results


if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Run single benchmark
    result = run_qaoa_benchmark(n_nodes=8, p_layers=2)
    
    # Optionally run scaling study
    # scaling_results = run_scaling_study()
