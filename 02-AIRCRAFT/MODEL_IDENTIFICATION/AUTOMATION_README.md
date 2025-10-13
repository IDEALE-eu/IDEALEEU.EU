# TFA Automation Tools

This directory contains automation tools for managing the TFA (Technical Framework Architecture) structure.

## 📋 Contents

- **[Makefile](./Makefile)** - Main automation interface
- **[scripts/add_item.sh](./scripts/add_item.sh)** - Script to add items/artifacts
- **[tools/validate_tree.py](./tools/validate_tree.py)** - Structure validation tool

## 🚀 Quick Start

### 1. View Available Commands

```bash
make help
```

### 2. Initialize PLM Structure

Create the PLM/CAx directory structure for a system:

```bash
make init \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10
```

### 3. Add a New Item/Artifact

Add a new item with all required metadata files:

```bash
make add-item \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01 \
  SUBPROD_ID=SUBPROD_001 \
  SUBJECT_ID=SUBJ_001 \
  ITEM_DESC=design-specification \
  OWNER=StructuralTeam
```

### 4. Validate Structure

Validate that the structure is correct and all files are present:

```bash
make validate \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01
```

## 📖 Detailed Usage

### Makefile Targets

#### `make help`
Display all available commands and their descriptions.

#### `make init`
Initialize PLM/CAx directory structure for a system.

**Required Variables:**
- `DOMAIN` - Domain ID (e.g., `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS`)
- `ATA_CHAPTER` - ATA chapter (e.g., `ATA-53`)
- `ATA_MID` - System ID (e.g., `ATA-53-10`)

**Creates:**
- `PLM/CAx/CAD/` - Computer-Aided Design
- `PLM/CAx/CAE/` - Computer-Aided Engineering
- `PLM/CAx/CAM/` - Computer-Aided Manufacturing
- `PLM/CAx/CAI/` - Computer-Aided Integration
- `PLM/CAx/CAO/` - Computer-Aided Optimization
- `PLM/CAx/CAP/` - Computer-Aided Production
- `PLM/CAx/CAS/` - Computer-Aided Service
- `PLM/CAx/CAV/` - Computer-Aided Verification
- `PLM/CAx/CMP/` - Computer-Aided Management & Planning
- `CONF/BASELINE/COMPONENTS/` - Configuration baseline

#### `make add-item`
Add a new item/artifact to the structure.

**Required Variables:**
- `DOMAIN` - Domain ID
- `ATA_CHAPTER` - ATA chapter
- `ATA_MID` - System ID
- `COMP` - Component ID (e.g., `ATA-53-10-01`)
- `EFFECT` - Effectivity range (default: `0001-9999`)
- `SUBPROD_ID` - Subproduct ID (default: `SUBPROD_001`)
- `SUBJECT_ID` - Subject ID (default: `SUBJ_001`)
- `ITEM_DESC` - Item description (e.g., `design-spec`)
- `OWNER` - Owner/responsible team

**Creates:**
- `SUBPRODUCT_INDEX.csv` - Subproduct inventory
- `SUBJECT_META.json` - Subject metadata
- `SUBJECT_MANIFEST.csv` - Artifact manifest
- `SUBJECT_CONFIG.yml` - Subject configuration
- `artifacts/01-{ITEM_DESC}/META.json` - Artifact metadata
- `artifacts/01-{ITEM_DESC}/MANIFEST.csv` - File manifest
- `artifacts/01-{ITEM_DESC}/CONFIG.yml` - Artifact configuration
- `artifacts/01-{ITEM_DESC}/DOC/README.md` - Documentation folder

#### `make validate`
Validate structure integrity and metadata files.

**Required Variables:**
- `DOMAIN` - Domain ID
- `ATA_CHAPTER` - ATA chapter
- `ATA_MID` - System ID
- `COMP` - Component ID

**Checks:**
- PLM/CAx directory structure (all 9 categories)
- Required metadata files exist
- JSON files are valid
- CSV files have required headers
- YAML files are readable

#### `make list-structure`
Display current structure tree.

#### `make clean`
Remove generated files and temporary artifacts.

#### `make install-deps`
Check for required dependencies.

### Script Usage

#### scripts/add_item.sh

Direct script usage (without Makefile):

```bash
./scripts/add_item.sh \
  AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA-53 \
  ATA-53-10 \
  ATA-53-10-01 \
  0001-9999 \
  SUBPROD_001 \
  SUBJ_001 \
  design-spec \
  StructuralTeam
```

**Arguments (in order):**
1. DOMAIN
2. ATA_CHAPTER
3. ATA_MID (System ID)
4. COMP (Component ID)
5. EFFECT (Effectivity range)
6. SUBPROD_ID
7. SUBJECT_ID
8. ITEM_DESC
9. OWNER

#### tools/validate_tree.py

Direct validation script usage:

```bash
python3 tools/validate_tree.py \
  --domain AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  --ata-chapter ATA-53 \
  --ata-mid ATA-53-10 \
  --comp ATA-53-10-01
```

**Options:**
- `--domain` - Domain ID (required)
- `--ata-chapter` - ATA chapter (required)
- `--ata-mid` - System ID (required)
- `--comp` - Component ID (required)
- `--path` - Base path (default: current directory)

## 📝 Examples

### Example 1: Create Structure for Fuselage Center Body

```bash
# Initialize PLM structure
make init \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10

# Add a design specification artifact
make add-item \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01 \
  SUBPROD_ID=SUBPROD_001 \
  SUBJECT_ID=BWB-01-ESTR-ATA-53-10-01-0001 \
  ITEM_DESC=structural-design-spec \
  OWNER=StructuralEngineering

# Validate the structure
make validate \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01
```

### Example 2: Add Multiple Artifacts

```bash
# Add analysis report
make add-item \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01 \
  SUBPROD_ID=SUBPROD_001 \
  SUBJECT_ID=SUBJ_001 \
  ITEM_DESC=fea-analysis-report \
  OWNER=AnalysisTeam

# Add manufacturing spec
make add-item \
  DOMAIN=AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
  ATA_CHAPTER=ATA-53 \
  ATA_MID=ATA-53-10 \
  COMP=ATA-53-10-01 \
  SUBPROD_ID=SUBPROD_001 \
  SUBJECT_ID=SUBJ_001 \
  ITEM_DESC=manufacturing-spec \
  OWNER=ManufacturingTeam
```

### Example 3: Create Structure for Propulsion System

```bash
# Initialize for a different domain
make init \
  DOMAIN=PPP-PROPULSION-FUEL-SYSTEMS \
  ATA_CHAPTER=ATA-71 \
  ATA_MID=ATA-71-10

# Add propulsion design artifact
make add-item \
  DOMAIN=PPP-PROPULSION-FUEL-SYSTEMS \
  ATA_CHAPTER=ATA-71 \
  ATA_MID=ATA-71-10 \
  COMP=ATA-71-10-01 \
  SUBPROD_ID=SUBPROD_001 \
  SUBJECT_ID=SUBJ_001 \
  ITEM_DESC=propulsion-design \
  OWNER=PropulsionTeam

# Validate
make validate \
  DOMAIN=PPP-PROPULSION-FUEL-SYSTEMS \
  ATA_CHAPTER=ATA-71 \
  ATA_MID=ATA-71-10 \
  COMP=ATA-71-10-01
```

## 🔧 Variables Reference

### All Supported Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `DOMAIN` | Engineering domain ID | `XXX` | `AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS` |
| `ATA_CHAPTER` | ATA chapter number | `ATA-XX` | `ATA-53` |
| `ATA_MID` | System identifier | `ATA-XX-YY` | `ATA-53-10` |
| `COMP` | Component identifier | `ATA-XX-YY-ZZ` | `ATA-53-10-01` |
| `EFFECT` | Effectivity range | `0001-9999` | `0001-9999` |
| `SUBPROD_ID` | Subproduct identifier | `SUBPROD_001` | `SUBPROD_001` |
| `SUBJECT_ID` | Subject identifier | `SUBJ_001` | `BWB-01-ESTR-ATA-53-10-01-0001` |
| `ITEM_DESC` | Item description | `example-item` | `design-specification` |
| `OWNER` | Owner/responsible | `Engineering` | `StructuralEngineering` |

## 🎯 Best Practices

### Naming Conventions

**Subject IDs:**
Use format: `{ARCH}-{SEQ}-{DISCIPLINE}-{COMP}-{NUM}`
- Example: `BWB-01-ESTR-ATA-53-10-01-0001`

**Item Descriptions:**
Use kebab-case, be descriptive:
- ✅ `structural-design-spec`
- ✅ `fea-analysis-report`
- ✅ `manufacturing-procedure`
- ❌ `spec1`
- ❌ `doc`

**Owner Names:**
Use team or department names:
- ✅ `StructuralEngineering`
- ✅ `AnalysisTeam`
- ✅ `ManufacturingDept`

### Workflow

1. **Initialize** - Create PLM structure first
2. **Add Items** - Add artifacts one at a time
3. **Validate** - Run validation after adding items
4. **Document** - Add actual files to DOC/ directories
5. **Update** - Update MANIFEST.csv with file checksums
6. **Re-validate** - Validate again after changes

## 🐛 Troubleshooting

### "Script not found" Error

Make sure scripts are executable:
```bash
chmod +x scripts/add_item.sh
chmod +x tools/validate_tree.py
```

### "Directory already exists" Warning

This is normal if re-running commands. The scripts won't overwrite existing files.

### Validation Failures

Check the output for specific errors:
- Missing files: Run `make add-item` again
- Invalid JSON: Check file syntax
- Invalid CSV: Ensure headers are correct

### Python Not Found

Install Python 3:
```bash
# Ubuntu/Debian
sudo apt-get install python3

# macOS
brew install python3
```

## 📚 Related Documentation

- [Main TFA README](./README.md)
- [Navigation Index](./NAVIGATION_INDEX.md)
- [Quick Reference](./TFA_QUICK_REFERENCE.md)
- [Implementation Summary](./TFA_IMPLEMENTATION_SUMMARY.md)

---

**Last Updated**: 2025-10-13  
**Maintained By**: Configuration Management Team
