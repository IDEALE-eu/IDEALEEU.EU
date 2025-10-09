# OEM — Original Equipment Manufacturer Data

## Purpose

Integration data packages provided by Original Equipment Manufacturers (OEMs) for equipment and systems integrated into the CENTER-BODY subsystem.

## Content Types

- **Installation Drawings** — Equipment mounting and interface drawings
- **Interface Control Documents** — OEM-provided ICDs
- **Envelope Models** — 3D equipment geometry and clearances
- **Load Specifications** — Weight, CG, and dynamic loads
- **Utilities Requirements** — Power, cooling, data interfaces

## File Formats

- `.pdf` — OEM documentation and specifications
- `.step` / `.iges` — 3D CAD models from OEM
- `.csv` — Equipment specifications and schedules
- `.xlsx` — Interface requirement matrices

## Naming Convention

```
OEM_{manufacturer}_{equipment}_{type}_v{version}.{ext}
```

Examples:
- `OEM_Honeywell_APU_installation_dwg_v001.pdf`
- `OEM_Collins_avionics_rack_envelope_v002.step`
- `OEM_Safran_landing_gear_interface_v001.csv`

## Cross-References

- [Parent: SUPPLIER_DATA](../README.md)
- [Tier 1 Supplier Data](../TIER1/README.md)
- [Mounting Provisions](../../MOUNTING/)
- [Interface Definitions](../../INTERFACES/)
- [Access Clearances](../../ACCESS_CLEARANCES/)

## OEM Data Requirements

Each OEM package must include:
- **Equipment specification** — Performance, weight, dimensions
- **Installation requirements** — Mounting, orientation, clearances
- **Interface definitions** — Electrical, hydraulic, pneumatic, data
- **Envelope models** — 3D CAD geometry (neutral format preferred)
- **Maintenance requirements** — Access needs, inspection intervals
- **Certification basis** — TSO, ETSO, or equivalent

## Typical OEM Equipment

| Equipment Type | Typical OEM | Data Package |
|----------------|-------------|--------------|
| APU | Honeywell, Safran | Installation + Interface |
| Landing Gear | Safran, Collins | Full integration package |
| Avionics | Collins, Honeywell | Rack mount + cooling |
| Environmental | Liebherr, Hamilton | Ducting + mounting |
| Fuel Pumps | Parker, Eaton | Installation + electrical |

## Data Package Checklist

OEM deliverables verification:
- [ ] Installation drawing (current revision)
- [ ] Interface Control Document
- [ ] 3D CAD model (STEP or IGES)
- [ ] Weight and CG data
- [ ] Electrical load requirements
- [ ] Cooling/heating requirements
- [ ] Maintenance access requirements
- [ ] Certification documentation

## Integration Process

1. **Data Receipt** — OEM provides integration package
2. **Review** — Engineering review for completeness
3. **CAD Integration** — Import models, check interference
4. **Interface Validation** — Verify compatibility with aircraft
5. **Installation Design** — Design mounting and interfaces
6. **Documentation** — Update aircraft integration data
7. **Approval** — Sign-off by integration lead

## Validation Requirements

- 3D CAD model accuracy verification
- Interface definition validation
- Load data validation (test data preferred)
- Certification documentation review
- Vendor capability assessment

## Change Control

OEM data updates require:
- Revision control and tracking
- Impact assessment on aircraft integration
- ECO if affecting aircraft design
- Re-validation of interfaces
- Update to [INTERFACE_MATRIX](../../INTERFACE_MATRIX/README.md)

## Supplier Management

- Maintain current contact information
- Track revision levels of all OEM data
- Schedule periodic technical interchange meetings (TIMs)
- Coordinate design changes bilaterally
- Maintain supplier performance metrics
