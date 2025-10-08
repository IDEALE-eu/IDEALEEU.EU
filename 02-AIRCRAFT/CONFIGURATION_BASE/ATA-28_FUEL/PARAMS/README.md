# Parameters Directory

This directory contains all system parameter definitions, limits, thresholds, and operating specifications for the fuel system.

## Contents

Parameter files define:
- Operating ranges and nominal values
- Minimum and maximum limits
- Tolerance specifications
- Safety margins
- Threshold values for monitoring and alerts

## File Format

Parameters are typically stored in CSV format following the template in `00-COMMON/TEMPLATES/PARAMS.csv`.

Required fields:
- Parameter_Name
- Unit
- Nominal_Value
- Min_Limit
- Max_Limit
- Tolerance
- Safety_Critical
- Description
- Source_Requirement
- Last_Updated
- Status

## Expected Files

- `H2_STORAGE_PRESSURE.csv` - Hydrogen storage pressure parameters
- `CRYO_TEMP_LIMITS.csv` - Cryogenic temperature limits
- `FUEL_FLOW_PARAMS.csv` - Fuel flow parameters
- `LEAK_DETECTION_THRESHOLDS.csv` - Leak detection sensitivity
- `SAFETY_MARGINS.csv` - Safety margin specifications

## Usage

1. Copy template from `../../00-COMMON/TEMPLATES/PARAMS.csv`
2. Fill in parameter values
3. Validate against schema
4. Review and approve through CCB
5. Document in CHANGE_LOG

## Validation

Validate parameter files using:
```bash
csvlint H2_STORAGE_PRESSURE.csv
```

---

**Last Updated**: 2024-01-15
