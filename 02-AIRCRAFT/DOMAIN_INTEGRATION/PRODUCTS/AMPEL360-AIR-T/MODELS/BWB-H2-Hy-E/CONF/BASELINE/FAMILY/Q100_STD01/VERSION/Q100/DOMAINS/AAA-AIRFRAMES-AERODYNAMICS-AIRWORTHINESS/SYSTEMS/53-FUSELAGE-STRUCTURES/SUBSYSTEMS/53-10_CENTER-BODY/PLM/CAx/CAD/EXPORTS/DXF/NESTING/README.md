# NESTING — Material Nesting Layouts

## Purpose
DXF files for material nesting layouts and optimization for efficient material utilization.

## Contents
- **[NEST_JOBS/](NEST_JOBS/)** — Nesting job files and layouts
- **[REPORTS/](REPORTS/)** — Nesting efficiency reports and documentation

## Organization
Organize by:
- Material type and thickness
- Cutting method (laser, waterjet, plasma)
- Production batch or order
- Date and nesting job number

## File Naming Convention
```
NEST_<material>_<thickness>_<job-number>_<date>.dxf
```

Examples:
- `NEST_AL2024-T3_2MM_JOB-001_20250110.dxf`
- `NEST_AL7075-T6_3MM_JOB-015_20250110.dxf`
- `NEST_STEEL_1.5MM_JOB-042_20250110.dxf`

## Nesting Information
Document for each nest:
- Material specification
- Sheet size and thickness
- Cutting method
- Nesting efficiency (%)
- Part list and quantities
- Scrap percentage
- Grain direction requirements

## Guidelines
- Maximize material utilization
- Maintain minimum spacing between parts
- Account for cutting kerf width
- Respect material grain direction
- Consider sheet remnants for future use
- Document nesting efficiency

## Related Directories
- **[../PARTS/FLAT_PATTERNS/](../PARTS/FLAT_PATTERNS/)** — Individual part flat patterns
- **[../../../CAM/NESTING/](../../../CAM/NESTING/)** — CAM nesting data
- **[../../../CAM/NC_PROGRAMS/](../../../CAM/NC_PROGRAMS/)** — NC cutting programs

## Best Practices
- Optimize for material efficiency
- Group similar parts when possible
- Account for cutting method constraints
- Label each part clearly in nest
- Document material traceability
- Track scrap and remnants
