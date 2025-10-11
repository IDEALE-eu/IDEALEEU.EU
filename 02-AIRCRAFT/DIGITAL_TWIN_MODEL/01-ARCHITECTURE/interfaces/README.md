# interfaces

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > interfaces**

Interface control documents and protocol definitions.

## Purpose

This directory contains interface specifications for digital twin communication with external systems.

## Contents

- **[icd/](icd/)** - Interface Control Documents
  - **[DTM↔06_21_24_40_42_93.csv](icd/DTM↔06_21_24_40_42_93.csv)** - Digital Twin ↔ Aircraft Systems ICD
- **[dds/](dds/)** - Data Distribution Service (DDS) definitions
  - **[idl/dt.idl](dds/idl/dt.idl)** - DDS Interface Definition Language
- **[ros2/](ros2/)** - ROS2 message definitions
  - **[msg/State.msg](ros2/msg/State.msg)** - ROS2 state message

## Interface Types

### ICD (Interface Control Documents)
- Aircraft systems ↔ Digital twin data exchange
- Message formats, protocols, timing

### DDS (Data Distribution Service)
- Real-time publish-subscribe middleware
- IDL definitions for typed data exchange

### ROS2 (Robot Operating System 2)
- Middleware for modular system integration
- Message and service definitions

## Related Documents

- **[../../03-INTERFACES_APIS/](../../03-INTERFACES_APIS/)** - API specifications
- **[../data_contracts/](../data_contracts/)** - Data contracts
- **[../mapping/](../mapping/)** - Signal mappings

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Integration Team | Initial interface definitions |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
