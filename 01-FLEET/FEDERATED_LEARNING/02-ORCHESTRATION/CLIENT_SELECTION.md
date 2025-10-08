# CLIENT_SELECTION

Federated learning client selection algorithms, fairness policies, and eligibility criteria.

## Overview

Client selection determines which aircraft, ground stations, and simulation rigs participate in each training round. The selection process balances:
- **Data diversity**: Ensure representative sampling across flight conditions, aircraft types, and operational scenarios
- **Resource efficiency**: Select clients with adequate compute, storage, and network capacity
- **Fairness**: Prevent bias toward high-connectivity or high-compute clients
- **Compliance**: Only select clients meeting safety and certification criteria

## Selection Criteria

### Eligibility Requirements

#### Aircraft Clients

**Pre-Flight Checks:**
- [ ] **No open NCRs** in FL-relevant systems (avionics, sensors, compute platform)
- [ ] **Minimum flight hours**: ≥ 50 hours since last FL model deployment
- [ ] **Hardware health**: CPU, memory, disk, network pass diagnostics
- [ ] **Data quality**: Telemetry completeness ≥ 95% in last 10 flights
- [ ] **Connectivity**: LEO or GEO SATCOM active and validated

**Certification Status:**
- [ ] **DO-178C compliance**: FL client software certified to Level C
- [ ] **Sandboxing active**: ARINC 653 partitioning enforced
- [ ] **Safety boundaries**: No flight-critical system interference

**Operational Status:**
- [ ] **Not AOG** (Aircraft On Ground)
- [ ] **Not in heavy maintenance** (C-check, D-check)
- [ ] **Active flight schedule**: ≥ 2 flights per week

#### Ground Station Clients

**Infrastructure Checks:**
- [ ] **Connectivity**: Fiber link active, latency < 50 ms
- [ ] **Compute capacity**: GPU available, memory ≥ 128 GB
- [ ] **Data access**: Full fleet dataset synchronized (no stale data)
- [ ] **Security**: ISO 27001 compliance, VPN active

**Operational Status:**
- [ ] **Not under maintenance**: No scheduled downtime in training window
- [ ] **Data quality**: No missing or corrupted telemetry batches

#### Simulation Rig Clients

**On-Demand Only:**
- Simulation rigs are selected manually for specific experiments
- Not part of routine training rounds (unless explicitly requested)

### Fairness Policies

#### Minimum Participation

**Per-Client Quotas:**
- Each eligible aircraft must participate in ≥ **3 training rounds per quarter**
- Ground stations participate in **all training rounds** (unless maintenance)
- Simulation rigs: On-demand only

**Rationale:**
- Ensures all aircraft benefit from FL (no "free riders")
- Prevents model bias toward high-participation clients

#### Data Distribution Balancing

**Stratified Sampling:**
- Sample clients proportionally across:
  - **Aircraft type**: Airbus A320, Boeing 737, Embraer E-Jet
  - **Flight phase distribution**: Short-haul (< 2h), medium-haul (2-6h), long-haul (> 6h)
  - **Environmental conditions**: Tropical, temperate, polar regions
  - **Age of aircraft**: New (< 5 years), mid-life (5-15 years), legacy (> 15 years)

**Sampling Method:**
- Use **weighted random sampling** with replacement
- Weights inversely proportional to recent participation frequency

#### Computational Fairness

**Aggregation Weights:**
- Clients with higher data quality or quantity receive higher weights
- FedAvg: Weight = `num_local_samples / total_samples`
- FedProx: Weight adjusted for system heterogeneity (see [04-ALGORITHMS/FEDPROX.md](04-ALGORITHMS/FEDPROX.md))

**Resource Normalization:**
- Aircraft (limited compute): Weight × 1.0
- Ground stations (high compute): Weight × 0.8 (to prevent dominance)
- Simulation rigs (synthetic data): Weight × 0.5 (lower trust)

## Selection Algorithms

### Algorithm 1: Random Selection (Default)

**Method:**
1. Query all eligible clients (meet criteria above)
2. Randomly sample **N clients** (e.g., N = 50)
3. Use stratified sampling to ensure diversity

**Pros:**
- Simple, easy to implement
- Unbiased (all clients have equal chance)

**Cons:**
- May miss critical data from specific clients
- No optimization for convergence speed

**Parameters:**
```yaml
algorithm: random
num_clients: 50
stratify_by: [aircraft_type, flight_phase]
```

### Algorithm 2: Importance Sampling

**Method:**
1. Compute importance score for each client:
   - Data quantity: Number of samples since last round
   - Data quality: Telemetry completeness, sensor calibration
   - Diversity: Underrepresented flight conditions
2. Sample clients with probability ∝ importance score
3. Ensure minimum participation quotas

**Pros:**
- Faster convergence (prioritizes informative data)
- Balances quantity and quality

**Cons:**
- More complex, requires metric tracking
- Risk of overfitting to "important" clients

**Scoring Formula:**
```
importance_score = 
  α * data_quantity_normalized +
  β * data_quality_score +
  γ * diversity_score
  
where α=0.4, β=0.3, γ=0.3
```

### Algorithm 3: Active Learning

**Method:**
1. Train a surrogate model to predict client contribution to global model loss
2. Select clients with highest predicted loss reduction
3. Incorporate exploration (ε-greedy: 10% random selection)

**Pros:**
- Maximum convergence efficiency
- Reduces communication rounds needed

**Cons:**
- High overhead (requires surrogate model)
- Risk of exploitation (ignoring tail clients)

**Use Case:**
- Experimental only (not for production yet)
- See 07-EXPERIMENTS/AB_TESTS/ for evaluation

## Selection Process

### Weekly Workflow

**Step 1: Eligibility Check (Saturday 00:00 UTC)**
- Query fleet management system for eligible clients
- Run health checks on all clients
- Filter out clients with open NCRs or maintenance

**Step 2: Stratified Sampling (Saturday 06:00 UTC)**
- Apply fairness policies (minimum participation, balancing)
- Run selection algorithm (default: random)
- Generate client list for upcoming round

**Step 3: Notification (Saturday 12:00 UTC)**
- Notify selected clients via SATCOM or ground link
- Clients acknowledge receipt (timeout: 12 hours)
- Fallback: If client unavailable, select alternate

**Step 4: Training Launch (Sunday 00:00 UTC)**
- Distribute global model to selected clients
- Clients begin local training

### Client Dropout Handling

**During Training:**
- If client drops out (no heartbeat for 1 hour):
  - Mark as "offline" (do not wait for update)
  - Proceed with aggregation using remaining clients
  - Minimum quorum: 10 clients (abort if < 10)

**During Upload:**
- If client upload fails (timeout or network error):
  - Retry with exponential backoff (see [SCHEDULER.md](SCHEDULER.md))
  - If all retries fail, exclude from current round
  - Client queued for next round

**Post-Aggregation:**
- Clients that missed round receive new global model anyway
- No penalty for single missed round (tracking for fairness)

## Blacklist and Greylist

### Blacklist (Permanent Exclusion)

**Criteria:**
- Client repeatedly sends malicious or corrupted updates
- Client fails Byzantine detection (see [04-ALGORITHMS/ROBUST_AGGREGATION.md](04-ALGORITHMS/ROBUST_AGGREGATION.md))
- Client violates security policies (unauthorized access attempts)

**Process:**
- AI/ML Team Lead approves blacklist entry
- Client removed from eligibility pool
- Documented in 16-INCIDENT_RESPONSE/POSTMORTEMS/

### Greylist (Temporary Exclusion)

**Criteria:**
- Client data quality below threshold (< 80% completeness)
- Client hardware degraded (CPU, memory, disk failing diagnostics)
- Client under investigation for anomalous behavior

**Process:**
- Automatic greylist upon health check failure
- Client re-evaluated after 7 days or after maintenance
- Auto-removed from greylist if health checks pass

## Metrics and Monitoring

### Selection Metrics
- **Eligible client count**: Total clients meeting criteria
- **Selected client count**: Clients chosen for training round
- **Participation rate**: % of selected clients that completed training
- **Diversity score**: Entropy of client distribution (aircraft type, region, etc.)

### Fairness Metrics
- **Gini coefficient**: Inequality in participation frequency (target: < 0.3)
- **Minimum participation violations**: Clients below 3 rounds/quarter quota
- **Oversampling ratio**: Max participation / mean participation (target: < 2.0)

**Tracking:**
- Logged to 12-METRICS/TRAINING_METRICS.csv
- Dashboard: Grafana (see [12-METRICS/KPI_DEFINITIONS.md](12-METRICS/KPI_DEFINITIONS.md))

## Related Documents

- [**SCHEDULER.md**](SCHEDULER.md) - Training round schedules and timing
- [**CONNECTIVITY_PROFILES.md**](CONNECTIVITY_PROFILES.md) - Network availability for clients
- [**01-ARCHITECTURE/CLIENT_TYPES.md**](01-ARCHITECTURE/CLIENT_TYPES.md) - Client capabilities and constraints
- [**04-ALGORITHMS/ROBUST_AGGREGATION.md**](04-ALGORITHMS/ROBUST_AGGREGATION.md) - Byzantine-resilient aggregation
- [**12-METRICS/KPI_DEFINITIONS.md**](12-METRICS/KPI_DEFINITIONS.md) - Selection performance metrics

## Change History

| Version | Date    | Changes                          | Author    |
|---------|---------|----------------------------------|-----------|
| 1.0     | 2024-Q4 | Initial client selection policy  | AI/ML Team|
