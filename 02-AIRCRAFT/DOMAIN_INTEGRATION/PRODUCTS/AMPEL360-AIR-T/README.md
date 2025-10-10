# AMPEL360-AIR-T — Product Root

Authoritative root for the AMPEL360 aircraft program.

## Scope
- Aircraft product tree, all domains and systems.
- Governance: IDEALE.eu, AIR-T rules, IEF artifacts.

## Path convention
`PRODUCTS/AMPEL360-AIR-T/MODELS/<MODEL>/VERSION/<TAG>/DOMAINS/<DOMAIN>/SYSTEMS/<XX>/SUBSYSTEMS/<XX-YY>/PLM/CAx/<CAD|CAE|CAO|CAM|CAI|CAV|CAS|CMP>/`

## Rules
- **PLM/CAx only** in leaf `SUBSYSTEMS/*/PLM/CAx/`.
- Integrated systems use **INTEGRATION_VIEW.md** + `INTERFACE_MATRIX/`.
- Non-flight helpers (e.g., MGSE) use a **single README.md** only.
- Evidence is **IEF-wrapped** (`*.ief.json`). No raw binaries.

## Index
- **Models** → [./MODELS/](./MODELS/)
  - **BWB-H2-Hy-E** → [./MODELS/BWB-H2-Hy-E/](./MODELS/BWB-H2-Hy-E/)
    - **Q100** → [./MODELS/BWB-H2-Hy-E/VERSION/Q100/](./MODELS/BWB-H2-Hy-E/VERSION/Q100/)
      - **Domains** → [./MODELS/BWB-H2-Hy-E/VERSION/Q100/DOMAINS/](./MODELS/BWB-H2-Hy-E/VERSION/Q100/DOMAINS/)

## Checks
- [ ] Paths match convention  
- [ ] No PLM/CAx outside `SUBSYSTEMS`  
- [ ] Integration artifacts only for flight systems  
- [ ] All evidence portable (IEF)
