# Schema Registry Links

## Purpose
Links to enterprise schema registry for versioned data contracts.

## Registry Endpoints

### Production
- **URL**: https://schema-registry.idealeeu.eu
- **API**: https://schema-registry.idealeeu.eu/api/v1
- **Auth**: OAuth 2.0 with service account

### Development
- **URL**: https://schema-registry-dev.idealeeu.eu
- **API**: https://schema-registry-dev.idealeeu.eu/api/v1

## Registered Schemas

### Digital Twin State
- **Subject**: `digitaltwin.state.v1`
- **Version**: 1.0.0
- **Schema ID**: 1001
- **Format**: JSON Schema

### Simulation Input
- **Subject**: `digitaltwin.simulation.input.v1`
- **Version**: 1.0.0
- **Schema ID**: 1002
- **Format**: JSON Schema

### Simulation Output
- **Subject**: `digitaltwin.simulation.output.v1`
- **Version**: 1.0.0
- **Schema ID**: 1003
- **Format**: JSON Schema

### Telemetry Event
- **Subject**: `digitaltwin.telemetry.v1`
- **Version**: 1.0.0
- **Schema ID**: 1004
- **Format**: Avro

## Compatibility Policy
- **Backward Compatible**: New versions must be readable by old consumers
- **Forward Compatible**: Old versions must be readable by new consumers
- **Full Compatible**: Both backward and forward compatible

## Registration Process
1. Define schema in JSON Schema or Avro format
2. Validate schema against compatibility rules
3. Submit to registry via API or UI
4. Receive schema ID for referencing
5. Update documentation with schema ID
