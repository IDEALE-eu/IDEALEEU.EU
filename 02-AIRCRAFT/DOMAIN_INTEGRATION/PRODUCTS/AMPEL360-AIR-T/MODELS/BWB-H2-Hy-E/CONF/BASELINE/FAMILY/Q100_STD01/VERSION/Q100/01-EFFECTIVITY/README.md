# 01-EFFECTIVITY

Define effectivity for configurations, serial blocks, and modification states for the **Q100** aircraft line. Establishes a clear mapping from **MSN → Config Set + Block + Mod State** with dates and notes.

## Directory

* **[MSN_EFFECTIVITY.csv](MSN_EFFECTIVITY.csv)** — Master effectivity table
* **[BLOCKS/](BLOCKS/)** — Serial block definitions (YAML)
* **[MODS/](MODS/)** — Modification package definitions (YAML)

```
01-EFFECTIVITY/
├─ MSN_EFFECTIVITY.csv
├─ BLOCKS/
│  ├─ BLK-2026A.yaml
│  └─ BLK-2026B.yaml
└─ MODS/
   ├─ MOD-BASE.yaml
   └─ MOD-M1.yaml
```

## MSN Effectivity

**CSV schema**

```csv
msn,config_set_id,serial_block,mod_state,effective_date,notes
```

**Examples**

```csv
Q100-0001,CFG-Q100-BASE,BLK-2026A,MOD-BASE,2026-02-15,Initial delivery configuration
Q100-0020,CFG-Q100-BASE,BLK-2026B,MOD-M1,2026-09-30,Avionics + cabin upgrade per ECO-2026-013
```

## Blocks (production batches)

* **[BLK-2026A](BLOCKS/BLK-2026A.yaml)** — First production block (Q1–Q2 2026)
* **[BLK-2026B](BLOCKS/BLK-2026B.yaml)** — Second production block (Q3–Q4 2026)

**YAML template**

```yaml
block_id: BLK-YYYYX
title: "<short name>"
window:
  start: YYYY-MM-DD
  end:   YYYY-MM-DD
plant: "<site / line>"
standard_fit:
  config_set_id: CFG-Q100-BASE
  mods_default: [MOD-BASE]
cert_status:
  tc_basis: "CS-25 ..."
  notes: ""
```

## Modifications (from baseline)

* **[MOD-BASE](MODS/MOD-BASE.yaml)** — As-manufactured baseline
* **[MOD-M1](MODS/MOD-M1.yaml)** — Avionics & cabin enhancement

**YAML template**

```yaml
mod_id: MOD-M1
title: "Avionics & cabin upgrade"
type: "optional | mandatory | embodied | service_bulletin"
effective_from: YYYY-MM-DD
affected_systems: [ATA-42, ATA-25, ATA-31]
requires:
  - ECO: ECO-2026-013
  - Tests: ["VVP-TC-042", "CAB-ILLUM-015"]
impact:
  weight_delta_kg: +3.2
  power_delta_w: +45
  sw:
    - part_number: "42-IMC-APP-001"
      version: "v1.3.0"
docs:
  icds: ["../../../../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0042.md"]
  evidence: ["../../../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/08-COMPLIANCE/"]
notes: ""
```

## Usage

### Determine configuration for an MSN

1. Find MSN in **[MSN_EFFECTIVITY.csv](MSN_EFFECTIVITY.csv)**.
2. Note `config_set_id` & `mod_state`.
3. Open config set: **[../00-CONFIG/CONFIG_SETS/](../00-CONFIG/CONFIG_SETS/)**.
4. Open mod package: **[MODS/](MODS/)**.

### Apply a configuration change

1. Obtain CCB approval: **[00-PROGRAM/CONFIG_MGMT/05-CCB/](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/05-CCB/)**.
2. Update **MSN_EFFECTIVITY.csv** with new `effective_date`.
3. Add/update YAML in **MODS/** or **BLOCKS/** as needed.
4. Update traceability: **[../03-TRACEABILITY/](../03-TRACEABILITY/)**.
5. Ensure baseline refs are current: **[.../04-BASELINES/](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)**.

## Validation rules (CI)

* Every `msn` must be unique.
* `config_set_id` must exist under **../00-CONFIG/CONFIG_SETS/**.
* `serial_block` must match a file in **BLOCKS/**.
* `mod_state` must match a file in **MODS/**.
* `effective_date` is ISO-8601 (YYYY-MM-DD).
* Changes require an approved ECR/ECO in **[.../06-CHANGES/](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)**.

## Compliance

* CCB-approved effectivity only.
* Full traceability to requirements & ICDs.
* Verification/validation evidence linked in mods/blocks.

## References

* **Serialization:** **[03-SERIALIZATION.md](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/03-SERIALIZATION.md)**
* **Changes:** **[06-CHANGES/](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)**
* **Baselines:** **[04-BASELINES/](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)**
* **Versioning:** **[VERSIONING_SCHEME.md](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/01-POLICY/VERSIONING_SCHEME.md)**

---

**Owner:** Configuration Management
**Status:** Active (Q100 line)
**Review:** At each gate & quarterly

