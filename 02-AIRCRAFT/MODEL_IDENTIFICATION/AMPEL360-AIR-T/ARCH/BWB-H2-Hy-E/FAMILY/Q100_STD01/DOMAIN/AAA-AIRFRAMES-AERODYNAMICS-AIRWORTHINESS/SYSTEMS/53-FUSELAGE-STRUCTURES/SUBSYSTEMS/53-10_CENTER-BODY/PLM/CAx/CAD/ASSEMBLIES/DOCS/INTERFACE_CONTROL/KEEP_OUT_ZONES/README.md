# KEEP_OUT_ZONES — Keep-Out Zones and Restricted Volumes

## Purpose

This directory defines keep-out zones, restricted volumes, and no-build areas where components, systems, or structures must not be placed.

## Content Types

### Keep-Out Zone Definitions
- Reserved volumes for future growth
- Maintenance access corridors
- Safety zones around hazards
- EMI/RFI sensitive areas
- Hot zones around high-temperature components
- Rotating equipment envelopes

### Restricted Volume Types
- Hard keep-outs (absolute prohibition)
- Soft keep-outs (coordinate before use)
- Conditional keep-outs (specific conditions)
- Temporary keep-outs (during specific operations)

## File Formats

- `.step` — 3D keep-out zone geometry
- `.pdf` — Keep-out zone drawings and specifications
- `.csv` — Zone definition tables
- `.json` — Machine-readable zone definitions

## Zone Categories

### Safety Keep-Outs
- Emergency egress paths
- Fire zones
- Hot surface zones
- High voltage areas
- Rotating machinery guards
- Pressurized component burst zones

### Maintenance Keep-Outs
- Access corridors
- Tool swing radius
- Equipment removal paths
- Inspection access zones

### System Keep-Outs
- EMI/EMC sensitive volumes
- Antenna fields of view
- Sensor line-of-sight
- Airflow paths
- Wire bundle routing corridors

### Growth Zones
- Future equipment locations
- System expansion volumes
- Upgrade provisions
- Optional equipment zones

## Documentation Structure

### Zone Definition
- Zone ID and name
- 3D geometric boundaries
- Reference coordinate system
- Zone classification (hard/soft/conditional)

### Restrictions
- Prohibited items/activities
- Approval authority for exceptions
- Coordination requirements
- Alternative locations

### Rationale
- Reason for restriction
- Safety or operational basis
- Regulatory requirements
- Design standards

## Naming Convention

```
KOZ_{location}_{reason}_v{version}.{ext}
```

Examples:
- `KOZ_WING-ROOT_MAINTENANCE-ACCESS_v001.step`
- `KOZ_DOOR-AREA_EMERGENCY-EGRESS_v002.pdf`
- `KOZ_NOSE_ANTENNA-FIELD_v001.csv`

## Zone Types

### Hard Keep-Outs (Non-Negotiable)
- Safety-critical zones
- Regulatory-mandated spaces
- Structural load paths
- Critical system paths

### Soft Keep-Outs (Negotiable)
- Preferred maintenance access
- Optimal routing paths
- Growth provisions
- Design preferences

### Conditional Keep-Outs
- Active only during specific flight phases
- Temperature-dependent zones
- Configuration-dependent
- Time-dependent restrictions

## Coordination Process

### Exception Requests
1. Identify need to violate keep-out
2. Document justification
3. Coordinate with zone owner
4. Analyze impacts
5. Obtain approval
6. Update documentation

## Verification Methods

### Design Verification
- 3D CAD interference checking
- Zone boundary validation
- Clearance verification
- Drawing annotation

### Installation Verification
- Physical measurement
- Mock-up verification
- Production build checks

## Cross-References

- [Clearances](../CLEARANCES/)
- [Envelopes and Loads](../ENVELOPES_LOADS/)
- [Interface Control Documents](../ICD/)
- [Material Compatibility](../MATERIAL_COMPATIBILITY/)

## Standards

- **MIL-STD-1472**: Human engineering design criteria
- **DO-160**: Environmental conditions and test procedures
- **FAA regulations**: Safety zones and clearances
- **NFPA 409**: Aircraft hangars - safety requirements
