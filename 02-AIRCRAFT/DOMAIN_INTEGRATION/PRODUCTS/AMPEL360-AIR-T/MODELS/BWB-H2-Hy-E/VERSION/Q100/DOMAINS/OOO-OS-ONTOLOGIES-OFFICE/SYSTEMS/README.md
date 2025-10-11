# OOO-OS-ONTOLOGIES-OFFICE — Systems Directory

This directory contains all systems for the OOO (Ontologies & Standards Office) domain.

## Systems Overview

- **20-STANDARD_PRACTICES_AIRFRAME** - Standard practices and methods for airframe design
- **40-AVIONICS_STD_GENERAL** - General avionics standards and templates
- **48-OPTICAL_VIDEO_PLATFORM** - Optical and video system standards
- **58-FLT_COMP_EQUIP_TEMPLATES** - Flight compartment equipment templates
- **59-FLT_COMP_FURNISHINGS_TEMPLATES** - Flight compartment furnishings templates
- **68-ROTORCRAFT_RESERVED_TEMPLATES** - Reserved for rotorcraft (placeholder)
- **69-ROTORCRAFT_RESERVED_TEMPLATES** - Reserved for rotorcraft (placeholder)
- **88-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **89-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **95-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **96-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **97-RESERVED_WIRING_AUX** - Reserved for wiring (all EWIS in 92, keep empty)
- **98-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **99-RESERVED_TEMPLATES** - Reserved templates (placeholder)
- **100-GENERAL** - General templates, naming conventions, and ICD templates

## Top-Level Interface Matrix

See [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for cross-domain interface definitions.

## Structure Convention

Each system follows the pattern:
```
<SYSTEM>/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/
│  └─ *.csv
├─ README.md
└─ SUBSYSTEMS/
   └─ <SUBSYSTEM>/
      ├─ README.md
      ├─ META.json
      ├─ inherit.json
      └─ PLM/
         ├─ EBOM_LINKS.md
         └─ CAx/
            ├─ CAD/
            ├─ CAE/
            ├─ CAO/
            ├─ CAI/
            ├─ CAM/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            └─ CMP/
```

Exception: System 97 (RESERVED_WIRING_AUX) has no PLM/CAx as all EWIS belongs in ATA-92.

---

**Last Updated:** 2025-10-11
