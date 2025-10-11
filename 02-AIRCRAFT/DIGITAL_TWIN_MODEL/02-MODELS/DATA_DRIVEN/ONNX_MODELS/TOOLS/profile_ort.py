#!/usr/bin/env python3
"""
Profile ONNX Runtime performance: measure latency, throughput, and memory usage.

Usage:
    python profile_ort.py --model <model.onnx> --batch-size 1 --iterations 100

Profiling metrics:
    - Inference latency (mean, p50, p95, p99)
    - Throughput (inferences per second)
    - Memory usage (peak RSS)
    - Per-operator timing breakdown
"""

import argparse
import logging
import sys
import time
from pathlib import Path
from typing import Dict, Any

import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_memory_usage():
    """Get current memory usage in MB."""
    try:
        import psutil
        process = psutil.Process()
        return process.memory_info().rss / (1024 * 1024)  # MB
    except ImportError:
        logger.warning("psutil not available, memory profiling disabled")
        return None


def profile_latency(session, input_data: Dict[str, np.ndarray], 
                    output_names: list, iterations: int = 100) -> Dict[str, float]:
    """Profile inference latency."""
    logger.info(f"Profiling latency over {iterations} iterations...")
    
    # Warmup
    for _ in range(10):
        session.run(output_names, input_data)
    
    # Measure latency
    latencies = []
    for i in range(iterations):
        start = time.perf_counter()
        session.run(output_names, input_data)
        end = time.perf_counter()
        latencies.append((end - start) * 1000)  # Convert to ms
    
    latencies = np.array(latencies)
    
    results = {
        "mean_ms": float(np.mean(latencies)),
        "std_ms": float(np.std(latencies)),
        "p50_ms": float(np.percentile(latencies, 50)),
        "p95_ms": float(np.percentile(latencies, 95)),
        "p99_ms": float(np.percentile(latencies, 99)),
        "min_ms": float(np.min(latencies)),
        "max_ms": float(np.max(latencies))
    }
    
    logger.info(f"Latency results:")
    logger.info(f"  Mean:    {results['mean_ms']:.2f} ms")
    logger.info(f"  Std:     {results['std_ms']:.2f} ms")
    logger.info(f"  P50:     {results['p50_ms']:.2f} ms")
    logger.info(f"  P95:     {results['p95_ms']:.2f} ms")
    logger.info(f"  P99:     {results['p99_ms']:.2f} ms")
    
    return results


def profile_throughput(session, input_data: Dict[str, np.ndarray], 
                       output_names: list, duration_sec: int = 10) -> Dict[str, float]:
    """Profile inference throughput."""
    logger.info(f"Profiling throughput over {duration_sec} seconds...")
    
    count = 0
    start = time.perf_counter()
    end = start + duration_sec
    
    while time.perf_counter() < end:
        session.run(output_names, input_data)
        count += 1
    
    elapsed = time.perf_counter() - start
    throughput = count / elapsed
    
    logger.info(f"Throughput: {throughput:.2f} inferences/sec ({count} inferences in {elapsed:.2f}s)")
    
    return {
        "inferences_per_sec": throughput,
        "total_inferences": count,
        "duration_sec": elapsed
    }


def profile_memory(session, input_data: Dict[str, np.ndarray], 
                   output_names: list, iterations: int = 100) -> Dict[str, float]:
    """Profile memory usage."""
    logger.info("Profiling memory usage...")
    
    mem_before = get_memory_usage()
    if mem_before is None:
        return {"error": "psutil not available"}
    
    # Run inference to measure memory
    for _ in range(iterations):
        session.run(output_names, input_data)
    
    mem_after = get_memory_usage()
    mem_increase = mem_after - mem_before
    
    logger.info(f"Memory usage:")
    logger.info(f"  Before:   {mem_before:.2f} MB")
    logger.info(f"  After:    {mem_after:.2f} MB")
    logger.info(f"  Increase: {mem_increase:.2f} MB")
    
    return {
        "before_mb": mem_before,
        "after_mb": mem_after,
        "increase_mb": mem_increase
    }


def profile_operators(model_path: str, input_data: Dict[str, np.ndarray]):
    """Profile per-operator timing."""
    try:
        import onnxruntime as ort
    except ImportError:
        logger.error("onnxruntime is required")
        sys.exit(1)
    
    logger.info("Profiling per-operator timing...")
    
    # Enable profiling
    options = ort.SessionOptions()
    options.enable_profiling = True
    
    sess = ort.InferenceSession(model_path, options)
    output_names = [out.name for out in sess.get_outputs()]
    
    # Run inference with profiling
    sess.run(output_names, input_data)
    
    # Get profile file
    prof_file = sess.end_profiling()
    logger.info(f"Profiling data saved to: {prof_file}")
    
    # Parse and display top operators
    try:
        import json
        with open(prof_file, 'r') as f:
            prof_data = json.load(f)
        
        # Sort by duration
        events = sorted(prof_data, key=lambda x: x.get('dur', 0), reverse=True)[:10]
        
        logger.info("\nTop 10 operators by time:")
        for i, event in enumerate(events):
            name = event.get('name', 'unknown')
            dur_us = event.get('dur', 0)
            logger.info(f"  {i+1}. {name}: {dur_us/1000:.2f} ms")
    
    except Exception as e:
        logger.warning(f"Could not parse profiling data: {e}")


def main():
    parser = argparse.ArgumentParser(description='Profile ONNX Runtime performance')
    parser.add_argument('--model', required=True, help='Path to ONNX model')
    parser.add_argument('--batch-size', type=int, default=1, help='Batch size for profiling')
    parser.add_argument('--iterations', type=int, default=100, help='Number of iterations for latency profiling')
    parser.add_argument('--duration', type=int, default=10, help='Duration in seconds for throughput profiling')
    parser.add_argument('--profile-ops', action='store_true', help='Enable per-operator profiling')
    parser.add_argument('--output', help='Output JSON file for results')
    
    args = parser.parse_args()
    
    if not Path(args.model).exists():
        logger.error(f"Model file not found: {args.model}")
        sys.exit(1)
    
    try:
        import onnxruntime as ort
    except ImportError:
        logger.error("onnxruntime is required")
        sys.exit(1)
    
    # Create session
    logger.info(f"Loading model from {args.model}")
    sess = ort.InferenceSession(args.model)
    
    input_names = [inp.name for inp in sess.get_inputs()]
    output_names = [out.name for out in sess.get_outputs()]
    
    # Create dummy input
    logger.info("Creating dummy input data...")
    input_shapes = [inp.shape for inp in sess.get_inputs()]
    input_data = {}
    for name, shape in zip(input_names, input_shapes):
        # Replace dynamic dimensions with batch size
        concrete_shape = [args.batch_size if (d is None or isinstance(d, str)) else d for d in shape]
        input_data[name] = np.random.randn(*concrete_shape).astype(np.float32)
    
    # Profile
    results = {
        "model": args.model,
        "batch_size": args.batch_size,
        "latency": profile_latency(sess, input_data, output_names, args.iterations),
        "throughput": profile_throughput(sess, input_data, output_names, args.duration),
        "memory": profile_memory(sess, input_data, output_names, args.iterations)
    }
    
    # Per-operator profiling
    if args.profile_ops:
        profile_operators(args.model, input_data)
    
    # Save results
    if args.output:
        import json
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        logger.info(f"\nResults saved to {args.output}")
    
    logger.info("\n" + "="*50)
    logger.info("✓ Profiling complete!")
    logger.info("="*50)


if __name__ == '__main__':
    main()
