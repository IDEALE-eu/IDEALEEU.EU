# 04-ALGORITHMS

Federated learning algorithms, aggregation methods, and optimization techniques.

## Purpose

This directory contains specifications for FL algorithms, compression techniques, drift detection, and robust aggregation methods.

## Contents

- **00-README.md** - This file
- **FEDAVG.md** - Federated Averaging algorithm
- **FEDPROX.md** - FedProx (proximal term for heterogeneous clients)
- **FEDOPT.md** - FedOpt (adaptive optimizers: FedAdam, FedYogi)
- **COMPRESSION.md** - Quantization (FP16→INT8), sparsification
- **DRIFT_DETECTION.md** - PSI, KS test, concept drift alerts
- **ROBUST_AGGREGATION.md** - Krum, TrimmedMean (Byzantine resilience)

## Algorithm Selection

- **Default**: FedAvg (simple, well-tested)
- **Heterogeneous clients**: FedProx (handles system variability)
- **Fast convergence**: FedOpt (adaptive learning rates)
- **Adversarial**: Krum or TrimmedMean (Byzantine-resilient)

## Related Documents

- **../02-ORCHESTRATION/JOB_SPECS/** - Algorithm configuration in jobs
- **../05-PRIVACY_SECURITY/** - Privacy-preserving techniques
- **../12-METRICS/KPI_DEFINITIONS.md** - Algorithm performance metrics
