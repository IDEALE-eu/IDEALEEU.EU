# 24-ELECTRICAL_POWER — Integration View

## System Overview

The Electrical Power System (EPS) provides generation, conditioning, distribution, storage, and protection of electrical power throughout the spacecraft. It ensures reliable power delivery to all spacecraft subsystems under all mission phases and operational modes.

## Functional Description

The EPS integrates solar arrays for power generation, batteries for energy storage, power conditioning and distribution units (PCDU), DC-DC converters, protection devices, and control algorithms to manage power flow and maintain voltage regulation.

## Key Interfaces

- **06 - Dimensions/Alignments**: Mounting provisions and alignment references for power equipment
- **15 - Environment/Vibration**: Environmental protection and shock/vibration isolation
- **31 - Data Handling**: Command and telemetry interface for power management
- **39 - Power Control Panels**: Integration with power control and switching units
- **42 - Thermal Control**: Heat dissipation from power components
- **51 - Primary Structure**: Structural mounting and load paths
- **57 - Solar Arrays**: Solar panel interfaces and power generation
- **97 - Harness/EWIS**: Electrical wiring and interconnects

## Operational Modes

- **Launch**: Battery-powered operation
- **Deployment**: Solar array deployment and power system checkout
- **Normal Operations**: Solar power generation with battery charge management
- **Eclipse**: Battery discharge to maintain spacecraft operations
- **Safe Mode**: Reduced power configuration for fault conditions
- **End-of-Life**: Degraded power generation capability

## Subsystems

- **24-10 Power Generation**: Solar arrays and power generation equipment
- **24-20 Power Conditioning**: Voltage regulation and power conversion
- **24-30 Power Distribution**: Power bus management and distribution
- **24-40 Energy Storage**: Battery systems and charge control
- **24-50 Protection/Fuses/Breakers**: Overcurrent protection and fault isolation
- **24-60 Converters (DC-DC, AC-DC)**: Secondary power conversion
- **24-70 Algorithms/Control**: Power management software and control algorithms
- **24-80 Testing/Qualification**: EPS testing and qualification procedures
