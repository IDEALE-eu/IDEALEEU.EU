# VARIANTS PARAMETER SETS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 04-VERSIONING_CONFIG/PARAMETER_SETS > VARIANTS**

Mission/option pack parameter sets (e.g., cargo vs. passenger configuration).

## Purpose

Variant parameter sets representing different aircraft configurations or mission profiles.

## Variants

### VARIANT_PAX (Passenger)
- **Description**: Standard passenger configuration
- **Capacity**: 150 passengers, cargo hold
- **MTOW**: 75,000 kg
- **Range**: 3,500 nm

### VARIANT_CARGO (Cargo)
- **Description**: Cargo-only configuration
- **Capacity**: 20,000 kg cargo payload
- **MTOW**: 78,000 kg
- **Range**: 3,200 nm

### VARIANT_LONG_RANGE (Long Range)
- **Description**: Extended range with additional H₂ tanks
- **Capacity**: 120 passengers, reduced cargo
- **MTOW**: 76,000 kg
- **Range**: 4,500 nm

## Parameter Deltas

Variant parameters are stored as deltas from baseline:

```yaml
variant: VARIANT_CARGO
baseline_ref: CDR_BASELINE_2025-01-15
deltas:
  structures:
    cargo_floor_strength: +50%
    fuselage_mass_kg: +1200
  h2_energy:
    tank_capacity_kg: -200  # Less fuel for shorter range
  aerodynamics:
    drag_count_delta: +5  # Cargo door drag
```

## Application

To apply a variant:
1. Load baseline parameters
2. Apply variant delta
3. Validate combined parameter set
4. Deploy to twin instance

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
