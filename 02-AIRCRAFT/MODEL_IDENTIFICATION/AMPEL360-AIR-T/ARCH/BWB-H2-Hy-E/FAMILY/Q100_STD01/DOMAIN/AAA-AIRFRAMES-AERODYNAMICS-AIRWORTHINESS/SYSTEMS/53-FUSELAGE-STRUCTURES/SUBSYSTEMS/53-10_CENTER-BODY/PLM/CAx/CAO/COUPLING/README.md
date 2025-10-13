# COUPLING — CAD/CAE Integration

## Purpose
Manage coupling between optimization, CAD models, and CAE analysis.

## Subdirectories

### [CAD_LINKS/](CAD_LINKS/) — CAD Model Links
Parametric CAD model integration:
- Parametric CAD model references
- Design variable to CAD parameter mappings
- Geometry update scripts
- CAD API interfaces (CATIA, NX, SolidWorks)
- Geometry export formats (STEP, IGES, Parasolid)
- Model regeneration automation

**Purpose**: Enable automated geometry updates during optimization loops

### [CAE_LINKS/](CAE_LINKS/) — CAE Analysis Links
FEA model coupling:
- Mesh update procedures
- Analysis model templates
- Load case application scripts
- Boundary condition mapping
- Material property updates
- Results extraction interfaces

**Purpose**: Automate structural analysis in optimization workflow

## Integration Workflow
1. Optimization algorithm proposes new design
2. CAD_LINKS updates parametric geometry
3. CAE_LINKS regenerates analysis model
4. FEA solver evaluates constraints and objectives
5. Results returned to optimizer
6. Repeat until convergence

## Guidelines
- Maintain robust geometry-to-mesh pipelines
- Validate mesh quality after updates
- Handle geometry failures gracefully
- Document API versions and dependencies
- Test coupling with representative design changes
- Archive successful coupling configurations
- Monitor computational efficiency of coupling
