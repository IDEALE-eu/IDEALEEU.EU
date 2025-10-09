# SERIALIZED_INSTANCES

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 04-VERSIONING_CONFIG > SERIALIZED_INSTANCES**

Per-aircraft instance manifests with as-built configuration and calibration deltas.

## Purpose

Store per-aircraft digital twin instances with unique configurations.

## Directory Structure

```
SERIALIZED_INSTANCES/
├── ACFT-001/
│   ├── INSTANCE_MANIFEST.yaml
│   ├── AS_BUILT_CONFIG.yaml
│   ├── MAINTENANCE_LOG.csv
│   └── CALIBRATION_DELTAS.yaml
├── ACFT-002/
│   ├── INSTANCE_MANIFEST.yaml
│   ├── AS_BUILT_CONFIG.yaml
│   ├── MAINTENANCE_LOG.csv
│   └── CALIBRATION_DELTAS.yaml
└── ...
```

## Instance Manifest

Each `INSTANCE_MANIFEST.yaml` contains:
- **aircraft_id**: Unique identifier (e.g., "ACFT-001")
- **serial_number**: Manufacturer serial number
- **registration**: Civil aviation registration (e.g., "N12345")
- **variant**: Configuration variant (e.g., "VARIANT_PAX")
- **baseline_ref**: Reference to baseline parameter set
- **as_built_config_ref**: Path to as-built configuration
- **calibration_deltas_ref**: Path to calibration deltas
- **deployment_date**: Date twin instance deployed
- **owner**: Operating airline/organization

## As-Built Configuration

Manufacturing deviations from baseline (e.g., actual wing rigging angles, engine performance):
```yaml
as_built_deltas:
  structures:
    wing_rigging_left_deg: 2.15  # Nominal: 2.0
    wing_rigging_right_deg: 1.98
  propulsion:
    engine_left_thrust_deviation_percent: +1.2  # 1.2% above nominal
    engine_right_thrust_deviation_percent: -0.5
```

## Calibration Deltas

Post-flight-test calibration adjustments:
```yaml
calibration_deltas:
  aerodynamics:
    cd0_correction: -0.002  # Drag correction from flight test
  thermal:
    h2_boil_off_correction: +0.3  # Percent per day correction
```

## Maintenance Log

CSV format tracking maintenance actions affecting twin:
```csv
date,action_type,component,description,twin_update_required
2025-01-10,replacement,H2_VALVE_01,Replaced H2 valve,yes
2025-01-15,inspection,WING_LEFT,Visual inspection - no issues,no
```

## Instance Lifecycle

1. **Creation**: Upon aircraft rollout, create instance from baseline + as-built config
2. **Calibration**: After flight test, add calibration deltas
3. **Operation**: Update with maintenance actions, usage data
4. **Update**: Periodically sync with new model versions
5. **Retirement**: Archive instance when aircraft decommissioned

## Related Documents

- **../../13-TEMPLATES/INSTANCE_MANIFEST_TEMPLATE.yaml** - Template for new instances
- **../MODEL_MANIFEST.yaml** - Main model manifest
- **../../00-README.md** - Update policy

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
