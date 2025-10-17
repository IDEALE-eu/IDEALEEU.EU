# A360 Data Models

**Version:** 1.0  
**Status:** Active  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/DATA-MODELS`

## Overview

This directory contains the canonical data models for the A360exchanges-TT platform. All models are designed for:
- EU regulatory compliance (ESPR, DPP, CRA, WEEE)
- Integration with existing PLM systems
- Blockchain/QS anchoring capability
- Multi-tenant support

## Model Categories

### Core Models
- `asset.schema.json` - Asset definition and specifications
- `unit.schema.json` - Individual unit/serial tracking
- `listing.schema.json` - Marketplace listings
- `lease.schema.json` - Lease contracts
- `repair.schema.json` - Repair workflows

### Token Models
- `stake.schema.json` - Staking positions
- `fee_event.schema.json` - Fee transactions
- `reward.schema.json` - Reward distributions

### Compliance Models
- `dpp.schema.json` - Digital Product Passport
- `eu_repair_form.schema.json` - Right-to-Repair form
- `sbom.schema.json` - Software Bill of Materials
- `weee.schema.json` - WEEE categorization

## Schema Format

All schemas follow JSON Schema Draft-07 specification:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://idealeeu.eu/schemas/a360/...",
  "title": "...",
  "type": "object",
  "properties": { ... },
  "required": [ ... ]
}
```

## Validation

Schemas can be validated using standard JSON Schema validators:
```bash
# Python
python -m jsonschema -i instance.json schema.json

# Node.js
ajv validate -s schema.json -d instance.json
```

## Evolution Policy

### Versioning
- Major version: Breaking changes
- Minor version: Backward-compatible additions
- Patch version: Clarifications and fixes

### Deprecation
- Minimum 6-month notice period
- Migration guides provided
- Dual-version support during transition

## Integration Points

### UTCS
- All models include `utcs_anchor` field
- Links to component traceability threads

### PLM
- Asset and Unit models sync with EBOM/MBOM
- Part numbers aligned with `00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER`

### Finance
- Fee events integrate with `10-BUSINESS/FINANCE`
- Token rewards link to Teknia system

## Files

- [asset.schema.json](./asset.schema.json)
- [unit.schema.json](./unit.schema.json)
- [listing.schema.json](./listing.schema.json)
- [lease.schema.json](./lease.schema.json)
- [repair.schema.json](./repair.schema.json)
- [stake.schema.json](./stake.schema.json)
- [fee_event.schema.json](./fee_event.schema.json)
- [dpp.schema.json](./dpp.schema.json)
- [eu_repair_form.schema.json](./eu_repair_form.schema.json)

## Usage Examples

See [../09-EXAMPLES/](../09-EXAMPLES/) for practical usage examples of each model.
