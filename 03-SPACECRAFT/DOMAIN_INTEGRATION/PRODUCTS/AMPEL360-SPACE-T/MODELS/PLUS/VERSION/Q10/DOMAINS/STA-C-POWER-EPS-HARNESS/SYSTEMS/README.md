# STA-C-POWER-EPS-HARNESS Systems

This directory contains all systems within the Power/EPS/Harness domain integration set.

## Systems Overview

### 24-ELECTRICAL_POWER
Electrical Power System (EPS) providing generation, conditioning, distribution, storage, and protection of electrical power for the spacecraft.

**Key Capabilities:**
- Solar power generation
- Battery energy storage
- Power conditioning and distribution
- Protection and fault isolation
- Power management and control

**Interfaces:** 06, 15, 31, 39, 42, 51, 57, 97

### 39-POWER_CONTROL_PANELS
Power Control Panels providing centralized control, switching, and monitoring of electrical power distribution.

**Key Capabilities:**
- Power switching and control
- Load management
- Fault detection and isolation
- Distribution monitoring
- Remote power control

**Interfaces:** 06, 15, 24, 31, 42, 51, 97

### 49-AUXILIARY_POWER
Auxiliary Power system providing supplementary or alternative power sources for mission-specific requirements.

**Key Capabilities:**
- Fuel cell power generation
- Radioisotope power (RTG)
- Auxiliary power units
- Backup power systems
- Peak power augmentation

**Interfaces:** 06, 15, 24, 31, 39, 42, 51, 97

### 97-HARNESS_EWIS
Harness/EWIS providing all electrical wiring, cables, connectors, and associated hardware for spacecraft electrical connectivity.

**Key Capabilities:**
- Electrical wiring infrastructure
- Power distribution wiring
- Signal and data transmission
- EMI/EMC protection
- Cable routing and installation

**Interfaces:** 06, 15, 24, 31, 39, 42, 51, 57

## Structure Convention

Each system follows the standard structure:

```
<SYSTEM>/
├── README.md                    # System description and navigation
├── INTEGRATION_VIEW.md          # System integration overview
├── INTERFACE_MATRIX/            # Interface definitions
│   └── <SYSTEM>↔<OTHERS>.csv   # CSV format interface matrix
└── SUBSYSTEMS/                  # System subsystems
    └── <XX-YY_SUBSYSTEM>/
        └── PLM/                 # Product Lifecycle Management
            ├── EBOM_LINKS.md    # Engineering BOM references
            └── CAx/             # Engineering tools
                ├── README.md    # CAx directory guide
                ├── CAD/         # Computer-Aided Design
                ├── CAE/         # Computer-Aided Engineering
                ├── CAM/         # Computer-Aided Manufacturing
                ├── CAI/         # Computer-Aided Integration
                ├── CAV/         # Computer-Aided Verification
                ├── CAP/         # Computer-Aided Production
                ├── CAS/         # Computer-Aided Service
                └── CMP/         # Computer-Aided Management & Planning
```

## Domain Rules

1. **PLM/CAx only in SUBSYSTEMS** - Engineering artifacts reside at subsystem level
2. **Interface definitions in CSV** - All interfaces documented in machine-readable format
3. **Integration focus** - Each system has INTEGRATION_VIEW.md describing functional integration
4. **Consistent naming** - Uppercase with dashes, numeric prefixes with underscores

## Navigation

- [⬆️ Back to Domain](../)
- [📋 Domain README](../README.md)

## Quick Links

- [System 24: ELECTRICAL_POWER](./24-ELECTRICAL_POWER/)
- [System 39: POWER_CONTROL_PANELS](./39-POWER_CONTROL_PANELS/)
- [System 49: AUXILIARY_POWER](./49-AUXILIARY_POWER/)
- [System 97: HARNESS_EWIS](./97-HARNESS_EWIS/)

---

**Status**: Structure scaffolded - Ready for engineering artifact population
