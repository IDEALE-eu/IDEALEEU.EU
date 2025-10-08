# Partition Definitions Directory

This directory contains IMA partition definitions, CPU allocations, memory allocations, and partition-to-application bindings.

## Contents

Key files for ARINC 653 partition management:
- Partition definitions with resource allocations
- Timing budgets and scheduling parameters
- Application-to-partition bindings
- Module-to-partition mappings

## File Format

Partition maps typically in CSV format following `../../00-COMMON/TEMPLATES/PARTITION_MAP.csv`.

Required fields:
- Partition_ID
- Partition_Name
- Module_ID
- Core_Assignment
- Memory_MB
- CPU_Percent
- Period_ms
- Safety_Level (DAL-A through DAL-E)
- Hosted_Application
- Status

## Expected Files

- `PARTITION_MAP.csv` - Master partition mapping
- `CPU_ALLOCATIONS.csv` - CPU percentage allocations
- `MEMORY_ALLOCATIONS.csv` - Memory allocations
- `TIMING_BUDGETS.csv` - Timing windows and periods

## Validation

Ensure:
- CPU allocations per core do not exceed 100%
- Memory allocations fit within module capacity
- Timing budgets allow for worst-case execution time (WCET)
- Partition isolation requirements met

## Related Files

- `../BASELINE/IMA_PLATFORM_CONFIG.xml` - Complete ARINC 653 configuration
- `../BASELINE/PARTITION_BINDINGS.csv` - Detailed application bindings

---

**Last Updated**: 2024-01-15
