# packaging

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > packaging**

Model packaging tools and software bill of materials.

## Purpose

This directory contains tools for packaging models and generating SBOM (Software Bill of Materials).

## Contents

- **[fmu_packager.py](fmu_packager.py)** - Script to package models as FMU
- **[sbom/spdx.json](sbom/spdx.json)** - SPDX format SBOM

## Usage

```bash
python fmu_packager.py --model ../models/fuel_cell --output fuel_cell.fmu
```

## Related Documents

- **[../models/](../models/)** - Model artifacts
- **[../compliance/](../compliance/)** - Compliance documentation

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Build Team | Initial packaging tools |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
