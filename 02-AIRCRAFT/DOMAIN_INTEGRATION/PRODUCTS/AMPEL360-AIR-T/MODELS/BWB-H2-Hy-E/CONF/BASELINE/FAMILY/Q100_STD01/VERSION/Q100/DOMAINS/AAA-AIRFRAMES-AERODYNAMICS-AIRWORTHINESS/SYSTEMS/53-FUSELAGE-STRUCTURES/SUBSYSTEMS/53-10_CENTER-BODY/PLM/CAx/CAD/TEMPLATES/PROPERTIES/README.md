# PROPERTIES — CAD Metadata and Property Standards

## Purpose

Standardized metadata properties and attributes for CAD files to ensure consistent data management and traceability.

## Property Categories

### File Properties

#### Required Properties (All Files)
- **Part Number**: Unique identifier per part numbering scheme
- **Revision**: Current revision (A, B, C, etc.)
- **Description**: Brief part/assembly description
- **Author**: Designer name
- **Created Date**: File creation date (auto-populated)
- **Modified Date**: Last modification date (auto-populated)
- **Status**: Design status (In-Work, For-Review, Released, Obsolete)

#### Optional Properties
- **Project**: AMPEL360-AIR-T
- **Model**: BWB-H2-Hy-E
- **Version**: Q100
- **System**: 53 FUSELAGE STRUCTURES
- **Subsystem**: 53-10 CENTER-BODY

### Part-Specific Properties

#### Physical Properties
- **Material**: Material specification (e.g., "ALUMINUM 2024-T3")
- **Mass**: Calculated mass (auto-populated from CAD)
- **Volume**: Part volume (auto-populated)
- **Surface Area**: Total surface area (auto-populated)
- **Center of Gravity**: X, Y, Z coordinates

#### Manufacturing Properties
- **Manufacturing Process**: Machined, Sheet Metal, Composite, Forged, Cast
- **Surface Finish**: Surface roughness requirement (Ra value)
- **Heat Treatment**: Heat treatment specification if applicable
- **Special Processes**: Coating, plating, anodizing, etc.

#### Engineering Properties
- **Design Engineer**: Responsible engineer name
- **Checker**: QA checker name
- **Approver**: Approval authority name
- **Design Load Case**: Critical load case for structural parts
- **Safety Factor**: Applied safety factor
- **Criticality**: Critical/Major/Minor component classification

### Assembly-Specific Properties

#### Assembly Information
- **Assembly Level**: Top-Level, Sub-Assembly, Detail Assembly
- **Number of Components**: Component count (auto-populated)
- **Assembly Mass**: Total assembly mass (auto-populated)
- **Assembly Zone**: Location zone (Forward, Center, Aft)

#### Interface Information
- **Interfaces To**: Adjacent systems/assemblies
- **Interface Documents**: Related interface control documents
- **Mate Strategy**: How assembly is constrained

### Drawing-Specific Properties

#### Drawing Information
- **Drawing Number**: Unique drawing identifier
- **Sheet Size**: A4, A3, A1, etc.
- **Sheet Count**: Total number of sheets
- **Scale**: Drawing scale (1:1, 1:2, etc.)
- **Drawing Type**: Part, Assembly, Installation, Schematic

#### Approval Information
- **Drawn By**: Designer name and date
- **Checked By**: Checker name and date
- **Approved By**: Approver name and date
- **Drawing Status**: For-Review, Approved, Released

## Property Templates

### Part Property Template
```
Part Number:      [AUTO - FROM SYSTEM]
Revision:         A
Description:      [USER INPUT - REQUIRED]
Author:           [AUTO - FROM LOGIN]
Created Date:     [AUTO]
Modified Date:    [AUTO]
Status:           In-Work

Material:         [USER INPUT - REQUIRED]
Mass:             [AUTO - CALCULATED]
Manufacturing:    [USER INPUT - REQUIRED]
Surface Finish:   Ra 3.2 (default)

Design Engineer:  [USER INPUT]
Checker:          [PENDING]
Approver:         [PENDING]
Criticality:      [Major/Critical/Minor]
```

### Assembly Property Template
```
Part Number:      [AUTO - FROM SYSTEM]
Revision:         A
Description:      [USER INPUT - REQUIRED]
Author:           [AUTO - FROM LOGIN]
Created Date:     [AUTO]
Modified Date:    [AUTO]
Status:           In-Work

Assembly Level:   [Top/Sub/Detail]
Component Count:  [AUTO - CALCULATED]
Assembly Mass:    [AUTO - CALCULATED]
Assembly Zone:    [Forward/Center/Aft]

Design Engineer:  [USER INPUT]
Checker:          [PENDING]
Approver:         [PENDING]
```

### Drawing Property Template
```
Drawing Number:   [AUTO - FROM SYSTEM]
Sheet Size:       A3
Sheet Count:      1 of 1
Scale:            1:1
Drawing Type:     Part

Drawn By:         [USER INPUT - REQUIRED]
Drawn Date:       [USER INPUT - REQUIRED]
Checked By:       [PENDING]
Checked Date:     [PENDING]
Approved By:      [PENDING]
Approved Date:    [PENDING]
Status:           For-Review
```

## Property Standards by CAD System

### CATIA V5
- Use Properties → Product Properties
- Custom properties tab for IDEALE-specific fields
- Link to ENOVIA/PDM for part numbers
- Mass properties auto-update on save

### Siemens NX
- Use File → Properties
- Customer defaults for IDEALE properties
- Teamcenter integration for part numbering
- Mass properties in modeling preferences

### SOLIDWORKS
- Use File → Properties → Custom
- Property tab builder for templates
- PDM integration for metadata
- Configuration-specific properties

### PTC Creo
- Use File → Prepare → Model Properties
- Parameters for custom properties
- Windchill integration for lifecycle
- Mass properties auto-calculated

## Usage Guidelines

### Property Completion Workflow
1. **On file creation**: Complete required properties immediately
2. **During design**: Update status, mass, and design engineer
3. **At review**: Add checker name and date
4. **At approval**: Add approver name and date
5. **At release**: Change status to "Released"

### Property Validation
- Required properties must be filled before file release
- Part numbers must match numbering scheme
- Revision must match file revision
- Mass properties must be up-to-date
- Status must reflect current lifecycle state

### Property Maintenance
- Update properties with each revision
- Archive old property values in revision history
- Synchronize properties with PDM/PLM system
- Verify properties during design reviews

## Automation

### Auto-Populated Properties
Properties that CAD systems calculate automatically:
- Mass, volume, surface area
- Center of gravity
- Moments of inertia
- Bounding box dimensions
- Component count (assemblies)
- Created/modified dates

### User-Required Properties
Properties that must be manually entered:
- Part number (or selected from PDM)
- Description
- Material
- Manufacturing process
- Design engineer
- Revision reason

### Property Extraction Scripts
See [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) for scripts to:
- Extract properties to CSV/Excel
- Validate property completion
- Sync properties with PDM
- Generate property reports

## Related Directories

- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — File naming standards
- **Parameters**: [`../PARAMETERS/`](../PARAMETERS/) — Design parameter standards
- **BOM**: [`../BOM/`](../BOM/) — Bill of Materials requirements
- **Scripts/Macros**: [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) — Property automation scripts

## References

- PLM system documentation
- Configuration management procedures
- Part numbering scheme: [`/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md`](/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
- Change control procedures: [`/00-PROGRAM/CONFIG_MGMT/01-CHANGE_CONTROL.md`](/00-PROGRAM/CONFIG_MGMT/01-CHANGE_CONTROL.md)
