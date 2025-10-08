# FLEET_DATA_INGEST

API specifications for fleet operational data ingestion.

## Purpose

Defines APIs and processes for ingesting operational data from aircraft and spacecraft fleets into the Digital Thread.

## Data Sources

### Aircraft Telemetry
- Flight data (FDR/QAR)
- Engine data (FADEC)
- Health monitoring (HUMS)
- Maintenance events

### Spacecraft Telemetry
- Mission telemetry (ground station)
- Housekeeping data
- Anomaly reports
- Consumables tracking

## Integration Approach

- **Real-Time**: Streaming telemetry (Kafka, MQTT)
- **Near-Real-Time**: Aggregated data (REST API)
- **Batch**: Historical data (S3, SFTP)

## Related Documents

- **07-INTEGRATIONS/00-README.md** - Integration overview
- **05-DIGITAL_TWIN/** - Digital twin data ingestion
- **01-FLEET/OPERATIONAL_DATA_HUB** - Fleet data hub
