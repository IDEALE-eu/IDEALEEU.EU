# RUNTIME_CONSTRAINTS

Runtime resource constraints for aircraft edge FL clients.

## CPU Constraints

- **Maximum usage**: 30% of total CPU capacity
- **Training priority**: Low (yield to flight-critical systems)
- **Thermal limit**: Suspend training if CPU temp > 75°C

## Memory Constraints

- **Maximum allocation**: 1 GB RAM
- **Swap**: Disabled (no paging to disk)
- **OOM handling**: Graceful degradation, no crash

## Power Constraints

- **Continuous power**: ≤ 50W
- **Peak power**: ≤ 100W (during model upload)
- **Battery backup**: Not required (powered from aircraft bus)

## Disk I/O Constraints

- **Maximum throughput**: 10 MB/s
- **Wear leveling**: SSD write cycles managed
- **Storage limit**: 10 GB for FL client (logs, models, gradients)

## Network Constraints

- **Upload bandwidth**: ≤ 10 Mbps (shared with other systems)
- **Download bandwidth**: ≤ 20 Mbps
- **Connection timeout**: 10 minutes per upload attempt

## Temporal Constraints

- **Training window**: Cruise phase only (altitude > 10,000 ft)
- **No training during**: Takeoff, landing, emergencies
- **Automatic suspension**: High workload or thermal throttling

## Monitoring

- **Metrics**: CPU%, memory%, disk%, network latency
- **Alerts**: Threshold violations logged to 12-METRICS/
- **Enforcement**: cgroups (Linux) or partition manager (RTOS)

## Related Documents

- [**../../02-ORCHESTRATION/SCHEDULER.md**](../../02-ORCHESTRATION/SCHEDULER.md) - Training schedules
- [**SANDBOXING.md**](SANDBOXING.md) - Resource isolation policies
