# 35-OXYGEN — Integration View

## Functional Description

Provides breathable oxygen supply for passengers and crew in emergency situations (cabin depressurization) and continuous supply for flight crew at high altitudes.

## Dependencies

- **ATA-31 (Instruments)**: Oxygen pressure indication and monitoring
- **ATA-42 (Electrical System)**: Power for oxygen generation/distribution systems
- **EER Domain**: Environmental control integration
- **EEE Domain**: Electrical power distribution

## Operating Modes

- Normal: System on standby, monitoring pressure
- Emergency: Automatic mask deployment on cabin depressurization
- Crew Continuous: Continuous oxygen supply above FL250

## Integration Points

See [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for detailed interface specifications.
