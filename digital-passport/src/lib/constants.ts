import type { TFADomain, CAXPhase, State, VerificationStatus, ComponentType } from '@/types'

export const DOMAIN_NAMES: Record<TFADomain, string> = {
  AAA: 'Airframes-Aerodynamics-Airworthiness',
  AAP: 'Airport-Adaptable-Platforms',
  CCC: 'Cockpit-Cabin-Cargo',
  CQH: 'Cryogenics-Quantum-H2',
  DDD: 'Drainage-Dehumidification-Drying',
  EDI: 'Electronics-Digital-Instruments',
  EEE: 'Electrical-Endocircular-Energization',
  EER: 'Environmental-Emissions-Remediation',
  IIF: 'Industrial-Infrastructure-Facilities',
  IIS: 'Information-Intelligence-Systems',
  LCC: 'Linkages-Control-Communications',
  LIB: 'Logistics-Inventory-Blockchain',
  MMM: 'Mechanical-Material-Modules',
  OOO: 'Operations-Optimization-Outcomes',
  PPP: 'Propellers-Propellents-Propulsion',
}

export const PHASE_NAMES: Record<CAXPhase, string> = {
  CAD: 'Design',
  CAE: 'Analysis',
  CAI: 'Integration',
  CAO: 'Optimization',
  CAM: 'Manufacturing',
  CAP: 'Planning',
  CAV: 'Validation',
  CMP: 'Compliance',
  CAS: 'Services',
}

export const STATE_NAMES: Record<State, string> = {
  QS: 'Quantum Superposition',
  FWD: 'Future/Waves Dynamics',
  UE: 'Unit Element',
  FE: 'Federation Entanglement',
  CB: 'Classical Bit',
  QB: 'Qubit',
}

export const STATUS_LABELS: Record<VerificationStatus, string> = {
  verified: 'Verified',
  pending: 'Pending',
  failed: 'Failed',
  expired: 'Expired',
  drift: 'Checksum Drift',
}

export const COMPONENT_TYPE_LABELS: Record<ComponentType, string> = {
  hardware: 'Hardware',
  software: 'Software',
  firmware: 'Firmware',
  model: 'Model',
}

export function getDomainColor(domain: TFADomain): string {
  const colors: Record<TFADomain, string> = {
    AAA: 'oklch(0.55 0.15 250)',
    AAP: 'oklch(0.60 0.12 280)',
    CCC: 'oklch(0.50 0.18 320)',
    CQH: 'oklch(0.45 0.20 300)',
    DDD: 'oklch(0.58 0.14 200)',
    EDI: 'oklch(0.52 0.16 260)',
    EEE: 'oklch(0.62 0.17 95)',
    EER: 'oklch(0.56 0.18 145)',
    IIF: 'oklch(0.48 0.12 240)',
    IIS: 'oklch(0.54 0.15 290)',
    LCC: 'oklch(0.60 0.16 50)',
    LIB: 'oklch(0.50 0.14 310)',
    MMM: 'oklch(0.52 0.12 220)',
    OOO: 'oklch(0.58 0.15 180)',
    PPP: 'oklch(0.56 0.19 25)',
  }
  return colors[domain]
}

export function getStatusColor(status: VerificationStatus): string {
  const colors: Record<VerificationStatus, string> = {
    verified: 'oklch(0.65 0.15 145)',
    pending: 'oklch(0.72 0.14 95)',
    failed: 'oklch(0.55 0.20 25)',
    expired: 'oklch(0.60 0.02 260)',
    drift: 'oklch(0.68 0.18 65)',
  }
  return colors[status]
}

export function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

export function formatDateTime(dateString: string): string {
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}
