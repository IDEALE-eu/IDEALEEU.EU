#!/usr/bin/env python3
"""
Compare Metrics Script

This script compares metrics from simulation results against baseline values
and reports differences exceeding tolerance thresholds.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Tuple, List


DEFAULT_TOLERANCES = {
    "mass": 0.01,           # 1%
    "energy_kwh": 0.02,     # 2%
    "peak_temp_C": 2.0,     # 2°C absolute
    "mass_flow_kg_s": 0.03, # 3%
    "runtime_s": None,      # Not checked (machine-dependent)
}


def load_metrics(file_path: Path) -> Dict:
    """Load metrics from JSON file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Metrics file not found: {file_path}")
    
    with open(file_path, 'r') as f:
        return json.load(f)


def compare_value(baseline: float, current: float, tolerance: float, 
                  is_absolute: bool = False) -> Tuple[bool, float]:
    """
    Compare two values with tolerance.
    
    Args:
        baseline: Baseline value
        current: Current value
        tolerance: Tolerance (relative or absolute)
        is_absolute: If True, tolerance is absolute; else relative
        
    Returns:
        Tuple of (passed, difference)
    """
    if baseline == 0:
        # Avoid division by zero
        diff = abs(current - baseline)
        passed = diff <= tolerance if is_absolute else current == baseline
    else:
        if is_absolute:
            diff = abs(current - baseline)
            passed = diff <= tolerance
        else:
            diff = abs((current - baseline) / baseline)
            passed = diff <= tolerance
    
    return passed, diff


def compare_metrics(baseline_path: Path, current_path: Path, 
                   tolerances: Dict = None) -> Tuple[bool, Dict]:
    """
    Compare current metrics against baseline.
    
    Args:
        baseline_path: Path to baseline metrics.json
        current_path: Path to current metrics.json
        tolerances: Dictionary of tolerances per metric
        
    Returns:
        Tuple of (all_passed, differences_dict)
    """
    if tolerances is None:
        tolerances = DEFAULT_TOLERANCES
    
    baseline = load_metrics(baseline_path)
    current = load_metrics(current_path)
    
    differences = {}
    all_passed = True
    
    # Check each metric with defined tolerance
    for metric, tolerance in tolerances.items():
        if tolerance is None:
            # Skip this metric
            continue
        
        if metric not in baseline:
            differences[metric] = {
                "status": "missing_baseline",
                "message": f"Metric not in baseline"
            }
            continue
        
        if metric not in current:
            differences[metric] = {
                "status": "missing_current",
                "message": f"Metric not in current results"
            }
            all_passed = False
            continue
        
        baseline_val = baseline[metric]
        current_val = current[metric]
        
        # Determine if tolerance is absolute (for temperature)
        is_absolute = "temp" in metric.lower()
        
        passed, diff = compare_value(baseline_val, current_val, tolerance, is_absolute)
        
        differences[metric] = {
            "status": "pass" if passed else "fail",
            "baseline": baseline_val,
            "current": current_val,
            "difference": diff,
            "tolerance": tolerance,
            "absolute": is_absolute
        }
        
        if not passed:
            all_passed = False
    
    return all_passed, differences


def print_results(differences: Dict, verbose: bool = False):
    """Print comparison results."""
    print("\nMetric Comparison Results")
    print("=" * 80)
    
    for metric, info in differences.items():
        status = info["status"]
        
        if status == "pass":
            if verbose:
                print(f"✓ {metric:20s} PASS")
                print(f"  Baseline: {info['baseline']:.6g}")
                print(f"  Current:  {info['current']:.6g}")
                print(f"  Diff:     {info['difference']:.6g} " +
                      f"({'absolute' if info['absolute'] else 'relative'})")
        elif status == "fail":
            print(f"✗ {metric:20s} FAIL")
            print(f"  Baseline:  {info['baseline']:.6g}")
            print(f"  Current:   {info['current']:.6g}")
            print(f"  Diff:      {info['difference']:.6g} " +
                  f"({'absolute' if info['absolute'] else 'relative'})")
            print(f"  Tolerance: {info['tolerance']:.6g}")
        else:
            print(f"? {metric:20s} {status.upper()}")
            print(f"  Message: {info['message']}")
        
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Compare simulation metrics against baseline"
    )
    parser.add_argument("--baseline", required=True, 
                       help="Path to baseline metrics.json")
    parser.add_argument("--current", required=True,
                       help="Path to current metrics.json")
    parser.add_argument("--tolerance", type=float,
                       help="Override default tolerance (relative)")
    parser.add_argument("--verbose", action="store_true",
                       help="Show all comparisons including passes")
    
    args = parser.parse_args()
    
    baseline_path = Path(args.baseline).resolve()
    current_path = Path(args.current).resolve()
    
    # Override tolerances if specified
    tolerances = DEFAULT_TOLERANCES.copy()
    if args.tolerance:
        for key in tolerances:
            if tolerances[key] is not None:
                tolerances[key] = args.tolerance
    
    try:
        all_passed, differences = compare_metrics(
            baseline_path, 
            current_path, 
            tolerances
        )
        
        print_results(differences, args.verbose)
        
        if all_passed:
            print("=" * 80)
            print("✓ All metrics within tolerance")
            return 0
        else:
            print("=" * 80)
            print("✗ Some metrics outside tolerance")
            return 1
            
    except Exception as e:
        print(f"ERROR: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
