/**
 * SEALING - Embedded Systems Type Definitions
 * 
 * Comprehensive data structures for embedded systems including hardware
 * specifications, firmware, communication interfaces, and diagnostics.
 */

import { SoftwareComponent } from './software';

// ============================================================================
// Core Identification
// ============================================================================

export interface EmbeddedIdentification {
  name: string;
  part_number: string;
  hardware_revision: string;
  firmware_version: string;
  domain: string; // e.g., 'LCC', 'EDI', 'EEE'
  description?: string;
}

// ============================================================================
// Hardware Specifications
// ============================================================================

export interface MCU {
  manufacturer: string;
  part_number: string;
  architecture: 'ARM' | 'RISC-V' | 'x86' | 'AVR' | 'PIC' | 'PowerPC';
  cores: number;
  clock_speed_mhz: number;
  features: {
    fpu: boolean;
    dsp: boolean;
    crypto: boolean;
    secure_boot: boolean;
  };
}

export interface Memory {
  flash?: {
    size_kb: number;
    ecc: boolean;
    type?: 'NOR' | 'NAND';
  };
  ram?: {
    size_kb: number;
    ecc: boolean;
    type?: 'SRAM' | 'DRAM' | 'SDRAM';
  };
  eeprom?: {
    size_kb: number;
  };
  external_storage?: {
    type: 'SD' | 'MMC' | 'NVMe' | 'SSD';
    size_gb: number;
  };
}

export interface Peripheral {
  peripheral_id: string;
  type: 'CAN' | 'UART' | 'SPI' | 'I2C' | 'USB' | 'ETHERNET' | 'ADC' | 'DAC' | 'GPIO' | 'TIMER' | 'PWM';
  instance: number;
  configuration: Record<string, any>;
  connected_to?: string;
}

export interface PowerRequirements {
  voltage_v: number;
  current_typical_ma: number;
  current_max_ma: number;
  power_modes?: Array<{
    mode: 'ACTIVE' | 'IDLE' | 'SLEEP' | 'DEEP_SLEEP' | 'SHUTDOWN';
    current_ma: number;
    wakeup_time_ms: number;
  }>;
}

export interface HardwareInfo {
  mcu: MCU;
  memory: Memory;
  peripherals: Peripheral[];
  power: PowerRequirements;
  environmental_rating?: {
    temp_min_c: number;
    temp_max_c: number;
    humidity_max_percent: number;
    vibration_g: number;
  };
}

// ============================================================================
// Software/Firmware
// ============================================================================

export interface FirmwareInfo {
  bootloader?: SoftwareComponent;
  firmware: SoftwareComponent;
  runtime: 'BARE_METAL' | 'RTOS' | 'LINUX' | 'RTOS_FREERTOS' | 'RTOS_ZEPHYR' | 'RTOS_THREADX';
  applications?: SoftwareComponent[];
}

// ============================================================================
// Communication
// ============================================================================

export interface CommunicationInterface {
  interface_id: string;
  type: 'CAN' | 'ETHERNET' | 'WIFI' | 'BLUETOOTH' | 'ZIGBEE' | 'LORA' | 'SERIAL' | 'USB';
  physical_layer: string; // e.g., 'ISO 11898', '802.3', '802.11ax'
  data_rate: string; // e.g., '1 Mbps', '100 Mbps'
  redundant: boolean;
}

export interface CommunicationProtocol {
  protocol_name: string;
  version: string;
  layer: 'PHYSICAL' | 'DATA_LINK' | 'NETWORK' | 'TRANSPORT' | 'APPLICATION';
  specification: string; // e.g., 'ARINC-825', 'CANopen', 'Modbus'
}

export interface CommunicationInfo {
  interfaces: CommunicationInterface[];
  protocols: CommunicationProtocol[];
}

// ============================================================================
// Safety Features
// ============================================================================

export interface SafetyInfo {
  criticality: 'DAL_A' | 'DAL_B' | 'DAL_C' | 'DAL_D' | 'DAL_E' | 'ASIL_A' | 'ASIL_B' | 'ASIL_C' | 'ASIL_D' | 'SIL_1' | 'SIL_2' | 'SIL_3' | 'SIL_4';
  watchdog: boolean;
  redundancy: 'NONE' | 'DUAL' | 'TRIPLE' | 'QUAD';
  self_test: {
    enabled: boolean;
    tests: {
      ram_test: boolean;
      flash_test: boolean;
      peripheral_test: boolean;
      communication_test: boolean;
    };
    frequency: 'BOOT' | 'PERIODIC' | 'ON_DEMAND';
    interval_seconds?: number;
  };
  fault_handling?: {
    strategy: 'RESET' | 'SAFE_STATE' | 'DEGRADED_MODE' | 'NOTIFICATION_ONLY';
    safe_state_description?: string;
  };
}

// ============================================================================
// OTA (Over-The-Air) Updates
// ============================================================================

export interface OTAInfo {
  method: 'CAN' | 'ETHERNET' | 'WIFI' | 'CELLULAR' | 'USB';
  bootloader: {
    secure: boolean;
    rollback_protection: boolean;
    signature_verification: boolean;
  };
  update_policy: {
    auto_update: boolean;
    require_approval: boolean;
    rollback_on_failure: boolean;
    max_retry_attempts?: number;
  };
}

// ============================================================================
// Diagnostics
// ============================================================================

export interface DiagnosticTroubleCode {
  dtc_code: string;
  description: string;
  severity: 'CRITICAL' | 'WARNING' | 'INFO';
  action: string;
}

export interface TelemetryMetric {
  metric_name: string;
  type: 'COUNTER' | 'GAUGE' | 'HISTOGRAM' | 'SUMMARY';
  unit: string;
  threshold?: {
    warning: number;
    critical: number;
  };
}

export interface DiagnosticInfo {
  dtc_enabled: boolean;
  dtc_codes?: DiagnosticTroubleCode[];
  logging: {
    level: 'DEBUG' | 'INFO' | 'WARNING' | 'ERROR' | 'CRITICAL';
    destinations: Array<'UART' | 'CAN' | 'ETHERNET' | 'FLASH' | 'SD_CARD'>;
  };
  telemetry?: {
    enabled: boolean;
    metrics: TelemetryMetric[];
    reporting_interval_seconds: number;
  };
}

// ============================================================================
// Main Embedded System Interface
// ============================================================================

export interface EmbeddedSystem {
  // Identification
  system_id: string;
  utcs_ref: string; // e.g., "UTCS-LCC/FCC-001@1.0.0"
  identification: EmbeddedIdentification;

  // Hardware
  hardware: HardwareInfo;

  // Software/Firmware
  software: FirmwareInfo;

  // Communication
  communication: CommunicationInfo;

  // Safety
  safety: SafetyInfo;

  // Deployment
  deployment?: OTAInfo;

  // Diagnostics
  diagnostics?: DiagnosticInfo;

  // Metadata
  created_date: string;
  last_modified_date: string;
  owner: string;
  documentation_uri?: string;

  // Relationships
  parent_prd?: string; // Reference to PRD document
  related_systems?: string[]; // Other system IDs
  subsystems?: EmbeddedSystem[]; // Child embedded systems
}

// ============================================================================
// Helper Functions
// ============================================================================

export function calculatePowerConsumption(system: EmbeddedSystem, mode: string = 'ACTIVE'): number {
  const powerMode = system.hardware.power.power_modes?.find(pm => pm.mode === mode);
  if (powerMode) {
    return (system.hardware.power.voltage_v * powerMode.current_ma) / 1000; // Watts
  }
  return (system.hardware.power.voltage_v * system.hardware.power.current_typical_ma) / 1000;
}

export function getMemoryUtilization(system: EmbeddedSystem): {
  flash_used_percent?: number;
  ram_used_percent?: number;
} {
  // This would be populated from runtime telemetry
  return {};
}

export function validateEmbeddedSystem(system: EmbeddedSystem): {
  valid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (!system.system_id) errors.push('system_id is required');
  if (!system.utcs_ref) errors.push('utcs_ref is required');
  if (!system.identification?.name) errors.push('identification.name is required');
  if (!system.hardware?.mcu) errors.push('hardware.mcu is required');
  if (!system.software?.firmware) errors.push('software.firmware is required');
  if (!system.safety?.criticality) errors.push('safety.criticality is required');

  return {
    valid: errors.length === 0,
    errors
  };
}

export function generateDTCFromError(
  error: Error,
  severity: 'CRITICAL' | 'WARNING' | 'INFO'
): DiagnosticTroubleCode {
  return {
    dtc_code: `DTC-${Date.now()}`,
    description: error.message,
    severity,
    action: 'Review system logs and take appropriate action'
  };
}
