# interfaces/ — ICDs, data models

## Purpose

Define software-visible interfaces: ICDs, messages, signals, and data models with exact formats, units, timing, and integrity rules for DAL A.

## Related

* Parent: [../README.md](../README.md)
* HLRs: [../high/](../high/) · LLRs: [../low/](../low/) · Derived: [../derived/](../derived/)
* Constraints: [../constraints/](../constraints/)
* Schemas: [../schemas/](../schemas/)
* Reviews: [../reviews/](../reviews/) · Changes: [../changes/](../changes/)
* Trace: [../TRACE.md](../TRACE.md)

## Layout

* [icd/](./icd/) — interface specs `IF-XXXX.yaml`
* [messages/](./messages/) — message/frame specs `MSG-XXXX.yaml`
* [signals/](./signals/) — signal dictionaries `SIG-XXXX.yaml`
* [datamodels/](./datamodels/) — logical data models `DM-XXXX.yaml`
* [dictionaries/](./dictionaries/) — bus labels, enums, units tables
* [conformance/](./conformance/) — test vectors, golden frames

## IDs and files

* Interface: `IF-XXXX` → [icd/IF-XXXX.yaml](./icd/)
* Message: `MSG-XXXX` → [messages/MSG-XXXX.yaml](./messages/)
* Signal: `SIG-XXXX` → [signals/SIG-XXXX.yaml](./signals/)
* Data model: `DM-XXXX` → [datamodels/DM-XXXX.yaml](./datamodels/)
* Regex: `^IF-\d{4}$`, `^MSG-\d{4}$`, `^SIG-\d{4}$`, `^DM-\d{4}$`

## Authoring rules

* One source of truth per ID. No duplication.
* Define units, ranges, resolution, scaling, encoding. No TBD/TBC.
* Specify endianness, alignment, signedness, padding.
* Specify rates, deadlines, jitter, freshness, timeouts.
* Define integrity: CRC, sequence counters, auth tags if used.
* Document modes and state-dependent behavior.
* Link to HLR/LLR, design, code, tests in [../TRACE.md](../TRACE.md).
* Version with SemVer. Major = breaking wire or schema change.
* Changes require CR and CCB approval in [../changes/](../changes/).

## Templates

### Interface spec ([icd/](./icd/) `IF-XXXX.yaml`)

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
  CRC: {poly: "0x1021", init: "0xFFFF", reflect: false, append: <offset_bits>}
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

### Message spec ([messages/](./messages/) `MSG-XXXX.yaml`)

```yaml
# MSG-1001 — <Title>

BusId: <CAN ID|ARINC label|UDP port|Topic>
Period_ms: <number>
Deadline_ms: <number>
Packing:
  Endianness: <Little|Big>
  AlignmentBytes: <number>
  Length_bytes: <number>
  Layout:
    - {signal: SIG-0001, bit_offset: 0, bit_len: 16}
    - {signal: SIG-0002, bit_offset: 16, bit_len: 8}
Footer:
  CRC: {offset_bit: <>, len_bit: <>}
  PaddingBitsZeroed: true
Signals: [SIG-0001, SIG-0002]
ValidWhen:
  Mode: [<mode-ids>]
  Preconditions: [<conditions>]
OnInvalid:
  Policy: <discard|latched_prev|safe_default>
  SafeDefaults: {SIG-0001: <value>}
Links:
  IF: IF-0001
  Tests: [TST-xxxx]
Version: 1.0.0
Status: <Draft|Baselined|Changed>
Change: CR-2025-00xx
```

### Signal spec ([signals/](./signals/) `SIG-XXXX.yaml`)

```yaml
# SIG-0001 — <Name>

Unit: "<unit, e.g., m/s^2>"
Range: {min: <>, max: <>}
Resolution: <e.g., 0.01>
Scale: {gain: <>, offset: <>}
Type: <uint8|int16|uQ15.16|float32|enum>
Encoding:
  Enum: [{name: OFF, value: 0}, {name: ON, value: 1}]
  SpecialValues: {NaN: <uses?>, NotAvailable: <code>}
Quality:
  Accuracy: <±unit>
  Precision: <unit or LSBs>
  Hysteresis: <unit>
Timing:
  MaxAge_ms: <number>
  Jitter_ms: <number>
Validity:
  RangeCheck: true
  Plausibility: "<rule or link to TST>"
Links:
  HLR: [HLR-xxxx]
  LLR: [LLR-xxxx]
  MSG: [MSG-1001]
  Tests: [TST-xxxx]
Version: 1.0.0
Status: <Draft|Baselined|Changed>
Change: CR-2025-00xx
```

### Data model ([datamodels/](./datamodels/) `DM-XXXX.yaml`)

```yaml
# DM-0001 — <Logical Model Title>

Description: "<entities and relationships>"
Entities:
  - name: Sensor
    keys: [sensor_id]
    attrs:
      - {name: type, type: enum, values: [ACCEL, GYRO]}
      - {name: range_min, type: float, unit: "<>"}
      - {name: range_max, type: float, unit: "<>"}
Relationships:
  - {from: Sensor, to: Measurement, type: one_to_many}
Constraints:
  Invariants: ["range_min < range_max", "unit consistency"]
SerializationProfile: <JSON-Schema|ASN.1|Proto>
SchemaRef: "../schemas/datamodel.schema.json"
Links:
  HLR: [HLR-xxxx]
  LLR: [LLR-xxxx]
  Tests: [TST-xxxx]
Version: 1.0.0
Status: <Draft|Baselined|Changed>
Change: CR-2025-00xx
```

## Reviews

* Independent review for every IF/MSG/SIG/DM.
* Reject if missing units, ranges, timing, integrity, or links.
* Store records in [../reviews/](../reviews/).

## CI checks

* Schema validation: [../schemas/](../schemas/) (`if.schema.json`, `msg.schema.json`, `sig.schema.json`, `datamodel.schema.json`).
* ID regex and filename match. Unique IDs and signal names.
* No overlapping bitfields; padding explicit; CRC defined if required.
* Units, ranges, endianness, timing present for all signals/messages.
* Bus-load analysis within limits; freshness and timeout consistent with LLRs.
* All LLR `Interfaces/Inputs|Outputs` reference existing `SIG-*` or `MSG-*`.
* [../TRACE.md](../TRACE.md) updated in the same commit.
* Conformance tests in [conformance/](./conformance/) pass on golden vectors.

## Entry / Exit

* **Entry:** PSAC, SDP, SVP, SQAP, SCMP approved.
* **Exit:** Interfaces baselined; conformance tests passing; bus-load and timing verified; trace to HLR/LLR/design/code/tests closed; [../TRACE.md](../TRACE.md) current.
