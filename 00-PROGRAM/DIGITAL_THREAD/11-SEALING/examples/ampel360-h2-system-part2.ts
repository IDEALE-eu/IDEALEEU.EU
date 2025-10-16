/**
 * SEALING Example: AMPEL360-AIR-T H2-Powered Aircraft System (Part 2)
 * 
 * Continuation: Edge Gateway and Integrated System
 */

import {
  NetworkNode,
  IntegratedSystem,
  createJointRelation
} from '../types';

import {
  flightControlFirmware,
  flightControlComputer,
  predictiveMaintenanceAI
} from './ampel360-h2-system-part1';

// ============================================================================
// 4. EDGE COMPUTING GATEWAY (Network Node)
// ============================================================================

export const edgeComputeGateway: NetworkNode = {
  // Identification
  node_id: 'EDGE-GW-001',
  utcs_ref: 'UTCS-LCC/EDGE-GW-001@1.0.0',
  identification: {
    name: 'Edge Compute Gateway',
    type: 'PHYSICAL',
    role: 'GATEWAY'
  },

  // Location
  location: {
    physical: {
      aircraft_zone: 'FWD-EQUIP-BAY',
      ata_reference: 'ATA-42-10',
      rack: 'AVIONICS-RACK-1'
    },
    network: {
      ip_address: '192.168.100.10',
      subnet: '255.255.255.0',
      vlan: 100,
      domain: 'avionics.ampel360.local'
    }
  },

  // Capabilities
  capabilities: {
    compute: {
      cpu_cores: 8,
      ram_gb: 16,
      storage_gb: 256
    },
    communication: {
      interfaces: ['CAN', 'Ethernet', 'WiFi-6'],
      bandwidth_mbps: 1000,
      protocols: ['TCP/IP', 'ARINC-825', 'gRPC', 'MQTT']
    }
  },

  // Services
  services: [
    {
      service_id: 'SVC-AI-PREDMAINT',
      name: 'Predictive Maintenance Service',
      version: '1.2.0',
      type: 'AI_MODEL',
      container: {
        image: 'ideale-registry/predmaint-inference',
        tag: '1.2.0',
        registry: 'registry.ideale-eu.org'
      },
      resources: {
        cpu_request: '500m',
        cpu_limit: '2000m',
        memory_request: '512Mi',
        memory_limit: '2Gi'
      },
      endpoints: [
        {
          endpoint_id: 'EP-INFERENCE',
          protocol: 'gRPC',
          port: 8500,
          path: '/predict',
          authentication: 'mTLS',
          rate_limit: {
            requests_per_second: 100,
            burst: 150
          }
        }
      ],
      dependencies: ['SVC-DATA-PROCESSOR'],
      health_check: {
        path: '/health',
        interval_seconds: 30,
        timeout_seconds: 5
      }
    },
    {
      service_id: 'SVC-DATA-PROCESSOR',
      name: 'Sensor Data Processing Service',
      version: '2.1.0',
      type: 'MICROSERVICE',
      container: {
        image: 'ideale-registry/data-processor',
        tag: '2.1.0',
        registry: 'registry.ideale-eu.org'
      },
      resources: {
        cpu_request: '250m',
        cpu_limit: '1000m',
        memory_request: '256Mi',
        memory_limit: '1Gi'
      },
      endpoints: [
        {
          endpoint_id: 'EP-DATA-INGEST',
          protocol: 'gRPC',
          port: 8501,
          path: '/ingest',
          authentication: 'mTLS'
        }
      ],
      dependencies: [],
      health_check: {
        path: '/health',
        interval_seconds: 30,
        timeout_seconds: 5
      }
    },
    {
      service_id: 'SVC-TELEMETRY-AGENT',
      name: 'Telemetry Collection Agent',
      version: '3.0.1',
      type: 'MICROSERVICE',
      resources: {
        cpu_request: '100m',
        cpu_limit: '500m',
        memory_request: '128Mi',
        memory_limit: '512Mi'
      },
      endpoints: [
        {
          endpoint_id: 'EP-METRICS',
          protocol: 'HTTP',
          port: 9090,
          path: '/metrics',
          authentication: 'NONE'
        }
      ],
      dependencies: []
    }
  ],

  // Security
  security: {
    security_level: 'MISSION_CRITICAL',
    authentication: {
      method: 'CERTIFICATE',
      certificate_expiry: '2026-10-16T00:00:00Z',
      mfa_required: false
    },
    encryption: {
      at_rest: true,
      in_transit: true,
      algorithms: ['AES-256-GCM', 'RSA-4096', 'ECDSA-P256'],
      key_management: {
        system: 'HSM',
        key_rotation_days: 90
      }
    },
    firewall: {
      enabled: true,
      default_policy: 'DENY',
      rules: [
        {
          rule_id: 'FW-001',
          action: 'ALLOW',
          source: { ip_range: '192.168.100.0/24' },
          destination: { port_range: '8500-8501' },
          protocol: 'TCP',
          priority: 100
        },
        {
          rule_id: 'FW-002',
          action: 'ALLOW',
          source: { ip_range: '192.168.100.0/24' },
          destination: { port_range: '9090' },
          protocol: 'TCP',
          priority: 110
        },
        {
          rule_id: 'FW-003',
          action: 'DENY',
          source: { ip_range: '0.0.0.0/0' },
          destination: { port_range: '1-65535' },
          protocol: 'ANY',
          priority: 999
        }
      ]
    },
    intrusion_detection: {
      enabled: true,
      system: 'Suricata',
      rules_version: '2025.10.01',
      alerting: {
        email: ['security-ops@ideale-eu.org'],
        webhook: 'https://alerts.ideale-eu.org/ids'
      }
    },
    vulnerabilities: {
      last_scan: '2025-10-15T00:00:00Z',
      scanner: 'Trivy',
      critical: 0,
      high: 0,
      medium: 2,
      low: 5
    },
    compliance: {
      standards: ['DO-326A', 'NIST-800-53', 'ISO-27001'],
      last_audit: '2025-09-01T00:00:00Z',
      status: 'COMPLIANT',
      findings: []
    }
  },

  // Health
  health: {
    status: 'HEALTHY',
    last_heartbeat: '2025-10-16T15:30:00Z',
    metrics: {
      cpu_usage_percent: 35,
      memory_usage_percent: 45,
      disk_usage_percent: 30,
      network_rx_mbps: 25,
      network_tx_mbps: 15,
      temperature_celsius: 45
    },
    alerts: [],
    uptime_seconds: 2592000 // 30 days
  },

  // Metadata
  created_date: '2025-09-01T00:00:00Z',
  last_modified_date: '2025-10-16T00:00:00Z',
  owner: 'edge-computing-team@ideale-eu.org',
  documentation_uri: 'https://docs.ideale-eu.org/edge-gateway',

  // Relationships
  parent_prd: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EDI-ELECTRONICS-DIGITAL-INSTRUMENTS/PRD.md'
};

// ============================================================================
// 5. INTEGRATED FLIGHT CONTROL & PREDICTIVE MAINTENANCE SYSTEM
// ============================================================================

export const integratedFlightSystem: IntegratedSystem = {
  // Identification
  system_id: 'INT-FLIGHT-PREDMAINT-001',
  utcs_ref: 'UTCS-LCC/INT-FLIGHT-001@1.0.0',
  name: 'Integrated Flight Control & Predictive Maintenance System',
  description: 'Complete system integrating flight controller, AI predictive maintenance, and edge computing for the AMPEL360-AIR-T hydrogen-electric aircraft',

  // Components
  components: {
    software: [flightControlFirmware],
    embedded: [flightControlComputer],
    ai_models: [predictiveMaintenanceAI],
    network_nodes: [edgeComputeGateway]
  },

  // Integration Points
  integration_points: [
    {
      integration_id: 'INT-FCC-TO-GATEWAY',
      from_component: {
        type: 'EMBEDDED',
        id: 'FCC-001',
        interface: 'CAN1'
      },
      to_component: {
        type: 'NETWORK_NODE',
        id: 'EDGE-GW-001',
        interface: 'CAN0'
      },
      protocol: 'ARINC 825',
      data_contract: {
        schema_uri: 's3://ideale-schemas/arinc825-messages.json',
        version: '1.0',
        validation_required: true
      },
      quality_of_service: {
        latency_ms_max: 10,
        throughput_min: 1000,
        reliability_percent: 99.99
      }
    },
    {
      integration_id: 'INT-GATEWAY-TO-AI',
      from_component: {
        type: 'NETWORK_NODE',
        id: 'EDGE-GW-001',
        interface: 'SVC-DATA-PROCESSOR'
      },
      to_component: {
        type: 'AI_MODEL',
        id: 'AI-PREDMAINT-001',
        interface: 'inference-endpoint'
      },
      protocol: 'gRPC',
      data_contract: {
        schema_uri: 's3://ideale-schemas/sensor-features.proto',
        version: '2.0',
        validation_required: true
      },
      quality_of_service: {
        latency_ms_max: 50,
        throughput_min: 100,
        reliability_percent: 99.9
      }
    }
  ],

  // Orchestration
  orchestration: {
    orchestrator: 'KUBERNETES',
    namespace: 'flight-systems',
    deployment_order: ['EDGE-GW-001', 'SVC-DATA-PROCESSOR', 'SVC-AI-PREDMAINT', 'FCC-001'],
    health_checks: [
      {
        check_id: 'HC-GATEWAY',
        type: 'HTTP',
        endpoint: 'http://192.168.100.10:9090/health',
        interval_seconds: 30,
        timeout_seconds: 5,
        healthy_threshold: 2,
        unhealthy_threshold: 3
      },
      {
        check_id: 'HC-AI-SERVICE',
        type: 'GRPC',
        endpoint: 'edge-gw-001:8500',
        interval_seconds: 30,
        timeout_seconds: 5,
        healthy_threshold: 2,
        unhealthy_threshold: 3
      }
    ],
    auto_scaling: {
      enabled: false,
      metrics: [],
      min_replicas: 1,
      max_replicas: 1
    }
  },

  // Monitoring
  monitoring: {
    observability_stack: {
      metrics: 'PROMETHEUS',
      logging: 'LOKI',
      tracing: 'JAEGER'
    },
    dashboards: [
      {
        dashboard_id: 'DASH-FLIGHT-OPS',
        name: 'Flight Operations Dashboard',
        platform: 'Grafana',
        url: 'https://grafana.ideale-eu.org/d/flight-ops',
        panels: ['flight-hours', 'control-surfaces', 'actuator-health', 'ai-predictions']
      },
      {
        dashboard_id: 'DASH-PREDICTIVE-MAINT',
        name: 'Predictive Maintenance Dashboard',
        platform: 'Grafana',
        url: 'https://grafana.ideale-eu.org/d/pred-maint',
        panels: ['anomaly-scores', 'prediction-accuracy', 'false-positives', 'maintenance-schedule']
      }
    ],
    alerts: [
      {
        rule_id: 'ALERT-FCC-CPU',
        name: 'FCC CPU Usage High',
        condition: 'fcc_cpu_usage_percent > 80',
        severity: 'WARNING',
        notification_channels: ['ops-team-slack', 'ops-email']
      },
      {
        rule_id: 'ALERT-AI-PREDICTION',
        name: 'Actuator Failure Predicted',
        condition: 'ai_anomaly_score > 0.85',
        severity: 'CRITICAL',
        notification_channels: ['maintenance-team-slack', 'maintenance-email', 'pager']
      },
      {
        rule_id: 'ALERT-CAN-BUS',
        name: 'CAN Bus Error Rate High',
        condition: 'can_error_rate > 0.01',
        severity: 'CRITICAL',
        notification_channels: ['ops-team-slack', 'engineering-email']
      }
    ],
    slos: [
      {
        slo_id: 'SLO-FLIGHT-AVAILABILITY',
        name: 'Flight Control System Availability',
        description: 'Flight control system must be available 99.99% of the time',
        target_percent: 99.99,
        measurement_window_days: 30,
        slis: [
          {
            sli_id: 'SLI-FCC-UPTIME',
            name: 'FCC Uptime',
            metric: 'fcc_uptime_seconds',
            good_events_query: 'fcc_status == "HEALTHY"',
            total_events_query: 'count(fcc_status)',
            threshold: 0.9999
          }
        ],
        error_budget_percent: 0.01,
        error_budget_remaining_percent: 0.008
      },
      {
        slo_id: 'SLO-AI-LATENCY',
        name: 'AI Inference Latency',
        description: '95% of AI inferences must complete within 50ms',
        target_percent: 95,
        measurement_window_days: 7,
        slis: [
          {
            sli_id: 'SLI-AI-P95-LATENCY',
            name: 'AI P95 Latency',
            metric: 'ai_inference_latency_ms',
            good_events_query: 'ai_inference_latency_ms < 50',
            total_events_query: 'count(ai_inference_requests)',
            threshold: 0.95
          }
        ],
        error_budget_percent: 5,
        error_budget_remaining_percent: 4.2
      }
    ]
  },

  // Lifecycle
  lifecycle: {
    current_phase: 'PRODUCTION',
    environments: [
      {
        environment_id: 'ENV-DEV',
        name: 'DEVELOPMENT',
        deployed_version: '1.1.0-dev',
        deployment_date: '2025-10-10T00:00:00Z',
        configuration_override: {
          log_level: 'DEBUG',
          enable_test_mode: true
        }
      },
      {
        environment_id: 'ENV-STAGING',
        name: 'STAGING',
        deployed_version: '1.0.0',
        deployment_date: '2025-10-12T00:00:00Z',
        configuration_override: {
          log_level: 'INFO'
        }
      },
      {
        environment_id: 'ENV-PROD',
        name: 'PRODUCTION',
        deployed_version: '1.0.0',
        deployment_date: '2025-10-01T00:00:00Z',
        configuration_override: {
          log_level: 'WARNING',
          enable_high_availability: true
        }
      }
    ],
    promotion_gates: [
      {
        gate_id: 'GATE-DEV-TO-STAGING',
        from_environment: 'DEVELOPMENT',
        to_environment: 'STAGING',
        checks: [
          {
            check_type: 'TESTS',
            required: true,
            status: 'PASSED'
          },
          {
            check_type: 'SECURITY_SCAN',
            required: true,
            status: 'PASSED'
          },
          {
            check_type: 'APPROVAL',
            required: true,
            status: 'PASSED'
          }
        ]
      },
      {
        gate_id: 'GATE-STAGING-TO-PROD',
        from_environment: 'STAGING',
        to_environment: 'PRODUCTION',
        checks: [
          {
            check_type: 'TESTS',
            required: true,
            status: 'PASSED'
          },
          {
            check_type: 'SECURITY_SCAN',
            required: true,
            status: 'PASSED'
          },
          {
            check_type: 'PERFORMANCE',
            required: true,
            status: 'PASSED'
          },
          {
            check_type: 'APPROVAL',
            required: true,
            status: 'PASSED'
          }
        ]
      }
    ],
    change_history: [
      {
        change_id: 'CHG-001',
        timestamp: '2025-10-01T00:00:00Z',
        user: 'ops-team',
        type: 'DEPLOYMENT',
        description: 'Initial production deployment of integrated flight system',
        version_before: '0.0.0',
        version_after: '1.0.0'
      },
      {
        change_id: 'CHG-002',
        timestamp: '2025-10-05T14:30:00Z',
        user: 'ops-team',
        type: 'CONFIGURATION',
        description: 'Updated AI model threshold for anomaly detection',
        version_before: '1.0.0',
        version_after: '1.0.0'
      }
    ]
  },

  // Metadata
  created_date: '2025-08-01T00:00:00Z',
  last_modified_date: '2025-10-16T00:00:00Z',
  owner: 'systems-integration-team@ideale-eu.org',
  documentation_uri: 'https://docs.ideale-eu.org/integrated-flight-system',

  // Relationships
  parent_prd: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/PRD.md',
  related_systems: ['INT-HYDROGEN-PROPULSION-001', 'INT-AVIONICS-001']
};

// ============================================================================
// EXAMPLE USAGE AND VALIDATION
// ============================================================================

console.log('='.repeat(80));
console.log('AMPEL360-AIR-T H2-POWERED AIRCRAFT - INTEGRATED SYSTEM');
console.log('='.repeat(80));
console.log('');
console.log(`System: ${integratedFlightSystem.name}`);
console.log(`UTCS Reference: ${integratedFlightSystem.utcs_ref}`);
console.log(`Status: ${integratedFlightSystem.lifecycle.current_phase}`);
console.log('');
console.log('Components:');
console.log(`  - Software Components: ${integratedFlightSystem.components.software.length}`);
console.log(`  - Embedded Systems: ${integratedFlightSystem.components.embedded.length}`);
console.log(`  - AI Models: ${integratedFlightSystem.components.ai_models.length}`);
console.log(`  - Network Nodes: ${integratedFlightSystem.components.network_nodes.length}`);
console.log('');
console.log('Integration Points:');
integratedFlightSystem.integration_points.forEach(ip => {
  console.log(`  - ${ip.from_component.id} → ${ip.to_component.id} (${ip.protocol})`);
});
console.log('');
console.log('Monitoring:');
console.log(`  - Dashboards: ${integratedFlightSystem.monitoring.dashboards.length}`);
console.log(`  - Alerts: ${integratedFlightSystem.monitoring.alerts.length}`);
console.log(`  - SLOs: ${integratedFlightSystem.monitoring.slos.length}`);
console.log('');
console.log('='.repeat(80));

// Export for use in other modules
export default integratedFlightSystem;
