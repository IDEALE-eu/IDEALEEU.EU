"""
evaluate.py - Stable prediction API for thermal_avionics_temp surrogate model

This module provides a simple, stable API for making predictions with the
trained surrogate model.

Usage:
    from runtime.python.evaluate import predict
    
    result = predict({
        'T_ambient': 35.0,
        'P_load': 65.0,
        'airflow': 3.5
    })
    
    print(result['T_component'])  # Predicted temperature
    print(result['uncertainty_95'])  # 95% confidence interval

Author: Thermal Analysis Team
Version: 1.0.0
"""

from pathlib import Path
from typing import Dict, Any
import warnings

try:
    import numpy as np
    import joblib
except ImportError as e:
    raise ImportError(f"Required package not available: {e}. "
                     "Install with: pip install numpy joblib scikit-learn")


# Model paths (relative to this file)
MODEL_DIR = Path(__file__).parent.parent.parent
MODEL_FILE = MODEL_DIR / 'model.joblib'
SCALER_X_FILE = MODEL_DIR / 'scaler_X.joblib'
SCALER_Y_FILE = MODEL_DIR / 'scaler_y.joblib'

# Load model and scalers once at module import
_model = None
_scaler_X = None
_scaler_y = None

def _load_model():
    """Load model and scalers (called once on first prediction)."""
    global _model, _scaler_X, _scaler_y
    
    if _model is not None:
        return  # Already loaded
    
    if not MODEL_FILE.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_FILE}")
    
    _model = joblib.load(MODEL_FILE)
    
    if SCALER_X_FILE.exists():
        _scaler_X = joblib.load(SCALER_X_FILE)
    
    if SCALER_Y_FILE.exists():
        _scaler_y = joblib.load(SCALER_Y_FILE)


def predict(inputs: Dict[str, float], return_std: bool = True) -> Dict[str, Any]:
    """
    Predict component temperature from inputs.
    
    Args:
        inputs: Dictionary with keys 'T_ambient', 'P_load', 'airflow'
        return_std: Whether to return uncertainty estimate (default: True)
    
    Returns:
        Dictionary with predicted 'T_component' and optionally 'uncertainty_95'
    
    Raises:
        ValueError: If inputs are invalid or out of domain
    """
    # Load model if not already loaded
    _load_model()
    
    # Expected input names (in order)
    input_names = ['T_ambient', 'P_load', 'airflow']
    
    # Validate inputs
    for name in input_names:
        if name not in inputs:
            raise ValueError(f"Missing required input: {name}")
    
    # Check domain of validity (with warnings)
    _check_domain_validity(inputs)
    
    # Prepare input array
    X_input = np.array([[inputs[name] for name in input_names]])
    
    # Scale inputs
    if _scaler_X is not None:
        X_scaled = _scaler_X.transform(X_input)
    else:
        X_scaled = X_input
    
    # Predict
    if return_std and hasattr(_model, 'predict'):
        # For GP models, get uncertainty
        try:
            y_pred, y_std = _model.predict(X_scaled, return_std=True)
        except TypeError:
            # Model doesn't support return_std
            y_pred = _model.predict(X_scaled)
            y_std = None
    else:
        y_pred = _model.predict(X_scaled)
        y_std = None
    
    # Inverse transform output
    if _scaler_y is not None:
        y_pred = _scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()
        if y_std is not None:
            # Scale std (assuming standardization)
            y_std = y_std * _scaler_y.scale_[0]
    
    # Build result
    result = {
        'T_component': float(y_pred[0])
    }
    
    if y_std is not None:
        # 95% confidence interval (1.96 * std for normal distribution)
        result['uncertainty_95'] = float(1.96 * y_std[0])
        result['std'] = float(y_std[0])
    
    return result


def _check_domain_validity(inputs: Dict[str, float]) -> None:
    """
    Check if inputs are within domain of validity.
    
    Raises warnings for out-of-domain inputs.
    """
    # Define valid ranges (from domain_of_validity.yaml)
    ranges = {
        'T_ambient': (-20.0, 70.0),
        'P_load': (5.0, 120.0),
        'airflow': (0.5, 8.0)
    }
    
    for name, (min_val, max_val) in ranges.items():
        value = inputs[name]
        
        # Check hard limits
        if value < min_val or value > max_val:
            warnings.warn(
                f"Input '{name}' = {value} is outside valid range [{min_val}, {max_val}]. "
                f"Prediction may be inaccurate.",
                UserWarning
            )
        
        # Check warning margin (5%)
        margin = 0.05 * (max_val - min_val)
        if value < min_val + margin or value > max_val - margin:
            warnings.warn(
                f"Input '{name}' = {value} is near domain boundary. "
                f"Recommended range: [{min_val + margin:.1f}, {max_val - margin:.1f}]",
                UserWarning
            )


def predict_batch(inputs_batch: np.ndarray, return_std: bool = True) -> Dict[str, np.ndarray]:
    """
    Predict for batch of inputs.
    
    Args:
        inputs_batch: Array of shape (n_samples, 3) with columns [T_ambient, P_load, airflow]
        return_std: Whether to return uncertainty estimates
    
    Returns:
        Dictionary with 'T_component' array and optionally 'uncertainty_95' array
    """
    # Load model if not already loaded
    _load_model()
    
    # Scale inputs
    if _scaler_X is not None:
        X_scaled = _scaler_X.transform(inputs_batch)
    else:
        X_scaled = inputs_batch
    
    # Predict
    if return_std and hasattr(_model, 'predict'):
        try:
            y_pred, y_std = _model.predict(X_scaled, return_std=True)
        except TypeError:
            y_pred = _model.predict(X_scaled)
            y_std = None
    else:
        y_pred = _model.predict(X_scaled)
        y_std = None
    
    # Inverse transform output
    if _scaler_y is not None:
        y_pred = _scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()
        if y_std is not None:
            y_std = y_std * _scaler_y.scale_[0]
    
    # Build result
    result = {
        'T_component': y_pred
    }
    
    if y_std is not None:
        result['uncertainty_95'] = 1.96 * y_std
        result['std'] = y_std
    
    return result


if __name__ == '__main__':
    # Example usage
    print("Thermal Avionics Temperature Surrogate - Example Usage")
    print("=" * 60)
    
    # Example inputs
    test_inputs = {
        'T_ambient': 35.0,  # °C
        'P_load': 65.0,     # W
        'airflow': 3.5      # m³/min
    }
    
    print(f"\nInput:")
    for key, value in test_inputs.items():
        print(f"  {key}: {value}")
    
    # Make prediction
    try:
        result = predict(test_inputs)
        
        print(f"\nOutput:")
        print(f"  T_component: {result['T_component']:.2f} °C")
        if 'uncertainty_95' in result:
            print(f"  Uncertainty (95% CI): ±{result['uncertainty_95']:.2f} °C")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nNote: Model files not found. This is expected in the example structure.")
        print("      In production, model.joblib and scalers would be present.")
