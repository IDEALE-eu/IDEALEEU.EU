# SANDBOXING

Security sandboxing and isolation for aircraft edge FL clients.

## ARINC 653 Partitioning

### Partition Configuration

- **Partition ID**: P-FL-CLIENT (non-critical)
- **Criticality Level**: Level C (Major)
- **Execution Time**: 30% CPU allocation
- **Memory**: 1 GB fixed allocation
- **I/O**: ARINC 664 (AFDX) limited to FL traffic

### Partition Isolation

- **No cross-domain leakage**: FL partition cannot access flight-critical partitions
- **No shared memory**: All IPC via ARINC 653 messaging
- **No direct hardware access**: Mediated by partition manager

## IMA (Integrated Modular Avionics) Integration

### Module Boundaries

- **Physical isolation**: FL client runs on separate compute module (if feasible)
- **Logical isolation**: If shared module, strict ARINC 653 enforcement
- **Network isolation**: FL traffic on separate VLAN (avionics vs. FL)

## Security Policies

### Process Isolation

- **User**: Non-privileged (no root/admin)
- **SELinux/AppArmor**: Mandatory Access Control (MAC) enforced
- **Capabilities**: Minimal (CAP_NET_BIND_SERVICE only)

### File System

- **Read-only root**: Root filesystem mounted read-only
- **Writable**: /var/fl-client (logs, gradients) - 10 GB quota
- **No external mounts**: No USB, SD card access

### Network

- **Firewall**: Only outbound to aggregation server (port 443)
- **No lateral movement**: Cannot access other aircraft systems
- **TLS 1.3**: All communication encrypted

## Fault Containment

### Crash Isolation

- **Watchdog**: 60-second timeout (restart if hung)
- **Core dumps**: Disabled (sensitive data)
- **Graceful degradation**: Failure does not affect flight systems

### Resource Exhaustion

- **OOM killer**: FL client is first to be killed (low priority)
- **CPU throttling**: Automatic if exceeding quota
- **Disk quota**: Hard limit enforced (10 GB)

## Audit and Compliance

- **Audit logs**: Immutable, signed logs to 16-INCIDENT_RESPONSE/AUDIT_LOGS/
- **Compliance**: DO-326A (cybersecurity), DO-178C (software)

## Related Documents

- [**../../05-PRIVACY_SECURITY/THREAT_MODEL.md**](../../05-PRIVACY_SECURITY/THREAT_MODEL.md) - Threat analysis
- [**RUNTIME_CONSTRAINTS.md**](RUNTIME_CONSTRAINTS.md) - Resource limits
- [**../../11-COMPLIANCE/AVIATION.md**](../../11-COMPLIANCE/AVIATION.md) - DO-178C compliance
