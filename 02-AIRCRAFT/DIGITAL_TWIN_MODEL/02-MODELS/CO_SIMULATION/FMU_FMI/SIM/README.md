# SIM - Simulation Scenarios and Results

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > SIM**

Simulation scenarios, execution logs, and result files.

## Directory Structure

```
SIM/
├── scenarios/          # Scenario definition files
├── runs/               # Execution logs and traces
└── results/            # Output data (CSV, MAT)
```

## Scenarios

Simulation scenarios define:
- Initial conditions
- Mission profile
- Input sequences
- FMU configuration

Example scenario files in `scenarios/`:
- `01_cruise_flight.yaml` - Steady cruise at 35,000 ft
- `02_climb_profile.yaml` - Climb from FL250 to FL350
- `03_descent_approach.yaml` - Descent and approach
- `04_maneuver_pull_up.yaml` - 2g pull-up maneuver

## Results

Simulation results are saved as:
- **CSV**: Time series data (readable)
- **MAT**: MATLAB format (for post-processing)
- **Logs**: Text logs of execution

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
