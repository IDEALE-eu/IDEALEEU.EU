# SUBSYSTEM: 32-50_WHEELS_BRAKES_ASSEMBLIES

**Under System:** 32-LANDING-GEAR-SYSTEMS • **Architecture:** BWB-H2-Hy-E • **Domain:** MMM-MECHANICAL-MATERIAL-MODULES

## Purpose

Implements the 32-50_WHEELS_BRAKES_ASSEMBLIES mechanical subsystem with full PLM artifacts.

## Folder Contract

- `PLM/CAx/*` → design / reports / MOCs
- `PLM/EBOM_LINKS.md` → packaging / on & off-board bundles
- `META.json` + `inherit.json` → CAD/CAE/CAM only here

## Rules

- **Verification:** see `README.md` + template provenance
- **ICDs:** see traceability in `INTERFACE_MATRIX`
- **Sourcing:** see `PLM/EBOM_LINKS.md`

## How to Contribute

- Keep SW in its host LRU chapter
- EWIS lives in ATA-92; reference via interfaces
- Update `META.json` with owner & status

## CAx Disciplines

- **CAD**: Mechanical design models
- **CAE**: Engineering analysis (FEA, CFD)
- **CAO**: Optimization studies
- **CAM**: Manufacturing data (NC programs, tooling)
- **CAI**: Installation drawings and procedures
- **CAV**: Validation models and test setups
- **CAP**: Procurement specifications
- **CAS**: Simulation models
- **CMP**: Composite materials data
