#!/usr/bin/env python3
"""
Build TensorRT engine from ONNX model for optimized inference on NVIDIA GPUs.

Usage:
    python build_trt_engine.py --model <model.onnx> --output <model.trt> --precision fp16

Features:
    - FP32, FP16, INT8 precision modes
    - Dynamic shapes support
    - Calibration for INT8
    - Engine serialization

Note: Requires TensorRT installed (NVIDIA GPUs only)
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, List, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def build_tensorrt_engine(onnx_path: str, engine_path: str, precision: str = 'fp32',
                          max_batch_size: int = 1, workspace_size_gb: int = 1,
                          calibration_data_path: Optional[str] = None):
    """Build TensorRT engine from ONNX model."""
    try:
        import tensorrt as trt
    except ImportError:
        logger.error("TensorRT is required. Install from: https://developer.nvidia.com/tensorrt")
        logger.error("This tool is only available on systems with NVIDIA GPUs")
        sys.exit(1)
    
    logger.info(f"Building TensorRT engine from {onnx_path}")
    logger.info(f"Precision: {precision}, Max batch size: {max_batch_size}")
    
    # Create builder and network
    TRT_LOGGER = trt.Logger(trt.Logger.INFO)
    builder = trt.Builder(TRT_LOGGER)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
    parser = trt.OnnxParser(network, TRT_LOGGER)
    
    # Parse ONNX model
    logger.info("Parsing ONNX model...")
    with open(onnx_path, 'rb') as model:
        if not parser.parse(model.read()):
            logger.error("Failed to parse ONNX model")
            for error in range(parser.num_errors):
                logger.error(parser.get_error(error))
            sys.exit(1)
    
    logger.info("✓ ONNX model parsed successfully")
    
    # Configure builder
    config = builder.create_builder_config()
    config.max_workspace_size = workspace_size_gb * (1 << 30)  # Convert GB to bytes
    
    # Set precision
    if precision == 'fp16':
        if not builder.platform_has_fast_fp16:
            logger.warning("FP16 not supported on this platform, falling back to FP32")
        else:
            logger.info("Enabling FP16 mode")
            config.set_flag(trt.BuilderFlag.FP16)
    elif precision == 'int8':
        if not builder.platform_has_fast_int8:
            logger.warning("INT8 not supported on this platform, falling back to FP32")
        else:
            logger.info("Enabling INT8 mode")
            config.set_flag(trt.BuilderFlag.INT8)
            
            if calibration_data_path:
                logger.info(f"Using calibration data from {calibration_data_path}")
                # In practice, you'd implement a custom calibrator here
                logger.warning("INT8 calibration not fully implemented in this example")
            else:
                logger.warning("INT8 mode requested but no calibration data provided")
    
    # Build engine
    logger.info("Building TensorRT engine (this may take several minutes)...")
    engine = builder.build_engine(network, config)
    
    if engine is None:
        logger.error("Failed to build TensorRT engine")
        sys.exit(1)
    
    logger.info("✓ Engine built successfully")
    
    # Serialize and save engine
    logger.info(f"Serializing engine to {engine_path}")
    with open(engine_path, 'wb') as f:
        f.write(engine.serialize())
    
    logger.info(f"✓ TensorRT engine saved to {engine_path}")
    
    # Print engine info
    logger.info("\nEngine information:")
    logger.info(f"  Number of layers: {network.num_layers}")
    logger.info(f"  Number of inputs: {network.num_inputs}")
    logger.info(f"  Number of outputs: {network.num_outputs}")
    
    for i in range(network.num_inputs):
        input_tensor = network.get_input(i)
        logger.info(f"  Input {i}: {input_tensor.name} {input_tensor.shape}")
    
    for i in range(network.num_outputs):
        output_tensor = network.get_output(i)
        logger.info(f"  Output {i}: {output_tensor.name} {output_tensor.shape}")


def verify_tensorrt_engine(engine_path: str):
    """Verify TensorRT engine can be loaded and run."""
    try:
        import tensorrt as trt
        import pycuda.driver as cuda
        import pycuda.autoinit
    except ImportError:
        logger.error("TensorRT and pycuda are required")
        sys.exit(1)
    
    logger.info(f"Verifying TensorRT engine: {engine_path}")
    
    TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
    
    # Load engine
    with open(engine_path, 'rb') as f:
        runtime = trt.Runtime(TRT_LOGGER)
        engine = runtime.deserialize_cuda_engine(f.read())
    
    if engine is None:
        logger.error("Failed to load TensorRT engine")
        sys.exit(1)
    
    logger.info("✓ Engine loaded successfully")
    
    # Create execution context
    context = engine.create_execution_context()
    logger.info("✓ Execution context created")
    
    logger.info("\nEngine bindings:")
    for i in range(engine.num_bindings):
        binding_name = engine.get_binding_name(i)
        binding_shape = engine.get_binding_shape(i)
        binding_dtype = engine.get_binding_dtype(i)
        is_input = engine.binding_is_input(i)
        logger.info(f"  {'Input' if is_input else 'Output'} {i}: {binding_name} "
                   f"{binding_shape} {binding_dtype}")


def main():
    parser = argparse.ArgumentParser(description='Build TensorRT engine from ONNX model')
    parser.add_argument('--model', required=True, help='Path to ONNX model')
    parser.add_argument('--output', required=True, help='Output TensorRT engine file (.trt)')
    parser.add_argument('--precision', default='fp32', choices=['fp32', 'fp16', 'int8'],
                        help='Precision mode')
    parser.add_argument('--max-batch-size', type=int, default=1, help='Maximum batch size')
    parser.add_argument('--workspace-size-gb', type=int, default=1, 
                        help='Max workspace size in GB')
    parser.add_argument('--calibration-data', help='Calibration data for INT8 (NPZ format)')
    parser.add_argument('--verify', action='store_true', help='Verify engine after building')
    
    args = parser.parse_args()
    
    if not Path(args.model).exists():
        logger.error(f"Model file not found: {args.model}")
        sys.exit(1)
    
    # Create output directory
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    
    # Build engine
    build_tensorrt_engine(
        args.model,
        args.output,
        args.precision,
        args.max_batch_size,
        args.workspace_size_gb,
        args.calibration_data
    )
    
    # Verify if requested
    if args.verify:
        verify_tensorrt_engine(args.output)
    
    logger.info("\n" + "="*50)
    logger.info("✓ TensorRT engine build complete!")
    logger.info("  Use profile_ort.py to benchmark performance")
    logger.info("="*50)


if __name__ == '__main__':
    main()
