# configuration

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > configuration**

Digital twin configuration management, variants, and calibration parameters.

## Purpose

This directory contains configuration artifacts for the digital twin, including variant definitions, calibration parameters, and configuration baselines.

## Contents

- **[variants.manifest.yaml](variants.manifest.yaml)** - Configuration variants for different aircraft configurations
- **[calibration/](calibration/)** - Calibration parameters for sensors, controllers, and environmental models

## Configuration Management

### Variants
Configuration variants support:
- Different aircraft models (e.g., baseline vs. advanced H2 system)
- Different operational profiles (e.g., short-haul vs. long-haul)
- Different sensor suites (e.g., basic vs. enhanced monitoring)

### Calibration
Calibration parameters are organized by subsystem:
- **Sensors**: Calibration offsets, scale factors, noise characteristics
- **Controllers**: Tuning parameters, gains, thresholds
- **Environmental Models**: Atmospheric conditions, wind profiles, icing models

## Usage

Configuration variants are selected at twin instantiation:
```python
twin = DigitalTwin(config_variant="baseline_v1.0")
twin.load_calibration(sensor_cal="calibration/sensors.yaml")
```

## Related Documents

- **[../../05-CALIBRATION_ALIGNMENT/](../../05-CALIBRATION_ALIGNMENT/)** - Calibration methodology
- **[../../04-VERSIONING_CONFIG/](../../04-VERSIONING_CONFIG/)** - Configuration version control
- **[../requirements/](../requirements/)** - Configuration requirements

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Configuration Team | Initial configuration baseline |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
