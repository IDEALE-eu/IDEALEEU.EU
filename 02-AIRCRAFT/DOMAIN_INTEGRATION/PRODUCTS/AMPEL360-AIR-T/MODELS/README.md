# MODELS — Product Configurations

Authoritative roots for AMPEL360-AIR-T product configurations.

## Path convention
`PRODUCTS/AMPEL360-AIR-T/MODELS/<MODEL>/VERSION/<TAG>/DOMAINS/<DOMAIN>/SYSTEMS/<XX>/SUBSYSTEMS/<XX-YY>/PLM/CAx/<CAD|CAE|CAO|CAM|CAI|CAV|CAS|CMP>/`

## Naming
- **MODEL**: uppercase; hyphenated descriptor allowed (e.g., `BWB-H2-Hy-E`).
- **VERSION/<TAG>**: program tag (e.g., `Q100`). One tag per frozen baseline.

## Rules
- Integration artifacts only under `SYSTEMS/<XX>/` (use `INTEGRATION_VIEW.md` and `INTERFACE_MATRIX/`).
- **PLM/CAx only** in leaf `SUBSYSTEMS/*/PLM/CAx/`.
- Evidence is IEF-wrapped (`*.ief.json`). No raw binaries.

## Models
- **BWB-H2-Hy-E** → [./BWB-H2-Hy-E/](./BWB-H2-Hy-E/)

## Checklist (new model)
- [ ] Create `MODELS/<MODEL>/VERSION/<TAG>/DOMAINS/`
- [ ] Add domain trees and system interface matrices
- [ ] Ensure PLM/CAx appears only in leaf subsystems
- [ ] Add CI metadata if required by program
