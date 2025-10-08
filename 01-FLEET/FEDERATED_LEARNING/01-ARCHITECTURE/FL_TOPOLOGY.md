# FL_TOPOLOGY

Federated learning network topology and communication patterns.

## Overview

The IDEALE FL system employs a **star topology** for initial deployment, with scalability to **hierarchical topology** as the fleet grows. This design balances simplicity, reliability, and regulatory compliance.

## Topology Options

### Star Topology (Current)

```
                    ┌─────────────────┐
                    │  Aggregation    │
                    │     Server      │
                    │   (Ground HQ)   │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
    ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
    │  Aircraft 1  │   │  Aircraft 2  │   │  Aircraft N  │
    │  (Edge FL)   │   │  (Edge FL)   │   │  (Edge FL)   │
    └──────────────┘   └──────────────┘   └──────────────┘
           │                 │                 │
    ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
    │   Ground     │   │   Ground     │   │   Sim Rig   │
    │  Station 1   │   │  Station 2   │   │     HIL     │
    └──────────────┘   └──────────────┘   └──────────────┘
```

**Advantages:**
- Simple coordination and debugging
- Single point of aggregation for auditing
- Clear regulatory oversight
- Lower latency for model distribution

**Limitations:**
- Single point of failure (mitigated by redundancy)
- Scaling challenges beyond 500 clients
- Central bandwidth bottleneck

### Hierarchical Topology (Future)

```
                    ┌─────────────────┐
                    │  Global Server  │
                    │   (Ground HQ)   │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
    ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
    │  Regional    │   │  Regional    │   │  Regional    │
    │  Aggregator  │   │  Aggregator  │   │  Aggregator  │
    │  (Europe)    │   │  (Americas)  │   │  (Asia-Pac)  │
    └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
           │                 │                 │
      ┌────┴────┐       ┌────┴────┐       ┌────┴────┐
      │Aircraft │       │Aircraft │       │Aircraft │
      │ Cluster │       │ Cluster │       │ Cluster │
      └─────────┘       └─────────┘       └─────────┘
```

**Advantages:**
- Scalable to 1000+ clients
- Geographic distribution reduces latency
- Fault isolation (regional failures)
- Better bandwidth utilization

**Triggers for Transition:**
- Fleet size > 200 active FL clients
- Regional latency > 5 seconds
- Compliance requirement for regional data residency

## Cross-Silo Communication

### Aircraft ↔ Ground (Primary)

**Communication Channel:**
- **LEO Satellite**: Starlink, OneWeb (low latency, moderate bandwidth)
- **GEO Satellite**: Traditional SATCOM (higher latency, lower bandwidth)
- **Fallback**: Store-and-forward via ground station when landed

**Training Round Flow:**
1. Aircraft receives global model from aggregation server
2. Aircraft trains locally on telemetry data (hours to days)
3. Aircraft uploads gradients/weights during SATCOM window
4. Aggregation server combines updates from all clients
5. New global model distributed in next training round

**Bandwidth Optimization:**
- Gradient compression (FP32 → FP16 → INT8)
- Sparsification (top-k gradients only)
- Scheduled upload windows (weekly/bi-weekly)

### Ground Stations (Secondary)

**Communication Channel:**
- High-bandwidth fiber/ethernet connections
- Continuous connectivity (no scheduling constraints)

**Role:**
- Supplement aircraft data with ground-based simulations
- Provide high-fidelity models for validation
- Act as fallback aggregators in hierarchical mode

### Simulation Rigs (Tertiary)

**Communication Channel:**
- Internal network (data center or lab)
- Continuous connectivity, highest bandwidth

**Role:**
- HIL (Hardware-in-Loop) and SIL (Software-in-Loop) validation
- Synthetic data generation for edge cases
- Pre-flight testing of FL algorithms

## Communication Protocols

### Synchronization Strategy

**Asynchronous Training:**
- Clients train at their own pace
- Aggregator combines updates as they arrive
- No requirement for all clients to participate in each round

**Scheduled Rounds:**
- Weekly training rounds (aligned with SATCOM availability)
- 7-day local training window
- 24-hour upload window for model updates

### Security Protocols

- **TLS 1.3** for all client-server communication
- **Mutual authentication** using X.509 certificates
- **Secure aggregation** (Threshold Paillier or MPC)
- **Payload encryption** for model weights

### Failure Handling

- **Client dropout**: Aggregation proceeds with available clients (minimum 10)
- **Network partition**: Store-and-forward queue for delayed updates
- **Server failure**: Redundant aggregators with active-passive failover
- **Byzantine clients**: Krum or TrimmedMean aggregation (see 04-ALGORITHMS/ROBUST_AGGREGATION.md)

## Topology Configuration

### Current Deployment

```yaml
topology:
  type: star
  aggregation_server:
    location: Ground HQ (primary data center)
    redundancy: active-passive
    failover_time: < 60 seconds
  
  clients:
    aircraft:
      count: 50 (target: 200)
      connectivity: LEO/GEO satellite
      training_interval: 7 days
    
    ground_stations:
      count: 5
      connectivity: fiber
      training_interval: continuous
    
    sim_rigs:
      count: 10
      connectivity: data center LAN
      training_interval: on-demand
```

### Scalability Plan

- **Phase 1 (0-100 clients)**: Single star topology
- **Phase 2 (100-300 clients)**: Star with regional load balancers
- **Phase 3 (300+ clients)**: Transition to hierarchical topology

## Compliance Considerations

### DO-326A (Airworthiness Security)
- All communication channels authenticated and encrypted
- Segregated from flight-critical avionics systems
- No direct actuation from FL models

### GDPR (Data Protection)
- Pseudonymised client IDs (no tail numbers in clear)
- Model updates contain no raw telemetry data
- Right to erasure: client can opt-out and have gradients deleted

### ITAR/EAR (Export Control)
- Model architectures and weights subject to export review
- Regional aggregators constrain data to approved jurisdictions

## Related Documents

- **CLIENT_TYPES.md** - Client implementation details
- **DATA_CONTRACTS/** - Data schemas for model updates
- **02-ORCHESTRATION/CONNECTIVITY_PROFILES.md** - Network specifications
- **05-PRIVACY_SECURITY/SECURE_AGGREGATION.md** - Cryptographic protocols

## Change History

| Version | Date    | Changes                          | Author    |
|---------|---------|----------------------------------|-----------|
| 1.0     | 2024-Q4 | Initial star topology definition | AI/ML Team|
