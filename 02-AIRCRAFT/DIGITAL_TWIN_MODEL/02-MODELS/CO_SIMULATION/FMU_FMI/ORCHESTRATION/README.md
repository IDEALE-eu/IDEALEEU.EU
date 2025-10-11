# ORCHESTRATION

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > ORCHESTRATION**

Master algorithm and co-simulation orchestration configuration.

## Purpose

This directory contains the master co-simulation algorithm that coordinates execution of multiple FMUs according to the FMI 3.0 standard.

## Directory Structure

```
ORCHESTRATION/
├── configs/                    # Scenario configurations
│   └── flight_controls.yaml    # Flight control scenario
├── master_python.py            # Python master algorithm (TODO)
├── master_cpp.cpp              # C++ master algorithm (TODO)
└── README.md
```

## Master Algorithm

The master algorithm is responsible for:
1. **FMU Initialization**: Load and initialize all FMUs
2. **Time Stepping**: Advance simulation time in coordinated steps
3. **Variable Exchange**: Transfer outputs to inputs between FMUs
4. **Event Handling**: Process discrete events (FMI 3.0)
5. **Error Control**: Monitor and manage numerical errors
6. **Termination**: Gracefully shut down simulation

### Communication Schemes

**Jacobi (Parallel)**
- All FMUs step simultaneously using inputs from t_n
- Advantages: Natural parallelization, better performance
- Disadvantages: May require smaller step sizes

**Gauss-Seidel (Sequential)**
- FMUs step sequentially using latest available outputs
- Advantages: Better numerical stability
- Disadvantages: No parallelization

Configuration: [../SPECS/fmi_config.yaml](../SPECS/fmi_config.yaml)

## Scenario Configurations

Example: `configs/flight_controls.yaml`
```yaml
scenario:
  name: "ATA-27 Flight Control Validation"
  duration: 10.0 s
  master_step: 0.01 s
  
fmus:
  - name: Control_FMU
    path: "../COMPONENTS/Control_FMU/fmu/Control_FMU_cs_v1.0.0.fmu"
    step_size: 0.02 s
  - name: Aero_FMU
    path: "../COMPONENTS/Aero_FMU/fmu/Aero_FMU_cs_v1.0.0.fmu"
    step_size: 0.01 s
  - name: Struct_FMU
    path: "../COMPONENTS/Struct_FMU/fmu/Struct_FMU_cs_v1.0.0.fmu"
    step_size: 0.01 s
    
connections:
  - source: Control_FMU.elevator_cmd
    destination: Aero_FMU.elevator_deflection
  - source: Aero_FMU.lift_coefficient
    destination: Struct_FMU.aerodynamic_lift
```

## Related Documents

- [../SPECS/fmi_config.yaml](../SPECS/fmi_config.yaml) - Algorithm configuration
- [../ORCHESTRATION.md](../../ORCHESTRATION.md) - Detailed orchestration documentation

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
