#!/usr/bin/env python3
"""
CFD Runner Script

This script orchestrates CFD simulations with timeout handling,
logging, and metric extraction.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path


def run_cfd_case(case_path: Path, timeout: int = 3600) -> int:
    """
    Run a CFD case with timeout.
    
    Args:
        case_path: Path to the case directory
        timeout: Maximum runtime in seconds
        
    Returns:
        Exit code (0 for success)
    """
    print(f"Running CFD case: {case_path}")
    print(f"Timeout: {timeout}s")
    
    # Check if case directory exists
    if not case_path.exists():
        print(f"ERROR: Case directory not found: {case_path}")
        return 1
    
    # Check for solver script (example: Allrun)
    allrun = case_path / "Allrun"
    if allrun.exists():
        print("Found Allrun script, executing...")
        try:
            result = subprocess.run(
                [str(allrun)],
                cwd=case_path,
                timeout=timeout,
                capture_output=True,
                text=True
            )
            print(result.stdout)
            if result.returncode != 0:
                print(f"ERROR: {result.stderr}")
            return result.returncode
        except subprocess.TimeoutExpired:
            print(f"ERROR: Case exceeded timeout of {timeout}s")
            return 1
    else:
        print("WARNING: No Allrun script found. Implement solver-specific logic here.")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Run CFD cases")
    parser.add_argument("--case", required=True, help="Path to case directory")
    parser.add_argument("--timeout", type=int, default=3600, 
                       help="Timeout in seconds (default: 3600)")
    
    args = parser.parse_args()
    case_path = Path(args.case).resolve()
    
    start_time = time.time()
    exit_code = run_cfd_case(case_path, args.timeout)
    elapsed = time.time() - start_time
    
    print(f"\nCompleted in {elapsed:.1f}s")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
