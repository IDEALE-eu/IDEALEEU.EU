"""
test_aero_interp.py - Tests for aerodynamic coefficient interpolation

This module tests the bilinear interpolation and coefficient build-up logic
for the aerodynamics block.

Test data is provided in golden_inputs.npz and golden_outputs.npz.
"""

import numpy as np
import yaml
import csv
from pathlib import Path


def load_csv_table(filepath):
    """
    Load a CSV table with alpha_deg in first column and Mach numbers as headers.
    
    Returns:
        alpha_vals: List of alpha values (degrees)
        mach_vals: List of Mach values
        data: 2D array of coefficient values [alpha_idx, mach_idx]
    """
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        # Extract Mach values from header (skip first column which is 'alpha_deg')
        mach_vals = [float(m) for m in header[1:]]
        
        alpha_vals = []
        data_rows = []
        
        for row in reader:
            alpha_vals.append(float(row[0]))
            data_rows.append([float(v) for v in row[1:]])
    
    return alpha_vals, mach_vals, np.array(data_rows)


def bilinear_interp(x, y, x_vals, y_vals, data):
    """
    Perform bilinear interpolation on a 2D grid.
    
    Args:
        x: Query point x-coordinate (alpha in degrees)
        y: Query point y-coordinate (Mach number)
        x_vals: List of x grid values (alpha values)
        y_vals: List of y grid values (Mach values)
        data: 2D array of data values [x_idx, y_idx]
    
    Returns:
        Interpolated value at (x, y)
    """
    # Find surrounding indices
    x_idx = np.searchsorted(x_vals, x) - 1
    y_idx = np.searchsorted(y_vals, y) - 1
    
    # Clamp to valid range
    x_idx = np.clip(x_idx, 0, len(x_vals) - 2)
    y_idx = np.clip(y_idx, 0, len(y_vals) - 2)
    
    # Get surrounding grid points
    x0, x1 = x_vals[x_idx], x_vals[x_idx + 1]
    y0, y1 = y_vals[y_idx], y_vals[y_idx + 1]
    
    # Compute interpolation weights
    tx = (x - x0) / (x1 - x0) if x1 != x0 else 0.0
    ty = (y - y0) / (y1 - y0) if y1 != y0 else 0.0
    
    # Bilinear interpolation
    f00 = data[x_idx, y_idx]
    f10 = data[x_idx + 1, y_idx]
    f01 = data[x_idx, y_idx + 1]
    f11 = data[x_idx + 1, y_idx + 1]
    
    result = (1 - tx) * (1 - ty) * f00 + \
             tx * (1 - ty) * f10 + \
             (1 - tx) * ty * f01 + \
             tx * ty * f11
    
    return result


def compute_aero_coeffs(alpha_deg, mach, delta_e_rad=0.0, params_dir='../PARAMS'):
    """
    Compute aerodynamic coefficients for given flight condition.
    
    Args:
        alpha_deg: Angle of attack (degrees)
        mach: Mach number
        delta_e_rad: Elevator deflection (radians)
        params_dir: Path to PARAMS directory
    
    Returns:
        Dictionary with CL, CD, Cm values
    """
    params_path = Path(__file__).parent.parent / 'PARAMS'
    
    # Load tables
    alpha_cl, mach_cl, cl_table = load_csv_table(params_path / 'tables' / 'CL_alpha_mach.csv')
    alpha_cd, mach_cd, cd_table = load_csv_table(params_path / 'tables' / 'CD_alpha_mach.csv')
    alpha_cm, mach_cm, cm_table = load_csv_table(params_path / 'tables' / 'Cm_alpha_mach.csv')
    
    # Base coefficients from tables
    CL_base = bilinear_interp(alpha_deg, mach, alpha_cl, mach_cl, cl_table)
    CD_base = bilinear_interp(alpha_deg, mach, alpha_cd, mach_cd, cd_table)
    Cm_base = bilinear_interp(alpha_deg, mach, alpha_cm, mach_cm, cm_table)
    
    # Load linear derivatives
    with open(params_path / 'coeffs_airframe.yaml', 'r') as f:
        coeffs = yaml.safe_load(f)
    
    # Load control effectiveness
    with open(params_path / 'control_effectiveness.yaml', 'r') as f:
        control = yaml.safe_load(f)
    
    # Add trim offsets
    CL = CL_base + coeffs['trim']['CL0']
    CD = CD_base + coeffs['trim']['CD0']
    Cm = Cm_base + coeffs['trim']['Cm0']
    
    # Add control surface effects
    CL += control['delta_effectiveness']['CL_delta_e'] * delta_e_rad
    Cm += control['delta_effectiveness']['Cm_delta_e'] * delta_e_rad
    
    return {'CL': CL, 'CD': CD, 'Cm': Cm}


def test_bilinear_interpolation():
    """Test bilinear interpolation with known values."""
    # Create simple test grid
    x_vals = [0.0, 1.0, 2.0]
    y_vals = [0.0, 1.0, 2.0]
    data = np.array([
        [0.0, 1.0, 2.0],
        [1.0, 2.0, 3.0],
        [2.0, 3.0, 4.0]
    ])
    
    # Test exact grid points
    assert bilinear_interp(0.0, 0.0, x_vals, y_vals, data) == 0.0
    assert bilinear_interp(1.0, 1.0, x_vals, y_vals, data) == 2.0
    assert bilinear_interp(2.0, 2.0, x_vals, y_vals, data) == 4.0
    
    # Test midpoint interpolation
    result = bilinear_interp(0.5, 0.5, x_vals, y_vals, data)
    expected = 1.0  # Average of 0, 1, 1, 2
    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"
    
    print("✓ Bilinear interpolation test passed")


def test_validation_case():
    """Test against validation case from VALIDATION/cases.yaml"""
    cases_path = Path(__file__).parent.parent / 'VALIDATION' / 'cases.yaml'
    
    with open(cases_path, 'r') as f:
        cases = yaml.safe_load(f)
    
    # Test first validation case
    case = cases[0]
    result = compute_aero_coeffs(
        alpha_deg=case['alpha_deg'],
        mach=case['mach'],
        delta_e_rad=case['deltas_rad']['e']
    )
    
    # Check against expected values with tolerance
    for key in ['CL', 'CD', 'Cm']:
        expected = case['expected'][key]['value']
        atol = case['expected'][key]['atol']
        actual = result[key]
        
        assert abs(actual - expected) <= atol, \
            f"{key}: expected {expected} ± {atol}, got {actual}"
    
    print(f"✓ Validation case '{case['name']}' passed")
    print(f"  CL={result['CL']:.4f}, CD={result['CD']:.4f}, Cm={result['Cm']:.4f}")


def test_golden_data():
    """Test against golden input/output data."""
    test_dir = Path(__file__).parent
    
    # Check if golden files exist
    if not (test_dir / 'golden_inputs.npz').exists():
        print("⚠ Golden data files not found, skipping test")
        return
    
    # Load golden data
    inputs = np.load(test_dir / 'golden_inputs.npz')
    outputs = np.load(test_dir / 'golden_outputs.npz')
    
    # Test each case
    n_cases = len(inputs['alpha_deg'])
    for i in range(n_cases):
        result = compute_aero_coeffs(
            alpha_deg=inputs['alpha_deg'][i],
            mach=inputs['mach'][i],
            delta_e_rad=inputs['delta_e_rad'][i]
        )
        
        # Check with small tolerance
        assert abs(result['CL'] - outputs['CL'][i]) < 1e-4
        assert abs(result['CD'] - outputs['CD'][i]) < 1e-4
        assert abs(result['Cm'] - outputs['Cm'][i]) < 1e-4
    
    print(f"✓ Golden data test passed ({n_cases} cases)")


def test_table_loading():
    """Test that CSV tables can be loaded correctly."""
    params_path = Path(__file__).parent.parent / 'PARAMS' / 'tables'
    
    # Load CL table
    alpha_vals, mach_vals, data = load_csv_table(params_path / 'CL_alpha_mach.csv')
    
    # Check dimensions
    assert len(alpha_vals) == 6, f"Expected 6 alpha values, got {len(alpha_vals)}"
    assert len(mach_vals) == 5, f"Expected 5 Mach values, got {len(mach_vals)}"
    assert data.shape == (6, 5), f"Expected shape (6, 5), got {data.shape}"
    
    # Check some known values
    assert alpha_vals[0] == -10.0
    assert alpha_vals[-1] == 15.0
    assert mach_vals[0] == 0.0
    assert mach_vals[-1] == 0.8
    
    print("✓ Table loading test passed")


if __name__ == '__main__':
    print("Running aerodynamic interpolation tests...\n")
    
    test_table_loading()
    test_bilinear_interpolation()
    test_validation_case()
    test_golden_data()
    
    print("\n✅ All tests passed!")
