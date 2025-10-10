# INTERFERENCE — Interference Checks

## Purpose

This directory contains interference and clearance check results for the top-level assembly.

## Interference Types

### Hard Interferences
- **Physical overlap**: Components occupy same space
- **Severity**: Critical — must be resolved
- **Action**: Redesign to eliminate overlap

### Soft Interferences
- **Clearance violation**: Components within minimum clearance
- **Severity**: High — should be resolved
- **Action**: Adjust design or review clearance requirements

### Acceptable Interferences
- **Mating features**: Intentional fits (press fit, interference fit)
- **Weld/bond areas**: Intentional overlaps
- **Fastener penetrations**: Holes and fasteners

## Check Process

### Setup
1. Define clearance requirements by component type
2. Set up interference zones and exclusions
3. Configure check parameters (tolerance, zones)
4. Identify acceptable interferences (mating features)

### Execution
1. Run global interference check
2. Review all detected interferences
3. Classify each interference (hard/soft/acceptable)
4. Document findings
5. Create issue list for hard/soft interferences

### Resolution
1. Prioritize by severity
2. Coordinate with affected disciplines
3. Implement design changes
4. Re-run check to verify
5. Update documentation

## Clearance Requirements

### Minimum Clearances
- **Part-to-part**: 2 mm minimum (no contact during operation)
- **Part-to-system**: 5 mm (maintenance access)
- **Part-to-structure**: 3 mm (assembly tolerance)
- **Moving parts**: 10 mm (operational clearance)
- **Thermal growth**: Additional clearance for temperature effects

### Critical Clearances
- **Pressure seals**: No interference allowed
- **Doors/access panels**: Full clearance for operation
- **Systems routing**: Adequate bend radius and service loop
- **Safety-critical**: Double-check and document

## File Formats

- `.pdf` — Interference report with images
- `.xlsx` — Interference list spreadsheet
- `.html` — Interactive interference report
- `.csv` — Data export for tracking

## Naming Convention

```
53-10_INTERFERENCE_<date>_<version>.<ext>
```

Examples:
- `53-10_INTERFERENCE_2024-01-15_v01.pdf`
- `53-10_INTERFERENCE_2024-01-15_v01.xlsx`

## Report Contents

Each report should include:
- **Check date and version**: When and what was checked
- **Tool used**: Software and settings
- **Summary**: Total interferences by type
- **Detailed list**: All interferences found
  - Component 1 and Component 2
  - Interference volume
  - Location (X, Y, Z)
  - Classification (hard/soft/acceptable)
  - Status (open/closed)
  - Action taken
- **Screenshots**: Visual documentation of issues
- **Recommendations**: Suggested corrective actions

## Tracking

Maintain interference log:
- [ ] Interference ID and description
- [ ] Date found
- [ ] Components involved
- [ ] Severity (critical/high/medium/low)
- [ ] Assigned to (responsible engineer)
- [ ] Status (open/in-progress/resolved/verified)
- [ ] Resolution date

## Related Checks

- **Clearance analysis**: [`../VALIDATION/`](../VALIDATION/)
- **Mass properties**: [`../MASS_PROPERTIES/`](../MASS_PROPERTIES/)
