# SAFETY_GUARDS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 07-RUNTIME_DEPLOYMENT > SAFETY_GUARDS**

Safety guardrails: No autotuning on safety-critical paths, hard bounds, interlocks.

## Purpose

Define safety constraints to prevent digital twin from issuing unsafe commands or predictions.

## Safety Principles

### 1. No Autotuning on Safety-Critical Paths

**Rule**: Model parameters affecting flight control, propulsion, or structural integrity must NOT be updated in-flight.

**Affected Models**:
- Flight control models (autopilot, stability augmentation)
- Structural load predictions
- H₂ leak detection thresholds

**Enforcement**:
- Parameter updates only on ground, with parking brake set
- Runtime flag: `SAFETY_CRITICAL_MODE = TRUE` → block parameter updates
- Audit log: All attempted parameter changes logged

### 2. Hard Bounds on Outputs

**Rule**: All model outputs must be validated against physical limits before use.

**Bounds**:
```yaml
bounds:
  h2_tank_temperature:
    min: 18  # Kelvin (below triple point → invalid)
    max: 42  # Kelvin (excessive boil-off → invalid)
  structure_load_factor:
    min: -1.5  # g (below ultimate negative load)
    max: 4.5   # g (above ultimate positive load)
  engine_egt:
    min: 0     # °C (unrealistic)
    max: 1350  # °C (material limit)
  bus_voltage_ac:
    min: 90    # VAC (equipment damage)
    max: 130   # VAC (equipment damage)
```

**Actions on Violation**:
1. Flag output as `INVALID - OUT OF BOUNDS`
2. Log violation with context
3. Alert operator (severity: HIGH)
4. Revert to last known-good prediction or safe default

### 3. Interlocks

**Rule**: Model-based commands require dual validation (model + independent check).

**Critical Commands**:
- H₂ valve actuation (leak detection → valve closure)
- Engine thrust reduction (anomaly detected)
- Flight control mode changes (autopilot engagement)

**Interlock Logic**:
```
IF (model_command == CLOSE_H2_VALVE) THEN
  IF (independent_sensor_confirms_leak == TRUE) THEN
    EXECUTE_COMMAND()
  ELSE
    LOG_CONFLICT()
    ALERT_OPERATOR()
    DO_NOT_EXECUTE()
  ENDIF
ENDIF
```

### 4. Validation Envelope

**Rule**: Models only valid within calibrated operational envelope (see `../01-ARCHITECTURE/ASSUMPTIONS_LIMITATIONS.md`).

**Envelope Checks**:
- Altitude: 0 - 45,000 ft
- Speed: 0 - 350 KTAS
- Mach: 0 - 0.82
- H₂ tank pressure: 1 - 350 bar

**Actions if Outside Envelope**:
1. Flag output with `OUTSIDE VALIDATION ENVELOPE`
2. Increase uncertainty bounds (widen confidence intervals)
3. Recommend ground analytics or physical inspection

### 5. Edge Runtime Constraints

**Rule**: On-aircraft CPU usage <15%, no remote updates during flight phases.

**Constraints**:
- **CPU Usage**: Monitor CPU%, if >15% → throttle non-critical models
- **Memory**: <256 MB for twin runtime
- **No Remote Updates**: Model updates only on ground, with explicit approval
- **Hardened Against Cyber Threats**: Secure boot, signed models (see `CYBERSECURITY.md`)

## Operational Modes

### Ground Mode (Safe for Updates)
- **Conditions**: Parking brake set, engines off, weight-on-wheels
- **Allowed**: Parameter updates, model retraining deployment, what-if scenarios
- **Constraints**: None (except cybersecurity)

### Flight Mode (Locked)
- **Conditions**: Airborne, engines running
- **Allowed**: Real-time inference, anomaly detection, health monitoring
- **Constraints**: No parameter updates, no model redeployment

### Emergency Mode
- **Conditions**: System failure, critical alert
- **Behavior**: Revert to last known-good baseline, disable advanced analytics
- **Human-in-the-Loop**: Require operator confirmation for any action

## Monitoring and Alerts

### Safety Violations
- **Metric**: Count of hard bound violations, interlock conflicts
- **Threshold**: >3 violations in 1 hour → escalate to engineering
- **Action**: Automated alert (email, SMS) + log review

### CPU Overload
- **Metric**: CPU usage (%)
- **Threshold**: >15% sustained for >1 minute
- **Action**: Throttle non-critical models, alert crew

### Model Staleness
- **Metric**: Time since last prediction update
- **Threshold**: >10 seconds for real-time models
- **Action**: Flag as `STALE`, recompute or use last valid value

## Testing

All safety guards must be validated:
1. **Unit Tests**: Verify bounds checking, interlock logic
2. **Integration Tests**: HIL/SIL rig testing (see `../05-CALIBRATION_ALIGNMENT/DATASETS/LAB_RIG/`)
3. **Fault Injection**: Inject out-of-bounds values, verify guards trigger

## Related Documents

- **CYBERSECURITY.md** - Cybersecurity controls (secure boot, model signing)
- **../01-ARCHITECTURE/ASSUMPTIONS_LIMITATIONS.md** - Validity domains
- **../11-SAFETY_COMPLIANCE/HAZARD_BOUNDARIES.md** - Hazard analysis

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
