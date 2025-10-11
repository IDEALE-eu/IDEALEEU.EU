# CAE - Computer-Aided Engineering

## Purpose

This directory contains CAE artifacts including FEA models, analysis results, simulation data, and validation reports.

## File Organization

- Use clear, descriptive filenames
- Include analysis type and revision in filename
- Maintain solver-neutral formats where possible
- Document assumptions and boundary conditions

## Naming Convention

```
{ANALYSIS_TYPE}_{DESCRIPTION}_{REV}.{ext}
```

Example: `FEA_Wing_Attach_Static_R001.nas`

## Standards

- Follow applicable CAE standards for this discipline
- Ensure traceability to requirements and load cases
- Maintain configuration control
- Document mesh quality and convergence

## Typical Content

- **GEOMETRY/** — Simplified geometry for analysis
- **MESH/** — Mesh files and quality reports
- **LOADS/** — Load case definitions
- **CASES/** — Analysis cases and boundary conditions
- **RESULTS/** — Solver output files
- **REPORTS/** — Analysis reports and summaries
- **FEA/** — Finite element analysis models
- **CFD/** — Computational fluid dynamics models
- **COUPLING/** — Multi-physics coupling definitions
- **SCRIPTS/** — Automation and post-processing scripts

---

**Last Updated:** 2025-10-11

