# BWB-H2-Hy-E — Model Root

Authoritative root for the AMPEL360-AIR-T **BWB-H2-Hy-E** configuration.

## Path convention
`PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/<TAG>/DOMAINS/<DOMAIN>/SYSTEMS/<XX>/SUBSYSTEMS/<XX-YY>/PLM/CAx/<CAD|CAE|CAO|CAM|CAI|CAV|CAS|CMP>/`

## Rules
- **PLM/CAx only** in leaf `SUBSYSTEMS/*/PLM/CAx/`.
- Flight systems use **INTEGRATION_VIEW.md** and `INTERFACE_MATRIX/`.
- Non-flight helpers (e.g., MGSE) use a **single README.md** only.
- Evidence is **IEF-wrapped** (`*.ief.json`). No raw binaries.

## Index
- **Versions** → [./VERSION/](./VERSION/)
  - **Q100** → [./VERSION/Q100/](./VERSION/Q100/)

## Checklist
- [ ] Paths match convention  
- [ ] Integration artifacts only for flight systems  
- [ ] No PLM/CAx outside `SUBSYSTEMS`  
- [ ] Artifacts are portable (IEF)
