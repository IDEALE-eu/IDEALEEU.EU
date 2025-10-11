# FMU_FMI

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/CO_SIMULATION > FMU_FMI**

Functional Mock-up Units (FMUs) and FMI 3.0 configurations for co-simulation.

## Purpose

FMU library for co-simulation of aircraft subsystems, with primary focus on **ATA-27 Flight Control System** integration with aerodynamics, structures, propulsion, and H₂ energy systems.

## Directory Structure

```
FMU_FMI/
├── SPECS/                      # FMI 2.0/3.0, cs/me, step sizes, tolerances
│   ├── fmi_config.yaml         # Main FMI configuration
│   └── README.md
├── INTERFACES/                 # Signal definitions, units, mapping
│   ├── signals.yaml            # Complete signal interface definitions
│   ├── units.yaml              # Unit conversions and standards
│   ├── mapping.csv             # FMU connection matrix
│   └── README.md
├── COMPONENTS/                 # FMU source code and binaries
│   └── <comp>/
│       ├── src/                # C/C++/Modelica export
│       ├── build/              # Build artifacts
│       ├── fmu/
│       │   └── <comp>_cs|me_<semver>.fmu
│       └── README.md
├── ADAPTERS/                   # Wrappers for Simulink, Python (FMPy), C++
├── ORCHESTRATION/              # Master algorithm
│   ├── configs/                # YAML scenarios and scheduler
│   └── master_<lang>.{py,cpp}
├── SIM/                        # Simulation environment
│   ├── scenarios/              # NN_desc.yaml scenario definitions
│   ├── runs/                   # Execution logs and traces
│   └── results/                # CSV, MAT output files
├── TESTS/                      # Validation and verification
│   ├── compliance/             # fmuCheck, FMPy reports
│   ├── integration/            # Integration tests
│   ├── regression/             # Regression tests
│   └── VECTORS/                # Test vectors for requirement validation
├── EVIDENCE/                   # Test evidence, determinism, KPIs, coverage
├── TOOLS/                      # Build and test automation
│   ├── cmake/                  # CMake build configuration
│   ├── scripts/                # pack_fmu.sh, simulate.py, run_test_vector.py
│   └── README.md
└── README.md                   # This file
```

## FMU List

| FMU Name | Subsystem | Inputs | Outputs | Update Rate |
|----------|-----------|--------|---------|-------------|
| **Aero_FMU** | Aerodynamics | α, β, Mach, δ (control surfaces) | CL, CD, CM | 100 Hz |
| **Struct_FMU** | Structures | Loads (Fx, Fy, Fz, Mx, My, Mz) | Deflections, Stress | 100 Hz |
| **Thermal_FMU** | Thermal | Heat sources, ambient T | Component temps | 1 Hz |
| **Propulsion_FMU** | Propulsion | Throttle, altitude, Mach | Thrust, fuel flow, EGT | 10 Hz |
| **H2_FMU** | H₂ Energy | Fuel demand, ambient T | Tank pressure, boil-off | 1 Hz |
| **Control_FMU** | Control Logic | Sensors, pilot commands | Actuator commands | 50 Hz |

## FMI 3.0 Features

- **Co-Simulation**: Model exchange for subsystem simulation
- **Event Handling**: Discrete events (e.g., gear extension, mode changes)
- **Continuous Outputs**: Smooth interpolation between time steps

## Use Case: ATA-27 Flight Control System

The FMU co-simulation framework is designed to support the **Flight Control System (ATA-27)** as the primary use case, demonstrating integration between:

### Control Loop Architecture
```
Pilot Input → Control_FMU → Control Surface Commands
                   ↓
         [Control Laws, DAL-A]
                   ↓
    Aero_FMU ← → Struct_FMU ← → Propulsion_FMU
       ↓              ↓              ↓
   Aerodynamic    Structural     Propulsion
   Coefficients   Deflections    Forces
       ↓              ↓              ↓
   └──────────→ Feedback ←─────────┘
```

### Example Signal Chain (Elevator)
```
pilot_stick_pitch (Control_FMU, 50 Hz)
    → elevator_cmd (Control_FMU → Aero_FMU, 50 Hz)
        → lift_coefficient (Aero_FMU → Struct_FMU, 100 Hz)
            → elevator_position_fb (Struct_FMU → Control_FMU, 100 Hz)
```

### Validation Test Vector Example
**TV-ATA27-001**: Elevator step response
- **Requirement**: REQ-FC-ELEVATOR-001 (response time < 200 ms)
- **Scenario**: Step input from 0° to 5° pitch
- **Expected**: Elevator deflects to -3.5° within 200 ms
- **Validation**: Position error < 0.1°, rate limit ≤ 30°/s
- **Result**: See `TESTS/VECTORS/TV-ATA27-001_elevator_step.yaml`

Full test vectors and validation results in [TESTS/VECTORS/](TESTS/VECTORS/)

## Connection Matrix

Signal connections between FMUs are defined in [INTERFACES/mapping.csv](INTERFACES/mapping.csv).

Example connections:
```
Control_FMU.elevator_cmd → Aero_FMU.elevator_deflection (50 Hz, DAL-A)
Control_FMU.elevator_cmd → Struct_FMU.elevator_input (50 Hz, DAL-A)
Struct_FMU.elevator_position_fb → Control_FMU.elevator_sensor (100 Hz)
Aero_FMU.lift_coefficient → Struct_FMU.aerodynamic_lift (100 Hz)
Aero_FMU.drag_coefficient → Propulsion_FMU.drag_input (100 Hz)
Propulsion_FMU.thrust_output → Aero_FMU.thrust_input (10 Hz)
H2_FMU.fuel_flow → Propulsion_FMU.fuel_available (1 Hz)
```

Full connection matrix with all 37+ signal connections: [INTERFACES/mapping.csv](INTERFACES/mapping.csv)

## Quick Start

### 1. Explore Signal Interfaces
```bash
cd INTERFACES/
cat signals.yaml  # Review signal definitions
cat units.yaml    # Review unit conversions
cat mapping.csv   # Review FMU connections
```

### 2. Review Specifications
```bash
cd SPECS/
cat fmi_config.yaml  # FMI configuration, tolerances, step sizes
```

### 3. Run Test Vector
```bash
cd TOOLS/scripts/
python run_test_vector.py \
    --test-vector ../../TESTS/VECTORS/TV-ATA27-001_elevator_step.yaml \
    --output ../../SIM/results/
```

### 4. View Results
```bash
cd SIM/results/
cat TV-ATA27-001_results.csv    # Time series data
cat TV-ATA27-001_report.txt     # Test report
```

## Key Features

### FMI 3.0 Enhancements
- **Event Handling**: Mode changes, actuator faults, discrete events
- **Clocks**: Periodic clocks for hybrid co-simulation (50 Hz control, 100 Hz aero)
- **Continuous Outputs**: Smooth interpolation between time steps
- **Improved Initialization**: Dedicated initialization mode with algebraic loop solving

### Safety-Critical Support
- **DAL-A/B Compliance**: Safety-critical signals identified (DO-178C)
- **Redundancy**: Triple/quadruple voting for primary controls
- **Fault Injection**: Test vectors for actuator jams, sensor failures
- **Determinism**: Reproducible results for verification

### Traceability
- **EBOM References**: All signals linked to Engineering Bill of Materials
- **Requirements**: Traceable to system requirements (ATA-27)
- **Test Coverage**: Comprehensive test vectors validating each requirement

## Related Documents

### Internal References
- [INTERFACES/signals.yaml](INTERFACES/signals.yaml) - Complete signal definitions
- [INTERFACES/units.yaml](INTERFACES/units.yaml) - Unit standards and conversions
- [SPECS/fmi_config.yaml](SPECS/fmi_config.yaml) - FMI configuration
- [TESTS/VECTORS/](TESTS/VECTORS/) - Validation test vectors
- [TOOLS/](TOOLS/) - Build and test automation scripts

### System Configuration
- [../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/](../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/) - Flight control system configuration
- [../../03-INTERFACES_APIS/](../../03-INTERFACES_APIS/) - Digital twin API specifications

### Co-Simulation Documentation
- [../ORCHESTRATION.md](../ORCHESTRATION.md) - Master algorithm, error control

## Standards and Compliance

### FMI Standards
- **FMI 3.0**: Primary (with FMI 2.0 fallback)
- **Co-Simulation**: Selected interface type
- **Compliance Checking**: All FMUs validated with FMI Compliance Checker

### Aviation Standards
- **DO-178C**: Software (DAL-A for flight controls)
- **DO-254**: Hardware (DAL-A for flight controls)
- **ARP-4754A**: System development and verification
- **ATA iSpec 2200**: ATA chapter organization

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-10-11 | Digital Twin Team | Initial FMU structure with ATA-27 focus |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
