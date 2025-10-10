# DRAWINGS — Technical Drawings

## Purpose

This directory contains fully dimensioned technical drawings with GD&T for all 21-10 radiators and heat exchangers assemblies and parts.

## Content

### Drawing Types
- **Assembly drawings**: Overall assembly views, BOM tables, assembly notes
- **Part drawings**: Detailed part dimensions, GD&T, manufacturing notes
- **Interface drawings**: Interface control documents, mounting patterns
- **Installation drawings**: Installation procedures and sequences

### File Formats
- **PDF**: Primary format for released drawings (mandatory for REL status)
- **DWG**: Native CAD drawing format (optional, for editing)
- **DXF**: Exchange format (when needed for manufacturing)

## Naming Convention

```
21-10_DWG_<type>_<description>__r<NN>__<status>.pdf
```

Examples:
- `21-10_DWG_ASSY_RAD-PANEL-L1__r03__REL.pdf`
- `21-10_DWG_PART_FACESHEET__r02__RVW.pdf`
- `21-10_DWG_INST_COLDPLATE-MOUNT__r01__WIP.pdf`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released (sign-offs must be visible)

## Drawing Standards

### Units
- Primary: millimeters (mm)
- Mass: kilograms (kg)
- Angles: degrees (deg)

### Tolerances
- Default: ISO 2768-mK (document in title block)
- GD&T per ISO 1101
- Critical dimensions: specify individual tolerances

### Title Block Requirements
- Part number / assembly number
- Revision level
- Design approval signature
- Date of last revision
- Material specification (for part drawings)
- Mass properties (calculated from CAD model)
- Company/project logo and information

## Content Requirements

### Assembly Drawings Must Include
- Overall assembly views (isometric, front, side, top)
- Section views showing internal details
- BOM table with all components
- Assembly notes and procedures
- Interface callouts and references to ICDs
- Torque specifications for fasteners
- Special handling requirements

### Part Drawings Must Include
- Multiple orthogonal views (as needed for clarity)
- Section views for complex geometry
- Fully dimensioned with GD&T
- Surface finish callouts (Ra values)
- Material specification
- Manufacturing notes (special processes, coatings)
- Inspection requirements

### GD&T Requirements
- Datum reference frames (A, B, C)
- Form tolerances (flatness, straightness, roundness)
- Orientation tolerances (parallelism, perpendicularity, angularity)
- Location tolerances (position, concentricity, symmetry)
- Profile tolerances (surface profile, line profile)
- Runout tolerances (circular runout, total runout)

## Release Requirements (DoD for REL)

### Mandatory for REL Status
- [ ] PDF format with high resolution (minimum 300 DPI)
- [ ] Sign-offs visible in title block
- [ ] All dimensions and GD&T clearly legible
- [ ] BOM tables match EBOM structure
- [ ] Revision history block populated
- [ ] Material specifications documented
- [ ] Surface finish requirements specified
- [ ] Manufacturing notes included

### Quality Checks
- [ ] All views properly scaled
- [ ] Dimensions do not conflict
- [ ] GD&T properly applied and referenced
- [ ] No missing dimensions for critical features
- [ ] Notes and callouts clear and unambiguous
- [ ] Title block completely filled out

## Interface Specifications

### Critical Interfaces to Document
- **Coldplate flatness**: ≤ 0.05 mm with proper datum reference
- **TIM thickness**: Nominal and tolerance range
- **Port threads/sizes**: Must match ICD for LPHX inlet/outlet
- **Mounting holes**: Pattern, size, and thread specification per 51 standards
- **Keep-out zones**: Document for harness/heaters (97/21-30)
- **Ground/bond points**: Hole class and torque notes per 51 standards

## Manufacturing Notes

### Standard Notes to Include
- Material and heat treatment specifications
- Surface finish requirements
- Coating specifications (reference CAP/coating spec)
- Bonding/welding process references
- Inspection and test requirements
- Special handling or storage requirements

## Revision Control

### Drawing Revisions
- Each revision must be documented in revision block
- Revision letter/number in filename must match title block
- Describe changes made in revision description
- Update date and approval signatures

### Revision History Block
- Revision level
- Date of change
- Description of change
- Approved by (signature or initial)

## Export and Distribution

### Release Process
1. Complete drawing with all details
2. Internal review (WIP → RVW)
3. Sign-offs from design authority
4. Export to PDF with proper naming
5. Place in drawings directory
6. Update EBOM links
7. Set status to REL

### File Management
- Keep only current revision in main directory
- Archive superseded revisions (if archival system exists)
- Maintain link between 3D model and drawing

## Related Directories

- **Assemblies**: [`../assemblies/`](../assemblies/) - 3D assembly models
- **Parts**: [`../parts/`](../parts/) - 3D part models
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - Neutral 3D exports
- **Exports (DXF)**: [`../exports_dxf/`](../exports_dxf/) - Flat pattern exports
- **Templates**: [`../templates/`](../templates/) - Drawing templates and title blocks
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - Engineering BOM links

## Standards References

- **ISO 1101**: Geometrical Product Specifications (GPS) - Geometrical tolerancing
- **ISO 2768**: General tolerances for linear and angular dimensions
- **ASME Y14.5**: Dimensioning and tolerancing
- **ISO 128**: Technical drawings - General principles of presentation

---

**Last Updated**: 2025-10-10
