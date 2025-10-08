# FEDPROX

FedProx algorithm for heterogeneous federated learning.

## Overview

FedProx adds a proximal term to the local objective, making it more robust to client heterogeneity (varying compute, data distributions, staleness).

## Algorithm

Same as FedAvg, but local training objective is modified:

```
Client k:
  Local objective: L(w) + (μ/2) * ||w - w_global||^2
  
  # Proximal term penalizes deviation from global model
```

## Hyperparameters

- **μ (proximal term)**: 0.001-0.1 (higher = more regularization)
- Other hyperparameters same as FedAvg

## Advantages

- Robust to heterogeneous clients (different compute speeds, data distributions)
- Handles stragglers gracefully (late updates less harmful)
- Better convergence than FedAvg in non-IID settings

## Use Cases

- Aircraft with varying flight profiles (short-haul vs. long-haul)
- Mixed client types (aircraft, ground stations, sim rigs)
- High system heterogeneity

## Related Documents

- **FEDAVG.md** - Baseline algorithm
- **../02-ORCHESTRATION/CLIENT_SELECTION.md** - Client heterogeneity
