/**
 * SEALING - Network Governance Type Definitions
 * 
 * Comprehensive data structures for network nodes, services, security,
 * and governance policies.
 */

// ============================================================================
// Core Identification
// ============================================================================

export interface NetworkIdentification {
  name: string;
  type: 'PHYSICAL' | 'VIRTUAL' | 'CONTAINER' | 'SERVICE_MESH';
  role: 'GATEWAY' | 'EDGE' | 'CORE' | 'COMPUTE' | 'STORAGE' | 'CONTROLLER';
}

// ============================================================================
// Location
// ============================================================================

export interface PhysicalLocation {
  aircraft_zone?: string;
  ata_reference?: string;
  rack?: string;
  datacenter?: string;
  coordinates?: {
    latitude: number;
    longitude: number;
  };
}

export interface NetworkLocation {
  ip_address: string;
  subnet: string;
  vlan?: number;
  domain: string;
}

export interface LocationInfo {
  physical?: PhysicalLocation;
  network: NetworkLocation;
}

// ============================================================================
// Capabilities
// ============================================================================

export interface ComputeCapabilities {
  cpu_cores: number;
  ram_gb: number;
  storage_gb: number;
  gpu?: {
    model: string;
    memory_gb: number;
  };
}

export interface CommunicationCapabilities {
  interfaces: string[]; // e.g., ['CAN', 'Ethernet', 'WiFi-6']
  bandwidth_mbps: number;
  protocols: string[];
}

export interface NodeCapabilities {
  compute?: ComputeCapabilities;
  communication: CommunicationCapabilities;
  specialized?: Record<string, any>;
}

// ============================================================================
// Services
// ============================================================================

export interface ServiceResources {
  cpu_request: string; // e.g., '500m'
  cpu_limit: string;
  memory_request: string; // e.g., '512Mi'
  memory_limit: string;
}

export interface ServiceEndpoint {
  endpoint_id: string;
  protocol: 'HTTP' | 'HTTPS' | 'gRPC' | 'WebSocket' | 'MQTT' | 'AMQP';
  port: number;
  path: string;
  authentication: 'NONE' | 'BASIC' | 'BEARER' | 'mTLS' | 'API_KEY';
  rate_limit?: {
    requests_per_second: number;
    burst: number;
  };
}

export interface Service {
  service_id: string;
  name: string;
  version: string;
  type: 'MICROSERVICE' | 'DATABASE' | 'MESSAGE_QUEUE' | 'CACHE' | 'AI_MODEL' | 'GATEWAY' | 'PROXY';
  container?: {
    image: string;
    tag: string;
    registry: string;
  };
  resources: ServiceResources;
  endpoints: ServiceEndpoint[];
  dependencies: string[]; // Other service IDs
  health_check?: {
    path: string;
    interval_seconds: number;
    timeout_seconds: number;
  };
}

// ============================================================================
// Security
// ============================================================================

export interface FirewallRule {
  rule_id: string;
  action: 'ALLOW' | 'DENY' | 'LOG';
  source: {
    ip_range?: string;
    service_id?: string;
  };
  destination: {
    port_range?: string;
    service_id?: string;
  };
  protocol: 'TCP' | 'UDP' | 'ICMP' | 'ANY';
  priority: number;
}

export interface FirewallConfig {
  enabled: boolean;
  default_policy: 'ALLOW' | 'DENY';
  rules: FirewallRule[];
}

export interface IntrusionDetection {
  enabled: boolean;
  system: 'Snort' | 'Suricata' | 'Zeek' | 'OSSEC';
  rules_version: string;
  alerting: {
    email?: string[];
    webhook?: string;
  };
}

export interface EncryptionConfig {
  at_rest: boolean;
  in_transit: boolean;
  algorithms: string[];
  key_management?: {
    system: 'KMS' | 'Vault' | 'HSM';
    key_rotation_days: number;
  };
}

export interface AuthenticationConfig {
  method: 'PASSWORD' | 'CERTIFICATE' | 'OAUTH2' | 'SAML' | 'LDAP';
  certificate_expiry?: string;
  mfa_required?: boolean;
}

export interface VulnerabilityScan {
  last_scan: string;
  scanner: string;
  critical: number;
  high: number;
  medium: number;
  low: number;
}

export interface ComplianceStatus {
  standards: string[]; // e.g., ['DO-326A', 'NIST-800-53', 'ISO-27001']
  last_audit: string;
  status: 'COMPLIANT' | 'NON_COMPLIANT' | 'PARTIAL';
  findings?: string[];
}

export interface SecurityInfo {
  security_level: 'PUBLIC' | 'INTERNAL' | 'CONFIDENTIAL' | 'MISSION_CRITICAL';
  authentication: AuthenticationConfig;
  encryption: EncryptionConfig;
  firewall: FirewallConfig;
  intrusion_detection?: IntrusionDetection;
  vulnerabilities?: VulnerabilityScan;
  compliance?: ComplianceStatus;
}

// ============================================================================
// Health and Monitoring
// ============================================================================

export interface HealthMetrics {
  cpu_usage_percent: number;
  memory_usage_percent: number;
  disk_usage_percent: number;
  network_rx_mbps: number;
  network_tx_mbps: number;
  temperature_celsius?: number;
}

export interface Alert {
  alert_id: string;
  severity: 'CRITICAL' | 'WARNING' | 'INFO';
  message: string;
  timestamp: string;
  acknowledged: boolean;
}

export interface HealthInfo {
  status: 'HEALTHY' | 'DEGRADED' | 'UNHEALTHY' | 'UNKNOWN';
  last_heartbeat: string;
  metrics: HealthMetrics;
  alerts: Alert[];
  uptime_seconds?: number;
}

// ============================================================================
// Main Network Node Interface
// ============================================================================

export interface NetworkNode {
  // Identification
  node_id: string;
  utcs_ref: string; // e.g., "UTCS-LCC/EDGE-GW-001@1.0.0"
  identification: NetworkIdentification;

  // Location
  location: LocationInfo;

  // Capabilities
  capabilities: NodeCapabilities;

  // Services
  services: Service[];

  // Security
  security: SecurityInfo;

  // Health
  health: HealthInfo;

  // Metadata
  created_date: string;
  last_modified_date: string;
  owner: string;
  documentation_uri?: string;

  // Relationships
  parent_prd?: string; // Reference to PRD document
  related_nodes?: string[]; // Other node IDs
  parent_node?: string; // Parent node in hierarchy
}

// ============================================================================
// Network Topology
// ============================================================================

export interface NetworkSegment {
  segment_id: string;
  name: string;
  type: 'DMZ' | 'INTERNAL' | 'MANAGEMENT' | 'PRODUCTION' | 'DEVELOPMENT';
  cidr: string;
  nodes: string[]; // Node IDs
}

export interface NetworkTopology {
  topology_id: string;
  name: string;
  segments: NetworkSegment[];
  connections: Array<{
    from_node: string;
    to_node: string;
    link_type: 'ETHERNET' | 'FIBER' | 'WIRELESS' | 'VPN';
    bandwidth_mbps: number;
  }>;
}

// ============================================================================
// Governance Policies
// ============================================================================

export interface AccessPolicy {
  policy_id: string;
  name: string;
  rules: Array<{
    principal: string; // User or service
    resource: string;
    actions: string[];
    effect: 'ALLOW' | 'DENY';
  }>;
}

export interface DataGovernance {
  classification: 'PUBLIC' | 'INTERNAL' | 'CONFIDENTIAL' | 'RESTRICTED';
  retention_days: number;
  encryption_required: boolean;
  pii_present: boolean;
  gdpr_compliant: boolean;
}

export interface GovernancePolicies {
  access_policies: AccessPolicy[];
  data_governance: DataGovernance;
  incident_response_plan: string; // URI to plan
}

// ============================================================================
// Helper Functions
// ============================================================================

export function calculateNetworkUtilization(node: NetworkNode): number {
  const metrics = node.health.metrics;
  return (metrics.network_rx_mbps + metrics.network_tx_mbps) / node.capabilities.communication.bandwidth_mbps * 100;
}

export function validateNetworkNode(node: NetworkNode): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!node.node_id) errors.push('node_id is required');
  if (!node.utcs_ref) errors.push('utcs_ref is required');
  if (!node.identification?.name) errors.push('identification.name is required');
  if (!node.location?.network?.ip_address) errors.push('location.network.ip_address is required');
  if (!node.security) errors.push('security configuration is required');

  return {
    valid: errors.length === 0,
    errors
  };
}

export function getServicesByType(node: NetworkNode, type: Service['type']): Service[] {
  return node.services.filter(s => s.type === type);
}

export function checkSecurityCompliance(node: NetworkNode): {
  compliant: boolean;
  issues: string[];
} {
  const issues: string[] = [];

  if (!node.security.encryption.in_transit) {
    issues.push('Encryption in transit is not enabled');
  }

  if (!node.security.firewall.enabled) {
    issues.push('Firewall is not enabled');
  }

  if (node.security.vulnerabilities) {
    if (node.security.vulnerabilities.critical > 0) {
      issues.push(`${node.security.vulnerabilities.critical} critical vulnerabilities found`);
    }
  }

  return {
    compliant: issues.length === 0,
    issues
  };
}
