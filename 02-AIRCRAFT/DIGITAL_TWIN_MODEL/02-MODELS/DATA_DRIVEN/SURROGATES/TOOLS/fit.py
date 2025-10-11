#!/usr/bin/env python3
"""
fit.py - Train surrogate models from DOE data or high-fidelity simulation results.

This script handles the complete training pipeline:
1. Load training and validation data
2. Preprocess and scale data
3. Train surrogate model (GP, RBF, PCE, XGB, MLP, etc.)
4. Validate performance
5. Save trained model and metadata

Usage:
    python fit.py --config train_config.yaml --output-dir ../aero_wing_cl_cd/1.0.0/

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import hashlib
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Tuple

import numpy as np
import yaml

# Optional imports (add as needed)
try:
    import joblib
except ImportError:
    joblib = None

try:
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, Matern, ConstantKernel as C
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
except ImportError:
    print("Warning: scikit-learn not available. Install with: pip install scikit-learn")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_config(config_path: Path) -> Dict[str, Any]:
    """Load training configuration from YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def load_data(data_path: Path, format: str = 'npz') -> np.ndarray:
    """Load training/validation data from file."""
    logger.info(f"Loading data from {data_path} (format: {format})")
    
    if format == 'npz':
        data = np.load(data_path)
        # Assume npz contains 'data' key or return first array
        if 'data' in data:
            return data['data']
        else:
            # Return first array in npz file
            return data[data.files[0]]
    elif format == 'csv':
        return np.loadtxt(data_path, delimiter=',')
    else:
        raise ValueError(f"Unsupported data format: {format}")


def compute_data_hash(data: np.ndarray) -> str:
    """Compute SHA-256 hash of data for integrity checking."""
    data_bytes = data.tobytes()
    hash_obj = hashlib.sha256(data_bytes)
    return hash_obj.hexdigest()


def preprocess_data(X: np.ndarray, y: np.ndarray, config: Dict[str, Any]) -> Tuple[np.ndarray, np.ndarray, Any, Any]:
    """
    Preprocess training data according to config.
    
    Returns:
        X_scaled, y_scaled, scaler_X, scaler_y
    """
    logger.info("Preprocessing data...")
    
    preprocessing_config = config.get('data', {}).get('preprocessing', {})
    
    # Handle outliers if configured
    if preprocessing_config.get('outlier_removal', {}).get('enabled', False):
        logger.info("Outlier removal is configured but not implemented in this example")
        # TODO: Implement outlier removal
    
    # Scaling
    scaler_X = None
    scaler_y = None
    
    if preprocessing_config.get('scaling', False):
        from sklearn.preprocessing import StandardScaler
        scaler_X = StandardScaler()
        scaler_y = StandardScaler()
        
        X_scaled = scaler_X.fit_transform(X)
        y_scaled = scaler_y.fit_transform(y.reshape(-1, 1) if y.ndim == 1 else y)
        
        logger.info(f"Data scaled: X {X.shape} -> {X_scaled.shape}, y {y.shape} -> {y_scaled.shape}")
    else:
        X_scaled = X
        y_scaled = y
    
    return X_scaled, y_scaled, scaler_X, scaler_y


def train_model(X_train: np.ndarray, y_train: np.ndarray, config: Dict[str, Any]) -> Any:
    """
    Train surrogate model based on algorithm specified in config.
    
    Returns:
        Trained model
    """
    algorithm_config = config.get('algorithm', {})
    algo_type = algorithm_config.get('type', 'gaussian_process')
    
    logger.info(f"Training model: {algo_type}")
    
    if algo_type == 'gaussian_process':
        return train_gaussian_process(X_train, y_train, algorithm_config)
    elif algo_type == 'random_forest':
        logger.warning("Random Forest training not implemented in this example")
        raise NotImplementedError("Random Forest not implemented")
    elif algo_type == 'xgboost':
        logger.warning("XGBoost training not implemented in this example")
        raise NotImplementedError("XGBoost not implemented")
    elif algo_type == 'neural_network':
        logger.warning("Neural Network training not implemented in this example")
        raise NotImplementedError("Neural Network not implemented")
    else:
        raise ValueError(f"Unsupported algorithm type: {algo_type}")


def train_gaussian_process(X_train: np.ndarray, y_train: np.ndarray, config: Dict[str, Any]) -> Any:
    """Train Gaussian Process Regression model."""
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
    
    # Get hyperparameters from config
    kernel_type = config.get('hyperparameters', {}).get('kernel', 'RBF')
    length_scale = config.get('hyperparameters', {}).get('length_scale', 1.0)
    
    # Create kernel
    if kernel_type == 'RBF':
        kernel = C(1.0, (1e-3, 1e3)) * RBF(length_scale=length_scale, length_scale_bounds=(1e-2, 1e2))
    else:
        kernel = RBF(length_scale=length_scale)
    
    # Create and train GP
    gp = GaussianProcessRegressor(
        kernel=kernel,
        n_restarts_optimizer=config.get('hyperparameters', {}).get('n_restarts_optimizer', 10),
        alpha=config.get('hyperparameters', {}).get('noise_level', 1e-6),
        random_state=config.get('training', {}).get('random_seed', 42)
    )
    
    logger.info("Fitting Gaussian Process...")
    gp.fit(X_train, y_train.ravel() if y_train.ndim > 1 and y_train.shape[1] == 1 else y_train)
    logger.info(f"GP trained. Kernel: {gp.kernel_}")
    
    return gp


def evaluate_model(model: Any, X_test: np.ndarray, y_test: np.ndarray, config: Dict[str, Any]) -> Dict[str, float]:
    """
    Evaluate model performance on test data.
    
    Returns:
        Dictionary of metrics
    """
    logger.info("Evaluating model...")
    
    y_pred = model.predict(X_test)
    
    # Ensure shapes are compatible
    if y_pred.ndim == 1:
        y_pred = y_pred.reshape(-1, 1)
    if y_test.ndim == 1:
        y_test = y_test.reshape(-1, 1)
    
    metrics = {}
    metrics['rmse'] = np.sqrt(mean_squared_error(y_test, y_pred))
    metrics['mae'] = mean_absolute_error(y_test, y_pred)
    metrics['r2'] = r2_score(y_test, y_pred)
    metrics['max_error'] = np.max(np.abs(y_test - y_pred))
    
    # Compute percentile errors
    errors = np.abs(y_test - y_pred).flatten()
    metrics['p50_error'] = np.percentile(errors, 50)
    metrics['p95_error'] = np.percentile(errors, 95)
    metrics['p99_error'] = np.percentile(errors, 99)
    
    logger.info(f"Metrics: RMSE={metrics['rmse']:.6f}, MAE={metrics['mae']:.6f}, R2={metrics['r2']:.6f}")
    
    return metrics


def save_model(model: Any, scaler_X: Any, scaler_y: Any, output_dir: Path, config: Dict[str, Any]) -> None:
    """Save trained model and scalers."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    model_file = output_dir / 'model.joblib'
    logger.info(f"Saving model to {model_file}")
    joblib.dump(model, model_file)
    
    if scaler_X is not None:
        scaler_X_file = output_dir / 'scaler_X.joblib'
        logger.info(f"Saving X scaler to {scaler_X_file}")
        joblib.dump(scaler_X, scaler_X_file)
    
    if scaler_y is not None:
        scaler_y_file = output_dir / 'scaler_y.joblib'
        logger.info(f"Saving y scaler to {scaler_y_file}")
        joblib.dump(scaler_y, scaler_y_file)


def save_training_data(X_train: np.ndarray, y_train: np.ndarray, X_val: np.ndarray, y_val: np.ndarray, 
                       output_dir: Path) -> None:
    """Save training and validation data with hashes."""
    training_dir = output_dir / 'training'
    validation_dir = output_dir / 'validation'
    
    training_dir.mkdir(parents=True, exist_ok=True)
    validation_dir.mkdir(parents=True, exist_ok=True)
    
    # Save training data
    np.savez_compressed(training_dir / 'X_train.npz', data=X_train)
    np.savez_compressed(training_dir / 'y_train.npz', data=y_train)
    
    # Compute and save hash
    data_hash = compute_data_hash(np.concatenate([X_train.flatten(), y_train.flatten()]))
    with open(training_dir / 'data_hash.sha256', 'w') as f:
        f.write(data_hash)
    
    logger.info(f"Training data saved to {training_dir}")
    
    # Save validation data
    np.savez_compressed(validation_dir / 'X_val.npz', data=X_val)
    np.savez_compressed(validation_dir / 'y_val.npz', data=y_val)
    
    logger.info(f"Validation data saved to {validation_dir}")


def save_metrics(metrics: Dict[str, float], output_dir: Path) -> None:
    """Save evaluation metrics to JSON."""
    validation_dir = output_dir / 'validation'
    validation_dir.mkdir(parents=True, exist_ok=True)
    
    metrics_file = validation_dir / 'metrics.json'
    
    # Add timestamp
    metrics['timestamp'] = datetime.now().isoformat()
    
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    logger.info(f"Metrics saved to {metrics_file}")


def main():
    """Main training pipeline."""
    parser = argparse.ArgumentParser(description='Train surrogate model from DOE data')
    parser.add_argument('--config', type=Path, required=True, help='Path to train_config.yaml')
    parser.add_argument('--output-dir', type=Path, required=True, help='Output directory for trained model')
    parser.add_argument('--X-train', type=Path, help='Path to training inputs (if not in config)')
    parser.add_argument('--y-train', type=Path, help='Path to training outputs (if not in config)')
    parser.add_argument('--X-val', type=Path, help='Path to validation inputs (if not in config)')
    parser.add_argument('--y-val', type=Path, help='Path to validation outputs (if not in config)')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Load data (simplified - in practice would use paths from config)
    logger.info("=" * 80)
    logger.info("SURROGATE MODEL TRAINING")
    logger.info("=" * 80)
    
    # TODO: Load actual data from paths specified in config or args
    # For now, generate synthetic data for demonstration
    logger.warning("Using synthetic data for demonstration. Replace with actual data loading.")
    
    np.random.seed(config.get('training', {}).get('random_seed', 42))
    
    # Generate synthetic data
    n_train = 100
    n_val = 30
    n_features = 2
    
    X_train = np.random.rand(n_train, n_features) * 10
    y_train = np.sin(X_train[:, 0]) * np.cos(X_train[:, 1]) + np.random.randn(n_train) * 0.1
    
    X_val = np.random.rand(n_val, n_features) * 10
    y_val = np.sin(X_val[:, 0]) * np.cos(X_val[:, 1]) + np.random.randn(n_val) * 0.1
    
    logger.info(f"Training data: X_train={X_train.shape}, y_train={y_train.shape}")
    logger.info(f"Validation data: X_val={X_val.shape}, y_val={y_val.shape}")
    
    # Preprocess data
    X_train_scaled, y_train_scaled, scaler_X, scaler_y = preprocess_data(X_train, y_train, config)
    X_val_scaled, y_val_scaled, _, _ = preprocess_data(X_val, y_val, config)
    
    # Train model
    model = train_model(X_train_scaled, y_train_scaled, config)
    
    # Evaluate model
    metrics_train = evaluate_model(model, X_train_scaled, y_train_scaled, config)
    metrics_val = evaluate_model(model, X_val_scaled, y_val_scaled, config)
    
    logger.info("Training metrics:")
    for key, value in metrics_train.items():
        logger.info(f"  {key}: {value:.6f}")
    
    logger.info("Validation metrics:")
    for key, value in metrics_val.items():
        logger.info(f"  {key}: {value:.6f}")
    
    # Save model
    save_model(model, scaler_X, scaler_y, args.output_dir, config)
    
    # Save training data
    save_training_data(X_train, y_train, X_val, y_val, args.output_dir)
    
    # Save metrics
    metrics_combined = {
        'training': metrics_train,
        'validation': metrics_val
    }
    save_metrics(metrics_combined, args.output_dir)
    
    logger.info("=" * 80)
    logger.info("TRAINING COMPLETE")
    logger.info("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
