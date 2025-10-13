# PPP-PROPULSION-FUEL-SYSTEMS — SYSTEMS Overview

This directory contains all ATA systems under the PPP (Propulsion, Fuel Systems) domain for the BWB-H2-Hy-E aircraft configuration.

## Systems Included

### Fuel Systems
- **28-FUEL_(INCL_H2)** — Fuel system including LH2 storage, distribution, and management

### Auxiliary Power
- **49-APU** — Auxiliary Power Unit

### Propeller Systems
- **60-PROPELLER_PRACTICES** — Standards and practices for propeller systems (if applicable)
- **61-PROPELLERS** — Propeller assemblies including blades, hub, and governor (if applicable)

### Powerplant Integration
- **70-POWERPLANT_PRACTICES** — General powerplant installation standards and practices
- **71-POWER_PLANT_(ENGINE_INSTALLATION)** — Engine installation including mounts and interfaces

### Engine Systems
- **72-ENGINE** — Core engine modules, compressor, turbine, fan/EM drive
- **73-ENGINE_FUEL_AND_CONTROL** — FADEC, fuel metering, actuators, and engine protection
- **75-ENGINE_BLEED_AIR** — Bleed air taps, regulation, and distribution
- **78-EXHAUST** — Exhaust ducts, nozzles, and emissions control

### Auxiliary Turbines & Water Injection
- **81-TURBINES_AUX** — Auxiliary turbine systems (if applicable)
- **82-WATER_INJECTION** — Water injection systems (if applicable)

## Structure Convention

Each system follows this structure:
```
{SYSTEM}/
├─ README.md                    # System documentation
├─ INTEGRATION_VIEW.md          # Integration overview
├─ INTERFACE_MATRIX/            # System interface definitions
│  └─ *.csv                     # Interface requirement CSVs
└─ SUBSYSTEMS/                  # All subsystems
   └─ {SUBSYSTEM}/
      ├─ README.md              # Subsystem documentation
      └─ PLM/                   # Engineering artifacts
         ├─ EBOM_LINKS.md       # BOM references
         └─ CAx/                # CAx artifacts by discipline
            ├─ CAD/             # Computer-Aided Design
            ├─ CAE/             # Computer-Aided Engineering
            ├─ CAO/             # Computer-Aided Optimization
            ├─ CAM/             # Computer-Aided Manufacturing
            ├─ CAI/             # Computer-Aided Inspection
            ├─ CAV/             # Computer-Aided Verification
            ├─ CAP/             # Computer-Aided Planning
            ├─ CAS/             # Computer-Aided Simulation
            └─ CMP/             # Computer-Aided Modeling & Prototyping
```

## Domain-Level Interfaces

See `INTERFACE_MATRIX/PPP↔24_26_29_31_34_42_44_71_72_73_75_76_77_78_92_93_94.csv` for cross-domain interface definitions.

## Rules

- **PLM/CAx artifacts** are stored **only** at the subsystem level
- All flight systems must have `INTEGRATION_VIEW.md` and `INTERFACE_MATRIX/`
- Non-flight helpers (e.g., MGSE) use a **single README.md** only
- Evidence is **IEF-wrapped** (`*.ief.json`)

## References

- ATA Spec 100 — Aircraft system codes
- BWB-H2-Hy-E Model Documentation → `../../README.md`
- Domain Configuration → `../domain-config.yaml`
