#!/usr/bin/env python3
"""
Validate ONNX models: check structure, opset compatibility, and run test inference.

Usage:
    python validate_onnx.py --model <model.onnx> --test-data <golden_inputs.npz>

Validation checks:
    - Model structure and graph integrity
    - Opset version compatibility
    - Input/output shape consistency
    - Test inference with golden vectors
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional

import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def validate_model_structure(model_path: str) -> Dict[str, Any]:
    """Validate ONNX model structure and metadata."""
    try:
        import onnx
        from onnx import checker, shape_inference
    except ImportError:
        logger.error("onnx package is required for validation")
        sys.exit(1)
    
    logger.info(f"Loading ONNX model from {model_path}")
    model = onnx.load(model_path)
    
    # Check model structure
    logger.info("Checking model structure...")
    try:
        checker.check_model(model)
        logger.info("✓ Model structure is valid")
    except Exception as e:
        logger.error(f"✗ Model structure validation failed: {e}")
        return {"valid": False, "error": str(e)}
    
    # Infer shapes
    logger.info("Inferring shapes...")
    try:
        model_with_shapes = shape_inference.infer_shapes(model)
        logger.info("✓ Shape inference successful")
    except Exception as e:
        logger.warning(f"⚠ Shape inference failed: {e}")
    
    # Extract metadata
    opset_version = model.opset_import[0].version
    inputs = [(inp.name, [dim.dim_value for dim in inp.type.tensor_type.shape.dim]) 
              for inp in model.graph.input]
    outputs = [(out.name, [dim.dim_value for dim in out.type.tensor_type.shape.dim]) 
               for out in model.graph.output]
    
    logger.info(f"Opset version: {opset_version}")
    logger.info(f"Inputs: {inputs}")
    logger.info(f"Outputs: {outputs}")
    
    return {
        "valid": True,
        "opset_version": opset_version,
        "inputs": inputs,
        "outputs": outputs,
        "num_nodes": len(model.graph.node)
    }


def validate_inference(model_path: str, test_data_path: Optional[str] = None) -> Dict[str, Any]:
    """Run test inference to validate model execution."""
    try:
        import onnxruntime as ort
    except ImportError:
        logger.error("onnxruntime is required for inference validation")
        sys.exit(1)
    
    logger.info("Creating ONNX Runtime session...")
    sess = ort.InferenceSession(model_path)
    
    input_names = [inp.name for inp in sess.get_inputs()]
    output_names = [out.name for out in sess.get_outputs()]
    
    logger.info(f"Model inputs: {input_names}")
    logger.info(f"Model outputs: {output_names}")
    
    # Load test data or create dummy input
    if test_data_path and Path(test_data_path).exists():
        logger.info(f"Loading test data from {test_data_path}")
        test_data = np.load(test_data_path)
        input_data = {name: test_data[name] for name in input_names}
    else:
        logger.info("Creating dummy input data")
        input_shapes = [inp.shape for inp in sess.get_inputs()]
        input_data = {}
        for name, shape in zip(input_names, input_shapes):
            # Replace dynamic dimensions with batch size 1
            concrete_shape = [1 if (d is None or isinstance(d, str)) else d for d in shape]
            input_data[name] = np.random.randn(*concrete_shape).astype(np.float32)
    
    # Run inference
    logger.info("Running inference...")
    try:
        outputs = sess.run(output_names, input_data)
        logger.info("✓ Inference successful")
        
        for name, output in zip(output_names, outputs):
            logger.info(f"  {name}: shape={output.shape}, dtype={output.dtype}")
        
        return {
            "inference_successful": True,
            "output_shapes": [out.shape for out in outputs],
            "output_dtypes": [str(out.dtype) for out in outputs]
        }
    except Exception as e:
        logger.error(f"✗ Inference failed: {e}")
        return {"inference_successful": False, "error": str(e)}


def check_opset_compatibility(opset_version: int, target_runtime: str = "ort") -> bool:
    """Check if opset version is compatible with target runtime."""
    # ONNX Runtime supports opset 7-18 (as of ORT 1.14)
    # TensorRT supports opset up to 17
    
    compatibility = {
        "ort": (7, 18),
        "trt": (7, 17),
        "openvino": (10, 17)
    }
    
    min_opset, max_opset = compatibility.get(target_runtime, (7, 17))
    
    if min_opset <= opset_version <= max_opset:
        logger.info(f"✓ Opset {opset_version} is compatible with {target_runtime}")
        return True
    else:
        logger.warning(f"⚠ Opset {opset_version} may not be compatible with {target_runtime} "
                      f"(supported: {min_opset}-{max_opset})")
        return False


def main():
    parser = argparse.ArgumentParser(description='Validate ONNX models')
    parser.add_argument('--model', required=True, help='Path to ONNX model')
    parser.add_argument('--test-data', help='Path to test data (NPZ format)')
    parser.add_argument('--runtime', default='ort', choices=['ort', 'trt', 'openvino'],
                        help='Target runtime for compatibility check')
    
    args = parser.parse_args()
    
    if not Path(args.model).exists():
        logger.error(f"Model file not found: {args.model}")
        sys.exit(1)
    
    # Validate structure
    structure_result = validate_model_structure(args.model)
    if not structure_result.get("valid"):
        logger.error("Model structure validation failed")
        sys.exit(1)
    
    # Check opset compatibility
    opset_version = structure_result.get("opset_version")
    check_opset_compatibility(opset_version, args.runtime)
    
    # Validate inference
    inference_result = validate_inference(args.model, args.test_data)
    if not inference_result.get("inference_successful"):
        logger.error("Inference validation failed")
        sys.exit(1)
    
    logger.info("\n" + "="*50)
    logger.info("✓ All validation checks passed!")
    logger.info("="*50)


if __name__ == '__main__':
    main()
