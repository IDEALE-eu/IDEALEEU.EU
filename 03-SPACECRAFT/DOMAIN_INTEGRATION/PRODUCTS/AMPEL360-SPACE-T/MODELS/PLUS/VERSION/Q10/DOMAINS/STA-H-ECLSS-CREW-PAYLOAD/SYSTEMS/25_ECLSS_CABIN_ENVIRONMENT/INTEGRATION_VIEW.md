# 25_ECLSS_CABIN_ENVIRONMENT — Integration View

## Overview
The Environmental Control and Life Support System (ECLSS) provides a habitable environment for crew and payload accommodation. This system integrates atmosphere control, pressure regulation, CO₂ and trace gas removal, humidity management, water/waste systems, fire suppression, environmental sensors, control interfaces, and operations/maintenance.

## Functional Integration
The ECLSS integrates with multiple spacecraft systems:
- **STA-06**: Dimensional interfaces and mounting locations
- **STA-15**: Environmental safety coordination
- **STA-21**: Thermal management for ECLSS components
- **STA-24**: Power distribution to ECLSS equipment
- **STA-26**: Fire suppression system interfaces
- **STA-33**: Communication of environmental data
- **STA-40**: Avionics integration for control
- **STA-42**: Software control interfaces
- **STA-51**: Structural mounting and support
- **STA-93**: Data bus connectivity
- **STA-97**: Electrical harness distribution

## Subsystem Breakdown
- **25-10**: Atmosphere Control
- **25-20**: Pressure Regulation (formerly Ch. 35)
- **25-30**: CO₂ and Trace Gas Removal (formerly Ch. 36)
- **25-40**: Humidity Management (formerly Ch. 37)
- **25-50**: Water/Waste System (formerly Ch. 38)
- **25-60**: Fire Suppression Interfaces (with Ch. 26)
- **25-70**: Environmental Sensors
- **25-80**: Control Interfaces (with Ch. 42)
- **25-90**: Operations and Maintenance

## Dependencies
- Requires continuous power from STA-24
- Interfaces with thermal control (STA-21) for temperature management
- Depends on data handling (STA-42) for monitoring and control
- Coordinates with safety systems (STA-26) for fire suppression

## Operational Modes
- Nominal operations
- Reduced capability mode
- Emergency mode
- Maintenance mode
