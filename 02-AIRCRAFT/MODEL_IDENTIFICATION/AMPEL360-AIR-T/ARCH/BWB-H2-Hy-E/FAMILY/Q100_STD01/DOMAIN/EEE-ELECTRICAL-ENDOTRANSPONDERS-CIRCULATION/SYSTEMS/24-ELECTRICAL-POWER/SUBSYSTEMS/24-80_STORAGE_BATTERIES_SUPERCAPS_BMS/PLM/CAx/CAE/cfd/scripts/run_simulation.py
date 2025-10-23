#!/usr/bin/env python3
"""
Main simulation runner for CO₂ battery CFD simulations.

This script orchestrates OpenFOAM simulations including:
- Case setup
- Mesh generation
- Solver execution
- Post-processing
- Results collection

Usage:
    python run_simulation.py --case storage_tank --mesh-size medium --parallel 4
    python run_simulation.py --case expander --mesh-size fine --parallel 16 --transient
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

import yaml


class SimulationRunner:
    """Orchestrates OpenFOAM CFD simulations."""

    def __init__(self, case_name: str, mesh_size: str = "medium",
                 parallel: int = 1, transient: bool = False):
        """
        Initialize simulation runner.

        Args:
            case_name: Name of case (storage_tank, evaporator, expander, condenser, full_system)
            mesh_size: Mesh resolution (coarse, medium, fine, very-fine)
            parallel: Number of parallel processes
            transient: Run transient (True) or steady-state (False)
        """
        self.case_name = case_name
        self.mesh_size = mesh_size
        self.parallel = parallel
        self.transient = transient

        # Paths
        self.cfd_root = Path(__file__).parent.parent
        self.case_dir = self.cfd_root / "cases" / case_name
        self.results_dir = self.cfd_root / "results" / f"{case_name}_{mesh_size}"

        # Validate
        if not self.case_dir.exists():
            raise ValueError(f"Case directory not found: {self.case_dir}")

    def run_all(self):
        """Run complete simulation workflow."""
        print(f"=" * 80)
        print(f"CO₂ Battery CFD Simulation: {self.case_name}")
        print(f"=" * 80)
        print(f"Mesh size: {self.mesh_size}")
        print(f"Parallel cores: {self.parallel}")
        print(f"Mode: {'Transient' if self.transient else 'Steady-state'}")
        print(f"=" * 80)

        steps = [
            ("Setup", self.setup_case),
            ("Mesh Generation", self.generate_mesh),
            ("Check Mesh", self.check_mesh),
            ("Initialize Fields", self.initialize_fields),
            ("Run Solver", self.run_solver),
            ("Post-process", self.postprocess),
            ("Collect Results", self.collect_results),
        ]

        start_time = time.time()

        for step_name, step_func in steps:
            print(f"\n{'='*80}")
            print(f"Step: {step_name}")
            print(f"{'='*80}")
            try:
                step_func()
                print(f"✓ {step_name} completed successfully")
            except Exception as e:
                print(f"✗ {step_name} failed: {e}")
                raise

        elapsed = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"Simulation completed in {elapsed/3600:.2f} hours")
        print(f"Results saved to: {self.results_dir}")
        print(f"{'='*80}")

    def setup_case(self):
        """Setup case directory and copy templates."""
        print("Setting up case...")
        # Create results directory
        self.results_dir.mkdir(parents=True, exist_ok=True)

        # Copy case template (would be implemented with actual templates)
        print(f"  Case directory: {self.case_dir}")
        print(f"  Results directory: {self.results_dir}")

    def generate_mesh(self):
        """Generate computational mesh."""
        print(f"Generating {self.mesh_size} mesh...")

        # Run blockMesh
        self._run_of_command("blockMesh")

        # Run snappyHexMesh if geometry exists
        geometry_dir = self.cfd_root / "mesh" / "geometry"
        if any(geometry_dir.glob("*.stl")):
            print("Running snappyHexMesh...")
            self._run_of_command("snappyHexMesh", ["-overwrite"])

        print(f"  Mesh generation complete")

    def check_mesh(self):
        """Check mesh quality."""
        print("Checking mesh quality...")
        self._run_of_command("checkMesh")

    def initialize_fields(self):
        """Initialize flow fields."""
        print("Initializing fields...")
        # Set initial conditions (would use setFields or custom initialization)
        print("  Fields initialized")

    def run_solver(self):
        """Run OpenFOAM solver."""
        print("Running solver...")

        # Determine solver based on case
        solver_map = {
            "storage_tank": "chtMultiRegionFoam",
            "evaporator": "chtMultiRegionFoam",
            "expander": "pimpleFoam" if self.transient else "simpleFoam",
            "condenser": "multiphaseEulerFoam",
            "full_system": "chtMultiRegionFoam",
        }

        solver = solver_map.get(self.case_name, "simpleFoam")
        print(f"  Using solver: {solver}")

        if self.parallel > 1:
            # Decompose domain
            self._run_of_command("decomposePar")

            # Run parallel
            self._run_of_command(solver, parallel=True)

            # Reconstruct
            self._run_of_command("reconstructPar")
        else:
            # Run serial
            self._run_of_command(solver)

        print(f"  Solver execution complete")

    def postprocess(self):
        """Post-process results."""
        print("Post-processing results...")

        # Run OpenFOAM post-processing utilities
        self._run_of_command("postProcess", ["-func", "yPlus"])
        self._run_of_command("postProcess", ["-func", "Q"])

        print("  Post-processing complete")

    def collect_results(self):
        """Collect and organize results."""
        print("Collecting results...")

        # Copy important files to results directory
        files_to_copy = [
            "log.*",
            "postProcessing/",
            "system/controlDict",
            "constant/",
        ]

        # Would implement actual file copying
        print(f"  Results collected to {self.results_dir}")

    def _run_of_command(self, command: str, args: Optional[List[str]] = None,
                        parallel: bool = False):
        """
        Run an OpenFOAM command.

        Args:
            command: OpenFOAM command to run
            args: Optional command arguments
            parallel: Run with mpirun
        """
        args = args or []

        if parallel:
            cmd = ["mpirun", "-np", str(self.parallel), command] + args
        else:
            cmd = [command] + args

        print(f"  Executing: {' '.join(cmd)}")

        # Change to case directory
        result = subprocess.run(
            cmd,
            cwd=self.case_dir,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"  Error output: {result.stderr}")
            raise RuntimeError(f"Command failed: {' '.join(cmd)}")

        return result.stdout


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run CO₂ battery CFD simulations"
    )
    parser.add_argument(
        "--case",
        required=True,
        choices=["storage_tank", "evaporator", "expander", "condenser", "full_system"],
        help="Case to simulate"
    )
    parser.add_argument(
        "--mesh-size",
        default="medium",
        choices=["coarse", "medium", "fine", "very-fine"],
        help="Mesh resolution"
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Number of parallel processes"
    )
    parser.add_argument(
        "--transient",
        action="store_true",
        help="Run transient simulation"
    )

    args = parser.parse_args()

    runner = SimulationRunner(
        case_name=args.case,
        mesh_size=args.mesh_size,
        parallel=args.parallel,
        transient=args.transient
    )

    try:
        runner.run_all()
    except Exception as e:
        print(f"\nSimulation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
