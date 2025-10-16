/**
 * SEALING - Software, Embedded Systems, AI Lifecycle, and Network Governance
 * Software Component Type Definitions
 * 
 * This module defines comprehensive data structures for software components
 * including SBOM, build artifacts, security scanning, and certification.
 */

// ============================================================================
// Core Identification
// ============================================================================

export interface SoftwareIdentification {
  name: string;
  version: string;
  type: 'FIRMWARE' | 'APPLICATION' | 'LIBRARY' | 'DRIVER' | 'MIDDLEWARE' | 'OS';
  domain: string; // e.g., 'LCC', 'AAA', 'IIS'
  description?: string;
}

// ============================================================================
// Repository and Version Control
// ============================================================================

export interface RepositoryInfo {
  vcs: 'git' | 'svn' | 'mercurial';
  url: string;
  branch: string;
  commit_sha: string;
  tag?: string;
  submodules?: RepositoryInfo[];
}

// ============================================================================
// Build Information
// ============================================================================

export interface BuildArtifact {
  artifact_id: string;
  type: 'BINARY' | 'LIBRARY' | 'SOURCE' | 'DOCUMENTATION';
  file_name: string;
  file_size_bytes: number;
  checksum: {
    sha256: string;
    sha512?: string;
    md5?: string;
  };
  signature?: {
    algorithm: 'RSA' | 'ECDSA' | 'EdDSA';
    public_key_id: string;
    signature_base64: string;
  };
  storage_location: string;
}

export interface BuildInfo {
  build_id: string;
  build_date: string; // ISO 8601
  build_tool: string; // e.g., 'cmake', 'make', 'maven', 'gradle'
  compiler: string;
  compiler_version: string;
  build_flags: string[];
  artifacts: BuildArtifact[];
}

// ============================================================================
// Dependencies
// ============================================================================

export interface Dependency {
  name: string;
  version: string;
  type: 'COMPILE' | 'RUNTIME' | 'DEVELOPMENT' | 'PROVIDED';
  license: string;
  source: string; // URL or package repository
  checksum?: string;
  vulnerabilities?: Vulnerability[];
}

export interface Vulnerability {
  cve_id: string;
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  description: string;
  affected_versions: string;
  fixed_version?: string;
  published_date: string;
  cvss_score?: number;
}

// ============================================================================
// SBOM (Software Bill of Materials)
// ============================================================================

export interface SBOM {
  sbom_id: string;
  format: 'SPDX' | 'CycloneDX';
  version: string;
  created_date: string;
  creator: string;
  components: SBOMComponent[];
  relationships: SBOMRelationship[];
  document_uri: string;
  checksum: string;
}

export interface SBOMComponent {
  component_id: string;
  name: string;
  version: string;
  type: 'APPLICATION' | 'FRAMEWORK' | 'LIBRARY' | 'CONTAINER' | 'OPERATING_SYSTEM' | 'DEVICE' | 'FIRMWARE' | 'FILE';
  supplier: string;
  author?: string;
  license: string;
  purl?: string; // Package URL
  cpe?: string; // Common Platform Enumeration
  hashes?: {
    sha256?: string;
    sha512?: string;
  };
}

export interface SBOMRelationship {
  from_component: string;
  to_component: string;
  relationship_type: 'DEPENDS_ON' | 'CONTAINS' | 'OPTIONAL_DEPENDENCY' | 'PROVIDED_DEPENDENCY' | 'TEST_DEPENDENCY';
}

// ============================================================================
// Testing
// ============================================================================

export interface TestSuite {
  suite_id: string;
  total_tests: number;
  passed: number;
  failed: number;
  skipped: number;
  execution_time_seconds: number;
  failures: TestFailure[];
  report_uri: string;
}

export interface TestFailure {
  test_name: string;
  error_message: string;
  stack_trace?: string;
}

export interface TestingInfo {
  unit_tests?: TestSuite;
  integration_tests?: TestSuite;
  system_tests?: TestSuite;
  coverage_percent?: number;
}

// ============================================================================
// Security Scanning
// ============================================================================

export interface SASTScan {
  scan_id: string;
  tool: string; // e.g., 'CodeQL', 'SonarQube', 'Coverity'
  scan_date: string;
  findings: SecurityFinding[];
  report_uri: string;
}

export interface DASTScan {
  scan_id: string;
  tool: string; // e.g., 'OWASP ZAP', 'Burp Suite'
  scan_date: string;
  findings: SecurityFinding[];
  report_uri: string;
}

export interface DependencyScan {
  scan_id: string;
  tool: string; // e.g., 'Snyk', 'WhiteSource', 'Dependabot'
  scan_date: string;
  vulnerabilities: Vulnerability[];
  report_uri: string;
}

export interface SecurityFinding {
  finding_id: string;
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW' | 'INFO';
  category: string; // e.g., 'SQL Injection', 'Buffer Overflow', 'Hardcoded Credentials'
  description: string;
  location: {
    file_path: string;
    line_number?: number;
    function_name?: string;
  };
  cwe_id?: string;
  remediation?: string;
  status: 'OPEN' | 'IN_PROGRESS' | 'RESOLVED' | 'FALSE_POSITIVE' | 'ACCEPTED_RISK';
}

export interface SecurityInfo {
  sast_scan?: SASTScan;
  dast_scan?: DASTScan;
  dependency_scan?: DependencyScan;
  vulnerabilities: Vulnerability[];
}

// ============================================================================
// Certification (DO-178C)
// ============================================================================

export interface CertificationInfo {
  standard: 'DO-178C' | 'DO-254' | 'IEC-61508' | 'ISO-26262';
  level: 'DAL_A' | 'DAL_B' | 'DAL_C' | 'DAL_D' | 'DAL_E' | 'ASIL_A' | 'ASIL_B' | 'ASIL_C' | 'ASIL_D' | 'SIL_1' | 'SIL_2' | 'SIL_3' | 'SIL_4';
  evidence_package: string; // URI to certification evidence
  verification_methods?: string[];
  certification_authority?: string;
  certification_date?: string;
}

// ============================================================================
// SLSA Provenance
// ============================================================================

export interface SLSAProvenance {
  slsa_level: 0 | 1 | 2 | 3 | 4;
  builder: {
    id: string;
    version: string;
  };
  invocation: {
    config_source: {
      uri: string;
      digest: { sha256: string };
      entry_point: string;
    };
    parameters?: Record<string, any>;
    environment?: Record<string, string>;
  };
  metadata: {
    build_started_on: string;
    build_finished_on: string;
    completeness: {
      parameters: boolean;
      environment: boolean;
      materials: boolean;
    };
    reproducible: boolean;
  };
  materials: Array<{
    uri: string;
    digest: { sha256: string };
  }>;
}

// ============================================================================
// Main Software Component Interface
// ============================================================================

export interface SoftwareComponent {
  // Identification
  component_id: string;
  utcs_ref: string; // e.g., "UTCS-LCC/FW-FCC-001@2.5.3"
  identification: SoftwareIdentification;

  // Source and Build
  repository?: RepositoryInfo;
  build: BuildInfo;

  // Dependencies
  dependencies: Dependency[];

  // SBOM
  sbom: SBOM;

  // Testing
  testing?: TestingInfo;

  // Security
  security?: SecurityInfo;

  // Certification
  certification?: CertificationInfo;

  // Provenance
  provenance?: SLSAProvenance;

  // Metadata
  created_date: string;
  last_modified_date: string;
  owner: string;
  maintainers?: string[];
  documentation_uri?: string;
  release_notes_uri?: string;

  // Relationships
  parent_prd?: string; // Reference to PRD document
  related_components?: string[]; // Other component IDs
  supersedes?: string; // Previous version component ID
}

// ============================================================================
// Helper Functions
// ============================================================================

export function createJointRelation(
  from_component: SoftwareComponent,
  to_component: SoftwareComponent,
  relation_type: 'DEPENDS_ON' | 'INTEGRATES_WITH' | 'REPLACES' | 'EXTENDS'
): {
  from_id: string;
  to_id: string;
  relation: string;
} {
  return {
    from_id: from_component.component_id,
    to_id: to_component.component_id,
    relation: relation_type
  };
}

export function validateSoftwareComponent(component: SoftwareComponent): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!component.component_id) errors.push('component_id is required');
  if (!component.utcs_ref) errors.push('utcs_ref is required');
  if (!component.identification?.name) errors.push('identification.name is required');
  if (!component.identification?.version) errors.push('identification.version is required');
  if (!component.build?.build_id) errors.push('build.build_id is required');
  if (!component.sbom?.sbom_id) errors.push('sbom.sbom_id is required');

  return {
    valid: errors.length === 0,
    errors
  };
}
