# TELEMETRY_SCHEMA_VERSIONING

Semantic versioning and lifecycle management for telemetry schemas.

## Semantic Versioning (SemVer)

Format: `MAJOR.MINOR.PATCH`

### Version Increment Rules

| Change Type | Version Increment | Example |
|-------------|-------------------|---------|
| **Breaking Change** | MAJOR | 1.2.3 → 2.0.0 |
| **Backward-Compatible Addition** | MINOR | 1.2.3 → 1.3.0 |
| **Bug Fix / Documentation** | PATCH | 1.2.3 → 1.2.4 |

### Breaking Changes (MAJOR)

Changes that prevent old code from reading new data:

- **Remove Required Field**
  ```json
  // v1.0.0
  {"name": "pressure", "type": "double"}
  
  // v2.0.0 (BREAKING: removed field)
  // Field removed entirely
  ```

- **Change Field Type**
  ```json
  // v1.0.0
  {"name": "status", "type": "int"}
  
  // v2.0.0 (BREAKING: type change)
  {"name": "status", "type": "string"}
  ```

- **Rename Field**
  ```json
  // v1.0.0
  {"name": "pressure", "type": "double"}
  
  // v2.0.0 (BREAKING: renamed)
  {"name": "pressure_bar", "type": "double"}
  ```

- **Change Field Semantics**
  ```json
  // v1.0.0: pressure in bar
  {"name": "pressure", "type": "double"}
  
  // v2.0.0 (BREAKING: unit change)
  // Same name, but now in PSI (semantic change)
  {"name": "pressure", "type": "double"}
  ```

### Backward-Compatible Changes (MINOR)

Changes that allow old code to continue working:

- **Add Optional Field**
  ```json
  // v1.0.0
  {"name": "pressure", "type": "double"}
  
  // v1.1.0 (BACKWARD COMPATIBLE)
  {"name": "pressure", "type": "double"},
  {"name": "quality", "type": "int", "default": 0}
  ```

- **Add Field with Default Value**
  ```json
  // v1.1.0
  {"name": "sensor_id", "type": "string", "default": "unknown"}
  ```

- **Delete Optional Field** (with BACKWARD compatibility)
  ```json
  // v1.2.0: removed optional field (readers ignore it)
  ```

### Non-Breaking Changes (PATCH)

Changes that don't affect schema structure:

- Update documentation strings
- Fix typos in field descriptions
- Update metadata (owner, EBOM reference)
- No actual schema field changes

## Lifecycle States

### State Diagram

```
DRAFT ──┐
        ├──▶ ACTIVE ──▶ DEPRECATED ──▶ ARCHIVED
        │       │
        │       └──▶ (new version) ──▶ ACTIVE
        │
        └──▶ (abandoned)
```

### State Definitions

#### DRAFT
- **Purpose**: Development and testing
- **Actions**:
  - ✅ Edit schema
  - ✅ Delete schema
  - ✅ Promote to ACTIVE
- **Restrictions**:
  - ❌ Cannot be used in production pipelines
- **Duration**: No time limit

#### ACTIVE
- **Purpose**: Production use
- **Actions**:
  - ✅ Read schema
  - ✅ Use in pipelines
  - ✅ Create new version (increment)
  - ✅ Deprecate schema
- **Restrictions**:
  - ❌ Cannot edit (must create new version)
  - ❌ Cannot delete
- **Duration**: Until deprecated or superseded

#### DEPRECATED
- **Purpose**: Scheduled for removal
- **Actions**:
  - ✅ Read schema (legacy support)
  - ✅ Archive after notice period
- **Restrictions**:
  - ❌ Cannot use in new pipelines
  - ❌ Cannot create new versions
- **Duration**: 90 days minimum (can be extended)
- **Notification**: All consumers notified at deprecation

#### ARCHIVED
- **Purpose**: Historical reference
- **Actions**:
  - ✅ Read schema (audit/compliance)
- **Restrictions**:
  - ❌ Cannot use in pipelines
  - ❌ Cannot modify or delete
- **Duration**: Permanent (unless legal requirement to delete)

## Version Management

### Creating New Version

#### MINOR Version (Backward Compatible)
1. Copy existing schema
2. Add optional fields or delete optional fields
3. Increment MINOR version
4. Submit PR with change rationale
5. Data steward approval
6. Register new version
7. Both versions ACTIVE simultaneously (old version still valid)

#### MAJOR Version (Breaking Change)
1. Document why breaking change is necessary
2. Create Engineering Change Request (ECR)
3. Impact assessment (which consumers affected)
4. CCB approval required
5. Plan migration:
   - Dual-publish period (old + new)
   - Consumer migration schedule
   - Deprecation timeline
6. Register new version with new topic name (e.g., `v2`)
7. Notify all consumers
8. After migration, deprecate old version

### Version Deprecation Process

#### Step 1: Announce Deprecation (Day 0)
- Mark schema as DEPRECATED
- Update status in registry
- Send notifications to all consumers
- Document migration path

#### Step 2: Dual-Support Period (Day 0-90)
- Keep old version ACTIVE
- New version also ACTIVE
- Consumers migrate at their pace
- Monitor usage of old version

#### Step 3: Archive Old Version (Day 90+)
- After 90 days (or when usage drops to zero)
- Archive old version (read-only)
- Stop accepting new data with old schema

#### Step 4: Permanent Archive (Day 365+)
- After 1 year, old version fully archived
- Data retained but schema no longer in active registry

## Version Selection

### At Ingestion
- Message specifies schema version in topic name or header
- Pipeline validates against specified version
- If no version specified, use latest ACTIVE version

### At Consumption
- Consumers specify required schema version
- Registry provides schema for validation
- Forward/backward compatibility handled automatically

## Schema Change Examples

### Example 1: Add Optional Telemetry Field

**Scenario**: Add sensor quality indicator to pressure signal

**Change Type**: MINOR (backward compatible)

**Before (v1.0.0)**:
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"}
  ]
}
```

**After (v1.1.0)**:
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "pressure", "type": "double"},
    {"name": "quality", "type": "int", "default": 0}  // New field
  ]
}
```

**Migration**: None required (old consumers continue working)

### Example 2: Change Field Type (Breaking)

**Scenario**: Change flight phase from int code to string enum

**Change Type**: MAJOR (breaking change)

**Before (v1.3.0)**:
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "flight_phase", "type": "int"}  // 0=ground, 1=taxi, etc.
  ]
}
```

**After (v2.0.0)**:
```json
{
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "flight_phase", "type": "string"}  // "ground", "taxi", etc.
  ]
}
```

**Migration**:
1. Register v2.0.0 with new topic: `fl.acft.phase.v2`
2. Producers dual-publish to v1 and v2
3. Consumers migrate to v2 within 90 days
4. Deprecate v1, archive after 1 year

## Related Documents

- **COMPATIBILITY_POLICY.md** - Compatibility rules
- **00-README.md** - Schema registry overview
- **../../09-TEMPLATES/SCHEMA_CHANGE_RFC.md** - Schema change request process

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial versioning specification | Data Engineering Team |
