# Telemetry Gateways

## Architecture

### Edge Gateway (On-Aircraft)
- **Location**: Avionics bay
- **Function**: Collect, filter, buffer sensor data
- **Protocols**: ARINC 429, AFDX, CAN, MIL-STD-1553
- **Output**: MQTT over cellular/satcom
- **Bandwidth**: Limited (10-100 kbps)
- **Latency**: Real-time critical (<50 ms)

### Ground Gateway (Operations Center)
- **Location**: Operations center datacenter
- **Function**: Receive, decrypt, route telemetry
- **Protocols**: MQTT, AMQP, Kafka
- **Output**: Time-series DB, event bus
- **Bandwidth**: High (Gbps)
- **Latency**: Non-critical (seconds)

### Cloud Gateway (Fleet Analytics)
- **Location**: Cloud infrastructure (AWS/Azure)
- **Function**: Aggregate multi-aircraft data
- **Protocols**: HTTPS, gRPC, Kafka
- **Output**: Data lake, analytics pipelines
- **Bandwidth**: Elastic
- **Latency**: Batch processing (minutes to hours)

## Data Pipeline

```
Aircraft Sensors → Edge Gateway → Satcom/Cellular → Ground Gateway → Message Bus → Digital Twin Runtime
                                                                    → Time-series DB → Analytics
                                                                    → Data Lake → ML Training
```

## Telemetry Streams

### High-Frequency (100 Hz)
- Flight control surfaces
- Engine parameters
- Inertial navigation
- Purpose: Real-time monitoring, control validation

### Medium-Frequency (1 Hz)
- Electrical system voltages/currents
- Hydraulic pressures
- Fuel quantities
- Purpose: System health monitoring

### Low-Frequency (0.1 Hz)
- Cabin environment
- Auxiliary systems
- Non-critical sensors
- Purpose: Operational trends

## Security

### Encryption
- **In-flight**: AES-256-GCM
- **Ground-to-cloud**: TLS 1.3
- **At-rest**: Encrypted storage (AES-256)

### Authentication
- **Aircraft**: X.509 certificates
- **Users**: OAuth 2.0 with MFA
- **Services**: mTLS service mesh

### Integrity
- **Checksums**: SHA-3 for message integrity
- **Signing**: Digital signatures for critical commands
- **Replay Protection**: Timestamp and nonce validation

## Quality of Service

### Reliability
- **Edge**: Store-and-forward during connectivity loss
- **Ground**: Message broker with persistence
- **Cloud**: Multi-region replication

### Availability
- **Target**: 99.9% uptime
- **Redundancy**: Dual satcom/cellular paths
- **Failover**: Automatic with <10s switchover

## Monitoring
- Gateway health metrics
- Message throughput and latency
- Error rates and anomalies
- Bandwidth utilization
