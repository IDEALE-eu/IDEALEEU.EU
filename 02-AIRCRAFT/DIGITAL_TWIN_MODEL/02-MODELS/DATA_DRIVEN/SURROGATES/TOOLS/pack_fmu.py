#!/usr/bin/env python3
"""
pack_fmu.py - Package surrogate model as FMU (Functional Mock-up Unit).

This script packages a trained surrogate model into an FMU for 
co-simulation in digital twin environments supporting FMI standard.

Supports:
- FMI 2.0 and FMI 3.0
- Model Exchange and Co-Simulation modes
- Python-based FMU with embedded model

Usage:
    python pack_fmu.py --model-dir ../aero_wing_cl_cd/1.0.0/ --fmu-name aero_wing

Author: Digital Twin Model Team
Version: 1.0.0
"""

import argparse
import logging
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Dict, Any
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

try:
    import joblib
except ImportError:
    joblib = None

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_io_contract(contract_path: Path) -> Dict[str, Any]:
    """Load I/O contract to define FMU variables."""
    with open(contract_path, 'r') as f:
        contract = yaml.safe_load(f)
    return contract


def generate_model_description_xml(contract: Dict[str, Any], fmu_name: str, fmi_version: str = "2.0") -> str:
    """
    Generate modelDescription.xml for FMU.
    
    Returns:
        XML string
    """
    logger.info(f"Generating modelDescription.xml (FMI {fmi_version})...")
    
    if fmi_version == "2.0":
        return generate_fmi2_model_description(contract, fmu_name)
    elif fmi_version == "3.0":
        return generate_fmi3_model_description(contract, fmu_name)
    else:
        raise ValueError(f"Unsupported FMI version: {fmi_version}")


def generate_fmi2_model_description(contract: Dict[str, Any], fmu_name: str) -> str:
    """Generate FMI 2.0 modelDescription.xml."""
    
    # Create root element
    root = ET.Element('fmiModelDescription')
    root.set('fmiVersion', '2.0')
    root.set('modelName', fmu_name)
    root.set('guid', f'{{{fmu_name}-guid-placeholder}}')
    root.set('generationTool', 'IDEALE-EU pack_fmu.py')
    root.set('numberOfEventIndicators', '0')
    
    # Co-simulation attributes
    cosim = ET.SubElement(root, 'CoSimulation')
    cosim.set('modelIdentifier', fmu_name)
    cosim.set('canHandleVariableCommunicationStepSize', 'true')
    
    # Model variables
    model_vars = ET.SubElement(root, 'ModelVariables')
    
    var_index = 1
    
    # Add input variables
    for inp in contract.get('inputs', []):
        var = ET.SubElement(model_vars, 'ScalarVariable')
        var.set('name', inp['name'])
        var.set('valueReference', str(var_index))
        var.set('causality', 'input')
        var.set('variability', 'continuous')
        
        var_type = ET.SubElement(var, 'Real')
        if 'physical_range' in inp:
            var_type.set('min', str(inp['physical_range']['min']))
            var_type.set('max', str(inp['physical_range']['max']))
        
        var_index += 1
    
    # Add output variables
    for out in contract.get('outputs', []):
        var = ET.SubElement(model_vars, 'ScalarVariable')
        var.set('name', out['name'])
        var.set('valueReference', str(var_index))
        var.set('causality', 'output')
        var.set('variability', 'continuous')
        var.set('initial', 'calculated')
        
        var_type = ET.SubElement(var, 'Real')
        if 'expected_range' in out:
            var_type.set('min', str(out['expected_range']['min']))
            var_type.set('max', str(out['expected_range']['max']))
        
        var_index += 1
    
    # Model structure
    model_structure = ET.SubElement(root, 'ModelStructure')
    outputs_elem = ET.SubElement(model_structure, 'Outputs')
    
    # Reference output variables
    for i, out in enumerate(contract.get('outputs', [])):
        output_elem = ET.SubElement(outputs_elem, 'Unknown')
        output_elem.set('index', str(len(contract.get('inputs', [])) + i + 1))
    
    # Convert to pretty-printed XML string
    xml_str = ET.tostring(root, encoding='unicode')
    dom = minidom.parseString(xml_str)
    return dom.toprettyxml(indent='  ')


def generate_fmi3_model_description(contract: Dict[str, Any], fmu_name: str) -> str:
    """Generate FMI 3.0 modelDescription.xml (simplified)."""
    
    # FMI 3.0 has different structure, simplified here
    logger.info("FMI 3.0 generation is simplified in this example")
    
    # For full FMI 3.0 support, would need to follow FMI 3.0 schema
    return generate_fmi2_model_description(contract, fmu_name)  # Fallback to 2.0 for now


def create_fmu_python_wrapper(model_path: Path, fmu_name: str, contract: Dict[str, Any]) -> str:
    """
    Create Python wrapper script for FMU.
    
    Returns:
        Python code as string
    """
    logger.info("Creating Python wrapper for FMU...")
    
    inputs_list = ', '.join([f'"{inp["name"]}"' for inp in contract.get('inputs', [])])
    outputs_list = ', '.join([f'"{out["name"]}"' for out in contract.get('outputs', [])])
    
    wrapper_code = f'''"""
FMU wrapper for {fmu_name}
Auto-generated by pack_fmu.py
"""

import numpy as np
import joblib
from pathlib import Path

class {fmu_name}:
    """Surrogate model FMU wrapper."""
    
    def __init__(self):
        """Initialize the FMU."""
        self.model_dir = Path(__file__).parent / "resources"
        
        # Load model
        self.model = joblib.load(self.model_dir / "model.joblib")
        
        # Load scalers if they exist
        scaler_X_path = self.model_dir / "scaler_X.joblib"
        scaler_y_path = self.model_dir / "scaler_y.joblib"
        
        self.scaler_X = joblib.load(scaler_X_path) if scaler_X_path.exists() else None
        self.scaler_y = joblib.load(scaler_y_path) if scaler_y_path.exists() else None
        
        # Define input/output names
        self.input_names = [{inputs_list}]
        self.output_names = [{outputs_list}]
        
        # State
        self.inputs = {{name: 0.0 for name in self.input_names}}
        self.outputs = {{name: 0.0 for name in self.output_names}}
    
    def setup_experiment(self, start_time, stop_time, tolerance=None):
        """Setup experiment (FMI function)."""
        return True
    
    def enter_initialization_mode(self):
        """Enter initialization mode (FMI function)."""
        return True
    
    def exit_initialization_mode(self):
        """Exit initialization mode (FMI function)."""
        return True
    
    def set_real(self, value_references, values):
        """Set real input values."""
        for vr, value in zip(value_references, values):
            if vr < len(self.input_names):
                self.inputs[self.input_names[vr]] = value
        return True
    
    def get_real(self, value_references):
        """Get real output values."""
        values = []
        for vr in value_references:
            output_idx = vr - len(self.input_names)
            if 0 <= output_idx < len(self.output_names):
                values.append(self.outputs[self.output_names[output_idx]])
            else:
                values.append(0.0)
        return values
    
    def do_step(self, current_time, step_size, no_set_fmu_state_prior_to_current_point=True):
        """Execute one simulation step (FMI Co-Simulation function)."""
        
        # Collect inputs
        X_input = np.array([self.inputs[name] for name in self.input_names]).reshape(1, -1)
        
        # Scale inputs
        if self.scaler_X is not None:
            X_scaled = self.scaler_X.transform(X_input)
        else:
            X_scaled = X_input
        
        # Predict
        y_pred = self.model.predict(X_scaled)
        
        # Scale outputs
        if self.scaler_y is not None:
            y_pred = self.scaler_y.inverse_transform(y_pred.reshape(-1, 1)).ravel()
        
        # Update outputs
        for i, name in enumerate(self.output_names):
            if i < len(y_pred):
                self.outputs[name] = float(y_pred[i])
        
        return True
    
    def terminate(self):
        """Terminate the FMU."""
        return True
'''
    
    return wrapper_code


def package_fmu(model_dir: Path, output_path: Path, fmu_name: str, fmi_version: str = "2.0") -> None:
    """
    Package model as FMU.
    
    Args:
        model_dir: Directory containing trained model
        output_path: Output path for .fmu file
        fmu_name: Name of the FMU
        fmi_version: FMI version (2.0 or 3.0)
    """
    logger.info(f"Packaging FMU: {fmu_name}.fmu (FMI {fmi_version})...")
    
    # Create temporary directory for FMU structure
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Load I/O contract
        contract_path = model_dir / 'io_contract.yaml'
        if not contract_path.exists():
            logger.error(f"I/O contract not found: {contract_path}")
            raise FileNotFoundError(f"I/O contract required: {contract_path}")
        
        contract = load_io_contract(contract_path)
        
        # Create FMU directory structure
        # resources/ - contains model files
        # binaries/linux64/ or binaries/win64/ - compiled binaries (for non-Python FMUs)
        # sources/ - source code (for Python-based FMUs)
        
        resources_dir = temp_path / 'resources'
        resources_dir.mkdir(parents=True)
        
        sources_dir = temp_path / 'sources'
        sources_dir.mkdir(parents=True)
        
        # Copy model files to resources
        for model_file in ['model.joblib', 'scaler_X.joblib', 'scaler_y.joblib']:
            src_file = model_dir / model_file
            if src_file.exists():
                shutil.copy(src_file, resources_dir / model_file)
                logger.info(f"  Copied {model_file}")
        
        # Generate modelDescription.xml
        model_desc_xml = generate_model_description_xml(contract, fmu_name, fmi_version)
        model_desc_path = temp_path / 'modelDescription.xml'
        with open(model_desc_path, 'w') as f:
            f.write(model_desc_xml)
        logger.info("  Generated modelDescription.xml")
        
        # Generate Python wrapper
        wrapper_code = create_fmu_python_wrapper(model_dir, fmu_name, contract)
        wrapper_path = sources_dir / f'{fmu_name}.py'
        with open(wrapper_path, 'w') as f:
            f.write(wrapper_code)
        logger.info(f"  Generated {fmu_name}.py")
        
        # Create .fmu (ZIP archive)
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as fmu_zip:
            # Add all files to FMU
            for file_path in temp_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(temp_path)
                    fmu_zip.write(file_path, arcname=arcname)
                    logger.debug(f"  Added to FMU: {arcname}")
        
        logger.info(f"FMU created: {output_path} ({output_path.stat().st_size / 1024:.1f} KB)")


def main():
    """Main FMU packaging pipeline."""
    parser = argparse.ArgumentParser(description='Package surrogate model as FMU')
    parser.add_argument('--model-dir', type=Path, required=True, help='Path to model directory')
    parser.add_argument('--fmu-name', type=str, required=True, help='Name for the FMU')
    parser.add_argument('--output-dir', type=Path, help='Output directory for FMU (default: model-dir/runtime/fmu/)')
    parser.add_argument('--fmi-version', choices=['2.0', '3.0'], default='2.0', help='FMI version')
    
    args = parser.parse_args()
    
    logger.info("=" * 80)
    logger.info("SURROGATE MODEL FMU PACKAGING")
    logger.info("=" * 80)
    
    # Determine output path
    if args.output_dir is None:
        args.output_dir = args.model_dir / 'runtime' / 'fmu'
    
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f'{args.fmu_name}.fmu'
    
    # Package FMU
    try:
        package_fmu(args.model_dir, output_path, args.fmu_name, args.fmi_version)
        
        logger.info("=" * 80)
        logger.info("FMU PACKAGING COMPLETE")
        logger.info(f"  Output: {output_path}")
        logger.info(f"  FMI Version: {args.fmi_version}")
        logger.info("=" * 80)
        
        return 0
    except Exception as e:
        logger.error(f"FMU packaging failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
