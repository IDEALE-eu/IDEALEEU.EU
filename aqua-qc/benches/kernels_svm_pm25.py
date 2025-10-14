"""
Quantum Kernel SVM for PM2.5 Prediction

Benchmark quantum kernel methods on air quality (PM2.5) time-series data.
Tests environmental monitoring capabilities.
"""

import sys
from pathlib import Path

import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algos.qml_env_002 import train_quantum_kernel


def generate_pm25_data(n_samples=200, n_features=10, window_size=24):
    """
    Generate synthetic PM2.5 time-series data.
    
    Args:
        n_samples: Number of samples
        n_features: Number of features per sample
        window_size: Temporal window size (hours)
        
    Returns:
        Training and validation data
    """
    np.random.seed(42)
    
    # Split into train/val
    n_train = int(0.7 * n_samples)
    n_val = n_samples - n_train
    
    # Generate synthetic features
    # Simulates: temperature, humidity, wind, traffic, etc.
    X = np.random.randn(n_samples, n_features)
    
    # Add temporal correlation
    for i in range(1, n_samples):
        X[i] += 0.3 * X[i - 1]
    
    # Generate PM2.5 values (regression target)
    # Higher values indicate anomalies
    y = 20 + 10 * np.sin(np.arange(n_samples) * 0.1) + 5 * np.random.randn(n_samples)
    y = np.maximum(y, 0)  # PM2.5 can't be negative
    
    # Binary labels for anomaly detection (PM2.5 > 50)
    y_binary = (y > 50).astype(int)
    
    # Split
    X_train, X_val = X[:n_train], X[n_train:]
    y_train, y_val = y_binary[:n_train], y_binary[n_train:]
    
    return {
        "X_train": X_train,
        "y_train": y_train,
        "X_val": X_val,
        "y_val": y_val,
        "y_continuous": y
    }


def run_pm25_benchmark(
    n_samples=200,
    n_features=10,
    nyström=None,
    mix_classical=True,
    verbose=True
):
    """
    Run PM2.5 prediction benchmark with quantum kernel.
    
    Args:
        n_samples: Number of samples
        n_features: Number of features
        nyström: Nyström approximation landmarks
        mix_classical: Use hybrid features
        verbose: Print results
        
    Returns:
        Result dictionary with metrics
    """
    # Generate data
    data = generate_pm25_data(n_samples, n_features)
    
    # Configuration
    feature_map_cfg = {
        "type": "ZZ",
        "n_qubits": min(8, n_features),
        "reps": 2
    }
    
    temporal_embed_cfg = {
        "window_size": 6,  # 6-hour window
        "stride": 1,
        "aggregation": "mean"
    }
    
    # Track metrics
    metrics = {
        "embed_stats": [],
        "kernel_spectrum": [],
        "domain_adapt": [],
        "eval_results": []
    }
    
    def on_embed_stat(mean_amp, sparsity):
        metrics["embed_stats"].append({"mean_amp": mean_amp, "sparsity": sparsity})
    
    def on_kernel_spectrum(cond_num, eig_decay):
        metrics["kernel_spectrum"].append({"cond_num": cond_num, "eig_decay": eig_decay})
    
    def on_domain_adapt(mmd, coral_loss):
        metrics["domain_adapt"].append({"mmd": mmd, "coral_loss": coral_loss})
    
    def on_eval(f1, rmse, energy_j):
        metrics["eval_results"].append({"f1": f1, "rmse": rmse, "energy_j": energy_j})
    
    hooks = {
        "on_embed_stat": on_embed_stat,
        "on_kernel_spectrum": on_kernel_spectrum,
        "on_domain_adapt": on_domain_adapt,
        "on_eval": on_eval
    }
    
    # Train model
    result = train_quantum_kernel(
        X_train=data["X_train"],
        y_train=data["y_train"],
        X_val=data["X_val"],
        y_val=data["y_val"],
        feature_map_cfg=feature_map_cfg,
        temporal_embed_cfg=temporal_embed_cfg,
        nyström=nyström,
        mix_classical=mix_classical,
        hooks=hooks,
        uid="Qiskit_002_20240624_APCGPT"
    )
    
    if verbose:
        print("=" * 70)
        print("PM2.5 Quantum Kernel SVM Benchmark Results")
        print("=" * 70)
        print(f"Samples: {n_samples} (train: {len(data['X_train'])}, val: {len(data['X_val'])})")
        print(f"Features: {n_features}")
        print(f"Quantum feature map: {feature_map_cfg['type']} ({feature_map_cfg['n_qubits']} qubits)")
        print(f"Nyström landmarks: {nyström if nyström else 'None (exact)'}")
        print(f"Hybrid features: {'Yes' if mix_classical else 'No'}")
        print()
        
        val_metrics = result["val_metrics"]
        print("Validation Metrics:")
        print(f"  F1 Score: {val_metrics['f1']:.4f} (target: ≥ 0.80)")
        print(f"  RMSE: {val_metrics['rmse']:.4f}")
        print(f"  Energy per inference: {val_metrics['energy_j']:.6f} J")
        print()
        
        print("KPIs:")
        kpi = result["meta"]["kpi"]
        print(f"  F1 Anomaly: {kpi['F1_anomaly']:.4f} (target: ≥ 0.80)")
        print(f"  RMSE Drop: {kpi['RMSE_drop']:.4f} (target: ≥ 0.10)")
        print(f"  Energy Drop: {kpi['Energy_per_inf_drop']:.4f} (target: ≥ 0.15)")
        print()
        
        if metrics["kernel_spectrum"]:
            spectrum = metrics["kernel_spectrum"][0]
            print("Kernel Statistics:")
            print(f"  Condition number: {spectrum['cond_num']:.2e}")
            print(f"  Eigenvalue decay: {spectrum['eig_decay']:.4f}")
            print()
        
        if metrics["domain_adapt"]:
            domain = metrics["domain_adapt"][0]
            print("Domain Adaptation:")
            print(f"  MMD: {domain['mmd']:.4f}")
            print(f"  CORAL loss: {domain['coral_loss']:.4f}")
            print()
        
        print("UTCS Metadata:")
        meta = result["meta"]
        print(f"  UID: {meta['uid']}")
        print(f"  UTCS ID: {meta['utcs_id13']}")
        print(f"  Bench case: {meta['bench_case']}")
        print("=" * 70)
    
    result["benchmark_metrics"] = metrics
    return result


def run_ablation_study():
    """Run ablation study on hybrid features and Nyström."""
    print("\n" + "=" * 70)
    print("PM2.5 Benchmark Ablation Study")
    print("=" * 70)
    
    configurations = [
        {"name": "Exact Kernel + Hybrid", "nyström": None, "mix_classical": True},
        {"name": "Exact Kernel + Quantum-only", "nyström": None, "mix_classical": False},
        {"name": "Nyström (50) + Hybrid", "nyström": 50, "mix_classical": True},
        {"name": "Nyström (50) + Quantum-only", "nyström": 50, "mix_classical": False},
    ]
    
    results = []
    
    for config in configurations:
        print(f"\n{config['name']}:")
        print("-" * 70)
        result = run_pm25_benchmark(
            n_samples=150,
            nyström=config["nyström"],
            mix_classical=config["mix_classical"],
            verbose=False
        )
        results.append(result)
        
        kpi = result["meta"]["kpi"]
        val_metrics = result["val_metrics"]
        print(f"  F1: {kpi['F1_anomaly']:.4f}")
        print(f"  RMSE drop: {kpi['RMSE_drop']:.4f}")
        print(f"  Energy: {val_metrics['energy_j']:.6f} J")
    
    print("\n" + "=" * 70)
    return results


if __name__ == "__main__":
    # Run single benchmark
    result = run_pm25_benchmark(n_samples=200, mix_classical=True)
    
    # Optionally run ablation study
    # ablation_results = run_ablation_study()
