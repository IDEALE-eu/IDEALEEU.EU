# SCHEDULER

Federated learning training round scheduler and timing policies.

## Overview

The FL scheduler coordinates training rounds across distributed clients, optimizing for:
- SATCOM availability windows (LEO/GEO satellite connectivity)
- Client computational capacity (avoid overloading edge devices)
- Model convergence speed (balance frequency vs. quality)
- Operational constraints (no training during critical flight phases)

## Scheduling Policies

### Weekly Training Rounds (Default)

**Schedule:**
- Training rounds initiated **every 7 days**
- Aligned with SATCOM window availability
- Launch time: **Sunday 00:00 UTC** (low air traffic period)

**Rationale:**
- Weekly cadence balances model freshness with bandwidth costs
- Sunday launch aligns with lowest aircraft utilization
- 7-day window allows all aircraft to complete ≥1 flight

**Timeline:**
```
Sunday 00:00 UTC  : Global model v1.0 distributed
Sunday-Saturday   : Clients train locally (7-day window)
Saturday 12:00 UTC: Aggregation deadline (72-hour upload window)
Sunday 00:00 UTC  : Global model v1.1 distributed
```

### Bi-Weekly Training Rounds (Low-Bandwidth)

**Schedule:**
- Training rounds every **14 days**
- Used for large models (>100 MB) or limited bandwidth scenarios
- Launch time: **1st and 15th of each month, 00:00 UTC**

### On-Demand Training Rounds (Experimental)

**Trigger Conditions:**
- New aircraft joins fleet (model initialization)
- Critical model drift detected (KS test p-value < 0.05)
- Safety incident requires model update (see 16-INCIDENT_RESPONSE/)
- A/B test for new algorithm (see 07-EXPERIMENTS/AB_TESTS/)

**Approval:**
- Requires MAL-FE (Fleet Experiments) approval
- Documented in 10-GOVERNANCE/MAL-FE/POLICY.md

## SATCOM Window Alignment

### LEO Satellite Windows (Starlink, OneWeb)

**Characteristics:**
- Latency: 20-40 ms
- Bandwidth: 50-200 Mbps downlink, 10-40 Mbps uplink
- Availability: 95%+ globally (polar coverage)
- Window duration: Continuous (no orbital gaps)

**Scheduling:**
- No special windowing required (always available)
- Upload models during cruise phase (altitude > 10,000 ft)

### GEO Satellite Windows (Traditional SATCOM)

**Characteristics:**
- Latency: 500-700 ms
- Bandwidth: 1-10 Mbps (shared across fleet)
- Availability: 80-90% (coverage gaps over poles)
- Window duration: Variable (depends on orbit position)

**Scheduling:**
- Pre-scheduled upload windows (4-hour blocks)
- Priority queue: Critical updates first, FL updates second
- Fallback: Store-and-forward via ground station

## Client Training Windows

### Aircraft Clients

**Training Phase:**
- Local training starts upon global model reception
- Training runs during **cruise phase only** (altitude > 10,000 ft)
- Automatic suspension during:
  - Takeoff and landing (critical flight phases)
  - High CPU load (> 70% from other systems)
  - Thermal throttling (CPU temp > 75°C)

**Upload Phase:**
- Upload window: **72 hours before aggregation deadline**
- Retry policy: Exponential backoff (1min, 5min, 15min, 60min)
- Timeout: 10 minutes per upload attempt
- Fallback: Store gradients, upload during next flight

### Ground Station Clients

**Training Phase:**
- Continuous training (no flight phase restrictions)
- Prioritized during off-peak hours (2:00-6:00 local time)

**Upload Phase:**
- Immediate upload upon training completion
- No bandwidth restrictions (fiber connection)

### Simulation Rig Clients

**Training Phase:**
- On-demand training (triggered by experiment launch)
- Parallelized across multiple rigs

**Upload Phase:**
- Immediate upload (data center LAN, <1 second)

## Aggregation Schedule

### Aggregation Window

**Collection Phase:**
- **Duration**: 72 hours (Friday 00:00 UTC - Saturday 12:00 UTC)
- **Minimum quorum**: 10 clients (fail-safe: do not aggregate if < 10)
- **Deadline**: Hard cutoff at Saturday 12:00 UTC
- **Stragglers**: Updates after deadline queued for next round

**Aggregation Phase:**
- **Start**: Saturday 12:00 UTC
- **Duration**: ~30 minutes (depends on client count and algorithm)
- **Algorithm**: FedAvg (default), FedProx, or FedOpt (see 04-ALGORITHMS/)
- **Validation**: 2-hour validation window on holdout dataset

**Distribution Phase:**
- **Start**: Sunday 00:00 UTC
- **Duration**: 24 hours (progressive rollout)
- **Canary**: First 5 aircraft receive new model, monitored for 24h
- **Full rollout**: If canary successful, deploy to all clients

## Dynamic Scheduling

### Adaptive Intervals

**Triggers for Shorter Intervals:**
- High model drift detected (PSI > 0.2, see 04-ALGORITHMS/DRIFT_DETECTION.md)
- New aircraft type added to fleet (faster convergence needed)
- Incident response (see 16-INCIDENT_RESPONSE/)

**Triggers for Longer Intervals:**
- Model converged (validation loss plateau for 3 rounds)
- Bandwidth constraints (excessive SATCOM costs)
- Fleet downtime (maintenance season)

**Adjustment Policy:**
- Changes approved by AI/ML Team Lead
- Communicated to fleet 48 hours in advance
- Documented in 09-DEPLOYMENT/CHANGELOG.md

## Scheduling Configuration

### Current Configuration (YAML)

```yaml
scheduler:
  default_policy: weekly
  
  weekly:
    interval: 7 days
    launch_time: "Sunday 00:00 UTC"
    aggregation_deadline: "Saturday 12:00 UTC"
    upload_window: 72 hours
    
  bi_weekly:
    interval: 14 days
    launch_days: [1, 15]
    launch_time: "00:00 UTC"
    
  client_windows:
    aircraft:
      training_phases: ["cruise"]  # altitude > 10,000 ft
      upload_retry: [1m, 5m, 15m, 60m]
      upload_timeout: 10 minutes
      
    ground_stations:
      training_phases: ["continuous"]
      upload_retry: [1m, 5m]
      upload_timeout: 5 minutes
      
    sim_rigs:
      training_phases: ["on_demand"]
      upload_retry: [30s]
      upload_timeout: 1 minute
  
  aggregation:
    quorum_min: 10
    deadline_hard: true
    timeout: 30 minutes
    
  distribution:
    canary_count: 5
    canary_duration: 24 hours
    rollout_duration: 24 hours
```

## Monitoring and Alerts

### Key Metrics
- **Client participation rate**: % of eligible clients that contributed to round
- **Round completion time**: Time from launch to distribution
- **Aggregation delay**: Time waiting for minimum quorum
- **Upload failures**: Count of failed upload attempts

### Alerting Thresholds
- Participation rate < 50%: Warning (investigate client health)
- Participation rate < 30%: Critical (abort round, rollback)
- Aggregation delay > 12 hours: Warning (check network, stragglers)
- Upload failures > 20%: Critical (SATCOM outage suspected)

**Alert Routing:**
- Slack: #fl-ops-alerts
- PagerDuty: FL Operations Team (on-call)
- Email: AI/ML Team Lead

## Related Documents

- **CLIENT_SELECTION.md** - How clients are selected for each round
- **CONNECTIVITY_PROFILES.md** - Network bandwidth and latency specifications
- **01-ARCHITECTURE/FL_TOPOLOGY.md** - Communication patterns
- **12-METRICS/KPI_DEFINITIONS.md** - Scheduler performance metrics

## Change History

| Version | Date    | Changes                        | Author         |
|---------|---------|--------------------------------|----------------|
| 1.0     | 2024-Q4 | Initial scheduler policy       | AI/ML Team     |
