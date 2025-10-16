/**
 * SEALING - Network Infrastructure and Security Module
 * Comprehensive utilities for network management, security, and monitoring
 */

import type {
  NetworkInfrastructure,
  NetworkDevice,
  Subnet,
  FirewallRule,
  Certificate,
  VPNTunnel,
  AccessPolicy,
} from './types'

/**
 * Create a new network infrastructure
 */
export function createNetworkInfrastructure(
  networkId: string,
  name: string,
  type: 'LAN' | 'WAN' | 'VPN' | 'SDN' | 'MESH' | 'SATELLITE' | 'CELLULAR'
): NetworkInfrastructure {
  return {
    network_id: networkId,
    name,
    type,
    topology: {
      type: 'STAR',
      subnets: [],
      routes: [],
      redundancy: 'NONE',
    },
    security: {
      firewall: {
        type: 'STATEFUL',
        rules: [],
        default_policy: 'DENY',
        logging: true,
      },
      ids_ips: {
        enabled: false,
        mode: 'IDS',
        signatures_version: '',
        policies: [],
        alerts: [],
      },
      vpn: {
        protocol: 'IPSEC',
        encryption: 'AES256',
        authentication: 'PSK',
        tunnels: [],
      },
      certificates: [],
      access_policies: [],
      threat_intelligence: {
        feeds: [],
        indicators: [],
        last_updated: new Date().toISOString(),
      },
    },
    performance: {
      bandwidth: {
        capacity_mbps: 0,
        utilization_percent: 0,
        ingress_mbps: 0,
        egress_mbps: 0,
        peak_utilization_percent: 0,
      },
      latency: {
        average_ms: 0,
        p50_ms: 0,
        p95_ms: 0,
        p99_ms: 0,
        max_ms: 0,
      },
      packet_loss: 0,
      jitter_ms: 0,
      availability_percent: 99.9,
      sla_compliance: true,
    },
    devices: [],
    services: [],
    monitoring: {
      tools: [],
      metrics: [],
      events: [],
      topology_map: '',
    },
  }
}

/**
 * Add subnet to network
 */
export function addSubnet(
  network: NetworkInfrastructure,
  cidr: string,
  vlan?: number,
  gateway?: string,
  dnsServers: string[] = [],
  dhcpEnabled: boolean = true
): Subnet {
  const subnet: Subnet = {
    subnet_id: `SUBNET-${Date.now()}`,
    cidr,
    vlan,
    gateway: gateway || cidr.split('/')[0],
    dns_servers: dnsServers,
    dhcp_enabled: dhcpEnabled,
  }

  network.topology.subnets.push(subnet)

  return subnet
}

/**
 * Add firewall rule
 */
export function addFirewallRule(
  network: NetworkInfrastructure,
  priority: number,
  source: string,
  destination: string,
  port: number | string,
  protocol: 'TCP' | 'UDP' | 'ICMP' | 'ANY',
  action: 'ALLOW' | 'DENY' | 'LOG'
): FirewallRule {
  const rule: FirewallRule = {
    rule_id: `FW-${Date.now()}`,
    priority,
    source,
    destination,
    port,
    protocol,
    action,
    enabled: true,
  }

  network.security.firewall.rules.push(rule)
  
  // Sort rules by priority
  network.security.firewall.rules.sort((a, b) => a.priority - b.priority)

  return rule
}

/**
 * Add network device
 */
export function addNetworkDevice(
  network: NetworkInfrastructure,
  deviceId: string,
  name: string,
  type: 'ROUTER' | 'SWITCH' | 'FIREWALL' | 'LOAD_BALANCER' | 'ACCESS_POINT' | 'GATEWAY',
  model: string,
  firmwareVersion: string,
  managementIp: string,
  location: string
): NetworkDevice {
  const device: NetworkDevice = {
    device_id: deviceId,
    name,
    type,
    model,
    firmware_version: firmwareVersion,
    management_ip: managementIp,
    location,
    interfaces: [],
    status: 'ONLINE',
  }

  network.devices.push(device)

  return device
}

/**
 * Add VPN tunnel
 */
export function addVPNTunnel(
  network: NetworkInfrastructure,
  localEndpoint: string,
  remoteEndpoint: string
): VPNTunnel {
  const tunnel: VPNTunnel = {
    tunnel_id: `VPN-${Date.now()}`,
    local_endpoint: localEndpoint,
    remote_endpoint: remoteEndpoint,
    status: 'UP',
    established_at: new Date().toISOString(),
    traffic_bytes: 0,
  }

  network.security.vpn.tunnels.push(tunnel)

  return tunnel
}

/**
 * Add SSL/TLS certificate
 */
export function addCertificate(
  network: NetworkInfrastructure,
  type: 'SSL_TLS' | 'CODE_SIGNING' | 'CLIENT' | 'ROOT_CA' | 'INTERMEDIATE_CA',
  subject: string,
  issuer: string,
  validFrom: string,
  validUntil: string,
  serialNumber: string,
  fingerprint: string,
  keySizeBits: number = 2048,
  algorithm: string = 'RSA'
): Certificate {
  const now = new Date()
  const validFromDate = new Date(validFrom)
  const validUntilDate = new Date(validUntil)

  const status: 'VALID' | 'EXPIRED' | 'PENDING' =
    now < validFromDate ? 'PENDING' :
    now > validUntilDate ? 'EXPIRED' :
    'VALID'

  const cert: Certificate = {
    cert_id: `CERT-${Date.now()}`,
    type,
    subject,
    issuer,
    valid_from: validFrom,
    valid_until: validUntil,
    serial_number: serialNumber,
    fingerprint,
    key_size_bits: keySizeBits,
    algorithm,
    status,
  }

  network.security.certificates.push(cert)

  return cert
}

/**
 * Add access policy
 */
export function addAccessPolicy(
  network: NetworkInfrastructure,
  name: string,
  type: 'INGRESS' | 'EGRESS' | 'INTERNAL',
  subjects: string[],
  resources: string[],
  actions: string[],
  effect: 'ALLOW' | 'DENY'
): AccessPolicy {
  const policy: AccessPolicy = {
    policy_id: `POLICY-${Date.now()}`,
    name,
    type,
    subjects,
    resources,
    actions,
    effect,
  }

  network.security.access_policies.push(policy)

  return policy
}

/**
 * Check certificate expiration
 */
export function checkCertificateExpiration(
  network: NetworkInfrastructure,
  warningDays: number = 30
): {
  expired: Certificate[]
  expiring_soon: Certificate[]
  valid: Certificate[]
} {
  const now = new Date()
  const warningDate = new Date(now.getTime() + warningDays * 24 * 60 * 60 * 1000)

  const expired: Certificate[] = []
  const expiring_soon: Certificate[] = []
  const valid: Certificate[] = []

  network.security.certificates.forEach(cert => {
    const expiryDate = new Date(cert.valid_until)
    
    if (expiryDate < now) {
      expired.push(cert)
    } else if (expiryDate < warningDate) {
      expiring_soon.push(cert)
    } else {
      valid.push(cert)
    }
  })

  return { expired, expiring_soon, valid }
}

/**
 * Calculate network security score
 */
export function calculateSecurityScore(network: NetworkInfrastructure): {
  score: number
  grade: 'A' | 'B' | 'C' | 'D' | 'F'
  factors: { factor: string; points: number; max: number; details: string }[]
} {
  const factors = []
  let totalScore = 0

  // Firewall configuration (0-20 points)
  const hasFirewall = network.security.firewall.rules.length > 0
  const firewallPoints = hasFirewall ? 20 : 0
  factors.push({
    factor: 'Firewall Configuration',
    points: firewallPoints,
    max: 20,
    details: hasFirewall ? `${network.security.firewall.rules.length} rules configured` : 'No firewall rules',
  })
  totalScore += firewallPoints

  // IDS/IPS (0-15 points)
  const idsIpsPoints = network.security.ids_ips.enabled ? 15 : 0
  factors.push({
    factor: 'IDS/IPS',
    points: idsIpsPoints,
    max: 15,
    details: network.security.ids_ips.enabled ? `${network.security.ids_ips.mode} enabled` : 'Not enabled',
  })
  totalScore += idsIpsPoints

  // VPN Configuration (0-15 points)
  const hasVPN = network.security.vpn.tunnels.length > 0
  const vpnPoints = hasVPN ? 15 : 0
  factors.push({
    factor: 'VPN/Encryption',
    points: vpnPoints,
    max: 15,
    details: hasVPN ? `${network.security.vpn.tunnels.length} tunnels active` : 'No VPN configured',
  })
  totalScore += vpnPoints

  // Certificate Management (0-15 points)
  const certStatus = checkCertificateExpiration(network)
  const hasCerts = network.security.certificates.length > 0
  const certPoints = hasCerts && certStatus.expired.length === 0 ? 15 : hasCerts ? 7 : 0
  factors.push({
    factor: 'Certificate Management',
    points: certPoints,
    max: 15,
    details: hasCerts 
      ? `${certStatus.valid.length} valid, ${certStatus.expired.length} expired, ${certStatus.expiring_soon.length} expiring soon`
      : 'No certificates managed',
  })
  totalScore += certPoints

  // Access Control (0-20 points)
  const hasAccessPolicies = network.security.access_policies.length > 0
  const accessPoints = hasAccessPolicies ? 20 : 0
  factors.push({
    factor: 'Access Control',
    points: accessPoints,
    max: 20,
    details: hasAccessPolicies ? `${network.security.access_policies.length} policies defined` : 'No access policies',
  })
  totalScore += accessPoints

  // Threat Intelligence (0-15 points)
  const hasThreatIntel = network.security.threat_intelligence.feeds.length > 0
  const threatPoints = hasThreatIntel ? 15 : 0
  factors.push({
    factor: 'Threat Intelligence',
    points: threatPoints,
    max: 15,
    details: hasThreatIntel ? `${network.security.threat_intelligence.feeds.length} feeds active` : 'No threat intel feeds',
  })
  totalScore += threatPoints

  // Determine grade
  const grade: 'A' | 'B' | 'C' | 'D' | 'F' =
    totalScore >= 90 ? 'A' :
    totalScore >= 80 ? 'B' :
    totalScore >= 70 ? 'C' :
    totalScore >= 60 ? 'D' :
    'F'

  return {
    score: totalScore,
    grade,
    factors,
  }
}

/**
 * Generate network diagram in Mermaid format
 */
export function generateNetworkDiagram(network: NetworkInfrastructure): string {
  let diagram = 'graph TD\n'
  
  // Add devices
  network.devices.forEach(device => {
    const icon = 
      device.type === 'ROUTER' ? '((Router))' :
      device.type === 'SWITCH' ? '[Switch]' :
      device.type === 'FIREWALL' ? '{Firewall}' :
      device.type === 'LOAD_BALANCER' ? '{{Load Balancer}}' :
      device.type === 'ACCESS_POINT' ? '(((AP)))' :
      '[Gateway]'
    
    diagram += `    ${device.device_id}${icon}\n`
  })

  // Add subnets
  network.topology.subnets.forEach((subnet, i) => {
    diagram += `    SUBNET${i}[Subnet: ${subnet.cidr}]\n`
  })

  // Add connections (simplified)
  if (network.devices.length > 0) {
    for (let i = 0; i < network.devices.length - 1; i++) {
      diagram += `    ${network.devices[i].device_id} --> ${network.devices[i + 1].device_id}\n`
    }
  }

  return diagram
}

/**
 * Export network configuration to JSON
 */
export function exportNetworkJSON(network: NetworkInfrastructure): string {
  return JSON.stringify(network, null, 2)
}

/**
 * Validate network security configuration
 */
export function validateNetworkSecurity(network: NetworkInfrastructure): {
  compliant: boolean
  checks: { check: string; passed: boolean; message: string }[]
} {
  const checks = []

  // Check firewall configuration
  checks.push({
    check: 'Firewall Rules',
    passed: network.security.firewall.rules.length > 0,
    message: network.security.firewall.rules.length > 0
      ? `${network.security.firewall.rules.length} rules configured`
      : 'No firewall rules configured',
  })

  // Check default deny policy
  checks.push({
    check: 'Default Deny Policy',
    passed: network.security.firewall.default_policy === 'DENY',
    message: network.security.firewall.default_policy === 'DENY'
      ? 'Secure default policy in place'
      : 'Insecure default policy (should be DENY)',
  })

  // Check certificate expiration
  const certStatus = checkCertificateExpiration(network)
  checks.push({
    check: 'Certificate Validity',
    passed: certStatus.expired.length === 0,
    message: certStatus.expired.length === 0
      ? 'All certificates valid'
      : `${certStatus.expired.length} certificates expired`,
  })

  // Check VPN encryption
  const hasStrongEncryption = network.security.vpn.encryption.includes('AES256') || network.security.vpn.encryption.includes('AES-256')
  checks.push({
    check: 'VPN Encryption',
    passed: hasStrongEncryption,
    message: hasStrongEncryption
      ? 'Strong encryption configured'
      : `Weak encryption: ${network.security.vpn.encryption}`,
  })

  // Check monitoring
  checks.push({
    check: 'Network Monitoring',
    passed: network.monitoring.tools.length > 0,
    message: network.monitoring.tools.length > 0
      ? `${network.monitoring.tools.length} monitoring tools active`
      : 'No monitoring tools configured',
  })

  const allPassed = checks.every(c => c.passed)

  return {
    compliant: allPassed,
    checks,
  }
}
