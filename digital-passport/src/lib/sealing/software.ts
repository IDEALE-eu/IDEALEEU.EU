/**
 * SEALING - Software Lifecycle Management Module
 * Comprehensive utilities for software package management, SBOM generation, and lifecycle tracking
 */

import type {
  SoftwarePackage,
  SoftwareType,
  DevelopmentStage,
  CriticalityLevel,
  SoftwareRelease,
  SBOM,
  SBOMComponent,
  QualityMetrics,
  ReleaseArtifact,
  StageMetadata,
} from './types'

/**
 * Create a new software package with default structure
 */
export function createSoftwarePackage(
  name: string,
  version: string,
  type: SoftwareType,
  language: string,
  criticality: CriticalityLevel,
  domain: string,
  creator: string
): SoftwarePackage {
  const timestamp = new Date().toISOString()
  const packageId = `SW-${type}-${name.replace(/[^a-zA-Z0-9]/g, '-')}-${version}`
  const utcsRef = `UTCS-${domain}/${name}@${version}`

  return {
    package_id: packageId,
    name,
    version,
    type,
    stage: 'DESIGN',
    criticality,
    utcs_ref: utcsRef,
    created_at: timestamp,
    updated_at: timestamp,
    metadata: {
      description: '',
      language,
      dependencies: [],
    },
    lifecycle: {
      current_stage: 'DESIGN',
      stages: {},
      releases: [],
    },
    sbom: {
      spec_version: '1.4',
      format: 'CYCLONEDX',
      generated_at: timestamp,
      components: [],
      licenses: [],
      supplier: '',
      author: creator,
    },
    security: {
      security_level: 'PUBLIC',
      threats: [],
      vulnerabilities: [],
      scans: [],
      certifications: [],
      access_control: {
        authentication: 'NONE',
        authorization: 'NONE',
        encryption_at_rest: false,
        encryption_in_transit: false,
        key_management: 'SOFTWARE',
      },
    },
    quality: {
      code_coverage: {
        lines_covered: 0,
        lines_total: 0,
        coverage_percent: 0,
        branches_covered: 0,
        branches_total: 0,
        branch_coverage_percent: 0,
        functions_covered: 0,
        functions_total: 0,
        function_coverage_percent: 0,
      },
      static_analysis: {
        tool: '',
        version: '',
        executed_at: timestamp,
        issues: {
          blocker: 0,
          critical: 0,
          major: 0,
          minor: 0,
          info: 0,
        },
        code_smells: 0,
        bugs: 0,
        vulnerabilities: 0,
        duplicated_lines_percent: 0,
      },
      complexity: {
        cyclomatic_complexity: 0,
        cognitive_complexity: 0,
      },
      maintainability: {
        score: 100,
        grade: 'A',
        comment_ratio: 0,
        average_lines_per_function: 0,
      },
      technical_debt: {
        debt_ratio: 0,
        debt_minutes: 0,
        sqale_rating: 'A',
        remediation_effort_minutes: 0,
      },
      test_results: {
        total_tests: 0,
        passed: 0,
        failed: 0,
        skipped: 0,
        duration_seconds: 0,
        test_suites: [],
      },
    },
    compliance: {
      standards: [],
      policies: [],
      audits: [],
      traceability: {
        requirements: [],
        coverage: {
          requirements_traced: 0,
          requirements_total: 0,
          coverage_percent: 0,
        },
      },
    },
  }
}

/**
 * Advance software package to next lifecycle stage
 */
export function advanceToStage(
  pkg: SoftwarePackage,
  stage: DevelopmentStage
): SoftwarePackage {
  const timestamp = new Date().toISOString()
  
  // Complete current stage
  const currentStage = pkg.lifecycle.current_stage.toLowerCase() as keyof typeof pkg.lifecycle.stages
  if (pkg.lifecycle.stages[currentStage]) {
    pkg.lifecycle.stages[currentStage]!.completed_at = timestamp
    pkg.lifecycle.stages[currentStage]!.status = 'COMPLETED'
  }

  // Start new stage
  const newStageKey = stage.toLowerCase() as keyof typeof pkg.lifecycle.stages
  const stageMetadata: StageMetadata = {
    started_at: timestamp,
    status: 'IN_PROGRESS',
    artifacts: [],
    approvals: [],
    issues: [],
  }

  pkg.lifecycle.stages = {
    ...pkg.lifecycle.stages,
    [newStageKey]: stageMetadata,
  }

  pkg.lifecycle.current_stage = stage
  pkg.updated_at = timestamp

  return pkg
}

/**
 * Add a software dependency
 */
export function addDependency(
  pkg: SoftwarePackage,
  name: string,
  version: string,
  type: 'DIRECT' | 'TRANSITIVE',
  license: string
): SoftwarePackage {
  const dependency = {
    name,
    version,
    type,
    license,
    vulnerabilities: [],
  }

  pkg.metadata.dependencies.push(dependency)
  pkg.updated_at = new Date().toISOString()

  return pkg
}

/**
 * Create a software release
 */
export function createRelease(
  pkg: SoftwarePackage,
  version: string,
  releaseType: 'MAJOR' | 'MINOR' | 'PATCH' | 'HOTFIX',
  commitSha: string,
  changelog: string,
  artifacts: ReleaseArtifact[]
): SoftwareRelease {
  const release: SoftwareRelease = {
    version,
    release_date: new Date().toISOString(),
    type: releaseType,
    commit_sha: commitSha,
    artifacts,
    changelog,
  }

  pkg.lifecycle.releases.push(release)
  pkg.version = version
  pkg.updated_at = new Date().toISOString()

  return release
}

/**
 * Generate SBOM for software package
 */
export function generateSBOM(
  pkg: SoftwarePackage,
  format: 'CYCLONEDX' | 'SPDX' = 'CYCLONEDX'
): SBOM {
  const timestamp = new Date().toISOString()
  const components: SBOMComponent[] = []

  // Add main component
  components.push({
    bom_ref: `${pkg.name}@${pkg.version}`,
    type: 'APPLICATION',
    name: pkg.name,
    version: pkg.version,
    licenses: [],
    hashes: [],
    dependencies: pkg.metadata.dependencies.map(d => `${d.name}@${d.version}`),
  })

  // Add dependencies as components
  pkg.metadata.dependencies.forEach(dep => {
    components.push({
      bom_ref: `${dep.name}@${dep.version}`,
      type: 'LIBRARY',
      name: dep.name,
      version: dep.version,
      licenses: [dep.license],
      hashes: [],
      dependencies: [],
    })
  })

  pkg.sbom = {
    spec_version: format === 'CYCLONEDX' ? '1.4' : '2.3',
    format,
    generated_at: timestamp,
    components,
    licenses: pkg.sbom.licenses,
    supplier: pkg.sbom.supplier,
    author: pkg.sbom.author,
  }

  return pkg.sbom
}

/**
 * Add security scan results to package
 */
export function addSecurityScan(
  pkg: SoftwarePackage,
  scanType: 'SAST' | 'DAST' | 'IAST' | 'SCA' | 'CONTAINER' | 'SECRETS' | 'LICENSE',
  tool: string,
  toolVersion: string,
  findings: any[]
): SoftwarePackage {
  const timestamp = new Date().toISOString()
  const summary = findings.reduce(
    (acc, f) => {
      const severity = f.severity.toLowerCase()
      if (severity === 'critical') acc.critical++
      else if (severity === 'high') acc.high++
      else if (severity === 'medium') acc.medium++
      else if (severity === 'low') acc.low++
      else acc.info++
      return acc
    },
    { critical: 0, high: 0, medium: 0, low: 0, info: 0 }
  )

  pkg.security.scans.push({
    scan_id: `SCAN-${scanType}-${timestamp}`,
    type: scanType,
    tool,
    version: toolVersion,
    executed_at: timestamp,
    duration_seconds: 0,
    findings,
    summary,
  })

  pkg.updated_at = timestamp

  return pkg
}

/**
 * Update code quality metrics
 */
export function updateQualityMetrics(
  pkg: SoftwarePackage,
  metrics: Partial<QualityMetrics>
): SoftwarePackage {
  pkg.quality = {
    ...pkg.quality,
    ...metrics,
  }
  pkg.updated_at = new Date().toISOString()

  return pkg
}

/**
 * Validate software package for deployment readiness
 */
export function validateDeploymentReadiness(pkg: SoftwarePackage): {
  ready: boolean
  checks: { check: string; passed: boolean; message: string }[]
} {
  const checks = []

  // Check lifecycle stage
  checks.push({
    check: 'Lifecycle Stage',
    passed: pkg.stage === 'DEPLOYMENT' || pkg.stage === 'MAINTENANCE',
    message: pkg.stage === 'DEPLOYMENT' || pkg.stage === 'MAINTENANCE'
      ? 'Package is in deployment-ready stage'
      : `Package is in ${pkg.stage} stage, must be DEPLOYMENT or MAINTENANCE`,
  })

  // Check code coverage
  const coverageThreshold = pkg.criticality === 'DAL_A' ? 100 : 
                            pkg.criticality === 'DAL_B' ? 90 :
                            pkg.criticality === 'DAL_C' ? 80 : 70
  checks.push({
    check: 'Code Coverage',
    passed: pkg.quality.code_coverage.coverage_percent >= coverageThreshold,
    message: `Coverage ${pkg.quality.code_coverage.coverage_percent}% (required: ${coverageThreshold}%)`,
  })

  // Check security vulnerabilities
  const hasBlockerVulns = pkg.security.scans.some(
    scan => scan.summary.critical > 0 || scan.summary.high > 0
  )
  checks.push({
    check: 'Security Vulnerabilities',
    passed: !hasBlockerVulns,
    message: hasBlockerVulns
      ? 'Critical or High severity vulnerabilities found'
      : 'No blocking vulnerabilities',
  })

  // Check static analysis
  const hasBlockerIssues = pkg.quality.static_analysis.issues.blocker > 0
  checks.push({
    check: 'Static Analysis',
    passed: !hasBlockerIssues,
    message: hasBlockerIssues
      ? `${pkg.quality.static_analysis.issues.blocker} blocker issues found`
      : 'No blocker issues',
  })

  // Check test results
  const testsPass = pkg.quality.test_results.failed === 0
  checks.push({
    check: 'Test Results',
    passed: testsPass,
    message: testsPass
      ? `All ${pkg.quality.test_results.total_tests} tests passed`
      : `${pkg.quality.test_results.failed} tests failed`,
  })

  // Check SBOM
  const hasSBOM = pkg.sbom.components.length > 0
  checks.push({
    check: 'SBOM',
    passed: hasSBOM,
    message: hasSBOM
      ? `SBOM contains ${pkg.sbom.components.length} components`
      : 'SBOM not generated',
  })

  const allPassed = checks.every(c => c.passed)

  return {
    ready: allPassed,
    checks,
  }
}

/**
 * Calculate software maturity score (0-100)
 */
export function calculateMaturityScore(pkg: SoftwarePackage): number {
  let score = 0

  // Lifecycle progress (0-20 points)
  const stageScores = {
    DESIGN: 5,
    IMPLEMENTATION: 10,
    TESTING: 13,
    INTEGRATION: 16,
    DEPLOYMENT: 18,
    MAINTENANCE: 20,
    DECOMMISSION: 20,
  }
  score += stageScores[pkg.stage] || 0

  // Code coverage (0-20 points)
  score += Math.min(20, pkg.quality.code_coverage.coverage_percent / 5)

  // Test results (0-15 points)
  if (pkg.quality.test_results.total_tests > 0) {
    const passRate = pkg.quality.test_results.passed / pkg.quality.test_results.total_tests
    score += passRate * 15
  }

  // Security (0-15 points)
  const vulnCount = pkg.security.vulnerabilities.length
  if (vulnCount === 0) {
    score += 15
  } else if (vulnCount <= 5) {
    score += 10
  } else if (vulnCount <= 10) {
    score += 5
  }

  // Maintainability (0-15 points)
  score += (pkg.quality.maintainability.score / 100) * 15

  // Documentation & compliance (0-15 points)
  const hasDocumentation = pkg.metadata.description.length > 0
  const hasCompliance = pkg.compliance.standards.length > 0
  const hasSBOM = pkg.sbom.components.length > 0
  score += (hasDocumentation ? 5 : 0) + (hasCompliance ? 5 : 0) + (hasSBOM ? 5 : 0)

  return Math.round(Math.min(100, score))
}

/**
 * Export software package to JSON
 */
export function exportPackageJSON(pkg: SoftwarePackage): string {
  return JSON.stringify(pkg, null, 2)
}

/**
 * Export SBOM to CycloneDX JSON format
 */
export function exportSBOMCycloneDX(sbom: SBOM): string {
  const cycloneDX = {
    bomFormat: 'CycloneDX',
    specVersion: sbom.spec_version,
    serialNumber: `urn:uuid:${Date.now()}`,
    version: 1,
    metadata: {
      timestamp: sbom.generated_at,
      authors: [{ name: sbom.author }],
      supplier: { name: sbom.supplier },
    },
    components: sbom.components.map(c => ({
      'bom-ref': c.bom_ref,
      type: c.type.toLowerCase(),
      name: c.name,
      version: c.version,
      purl: c.purl,
      cpe: c.cpe,
      licenses: c.licenses.map(l => ({ license: { id: l } })),
      hashes: c.hashes,
    })),
    dependencies: sbom.components.map(c => ({
      ref: c.bom_ref,
      dependsOn: c.dependencies,
    })),
  }

  return JSON.stringify(cycloneDX, null, 2)
}

/**
 * Export SBOM to SPDX format
 */
export function exportSBOMSPDX(sbom: SBOM): string {
  const spdx = {
    spdxVersion: `SPDX-${sbom.spec_version}`,
    dataLicense: 'CC0-1.0',
    SPDXID: 'SPDXRef-DOCUMENT',
    name: 'Software Bill of Materials',
    documentNamespace: `https://sbom.example.com/${Date.now()}`,
    creationInfo: {
      created: sbom.generated_at,
      creators: [`Tool: IDEALE-EU`, `Person: ${sbom.author}`],
    },
    packages: sbom.components.map((c, i) => ({
      SPDXID: `SPDXRef-Package-${i}`,
      name: c.name,
      versionInfo: c.version,
      downloadLocation: c.purl || 'NOASSERTION',
      filesAnalyzed: false,
      licenseConcluded: c.licenses.join(' AND ') || 'NOASSERTION',
      licenseDeclared: c.licenses.join(' AND ') || 'NOASSERTION',
      copyrightText: 'NOASSERTION',
    })),
  }

  return JSON.stringify(spdx, null, 2)
}
