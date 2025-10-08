# Availability Metrics

## Overview

Availability metrics measure the percentage of time fleet assets are operationally ready and available for service, tracking the effectiveness of maintenance strategies and operational practices.

## Key Metrics

### Aircraft Availability
- **Operational Availability (Ao)**: Percentage of time aircraft is ready for flight
- **Inherent Availability (Ai)**: Availability considering only scheduled maintenance
- **Achieved Availability (Aa)**: Includes scheduled and unscheduled maintenance

### Calculation
```
Availability = Uptime / (Uptime + Downtime)
            = MTBF / (MTBF + MTTR)

Where:
- MTBF = Mean Time Between Failures
- MTTR = Mean Time To Repair
```

### Reliability Metrics
- **Dispatch Reliability**: Percentage of flights departing on-time without technical delays
- **Mean Time Between Unscheduled Removals (MTBUR)**: Component reliability
- **Pilot Report (PIREP) Rate**: Technical issues reported per flight hour
- **Delays per 1000 departures**: Technical delay frequency

### Utilization vs. Availability
- **Utilization**: Actual usage / available capacity
- **Availability**: Ready for use / total time
- Relationship: High availability enables high utilization

## Performance Targets

### Aircraft Operations
- Operational availability: >95%
- Dispatch reliability: >98%
- Technical delays: <2 per 1000 departures

### Spacecraft Operations
- On-orbit availability: >99%
- Mission success rate: >98%
- Anomaly-free missions: >95%

## Monitoring and Improvement

- Daily availability tracking
- Root cause analysis of unavailability
- Trend analysis and forecasting
- Continuous improvement initiatives

## References
- Operational data: **01-FLEET/OPERATIONAL_DATA_HUB/**
- Maintenance planning: **04-MAINTENANCE_PLANNING/**
- Reporting: **10-REPORTING/MONTHLY_FLEET_REVIEW.md**
