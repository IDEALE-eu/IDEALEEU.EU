/**
 * SEALING Example: AMPEL360-AIR-T H2-Powered Aircraft System
 * 
 * This example demonstrates the complete integration of Software, Embedded Systems,
 * AI Lifecycle, and Network Governance for the AMPEL360-AIR-T hydrogen-electric aircraft.
 * 
 * This system includes:
 * - Flight Control Computer (Embedded System)
 * - Flight Control Firmware (Software Component)
 * - Predictive Maintenance AI Model
 * - Edge Computing Gateway (Network Node)
 * - Complete Integration and Monitoring
 */

import {
  SoftwareComponent,
  EmbeddedSystem,
  AIModel,
  NetworkNode,
  IntegratedSystem,
  createJointRelation
} from '../types';

// ============================================================================
// 1. FLIGHT CONTROL FIRMWARE (Software Component)
// ============================================================================

export const flightControlFirmware: SoftwareComponent = {
  // Identification
  component_id: 'FW-FCC-001',
  utcs_ref: 'UTCS-LCC/FW-FCC-001@2.5.3',
  identification: {
    name: 'Flight Control Firmware',
    version: '2.5.3',
    type: 'FIRMWARE',
    domain: 'LCC', // Linkages, Control, Communications
    description: 'Primary flight control firmware for BWB-H2 aircraft'
  },

  // Repository
  repository: {
    vcs: 'git',
    url: 'https://github.com/IDEALE-EU/ampel360-fcc-firmware',
    branch: 'main',
    commit_sha: 'a1b2c3d4e5f6789012345678901234567890abcd',
    tag: 'v2.5.3'
  },

  // Build
  build: {
    build_id: 'BUILD-20251016-001',
    build_date: '2025-10-16T10:00:00Z',
    build_tool: 'cmake',
    compiler: 'arm-none-eabi-gcc',
    compiler_version: '11.3.0',
    build_flags: ['-O2', '-Wall', '-Werror', '-fstack-protector-strong', '-DNDEBUG'],
    artifacts: [
      {
        artifact_id: 'BIN-001',
        type: 'BINARY',
        file_name: 'fcc_firmware.bin',
        file_size_bytes: 524288, // 512 KB
        checksum: {
          sha256: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
          sha512: 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
        },
        signature: {
          algorithm: 'RSA',
          public_key_id: 'KEY-FCC-PROD-2025',
          signature_base64: 'MEUCIQDxyz...truncated...signature'
        },
        storage_location: 's3://ideale-artifacts/fcc/v2.5.3/fcc_firmware.bin'
      }
    ]
  },

  // Dependencies
  dependencies: [
    {
      name: 'FreeRTOS',
      version: '10.5.1',
      type: 'RUNTIME',
      license: 'MIT',
      source: 'https://github.com/FreeRTOS/FreeRTOS',
      checksum: 'sha256:abc123...'
    },
    {
      name: 'ARM CMSIS',
      version: '5.9.0',
      type: 'COMPILE',
      license: 'Apache-2.0',
      source: 'https://github.com/ARM-software/CMSIS_5',
      checksum: 'sha256:def456...'
    }
  ],

  // SBOM
  sbom: {
    sbom_id: 'SBOM-FCC-20251016',
    format: 'SPDX',
    version: '2.3',
    created_date: '2025-10-16T10:30:00Z',
    creator: 'IDEALE-EU Build System',
    components: [
      {
        component_id: 'COMP-001',
        name: 'Flight Control Firmware',
        version: '2.5.3',
        type: 'FIRMWARE',
        supplier: 'IDEALE-EU',
        license: 'Proprietary',
        hashes: {
          sha256: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        }
      },
      {
        component_id: 'COMP-002',
        name: 'FreeRTOS',
        version: '10.5.1',
        type: 'LIBRARY',
        supplier: 'Amazon Web Services',
        license: 'MIT'
      }
    ],
    relationships: [
      {
        from_component: 'COMP-001',
        to_component: 'COMP-002',
        relationship_type: 'DEPENDS_ON'
      }
    ],
    document_uri: 's3://ideale-sboms/fcc-v2.5.3.spdx',
    checksum: 'sha256:sbom123...'
  },

  // Testing
  testing: {
    unit_tests: {
      suite_id: 'UT-FCC-001',
      total_tests: 450,
      passed: 450,
      failed: 0,
      skipped: 0,
      execution_time_seconds: 120,
      failures: [],
      report_uri: 's3://ideale-reports/fcc/unit-tests-v2.5.3.html'
    },
    integration_tests: {
      suite_id: 'IT-FCC-001',
      total_tests: 120,
      passed: 120,
      failed: 0,
      skipped: 0,
      execution_time_seconds: 300,
      failures: [],
      report_uri: 's3://ideale-reports/fcc/integration-tests-v2.5.3.html'
    },
    coverage_percent: 95.5
  },

  // Security
  security: {
    sast_scan: {
      scan_id: 'SAST-FCC-20251016',
      tool: 'CodeQL',
      scan_date: '2025-10-16T09:00:00Z',
      findings: [],
      report_uri: 's3://ideale-security/fcc/sast-report-v2.5.3.html'
    },
    vulnerabilities: []
  },

  // Certification
  certification: {
    standard: 'DO-178C',
    level: 'DAL_A',
    evidence_package: 's3://ideale-cert/fcc/do178c-dal-a-package-v2.5.3.zip',
    verification_methods: ['Requirements-Based Testing', 'Structural Coverage Analysis', 'Code Reviews'],
    certification_authority: 'EASA',
    certification_date: '2025-09-30T00:00:00Z'
  },

  // Provenance
  provenance: {
    slsa_level: 3,
    builder: {
      id: 'github-actions-runner-prod',
      version: '2.310.0'
    },
    invocation: {
      config_source: {
        uri: 'https://github.com/IDEALE-EU/ampel360-fcc-firmware',
        digest: { sha256: 'abc123...' },
        entry_point: '.github/workflows/build-release.yml'
      },
      parameters: {
        target: 'release',
        optimization: 'O2'
      },
      environment: {
        'CI': 'true',
        'BUILD_ENV': 'production'
      }
    },
    metadata: {
      build_started_on: '2025-10-16T09:00:00Z',
      build_finished_on: '2025-10-16T10:00:00Z',
      completeness: {
        parameters: true,
        environment: true,
        materials: true
      },
      reproducible: true
    },
    materials: [
      {
        uri: 'https://github.com/FreeRTOS/FreeRTOS',
        digest: { sha256: 'def456...' }
      }
    ]
  },

  // Metadata
  created_date: '2025-01-15T00:00:00Z',
  last_modified_date: '2025-10-16T10:00:00Z',
  owner: 'flight-controls-team@ideale-eu.org',
  maintainers: ['john.smith@ideale-eu.org', 'jane.doe@ideale-eu.org'],
  documentation_uri: 'https://docs.ideale-eu.org/fcc-firmware',
  release_notes_uri: 's3://ideale-docs/fcc/release-notes-v2.5.3.md',

  // Relationships
  parent_prd: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LCC-LINKAGES-CONTROL-COMMUNICATIONS/PRD.md'
};

// ============================================================================
// 2. FLIGHT CONTROL COMPUTER (Embedded System)
// ============================================================================

export const flightControlComputer: EmbeddedSystem = {
  // Identification
  system_id: 'FCC-001',
  utcs_ref: 'UTCS-LCC/FCC-001@1.0.0',
  identification: {
    name: 'Primary Flight Control Computer',
    part_number: 'FCC-H2-BWB-001',
    hardware_revision: 'B',
    firmware_version: '2.5.3',
    domain: 'LCC',
    description: 'Triple-redundant flight control computer for BWB-H2 aircraft'
  },

  // Hardware
  hardware: {
    mcu: {
      manufacturer: 'NXP',
      part_number: 'i.MX RT1170',
      architecture: 'ARM',
      cores: 2,
      clock_speed_mhz: 1000,
      features: {
        fpu: true,
        dsp: true,
        crypto: true,
        secure_boot: true
      }
    },
    memory: {
      flash: {
        size_kb: 2048,
        ecc: true,
        type: 'NOR'
      },
      ram: {
        size_kb: 2048,
        ecc: true,
        type: 'SDRAM'
      },
      eeprom: {
        size_kb: 128
      }
    },
    peripherals: [
      {
        peripheral_id: 'CAN1',
        type: 'CAN',
        instance: 1,
        configuration: {
          baudrate: 1000000,
          mode: 'FD'
        },
        connected_to: 'AFDX_GATEWAY'
      },
      {
        peripheral_id: 'CAN2',
        type: 'CAN',
        instance: 2,
        configuration: {
          baudrate: 1000000,
          mode: 'FD'
        },
        connected_to: 'BACKUP_BUS'
      },
      {
        peripheral_id: 'ETH0',
        type: 'ETHERNET',
        instance: 0,
        configuration: {
          speed: '1Gbps',
          mode: 'full-duplex'
        },
        connected_to: 'AVIONICS_NETWORK'
      }
    ],
    power: {
      voltage_v: 28,
      current_typical_ma: 250,
      current_max_ma: 500,
      power_modes: [
        {
          mode: 'ACTIVE',
          current_ma: 250,
          wakeup_time_ms: 0
        },
        {
          mode: 'IDLE',
          current_ma: 50,
          wakeup_time_ms: 10
        },
        {
          mode: 'SLEEP',
          current_ma: 5,
          wakeup_time_ms: 100
        }
      ]
    },
    environmental_rating: {
      temp_min_c: -55,
      temp_max_c: 85,
      humidity_max_percent: 95,
      vibration_g: 15
    }
  },

  // Software
  software: {
    firmware: flightControlFirmware,
    runtime: 'RTOS',
    applications: []
  },

  // Communication
  communication: {
    interfaces: [
      {
        interface_id: 'CAN-PRIMARY',
        type: 'CAN',
        physical_layer: 'ISO 11898',
        data_rate: '1 Mbps',
        redundant: true
      },
      {
        interface_id: 'ETHERNET-AVIONICS',
        type: 'ETHERNET',
        physical_layer: '802.3',
        data_rate: '1 Gbps',
        redundant: false
      }
    ],
    protocols: [
      {
        protocol_name: 'ARINC 825',
        version: '1.0',
        layer: 'APPLICATION',
        specification: 'ARINC-825'
      },
      {
        protocol_name: 'AFDX',
        version: '2.0',
        layer: 'DATA_LINK',
        specification: 'ARINC-664P7'
      }
    ]
  },

  // Safety
  safety: {
    criticality: 'DAL_A',
    watchdog: true,
    redundancy: 'TRIPLE',
    self_test: {
      enabled: true,
      tests: {
        ram_test: true,
        flash_test: true,
        peripheral_test: true,
        communication_test: true
      },
      frequency: 'BOOT',
      interval_seconds: 60
    },
    fault_handling: {
      strategy: 'SAFE_STATE',
      safe_state_description: 'Transfer control to backup FCC, maintain level flight'
    }
  },

  // Deployment
  deployment: {
    method: 'CAN',
    bootloader: {
      secure: true,
      rollback_protection: true,
      signature_verification: true
    },
    update_policy: {
      auto_update: false,
      require_approval: true,
      rollback_on_failure: true,
      max_retry_attempts: 3
    }
  },

  // Diagnostics
  diagnostics: {
    dtc_enabled: true,
    dtc_codes: [
      {
        dtc_code: 'FCC-E001',
        description: 'CAN bus communication failure',
        severity: 'CRITICAL',
        action: 'Switch to backup communication path'
      },
      {
        dtc_code: 'FCC-W001',
        description: 'Sensor data quality degraded',
        severity: 'WARNING',
        action: 'Monitor sensor health, prepare for redundancy activation'
      }
    ],
    logging: {
      level: 'INFO',
      destinations: ['CAN', 'ETHERNET', 'FLASH']
    },
    telemetry: {
      enabled: true,
      metrics: [
        {
          metric_name: 'cpu_usage_percent',
          type: 'GAUGE',
          unit: 'percent',
          threshold: {
            warning: 80,
            critical: 95
          }
        },
        {
          metric_name: 'memory_usage_percent',
          type: 'GAUGE',
          unit: 'percent',
          threshold: {
            warning: 85,
            critical: 95
          }
        },
        {
          metric_name: 'flight_hours',
          type: 'COUNTER',
          unit: 'hours'
        },
        {
          metric_name: 'control_loop_cycles',
          type: 'COUNTER',
          unit: 'cycles'
        }
      ],
      reporting_interval_seconds: 60
    }
  },

  // Metadata
  created_date: '2025-01-10T00:00:00Z',
  last_modified_date: '2025-10-16T00:00:00Z',
  owner: 'flight-controls-team@ideale-eu.org',
  documentation_uri: 'https://docs.ideale-eu.org/fcc-hardware',

  // Relationships
  parent_prd: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/LCC-LINKAGES-CONTROL-COMMUNICATIONS/PRD.md'
};

// ============================================================================
// 3. PREDICTIVE MAINTENANCE AI MODEL
// ============================================================================

export const predictiveMaintenanceAI: AIModel = {
  // Identification
  model_id: 'AI-PREDMAINT-001',
  utcs_ref: 'UTCS-IIS/AI-PREDMAINT-001@1.2.0',
  identification: {
    name: 'Actuator Failure Prediction Model',
    version: '1.2.0',
    type: 'ANOMALY_DETECTION',
    domain: 'IIS', // Information, Intelligence, Systems
    description: 'LSTM-based model for predicting actuator failures 72 hours in advance'
  },

  // Framework
  framework: {
    name: 'TensorFlow',
    version: '2.15.0'
  },

  // Architecture
  architecture: {
    type: 'LSTM-Autoencoder',
    parameters_count: 1250000,
    layers: 12,
    input_shape: [100, 20], // 100 timesteps, 20 features
    output_shape: [1], // Anomaly score
    diagram_uri: 's3://ideale-models/predmaint/architecture-diagram.png'
  },

  // Training
  training: {
    training_id: 'TRAIN-PREDMAINT-20250915',
    dataset: {
      name: 'Flight Control Actuator Sensor Data',
      version: '2.0',
      size_samples: 50000,
      split: {
        train_percent: 70,
        val_percent: 15,
        test_percent: 15
      },
      data_quality: {
        completeness_percent: 98.5,
        duplicates_removed: 250,
        outliers_handled: 120
      },
      provenance: 's3://ideale-datasets/actuator-data-v2',
      license: 'Internal Use Only'
    },
    hyperparameters: {
      learning_rate: 0.001,
      dropout: 0.2,
      lstm_units: 128,
      batch_size: 32,
      epochs: 100
    },
    training_config: {
      epochs: 100,
      batch_size: 32,
      learning_rate: 0.001,
      optimizer: 'Adam',
      loss_function: 'MSE'
    },
    compute: {
      hardware: 'GPU',
      device_count: 4,
      training_time_hours: 6.5
    },
    reproducibility: {
      random_seed: 42,
      environment_hash: 'sha256:env123...',
      requirements_file: 's3://ideale-models/predmaint/requirements.txt'
    },
    experiment_tracking: {
      platform: 'MLflow',
      experiment_id: 'exp-predmaint-2025',
      run_id: 'run-20250915-001'
    }
  },

  // Evaluation
  evaluation: {
    evaluation_id: 'EVAL-PREDMAINT-20250920',
    evaluation_date: '2025-09-20T12:00:00Z',
    metrics: {
      precision: 0.94,
      recall: 0.91,
      f1_score: 0.925,
      auc_roc: 0.96
    },
    inference_performance: {
      latency_ms_p50: 15,
      latency_ms_p95: 28,
      latency_ms_p99: 35,
      throughput_samples_per_second: 100
    },
    resource_usage: {
      memory_mb: 512,
      cpu_percent: 25,
      gpu_utilization_percent: 40
    },
    test_results: {
      total_samples: 7500,
      correct_predictions: 7200,
      accuracy_percent: 96
    }
  },

  // Artifacts
  artifacts: {
    model_file: 's3://ideale-models/predmaint/v1.2.0/model.pb',
    weights_file: 's3://ideale-models/predmaint/v1.2.0/weights.h5',
    config_file: 's3://ideale-models/predmaint/v1.2.0/config.json',
    checksum: {
      sha256: 'model123abc...'
    },
    size_mb: 48
  },

  // Deployment
  deployment: {
    deployment_id: 'DEPLOY-AI-EDGE-001',
    target: 'EDGE_DEVICE',
    optimization: {
      quantization: '8bit',
      pruning: false,
      distillation: false,
      optimized_for: 'LATENCY'
    },
    versioning: {
      strategy: 'CANARY',
      rollback_enabled: true
    },
    edge_deployment: {
      target_hardware: 'NXP i.MX RT1170',
      runtime: 'TensorFlow Lite',
      model_format: 'TFLite',
      optimizations: {
        quantized: true,
        pruned: false,
        compiled: true
      },
      size_mb: 12,
      inference_time_ms: 15,
      power_consumption_mw: 50
    }
  },

  // Monitoring
  monitoring: {
    monitoring_enabled: true,
    drift_detection: {
      enabled: true,
      method: 'PSI',
      threshold: 0.2,
      last_check: '2025-10-16T14:00:00Z',
      status: 'STABLE'
    },
    performance_tracking: {
      metrics: ['precision', 'recall', 'f1_score'],
      alerting_thresholds: {
        precision: { warning: 0.85, critical: 0.80 },
        recall: { warning: 0.85, critical: 0.80 },
        f1_score: { warning: 0.85, critical: 0.80 }
      }
    },
    data_quality: {
      null_rate_threshold: 0.05,
      outlier_detection: true
    },
    audit_trail: [
      {
        timestamp: '2025-10-16T10:00:00Z',
        user: 'ml-ops-system',
        action: 'DEPLOYMENT',
        details: { version: '1.2.0', environment: 'production-edge' }
      }
    ]
  },

  // Explainability
  explainability: {
    method: 'SHAP',
    global_explanations: {
      feature_importance: [
        { feature_name: 'vibration_rms', importance_score: 0.35 },
        { feature_name: 'temperature_celsius', importance_score: 0.25 },
        { feature_name: 'current_draw_ma', importance_score: 0.20 },
        { feature_name: 'position_error_deg', importance_score: 0.12 },
        { feature_name: 'response_time_ms', importance_score: 0.08 }
      ]
    },
    local_explanations_available: true,
    visualization_uri: 's3://ideale-models/predmaint/shap-analysis.html'
  },

  // Ethics
  ethics: {
    assessment_id: 'ETHICS-PREDMAINT-001',
    assessment_date: '2025-09-25T00:00:00Z',
    bias_analysis: {
      tested: true,
      protected_attributes: [],
      fairness_metrics: {},
      bias_detected: false
    },
    privacy: {
      pii_present: false,
      anonymization_applied: true,
      differential_privacy: false
    },
    transparency: {
      model_card_uri: 's3://ideale-models/predmaint/model-card.md',
      data_sheet_uri: 's3://ideale-datasets/actuator-data-sheet.md'
    },
    regulatory_compliance: {
      gdpr: true,
      ccpa: true,
      ai_act: true
    },
    human_oversight: {
      required: true,
      level: 'PARTIAL'
    }
  },

  // Metadata
  created_date: '2025-08-01T00:00:00Z',
  last_modified_date: '2025-10-01T00:00:00Z',
  owner: 'ai-ml-team@ideale-eu.org',
  maintainers: ['data-scientist@ideale-eu.org'],
  documentation_uri: 'https://docs.ideale-eu.org/ai-predmaint',

  // Relationships
  parent_prd: '02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/IIS-INFORMATION-INTELLIGENCE-SYSTEMS/PRD.md'
};

// To be continued in part 2...
