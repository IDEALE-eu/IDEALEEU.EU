# TOPIC_NAMING_CONVENTION

Kafka/MQTT topic naming standards for fleet telemetry.

## Format

```
{domain}.{platform}.{system}.{parameter}.{version}
```

## Domain Prefixes

| Domain | Code | Description |
|--------|------|-------------|
| Fleet Operations | `fl` | Live telemetry from operational fleet |
| Digital Twin | `dt` | Synthetic telemetry from digital twins |
| Maintenance | `mro` | Maintenance events and reports |
| Simulation | `sim` | Test rig and simulator data |

## Platform Identifiers

| Platform | Code | Description |
|----------|------|-------------|
| Aircraft | `acft` | Fixed-wing aircraft (H2-powered) |
| Spacecraft | `sc` | Satellites and space vehicles |
| Ground Station | `gs` | Ground segment telemetry |
| Simulator | `sim` | Hardware-in-the-loop simulators |

## System Codes

### Aircraft Systems (ATA Chapters)
| System | Code | ATA Chapter |
|--------|------|-------------|
| Hydrogen Propulsion | `h2` | 28 (Fuel), 71 (Powerplant) |
| Engine | `eng` | 71-80 |
| Flight Controls | `fctl` | 27 |
| Avionics | `avx` | 31, 34, 45, 46 |
| Guidance/Navigation | `gnc` | 34 |
| Cabin | `cabin` | 21, 35 |

### Spacecraft Systems (ECSS)
| System | Code | Description |
|--------|------|-------------|
| Power | `power` | Electrical power system |
| Thermal | `thermal` | Thermal control |
| Propulsion | `prop` | Chemical/electric propulsion |
| Guidance/Navigation | `gnc` | AOCS (Attitude and Orbit Control) |
| Payload | `payload` | Mission payload instruments |
| Communications | `comm` | TT&C and payload comms |

## Versioning

Schema version appended as `v{major}`:
- `v1` - Initial schema
- `v2` - Breaking change (new major version)

Minor/patch versions do NOT change topic name (backward compatible).

## Examples

```
# Aircraft Hydrogen Systems
fl.acft.h2.tank_pressure_fwd.v1
fl.acft.h2.tank_pressure_aft.v1
fl.acft.h2.flow_rate_eng1.v1
fl.acft.h2.temp_fuel_line.v1

# Aircraft Engine
fl.acft.eng.n1_speed_eng1.v1
fl.acft.eng.egt_eng1.v1
fl.acft.eng.oil_pressure_eng1.v1

# Spacecraft Power
fl.sc.power.battery_voltage_bus1.v1
fl.sc.power.solar_current_panel1.v1
fl.sc.power.load_current.v1

# Spacecraft Propulsion
fl.sc.prop.thrust_thruster1.v1
fl.sc.prop.fuel_mass_remaining.v1

# Maintenance Events
mro.acft.events.fault_detected.v1
mro.acft.maintenance.task_complete.v1
mro.sc.anomaly.radiation_upset.v1
```

## Wildcard Subscriptions

Consumers can subscribe to multiple topics using wildcards:

```
# All aircraft telemetry
fl.acft.*.*.v1

# All hydrogen system parameters
fl.acft.h2.*.v1

# All telemetry for a specific system across platforms
fl.*.h2.*.v1

# All versions of a specific parameter
fl.acft.h2.tank_pressure_fwd.*
```

## Deprecated Topics

When a topic is deprecated (schema breaking change):
1. New topic created with incremented version (e.g., `v2`)
2. Old topic marked DEPRECATED in schema registry
3. Dual-publish for 90 days (both `v1` and `v2`)
4. After 90 days, old topic archived (read-only)
5. After 1 year, old topic deleted

## Related Documents

- **../../SCHEMA_REGISTRY/TELEMETRY_SCHEMA_VERSIONING.md** - Schema versioning
- **../../SCHEMA_REGISTRY/COMPATIBILITY_POLICY.md** - Compatibility rules

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial naming convention       | Data Engineering Team |
