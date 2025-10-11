#!/usr/bin/env python3
"""
gen_tables.py - Generate aerodynamic coefficient tables

This script generates CSV lookup tables for aerodynamic coefficients (CL, CD, Cm)
as functions of angle of attack (alpha) and Mach number.

Tables can be generated from:
1. CFD simulation results
2. Wind tunnel data
3. Semi-empirical methods (DATCOM, Vortex Lattice)
4. Fitted polynomials

Usage:
    python gen_tables.py --method datcom --output ../PARAMS/tables/
    python gen_tables.py --method cfd --input cfd_results.csv --output ../PARAMS/tables/
    python gen_tables.py --method fit --input wind_tunnel.csv --output ../PARAMS/tables/

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Tuple

import numpy as np


def datcom_cl(alpha_deg: float, mach: float) -> float:
    """
    Compute CL using DATCOM-like empirical method.
    
    Simplified linear lift curve with compressibility correction.
    """
    # Prandtl-Glauert compressibility correction
    beta = np.sqrt(1 - mach**2) if mach < 1.0 else 1.0
    
    # Linear region
    CL_alpha = 5.5 / beta  # per radian
    alpha_rad = np.deg2rad(alpha_deg)
    
    # Base trim point
    CL0 = 0.0
    
    # Linear model with saturation
    CL = CL0 + CL_alpha * alpha_rad
    
    # Apply stall limits (rough approximation)
    if alpha_deg > 12:
        stall_factor = 1.0 - 0.1 * (alpha_deg - 12)
        CL *= max(0.3, stall_factor)
    
    return CL


def datcom_cd(alpha_deg: float, mach: float) -> float:
    """
    Compute CD using DATCOM-like empirical method.
    
    Includes zero-lift drag and induced drag.
    """
    # Zero-lift drag (parasite drag)
    CD0 = 0.025
    
    # Wave drag near transonic
    if mach > 0.7:
        wave_drag = 0.015 * ((mach - 0.7) / 0.15)**2
        CD0 += wave_drag
    
    # Induced drag: CD_i = CL^2 / (pi * AR * e)
    # Assume AR ~= 10, e ~= 0.85
    CL = datcom_cl(alpha_deg, mach)
    AR = 10.0
    e = 0.85
    CD_induced = CL**2 / (np.pi * AR * e)
    
    return CD0 + CD_induced


def datcom_cm(alpha_deg: float, mach: float) -> float:
    """
    Compute Cm using DATCOM-like empirical method.
    
    Simple pitching moment model.
    """
    # Trim offset
    Cm0 = -0.05
    
    # Pitching moment slope
    Cm_alpha = -1.2  # per radian (negative = stable)
    alpha_rad = np.deg2rad(alpha_deg)
    
    return Cm0 + Cm_alpha * alpha_rad


def generate_table(alpha_range: Tuple[float, float, int],
                   mach_range: Tuple[float, float, int],
                   coeff_func,
                   output_path: Path):
    """
    Generate coefficient table over alpha-Mach grid.
    
    Args:
        alpha_range: (min, max, num_points) for alpha in degrees
        mach_range: (min, max, num_points) for Mach number
        coeff_func: Function(alpha_deg, mach) -> coefficient value
        output_path: Path to output CSV file
    """
    alpha_min, alpha_max, n_alpha = alpha_range
    mach_min, mach_max, n_mach = mach_range
    
    # Generate grid
    alpha_vals = np.linspace(alpha_min, alpha_max, n_alpha)
    mach_vals = np.linspace(mach_min, mach_max, n_mach)
    
    # Compute coefficients
    data = np.zeros((n_alpha, n_mach))
    for i, alpha in enumerate(alpha_vals):
        for j, mach in enumerate(mach_vals):
            data[i, j] = coeff_func(alpha, mach)
    
    # Write CSV
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header row
        header = ['alpha_deg'] + [f'{m:.1f}' for m in mach_vals]
        writer.writerow(header)
        
        # Data rows
        for i, alpha in enumerate(alpha_vals):
            row = [f'{alpha:.0f}'] + [f'{data[i, j]:.2f}' for j in range(n_mach)]
            writer.writerow(row)
    
    print(f"Generated {output_path.name}")
    print(f"  Alpha range: {alpha_min}° to {alpha_max}° ({n_alpha} points)")
    print(f"  Mach range: {mach_min} to {mach_max} ({n_mach} points)")


def generate_datcom_tables(output_dir: Path):
    """Generate tables using DATCOM empirical method."""
    print("\nGenerating tables using DATCOM method...")
    
    # Define grid
    alpha_range = (-10, 15, 6)  # -10° to 15° in 6 points
    mach_range = (0.0, 0.8, 5)  # 0.0 to 0.8 in 5 points
    
    # Generate CL table
    generate_table(alpha_range, mach_range, datcom_cl,
                   output_dir / 'CL_alpha_mach.csv')
    
    # Generate CD table
    generate_table(alpha_range, mach_range, datcom_cd,
                   output_dir / 'CD_alpha_mach.csv')
    
    # Generate Cm table
    generate_table(alpha_range, mach_range, datcom_cm,
                   output_dir / 'Cm_alpha_mach.csv')


def load_cfd_data(input_path: Path):
    """
    Load CFD results from CSV file.
    
    Expected format:
    alpha_deg,mach,CL,CD,Cm
    0.0,0.3,0.2,0.025,-0.05
    ...
    """
    print(f"\nLoading CFD data from {input_path}...")
    
    data = np.genfromtxt(input_path, delimiter=',', skip_header=1)
    
    alpha_vals = np.unique(data[:, 0])
    mach_vals = np.unique(data[:, 1])
    
    print(f"  Found {len(alpha_vals)} alpha points, {len(mach_vals)} Mach points")
    
    # Reshape into grids
    n_alpha = len(alpha_vals)
    n_mach = len(mach_vals)
    
    CL_grid = data[:, 2].reshape(n_alpha, n_mach)
    CD_grid = data[:, 3].reshape(n_alpha, n_mach)
    Cm_grid = data[:, 4].reshape(n_alpha, n_mach)
    
    return alpha_vals, mach_vals, CL_grid, CD_grid, Cm_grid


def generate_cfd_tables(input_path: Path, output_dir: Path):
    """Generate tables from CFD data."""
    alpha_vals, mach_vals, CL_grid, CD_grid, Cm_grid = load_cfd_data(input_path)
    
    # Write tables
    def write_table(filename, data_grid):
        path = output_dir / filename
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Header
            header = ['alpha_deg'] + [f'{m:.1f}' for m in mach_vals]
            writer.writerow(header)
            
            # Data
            for i, alpha in enumerate(alpha_vals):
                row = [f'{alpha:.0f}'] + [f'{data_grid[i, j]:.2f}' 
                                          for j in range(len(mach_vals))]
                writer.writerow(row)
        
        print(f"Generated {filename}")
    
    write_table('CL_alpha_mach.csv', CL_grid)
    write_table('CD_alpha_mach.csv', CD_grid)
    write_table('Cm_alpha_mach.csv', Cm_grid)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate aerodynamic coefficient lookup tables',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate using DATCOM method
  python gen_tables.py --method datcom --output ../PARAMS/tables/
  
  # Generate from CFD data
  python gen_tables.py --method cfd --input cfd_results.csv --output ../PARAMS/tables/
        """
    )
    
    parser.add_argument('--method', type=str, required=True,
                        choices=['datcom', 'cfd', 'fit'],
                        help='Method for generating tables')
    
    parser.add_argument('--input', type=Path,
                        help='Input data file (required for cfd/fit methods)')
    
    parser.add_argument('--output', type=Path, required=True,
                        help='Output directory for tables')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.method in ['cfd', 'fit'] and args.input is None:
        parser.error(f"--input is required for method '{args.method}'")
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Generate tables
    if args.method == 'datcom':
        generate_datcom_tables(args.output)
    
    elif args.method == 'cfd':
        if not args.input.exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            return 1
        generate_cfd_tables(args.input, args.output)
    
    elif args.method == 'fit':
        print("Fit method not yet implemented", file=sys.stderr)
        return 1
    
    print("\n✅ Table generation complete!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
