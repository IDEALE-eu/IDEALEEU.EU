# ZONES — Drawings Organized by Center Body Zones

## Purpose

This directory organizes drawings by physical location within the 53-10 Center Body, divided into Forward (FWD), Center (CTR), and Aft (AFT) zones.

## What to Store

Zone-based organization provides an alternative view of drawings based on physical location, complementing the type-based organization in the parent directory.

### Zone-Organized Drawings
- Symbolic links or copies of drawings from type directories (PART, ASSEMBLY, etc.)
- Zone-specific design packages
- Zone installation sequences
- Zone inspection packages
- Zone manufacturing packages

## Zone Definitions

### FWD (Forward Zone)
- **Description**: Forward section of center body
- **Typical stations**: Fuselage stations 0-500 (example)
- **Major components**: 
  - Forward frames (F01-F10)
  - Forward skin panels
  - Forward floor sections
  - Nose interface fittings
  - Cockpit structure attachments

### CTR (Center Zone)
- **Description**: Center section of center body
- **Typical stations**: Fuselage stations 500-1000 (example)
- **Major components**:
  - Center frames (F11-F20)
  - Wing interface structure
  - Main landing gear bay
  - Center fuel tank boundaries
  - Wing carry-through structure

### AFT (Aft Zone)
- **Description**: Aft section of center body
- **Typical stations**: Fuselage stations 1000-1500 (example)
- **Major components**:
  - Aft frames (F21-F30)
  - Aft skin panels
  - Aft floor sections
  - Aft fuselage interface
  - Empennage attachment provisions

## Subdirectories

- [`FWD/`](./FWD/) - Forward zone drawings
- [`CTR/`](./CTR/) - Center zone drawings
- [`AFT/`](./AFT/) - Aft zone drawings

## Organization Methods

### Option 1: Symbolic Links (Recommended)
Use symbolic links to reference drawings in type directories:
```bash
ln -s ../../PART/53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf FWD/
ln -s ../../ASSEMBLY/53-10_DWG_ASM_WING-INTERFACE_D1100_SH1_RevA.pdf CTR/
```

### Option 2: Zone Index Files
Create index files that list drawings by zone:
- `FWD/ZONE_FWD_INDEX.md` - List of all FWD zone drawings
- `CTR/ZONE_CTR_INDEX.md` - List of all CTR zone drawings
- `AFT/ZONE_AFT_INDEX.md` - List of all AFT zone drawings

### Option 3: Zone-Specific Packages
Create zone-specific drawing packages:
- `FWD/53-10_FWD_ZONE_PACKAGE_v01.pdf` - Complete FWD zone package
- `CTR/53-10_CTR_ZONE_PACKAGE_v01.pdf` - Complete CTR zone package
- `AFT/53-10_AFT_ZONE_PACKAGE_v01.pdf` - Complete AFT zone package

## Benefits of Zone Organization

### Manufacturing
- Facilitates zone-based manufacturing strategy
- Supports parallel manufacturing of zones
- Simplifies work package organization
- Enables zone-specific tooling and fixtures

### Installation
- Organizes drawings by installation sequence
- Groups interface drawings by zone
- Supports zone-based quality control
- Facilitates zone completion sign-off

### Maintenance
- Enables zone-based maintenance planning
- Groups related components for service
- Supports zone isolation for maintenance
- Facilitates damage assessment by zone

## Usage Guidelines

### Creating Zone Organization
1. Identify component zone assignment
2. Create links or references to type-based drawings
3. Maintain consistency with type directories
4. Update zone indices when drawings added
5. Note any components spanning multiple zones

### Multi-Zone Components
Some components span multiple zones:
- **Keel beam**: Runs full length (FWD+CTR+AFT)
- **Stringers**: May span multiple zones
- **Floor beams**: May span FWD+CTR or CTR+AFT
- **Skin panels**: May span zone boundaries

**Handling**: Link to primary zone, note in secondary zones, or link in all applicable zones

## Related Directories

- **Type organization**: [`../PART/`](../PART/), [`../ASSEMBLY/`](../ASSEMBLY/), etc.
- **Installation drawings**: [`../INSTALLATION/`](../INSTALLATION/)
- **Detail drawings**: [`../DETAIL/`](../DETAIL/)
- **Index**: [`../INDEX/`](../INDEX/) - Master drawing index

## Best Practices

### Zone Assignment
- Assign components to primary zone based on major location
- Note multi-zone components in all applicable zones
- Use consistent station ranges for zone boundaries
- Document zone boundary definitions clearly

### Maintenance
- Keep zone links synchronized with type directories
- Update zone indices when drawings are added/revised
- Maintain consistency across zone views
- Verify links periodically

### Drawing References
- Use relative paths for links
- Reference source drawing location
- Note revision in zone indices
- Track zone-specific configurations

## Quality Requirements

### Zone Organization Checklist
- [ ] All zone components identified
- [ ] Drawings linked or indexed correctly
- [ ] Multi-zone components noted
- [ ] Zone boundaries defined
- [ ] Indices up to date
- [ ] Links functional
- [ ] Revisions tracked

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **FWD Zone**: [`./FWD/README.md`](./FWD/README.md) - Forward zone details
- **CTR Zone**: [`./CTR/README.md`](./CTR/README.md) - Center zone details
- **AFT Zone**: [`./AFT/README.md`](./AFT/README.md) - Aft zone details
