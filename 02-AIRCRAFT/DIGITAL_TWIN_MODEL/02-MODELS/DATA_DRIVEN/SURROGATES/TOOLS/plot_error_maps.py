#!/usr/bin/env python3
"""
plot_error_maps.py - Generate residual and error maps for surrogate models.

This script creates visualizations to diagnose model performance:
1. Parity plots (predicted vs. actual)
2. Residual plots (error vs. predicted)
3. Error heat maps (error across input space)
4. Slice-based error analysis
5. Uncertainty calibration plots

Usage:
    python plot_error_maps.py --model-dir ../aero_wing_cl_cd/1.0.0/ --test-data test_data.npz

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Tuple, Optional

import numpy as np

try:
    import joblib
except ImportError:
    joblib = None

try:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
except ImportError:
    plt = None
    logger = logging.getLogger(__name__)
    logger.warning("matplotlib not available, plotting disabled")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_model(model_dir: Path) -> Tuple:
    """Load trained model and scalers."""
    model_file = model_dir / 'model.joblib'
    logger.info(f"Loading model from {model_file}")
    model = joblib.load(model_file)
    
    scaler_X_file = model_dir / 'scaler_X.joblib'
    scaler_y_file = model_dir / 'scaler_y.joblib'
    
    scaler_X = joblib.load(scaler_X_file) if scaler_X_file.exists() else None
    scaler_y = joblib.load(scaler_y_file) if scaler_y_file.exists() else None
    
    return model, scaler_X, scaler_y


def load_test_data(test_data_path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """Load test data."""
    logger.info(f"Loading test data from {test_data_path}")
    data = np.load(test_data_path)
    X_test = data['X']
    y_test = data['y']
    return X_test, y_test


def predict_with_model(model, scaler_X, scaler_y, X_test: np.ndarray) -> np.ndarray:
    """Make predictions with model."""
    X_test_scaled = scaler_X.transform(X_test) if scaler_X is not None else X_test
    y_pred = model.predict(X_test_scaled)
    
    if scaler_y is not None:
        y_pred = scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()
    
    return y_pred


def plot_parity(y_test: np.ndarray, y_pred: np.ndarray, output_path: Path, 
                output_name: str = "output") -> None:
    """
    Create parity plot (predicted vs. actual).
    
    Args:
        y_test: Actual values
        y_pred: Predicted values
        output_path: Path to save plot
        output_name: Name of output variable
    """
    if plt is None:
        logger.warning("matplotlib not available, skipping parity plot")
        return
    
    logger.info("Generating parity plot...")
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Scatter plot
    ax.scatter(y_test, y_pred, alpha=0.5, s=20, edgecolors='none')
    
    # Perfect prediction line
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect prediction')
    
    # Error bands (±10%)
    margin = 0.1 * (max_val - min_val)
    ax.plot([min_val, max_val], [min_val + margin, max_val + margin], 'k:', linewidth=1, alpha=0.5)
    ax.plot([min_val, max_val], [min_val - margin, max_val - margin], 'k:', linewidth=1, alpha=0.5)
    
    ax.set_xlabel(f'Actual {output_name}', fontsize=12)
    ax.set_ylabel(f'Predicted {output_name}', fontsize=12)
    ax.set_title(f'Parity Plot: {output_name}', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    plt.savefig(output_path / 'parity_plot.png', dpi=150)
    plt.close()
    
    logger.info(f"  Saved: {output_path / 'parity_plot.png'}")


def plot_residuals(y_test: np.ndarray, y_pred: np.ndarray, output_path: Path,
                   output_name: str = "output") -> None:
    """
    Create residual plot (error vs. predicted value).
    
    Args:
        y_test: Actual values
        y_pred: Predicted values
        output_path: Path to save plot
        output_name: Name of output variable
    """
    if plt is None:
        logger.warning("matplotlib not available, skipping residual plot")
        return
    
    logger.info("Generating residual plot...")
    
    residuals = y_test - y_pred
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot of residuals
    ax.scatter(y_pred, residuals, alpha=0.5, s=20, edgecolors='none')
    
    # Zero line
    ax.axhline(y=0, color='r', linestyle='--', linewidth=2, label='Zero error')
    
    # Mean residual
    mean_residual = np.mean(residuals)
    ax.axhline(y=mean_residual, color='g', linestyle=':', linewidth=1, 
               label=f'Mean residual: {mean_residual:.4f}')
    
    # ±1 std bands
    std_residual = np.std(residuals)
    ax.axhline(y=mean_residual + std_residual, color='k', linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=mean_residual - std_residual, color='k', linestyle=':', linewidth=1, alpha=0.5)
    
    ax.set_xlabel(f'Predicted {output_name}', fontsize=12)
    ax.set_ylabel(f'Residual (Actual - Predicted)', fontsize=12)
    ax.set_title(f'Residual Plot: {output_name}', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path / 'residual_plot.png', dpi=150)
    plt.close()
    
    logger.info(f"  Saved: {output_path / 'residual_plot.png'}")


def plot_error_histogram(y_test: np.ndarray, y_pred: np.ndarray, output_path: Path,
                         output_name: str = "output") -> None:
    """
    Create histogram of absolute errors.
    
    Args:
        y_test: Actual values
        y_pred: Predicted values
        output_path: Path to save plot
        output_name: Name of output variable
    """
    if plt is None:
        logger.warning("matplotlib not available, skipping error histogram")
        return
    
    logger.info("Generating error histogram...")
    
    errors = np.abs(y_test - y_pred)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histogram
    n, bins, patches = ax.hist(errors, bins=50, edgecolor='black', alpha=0.7)
    
    # Statistics
    mean_error = np.mean(errors)
    median_error = np.median(errors)
    p95_error = np.percentile(errors, 95)
    
    # Add vertical lines for statistics
    ax.axvline(mean_error, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean_error:.4f}')
    ax.axvline(median_error, color='g', linestyle='--', linewidth=2, label=f'Median: {median_error:.4f}')
    ax.axvline(p95_error, color='orange', linestyle='--', linewidth=2, label=f'p95: {p95_error:.4f}')
    
    ax.set_xlabel(f'Absolute Error', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Error Distribution: {output_name}', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(output_path / 'error_histogram.png', dpi=150)
    plt.close()
    
    logger.info(f"  Saved: {output_path / 'error_histogram.png'}")


def plot_error_heatmap_2d(X_test: np.ndarray, y_test: np.ndarray, y_pred: np.ndarray, 
                          output_path: Path, input_names: Optional[list] = None) -> None:
    """
    Create 2D error heat map across input space (for 2D inputs).
    
    Args:
        X_test: Test inputs
        y_test: Actual outputs
        y_pred: Predicted outputs
        output_path: Path to save plot
        input_names: Names of input variables
    """
    if plt is None:
        logger.warning("matplotlib not available, skipping error heatmap")
        return
    
    if X_test.shape[1] != 2:
        logger.info(f"Error heatmap requires 2D input, got {X_test.shape[1]}D, skipping")
        return
    
    logger.info("Generating 2D error heatmap...")
    
    errors = np.abs(y_test - y_pred)
    
    if input_names is None:
        input_names = [f'Input {i+1}' for i in range(X_test.shape[1])]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create scatter plot with color representing error
    scatter = ax.scatter(X_test[:, 0], X_test[:, 1], c=errors, cmap='hot', 
                        s=50, alpha=0.6, edgecolors='none')
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Absolute Error', fontsize=12)
    
    ax.set_xlabel(input_names[0], fontsize=12)
    ax.set_ylabel(input_names[1], fontsize=12)
    ax.set_title('Error Heatmap Across Input Space', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path / 'error_heatmap_2d.png', dpi=150)
    plt.close()
    
    logger.info(f"  Saved: {output_path / 'error_heatmap_2d.png'}")


def generate_summary_plot(y_test: np.ndarray, y_pred: np.ndarray, output_path: Path,
                         output_name: str = "output") -> None:
    """
    Generate a summary plot with multiple subplots.
    
    Args:
        y_test: Actual values
        y_pred: Predicted values
        output_path: Path to save plot
        output_name: Name of output variable
    """
    if plt is None:
        logger.warning("matplotlib not available, skipping summary plot")
        return
    
    logger.info("Generating summary plot...")
    
    residuals = y_test - y_pred
    errors = np.abs(residuals)
    
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # 1. Parity plot
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.scatter(y_test, y_pred, alpha=0.5, s=20)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2)
    ax1.set_xlabel(f'Actual {output_name}')
    ax1.set_ylabel(f'Predicted {output_name}')
    ax1.set_title('Parity Plot')
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # 2. Residual plot
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.scatter(y_pred, residuals, alpha=0.5, s=20)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax2.set_xlabel(f'Predicted {output_name}')
    ax2.set_ylabel('Residual')
    ax2.set_title('Residual Plot')
    ax2.grid(True, alpha=0.3)
    
    # 3. Error histogram
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.hist(errors, bins=30, edgecolor='black', alpha=0.7)
    ax3.axvline(np.mean(errors), color='r', linestyle='--', linewidth=2, 
                label=f'Mean: {np.mean(errors):.4f}')
    ax3.set_xlabel('Absolute Error')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Error Distribution')
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')
    
    # 4. Residual histogram (normal distribution check)
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.hist(residuals, bins=30, edgecolor='black', alpha=0.7)
    ax4.axvline(0, color='r', linestyle='--', linewidth=2)
    ax4.set_xlabel('Residual')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Residual Distribution')
    ax4.grid(True, alpha=0.3, axis='y')
    
    # 5. Error vs. actual value
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.scatter(y_test, errors, alpha=0.5, s=20)
    ax5.set_xlabel(f'Actual {output_name}')
    ax5.set_ylabel('Absolute Error')
    ax5.set_title('Error vs. Actual Value')
    ax5.grid(True, alpha=0.3)
    
    # 6. Statistics summary (text)
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.axis('off')
    
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    max_error = np.max(errors)
    p95_error = np.percentile(errors, 95)
    
    stats_text = f"""Performance Metrics
    
RMSE:     {rmse:.6f}
MAE:      {mae:.6f}
R²:       {r2:.6f}
Max Error: {max_error:.6f}
p95 Error: {p95_error:.6f}

Samples:  {len(y_test)}
"""
    
    ax6.text(0.1, 0.5, stats_text, transform=ax6.transAxes, 
             fontsize=12, verticalalignment='center', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle(f'Surrogate Model Diagnostics: {output_name}', 
                fontsize=16, fontweight='bold')
    
    plt.savefig(output_path / 'diagnostics_summary.png', dpi=150)
    plt.close()
    
    logger.info(f"  Saved: {output_path / 'diagnostics_summary.png'}")


def main():
    """Main plotting pipeline."""
    parser = argparse.ArgumentParser(description='Generate error maps for surrogate model')
    parser.add_argument('--model-dir', type=Path, required=True, help='Path to model directory')
    parser.add_argument('--test-data', type=Path, required=True, help='Path to test data (X_test, y_test)')
    parser.add_argument('--output-name', type=str, default='output', help='Name of output variable')
    parser.add_argument('--input-names', nargs='+', help='Names of input variables')
    
    args = parser.parse_args()
    
    if plt is None:
        logger.error("matplotlib is required for plotting. Install with: pip install matplotlib")
        return 1
    
    logger.info("=" * 80)
    logger.info("SURROGATE MODEL ERROR MAPS")
    logger.info("=" * 80)
    
    # Load model
    model, scaler_X, scaler_y = load_model(args.model_dir)
    
    # Load test data
    X_test, y_test = load_test_data(args.test_data)
    
    # Make predictions
    logger.info("Making predictions on test data...")
    y_pred = predict_with_model(model, scaler_X, scaler_y, X_test)
    
    # Create output directory
    diagnostics_dir = args.model_dir / 'validation' / 'diagnostics'
    diagnostics_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate plots
    plot_parity(y_test, y_pred, diagnostics_dir, args.output_name)
    plot_residuals(y_test, y_pred, diagnostics_dir, args.output_name)
    plot_error_histogram(y_test, y_pred, diagnostics_dir, args.output_name)
    plot_error_heatmap_2d(X_test, y_test, y_pred, diagnostics_dir, args.input_names)
    generate_summary_plot(y_test, y_pred, diagnostics_dir, args.output_name)
    
    logger.info("=" * 80)
    logger.info("ERROR MAP GENERATION COMPLETE")
    logger.info(f"  Plots saved to: {diagnostics_dir}")
    logger.info("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
