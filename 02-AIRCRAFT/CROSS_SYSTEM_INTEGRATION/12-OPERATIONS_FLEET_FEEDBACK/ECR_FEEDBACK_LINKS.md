# ECR Feedback Links

## Overview

Links between operational feedback and Engineering Change Requests (ECRs).

## Active ECRs from Fleet Feedback

### ECR-2024-089: False Fire Warnings (Cold Weather)
- **Source**: Anomaly pattern analysis
- **Frequency**: 5 events per 1000 flight hours in temperatures <-20°C
- **Root Cause**: Fire sensor thermal coefficient out of specification
- **Status**: Under investigation
- **Link**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/ECR-2024-089.yaml](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)

### ECR-2024-102: AFDX Switch Latency Degradation
- **Source**: KPI trending (latency increase after 2000 hrs)
- **Frequency**: Observed on 15% of aircraft after 2000 flight hours
- **Root Cause**: Memory leak in switch firmware
- **Status**: Software patch released (SW v2.1.3)
- **Link**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/ECR-2024-102.yaml](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)

### ECR-2024-115: GPS-1 Intermittent Lock Loss
- **Source**: Maintenance logs and ACMS data
- **Frequency**: 2 events per 10,000 flight hours
- **Root Cause**: GPS receiver antenna connector corrosion
- **Status**: Hardware replacement SB issued
- **Link**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/ECR-2024-115.yaml](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)

## Closed ECRs (Incorporated in Baselines)

### ECR-2024-035: Display Brightness Flicker
- **Resolution**: Firmware update (Display v1.7.1)
- **Incorporated**: Integration Baseline IBL-2024-Q3

### ECR-2024-057: FMS Navigation Accuracy Drift
- **Resolution**: Software update (FMS v3.2.0)
- **Incorporated**: Integration Baseline IBL-2024-Q3

## Process

1. **Fleet Data Analysis**: Identify patterns
2. **ECR Submission**: Engineering team creates ECR
3. **Root Cause Investigation**: Determine failure mechanism
4. **Solution Development**: Design, test, verify fix
5. **CCB Approval**: Configuration Control Board approves change
6. **Fleet Implementation**: Service Bulletin or software update

## References

- [ANOMALY_PATTERNS.md](./ANOMALY_PATTERNS.md) - Detected patterns
- [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/) - ECR repository
