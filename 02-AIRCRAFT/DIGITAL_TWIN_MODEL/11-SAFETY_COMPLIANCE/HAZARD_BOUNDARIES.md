# HAZARD_BOUNDARIES

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 11-SAFETY_COMPLIANCE > HAZARD_BOUNDARIES**

Operational envelopes (e.g., H₂ temp >20K for model validity).

## Purpose

Define hazard boundaries and operational limits for safe digital twin operation.

## Hazard Categories

### 1. H₂ Fuel System Hazards

#### H₂ Temperature Limits
- **Lower Bound**: 18K (below triple point → invalid physics)
- **Nominal Range**: 20K - 40K
- **Upper Bound**: 42K (excessive boil-off, insulation failure suspected)
- **Hazard**: Temperature <18K or >42K → model invalid, alert operator

#### H₂ Pressure Limits
- **Lower Bound**: 1 bar (minimum operating pressure)
- **Nominal Range**: 1 - 350 bar
- **Upper Bound**: 350 bar (maximum design pressure)
- **Hazard**: Pressure >350 bar → tank rupture risk, immediate shutdown

#### H₂ Leak Detection
- **Normal**: <10 ppm H₂ concentration
- **Alert Threshold**: 10-100 ppm (minor leak, monitor)
- **Critical Threshold**: >100 ppm (major leak, emergency procedures)
- **Hazard**: Leak >100 ppm → fire/explosion risk, isolate system

### 2. Structural Load Hazards

#### Load Factor Limits
- **Normal Operations**: -1.0g to +3.8g
- **Ultimate Load**: -1.5g to +4.5g (1.5× safety factor)
- **Hazard**: Load factor >+4.5g or <-1.5g → structural failure risk

#### Fatigue Damage
- **Nominal**: 0-80% of design life
- **Alert Threshold**: 80-100% (inspection required)
- **Critical Threshold**: >100% (replacement required)
- **Hazard**: Fatigue >100% → crack propagation, structural failure

### 3. Propulsion Hazards

#### Engine EGT (Exhaust Gas Temperature)
- **Normal**: 0-1200°C (continuous)
- **Transient**: 1200-1350°C (max 5 minutes)
- **Hazard**: EGT >1350°C → turbine blade damage, engine failure

#### Thrust Asymmetry
- **Normal**: <5% thrust difference between engines
- **Alert Threshold**: 5-10% (minor asymmetry)
- **Critical Threshold**: >10% (significant asymmetry, handling issues)
- **Hazard**: >10% asymmetry → loss of control risk

### 4. Thermal Hazards

#### Cabin Temperature
- **Normal**: 18°C - 27°C
- **Alert Threshold**: <10°C or >35°C (discomfort)
- **Critical Threshold**: <0°C or >40°C (safety risk)
- **Hazard**: Extreme temperature → hypothermia/hyperthermia risk

#### Avionics Bay Temperature
- **Normal**: 0°C - 55°C
- **Alert Threshold**: 55-70°C (reduced reliability)
- **Critical Threshold**: >70°C (equipment failure risk)
- **Hazard**: >70°C → avionics failure, loss of systems

### 5. Electrical Hazards

#### Bus Voltage (AC)
- **Normal**: 115 VAC ±5% (109-121 VAC)
- **Alert Threshold**: 115 VAC ±10% (103.5-126.5 VAC)
- **Critical Threshold**: <90 VAC or >130 VAC
- **Hazard**: Out-of-range voltage → equipment damage, fire risk

#### Bus Voltage (DC)
- **Normal**: 28 VDC ±5% (26.6-29.4 VDC)
- **Alert Threshold**: 28 VDC ±10% (25.2-30.8 VDC)
- **Critical Threshold**: <20 VDC or >32 VDC
- **Hazard**: Out-of-range voltage → equipment damage

## Model Validity Boundaries

### Operational Envelope
- **Altitude**: 0 - 45,000 ft (above 45,000 ft → model extrapolation)
- **Speed**: 0 - 350 KTAS (above 350 KTAS → compressibility effects not modeled)
- **Mach**: 0 - 0.82 (above 0.82 → transonic effects not modeled)

### Environmental Conditions
- **Temperature**: ISA -40°C to ISA +35°C (outside range → model degraded accuracy)
- **Wind**: <50 kts (above 50 kts → turbulence effects significant)

## Safety Actions

### Boundary Violation Response

**Immediate Actions**:
1. Flag model output as `INVALID - HAZARD BOUNDARY VIOLATED`
2. Log violation with context (timestamp, aircraft ID, parameter, value)
3. Alert operator (severity: CRITICAL)
4. Trigger emergency procedures (if applicable, e.g., H₂ leak >100 ppm)

**Follow-Up Actions**:
1. Root cause analysis (sensor fault? actual hazard?)
2. Engineering review (model update needed?)
3. Incident report (see `../07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md#incident-response`)

## Hazard Analysis

**Method**: ARP4761 Functional Hazard Assessment (FHA)

**Hazard Classifications**:
- **Catastrophic**: Loss of aircraft, multiple fatalities
- **Hazardous**: Serious injury, major aircraft damage
- **Major**: Discomfort, minor injuries
- **Minor**: Inconvenience

## Related Documents

- **../01-ARCHITECTURE/ASSUMPTIONS_LIMITATIONS.md** - Validity domains
- **../07-RUNTIME_DEPLOYMENT/SAFETY_GUARDS.md** - Safety guardrails
- **ASSURANCE_CASE/GSN.md** - Safety assurance case
- **STANDARDS_MAP.md** - Compliance standards

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
