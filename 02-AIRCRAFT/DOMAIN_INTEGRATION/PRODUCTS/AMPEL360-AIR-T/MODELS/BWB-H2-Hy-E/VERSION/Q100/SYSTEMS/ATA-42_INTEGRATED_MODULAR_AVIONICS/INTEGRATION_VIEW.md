# ATA-42 INTEGRATED MODULAR AVIONICS — Integration View

## Functional Overview
IMA platform hosting critical H₂ management partitions, fuel cell control, and hybrid propulsion system management.

## Key Dependencies
- **ATA-21**: Thermal management data and control
- **ATA-24**: Power supply and load management
- **ATA-28**: H₂ system monitoring and control
- **ATA-45**: Central maintenance and health monitoring
- **ATA-46**: Flight deck information systems
- **ATA-92**: EWIS for IMA modules

## Key Partitions
- H₂ Fuel Management System (FMS)
- Battery Management System (BMS)
- Thermal Management Control
- Propulsion System Supervisor
- Safety Monitor and Fault Detection

## Operating Modes
- Ground: System health checks, configuration
- Flight: Real-time monitoring and control
- Emergency: Fault isolation and safe mode

## Integration Points
See INTERFACE_MATRIX for detailed cross-system interfaces.
