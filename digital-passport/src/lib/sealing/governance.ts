/**
 * SEALING - Governance, Risk, and Compliance Module
 * Comprehensive utilities for organizational governance, risk management, and compliance
 */

import type {
  GovernanceFramework,
  GovernancePolicy,
  Risk,
  ChangeRequest,
  IncidentRecord,
  Dataset,
  Control,
  MitigationStrategy,
} from './types'

/**
 * Create a new governance framework
 */
export function createGovernanceFramework(
  frameworkId: string,
  name: string,
  version: string,
  organization: string
): GovernanceFramework {
  const timestamp = new Date().toISOString()

  return {
    framework_id: frameworkId,
    name,
    version,
    organization,
    effective_date: timestamp,
    policies: [],
    risk_management: {
      methodology: 'NIST',
      risk_appetite: 'BALANCED',
      risks: [],
      risk_matrix: {
        dimensions: 5,
        thresholds: {
          low: 5,
          medium: 10,
          high: 15,
          critical: 20,
        },
        heat_map: [],
      },
      mitigation_strategies: [],
    },
    compliance_management: {
      frameworks: [],
      assessments: [],
      gaps: [],
      remediation_plan: {
        plan_id: `PLAN-${timestamp}`,
        gaps: [],
        timeline: '',
        budget: 0,
        milestones: [],
        progress_percent: 0,
      },
    },
    data_governance: {
      data_catalog: {
        datasets: [],
        total_datasets: 0,
        total_data_size_gb: 0,
        metadata_completeness_percent: 0,
      },
      data_quality: {
        dimensions: [],
        overall_score: 0,
        issues: [],
        rules: [],
      },
      data_lineage: {
        lineage_id: '',
        dataset_id: '',
        upstream: [],
        downstream: [],
        transformations: [],
        impact_analysis: {
          upstream_dependencies: 0,
          downstream_dependents: 0,
          critical_paths: [],
          blast_radius: 0,
        },
      },
      data_privacy: {
        regulations: [],
        consent_management: {
          consent_required: false,
          consent_records: [],
          withdrawal_process: '',
        },
        data_subject_rights: {
          access: false,
          rectification: false,
          erasure: false,
          portability: false,
          objection: false,
          requests: [],
        },
        privacy_incidents: [],
      },
      master_data_management: {
        golden_records: [],
        data_domains: [],
        matching_rules: [],
        data_stewards: [],
      },
    },
    change_management: {
      changes: [],
      change_board: {
        members: [],
        meeting_schedule: 'Weekly',
        next_meeting: '',
        voting_threshold: 0.5,
      },
      emergency_changes: [],
      change_calendar: {
        scheduled_changes: [],
        blackout_periods: [],
        maintenance_windows: [],
      },
    },
    incident_management: {
      incidents: [],
      severity_matrix: {
        p0: {
          name: 'Critical',
          description: 'Complete service outage',
          response_time_minutes: 15,
          update_frequency_minutes: 30,
          escalation_time_minutes: 30,
        },
        p1: {
          name: 'High',
          description: 'Severe degradation',
          response_time_minutes: 30,
          update_frequency_minutes: 60,
          escalation_time_minutes: 60,
        },
        p2: {
          name: 'Medium',
          description: 'Moderate impact',
          response_time_minutes: 120,
          update_frequency_minutes: 240,
          escalation_time_minutes: 240,
        },
        p3: {
          name: 'Low',
          description: 'Minor issue',
          response_time_minutes: 480,
          update_frequency_minutes: 480,
          escalation_time_minutes: 480,
        },
        p4: {
          name: 'Minimal',
          description: 'Cosmetic issue',
          response_time_minutes: 1440,
          update_frequency_minutes: 1440,
          escalation_time_minutes: 2880,
        },
      },
      escalation_procedures: [],
      post_incident_reviews: [],
    },
    audit_trail: {
      events: [],
      retention_days: 2555, // 7 years
      encryption: true,
      tamper_proof: true,
    },
  }
}

/**
 * Add governance policy
 */
export function addGovernancePolicy(
  framework: GovernanceFramework,
  name: string,
  category: 'SECURITY' | 'PRIVACY' | 'QUALITY' | 'OPERATIONAL' | 'FINANCIAL' | 'LEGAL',
  description: string,
  scope: string,
  owner: string,
  approvers: string[]
): GovernancePolicy {
  const timestamp = new Date().toISOString()

  const policy: GovernancePolicy = {
    policy_id: `POL-${Date.now()}`,
    name,
    category,
    description,
    scope,
    effective_date: timestamp,
    review_date: new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toISOString(), // 1 year
    owner,
    approvers,
    status: 'DRAFT',
    controls: [],
    violations: [],
  }

  framework.policies.push(policy)

  return policy
}

/**
 * Add control to policy
 */
export function addControl(
  policy: GovernancePolicy,
  name: string,
  type: 'PREVENTIVE' | 'DETECTIVE' | 'CORRECTIVE' | 'COMPENSATING',
  description: string,
  implementation: string,
  testingFrequency: 'CONTINUOUS' | 'DAILY' | 'WEEKLY' | 'MONTHLY' | 'QUARTERLY' | 'ANNUALLY'
): Control {
  const control: Control = {
    control_id: `CTRL-${Date.now()}`,
    name,
    type,
    description,
    implementation,
    testing_frequency: testingFrequency,
    last_tested: new Date().toISOString(),
    effectiveness: 'EFFECTIVE',
  }

  policy.controls.push(control)

  return control
}

/**
 * Create a risk
 */
export function createRisk(
  framework: GovernanceFramework,
  title: string,
  category: 'STRATEGIC' | 'OPERATIONAL' | 'FINANCIAL' | 'COMPLIANCE' | 'REPUTATIONAL' | 'TECHNICAL',
  description: string,
  likelihood: 'VERY_LOW' | 'LOW' | 'MEDIUM' | 'HIGH' | 'VERY_HIGH',
  impact: 'NEGLIGIBLE' | 'MINOR' | 'MODERATE' | 'MAJOR' | 'CATASTROPHIC',
  owner: string
): Risk {
  const likelihoodScore = {
    VERY_LOW: 1,
    LOW: 2,
    MEDIUM: 3,
    HIGH: 4,
    VERY_HIGH: 5,
  }

  const impactScore = {
    NEGLIGIBLE: 1,
    MINOR: 2,
    MODERATE: 3,
    MAJOR: 4,
    CATASTROPHIC: 5,
  }

  const riskScore = likelihoodScore[likelihood] * impactScore[impact]

  const risk: Risk = {
    risk_id: `RISK-${Date.now()}`,
    title,
    category,
    description,
    likelihood,
    impact,
    risk_score: riskScore,
    inherent_risk: riskScore,
    residual_risk: riskScore,
    owner,
    status: 'IDENTIFIED',
    controls: [],
    last_reviewed: new Date().toISOString(),
  }

  framework.risk_management.risks.push(risk)

  return risk
}

/**
 * Add mitigation strategy to risk
 */
export function addMitigationStrategy(
  framework: GovernanceFramework,
  riskId: string,
  type: 'AVOID' | 'REDUCE' | 'TRANSFER' | 'ACCEPT',
  description: string,
  actions: { description: string; responsible_party: string; due_date: string }[],
  costEstimate: number,
  effectivenessPercent: number
): MitigationStrategy {
  const strategy: MitigationStrategy = {
    strategy_id: `MIT-${Date.now()}`,
    risk_id: riskId,
    type,
    description,
    actions: actions.map(a => ({
      action_id: `ACT-${Date.now()}-${Math.random()}`,
      description: a.description,
      responsible_party: a.responsible_party,
      due_date: a.due_date,
      status: 'NOT_STARTED',
    })),
    cost_estimate: costEstimate,
    effectiveness_percent: effectivenessPercent,
    status: 'PLANNED',
  }

  framework.risk_management.mitigation_strategies.push(strategy)

  // Update residual risk
  const risk = framework.risk_management.risks.find(r => r.risk_id === riskId)
  if (risk) {
    risk.residual_risk = Math.round(risk.inherent_risk * (1 - effectivenessPercent / 100))
  }

  return strategy
}

/**
 * Calculate risk heat map
 */
export function calculateRiskHeatMap(framework: GovernanceFramework): void {
  const heatMap = new Map<string, string[]>()

  framework.risk_management.risks.forEach(risk => {
    const key = `${risk.likelihood}-${risk.impact}`
    if (!heatMap.has(key)) {
      heatMap.set(key, [])
    }
    heatMap.get(key)!.push(risk.risk_id)
  })

  framework.risk_management.risk_matrix.heat_map = Array.from(heatMap.entries()).map(
    ([key, risk_ids]) => {
      const [likelihood, impact] = key.split('-')
      return {
        likelihood,
        impact,
        risk_count: risk_ids.length,
        risk_ids,
      }
    }
  )
}

/**
 * Create change request
 */
export function createChangeRequest(
  framework: GovernanceFramework,
  title: string,
  type: 'STANDARD' | 'NORMAL' | 'EMERGENCY',
  category: 'INFRASTRUCTURE' | 'APPLICATION' | 'CONFIGURATION' | 'SECURITY',
  priority: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL',
  requester: string,
  description: string,
  justification: string,
  affectedSystems: string[],
  downtimeRequired: boolean
): ChangeRequest {
  const change: ChangeRequest = {
    change_id: `CHG-${Date.now()}`,
    title,
    type,
    category,
    priority,
    requester,
    description,
    justification,
    impact_assessment: {
      scope: '',
      affected_systems: affectedSystems,
      affected_users: 0,
      downtime_required: downtimeRequired,
      risk_level: 'MEDIUM',
      mitigation_plan: '',
    },
    implementation_plan: '',
    rollback_plan: '',
    testing_plan: '',
    requested_date: new Date().toISOString(),
    status: 'DRAFT',
    approvals: [],
  }

  framework.change_management.changes.push(change)

  return change
}

/**
 * Create incident
 */
export function createIncident(
  framework: GovernanceFramework,
  title: string,
  description: string,
  severity: 'P0' | 'P1' | 'P2' | 'P3' | 'P4',
  category: 'OUTAGE' | 'DEGRADATION' | 'SECURITY' | 'DATA' | 'OPERATIONAL',
  reportedBy: string,
  affectedServices: string[]
): IncidentRecord {
  const timestamp = new Date().toISOString()

  const incident: IncidentRecord = {
    incident_id: `INC-${Date.now()}`,
    title,
    description,
    severity,
    priority: severity === 'P0' || severity === 'P1' ? 'CRITICAL' : 
              severity === 'P2' ? 'HIGH' : 
              severity === 'P3' ? 'MEDIUM' : 'LOW',
    category,
    reported_at: timestamp,
    reported_by: reportedBy,
    assigned_to: '',
    status: 'NEW',
    affected_services: affectedServices,
    affected_users: 0,
    timeline: [
      {
        timestamp,
        event: 'Incident reported',
        actor: reportedBy,
      },
    ],
    resolution: '',
  }

  framework.incident_management.incidents.push(incident)

  return incident
}

/**
 * Update incident status
 */
export function updateIncidentStatus(
  incident: IncidentRecord,
  status: 'NEW' | 'ACKNOWLEDGED' | 'INVESTIGATING' | 'IDENTIFIED' | 'RESOLVING' | 'RESOLVED' | 'CLOSED',
  actor: string,
  details?: string
): IncidentRecord {
  incident.status = status
  incident.timeline.push({
    timestamp: new Date().toISOString(),
    event: `Status changed to ${status}`,
    actor,
    details,
  })

  if (status === 'RESOLVED') {
    incident.resolved_at = new Date().toISOString()
  } else if (status === 'CLOSED') {
    incident.closed_at = new Date().toISOString()
  }

  return incident
}

/**
 * Add dataset to data catalog
 */
export function addDataset(
  framework: GovernanceFramework,
  name: string,
  description: string,
  owner: string,
  classification: 'PUBLIC' | 'INTERNAL' | 'CONFIDENTIAL' | 'RESTRICTED',
  sensitivity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL',
  location: string,
  sizeGb: number,
  recordCount: number
): Dataset {
  const dataset: Dataset = {
    dataset_id: `DS-${Date.now()}`,
    name,
    description,
    owner,
    classification,
    sensitivity,
    schema: {
      fields: [],
    },
    location,
    size_gb: sizeGb,
    record_count: recordCount,
    last_updated: new Date().toISOString(),
    tags: [],
  }

  framework.data_governance.data_catalog.datasets.push(dataset)
  framework.data_governance.data_catalog.total_datasets++
  framework.data_governance.data_catalog.total_data_size_gb += sizeGb

  return dataset
}

/**
 * Calculate governance maturity score
 */
export function calculateGovernanceMaturity(framework: GovernanceFramework): {
  score: number
  level: 'INITIAL' | 'MANAGED' | 'DEFINED' | 'QUANTITATIVELY_MANAGED' | 'OPTIMIZING'
  dimensions: { dimension: string; score: number; details: string }[]
} {
  const dimensions = []
  let totalScore = 0

  // Policy Management (0-20 points)
  const activePolicies = framework.policies.filter(p => p.status === 'ACTIVE').length
  const policyScore = Math.min(20, activePolicies * 4)
  dimensions.push({
    dimension: 'Policy Management',
    score: policyScore,
    details: `${activePolicies} active policies`,
  })
  totalScore += policyScore

  // Risk Management (0-20 points)
  const identifiedRisks = framework.risk_management.risks.length
  const mitigatedRisks = framework.risk_management.risks.filter(r => r.status === 'MITIGATED').length
  const riskScore = identifiedRisks > 0 ? Math.min(20, (mitigatedRisks / identifiedRisks) * 20) : 0
  dimensions.push({
    dimension: 'Risk Management',
    score: riskScore,
    details: `${mitigatedRisks}/${identifiedRisks} risks mitigated`,
  })
  totalScore += riskScore

  // Compliance Management (0-20 points)
  const complianceScore = framework.compliance_management.frameworks.length > 0 ? 15 : 0
  dimensions.push({
    dimension: 'Compliance Management',
    score: complianceScore,
    details: `${framework.compliance_management.frameworks.length} compliance frameworks`,
  })
  totalScore += complianceScore

  // Change Management (0-20 points)
  const hasChangeProcess = framework.change_management.changes.length > 0
  const changeScore = hasChangeProcess ? 15 : 0
  dimensions.push({
    dimension: 'Change Management',
    score: changeScore,
    details: hasChangeProcess ? `${framework.change_management.changes.length} changes tracked` : 'No change process',
  })
  totalScore += changeScore

  // Incident Management (0-20 points)
  const incidents = framework.incident_management.incidents
  const resolvedIncidents = incidents.filter(i => i.status === 'RESOLVED' || i.status === 'CLOSED').length
  const incidentScore = incidents.length > 0 ? Math.min(20, (resolvedIncidents / incidents.length) * 20) : 0
  dimensions.push({
    dimension: 'Incident Management',
    score: incidentScore,
    details: `${resolvedIncidents}/${incidents.length} incidents resolved`,
  })
  totalScore += incidentScore

  // Determine maturity level
  const level: 'INITIAL' | 'MANAGED' | 'DEFINED' | 'QUANTITATIVELY_MANAGED' | 'OPTIMIZING' =
    totalScore >= 80 ? 'OPTIMIZING' :
    totalScore >= 60 ? 'QUANTITATIVELY_MANAGED' :
    totalScore >= 40 ? 'DEFINED' :
    totalScore >= 20 ? 'MANAGED' :
    'INITIAL'

  return {
    score: totalScore,
    level,
    dimensions,
  }
}

/**
 * Generate governance report
 */
export function generateGovernanceReport(framework: GovernanceFramework): string {
  const maturity = calculateGovernanceMaturity(framework)
  
  return `# Governance Framework Report: ${framework.name}

## Framework Details
- **Framework ID**: ${framework.framework_id}
- **Version**: ${framework.version}
- **Organization**: ${framework.organization}
- **Effective Date**: ${framework.effective_date}

## Maturity Assessment
- **Maturity Score**: ${maturity.score}/100
- **Maturity Level**: ${maturity.level}

### Dimension Scores
${maturity.dimensions.map(d => `- **${d.dimension}**: ${d.score}/20 - ${d.details}`).join('\n')}

## Policy Management
- **Total Policies**: ${framework.policies.length}
- **Active Policies**: ${framework.policies.filter(p => p.status === 'ACTIVE').length}
- **Draft Policies**: ${framework.policies.filter(p => p.status === 'DRAFT').length}
- **Total Controls**: ${framework.policies.reduce((sum, p) => sum + p.controls.length, 0)}

## Risk Management
- **Methodology**: ${framework.risk_management.methodology}
- **Risk Appetite**: ${framework.risk_management.risk_appetite}
- **Total Risks**: ${framework.risk_management.risks.length}
- **Critical Risks**: ${framework.risk_management.risks.filter(r => r.risk_score >= 15).length}
- **High Risks**: ${framework.risk_management.risks.filter(r => r.risk_score >= 10 && r.risk_score < 15).length}
- **Mitigation Strategies**: ${framework.risk_management.mitigation_strategies.length}

## Compliance Management
- **Frameworks**: ${framework.compliance_management.frameworks.length}
- **Assessments**: ${framework.compliance_management.assessments.length}
- **Open Gaps**: ${framework.compliance_management.gaps.filter(g => g.priority === 'CRITICAL' || g.priority === 'HIGH').length}

## Change Management
- **Total Changes**: ${framework.change_management.changes.length}
- **Pending Approval**: ${framework.change_management.changes.filter(c => c.status === 'PENDING_APPROVAL').length}
- **Implemented**: ${framework.change_management.changes.filter(c => c.status === 'IMPLEMENTED').length}
- **Emergency Changes**: ${framework.change_management.emergency_changes.length}

## Incident Management
- **Total Incidents**: ${framework.incident_management.incidents.length}
- **P0 (Critical)**: ${framework.incident_management.incidents.filter(i => i.severity === 'P0').length}
- **P1 (High)**: ${framework.incident_management.incidents.filter(i => i.severity === 'P1').length}
- **Open Incidents**: ${framework.incident_management.incidents.filter(i => i.status !== 'RESOLVED' && i.status !== 'CLOSED').length}
- **Resolved**: ${framework.incident_management.incidents.filter(i => i.status === 'RESOLVED' || i.status === 'CLOSED').length}

## Data Governance
- **Total Datasets**: ${framework.data_governance.data_catalog.total_datasets}
- **Total Data Size**: ${framework.data_governance.data_catalog.total_data_size_gb.toFixed(2)} GB
- **Data Quality Score**: ${framework.data_governance.data_quality.overall_score}/100
- **Privacy Regulations**: ${framework.data_governance.data_privacy.regulations.length}

## Recommendations
${maturity.score < 60 ? '- Focus on establishing comprehensive policies and procedures' : ''}
${framework.risk_management.risks.filter(r => r.risk_score >= 15).length > 0 ? '- Address critical risks immediately' : ''}
${framework.incident_management.incidents.filter(i => i.status !== 'RESOLVED' && i.status !== 'CLOSED').length > 5 ? '- Improve incident resolution process' : ''}
`
}

/**
 * Export governance framework to JSON
 */
export function exportGovernanceJSON(framework: GovernanceFramework): string {
  return JSON.stringify(framework, null, 2)
}
