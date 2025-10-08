# REAL_TIME_STREAM

Real-time streaming telemetry ingestion configuration.

## Purpose

Defines Kafka/MQTT topic naming conventions, stream processing specifications, and real-time data flow for aircraft and spacecraft telemetry.

## Topic Naming Convention

### Format
```
{domain}.{platform}.{system}.{parameter}.{version}
```

### Components
- **domain**: `fl` (fleet), `dt` (digital twin), `mro` (maintenance)
- **platform**: `acft` (aircraft), `sc` (spacecraft), `sim` (simulator)
- **system**: ATA/ECSS chapter code or system identifier
- **parameter**: Specific signal or parameter name
- **version**: Schema version (`v1`, `v2`, etc.)

### Examples

**Aircraft Telemetry:**
```
fl.acft.h2.pressure.v1          # Hydrogen tank pressure
fl.acft.h2.flow_rate.v1         # Hydrogen flow rate
fl.acft.eng.n1_speed.v1         # Engine N1 speed
fl.acft.gnc.altitude.v1         # Altitude
fl.acft.cabin.temp.v1           # Cabin temperature
```

**Spacecraft Telemetry:**
```
fl.sc.power.battery_voltage.v1  # Battery voltage
fl.sc.thermal.radiator_temp.v1  # Radiator temperature
fl.sc.prop.thrust.v1            # Thruster output
fl.sc.gnc.attitude_q.v1         # Attitude quaternion
fl.sc.payload.image_count.v1    # Payload image count
```

**Maintenance and Events:**
```
mro.acft.events.fault_detected.v1    # Fault event
mro.acft.maintenance.task_complete.v1 # Maintenance completion
```

## Message Format

### Schema (Avro)
```json
{
  "type": "record",
  "name": "TelemetryMessage",
  "namespace": "ideale.fleet.telemetry",
  "fields": [
    {"name": "timestamp", "type": "long", "doc": "UTC timestamp (milliseconds since epoch)"},
    {"name": "platform_id", "type": "string", "doc": "Aircraft/spacecraft registration or serial number"},
    {"name": "signal_name", "type": "string", "doc": "Signal identifier (matches EBOM)"},
    {"name": "value", "type": ["double", "long", "string", "boolean"], "doc": "Measured value"},
    {"name": "unit", "type": "string", "doc": "Unit of measurement (SI preferred)"},
    {"name": "quality", "type": "int", "doc": "Quality indicator (0=good, 1=suspect, 2=bad)"},
    {"name": "source", "type": "string", "doc": "Data source identifier (sensor ID, system name)"}
  ]
}
```

### Example Message (JSON representation)
```json
{
  "timestamp": 1704067200000,
  "platform_id": "AC-H2-001",
  "signal_name": "h2_tank_pressure_fwd",
  "value": 285.3,
  "unit": "bar",
  "quality": 0,
  "source": "PT-H2-FWD-001"
}
```

## Stream Processing Specifications

See [**STREAM_PROCESSING_SPECS/**](STREAM_PROCESSING_SPECS/) for detailed specifications.

**Processing Stages:**
1. **Deserialization** - Parse Avro/Protobuf message
2. **Schema Validation** - Check against registered schema
3. **Enrichment** - Add flight phase, mission phase, configuration baseline
4. **Windowing** - Aggregate over time windows (e.g., 1-minute averages)
5. **Anomaly Detection** - Apply real-time anomaly detectors
6. **Routing** - Partition by platform, system, date
7. **Sink** - Write to raw vault and forward to consumers

**Performance:**
- **Latency**: <2 seconds (p99)
- **Throughput**: 100k messages/sec per partition
- **Parallelism**: Auto-scale based on lag

## Quality of Service (QoS)

### Kafka Configuration
- **Replication Factor**: 3 (for production topics)
- **Min In-Sync Replicas**: 2
- **Retention**: 7 days (real-time topics), 30 days (archived topics)
- **Compression**: LZ4 (balance between CPU and bandwidth)

### MQTT Configuration (for constrained networks)
- **QoS Level**: 1 (at-least-once delivery)
- **Keep-Alive**: 60 seconds
- **Clean Session**: False (persist subscriptions)
- **Max Message Size**: 256 KB

## Security

- **Encryption**: TLS 1.3 in transit
- **Authentication**: SASL/SCRAM or OAuth 2.0
- **Authorization**: ACLs per topic (read/write permissions)
- **Audit**: All access logged to audit trail

## Monitoring

**Key Metrics:**
- Topic lag (messages behind)
- Consumer lag (time behind)
- Message rate (messages/sec)
- Error rate (failed deserializations)

**Alerts:**
- Lag >10,000 messages
- Consumer down >5 minutes
- Error rate >1%

## Related Documents

- **../../SCHEMA_REGISTRY/TELEMETRY_SCHEMA_VERSIONING.md** - Schema versioning
- **../../DATA_VALIDATION_RULES.md** - Validation rules
- **../../../09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json** - Schema template

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial topic naming and specs  | Data Engineering Team |
