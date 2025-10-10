# GO_NO_GO — Go/No-Go Gauges

## Purpose

This directory contains specifications, drawings, and documentation for go/no-go gauges used in quick attribute inspection.

## Contents

### Gauge Types
- **Hole diameter gauges**: Verify hole sizes
- **Thread gauges**: Thread pitch and fit verification
- **Profile gauges**: Contour and shape checks
- **Gap gauges**: Clearance and spacing verification
- **Feature location gauges**: Position verification

## Naming Convention

Use the following pattern:
```
GAGE_GONO_<feature>_<size>_<version>.pdf
```

Examples:
- `GAGE_GONO_HOLE-DIA_10MM_v01.pdf`
- `GAGE_GONO_THREAD_M8X1.25_v02.pdf`
- `GAGE_GONO_PROFILE_FRAME-F05_v01.pdf`

## Gauge Specifications

Each gauge specification should include:
- **Gauge ID**: Unique identifier
- **Description**: Purpose and application
- **Go dimension**: Maximum material condition
- **No-go dimension**: Minimum material condition
- **Tolerance**: Gauge manufacturing tolerance
- **Material**: Gauge material specification
- **Hardness**: Required hardness (typically Rc 60-65)
- **Calibration frequency**: Required calibration interval

## Usage Instructions

### Go Side (Green)
- Should enter or fit the feature
- Verifies feature is not undersized
- Maximum material condition

### No-Go Side (Red)
- Should NOT enter or fit the feature
- Verifies feature is not oversized
- Minimum material condition

### Acceptance Criteria
- **Pass**: Go side enters, No-Go does not enter
- **Fail**: Go side does not enter OR No-Go side enters
- **Document**: Record results on inspection form

## Gauge Design Requirements

Go/no-go gauges should:
- Be clearly marked GO and NO-GO
- Use color coding (green/red)
- Be easy to use and interpret
- Have wear allowances
- Include handles or grips
- Be compact and portable

## Related Directories

- **Pin gauges**: [`../PIN_GAUGES/`](../PIN_GAUGES/)
- **Calibration**: [`../../CALIBRATION/`](../../CALIBRATION/)
- **Inspection procedures**: [`../../SETUP/PROCEDURES/`](../../SETUP/PROCEDURES/)
