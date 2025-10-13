# STACKUPS — Tolerance Stack-Up Analyses

## Purpose

Tolerance stack-up analyses ensuring dimensional compatibility and assembly feasibility for the CENTER-BODY subsystem.

## Content Types

- **1D Stack-Up Analyses** — Linear dimension chains
- **2D Stack-Up Analyses** — Planar tolerance loops
- **3D Stack-Up Analyses** — Complex spatial assemblies
- **Statistical Analyses** — RSS and Monte Carlo methods

## File Formats

- `.pdf` — Stack-up analysis reports
- `.xlsx` — Stack-up calculation spreadsheets
- `.csv` — Tolerance component tables
- `.cetol` / `.3dcs` — 3D tolerance analysis models

## Naming Convention

```
Stackup_{assembly}_{dimension}_v{version}.{ext}
```

Examples:
- `Stackup_wing_attach_gap_v001.pdf`
- `Stackup_floor_beam_height_v002.xlsx`
- `Stackup_bulkhead_to_skin_3D_v001.cetol`

## Cross-References

- [Parent: TOLERANCES](../README.md)
- [GD&T Schemes](../GDNT_SCHEMES/README.md)
- [Master Geometry](../../MASTER_GEOMETRY/REFERENCES/README.md)
- [Interface Definitions](../../INTERFACES/)
- [Mounting Provisions](../../MOUNTING/)

## Stack-Up Methodologies

### Worst-Case Analysis
Maximum variation = Σ(individual tolerances)
- **Use**: Critical safety interfaces
- **Result**: Conservative, expensive
- **Typical margin**: 0% risk

### Root Sum Square (RSS)
Maximum variation = √(Σ(tolerances²))
- **Use**: Non-critical assemblies
- **Assumption**: Normal distribution, independent
- **Typical margin**: 3σ (99.73%)

### Monte Carlo Simulation
Statistical modeling with distribution sampling
- **Use**: Complex assemblies
- **Benefit**: Accounts for correlations
- **Output**: Probability distributions

## Typical Stack-Up Paths

### Critical Interface Gaps
Example: Wing-to-fuselage attachment gap
```
Gap = Wing_Position + Wing_Tolerance 
      - Fuselage_Position - Fuselage_Tolerance
      + Fitting_Clearance + Fitting_Tolerance
      + Thermal_Expansion ± Temperature_Variation
```

### Assembly Sequence Dependencies
- Part positioning tolerances
- Tooling tolerances
- Assembly method variations
- Measurement uncertainties

## Tolerance Components

Each stack-up includes:
| Component | Source | Distribution | Typical Value |
|-----------|--------|--------------|---------------|
| **Part tolerance** | Drawing | Normal (3σ) | ±0.5mm |
| **Assembly tolerance** | Process | Normal (3σ) | ±0.3mm |
| **Thermal expansion** | Material | Uniform | ±0.2mm |
| **Measurement error** | Equipment | Normal (2σ) | ±0.05mm |
| **Tool wear** | Process | Drift | ±0.1mm |

## Stackup Analysis Format

```csv
dimension_id,nominal,tolerance_pos,tolerance_neg,distribution,sensitivity
D1_part,100.0,0.5,-0.5,Normal,+1.0
D2_assy,50.0,0.3,-0.3,Normal,+1.0
D3_thermal,0.0,0.2,-0.2,Uniform,+1.0
D4_total,150.0,0.65,-0.65,RSS,-
```

## Acceptance Criteria

Stack-up must demonstrate:
- **Minimum gap**: ≥0 mm (no interference)
- **Maximum gap**: Within assembly specifications
- **Probability**: ≥99.73% yield (3σ for RSS)
- **Margin**: Safety factor ≥1.2 for critical paths

## Validation Requirements

- Analytical stack-up calculations verified
- 3D CAD model validation (digital mockup)
- Physical mockup verification for critical paths
- Production sampling and measurement
- Continuous improvement (Cpk tracking)

## Documentation Requirements

Each stack-up analysis must include:
1. **Objective**: What dimension is being verified
2. **Method**: Worst-case, RSS, or Monte Carlo
3. **Assumptions**: Distributions, independence
4. **Input tolerances**: All contributing sources
5. **Results**: Min/max/mean values, probabilities
6. **Conclusion**: Pass/fail vs. requirements
7. **Recommendations**: Tolerance adjustments if needed

## Example Stack-Up Report Structure

```
1. OBJECTIVE
   Verify wing attachment bolt hole alignment

2. METHOD
   3D RSS tolerance analysis (CETOL 6σ)

3. INPUTS
   - Wing hole pattern: ±0.2mm (drawing)
   - Fuselage hole pattern: ±0.2mm (drawing)
   - Assembly jig tolerance: ±0.15mm (process)
   - Thermal effects: ±0.1mm (analysis)

4. RESULTS
   - Mean offset: 0.05mm
   - 6σ variation: ±0.38mm
   - Bolt clearance: 0.5mm minimum required
   - Available clearance range: 0.12mm to 0.88mm

5. CONCLUSION
   PASS - 100% probability of assembly success

6. RECOMMENDATIONS
   None - adequate margin maintained
```

## Change Control

Stack-up analysis updates required when:
- Part tolerances change
- Assembly method changes
- New thermal analysis available
- Interface definitions modified

All changes via:
- ECO process [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- Re-analysis and re-validation
- Update to [GD&T schemes](../GDNT_SCHEMES/README.md)
- Notification to affected interface owners
