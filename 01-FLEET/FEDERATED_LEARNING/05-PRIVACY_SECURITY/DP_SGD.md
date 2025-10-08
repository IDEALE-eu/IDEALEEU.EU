# DP_SGD

Differential Privacy via DP-SGD (Differentially Private Stochastic Gradient Descent).

## Overview

DP-SGD adds calibrated noise to gradients during training to provide (ε, δ)-differential privacy guarantees.

## Privacy Budgets

- **ε (epsilon)**: Privacy loss parameter (lower = more private)
  - ε ≤ 1.0: Strong privacy
  - 1.0 < ε ≤ 5.0: Moderate privacy
  - ε > 5.0: Weak privacy
- **δ (delta)**: Failure probability (typically 1e-5 for n=10,000 clients)

## Implementation

```python
# Pseudo-code for DP-SGD
def dp_sgd_step(gradients, C, σ):
    # Clip gradients
    clipped_grads = [clip(g, C) for g in gradients]
    
    # Add Gaussian noise
    noisy_grads = [g + N(0, σ²C²) for g in clipped_grads]
    
    return noisy_grads
```

## Hyperparameters

- **C (clipping norm)**: 1.0 (max gradient norm)
- **σ (noise multiplier)**: 1.1 (higher = more noise, more privacy)
- **Sampling rate**: q = K/N (fraction of clients per round)
- **Composition**: Track privacy budget across rounds (privacy accountant)

## Privacy Accountant

- **Rényi DP**: Tight composition bounds
- **Log every round**: (ε_t, δ_t) to 12-METRICS/
- **Alert if ε_total > ε_budget**: Stop training, retrain with higher noise

## Related Documents

- [**SECURE_AGGREGATION.md**](SECURE_AGGREGATION.md) - Combine with secure aggregation for stronger privacy
- [**../11-COMPLIANCE/PRIVACY.md**](../11-COMPLIANCE/PRIVACY.md) - GDPR compliance
