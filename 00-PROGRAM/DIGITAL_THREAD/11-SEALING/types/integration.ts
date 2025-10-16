/**
 * SEALING - Integration Type Definitions
 * 
 * Comprehensive data structures for integrating software, embedded systems,
 * AI models, and network nodes into cohesive systems.
 */

import { SoftwareComponent } from './software';
import { EmbeddedSystem } from './embedded';
import { AIModel } from './ai';
import { NetworkNode } from './network';

// ============================================================================
// Integration Points
// ============================================================================

export interface IntegrationPoint {
  integration_id: string;
  from_component: {
    type: 'SOFTWARE' | 'EMBEDDED' | 'AI_MODEL' | 'NETWORK_NODE';
    id: string;
    interface: string;
  };
  to_component: {
    type: 'SOFTWARE' | 'EMBEDDED' | 'AI_MODEL' | 'NETWORK_NODE';
    id: string;
    interface: string;
  };
  protocol: string; // e.g., 'ARINC 825', 'REST', 'gRPC', 'CAN'
  data_contract: {
    schema_uri: string;
    version: string;
    validation_required: boolean;
  };
  quality_of_service?: {
    latency_ms_max: number;
    throughput_min: number;
    reliability_percent: number;
  };
}

// ============================================================================
// Orchestration
// ============================================================================

export interface HealthCheck {
  check_id: string;
  type: 'HTTP' | 'TCP' | 'EXEC' | 'GRPC';
  endpoint?: string;
  command?: string;
  interval_seconds: number;
  timeout_seconds: number;
  healthy_threshold: number;
  unhealthy_threshold: number;
}

export interface AutoScalingMetric {
  metric_name: string;
  target_value: number;
  scale_up_threshold: number;
  scale_down_threshold: number;
}

export interface OrchestrationInfo {
  orchestrator: 'KUBERNETES' | 'DOCKER_SWARM' | 'NOMAD' | 'ECS' | 'CUSTOM';
  namespace?: string;
  deployment_order: string[]; // Component IDs in order
  health_checks: HealthCheck[];
  auto_scaling?: {
    enabled: boolean;
    metrics: AutoScalingMetric[];
    min_replicas: number;
    max_replicas: number;
  };
}

// ============================================================================
// Monitoring
// ============================================================================

export interface Dashboard {
  dashboard_id: string;
  name: string;
  platform: 'Grafana' | 'Kibana' | 'Datadog' | 'Custom';
  url: string;
  panels: string[];
}

export interface AlertRule {
  rule_id: string;
  name: string;
  condition: string; // e.g., 'cpu_usage > 80'
  severity: 'CRITICAL' | 'WARNING' | 'INFO';
  notification_channels: string[];
}

export interface SLO {
  slo_id: string;
  name: string;
  description: string;
  target_percent: number; // e.g., 99.9
  measurement_window_days: number;
  slis: SLI[];
  error_budget_percent: number;
  error_budget_remaining_percent?: number;
}

export interface SLI {
  sli_id: string;
  name: string;
  metric: string;
  good_events_query: string;
  total_events_query: string;
  threshold: number;
}

export interface ObservabilityStack {
  metrics: 'PROMETHEUS' | 'INFLUXDB' | 'DATADOG' | 'CUSTOM';
  logging: 'ELK' | 'LOKI' | 'SPLUNK' | 'CUSTOM';
  tracing: 'JAEGER' | 'ZIPKIN' | 'DATADOG' | 'CUSTOM';
}

export interface MonitoringInfo {
  observability_stack: ObservabilityStack;
  dashboards: Dashboard[];
  alerts: AlertRule[];
  slos: SLO[];
}

// ============================================================================
// Lifecycle Management
// ============================================================================

export interface Environment {
  environment_id: string;
  name: 'DEVELOPMENT' | 'STAGING' | 'PRODUCTION' | 'DR';
  deployed_version: string;
  deployment_date: string;
  configuration_override: Record<string, any>;
}

export interface PromotionGate {
  gate_id: string;
  from_environment: string;
  to_environment: string;
  checks: Array<{
    check_type: 'TESTS' | 'SECURITY_SCAN' | 'PERFORMANCE' | 'APPROVAL';
    required: boolean;
    status: 'PENDING' | 'PASSED' | 'FAILED';
  }>;
}

export interface ChangeRecord {
  change_id: string;
  timestamp: string;
  user: string;
  type: 'DEPLOYMENT' | 'CONFIGURATION' | 'SCALING' | 'ROLLBACK';
  description: string;
  version_before: string;
  version_after: string;
}

export interface LifecycleInfo {
  current_phase: 'DEVELOPMENT' | 'TESTING' | 'STAGING' | 'PRODUCTION' | 'DEPRECATED';
  environments: Environment[];
  promotion_gates: PromotionGate[];
  change_history: ChangeRecord[];
}

// ============================================================================
// Main Integrated System Interface
// ============================================================================

export interface IntegratedSystem {
  // Identification
  system_id: string;
  utcs_ref: string; // e.g., "UTCS-LCC/INT-FLIGHT-001@1.0.0"
  name: string;
  description: string;

  // Components
  components: {
    software: SoftwareComponent[];
    embedded: EmbeddedSystem[];
    ai_models: AIModel[];
    network_nodes: NetworkNode[];
  };

  // Integration
  integration_points: IntegrationPoint[];

  // Orchestration
  orchestration?: OrchestrationInfo;

  // Monitoring
  monitoring: MonitoringInfo;

  // Lifecycle
  lifecycle: LifecycleInfo;

  // Metadata
  created_date: string;
  last_modified_date: string;
  owner: string;
  documentation_uri?: string;

  // Relationships
  parent_prd?: string; // Reference to PRD document
  related_systems?: string[]; // Other system IDs
}

// ============================================================================
// DevSecOps Pipeline
// ============================================================================

export interface PipelineStage {
  stage_id: string;
  name: string;
  order: number;
  jobs: Array<{
    job_id: string;
    name: string;
    type: 'BUILD' | 'TEST' | 'SCAN' | 'DEPLOY' | 'VERIFY';
    commands: string[];
    artifacts?: string[];
  }>;
}

export interface DeploymentStrategy {
  strategy: 'BLUE_GREEN' | 'CANARY' | 'ROLLING' | 'RECREATE';
  canary_percent?: number;
  rollout_duration_minutes?: number;
  rollback_on_failure: boolean;
}

export interface PipelineMetrics {
  total_runs: number;
  success_rate_percent: number;
  average_duration_minutes: number;
  last_run_date: string;
  last_run_status: 'SUCCESS' | 'FAILURE' | 'CANCELLED' | 'RUNNING';
}

export interface CICDPipeline {
  pipeline_id: string;
  name: string;
  trigger: 'PUSH' | 'PR' | 'SCHEDULE' | 'MANUAL';
  stages: PipelineStage[];
  deployment_strategy: DeploymentStrategy;
  metrics: PipelineMetrics;
}

// ============================================================================
// Helper Functions
// ============================================================================

export function createJointRelation(
  from_component: SoftwareComponent | EmbeddedSystem | AIModel | NetworkNode,
  to_component: SoftwareComponent | EmbeddedSystem | AIModel | NetworkNode,
  protocol: string
): IntegrationPoint {
  const getComponentType = (comp: any): 'SOFTWARE' | 'EMBEDDED' | 'AI_MODEL' | 'NETWORK_NODE' => {
    if ('component_id' in comp) return 'SOFTWARE';
    if ('system_id' in comp) return 'EMBEDDED';
    if ('model_id' in comp) return 'AI_MODEL';
    return 'NETWORK_NODE';
  };

  const getId = (comp: any): string => {
    return comp.component_id || comp.system_id || comp.model_id || comp.node_id;
  };

  return {
    integration_id: `INT-${Date.now()}`,
    from_component: {
      type: getComponentType(from_component),
      id: getId(from_component),
      interface: 'default'
    },
    to_component: {
      type: getComponentType(to_component),
      id: getId(to_component),
      interface: 'default'
    },
    protocol,
    data_contract: {
      schema_uri: `schema://${protocol}`,
      version: '1.0',
      validation_required: true
    }
  };
}

export function validateIntegratedSystem(system: IntegratedSystem): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!system.system_id) errors.push('system_id is required');
  if (!system.utcs_ref) errors.push('utcs_ref is required');
  if (!system.name) errors.push('name is required');

  const totalComponents = 
    system.components.software.length +
    system.components.embedded.length +
    system.components.ai_models.length +
    system.components.network_nodes.length;

  if (totalComponents === 0) {
    errors.push('At least one component is required');
  }

  return {
    valid: errors.length === 0,
    errors
  };
}

export function calculateSystemComplexity(system: IntegratedSystem): {
  total_components: number;
  integration_points: number;
  complexity_score: number;
} {
  const total_components =
    system.components.software.length +
    system.components.embedded.length +
    system.components.ai_models.length +
    system.components.network_nodes.length;

  const integration_points = system.integration_points.length;
  const complexity_score = total_components * integration_points;

  return {
    total_components,
    integration_points,
    complexity_score
  };
}
