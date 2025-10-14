# PLUMA Quick Start Guide

## What is PLUMA?

**PLUMA** (Product Lifecycle UiX Management Automation) is an industrial-scale automation engine for aerospace lifecycle management. It transforms manual, artisanal processes into replicable, parallelizable, and federated operations.

**Key Benefits**:
- 65% artifact reuse across programs (target: 70%)
- <5 minute UI regeneration from schema changes
- 50+ concurrent programs by 2027
- <2 second federation sync latency

## Prerequisites

- Access to PLUMA platform
- Valid authentication credentials
- Program ID assigned
- TFA structure initialized

## 5-Minute Quickstart

### 1. Initialize Program

```bash
# Clone the repository
git clone https://github.com/IDEALE-eu/IDEALEEU.EU.git
cd IDEALEEU.EU

# Initialize PLUMA for your program
make pluma-init \
  PROGRAM=YOUR-PROGRAM-ID \
  ARCH=YOUR-ARCHITECTURE \
  DOMAINS=AAA,PPP,EDI,LCC
```

### 2. Create First Frozen Context

```bash
# Navigate to your program directory
cd 02-AIRCRAFT/MODEL_IDENTIFICATION/YOUR-PROGRAM/

# Create frozen context for CAD phase
make pluma-freeze \
  PHASE=CAD \
  PROGRAM=YOUR-PROGRAM-ID \
  TAG=baseline-v1
```

### 3. Transition to Next Phase

```bash
# Transition from CAD to CAE
make pluma-phase \
  FROM_PHASE=CAD \
  TO_PHASE=CAE \
  PROGRAM=YOUR-PROGRAM-ID
```

### 4. Clone Context from Another Program

```bash
# Clone successful CAD phase from another program
make pluma-clone \
  FROM_CONTEXT=AMPEL360-BWB-Q100/CAD \
  TO_CONTEXT=YOUR-PROGRAM-ID/CAD \
  OVERRIDES_FILE=config/your-overrides.yaml
```

### 5. View Metrics

```bash
# View program metrics
make pluma-metrics \
  PROGRAM=YOUR-PROGRAM-ID \
  DASHBOARD
```

## Common Use Cases

### Use Case 1: Starting a New Program

**Scenario**: You're starting a new aircraft variant based on an existing design.

**Steps**:
1. **Clone Baseline**:
   ```bash
   pluma clone-context \
     --from AMPEL360-BWB-Q100/CAD \
     --to YOUR-PROGRAM/CAD \
     --param-overrides wing_span=45m,engines=4
   ```

2. **Customize Parameters**:
   - Edit `config/overrides.yaml`
   - Update program-specific values

3. **Validate Structure**:
   ```bash
   pluma validate \
     --program YOUR-PROGRAM \
     --comprehensive
   ```

4. **Create Baseline**:
   ```bash
   pluma freeze-context \
     --phase CAD \
     --program YOUR-PROGRAM \
     --tag initial-baseline
   ```

### Use Case 2: Phase Transition

**Scenario**: Your design is complete and you need to move to engineering analysis.

**Steps**:
1. **Pre-Gate Validation**:
   ```bash
   pluma validate \
     --program YOUR-PROGRAM \
     --phase CAD \
     --check-completeness
   ```

2. **Capacity Check**:
   ```bash
   pluma capacity-plan \
     --program YOUR-PROGRAM \
     --next-phase CAE
   ```

3. **Request Approvals**:
   ```bash
   pluma phase-gate \
     --from CAD \
     --to CAE \
     --program YOUR-PROGRAM \
     --notify-approvers
   ```

4. **Execute Transition** (after approvals):
   ```bash
   pluma phase-transition \
     --from CAD \
     --to CAE \
     --program YOUR-PROGRAM
   ```

### Use Case 3: Collaborative Development

**Scenario**: Multiple organizations working on your program need to share data.

**Steps**:
1. **Configure Federation**:
   ```yaml
   # pluma-federation.yaml
   organization: your-org
   role: prime_contractor
   
   export_policies:
     - domains: [AAA, PPP, EDI]
       partners: [supplier-org-1, supplier-org-2]
       real_time: true
   ```

2. **Deploy Federation**:
   ```bash
   pluma federation deploy \
     --config pluma-federation.yaml
   ```

3. **Monitor Sync**:
   ```bash
   pluma federation status \
     --show-latency \
     --show-partners
   ```

### Use Case 4: Generating Documentation

**Scenario**: You need to create an ICD for a new interface.

**Steps**:
1. **Browse Templates**:
   ```bash
   pluma templates list \
     --category ICD \
     --domain AAA
   ```

2. **Instantiate Template**:
   ```bash
   pluma template instantiate \
     --template ICD-MAP-INTERFACE-V1 \
     --params params.yaml \
     --output ICD-AAA-PPP-v1.md
   ```

3. **Review and Approve**:
   - Edit generated document
   - Submit for review via PLUMA UI
   - Track approval status

## Architecture Overview

```
┌─────────────────────────────────────┐
│         PLUMA Platform              │
├─────────────────────────────────────┤
│ ┌─────────────────────────────────┐ │
│ │ PPUI                            │ │
│ │ (Parametric Documentation)      │ │
│ └─────────────────────────────────┘ │
│ ┌─────────────────────────────────┐ │
│ │ Interphase Control              │ │
│ │ (Phase Transitions)             │ │
│ └─────────────────────────────────┘ │
│ ┌─────────────────────────────────┐ │
│ │ Metabuilders                    │ │
│ │ (UI Generation)                 │ │
│ └─────────────────────────────────┘ │
│ ┌─────────────────────────────────┐ │
│ │ Enterprise Memory               │ │
│ │ (Frozen Contexts)               │ │
│ └─────────────────────────────────┘ │
│ ┌─────────────────────────────────┐ │
│ │ Infranet Protocol               │ │
│ │ (Federation)                    │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│      TFA Backend Ecosystem          │
│  (MAL Services, MAP Services)       │
└─────────────────────────────────────┘
```

## The 9 CAx Phases

| Code | Phase | Purpose |
|------|-------|---------|
| CAD | Design | Conceptual & detailed design |
| CAE | Engineering Analysis | CFD, FEA, thermal analysis |
| CAI | Integration | System integration & testing |
| CAO | Optimization | Trade-space exploration |
| CAM | Manufacturing | Production engineering |
| CAP | Production | Rate ramp-up, supply chain |
| CAV | Verification | Flight & ground tests |
| CMP | Compliance | Certification management |
| CAS | Services | MRO, fleet operations |

## Key Concepts

### Frozen Context
A snapshot of program state at a specific phase. Includes:
- All artifacts and documents
- Validation results
- Approval records
- Configuration metadata
- UTCS blockchain anchor

### Context Reuse Ratio (CRR)
Percentage of artifacts cloned from existing programs:
- Current average: 65%
- Target: >70%
- Best-in-class: 78%

### Parametric Templates
Reusable templates with configurable parameters:
- 50+ templates available
- Cover all CAx phases
- Support multi-program instantiation

### Metabuilders
Auto-generate UIs from backend schemas:
- Zero manual UI coding
- <5 minute regeneration
- 100% type-safe

## Configuration Files

### Program Manifest
```yaml
# program-manifest.yaml
program_id: YOUR-PROGRAM-ID
architecture: BWB-H2-Hy-E
segments: [AIR]
domains: [AAA, PPP, EDI, LCC, EEE, IIS, MMM]
phases: [CAD, CAE, CAI, CAO, CAM, CAP, CAV, CMP, CAS]

metadata:
  passenger_capacity: 250
  range_nm: 6000
  mtow_kg: 180000
  
resources:
  cpu_cores: 200
  memory_gb: 400
  storage_tb: 5
  qubits: 128
```

### Parameter Overrides
```yaml
# overrides.yaml
wing_span_m: 45
passenger_capacity: 350
range_nm: 8000
engines: 4
mtow_kg: 240000

domains:
  AAA:
    wing_config: BWB
    materials: [CFRP, Aluminum]
  PPP:
    engine_type: turbofan
    thrust_kn: 250
```

### Federation Config
```yaml
# federation.yaml
organization: your-org
role: prime_contractor

export_policies:
  - domains: [AAA, PPP, EDI]
    partners: [all_consortium]
    real_time: true
  
  - domains: [DDD]
    partners: [defense_cleared_only]
    encryption: aes256

import_subscriptions:
  - partner: supplier-org
    domains: [CQH]
    sla_ms: 2000
```

## CLI Commands Reference

### Program Management
```bash
pluma init --program ID --arch ARCH --domains DOMAINS
pluma validate --program ID [--phase PHASE]
pluma metrics --program ID [--dashboard]
pluma freeze-context --phase PHASE --program ID --tag TAG
```

### Phase Management
```bash
pluma phase-transition --from PHASE --to PHASE --program ID
pluma phase-gate --from PHASE --to PHASE --program ID
pluma capacity-plan --program ID --next-phase PHASE
```

### Context Management
```bash
pluma clone-context --from SRC --to DST --overrides FILE
pluma query-context --context-id ID
pluma verify-frozen-context --context-id ID
```

### Template Management
```bash
pluma templates list [--category CAT] [--domain DOM]
pluma template instantiate --template ID --params FILE --output FILE
pluma template validate --template ID
```

### Federation Management
```bash
pluma federation deploy --config FILE
pluma federation status [--show-latency] [--show-partners]
pluma federation diagnose --endpoint URI
```

## Web UI Access

**URL**: https://pluma.ideale.eu

**Main Views**:
- **Dashboard**: Program overview and metrics
- **Phase Timeline**: CAx phase progress
- **Frozen Contexts**: Browse and compare contexts
- **Templates**: Template library and instantiation
- **Federation**: Multi-org coordination
- **Capacity Planning**: Resource forecasting

## Getting Help

### Documentation
- [Master Architecture](./01-ARCHITECTURE/MASTER_ARCHITECTURE_V1.1.md)
- [CAx Phases](./03-CAX_PHASES/README.md)
- [Integration Guide](./07-INTEGRATION/README.md)
- [Metrics](./06-METRICS/README.md)

### Support
- **Email**: pluma-support@ideale.eu
- **Slack**: #pluma-support
- **Office Hours**: Tuesdays 14:00-15:00 CET

### Training
- **Onboarding**: 2-hour session for new users
- **Phase Lead Training**: 1-day workshop
- **Admin Training**: 2-day workshop

### Community
- **User Forum**: https://forum.ideale.eu/pluma
- **GitHub**: https://github.com/IDEALE-eu/IDEALEEU.EU
- **Monthly User Group**: First Thursday of each month

## Next Steps

1. **Complete Onboarding**: Schedule with pluma-support@ideale.eu
2. **Join User Group**: Get invitation from your program lead
3. **Start Small**: Clone an existing context for your first program
4. **Provide Feedback**: Help us improve PLUMA

---

**Quick Start Version**: 1.0  
**Last Updated**: October 14, 2025  
**PLUMA Version**: 1.1
