# COMPONENTS

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > COMPONENTS**

FMU component source code, build artifacts, and compiled FMU packages.

## Purpose

This directory contains the source code and compiled FMUs for each subsystem in the co-simulation environment.

## Directory Structure

Each component follows this structure:
```
COMPONENTS/
└── <component_name>/
    ├── src/                    # Source code (C/C++/Modelica)
    │   ├── fmi_interface.c     # FMI wrapper functions
    │   ├── model_logic.c       # Core model implementation
    │   └── modelDescription.xml # FMI model description
    ├── build/                  # Build artifacts (temporary)
    │   ├── obj/                # Object files
    │   └── lib/                # Intermediate libraries
    ├── fmu/                    # Compiled FMU packages
    │   └── <name>_cs_v1.0.0.fmu
    └── README.md               # Component-specific documentation
```

## FMU Components

### Control_FMU
**Flight Control Computer**
- **Purpose**: Implements flight control laws (pitch, roll, yaw)
- **Inputs**: Pilot commands, sensor feedback, air data
- **Outputs**: Control surface commands
- **Update Rate**: 50 Hz
- **DAL Level**: A (safety-critical)
- **Status**: TODO - Implement

### Aero_FMU
**Aerodynamics Model**
- **Purpose**: Computes aerodynamic forces and moments
- **Inputs**: Control surface deflections, angle of attack, Mach number
- **Outputs**: CL, CD, CM (lift, drag, moment coefficients)
- **Update Rate**: 100 Hz
- **DAL Level**: B
- **Status**: TODO - Implement

### Struct_FMU
**Structures and Actuators**
- **Purpose**: Structural dynamics and actuator models
- **Inputs**: Aerodynamic loads, control commands
- **Outputs**: Deflections, position feedback, hinge moments
- **Update Rate**: 100 Hz
- **DAL Level**: A (actuator feedback)
- **Status**: TODO - Implement

### Propulsion_FMU
**Propulsion System**
- **Purpose**: Engine and thrust management
- **Inputs**: Throttle, altitude, Mach number, drag
- **Outputs**: Thrust, fuel flow, exhaust gas temperature
- **Update Rate**: 10 Hz
- **DAL Level**: B
- **Status**: TODO - Implement

### H2_FMU
**Hydrogen Energy System**
- **Purpose**: H₂ storage, boil-off, fuel cell
- **Inputs**: Fuel demand, ambient temperature, altitude
- **Outputs**: Tank pressure, fuel flow, boil-off rate
- **Update Rate**: 1 Hz
- **DAL Level**: C
- **Status**: TODO - Implement

### Thermal_FMU
**Thermal Management**
- **Purpose**: Thermal model for avionics and fuel system
- **Inputs**: Heat sources, ambient temperature
- **Outputs**: Component temperatures
- **Update Rate**: 1 Hz
- **DAL Level**: C
- **Status**: TODO - Implement

## Building FMUs

### Using CMake
```bash
cd <component_name>/
mkdir build && cd build
cmake .. -DFMI_VERSION=3.0 -DFMI_TYPE=co-simulation
make
make package
```

Output: `fmu/<component>_cs_v1.0.0.fmu`

### Using pack_fmu.sh Script
```bash
cd ../../TOOLS/scripts/
./pack_fmu.sh --component Control_FMU \
              --version 1.0.0 \
              --fmi-version 3.0
```

## FMU Validation

### Compliance Checking
All FMUs must pass FMI Compliance Checker:
```bash
fmuCheck -h 0.01 -s 10 Control_FMU/fmu/Control_FMU_cs_v1.0.0.fmu
```

Results saved to: `../TESTS/compliance/`

### Unit Testing
Each component should include unit tests:
```bash
cd <component>/build/
ctest --verbose
```

## FMI Interface Requirements

### Required FMI Functions (Co-Simulation)
- `fmi3InstantiateCoSimulation()`
- `fmi3EnterInitializationMode()`
- `fmi3ExitInitializationMode()`
- `fmi3DoStep()`
- `fmi3Terminate()`
- `fmi3FreeInstance()`

### Variable Naming Convention
Variables must match [INTERFACES/signals.yaml](../INTERFACES/signals.yaml):
```c
// Example: Control_FMU outputs
fmi3Float64 elevator_cmd;      // deg
fmi3Float64 aileron_left_cmd;  // deg
fmi3Float64 aileron_right_cmd; // deg
fmi3Float64 rudder_cmd;        // deg
```

## Model Description XML

Each FMU must include `modelDescription.xml` following FMI 3.0 schema:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<fmiModelDescription
    fmiVersion="3.0"
    modelName="Control_FMU"
    description="Flight Control Computer"
    generationTool="Custom"
    generationDateAndTime="2025-10-11T00:00:00Z">
    
    <CoSimulation
        modelIdentifier="Control_FMU"
        canHandleVariableCommunicationStepSize="true"
        canInterpolateInputs="true"/>
    
    <ModelVariables>
        <Float64 name="elevator_cmd" valueReference="1" causality="output" unit="deg"/>
        <!-- ... more variables ... -->
    </ModelVariables>
</fmiModelDescription>
```

## Version Control

### FMU Versioning
- **Semantic versioning**: MAJOR.MINOR.PATCH
- **Naming convention**: `<name>_cs_vMAJOR.MINOR.PATCH.fmu`
- **Change tracking**: Update CHANGELOG.md in each component

### Source Code
- All source code in Git
- Tag releases: `v1.0.0`
- Build artifacts (.fmu files) can be in Git LFS or artifact storage

## Best Practices

### Code Quality
1. **Modularity**: Separate FMI interface from model logic
2. **Testability**: Unit tests for model functions
3. **Documentation**: Inline comments and README
4. **Error handling**: Return proper FMI status codes
5. **Memory management**: No leaks, proper cleanup

### Performance
1. **Optimize hot paths**: doStep() should be fast
2. **Preallocate buffers**: Avoid dynamic allocation in doStep()
3. **Profile**: Measure execution time
4. **Cache**: Cache expensive calculations

### Safety-Critical (DAL-A)
1. **DO-178C compliance**: Follow coding standards
2. **Certification artifacts**: Save all evidence
3. **Traceability**: Link code to requirements
4. **Static analysis**: Use tools like Polyspace, Coverity
5. **Code coverage**: 100% MC/DC for DAL-A

## Related Documents

- [../INTERFACES/signals.yaml](../INTERFACES/signals.yaml) - Signal interface definitions
- [../SPECS/fmi_config.yaml](../SPECS/fmi_config.yaml) - FMI configuration
- [../TOOLS/](../TOOLS/) - Build scripts and utilities
- [../TESTS/compliance/](../TESTS/compliance/) - FMU compliance reports

## References

- **FMI 3.0 Specification**: https://fmi-standard.org/docs/3.0/
- **FMI Compliance Checker**: https://github.com/modelica-tools/FMUComplianceChecker

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
