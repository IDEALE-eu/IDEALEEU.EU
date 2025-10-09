# 00-CONFIG

## Purpose

Configuration management for Q100 version baseline. Defines configuration sets, rules, and schemas for the ~100 passenger class aircraft (96-110 pax range).

## Directory Structure

- **[RULES.md](RULES.md)** — Configuration rules and constraints specific to Q100
- **SCHEMAS/** — JSON schemas for validating configuration sets
- **CONFIG_SETS/** — YAML configuration set definitions

## Configuration Sets

### [BASELINE-Q100.yaml](CONFIG_SETS/BASELINE-Q100.yaml)
Baseline configuration for Q100 class aircraft with standard passenger layout.

### [CFG-PAX-Q100.yaml](CONFIG_SETS/CFG-PAX-Q100.yaml)
Q100 passenger configuration variant (~100 passengers, range 96-110).

## Usage

Configuration sets define:
- Passenger capacity and layout
- Performance parameters (MTOW, range, fuel capacity)
- System options and variants
- Equipment fitment

Each configuration must:
1. Validate against schema in [config-set.schema.json](SCHEMAS/config-set.schema.json)
2. Comply with rules in [RULES.md](RULES.md)
3. Be traceable to requirements (see [03-TRACEABILITY](../03-TRACEABILITY/))

## Effectivity

Configuration sets are mapped to specific aircraft serial numbers via [MSN_EFFECTIVITY.csv](../01-EFFECTIVITY/MSN_EFFECTIVITY.csv).

## References

- **Configuration Management Plan:** [01-CM_PLAN.md](../../../../../../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
- **Baselines:** [04-BASELINES](../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
- **Change Control:** [06-CHANGES](../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
