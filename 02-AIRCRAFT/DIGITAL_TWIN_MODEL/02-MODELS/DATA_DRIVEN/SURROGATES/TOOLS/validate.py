#!/usr/bin/env python3
"""
validate.py - Validate surrogate model against contract, ranges, and metrics.

This script performs comprehensive validation:
1. I/O contract compliance (input/output dimensions, types, units)
2. Domain of validity checks (input ranges, combined constraints)
3. Performance metrics verification (RMSE, MAE, R2 against targets)
4. Monotonicity and physics constraints (if specified)
5. Golden test set validation (regression tests)

Usage:
    python validate.py --model-dir ../aero_wing_cl_cd/1.0.0/ --test-data test_data.npz

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple

import numpy as np
import yaml

try:
    import joblib
except ImportError:
    joblib = None

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass


def load_io_contract(contract_path: Path) -> Dict[str, Any]:
    """Load I/O contract from YAML file."""
    logger.info(f"Loading I/O contract from {contract_path}")
    with open(contract_path, 'r') as f:
        contract = yaml.safe_load(f)
    return contract


def load_domain_validity(domain_path: Path) -> Dict[str, Any]:
    """Load domain of validity specification."""
    logger.info(f"Loading domain of validity from {domain_path}")
    with open(domain_path, 'r') as f:
        domain = yaml.safe_load(f)
    return domain


def load_model(model_dir: Path) -> Tuple[Any, Any, Any]:
    """Load trained model and scalers."""
    model_file = model_dir / 'model.joblib'
    logger.info(f"Loading model from {model_file}")
    model = joblib.load(model_file)
    
    # Load scalers if they exist
    scaler_X_file = model_dir / 'scaler_X.joblib'
    scaler_y_file = model_dir / 'scaler_y.joblib'
    
    scaler_X = joblib.load(scaler_X_file) if scaler_X_file.exists() else None
    scaler_y = joblib.load(scaler_y_file) if scaler_y_file.exists() else None
    
    return model, scaler_X, scaler_y


def validate_io_contract(model: Any, contract: Dict[str, Any]) -> List[str]:
    """
    Validate that model complies with I/O contract.
    
    Returns:
        List of validation errors (empty if all pass)
    """
    logger.info("Validating I/O contract...")
    errors = []
    
    # Check input dimensions
    expected_n_inputs = len(contract.get('inputs', []))
    
    # Try to infer actual input dimensions from model
    # This is model-specific, here we assume sklearn-like models
    if hasattr(model, 'n_features_in_'):
        actual_n_inputs = model.n_features_in_
        if actual_n_inputs != expected_n_inputs:
            errors.append(f"Input dimension mismatch: expected {expected_n_inputs}, got {actual_n_inputs}")
    
    # Check output dimensions (would need test prediction)
    # TODO: Implement output dimension check
    
    # Check units and types (metadata check)
    for inp in contract.get('inputs', []):
        if 'name' not in inp:
            errors.append(f"Input missing 'name' field")
        if 'unit' not in inp:
            errors.append(f"Input '{inp.get('name', 'unknown')}' missing 'unit' field")
    
    for out in contract.get('outputs', []):
        if 'name' not in out:
            errors.append(f"Output missing 'name' field")
        if 'unit' not in out:
            errors.append(f"Output '{out.get('name', 'unknown')}' missing 'unit' field")
    
    if errors:
        logger.error(f"I/O contract validation failed with {len(errors)} error(s)")
        for error in errors:
            logger.error(f"  - {error}")
    else:
        logger.info("✓ I/O contract validation passed")
    
    return errors


def validate_domain_of_validity(X_test: np.ndarray, domain: Dict[str, Any]) -> List[str]:
    """
    Validate that test data falls within domain of validity.
    
    Returns:
        List of validation errors (empty if all pass)
    """
    logger.info("Validating domain of validity...")
    errors = []
    
    input_bounds = domain.get('domain_of_validity', {}).get('input_bounds', {})
    
    if not input_bounds:
        logger.warning("No input bounds specified in domain of validity")
        return errors
    
    # Check each input against its bounds
    for i, (input_name, bounds) in enumerate(input_bounds.items()):
        if i >= X_test.shape[1]:
            errors.append(f"Input '{input_name}' index {i} exceeds test data dimensions")
            continue
        
        X_col = X_test[:, i]
        min_bound, max_bound = bounds
        
        below_min = np.sum(X_col < min_bound)
        above_max = np.sum(X_col > max_bound)
        
        if below_min > 0:
            errors.append(f"Input '{input_name}': {below_min} samples below min bound {min_bound}")
        if above_max > 0:
            errors.append(f"Input '{input_name}': {above_max} samples above max bound {max_bound}")
    
    if errors:
        logger.error(f"Domain of validity validation failed with {len(errors)} error(s)")
        for error in errors:
            logger.error(f"  - {error}")
    else:
        logger.info("✓ Domain of validity validation passed")
    
    return errors


def validate_metrics(metrics: Dict[str, float], targets: Dict[str, float]) -> List[str]:
    """
    Validate that performance metrics meet targets.
    
    Returns:
        List of validation errors (empty if all pass)
    """
    logger.info("Validating performance metrics...")
    errors = []
    
    for metric_name, target_value in targets.items():
        if metric_name not in metrics:
            errors.append(f"Metric '{metric_name}' not found in results")
            continue
        
        actual_value = metrics[metric_name]
        
        # Determine pass/fail based on metric type
        # For error metrics (RMSE, MAE, max_error), lower is better
        # For score metrics (R2), higher is better
        if metric_name.lower() in ['rmse', 'mae', 'max_error', 'mse']:
            if actual_value > target_value:
                errors.append(f"Metric '{metric_name}': {actual_value:.6f} exceeds target {target_value:.6f}")
        elif metric_name.lower() in ['r2', 'r2_score', 'accuracy']:
            if actual_value < target_value:
                errors.append(f"Metric '{metric_name}': {actual_value:.6f} below target {target_value:.6f}")
        else:
            logger.warning(f"Unknown metric type '{metric_name}', skipping validation")
    
    if errors:
        logger.error(f"Metrics validation failed with {len(errors)} error(s)")
        for error in errors:
            logger.error(f"  - {error}")
    else:
        logger.info("✓ Metrics validation passed")
    
    return errors


def validate_monotonicity(model: Any, X_test: np.ndarray, constraints_file: Path) -> List[str]:
    """
    Validate monotonicity and physics constraints.
    
    Returns:
        List of validation errors (empty if all pass)
    """
    logger.info("Validating monotonicity constraints...")
    
    if not constraints_file.exists():
        logger.info("No monotonicity constraints file found, skipping")
        return []
    
    with open(constraints_file, 'r') as f:
        constraints = yaml.safe_load(f)
    
    errors = []
    
    # TODO: Implement monotonicity checking logic
    # This would involve:
    # 1. For each constraint, vary one input while holding others constant
    # 2. Check that output changes in expected direction
    # 3. Report violations
    
    logger.info("✓ Monotonicity validation (not implemented in this example)")
    
    return errors


def validate_golden_tests(model: Any, scaler_X: Any, scaler_y: Any, golden_file: Path) -> List[str]:
    """
    Validate against golden test set (regression tests).
    
    Returns:
        List of validation errors (empty if all pass)
    """
    logger.info("Validating against golden test set...")
    
    if not golden_file.exists():
        logger.warning(f"Golden test file not found: {golden_file}")
        return []
    
    golden_data = np.load(golden_file)
    X_golden = golden_data['X']
    y_golden_expected = golden_data['y']
    
    errors = []
    
    # Make predictions
    X_golden_scaled = scaler_X.transform(X_golden) if scaler_X is not None else X_golden
    y_golden_pred = model.predict(X_golden_scaled)
    
    if scaler_y is not None:
        y_golden_pred = scaler_y.inverse_transform(y_golden_pred.reshape(-1, 1)).ravel()
    
    # Check if predictions match expected values within tolerance
    tolerance = 1e-6  # Tight tolerance for regression tests
    
    max_diff = np.max(np.abs(y_golden_pred - y_golden_expected))
    
    if max_diff > tolerance:
        errors.append(f"Golden test failed: max difference {max_diff:.2e} exceeds tolerance {tolerance:.2e}")
        logger.error(f"  Max difference: {max_diff:.2e}")
        logger.error(f"  Sample predictions: {y_golden_pred[:5]}")
        logger.error(f"  Sample expected: {y_golden_expected[:5]}")
    else:
        logger.info(f"✓ Golden test validation passed (max diff: {max_diff:.2e})")
    
    return errors


def generate_validation_report(validation_results: Dict[str, Any], output_dir: Path) -> None:
    """Generate validation report."""
    report_file = output_dir / 'validation' / 'validation_report.json'
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(validation_results, f, indent=2)
    
    logger.info(f"Validation report saved to {report_file}")


def main():
    """Main validation pipeline."""
    parser = argparse.ArgumentParser(description='Validate surrogate model')
    parser.add_argument('--model-dir', type=Path, required=True, help='Path to model directory')
    parser.add_argument('--test-data', type=Path, help='Path to test data (X_test, y_test)')
    parser.add_argument('--io-contract', type=Path, help='Path to io_contract.yaml (default: model-dir/io_contract.yaml)')
    parser.add_argument('--domain-validity', type=Path, help='Path to domain_of_validity.yaml')
    parser.add_argument('--strict', action='store_true', help='Exit with error code if any validation fails')
    
    args = parser.parse_args()
    
    logger.info("=" * 80)
    logger.info("SURROGATE MODEL VALIDATION")
    logger.info("=" * 80)
    
    # Set default paths
    if args.io_contract is None:
        args.io_contract = args.model_dir / 'io_contract.yaml'
    if args.domain_validity is None:
        args.domain_validity = args.model_dir / 'domain_of_validity.yaml'
    
    # Load model
    model, scaler_X, scaler_y = load_model(args.model_dir)
    
    # Load contracts and specifications
    contract = load_io_contract(args.io_contract) if args.io_contract.exists() else {}
    domain = load_domain_validity(args.domain_validity) if args.domain_validity.exists() else {}
    
    # Collect all validation errors
    all_errors = []
    validation_results = {
        'timestamp': np.datetime64('now').astype(str),
        'model_dir': str(args.model_dir),
        'validations': {}
    }
    
    # 1. Validate I/O contract
    io_errors = validate_io_contract(model, contract)
    all_errors.extend(io_errors)
    validation_results['validations']['io_contract'] = {
        'passed': len(io_errors) == 0,
        'errors': io_errors
    }
    
    # 2. Validate domain of validity (requires test data)
    if args.test_data and args.test_data.exists():
        test_data = np.load(args.test_data)
        X_test = test_data['X']
        y_test = test_data['y']
        
        domain_errors = validate_domain_of_validity(X_test, domain)
        all_errors.extend(domain_errors)
        validation_results['validations']['domain_of_validity'] = {
            'passed': len(domain_errors) == 0,
            'errors': domain_errors
        }
        
        # 3. Validate metrics (requires test data)
        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
        
        X_test_scaled = scaler_X.transform(X_test) if scaler_X is not None else X_test
        y_pred = model.predict(X_test_scaled)
        
        if scaler_y is not None:
            y_pred = scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()
        
        metrics = {
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
            'mae': mean_absolute_error(y_test, y_pred),
            'r2': r2_score(y_test, y_pred)
        }
        
        # Define targets (could be from contract or config)
        targets = contract.get('performance', {}).get('accuracy', {})
        if 'target_value' in targets:
            metric_targets = {'rmse': targets['target_value']}
            metric_errors = validate_metrics(metrics, metric_targets)
            all_errors.extend(metric_errors)
            validation_results['validations']['metrics'] = {
                'passed': len(metric_errors) == 0,
                'errors': metric_errors,
                'values': metrics
            }
    else:
        logger.warning("No test data provided, skipping domain and metrics validation")
    
    # 4. Validate monotonicity constraints
    constraints_file = args.model_dir / 'tests' / 'monotonicity.yaml'
    if constraints_file.exists() and args.test_data and args.test_data.exists():
        monotonicity_errors = validate_monotonicity(model, X_test, constraints_file)
        all_errors.extend(monotonicity_errors)
        validation_results['validations']['monotonicity'] = {
            'passed': len(monotonicity_errors) == 0,
            'errors': monotonicity_errors
        }
    
    # 5. Validate golden tests
    golden_file = args.model_dir / 'tests' / 'golden.npz'
    if golden_file.exists():
        golden_errors = validate_golden_tests(model, scaler_X, scaler_y, golden_file)
        all_errors.extend(golden_errors)
        validation_results['validations']['golden_tests'] = {
            'passed': len(golden_errors) == 0,
            'errors': golden_errors
        }
    
    # Generate validation report
    validation_results['overall_passed'] = len(all_errors) == 0
    validation_results['total_errors'] = len(all_errors)
    generate_validation_report(validation_results, args.model_dir)
    
    # Summary
    logger.info("=" * 80)
    if len(all_errors) == 0:
        logger.info("✓ ALL VALIDATIONS PASSED")
        logger.info("=" * 80)
        return 0
    else:
        logger.error(f"✗ VALIDATION FAILED: {len(all_errors)} error(s)")
        logger.info("=" * 80)
        return 1 if args.strict else 0


if __name__ == '__main__':
    sys.exit(main())
