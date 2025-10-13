# VARIANT — Configuration Variants

This directory contains configuration variants and derivatives of the BWB-H2-Hy-E aircraft model.

## Purpose

VARIANT configurations represent approved variations from the standard BASELINE configuration. These may include:
- Special mission variants
- Performance variants
- Regional variants
- Derivative configurations

Each variant maintains traceability to the base BASELINE configuration while documenting specific differences.

## Structure

```
VARIANT/
└── FAMILY/
    └── Q100_STD01/              # Base family
        └── V001/                # Variant 001
            └── VERSION/
                └── HEAD/        # Development version
                    └── EFFECTIVITY/
                        └── 0100-0299/  # Variant serial range
```

## Configuration Hierarchy

### FAMILY Level
- **Q100_STD01** - Base aircraft family
  - References the baseline family configuration
  - Maintains compatibility with base family standards

### VARIANT ID Level
- **V001, V002, ...** - Variant identifiers
  - V001 - First approved variant
  - Each variant has unique identifier
  - Documents specific mission or configuration purpose

### VERSION Level
- **HEAD** - Active development version
  - Used for variant development and testing
  - Becomes frozen upon variant release
  
- **R01, R02, ...** - Released versions (future)
  - Frozen variant configurations
  - Certified variant baseline

### EFFECTIVITY Level
- **0100-0299** - Variant serial number range
  - Subset or separate range from baseline
  - Identifies specific aircraft built to this variant
  - May use different numbering scheme for special missions

## Usage

### Creating a New Variant

1. Identify need for configuration variant
2. Obtain CCB approval for variant creation
3. Create variant directory structure under FAMILY
4. Document variant purpose and differences from baseline
5. Establish variant effectivity range
6. Develop configuration in HEAD version

### Variant Documentation

At the EFFECTIVITY level, include:
- **VARIANT_SPEC.md** - Variant specification document
- **DELTA_FROM_BASELINE.md** - Differences from baseline
- Configuration identifiers specific to variant
- System modifications and additions
- Performance characteristics
- Certification basis and deviations

### Applying a Variant Configuration

1. Verify aircraft MSN falls within variant effectivity range
2. Reference base BASELINE configuration
3. Apply variant deltas and modifications
4. Validate variant-specific requirements
5. Cross-reference with effectivity system

## Variant Types

### Special Mission Variants
- Cargo configuration
- VIP transport
- Medical evacuation
- Special operations

### Performance Variants
- Extended range
- High capacity
- Short field capability
- Enhanced performance

### Regional Variants
- Regional certification compliance
- Market-specific configurations
- Environmental adaptations

## Integration

Variants integrate with:
- **Base BASELINE** - `CONF/BASELINE/FAMILY/Q100_STD01/`
- **Effectivity System** - `VERSION/Q100/01-EFFECTIVITY/`
- **Modification System** - `VERSION/Q100/01-EFFECTIVITY/MODS/`

## Change Control

Variant configurations follow same control as BASELINE:
- CCB approval required
- Full traceability to baseline
- Changes tracked through ECR/ECO
- Version control for all modifications

## Certification

Each variant must:
- Have approved certification basis
- Document deviations from baseline
- Complete verification program
- Obtain type certificate amendment or supplemental type certificate

## Example: V001 Configuration

```
VARIANT/FAMILY/Q100_STD01/V001/
├── README.md                    # Variant overview and purpose
├── VERSION/
│   └── HEAD/
│       └── EFFECTIVITY/
│           └── 0100-0299/
│               ├── VARIANT_SPEC.md
│               ├── DELTA_FROM_BASELINE.md
│               ├── CONFIG_DATA/
│               └── CERTIFICATION/
```

## References

- **Base Configuration** - [CONF/BASELINE/](../BASELINE/)
- **Configuration Management** - [00-PROGRAM/CONFIG_MGMT/](../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Effectivity** - [VERSION/Q100/01-EFFECTIVITY/](../../VERSION/Q100/01-EFFECTIVITY/)

---

**Owner:** Configuration Management  
**Status:** Active  
**Last Updated:** 2025-10-13
