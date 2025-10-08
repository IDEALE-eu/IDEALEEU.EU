# FEDOPT

FedOpt: Federated learning with adaptive server-side optimizers.

## Overview

FedOpt applies adaptive optimizers (Adam, Yogi) on the server side, accelerating convergence compared to vanilla FedAvg.

## Variants

- **FedAdam**: Server uses Adam optimizer
- **FedYogi**: Server uses Yogi optimizer (more stable than Adam)
- **FedAdagrad**: Server uses Adagrad (adaptive learning rates)

## Algorithm

```
Server:
  Initialize optimizer (e.g., Adam with β1=0.9, β2=0.999)
  
  for round t = 1 to T:
    Δ_t = AggregateUpdates()  # Pseudo-gradient
    w_global_{t+1} = Optimizer.step(w_global_t, Δ_t)
```

## Hyperparameters

- **Server learning rate**: 0.01-0.1 (higher than FedAvg)
- **β1, β2**: 0.9, 0.999 (Adam defaults)
- **Client learning rate**: 0.001-0.01

## Advantages

- Faster convergence (fewer rounds needed)
- Better for non-IID data
- Adaptive to gradient magnitudes

## Use Cases

- When communication is expensive (LEO/GEO satellite)
- Need fast convergence (urgent model updates)
- Non-IID data distributions

## Related Documents

- **FEDAVG.md** - Baseline algorithm
- **../02-ORCHESTRATION/CONNECTIVITY_PROFILES.md** - Communication costs
