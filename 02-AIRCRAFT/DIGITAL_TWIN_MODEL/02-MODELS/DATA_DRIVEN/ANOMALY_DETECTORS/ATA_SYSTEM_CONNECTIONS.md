# ATA System Connections for Anomaly Detectors

**Document Version**: 1.0.0  
**Last Updated**: 2025-10-11  
**Owner**: Data Science Team, Systems Engineering

---

## Overview

This document describes how anomaly detection models integrate with specific ATA (Air Transport Association) system chapters, particularly focusing on:
- **ATA-72**: Engine (turbine/jet)
- **ATA-32**: Landing Gear

These connections ensure traceability between ML models and physical aircraft systems, enabling:
- Predictive maintenance scheduling
- Real-time health monitoring
- Configuration management
- Safety assessment and certification

---

## ATA-72: Engine System Integration

### System Description
**ATA-72** covers the complete engine system, including:
- Fan/compressor assemblies
- Turbine sections
- Bearings and rotating assemblies
- Engine mounting
- Vibration monitoring systems

### Anomaly Detector: Engine Vibration Detector

**Model ID**: `ANOMALY_DETECTOR_ENGINE_VIB_V1.0.0`  
**ATA Chapter**: ATA-72  
**ATA Section**: 72-00 Engine  
**Criticality**: Level A (Catastrophic)

#### Physical System Mapping

| ATA Reference | Component | Sensors | Model Input Features |
|---------------|-----------|---------|---------------------|
| ATA-72-11 | Fan Section | Vibration sensor (fan bearing) | `vib_fan_rms`, `vib_fan_peak` |
| ATA-72-12 | Compressor Section | Vibration sensor (compressor bearing) | `vib_compressor_rms` |
| ATA-72-13 | Turbine Section | Vibration sensor (turbine bearing) | `vib_turbine_rms` |
| ATA-77-11 | Engine Indication | N1, N2 speed sensors | `n1`, `n2`, `n1_rate_of_change` |
| ATA-77-11 | Engine Indication | EGT sensor | `egt` |
| ATA-79-11 | Oil System | Oil pressure/temp sensors | `oil_pressure`, `oil_temperature` |

#### Data Flow

```
Physical Sensors (ATA-72) 
    ↓
Data Acquisition Unit (DAU)
    ↓
Aircraft Data Bus (ARINC 429 / AFDX)
    ↓
Ground Station / Edge Device
    ↓
Data Ingestion (MQTT)
    ↓
Anomaly Detection Model
    ↓
Alert/Action System
    ↓
Maintenance Planning (MRO)
```

#### Fault Detection Capabilities

| Fault Type | ATA System | Detection Method | Typical Indicators |
|------------|------------|------------------|-------------------|
| Bearing Wear | ATA-72-11/12/13 | RMS vibration increase | Elevated `vib_*_rms` > baseline |
| Blade Imbalance | ATA-72-11 | FFT 1P component | High `vib_imbalance_score` |
| Mounting Looseness | ATA-72-14 | Broadband vibration | Multiple sensor correlation |
| Shaft Misalignment | ATA-72 | Frequency analysis | Specific frequency signatures |
| Oil System Degradation | ATA-79 | Combined oil + vib | `oil_pressure` drop + vib increase |

#### Maintenance Actions

When anomalies are detected, the model triggers actions per ATA maintenance procedures:

| Severity | ATA Procedure | Action |
|----------|---------------|--------|
| Minor | ATA-72-00-00-700 | Log for next scheduled maintenance |
| Moderate | ATA-72-00-00-710 | Schedule inspection within 48 hours |
| Severe | ATA-72-00-00-720 | Immediate engine shutdown, ground aircraft |

#### Configuration Control

**EBOM References**:
- Engine vibration sensors: `ATA-72-11-001` (fan), `ATA-72-11-002` (compressor), `ATA-72-11-003` (turbine)
- Speed sensors: `ATA-77-11-001` (N1), `ATA-77-11-002` (N2)
- Temperature sensors: `ATA-77-11-003` (EGT), `ATA-79-11-002` (oil temp)

**Configuration Baseline**: See `02-AIRCRAFT/CONFIGURATION_BASE/ATA-72_ENGINE/`

**Change Control**: Any changes to sensor types, locations, or calibration require ECR (Engineering Change Request) and model revalidation.

---

## ATA-32: Landing Gear System Integration

### System Description
**ATA-32** covers the landing gear system, including:
- Main landing gear (left/right)
- Nose landing gear
- Extension/retraction system
- Wheel brakes
- Steering system
- Position sensors

### Anomaly Detector: Landing Gear Health Monitor (Planned)

**Model ID**: `ANOMALY_DETECTOR_LANDING_GEAR_V1.0.0` (Development)  
**ATA Chapter**: ATA-32  
**ATA Section**: 32-00 Landing Gear  
**Criticality**: Level A (Catastrophic)  
**Status**: In Development (Planned for Q2 2026)

#### Planned Physical System Mapping

| ATA Reference | Component | Sensors | Planned Model Inputs |
|---------------|-----------|---------|---------------------|
| ATA-32-11 | Main Gear Structure | Strain gauges | `main_gear_strain_left`, `main_gear_strain_right` |
| ATA-32-12 | Main Gear Extension/Retraction | Position sensors, pressure | `gear_position`, `hydraulic_pressure` |
| ATA-32-13 | Main Gear Doors | Position sensors | `door_position`, `door_cycle_count` |
| ATA-32-30 | Nose Gear | Strain, position sensors | `nose_gear_strain`, `nose_gear_position` |
| ATA-32-42 | Wheel Brakes | Temperature, wear sensors | `brake_temp`, `brake_wear_indicator` |
| ATA-32-50 | Steering | Position, force sensors | `steering_angle`, `steering_force` |

#### Planned Fault Detection Capabilities

| Fault Type | ATA System | Detection Method | Typical Indicators |
|------------|------------|------------------|-------------------|
| Strut Wear | ATA-32-11 | Strain pattern analysis | Abnormal strain distribution |
| Retraction Anomaly | ATA-32-12 | Timing and pressure | Slow retraction, pressure drops |
| Door Misalignment | ATA-32-13 | Position sensor drift | Inconsistent door position |
| Brake Wear | ATA-32-42 | Temperature + cycle count | High brake temp, wear indicator |
| Hydraulic Leak | ATA-32-12 | Pressure drop patterns | Gradual pressure loss |
| Tire Condition | ATA-32-44 | Vibration on landing | Landing vibration signature |

#### Data Sources for Development

- Flight test data: Landing cycles, brake applications
- Ground test data: Hydraulic system tests, door cycling
- Maintenance records: Historical landing gear issues
- Seeded fault data: Controlled degradation tests

**Development Timeline**:
- Q4 2025: Data collection and labeling
- Q1 2026: Model development and training
- Q2 2026: Validation and shadow mode
- Q3 2026: Production deployment (pending validation)

---

## Cross-System Integration

### Multi-System Health Scoring

Future capability: Combine anomaly scores from multiple ATA systems for holistic aircraft health assessment.

**Example**: Engine vibration (ATA-72) + landing gear strain (ATA-32) during takeoff/landing:
- Correlated anomalies may indicate structural issues (ATA-53 fuselage)
- Single-system anomalies indicate localized faults

### ATA System Prioritization

When multiple anomalies detected simultaneously:

1. **Level A Systems** (Catastrophic): ATA-72 (Engine), ATA-32 (Landing Gear)
   - Immediate action, ground aircraft if severe
   
2. **Level B Systems** (Hazardous): ATA-27 (Flight Controls), ATA-28 (Fuel)
   - Schedule maintenance within 24-48 hours
   
3. **Level C Systems** (Major): ATA-21 (Air Conditioning), ATA-24 (Electrical)
   - Schedule maintenance within 7 days
   
4. **Level D Systems** (Minor): ATA-33 (Lights), ATA-36 (Pneumatic)
   - Log for next scheduled maintenance

---

## Configuration Management Integration

### EBOM (Engineering Bill of Materials) Linkage

All anomaly detection models must reference specific EBOM items:

- **Data Contract**: Links signals to EBOM references (e.g., `ebom_ref: ATA-72-11-001`)
- **Model Card**: Documents ATA chapter and system coverage
- **ATA Mapping CSV**: Central registry of model ↔ ATA mappings

**Location**: `02-AIRCRAFT/DIGITAL_TWIN_MODEL/09-INTEGRATIONS/ATA_MAPPING.csv`

### Configuration Change Process

When ATA systems change (sensor type, location, calibration):

1. **ECR Initiated**: Engineering Change Request documents the change
2. **Impact Assessment**: Evaluate impact on anomaly detection models
3. **Model Revalidation**: If sensor changes, retrain/revalidate model
4. **Data Contract Update**: Update signal definitions in data contract
5. **EBOM Update**: Update EBOM references
6. **Certification Update**: Update certification evidence if required

---

## Certification and Compliance

### DO-178C Software Compliance

Anomaly detection models for Level A systems (ATA-72, ATA-32) must comply with:
- **DO-178C Level A**: Formal methods, MC/DC coverage
- **ARP4754A**: Safety assessment (FMEA, FTA)
- **DO-326A**: Cybersecurity (model signing, secure deployment)

### Traceability Matrix

Each model maintains traceability to:
- **Requirements**: System-level requirements (REQ-*)
- **Hazards**: Hazard analysis (HAZ-*)
- **ATA Systems**: Physical system mapping
- **Certification Memos**: Certification evidence (CERT-*)

**Example for Engine Vibration Detector**:
- Requirement: `REQ-ANOMALY-ENGINE-001` (Engine health monitoring)
- Hazard: `HAZ-ENGINE-001` (Undetected bearing failure)
- ATA System: `ATA-72-00` (Engine)
- Certification: `CERT-ML-ENGINE-VIB-001`

---

## Maintenance and Operations Integration

### MRO System Integration

Anomaly detection alerts integrate with Maintenance, Repair, and Overhaul (MRO) systems:

**Data Flow**:
```
Anomaly Detected
    ↓
Alert Generated (severity, confidence, component)
    ↓
MRO System API Call
    ↓
Work Order Created (ATA chapter, recommended action)
    ↓
Maintenance Scheduled
    ↓
Technician Dispatch
    ↓
Repair/Inspection Completed
    ↓
Feedback Loop (confirm/false alarm) → Model Improvement
```

### Flight Operations Integration

Real-time anomaly monitoring integrates with flight operations:

- **Pre-Flight**: Health check report (all systems green/yellow/red)
- **In-Flight**: Edge device monitoring (future capability, Phase 2)
- **Post-Flight**: Automated health report generation
- **Trend Analysis**: Fleet-wide health trending by ATA system

---

## Future Enhancements

### Planned ATA System Coverage

**Phase 2 (2026)**:
- ATA-27: Flight Controls (control surface anomalies)
- ATA-28: Fuel System (leak detection, pump health)
- ATA-24: Electrical Power (generator health, battery state)

**Phase 3 (2027)**:
- ATA-21: Air Conditioning (compressor health, duct leaks)
- ATA-49: APU (auxiliary power unit health)
- ATA-53: Fuselage (structural health, fatigue)

### Cross-System Correlation

**Multi-System Anomaly Correlation Engine** (Planned):
- Detect anomalies that manifest across multiple ATA systems
- Example: Engine vibration (ATA-72) + wing flutter (ATA-57) → mounting issue
- Requires federated model or ensemble approach

---

## Related Documents

- **ATA Mapping**: `../../09-INTEGRATIONS/ATA_MAPPING.md`
- **Configuration Base**: `../../../CONFIGURATION_BASE/ATA-72_ENGINE/`, `ATA-32_LANDING_GEAR/`
- **Data Contracts**: `../DATA/contracts/`
- **Model Registry**: `../REGISTRY/index.yaml`
- **Certification Evidence**: `../../06-VALIDATION_VERIFICATION/CERT_EVIDENCE_LINKS.md`

---

## Contacts

- **ATA-72 Engine Systems**: John Peterson (john.peterson@ideale.eu)
- **ATA-32 Landing Gear**: Maria Garcia (maria.garcia@ideale.eu)
- **Data Science Lead**: Dr. Thomas Chen (thomas.chen@ideale.eu)
- **Configuration Management**: CCB (ccb@ideale.eu)
- **Safety Engineering**: Sarah Williams (sarah.williams@ideale.eu)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
