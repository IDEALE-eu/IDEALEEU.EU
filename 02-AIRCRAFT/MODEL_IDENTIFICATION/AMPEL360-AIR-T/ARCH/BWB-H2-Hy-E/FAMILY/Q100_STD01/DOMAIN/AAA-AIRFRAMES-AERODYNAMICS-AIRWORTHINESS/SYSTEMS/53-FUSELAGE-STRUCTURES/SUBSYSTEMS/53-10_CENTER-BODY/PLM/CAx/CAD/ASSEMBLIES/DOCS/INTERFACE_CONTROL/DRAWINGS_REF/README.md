# DRAWINGS_REF — Reference Drawings and Documentation

## Purpose

This directory contains reference drawings, sketches, and 2D documentation that support interface control and coordination.

## Content Types

### Interface Drawings
- Interface control drawings
- Installation drawings
- Assembly drawings
- Detail drawings of interface features

### Reference Documentation
- Engineering sketches
- Preliminary layouts
- Coordination drawings
- Redline markups

### Extracted Views
- Section views of interfaces
- Detail views of critical features
- Exploded views
- Installation sequences

## File Formats

- `.pdf` — Released engineering drawings (preferred)
- `.dwg` / `.dxf` — 2D CAD formats
- `.png` / `.jpg` — Raster images for quick reference
- `.svg` — Vector graphics

## Drawing Types

### Formal Engineering Drawings
- Released and approved drawings
- Drawing numbers and revisions
- Title blocks with approvals
- Configuration controlled

### Coordination Drawings
- Working drawings for coordination
- Preliminary layouts
- Interface sketches
- Not configuration controlled

### Installation Drawings
- Assembly sequences
- Installation procedures
- Fastener locations
- Torque specifications

### Interface Detail Drawings
- Interface cross-sections
- Fastener details
- Seal details
- Critical dimensions

## Drawing Standards

### Title Block Information
- Drawing number
- Revision letter/number
- Date and approvals
- Scale and units
- Sheet number (sheet X of Y)

### Drawing Content
- Multiple views as needed
- Dimensions with tolerances
- GD&T callouts
- Material specifications
- Notes and general notes
- Reference drawings

### Dimensioning
- Units clearly specified
- Tolerances per company standard or as specified
- Datum references
- GD&T per ASME Y14.5

## Naming Convention

```
{drawing_type}_{interface}_{sheet}_{rev}.{ext}
```

Examples:
- `ICD_WING-ATTACH_SH01_A.pdf`
- `INSTALL_DOOR-FRAME_SH01_B.pdf`
- `DETAIL_BULKHEAD-INTERFACE_A.pdf`

## Drawing Index

Maintain index of all drawings:
```csv
drawing_number,title,interface,sheets,revision,date,status
53-10-1001,Wing Attachment Interface,Wing-to-body,3,C,2024-01-15,Released
53-10-1002,Door Frame Installation,Door frame,2,B,2024-01-12,Released
```

## Drawing Organization

### By Interface
Organize drawings by interface:
- 53_TO_57_WING/
- 53_TO_52_DOORS/
- 53_TO_30_AFT/
- etc.

### By Type
Or by drawing type:
- INTERFACE_CONTROL/
- INSTALLATION/
- DETAILS/
- ASSEMBLY/

## Drawing Content Requirements

### Interface Control Drawings
- Interface location
- Mating components
- Coordinate system
- Critical dimensions
- Tolerances and GD&T
- Material callouts
- Fastener specifications

### Installation Drawings
- Assembly sequence
- Orientation and positioning
- Fastener locations and types
- Torque specifications
- Sealant application
- Inspection requirements

### Detail Drawings
- Enlarged views
- Section views
- Hidden line removal
- Dimension details
- Tolerance callouts

## Drawing Views

### Standard Views
- Front, Top, Side (orthographic)
- Isometric views
- Section views (indicated)
- Detail views (indicated)

### Special Views
- Auxiliary views
- Broken-out sections
- Partial views
- Rotated views

## Dimensioning Best Practices

### Dimension Placement
- Outside the view
- Between views
- Aligned and grouped
- Clear and uncluttered

### Reference Dimensions
- Shown in parentheses: (100)
- For information only
- Not for manufacturing

### Chain vs. Baseline
- Baseline dimensioning preferred
- Chain dimensioning when needed
- Avoid tolerance stackup

## Notes and Callouts

### General Notes
- Drawing-wide information
- Material specifications
- Finish requirements
- Standards compliance

### Specific Notes
- Feature-specific information
- Flagged with bubbles/flags
- Referenced in views
- Sequential numbering

### Revision Notes
- Changes per revision
- Location and description
- Date and approver

## Drawing Revisions

### Revision Control
- Letter or number system
- Revision history block
- Cloud/highlight changes
- Change description

### Revision Process
1. Engineering change request
2. Drawing update
3. Review and approval
4. Revision letter increment
5. Release notification

## Drawing Distribution

### Internal Distribution
- Design team
- Manufacturing
- Quality assurance
- Configuration management

### External Distribution
- Suppliers
- Partners
- Customer (if required)
- Certification authorities

## Related Documents

Link drawings to related documentation:
- ICDs
- Specifications
- Test procedures
- Work instructions

## Cross-References

- [Interface Control Documents](../ICD/)
- [Models Reference](../MODELS_REF/)
- [CAD Drawings](../../../DRAWINGS/)
- [Assembly Documentation](../)

## Drawing Standards

- **ASME Y14.100**: Engineering Drawing Practices
- **ASME Y14.5**: Dimensioning and Tolerancing
- **ASME Y14.24**: Types and Applications of Engineering Drawings
- **ISO 128**: Technical drawings - General principles of presentation
- **ISO 5457**: Technical product documentation - Sizes and layout of drawing sheets
- **ISO 7200**: Technical product documentation - Data fields in title blocks

## Drawing Software

### CAD Systems
- AutoCAD
- DraftSight
- CATIA Drafting
- NX Drafting
- SolidWorks Drawing

### PDF Tools
- Adobe Acrobat
- PDF readers
- Markup tools
- Comparison tools
