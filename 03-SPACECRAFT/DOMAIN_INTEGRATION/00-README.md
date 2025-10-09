# DOMAIN_INTEGRATION

Domain Integration deliverables for SPACE-T (Space Transport Architecture) products.

## Overview

This directory contains domain integration artifacts for spacecraft systems following the same organizational pattern as AIR-T (aircraft), but adapted for spacecraft systems and STA (Space Transport Architecture) taxonomies.

## Structure

Both product lines use the **same path pattern** for Domain Integration deliverables:

```
DOMAIN_INTEGRATION/PRODUCTS/
└─ AMPEL360-SPACE-T/MODELS/[BWB|PLUS]/VERSION/[Q100|Q10]/
    ├─ 00-README.md
    ├─ [15 DOMAINS]/                # one folder per domain (shared naming)
    │   └─ SYSTEMS/                 # unified (no ZONES/PLATFORM)
    │       └─ <System>/
    │           ├─ INTEGRATION_VIEW.md
    │           ├─ INTERFACE_MATRIX/*.csv
    │           └─ SUBSYSTEMS/<SubSystem>/
    │               └─ PLM/
    │                   ├─ EBOM_LINKS.md
    │                   └─ CAx/ (CAD/CAE/CAO/CAM/CAI/CAV/CAP/CAS/CMP)
    └─ scripts/ (create-domains.sh, validate-structure.sh)
```

## Domain Organization

The 15 domains are shared between aircraft (AIR-T) and spacecraft (SPACE-T):

| Domain Code | Domain Name |
|-------------|-------------|
| **AAA** | Airframes, Aerodynamics, Airworthiness |
| **PPP** | Propulsion & Fuel Systems |
| **MEC** | Mechanical Systems & Modules |
| **LCC** | Linkages, Control & Comms |
| **EDI** | Electronics, Digital & Instruments |
| **EEE** | Electrical, Lights & Start |
| **EER** | Environmental & Remediation |
| **DDD** | Drainage & De-ice |
| **CCC** | Cockpit, Cabin & Cargo |
| **IIS** | Information Systems & IT |
| **LIB** | Logistics, Limits & Servicing |
| **AAP** | Airport/Air-Ops Platforms |
| **CQH** | Cryogenics/Nitrogen/H₂ |
| **IIF** | Industrial Infrastructure |
| **OOO** | OS, Ontologies & Reserved |

## Rules

- **PLM/CAx solo en `SUBSYSTEMS/`** (artefactos reales)
- **SW con su LRU** (en su ATA/host; p.ej. FADEC→ATA-73, IMA partitions→ATA-42)
- **EWIS solo ATA-92** (referenciado vía matrices de interfaz)
- Cada *System* requiere: `INTEGRATION_VIEW.md`, `INTERFACE_MATRIX/*.csv`, y ≥1 `SUBSYSTEMS/*/PLM/CAx/*`

## STA System Sets

Systems and matrices follow STA groupings:

- **A) Structures & Mechanisms:** ch. 06, 50, 51, 52, 53, 55, 56, 57, 66, 94
- **B) Thermal & TPS:** 21, 30
- **C) Power / EPS / Harness:** 24, 39, 49, 97
- **D) Comms & TT&C:** 23, 33, 48
- **E) Navigation, Time & Data Handling:** 31, 34, 41
- **F) Avionics, Flight SW & Databus:** 40, 42, 93
- **G) Control, Autonomy & FDIR:** 22, 44, 45
- **H) ECLSS, Crew & Payload Accommodation:** 25, 35, 36, 37, 38
- **I) Propulsion & Fluids:** 28, 29, 47, 60–61, 70–82, 83–85
- **J) Docking, Sampling & Robotics:** 58, 59
- **K) Environment, Safety & Space Traffic:** 15, 26, 86, 87, 90
- **L) Ground, Integration & Mission Ops:** 07, 10, 16, 32, 46, 92
- **M) Program, Compliance & Records:** 01, 04, 05, 11–14, 17–20, 98–99

## Integration with Configuration Base

Domain integration artifacts link to baseline configurations:
- Spacecraft baselines: [`../CONFIGURATION_BASE/`](../CONFIGURATION_BASE/)
- Configuration Management: [`../../00-PROGRAM/CONFIG_MGMT/`](../../00-PROGRAM/CONFIG_MGMT/)
- Digital Thread: [`../../00-PROGRAM/DIGITAL_THREAD/`](../../00-PROGRAM/DIGITAL_THREAD/)

## Related Documentation

- Main README: [`../../README.md`](../../README.md)
- Spacecraft Overview: [`../00-README.md`](../00-README.md)
- Aircraft Domain Integration: [`../../02-AIRCRAFT/DOMAIN_INTEGRATION/`](../../02-AIRCRAFT/DOMAIN_INTEGRATION/)
