#!/usr/bin/env python3
"""
profile.py - Profile surrogate model latency and throughput.

This script measures:
1. Inference latency (mean, p50, p95, p99)
2. Throughput (queries per second)
3. Memory footprint during inference
4. Scalability with batch size

Usage:
    python profile.py --model-dir ../aero_wing_cl_cd/1.0.0/ --n-samples 1000

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Dict, Any, List

import numpy as np

try:
    import joblib
except ImportError:
    joblib = None

try:
    import psutil
except ImportError:
    psutil = None

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_model(model_dir: Path):
    """Load trained model and scalers."""
    model_file = model_dir / 'model.joblib'
    logger.info(f"Loading model from {model_file}")
    model = joblib.load(model_file)
    
    scaler_X_file = model_dir / 'scaler_X.joblib'
    scaler_y_file = model_dir / 'scaler_y.joblib'
    
    scaler_X = joblib.load(scaler_X_file) if scaler_X_file.exists() else None
    scaler_y = joblib.load(scaler_y_file) if scaler_y_file.exists() else None
    
    return model, scaler_X, scaler_y


def generate_test_inputs(n_samples: int, n_features: int) -> np.ndarray:
    """Generate random test inputs."""
    return np.random.rand(n_samples, n_features)


def profile_single_inference(model: Any, scaler_X: Any, scaler_y: Any, X_sample: np.ndarray, 
                             n_iterations: int = 1000) -> Dict[str, float]:
    """
    Profile single-sample inference latency.
    
    Returns:
        Dictionary of latency statistics in milliseconds
    """
    logger.info(f"Profiling single inference over {n_iterations} iterations...")
    
    latencies = []
    
    for _ in range(n_iterations):
        X_input = X_sample.copy()
        
        # Time the full inference pipeline
        start_time = time.perf_counter()
        
        if scaler_X is not None:
            X_scaled = scaler_X.transform(X_input.reshape(1, -1))
        else:
            X_scaled = X_input.reshape(1, -1)
        
        y_pred = model.predict(X_scaled)
        
        if scaler_y is not None:
            y_pred = scaler_y.inverse_transform(y_pred.reshape(-1, 1))
        
        end_time = time.perf_counter()
        
        latency_ms = (end_time - start_time) * 1000
        latencies.append(latency_ms)
    
    latencies = np.array(latencies)
    
    stats = {
        'mean_ms': np.mean(latencies),
        'median_ms': np.median(latencies),
        'std_ms': np.std(latencies),
        'min_ms': np.min(latencies),
        'max_ms': np.max(latencies),
        'p50_ms': np.percentile(latencies, 50),
        'p95_ms': np.percentile(latencies, 95),
        'p99_ms': np.percentile(latencies, 99)
    }
    
    logger.info(f"Single inference latency: mean={stats['mean_ms']:.4f} ms, "
                f"p95={stats['p95_ms']:.4f} ms, p99={stats['p99_ms']:.4f} ms")
    
    return stats


def profile_batch_inference(model: Any, scaler_X: Any, scaler_y: Any, X_batch: np.ndarray) -> Dict[str, float]:
    """
    Profile batch inference throughput.
    
    Returns:
        Dictionary of throughput statistics
    """
    logger.info(f"Profiling batch inference with {X_batch.shape[0]} samples...")
    
    start_time = time.perf_counter()
    
    if scaler_X is not None:
        X_scaled = scaler_X.transform(X_batch)
    else:
        X_scaled = X_batch
    
    y_pred = model.predict(X_scaled)
    
    if scaler_y is not None:
        y_pred = scaler_y.inverse_transform(y_pred.reshape(-1, 1))
    
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    throughput = X_batch.shape[0] / elapsed_time
    
    stats = {
        'batch_size': X_batch.shape[0],
        'elapsed_time_s': elapsed_time,
        'throughput_qps': throughput,
        'latency_per_sample_ms': (elapsed_time / X_batch.shape[0]) * 1000
    }
    
    logger.info(f"Batch inference: {throughput:.1f} queries/sec, "
                f"{stats['latency_per_sample_ms']:.4f} ms/sample")
    
    return stats


def profile_memory_footprint(model: Any) -> Dict[str, float]:
    """
    Estimate memory footprint of model.
    
    Returns:
        Dictionary of memory statistics in MB
    """
    logger.info("Profiling memory footprint...")
    
    if psutil is None:
        logger.warning("psutil not available, skipping memory profiling")
        return {}
    
    import os
    process = psutil.Process(os.getpid())
    
    # Get current memory usage
    mem_before = process.memory_info().rss / (1024 ** 2)  # MB
    
    # Try to estimate model size
    # This is approximate and model-specific
    import sys
    model_size_mb = sys.getsizeof(model) / (1024 ** 2)
    
    mem_after = process.memory_info().rss / (1024 ** 2)  # MB
    
    stats = {
        'model_size_estimate_mb': model_size_mb,
        'process_memory_mb': mem_after,
        'memory_delta_mb': mem_after - mem_before
    }
    
    logger.info(f"Memory footprint: model ~{model_size_mb:.2f} MB, "
                f"process ~{mem_after:.2f} MB")
    
    return stats


def profile_scalability(model: Any, scaler_X: Any, scaler_y: Any, n_features: int, 
                        batch_sizes: List[int]) -> Dict[str, Any]:
    """
    Profile scalability with different batch sizes.
    
    Returns:
        Dictionary of scalability results
    """
    logger.info(f"Profiling scalability with batch sizes: {batch_sizes}")
    
    results = []
    
    for batch_size in batch_sizes:
        X_batch = generate_test_inputs(batch_size, n_features)
        stats = profile_batch_inference(model, scaler_X, scaler_y, X_batch)
        results.append({
            'batch_size': batch_size,
            'throughput_qps': stats['throughput_qps'],
            'latency_per_sample_ms': stats['latency_per_sample_ms']
        })
    
    return {'scalability': results}


def save_profile_results(results: Dict[str, Any], output_dir: Path) -> None:
    """Save profiling results to JSON."""
    runtime_dir = output_dir / 'runtime'
    runtime_dir.mkdir(parents=True, exist_ok=True)
    
    profile_file = runtime_dir / 'profile_results.json'
    
    with open(profile_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"Profile results saved to {profile_file}")


def main():
    """Main profiling pipeline."""
    parser = argparse.ArgumentParser(description='Profile surrogate model performance')
    parser.add_argument('--model-dir', type=Path, required=True, help='Path to model directory')
    parser.add_argument('--n-samples', type=int, default=1000, help='Number of samples for single inference profiling')
    parser.add_argument('--batch-size', type=int, default=1000, help='Batch size for throughput test')
    parser.add_argument('--n-features', type=int, default=2, help='Number of input features')
    
    args = parser.parse_args()
    
    logger.info("=" * 80)
    logger.info("SURROGATE MODEL PROFILING")
    logger.info("=" * 80)
    
    # Load model
    model, scaler_X, scaler_y = load_model(args.model_dir)
    
    # Generate test input
    X_sample = generate_test_inputs(1, args.n_features)[0]
    X_batch = generate_test_inputs(args.batch_size, args.n_features)
    
    # Collect all profiling results
    results = {
        'timestamp': np.datetime64('now').astype(str),
        'model_dir': str(args.model_dir),
        'profiling': {}
    }
    
    # 1. Profile single inference latency
    latency_stats = profile_single_inference(model, scaler_X, scaler_y, X_sample, n_iterations=args.n_samples)
    results['profiling']['latency'] = latency_stats
    
    # 2. Profile batch inference throughput
    throughput_stats = profile_batch_inference(model, scaler_X, scaler_y, X_batch)
    results['profiling']['throughput'] = throughput_stats
    
    # 3. Profile memory footprint
    memory_stats = profile_memory_footprint(model)
    results['profiling']['memory'] = memory_stats
    
    # 4. Profile scalability
    batch_sizes = [1, 10, 100, 1000, 10000]
    scalability_stats = profile_scalability(model, scaler_X, scaler_y, args.n_features, batch_sizes)
    results['profiling'].update(scalability_stats)
    
    # Save results
    save_profile_results(results, args.model_dir)
    
    # Summary
    logger.info("=" * 80)
    logger.info("PROFILING COMPLETE")
    logger.info(f"  Mean latency: {latency_stats['mean_ms']:.4f} ms")
    logger.info(f"  p95 latency: {latency_stats['p95_ms']:.4f} ms")
    logger.info(f"  p99 latency: {latency_stats['p99_ms']:.4f} ms")
    logger.info(f"  Throughput: {throughput_stats['throughput_qps']:.1f} queries/sec")
    logger.info("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
