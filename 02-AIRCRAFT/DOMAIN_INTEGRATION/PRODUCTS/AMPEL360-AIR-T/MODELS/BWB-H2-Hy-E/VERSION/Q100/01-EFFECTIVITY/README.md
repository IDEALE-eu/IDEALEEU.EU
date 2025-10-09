# 01-EFFECTIVITY

## Purpose

Defines the effectivity of configurations, modifications, and serial blocks for Q100 version aircraft. Maps configuration sets to specific aircraft Manufacturing Serial Numbers (MSN).

## Directory Structure

- **MSN_EFFECTIVITY.csv** — Master effectivity mapping table
- **BLOCKS/** — Serial block definitions (production batches)
- **MODS/** — Modification package definitions

## MSN Effectivity

The `MSN_EFFECTIVITY.csv` file maps each aircraft serial number to:
- Configuration set ID
- Serial block
- Modification state
- Effectivity dates
- Special notes

### CSV Format

```csv
msn,config_set_id,serial_block,mod_state,effective_date,notes
```

## Serial Blocks

Serial blocks group aircraft manufactured in the same production batch with common characteristics:

- **BLK-2026A** — First production block (Q1-Q2 2026)
- **BLK-2026B** — Second production block (Q3-Q4 2026)

Each block may have specific:
- Manufacturing dates
- Production location
- Standard equipment fit
- Certification status

## Modification States

Modifications represent changes from baseline configuration:

- **MOD-BASE** — Baseline configuration (as manufactured)
- **MOD-M1** — Modification package 1 (avionics and cabin upgrades)

### Modification Types

- **Embodied:** Incorporated during manufacturing
- **Mandatory:** Required retrofit by specific date
- **Optional:** Customer-selectable retrofit
- **Service Bulletin:** Field-applied change

## Usage

### Query Effectivity
To determine configuration for a specific MSN:
1. Look up MSN in `MSN_EFFECTIVITY.csv`
2. Identify config_set_id and mod_state
3. Reference config set in `../00-CONFIG/CONFIG_SETS/`
4. Reference mod package in `MODS/`

### Apply Configuration Change
To change aircraft configuration:
1. Obtain CCB approval (see `00-PROGRAM/CONFIG_MGMT/05-CCB/`)
2. Update `MSN_EFFECTIVITY.csv` with new effective date
3. Create or update modification definition in `MODS/`
4. Update traceability in `../03-TRACEABILITY/`

## Compliance

All effectivity changes must:
- Be approved by Configuration Control Board (CCB)
- Maintain traceability to requirements
- Document impact on systems and interfaces
- Include verification/validation evidence

## References

- **Serialization:** `00-PROGRAM/CONFIG_MGMT/03-SERIALIZATION.md`
- **Change Process:** `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`
- **Baselines:** `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
- **Versioning:** `00-PROGRAM/CONFIG_MGMT/07-RELEASES/01-POLICY/VERSIONING_SCHEME.md`
