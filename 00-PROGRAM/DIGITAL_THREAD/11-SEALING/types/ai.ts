/**
 * SEALING - AI Lifecycle Type Definitions
 * 
 * Comprehensive data structures for AI/ML models including training,
 * evaluation, deployment, monitoring, and ethics assessment.
 */

// ============================================================================
// Core Identification
// ============================================================================

export interface AIIdentification {
  name: string;
  version: string;
  type: 'CLASSIFICATION' | 'REGRESSION' | 'CLUSTERING' | 'ANOMALY_DETECTION' | 'FORECASTING' | 'RECOMMENDATION' | 'NLP' | 'COMPUTER_VISION' | 'REINFORCEMENT_LEARNING';
  domain: string; // e.g., 'IIS', 'EDI', 'AAA'
  description?: string;
}

// ============================================================================
// Framework and Architecture
// ============================================================================

export interface Framework {
  name: 'TensorFlow' | 'PyTorch' | 'JAX' | 'Scikit-learn' | 'XGBoost' | 'Keras' | 'ONNX';
  version: string;
}

export interface ModelArchitecture {
  type: string; // e.g., 'CNN', 'RNN', 'LSTM', 'Transformer', 'Random Forest'
  parameters_count: number;
  layers: number;
  input_shape: number[] | string;
  output_shape: number[] | string;
  diagram_uri?: string;
}

// ============================================================================
// Training
// ============================================================================

export interface Dataset {
  name: string;
  version: string;
  size_samples: number;
  split: {
    train_percent: number;
    val_percent: number;
    test_percent: number;
  };
  data_quality: {
    completeness_percent: number;
    duplicates_removed: number;
    outliers_handled: number;
  };
  provenance: string; // URI to data source
  license: string;
}

export interface TrainingInfo {
  training_id: string;
  dataset: Dataset;
  hyperparameters: Record<string, any>;
  training_config: {
    epochs: number;
    batch_size: number;
    learning_rate: number;
    optimizer: string;
    loss_function: string;
  };
  compute: {
    hardware: 'CPU' | 'GPU' | 'TPU' | 'NPU';
    device_count: number;
    training_time_hours: number;
  };
  reproducibility: {
    random_seed: number;
    environment_hash: string;
    requirements_file: string;
  };
  experiment_tracking?: {
    platform: 'MLflow' | 'Weights&Biases' | 'TensorBoard' | 'Neptune';
    experiment_id: string;
    run_id: string;
  };
}

// ============================================================================
// Evaluation
// ============================================================================

export interface PerformanceMetrics {
  // Classification metrics
  precision?: number;
  recall?: number;
  f1_score?: number;
  accuracy?: number;
  auc_roc?: number;
  
  // Regression metrics
  mse?: number;
  rmse?: number;
  mae?: number;
  r2_score?: number;
  
  // Custom metrics
  custom_metrics?: Record<string, number>;
}

export interface InferencePerformance {
  latency_ms_p50: number;
  latency_ms_p95: number;
  latency_ms_p99: number;
  throughput_samples_per_second: number;
}

export interface ResourceUsage {
  memory_mb: number;
  cpu_percent: number;
  gpu_utilization_percent?: number;
}

export interface EvaluationInfo {
  evaluation_id: string;
  evaluation_date: string;
  metrics: PerformanceMetrics;
  inference_performance: InferencePerformance;
  resource_usage: ResourceUsage;
  test_results: {
    total_samples: number;
    correct_predictions: number;
    accuracy_percent: number;
  };
  confusion_matrix?: number[][];
}

// ============================================================================
// Artifacts
// ============================================================================

export interface ModelArtifacts {
  model_file: string; // URI to model file
  weights_file?: string;
  config_file: string;
  checksum: {
    sha256: string;
  };
  size_mb: number;
}

// ============================================================================
// Deployment
// ============================================================================

export interface ServingInfo {
  framework: 'TensorFlow Serving' | 'TorchServe' | 'ONNX Runtime' | 'Triton' | 'KServe';
  endpoint?: string;
  scaling: {
    min_replicas: number;
    max_replicas: number;
    target_cpu_percent?: number;
  };
}

export interface EdgeDeployment {
  target_hardware: string; // e.g., 'NXP i.MX RT1170', 'NVIDIA Jetson Nano'
  runtime: 'TensorFlow Lite' | 'ONNX Runtime' | 'TVM' | 'Edge TPU';
  model_format: 'TFLite' | 'ONNX' | 'TensorRT' | 'CoreML';
  optimizations: {
    quantized: boolean;
    pruned: boolean;
    compiled: boolean;
  };
  size_mb: number;
  inference_time_ms: number;
  power_consumption_mw: number;
}

export interface DeploymentInfo {
  deployment_id: string;
  target: 'CLOUD' | 'EDGE_DEVICE' | 'ON_PREMISE' | 'HYBRID';
  serving?: ServingInfo;
  optimization?: {
    quantization: '8bit' | '16bit' | 'mixed';
    pruning: boolean;
    distillation: boolean;
    optimized_for: 'LATENCY' | 'THROUGHPUT' | 'MEMORY' | 'ACCURACY';
  };
  versioning: {
    strategy: 'BLUE_GREEN' | 'CANARY' | 'ROLLING' | 'SHADOW';
    rollback_enabled: boolean;
  };
  edge_deployment?: EdgeDeployment;
}

// ============================================================================
// Monitoring
// ============================================================================

export interface DriftDetection {
  enabled: boolean;
  method: 'KS' | 'PSI' | 'KL_DIVERGENCE' | 'WASSERSTEIN';
  threshold: number;
  last_check: string;
  status: 'STABLE' | 'WARNING' | 'DRIFT_DETECTED';
}

export interface AuditEntry {
  timestamp: string;
  user: string;
  action: 'PREDICTION' | 'RETRAINING' | 'DEPLOYMENT' | 'CONFIGURATION_CHANGE';
  details: Record<string, any>;
}

export interface MonitoringInfo {
  monitoring_enabled: boolean;
  drift_detection?: DriftDetection;
  performance_tracking: {
    metrics: string[];
    alerting_thresholds: Record<string, {
      warning: number;
      critical: number;
    }>;
  };
  data_quality?: {
    null_rate_threshold: number;
    outlier_detection: boolean;
  };
  audit_trail: AuditEntry[];
}

// ============================================================================
// Explainability
// ============================================================================

export interface FeatureImportance {
  feature_name: string;
  importance_score: number;
}

export interface ExplainabilityInfo {
  method: 'SHAP' | 'LIME' | 'INTEGRATED_GRADIENTS' | 'ATTENTION' | 'NONE';
  global_explanations?: {
    feature_importance: FeatureImportance[];
  };
  local_explanations_available: boolean;
  visualization_uri?: string;
}

// ============================================================================
// Ethics and Compliance
// ============================================================================

export interface BiasAnalysis {
  tested: boolean;
  protected_attributes: string[];
  fairness_metrics: Record<string, number>;
  bias_detected: boolean;
  mitigation_applied?: string;
}

export interface PrivacyInfo {
  pii_present: boolean;
  anonymization_applied: boolean;
  differential_privacy: boolean;
  privacy_budget?: number;
}

export interface EthicsInfo {
  assessment_id: string;
  assessment_date: string;
  bias_analysis: BiasAnalysis;
  privacy: PrivacyInfo;
  transparency: {
    model_card_uri: string;
    data_sheet_uri: string;
  };
  regulatory_compliance: {
    gdpr: boolean;
    ccpa: boolean;
    ai_act: boolean;
  };
  human_oversight: {
    required: boolean;
    level: 'FULL' | 'PARTIAL' | 'NONE';
  };
}

// ============================================================================
// Main AI Model Interface
// ============================================================================

export interface AIModel {
  // Identification
  model_id: string;
  utcs_ref: string; // e.g., "UTCS-IIS/AI-PREDMAINT-001@1.2.0"
  identification: AIIdentification;

  // Framework and Architecture
  framework: Framework;
  architecture: ModelArchitecture;

  // Training
  training: TrainingInfo;

  // Evaluation
  evaluation: EvaluationInfo;

  // Artifacts
  artifacts: ModelArtifacts;

  // Deployment
  deployment: DeploymentInfo;

  // Monitoring
  monitoring: MonitoringInfo;

  // Explainability
  explainability?: ExplainabilityInfo;

  // Ethics
  ethics?: EthicsInfo;

  // Metadata
  created_date: string;
  last_modified_date: string;
  owner: string;
  maintainers?: string[];
  documentation_uri?: string;

  // Relationships
  parent_prd?: string; // Reference to PRD document
  related_models?: string[]; // Other model IDs
  supersedes?: string; // Previous version model ID
}

// ============================================================================
// Helper Functions
// ============================================================================

export function calculateModelComplexity(model: AIModel): {
  parameters: number;
  layers: number;
  complexity_score: number;
} {
  const complexity_score = (model.architecture.parameters_count / 1000000) * model.architecture.layers;
  return {
    parameters: model.architecture.parameters_count,
    layers: model.architecture.layers,
    complexity_score
  };
}

export function validateAIModel(model: AIModel): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!model.model_id) errors.push('model_id is required');
  if (!model.utcs_ref) errors.push('utcs_ref is required');
  if (!model.identification?.name) errors.push('identification.name is required');
  if (!model.training?.training_id) errors.push('training.training_id is required');
  if (!model.evaluation?.evaluation_id) errors.push('evaluation.evaluation_id is required');
  if (!model.artifacts?.model_file) errors.push('artifacts.model_file is required');

  return {
    valid: errors.length === 0,
    errors
  };
}

export function detectDrift(model: AIModel): boolean {
  return model.monitoring?.drift_detection?.status === 'DRIFT_DETECTED' || false;
}
