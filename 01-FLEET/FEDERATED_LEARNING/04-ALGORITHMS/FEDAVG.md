# FEDAVG

Federated Averaging (FedAvg) algorithm specification.

## Overview

FedAvg is the baseline federated learning algorithm. Clients train locally for E epochs, then server aggregates model weights using weighted averaging.

## Algorithm

```
Server (aggregation):
  for round t = 1 to T:
    S_t = SelectClients()  # Sample K clients
    w_global_t = 0
    total_samples = 0
    
    for each client k in S_t:
      Send w_global_t to client k
      Receive w_k, n_k from client k  # n_k = number of samples
      w_global_t += (n_k / N) * w_k
      total_samples += n_k
    
    w_global_{t+1} = w_global_t  # Weighted average

Client k (local training):
  Receive w_global_t from server
  w_k = w_global_t
  
  for epoch e = 1 to E:
    for each batch B in local_data:
      w_k = w_k - η * ∇L(w_k; B)  # SGD update
  
  Send w_k, n_k to server
```

## Hyperparameters

- **E (local epochs)**: 1-10 (trade-off: communication vs. computation)
- **η (learning rate)**: 0.001-0.01 (client-side)
- **B (batch size)**: 32-128 (depends on client memory)
- **K (clients per round)**: 10-50 (minimum 10 for statistical validity)

## Advantages

- Simple, easy to implement
- Provable convergence (convex and non-convex settings)
- Efficient (minimal communication overhead)

## Limitations

- Assumes IID data (not always true in practice)
- Sensitive to client heterogeneity (varying compute, data distributions)
- No explicit privacy (use DP-SGD for privacy, see ../05-PRIVACY_SECURITY/DP_SGD.md)

## Related Documents

- **FEDPROX.md** - Extension for heterogeneous clients
- **COMPRESSION.md** - Reduce communication costs
- **../05-PRIVACY_SECURITY/DP_SGD.md** - Add differential privacy
