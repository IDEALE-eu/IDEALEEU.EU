# Full System Co-Simulation

## Overview

Coupled CFD simulation of complete CO₂ endocircular battery system using preCICE.

## Architecture

```
┌─────────────┐     preCICE     ┌──────────────┐
│ Tank CFD    │ ←────────────→ │ Controller   │
└─────────────┘                 └──────────────┘
       ↓                               ↓
┌─────────────┐                 ┌──────────────┐
│ Evap CFD    │ ←────────────→ │ Flow Control │
└─────────────┘                 └──────────────┘
       ↓                               ↓
┌─────────────┐                 ┌──────────────┐
│ Expand CFD  │ ←────────────→ │ Power Output │
└─────────────┘                 └──────────────┘
       ↓                               ↓
┌─────────────┐                 ┌──────────────┐
│ Cond CFD    │ ←────────────→ │ Heat Reject  │
└─────────────┘                 └──────────────┘
```

## Coupling Strategy

- **Explicit**: Fast, may require small time steps
- **Implicit**: Stable, larger time steps, iterative

## Exchanged Data

- Mass flow rates [kg/s]
- Pressures [Pa]
- Temperatures [K]
- Power output [W]
- Control signals

## Running Co-Simulation

```bash
# Start preCICE server
precice-server &

# Start each component
python scripts/co_simulation.py --component tank &
python scripts/co_simulation.py --component evaporator &
python scripts/co_simulation.py --component expander &
python scripts/co_simulation.py --component condenser &
python scripts/co_simulation.py --component controller

# Monitor
precice-profiling
```

## Key Outputs

- System-level efficiency
- Transient response
- Control stability
- Cycle performance metrics

## Notes

- Requires preCICE v2.5+
- Configure coupling time windows carefully
- Use conservative data mapping for mass conservation
