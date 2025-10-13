# CUSTOMER — Customer-Specific Configurations

This directory contains customer-specific configurations for the BWB-H2-Hy-E aircraft model.

## Purpose

CUSTOMER configurations represent aircraft configurations tailored to specific customer requirements under defined contracts. These configurations:
- Reference baseline or variant configurations
- Include customer-specific modifications
- Are controlled under customer contracts
- Maintain full traceability to customer requirements

## Structure

```
CUSTOMER/
└── <CUST_ID>/                   # Customer identifier (placeholder)
    └── FAMILY/
        └── Q100_STD01/          # Aircraft family
            └── CONTRACT/
                └── <CNTRCT_ID>/  # Contract identifier (placeholder)
                    └── VERSION/
                        └── HEAD/
                            └── EFFECTIVITY/
                                └── <range>/  # Customer serial range (placeholder)
```

## Configuration Hierarchy

### CUSTOMER ID Level
- **<CUST_ID>** - Customer identifier placeholder
  - Replaced with actual customer code (e.g., AAL, DAL, etc.)
  - One directory per customer
  - Maintains customer confidentiality as needed

### FAMILY Level
- **Q100_STD01** - Base aircraft family
  - References standard family configuration
  - Customer configuration built on family baseline

### CONTRACT Level
- **<CNTRCT_ID>** - Contract identifier placeholder
  - Replaced with actual contract number
  - One directory per contract
  - Multiple contracts per customer possible

### VERSION Level
- **HEAD** - Active development version
  - Used during contract negotiation and configuration
  - Frozen upon contract signature
  
- **R01, R02, ...** - Released versions (future)
  - Frozen customer configurations
  - Delivered configuration baseline

### EFFECTIVITY Level
- **<range>** - Customer serial range placeholder
  - Replaced with actual serial number range (e.g., 0500-0520)
  - Defines aircraft delivered under this contract
  - May be non-contiguous ranges

## Usage

### Creating Customer Configuration

1. Obtain customer contract and requirements
2. Create customer directory structure
3. Define customer-specific effectivity range
4. Document configuration requirements
5. Reference base configuration
6. Develop customer-specific modifications

### Customer Configuration Content

At the EFFECTIVITY level, include:
- **CUSTOMER_SPEC.md** - Customer specification document
- **REQUIREMENTS.md** - Customer requirements traceability
- **DELTA_FROM_BASELINE.md** - Differences from baseline
- Configuration identifiers
- Customer-specific systems and equipment
- Interior configuration
- Special provisions
- Delivery acceptance criteria

### Configuration Privacy

Customer configurations may contain sensitive information:
- Pricing and commercial terms
- Proprietary equipment
- Special mission capabilities
- Delivery schedules

**Note:** Use appropriate access controls and confidentiality measures.

## Example Structure

Real customer configuration example:

```
CUSTOMER/
├── AAL_AEROSPACE/
│   └── FAMILY/
│       └── Q100_STD01/
│           └── CONTRACT/
│               ├── CTR-2026-001/
│               │   └── VERSION/
│               │       └── HEAD/
│               │           └── EFFECTIVITY/
│               │               └── 0500-0520/
│               └── CTR-2027-015/
│                   └── VERSION/
│                       └── HEAD/
│                           └── EFFECTIVITY/
│                               └── 0800-0825/
```

## Integration

Customer configurations integrate with:
- **Base Configuration** - `CONF/BASELINE/` or `CONF/VARIANT/`
- **Effectivity System** - `BASELINE/FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/`
- **Contract Management** - Customer contract database
- **Modification System** - `BASELINE/FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/MODS/`

## Change Control

Customer configuration changes:
- Require customer approval
- Follow standard ECR/ECO process
- May trigger contract amendments
- Must maintain contract compliance
- Full traceability to customer requirements

## Customer Acceptance

Each customer configuration must:
- Meet customer specification
- Complete customer acceptance testing
- Include customer-required documentation
- Obtain customer sign-off
- Include delivery acceptance criteria

## Compliance

Customer configurations must comply with:
- Customer specification and requirements
- Contract terms and conditions
- Regulatory requirements
- Export control regulations (ITAR/EAR)
- Baseline configuration standards

## Template Files

The placeholder structure `<CUST_ID>/...<CNTRCT_ID>/...<range>/` serves as a template. When creating actual customer configurations:

1. Replace `<CUST_ID>` with actual customer identifier
2. Replace `<CNTRCT_ID>` with actual contract number
3. Replace `<range>` with actual serial number range
4. Remove template directory once real configurations exist

## References

- **Base Configuration** - [CONF/BASELINE/](../BASELINE/)
- **Configuration Management** - [00-PROGRAM/CONFIG_MGMT/](../../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Effectivity** - [BASELINE/FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/](../BASELINE/FAMILY/Q100_STD01/VERSION/Q100/01-EFFECTIVITY/)
- **Contract Management** - Customer contract system

---

**Owner:** Configuration Management & Contracts  
**Status:** Template (placeholder structure)  
**Last Updated:** 2025-10-13  
**Note:** This is a template structure. Actual customer directories should be created as contracts are awarded.
