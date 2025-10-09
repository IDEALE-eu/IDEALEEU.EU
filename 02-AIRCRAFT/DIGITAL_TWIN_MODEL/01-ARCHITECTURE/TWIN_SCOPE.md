# TWIN_SCOPE

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 01-ARCHITECTURE > TWIN_SCOPE**

Digital twin scope definition, covering predictive, prescriptive, and what-if use cases.

## Purpose

This document defines the scope and use cases for the aircraft digital twin, distinguishing between different operational modes and analytical capabilities.

## Twin Types

### 1. Design Twin
**Lifecycle Phase**: Concept through certification  
**Purpose**: Virtual testing, design validation, certification support  
**Fidelity**: Level 3-4 (detailed to high-fidelity)  
**Update Frequency**: Per design iteration  

**Use Cases**:
- Virtual testing of design changes before physical prototypes
- Trade studies for propulsion, aerodynamics, thermal management
- Certification evidence generation (flutter, loads, thermal margins)
- Integration testing of systems before hardware availability

### 2. Test Twin
**Lifecycle Phase**: Ground test, flight test  
**Purpose**: Test planning, data analysis, anomaly investigation  
**Fidelity**: Level 4 (high-fidelity)  
**Update Frequency**: Daily during test campaigns  

**Use Cases**:
- Test envelope expansion planning
- Real-time test monitoring with predicted vs. actual comparison
- Post-flight data correlation and model calibration
- Failure mode investigation and root cause analysis

### 3. Operational Twin
**Lifecycle Phase**: In-service operations  
**Purpose**: Fleet management, predictive maintenance, mission optimization  
**Fidelity**: Level 5 (real-time) for operations, Level 3-4 for deep analysis  
**Update Frequency**: Real-time (edge), hourly (ground analytics)  

**Use Cases**:
- Real-time health monitoring and anomaly detection
- Predictive maintenance scheduling
- Mission planning and optimization (fuel, range, payload)
- Fleet-wide performance benchmarking

### 4. Mission Twin (Per-Aircraft Instance)
**Lifecycle Phase**: In-service  
**Purpose**: Individual aircraft tracking, as-maintained configuration  
**Fidelity**: Level 5 (real-time)  
**Update Frequency**: Real-time telemetry, event-driven for maintenance  

**Use Cases**:
- Per-aircraft usage tracking (cycles, hours, load spectrum)
- As-maintained configuration delta from baseline
- Individual aircraft performance trends and degradation
- Warranty and life-limited parts management

## Use Case Categories

### Predictive Use Cases

**Definition**: Forecast future states based on current conditions and historical trends

#### UC-PRED-001: Remaining Useful Life (RUL) Prediction
- **Description**: Predict time-to-failure for critical components (e.g., H₂ valves, pumps, bearings)
- **Models**: Fatigue (structures), degradation (thermal), anomaly detection (ML)
- **Inputs**: Flight history, maintenance records, sensor trends
- **Outputs**: RUL (hours/cycles), confidence interval, replacement recommendation
- **Safety Level**: Level B (Hazardous) - incorrect prediction may defer needed maintenance
- **Validation**: Correlation with actual failures (AUC >0.85)

#### UC-PRED-002: H₂ Boil-Off Prediction
- **Description**: Predict hydrogen boil-off rate for mission planning
- **Models**: Thermal (cryo tank), environment (ambient conditions)
- **Inputs**: Tank temperature profile, mission duration, ambient conditions
- **Outputs**: Boil-off mass (kg), remaining usable H₂, range impact
- **Safety Level**: Level B (Hazardous) - incorrect prediction affects fuel planning
- **Validation**: Ground test correlation within ±5%

#### UC-PRED-003: Performance Degradation Tracking
- **Description**: Track aircraft performance degradation over time (drag, engine efficiency)
- **Models**: Aerodynamics (CFD surrogates), propulsion (engine performance)
- **Inputs**: Flight data (speed, altitude, fuel flow), maintenance actions
- **Outputs**: Degradation factors, efficiency loss (%), recommended actions
- **Safety Level**: Level C (Major) - affects operational efficiency
- **Validation**: Baseline vs. degraded state within ±3%

### Prescriptive Use Cases

**Definition**: Recommend specific actions to optimize outcomes

#### UC-PRESC-001: Maintenance Action Recommendation
- **Description**: Recommend optimal maintenance actions based on cost-benefit analysis
- **Models**: RUL predictions, cost models, availability models
- **Inputs**: Fleet schedule, part inventory, labor availability, predicted failures
- **Outputs**: Maintenance schedule, part orders, downtime minimization plan
- **Safety Level**: Level C (Major) - affects maintenance planning
- **Validation**: Comparison with expert maintenance planners (agreement >80%)

#### UC-PRESC-002: Mission Profile Optimization
- **Description**: Optimize flight profile for efficiency (speed, altitude, routing)
- **Models**: Aerodynamics, propulsion, H₂ consumption, atmospheric models
- **Inputs**: Origin, destination, payload, winds aloft, weather
- **Outputs**: Optimized flight plan (speed/altitude profile), fuel savings (%), time penalty
- **Safety Level**: Level C (Major) - recommendations must respect safety margins
- **Validation**: Simulator trials, comparison with baseline profiles

#### UC-PRESC-003: Load Balancing and CG Management
- **Description**: Recommend cargo/passenger distribution for optimal performance and safety
- **Models**: Structures (loads), aerodynamics (stability), fuel sequencing
- **Inputs**: Payload manifest, fuel state, flight phase
- **Outputs**: Recommended load distribution, CG position, trim settings
- **Safety Level**: Level A (Catastrophic) - incorrect CG affects controllability
- **Validation**: Ground test, flight test envelope validation

### What-If Use Cases

**Definition**: Explore hypothetical scenarios for training, planning, or investigation

#### UC-WHATIF-001: Failure Mode Simulation
- **Description**: Simulate system failure scenarios for training or investigation
- **Models**: Behavioral (fault propagation), control logic (degraded modes)
- **Inputs**: Failure scenario (component, severity, timing), flight conditions
- **Outputs**: System response, available degraded modes, pilot actions required
- **Safety Level**: Level B (Hazardous) - incorrect simulation affects training
- **Validation**: Comparison with simulator, flight test results

#### UC-WHATIF-002: Design Modification Impact
- **Description**: Assess impact of proposed design changes (e.g., wingtip extension, engine upgrade)
- **Models**: Aerodynamics, structures, propulsion, energy balance
- **Inputs**: Design delta (geometry, mass, power), flight conditions
- **Outputs**: Performance impact (range, speed, efficiency), certification implications
- **Safety Level**: Level C (Major) - informs design decisions
- **Validation**: Wind tunnel, ground test before flight test

#### UC-WHATIF-003: Extreme Condition Analysis
- **Description**: Explore aircraft behavior under extreme but certifiable conditions
- **Models**: All physics models, control logic (limit protection)
- **Inputs**: Extreme conditions (high altitude, low temperature, max payload)
- **Outputs**: System margins, warnings/alerts triggered, operational limitations
- **Safety Level**: Level A (Catastrophic) - defines operational envelope
- **Validation**: Flight test envelope expansion, simulator validation

## Model Fidelity Requirements by Use Case

| Use Case | Aerodynamics | Structures | Thermal | Propulsion | H₂ Energy | Behavioral | Data-Driven |
|----------|--------------|------------|---------|------------|-----------|------------|-------------|
| UC-PRED-001 (RUL) | L2 | L4 | L3 | L3 | L3 | L2 | L5 |
| UC-PRED-002 (H₂ Boil-Off) | L1 | L1 | L4 | L1 | L4 | L2 | L3 |
| UC-PRED-003 (Perf Degradation) | L4 | L2 | L2 | L4 | L3 | L2 | L4 |
| UC-PRESC-001 (Maint Rec) | L1 | L2 | L2 | L2 | L2 | L3 | L5 |
| UC-PRESC-002 (Mission Opt) | L4 | L2 | L3 | L4 | L4 | L3 | L4 |
| UC-PRESC-003 (Load Balance) | L3 | L4 | L2 | L2 | L3 | L3 | L2 |
| UC-WHATIF-001 (Failure Sim) | L3 | L3 | L3 | L3 | L3 | L4 | L2 |
| UC-WHATIF-002 (Design Mod) | L4 | L4 | L3 | L4 | L3 | L3 | L1 |
| UC-WHATIF-003 (Extreme) | L4 | L4 | L4 | L4 | L4 | L4 | L2 |

**Fidelity Levels**: L1=Conceptual, L2=Preliminary, L3=Detailed, L4=High-Fidelity, L5=Real-Time

## Operational Modes

### Edge Mode (On-Aircraft)
- **Compute Environment**: Aircraft IMA, limited CPU/memory
- **Models**: Level 5 (real-time), reduced-order or surrogate models
- **Latency**: <100ms for critical alerts, <1s for health monitoring
- **Network**: Intermittent connectivity, no internet dependency for safety-critical functions
- **Safety**: No remote updates during flight, hardened against cyber threats

### Ground Mode (Operations Center)
- **Compute Environment**: Cloud/on-premise datacenter
- **Models**: All fidelity levels (L1-L5)
- **Latency**: <5s for interactive analytics, <1hr for batch optimization
- **Network**: Continuous connectivity, secure VPN/API gateway
- **Safety**: Full validation before deployment to edge

### Lab/HIL Mode (Development/Test)
- **Compute Environment**: Engineering workstations, test rigs
- **Models**: All fidelity levels, development/experimental models
- **Latency**: Variable (seconds to hours)
- **Network**: Isolated or development network
- **Safety**: Not safety-certified, for development/calibration only

## Integration Points

### Upstream (Inputs to Twin)
- **Telemetry**: Real-time sensor data from aircraft (see `03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`)
- **Configuration**: As-built, as-maintained configuration from CM (see `09-INTEGRATIONS/MBSE_LINKS.md`)
- **Maintenance Events**: MRO actions from fleet management (see `09-INTEGRATIONS/MRO_LINKS.md`)
- **Mission Plans**: Flight plans, payload manifests from ops (see `01-FLEET/OPERATIONAL_DATA_HUB/`)

### Downstream (Outputs from Twin)
- **KPIs**: Health scores, RUL, efficiency metrics (see `03-INTERFACES_APIS/STREAMS/OUTPUTS/KPIs_SCHEMA.yaml`)
- **Alerts**: Anomalies, threshold exceedances, maintenance recommendations
- **Reports**: Performance trends, correlation studies, certification evidence
- **Feedback**: Model updates, calibration deltas to configuration management

## Exclusions

**Out-of-Scope for Current Phase**:
- Ground support equipment (GSE) digital twins (future phase)
- Manufacturing process twins (separate program, see `02-AIRCRAFT/FINAL_ASSEMBLY_OPS/`)
- Supply chain digital twins (out-of-scope)
- Passenger experience simulation (not safety-critical)
- Airline-specific business intelligence (provided via API, not in core twin)

## Related Documents

- **REFERENCE_ARCHITECTURE.md** - Twin architecture and data flows
- **ASSUMPTIONS_LIMITATIONS.md** - Validity domains and exclusions
- **../02-MODELS/** - Detailed model specifications
- **../03-INTERFACES_APIS/** - API and data interface specifications
- **../06-VALIDATION_VERIFICATION/VVP_PLAN.md** - Use case validation methodology

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Digital Twin Team | Initial scope definition with use cases |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
