# 56-70 SENSOR_HEALTH_DELAMINATION — Windows (BWB-H2-Hy-E, Q100)

**Purpose**: Sensors and monitoring systems for window health, delamination detection, crack monitoring, and lifecycle tracking. **Interfaces with ATA-31 (Indicating/Recording) and ATA-42 (IMA).**

## Scope
- Delamination detection sensors (acoustic, ultrasonic)
- Crack monitoring systems
- Temperature sensors (for heating system)
- Impact detection sensors (bird strike, hail)
- Health and usage monitoring integration (ATA-93)
- Data acquisition and processing
- Sensor wiring and installation
- Integration with aircraft health monitoring systems

## Key Requirements
- **Detection**: Early detection of delamination and cracks
- **Reliability**: High availability, low false alarm rate
- **Integration**: Data interface to ATA-31/42 systems
- **Installation**: Non-intrusive sensor mounting
- **Coverage**: Adequate coverage of critical window areas
- **Maintenance**: Built-in test capability, fault detection

## Interfaces
- **31 Indicating/Recording** — Health status display, fault indication
- **42 IMA** — Sensor data integration, health monitoring algorithms
- **92 EWIS** — Sensor wiring and power distribution
- **93 HUMS** — Health and usage monitoring system integration

## Deliverables
- Sensor specifications and locations (CAD)
- Sensor installation procedures (CAI)
- Data acquisition and processing design (CAS)
- Validation and testing results (CAV)
- Troubleshooting procedures (CAS)

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline in the [PLM/CAx/](./PLM/CAx/) directory.

### Engineering BOM
See [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) for Bill of Materials references.

## Directory Structure

```
56-70_SENSOR_HEALTH_DELAMINATION/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/  — Sensor layouts, wiring diagrams
      ├─ CAE/  — Sensor coverage analysis
      ├─ CAO/  — Sensor placement optimization
      ├─ CAI/  — Installation procedures
      ├─ CAM/  — Manufacturing specifications
      ├─ CAV/  — Validation testing
      ├─ CAP/  — Production procedures
      ├─ CAS/  — System operation, troubleshooting
      └─ CMP/  — Materials processing
```

## Configuration Management
- Changes via ECR/ECO per `00-PROGRAM/CONFIG_MGMT/`

## References
- Parent system: [56-WINDOWS](../../README.md)
- Standards: [56-00_STANDARDS_GENERAL](../56-00_STANDARDS_GENERAL/README.md)
- Interface with: [31-INDICATING_RECORDING], [42-IMA]
