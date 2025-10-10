# 24-ELECTRICAL_POWER — Integration View

## System Overview

The Electrical Power System (EPS) provides end-to-end power generation, conditioning, storage, distribution, and protection for the spacecraft across all mission phases. It ensures stable, regulated power delivery to all subsystems while maintaining fault tolerance, efficiency, and compliance with spacecraft-level power budgets.

## Functional Description

The EPS comprises:
- **Solar arrays** (primary generation),
- **Lithium-ion battery assemblies** (energy storage),
- **Power Conditioning and Distribution Unit (PCDU)** with integrated DC-DC converters,
- **Solid-state power controllers (SSPCs)** for load switching,
- **Protection circuitry** (fuses, current limiters),
- **Power management algorithms** (hosted on 31-Data Handling).

Power is distributed via the **97-Harness/EWIS** backbone, with thermal management coordinated through **42-Thermal Control**.

## Key Interfaces

| Interface To | System ID | Interface Type | Key Exchange |
|-------------|----------|----------------|--------------|
| Dimensions & Alignment | 06 | Mechanical | Mounting datums, alignment pins for PCDU and battery boxes |
| Environment & Vibration | 15 | Environmental | Shock/vibe qualification, acoustic load survival |
| Data Handling | 31 | Data/Command | Telemetry (bus voltage, current, SOC), commands (load on/off) |
| [Power Control Panels](../39-POWER_CONTROL_PANELS/) | 39 | Power/Control | Switched loads, RPC commands, FDIR coordination |
| [Thermal Control](../../STA-E-THERMAL-ENVIRONMENTAL-LIFESUPPORT/SYSTEMS/42-THERMAL_CONTROL/) | 42 | Thermal | Heat rejection from PCDU, batteries (conduction/radiation) |
| [Primary Structure](../../STA-A-STRUCTURES-MECHANISMS/SYSTEMS/51-PRIMARY_STRUCTURE/) | 51 | Structural | Load-bearing mounts, launch loads, shock transfer |
| Solar Arrays | 57 | Power | High-voltage DC from solar wings (80–120 V nominal) |
| [Harness / EWIS](../97-HARNESS_EWIS/) | 97 | Electrical | Power cables (primary/secondary buses), signal wiring |

## Operational Modes

- **Launch**: Battery-powered operation (solar arrays stowed)
- **Deployment**: Solar array deployment and power system checkout
- **Sun Pointing**: Solar power generation with battery charge management
- **Eclipse**: Battery discharge to maintain spacecraft operations
- **Safe Mode**: Reduced power configuration for fault conditions (critical loads only)
- **End-of-Life**: Degraded power generation capability (solar cell aging)

## Subsystems

- [**24-10 Power Generation**](./SUBSYSTEMS/24-10_POWER_GENERATION/): Solar arrays and power generation equipment
- [**24-20 Power Conditioning**](./SUBSYSTEMS/24-20_POWER_CONDITIONING/): Voltage regulation and power conversion
- [**24-30 Power Distribution**](./SUBSYSTEMS/24-30_POWER_DISTRIBUTION/): Power bus management and distribution
- [**24-40 Energy Storage**](./SUBSYSTEMS/24-40_ENERGY_STORAGE/): Battery systems and charge control
- [**24-50 Protection/Fuses/Breakers**](./SUBSYSTEMS/24-50_PROTECTION_FUSES_BREAKERS/): Overcurrent protection and fault isolation
- [**24-60 Converters (DC-DC, AC-DC)**](./SUBSYSTEMS/24-60_CONVERTERS_DCDC_ACDC/): Secondary power conversion
- [**24-70 Algorithms/Control**](./SUBSYSTEMS/24-70_ALGORITHMS_CONTROL/): Power management software and control algorithms
- [**24-80 Testing/Qualification**](./SUBSYSTEMS/24-80_TESTING_QUALIFICATION/): EPS testing and qualification procedures
