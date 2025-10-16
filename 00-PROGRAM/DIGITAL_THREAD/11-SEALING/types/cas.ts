/**
 * SEALING - CAS (CAx Services) Type Definitions
 * 
 * Comprehensive data structures for CAx-driven work order generation,
 * maintenance automation, and real-time technical publication updates.
 */

// ============================================================================
// Core CAx Change Event
// ============================================================================

export interface CAXChangeEvent {
  event_id: string;
  utcs_ref: string; // e.g., "UTCS-LCC/CAD-FCC-HOUSING@2.1.0"
  timestamp: string;
  event_type: 'CAD_UPDATE' | 'CAE_UPDATE' | 'CAM_UPDATE' | 'CAO_UPDATE' | 'CAI_UPDATE' | 'CAP_UPDATE' | 'CAV_UPDATE' | 'CMP_UPDATE' | 'CAS_UPDATE';
  
  // Change Details
  change: {
    artifact_type: 'CAD' | 'CAE' | 'CAM' | 'CAO' | 'CAI' | 'CAP' | 'CAV' | 'CMP' | 'CAS';
    artifact_id: string;
    artifact_path: string;
    previous_version: string;
    new_version: string;
    change_description: string;
    change_category: 'DESIGN' | 'MATERIAL' | 'PROCESS' | 'SPECIFICATION' | 'DOCUMENTATION' | 'CONFIGURATION';
  };
  
  // Impacted Product Chain
  product_chain: {
    product_line: string; // e.g., '02-AIRCRAFT'
    product_id: string; // e.g., 'AMPEL360-AIR-T'
    domain: string; // e.g., 'LCC'
    system: string; // e.g., 'Flight Control Computer'
    part_number: string;
  };
  
  // Change Classification
  classification: {
    impact_level: 'CRITICAL' | 'MAJOR' | 'MINOR' | 'COSMETIC';
    requires_certification: boolean;
    requires_testing: boolean;
    requires_documentation_update: boolean;
    affects_production: boolean;
    affects_maintenance: boolean;
  };
  
  // Trigger Criteria
  trigger_criteria: {
    dimensional_change: boolean;
    material_change: boolean;
    weight_change: boolean;
    performance_change: boolean;
    safety_impact: boolean;
    interchangeability_affected: boolean;
  };
  
  // Change Initiator
  initiator: {
    user: string;
    department: string;
    reason: string;
    authorization_level: string;
  };
}

// ============================================================================
// Work Order
// ============================================================================

export interface WorkOrder {
  work_order_id: string;
  utcs_ref: string;
  
  // Basic Information
  title: string;
  description: string;
  priority: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  status: 'PENDING' | 'APPROVED' | 'IN_PROGRESS' | 'COMPLETED' | 'CANCELLED';
  
  // Work Order Type
  type: 'DESIGN_UPDATE' | 'MANUFACTURING_CHANGE' | 'MAINTENANCE_ACTION' | 'INSPECTION' | 'REPAIR' | 'MODIFICATION' | 'DOCUMENTATION_UPDATE' | 'TESTING';
  
  // Source Event
  source_event: CAXChangeEvent;
  
  // Tasks
  tasks: WorkOrderTask[];
  
  // Resources
  resources: {
    required_personnel: Array<{
      role: string;
      quantity: number;
      skill_level: string;
    }>;
    required_tools: string[];
    required_materials: Array<{
      part_number: string;
      quantity: number;
      unit: string;
    }>;
    estimated_hours: number;
    estimated_cost: number;
  };
  
  // Schedule
  schedule: {
    created_date: string;
    due_date: string;
    start_date?: string;
    completion_date?: string;
    estimated_duration_hours: number;
  };
  
  // Assignment
  assignment: {
    assigned_to: string;
    assigned_team: string;
    assigned_facility: string;
  };
  
  // Approval Workflow
  approval: {
    required_approvers: string[];
    approvals_received: Array<{
      approver: string;
      approval_date: string;
      status: 'APPROVED' | 'REJECTED' | 'PENDING';
      comments?: string;
    }>;
  };
  
  // Impact Assessment
  impact: WorkOrderImpact;
}

export interface WorkOrderTask {
  task_id: string;
  task_number: number;
  description: string;
  procedure_reference?: string;
  status: 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'BLOCKED';
  assigned_to?: string;
  estimated_hours: number;
  actual_hours?: number;
  dependencies: string[]; // Other task IDs
  verification_required: boolean;
  verification_method?: string;
}

export interface WorkOrderImpact {
  affected_artifacts: Array<{
    artifact_type: string;
    artifact_id: string;
    artifact_path: string;
    impact_description: string;
    requires_update: boolean;
  }>;
  affected_documents: Array<{
    document_type: 'TECHNICAL_PUBLICATION' | 'MAINTENANCE_MANUAL' | 'IPC' | 'AMM' | 'SRM' | 'WIRING_DIAGRAM' | 'TRAINING_MATERIAL';
    document_id: string;
    chapter: string;
    requires_update: boolean;
  }>;
  affected_parts: Array<{
    part_number: string;
    part_name: string;
    change_type: 'DESIGN' | 'MATERIAL' | 'PROCESS' | 'OBSOLESCENCE';
    interchangeable: boolean;
  }>;
  affected_assemblies: string[];
  affected_test_procedures: string[];
}

// ============================================================================
// Technical Publication
// ============================================================================

export interface TechnicalPublication {
  publication_id: string;
  utcs_ref: string;
  
  // Publication Details
  title: string;
  document_type: 'AMM' | 'IPC' | 'SRM' | 'WIRING_DIAGRAM' | 'TSM' | 'CMM' | 'FIM' | 'EMM';
  ata_chapter: string; // e.g., '32-10' for Landing Gear
  revision: string;
  effective_date: string;
  
  // Content Structure
  sections: TechPubSection[];
  
  // Change Management
  changes: TechPubChange[];
  pending_changes: TechPubChange[];
  
  // Metadata
  applicability: {
    aircraft_models: string[];
    serial_numbers?: string[];
    effectivity_date: string;
  };
  
  // Distribution
  distribution: {
    operators: string[];
    maintenance_organizations: string[];
    regulatory_authorities: string[];
  };
}

export interface TechPubSection {
  section_id: string;
  section_number: string;
  title: string;
  content: string; // Markdown or structured content
  figures: Array<{
    figure_number: string;
    title: string;
    cad_reference?: string;
    image_uri: string;
  }>;
  tables: Array<{
    table_number: string;
    title: string;
    data: any;
  }>;
  referenced_parts: string[];
  last_updated: string;
}

export interface TechPubChange {
  change_id: string;
  change_number: string;
  source_event: CAXChangeEvent;
  affected_sections: string[];
  change_description: string;
  change_type: 'ADDITION' | 'DELETION' | 'REVISION' | 'CORRECTION';
  status: 'DRAFT' | 'REVIEW' | 'APPROVED' | 'PUBLISHED';
  author: string;
  reviewer?: string;
  approved_by?: string;
  published_date?: string;
}

// ============================================================================
// Maintenance Workflow
// ============================================================================

export interface MaintenanceWorkflow {
  workflow_id: string;
  utcs_ref: string;
  
  // Workflow Details
  name: string;
  description: string;
  workflow_type: 'PREVENTIVE' | 'CORRECTIVE' | 'PREDICTIVE' | 'MODIFICATION' | 'INSPECTION';
  
  // Trigger
  trigger: {
    trigger_type: 'SCHEDULED' | 'CONDITION_BASED' | 'EVENT_DRIVEN' | 'MANUAL';
    trigger_source?: CAXChangeEvent;
    trigger_condition?: string;
  };
  
  // Workflow Steps
  steps: WorkflowStep[];
  
  // Automation Rules
  automation: {
    auto_generate_work_orders: boolean;
    auto_update_documentation: boolean;
    auto_notify_stakeholders: boolean;
    auto_schedule_tasks: boolean;
  };
  
  // Status
  status: 'ACTIVE' | 'INACTIVE' | 'SUSPENDED';
  execution_count: number;
  last_execution: string;
}

export interface WorkflowStep {
  step_id: string;
  step_number: number;
  step_type: 'GENERATE_WORK_ORDER' | 'UPDATE_DOCUMENTATION' | 'NOTIFY' | 'INSPECT' | 'TEST' | 'APPROVE' | 'RECORD';
  description: string;
  automated: boolean;
  
  // Execution Details
  handler?: string; // Function or service that executes this step
  inputs: Record<string, any>;
  outputs: Record<string, any>;
  
  // Conditions
  preconditions: string[];
  postconditions: string[];
  
  // Error Handling
  on_error: 'RETRY' | 'SKIP' | 'ABORT' | 'NOTIFY';
  max_retries?: number;
}

// ============================================================================
// Change Propagation
// ============================================================================

export interface ChangePropagation {
  propagation_id: string;
  source_event: CAXChangeEvent;
  timestamp: string;
  
  // Propagation Analysis
  impact_analysis: {
    direct_impacts: ImpactItem[];
    indirect_impacts: ImpactItem[];
    risk_assessment: RiskAssessment;
  };
  
  // Generated Actions
  generated_work_orders: string[]; // Work order IDs
  updated_documents: string[]; // Document IDs
  notifications_sent: NotificationRecord[];
  
  // Propagation Status
  status: 'ANALYZING' | 'IN_PROGRESS' | 'COMPLETED' | 'FAILED';
  completion_date?: string;
  errors: string[];
}

export interface ImpactItem {
  item_type: 'PART' | 'ASSEMBLY' | 'DOCUMENT' | 'PROCESS' | 'TOOL' | 'TEST';
  item_id: string;
  item_name: string;
  impact_severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  impact_description: string;
  required_action: string;
  estimated_effort_hours: number;
}

export interface RiskAssessment {
  overall_risk_level: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  safety_risk: boolean;
  certification_risk: boolean;
  production_risk: boolean;
  schedule_risk: boolean;
  cost_risk: boolean;
  risk_description: string;
  mitigation_required: boolean;
  mitigation_plan?: string;
}

export interface NotificationRecord {
  notification_id: string;
  timestamp: string;
  recipient: string;
  notification_type: 'EMAIL' | 'SLACK' | 'SMS' | 'SYSTEM';
  subject: string;
  message: string;
  status: 'SENT' | 'DELIVERED' | 'FAILED';
}

// ============================================================================
// CAS Automation Engine
// ============================================================================

export interface CASAutomationEngine {
  engine_id: string;
  name: string;
  version: string;
  
  // Configuration
  configuration: {
    enabled: boolean;
    auto_propagation: boolean;
    auto_work_order_generation: boolean;
    auto_documentation_update: boolean;
    notification_enabled: boolean;
  };
  
  // Rules Engine
  rules: AutomationRule[];
  
  // Event Processing
  event_queue: CAXChangeEvent[];
  processing_status: {
    events_processed: number;
    work_orders_generated: number;
    documents_updated: number;
    notifications_sent: number;
    errors: number;
  };
  
  // Monitoring
  monitoring: {
    last_health_check: string;
    status: 'HEALTHY' | 'DEGRADED' | 'UNHEALTHY';
    metrics: {
      avg_processing_time_ms: number;
      success_rate_percent: number;
      queue_depth: number;
    };
  };
}

export interface AutomationRule {
  rule_id: string;
  name: string;
  description: string;
  enabled: boolean;
  priority: number;
  
  // Trigger Conditions
  conditions: {
    event_types: string[];
    impact_levels: string[];
    product_lines: string[];
    domains: string[];
    trigger_criteria: Record<string, boolean>;
  };
  
  // Actions
  actions: Array<{
    action_type: 'GENERATE_WORK_ORDER' | 'UPDATE_DOCUMENT' | 'SEND_NOTIFICATION' | 'CREATE_TASK' | 'RUN_ANALYSIS';
    parameters: Record<string, any>;
  }>;
  
  // Execution
  execution_count: number;
  last_execution: string;
  success_rate: number;
}

// ============================================================================
// Repository Impact Analysis
// ============================================================================

export interface RepositoryImpactAnalysis {
  analysis_id: string;
  source_event: CAXChangeEvent;
  timestamp: string;
  
  // Impacted Repository Artifacts
  impacted_files: Array<{
    file_path: string;
    file_type: 'CAD' | 'CAE' | 'DOCUMENT' | 'CODE' | 'CONFIG' | 'DATA';
    change_type: 'MODIFIED' | 'ADDED' | 'DELETED' | 'RENAMED';
    change_summary: string;
    requires_commit: boolean;
  }>;
  
  // Impacted PRDs
  impacted_prds: Array<{
    prd_path: string;
    section_affected: string;
    update_required: boolean;
    update_description: string;
  }>;
  
  // Impacted SEALING Components
  impacted_sealing: Array<{
    component_type: 'SOFTWARE' | 'EMBEDDED' | 'AI_MODEL' | 'NETWORK_NODE';
    component_id: string;
    impact_description: string;
    requires_update: boolean;
  }>;
  
  // Repository Structure Changes
  structure_changes: Array<{
    change_type: 'NEW_DIRECTORY' | 'NEW_FILE' | 'MOVED' | 'DELETED';
    path: string;
    reason: string;
  }>;
  
  // Automated Actions Taken
  automated_actions: Array<{
    action_type: string;
    timestamp: string;
    status: 'SUCCESS' | 'FAILED';
    details: string;
  }>;
  
  // Summary
  summary: {
    total_files_impacted: number;
    total_prds_impacted: number;
    total_sealing_components_impacted: number;
    estimated_update_effort_hours: number;
    priority: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  };
}

// ============================================================================
// Helper Functions
// ============================================================================

export function createWorkOrderFromEvent(event: CAXChangeEvent): WorkOrder {
  const workOrderId = `WO-${Date.now()}`;
  
  return {
    work_order_id: workOrderId,
    utcs_ref: `${event.utcs_ref}-WO`,
    title: `Update for ${event.change.artifact_id}`,
    description: event.change.change_description,
    priority: event.classification.impact_level === 'CRITICAL' ? 'CRITICAL' : 
              event.classification.impact_level === 'MAJOR' ? 'HIGH' : 'MEDIUM',
    status: 'PENDING',
    type: determineWorkOrderType(event),
    source_event: event,
    tasks: generateTasksFromEvent(event),
    resources: estimateResources(event),
    schedule: {
      created_date: new Date().toISOString(),
      due_date: calculateDueDate(event),
      estimated_duration_hours: estimateDuration(event)
    },
    assignment: {
      assigned_to: 'TBD',
      assigned_team: event.product_chain.domain,
      assigned_facility: 'PRIMARY'
    },
    approval: {
      required_approvers: getRequiredApprovers(event),
      approvals_received: []
    },
    impact: analyzeImpact(event)
  };
}

function determineWorkOrderType(event: CAXChangeEvent): WorkOrder['type'] {
  if (event.change.change_category === 'DESIGN') return 'DESIGN_UPDATE';
  if (event.change.change_category === 'PROCESS') return 'MANUFACTURING_CHANGE';
  if (event.change.change_category === 'DOCUMENTATION') return 'DOCUMENTATION_UPDATE';
  return 'MODIFICATION';
}

function generateTasksFromEvent(event: CAXChangeEvent): WorkOrderTask[] {
  const tasks: WorkOrderTask[] = [];
  
  if (event.classification.requires_testing) {
    tasks.push({
      task_id: `TASK-TEST-${Date.now()}`,
      task_number: tasks.length + 1,
      description: 'Perform verification testing',
      status: 'PENDING',
      estimated_hours: 8,
      dependencies: [],
      verification_required: true
    });
  }
  
  if (event.classification.requires_documentation_update) {
    tasks.push({
      task_id: `TASK-DOC-${Date.now()}`,
      task_number: tasks.length + 1,
      description: 'Update technical documentation',
      status: 'PENDING',
      estimated_hours: 4,
      dependencies: [],
      verification_required: true
    });
  }
  
  return tasks;
}

function estimateResources(event: CAXChangeEvent): WorkOrder['resources'] {
  return {
    required_personnel: [
      { role: 'Engineer', quantity: 1, skill_level: 'Senior' }
    ],
    required_tools: ['CAD Workstation', 'Testing Equipment'],
    required_materials: [],
    estimated_hours: estimateDuration(event),
    estimated_cost: 0
  };
}

function estimateDuration(event: CAXChangeEvent): number {
  switch (event.classification.impact_level) {
    case 'CRITICAL': return 40;
    case 'MAJOR': return 24;
    case 'MINOR': return 8;
    default: return 4;
  }
}

function calculateDueDate(event: CAXChangeEvent): string {
  const now = new Date();
  const daysToAdd = event.classification.impact_level === 'CRITICAL' ? 7 : 
                    event.classification.impact_level === 'MAJOR' ? 14 : 30;
  now.setDate(now.getDate() + daysToAdd);
  return now.toISOString();
}

function getRequiredApprovers(event: CAXChangeEvent): string[] {
  const approvers = ['Engineering Manager'];
  if (event.classification.requires_certification) {
    approvers.push('Certification Authority');
  }
  if (event.classification.impact_level === 'CRITICAL') {
    approvers.push('Chief Engineer');
  }
  return approvers;
}

function analyzeImpact(event: CAXChangeEvent): WorkOrderImpact {
  return {
    affected_artifacts: [],
    affected_documents: [],
    affected_parts: [],
    affected_assemblies: [],
    affected_test_procedures: []
  };
}

export function propagateChange(event: CAXChangeEvent): ChangePropagation {
  return {
    propagation_id: `PROP-${Date.now()}`,
    source_event: event,
    timestamp: new Date().toISOString(),
    impact_analysis: {
      direct_impacts: [],
      indirect_impacts: [],
      risk_assessment: {
        overall_risk_level: event.classification.impact_level,
        safety_risk: event.trigger_criteria.safety_impact,
        certification_risk: event.classification.requires_certification,
        production_risk: event.classification.affects_production,
        schedule_risk: false,
        cost_risk: false,
        risk_description: 'Automated risk assessment',
        mitigation_required: event.classification.impact_level === 'CRITICAL'
      }
    },
    generated_work_orders: [],
    updated_documents: [],
    notifications_sent: [],
    status: 'ANALYZING',
    errors: []
  };
}
