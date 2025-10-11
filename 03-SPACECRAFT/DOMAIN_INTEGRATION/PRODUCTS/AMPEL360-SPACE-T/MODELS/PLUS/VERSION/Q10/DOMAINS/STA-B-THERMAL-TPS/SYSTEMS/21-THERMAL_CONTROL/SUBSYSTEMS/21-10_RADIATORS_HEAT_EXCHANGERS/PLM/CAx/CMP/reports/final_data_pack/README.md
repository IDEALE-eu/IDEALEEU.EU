# FINAL_DATA_PACK — Final Data Package

## Purpose

This directory contains the final data package manifest including IEF (Information Exchange Format) manifest, digital checksums, and delivery certification.

## Contents

- IEF manifest (JSON format)
- SHA256 checksums for all deliverables
- Configuration baseline documentation
- As-built configuration
- Delivery acceptance certificate
- Data rights and restrictions documentation

### IEF Manifest Contents

```json
{
  "subsystem": "21-10_RADIATORS_HEAT_EXCHANGERS",
  "baseline": "Q10",
  "delivery_date": "2025-XX-XX",
  "files": [
    {
      "path": "CAD/...",
      "sha256": "...",
      "size": "...",
      "type": "..."
    }
  ]
}
```

### Checksum Verification

- SHA256 for file integrity
- Verify before and after transfer
- Document any discrepancies
- Re-generate if files modified

## File Naming

```
21-10-CMP-FINAL_DATA_PACK_<topic>__r<NN>__<STATUS>.<ext>
```

## Standards

- Follow ECSS and NASA documentation standards
- Maintain version control through PLM system
- Configuration control per project procedures

## Related Documentation

- Parent directory: [`../README.md`](../README.md) 
- Requirements: [`../requirements/`](../requirements/) or [`../../requirements/`](../../requirements/)
- System documentation: [`../../../EBOM_LINKS.md`](../../../EBOM_LINKS.md)
