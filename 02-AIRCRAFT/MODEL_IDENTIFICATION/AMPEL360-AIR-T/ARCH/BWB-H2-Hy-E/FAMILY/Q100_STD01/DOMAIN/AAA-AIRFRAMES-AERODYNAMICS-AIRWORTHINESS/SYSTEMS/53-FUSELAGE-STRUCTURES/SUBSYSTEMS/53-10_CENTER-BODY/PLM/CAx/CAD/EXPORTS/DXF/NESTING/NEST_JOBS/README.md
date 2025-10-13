# NEST_JOBS — Nesting Job Files

## Purpose
DXF nesting layouts showing optimized part placement on material sheets.

## Contents
- Nested part layouts on material sheets
- Part identification labels
- Material sheet boundaries
- Cutting paths and sequences
- Scrap areas and remnant zones
- Grain direction indicators

## Nesting Job Information
Each nest job includes:
- Job number and date
- Material specification and thickness
- Sheet dimensions
- List of parts and quantities
- Nesting efficiency percentage
- Total parts count
- Estimated cutting time

## Layer Structure
**Standard layers**:
- **SHEET_BOUNDARY**: Material sheet outline
- **CUTTING**: Part cutting paths
- **LABELS**: Part identification labels
- **SCRAP**: Scrap and remnant areas
- **GRAIN**: Material grain direction
- **SEQUENCE**: Cutting sequence numbers
- **TEXT**: Job information and notes

## Nesting Parameters
Document:
- **Spacing**: Minimum part spacing
- **Kerf width**: Cutting tool kerf
- **Edge margin**: Distance from sheet edge
- **Grain alignment**: Parts requiring specific grain direction
- **Nest efficiency**: Percentage of material used
- **Common line cutting**: Shared cutting paths

## File Naming
```
NEST-JOB_<material>_<thickness>_<job-number>_<date>.dxf
```

Examples:
- `NEST-JOB_AL2024_2MM_001_20250110.dxf`
- `NEST-JOB_AL7075_3MM_042_20250110.dxf`
- `NEST-JOB_STEEL_1.5MM_105_20250110.dxf`

## Nesting Software
Common nesting tools:
- SigmaNEST
- Lantek
- Alma CAM
- ProNest
- TruTops Boost
- CAMduct (for HVAC)

## Manufacturing Considerations
- Minimize material waste
- Optimize cutting path for speed
- Account for machine constraints
- Consider part priority and sequencing
- Plan for material remnant reuse
- Verify grain direction requirements

## Related Directories
- **[../REPORTS/](../REPORTS/)** — Nesting reports and efficiency data
- **[../../PARTS/FLAT_PATTERNS/](../../PARTS/FLAT_PATTERNS/)** — Source flat patterns
- **[../../../../CAM/NC_PROGRAMS/TRIMMING_ROUTING/](../../../../CAM/NC_PROGRAMS/TRIMMING_ROUTING/)** — NC cutting programs

## Quality Control
Before releasing nest:
- [ ] All parts present and correctly oriented
- [ ] Part spacing meets requirements
- [ ] Grain direction respected
- [ ] Labels clear and readable
- [ ] Cutting paths closed and clean
- [ ] Material utilization optimized
- [ ] Job information complete

## Traceability
Document:
- Material batch/lot number
- Sheet serial number (if applicable)
- Cutting date and operator
- Post-cut inspection results
- Part routing after cutting
