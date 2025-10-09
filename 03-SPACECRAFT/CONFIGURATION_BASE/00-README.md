# CONFIGURATION_BASE

Spacecraft systems configuration baseline organized by STA (Space Transport Architecture) chapter structure.

## Overview

The CONFIGURATION_BASE directory contains the baseline configuration for all spacecraft systems organized according to STA system sets. Each STA chapter represents a specific spacecraft system or subsystem and contains comprehensive configuration data including parameters, baselines, hardware configurations, software baselines, interface control documents, verification artifacts, and change logs.

## Purpose

This structure serves as the single source of truth for:
- System parameter definitions and limits
- Hardware configuration baselines
- Software release baselines
- Interface control documents (ICDs)
- Verification and validation artifacts
- Change history and traceability

## Structure

```
CONFIGURATION_BASE/
├─ 00-README.md                            # This file
├─ 00-COMMON/                              # Shared resources across all STA chapters
│  ├─ RULES.md                             # Configuration rules and guidelines
│  ├─ SCHEMAS/                             # JSON/XML schemas for BASELINE, PARAMS, etc.
│  ├─ TEMPLATES/                           # Standard templates
│  │  ├─ PARAMS.csv
│  │  └─ ICD_TEMPLATE.md
│  └─ GLOBAL_CHANGE_LOG.csv                # Master change log
├─ STA-[XX]_[SYSTEM_NAME]/                 # Individual STA chapters
│  ├─ PARAMS/                              # System parameters and limits
│  ├─ BASELINE/                            # Configuration baselines
│  ├─ HW_CONFIG/                           # Hardware configuration
│  ├─ SW_BASELINE/                         # Software baselines
│  ├─ ICD/                                 # Interface control documents
│  ├─ VERIFICATION/                        # V&V artifacts
│  └─ CHANGE_LOG/                          # Chapter-specific change log
```

### STA System Sets Organization

Systems are organized by functional groups following the STA (Space Transport Architecture) taxonomy:

#### A) Structures & Mechanisms
- ch. 06, 50, 51, 52, 53, 55, 56, 57, 66, 94
- Primary/secondary structure, doors/hatches, deployables, mechanisms, NDI, qualification

#### B) Thermal & TPS
- ch. 21, 30
- Radiators/HX, MLI, heaters, pipes/straps, TPS, sensors, TVAC

#### C) Power / EPS / Harness
- ch. 24, 39, 49, 97
- Generation, storage, PCDU, distribution/protection, harness, EGSE

#### D) Comms & TT&C
- ch. 23, 33, 48
- RF FE, TRX/modems, antennas, CCSDS TM/TC, optical terminals, ground IF

#### E) Navigation, Time & Data Handling
- ch. 31, 34, 41
- Nav sensors, timing, C&DH, I/O, processing/storage, FDIR hooks

#### F) Avionics, Flight SW & Databus
- ch. 40, 42, 93
- OBC, FS, networks (SpW/1553/CAN/IMA), boot/update, sync, HIL/SIL, cyber

#### G) Control, Autonomy & FDIR
- ch. 22, 44, 45
- Control architecture, GNC, allocation, FDIR, health/CBM, redundancy

#### H) ECLSS, Crew & Payload Accommodation
- ch. 25, 35, 36, 37, 38
- Atmosphere, pressure, CO₂/trace, humidity, water/waste, fire

#### I) Propulsion & Fluids
- ch. 28, 29, 47, 60–61, 70–82, 83–85
- Tanks/PMD, pressurize/purge, feed, thrusters, ignition, thermal, TVC, safety/plume

#### J) Docking, Sampling & Robotics
- ch. 58, 59
- Sensing, capture, seals, umbilicals, drives, autonomy, testbeds

#### K) Environment, Safety & Space Traffic
- ch. 15, 26, 86, 87, 90
- Acoustics/vibe, ordnance/hazards, planetary protection, radiation, conjunctions

#### L) Ground, Integration & Mission Ops
- ch. 07, 10, 16, 32, 46, 92
- MGSE/EGSE, I&T, EDL, ground segment, geometry/calibration

#### M) Program, Compliance & Records
- ch. 01, 04, 05, 11–14, 17–20, 98–99
- Governance, plans, compliance, reviews, data/records

## Standards Compliance

All spacecraft configurations follow ECSS standards:
- **ECSS-E**: Engineering standards
- **ECSS-M**: Management standards (ECSS-M-ST-40)
- **ECSS-Q**: Quality assurance standards (ECSS-Q-ST-80)

## Configuration Management

Configuration baselines are managed through:
- **Baselines**: [`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`](../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
- **Changes**: [`00-PROGRAM/CONFIG_MGMT/06-CHANGES/`](../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **CCB**: [`00-PROGRAM/CONFIG_MGMT/05-CCB/`](../../00-PROGRAM/CONFIG_MGMT/05-CCB/)
- **Releases**: [`00-PROGRAM/CONFIG_MGMT/07-RELEASES/`](../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/)

## Related Documentation

- Main README: [`../../README.md`](../../README.md)
- Spacecraft Overview: [`../00-README.md`](../00-README.md)
- Digital Thread: [`../../00-PROGRAM/DIGITAL_THREAD/`](../../00-PROGRAM/DIGITAL_THREAD/)
- Traceability: [`../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/`](../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)
