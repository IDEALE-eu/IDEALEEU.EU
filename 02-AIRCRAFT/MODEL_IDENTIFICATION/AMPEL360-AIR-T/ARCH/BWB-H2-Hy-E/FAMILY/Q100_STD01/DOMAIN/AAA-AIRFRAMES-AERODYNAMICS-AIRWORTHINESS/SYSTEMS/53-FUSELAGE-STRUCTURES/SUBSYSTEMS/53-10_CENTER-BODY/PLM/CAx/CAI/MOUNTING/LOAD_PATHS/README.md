# LOAD_PATHS — Load Transfer Paths and Structural Analysis

## Purpose

Documentation of load transfer paths through the CENTER-BODY structure, including structural analysis models, load distributions, and stress analysis results.

## Content Types

- **Load Path Diagrams** — Schematic representations of load flows
- **FEA Models** — Finite element analysis models and results
- **Load Distribution Data** — Force and moment distributions
- **Stress Analysis Reports** — Margin of safety calculations

## File Formats

- `.pdf` — Load path reports and analysis summaries
- `.step` — FEA model geometry
- `.bdf` / `.inp` — FEA input decks (Nastran, Abaqus)
- `.op2` / `.odb` — FEA results files
- `.csv` — Load distribution tables
- `.xlsx` — Margin of safety spreadsheets

## Naming Convention

```
LoadPath_{case}_{analysis_type}_v{version}.{ext}
```

Examples:
- `LoadPath_max_gust_global_FEA_v001.pdf`
- `LoadPath_landing_local_analysis_v002.xlsx`
- `LoadPath_engine_failure_diagram_v001.pdf`

## Cross-References

- [Parent: MOUNTING](../README.md)
- [Hardpoints](../HARDPOINTS/README.md)
- [Fastener Maps](../FASTENER_MAPS/README.md)
- [Interface Definitions](../../INTERFACES/)
- [Master Geometry](../../MASTER_GEOMETRY/REFERENCES/README.md)

## Load Case Categories

### Flight Loads
- Maximum vertical gust (+)
- Maximum vertical gust (-)
- Maximum lateral gust
- Maximum pitch maneuver
- Maximum roll maneuver
- Maximum yaw maneuver

### Ground Loads
- Hard landing (maximum vertical)
- Braking maximum
- Jacking and towing
- Ground handling

### Limit Load Conditions
Critical load combinations per CS-25:
1. Wing bending + torsion
2. Empennage loads
3. Engine thrust/side loads
4. Pressurization loads
5. Landing gear reactions

## Load Distribution Format

```csv
load_case_id,location_id,Fx_kN,Fy_kN,Fz_kN,Mx_kNm,My_kNm,Mz_kNm,margin_of_safety
LC-001,HP_fwd_001,125.5,45.2,98.7,15.3,22.1,8.4,0.25
LC-001,HP_center_005,85.3,22.1,105.2,8.9,18.5,12.3,0.42
```

## FEA Model Requirements

All FEA models must include:
- **Geometry**: Accurate representation of structure
- **Material Properties**: Temperature-dependent if required
- **Boundary Conditions**: Clearly defined constraints
- **Load Application**: Correct load introduction
- **Mesh Quality**: Validated element quality
- **Results Validation**: Comparison with hand calculations

## Margin of Safety Calculation

Standard MS calculation:
```
MS = (Allowable / Applied) - 1.0

Where:
- MS ≥ 0.0 is acceptable
- MS < 0.0 requires redesign
- Ultimate factor of safety = 1.5
```

## Analysis Types

| Analysis | Purpose | Tool | Frequency |
|----------|---------|------|-----------|
| **Global FEA** | Overall load distribution | Nastran | Major design changes |
| **Local FEA** | Detail stress analysis | Abaqus | All critical details |
| **Hand Calc** | Simple load paths | Excel/MathCAD | All fastener joints |
| **Fatigue** | Life prediction | nCode/FE-Safe | Critical locations |

## Validation Requirements

- Global FEA validation with strain gauge data
- Local FEA validation with closed-form solutions
- Margin of safety ≥ 0.0 for all ultimate loads
- Fatigue life ≥ design service goal (DSG)
- Damage tolerance analysis for critical structures

## Documentation Requirements

Each load path analysis must include:
1. Load case description and justification
2. FEA model description (elements, BC, loads)
3. Material properties and allowables
4. Results summary (plots, tables)
5. Margin of safety calculations
6. Conclusions and recommendations

## Change Control

Load path modifications require:
- Structural analysis re-validation
- ECO via [CHANGE_CONTROL/ECO](../../CHANGE_CONTROL/ECO/README.md)
- [CDR review](../../REVIEWS/CDR/README.md) for major changes
- Update to affected [Interface Definitions](../../INTERFACES/)
- Stress report update and re-approval
