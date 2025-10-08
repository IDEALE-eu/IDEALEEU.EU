# DATASETS_INDEX

Dataset provenance, retention policies, and consent tracking for FL.

## Dataset Registry

| dataset_id | source | date_range | num_samples | consent | retention |
|------------|--------|------------|-------------|---------|-----------|
| fleet_telemetry_2024q3 | Operational Data Hub | 2024-07 to 2024-09 | 1M | Art. 6(1)(f) | 90 days |
| sim_data_failure_modes | Sim Rigs | 2024-08 | 10K | N/A (synthetic) | 2 years |

## Provenance Tracking

- **Source**: Origin of data (aircraft, ground station, sim rig)
- **Date range**: Temporal coverage
- **Num samples**: Count of data points
- **Consent basis**: GDPR legal basis (Art. 6(1)(f) - legitimate interest)
- **Retention**: How long data is kept

## GDPR Compliance

- **Data minimization**: Only collect signals needed for FL use case
- **Purpose limitation**: Data used only for specified FL models
- **Retention**: Raw telemetry deleted after 90 days (aggregated metrics kept 2 years)

## Related Documents

- **../01-ARCHITECTURE/DATA_CONTRACTS/** - Data schemas
- **../11-COMPLIANCE/PRIVACY.md** - GDPR framework
