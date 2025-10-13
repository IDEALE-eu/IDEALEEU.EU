# PROBES — CMM Probe Configurations

## Purpose

This directory contains probe configuration files and documentation for CMM measurement operations.

## Contents

### Configuration Types
- **Probe definitions**: Probe geometry and specifications
- **Qualification files**: Probe qualification results
- **Stylus configurations**: Tip and extension configurations
- **Probe libraries**: Standard probe setups

## Naming Convention

Use the following pattern:
```
PROBE_<probe-type>_<configuration>_<version>.<ext>
```

Examples:
- `PROBE_TP20_STANDARD-TIP_v01.prb`
- `PROBE_SP25_EXTENDED-STYLUS_v02.prb`
- `PROBE_RENISHAW_5-WAY_v01.prb`

## Probe Configuration Data

Each probe configuration should include:
- **Probe type**: Manufacturer and model
- **Stylus length**: Extension from probe body
- **Tip diameter**: Ball tip size
- **Qualification data**: Sphere diameter and form error
- **Accuracy specifications**: Expected measurement uncertainty
- **Usage notes**: Recommended applications

## Probe Qualification

### Qualification Process
1. Mount probe on CMM head
2. Qualify using reference sphere
3. Record sphere diameter and form error
4. Verify qualification within tolerance
5. Save qualification file
6. Document qualification date

### Qualification Frequency
- Before each measurement session
- After probe changes
- When suspect results occur
- Per quality procedures

## Related Directories

- **CMM programs**: [`../PROGRAMS/`](../PROGRAMS/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
- **Calibration**: [`../../CALIBRATION/`](../../CALIBRATION/)
