# CONF — Configuration Management Structure

This directory contains the configuration management structure for the BWB-H2-Hy-E aircraft model, organizing configurations by type, family, version, and effectivity.

## Purpose

The CONF directory provides a hierarchical structure for managing different types of configurations:
- **BASELINE** - Standard production configurations
- **VARIANT** - Configuration variants and derivatives
- **CUSTOMER** - Customer-specific configurations
- **TEST** - Test and development configurations

## Directory Structure

```
CONF/
├── BASELINE/           # Standard production configurations
├── VARIANT/            # Configuration variants
├── CUSTOMER/           # Customer-specific configurations
└── TEST/               # Test configurations
```

## Configuration Types

### BASELINE

Standard production configurations organized by:
- **FAMILY** - Aircraft family designation (e.g., Q100_STD01)
- **VERSION** - Configuration version (HEAD for development, R01+ for releases)
- **EFFECTIVITY** - Serial number ranges (e.g., 0001-9999)

Path pattern: `BASELINE/FAMILY/<FAMILY_ID>/VERSION/<VERSION_ID>/EFFECTIVITY/<RANGE>/`

### VARIANT

Configuration variants and derivatives organized by:
- **FAMILY** - Base aircraft family
- **VARIANT ID** - Specific variant designation (e.g., V001)
- **VERSION** - Variant version
- **EFFECTIVITY** - Serial number ranges

Path pattern: `VARIANT/FAMILY/<FAMILY_ID>/<VARIANT_ID>/VERSION/<VERSION_ID>/EFFECTIVITY/<RANGE>/`

### CUSTOMER

Customer-specific configurations organized by:
- **CUSTOMER ID** - Customer identifier placeholder
- **FAMILY** - Aircraft family
- **CONTRACT** - Contract identifier
- **VERSION** - Configuration version
- **EFFECTIVITY** - Customer-specific serial ranges

Path pattern: `CUSTOMER/<CUST_ID>/FAMILY/<FAMILY_ID>/CONTRACT/<CNTRCT_ID>/VERSION/<VERSION_ID>/EFFECTIVITY/<RANGE>/`

### TEST

Test and development configurations organized by:
- **FAMILY** - Aircraft family
- **TEST TYPE** - Type of test (e.g., LOADS_DEV, OPS_TRAINER)
- **MODE** - Test mode (e.g., FTI, SIM)
- **VERSION** - Configuration version
- **EFFECTIVITY** - Test article ranges

Path pattern: `TEST/FAMILY/<FAMILY_ID>/<TEST_TYPE>/MODE/<MODE>/VERSION/<VERSION_ID>/EFFECTIVITY/<RANGE>/`

## Usage

### Creating a New Configuration

1. Identify the configuration type (BASELINE, VARIANT, CUSTOMER, or TEST)
2. Navigate to the appropriate directory hierarchy
3. Create configuration files at the EFFECTIVITY level
4. Document the configuration in the appropriate README
5. Link to relevant effectivity data in `VERSION/Q100/01-EFFECTIVITY/`

### Version Management

- **HEAD** - Active development version
- **R01, R02, ...** - Released versions (frozen, immutable)

### Effectivity Ranges

Effectivity ranges specify which serial numbers or test articles the configuration applies to:
- Production: `0001-9999` (serial number ranges)
- Variants: `0100-0299` (subset of production range)
- Customer: `<range>` (customer-specific range placeholder)
- Test: `FT-0001-0099`, `SIM-ALL` (test article identifiers)

## Integration

This structure integrates with:
- **[VERSION/Q100/01-EFFECTIVITY/](../VERSION/Q100/01-EFFECTIVITY/)** - Master effectivity definitions
- **[VERSION/Q100/00-CONFIG/](../VERSION/Q100/00-CONFIG/)** - Configuration sets
- **[VERSION/Q100/02-RELEASE_TAGS/](../VERSION/Q100/02-RELEASE_TAGS/)** - Release management

## Configuration Control

All configurations must:
- Be approved through the Configuration Control Board (CCB)
- Have traceability to requirements and changes
- Include effectivity data linking to serial numbers
- Maintain version history
- Follow change management procedures

## References

- **Configuration Management Plan** - [00-PROGRAM/CONFIG_MGMT/](../../../../../00-PROGRAM/CONFIG_MGMT/)
- **Effectivity Management** - [VERSION/Q100/01-EFFECTIVITY/](../VERSION/Q100/01-EFFECTIVITY/)
- **Baselines** - [00-PROGRAM/CONFIG_MGMT/04-BASELINES/](../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)

---

**Owner:** Configuration Management  
**Status:** Active  
**Last Updated:** 2025-10-13
