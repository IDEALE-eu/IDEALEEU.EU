# ATA-73 ENGINE FUEL CONTROL — Integration View

## Functional Overview
FADEC system for hybrid-electric propulsion. Controls H₂ flow, fuel cell operation, and electric motor performance.

## Key Dependencies
- **ATA-28**: H₂ fuel supply control
- **ATA-24**: Electrical control power
- **ATA-76**: Engine control integration
- **ATA-77**: Engine indication systems
- **ATA-42**: IMA integration for health monitoring
- **ATA-92**: EWIS for FADEC

## Control Functions
- H₂ flow rate management
- Fuel cell power output control
- Electric motor speed and torque control
- Thermal management coordination
- Fault detection and isolation

## Operating Modes
- Ground: Pre-start checks and configuration
- Start: Fuel cell startup sequence
- Flight: Real-time performance optimization
- Emergency: Safe shutdown and fault handling

## Integration Points
See INTERFACE_MATRIX for detailed cross-system interfaces.
