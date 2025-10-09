# PIN_GAUGES — Pin and Plug Gauges

## Purpose

This directory contains specifications and documentation for pin gauges and plug gauges used for precision diameter and location verification.

## Contents

### Gauge Types
- **Pin gauge sets**: Incremental diameter sets
- **Plug gauges**: Fixed diameter verification
- **Tapered pin gauges**: Variable diameter checks
- **Thread plug gauges**: Thread verification
- **Special feature gauges**: Custom geometry verification

## Naming Convention

Use the following pattern:
```
GAGE_PIN_<feature>_<size>_<version>.pdf
```

Examples:
- `GAGE_PIN_HOLE-DIA_10.000MM_v01.pdf`
- `GAGE_PIN_SET_0.50-1.00MM_v02.pdf`
- `GAGE_PIN_THREAD_M8X1.25_v01.pdf`

## Pin Gauge Classes

### Class X (±0.0005 inch / ±0.013 mm)
- General purpose inspection
- Standard production use
- Annual calibration

### Class XX (±0.0002 inch / ±0.005 mm)
- Precision inspection
- Tooling and fixture verification
- Semi-annual calibration

### Class XXX (±0.0001 inch / ±0.0025 mm)
- High-precision inspection
- Master gauge verification
- Quarterly calibration

## Usage Instructions

### Hole Diameter Verification
1. Clean hole and gauge
2. Insert gauge with light pressure
3. Gauge should enter smoothly
4. Check for binding or looseness
5. Verify fit per acceptance criteria

### Gauge Selection
- Select gauge closest to nominal size
- Use go gauge for minimum diameter
- Use no-go gauge for maximum diameter
- Document gauge size used

## Gauge Care and Handling

### Best Practices
- Store in protective case
- Clean before and after use
- Avoid dropping or impact
- Protect from corrosion
- Handle by non-measuring surfaces
- Never force into tight holes

### Maintenance
- Clean with approved solvents
- Apply light protective oil
- Inspect for wear and damage
- Retire worn or damaged gauges
- Maintain calibration records

## Related Directories

- **Go/no-go gauges**: [`../GO_NO_GO/`](../GO_NO_GO/)
- **Calibration records**: [`../../CALIBRATION/`](../../CALIBRATION/)
- **Tool lists**: [`../../SETUP/TOOL_LIST/`](../../SETUP/TOOL_LIST/)
