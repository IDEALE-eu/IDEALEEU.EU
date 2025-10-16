/**
 * SEALING - Software, Embedded, AI Lifecycle, Integrated Network, Governance
 * Comprehensive type definitions for software and AI lifecycle management
 */

// ============================================================================
// SOFTWARE LIFECYCLE TYPES
// ============================================================================

export type SoftwareType =
  | 'APPLICATION'
  | 'LIBRARY'
  | 'FIRMWARE'
  | 'MIDDLEWARE'
  | 'DRIVER'
  | 'OPERATING_SYSTEM'
  | 'MICROSERVICE'
  | 'CONTAINER'
  | 'SERVERLESS'

export type DevelopmentStage =
  | 'DESIGN'
  | 'IMPLEMENTATION'
  | 'TESTING'
  | 'INTEGRATION'
  | 'DEPLOYMENT'
  | 'MAINTENANCE'
  | 'DECOMMISSION'

export type CriticalityLevel =
  | 'DAL_A' // Catastrophic failure
  | 'DAL_B' // Hazardous/Severe-Major
  | 'DAL_C' // Major
  | 'DAL_D' // Minor
  | 'DAL_E' // No safety effect
  | 'CRITICAL'
  | 'HIGH'
  | 'MEDIUM'
  | 'LOW'

export interface SoftwarePackage {
  package_id: string
  name: string
  version: string
  type: SoftwareType
  stage: DevelopmentStage
  criticality: CriticalityLevel
  utcs_ref: string
  created_at: string
  updated_at: string
  metadata: {
    description: string
    language: string
    framework?: string
    runtime?: string
    dependencies: SoftwareDependency[]
    repo_url?: string
    commit_sha?: string
    branch?: string
    tags?: string[]
  }
  lifecycle: SoftwareLifecycle
  sbom: SBOM
  security: SecurityProfile
  quality: QualityMetrics
  compliance: ComplianceStatus
}

export interface SoftwareDependency {
  name: string
  version: string
  type: 'DIRECT' | 'TRANSITIVE'
  license: string
  vulnerabilities: Vulnerability[]
}

export interface SoftwareLifecycle {
  current_stage: DevelopmentStage
  stages: {
    design?: StageMetadata
    implementation?: StageMetadata
    testing?: StageMetadata
    integration?: StageMetadata
    deployment?: StageMetadata
    maintenance?: StageMetadata
  }
  releases: SoftwareRelease[]
}

export interface StageMetadata {
  started_at: string
  completed_at?: string
  status: 'IN_PROGRESS' | 'COMPLETED' | 'BLOCKED' | 'SKIPPED'
  artifacts: string[]
  approvals: Approval[]
  issues: Issue[]
}

export interface SoftwareRelease {
  version: string
  release_date: string
  type: 'MAJOR' | 'MINOR' | 'PATCH' | 'HOTFIX'
  commit_sha: string
  artifacts: ReleaseArtifact[]
  changelog: string
  breaking_changes?: string[]
  deprecations?: string[]
}

export interface ReleaseArtifact {
  name: string
  type: 'BINARY' | 'SOURCE' | 'CONTAINER' | 'PACKAGE'
  url: string
  checksum: string
  signature: string
  size_bytes: number
}

// ============================================================================
// SBOM (Software Bill of Materials) TYPES
// ============================================================================

export interface SBOM {
  spec_version: string // CycloneDX, SPDX
  format: 'CYCLONEDX' | 'SPDX'
  generated_at: string
  components: SBOMComponent[]
  licenses: LicenseInfo[]
  supplier: string
  author: string
}

export interface SBOMComponent {
  bom_ref: string
  type: 'APPLICATION' | 'LIBRARY' | 'FRAMEWORK' | 'CONTAINER' | 'FILE'
  name: string
  version: string
  purl?: string // Package URL
  cpe?: string // Common Platform Enumeration
  licenses: string[]
  hashes: {
    algorithm: string
    value: string
  }[]
  dependencies: string[] // References to other bom_refs
  properties?: Record<string, string>
}

export interface LicenseInfo {
  id: string
  name: string
  url?: string
  text?: string
  compatibility: 'PERMISSIVE' | 'COPYLEFT' | 'PROPRIETARY' | 'UNKNOWN'
}

// ============================================================================
// SECURITY TYPES
// ============================================================================

export interface SecurityProfile {
  security_level: 'CLASSIFIED' | 'SECRET' | 'CONFIDENTIAL' | 'PUBLIC'
  threats: ThreatAnalysis[]
  vulnerabilities: Vulnerability[]
  scans: SecurityScan[]
  certifications: SecurityCertification[]
  access_control: AccessControl
}

export interface ThreatAnalysis {
  threat_id: string
  category: 'CONFIDENTIALITY' | 'INTEGRITY' | 'AVAILABILITY' | 'AUTHENTICATION' | 'AUTHORIZATION'
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  description: string
  mitigation: string
  residual_risk: string
  status: 'OPEN' | 'MITIGATED' | 'ACCEPTED' | 'TRANSFERRED'
}

export interface Vulnerability {
  cve_id?: string
  cwe_id?: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'INFO'
  cvss_score?: number
  description: string
  affected_versions: string[]
  fixed_version?: string
  published_date: string
  discovered_date: string
  remediation: string
  status: 'OPEN' | 'IN_PROGRESS' | 'FIXED' | 'WONT_FIX' | 'FALSE_POSITIVE'
}

export interface SecurityScan {
  scan_id: string
  type: 'SAST' | 'DAST' | 'IAST' | 'SCA' | 'CONTAINER' | 'SECRETS' | 'LICENSE'
  tool: string
  version: string
  executed_at: string
  duration_seconds: number
  findings: SecurityFinding[]
  summary: {
    critical: number
    high: number
    medium: number
    low: number
    info: number
  }
}

export interface SecurityFinding {
  finding_id: string
  rule_id: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'INFO'
  title: string
  description: string
  file_path?: string
  line_number?: number
  code_snippet?: string
  recommendation: string
  status: 'NEW' | 'TRIAGED' | 'RESOLVED' | 'IGNORED'
}

export interface SecurityCertification {
  cert_id: string
  standard: 'ISO_27001' | 'SOC2' | 'FIPS_140' | 'COMMON_CRITERIA' | 'DO_178C' | 'IEC_62443'
  level?: string
  issued_by: string
  issued_date: string
  expiry_date?: string
  scope: string
  certificate_url?: string
}

export interface AccessControl {
  authentication: 'NONE' | 'BASIC' | 'TOKEN' | 'OAUTH2' | 'SAML' | 'MTLS' | 'BIOMETRIC'
  authorization: 'NONE' | 'RBAC' | 'ABAC' | 'MAC' | 'DAC'
  encryption_at_rest: boolean
  encryption_in_transit: boolean
  key_management: 'SOFTWARE' | 'HSM' | 'KMS'
}

// ============================================================================
// QUALITY METRICS TYPES
// ============================================================================

export interface QualityMetrics {
  code_coverage: CodeCoverage
  static_analysis: StaticAnalysis
  complexity: ComplexityMetrics
  maintainability: MaintainabilityIndex
  technical_debt: TechnicalDebt
  test_results: TestResults
}

export interface CodeCoverage {
  lines_covered: number
  lines_total: number
  coverage_percent: number
  branches_covered: number
  branches_total: number
  branch_coverage_percent: number
  functions_covered: number
  functions_total: number
  function_coverage_percent: number
}

export interface StaticAnalysis {
  tool: string
  version: string
  executed_at: string
  issues: {
    blocker: number
    critical: number
    major: number
    minor: number
    info: number
  }
  code_smells: number
  bugs: number
  vulnerabilities: number
  duplicated_lines_percent: number
}

export interface ComplexityMetrics {
  cyclomatic_complexity: number
  cognitive_complexity: number
  halstead_metrics?: {
    volume: number
    difficulty: number
    effort: number
  }
}

export interface MaintainabilityIndex {
  score: number // 0-100
  grade: 'A' | 'B' | 'C' | 'D' | 'F'
  comment_ratio: number
  average_lines_per_function: number
}

export interface TechnicalDebt {
  debt_ratio: number
  debt_minutes: number
  sqale_rating: 'A' | 'B' | 'C' | 'D' | 'E'
  remediation_effort_minutes: number
}

export interface TestResults {
  total_tests: number
  passed: number
  failed: number
  skipped: number
  duration_seconds: number
  test_suites: TestSuite[]
}

export interface TestSuite {
  name: string
  tests: number
  passed: number
  failed: number
  skipped: number
  duration_seconds: number
  test_cases: TestCase[]
}

export interface TestCase {
  name: string
  status: 'PASSED' | 'FAILED' | 'SKIPPED' | 'ERROR'
  duration_seconds: number
  error_message?: string
  stack_trace?: string
}

// ============================================================================
// COMPLIANCE TYPES
// ============================================================================

export interface ComplianceStatus {
  standards: ComplianceStandard[]
  policies: PolicyCompliance[]
  audits: ComplianceAudit[]
  traceability: TraceabilityMatrix
}

export interface ComplianceStandard {
  standard: string // DO-178C, ISO 26262, IEC 61508, etc.
  level: string
  requirements: ComplianceRequirement[]
  coverage_percent: number
  status: 'COMPLIANT' | 'PARTIAL' | 'NON_COMPLIANT' | 'NOT_APPLICABLE'
}

export interface ComplianceRequirement {
  req_id: string
  description: string
  verification_method: 'INSPECTION' | 'ANALYSIS' | 'TEST' | 'DEMONSTRATION'
  verification_status: 'VERIFIED' | 'PARTIAL' | 'NOT_VERIFIED'
  evidence: string[]
  artifacts: string[]
}

export interface PolicyCompliance {
  policy_id: string
  policy_name: string
  category: 'SECURITY' | 'PRIVACY' | 'LICENSING' | 'QUALITY' | 'OPERATIONAL'
  rules: PolicyRule[]
  compliance_score: number
  violations: PolicyViolation[]
}

export interface PolicyRule {
  rule_id: string
  description: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  status: 'PASS' | 'FAIL' | 'WARNING' | 'NOT_APPLICABLE'
}

export interface PolicyViolation {
  violation_id: string
  rule_id: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  description: string
  location?: string
  remediation: string
  status: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED' | 'WAIVED'
}

export interface ComplianceAudit {
  audit_id: string
  type: 'INTERNAL' | 'EXTERNAL' | 'REGULATORY'
  auditor: string
  audit_date: string
  scope: string
  findings: AuditFinding[]
  recommendations: string[]
  certification_status: 'CERTIFIED' | 'CONDITIONAL' | 'FAILED' | 'PENDING'
}

export interface AuditFinding {
  finding_id: string
  category: 'MAJOR' | 'MINOR' | 'OBSERVATION'
  description: string
  evidence: string[]
  corrective_action: string
  status: 'OPEN' | 'IN_PROGRESS' | 'CLOSED' | 'ACCEPTED'
}

export interface TraceabilityMatrix {
  requirements: TraceabilityItem[]
  coverage: {
    requirements_traced: number
    requirements_total: number
    coverage_percent: number
  }
}

export interface TraceabilityItem {
  req_id: string
  source: string
  description: string
  traced_to: {
    design: string[]
    code: string[]
    tests: string[]
    verification: string[]
  }
  bidirectional: boolean
}

// ============================================================================
// EMBEDDED SYSTEMS TYPES
// ============================================================================

export interface EmbeddedSystem {
  system_id: string
  name: string
  type: 'MICROCONTROLLER' | 'MICROPROCESSOR' | 'SOC' | 'FPGA' | 'ASIC' | 'DSP'
  hardware: HardwareProfile
  firmware: FirmwareProfile
  realtime: RealtimeProfile
  safety: SafetyProfile
  power: PowerProfile
  communications: CommunicationProfile[]
  diagnostics: DiagnosticsProfile
  boot: BootProfile
}

export interface HardwareProfile {
  architecture: 'ARM' | 'X86' | 'RISCV' | 'MIPS' | 'POWER' | 'CUSTOM'
  cpu_mhz: number
  cores: number
  ram_kb: number
  flash_kb: number
  eeprom_kb?: number
  peripherals: Peripheral[]
  gpio_pins: number
  watchdog: boolean
}

export interface Peripheral {
  type: 'UART' | 'SPI' | 'I2C' | 'CAN' | 'USB' | 'ETHERNET' | 'ADC' | 'DAC' | 'PWM' | 'TIMER'
  count: number
  configuration?: Record<string, unknown>
}

export interface FirmwareProfile {
  version: string
  build_date: string
  checksum: string
  signature: string
  size_bytes: number
  components: FirmwareComponent[]
  bootloader_version?: string
  update_method: 'OTA' | 'JTAG' | 'USB' | 'SD_CARD' | 'SERIAL'
  rollback_supported: boolean
}

export interface FirmwareComponent {
  name: string
  version: string
  type: 'RTOS' | 'DRIVER' | 'MIDDLEWARE' | 'APPLICATION' | 'BSP'
  memory_usage: MemoryUsage
  criticality: CriticalityLevel
}

export interface MemoryUsage {
  code_size_bytes: number
  static_ram_bytes: number
  stack_size_bytes: number
  heap_size_bytes?: number
}

export interface RealtimeProfile {
  rtos: string
  rtos_version: string
  scheduling_algorithm: 'PRIORITY' | 'ROUND_ROBIN' | 'EDF' | 'RATE_MONOTONIC'
  tasks: RealtimeTask[]
  worst_case_response_time_ms: number
  timing_analysis: TimingAnalysis
}

export interface RealtimeTask {
  task_id: string
  name: string
  priority: number
  period_ms?: number
  deadline_ms?: number
  wcet_ms: number // Worst Case Execution Time
  stack_size_bytes: number
  state: 'READY' | 'RUNNING' | 'BLOCKED' | 'SUSPENDED'
}

export interface TimingAnalysis {
  method: 'STATIC' | 'DYNAMIC' | 'HYBRID'
  analysis_date: string
  schedulability: 'SCHEDULABLE' | 'NOT_SCHEDULABLE' | 'UNKNOWN'
  cpu_utilization_percent: number
  slack_time_ms: number
}

export interface SafetyProfile {
  safety_integrity_level: 'ASIL_A' | 'ASIL_B' | 'ASIL_C' | 'ASIL_D' | 'SIL_1' | 'SIL_2' | 'SIL_3' | 'SIL_4' | 'NONE'
  failure_mode: string
  fault_detection: FaultDetection
  redundancy: RedundancyStrategy
  diagnostics_coverage_percent: number
}

export interface FaultDetection {
  mechanisms: ('CRC' | 'PARITY' | 'ECC' | 'WATCHDOG' | 'PLAUSIBILITY' | 'RANGE_CHECK' | 'TIMEOUT')[]
  detection_time_ms: number
  reaction: 'SAFE_STATE' | 'DEGRADED_MODE' | 'RESTART' | 'ALERT'
}

export interface RedundancyStrategy {
  type: 'NONE' | 'DUAL' | 'TRIPLE' | 'QUADRUPLE'
  voting: 'NONE' | '2oo2' | '2oo3' | '3oo4'
  diversity: 'HARDWARE' | 'SOFTWARE' | 'BOTH' | 'NONE'
}

export interface PowerProfile {
  voltage_v: number
  voltage_tolerance_percent: number
  modes: PowerMode[]
  current_consumption_ma: PowerConsumption
  battery_operated: boolean
  power_budget_mw: number
}

export interface PowerMode {
  mode: 'ACTIVE' | 'IDLE' | 'SLEEP' | 'DEEP_SLEEP' | 'SHUTDOWN'
  current_ma: number
  wake_time_ms: number
  peripherals_active: string[]
}

export interface PowerConsumption {
  typical_ma: number
  maximum_ma: number
  standby_ma: number
}

export interface CommunicationProfile {
  protocol: 'CAN' | 'CANFD' | 'LIN' | 'FLEXRAY' | 'ETHERNET' | 'RS485' | 'MODBUS' | 'PROFIBUS' | 'MQTT' | 'COAP'
  speed_bps: number
  mode: 'MASTER' | 'SLAVE' | 'PEER'
  encryption: boolean
  authentication: boolean
  message_definitions: MessageDefinition[]
}

export interface MessageDefinition {
  msg_id: string
  name: string
  direction: 'TX' | 'RX' | 'BOTH'
  period_ms?: number
  length_bytes: number
  signals: Signal[]
}

export interface Signal {
  name: string
  start_bit: number
  length_bits: number
  byte_order: 'LITTLE_ENDIAN' | 'BIG_ENDIAN'
  type: 'UNSIGNED' | 'SIGNED' | 'FLOAT' | 'ENUM'
  scale?: number
  offset?: number
  unit?: string
  min_value?: number
  max_value?: number
}

export interface DiagnosticsProfile {
  protocol: 'UDS' | 'OBD2' | 'J1939' | 'CUSTOM'
  dtcs: DiagnosticTroubleCode[]
  freeze_frames: boolean
  live_data: boolean
  routines: DiagnosticRoutine[]
}

export interface DiagnosticTroubleCode {
  code: string
  description: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  trigger_condition: string
  effects: string
  corrective_action: string
}

export interface DiagnosticRoutine {
  routine_id: string
  name: string
  type: 'READ' | 'WRITE' | 'CLEAR' | 'TEST'
  description: string
  parameters?: Record<string, unknown>
}

export interface BootProfile {
  stages: BootStage[]
  secure_boot: boolean
  verified_boot: boolean
  boot_time_ms: number
  recovery_mode: boolean
}

export interface BootStage {
  stage: number
  name: string
  duration_ms: number
  checksum_verification: boolean
  signature_verification: boolean
}

// ============================================================================
// AI LIFECYCLE TYPES
// ============================================================================

export interface AIModel {
  model_id: string
  name: string
  version: string
  type: 'CLASSIFICATION' | 'REGRESSION' | 'DETECTION' | 'SEGMENTATION' | 'NLP' | 'REINFORCEMENT' | 'GENERATIVE'
  framework: 'TENSORFLOW' | 'PYTORCH' | 'ONNX' | 'KERAS' | 'SCIKIT' | 'XGBOOST' | 'CUSTOM'
  domain: 'VISION' | 'NLP' | 'AUDIO' | 'TIME_SERIES' | 'MULTIMODAL'
  lifecycle: AILifecycle
  architecture: ModelArchitecture
  training: TrainingProfile
  evaluation: EvaluationMetrics
  deployment: DeploymentProfile
  monitoring: ModelMonitoring
  explainability: ExplainabilityProfile
  ethics: EthicsAssessment
}

export interface AILifecycle {
  current_stage: 'DESIGN' | 'TRAINING' | 'VALIDATION' | 'DEPLOYMENT' | 'MONITORING' | 'RETRAINING' | 'RETIRED'
  stages: {
    design?: AIStageMetadata
    training?: AIStageMetadata
    validation?: AIStageMetadata
    deployment?: AIStageMetadata
    monitoring?: AIStageMetadata
  }
  versions: ModelVersion[]
}

export interface AIStageMetadata {
  started_at: string
  completed_at?: string
  status: 'IN_PROGRESS' | 'COMPLETED' | 'FAILED'
  artifacts: ModelArtifact[]
  experiments: Experiment[]
}

export interface ModelVersion {
  version: string
  created_at: string
  model_uri: string
  metrics: Record<string, number>
  tags: string[]
  status: 'ACTIVE' | 'ARCHIVED' | 'DEPRECATED'
}

export interface ModelArtifact {
  type: 'MODEL_WEIGHTS' | 'TRAINING_DATA' | 'TEST_DATA' | 'CONFIG' | 'PREPROCESSING' | 'ONNX' | 'TFLITE'
  uri: string
  checksum: string
  size_bytes: number
  format: string
}

export interface Experiment {
  experiment_id: string
  name: string
  started_at: string
  completed_at?: string
  parameters: Record<string, unknown>
  metrics: Record<string, number>
  artifacts: string[]
  tags: string[]
}

export interface ModelArchitecture {
  architecture_type: string
  layers: number
  parameters: number
  trainable_parameters: number
  flops: number
  model_size_mb: number
  input_shape: number[]
  output_shape: number[]
  backbone?: string
  pretrained: boolean
}

export interface TrainingProfile {
  dataset: DatasetInfo
  hyperparameters: Hyperparameters
  training_time_hours: number
  compute_resources: ComputeResources
  data_augmentation: string[]
  regularization: string[]
  optimization: OptimizationStrategy
  convergence: ConvergenceMetrics
}

export interface DatasetInfo {
  name: string
  version: string
  size_samples: number
  splits: {
    train: number
    validation: number
    test: number
  }
  classes: number
  imbalance_ratio?: number
  source: string
  license: string
  data_drift_score?: number
}

export interface Hyperparameters {
  learning_rate: number
  batch_size: number
  epochs: number
  optimizer: string
  loss_function: string
  weight_decay?: number
  dropout?: number
  early_stopping?: boolean
  [key: string]: unknown
}

export interface ComputeResources {
  gpu_type?: string
  gpu_count: number
  cpu_cores: number
  memory_gb: number
  distributed: boolean
  framework_version: string
}

export interface OptimizationStrategy {
  method: 'SGD' | 'ADAM' | 'ADAMW' | 'RMSPROP' | 'ADAGRAD'
  learning_rate_schedule: 'CONSTANT' | 'STEP' | 'EXPONENTIAL' | 'COSINE' | 'CYCLIC'
  momentum?: number
  gradient_clipping?: number
}

export interface ConvergenceMetrics {
  converged: boolean
  final_loss: number
  best_epoch: number
  training_curve: TrainingPoint[]
}

export interface TrainingPoint {
  epoch: number
  train_loss: number
  val_loss: number
  train_metric?: number
  val_metric?: number
}

export interface EvaluationMetrics {
  accuracy?: number
  precision?: number
  recall?: number
  f1_score?: number
  auc_roc?: number
  confusion_matrix?: number[][]
  inference_time_ms: number
  throughput_samples_per_sec: number
  resource_usage: ResourceUsage
  robustness: RobustnessMetrics
}

export interface ResourceUsage {
  memory_mb: number
  cpu_percent: number
  gpu_percent?: number
  power_watts?: number
}

export interface RobustnessMetrics {
  adversarial_accuracy?: number
  noise_tolerance?: number
  out_of_distribution_score?: number
  calibration_error?: number
}

export interface DeploymentProfile {
  environment: 'CLOUD' | 'EDGE' | 'EMBEDDED' | 'MOBILE' | 'HYBRID'
  runtime: 'TENSORFLOW_SERVING' | 'TORCHSERVE' | 'ONNX_RUNTIME' | 'TENSORRT' | 'TFLITE' | 'CUSTOM'
  endpoint?: string
  instances: number
  auto_scaling: boolean
  optimization: ModelOptimization
  version_strategy: 'BLUE_GREEN' | 'CANARY' | 'ROLLING' | 'SHADOW'
}

export interface ModelOptimization {
  quantization?: 'INT8' | 'FP16' | 'MIXED'
  pruning?: boolean
  knowledge_distillation?: boolean
  optimization_level: 'NONE' | 'O1' | 'O2' | 'O3'
}

export interface ModelMonitoring {
  metrics: MonitoringMetric[]
  alerts: Alert[]
  drift_detection: DriftDetection
  performance_degradation: boolean
  incidents: Incident[]
}

export interface MonitoringMetric {
  name: string
  value: number
  threshold: number
  status: 'HEALTHY' | 'WARNING' | 'CRITICAL'
  timestamp: string
}

export interface Alert {
  alert_id: string
  severity: 'INFO' | 'WARNING' | 'CRITICAL'
  message: string
  timestamp: string
  resolved: boolean
}

export interface DriftDetection {
  data_drift_detected: boolean
  concept_drift_detected: boolean
  drift_score: number
  detection_method: 'KS_TEST' | 'CHI_SQUARE' | 'KL_DIVERGENCE' | 'PSI'
  last_checked: string
}

export interface Incident {
  incident_id: string
  type: 'PERFORMANCE' | 'DRIFT' | 'ERROR' | 'OUTAGE'
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  description: string
  detected_at: string
  resolved_at?: string
  root_cause?: string
  corrective_action?: string
}

export interface ExplainabilityProfile {
  method: 'LIME' | 'SHAP' | 'GRAD_CAM' | 'ATTENTION' | 'INTEGRATED_GRADIENTS' | 'COUNTERFACTUAL'
  global_explanations: string[]
  local_explanations_available: boolean
  feature_importance: FeatureImportance[]
  interpretability_score: number
}

export interface FeatureImportance {
  feature: string
  importance: number
  contribution: 'POSITIVE' | 'NEGATIVE'
}

export interface EthicsAssessment {
  fairness: FairnessMetrics
  bias: BiasAnalysis
  privacy: PrivacyCompliance
  transparency: TransparencyScore
  accountability: AccountabilityFramework
  environmental_impact: EnvironmentalImpact
}

export interface FairnessMetrics {
  demographic_parity?: number
  equalized_odds?: number
  equal_opportunity?: number
  disparate_impact?: number
  protected_attributes: string[]
  mitigation_strategies: string[]
}

export interface BiasAnalysis {
  bias_detected: boolean
  bias_type: 'SELECTION' | 'CONFIRMATION' | 'SAMPLING' | 'ALGORITHMIC' | 'NONE'
  affected_groups: string[]
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  mitigation: string
}

export interface PrivacyCompliance {
  pii_detected: boolean
  anonymization: boolean
  differential_privacy: boolean
  data_retention_days: number
  gdpr_compliant: boolean
  right_to_explanation: boolean
}

export interface TransparencyScore {
  score: number
  model_card_available: boolean
  documentation_quality: 'POOR' | 'FAIR' | 'GOOD' | 'EXCELLENT'
  decision_explainability: boolean
}

export interface AccountabilityFramework {
  responsible_party: string
  oversight_mechanism: string
  audit_trail: boolean
  version_control: boolean
  rollback_capability: boolean
}

export interface EnvironmentalImpact {
  training_energy_kwh: number
  co2_emissions_kg: number
  carbon_offset: boolean
  green_computing_practices: string[]
}

// ============================================================================
// NETWORK TYPES
// ============================================================================

export interface NetworkInfrastructure {
  network_id: string
  name: string
  type: 'LAN' | 'WAN' | 'VPN' | 'SDN' | 'MESH' | 'SATELLITE' | 'CELLULAR'
  topology: NetworkTopology
  security: NetworkSecurity
  performance: NetworkPerformance
  devices: NetworkDevice[]
  services: NetworkService[]
  monitoring: NetworkMonitoring
}

export interface NetworkTopology {
  type: 'STAR' | 'MESH' | 'RING' | 'BUS' | 'TREE' | 'HYBRID'
  subnets: Subnet[]
  routes: Route[]
  redundancy: 'NONE' | 'ACTIVE_PASSIVE' | 'ACTIVE_ACTIVE' | 'N+1'
}

export interface Subnet {
  subnet_id: string
  cidr: string
  vlan?: number
  gateway: string
  dns_servers: string[]
  dhcp_enabled: boolean
}

export interface Route {
  destination: string
  gateway: string
  interface: string
  metric: number
  type: 'STATIC' | 'DYNAMIC'
}

export interface NetworkSecurity {
  firewall: FirewallConfiguration
  ids_ips: IDSIPSConfiguration
  vpn: VPNConfiguration
  certificates: Certificate[]
  access_policies: AccessPolicy[]
  threat_intelligence: ThreatIntelligence
}

export interface FirewallConfiguration {
  type: 'STATEFUL' | 'STATELESS' | 'NGFW'
  rules: FirewallRule[]
  default_policy: 'ALLOW' | 'DENY'
  logging: boolean
}

export interface FirewallRule {
  rule_id: string
  priority: number
  source: string
  destination: string
  port: number | string
  protocol: 'TCP' | 'UDP' | 'ICMP' | 'ANY'
  action: 'ALLOW' | 'DENY' | 'LOG'
  enabled: boolean
}

export interface IDSIPSConfiguration {
  enabled: boolean
  mode: 'IDS' | 'IPS' | 'BOTH'
  signatures_version: string
  policies: string[]
  alerts: SecurityAlert[]
}

export interface SecurityAlert {
  alert_id: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  type: string
  source_ip: string
  destination_ip: string
  timestamp: string
  description: string
  action_taken: 'BLOCKED' | 'LOGGED' | 'ALERTED'
}

export interface VPNConfiguration {
  protocol: 'IPSEC' | 'OPENVPN' | 'WIREGUARD' | 'SSL_VPN'
  encryption: string
  authentication: string
  tunnels: VPNTunnel[]
}

export interface VPNTunnel {
  tunnel_id: string
  local_endpoint: string
  remote_endpoint: string
  status: 'UP' | 'DOWN'
  established_at?: string
  traffic_bytes: number
}

export interface Certificate {
  cert_id: string
  type: 'SSL_TLS' | 'CODE_SIGNING' | 'CLIENT' | 'ROOT_CA' | 'INTERMEDIATE_CA'
  subject: string
  issuer: string
  valid_from: string
  valid_until: string
  serial_number: string
  fingerprint: string
  key_size_bits: number
  algorithm: string
  status: 'VALID' | 'EXPIRED' | 'REVOKED' | 'PENDING'
}

export interface AccessPolicy {
  policy_id: string
  name: string
  type: 'INGRESS' | 'EGRESS' | 'INTERNAL'
  subjects: string[]
  resources: string[]
  actions: string[]
  conditions?: Record<string, unknown>
  effect: 'ALLOW' | 'DENY'
}

export interface ThreatIntelligence {
  feeds: ThreatFeed[]
  indicators: ThreatIndicator[]
  last_updated: string
}

export interface ThreatFeed {
  feed_id: string
  name: string
  source: string
  type: 'IP_REPUTATION' | 'MALWARE_HASH' | 'DOMAIN_BLACKLIST' | 'URL_FILTERING'
  updated_at: string
}

export interface ThreatIndicator {
  indicator_id: string
  type: 'IP' | 'DOMAIN' | 'URL' | 'HASH' | 'EMAIL'
  value: string
  threat_type: string
  confidence: number
  first_seen: string
  last_seen: string
}

export interface NetworkPerformance {
  bandwidth: BandwidthMetrics
  latency: LatencyMetrics
  packet_loss: number
  jitter_ms: number
  availability_percent: number
  sla_compliance: boolean
}

export interface BandwidthMetrics {
  capacity_mbps: number
  utilization_percent: number
  ingress_mbps: number
  egress_mbps: number
  peak_utilization_percent: number
}

export interface LatencyMetrics {
  average_ms: number
  p50_ms: number
  p95_ms: number
  p99_ms: number
  max_ms: number
}

export interface NetworkDevice {
  device_id: string
  name: string
  type: 'ROUTER' | 'SWITCH' | 'FIREWALL' | 'LOAD_BALANCER' | 'ACCESS_POINT' | 'GATEWAY'
  model: string
  firmware_version: string
  management_ip: string
  location: string
  interfaces: NetworkInterface[]
  status: 'ONLINE' | 'OFFLINE' | 'DEGRADED'
}

export interface NetworkInterface {
  interface_id: string
  name: string
  type: 'ETHERNET' | 'FIBER' | 'WIRELESS' | 'VIRTUAL'
  speed_mbps: number
  duplex: 'FULL' | 'HALF' | 'AUTO'
  status: 'UP' | 'DOWN'
  ip_address?: string
  mac_address: string
  statistics: InterfaceStatistics
}

export interface InterfaceStatistics {
  rx_bytes: number
  tx_bytes: number
  rx_packets: number
  tx_packets: number
  rx_errors: number
  tx_errors: number
  rx_drops: number
  tx_drops: number
}

export interface NetworkService {
  service_id: string
  name: string
  type: 'DNS' | 'DHCP' | 'NTP' | 'SYSLOG' | 'SNMP' | 'RADIUS' | 'LDAP'
  status: 'RUNNING' | 'STOPPED' | 'ERROR'
  endpoints: ServiceEndpoint[]
  dependencies: string[]
}

export interface ServiceEndpoint {
  protocol: string
  host: string
  port: number
  path?: string
  health_check: HealthCheck
}

export interface HealthCheck {
  status: 'HEALTHY' | 'UNHEALTHY' | 'UNKNOWN'
  last_check: string
  response_time_ms: number
  error_message?: string
}

export interface NetworkMonitoring {
  tools: MonitoringTool[]
  metrics: NetworkMetric[]
  events: NetworkEvent[]
  topology_map: string
}

export interface MonitoringTool {
  tool: 'NAGIOS' | 'ZABBIX' | 'PROMETHEUS' | 'DATADOG' | 'SPLUNK' | 'CUSTOM'
  version: string
  agents_deployed: number
}

export interface NetworkMetric {
  metric_name: string
  value: number
  unit: string
  timestamp: string
  device_id?: string
  interface_id?: string
}

export interface NetworkEvent {
  event_id: string
  type: 'LINK_UP' | 'LINK_DOWN' | 'CONFIGURATION_CHANGE' | 'AUTHENTICATION_FAILURE' | 'THRESHOLD_EXCEEDED'
  severity: 'INFO' | 'WARNING' | 'ERROR' | 'CRITICAL'
  device_id?: string
  timestamp: string
  description: string
  acknowledged: boolean
}

// ============================================================================
// GOVERNANCE TYPES
// ============================================================================

export interface GovernanceFramework {
  framework_id: string
  name: string
  version: string
  organization: string
  effective_date: string
  policies: GovernancePolicy[]
  risk_management: RiskManagement
  compliance_management: ComplianceManagement
  data_governance: DataGovernance
  change_management: ChangeManagement
  incident_management: IncidentManagement
  audit_trail: AuditTrail
}

export interface GovernancePolicy {
  policy_id: string
  name: string
  category: 'SECURITY' | 'PRIVACY' | 'QUALITY' | 'OPERATIONAL' | 'FINANCIAL' | 'LEGAL'
  description: string
  scope: string
  effective_date: string
  review_date: string
  owner: string
  approvers: string[]
  status: 'DRAFT' | 'ACTIVE' | 'UNDER_REVIEW' | 'ARCHIVED'
  controls: Control[]
  violations: Violation[]
}

export interface Control {
  control_id: string
  name: string
  type: 'PREVENTIVE' | 'DETECTIVE' | 'CORRECTIVE' | 'COMPENSATING'
  description: string
  implementation: string
  testing_frequency: 'CONTINUOUS' | 'DAILY' | 'WEEKLY' | 'MONTHLY' | 'QUARTERLY' | 'ANNUALLY'
  last_tested: string
  effectiveness: 'EFFECTIVE' | 'NEEDS_IMPROVEMENT' | 'INEFFECTIVE'
}

export interface Violation {
  violation_id: string
  detected_at: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  description: string
  responsible_party: string
  remediation_plan: string
  status: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED' | 'CLOSED'
}

export interface RiskManagement {
  methodology: 'NIST' | 'ISO_31000' | 'COSO' | 'OCTAVE' | 'FAIR'
  risk_appetite: 'AVERSE' | 'CAUTIOUS' | 'BALANCED' | 'OPEN' | 'SEEKING'
  risks: Risk[]
  risk_matrix: RiskMatrix
  mitigation_strategies: MitigationStrategy[]
}

export interface Risk {
  risk_id: string
  title: string
  category: 'STRATEGIC' | 'OPERATIONAL' | 'FINANCIAL' | 'COMPLIANCE' | 'REPUTATIONAL' | 'TECHNICAL'
  description: string
  likelihood: 'VERY_LOW' | 'LOW' | 'MEDIUM' | 'HIGH' | 'VERY_HIGH'
  impact: 'NEGLIGIBLE' | 'MINOR' | 'MODERATE' | 'MAJOR' | 'CATASTROPHIC'
  risk_score: number
  inherent_risk: number
  residual_risk: number
  owner: string
  status: 'IDENTIFIED' | 'ASSESSED' | 'MITIGATED' | 'ACCEPTED' | 'TRANSFERRED' | 'CLOSED'
  controls: string[]
  last_reviewed: string
}

export interface RiskMatrix {
  dimensions: number // 3x3, 4x4, 5x5
  thresholds: {
    low: number
    medium: number
    high: number
    critical: number
  }
  heat_map: RiskHeatMapItem[]
}

export interface RiskHeatMapItem {
  likelihood: string
  impact: string
  risk_count: number
  risk_ids: string[]
}

export interface MitigationStrategy {
  strategy_id: string
  risk_id: string
  type: 'AVOID' | 'REDUCE' | 'TRANSFER' | 'ACCEPT'
  description: string
  actions: MitigationAction[]
  cost_estimate: number
  effectiveness_percent: number
  status: 'PLANNED' | 'IN_PROGRESS' | 'IMPLEMENTED' | 'MONITORING'
}

export interface MitigationAction {
  action_id: string
  description: string
  responsible_party: string
  due_date: string
  completed_date?: string
  status: 'NOT_STARTED' | 'IN_PROGRESS' | 'COMPLETED' | 'BLOCKED'
}

export interface ComplianceManagement {
  frameworks: ComplianceFramework[]
  assessments: ComplianceAssessment[]
  gaps: ComplianceGap[]
  remediation_plan: RemediationPlan
}

export interface ComplianceFramework {
  framework: string
  version: string
  scope: string
  applicable_controls: number
  implemented_controls: number
  compliance_percentage: number
  last_assessment: string
  next_assessment: string
}

export interface ComplianceAssessment {
  assessment_id: string
  framework: string
  assessment_date: string
  assessor: string
  type: 'SELF' | 'INTERNAL' | 'EXTERNAL' | 'REGULATORY'
  findings: AssessmentFinding[]
  overall_status: 'COMPLIANT' | 'PARTIALLY_COMPLIANT' | 'NON_COMPLIANT'
  report_url?: string
}

export interface AssessmentFinding {
  finding_id: string
  control_id: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  description: string
  evidence: string[]
  recommendation: string
  status: 'OPEN' | 'IN_PROGRESS' | 'REMEDIATED' | 'ACCEPTED'
}

export interface ComplianceGap {
  gap_id: string
  control_id: string
  requirement: string
  current_state: string
  target_state: string
  gap_description: string
  priority: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  remediation_effort: 'LOW' | 'MEDIUM' | 'HIGH'
}

export interface RemediationPlan {
  plan_id: string
  gaps: string[]
  timeline: string
  budget: number
  milestones: Milestone[]
  progress_percent: number
}

export interface Milestone {
  milestone_id: string
  name: string
  description: string
  due_date: string
  completion_date?: string
  status: 'NOT_STARTED' | 'IN_PROGRESS' | 'COMPLETED' | 'DELAYED'
  deliverables: string[]
}

export interface DataGovernance {
  data_catalog: DataCatalog
  data_quality: DataQuality
  data_lineage: DataLineage
  data_privacy: DataPrivacy
  master_data_management: MasterDataManagement
}

export interface DataCatalog {
  datasets: Dataset[]
  total_datasets: number
  total_data_size_gb: number
  metadata_completeness_percent: number
}

export interface Dataset {
  dataset_id: string
  name: string
  description: string
  owner: string
  classification: 'PUBLIC' | 'INTERNAL' | 'CONFIDENTIAL' | 'RESTRICTED'
  sensitivity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  schema: DataSchema
  location: string
  size_gb: number
  record_count: number
  last_updated: string
  tags: string[]
}

export interface DataSchema {
  fields: DataField[]
  primary_key?: string[]
  foreign_keys?: ForeignKey[]
}

export interface DataField {
  name: string
  type: string
  nullable: boolean
  description?: string
  pii: boolean
  sensitive: boolean
  constraints?: string[]
}

export interface ForeignKey {
  field: string
  references_dataset: string
  references_field: string
}

export interface DataQuality {
  dimensions: DataQualityDimension[]
  overall_score: number
  issues: DataQualityIssue[]
  rules: DataQualityRule[]
}

export interface DataQualityDimension {
  dimension: 'ACCURACY' | 'COMPLETENESS' | 'CONSISTENCY' | 'TIMELINESS' | 'VALIDITY' | 'UNIQUENESS'
  score: number
  threshold: number
  status: 'PASS' | 'FAIL' | 'WARNING'
}

export interface DataQualityIssue {
  issue_id: string
  dataset_id: string
  field?: string
  dimension: string
  description: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  detected_at: string
  status: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED'
}

export interface DataQualityRule {
  rule_id: string
  name: string
  dataset_id: string
  field?: string
  rule_type: 'FORMAT' | 'RANGE' | 'UNIQUENESS' | 'COMPLETENESS' | 'REFERENTIAL_INTEGRITY'
  condition: string
  severity: 'ERROR' | 'WARNING' | 'INFO'
  enabled: boolean
}

export interface DataLineage {
  lineage_id: string
  dataset_id: string
  upstream: LineageNode[]
  downstream: LineageNode[]
  transformations: Transformation[]
  impact_analysis: ImpactAnalysis
}

export interface LineageNode {
  node_id: string
  type: 'SOURCE' | 'TRANSFORMATION' | 'SINK'
  name: string
  description: string
  level: number
}

export interface Transformation {
  transformation_id: string
  name: string
  type: 'ETL' | 'ELT' | 'STREAM' | 'BATCH'
  source_datasets: string[]
  target_dataset: string
  logic: string
  schedule?: string
  last_run: string
}

export interface ImpactAnalysis {
  upstream_dependencies: number
  downstream_dependents: number
  critical_paths: string[][]
  blast_radius: number
}

export interface DataPrivacy {
  regulations: PrivacyRegulation[]
  consent_management: ConsentManagement
  data_subject_rights: DataSubjectRights
  privacy_incidents: PrivacyIncident[]
}

export interface PrivacyRegulation {
  regulation: 'GDPR' | 'CCPA' | 'HIPAA' | 'PIPEDA' | 'LGPD'
  scope: string
  applicable: boolean
  compliance_status: 'COMPLIANT' | 'PARTIAL' | 'NON_COMPLIANT'
  last_assessment: string
}

export interface ConsentManagement {
  consent_required: boolean
  consent_records: ConsentRecord[]
  withdrawal_process: string
}

export interface ConsentRecord {
  consent_id: string
  data_subject_id: string
  purpose: string
  granted_at: string
  withdrawn_at?: string
  status: 'ACTIVE' | 'WITHDRAWN' | 'EXPIRED'
}

export interface DataSubjectRights {
  access: boolean
  rectification: boolean
  erasure: boolean // Right to be forgotten
  portability: boolean
  objection: boolean
  requests: DataSubjectRequest[]
}

export interface DataSubjectRequest {
  request_id: string
  type: 'ACCESS' | 'RECTIFICATION' | 'ERASURE' | 'PORTABILITY' | 'OBJECTION'
  data_subject_id: string
  submitted_at: string
  due_date: string
  completed_at?: string
  status: 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'REJECTED'
}

export interface PrivacyIncident {
  incident_id: string
  type: 'DATA_BREACH' | 'UNAUTHORIZED_ACCESS' | 'DATA_LOSS' | 'CONSENT_VIOLATION'
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  detected_at: string
  reported_to_authority: boolean
  affected_subjects: number
  mitigation: string
  status: 'OPEN' | 'INVESTIGATING' | 'RESOLVED' | 'CLOSED'
}

export interface MasterDataManagement {
  golden_records: GoldenRecord[]
  data_domains: DataDomain[]
  matching_rules: MatchingRule[]
  data_stewards: DataSteward[]
}

export interface GoldenRecord {
  record_id: string
  domain: string
  attributes: Record<string, unknown>
  source_records: SourceRecord[]
  confidence_score: number
  last_updated: string
}

export interface SourceRecord {
  source_system: string
  source_id: string
  attributes: Record<string, unknown>
  quality_score: number
}

export interface DataDomain {
  domain_id: string
  name: string
  description: string
  entities: string[]
  owner: string
  stewards: string[]
}

export interface MatchingRule {
  rule_id: string
  domain: string
  fields: string[]
  algorithm: 'EXACT' | 'FUZZY' | 'PHONETIC' | 'ML'
  threshold: number
  weight: number
}

export interface DataSteward {
  steward_id: string
  name: string
  email: string
  domains: string[]
  responsibilities: string[]
}

export interface ChangeManagement {
  changes: ChangeRequest[]
  change_board: ChangeAdvisoryBoard
  emergency_changes: EmergencyChange[]
  change_calendar: ChangeCalendar
}

export interface ChangeRequest {
  change_id: string
  title: string
  type: 'STANDARD' | 'NORMAL' | 'EMERGENCY'
  category: 'INFRASTRUCTURE' | 'APPLICATION' | 'CONFIGURATION' | 'SECURITY'
  priority: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  requester: string
  description: string
  justification: string
  impact_assessment: ImpactAssessment
  implementation_plan: string
  rollback_plan: string
  testing_plan: string
  requested_date: string
  scheduled_date?: string
  implementation_date?: string
  status: 'DRAFT' | 'PENDING_APPROVAL' | 'APPROVED' | 'REJECTED' | 'SCHEDULED' | 'IMPLEMENTED' | 'FAILED' | 'CANCELLED'
  approvals: Approval[]
}

export interface ImpactAssessment {
  scope: string
  affected_systems: string[]
  affected_users: number
  downtime_required: boolean
  estimated_downtime_minutes?: number
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL'
  mitigation_plan: string
}

export interface Approval {
  approver: string
  role: string
  decision: 'APPROVED' | 'REJECTED' | 'PENDING'
  timestamp?: string
  comments?: string
}

export interface ChangeAdvisoryBoard {
  members: BoardMember[]
  meeting_schedule: string
  next_meeting: string
  voting_threshold: number
}

export interface BoardMember {
  member_id: string
  name: string
  role: string
  voting_rights: boolean
}

export interface EmergencyChange {
  change_id: string
  reason: string
  approved_by: string
  implemented_at: string
  post_implementation_review_due: string
}

export interface ChangeCalendar {
  scheduled_changes: ScheduledChange[]
  blackout_periods: BlackoutPeriod[]
  maintenance_windows: MaintenanceWindow[]
}

export interface ScheduledChange {
  change_id: string
  title: string
  scheduled_start: string
  scheduled_end: string
  systems: string[]
  status: 'SCHEDULED' | 'IN_PROGRESS' | 'COMPLETED' | 'CANCELLED'
}

export interface BlackoutPeriod {
  period_id: string
  name: string
  start_date: string
  end_date: string
  reason: string
  exemptions: string[]
}

export interface MaintenanceWindow {
  window_id: string
  name: string
  recurrence: 'WEEKLY' | 'MONTHLY' | 'QUARTERLY'
  day_of_week?: string
  time_start: string
  time_end: string
  systems: string[]
}

export interface IncidentManagement {
  incidents: IncidentRecord[]
  severity_matrix: SeverityMatrix
  escalation_procedures: EscalationProcedure[]
  post_incident_reviews: PostIncidentReview[]
}

export interface IncidentRecord {
  incident_id: string
  title: string
  description: string
  severity: 'P0' | 'P1' | 'P2' | 'P3' | 'P4'
  priority: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  category: 'OUTAGE' | 'DEGRADATION' | 'SECURITY' | 'DATA' | 'OPERATIONAL'
  reported_at: string
  reported_by: string
  assigned_to: string
  status: 'NEW' | 'ACKNOWLEDGED' | 'INVESTIGATING' | 'IDENTIFIED' | 'RESOLVING' | 'RESOLVED' | 'CLOSED'
  affected_services: string[]
  affected_users: number
  timeline: IncidentTimeline[]
  resolution: string
  root_cause?: string
  resolved_at?: string
  closed_at?: string
}

export interface IncidentTimeline {
  timestamp: string
  event: string
  actor: string
  details?: string
}

export interface SeverityMatrix {
  p0: SeverityDefinition
  p1: SeverityDefinition
  p2: SeverityDefinition
  p3: SeverityDefinition
  p4: SeverityDefinition
}

export interface SeverityDefinition {
  name: string
  description: string
  response_time_minutes: number
  update_frequency_minutes: number
  escalation_time_minutes: number
}

export interface EscalationProcedure {
  level: number
  role: string
  trigger: string
  notification_method: 'EMAIL' | 'SMS' | 'PHONE' | 'PAGER' | 'SLACK'
  contacts: string[]
}

export interface PostIncidentReview {
  review_id: string
  incident_id: string
  review_date: string
  attendees: string[]
  timeline: string
  root_cause: string
  contributing_factors: string[]
  what_went_well: string[]
  what_went_wrong: string[]
  action_items: ActionItem[]
  lessons_learned: string[]
}

export interface ActionItem {
  action_id: string
  description: string
  owner: string
  due_date: string
  priority: 'HIGH' | 'MEDIUM' | 'LOW'
  status: 'OPEN' | 'IN_PROGRESS' | 'COMPLETED'
}

export interface AuditTrail {
  events: AuditEvent[]
  retention_days: number
  encryption: boolean
  tamper_proof: boolean
}

export interface AuditEvent {
  event_id: string
  timestamp: string
  actor: string
  action: string
  resource_type: string
  resource_id: string
  before_state?: Record<string, unknown>
  after_state?: Record<string, unknown>
  ip_address?: string
  user_agent?: string
  result: 'SUCCESS' | 'FAILURE'
  error_message?: string
}

// ============================================================================
// COMMON UTILITY TYPES
// ============================================================================

export interface Issue {
  issue_id: string
  type: 'BUG' | 'FEATURE' | 'IMPROVEMENT' | 'TASK'
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  status: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED' | 'CLOSED'
  title: string
  description: string
  assigned_to?: string
  created_at: string
  updated_at: string
}
