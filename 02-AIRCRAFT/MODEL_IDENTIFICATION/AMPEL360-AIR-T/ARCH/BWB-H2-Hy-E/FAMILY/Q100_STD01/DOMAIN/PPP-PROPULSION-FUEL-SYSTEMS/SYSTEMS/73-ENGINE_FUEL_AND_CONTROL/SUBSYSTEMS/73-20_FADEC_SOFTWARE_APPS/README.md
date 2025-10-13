# SUBSYSTEM: 73-20_FADEC_SOFTWARE_APPS

**Under System:** 73-ENGINE_FUEL_AND_CONTROL • **Architecture:** BWB-H2-Hy-E • **Domain:** PPP-PROPULSION-FUEL-SYSTEMS

## Purpose

Implements the sub-assembly with full PLM artifacts.

## Folder Contract

- `PLM/CAx/*` → design / reports / MOCs
- `PLM/EBOM_LINKS.md` → packaging / on & off-board bundles
- `META.json` + `inherit.json` → CAD/CAE/CAM only here

## Rules

- **Verification:** see `README.md` + template provenance
- Contribute following CM: ECR → ECO → baselines + ICDs → *.
- Add docs & tests before models or code.

> Owner: Domain Lead • Status: scaffold • Year: 2025
