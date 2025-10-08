# AIRCRAFT_EDGE

Aircraft edge device FL clients with runtime constraints and safety boundaries.

## Purpose

FL client implementation for aircraft edge compute platforms, designed for resource-constrained environments with intermittent connectivity and safety-critical isolation requirements.

## Contents

- **00-README.md** - This file
- **RUNTIME_CONSTRAINTS.md** - CPU%, power budget, thermal limits
- **SANDBOXING.md** - ARINC 653/IMA partitioning, cross-domain isolation
- **DIAGNOSTICS/** - Local health checks (disk, memory, model drift)

## Key Characteristics

- **Compute**: ARM Cortex-A53 or equivalent (limited resources)
- **Connectivity**: LEO/GEO satellite (intermittent)
- **Certification**: DO-178C Level C
- **Safety**: ARINC 653 partitioning, no flight-critical actuation

## Related Documents

- **../../../01-ARCHITECTURE/CLIENT_TYPES.md** - Aircraft client specifications
- **RUNTIME_CONSTRAINTS.md** - Detailed resource limits
- **SANDBOXING.md** - Security isolation policies
