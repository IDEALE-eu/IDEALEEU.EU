# PARTITIONING_STRATEGY

Data partitioning scheme for efficient storage and query performance.

## Purpose

Defines how operational telemetry is partitioned to optimize:
- Query performance (reduce data scanned)
- Parallel processing (distribute workload)
- Cost efficiency (partition pruning)
- Data retention (targeted deletion)

## Partitioning Scheme

### Hierarchical Partitioning

```
dt=YYYY-MM-DD / platform={platform_id} / system={system_code}
```

### Partition Keys

#### 1. Date (dt)
**Format**: `dt=YYYY-MM-DD` (ISO 8601 date)

**Rationale**:
- Most common query pattern (time-range queries)
- Aligns with retention policies
- Enables efficient lifecycle management

**Examples**:
```
dt=2024-01-15
dt=2024-12-31
```

#### 2. Platform (platform)
**Format**: `platform={registration_or_serial_number}`

**Rationale**:
- Isolate data by aircraft/spacecraft
- Support per-platform analysis
- Enable fleet-wide comparisons

**Examples**:
```
platform=AC-H2-001  # Aircraft registration
platform=SC-LEO-005  # Spacecraft serial
platform=SIM-RIG-12  # Simulator ID
```

#### 3. System (system)
**Format**: `system={ATA_chapter_or_system_code}`

**Rationale**:
- Group related telemetry signals
- Support system-specific queries
- Reduce cross-system data scanning

**Examples**:
```
system=h2          # Hydrogen propulsion (ATA 28/71)
system=engine      # Engine (ATA 71-80)
system=power       # Electrical power (ECSS)
system=thermal     # Thermal control
```

## Full Path Examples

### Aircraft Telemetry
```
s3://ideale-raw-vault/
├─ dt=2024-01-15/
│  ├─ platform=AC-H2-001/
│  │  ├─ system=h2/
│  │  │  └─ part-00000.parquet
│  │  ├─ system=engine/
│  │  │  └─ part-00000.parquet
│  │  ├─ system=avionics/
│  │  │  └─ part-00000.parquet
│  ├─ platform=AC-H2-002/
│  │  ├─ system=h2/
│  │  │  └─ part-00000.parquet
```

### Spacecraft Telemetry
```
s3://ideale-raw-vault/
├─ dt=2024-01-15/
│  ├─ platform=SC-LEO-005/
│  │  ├─ system=power/
│  │  │  └─ part-00000.parquet
│  │  ├─ system=thermal/
│  │  │  └─ part-00000.parquet
│  │  ├─ system=propulsion/
│  │  │  └─ part-00000.parquet
```

## Query Optimization

### Time-Range Queries (Partition Pruning)
```sql
-- Efficient: Partition pruning on dt
SELECT * FROM raw_vault
WHERE dt BETWEEN '2024-01-01' AND '2024-01-31'
  AND platform = 'AC-H2-001'
  AND system = 'h2';

-- Scans only: 31 days × 1 platform × 1 system = 31 partitions
```

### Platform-Specific Queries
```sql
-- Efficient: Partition pruning on platform
SELECT * FROM raw_vault
WHERE platform = 'AC-H2-001'
  AND dt >= '2024-01-01';

-- Scans only: 1 platform × all systems × date range
```

### System-Specific Queries
```sql
-- Efficient: Partition pruning on system
SELECT * FROM raw_vault
WHERE system = 'h2'
  AND dt >= '2024-01-01';

-- Scans only: all platforms × 1 system × date range
```

## Partitioning Best Practices

### 1. Avoid Over-Partitioning
- **Problem**: Too many small partitions (< 100 MB)
- **Impact**: High metadata overhead, slow query planning
- **Solution**: Combine low-volume systems into `system=other`

### 2. Avoid Under-Partitioning
- **Problem**: Too few large partitions (> 10 GB)
- **Impact**: Slow queries, inefficient parallel processing
- **Solution**: Add sub-partitions if needed (e.g., by hour)

### 3. Partition Size Guidelines
- **Target**: 128 MB - 1 GB per partition
- **Max**: 10 GB per partition
- **Min**: 10 MB per partition (for low-volume signals)

### 4. Date Partitioning Format
- **Use**: `dt=YYYY-MM-DD` (not `year=YYYY/month=MM/day=DD`)
- **Rationale**: Simpler predicate pushdown, standard format

## Dynamic Partitioning (Spark/Hive)

```python
# PySpark dynamic partitioning example
df.write \
  .partitionBy("dt", "platform", "system") \
  .mode("append") \
  .parquet("s3://ideale-raw-vault/")
```

**Behavior**:
- Automatically creates partition directories
- Infers partition values from data
- Writes one file per partition per executor

## Partition Metadata

### Hive Metastore
```sql
-- Register partitions in Hive metastore
MSCK REPAIR TABLE raw_vault;

-- Or add partitions manually
ALTER TABLE raw_vault ADD PARTITION (
  dt='2024-01-15',
  platform='AC-H2-001',
  system='h2'
)
LOCATION 's3://ideale-raw-vault/dt=2024-01-15/platform=AC-H2-001/system=h2/';
```

### AWS Glue Catalog
- Automatic partition discovery (crawler)
- Partition projection for time-series data
- Faster query planning (no MSCK REPAIR needed)

## Special Cases

### High-Volume Systems
For systems with >10 GB/day:
```
dt=YYYY-MM-DD / platform={platform_id} / system={system_code} / hour=HH
```

**Example**:
```
dt=2024-01-15/platform=AC-H2-001/system=h2/hour=14/
```

### Low-Volume Systems
For systems with <10 MB/day:
```
dt=YYYY-MM-DD / platform={platform_id} / system=other
```

All low-volume systems combined into `system=other`.

### Cross-Platform Aggregations
For fleet-wide summaries:
```
dt=YYYY-MM-DD / system={system_code}
```

Skip `platform` partition for aggregated datasets.

## Partition Maintenance

### Adding New Partitions
- Automatic via dynamic partitioning
- Or manually: `ALTER TABLE ... ADD PARTITION`

### Dropping Old Partitions
```sql
-- Drop partitions older than retention period
ALTER TABLE raw_vault DROP PARTITION (dt < '2019-01-01');
```

### Compaction (Small Files)
```python
# Compact small files in a partition
df = spark.read.parquet("s3://ideale-raw-vault/dt=2024-01-15/")
df.repartition(10).write.mode("overwrite").parquet("s3://ideale-raw-vault-temp/dt=2024-01-15/")
# Move back after compaction
```

## Monitoring

**Key Metrics**:
- Partition count (target: <100k total)
- Partition size distribution (target: 128 MB - 1 GB)
- Query scan ratio (scanned/returned, target: <10x)

**Alerts**:
- Partition size >10 GB (over-partitioning warning)
- Partition count >100k (metadata overhead warning)

## Related Documents

- **RETENTION_POLICY.md** - Data retention rules
- **00-README.md** - Storage architecture overview
- **../02-DATA_INGESTION/** - Ingestion pipeline configuration

## Change History

| Version | Date    | Changes                         | Author          |
|---------|---------|----------------------------------|--------------------|
| 1.0     | 2024-Q4 | Initial partitioning strategy   | Data Engineering Team |
