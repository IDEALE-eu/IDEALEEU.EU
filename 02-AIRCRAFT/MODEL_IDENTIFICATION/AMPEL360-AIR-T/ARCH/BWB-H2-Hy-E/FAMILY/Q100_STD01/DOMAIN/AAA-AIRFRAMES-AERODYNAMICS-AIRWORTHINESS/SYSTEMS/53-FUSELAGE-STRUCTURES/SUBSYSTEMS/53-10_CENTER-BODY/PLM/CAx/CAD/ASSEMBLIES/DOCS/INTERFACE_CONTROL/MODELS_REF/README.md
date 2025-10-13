# MODELS_REF — Reference Models and Geometry

## Purpose

This directory contains reference CAD models, master geometry definitions, and interface geometry used for coordination and verification.

## Content Types

### Reference Geometry
- Master interface surfaces
- Control geometry
- Reference planes and axes
- Coordinate system definitions
- Critical dimensions

### Interface Models
- Simplified interface geometry
- Mating surface definitions
- Envelope models
- Clearance models
- Installation models

### Reference Models
- As-designed interface models
- Released baseline geometry
- Configuration-controlled models
- Archive of previous versions

## File Formats

### 3D Model Formats
- `.step` — Neutral CAD format (preferred)
- `.iges` — Legacy neutral format
- `.jt` — Lightweight visualization
- `.stl` — Mesh for checking
- `.prt` / `.sldprt` / `.catpart` — Native CAD

### Documentation Formats
- `.pdf` — Model documentation
- `.csv` — Model index and metadata
- `.json` — Model metadata and properties

## Model Types

### Master Geometry
- **Control Surfaces**: Defining geometry for interfaces
- **Datum Features**: Reference datums and tooling points
- **Coordinate Systems**: Interface coordinate frames
- **Critical Dimensions**: Key interface dimensions

### Envelope Models
- **Maximum Envelope**: Largest allowable boundary
- **Nominal Envelope**: As-designed size
- **Clearance Envelope**: Including tolerances
- **Interference Check Models**: Simplified for checking

### Interface Models
- **Mating Surfaces**: Exact interface geometry
- **Mounting Provisions**: Hole patterns, fasteners
- **Clearance Models**: For assembly verification
- **Installation Models**: Assembly sequence models

## Model Management

### Version Control
- Configuration management
- Released vs. working versions
- Change tracking
- Effectivity

### Metadata
- Model identification
- Creation date and author
- Software and version
- Units and scale
- Coordinate system
- Approval status

### Model Index
```csv
model_id,filename,description,version,date,status,owner,coord_system
REF-001,wing_attach_interface_v003.step,Wing attachment interface,3,2024-01-15,Released,J.Smith,BCS
REF-002,door_frame_envelope_v002.step,Door frame clearance envelope,2,2024-01-10,Released,A.Jones,BCS
```

## Naming Convention

```
{interface}_{type}_v{version}.{ext}
```

Examples:
- `wing_attach_interface_v003.step`
- `bulkhead_envelope_v002.step`
- `door_frame_mounting_v001.step`

## Model Characteristics

### Geometry Quality
- Clean surfaces (no gaps or overlaps)
- Properly trimmed edges
- Accurate dimensions
- Proper topology

### Simplification Level
- **Level 1**: Full detail
- **Level 2**: Medium detail (interfaces preserved)
- **Level 3**: Simplified (envelopes only)
- **Level 4**: Minimal (bounding boxes)

### Coordinate System
- All models referenced to aircraft body coordinate system (BCS)
- Local coordinate systems documented
- Transformation matrices provided

## Model Usage

### Design Coordination
- Interface checking
- Clearance verification
- Fit analysis
- Assembly planning

### Analysis
- FEA boundary conditions
- Load application points
- Constraint locations
- Contact surfaces

### Manufacturing
- Tooling design reference
- Fixture design
- Inspection planning
- Quality control

### Documentation
- Drawing references
- ICD illustrations
- Assembly instructions
- Maintenance manuals

## Quality Requirements

### Model Validation
- Dimension verification
- Coordinate system check
- File integrity check
- Compatibility testing

### Model Standards
- Units: Millimeters (preferred) or inches
- Coordinate system: Right-hand rule
- Modeling approach: Solid modeling preferred
- Layer/feature naming: Consistent convention

## Model Exchange

### Export Requirements
- STEP AP203 or AP214
- Single file per interface
- Include coordinate system
- Verify import in neutral viewer

### Import Verification
- Dimension check (3 critical dimensions minimum)
- Coordinate system verification
- Visual inspection
- Clearance checks

## Baseline Management

### Release Process
1. Model review and approval
2. Version assignment
3. Metadata creation
4. File archiving
5. Distribution notification

### Change Control
- Engineering change request
- Impact analysis
- Approval process
- Model update
- Re-release with new version

## Cross-References

- [Interface Control Documents](../ICD/)
- [Datums and Coordinates](../DATUMS_COORDS/)
- [Assembly Models](../../TOP_LEVEL/)
- [CAD Exports](../../../EXPORTS/)

## Tools and Software

### CAD Systems
- CATIA V5/V6
- Siemens NX
- SolidWorks
- Creo (Pro/E)

### Viewers
- 3DVIA Composer
- Siemens JT2Go
- FreeCAD
- Online STEP viewers

## Standards

- **ISO 10303 (STEP)**: Product data representation and exchange
- **ASME Y14.41**: Digital product definition data practices
- **ISO 16792**: Technical product documentation
- **AIA NAS 3000**: Coordinate system standards
