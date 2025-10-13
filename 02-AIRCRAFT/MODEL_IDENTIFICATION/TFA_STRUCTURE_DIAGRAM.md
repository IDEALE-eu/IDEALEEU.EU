# TFA Structure Visualization

## Complete Hierarchy Diagram

```
02-AIRCRAFT/
│
└── MODEL_IDENTIFICATION/                          # Root of TFA structure
    │
    ├── README.md                                  # TFA documentation
    ├── TFA_IMPLEMENTATION_SUMMARY.md              # Implementation details
    ├── TFA_QUICK_REFERENCE.md                     # Quick reference guide
    │
    └── {PRODUCT_ID}/                              # e.g., AMPEL360-AIR-T
        │
        ├── README.md                              # Product documentation
        │
        └── ARCH/                                  # Architecture variants
            │
            └── {ARCH_ID}/                         # e.g., BWB-H2-Hy-E
                │
                ├── README.md                      # Architecture documentation
                │
                └── FAMILY/                        # Product families
                    │
                    └── {FAMILY_ID}/               # e.g., Q100_STD01
                        │
                        ├── README.md              # Family documentation
                        │
                        └── DOMAIN/                # Engineering domains
                            │
                            └── {DOMAIN_ID}/       # e.g., AAA-AIRFRAMES-...
                                │
                                ├── README.md      # Domain documentation
                                │
                                └── ATA-{XX}/      # ATA chapter (e.g., ATA-53)
                                    │
                                    ├── README.md  # ATA chapter doc
                                    │
                                    └── SYSTEMS/   # Systems in this chapter
                                        │
                                        └── ATA-{XX}-{YY}/  # e.g., ATA-53-10
                                            │
                                            ├── README.md   # System doc
                                            │
                                            ├── PLM/        # Product Lifecycle
                                            │   │
                                            │   ├── README.md
                                            │   │
                                            │   └── CAx/    # Computer-Aided tools
                                            │       │
                                            │       ├── README.md
                                            │       │
                                            │       ├── CAD/    # Design
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAE/    # Engineering
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAM/    # Manufacturing
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAI/    # Integration
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAO/    # Optimization
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAP/    # Production
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAS/    # Service
                                            │       │   └── README.md
                                            │       │
                                            │       ├── CAV/    # Verification
                                            │       │   └── README.md
                                            │       │
                                            │       └── CMP/    # Management
                                            │           └── README.md
                                            │
                                            └── CONF/       # Configuration
                                                │
                                                ├── README.md
                                                │
                                                └── BASELINE/
                                                    │
                                                    └── COMPONENTS/
                                                        │
                                                        └── {COMPONENT_ID}/  # e.g., ATA-53-10-01
                                                            │
                                                            └── SUBPRODUCT/
                                                                │
                                                                └── {SUBPROD_ID}/  # e.g., SUBPROD_001
                                                                    │
                                                                    ├── SUBPRODUCT_INDEX.csv
                                                                    │
                                                                    └── SUBJECT/
                                                                        │
                                                                        └── {SUBJECT_ID}/  # e.g., SUBJ_001
                                                                            │
                                                                            ├── SUBJECT_META.json
                                                                            ├── SUBJECT_MANIFEST.csv
                                                                            ├── SUBJECT_CONFIG.yml
                                                                            │
                                                                            └── RANGE-EFFECT/
                                                                                │
                                                                                └── {RANGE}/  # e.g., 0001-9999
                                                                                    │
                                                                                    └── artifacts/
                                                                                        │
                                                                                        ├── 01-{item}/
                                                                                        │   ├── META.json
                                                                                        │   ├── MANIFEST.csv
                                                                                        │   ├── CONFIG.yml
                                                                                        │   └── DOC/
                                                                                        │       └── README.md
                                                                                        │
                                                                                        └── 02-{item}/
                                                                                            ├── META.json
                                                                                            ├── MANIFEST.csv
                                                                                            ├── CONFIG.yml
                                                                                            └── DOC/
```

## Hierarchy Levels

### Level 1: Root
- **MODEL_IDENTIFICATION/** - TFA root directory

### Level 2: Product
- **{PRODUCT_ID}/** - Aircraft product line
- Example: `AMPEL360-AIR-T/`

### Level 3: Architecture
- **ARCH/{ARCH_ID}/** - Configuration variant
- Example: `ARCH/BWB-H2-Hy-E/`

### Level 4: Family
- **FAMILY/{FAMILY_ID}/** - Product family
- Example: `FAMILY/Q100_STD01/`

### Level 5: Domain
- **DOMAIN/{DOMAIN_ID}/** - Engineering domain
- Example: `DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/`

### Level 6: ATA Chapter
- **ATA-{XX}/** - ATA Spec 100 chapter
- Example: `ATA-53/` (Fuselage)

### Level 7: Systems
- **SYSTEMS/ATA-{XX}-{YY}/** - Specific system
- Example: `SYSTEMS/ATA-53-10/` (Center Body)

### Level 8: Dual Branch

#### Branch A: PLM
- **PLM/CAx/** - Product Lifecycle Management
  - 9 categories: CAD, CAE, CAM, CAI, CAO, CAP, CAS, CAV, CMP

#### Branch B: CONF
- **CONF/BASELINE/COMPONENTS/** - Configuration Management
  - Component tracking
  - Subproduct organization
  - Subject management
  - Effectivity ranges
  - Artifact storage

## Navigation Examples

### Example 1: Access CAD Models for Center Body
```
MODEL_IDENTIFICATION/
  AMPEL360-AIR-T/
    ARCH/BWB-H2-Hy-E/
      FAMILY/Q100_STD01/
        DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/
          ATA-53/
            SYSTEMS/ATA-53-10/
              PLM/CAx/CAD/
```

### Example 2: Access Configuration Data
```
MODEL_IDENTIFICATION/
  AMPEL360-AIR-T/
    ARCH/BWB-H2-Hy-E/
      FAMILY/Q100_STD01/
        DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/
          ATA-53/
            SYSTEMS/ATA-53-10/
              CONF/BASELINE/COMPONENTS/ATA-53-10-01/
                SUBPRODUCT/SUBPROD_001/
                  SUBJECT/SUBJ_001/
```

### Example 3: Access Specific Artifact
```
MODEL_IDENTIFICATION/
  AMPEL360-AIR-T/
    ARCH/BWB-H2-Hy-E/
      FAMILY/Q100_STD01/
        DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/
          ATA-53/
            SYSTEMS/ATA-53-10/
              CONF/BASELINE/COMPONENTS/ATA-53-10-01/
                SUBPRODUCT/SUBPROD_001/
                  SUBJECT/SUBJ_001/
                    RANGE-EFFECT/0001-9999/
                      artifacts/01-example-item/
```

## Key Features by Level

| Level | Key Features | Purpose |
|-------|--------------|---------|
| **Product** | Product identification | Organize by aircraft program |
| **Architecture** | Variant configuration | Different design configurations |
| **Family** | Product family | Variations within architecture |
| **Domain** | Engineering discipline | Organize by technical area |
| **ATA Chapter** | System category | Industry-standard grouping |
| **System** | Specific subsystem | Detailed system level |
| **PLM/CAx** | Engineering artifacts | Design, analysis, manufacturing |
| **CONF** | Configuration data | Baseline, traceability, control |

## File Distribution

### Documentation Files (20 README.md)
- 1 at MODEL_IDENTIFICATION root
- 1 at PRODUCT level
- 1 at ARCH level
- 1 at FAMILY level
- 1 at DOMAIN level
- 1 at ATA chapter level
- 1 at SYSTEM level
- 1 at PLM level
- 1 at CAx level
- 9 at CAx category levels (CAD, CAE, etc.)
- 1 at CONF level
- 1 at artifact DOC level

### Data Files (10)
- 1 SUBPRODUCT_INDEX.csv
- 1 SUBJECT_META.json
- 1 SUBJECT_MANIFEST.csv
- 1 SUBJECT_CONFIG.yml
- 2 × META.json (per artifact)
- 2 × MANIFEST.csv (per artifact)
- 2 × CONFIG.yml (per artifact)

### Support Documents (2)
- TFA_IMPLEMENTATION_SUMMARY.md
- TFA_QUICK_REFERENCE.md

## Total Structure

- **Directories**: 30+
- **README files**: 20
- **Data files**: 10
- **Support docs**: 2
- **Total files**: 32

---

**Created**: 2025-10-13  
**Purpose**: Visual reference for TFA structure
