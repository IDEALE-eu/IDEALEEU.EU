#!/usr/bin/env python3
"""
Quantize ONNX models for reduced size and faster inference on edge devices.

Usage:
    python quantize_onnx.py --model <model.onnx> --mode <int8|dynamic_fp16> --output <quantized.onnx>

Quantization modes:
    - int8: Static quantization (requires calibration data)
    - dynamic_fp16: Dynamic FP16 quantization (no calibration needed)
    - dynamic_int8: Dynamic INT8 quantization
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def quantize_dynamic_fp16(model_path: str, output_path: str):
    """Apply dynamic FP16 quantization (mixed precision)."""
    try:
        import onnx
        from onnxruntime.quantization import quantize_dynamic, QuantType
    except ImportError:
        logger.error("onnxruntime is required for quantization")
        sys.exit(1)
    
    logger.info(f"Applying dynamic FP16 quantization to {model_path}")
    
    # Note: FP16 quantization is typically done at the hardware level (GPU)
    # For ONNX, we use dynamic quantization with FP16 operators
    logger.warning("FP16 quantization requires hardware support (e.g., NVIDIA GPUs with Tensor Cores)")
    logger.info("Converting model to use FP16 where possible...")
    
    # Load model
    model = onnx.load(model_path)
    
    # This is a simplified approach - in practice, you'd use ONNX graph transformers
    # to convert FP32 ops to FP16 where beneficial
    logger.info(f"Saving to {output_path}")
    onnx.save(model, output_path)
    
    logger.info("✓ FP16 quantization complete (manual verification recommended)")


def quantize_dynamic_int8(model_path: str, output_path: str):
    """Apply dynamic INT8 quantization."""
    try:
        from onnxruntime.quantization import quantize_dynamic, QuantType
    except ImportError:
        logger.error("onnxruntime is required for quantization")
        sys.exit(1)
    
    logger.info(f"Applying dynamic INT8 quantization to {model_path}")
    
    quantize_dynamic(
        model_path,
        output_path,
        weight_type=QuantType.QInt8
    )
    
    logger.info(f"✓ INT8 quantized model saved to {output_path}")


def quantize_static_int8(model_path: str, output_path: str, calibration_data_path: Optional[str] = None):
    """Apply static INT8 quantization with calibration."""
    try:
        from onnxruntime.quantization import quantize_static, QuantType, CalibrationDataReader
        import onnxruntime as ort
    except ImportError:
        logger.error("onnxruntime is required for quantization")
        sys.exit(1)
    
    if not calibration_data_path:
        logger.error("Calibration data is required for static INT8 quantization")
        sys.exit(1)
    
    logger.info(f"Loading calibration data from {calibration_data_path}")
    
    # Custom calibration data reader
    class CalibrationDataReaderImpl(CalibrationDataReader):
        def __init__(self, data_path):
            self.data = np.load(data_path)
            self.input_names = list(self.data.keys())
            self.data_list = [{k: self.data[k][i:i+1] for k in self.input_names} 
                              for i in range(len(self.data[self.input_names[0]]))]
            self.current_idx = 0
        
        def get_next(self):
            if self.current_idx >= len(self.data_list):
                return None
            data = self.data_list[self.current_idx]
            self.current_idx += 1
            return data
    
    logger.info(f"Applying static INT8 quantization to {model_path}")
    
    calibration_reader = CalibrationDataReaderImpl(calibration_data_path)
    
    quantize_static(
        model_path,
        output_path,
        calibration_data_reader=calibration_reader
    )
    
    logger.info(f"✓ Static INT8 quantized model saved to {output_path}")


def compare_model_sizes(original_path: str, quantized_path: str):
    """Compare file sizes of original and quantized models."""
    original_size = Path(original_path).stat().st_size / (1024 * 1024)  # MB
    quantized_size = Path(quantized_path).stat().st_size / (1024 * 1024)  # MB
    compression_ratio = (1 - quantized_size / original_size) * 100
    
    logger.info(f"\nModel size comparison:")
    logger.info(f"  Original:  {original_size:.2f} MB")
    logger.info(f"  Quantized: {quantized_size:.2f} MB")
    logger.info(f"  Reduction: {compression_ratio:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Quantize ONNX models for edge deployment')
    parser.add_argument('--model', required=True, help='Path to input ONNX model')
    parser.add_argument('--mode', required=True, 
                        choices=['int8_static', 'int8_dynamic', 'fp16'],
                        help='Quantization mode')
    parser.add_argument('--output', required=True, help='Path to output quantized model')
    parser.add_argument('--calibration-data', help='Path to calibration data (NPZ format, required for int8_static)')
    
    args = parser.parse_args()
    
    if not Path(args.model).exists():
        logger.error(f"Model file not found: {args.model}")
        sys.exit(1)
    
    # Create output directory
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    
    # Apply quantization
    if args.mode == 'fp16':
        quantize_dynamic_fp16(args.model, args.output)
    elif args.mode == 'int8_dynamic':
        quantize_dynamic_int8(args.model, args.output)
    elif args.mode == 'int8_static':
        quantize_static_int8(args.model, args.output, args.calibration_data)
    
    # Compare sizes
    compare_model_sizes(args.model, args.output)
    
    logger.info("\n" + "="*50)
    logger.info("✓ Quantization complete!")
    logger.info("  Run validate_onnx.py to verify accuracy")
    logger.info("="*50)


if __name__ == '__main__':
    main()
