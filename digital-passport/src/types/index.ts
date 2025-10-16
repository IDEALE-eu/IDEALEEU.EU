// TFA Domain codes (15 canonical domains)
export type TFADomain =
  | 'AAA' // Airframes-Aerodynamics-Airworthiness
  | 'AAP' // Airport-Adaptable-Platforms
  | 'CCC' // Cockpit-Cabin-Cargo
  | 'CQH' // Cryogenics-Quantum-H2
  | 'DDD' // Drainage-Dehumidification-Drying
  | 'EDI' // Electronics-Digital-Instruments
  | 'EEE' // Electrical-Endocircular-Energization
  | 'EER' // Environmental-Emissions-Remediation
  | 'IIF' // Industrial-Infrastructure-Facilities
  | 'IIS' // Information-Intelligence-Systems
  | 'LCC' // Linkages-Control-Communications
  | 'LIB' // Logistics-Inventory-Blockchain
  | 'MMM' // Mechanical-Material-Modules
  | 'OOO' // Operations-Optimization-Outcomes
  | 'PPP' // Propellers-Propellents-Propulsion

// CAx lifecycle phases (9 phases)
export type CAXPhase =
  | 'CAD' // Design
  | 'CAE' // Analysis
  | 'CAI' // Integration
  | 'CAO' // Optimization
  | 'CAM' // Manufacturing
  | 'CAP' // Planning
  | 'CAV' // Validation
  | 'CMP' // Compliance
  | 'CAS' // Services

// State progression (6 states)
export type State =
  | 'QS'  // Quantum Superposition - Pre-event
  | 'FWD' // Future/Waves Dynamics
  | 'UE'  // Unit Element
  | 'FE'  // Federation Entanglement
  | 'CB'  // Classical Bit - Post-event
  | 'QB'  // Qubit

// Layer abstraction (4 layers)
export type Layer =
  | 'L1' // DATA
  | 'L2' // MODEL
  | 'L3' // SERVICE
  | 'L4' // APP

// Verification status (5 states)
export type VerificationStatus =
  | 'verified'
  | 'pending'
  | 'failed'
  | 'expired'
  | 'drift'

// Component type
export type ComponentType =
  | 'hardware'
  | 'software'
  | 'firmware'
  | 'model'

// UTCS Manifest
export interface UTCSManifest {
  utcs_ref: string
  checksum: string
  signer: string
  timestamp: string
  component_type: ComponentType
  domain: TFADomain
  state: State
  layer: Layer
  verification_status: VerificationStatus
  metadata?: Record<string, unknown>
}

// Software UTCS extension with SBOM
export interface SoftwareUTCS extends UTCSManifest {
  component_type: 'software' | 'firmware' | 'model'
  repo?: string
  commit?: string
  sbom?: string
  license?: string
  build_provenance?: string
  artifacts?: Array<{
    type: string
    digest: string
  }>
  qa?: {
    tests: string
    coverage: string
    static_analysis: string
    vulnerabilities: string
  }
  policies?: Array<{
    rule_id: string
    status: string
  }>
}

// Digital Passport
export interface DigitalPassport {
  id: string
  title: string
  utcs_ref: string
  component_type: ComponentType
  domain: TFADomain
  phase: CAXPhase
  state: State
  layer: Layer
  verification_status: VerificationStatus
  program: string
  supplier?: string
  created_at: string
  updated_at: string
  manifest: UTCSManifest | SoftwareUTCS
  lifecycle_progress: number
  qs_anchored: boolean
  cb_anchored: boolean
  ata_chapter?: string
}

// Filter state
export interface FilterState {
  search: string
  domain: TFADomain | 'all'
  phase: CAXPhase | 'all'
  state: State | 'all'
  status: VerificationStatus | 'all'
}

// Template category
export type TemplateCategory =
  | 'path-grammar'
  | 'folder-scaffold'
  | 'utcs-hardware'
  | 'utcs-software'
  | 'operational-ledger'
  | 'artifact-inventory'
  | 'interface-matrix'
  | 'ecr-eco'
  | 'ci-gates'
  | 'domain-sublibs'
  | 'quick-examples'

// Template
export interface Template {
  id: string
  category: TemplateCategory
  title: string
  description: string
  content: string
  language: string
  placeholders: string[]
}
