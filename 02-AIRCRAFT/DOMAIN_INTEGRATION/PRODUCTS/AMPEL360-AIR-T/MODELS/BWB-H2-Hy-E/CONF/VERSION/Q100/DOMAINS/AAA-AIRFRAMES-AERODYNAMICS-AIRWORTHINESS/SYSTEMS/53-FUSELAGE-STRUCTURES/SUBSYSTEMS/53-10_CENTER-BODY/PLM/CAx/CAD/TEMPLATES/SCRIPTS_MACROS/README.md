# SCRIPTS_MACROS — CAD Automation Scripts and Macros

## Purpose

Automation scripts and macros for repetitive CAD tasks, batch operations, data validation, and export automation for the 53-10 Center Body project.

## Script Categories

### Validation Scripts
- Model validation and error checking
- Property completeness validation
- Naming convention verification
- Export quality validation

### Export Scripts
- Batch export to neutral formats (STEP, IGES, DXF, JT)
- Export with consistent settings
- Export report generation

### BOM Scripts
- BOM extraction to CSV/Excel
- Flattened BOM generation
- BOM comparison between revisions
- Standard parts report

### Utility Scripts
- Mass properties extraction
- Parameter extraction and reporting
- File renaming and organization
- Drawing view automation

## File Formats

### Python Scripts (`.py`)
- **Preferred format** for most automation
- Cross-platform compatible
- Good for data processing, validation, reporting
- Can interface with CAD APIs (if available)

### VBA Macros (`.vbs`, `.bas`)
- For CATIA, SOLIDWORKS automation
- Direct CAD API access
- Windows only

### Shell Scripts (`.sh`, `.bat`)
- For batch operations
- File management
- Calling external tools

### API Scripts
- CATIA VBA/CATScript
- NX NX Open (C#, Java, Python)
- SOLIDWORKS VBA/API
- Creo J-Link/WebLink

## Naming Convention

```
script_<function>_<purpose>_v<version>.<ext>
```

**Examples:**
- `script_validate_properties_v001.py`
- `script_export_step_batch_v002.py`
- `script_extract_bom_to_csv_v001.py`
- `macro_create_drawing_views_v001.vbs`

## Available Scripts

### Validation Scripts

#### validate_properties.py
**Purpose:** Validate that all CAD files have required properties filled in

**Usage:**
```bash
python validate_properties.py <directory>
```

**Checks:**
- Part number assigned
- Description not empty
- Revision level set
- Material assigned (parts only)
- Mass properties calculated

**Output:** CSV report of validation results

---

#### validate_naming_convention.py
**Purpose:** Verify file names follow naming convention

**Usage:**
```bash
python validate_naming_convention.py <directory>
```

**Checks:**
- Subsystem prefix (53-10)
- Type identifier (PRT, ASM, DWG)
- Version number format (vXX)
- No spaces or special characters

**Output:** List of files that don't comply

---

#### validate_export_quality.py
**Purpose:** Validate exported STEP/IGES files for quality

**Usage:**
```bash
python validate_export_quality.py <export_directory>
```

**Checks:**
- File opens without errors
- Geometry completeness
- Units correct (mm)
- File size reasonable

**Output:** Validation report

### Export Scripts

#### export_batch_step.py
**Purpose:** Batch export CAD files to STEP AP242 format

**Usage:**
```bash
python export_batch_step.py <input_directory> <output_directory>
```

**Settings:**
- Protocol: AP242
- Geometry: Solids + surfaces
- PMI: Include
- Assembly: Preserve structure

**Output:** STEP files + export log

---

#### export_batch_iges.py
**Purpose:** Batch export CAD files to IGES 5.3 format

**Usage:**
```bash
python export_batch_iges.py <input_directory> <output_directory>
```

**Settings:**
- Version: 5.3
- Surfaces: Trimmed NURBS
- Solids: BREP entity 186

---

#### export_batch_dxf.py
**Purpose:** Batch export flat patterns or 2D profiles to DXF

**Usage:**
```bash
python export_batch_dxf.py <input_directory> <output_directory>
```

**Use for:**
- Sheet metal flat patterns
- 2D profiles for machining
- Drawing views

### BOM Scripts

#### extract_bom_to_csv.py
**Purpose:** Extract BOM from assembly to CSV format

**Usage:**
```bash
python extract_bom_to_csv.py <assembly_file> <output_csv>
```

**Output columns:**
- Item, Part Number, Description, Qty, UOM, Material, Mass, Make/Buy

---

#### generate_flattened_bom.py
**Purpose:** Create flattened BOM with total quantities

**Usage:**
```bash
python generate_flattened_bom.py <assembly_file> <output_csv>
```

**Output:** Single-level BOM with rolled-up quantities

---

#### compare_bom_revisions.py
**Purpose:** Compare BOMs between two assembly revisions

**Usage:**
```bash
python compare_bom_revisions.py <asm_rev_A> <asm_rev_B> <output_report>
```

**Output:** Added, removed, and changed items

---

#### extract_standard_parts.py
**Purpose:** Generate report of all standard/catalog parts used

**Usage:**
```bash
python extract_standard_parts.py <directory> <output_csv>
```

**Output:** List of all fasteners, hardware, standard parts

### Utility Scripts

#### extract_mass_properties.py
**Purpose:** Extract mass, volume, and center of gravity from CAD models

**Usage:**
```bash
python extract_mass_properties.py <directory> <output_csv>
```

**Output:**
- Part Number, Mass (kg), Volume (mm³), CoG (X, Y, Z)

---

#### extract_parameters.py
**Purpose:** Extract design parameters from parametric models

**Usage:**
```bash
python extract_parameters.py <part_file> <output_csv>
```

**Output:** Parameter name, value, unit

---

#### batch_rename_files.py
**Purpose:** Rename files to comply with naming convention

**Usage:**
```bash
python batch_rename_files.py <directory> <mapping_csv>
```

**Input CSV:**
- Old filename, New filename

**Action:** Renames files and updates references (if possible)

---

#### automate_drawing_views.py
**Purpose:** Automatically create standard drawing views

**Usage:**
```bash
python automate_drawing_views.py <part_file> <drawing_template>
```

**Views created:**
- Front, Top, Right, Isometric

## Script Standards

### Code Quality
- **PEP 8** style for Python scripts
- Descriptive variable and function names
- Comments for complex logic
- Error handling with try/except
- Logging to file for debugging

### Documentation
Each script must include:
- Header comment with purpose, author, date
- Usage instructions
- Input/output descriptions
- Example invocation
- Dependencies and requirements

### Testing
- Test scripts with sample data before deployment
- Include test cases for edge conditions
- Validate output format and content
- Check for performance on large datasets

## Script Template

### Python Script Template

```python
#!/usr/bin/env python3
"""
Script Name: script_example_template.py
Purpose: Brief description of what the script does
Author: Your Name
Date: YYYY-MM-DD
Version: 001

Usage:
    python script_example_template.py <input> <output>
    
Example:
    python script_example_template.py parts/ output.csv

Requirements:
    - Python 3.7+
    - Libraries: pandas, numpy (if needed)
"""

import sys
import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('script_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main(input_path, output_path):
    """
    Main function logic
    
    Args:
        input_path (str): Input directory or file
        output_path (str): Output file or directory
        
    Returns:
        int: 0 for success, 1 for failure
    """
    try:
        logger.info(f"Starting script with input: {input_path}")
        
        # Script logic here
        # ...
        
        logger.info(f"Script completed successfully. Output: {output_path}")
        return 0
        
    except Exception as e:
        logger.error(f"Script failed: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_example_template.py <input> <output>")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    output_arg = sys.argv[2]
    
    exit_code = main(input_arg, output_arg)
    sys.exit(exit_code)
```

## CAD API Integration

### CATIA Automation (VBA)
```vba
Sub ExportSTEP()
    Dim partDoc As PartDocument
    Set partDoc = CATIA.ActiveDocument
    
    ' Export settings
    partDoc.ExportData "C:\output\part.step", "stp"
End Sub
```

### SOLIDWORKS API (VBA)
```vba
Sub ExportSTEP()
    Dim swModel As ModelDoc2
    Set swModel = swApp.ActiveDoc
    
    ' Export to STEP
    swModel.SaveAs "C:\output\part.step"
End Sub
```

### NX Open (Python)
```python
import NXOpen

def export_step(part_file, output_file):
    session = NXOpen.Session.GetSession()
    part = session.Parts.Work
    
    # Export to STEP
    # ... NX API calls
```

## Usage Guidelines

### Running Scripts
1. Test on sample data first
2. Backup files before batch operations
3. Review output/logs after execution
4. Document any issues or limitations

### Script Modification
1. Create new version (increment version number)
2. Test thoroughly before deployment
3. Update documentation
4. Archive old version

### Troubleshooting
- Check script log file for errors
- Verify input file/directory paths exist
- Ensure required libraries are installed
- Check CAD API version compatibility

## Related Directories

- **Export**: [`../EXPORT/`](../EXPORT/) — Export standards
- **BOM**: [`../BOM/`](../BOM/) — BOM structure
- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Property standards
- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — Naming rules

## References

- Main templates documentation: [`../README.md`](../README.md)
- CAD API documentation (CATIA, NX, SOLIDWORKS, Creo)
- Python scripting guides
- VBA programming references
- Automation best practices: [`/00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/`](/00-PROGRAM/CONFIG_MGMT/12-CI_CD_RULES/)
