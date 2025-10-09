# MASS_PROPERTIES — Mass Properties Analysis

## Purpose

This directory contains mass properties calculations and reports for the top-level assembly.

## Mass Properties

### Calculated Properties
- **Total mass**: Assembly weight (kg or lbs)
- **Center of gravity (CG)**: X, Y, Z coordinates
- **Moments of inertia**: Ixx, Iyy, Izz, Ixy, Ixz, Iyz
- **Component breakdown**: Mass by subsystem
- **Material distribution**: Mass by material type

## Property Sources

### CAD Model
- **Geometry volume**: From 3D solid models
- **Material density**: Assigned material properties
- **Calculated mass**: Volume × density

### Non-Geometric Mass (NGM)
- **Paint/coatings**: Surface area × thickness × density
- **Fasteners**: Count × unit mass
- **Sealants/adhesives**: Estimated mass
- **Fluids**: Operational fluids (hydraulic, fuel residuals)

### Target Mass
- **Budget allocation**: From systems engineering
- **Growth allowance**: Design margin (typically 10-15%)
- **Certification limit**: Maximum allowable mass

## Mass Property Reports

### Report Contents
1. **Summary**
   - Total mass
   - CG location (aircraft coordinates)
   - Comparison to target/budget
   - Status (green/yellow/red)

2. **Breakdown by Component**
   - Part number and description
   - Quantity
   - Unit mass
   - Total mass
   - Percentage of total

3. **Breakdown by Material**
   - Material type
   - Total mass
   - Percentage of total

4. **Moments of Inertia**
   - About aircraft axes
   - About CG
   - Principal axes if required

5. **Non-Geometric Mass**
   - Category (fasteners, paint, etc.)
   - Calculation method
   - Estimated mass

6. **Comparison to Targets**
   - Budget vs. actual
   - Variance and status
   - Trend over time

## File Formats

- `.xlsx` — Mass properties spreadsheet
- `.pdf` — Formal mass properties report
- `.csv` — Data export
- `.txt` — CAD mass properties output

## Naming Convention

```
53-10_MASS-PROPS_<date>_<version>.<ext>
```

Examples:
- `53-10_MASS-PROPS_2024-01-15_v01.xlsx`
- `53-10_MASS-PROPS_2024-01-15_v01.pdf`

## Calculation Process

### Step 1: Prepare Model
- [ ] All components have materials assigned
- [ ] Densities are correct
- [ ] Simplified components have estimated mass
- [ ] Assembly is up to date

### Step 2: Calculate
- [ ] Run CAD mass properties tool
- [ ] Export results
- [ ] Calculate NGM separately
- [ ] Sum total mass

### Step 3: Validate
- [ ] Compare to previous version (reasonable change?)
- [ ] Compare to similar structures (sanity check)
- [ ] Review with structures engineering
- [ ] Check against budget

### Step 4: Document
- [ ] Create report
- [ ] Update mass tracking spreadsheet
- [ ] Flag any issues or concerns
- [ ] Distribute to stakeholders

## Mass Control

### Mass Budget Management
- Track actual vs. budget
- Identify overweight areas
- Prioritize weight reduction efforts
- Document all changes

### Weight Reduction
- Material substitution
- Topology optimization
- Feature elimination
- Design simplification

## Accuracy

### Expected Accuracy
- **CAD geometry**: ±1% (with correct materials)
- **NGM estimates**: ±10-20%
- **Total assembly**: ±2-3% (before production)

### Validation Methods
- Weigh physical mockups
- Weigh qualification hardware
- Compare to similar structures
- Use test data when available

## Related Documents

- **Mass budget**: Systems engineering documentation
- **Material specs**: Material density database
- **BOM**: [`../DOCS/BOM/`](../DOCS/BOM/) — Component list
