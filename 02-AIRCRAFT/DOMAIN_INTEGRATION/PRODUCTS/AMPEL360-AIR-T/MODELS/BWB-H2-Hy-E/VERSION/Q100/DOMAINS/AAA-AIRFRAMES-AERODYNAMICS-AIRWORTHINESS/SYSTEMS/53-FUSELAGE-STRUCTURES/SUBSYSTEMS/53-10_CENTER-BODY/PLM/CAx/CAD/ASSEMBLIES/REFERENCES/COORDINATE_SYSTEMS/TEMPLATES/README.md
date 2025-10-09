# TEMPLATES — Coordinate System Templates

## Purpose

This directory contains template files and standard definitions for creating new coordinate systems in the 53-10 Center Body design.

## Contents

### CAD Templates
Template files for various CAD systems:
- CATIA V5/V6 coordinate system parts (`.CATPart`)
- NX/Siemens PLM coordinate system parts (`.prt`)
- SolidWorks coordinate system parts (`.sldprt`)
- Creo coordinate system parts (`.prt`)

### Definition Templates
Standard documentation templates:
- Coordinate system definition form (`.yaml`, `.json`)
- Transformation specification template
- Interface coordinate system ICD template
- Validation checklist template

### Example Files
Reference examples demonstrating proper usage:
- Global coordinate system examples
- Station coordinate system examples
- Local component coordinate system examples
- Interface coordinate system examples
- Complete documentation package examples

## Template Types

### Global System Template
```yaml
name: "TEMPLATE_GLOBAL_CS"
type: "global"
origin: [0.0, 0.0, 0.0]  # mm
axes:
  x: [1.0, 0.0, 0.0]  # direction cosines
  y: [0.0, 1.0, 0.0]
  z: [0.0, 0.0, 1.0]
units:
  length: "mm"
  angle: "degrees"
parent: null
description: "Template for global reference coordinate system"
owner: "Engineering Team"
version: "1.0"
status: "template"
```

### Station System Template
```yaml
name: "TEMPLATE_STATION_CS_FS_XXXX"
type: "station"
station_type: "FS"  # or "WL" or "BL"
station_value: 0.0  # station number
origin: [0.0, 0.0, 0.0]  # relative to parent
axes:
  x: [1.0, 0.0, 0.0]
  y: [0.0, 1.0, 0.0]
  z: [0.0, 0.0, 1.0]
units:
  length: "mm"
  angle: "degrees"
parent: "GLOBAL_AIRCRAFT_BODY"
description: "Template for fuselage station coordinate system"
owner: "Structures Team"
version: "1.0"
status: "template"
```

### Local Component Template
```yaml
name: "TEMPLATE_LOCAL_CS_<COMPONENT>_<ID>"
type: "local"
component_type: "frame"  # or "stringer", "panel", "door"
component_id: "XX"
origin: [0.0, 0.0, 0.0]  # relative to parent
axes:
  x: [1.0, 0.0, 0.0]
  y: [0.0, 1.0, 0.0]
  z: [0.0, 0.0, 1.0]
units:
  length: "mm"
  angle: "degrees"
parent: "STATION_CS_OR_GLOBAL"
transformation_matrix: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
description: "Template for local component coordinate system"
owner: "Detail Design Team"
version: "1.0"
status: "template"
```

### Interface Template
```yaml
name: "TEMPLATE_INTERFACE_CS_<FROM>_TO_<TO>"
type: "interface"
from_system: "53-10"
to_system: "XX-XX"
location: "description"
origin: [0.0, 0.0, 0.0]  # in global coordinates
axes:
  x: [1.0, 0.0, 0.0]
  y: [0.0, 1.0, 0.0]
  z: [0.0, 0.0, 1.0]
tolerance:
  position: 0.1  # mm
  orientation: 0.01  # degrees
units:
  length: "mm"
  angle: "degrees"
parent: "GLOBAL_AIRCRAFT_BODY"
icd_reference: "ICD_53_TO_XX"
description: "Template for interface coordinate system"
owner: "Integration Team"
counterpart_owner: "Counterpart Team"
version: "1.0"
status: "template"
approval_required: true
```

## Using Templates

### Step 1: Select Template
Choose the appropriate template based on coordinate system type:
- Global → Use global system template
- Station → Use station system template (FS/WL/BL)
- Local → Use local component template
- Interface → Use interface template

### Step 2: Customize
Fill in all required fields:
- Replace placeholder names and IDs
- Specify origin location accurately
- Define axes orientation
- Set appropriate tolerances
- Assign owner and approval chain

### Step 3: Validate
Run validation checks:
- Mathematical validation (orthogonality, determinant)
- Naming convention compliance
- Documentation completeness
- Parent-child relationship validity

### Step 4: Implement
Create coordinate system in CAD:
- Import or create using CAD template
- Apply transformation to parent
- Verify placement and orientation
- Save and version control

### Step 5: Document
Complete documentation:
- Definition file (YAML/JSON)
- Transformation specification
- Usage instructions
- Approval signatures

## Naming Rules

Follow the established naming convention:
```
<subsystem>_<type>_CS_<specific>_v<version>.<ext>
```

Where:
- `<subsystem>` = `53-10`
- `<type>` = `REF` (reference) or `INTF` (interface)
- `<specific>` = descriptive identifier
- `<version>` = 2-digit version number (01, 02, ...)

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [Naming Conventions](../METADATA/CONVENTIONS/)
- [Validation Procedures](../VALIDATION/README.md)
- [CAD Standards](../../../TEMPLATES/README.md)

## Standards

- **ISO 10303** (STEP): Coordinate system representation
- **ATA iSpec 2200**: Aircraft coordinate conventions
- **ASME Y14.5**: Dimensioning and tolerancing
- Internal: 53-10 CAD Modeling Standards

---

**Owner**: 53-10 CAD Standards / Integration  
**Status**: Active templates — update with best practices  
**Usage**: Required starting point for all new coordinate systems  
**Maintenance**: Review and update quarterly
