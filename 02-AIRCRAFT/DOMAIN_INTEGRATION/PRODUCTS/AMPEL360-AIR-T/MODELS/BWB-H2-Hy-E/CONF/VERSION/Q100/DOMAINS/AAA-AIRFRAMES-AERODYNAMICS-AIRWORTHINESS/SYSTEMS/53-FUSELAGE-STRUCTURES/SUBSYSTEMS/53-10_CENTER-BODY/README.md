# 53-10_CENTER-BODY — README

**Path:** `…/SYSTEMS/53-FUSELAGE-STRUCTURES/SUBSYSTEMS/53-10_CENTER-BODY/`

## Purpose
Define, design, and certify the **center body** of the BWB fuselage. Cover primary and secondary structure, wing-body interfaces, bulkheads, and full PLM/CAx readiness for manufacturing and service.

## Scope
**Includes**
- Frames, stringers, upper/lower skin panels, floors, joints.
- Wing–body fittings, tank/service supports, equipment mounts.
- Discontinuities: cutouts, access, local reinforcements.
- Documentation, models, and tests for 53-10.

**Excludes**
- 53-20 Nose and 53-30 Aft (except interfaces).
- 57 Wings structure.
- 52 Doors and 56 Windows hardware (only integration frames).

## Key interfaces
- **57-WINGS:** wing–body joint, hole patterns, sealants, transferred loads.
- **53-20 / 53-30:** frame/floor continuity, pressure boundary.
- **51-STRUCTURES-GENERAL:** standards, common materials, fasteners.
- **52-DOORS / 56-WINDOWS:** perimeter reinforcements and tolerances.
- **92-EWIS:** routes, corridors, protections.
- **21-THERMAL:** insulation and thermal barriers.

## Deliverables (DoD Q100)
- **CAD:** released PART/ASM, PDF/A drawings, STEP AP242.
- **CAE:** load cases, correlation, margins (strength, buckling, modal).
- **CAO:** variant study and minimal Pareto set.
- **CAM:** manufacturing routes and base tooling.
- **CAI:** signed interface matrix.
- **CAV/CAS:** verification and initial service docs.
- **CMP:** UTCS traceability and linked EBOM.

## Folder structure
- [`PLM/CAx/CAD/`](./PLM/CAx/CAD/)  
  - `MODELS/`, `ASSEMBLIES/`, `DRAWINGS/`, `EXPORTS/{STEP,JT,IGES,DXF}`, `TEMPLATES/`
- [`PLM/CAx/CAE/`](./PLM/CAx/CAE/)  
  - `GEOMETRY/`, `MESH/`, `LOADS/`, `CASES/`, `RESULTS/`, `REPORTS/`
- [`PLM/CAx/CAO/`](./PLM/CAx/CAO/)  
  - `VARIABLES/`, `OBJECTIVES/`, `CONSTRAINTS/`, `SOLVERS/`, `RUNS/`, `RESULTS/`
- [`PLM/CAx/CAM/`](./PLM/CAx/CAM/) — processes, NC, tooling  
- [`PLM/CAx/CAI/`](./PLM/CAx/CAI/) — interface matrix and ICDs  
- [`PLM/CAx/CAV/`](./PLM/CAx/CAV/) — verification and checklists  
- [`PLM/CAx/CAS/`](./PLM/CAx/CAS/) — service and maintenance tasks  
- [`PLM/CAx/CMP/`](./PLM/CAx/CMP/) — planning, reviews, risks  
- `INTERFACE_MATRIX/` — ICDs and references  
- `EBOM_LINKS.md`, `METADATA/`, `STANDARDS/`

## Conventions
- **CAD names**  
  - Parts: `53-10_PART_<NAME>_v##.ext`  
  - Assemblies: `53-10_ASM_<NAME>_v##.ext`  
  - Drawings: `53-10_DWG_<TYPE>_<NAME>_<D####>.pdf`
- **Units:** millimeters. **References:** `FS/WL/BL` and datums `A/B/C`.
- **Export:** STEP **AP242** mandatory; JT for visual reviews.

## RASCI (generic)
- **R:** 53-10 Lead  
- **A:** Chief Airframe  
- **S:** CAD/CAE/CAO/CAM owners  
- **C:** 57, 52, 92, 21  
- **I:** Quality/Certification

## Links
- [PLM/CAx](./PLM/CAx/)  
- [INTERFACE_MATRIX](./INTERFACE_MATRIX/)  
- [EBOM_LINKS.md](./EBOM_LINKS.md)

