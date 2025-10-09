# Co-Simulation Architecture

## Overview

Multi-domain co-simulation for aircraft systems integration using FMI (Functional Mock-up Interface), ROS2, and Simulink.

## Architecture

### Simulation Master
- **Platform**: Simulink (MATLAB R2024a)
- **Role**: Orchestrates co-simulation, manages time synchronization

### FMU Components
- Flight control laws (exported from Simulink)
- Engine model (exported from AMESim)
- Hydraulic system (exported from SimulationX)
- Electrical network (exported from PLECS)

### ROS2 Integration
- Hardware-in-the-Loop (HIL) interfaces
- Real-time sensor data injection
- Actuator command distribution

## FMI Version
- **FMI 2.0** for co-simulation
- **FMI 3.0** (future upgrade planned)

## Simulation Scenarios

Defined in [SCENARIOS/](./SCENARIOS/) folder:
- Nominal flight profiles
- Failure modes (engine failure, hydraulic leak, electrical fault)
- Edge cases (turbulence, icing, crosswind landing)

## Results

Simulation results archived in [RESULTS/](./RESULTS/) folder with traceability to verification requirements.

## References

- [FMI_FMU_INDEX.csv](./FMI_FMU_INDEX.csv) - FMU component registry
- [07-INTEGRATION_TEST/RIGS_HILSILS/](../../07-INTEGRATION_TEST/RIGS_HILSILS/) - HIL/SIL configuration
