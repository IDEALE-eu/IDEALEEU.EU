# PRODUCTS — Aircraft Programs

Authoritative root for aircraft product trees.

## Rules
- Use: `PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<TAG>/DOMAINS/<DOMAIN>/SYSTEMS/.../SUBSYSTEMS/...`
- **PLM/CAx only in leaf `SUBSYSTEMS/*/PLM/CAx/`**.
- Naming: UPPERCASE with dashes; codes use underscores when numeric prefixes are present.
- Evidence: only IEF-wrapped artifacts (`*.ief.json`) inside PLM/CAx.

## Structure (example)
```

AMPEL360-AIR-T/
MODELS/BWB-H2-Hy-E/
VERSION/Q100/
DOMAINS/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/
SYSTEMS/<XX-SYSTEM>/
SUBSYSTEMS/<XX-YY_SUBSYSTEM>/
PLM/CAx/<CAD|CAE|CAO|CAM|CAI|CAV|CAS|CMP>/

```

## Index
- **AMPEL360-AIR-T** → [./AMPEL360-AIR-T/](./AMPEL360-AIR-T/)

## Checklist
- [ ] Paths follow the convention above
- [ ] No PLM/CAx outside `SUBSYSTEMS`
- [ ] Interface artifacts live under each `SYSTEMS/<XX>/INTERFACE_MATRIX/` when applicable
- [ ] No raw binaries; only portable evidence
```
