# DATA_VALIDATION_RULES

Comprehensive validation rules applied at data ingestion.

## Purpose

Ensures data quality by validating telemetry against predefined rules before storage. Invalid data is flagged, rejected, or corrected based on severity.

## Validation Categories

### 1. Structural Validation

**Schema Compliance:**
- Message conforms to registered Avro/Protobuf schema
- All required fields present
- Field data types match schema definition

**Action on Failure:** Reject message, log error, alert pipeline owner

### 2. Range Validation

**Numeric Ranges:**
```yaml
# Example: Hydrogen tank pressure
signal: h2_tank_pressure_fwd
range: [0, 350]  # bar
action_below: REJECT  # Pressure cannot be negative
action_above: ALERT   # Overpressure condition
```

**Allowed Values (Enumerations):**
```yaml
# Example: Flight phase
signal: flight_phase
allowed_values: [ground, taxi, takeoff, climb, cruise, descent, approach, landing]
action_invalid: REJECT
```

**Action on Failure:** 
- Critical: Reject message
- Warning: Accept with quality flag `quality=1`

### 3. Consistency Validation

**Cross-Field Checks:**
```yaml
# Example: Altitude vs. atmospheric pressure consistency
rule: altitude_pressure_consistency
condition: |
  abs(pressure - standard_pressure(altitude)) < tolerance
tolerance: 10%  # Allow 10% deviation
action_fail: WARNING
```

**Physical Constraints:**
```yaml
# Example: Energy balance check
rule: power_balance
condition: |
  power_generated >= power_consumed - battery_discharge
action_fail: ALERT
```

**Action on Failure:** Accept with quality flag `quality=1`, forward to anomaly queue

### 4. Completeness Validation

**Missing Data Thresholds:**
```yaml
# Per signal, per flight/mission
max_missing_rate: 0.05  # 5% maximum missing values
window: 1_hour
action_exceed: ALERT
```

**Required Field Presence:**
```yaml
required_fields:
  - timestamp
  - platform_id
  - signal_name
  - value
action_missing: REJECT
```

### 5. Freshness Validation

**Timestamp Validation:**
```yaml
# Timestamps must be within acceptable window
max_age: 300  # seconds (5 minutes for real-time)
max_future: 60  # seconds (allow 1 minute clock skew)
action_stale: WARNING
action_future: WARNING
```

**Duplicate Detection:**
```yaml
# Detect duplicate messages (same timestamp + platform + signal)
duplicate_window: 10  # seconds
action_duplicate: IGNORE  # Silently drop duplicates
```

## Validation Severity Levels

| Level | Action | Description |
|-------|--------|-------------|
| **REJECT** | Drop message | Critical validation failure, data unusable |
| **ALERT** | Accept + notify | Severe issue, needs immediate attention |
| **WARNING** | Accept + flag | Minor issue, log for review |
| **IGNORE** | Accept silently | Benign condition (e.g., duplicate) |

## Quality Flags

Validated messages tagged with quality indicator:

| Quality | Value | Description |
|---------|-------|-------------|
| Good | 0 | Passed all validation rules |
| Suspect | 1 | Passed with warnings |
| Bad | 2 | Failed critical validations (should be rejected) |

## Validation Rule Configuration

Rules stored as YAML configurations in Schema Registry:

```yaml
# Example: h2_tank_pressure_fwd.validation.yaml
signal: h2_tank_pressure_fwd
validation_rules:
  - type: range
    min: 0
    max: 350
    unit: bar
    action_below: REJECT
    action_above: ALERT
  
  - type: rate_of_change
    max_delta: 50  # bar/second
    action_exceed: ALERT
  
  - type: consistency
    related_signal: h2_tank_temp_fwd
    condition: "pressure < 400 * (temp / 300)"  # Ideal gas approximation
    action_fail: WARNING
```

## Validation Pipeline Integration

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Raw Message │────▶│ Structural   │────▶│ Range       │
└─────────────┘     │ Validation   │     │ Validation  │
                    └──────────────┘     └─────────────┘
                                                  │
┌─────────────┐     ┌──────────────┐     ┌───────▼─────┐
│ Store or    │◀────│ Freshness    │◀────│ Consistency │
│ Reject      │     │ Validation   │     │ Validation  │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Performance Considerations

- **Rule Evaluation**: <1 ms per message (p99)
- **Caching**: Validation rules cached in memory, refreshed every 5 minutes
- **Parallelism**: Validation parallelized across partitions

## Monitoring

**Key Metrics:**
- Validation pass rate (target: >99%)
- Validation failure by rule type
- Validation latency (p50, p95, p99)
- Quality flag distribution (0, 1, 2)

**Alerts:**
- Validation pass rate <95%
- Specific rule failure rate >5%
- Validation latency >10 ms (p99)

## Validation Rule Governance

### Rule Creation
1. Identify validation need (from anomaly analysis, domain expertise)
2. Define rule in YAML format
3. Submit PR with rule + rationale
4. Review by data steward and domain expert
5. Merge and deploy

### Rule Updates
- Minor updates (adjust threshold): Data steward approval
- Major updates (change logic): ECR required

### Rule Deprecation
- Mark as DEPRECATED with 30-day notice
- Monitor impact (messages affected)
- Archive after 30 days

## Related Documents

- **SCHEMA_REGISTRY/TELEMETRY_SCHEMA_VERSIONING.md** - Schema versioning
- **ANOMALY_DETECTION_AT_INGEST.md** - Anomaly detection
- **../03-DATA_STORAGE/METADATA_REGISTRY/DQ_RULESETS.yaml** - Data quality rulesets

## Example Rule Library

### Aircraft Validation Rules
```yaml
# Airspeed
- signal: airspeed_indicated
  range: [0, 350]  # knots
  action_outside: WARNING

# Altitude
- signal: altitude_msl
  range: [-1000, 50000]  # feet
  action_outside: REJECT

# Engine N1
- signal: eng_n1_speed
  range: [0, 105]  # percent
  rate_of_change_max: 10  # percent/second
  action_exceed: ALERT
```

### Spacecraft Validation Rules
```yaml
# Battery voltage
- signal: battery_voltage
  range: [28, 32]  # volts
  action_below: ALERT
  action_above: ALERT

# Thruster thrust
- signal: thrust_thruster1
  range: [0, 100]  # Newtons
  action_negative: REJECT

# Attitude quaternion
- signal: attitude_q
  validation: quaternion_norm
  expected_norm: 1.0
  tolerance: 0.01
  action_fail: WARNING
```

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial validation rules        | Data Engineering Team |
