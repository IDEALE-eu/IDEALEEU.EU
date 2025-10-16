/**
 * SEALING - Software, Embedded, AI Lifecycle, Integrated Network, Governance
 * 
 * Comprehensive library for managing the complete lifecycle of software and AI systems
 * in aerospace and high-tech manufacturing environments.
 * 
 * Modules:
 * - Software: Software lifecycle management, SBOM generation, security scanning
 * - Embedded: Embedded systems, firmware, real-time operations, safety
 * - AI: AI model lifecycle, training, deployment, monitoring, ethics
 * - Network: Network infrastructure, security, monitoring
 * - Governance: Governance, risk, compliance, data governance, incident management
 */

// Export all types
export * from './types'

// Export Software module
export {
  createSoftwarePackage,
  advanceToStage,
  addDependency,
  createRelease,
  generateSBOM,
  addSecurityScan,
  updateQualityMetrics,
  validateDeploymentReadiness,
  calculateMaturityScore,
  exportPackageJSON,
  exportSBOMCycloneDX,
  exportSBOMSPDX,
} from './software'

// Export Embedded module
export {
  createEmbeddedSystem,
  addFirmwareComponent,
  addRealtimeTask,
  validateSchedulability,
  addCommunicationProtocol,
  addCANMessage,
  addSignal,
  addDTC,
  configureSecureBoot,
  calculateMemoryUsage,
  calculatePowerConsumption,
  validateSafetyRequirements,
  generateDBCFile,
  exportEmbeddedSystemJSON,
} from './embedded'

// Export AI module
export {
  createAIModel,
  recordExperiment,
  completeTraining,
  recordEvaluationMetrics,
  createModelVersion,
  deployModel,
  applyOptimization,
  addMonitoringMetric,
  detectDataDrift,
  calculateFeatureImportance,
  assessFairness,
  calculateEnvironmentalImpact,
  validateProductionReadiness,
  generateModelCard,
  exportAIModelJSON,
} from './ai'

// Export Network module
export {
  createNetworkInfrastructure,
  addSubnet,
  addFirewallRule,
  addNetworkDevice,
  addVPNTunnel,
  addCertificate,
  addAccessPolicy,
  checkCertificateExpiration,
  calculateSecurityScore,
  generateNetworkDiagram,
  exportNetworkJSON,
  validateNetworkSecurity,
} from './network'

// Export Governance module
export {
  createGovernanceFramework,
  addGovernancePolicy,
  addControl,
  createRisk,
  addMitigationStrategy,
  calculateRiskHeatMap,
  createChangeRequest,
  createIncident,
  updateIncidentStatus,
  addDataset,
  calculateGovernanceMaturity,
  generateGovernanceReport,
  exportGovernanceJSON,
} from './governance'

/**
 * SEALING Version
 */
export const SEALING_VERSION = '1.0.0'

/**
 * SEALING Module Information
 */
export const SEALING_MODULES = {
  software: {
    name: 'Software Lifecycle Management',
    description: 'Comprehensive software package management, SBOM generation, security scanning, and quality metrics',
    version: '1.0.0',
  },
  embedded: {
    name: 'Embedded Systems Management',
    description: 'Firmware management, real-time task scheduling, safety validation, and hardware profiling',
    version: '1.0.0',
  },
  ai: {
    name: 'AI Lifecycle Management',
    description: 'AI model training, evaluation, deployment, monitoring, and ethical assessment',
    version: '1.0.0',
  },
  network: {
    name: 'Network Infrastructure & Security',
    description: 'Network topology, security configuration, monitoring, and compliance validation',
    version: '1.0.0',
  },
  governance: {
    name: 'Governance, Risk & Compliance',
    description: 'Policy management, risk assessment, compliance tracking, and incident management',
    version: '1.0.0',
  },
} as const

/**
 * Get SEALING module information
 */
export function getSEALINGInfo() {
  return {
    version: SEALING_VERSION,
    modules: Object.keys(SEALING_MODULES),
    description: 'Software, Embedded, AI Lifecycle, Integrated Network, Governance',
  }
}
