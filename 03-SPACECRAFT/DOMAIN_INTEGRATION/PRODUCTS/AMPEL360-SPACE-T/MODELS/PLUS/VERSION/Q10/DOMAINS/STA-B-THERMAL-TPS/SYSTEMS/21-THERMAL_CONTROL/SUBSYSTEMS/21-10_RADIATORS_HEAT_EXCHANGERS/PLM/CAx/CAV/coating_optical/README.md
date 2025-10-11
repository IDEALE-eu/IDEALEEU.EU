# COATING_OPTICAL — Coating and Optical Properties Testing

## Purpose

This directory contains optical properties testing data for thermal control coatings, including solar absorptance (α), infrared emittance (ε), and durability testing.

## Contents

- Solar absorptance (α) measurements
- Infrared emittance (ε) measurements
- α/ε ratio calculations
- Spectrophotometer scans
- Coating thickness measurements
- Durability and adhesion test results
- UV exposure test data
- Thermal cycling effects on coatings
- Vendor certification data

## File Naming Convention

```
COATING_<test-type>_<sample-id>_<date>.<ext>
```

Examples:
- `COATING_alpha_epsilon_WC-001_20251011.xlsx`
- `COATING_thickness_map_RAD-SN001_20251012.csv`
- `COATING_UV_durability_WC-005_20251015.pdf`

## Test Objectives

### Optical Properties
Measure and verify:
- Solar absorptance (α): 0.25-0.95 typical range
- Infrared emittance (ε): 0.80-0.95 typical for radiators
- α/ε ratio: Critical for thermal performance
- Angular dependence

### Coating Quality
Verify:
- Thickness within specification (typically ±10%)
- Uniformity across surface
- Adhesion adequate (tape test)
- No defects (pinholes, contamination)

### Durability
Demonstrate:
- UV exposure resistance
- Thermal cycling stability
- Vacuum exposure compatibility
- No degradation over mission life

## Measurement Methods

### Solar Absorptance (α)
- **Method**: Spectrophotometer, 0.3-2.5 μm wavelength
- **Standard**: ASTM E903 or equivalent
- **Calculation**: Weighted average over solar spectrum
- **Incidence Angles**: Normal and representative angles

### Infrared Emittance (ε)
- **Method**: Emissometer or FTIR, 2.5-25 μm wavelength
- **Standard**: ASTM C1371 or equivalent
- **Temperature**: At relevant operating temperatures
- **Calculation**: Hemispherical emittance

### Coating Thickness
- **Method**: Eddy current (non-destructive)
- **Method**: Cross-section microscopy (destructive)
- **Locations**: Multiple points across surface
- **Specification**: Typical 50-150 μm ± 10%

## Witness Coupons

Use witness coupons for:
- Process verification samples
- Coated at same time as flight hardware
- Same substrate material
- Destructive testing without risking flight hardware
- Archive for post-flight comparison

## Acceptance Criteria

Coatings pass if:
- ✅ α within specification ± tolerance
- ✅ ε within specification ± tolerance
- ✅ α/ε ratio meets thermal requirement
- ✅ Thickness within ± 10% of nominal
- ✅ Adhesion passes tape test (no delamination)
- ✅ No visual defects >1mm diameter
- ✅ Uniformity <10% variation across surface

## Durability Testing

### UV Exposure
- Equivalent solar hours (ESH) per mission
- Measure α and ε before and after
- Document any degradation
- Verify acceptable for mission life

### Thermal Cycling
- Hot/cold cycles per mission profile
- Measure α and ε before and after
- Check for cracking, delamination
- Verify stability

### Adhesion Testing
- Cross-hatch tape test per ASTM D3359
- Document before/after photos
- Rating scale 0-5 (5 = best adhesion)
- Minimum acceptable rating per specification

## Data Presentation

For each sample, provide:
- Spectral curves (reflectance vs. wavelength)
- Integrated α and ε values
- α/ε ratio
- Thickness map or profile
- Photos of coating appearance
- Comparison to specification limits

## Related Directories

- **[../procedures/](../procedures/)** — Coating test procedures
- **[../fai/](../fai/)** — First article coating verification
- **[../calibration/](../calibration/)** — Instrument calibration
- **[../reports/](../reports/)** — Coating test reports
- **[../../CAP/](../../CAP/)** — Coating application process

---

**Last Updated**: 2025-10-10
