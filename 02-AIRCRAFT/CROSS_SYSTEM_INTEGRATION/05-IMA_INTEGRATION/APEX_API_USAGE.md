# APEX API Usage

## Overview

This document defines the ARINC 653 APEX (APplication/EXecutive) API usage for inter-partition communication and partition services on the IMA platform.

## APEX API Overview

The APEX API provides standardized services per ARINC 653:
- **Partition Management**: Start, stop, query partition state
- **Process Management**: Create, suspend, resume processes
- **Time Management**: Get time, periodic waits, delays
- **Inter-Partition Communication**: Sampling ports, queuing ports
- **Health Monitoring**: Error reporting, state queries
- **Memory Management**: Blackboard (intra-partition shared memory)

## Inter-Partition Communication (IPC)

### Sampling Ports
**Use Case**: Periodic data exchange with latest-value semantics (e.g., sensor data)
**Characteristics**:
- Non-blocking read/write
- Reader always gets most recent data
- Writer overwrites previous data
- No message queuing

**Example Sampling Ports**:

| Port Name | Source Partition | Dest Partition | Message Size | Refresh Rate | Direction |
|-----------|------------------|----------------|--------------|--------------|-----------|
| FCC1_PITCH_CMD | P001 (FCC-1) | P002 (FCC-2) | 32 bytes | 100 Hz | Send |
| ADC1_AIRSPEED | P008 (ADC-1) | P001 (FCC-1) | 16 bytes | 10 Hz | Receive |
| IRS1_ATTITUDE | P010 (IRS-1) | P001 (FCC-1) | 64 bytes | 50 Hz | Receive |
| GPS1_POSITION | P003 (Nav) | P004 (Display) | 128 bytes | 1 Hz | Receive |
| ENGINE_STATUS | P006 (Eng Mon) | P004 (Display) | 256 bytes | 5 Hz | Receive |

**APEX API Calls**:
```c
// Create sampling port (at partition init)
CREATE_SAMPLING_PORT(
    SAMPLING_PORT_NAME = "FCC1_PITCH_CMD",
    MAX_MESSAGE_SIZE = 32,
    PORT_DIRECTION = SOURCE,
    REFRESH_PERIOD = 10_MILLISECONDS,
    &SAMPLING_PORT_ID,
    &RETURN_CODE
);

// Write to sampling port (in partition code)
WRITE_SAMPLING_MESSAGE(
    SAMPLING_PORT_ID,
    MESSAGE_ADDR,
    LENGTH = 32,
    &RETURN_CODE
);

// Read from sampling port (in partition code)
READ_SAMPLING_MESSAGE(
    SAMPLING_PORT_ID,
    MESSAGE_ADDR,
    &LENGTH,
    &VALIDITY,
    &RETURN_CODE
);
```

### Queuing Ports
**Use Case**: Event-driven data exchange with FIFO queuing (e.g., alerts, commands)
**Characteristics**:
- FIFO message queue
- Reader dequeues messages in order
- Writer blocks if queue full (configurable)
- Supports priority queuing

**Example Queuing Ports**:

| Port Name | Source Partition | Dest Partition | Max Messages | Message Size | Direction |
|-----------|------------------|----------------|--------------|--------------|-----------|
| FIRE_ALERT | P012 (Fire Det) | P017 (Health Mon) | 10 | 64 bytes | Send |
| CONFIG_CMD | P018 (Config Mgr) | P001-P016 (All) | 5 | 128 bytes | Receive |
| HEALTH_EVENT | P001-P016 (All) | P017 (Health Mon) | 50 | 256 bytes | Send |
| CREW_ALERT | P017 (Health Mon) | P004 (Display) | 20 | 512 bytes | Send |

**APEX API Calls**:
```c
// Create queuing port (at partition init)
CREATE_QUEUING_PORT(
    QUEUING_PORT_NAME = "FIRE_ALERT",
    MAX_MESSAGE_SIZE = 64,
    MAX_NB_MESSAGE = 10,
    PORT_DIRECTION = SOURCE,
    QUEUING_DISCIPLINE = FIFO,
    &QUEUING_PORT_ID,
    &RETURN_CODE
);

// Send message (non-blocking or blocking)
SEND_QUEUING_MESSAGE(
    QUEUING_PORT_ID,
    MESSAGE_ADDR,
    LENGTH = 64,
    TIME_OUT = 0,  // 0 = non-blocking
    &RETURN_CODE
);

// Receive message
RECEIVE_QUEUING_MESSAGE(
    QUEUING_PORT_ID,
    TIME_OUT = INFINITE_TIME_VALUE,
    MESSAGE_ADDR,
    &LENGTH,
    &RETURN_CODE
);
```

## Time Management

### Get Time
```c
GET_TIME(&CURRENT_TIME, &RETURN_CODE);
// Returns system time (PTP synchronized)
```

### Periodic Wait
```c
PERIODIC_WAIT(&RETURN_CODE);
// Suspends process until next period (per ARINC 653 schedule)
```

### Timed Wait
```c
TIMED_WAIT(DELAY_TIME = 100_MILLISECONDS, &RETURN_CODE);
// Suspends process for specified duration
```

## Health Monitoring API

### Report Application Error
```c
// Application detects error and reports to HM
RAISE_APPLICATION_ERROR(
    ERROR_CODE = DEADLINE_MISSED,
    MESSAGE_ADDR = "FCC control law deadline miss",
    LENGTH = 30,
    &RETURN_CODE
);
```

### Get Partition Status
```c
GET_PARTITION_STATUS(&PARTITION_STATUS, &RETURN_CODE);
// Returns partition state, health, resource usage
```

## Blackboard (Intra-Partition Shared Memory)

**Use Case**: Shared memory between processes within same partition
**Not Used**: Inter-partition communication (use ports instead)

```c
// Create blackboard
CREATE_BLACKBOARD(
    BLACKBOARD_NAME = "SHARED_DATA",
    MAX_MESSAGE_SIZE = 1024,
    &BLACKBOARD_ID,
    &RETURN_CODE
);

// Write to blackboard (one process)
DISPLAY_BLACKBOARD(
    BLACKBOARD_ID,
    MESSAGE_ADDR,
    LENGTH = 1024,
    &RETURN_CODE
);

// Read from blackboard (another process)
READ_BLACKBOARD(
    BLACKBOARD_ID,
    TIME_OUT = 0,
    MESSAGE_ADDR,
    &LENGTH,
    &RETURN_CODE
);
```

## IPC Design Patterns

### Pattern 1: Sensor Data Distribution (Sampling Ports)
- Sensor partition reads hardware, publishes data via sampling port
- Multiple consumer partitions read from same sampling port
- Latest-value semantics ensure freshest data

### Pattern 2: Command/Response (Queuing Ports)
- Command issuer sends message via queuing port
- Command receiver processes and responds via separate queuing port
- FIFO ensures ordered processing

### Pattern 3: Health Monitoring (Queuing Ports)
- All partitions send health events to System Health Monitor (P017)
- Health monitor aggregates, analyzes, and alerts crew
- Queuing ensures no event loss

### Pattern 4: Configuration Updates (Queuing Ports)
- Configuration Manager (P018) sends updates via queuing port
- Target partitions receive and apply configuration
- Acknowledgment sent back via separate port

## Channel Configuration

### AFDX Channels
- Sampling ports mapped to AFDX VLs for inter-module communication
- Queuing ports use AFDX for event-driven messages
- See [02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv](../../02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv)

### Intra-Module Channels
- Sampling/queuing ports within same IMA module use shared memory
- No network overhead for local IPC
- OS kernel manages memory protection

## Performance Considerations

### Latency
- **Intra-module IPC**: <10 μs (shared memory)
- **Inter-module IPC**: <1 ms (AFDX network)
- **Queuing port overhead**: +50 μs per message

### Throughput
- **Sampling ports**: Limited by refresh rate (e.g., 100 Hz = max 100 messages/sec)
- **Queuing ports**: Limited by queue depth and message size
- **Network bandwidth**: Allocated per partition (see [IMA_RESOURCES.csv](./IMA_RESOURCES.csv))

## Error Handling

### Port Creation Errors
- **INVALID_CONFIG**: Port name already exists or invalid parameters
- **Action**: Log error, halt partition initialization

### Communication Errors
- **NOT_AVAILABLE**: Port not ready (e.g., source partition not started)
- **Action**: Retry after delay, log if persistent

- **INVALID_MODE**: Attempt to write to SOURCE port or read from DESTINATION port
- **Action**: Software defect, log and report

- **TIMED_OUT**: Queuing port full, message not sent within timeout
- **Action**: Log error, may drop message (DAL C/D) or halt partition (DAL A/B)

## Testing and Verification

### IPC Testing
- Verify all sampling ports receive data at expected rate
- Verify queuing ports deliver messages in FIFO order
- Inject faults (full queue, invalid port) and verify error handling
- Measure IPC latency and throughput
- Document in [07-INTEGRATION_TEST/EVIDENCE/](../../07-INTEGRATION_TEST/EVIDENCE/)

### Acceptance Criteria
- All ports configured correctly (no INVALID_CONFIG errors)
- Latency within budgets (see [01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv](../../01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv))
- No message loss for DAL A/B functions
- Correct error handling for DAL C/D functions

## Compliance

- **ARINC 653 Part 1**: APEX API specification
- **DO-178C**: Software verification of IPC implementation (DAL A)
- **DO-254**: Hardware shared memory protection (DAL A)

## References

- **ARINC 653**: Avionics Application Software Standard Interface
- **[PARTITION_MAP.csv](./PARTITION_MAP.csv)** - Partition configuration
- **[06-SOFTWARE_INTEGRATION/INTER_PARTITION_COMMS.md](../../06-SOFTWARE_INTEGRATION/INTER_PARTITION_COMMS.md)** - IPC architecture

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | IMA Integration Team | Initial APEX API usage document |
