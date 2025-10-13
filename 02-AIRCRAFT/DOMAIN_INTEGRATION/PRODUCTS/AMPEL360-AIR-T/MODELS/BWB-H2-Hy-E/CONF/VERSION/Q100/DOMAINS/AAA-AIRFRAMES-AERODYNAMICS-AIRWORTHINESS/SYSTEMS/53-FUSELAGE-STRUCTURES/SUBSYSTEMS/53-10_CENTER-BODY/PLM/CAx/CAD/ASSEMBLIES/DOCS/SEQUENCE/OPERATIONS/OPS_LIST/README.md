# OPS_LIST — Operations Master List

## Purpose

This directory contains the master list of all assembly operations for the 53-10 Center Body, providing an index and overview of all operations.

## Contents

### Master Lists
- **Operations index**: Complete list of all operations
- **Operation sequences**: Order of operations
- **Operation matrix**: Operations by assembly area
- **Resource allocation**: Operations by work center

## List Format

### Information to Include
- Operation number
- Operation description
- Work center
- Estimated time (setup and cycle)
- Required skills/certifications
- Tooling requirements
- Preceding operations
- Following operations

### Example Format
```
OP-001: Frame F05 Installation
  Work Center: Assembly Station A
  Setup Time: 30 min
  Cycle Time: 120 min
  Skills: Level 2 Assembly Tech
  Tooling: Frame Installation Jig
  Precedes: OP-002
```

## Naming Convention

Use the following pattern:
```
53-10_OPS-LIST_<list-type>_<version>.<ext>
```

Examples:
- `53-10_OPS-LIST_MASTER_v01.xlsx`
- `53-10_OPS-LIST_SEQUENCE_v02.xlsx`
- `53-10_OPS-LIST_BY-WORKCENTER_v01.pdf`

## Related Directories

- **OPS_DETAILS**: [`../OPS_DETAILS/`](../OPS_DETAILS/) — Detailed operation sheets
- **Time Study**: [`../../TIME_STUDY/`](../../TIME_STUDY/) — Time standards and methods
