# SCHEMA_REGISTRY

Central repository for telemetry schema definitions, versioning, and compatibility management.

## Purpose

The Schema Registry provides:
- **Schema Versioning**: Track schema evolution over time
- **Compatibility Enforcement**: Prevent breaking changes without proper approval
- **Schema Discovery**: Browse available telemetry signals and their definitions
- **Schema Validation**: Ensure messages conform to registered schemas

## Contents

- [**00-README.md**](00-README.md) - This file
- [**TELEMETRY_SCHEMA_VERSIONING.md**](TELEMETRY_SCHEMA_VERSIONING.md) - Semantic versioning and lifecycle states
- [**COMPATIBILITY_POLICY.md**](COMPATIBILITY_POLICY.md) - Compatibility rules (BACKWARD, FORWARD, FULL)

## Schema Structure

Schemas defined in Avro or Protobuf format with metadata:

```json
{
  "schema_id": "h2_tank_pressure_fwd",
  "version": "1.2.0",
  "status": "ACTIVE",
  "compatibility": "BACKWARD",
  "schema": {
    "type": "record",
    "name": "H2TankPressureFwd",
    "namespace": "ideale.fleet.telemetry.h2",
    "doc": "Forward hydrogen tank pressure sensor",
    "fields": [
      {
        "name": "timestamp",
        "type": "long",
        "doc": "UTC timestamp (ms since epoch)"
      },
      {
        "name": "platform_id",
        "type": "string",
        "doc": "Aircraft registration number"
      },
      {
        "name": "pressure",
        "type": "double",
        "doc": "Pressure in bar"
      },
      {
        "name": "quality",
        "type": "int",
        "default": 0,
        "doc": "Quality indicator (0=good, 1=suspect, 2=bad)"
      }
    ]
  },
  "metadata": {
    "ebom_ref": "ATA-28-42-001",
    "unit": "bar",
    "range": [0, 350],
    "sample_rate": "1 Hz",
    "owner": "H2 Propulsion Team",
    "created_at": "2024-01-15T10:00:00Z",
    "updated_at": "2024-06-20T14:30:00Z"
  }
}
```

## Schema Versioning

See [**TELEMETRY_SCHEMA_VERSIONING.md**](TELEMETRY_SCHEMA_VERSIONING.md) for complete specification.

### Semantic Versioning (SemVer)

Format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (remove field, change type)
- **MINOR**: Backward-compatible additions (add optional field)
- **PATCH**: Bug fixes, documentation updates (no schema change)

### Lifecycle States

| State | Description | Actions Allowed |
|-------|-------------|-----------------|
| **DRAFT** | Under development | Edit, delete |
| **ACTIVE** | Production use | Read, create new version |
| **DEPRECATED** | Scheduled for removal | Read only, 90-day notice |
| **ARCHIVED** | Historical reference | Read only |

## Compatibility Policies

See [**COMPATIBILITY_POLICY.md**](COMPATIBILITY_POLICY.md) for complete specification.

### BACKWARD (Default)
- New schema can read data written with old schema
- **Allowed**: Add optional fields, delete fields
- **Forbidden**: Remove required fields, change field types

### FORWARD
- Old schema can read data written with new schema
- **Allowed**: Delete fields
- **Forbidden**: Add required fields

### FULL
- Both BACKWARD and FORWARD
- **Allowed**: Add optional fields with defaults
- **Forbidden**: Remove fields, change types

### NONE
- No compatibility guarantees (use with caution)
- Requires ECR approval

## Schema Registration Process

### 1. Create Schema Definition
```bash
# Use template from ../../09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json
cp ../../09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json my_signal.schema.json
# Edit schema with signal details
```

### 2. Validate Schema
```bash
# Check schema validity
avro-tools validate my_signal.schema.json

# Check compatibility with existing versions
schema-registry-cli check-compatibility \
  --schema my_signal.schema.json \
  --subject h2_tank_pressure_fwd \
  --version latest
```

### 3. Submit for Review
- Create PR with schema file
- Include rationale for changes
- Link to EBOM reference, requirements, NCRs

### 4. Review and Approval
- **Minor Changes**: Data steward approval
- **Major Changes**: ECR required, CCB approval

### 5. Register Schema
```bash
# Register in schema registry
schema-registry-cli register \
  --schema my_signal.schema.json \
  --subject h2_tank_pressure_fwd
```

## Schema Evolution Example

### Version 1.0.0 (Initial)
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "platform_id", "type": "string"},
    {"name": "pressure", "type": "double"}
  ]
}
```

### Version 1.1.0 (Add optional field)
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "platform_id", "type": "string"},
    {"name": "pressure", "type": "double"},
    {"name": "quality", "type": "int", "default": 0}  // BACKWARD compatible
  ]
}
```

### Version 2.0.0 (Breaking change)
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "platform_id", "type": "string"},
    {"name": "pressure_bar", "type": "double"},  // Renamed field (BREAKING)
    {"name": "quality", "type": "int", "default": 0}
  ]
}
```

**Migration Path:**
1. Register v2.0.0 schema
2. Create new topic: `fl.acft.h2.pressure.v2`
3. Dual-publish to v1 and v2 for 90 days
4. Migrate consumers to v2
5. Deprecate v1, archive after 1 year

## Schema Discovery

### Browse Registry
```bash
# List all schemas
schema-registry-cli list

# Get schema details
schema-registry-cli get --subject h2_tank_pressure_fwd --version latest

# Search by EBOM reference
schema-registry-cli search --ebom ATA-28-42-001
```

### Query Metadata
```bash
# Find schemas by owner
schema-registry-cli query --owner "H2 Propulsion Team"

# Find deprecated schemas
schema-registry-cli query --status DEPRECATED
```

## Integration with Data Catalog

Schema Registry synchronized with Metadata Registry:
- Schemas exported to `../../03-DATA_STORAGE/METADATA_REGISTRY/DATA_DICTIONARY.csv`
- Lineage tracked in `../../03-DATA_STORAGE/METADATA_REGISTRY/LINEAGE_GRAPH/`

## Monitoring

**Key Metrics:**
- Total schemas registered
- Schemas by lifecycle state
- Schema validation failures
- Compatibility check failures

**Alerts:**
- Schema validation failure rate >1%
- Unauthorized schema registration attempt

## Related Documents

- **../INGESTION_PIPELINES/REAL_TIME_STREAM/TOPIC_NAMING_CONVENTION.md** - Topic naming
- **../../03-DATA_STORAGE/METADATA_REGISTRY/** - Data catalog
- **../../09-TEMPLATES/TELEMETRY_SCHEMA_TEMPLATE.json** - Schema template
- **../../09-TEMPLATES/SCHEMA_CHANGE_RFC.md** - Schema change process

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial schema registry         | Data Engineering Team |
