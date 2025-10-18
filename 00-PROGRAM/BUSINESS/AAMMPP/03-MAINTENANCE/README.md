# AAMMPP Maintenance Module

**Purpose:** MRO work order management, component exchanges, and service bulletin tracking with full UTCS traceability.

---

## Overview

The AAMMPP Maintenance module manages the complete maintenance lifecycle using FE (Federation Entanglement) coordination:
- **MRO Work Orders:** Scheduled and unscheduled maintenance tasks
- **Component Exchanges:** Removal, replacement, and traceability
- **Service Bulletins:** OEM advisories and compliance tracking

---

## Directory Structure

```
03-MAINTENANCE/
├── MRO_WORK_ORDERS/        # Maintenance work orders
│   ├── SCHEDULED/          # Planned maintenance
│   ├── UNSCHEDULED/        # AOG and corrective actions
│   ├── COMPLETED/          # Completed work orders
│   └── TEMPLATES/          # Work order templates
├── EXCHANGES/              # Component swaps
│   ├── PENDING/            # Exchanges awaiting parts
│   ├── IN_PROGRESS/        # Ongoing exchanges
│   ├── COMPLETED/          # Completed exchanges
│   └── RECORDS/            # Historical exchange records
└── SERVICE_BULLETINS/      # OEM advisories
    ├── ACTIVE/             # Current SBs requiring action
    ├── COMPLIED/           # Completed SBs
    └── APPLICABILITY/      # SB applicability matrix
```

---

## MRO Work Orders

### Work Order Types

#### 1. Scheduled Maintenance
**Trigger:** Inspection interval reached

**Process:**
1. Maintenance planning reviews flight hours/cycles
2. Work order created in `/MRO_WORK_ORDERS/SCHEDULED/`
3. UTCS passport checked for maintenance history
4. Parts reserved if required
5. Work scheduled with MRO provider

**Work Order Structure:**
```yaml
work_order:
  id: WO-2025-10-001234
  type: scheduled_inspection
  priority: routine
  aircraft: A/C-MSN-50123
  
  component:
    utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-001@2.0.0"
    part_number: "787-W-SPAR-57-2145"
    serial_number: "SN-787-SPAR-001234"
    location: LEFT-WING-MAIN-SPAR
    
  maintenance_task:
    description: "6-month structural inspection per AMM 57-10-00"
    interval: 6_months
    last_performed: "2025-04-15"
    next_due: "2025-10-15"
    flight_hours_due: 9200
    flight_cycles_due: 4500
    
  scope:
    - "Visual inspection for cracks, corrosion"
    - "NDT ultrasonic inspection per AMM"
    - "Torque check fasteners per AMM"
    - "Apply service bulletin SB-787-57-0118"
    
  mro_provider: CERTIFIED_AERO_MRO
  technician: "T.Anderson"
  scheduled_date: "2025-10-15"
  estimated_duration_hours: 8
  
  status: scheduled
  created: "2025-09-15T10:00:00Z"
```

#### 2. Unscheduled Maintenance
**Trigger:** Defect reported, AOG situation, or component failure

**Process:**
1. Defect report filed
2. Urgency assessed (AOG, critical, routine)
3. Work order created in `/MRO_WORK_ORDERS/UNSCHEDULED/`
4. Emergency parts procurement if needed
5. Immediate scheduling for AOG

**Work Order Structure:**
```yaml
work_order:
  id: WO-2025-10-002456
  type: corrective_action
  priority: AOG  # Aircraft On Ground
  aircraft: A/C-MSN-50123
  
  defect:
    report_number: DEF-2025-10-789
    description: "Hydraulic leak detected on main landing gear actuator"
    discovered_by: "Pilot"
    severity: critical
    
  component:
    utcs_ref: "UTCS-AAMMPP-MMM-HYDRAULIC-ACTUATOR-LG-042@1.2.0"
    part_number: "A320-LG-ACT-32-8890"
    serial_number: "SN-LG-ACT-987654"
    location: MAIN-LDG-GEAR-LEFT
    
  action_required: exchange
  replacement_part:
    status: available
    location: FRA_WAREHOUSE_A3
    serial_number: "SN-LG-ACT-987655"
    
  mro_provider: CERTIFIED_AERO_MRO
  technician: "R.Martinez"
  scheduled_date: "2025-10-18T18:00:00Z"
  estimated_duration_hours: 4
  
  status: in_progress
  created: "2025-10-18T14:30:00Z"
```

### Work Order Lifecycle

```
Created → Scheduled → In Progress → Inspection → Completed → Closed
              ↓
         [Hold for Parts]
              ↓
         [Parts Received] → Resume
```

---

## Component Exchanges

### Exchange Process (FE Coordination)

#### 1. Exchange Request
**Trigger:** Component fails, reaches life limit, or requires overhaul

**Process:**
1. Create exchange request in `/EXCHANGES/PENDING/`
2. Verify replacement component availability
3. Check interchangeability and compatibility
4. Reserve replacement from inventory or order via procurement

**Exchange Request:**
```yaml
exchange:
  id: EXC-2025-10-1234
  work_order: WO-2025-10-002456
  aircraft: A/C-MSN-50123
  
  removal:
    component:
      utcs_ref: "UTCS-AAMMPP-MMM-HYDRAULIC-ACTUATOR-LG-042@1.2.0"
      part_number: "A320-LG-ACT-32-8890"
      serial_number: "SN-LG-ACT-987654"
      location: MAIN-LDG-GEAR-LEFT
    reason: hydraulic_leak
    flight_hours: 4820
    flight_cycles: 3210
    condition: unserviceable
    
  installation:
    component:
      utcs_ref: "UTCS-AAMMPP-MMM-HYDRAULIC-ACTUATOR-LG-043@1.0.0"
      part_number: "A320-LG-ACT-32-8890"
      serial_number: "SN-LG-ACT-987655"
      source: warehouse
      certificates: [FAA_8130-3, EASA_FORM_1]
    
  status: pending_parts
  created: "2025-10-18T14:30:00Z"
```

#### 2. Exchange Execution
**Process:**
1. Move to `/EXCHANGES/IN_PROGRESS/`
2. Remove failed component
3. Update UTCS passport: mark removed, update custody
4. Install replacement component
5. Update UTCS passport: mark installed, update aircraft config
6. Functional test per AMM
7. Record exchange completion

**Exchange Completion:**
```yaml
exchange_complete:
  id: EXC-2025-10-1234
  
  removal:
    removed_by: "R.Martinez"
    removal_date: "2025-10-18T20:15:00Z"
    final_hours: 4820
    final_cycles: 3210
    disposition: send_to_repair
    
  installation:
    installed_by: "R.Martinez"
    install_date: "2025-10-18T21:45:00Z"
    initial_hours: 0
    initial_cycles: 0
    
  testing:
    functional_test: pass
    leak_check: pass
    system_test: pass
    test_date: "2025-10-18T22:30:00Z"
    
  utcs_updates:
    removed_component:
      lifecycle_state: FE  # Removed from service
      logistics.current_location: "MRO_REPAIR_SHOP"
      maintenance.condition: unserviceable
      
    installed_component:
      lifecycle_state: FE  # In service
      logistics.current_location: "A/C-MSN-50123-MAIN-LDG-GEAR-LEFT"
      maintenance.install_date: "2025-10-18T21:45:00Z"
      maintenance.total_hours: 0
      maintenance.total_cycles: 0
      
  completed: "2025-10-18T23:00:00Z"
  status: completed
```

#### 3. Traceability Update
**Process:**
1. Update aircraft configuration
2. Create traceability thread in `/07-TRACEABILITY/UTCS_THREADS/`
3. Link removal and installation in UTCS
4. Update fleet-wide records
5. Move to `/EXCHANGES/COMPLETED/`

---

## Service Bulletins (SB)

### SB Management

#### 1. SB Receipt
**Trigger:** OEM issues service bulletin

**Process:**
1. SB received and stored in `/SERVICE_BULLETINS/ACTIVE/`
2. Parse applicability (aircraft type, system, P/N range)
3. PLUMA workflow scans UTCS registry for affected components
4. Generate applicability matrix
5. Notify operators and MRO providers

**Service Bulletin:**
```yaml
service_bulletin:
  number: SB-787-57-0118
  issuer: BOEING
  issue_date: "2025-09-01"
  revision: A
  
  title: "Wing Spar Inspection Enhancement"
  category: mandatory
  compliance: within_12_months
  
  applicability:
    aircraft_types: [787-8, 787-9, 787-10]
    systems: [57-WINGS]
    part_numbers:
      - "787-W-SPAR-57-2145"
      - "787-W-SPAR-57-2146"
    serial_range:
      from: "SN-787-SPAR-001000"
      to: "SN-787-SPAR-005000"
      
  description: "Enhanced ultrasonic inspection for wing spar attach points"
  
  effectivity:
    urgent: false
    compliance_by: "2026-09-01"
    repeat_interval: 12_months
    
  work_required:
    hours: 12
    skill_level: "Level 3 NDT"
    special_tooling: ["Ultrasonic probe kit"]
    
  status: active
```

#### 2. SB Applicability Scan
**Process:**
1. PLUMA workflow queries UTCS registry
2. Filter components by applicability criteria
3. Generate list of affected aircraft/components
4. Create compliance tracking records

**Applicability Report:**
```yaml
sb_applicability:
  sb_number: SB-787-57-0118
  scan_date: "2025-09-02T10:00:00Z"
  
  affected_components:
    - utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-001@2.0.0"
      aircraft: A/C-MSN-50123
      serial_number: "SN-787-SPAR-001234"
      compliance_status: pending
      compliance_due: "2026-09-01"
      
    - utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-002@1.8.0"
      aircraft: A/C-MSN-50124
      serial_number: "SN-787-SPAR-001456"
      compliance_status: pending
      compliance_due: "2026-09-01"
      
  total_affected: 2
  operators_notified: [AIRLINE_A, AIRLINE_B]
```

#### 3. SB Compliance
**Process:**
1. Schedule compliance work
2. Create work order for SB embodiment
3. Execute SB per instructions
4. Update UTCS passport with SB compliance
5. Move SB to `/SERVICE_BULLETINS/COMPLIED/` for component

**Compliance Record:**
```yaml
sb_compliance:
  sb_number: SB-787-57-0118
  component:
    utcs_ref: "UTCS-AAMMPP-AAA-WING-SPAR-787-001@2.0.0"
    serial_number: "SN-787-SPAR-001234"
    
  compliance:
    work_order: WO-2025-10-001234
    performed_by: "T.Anderson"
    completion_date: "2025-10-15"
    result: satisfactory
    findings: "No defects found during enhanced inspection"
    
  next_action:
    repeat_interval: 12_months
    next_due: "2026-10-15"
    
  utcs_updated: true
  status: complied
```

---

## Integration Points

### UTCS Registry
- All maintenance events update UTCS passports
- Component lifecycle tracking
- Link: `/01-ASSETS/UTCS_REGISTRY/`

### Procurement
- Parts reservation and emergency procurement
- Link: `/02-PROCUREMENT/`

### Quantum Optimization
- Predictive maintenance via QSH jobs
- Failure prediction and prevention
- Link: `/08-QUANTUM/QSH_JOBS/failure_pred.yaml`

### A360Exchanges-TT
- Component exchange marketplace
- Repair service bidding
- Link: `/10-BUSINESS/A360-EXCHANGES-TT/`

---

## Automation (PLUMA)

### Automated Workflows
1. **SB Notification:** Scan registry, notify affected operators
2. **Inspection Scheduling:** Auto-schedule based on intervals
3. **Exchange Tracking:** Update custody chain and UTCS
4. **Predictive Maintenance:** Trigger based on QB recommendations
5. **Compliance Reminders:** Alert approaching SB deadlines

See: [PLUMA Hooks](../06-INTEGRATION/PLUMA_HOOKS/)

---

## Compliance

### Standards
- **ATA iSpec 2200:** Aircraft maintenance program specs
- **S1000D:** Technical publications (CSDB)
- **MSG-3:** Maintenance program development
- **FAR Part 43:** Maintenance, preventive maintenance, alterations

### Documentation
- Work orders retained for aircraft lifetime + 2 years
- SB compliance records permanent
- Exchange records linked to UTCS for full traceability

See: [Compliance](../07-TRACEABILITY/COMPLIANCE/)

---

## References

- [AAMMPP Platform](../)
- [UTCS Registry](../01-ASSETS/UTCS_REGISTRY/)
- [QSH Jobs](../08-QUANTUM/QSH_JOBS/)
- [PLUMA Workflows](../06-INTEGRATION/PLUMA_HOOKS/)

---

**Owner:** AAMMPP Maintenance Team  
**Last Updated:** 2025-10-18  
**Next Review:** 2025-11-18
