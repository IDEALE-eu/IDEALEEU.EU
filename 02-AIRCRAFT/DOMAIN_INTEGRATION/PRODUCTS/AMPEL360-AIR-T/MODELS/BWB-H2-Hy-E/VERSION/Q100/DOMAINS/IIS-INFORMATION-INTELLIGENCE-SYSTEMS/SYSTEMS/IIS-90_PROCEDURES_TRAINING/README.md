# IIS-90 — PROCEDURES & TRAINING

## System Overview

The Procedures & Training system provides standardized operational procedures, checklists, and computer-based training modules for all aircraft systems and operations.

## Scope

This system encompasses:
- Standard Operating Procedures (SOPs)
- Emergency procedures and checklists
- Computer-Based Training (CBT) modules
- Training curriculum and materials
- Competency assessment tools

## Subsystems

### 90-01 — SOPs & Checklists
Standard operating procedures and operational checklists including:
- Normal operations checklists
- Emergency procedures
- Abnormal situations handling
- System-specific operational procedures
- Quick Reference Handbooks (QRH)
- Minimum Equipment Lists (MEL)

**Key Content Areas:**
- Pre-flight procedures
- Start-up and shutdown sequences
- Normal flight operations
- Emergency response procedures
- Maintenance procedures
- Ground operations

### 90-02 — CBT Training Modules
Computer-Based Training modules and interactive learning materials:
- System familiarization courses
- Operational procedures training
- Emergency response training
- Maintenance training
- Type rating preparation
- Recurrent training modules

**Delivery Formats:**
- Interactive multimedia courses
- Virtual reality training scenarios
- Procedure simulators
- Assessment and testing modules
- Progress tracking systems

## Integration with Other Systems

Procedures and training materials interface with:
- **All ATA Chapters** — Comprehensive coverage of all aircraft systems
- **46** — Information Systems (for content management and delivery)
- **93** — Ground Support Equipment (for maintenance training)
- **94** — Training Systems (for simulator integration)

## Content Management

- Procedures stored in the 46-50 OTA Software Content Management subsystem
- Training modules delivered via 46-20 Data Bus UTCS Broker
- Version control through 46-30 Health Analytics & PDM
- Distribution via ground IT gateways (46-10)

## Regulatory Compliance

All procedures and training materials comply with:
- EASA Part-FCL (Flight Crew Licensing)
- EASA Part-OPS (Air Operations)
- EASA Part-145 (Maintenance Organizations)
- ATA Spec 2300 (Information Standards)
- S1000D (Technical Publications)

## PLM/CAx Structure

Each subsystem contains engineering artifacts in `PLM/CAx/` directories:
- CAD — Diagrams and visual aids
- CAE — Procedure simulations
- CAO — Training optimization
- CAI — Interactive content
- CAM — Media production
- CAV — Content validation
- CAP — Curriculum planning
- CAS — Training simulations
- CMP — Composite training materials

## Related Documentation

- Domain Documentation: `../../README.md`
- System Integration: `../46-INFORMATION-SYSTEMS/INTEGRATION_VIEW.md`
- Training Requirements: `../91-CHARTS_PERFORMANCE/` (performance training)
