# icd/ — Interface Control Documents

## Purpose

Store DAL A interface specs `IF-XXXX.yaml` with full trace to messages, signals, HLR/LLR, design, code, and tests.

## Related

* Parent: [../README.md](../README.md)
* HLRs: [../../high/](../../high/) · LLRs: [../../low/](../../low/) · Derived: [../../derived/](../../derived/)
* Messages: [../messages/](../messages/) · Signals: [../signals/](../signals/) · Data models: [../datamodels/](../datamodels/)
* Constraints: [../../constraints/](../../constraints/)
* Schemas: [../../schemas/](../../schemas/)
* Reviews: [../../reviews/](../../reviews/) · Changes: [../../changes/](../../changes/)
* Trace: [../../TRACE.md](../../TRACE.md)

## IDs and files

* ID: `IF-XXXX`
* Filename: `IF-XXXX.yaml` (one interface per file)
* Regex: `^IF-\d{4}$`

## Authoring rules

* Single source of truth per `IF-XXXX`.
* Define units, ranges, scaling, encoding, endianness, alignment, padding.
* Specify rate, deadline, jitter, freshness, timeout.
* Define integrity: sequence counter, CRC, auth tag if used.
* Document modes and FDIR for loss/late/invalid data.
* Link HLR/LLR, design, code, tests in [../../TRACE.md](../../TRACE.md).
* Version with SemVer; CR + CCB required for any change in [../../changes/](../../changes/).

## Template (`IF-XXXX.yaml`)

```yaml
# IF-0001 — <Title>

DAL: A
Scope:
  Provider: <component/process>
  Consumer: <component/process>
Transport:
  Type: <ARINC429|CAN|Ethernet|UART|SPI|I2C|SharedMem|API>
  Link:
    Speed: <e.g., 1Mbps>
    Addressing: <ids/topics/ports>
    Physical: <connector, voltage, termination>
Timing:
  Rate_Hz: <number>
  Deadline_ms: <number>
  Jitter_ms: <number>
  Freshness_ms: <number>
  Timeout_ms: <number>
Encoding:
  Serialization: <Raw|Bitfield|CBOR|ASN.1|Proto>
  Endianness: <Little|Big>
  Alignment: <bytes>
Integrity:
  SequenceCounter: {bits: <>, wrap: <>, offset_bits: <>}
  CRC: {poly: "0x1021", init: "0xFFFF", reflect: false, append_bit_offset: <>}
  AuthTag: {alg: <>, len_bytes: <>}
Content:
  Messages: [MSG-1001, MSG-1002]
Safety:
  HazardRefs: [HAZ-xxxx]
  FDIR: [<loss/late/invalid handling>]
Links:
  HLR: [HLR-xxxx]
  LLR: [LLR-xxxx]
  Design: [DES-xxxx]
  Code: ["src/if/driver.c:120-260"]
  Tests: [TST-xxxx]
Version: 1.0.0
Status: <Draft|Baselined|Changed>
Change: CR-2025-00xx
History:
  - {version: 1.0.0, date: 2025-10-22, change: "initial baseline", by: "<name>"}
Approvals:
  Reviewer: <name>, date: 2025-10-22
  Approver: <name>, date: 2025-10-22
```

## Catalog

> Add one row per interface. Keep links relative. Sort by ID.

| IF                        | Title             | Status    | Provider→Consumer | Transport | Rate [Hz] | Deadline [ms] | Messages                                                                     |
| ------------------------- | ----------------- | --------- | ----------------- | --------- | --------: | ------------: | ---------------------------------------------------------------------------- |
| [IF-0001](./IF-0001.yaml) | Example Interface | Baselined | `NAV` → `FMS`     | CAN       |        50 |            20 | [MSG-1001](../messages/MSG-1001.yaml), [MSG-1002](../messages/MSG-1002.yaml) |

<!--
Template row:
| [IF-XXXX](./IF-XXXX.yaml) | <title> | <Draft/Baselined/Changed> | `<prov>` → `<cons>` | <bus> | <rate> | <deadline> | [MSG-YYYY](../messages/MSG-YYYY.yaml) |
-->

## Reviews

* Independent review required.
* Reject if missing timing, integrity, encoding, or links.
* Store records in [../../reviews/](../../reviews/).

## CI checks

* ID regex and filename match.
* Schema validation: [../../schemas/if.schema.json](../../schemas/if.schema.json).
* No overlapping bitfields across linked [../messages/](../messages/); padding explicit.
* Units, ranges, endianness, timing defined.
* Bus-load and freshness within limits; consistent with LLRs.
* All linked messages and signals exist.
* [../../TRACE.md](../../TRACE.md) updated in the same commit.

## Merge checklist

* `IF-XXXX.yaml` added/updated
* Links to [../messages/](../messages/), [../signals/](../signals/), HLR/LLR, design, code, tests resolve
* CR in [../../changes/](../../changes/) if applicable
* Review logged in [../../reviews/](../../reviews/)
* Trace updated: [../../TRACE.md](../../TRACE.md)
