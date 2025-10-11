# MEC-MECHANICAL-SYSTEMS-MODULES — SYSTEMS

## Overview

This directory contains all mechanical systems for the AMPEL360-AIR-T BWB-H2-Hy-E aircraft, organized by ATA chapter.

## Systems Structure

Each system follows the standard hierarchy:
- **INTEGRATION_VIEW.md**: Functional integration overview
- **INTERFACE_MATRIX/**: CSV files with interface definitions
- **SUBSYSTEMS/**: Individual subsystems with PLM/CAx artifacts

## ATA Chapters in MEC Domain

- **27-FLIGHT_CONTROLS**: Primary/secondary flight control surfaces and actuators
- **29-HYDRAULIC_POWER**: Hydraulic power generation and distribution
- **32-LANDING_GEAR_SYSTEMS**: Landing gear assemblies and retraction systems
- **36-PNEUMATIC**: Pneumatic power sources and distribution
- **79-OIL_LUBRICATION**: Lubrication systems (MEC primary, PPP secondary)
- **MEC-90_PROCEDURES_TRAINING**: SOPs and training modules for mechanical systems

## PLM Convention

> PLM & CAx **inside each subsystem** only

### CSV Use Everywhere:

```csv
from_ata,to_ata,interface,signal_or_medium,protocol/spec,notes
```

## Compliance

- **ICDs:** see `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Baselines & Changes:** `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`

## Integration with Other Domains

The INTERFACE_MATRIX at domain level defines cross-domain interfaces:
- MEC ↔ EEE (Electrical power for actuators)
- MEC ↔ DDD (Drainage systems)
- MEC ↔ PPP (Engine-driven hydraulics)
- MEC ↔ LCC (Control linkages)
- MEC ↔ EDI (Position feedback sensors)
- And others per MEC↔08_21_22_24_26_28_31_32_34_42_44_53_57_71_72_92_93.csv
