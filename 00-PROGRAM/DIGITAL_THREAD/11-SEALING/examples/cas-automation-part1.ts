/**
 * SEALING CAS Example: Automated Work Order Generation and Documentation Updates
 * 
 * This example demonstrates how CAx change events trigger automated workflows:
 * 1. CAD update for Flight Control Computer housing
 * 2. Automatic impact analysis across repository
 * 3. Work order generation for manufacturing and maintenance
 * 4. Real-time technical publication updates
 * 5. Notification to stakeholders
 * 
 * Scenario: Design change to FCC housing to improve thermal management
 */

import {
  CAXChangeEvent,
  WorkOrder,
  TechnicalPublication,
  MaintenanceWorkflow,
  ChangePropagation,
  CASAutomationEngine,
  RepositoryImpactAnalysis,
  createWorkOrderFromEvent,
  propagateChange
} from '../types/cas';

// ============================================================================
// 1. CAX CHANGE EVENT: FCC Housing Design Update
// ============================================================================

export const fccHousingCADUpdate: CAXChangeEvent = {
  event_id: 'EVT-CAD-20251016-001',
  utcs_ref: 'UTCS-LCC/CAD-FCC-HOUSING@2.1.0',
  timestamp: '2025-10-16T14:30:00Z',
  event_type: 'CAD_UPDATE',
  
  // Change Details
  change: {
    artifact_type: 'CAD',
    artifact_id: 'CAD-FCC-HOUSING-001',
    artifact_path: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LCC-LINKAGES-CONTROL-COMMUNICATIONS/SYSTEMS/27-FLIGHT_CONTROLS/SUBSYSTEMS/27-30_FCC/CAD/FCC-HOUSING-V2.1.0.step',
    previous_version: '2.0.0',
    new_version: '2.1.0',
    change_description: 'Added cooling fins to FCC housing to improve thermal dissipation. Increased surface area by 15% to maintain junction temperature below 85°C under maximum load conditions.',
    change_category: 'DESIGN'
  },
  
  // Impacted Product Chain
  product_chain: {
    product_line: '02-AIRCRAFT',
    product_id: 'AMPEL360-AIR-T',
    domain: 'LCC',
    system: 'Flight Control Computer',
    part_number: 'FCC-HSG-BWB-001'
  },
  
  // Change Classification
  classification: {
    impact_level: 'MAJOR',
    requires_certification: true, // Form, fit, function change
    requires_testing: true, // Thermal and vibration testing
    requires_documentation_update: true,
    affects_production: true, // New manufacturing process
    affects_maintenance: true // Updated maintenance procedures
  },
  
  // Trigger Criteria
  trigger_criteria: {
    dimensional_change: true, // External dimensions changed
    material_change: false, // Same aluminum alloy
    weight_change: true, // +50g due to additional material
    performance_change: true, // Improved thermal performance
    safety_impact: false, // No safety degradation
    interchangeability_affected: true // Not backward compatible
  },
  
  // Change Initiator
  initiator: {
    user: 'john.engineer@ideale-eu.org',
    department: 'Thermal Engineering',
    reason: 'Flight test data showed FCC operating at 92°C, exceeding 85°C design limit. Cooling fins added to meet thermal requirements.',
    authorization_level: 'Engineering Manager Approved'
  }
};

// ============================================================================
// 2. AUTOMATED WORK ORDER GENERATION
// ============================================================================

export const generatedWorkOrders: WorkOrder[] = [
  // Work Order 1: Design Verification
  {
    work_order_id: 'WO-20251016-001',
    utcs_ref: 'UTCS-LCC/WO-FCC-HSG-VERIFY@1.0',
    title: 'Design Verification - FCC Housing v2.1.0',
    description: 'Verify thermal and structural performance of new FCC housing design with cooling fins',
    priority: 'HIGH',
    status: 'APPROVED',
    type: 'TESTING',
    source_event: fccHousingCADUpdate,
    
    tasks: [
      {
        task_id: 'TASK-001',
        task_number: 1,
        description: 'Perform CFD analysis to verify thermal performance',
        procedure_reference: 'ENG-PROC-THERMAL-001',
        status: 'COMPLETED',
        assigned_to: 'thermal-team@ideale-eu.org',
        estimated_hours: 16,
        actual_hours: 14,
        dependencies: [],
        verification_required: true,
        verification_method: 'CFD Report Review'
      },
      {
        task_id: 'TASK-002',
        task_number: 2,
        description: 'Perform FEA to verify structural integrity with modified geometry',
        procedure_reference: 'ENG-PROC-STRUCT-001',
        status: 'COMPLETED',
        assigned_to: 'structures-team@ideale-eu.org',
        estimated_hours: 12,
        actual_hours: 13,
        dependencies: [],
        verification_required: true,
        verification_method: 'FEA Report Review'
      },
      {
        task_id: 'TASK-003',
        task_number: 3,
        description: 'Vibration analysis for new fin geometry',
        procedure_reference: 'ENG-PROC-VIB-001',
        status: 'IN_PROGRESS',
        assigned_to: 'dynamics-team@ideale-eu.org',
        estimated_hours: 8,
        dependencies: ['TASK-002'],
        verification_required: true,
        verification_method: 'Modal Analysis Report'
      }
    ],
    
    resources: {
      required_personnel: [
        { role: 'Thermal Engineer', quantity: 1, skill_level: 'Senior' },
        { role: 'Structural Engineer', quantity: 1, skill_level: 'Senior' },
        { role: 'Test Engineer', quantity: 1, skill_level: 'Mid-level' }
      ],
      required_tools: [
        'ANSYS Fluent (CFD)',
        'ANSYS Mechanical (FEA)',
        'Thermal Chamber',
        'Vibration Test Rig'
      ],
      required_materials: [
        { part_number: 'FCC-HSG-PROTO-001', quantity: 3, unit: 'EA' }
      ],
      estimated_hours: 36,
      estimated_cost: 12500
    },
    
    schedule: {
      created_date: '2025-10-16T14:35:00Z',
      due_date: '2025-10-30T17:00:00Z',
      start_date: '2025-10-17T08:00:00Z',
      estimated_duration_hours: 36
    },
    
    assignment: {
      assigned_to: 'engineering-team@ideale-eu.org',
      assigned_team: 'LCC Engineering',
      assigned_facility: 'Munich Engineering Center'
    },
    
    approval: {
      required_approvers: [
        'Engineering Manager',
        'Chief Engineer',
        'Certification Authority'
      ],
      approvals_received: [
        {
          approver: 'Engineering Manager',
          approval_date: '2025-10-16T15:00:00Z',
          status: 'APPROVED',
          comments: 'Design change justified by flight test data'
        },
        {
          approver: 'Chief Engineer',
          approval_date: '2025-10-16T16:30:00Z',
          status: 'APPROVED',
          comments: 'Approved pending successful verification tests'
        }
      ]
    },
    
    impact: {
      affected_artifacts: [
        {
          artifact_type: 'CAE',
          artifact_id: 'CAE-FCC-THERMAL-001',
          artifact_path: '02-AIRCRAFT/.../CAE/THERMAL_ANALYSIS/',
          impact_description: 'Thermal model must be updated with new fin geometry',
          requires_update: true
        },
        {
          artifact_type: 'CAM',
          artifact_id: 'CAM-FCC-HSG-001',
          artifact_path: '02-AIRCRAFT/.../CAM/MACHINING/',
          impact_description: 'CNC program must be updated for new fin features',
          requires_update: true
        }
      ],
      affected_documents: [
        {
          document_type: 'TECHNICAL_PUBLICATION',
          document_id: 'AMM-27-30-01',
          chapter: 'ATA 27-30',
          requires_update: true
        },
        {
          document_type: 'IPC',
          document_id: 'IPC-27-30-01',
          chapter: 'ATA 27-30',
          requires_update: true
        }
      ],
      affected_parts: [
        {
          part_number: 'FCC-HSG-BWB-001',
          part_name: 'Flight Control Computer Housing',
          change_type: 'DESIGN',
          interchangeable: false
        }
      ],
      affected_assemblies: [
        'FCC-ASSY-001',
        'AVIONICS-RACK-001'
      ],
      affected_test_procedures: [
        'TEST-THERMAL-FCC-001',
        'TEST-VIB-FCC-001'
      ]
    }
  },
  
  // Work Order 2: Manufacturing Update
  {
    work_order_id: 'WO-20251016-002',
    utcs_ref: 'UTCS-LCC/WO-FCC-HSG-MFG@1.0',
    title: 'Manufacturing Process Update - FCC Housing v2.1.0',
    description: 'Update CNC programs and manufacturing procedures for new FCC housing design',
    priority: 'HIGH',
    status: 'PENDING',
    type: 'MANUFACTURING_CHANGE',
    source_event: fccHousingCADUpdate,
    
    tasks: [
      {
        task_id: 'TASK-MFG-001',
        task_number: 1,
        description: 'Generate new CNC programs for cooling fin features',
        procedure_reference: 'MFG-PROC-CNC-001',
        status: 'PENDING',
        estimated_hours: 24,
        dependencies: [],
        verification_required: true,
        verification_method: 'First Article Inspection'
      },
      {
        task_id: 'TASK-MFG-002',
        task_number: 2,
        description: 'Update manufacturing work instructions',
        procedure_reference: 'MFG-PROC-DOC-001',
        status: 'PENDING',
        estimated_hours: 8,
        dependencies: ['TASK-MFG-001'],
        verification_required: true
      },
      {
        task_id: 'TASK-MFG-003',
        task_number: 3,
        description: 'Produce first article for inspection',
        procedure_reference: 'MFG-PROC-FAI-001',
        status: 'PENDING',
        estimated_hours: 16,
        dependencies: ['TASK-MFG-001', 'TASK-MFG-002'],
        verification_required: true,
        verification_method: 'AS9102 First Article Inspection'
      }
    ],
    
    resources: {
      required_personnel: [
        { role: 'Manufacturing Engineer', quantity: 1, skill_level: 'Senior' },
        { role: 'CNC Programmer', quantity: 1, skill_level: 'Senior' },
        { role: 'Quality Inspector', quantity: 1, skill_level: 'Senior' }
      ],
      required_tools: [
        'CAM Software (Mastercam)',
        '5-Axis CNC Mill',
        'CMM for First Article Inspection'
      ],
      required_materials: [
        { part_number: 'AL-7075-T6-PLATE', quantity: 5, unit: 'KG' }
      ],
      estimated_hours: 48,
      estimated_cost: 8500
    },
    
    schedule: {
      created_date: '2025-10-16T14:35:00Z',
      due_date: '2025-11-15T17:00:00Z',
      estimated_duration_hours: 48
    },
    
    assignment: {
      assigned_to: 'manufacturing-team@ideale-eu.org',
      assigned_team: 'Manufacturing Engineering',
      assigned_facility: 'Hamburg Production Facility'
    },
    
    approval: {
      required_approvers: [
        'Manufacturing Manager',
        'Quality Manager'
      ],
      approvals_received: []
    },
    
    impact: {
      affected_artifacts: [
        {
          artifact_type: 'CAM',
          artifact_id: 'CAM-FCC-HSG-001',
          artifact_path: '02-AIRCRAFT/.../CAM/MACHINING/FCC-Housing-CNC.nc',
          impact_description: 'CNC program must be regenerated',
          requires_update: true
        }
      ],
      affected_documents: [
        {
          document_type: 'MAINTENANCE_MANUAL',
          document_id: 'MFG-WI-27-30-01',
          chapter: 'Work Instructions',
          requires_update: true
        }
      ],
      affected_parts: [],
      affected_assemblies: [],
      affected_test_procedures: []
    }
  },
  
  // Work Order 3: Documentation Update
  {
    work_order_id: 'WO-20251016-003',
    utcs_ref: 'UTCS-LCC/WO-FCC-HSG-DOC@1.0',
    title: 'Technical Publication Update - FCC Housing v2.1.0',
    description: 'Update AMM, IPC, and maintenance procedures for new FCC housing design',
    priority: 'MEDIUM',
    status: 'PENDING',
    type: 'DOCUMENTATION_UPDATE',
    source_event: fccHousingCADUpdate,
    
    tasks: [
      {
        task_id: 'TASK-DOC-001',
        task_number: 1,
        description: 'Update Aircraft Maintenance Manual (AMM) Chapter 27-30',
        procedure_reference: 'DOC-PROC-AMM-001',
        status: 'PENDING',
        estimated_hours: 12,
        dependencies: [],
        verification_required: true,
        verification_method: 'Technical Review'
      },
      {
        task_id: 'TASK-DOC-002',
        task_number: 2,
        description: 'Update Illustrated Parts Catalog (IPC) with new part number',
        procedure_reference: 'DOC-PROC-IPC-001',
        status: 'PENDING',
        estimated_hours: 6,
        dependencies: [],
        verification_required: true,
        verification_method: 'Technical Review'
      },
      {
        task_id: 'TASK-DOC-003',
        task_number: 3,
        description: 'Create Service Bulletin for retrofit instructions',
        procedure_reference: 'DOC-PROC-SB-001',
        status: 'PENDING',
        estimated_hours: 16,
        dependencies: ['TASK-DOC-001', 'TASK-DOC-002'],
        verification_required: true,
        verification_method: 'Regulatory Review'
      }
    ],
    
    resources: {
      required_personnel: [
        { role: 'Technical Writer', quantity: 1, skill_level: 'Senior' },
        { role: 'Illustrator', quantity: 1, skill_level: 'Mid-level' },
        { role: 'Subject Matter Expert', quantity: 1, skill_level: 'Senior' }
      ],
      required_tools: [
        'Arbortext (S1000D)',
        'Adobe Illustrator',
        'PDM System'
      ],
      required_materials: [],
      estimated_hours: 34,
      estimated_cost: 5500
    },
    
    schedule: {
      created_date: '2025-10-16T14:35:00Z',
      due_date: '2025-11-30T17:00:00Z',
      estimated_duration_hours: 34
    },
    
    assignment: {
      assigned_to: 'techpubs-team@ideale-eu.org',
      assigned_team: 'Technical Publications',
      assigned_facility: 'Munich Engineering Center'
    },
    
    approval: {
      required_approvers: [
        'Technical Publications Manager',
        'Engineering Manager',
        'Regulatory Affairs'
      ],
      approvals_received: []
    },
    
    impact: {
      affected_artifacts: [],
      affected_documents: [
        {
          document_type: 'AMM',
          document_id: 'AMM-27-30-01',
          chapter: 'ATA 27-30-00',
          requires_update: true
        },
        {
          document_type: 'IPC',
          document_id: 'IPC-27-30-01',
          chapter: 'ATA 27-30-00',
          requires_update: true
        }
      ],
      affected_parts: [],
      affected_assemblies: [],
      affected_test_procedures: []
    }
  }
];

// ============================================================================
// 3. TECHNICAL PUBLICATION REAL-TIME UPDATE
// ============================================================================

export const ammChapter2730: TechnicalPublication = {
  publication_id: 'AMM-27-30-01',
  utcs_ref: 'UTCS-DOC/AMM-27-30@3.1',
  title: 'Aircraft Maintenance Manual - Flight Control Computer',
  document_type: 'AMM',
  ata_chapter: '27-30',
  revision: '3.1',
  effective_date: '2025-12-01T00:00:00Z',
  
  sections: [
    {
      section_id: 'AMM-27-30-10',
      section_number: '27-30-10',
      title: 'Flight Control Computer - Description and Operation',
      content: `
# Flight Control Computer Housing - Thermal Management (Rev 3.1)

## Description
The Flight Control Computer (FCC) housing has been redesigned in version 2.1.0 to improve thermal dissipation. The new design incorporates cooling fins that increase the external surface area by 15%.

**CAUTION**: FCC Housing P/N FCC-HSG-BWB-001 Rev 2.1.0 is NOT interchangeable with previous revisions. Do not install Rev 2.0.0 or earlier housings in aircraft requiring Rev 2.1.0.

## Thermal Performance
- Maximum junction temperature: 85°C (improved from 92°C in Rev 2.0.0)
- Operating temperature range: -55°C to +85°C
- Passive cooling via aluminum fins
- No active cooling required

## Identification
- Part Number: FCC-HSG-BWB-001
- Revision: 2.1.0 (NEW)
- Effectivity: Aircraft S/N 001 and subsequent (effective December 1, 2025)

## Maintenance Notes
- Cooling fins must be inspected for damage during routine maintenance
- Clean fins with approved solvent to maintain thermal performance
- See Section 27-30-40 for maintenance procedures
      `,
      figures: [
        {
          figure_number: 'FIG-27-30-001',
          title: 'FCC Housing with Cooling Fins',
          cad_reference: 'CAD-FCC-HOUSING-001 v2.1.0',
          image_uri: 's3://ideale-techpubs/figures/fcc-housing-v2.1.0.png'
        }
      ],
      tables: [],
      referenced_parts: ['FCC-HSG-BWB-001'],
      last_updated: '2025-10-16T14:45:00Z'
    }
  ],
  
  changes: [
    {
      change_id: 'TC-27-30-001',
      change_number: 'TC-001',
      source_event: fccHousingCADUpdate,
      affected_sections: ['AMM-27-30-10', 'AMM-27-30-40'],
      change_description: 'Updated FCC housing description to reflect new cooling fin design (Rev 2.1.0)',
      change_type: 'REVISION',
      status: 'PUBLISHED',
      author: 'techwriter@ideale-eu.org',
      reviewer: 'engineer@ideale-eu.org',
      approved_by: 'manager@ideale-eu.org',
      published_date: '2025-10-16T16:00:00Z'
    }
  ],
  
  pending_changes: [],
  
  applicability: {
    aircraft_models: ['AMPEL360-AIR-T'],
    effectivity_date: '2025-12-01T00:00:00Z'
  },
  
  distribution: {
    operators: ['Lufthansa', 'Air France', 'British Airways'],
    maintenance_organizations: ['Lufthansa Technik', 'Air France Industries'],
    regulatory_authorities: ['EASA', 'FAA']
  }
};

// To be continued in part 2...
