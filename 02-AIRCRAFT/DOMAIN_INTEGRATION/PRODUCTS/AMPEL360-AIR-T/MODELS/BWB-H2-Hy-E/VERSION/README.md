# VERSION — Baselines and Tags

Authoritative roots for **BWB-H2-Hy-E** baselines of AMPEL360-AIR-T.

## Rules
- One folder per **tag** (frozen baseline), e.g. `Q100`.
- Changes only via **ECR/ECO**; new tag for each approved baseline.
- No engineering files at this level.
- Structure under each tag:
  `DOMAINS/<DOMAIN>/SYSTEMS/<XX>/SUBSYSTEMS/<XX-YY>/PLM/CAx/<CAD|CAE|CAO|CAM|CAI|CAV|CAS|CMP>/`
- **PLM/CAx only** in leaf `SUBSYSTEMS/*/PLM/CAx/`.
- Flight systems: `INTEGRATION_VIEW.md` + `INTERFACE_MATRIX/`.
- Non-flight helpers (e.g., MGSE): single `README.md` only.
- Evidence must be IEF-wrapped (`*.ief.json`). No raw binaries.

## Index
- **Q100** → [./Q100/](./Q100/)

## Checklist (new tag)
- [ ] Create `VERSION/<TAG>/DOMAINS/`
- [ ] Add domain trees and system interface matrices
- [ ] Enforce PLM/CAx only in leaf subsystems
- [ ] Run CI gates (schema, BREX, IEF)
