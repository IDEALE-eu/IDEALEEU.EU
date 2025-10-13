# CIR — Centralized Illustration Repository

## Overview

The **Centralized Illustration Repository (CIR)** is the single source of truth for all Illustration Control Numbers (ICNs) in the AMPEL360 AIR-T project. Instead of scattering illustrations across multiple DataModule subdirectories, all ICNs are stored in this central location and referenced using relative paths.

## Directory Structure

```
Illustrations/CIR/
├── _COMMON/                    # Shared/reusable illustrations
│   ├── MASTER/                 # Master source files
│   ├── DERIVED/
│   │   ├── SVG/                # Vector graphics (preferred)
│   │   ├── CGM/                # Computer Graphics Metafile (legacy)
│   │   └── PNG/                # Raster graphics
│   └── ALT_TEXT/               # Alternative text for accessibility
│
└── 53-10/                      # Subsystem-specific illustrations
    ├── MASTER/                 # Master source files (AI, Sketch, etc.)
    │   ├── ICN-53-10-10-0001-A.master
    │   ├── ICN-53-10-20-0001-A.master
    │   └── ...
    ├── DERIVED/
    │   ├── SVG/                # Vector graphics (preferred)
    │   │   ├── ICN-53-10-10-0001-A.svg
    │   │   ├── ICN-53-10-20-0001-A.svg
    │   │   └── ...
    │   ├── CGM/                # Computer Graphics Metafile (legacy)
    │   │   ├── ICN-53-10-10-0001-A.cgm
    │   │   └── ...
    │   └── PNG/                # Raster graphics (min 300 DPI)
    │       ├── ICN-53-10-10-0001-A.png
    │       └── ...
    ├── HOTSPOTS/               # Interactive hotspot maps
    │   ├── ICN-53-10-20-0001-A.map.xml
    │   └── ...
    ├── ALT_TEXT/               # Alternative text descriptions
    │   ├── ICN-53-10-10-0001-A.txt
    │   ├── ICN-53-10-20-0001-A.txt
    │   └── ...
    ├── cir-index.csv           # ICN inventory and metadata
    └── cir-manifest.json       # DMC to ICN mapping
```

## ICN Naming Convention

### Pattern

```
ICN-<chapter>-<section>-<subsection>-<seq>-<issue>.<ext>
```

### Examples

```
ICN-53-10-10-0001-A.svg      # Center Body Forward Bulkhead, SVG
ICN-53-10-20-0001-A.svg      # Center Body Aft Bulkhead, SVG
ICN-53-10-95-0003-A.png      # Generic illustration, PNG
```

### Components

- **chapter**: ATA chapter (e.g., 53 = Fuselage Structures)
- **section**: Subsystem (e.g., 10 = Center Body)
- **subsection**: Component within subsystem (e.g., 10 = Forward Bulkhead, 20 = Aft Bulkhead)
- **seq**: Sequential number (0001-9999)
- **issue**: Revision letter (A-Z)
- **ext**: File extension (svg, png, cgm, master, etc.)

## Linking from Data Modules

### Relative Path Pattern

Data Modules reference ICNs using relative paths from their location in `DataModules/`:

```xml
<!-- For graphicRef -->
<graphicRef xlink:href="../../../Illustrations/CIR/53-10/DERIVED/SVG/ICN-53-10-20-0001-A.svg"/>

<!-- For hotspotRef -->
<hotspotRef xlink:href="../../../Illustrations/CIR/53-10/HOTSPOTS/ICN-53-10-20-0001-A.map.xml"/>
```

### Path Calculation

From a DM in `DataModules/Descriptive/10_SYSTEM-DESCRIPTION/`:
- Go up 3 levels: `../../../`
- Navigate to: `Illustrations/CIR/53-10/DERIVED/SVG/`
- Reference the file: `ICN-53-10-20-0001-A.svg`

## Manifests

### cir-index.csv

Inventory of all ICNs with metadata:

```csv
ICN,Title,Format,Rev,Owner,Effectivity
ICN-53-10-10-0001-A,Center Body Forward Bulkhead Installation,SVG,A,AMPEL360,ALL
ICN-53-10-20-0001-A,Center Body Aft Bulkhead Assembly,SVG,A,AMPEL360,ALL
```

**Fields:**
- **ICN**: Illustration Control Number
- **Title**: Human-readable description
- **Format**: Primary format (SVG, PNG, CGM)
- **Rev**: Current revision letter
- **Owner**: Responsible organization
- **Effectivity**: Applicability (ALL, or specific configuration)

### cir-manifest.json

Maps Data Module Codes (DMCs) to their referenced ICNs for CI/CD cross-checks:

```json
{
  "dmc_to_icn_mapping": {
    "DMC-AMP360-AAA-53-10-10-00A-040A-D": [
      "ICN-53-10-10-0001-A"
    ],
    "DMC-AMP360-AAA-53-10-20-00A-040A-D": [
      "ICN-53-10-20-0001-A"
    ]
  }
}
```

This manifest enables automated validation to ensure:
- All referenced ICNs exist
- ICN files are not orphaned
- Version consistency across references

## File Management

### MASTER Files

- **Purpose**: Original source files from authoring tools (Adobe Illustrator, Sketch, etc.)
- **Extension**: `.master` (or actual format like `.ai`, `.sketch`)
- **Storage**: Keep in `MASTER/` subdirectory
- **Versioning**: Track in version control or external asset management

### DERIVED Files

- **Purpose**: Export formats for publication (SVG, PNG, CGM)
- **Generation**: Automated export from MASTER files
- **Formats**:
  - **SVG**: Preferred vector format for web/digital publications
  - **PNG**: Raster format at 300+ DPI for print
  - **CGM**: Legacy format for some systems

### ALT_TEXT Files

- **Purpose**: Accessibility descriptions for visually impaired users
- **Format**: Plain text (`.txt`)
- **Content**: Concise description of illustration content and purpose
- **Example**:
  ```
  Center Body Forward Bulkhead Installation - Isometric view showing the forward bulkhead assembly with mounting points and structural connections.
  ```

### HOTSPOTS Files

- **Purpose**: Define interactive clickable regions on illustrations
- **Format**: XML (`.map.xml`)
- **Links**: Reference other DMCs for detailed information
- **Example**:
  ```xml
  <hotspot id="hs001" shape="rect" coords="100,100,200,150" 
           target="DMC-AMP360-AAA-53-10-20-10A-040A-D" 
           description="Forward attachment point"/>
  ```

## Workflow

### Creating New ICNs

1. **Create master file** in appropriate tool
2. **Export to MASTER/** directory with naming convention
3. **Generate derived formats**:
   - Export SVG to `DERIVED/SVG/`
   - Export PNG to `DERIVED/PNG/` (300+ DPI)
   - Export CGM if needed to `DERIVED/CGM/`
4. **Create alt-text** in `ALT_TEXT/`
5. **Create hotspots** (if interactive) in `HOTSPOTS/`
6. **Update manifests**:
   - Add entry to `cir-index.csv`
   - Update `cir-manifest.json` with DMC references

### Updating Existing ICNs

1. **Increment revision letter** (A→B→C...)
2. **Update all formats** (MASTER, DERIVED/*)
3. **Update manifests** with new revision
4. **Validate links** in affected DMCs

### Validation

Use the validation tools to ensure integrity:

```bash
# Check all ICN references in DMCs
python ../../VALIDATION/tools/check_links.py ../DataModules/

# Validate manifest consistency
python ../../VALIDATION/tools/validate_cir_manifest.py CIR/53-10/cir-manifest.json
```

## Benefits of CIR

1. **Single Source of Truth**: All ICNs in one location
2. **Version Control**: Clear revision tracking
3. **Reusability**: Illustrations can be referenced by multiple DMCs
4. **Maintainability**: Update once, reflect everywhere
5. **Automation**: Easier CI/CD validation and link checking
6. **Consistency**: Standardized naming and structure
7. **Accessibility**: Centralized alt-text management

## Best Practices

1. **Never duplicate ICNs** - Always reference from CIR
2. **Use relative paths** - Ensures portability
3. **Keep MASTER files** - Enable future edits
4. **Generate DERIVED** - Automate exports when possible
5. **Document changes** - Update manifests with each ICN change
6. **Validate regularly** - Run link checks in CI/CD pipeline
7. **Version consistently** - Follow revision letter sequence
8. **Archive old revisions** - Keep history for traceability

## Migration from Old Structure

If migrating from the old scattered ICN structure:

1. **Identify all ICNs** across DataModule subdirectories
2. **Consolidate to CIR** with new naming convention
3. **Update DMC references** to use relative paths
4. **Create manifests** (cir-index.csv, cir-manifest.json)
5. **Validate all links** using validation tools
6. **Remove old ICN directories** after validation

## Related Documentation

- **Conventions**: `../GUIDES/Conventions.md` - Naming standards
- **Style Guide**: `../GUIDES/StyleGuide.md` - Illustration guidelines
- **Validation**: `../VALIDATION/README.md` - Link checking tools
- **DataModules**: `DataModules/README.md` - DM structure

## Support

For questions about CIR structure or ICN management:
- Review this documentation
- Check validation tools in `../VALIDATION/`
- Contact AMPEL360 Technical Publications team
