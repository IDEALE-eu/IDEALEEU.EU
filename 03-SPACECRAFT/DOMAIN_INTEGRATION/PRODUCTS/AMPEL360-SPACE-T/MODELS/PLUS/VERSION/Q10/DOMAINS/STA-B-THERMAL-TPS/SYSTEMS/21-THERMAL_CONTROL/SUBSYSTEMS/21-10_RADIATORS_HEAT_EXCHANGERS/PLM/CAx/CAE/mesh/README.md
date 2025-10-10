# MESH — Mesh Files and Quality Reports

## Purpose
Finite element and CFD mesh files, along with mesh quality assessments and convergence studies.

## Contents
- FEM mesh files for structural analysis
- CFD mesh files for fluid flow analysis
- Thermal model mesh files
- Mesh quality reports
- Mesh convergence studies
- Element type documentation

## File Organization
- One subdirectory per model or component
- Include mesh statistics and quality metrics
- Store mesh generation scripts
- Document meshing methodology

## Naming Convention
```
21-10-CAE_mesh_<component>_<type>__r<NN>__<STATUS>.{msh|cas|bdf}
```

Example: `21-10-CAE_mesh_radiator_panel_fem__r02__REL.bdf`

## Mesh Requirements
- Document element types and formulations
- Include mesh size and node count
- Assess element quality metrics
- Perform mesh convergence study
- Document boundary layer requirements (CFD)

## Quality Metrics
- **FEM**: Aspect ratio, warping, skewness, Jacobian
- **CFD**: Skewness, orthogonality, expansion ratio, y+
- **Thermal**: Node spacing, thermal resistance resolution

## Convergence Study
```
Mesh_Refinement/
  ├─ coarse_mesh/ (baseline)
  ├─ medium_mesh/ (2x refinement)
  ├─ fine_mesh/ (4x refinement)
  └─ convergence_results.xlsx
```

## Guidelines
- Document mesh generation software and version
- Include mesh independence verification
- Maintain quality metric thresholds
- Archive mesh with analysis results

---

**Last Updated**: 2025-10-10
