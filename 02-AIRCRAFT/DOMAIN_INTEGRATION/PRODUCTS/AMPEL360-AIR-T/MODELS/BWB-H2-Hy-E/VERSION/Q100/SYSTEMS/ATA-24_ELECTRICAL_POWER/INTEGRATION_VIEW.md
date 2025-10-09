# ATA-24 ELECTRICAL POWER — Integration View

## Functional Overview
Hybrid-electric power distribution system. DC bus architecture fed by fuel cells and batteries, supplying propulsion motors and aircraft systems.

## Key Dependencies
- **ATA-28**: Fuel cell power input from H₂ system
- **ATA-29**: Hydraulic backup power
- **ATA-36**: Pneumatic system electrical loads
- **ATA-42**: IMA health monitoring and control
- **ATA-45**: Central maintenance system integration
- **ATA-46**: Information systems power
- **ATA-92**: EWIS power distribution
- **ATA-33**: Lighting systems

## Operating Modes
- Ground: APU/GPU power, battery charging
- Takeoff: Maximum power demand, fuel cell + battery
- Cruise: Fuel cell primary, battery standby
- Descent: Regenerative charging where applicable
- Emergency: Battery emergency power only

## Integration Points
See INTERFACE_MATRIX for detailed cross-system interfaces.
