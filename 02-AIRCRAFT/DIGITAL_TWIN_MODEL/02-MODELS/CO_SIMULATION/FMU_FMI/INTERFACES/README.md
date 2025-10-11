# INTERFACES

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > INTERFACES**

Signal interface definitions, unit conversions, and FMU connection mappings.

## Purpose

This directory defines the standardized signal interfaces between Functional Mock-up Units (FMUs) in the co-simulation environment. It ensures:
- Consistent signal naming across all FMUs
- Proper unit handling and conversions
- Clear mapping of connections between FMUs
- Traceability to system requirements (especially ATA-27 Flight Controls)

## Files

### signals.yaml
**Primary signal interface definition**
- Comprehensive list of all signals exchanged between FMUs
- Signal properties: name, type, unit, range, sample rate
- Source and destination FMU mapping
- Safety-critical signal identification (DAL levels)
- EBOM references for traceability
- Focus on ATA-27 Flight Control System signals

**Key sections:**
- `pilot_inputs`: Control stick and pedal positions from cockpit
- `control_surface_commands`: Commands to actuators (elevator, aileron, rudder, spoilers)
- `actuator_feedback`: Position and force feedback from control surfaces
- `aerodynamic_outputs`: Lift, drag, and moment coefficients from aerodynamics model
- `air_data_inputs`: Angle of attack, sideslip, Mach number, altitude
- `system_status`: FCC mode, health status, fault flags

### units.yaml
**Unit definitions and conversion rules**
- Standard units for each physical quantity
- SI units with documented exceptions (aviation standards)
- Conversion factors and formulas
- Unit validation rules
- Signal-specific unit assignments

### mapping.csv
**FMU connection matrix**
- Tabular format showing all FMU interconnections
- Source FMU → Signal → Destination FMU(s)
- Used by orchestration layer to configure co-simulation

## Use Case: ATA-27 Flight Control System

The signal definitions in this directory are primarily designed to support the flight control system co-simulation:

### Control Loop Flow
1. **Pilot Input** → Control_FMU receives stick/pedal positions
2. **Control Laws** → Control_FMU computes surface deflections
3. **Actuator Commands** → Commands sent to Aero_FMU and Struct_FMU
4. **Aerodynamics** → Aero_FMU calculates forces and moments
5. **Structures** → Struct_FMU computes deflections and feedback
6. **Feedback Loop** → Position feedback returns to Control_FMU

### Example Signal Chain
```
pilot_stick_pitch (Control_FMU)
  → elevator_cmd (Control_FMU → Aero_FMU)
    → lift_coefficient (Aero_FMU → Struct_FMU)
      → elevator_position_fb (Struct_FMU → Control_FMU)
```

## Signal Naming Convention

Signals follow this pattern:
```
<system>_<subsystem>_<parameter>_<modifier>
```

Examples:
- `pilot_stick_pitch`: Pilot longitudinal stick position
- `elevator_cmd`: Elevator deflection command
- `elevator_position_fb`: Elevator position feedback
- `lift_coefficient`: Aerodynamic lift coefficient

## Safety-Critical Signals

Signals marked with `safety_critical: true` require:
- Triple or quadruple redundancy
- Voting/monitoring algorithms
- DO-178C DAL-A or DAL-B compliance
- Enhanced validation and testing

Examples:
- All primary control surface commands (elevator, aileron, rudder)
- FCC mode and health status
- Actuator fault flags

## Integration with Requirements

All signals are traceable to:
- **EBOM references**: Engineering Bill of Materials identifiers (e.g., ATA-27-21-001)
- **Requirements**: System requirements from SPECS/ directory
- **ICDs**: Interface Control Documents from ATA-27 configuration

## Validation

Signal interfaces are validated through:
- Range checking (min/max values)
- Rate-of-change checking (physical limits)
- Consistency checking (paired signals)
- Redundancy voting (for safety-critical signals)

See `../TESTS/VECTORS/` for validation test vectors.

## Related Documents

- [signals.yaml](signals.yaml) - Complete signal interface specification
- [units.yaml](units.yaml) - Unit definitions and conversions
- [mapping.csv](mapping.csv) - FMU connection matrix
- [../SPECS/](../SPECS/) - FMI specifications and tolerances
- [../TESTS/VECTORS/](../TESTS/VECTORS/) - Signal validation test vectors
- [../../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/](../../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/) - Flight control system configuration

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-10-11 | Digital Twin Team | Initial signal interface definitions for ATA-27 flight controls |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
