# Health Monitoring (HM) Configuration

## Overview

This document defines the ARINC 653 Health Monitoring (HM) table configuration for the IMA platform, including error detection, handling, and recovery actions.

## Health Monitoring Levels

Per ARINC 653, health monitoring operates at multiple levels:

### Module Level HM
- **Scope**: Entire IMA module (hardware + OS)
- **Events**: Hardware faults, OS kernel panics, watchdog timeouts
- **Response**: Module reset, failover to redundant module

### Partition Level HM
- **Scope**: Individual partition (application)
- **Events**: Deadline miss, memory violation, illegal instruction
- **Response**: Varies by DAL (see below)

### Process Level HM
- **Scope**: Individual process within partition
- **Events**: Exception, stack overflow, division by zero
- **Response**: Process restart or partition shutdown

## HM Event Table

### Module-Level Events

| Event ID | Event Type | Detection | Response | Recovery Time |
|----------|------------|-----------|----------|---------------|
| HM-M001 | Hardware failure | Built-in self-test (BIST) | Switch to redundant module | <1 second |
| HM-M002 | Watchdog timeout | Hardware watchdog (5 seconds) | Module reset | 10 seconds |
| HM-M003 | Temperature alarm | Thermal sensor >85°C | Throttle CPU, alert crew | N/A - degraded |
| HM-M004 | Memory ECC error | ECC detection | Log error, continue if correctable | Immediate |
| HM-M005 | Power supply fault | Voltage monitor | Switch to backup power | <100 ms |

### Partition-Level Events (DAL A)

| Event ID | Event Type | Detection | Response | Notes |
|----------|------------|-----------|----------|-------|
| HM-P001 | Deadline miss | Scheduler | Immediate partition shutdown, switch to backup | Critical - no delay tolerated |
| HM-P002 | Memory violation | MMU fault | Immediate partition shutdown, switch to backup | Safety hazard |
| HM-P003 | Illegal instruction | CPU exception | Immediate partition shutdown, switch to backup | Software defect |
| HM-P004 | Stack overflow | Stack guard page | Immediate partition shutdown, switch to backup | Memory corruption risk |
| HM-P005 | Watchdog timeout | Partition watchdog | Immediate partition shutdown, switch to backup | Application hang |

### Partition-Level Events (DAL B)

| Event ID | Event Type | Detection | Response | Notes |
|----------|------------|-----------|----------|-------|
| HM-P101 | Deadline miss | Scheduler | Shutdown partition, alert crew | Allow completion of current cycle |
| HM-P102 | Memory violation | MMU fault | Shutdown partition, alert crew | May be recoverable on next cycle |
| HM-P103 | Illegal instruction | CPU exception | Shutdown partition, alert crew | Software defect |
| HM-P104 | Watchdog timeout | Partition watchdog | Shutdown partition, alert crew | Application hang |

### Partition-Level Events (DAL C/D)

| Event ID | Event Type | Detection | Response | Notes |
|----------|------------|-----------|----------|-------|
| HM-P201 | Deadline miss | Scheduler | Log event, continue | Non-critical function |
| HM-P202 | Memory violation | MMU fault | Log event, restart partition | Attempt recovery |
| HM-P203 | Illegal instruction | CPU exception | Log event, restart partition | Software defect |
| HM-P204 | Watchdog timeout | Partition watchdog | Log event, restart partition | Application hang |

## HM Response Actions

### Immediate Shutdown (DAL A)
1. Stop partition execution immediately (within 1 scheduler tick)
2. Release all partition resources (memory, I/O)
3. Notify System Health Monitor partition (P017)
4. Activate redundant partition if available
5. Log event to non-volatile memory
6. Alert crew via EICAS warning (if dual-channel failure)

### Graceful Shutdown (DAL B)
1. Allow current minor frame to complete
2. Stop partition at next frame boundary
3. Release partition resources
4. Notify System Health Monitor
5. Alert crew via EICAS caution

### Log and Continue (DAL C/D)
1. Log event with timestamp and context
2. Increment error counter
3. If error count exceeds threshold (e.g., 10 in 1 hour), escalate to shutdown
4. Otherwise, continue normal operation

### Partition Restart
1. Shutdown partition per above
2. Wait 1 second for cleanup
3. Reload partition from non-volatile storage
4. Re-initialize partition state
5. Resume scheduling
6. Log restart event

## Crew Alerting

### EICAS Warning (Red)
- **Trigger**: Dual-channel failure of DAL A function
- **Example**: Both FCC-1 and FCC-2 partitions failed
- **Action**: Emergency procedure, manual reversion
- **Audio**: Master warning tone

### EICAS Caution (Amber)
- **Trigger**: Single-channel failure of DAL A or B function
- **Example**: FCC-1 partition failed, FCC-2 operating normally
- **Action**: Note system degradation, consider diversion
- **Audio**: Single chime

### EICAS Advisory (White)
- **Trigger**: DAL C/D partition failure
- **Example**: Display driver partition restart
- **Action**: Monitor, maintenance action required
- **Audio**: None

## Fault Logs

### Event Logging
All HM events logged to non-volatile memory with:
- Timestamp (PTP synchronized time)
- Event ID and type
- Partition ID
- CPU state (registers, stack trace)
- Sequence number (to detect log wrap)

### Log Storage
- **Location**: Non-volatile RAM (NVRAM) in IMA module
- **Capacity**: 10,000 events per module
- **Retention**: Minimum 100 flight hours or 500 flight cycles
- **Download**: Via maintenance interface (Zone 5)

### Log Analysis
- **Automated**: System Health Monitor analyzes logs for trends
- **Manual**: Maintenance review via ground tools
- **Escalation**: Repeated failures trigger ECR process

## Watchdog Configuration

### Hardware Watchdog
- **Timeout**: 5 seconds (module level)
- **Reset**: Module reset if OS fails to tickle watchdog
- **Non-maskable**: Cannot be disabled by software

### Partition Watchdog
- **Timeout**: Configurable per partition (typically 2x worst-case execution time)
- **Reset**: Partition shutdown if application fails to tickle
- **Monitoring**: OS kernel tickles based on partition heartbeat

## Testing and Verification

### HM Table Verification
- All HM events injected during integration testing
- Verify correct response per HM table
- Verify timing (e.g., immediate shutdown <10ms for DAL A)
- Document in [07-INTEGRATION_TEST/EVIDENCE/REPORTS/HM_TESTING/](../../07-INTEGRATION_TEST/EVIDENCE/REPORTS/)

### Fault Injection Testing
- Inject deadline miss (delay partition execution)
- Inject memory violation (access illegal address)
- Inject watchdog timeout (infinite loop in application)
- Verify failover to redundant partition
- Verify crew alerting

### Acceptance Criteria
- 100% HM event coverage (all events tested)
- Response time per DAL requirements
- No false positives (spurious HM events)
- Correct crew alerting

## Compliance

- **ARINC 653**: Health Monitoring per Part 1, Section 4
- **DO-178C**: Software verification of HM logic (DAL A)
- **DO-254**: Hardware watchdog implementation (DAL A)
- **ARP4754A**: Safety assessment of HM strategy

## References

- **[PARTITION_MAP.csv](../PARTITION_MAP.csv)** - Partition criticality and HM levels
- **[IMA_RESOURCES.csv](../IMA_RESOURCES.csv)** - Resource quotas
- **[06-SOFTWARE_INTEGRATION/SAFETY_MONITORS.md](../../06-SOFTWARE_INTEGRATION/SAFETY_MONITORS.md)** - Software safety monitors

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | IMA Integration Team | Initial HM configuration |
