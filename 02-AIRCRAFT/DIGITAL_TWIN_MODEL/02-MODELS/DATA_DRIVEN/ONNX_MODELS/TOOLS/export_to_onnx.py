#!/usr/bin/env python3
"""
Export trained models from ML frameworks (TensorFlow, PyTorch, scikit-learn) to ONNX format.

Usage:
    python export_to_onnx.py --model-path <path> --framework <tf|torch|sklearn> --output <output.onnx>

Features:
    - Automatic framework detection
    - Opset version configuration
    - Input/output shape inference
    - Metadata embedding
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def export_tensorflow_to_onnx(model_path: str, output_path: str, opset_version: int = 17) -> Dict[str, Any]:
    """Export TensorFlow/Keras model to ONNX."""
    try:
        import tensorflow as tf
        import tf2onnx
    except ImportError:
        logger.error("TensorFlow and tf2onnx are required for TensorFlow model export")
        sys.exit(1)
    
    logger.info(f"Loading TensorFlow model from {model_path}")
    model = tf.keras.models.load_model(model_path)
    
    logger.info(f"Converting to ONNX with opset {opset_version}")
    spec = (tf.TensorSpec(model.inputs[0].shape, tf.float32, name="input"),)
    output_path_obj = Path(output_path)
    
    model_proto, _ = tf2onnx.convert.from_keras(
        model,
        input_signature=spec,
        opset=opset_version,
        output_path=str(output_path_obj)
    )
    
    logger.info(f"Successfully exported to {output_path}")
    
    return {
        "framework": "tensorflow",
        "opset_version": opset_version,
        "input_names": [inp.name for inp in model.inputs],
        "output_names": [out.name for out in model.outputs],
        "input_shapes": [inp.shape.as_list() for inp in model.inputs],
        "output_shapes": [out.shape.as_list() for out in model.outputs]
    }


def export_pytorch_to_onnx(model_path: str, output_path: str, opset_version: int = 17, 
                           input_shape: tuple = (1, 10)) -> Dict[str, Any]:
    """Export PyTorch model to ONNX."""
    try:
        import torch
    except ImportError:
        logger.error("PyTorch is required for PyTorch model export")
        sys.exit(1)
    
    logger.info(f"Loading PyTorch model from {model_path}")
    model = torch.load(model_path)
    model.eval()
    
    logger.info(f"Creating dummy input with shape {input_shape}")
    dummy_input = torch.randn(*input_shape)
    
    logger.info(f"Converting to ONNX with opset {opset_version}")
    torch.onnx.export(
        model,
        dummy_input,
        output_path,
        export_params=True,
        opset_version=opset_version,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    
    logger.info(f"Successfully exported to {output_path}")
    
    return {
        "framework": "pytorch",
        "opset_version": opset_version,
        "input_names": ["input"],
        "output_names": ["output"],
        "input_shapes": [list(input_shape)],
    }


def export_sklearn_to_onnx(model_path: str, output_path: str, initial_types: list = None) -> Dict[str, Any]:
    """Export scikit-learn model to ONNX."""
    try:
        import pickle
        from skl2onnx import convert_sklearn
        from skl2onnx.common.data_types import FloatTensorType
    except ImportError:
        logger.error("scikit-learn and skl2onnx are required for sklearn model export")
        sys.exit(1)
    
    logger.info(f"Loading scikit-learn model from {model_path}")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    if initial_types is None:
        initial_types = [('input', FloatTensorType([None, 10]))]
    
    logger.info("Converting to ONNX")
    onnx_model = convert_sklearn(model, initial_types=initial_types)
    
    with open(output_path, 'wb') as f:
        f.write(onnx_model.SerializeToString())
    
    logger.info(f"Successfully exported to {output_path}")
    
    return {
        "framework": "sklearn",
        "opset_version": onnx_model.opset_import[0].version,
        "input_names": ["input"],
        "output_names": ["output"]
    }


def main():
    parser = argparse.ArgumentParser(description='Export ML models to ONNX format')
    parser.add_argument('--model-path', required=True, help='Path to trained model')
    parser.add_argument('--framework', required=True, choices=['tf', 'torch', 'sklearn'], 
                        help='Source framework')
    parser.add_argument('--output', required=True, help='Output ONNX file path')
    parser.add_argument('--opset', type=int, default=17, help='ONNX opset version (default: 17)')
    parser.add_argument('--input-shape', type=str, help='Input shape for PyTorch (e.g., "1,10")')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    
    # Export based on framework
    if args.framework == 'tf':
        metadata = export_tensorflow_to_onnx(args.model_path, args.output, args.opset)
    elif args.framework == 'torch':
        input_shape = tuple(map(int, args.input_shape.split(','))) if args.input_shape else (1, 10)
        metadata = export_pytorch_to_onnx(args.model_path, args.output, args.opset, input_shape)
    elif args.framework == 'sklearn':
        metadata = export_sklearn_to_onnx(args.model_path, args.output)
    
    # Save opset version to file
    opset_file = Path(args.output).parent / 'opset.txt'
    with open(opset_file, 'w') as f:
        f.write(str(metadata['opset_version']))
    
    logger.info(f"Opset version {metadata['opset_version']} saved to {opset_file}")
    logger.info("Export complete!")


if __name__ == '__main__':
    main()
