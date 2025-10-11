# BURST — Burst Pressure Testing

## Purpose

This directory contains burst test data for witness samples, demonstrating ultimate pressure capability and safety factors.

## Contents

- Pressure vs. time curves to failure
- Burst pressure values
- Failure mode documentation
- Photos of burst location and failure
- Stress analysis correlation
- Safety factor verification

## File Naming Convention

```
BURST_<part-id>_<date>_<witness>.<ext>
```

Examples:
- `BURST_RAD-PANEL-W01_20251011_witness.csv`
- `BURST_TUBE-W003_20251012_failure_photos.pdf`
- `BURST_JOINT-W02_20251015_analysis.xlsx`

## Test Purpose

Burst testing validates:
- Design safety factor (typically 2.0× MEOP or higher)
- Failure mode and location
- Ultimate pressure capability
- Margin to operating pressure

## Test Requirements

### Witness Samples
- Representative of flight hardware design
- Same materials and processes
- Same weld/joint configurations
- Traceability to flight lot

### Safety Factor Verification
- Burst pressure ≥ 2.0× MEOP (typical)
- Or per design requirement
- Statistical analysis if multiple samples

## Test Procedure

### Pre-Test
1. Inspect witness sample
2. Document dimensions and condition
3. Install pressure instrumentation
4. Set up high-speed camera (optional)
5. Install in blast containment

### Pressurization
1. Pressurize gradually to MEOP
2. Continue pressurization beyond MEOP
3. Monitor for first signs of yield
4. Continue to burst
5. Record burst pressure

### Post-Test
1. Depressurize safely
2. Remove sample from containment
3. Document failure mode
4. Photograph failure location
5. Perform failure analysis

## Data Collection

Record:
- Pressure vs. time to burst
- Burst pressure (peak pressure reached)
- Failure mode (weld, tube, joint, etc.)
- Failure location
- Visual appearance of failure
- Ductile vs. brittle failure characteristics

## Failure Mode Analysis

Document:
- **Failure Location**: Weld, base metal, joint, fitting
- **Failure Type**: Ductile tear, brittle fracture, leak-before-burst
- **Failure Orientation**: Longitudinal, circumferential
- **Photos**: Multiple angles of failure
- **Metallurgical Analysis**: If required for root cause

## Safety Factor Calculation

```
Safety Factor = Burst Pressure / MEOP
```

Verify:
- ✅ Safety factor ≥ 2.0 (or per requirement)
- ✅ Failure mode acceptable (ductile preferred)
- ✅ Margin adequate for flight qualification

## Safety Requirements

Burst testing requires:
- ⚠️ **Blast containment** or safety enclosure
- 🚫 **No personnel** in blast radius
- 📹 **Remote monitoring** mandatory
- 🔊 **Acoustic monitoring** for failure detection
- 🛡️ **Fragment containment** verified

## Test Report Content

Burst test report includes:
- Witness sample identification and traceability
- Test setup and instrumentation
- Pressure-time curve
- Burst pressure value
- Safety factor calculation
- Failure mode description
- Photos of failure
- Comparison to design analysis

## Related Directories

- **[../proof/](../proof/)** — Proof pressure testing
- **[../../procedures/](../../procedures/)** — Burst test procedures
- **[../../reports/](../../reports/)** — Test reports
- **[../../../CAE/](../../../CAE/)** — Stress analysis

---

**Last Updated**: 2025-10-10
