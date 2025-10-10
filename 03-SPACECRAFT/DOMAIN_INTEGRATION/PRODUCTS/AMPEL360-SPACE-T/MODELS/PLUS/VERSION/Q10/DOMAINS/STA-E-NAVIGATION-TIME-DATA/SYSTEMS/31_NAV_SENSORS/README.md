# System 31: NAV_SENSORS

## Description

Navigation sensor systems including IMUs, star trackers, sun sensors, and horizon sensors for spacecraft attitude and position determination.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [31-10_IMUS_GYROS_ACCELS](./SUBSYSTEMS/31-10_IMUS_GYROS_ACCELS/) - Inertial measurement units, gyroscopes, and accelerometers for attitude and motion sensing.
- [31-20_STAR_TRACKERS](./SUBSYSTEMS/31-20_STAR_TRACKERS/) - Star tracker systems for high-precision attitude determination.
- [31-30_SUN_SENSORS](./SUBSYSTEMS/31-30_SUN_SENSORS/) - Sun sensor systems for coarse and fine sun position determination.
- [31-40_HORIZON_SENSORS](./SUBSYSTEMS/31-40_HORIZON_SENSORS/) - Horizon sensor systems for Earth reference and attitude determination.
- [31-50_SENSOR_FUSION](./SUBSYSTEMS/31-50_SENSOR_FUSION/) - Sensor fusion algorithms and data processing for integrated navigation solution.
- [31-60_ALGORITHMS_ESTIMATION](./SUBSYSTEMS/31-60_ALGORITHMS_ESTIMATION/) - Estimation algorithms for sensor data processing and state estimation.
- [31-80_TESTING_CALIBRATION](./SUBSYSTEMS/31-80_TESTING_CALIBRATION/) - Testing procedures and calibration methods for navigation sensors.

## Directory Structure

```
{SYSTEM}/
├─ README.md (this file)
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/
│  └─ *.csv
└─ SUBSYSTEMS/
   └─ {SUBSYSTEM}/
      ├─ README.md
      └─ PLM/
         ├─ EBOM_LINKS.md
         └─ CAx/
            ├─ CAD/
            ├─ CAE/
            ├─ CAO/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            └─ CMP/
```

## Working with This System

### System Engineers
1. Review [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) for system scope
2. Check [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for interfaces with other systems
3. Navigate to specific subsystems in [SUBSYSTEMS/](./SUBSYSTEMS/)

### Subsystem Engineers
1. Access your subsystem directory under `SUBSYSTEMS/`
2. Review subsystem README for specific requirements
3. Place engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### Configuration Management
- Interface definitions in `INTERFACE_MATRIX/*.csv`
- Engineering BOMs in `SUBSYSTEMS/*/PLM/EBOM_LINKS.md`
- CAx artifacts in `SUBSYSTEMS/*/PLM/CAx/*`

## Navigation

- [⬆️ Back to SYSTEMS](../)
- [📋 Main SYSTEMS README](../README.md)

---

**Status**: Structure scaffolded - Ready for engineering artifact population
