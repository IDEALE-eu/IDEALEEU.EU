# TFA Quick Reference Guide

## 🧭 Quick Links

- 🏠 [Back to Main README](./README.md)
- 🗺️ [Interactive Navigation Index](./NAVIGATION_INDEX.md)
- 📊 [Implementation Summary](./TFA_IMPLEMENTATION_SUMMARY.md)
- 🎨 [Structure Diagram](./TFA_STRUCTURE_DIAGRAM.md)

---

## Directory Navigation

### Find a System by ATA Chapter

**Path Pattern:**
```
MODEL_IDENTIFICATION/{PRODUCT}/ARCH/{ARCH}/FAMILY/{FAMILY}/DOMAIN/{DOMAIN}/ATA-{XX}/SYSTEMS/ATA-{XX}-{YY}/
```

**Example (clickable):**
[Navigate to ATA-53-10 Center Body →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/README.md)

## Common Tasks

### Access CAD Models
**Link:** [ATA-53-10 CAD Directory →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/PLM/CAx/CAD/README.md)

### Access Analysis Results
**Link:** [ATA-53-10 CAE Directory →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/PLM/CAx/CAE/README.md)

### Access Configuration Data
**Link:** [ATA-53-10 Configuration →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/CONF/README.md)

### Access Manufacturing Data
**Link:** [ATA-53-10 CAM Directory →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/PLM/CAx/CAM/README.md)

### Access Service Documentation
**Link:** [ATA-53-10 CAS Directory →](./AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/ATA-53/SYSTEMS/ATA-53-10/PLM/CAx/CAS/README.md)

## File Templates

### Create New Artifact

1. Navigate to artifacts directory:
```bash
cd {SYSTEM_PATH}/CONF/BASELINE/COMPONENTS/{COMPONENT}/SUBPRODUCT/{SUBPROD}/SUBJECT/{SUBJECT}/RANGE-EFFECT/{RANGE}/artifacts/
```

2. Create new artifact directory:
```bash
mkdir {SEQ}-{description}
cd {SEQ}-{description}
```

3. Create required files:
```bash
touch META.json MANIFEST.csv CONFIG.yml
mkdir DOC
```

### Naming Conventions

#### Component ID
Format: `ATA-{XX}-{YY}-{ZZ}`
Example: `ATA-53-10-01`

#### Subproduct ID
Format: `SUBPROD_{NNN}`
Example: `SUBPROD_001`

#### Subject ID
Format: `SUBJ_{NNN}`
Example: `SUBJ_001`

#### Effectivity Range
Format: `{NNNN}-{NNNN}`
Example: `0001-9999` (all aircraft)

#### Artifact ID
Format: `{NN}-{description}`
Example: `01-design-specification`

## File Formats

### META.json Structure
```json
{
  "artifact_id": "...",
  "title": "...",
  "description": "...",
  "type": "...",
  "version": "...",
  "status": "...",
  "created_date": "YYYY-MM-DD",
  "modified_date": "YYYY-MM-DD",
  "owner": "...",
  "reviewers": [...],
  "classification": "...",
  "retention_period": "..."
}
```

### MANIFEST.csv Structure
```csv
file_name,file_type,file_size,checksum,created_date,created_by,status
example.pdf,document,1024,sha256:abc123,2025-10-13,Engineer,approved
```

### CONFIG.yml Structure
```yaml
artifact:
  id: ...
  name: ...
  type: ...
  version: ...
  
access_control:
  read: [...]
  write: [...]
  approve: [...]
  
workflow:
  state: ...
  approval_date: ...
  
versioning:
  major: ...
  minor: ...
  patch: ...
```

## ATA Chapter Reference

Common ATA chapters in aircraft systems:

| ATA | System |
|-----|--------|
| 05 | Time Limits / Maintenance Checks |
| 06 | Dimensions and Areas |
| 20 | Standard Practices - Airframe |
| 21 | Air Conditioning |
| 22 | Auto Flight |
| 23 | Communications |
| 24 | Electrical Power |
| 25 | Equipment/Furnishings |
| 26 | Fire Protection |
| 27 | Flight Controls |
| 28 | Fuel |
| 29 | Hydraulic Power |
| 32 | Landing Gear |
| 33 | Lights |
| 34 | Navigation |
| 49 | Airborne Auxiliary Power |
| 51 | Structures (General) |
| 52 | Doors |
| 53 | Fuselage |
| 54 | Nacelles/Pylons |
| 55 | Stabilizers |
| 56 | Windows |
| 57 | Wings |
| 70-79 | Engine chapters |

## PLM Category Guide

| Category | Purpose | Tools |
|----------|---------|-------|
| **CAD** | 3D models, drawings | CATIA, NX, SolidWorks |
| **CAE** | Analysis, simulation | NASTRAN, ANSYS, Abaqus |
| **CAM** | Manufacturing | Mastercam, PowerMill |
| **CAI** | Integration | Enterprise Architect, DOORS |
| **CAO** | Optimization | ModelCenter, HEEDS |
| **CAP** | Production | SAP, DELMIA |
| **CAS** | Service | S1000D tools, Arbortext |
| **CAV** | Verification | TestRail, Polarion |
| **CMP** | Management | MS Project, JIRA |

## Version Control

### Version Numbering
Format: `vMAJOR.MINOR.PATCH`

- **MAJOR**: Significant design changes
- **MINOR**: Updates and improvements
- **PATCH**: Corrections and fixes

Examples:
- `v1.0.0` - Initial release
- `v1.1.0` - Added features
- `v1.1.1` - Bug fixes

### Status Workflow
```
draft → review → approved → released → obsolete
```

## Effectivity Ranges

### Format
`{START}-{END}`

### Examples
- `0001-9999` - All aircraft
- `0001-0100` - First 100 aircraft
- `0101-9999` - After aircraft 100
- `0050-0050` - Only aircraft 50

## Quick Checklist

When creating new system:

- [ ] Create directory structure
- [ ] Add PLM/CAx folders (all 9 categories)
- [ ] Add CONF/BASELINE/COMPONENTS structure
- [ ] Create SUBPRODUCT directory
- [ ] Create SUBPRODUCT_INDEX.csv
- [ ] Create SUBJECT directory
- [ ] Create SUBJECT_META.json
- [ ] Create SUBJECT_MANIFEST.csv
- [ ] Create SUBJECT_CONFIG.yml
- [ ] Create RANGE-EFFECT directory
- [ ] Create artifacts directories
- [ ] Add META.json to each artifact
- [ ] Add MANIFEST.csv to each artifact
- [ ] Add CONFIG.yml to each artifact
- [ ] Create DOC folder in each artifact
- [ ] Add README.md files at key levels

## Support

For questions or issues:
1. Check parent README.md files
2. Review TFA_IMPLEMENTATION_SUMMARY.md
3. Contact Configuration Management team

---

**Version**: 1.0  
**Last Updated**: 2025-10-13
