# ASSUMPTIONS_LIMITATIONS

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 01-ARCHITECTURE > ASSUMPTIONS_LIMITATIONS**

Validity domains, exclusions, and fidelity bounds for the aircraft digital twin.

## Purpose

This document defines the assumptions, limitations, and validity boundaries for the digital twin models. Operating outside these bounds requires model re-validation or may yield inaccurate results.

## Validity Domains

### Operational Envelope

**Flight Envelope** (defined by certification basis, see ATA-05):
- **Altitude**: 0 - 45,000 ft pressure altitude
- **Speed**: 0 - 350 KTAS (Knots True Airspeed)
- **Mach**: 0 - 0.82 Mach
- **Load Factor**: -1.0g to +3.8g (normal category)
- **Temperature**: ISA -40°C to ISA +35°C (ambient)

**H₂ Fuel System** (ATA-28):
- **Tank Pressure**: 1 - 350 bar (abs)
- **H₂ Temperature**: 20K - 40K (liquid), 250K - 320K (gaseous)
- **Boil-Off Rate**: <2% per day (dormant), <5% per day (operational)
- **Leak Detection Threshold**: >10 ppm H₂ concentration

**Propulsion System** (ATA-70-80):
- **Thrust Range**: 0 - 100% rated thrust (per engine)
- **Fuel Flow**: 0 - 500 kg/hr H₂ (per engine at max continuous thrust)
- **EGT (Exhaust Gas Temp)**: <1200°C continuous, <1350°C transient (5 min)
- **Engine Cycles**: 0 - 20,000 cycles (design life)

**Electrical System** (ATA-24):
- **Bus Voltage**: 115 VAC ±10% (400 Hz), 28 VDC ±5%
- **Load**: 0 - 150 kVA (total aircraft)
- **Battery SOC**: 20% - 100% (operational), 0% - 100% (ground)

### Model-Specific Validity Domains

#### Aerodynamics Models

**CFD Surrogates** (`02-MODELS/PHYSICS/AERODYNAMICS/`):
- **Reynolds Number**: 1e6 - 1e8 (based on mean aerodynamic chord)
- **Angle of Attack**: -5° to +15° (nominal), -10° to +25° (extended for stall prediction)
- **Sideslip Angle**: -15° to +15°
- **Mach Number**: 0.1 - 0.82 (incompressible to high subsonic)
- **Configuration**: Clean, flaps 0°-40°, gear up/down
- **Exclusions**: 
  - Supersonic flight (Mach >1.0)
  - Deep stall (AoA >25°)
  - Spin dynamics (requires different model)

**Limitations**:
- ROM (Reduced-Order Model) accuracy degrades beyond training domain (extrapolation error >10%)
- Unsteady effects (vortex shedding, buffet) not captured in steady-state surrogates
- Ice accretion effects require separate model (ATA-30 Ice & Rain Protection)

#### Structures Models

**FEM Models** (`02-MODELS/PHYSICS/STRUCTURES/`):
- **Load Range**: -1.0g to +3.8g static, -1.5g to +4.5g ultimate (1.5× safety factor)
- **Fatigue Spectrum**: 0 - 60,000 flight hours, 0 - 40,000 cycles
- **Temperature Range**: -55°C to +85°C (structure), -196°C (cryo tank local)
- **Damage States**: Pristine, minor (crack <10mm), major (crack >10mm, repair required)
- **Exclusions**:
  - Bird strike (requires transient dynamic analysis)
  - Lightning strike (requires EM coupling analysis, ATA-24)
  - Ground handling loads (requires separate analysis)

**Limitations**:
- Static FEM only; dynamic modes require modal analysis (separate tool)
- Linear material models; plasticity/yielding not captured beyond 90% yield strength
- Joint stiffness modeled with effective properties (not micro-mechanics)

#### Thermal Models

**Cryo Tank Models** (`02-MODELS/PHYSICS/THERMAL/`):
- **Tank Temperature**: 20K - 40K (liquid H₂)
- **Ambient Temperature**: -55°C to +50°C
- **Pressure**: 1 - 350 bar
- **Insulation Effectiveness**: 90-98% (based on MLI - Multi-Layer Insulation)
- **Heat Leak**: 0.1 - 5 W (dependent on insulation, pressure, ambient)
- **Exclusions**:
  - Rapid depressurization transients (requires CFD)
  - Fire scenarios (requires combustion modeling, ATA-26)

**Heat Exchanger Models** (`02-MODELS/PHYSICS/THERMAL/`):
- **Effectiveness**: 60-95% (counter-flow, cross-flow)
- **Fluid Temperatures**: -40°C to +150°C
- **Flow Rates**: 0.1 - 10 kg/s
- **Pressure Drop**: <20 kPa (design constraint)
- **Exclusions**: Fouling effects (requires empirical degradation model)

**Limitations**:
- 1D/lumped parameter models; 3D effects (stratification, natural convection) simplified
- Steady-state or quasi-steady; fast transients (<1s) not accurate
- No phase-change modeling for cabin humidity (requires separate HVAC model)

#### Propulsion Models

**Engine Performance** (`02-MODELS/PHYSICS/PROPULSION/`):
- **Power Range**: 0 - 100% rated power
- **Altitude**: 0 - 45,000 ft
- **Mach Number**: 0 - 0.82
- **Ambient Temperature**: ISA -40°C to ISA +35°C
- **Degradation**: 0-5% thrust loss (time/cycle-based), 0-10% fuel consumption increase
- **Exclusions**:
  - Engine-out transients (requires dynamic simulation)
  - Compressor stall/surge (requires 1D/2D CFD)
  - Foreign object damage (FOD) effects

**Electric Motor Models** (if applicable):
- **Power Range**: 0 - 100% rated power (e.g., 500 kW per motor)
- **Efficiency**: 92-98% (dependent on load, RPM, temperature)
- **Temperature**: -40°C to +150°C (motor winding)
- **Voltage**: 540 VDC ±10% (high-voltage bus)
- **Exclusions**: Harmonic distortion effects on bus, EMI (requires EM analysis)

**Limitations**:
- Steady-state or quasi-steady; transients >5s only
- Degradation models based on fleet average (not physics-based wear)
- No engine health monitoring (EHM) sensor fault modeling

#### H₂ Energy System Models

**H₂ Tank & BOP** (`02-MODELS/PHYSICS/ENERGY_H2/`):
- **Tank Capacity**: 100 - 5000 kg H₂ (liquid)
- **Pressure Range**: 1 - 350 bar
- **Temperature Range**: 20K - 40K (tank), 250K - 320K (gaseous, post-vaporizer)
- **Boil-Off**: 0.5-5% per day (function of insulation, ambient, pressure)
- **Leak Rate**: <0.1% per day (normal), >0.5% per day (alert threshold)
- **Exclusions**:
  - Tank rupture (catastrophic failure, out-of-scope)
  - Large leak (>10 kg/hr, requires emergency procedures, not predictive model)

**Limitations**:
- Simplified thermodynamics (ideal gas + real gas correction); no detailed H₂ property tables
- No sloshing dynamics (requires CFD)
- Leak detection based on concentration sensors; no spatial distribution model

#### Behavioral Models

**State Machines** (`02-MODELS/BEHAVIORAL/STATE_MACHINES/`):
- **States**: 5-50 discrete states per system (e.g., IMA: Init, Healthy, Degraded, Failed)
- **Transitions**: Deterministic (event-driven) or probabilistic (failure rates)
- **Update Rate**: 1-10 Hz
- **Exclusions**: 
  - Complex continuous dynamics (use physics models)
  - Human operator behavior (requires cognitive modeling, out-of-scope)

**Control Logic** (`02-MODELS/BEHAVIORAL/CONTROL_LOGIC/`):
- **Autopilot Modes**: HDG, ALT, VS, NAV, APPR (standard modes)
- **Autothrottle**: SPEED, MACH, THR (thrust modes)
- **Update Rate**: 10-50 Hz (control loops)
- **Exclusions**:
  - Pilot inputs (assumed nominal or from scenario definition)
  - Non-standard modes (e.g., emergency descent, requires separate validation)

**Limitations**:
- Simplified control laws (PID, gain-scheduled); full FCS (Flight Control System) is proprietary
- No hardware-in-the-loop (HIL) for edge cases (requires test rig, see `05-CALIBRATION_ALIGNMENT/DATASETS/LAB_RIG/`)

#### Data-Driven Models

**Anomaly Detectors** (`02-MODELS/DATA_DRIVEN/ANOMALY_DETECTORS/`):
- **Training Data**: Minimum 1000 flights, 10,000 hours (per aircraft variant)
- **Feature Space**: 50-200 sensor signals (see `03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`)
- **Detection Threshold**: 95% specificity (5% false positive rate), 85% sensitivity
- **Retraining Frequency**: Quarterly or when drift detected (PSI >0.25, see `08-SYNCHRONISATION/DRIFT_DETECTION.md`)
- **Exclusions**:
  - Novel failure modes (zero-day faults, not in training data)
  - Sensor faults (requires separate FDIR model)

**Surrogate Models** (`02-MODELS/DATA_DRIVEN/SURROGATES/`):
- **Training Domain**: Must overlap with physics model validation domain
- **Accuracy**: RMSE <5% of mean (for critical parameters), <10% (for non-critical)
- **Inference Time**: <100ms (edge), <1s (ground)
- **Exclusions**: Extrapolation beyond training domain (error unbounded)

**Limitations**:
- Black-box nature limits interpretability (see Model Cards for explainability metrics)
- Adversarial robustness not guaranteed (requires separate validation)
- Calibration drift over time requires monitoring (see `08-SYNCHRONISATION/DRIFT_DETECTION.md`)

## Exclusions

### System-Level Exclusions

**Not Modeled in Current Phase**:
1. **Ground Operations**:
   - Taxi dynamics (requires tire/gear models)
   - Ground handling loads (towing, jacking)
   - De-icing operations (ATA-30, requires fluid dynamics)

2. **Emergency Scenarios**:
   - Fire (requires combustion modeling, ATA-26)
   - Rapid decompression (requires transient CFD)
   - Ditching (requires fluid-structure interaction)

3. **Environmental Extremes**:
   - Severe icing (ATA-30, requires ice accretion model)
   - Lightning strike effects (ATA-24, requires EM transient analysis)
   - Volcanic ash ingestion (ATA-70, requires engine durability model)

4. **Human Factors**:
   - Pilot workload, decision-making (requires cognitive modeling)
   - Maintenance technician errors (requires human reliability analysis)
   - Passenger comfort (vibration, noise) - non-safety-critical

5. **Manufacturing Variability**:
   - As-built tolerances (simplified to nominal + known deltas)
   - Surface finish effects on drag (bundled into roughness factor)
   - Material property scatter (use design allowables, not probabilistic)

### Temporal Exclusions

**Not Captured in Real-Time Models** (edge deployment):
- Long-term degradation trends (>1000 flight hours) - use ground analytics
- Seasonal effects (atmospheric density trends) - use ground analytics
- Fleet-wide anomalies (require cross-aircraft correlation) - use ground analytics

### Fidelity Trade-Offs

| Model Type | Edge (L5) | Ground Interactive (L3) | Ground Batch (L4) |
|------------|-----------|------------------------|-------------------|
| Aerodynamics | Polars (lookup) | ROM (GPR, 10s) | CFD (hours) |
| Structures | Margin check (1ms) | FEM (simplified, 1min) | FEM (full, hours) |
| Thermal | Lumped (1ms) | 1D network (1s) | 3D CFD (hours) |
| Propulsion | Map (lookup, 1ms) | 0D cycle (1s) | 1D/2D (hours) |
| H₂ Energy | 0D tank (10ms) | 1D flow (1s) | 3D sloshing (hours) |
| Behavioral | State machine (1ms) | Simulink (real-time) | Monte Carlo (hours) |
| Data-Driven | ONNX (10ms) | Ensemble (1s) | Hyperparameter tuning (hours) |

## Assumptions

### General Assumptions

1. **Sensor Accuracy**: All sensors meet specification (no drift, no faults)
   - Violated if: Sensor fault detected by FDIR (see behavioral models)
   - Mitigation: Sensor health monitoring, redundant sensors

2. **Maintenance Quality**: All maintenance actions performed per AMM (Aircraft Maintenance Manual)
   - Violated if: MRO deviation reported (see `09-INTEGRATIONS/MRO_LINKS.md`)
   - Mitigation: MRO action logging, quality checks

3. **Configuration Control**: As-maintained configuration matches CM records
   - Violated if: Configuration audit reveals discrepancy
   - Mitigation: Regular configuration audits (annual minimum)

4. **Data Integrity**: Telemetry data not corrupted, tampered, or spoofed
   - Violated if: Cryptographic hash mismatch (see `07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md`)
   - Mitigation: Data signing, secure datalink

5. **Operational Compliance**: Aircraft operated within AFM (Aircraft Flight Manual) limits
   - Violated if: Exceedance detected (e.g., overspeed, over-g)
   - Mitigation: Exceedance monitoring, pilot training

### Model-Specific Assumptions

#### Physics Models

- **Aerodynamics**: 
  - Standard atmosphere (ISA) unless wind data provided
  - No ice accretion (separate model, ATA-30)
  - Symmetric flight (no wind shear, turbulence modeled stochastically)

- **Structures**: 
  - Material properties per design specifications (no degradation beyond fatigue)
  - No manufacturing defects (assumed accepted per QA)
  - Linear elasticity (no plasticity, buckling analyzed separately)

- **Thermal**: 
  - Ambient conditions per weather data (METAR/TAF)
  - Insulation performance per design (no degradation beyond specified)
  - No solar radiation effects (conservative for H₂ tank, included for cabin)

- **Propulsion**: 
  - Engine performance per OEM (Original Equipment Manufacturer) model
  - Fuel quality per specification (no contamination)
  - No thrust reversers (modeled separately for landing analysis)

- **H₂ Energy**: 
  - Liquid H₂ purity >99.9% (no impurities)
  - Insulation effectiveness per design (no vacuum loss in MLI)
  - No micro-leaks (below detection threshold <10 ppm)

#### Data-Driven Models

- **Training Data Representativeness**: Training data covers operational envelope
  - Violated if: New mission profile introduced (e.g., high-altitude cruise not in training)
  - Mitigation: Retraining with new data, A/B testing

- **Label Quality**: Ground truth labels accurate for supervised learning
  - Violated if: Mislabeled failures in training set
  - Mitigation: Expert review, cross-validation

- **Stationarity**: Statistical properties of data do not change over time
  - Violated if: Drift detected (PSI >0.25, see `08-SYNCHRONISATION/DRIFT_DETECTION.md`)
  - Mitigation: Continuous monitoring, retraining triggers

## Boundary Conditions

### Safety Boundaries (Hard Limits)

**Critical Parameters** (violation triggers model invalidation):
- **H₂ Tank Temperature**: <18K (below triple point) or >42K (excessive boil-off)
- **Structure Load Factor**: <-1.5g or >+4.5g (beyond ultimate load)
- **Engine EGT**: >1350°C (material limits)
- **Bus Voltage**: <90 VAC or >130 VAC (equipment damage)
- **Altitude**: >50,000 ft (beyond certification, decompression risk)

**Actions on Boundary Violation**:
1. Flag model output as "INVALID - OUT OF BOUNDS"
2. Log violation event with context (timestamp, aircraft ID, parameter, value)
3. Notify operator/engineer (alert severity: HIGH)
4. Revert to last known-good prediction or safe default

### Performance Boundaries (Soft Limits)

**Warning Thresholds** (degraded accuracy expected):
- **Angle of Attack**: >12° (near stall, ROM accuracy degrades)
- **Fatigue Damage**: >80% of design life (extrapolation risk)
- **Boil-Off Rate**: >4% per day (insulation degradation suspected)
- **Anomaly Score**: >2 standard deviations (model uncertainty high)

**Actions on Soft Limit**:
1. Increase model uncertainty bounds (widen confidence intervals)
2. Flag output with "DEGRADED ACCURACY" warning
3. Recommend ground analytics or physical inspection
4. Continue operation with caution

## Validation Boundaries

**Models Valid Only If**:
1. **Calibration Current**: Last calibration within 12 months (or 500 flight hours)
   - See `05-CALIBRATION_ALIGNMENT/CALIBRATION_PLAN.md`
2. **Test Coverage**: Validation test suite covers ≥95% of operational envelope
   - See `06-VALIDATION_VERIFICATION/TEST_CASES/`
3. **Drift Within Tolerance**: PSI <0.25 (Population Stability Index) over 7 days
   - See `08-SYNCHRONISATION/DRIFT_DETECTION.md`
4. **Error Budget Met**: Prediction error within specified bounds (per use case)
   - See `10-METRICS/PREDICTION_QUALITY.csv`

**Revalidation Triggers**:
- Major design change (e.g., engine upgrade, aerodynamic modification)
- Configuration change (e.g., new avionics, structural repair)
- Drift detection (PSI >0.25)
- Systematic bias detected (mean error >2%, see `10-METRICS/`)

## Related Documents

- **TWIN_SCOPE.md** - Use cases and operational modes
- **REFERENCE_ARCHITECTURE.md** - Architecture and data flows
- **../02-MODELS/** - Model specifications with fidelity definitions
- **../05-CALIBRATION_ALIGNMENT/CALIBRATION_PLAN.md** - Calibration methodology
- **../06-VALIDATION_VERIFICATION/VVP_PLAN.md** - Validation acceptance criteria
- **../08-SYNCHRONISATION/DRIFT_DETECTION.md** - Drift monitoring and thresholds
- **../11-SAFETY_COMPLIANCE/HAZARD_BOUNDARIES.md** - Safety hazard analysis

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Digital Twin Team | Initial assumptions and limitations |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
