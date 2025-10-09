# BASELINE PARAMETER SETS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 04-VERSIONING_CONFIG/PARAMETER_SETS > BASELINE**

CDR/PRR default parameters frozen per release.

## Purpose

Baseline parameter sets representing the as-designed configuration at major stage gates.

## Contents

- **CDR_BASELINE_2025-01-15.yaml** - Critical Design Review baseline parameters
- **PRR_BASELINE_TBD.yaml** - Production Readiness Review baseline (future)

## Parameter Categories

### Aerodynamics
- Wing area, aspect ratio, sweep angle
- Airfoil section properties
- Control surface limits (deflection angles)

### Structures
- Material properties (E, G, ρ, σ_y)
- Fatigue S-N curves
- Safety factors (1.5× ultimate load)

### Thermal
- Insulation effectiveness (MLI: 95%)
- Heat exchanger effectiveness (80-95%)
- Ambient condition assumptions (ISA)

### Propulsion
- Engine rated thrust, fuel flow at SLS (sea level static)
- Degradation factors (0% at baseline)

### H₂ Energy
- Tank capacity (kg), insulation properties
- Boil-off rate nominal (1.5% per day)

## Freezing Process

1. **Baseline Selection**: At stage gate (CDR, PRR), freeze current parameters
2. **Version Tag**: Create git tag (e.g., `BASELINE_CDR_2025-01-15`)
3. **Manifest Update**: Update `../MODEL_MANIFEST.yaml` with baseline_id
4. **Change Control**: Any change to baseline requires CR + CCB approval

## Related Documents

- **../MODEL_MANIFEST.yaml** - Model manifest referencing baseline
- **../../00-README.md** - Update policy for baselines

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
