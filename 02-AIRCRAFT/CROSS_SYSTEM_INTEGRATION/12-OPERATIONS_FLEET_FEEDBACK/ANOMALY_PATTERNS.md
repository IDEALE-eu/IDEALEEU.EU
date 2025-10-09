# Anomaly Patterns and Fleet Feedback

## Overview

Operational anomaly patterns identified from fleet data, linked to Engineering Change Requests (ECRs).

## Anomaly Categories

### Nuisance Alerts
- **Pattern**: False fire warnings in cold weather
- **Frequency**: 5 events per 1000 flight hours
- **ECR**: [ECR-2024-089](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Status**: Under investigation

### Performance Degradation
- **Pattern**: AFDX switch latency increase over time
- **Frequency**: Observed after 2000 flight hours
- **ECR**: [ECR-2024-102](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Status**: Software patch released

### Intermittent Faults
- **Pattern**: GPS-1 receiver intermittent loss of lock
- **Frequency**: 2 events per 10,000 flight hours
- **ECR**: [ECR-2024-115](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Status**: Hardware replacement recommended

## Data Sources

- **ACMS (Aircraft Condition Monitoring System)**: Real-time health data
- **FDR (Flight Data Recorder)**: Flight parameters
- **Maintenance Logs**: Reported issues and corrective actions

## Analysis Process

1. **Data Collection**: Automated download via ACMS gateway
2. **Pattern Detection**: Machine learning algorithms identify trends
3. **Root Cause Analysis**: Engineering team investigates
4. **ECR Generation**: Formal change request if design change needed
5. **Fleet Update**: Service bulletins issued if applicable

## References

- [KPI_FEEDS.csv](./KPI_FEEDS.csv) - Key Performance Indicators from fleet
- [ECR_FEEDBACK_LINKS.md](./ECR_FEEDBACK_LINKS.md) - Links to CONFIG_MGMT/06-CHANGES
- [12-OPERATIONS_FLEET_FEEDBACK/](../../12-OPERATIONS_FLEET_FEEDBACK/) - Operations data
