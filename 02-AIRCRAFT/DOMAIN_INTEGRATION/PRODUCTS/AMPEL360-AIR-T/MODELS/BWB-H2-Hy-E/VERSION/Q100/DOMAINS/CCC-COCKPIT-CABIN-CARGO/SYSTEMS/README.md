# CCC-COCKPIT-CABIN-CARGO SYSTEMS

## Overview
This directory contains all systems for the CCC (Cockpit-Cabin-Cargo) domain organized according to ATA specifications.

## Systems Included

### 11-PLACARDS_MARKINGS
Safety placards, markings, and signage throughout the aircraft including cockpit, cabin, cargo, emergency exits, and photoluminescent escape path markings.

### 25-EQUIPMENT_FURNISHINGS
Cabin equipment and furnishings including passenger and cockpit seats, galleys, lavatories, partitions, overhead bins, floor coverings, emergency equipment stowage, and crew rest areas.

### 35-OXYGEN
Oxygen systems including flight crew fixed oxygen, passenger drop-down masks, storage cylinders, distribution lines, portable oxygen equipment, and monitoring sensors.

### 43-CABIN_SYSTEMS
Cabin systems including in-flight entertainment (IFE), connectivity, public address, cabin lighting (general and emergency), passenger service units (PSU), seat power outlets, cabin air quality sensors, and CCTV monitoring.

### 44-CABIN_CONTROL
Cabin management system (CMS) including core controllers, attendant panels, lighting control, seat power control, PA routing, ECS integration, door inhibit interlocks, and diagnostics.

### 50-CARGO_LOAD_SYSTEMS
Cargo compartments and load systems including liners, fire panels, roller tracks, locks, tie-downs, weight/CG sensing, cargo indications, and bulk cargo equipment.

### 58-FLT_COMP_EQUIP
Flight compartment equipment.

### 59-FLT_COMP_FURNISHINGS
Flight compartment furnishings.

## Interface Matrix
See [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for detailed interface specifications between CCC systems and other aircraft systems (ATA-24, 31, 42, 44, 50, 92, 93, 97).

## Structure Convention
- Each system has an INTEGRATION_VIEW.md describing functional integration
- Each system has an INTERFACE_MATRIX/ directory with CSV files documenting interfaces
- Each system has a SUBSYSTEMS/ directory containing detailed subsystem components
- PLM/CAx artifacts (CAD, CAE, CAO, CAI, CAM, CAV, CAP, CAS, CMP) are stored **only** at the subsystem level

## Related Documents
- [Domain README](../README.md)
- [Q100 Version Overview](../../README.md)
