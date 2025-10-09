# SCRIPTS — Automation Scripts for Integration Tasks

## Purpose

Automation scripts for repetitive integration tasks, data validation, and report generation for the CENTER-BODY subsystem.

## Content Types

- **Validation Scripts** — Data and model validation
- **Conversion Scripts** — Format conversion utilities
- **Report Generation Scripts** — Automated reporting
- **Analysis Scripts** — Batch analysis automation

## File Formats

- `.py` — Python scripts (preferred)
- `.sh` / `.bat` — Shell scripts
- `.m` — MATLAB scripts
- `.vbs` — VBA macros

## Naming Convention

```
script_{function}_{purpose}_v{version}.{ext}
```

Examples:
- `script_validate_interface_matrix_v001.py`
- `script_convert_cad_to_step_v002.sh`
- `script_generate_mass_properties_report_v001.py`

## Cross-References

- [Parent: CAI Root](../README.md)
- [Interface Matrix](../INTERFACE_MATRIX/README.md)
- [Validation Rules](../../../../../../../../00-PROGRAM/CONFIG_MGMT/12-CI/)

## Available Scripts

### Validation Scripts
- **validate_interface_matrix.py** — CSV format and content validation
- **validate_cad_geometry.py** — CAD model quality checks
- **validate_hole_patterns.py** — Fastener pattern verification
- **validate_clearances.py** — 3D clearance checking

### Conversion Scripts
- **convert_cad_formats.py** — Batch CAD file conversion
- **export_mass_properties.py** — Extract weight and CG data
- **generate_step_from_native.sh** — Native CAD to STEP export

### Report Generation
- **generate_interface_status_report.py** — Interface closure tracking
- **generate_integration_metrics.py** — KPI dashboard data
- **generate_bom_from_cad.py** — Automated BOM extraction

### Analysis Scripts
- **batch_tolerance_analysis.py** — Multiple stack-up analyses
- **batch_fea_submission.py** — Automated FEA job submission
- **compare_cad_revisions.py** — Geometry change detection

## Script Standards

All scripts must follow:
- Consistent coding style (PEP 8 for Python)
- Comprehensive error handling
- Logging for audit trail
- Command-line argument parsing
- Help/usage documentation
- Version information in header

## Script Template

```python
#!/usr/bin/env python3
"""
Script: script_name.py
Purpose: Brief description
Author: Name
Date: YYYY-MM-DD
Version: 1.0
"""

import logging
import argparse
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='Output file')
    args = parser.parse_args()
    
    try:
        logger.info("Starting script...")
        # Script logic here
        logger.info("Script completed successfully")
        return 0
    except Exception as e:
        logger.error(f"Script failed: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

## Usage Guidelines

Before running scripts:
1. Review script documentation
2. Verify input file formats
3. Check output directory permissions
4. Test on sample data first
5. Review log files for errors
6. Validate results

## Change Control

Script updates require:
- Version increment
- Testing and validation
- Update to script documentation
- Notification to users if interface changes
