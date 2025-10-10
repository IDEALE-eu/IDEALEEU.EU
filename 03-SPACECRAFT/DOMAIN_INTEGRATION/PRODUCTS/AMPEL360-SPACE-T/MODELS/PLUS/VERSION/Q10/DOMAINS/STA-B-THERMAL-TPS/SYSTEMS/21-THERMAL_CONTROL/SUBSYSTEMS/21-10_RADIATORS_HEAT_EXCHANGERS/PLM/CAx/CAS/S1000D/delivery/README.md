# DELIVERY — IETP/PDF Delivery Packages

## Purpose

This directory contains **finalized delivery packages** of S1000D technical publications for the 21-10 Radiators & Heat Exchangers subsystem, ready for distribution to maintenance personnel, operators, and support organizations.

## Contents

### IETP Packages
- Interactive Electronic Technical Publications
- S1000D CSDB exports
- SCORM-compliant packages
- Viewer-ready distributions

### PDF Publications
- Maintenance manuals (AMM)
- Component manuals (CMM)
- Illustrated parts catalogs (IPC)
- Combined publications

### Distribution Packages
- Complete documentation sets
- Incremental updates
- Revision packages
- Emergency change distributions

## Directory Structure

```
delivery/
├── ietp/                   # IETP packages
│   ├── ampel360-21-10-v001-00/
│   ├── ampel360-21-10-v001-01/
│   └── latest/            # Symlink to current
├── pdf/                    # PDF publications
│   ├── amm/               # Maintenance manuals
│   ├── cmm/               # Component manuals
│   └── ipc/               # Parts catalogs
├── scorm/                  # SCORM packages
│   └── ampel360-21-10-training/
└── releases/              # Release packages
    ├── 2025-Q1/
    └── 2025-Q2/
```

## Package Types

### IETP (Interactive Electronic Technical Publication)

**Format**: S1000D CSDB export
**Contents**:
- All Data Modules (XML)
- All illustrations (ICN)
- Publication Modules (PM)
- BREX and metadata
- Stylesheets and viewers

**Naming Convention**:
```
AMPEL360-21-10-IETP-v{issue}-{inwork}.zip
```

Example:
```
AMPEL360-21-10-IETP-v001-00.zip
```

### PDF Publications

**Format**: PDF (print-ready)
**Standards**: PDF/A for archival

**Publications**:
1. **AMM** (Aircraft/Spacecraft Maintenance Manual)
   - All maintenance procedures
   - Scheduled maintenance
   - Troubleshooting
   - File: `AMPEL360-21-10-AMM-v001-00.pdf`

2. **CMM** (Component Maintenance Manual)
   - Component-specific procedures
   - Repair and overhaul
   - Depot-level maintenance
   - File: `AMPEL360-21-10-CMM-v001-00.pdf`

3. **IPC** (Illustrated Parts Catalog)
   - Parts lists with illustrations
   - Ordering information
   - Interchangeability data
   - File: `AMPEL360-21-10-IPC-v001-00.pdf`

### SCORM Packages

**Format**: SCORM 2004 or SCORM 1.2
**Purpose**: Training and learning management systems
**Contents**:
- Interactive learning modules
- Assessments and quizzes
- Progress tracking
- Completion certificates

## Release Process

### 1. Pre-Release Validation

- [ ] All DMs pass QC validation
- [ ] Cross-references resolved
- [ ] Illustrations complete and linked
- [ ] Metadata verified
- [ ] Version numbers assigned
- [ ] Release notes prepared

### 2. Package Generation

**IETP Package**:
```bash
# Export CSDB
scripts/export_csdb.sh \
  --output delivery/ietp/ampel360-21-10-v001-00 \
  --include-all \
  --brex brex/BREX-AMPEL360-21-10.xml

# Create ZIP archive
cd delivery/ietp
zip -r ampel360-21-10-v001-00.zip ampel360-21-10-v001-00/
```

**PDF Generation**:
```bash
# Transform PM to PDF
scripts/generate_pdf.sh \
  --pm pm/AMM/PM-AMM-AMPEL360-21-10-Q10.xml \
  --output delivery/pdf/amm/AMPEL360-21-10-AMM-v001-00.pdf \
  --standard PDF/A-1b
```

### 3. Quality Verification

- [ ] IETP package opens in viewer
- [ ] All DMs accessible
- [ ] Illustrations display correctly
- [ ] Navigation works
- [ ] PDF readable and printable
- [ ] Bookmarks and links functional

### 4. Distribution

**Internal Release**:
- Upload to document management system
- Notify authorized users
- Provide access credentials

**External Release**:
- Encrypt if required
- Digital signature
- Secure transfer method
- Track distribution

## Version Control

### Issue Numbers
Format: `{issue}-{inwork}`
- Issue: Major version (001, 002, 003...)
- In-work: Revision number (00, 01, 02...)

Example progression:
- `001-00`: Initial release
- `001-01`: Revision 1
- `002-00`: Major update

### Change Tracking

Document in release notes:
- New Data Modules
- Modified Data Modules
- Deleted/obsoleted DMs
- Illustration changes
- Metadata updates

## Package Contents Manifest

Include `manifest.xml` in each package:
```xml
<manifest>
  <packageId>AMPEL360-21-10-IETP-v001-00</packageId>
  <issueDate>2025-10-11</issueDate>
  <dmCount>127</dmCount>
  <icnCount>83</icnCount>
  <pmCount>3</pmCount>
  <files>
    <file path="dm/000-general/..." />
    <!-- ... -->
  </files>
</manifest>
```

## Distribution Metadata

Include `README.txt` with:
- Package description
- Installation instructions
- System requirements
- Support contact information
- License information
- Known issues

## Archive and Retention

- **Active packages**: Current and previous release
- **Archive**: All historical releases
- **Retention**: Per regulatory requirements
- **Backup**: Off-site secure storage

## Access Control

- **Classification**: Per data sensitivity
- **Distribution list**: Authorized recipients only
- **Encryption**: If required
- **Download tracking**: Log all access

## Review Requirements

Before release:
- [ ] All content validated
- [ ] Package tested on target systems
- [ ] Release notes complete
- [ ] Manifest accurate
- [ ] Version numbers correct
- [ ] Distribution approval obtained

## Related Directories

- **[../../dm/](../../dm/)** — Source Data Modules
- **[../../pm/](../../pm/)** — Publication Modules
- **[../../qc/](../../qc/)** — Quality validation records

---

**Last Updated**: 2025-10-11
