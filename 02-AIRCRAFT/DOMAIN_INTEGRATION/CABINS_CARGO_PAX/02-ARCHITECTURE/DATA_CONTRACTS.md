# Data Contracts - CABINS_CARGO_PAX Domain

## Purpose

This document defines the data schemas, interfaces, and contracts for systems within the CABINS_CARGO_PAX domain.

## Overview

Data contracts ensure consistent data exchange between:
- Cabin systems (IFE, CMS, sensors)
- Cargo systems (load sensing, monitoring)
- Aircraft systems (power, ECS, fire, etc.)
- Ground systems (content, maintenance, operations)

## Data Contract Principles

1. **Well-Defined Schemas**: All data structures explicitly defined
2. **Versioning**: All contracts include version information
3. **Backward Compatibility**: Changes maintain compatibility when possible
4. **Validation**: All data validated against schemas
5. **Documentation**: Complete documentation for all fields

## Cabin Management System (CMS) Data

### CMS System Status

```json
{
  "schema_version": "1.0",
  "message_type": "CMS_SYSTEM_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "system_id": "string",
  "status": {
    "operational_state": "NORMAL | DEGRADED | FAILED",
    "active_faults": [
      {
        "fault_code": "string",
        "severity": "CRITICAL | WARNING | INFO",
        "affected_system": "string",
        "timestamp": "ISO8601_DATETIME"
      }
    ],
    "subsystem_status": {
      "lighting": "OK | DEGRADED | FAILED",
      "temperature": "OK | DEGRADED | FAILED",
      "entertainment": "OK | DEGRADED | FAILED",
      "galley": "OK | DEGRADED | FAILED"
    }
  }
}
```

### Cabin Lighting Control

```json
{
  "schema_version": "1.0",
  "message_type": "LIGHTING_CONTROL",
  "timestamp": "ISO8601_DATETIME",
  "zone_id": "string",
  "lighting_mode": "BRIGHT | DIM | NIGHT | BOARDING | TAKEOFF | LANDING",
  "brightness_level": "0-100",
  "color_temperature": "2700-6500",
  "individual_overrides": [
    {
      "seat_id": "string",
      "reading_light": "ON | OFF",
      "brightness": "0-100"
    }
  ]
}
```

### Passenger Service Unit (PSU) Data

```json
{
  "schema_version": "1.0",
  "message_type": "PSU_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "psu_id": "string",
  "seat_location": "ROW_SEAT",
  "components": {
    "reading_light": {
      "status": "ON | OFF | FAULT",
      "brightness": "0-100"
    },
    "attendant_call": {
      "status": "INACTIVE | ACTIVE | ACKNOWLEDGED"
    },
    "air_nozzle": {
      "status": "OPEN | CLOSED | FAULT",
      "position": "0-100"
    },
    "oxygen_mask": {
      "deployed": "boolean",
      "timestamp_deployed": "ISO8601_DATETIME"
    },
    "no_smoking_sign": {
      "illuminated": "boolean"
    },
    "fasten_seatbelt_sign": {
      "illuminated": "boolean"
    }
  }
}
```

## In-Flight Entertainment (IFE) Data

### IFE System Status

```json
{
  "schema_version": "1.0",
  "message_type": "IFE_SYSTEM_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "system_id": "string",
  "server_status": "ONLINE | OFFLINE | MAINTENANCE",
  "active_sessions": "integer",
  "content_library": {
    "movies_count": "integer",
    "tv_shows_count": "integer",
    "games_count": "integer",
    "last_update": "ISO8601_DATETIME"
  },
  "network_status": {
    "backend_connectivity": "OK | DEGRADED | FAILED",
    "seat_connectivity": "percentage",
    "bandwidth_utilization": "percentage"
  }
}
```

### Seat Entertainment Unit Status

```json
{
  "schema_version": "1.0",
  "message_type": "SEAT_IFE_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "seat_id": "string",
  "unit_status": "OPERATIONAL | DEGRADED | FAILED",
  "display": {
    "power_state": "ON | OFF | STANDBY",
    "current_content": "string",
    "playback_position": "seconds"
  },
  "connectivity": {
    "network_connected": "boolean",
    "signal_strength": "0-100"
  },
  "user_session": {
    "active": "boolean",
    "language": "ISO639_CODE",
    "profile_id": "string"
  }
}
```

### Passenger Connectivity

```json
{
  "schema_version": "1.0",
  "message_type": "CONNECTIVITY_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "service_type": "WIFI | CELLULAR",
  "service_status": "AVAILABLE | DEGRADED | UNAVAILABLE",
  "active_connections": "integer",
  "bandwidth": {
    "total_mbps": "float",
    "available_mbps": "float",
    "per_user_limit_mbps": "float"
  },
  "satellite_link": {
    "connected": "boolean",
    "signal_quality": "0-100",
    "latency_ms": "integer"
  }
}
```

## Cabin Sensor Data

### Temperature Sensors

```json
{
  "schema_version": "1.0",
  "message_type": "CABIN_TEMPERATURE",
  "timestamp": "ISO8601_DATETIME",
  "zone_id": "string",
  "temperature_celsius": "float",
  "setpoint_celsius": "float",
  "humidity_percentage": "float",
  "air_quality_index": "0-500",
  "sensor_status": "OK | DEGRADED | FAILED"
}
```

### Occupancy Sensors

```json
{
  "schema_version": "1.0",
  "message_type": "SEAT_OCCUPANCY",
  "timestamp": "ISO8601_DATETIME",
  "seat_id": "string",
  "occupied": "boolean",
  "seatbelt_fastened": "boolean",
  "confidence_level": "0-100"
}
```

### Lavatory Occupancy

```json
{
  "schema_version": "1.0",
  "message_type": "LAVATORY_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "lavatory_id": "string",
  "occupied": "boolean",
  "door_locked": "boolean",
  "smoke_detected": "boolean",
  "service_required": "boolean",
  "water_level": "0-100",
  "waste_level": "0-100"
}
```

## Galley Systems Data

### Galley Equipment Status

```json
{
  "schema_version": "1.0",
  "message_type": "GALLEY_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "galley_id": "string",
  "power_state": "ON | OFF | FAULT",
  "power_consumption_watts": "float",
  "equipment": [
    {
      "equipment_id": "string",
      "equipment_type": "OVEN | COFFEE_MAKER | REFRIGERATOR | WATER_HEATER",
      "status": "OPERATIONAL | HEATING | COOLING | FAULT",
      "temperature_celsius": "float",
      "setpoint_celsius": "float"
    }
  ],
  "water_supply": {
    "pressure_psi": "float",
    "flow_rate_lpm": "float",
    "available": "boolean"
  }
}
```

## Cargo Systems Data

### Load Sensing Data

```json
{
  "schema_version": "1.0",
  "message_type": "CARGO_LOAD_DATA",
  "timestamp": "ISO8601_DATETIME",
  "compartment_id": "string",
  "compartment_location": "MAIN_DECK | FWD_LOWER | AFT_LOWER | BULK",
  "load_cells": [
    {
      "cell_id": "string",
      "weight_kg": "float",
      "status": "OK | DEGRADED | FAILED"
    }
  ],
  "total_weight_kg": "float",
  "center_of_gravity": {
    "x_meters": "float",
    "y_meters": "float",
    "z_meters": "float"
  }
}
```

### ULD Lock Status

```json
{
  "schema_version": "1.0",
  "message_type": "ULD_LOCK_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "lock_id": "string",
  "position_id": "string",
  "lock_state": "LOCKED | UNLOCKED | FAULT",
  "uld_present": "boolean",
  "uld_type": "LD3 | LD6 | LD8 | LD11 | PALLET",
  "lock_force_newtons": "float",
  "sensor_status": "OK | DEGRADED | FAILED"
}
```

### Cargo Fire Detection

```json
{
  "schema_version": "1.0",
  "message_type": "CARGO_FIRE_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "compartment_id": "string",
  "fire_detected": "boolean",
  "smoke_level": "0-100",
  "temperature_celsius": "float",
  "detector_status": [
    {
      "detector_id": "string",
      "status": "OK | ALARM | FAULT",
      "last_test": "ISO8601_DATETIME"
    }
  ]
}
```

### Power Drive Unit (PDU) Status

```json
{
  "schema_version": "1.0",
  "message_type": "PDU_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "pdu_id": "string",
  "operational_state": "IDLE | LOADING | UNLOADING | FAULT",
  "position_mm": "float",
  "velocity_mps": "float",
  "motor_current_amps": "float",
  "motor_temperature_celsius": "float",
  "emergency_stop_active": "boolean"
}
```

## Interface Data Contracts

### To ATA-24 (Electrical Power)

```json
{
  "schema_version": "1.0",
  "message_type": "POWER_REQUEST",
  "timestamp": "ISO8601_DATETIME",
  "requesting_system": "string",
  "power_type": "AC_115V | DC_28V | USB_5V",
  "requested_watts": "float",
  "priority": "CRITICAL | NORMAL | LOW",
  "duration_seconds": "integer"
}
```

### To ATA-31 (Weight & Balance)

```json
{
  "schema_version": "1.0",
  "message_type": "WEIGHT_BALANCE_DATA",
  "timestamp": "ISO8601_DATETIME",
  "cabin_load": {
    "passenger_count": "integer",
    "average_weight_kg": "float",
    "baggage_weight_kg": "float"
  },
  "cargo_load": {
    "total_weight_kg": "float",
    "compartments": [
      {
        "compartment_id": "string",
        "weight_kg": "float",
        "cg_offset_meters": "float"
      }
    ]
  },
  "calculated_cg": {
    "x_meters": "float",
    "within_limits": "boolean"
  }
}
```

### To ATA-42 (IMA Platform)

```json
{
  "schema_version": "1.0",
  "message_type": "IMA_APPLICATION_STATUS",
  "timestamp": "ISO8601_DATETIME",
  "application_name": "string",
  "partition_id": "string",
  "health_status": "HEALTHY | DEGRADED | FAILED",
  "cpu_utilization_percent": "0-100",
  "memory_utilization_percent": "0-100",
  "network_traffic_mbps": "float"
}
```

## Data Quality Requirements

### Timeliness

| Data Type | Update Rate | Latency Requirement |
|-----------|-------------|---------------------|
| CMS status | 1 Hz | < 100 ms |
| IFE status | 0.1 Hz | < 1 s |
| Cabin sensors | 0.2 Hz | < 500 ms |
| Load sensing | 1 Hz | < 200 ms |
| Fire detection | 10 Hz | < 50 ms |
| PSU controls | Event-driven | < 100 ms |

### Accuracy

| Data Type | Accuracy Requirement |
|-----------|---------------------|
| Temperature | ±0.5°C |
| Load cell weight | ±1% of full scale |
| Position sensors | ±1 mm |
| Occupancy detection | 99% confidence |
| Flow rate | ±5% |

### Reliability

- Critical safety data: 10^-9 probability of undetected error
- Operational data: 10^-6 probability of undetected error
- Entertainment data: Best effort

## Data Storage and Retention

### Real-Time Data

- Buffer: 1 hour of high-frequency data
- Storage: In-memory circular buffer
- Archival: On fault detection or operator request

### Historical Data

- Flight data: Full flight + 30 days
- Fault logs: 1 year
- Trend data: 90 days detailed, 2 years aggregated
- Maintenance data: Life of aircraft

## Data Security

### Classification

- **Public**: Passenger-facing entertainment content
- **Internal**: Operational status, sensor data
- **Restricted**: Maintenance data, fault logs
- **Confidential**: Passenger personal data (PII)

### Protection Measures

- Encryption for PII data (AES-256)
- Network segmentation (cabin vs. flight deck)
- Authentication for management interfaces
- Audit logging for configuration changes

## References

- [Domain Context](./DOMAIN_CONTEXT.md)
- [Dependencies](./DEPENDENCIES.md)
- [ARINC 429 Specification](https://www.aviation-ia.com/standards/)
- [ARINC 664 (AFDX) Specification](https://www.aviation-ia.com/standards/)
- [DO-178C Software Considerations](https://www.rtca.org/)

---

**Last Updated**: 2025-01-15
