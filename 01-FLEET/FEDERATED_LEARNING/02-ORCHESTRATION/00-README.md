# 02-ORCHESTRATION

Federated learning orchestration, scheduling, and client coordination.

## Purpose

This directory defines how FL training rounds are coordinated across distributed clients, including scheduling policies, client selection algorithms, connectivity management, and job specifications.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**SCHEDULER.md**](SCHEDULER.md) - Training round schedules (e.g., weekly during SATCOM windows)
- [**CLIENT_SELECTION.md**](CLIENT_SELECTION.md) - Fairness, eligibility criteria, and selection algorithms
- [**CONNECTIVITY_PROFILES.md**](CONNECTIVITY_PROFILES.md) - Bandwidth caps, blackout recovery (LEO vs. GEO)
- [**JOB_SPECS/**](JOB_SPECS/) -  FL job specifications and templates

## Orchestration Architecture

### Components

```
┌─────────────────────────────────────────────┐
│         Orchestration Controller             │
│  (Ground-based, runs at aggregation server)  │
└───────────┬─────────────────────────────────┘
            │
    ┌───────┼────────┐
    │       │        │
    ▼       ▼        ▼
Scheduler  Client  Connectivity
           Selector  Manager
    │       │        │
    └───────┼────────┘
            │
    ┌───────▼────────┐
    │  FL Clients     │
    │ (Aircraft, GS)  │
    └─────────────────┘
```

### Workflow

1. **Job Submission**: AI/ML Team defines FL job (model, hyperparameters, data contract)
2. **Scheduling**: Scheduler selects training round time (aligned with SATCOM windows)
3. **Client Selection**: Selector identifies eligible clients (based on health, fairness, data quality)
4. **Model Distribution**: Global model broadcasted to selected clients
5. **Local Training**: Clients train locally on their data
6. **Update Collection**: Clients upload gradients/weights during connectivity window
7. **Aggregation**: Server aggregates updates into new global model
8. **Validation**: Model validated against holdout set
9. **Deployment**: New model distributed (if validation passed)

## Design Principles

### Asynchronous FL
- Clients train at their own pace (no global synchronization barrier)
- Aggregator accepts updates from stragglers (with time limit)
- Enables heterogeneous clients (aircraft vs. ground stations)

### Fault Tolerance
- Client dropout: Aggregation proceeds with minimum quorum (10 clients)
- Network partition: Store-and-forward queue for delayed updates
- Aggregator failure: Active-passive redundancy with <60s failover

### Scalability
- Horizontal scaling: Multiple aggregators for hierarchical topology
- Vertical scaling: Batched aggregation for high client count
- Adaptive batch size: Adjust based on server load and network bandwidth

### Security
- Authenticated clients only (X.509 certificates)
- Encrypted model updates (TLS 1.3)
- Secure aggregation (optional, see 05-PRIVACY_SECURITY/)

## Integration Points

### Upstream Dependencies
- [**01-ARCHITECTURE/FL_TOPOLOGY.md**](01-ARCHITECTURE/FL_TOPOLOGY.md) - Network topology and communication patterns
- [**01-ARCHITECTURE/CLIENT_TYPES.md**](01-ARCHITECTURE/CLIENT_TYPES.md) - Client capabilities and constraints
- [**06-MODELS/REGISTRY.md**](06-MODELS/REGISTRY.md) - Model versioning and storage

### Downstream Consumers
- [**03-CLIENTS/**](03-CLIENTS/) -  Receives job specifications and training schedules
- [**04-ALGORITHMS/**](04-ALGORITHMS/) -  Executes aggregation algorithms
- [**12-METRICS/**](12-METRICS/) -  Reports orchestration metrics (participation rate, round time)

## Related Documents

- [**03-CLIENTS/AIRCRAFT_EDGE/RUNTIME_CONSTRAINTS.md**](03-CLIENTS/AIRCRAFT_EDGE/RUNTIME_CONSTRAINTS.md) - Client-side resource limits
- [**09-DEPLOYMENT/ROLLOUT_STRATEGY.md**](09-DEPLOYMENT/ROLLOUT_STRATEGY.md) - Model deployment procedures
- [**10-GOVERNANCE/MAL-FE/POLICY.md**](10-GOVERNANCE/MAL-FE/POLICY.md) - Fleet experiments approval workflow

## Status

**Phase**: Orchestration Design  
**Owner**: AI/ML Team - FL Engineers  
**Last Review**: 2024-Q4
