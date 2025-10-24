#!/usr/bin/env python3
"""
Export Metrics Script

This script exports metrics from CAE cases to a standardized format.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict


def export_metrics(case_path: Path) -> Dict:
    """
    Export metrics from a case directory.
    
    Args:
        case_path: Path to the case directory
        
    Returns:
        Dictionary of metrics
    """
    print(f"Exporting metrics from: {case_path}")
    
    # Look for existing metrics file
    metrics_file = case_path / "metrics.json"
    
    if metrics_file.exists():
        with open(metrics_file, 'r') as f:
            metrics = json.load(f)
        print("Found existing metrics.json")
    else:
        # Create default metrics
        metrics = {
            "mass": 0.0,
            "energy_kwh": 0.0,
            "peak_temp_C": 0.0,
            "mass_flow_kg_s": 0.0,
            "runtime_s": 0.0,
            "notes": "Default metrics - update with actual values"
        }
        print("No metrics.json found, created default")
    
    # Validate required keys
    required_keys = ["mass", "energy_kwh", "peak_temp_C", "mass_flow_kg_s", "runtime_s"]
    missing_keys = [key for key in required_keys if key not in metrics]
    
    if missing_keys:
        print(f"WARNING: Missing required metric keys: {missing_keys}")
    
    # Save metrics
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Metrics saved to: {metrics_file}")
    print(json.dumps(metrics, indent=2))
    
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Export CAE metrics")
    parser.add_argument("--case", required=True, help="Path to case directory")
    parser.add_argument("--output", help="Optional output file path")
    
    args = parser.parse_args()
    case_path = Path(args.case).resolve()
    
    if not case_path.exists():
        print(f"ERROR: Case directory not found: {case_path}")
        return 1
    
    metrics = export_metrics(case_path)
    
    # Optionally save to a different location
    if args.output:
        output_path = Path(args.output).resolve()
        with open(output_path, 'w') as f:
            json.dump(metrics, f, indent=2)
        print(f"Also saved to: {output_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
