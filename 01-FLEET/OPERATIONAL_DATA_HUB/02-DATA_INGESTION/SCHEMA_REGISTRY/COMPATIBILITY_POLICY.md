# COMPATIBILITY_POLICY

Schema compatibility rules for telemetry evolution.

## Purpose

Defines how schemas can evolve over time while maintaining compatibility with existing producers and consumers.

## Compatibility Modes

### BACKWARD (Default)

**Definition**: New schema can read data written with old schema.

**Guarantee**: Old data readable by new code.

**Use Case**: Consumers upgrade before producers.

**Allowed Changes**:
- ✅ Add optional field with default value
- ✅ Delete field

**Forbidden Changes**:
- ❌ Add required field (no default)
- ❌ Change field type
- ❌ Rename field

**Example**:
```json
// v1.0.0 (old)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"}
  ]
}

// v1.1.0 (new, BACKWARD compatible)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"},
    {"name": "quality", "type": "int", "default": 0}  // Optional field
  ]
}
```

**Reading Old Data with New Schema**:
- Field `quality` not present in old data → use default value (0)
- New consumer reads old data successfully ✅

---

### FORWARD

**Definition**: Old schema can read data written with new schema.

**Guarantee**: New data readable by old code.

**Use Case**: Producers upgrade before consumers.

**Allowed Changes**:
- ✅ Delete field
- ✅ Add optional field (if old code ignores unknown fields)

**Forbidden Changes**:
- ❌ Add required field
- ❌ Change field type
- ❌ Rename field

**Example**:
```json
// v1.0.0 (old)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"},
    {"name": "obsolete_field", "type": "string"}
  ]
}

// v1.1.0 (new, FORWARD compatible)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"}
    // "obsolete_field" deleted
  ]
}
```

**Reading New Data with Old Schema**:
- Field `obsolete_field` not present in new data → old consumer uses default or null
- Old consumer reads new data successfully ✅

---

### FULL

**Definition**: Both BACKWARD and FORWARD compatible.

**Guarantee**: Bidirectional compatibility (old ↔ new).

**Use Case**: Gradual rollout (mixed producers/consumers).

**Allowed Changes**:
- ✅ Add optional field with default value

**Forbidden Changes**:
- ❌ Delete field (breaks BACKWARD)
- ❌ Add required field (breaks BACKWARD)
- ❌ Change field type (breaks both)
- ❌ Rename field (breaks both)

**Example**:
```json
// v1.0.0
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"}
  ]
}

// v1.1.0 (FULL compatible)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"},
    {"name": "quality", "type": "int", "default": 0}  // Optional with default
  ]
}

// v1.2.0 (FULL compatible)
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"},
    {"name": "quality", "type": "int", "default": 0},
    {"name": "sensor_id", "type": "string", "default": "unknown"}  // Another optional
  ]
}
```

**Bidirectional Compatibility**:
- v1.0.0 can read v1.1.0 and v1.2.0 (ignores new fields) ✅
- v1.2.0 can read v1.0.0 and v1.1.0 (uses defaults) ✅

---

### NONE

**Definition**: No compatibility guarantees.

**Guarantee**: None. Breaking changes allowed.

**Use Case**: Major refactoring, complete redesign.

**Allowed Changes**:
- ✅ Any change (at your own risk)

**Required**:
- ❌ Engineering Change Request (ECR)
- ❌ CCB approval
- ❌ Consumer impact assessment
- ❌ Migration plan

**Example**:
```json
// v1.5.0
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"}
  ]
}

// v2.0.0 (NONE compatibility, BREAKING)
{
  "fields": [
    {"name": "event_time", "type": "long"},  // Renamed
    {"name": "pressure_bar", "type": "float"},  // Type change
    {"name": "unit", "type": "string"}  // New required field
  ]
}
```

**Migration Required**:
- New topic: `fl.acft.h2.pressure.v2`
- Dual-publish for 90 days
- Consumers migrate to v2
- Deprecate v1

---

## Compatibility Decision Tree

```
┌─────────────────────────────────────┐
│ Do you need to change field types   │
│ or rename fields?                   │
└──────────────┬──────────────────────┘
               │
        Yes ◄──┴──► No
         │            │
         ▼            ▼
   ┌─────────┐  ┌──────────────────────┐
   │  NONE   │  │ Are you adding a new  │
   │         │  │ required field?       │
   └─────────┘  └──────────┬───────────┘
                           │
                    Yes ◄──┴──► No
                     │            │
                     ▼            ▼
               ┌─────────┐  ┌────────────────────┐
               │  NONE   │  │ Do you need old     │
               │         │  │ consumers to read   │
               └─────────┘  │ new data?           │
                            └──────────┬──────────┘
                                       │
                                Yes ◄──┴──► No
                                 │            │
                                 ▼            ▼
                           ┌─────────┐  ┌─────────┐
                           │  FULL   │  │BACKWARD │
                           └─────────┘  └─────────┘
```

## Compatibility Enforcement

### At Schema Registration
```bash
# Check compatibility before registering
schema-registry-cli check-compatibility \
  --schema new_schema.json \
  --subject h2_tank_pressure_fwd \
  --version latest

# Output
✅ Compatible (BACKWARD): Can register as v1.2.0
❌ Incompatible (BACKWARD): Breaks compatibility, requires MAJOR version bump
```

### Automatic Validation
- **CI/CD**: Compatibility checked in PR pipeline
- **Pre-commit Hook**: Local validation before commit
- **Registry**: Rejects incompatible schemas at registration

### Override Process (NONE compatibility)
1. Create Engineering Change Request (ECR)
2. Document rationale and impact
3. Obtain CCB approval
4. Mark schema with `compatibility: NONE`
5. Increment MAJOR version
6. Execute migration plan

## Real-World Examples

### Example 1: Add Sensor Quality (BACKWARD)

**Scenario**: Add quality indicator to existing pressure signal.

**Compatibility Mode**: BACKWARD

**Change**:
```json
// Add optional field with default
{"name": "quality", "type": "int", "default": 0}
```

**Version**: 1.3.0 → 1.4.0 (MINOR)

**Migration**: None (old consumers work without changes)

---

### Example 2: Remove Deprecated Field (FORWARD)

**Scenario**: Remove unused `legacy_id` field.

**Compatibility Mode**: FORWARD

**Change**:
```json
// Delete field: "legacy_id"
```

**Version**: 1.4.0 → 1.5.0 (MINOR, but requires consumer testing)

**Migration**: Ensure consumers don't depend on `legacy_id`

---

### Example 3: Change Unit (NONE - Breaking)

**Scenario**: Change pressure unit from bar to PSI.

**Compatibility Mode**: NONE

**Change**:
```json
// Same field name, different unit (semantic change)
{"name": "pressure", "type": "double"}  // Now in PSI, was bar
```

**Version**: 1.5.0 → 2.0.0 (MAJOR)

**Migration**:
1. Create new topic: `fl.acft.h2.pressure.v2`
2. Dual-publish (v1 in bar, v2 in PSI)
3. Update all consumers to v2
4. Deprecate v1 after 90 days

---

### Example 4: Add Optional Metadata (FULL)

**Scenario**: Add optional sensor ID for traceability.

**Compatibility Mode**: FULL

**Change**:
```json
{"name": "sensor_id", "type": "string", "default": "unknown"}
```

**Version**: 1.5.0 → 1.6.0 (MINOR)

**Migration**: None (bidirectional compatibility maintained)

---

## Best Practices

### 1. Default to BACKWARD Compatibility
- Most common use case
- Allows consumers to upgrade first
- Minimizes disruption

### 2. Use FULL for Critical Signals
- Safety-critical telemetry
- High-availability systems
- Gradual rollout scenarios

### 3. Avoid NONE Compatibility
- Only for major refactoring
- Requires ECR and CCB approval
- High coordination cost

### 4. Always Add Default Values
- Makes BACKWARD compatibility easier
- Reduces migration complexity
- Example: `{"name": "field", "type": "int", "default": 0}`

### 5. Document Schema Changes
- Update schema documentation
- Link to ECR or design document
- Note migration path for consumers

## Related Documents

- **TELEMETRY_SCHEMA_VERSIONING.md** - Semantic versioning rules
- **00-README.md** - Schema registry overview
- **../../09-TEMPLATES/SCHEMA_CHANGE_RFC.md** - Schema change process

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial compatibility policy    | Data Engineering Team |
