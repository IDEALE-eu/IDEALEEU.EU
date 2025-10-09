# ATA-71 POWERPLANT — Integration View

## Functional Overview
Hybrid-electric propulsion system combining fuel cells, electric motors, and propulsors. BWB-specific distributed propulsion architecture.

## Key Dependencies
- **ATA-24**: Electrical power distribution to motors
- **ATA-28**: H₂ fuel supply for fuel cells
- **ATA-29**: Hydraulic systems for actuators
- **ATA-36**: Pneumatic systems integration
- **ATA-75**: Bleed air systems
- **ATA-92**: EWIS for propulsion system

## Propulsion Architecture
- Distributed electric propulsion fans
- Fuel cell power generation
- Motor drives and inverters
- Thrust vectoring capability (if applicable)

## Operating Modes
- Ground: System tests, power checks
- Takeoff: Maximum thrust, combined power
- Cruise: Optimized efficiency, fuel cell primary
- Descent: Reduced power, regenerative mode
- Emergency: Safe shutdown procedures

## Integration Points
See INTERFACE_MATRIX for detailed cross-system interfaces.
