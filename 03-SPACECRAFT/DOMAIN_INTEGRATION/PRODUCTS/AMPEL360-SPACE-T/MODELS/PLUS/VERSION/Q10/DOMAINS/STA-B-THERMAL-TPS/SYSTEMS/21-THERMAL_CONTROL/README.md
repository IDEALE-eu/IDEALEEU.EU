# System 21: THERMAL_CONTROL

## Overview

This system manages all thermal control functions for the AMPEL360-SPACE-T spacecraft, including active and passive thermal management, heat rejection, thermal protection, and temperature monitoring.

## Scope

- Radiators and heat exchangers for heat rejection
- Multi-layer insulation (MLI) for passive thermal control
- Survival heaters and thermostatic controls
- Thermal pipes, heat straps, and fluid loops
- Thermal Protection System (TPS) for re-entry (if applicable)
- Temperature sensors and monitoring instrumentation
- Thermal control algorithms and software
- Thermal vacuum (TVAC) testing and validation

## System Breakdown

### 21-10 Radiators/Heat Exchangers
Primary heat rejection hardware for dissipating excess thermal energy to space.

### 21-20 MLI (Multi-Layer Insulation)
Passive thermal control using multi-layer insulation blankets to minimize heat exchange.

### 21-30 Heaters
Survival heaters and thermostatic controls to maintain minimum operating temperatures.

### 21-40 Pipes/Heat Straps
Thermal transport hardware including heat pipes, heat straps, and coolant loops.

### 21-50 Thermal Protection System
High-temperature protection for re-entry or extreme thermal environments (if applicable to mission).

### 21-60 Temperature Sensors
Temperature measurement instrumentation and monitoring systems.

### 21-70 Thermal Algorithms
Thermal control algorithms, software, and autonomous thermal management logic.

### 21-80 TVAC Testing
Thermal vacuum testing facilities, procedures, and validation campaigns.

## Key Interfaces

- **15 - Environment/Vibration**: Thermal loads and environment definitions
- **24 - Electrical Power**: Power supply for heaters and sensors
- **31 - Data Handling**: Temperature data acquisition and thermal control commands
- **51 - Structures**: Thermal mounting interfaces and conductive paths
- **70 - Thermal Algorithms**: Software interfaces for autonomous control
- **72 - Avionics Cooling**: Equipment thermal management requirements
- **75 - Fluid Systems**: Coolant distribution and thermal transport
- **97 - Harness**: Electrical distribution for sensors and heaters

## References

- [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) - System integration details
- [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) - Interface definitions
- [SUBSYSTEMS/](./SUBSYSTEMS/) - Individual subsystem documentation
- Domain: [STA-B-THERMAL-TPS](../../README.md)

## Standards and Compliance

- ECSS-E-ST-31C: Space engineering - Thermal control
- ECSS-Q-ST-70C: Space product assurance - Materials, mechanical parts and processes
- NASA-STD-7009: Standard for Models and Simulations

---

**Status**: Active Development  
**Last Updated**: 2025-10-10
