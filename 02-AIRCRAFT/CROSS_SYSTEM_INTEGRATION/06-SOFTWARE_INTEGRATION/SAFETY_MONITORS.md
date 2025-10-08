# Safety Monitors

## Overview

Safety monitors and FDIR (Fault Detection, Isolation, and Recovery) logic deployed across partitions.

## Monitor Types

### Flight Control Monitors (DAL A)
- Control surface position monitoring
- Actuator health monitoring
- Control law consistency checks
- Cross-channel comparison (FCC-1 vs FCC-2)

### Engine Control Monitors (DAL A)
- Engine parameter limit monitoring
- FADEC health monitoring
- Fuel flow rate monitoring

### System Health Monitor (Partition P017)
- Aggregates health events from all partitions
- Analyzes trends and patterns
- Alerts crew via EICAS
- Logs events for maintenance

## FDIR Strategy

### Detection
- Boundary checks on all critical parameters
- Sequence number monitoring
- Timeout detection
- CRC validation

### Isolation
- Identify faulty partition or LRU
- Disable faulty component
- Prevent error propagation

### Recovery
- Activate backup partition/LRU
- Restore from last known good state
- Alert crew if manual action required

## Compliance
- **DO-178C**: Software safety monitoring (DAL A/B)
- **ARP4754A**: System safety assessment

## References
- [05-IMA_INTEGRATION/SCHEDULE_TABLES/HEALTH_MONITORING.md](../../05-IMA_INTEGRATION/SCHEDULE_TABLES/HEALTH_MONITORING.md)
- [08-SAFETY_SECURITY/HAZARD_LINKS.csv](../../08-SAFETY_SECURITY/HAZARD_LINKS.csv)
