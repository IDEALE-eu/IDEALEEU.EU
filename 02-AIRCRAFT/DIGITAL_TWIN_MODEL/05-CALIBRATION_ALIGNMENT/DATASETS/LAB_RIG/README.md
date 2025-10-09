# LAB_RIG

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 05-CALIBRATION_ALIGNMENT/DATASETS > LAB_RIG**

Hardware-in-the-Loop (HIL) and Software-in-the-Loop (SIL) rig data.

## Purpose

Calibration and validation data from HIL/SIL test rigs for behavioral models.

## Rigs

### HIL_RIG_FLIGHT_CONTROL
- **Purpose**: Test autopilot/flight control logic with real hardware
- **Hardware**: IMA modules, control actuators, sensor simulators
- **Tests**: Control law validation, failure mode testing
- **Data**: Control commands, sensor feedback, state transitions

### SIL_RIG_ENGINE_MANAGEMENT
- **Purpose**: Test engine control logic (FADEC simulation)
- **Software**: FADEC software, engine model
- **Tests**: Thrust management, transient response, degraded modes
- **Data**: Throttle commands, engine states, fuel flow

### HIL_RIG_H2_SAFETY
- **Purpose**: Test H₂ safety monitoring and leak detection
- **Hardware**: H₂ sensors, safety interlocks, valve actuators
- **Tests**: Leak scenarios, emergency shutdown
- **Data**: H₂ concentration, valve states, alarm triggers

## Data Format

- **Time-Series**: CSV, synchronized with hardware clock
- **Events**: Discrete events (mode changes, failures) logged separately
- **Reports**: Test reports with pass/fail criteria

## Integration

HIL/SIL data used for:
1. **Behavioral Model Calibration**: Tune state machines, control logic
2. **Edge Cases**: Validate failure modes not feasible in flight test

## Related Documents

- **../../../CROSS_SYSTEM_INTEGRATION/06-HIL_SIL_RIGS/** - Rig specifications
- **../../02-MODELS/BEHAVIORAL/** - Behavioral models

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
