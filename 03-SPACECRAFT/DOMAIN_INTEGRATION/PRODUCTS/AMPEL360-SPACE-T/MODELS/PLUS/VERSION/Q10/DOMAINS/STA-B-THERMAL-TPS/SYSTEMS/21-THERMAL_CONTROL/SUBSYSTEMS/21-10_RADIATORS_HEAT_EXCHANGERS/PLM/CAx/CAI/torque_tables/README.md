# Torque Tables — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Torque tables specify fastener types, sizes, materials, torque values, patterns, and re-torque requirements for radiator, LPHX, and coldplate installations.

## Content Types

- **Torque Specifications** — Target torque values by fastener type/size
- **Torque Patterns** — Tightening sequence diagrams
- **Re-torque Requirements** — Re-torque intervals and acceptance criteria
- **Tool Specifications** — Required torque wrench types and ranges

## File Formats

- `.pdf` — Controlled torque specification documents
- `.xlsx` — Torque data tables (for reference)

## Naming Convention

```
TOR-21-10-{fastener_type}__{revision}.pdf
```

**Examples:**
- `TOR-21-10-M6__r01.pdf`
- `TOR-21-10-M8__r02.pdf`
- `TOR-21-10-M10__r01.pdf`
- `TOR-21-10-4-40__r00.pdf` (inch series if applicable)

## Torque Table Requirements

Each torque table must include:
- **Fastener Specification** — Type, size, grade, material, coating
- **Thread Engagement** — Minimum thread depth
- **Torque Value** — Target torque in N·m with tolerance
- **Lubrication** — Dry, lubed, anti-seize (affects torque)
- **Torque Pattern** — Sequence diagram (star, spiral, etc.)
- **Re-torque** — After cure time or thermal cycle
- **Tooling** — Torque wrench type, range, calibration requirement
- **Witness Requirements** — Inspection hold points
- **Special Conditions** — Temperature, humidity, cleanliness

## Torque Values by Fastener Type

### Metric Fasteners (Typical)

| Size | Grade | Coating | Torque (N·m) | Tolerance |
|------|-------|---------|--------------|-----------|
| M4   | 8.8   | Dry     | 2.5          | ±0.3      |
| M5   | 8.8   | Dry     | 5.0          | ±0.5      |
| M6   | 8.8   | Dry     | 9.0          | ±0.8      |
| M8   | 8.8   | Dry     | 22.0         | ±2.0      |
| M10  | 8.8   | Dry     | 43.0         | ±4.0      |

*Note: Values are typical for steel fasteners into aluminum structure, dry threads. Actual values per engineering specification and fastener material/coating.*

## Torque Patterns

### Star Pattern (Symmetric Bolt Circle)
```
    1
 5     2
    6
 4     3
```
Sequence: 1-3-5-2-4-6, then repeat for final torque

### Spiral Pattern (Non-symmetric)
Start at center or one end, work outward/along in spiral

### Cross Pattern (4-bolt)
```
1     2

3     4
```
Sequence: 1-4-2-3, then repeat

## Re-torque Requirements

- **Initial Torque:** Per table at initial assembly
- **Re-torque Interval:** After adhesive cure (4-24 hours) or thermal cycle
- **Re-torque Acceptance:** Within ±10% of initial torque
- **Documentation:** Record initial and final torque in traveler
- **Non-conformance:** If outside tolerance, investigate for joint relaxation or galling

## Tooling Requirements

- **Torque Wrench Type:** Calibrated beam, click, or electronic
- **Calibration:** Valid cal cert within 6 months
- **Range:** Torque value within 20-80% of wrench full scale
- **Units:** Display N·m or convert from ft-lb with clear labeling
- **Resolution:** ±2% of reading minimum

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Travelers](../travelers/README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)

## Standards & Constraints

- **Units:** N·m (newton-meters) for torque
- **Standards:** Per 51 fastener standards or MIL-STD-1312 equivalents
- **Material Compatibility:** Consider galvanic compatibility
- **Thread Condition:** Clean, dry unless specified otherwise
- **Witness:** Mandatory QA witness for critical joints

## Revision Control

- Torque tables maintained under configuration control
- Changes require structural/mechanical engineering approval
- Coordinate with work instructions and assembly plans
- Previous revisions archived with supersession notice
