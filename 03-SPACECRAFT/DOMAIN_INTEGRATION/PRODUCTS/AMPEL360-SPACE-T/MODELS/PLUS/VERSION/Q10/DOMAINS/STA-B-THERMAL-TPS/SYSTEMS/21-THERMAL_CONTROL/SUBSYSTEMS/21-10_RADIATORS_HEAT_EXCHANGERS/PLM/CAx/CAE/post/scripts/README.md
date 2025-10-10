# SCRIPTS — Post-Processing Scripts

## Purpose
Automation scripts for result extraction, data processing, plot generation, and report automation.

## Contents
- Result extraction utilities
- Plot generation scripts
- Table formatting and export tools
- Report automation scripts
- Data export for Digital Twin
- Batch processing utilities

## File Organization
- One file per utility or function
- Include documentation and usage examples
- Store requirements and dependencies
- Maintain version control

## Naming Convention
```
21-10-CAE_script_<function>__r<NN>__<STATUS>.{py|m|sh}
```

Example: `21-10-CAE_script_extract_temperatures__r01__REL.py`

## Script Requirements
- Include header with purpose and usage
- Document input/output parameters
- Provide usage examples
- Include error handling
- Maintain dependencies list

## Script Organization
```
script_name.py
  ├─ README.md (usage, inputs, outputs)
  ├─ requirements.txt (Python dependencies)
  ├─ examples/ (test cases and sample data)
  └─ tests/ (unit tests if applicable)
```

## Common Script Types

### Result Extraction
```python
# extract_temperatures.py
# Extract nodal temperatures from solver output
# Usage: python extract_temperatures.py -i output.rst -o temps.csv
```

### Plot Generation
```python
# generate_contour_plots.py
# Generate temperature contour plots
# Usage: python generate_contour_plots.py -c case_config.json
```

### Report Automation
```python
# generate_analysis_report.py
# Automated report generation from templates
# Usage: python generate_analysis_report.py -t template.docx
```

## Language Guidelines
- **Python**: NumPy, Pandas, Matplotlib, SciPy
- **MATLAB**: Standard toolboxes, no proprietary add-ons
- **Bash**: Standard Unix utilities

## Guidelines
- Use standard libraries when possible
- Include clear documentation
- Provide usage examples
- Test with representative data
- Maintain compatibility across platforms
- Archive scripts with generated results

---

**Last Updated**: 2025-10-10
