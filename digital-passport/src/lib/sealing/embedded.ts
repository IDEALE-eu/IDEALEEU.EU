/**
 * SEALING - Embedded Systems Management Module
 * Comprehensive utilities for embedded systems, firmware, and real-time operations
 */

import type {
  EmbeddedSystem,
  RealtimeTask,
  MessageDefinition,
  DiagnosticTroubleCode,
  CommunicationProfile,
} from './types'

/**
 * Create a new embedded system profile
 */
export function createEmbeddedSystem(
  systemId: string,
  name: string,
  type: 'MICROCONTROLLER' | 'MICROPROCESSOR' | 'SOC' | 'FPGA' | 'ASIC' | 'DSP',
  architecture: 'ARM' | 'X86' | 'RISCV' | 'MIPS' | 'POWER' | 'CUSTOM',
  cpuMhz: number,
  ramKb: number,
  flashKb: number
): EmbeddedSystem {
  return {
    system_id: systemId,
    name,
    type,
    hardware: {
      architecture,
      cpu_mhz: cpuMhz,
      cores: 1,
      ram_kb: ramKb,
      flash_kb: flashKb,
      peripherals: [],
      gpio_pins: 0,
      watchdog: true,
    },
    firmware: {
      version: '0.0.0',
      build_date: new Date().toISOString(),
      checksum: '',
      signature: '',
      size_bytes: 0,
      components: [],
      update_method: 'JTAG',
      rollback_supported: false,
    },
    realtime: {
      rtos: 'NONE',
      rtos_version: '',
      scheduling_algorithm: 'PRIORITY',
      tasks: [],
      worst_case_response_time_ms: 0,
      timing_analysis: {
        method: 'STATIC',
        analysis_date: new Date().toISOString(),
        schedulability: 'UNKNOWN',
        cpu_utilization_percent: 0,
        slack_time_ms: 0,
      },
    },
    safety: {
      safety_integrity_level: 'NONE',
      failure_mode: '',
      fault_detection: {
        mechanisms: ['WATCHDOG'],
        detection_time_ms: 1000,
        reaction: 'RESTART',
      },
      redundancy: {
        type: 'NONE',
        voting: 'NONE',
        diversity: 'NONE',
      },
      diagnostics_coverage_percent: 0,
    },
    power: {
      voltage_v: 3.3,
      voltage_tolerance_percent: 5,
      modes: [],
      current_consumption_ma: {
        typical_ma: 0,
        maximum_ma: 0,
        standby_ma: 0,
      },
      battery_operated: false,
      power_budget_mw: 0,
    },
    communications: [],
    diagnostics: {
      protocol: 'CUSTOM',
      dtcs: [],
      freeze_frames: false,
      live_data: false,
      routines: [],
    },
    boot: {
      stages: [],
      secure_boot: false,
      verified_boot: false,
      boot_time_ms: 0,
      recovery_mode: false,
    },
  }
}

/**
 * Add firmware component to embedded system
 */
export function addFirmwareComponent(
  system: EmbeddedSystem,
  name: string,
  version: string,
  type: 'RTOS' | 'DRIVER' | 'MIDDLEWARE' | 'APPLICATION' | 'BSP',
  codeSizeBytes: number,
  staticRamBytes: number,
  stackSizeBytes: number,
  criticality: 'DAL_A' | 'DAL_B' | 'DAL_C' | 'DAL_D' | 'DAL_E' | 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
): EmbeddedSystem {
  system.firmware.components.push({
    name,
    version,
    type,
    memory_usage: {
      code_size_bytes: codeSizeBytes,
      static_ram_bytes: staticRamBytes,
      stack_size_bytes: stackSizeBytes,
    },
    criticality,
  })

  // Update total firmware size
  system.firmware.size_bytes = system.firmware.components.reduce(
    (sum, c) => sum + c.memory_usage.code_size_bytes,
    0
  )

  return system
}

/**
 * Add real-time task to system
 */
export function addRealtimeTask(
  system: EmbeddedSystem,
  taskId: string,
  name: string,
  priority: number,
  periodMs: number | undefined,
  wcetMs: number,
  stackSizeBytes: number
): RealtimeTask {
  const task: RealtimeTask = {
    task_id: taskId,
    name,
    priority,
    period_ms: periodMs,
    deadline_ms: periodMs,
    wcet_ms: wcetMs,
    stack_size_bytes: stackSizeBytes,
    state: 'READY',
  }

  system.realtime.tasks.push(task)

  // Recalculate CPU utilization
  const utilization = system.realtime.tasks.reduce((sum, t) => {
    if (t.period_ms) {
      return sum + (t.wcet_ms / t.period_ms) * 100
    }
    return sum
  }, 0)

  system.realtime.timing_analysis.cpu_utilization_percent = utilization
  system.realtime.timing_analysis.schedulability = 
    utilization <= 100 ? 'SCHEDULABLE' : 'NOT_SCHEDULABLE'

  return task
}

/**
 * Validate real-time schedulability using Rate Monotonic Analysis (RMA)
 */
export function validateSchedulability(system: EmbeddedSystem): {
  schedulable: boolean
  utilization: number
  bound: number
  details: string
} {
  const tasks = system.realtime.tasks.filter(t => t.period_ms !== undefined)
  
  if (tasks.length === 0) {
    return {
      schedulable: true,
      utilization: 0,
      bound: 1,
      details: 'No periodic tasks to schedule',
    }
  }

  // Calculate CPU utilization
  const utilization = tasks.reduce((sum, t) => {
    return sum + (t.wcet_ms / t.period_ms!)
  }, 0)

  // Calculate RMA schedulability bound: n * (2^(1/n) - 1)
  const n = tasks.length
  const bound = n * (Math.pow(2, 1/n) - 1)

  const schedulable = utilization <= bound

  return {
    schedulable,
    utilization: utilization * 100,
    bound: bound * 100,
    details: schedulable
      ? `System is schedulable (U=${(utilization*100).toFixed(1)}% ≤ ${(bound*100).toFixed(1)}%)`
      : `System may not be schedulable (U=${(utilization*100).toFixed(1)}% > ${(bound*100).toFixed(1)}%)`,
  }
}

/**
 * Add communication protocol to system
 */
export function addCommunicationProtocol(
  system: EmbeddedSystem,
  protocol: 'CAN' | 'CANFD' | 'LIN' | 'FLEXRAY' | 'ETHERNET' | 'RS485' | 'MODBUS' | 'PROFIBUS' | 'MQTT' | 'COAP',
  speedBps: number,
  mode: 'MASTER' | 'SLAVE' | 'PEER',
  encryption: boolean = false
): CommunicationProfile {
  const comm: CommunicationProfile = {
    protocol,
    speed_bps: speedBps,
    mode,
    encryption,
    authentication: false,
    message_definitions: [],
  }

  system.communications.push(comm)

  return comm
}

/**
 * Add CAN message definition
 */
export function addCANMessage(
  comm: CommunicationProfile,
  msgId: string,
  name: string,
  direction: 'TX' | 'RX' | 'BOTH',
  periodMs: number | undefined,
  lengthBytes: number
): MessageDefinition {
  if (comm.protocol !== 'CAN' && comm.protocol !== 'CANFD') {
    throw new Error('Message definitions are only supported for CAN/CANFD protocols')
  }

  const message: MessageDefinition = {
    msg_id: msgId,
    name,
    direction,
    period_ms: periodMs,
    length_bytes: lengthBytes,
    signals: [],
  }

  comm.message_definitions.push(message)

  return message
}

/**
 * Add signal to CAN message
 */
export function addSignal(
  message: MessageDefinition,
  name: string,
  startBit: number,
  lengthBits: number,
  byteOrder: 'LITTLE_ENDIAN' | 'BIG_ENDIAN',
  type: 'UNSIGNED' | 'SIGNED' | 'FLOAT' | 'ENUM',
  scale?: number,
  offset?: number,
  unit?: string
): MessageDefinition {
  message.signals.push({
    name,
    start_bit: startBit,
    length_bits: lengthBits,
    byte_order: byteOrder,
    type,
    scale,
    offset,
    unit,
  })

  return message
}

/**
 * Add diagnostic trouble code (DTC)
 */
export function addDTC(
  system: EmbeddedSystem,
  code: string,
  description: string,
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW',
  triggerCondition: string,
  correctiveAction: string
): DiagnosticTroubleCode {
  const dtc: DiagnosticTroubleCode = {
    code,
    description,
    severity,
    trigger_condition: triggerCondition,
    effects: '',
    corrective_action: correctiveAction,
  }

  system.diagnostics.dtcs.push(dtc)

  return dtc
}

/**
 * Configure secure boot
 */
export function configureSecureBoot(
  system: EmbeddedSystem,
  bootStages: {
    stage: number
    name: string
    durationMs: number
    checksumVerification: boolean
    signatureVerification: boolean
  }[]
): EmbeddedSystem {
  system.boot.secure_boot = bootStages.some(s => s.signatureVerification)
  system.boot.verified_boot = bootStages.some(s => s.checksumVerification)
  system.boot.stages = bootStages.map(s => ({
    stage: s.stage,
    name: s.name,
    duration_ms: s.durationMs,
    checksum_verification: s.checksumVerification,
    signature_verification: s.signatureVerification,
  }))
  system.boot.boot_time_ms = bootStages.reduce((sum, s) => sum + s.durationMs, 0)

  return system
}

/**
 * Calculate memory usage statistics
 */
export function calculateMemoryUsage(system: EmbeddedSystem): {
  flash_used_kb: number
  flash_free_kb: number
  flash_percent: number
  ram_used_kb: number
  ram_free_kb: number
  ram_percent: number
  details: {
    firmware_kb: number
    static_kb: number
    stack_kb: number
    heap_kb: number
  }
} {
  // Calculate flash usage
  const flashUsedBytes = system.firmware.components.reduce(
    (sum, c) => sum + c.memory_usage.code_size_bytes,
    0
  )
  const flashUsedKb = flashUsedBytes / 1024
  const flashFreeKb = system.hardware.flash_kb - flashUsedKb
  const flashPercent = (flashUsedKb / system.hardware.flash_kb) * 100

  // Calculate RAM usage
  const staticRamBytes = system.firmware.components.reduce(
    (sum, c) => sum + c.memory_usage.static_ram_bytes,
    0
  )
  const stackBytes = system.firmware.components.reduce(
    (sum, c) => sum + c.memory_usage.stack_size_bytes,
    0
  )
  const heapBytes = system.firmware.components.reduce(
    (sum, c) => sum + (c.memory_usage.heap_size_bytes || 0),
    0
  )

  const totalRamBytes = staticRamBytes + stackBytes + heapBytes
  const ramUsedKb = totalRamBytes / 1024
  const ramFreeKb = system.hardware.ram_kb - ramUsedKb
  const ramPercent = (ramUsedKb / system.hardware.ram_kb) * 100

  return {
    flash_used_kb: flashUsedKb,
    flash_free_kb: flashFreeKb,
    flash_percent: flashPercent,
    ram_used_kb: ramUsedKb,
    ram_free_kb: ramFreeKb,
    ram_percent: ramPercent,
    details: {
      firmware_kb: flashUsedKb,
      static_kb: staticRamBytes / 1024,
      stack_kb: stackBytes / 1024,
      heap_kb: heapBytes / 1024,
    },
  }
}

/**
 * Calculate power consumption estimate
 */
export function calculatePowerConsumption(
  system: EmbeddedSystem,
  activeTimePercent: number = 100
): {
  average_ma: number
  average_mw: number
  daily_mah: number
  battery_life_days?: number
} {
  const activeMa = system.power.current_consumption_ma.typical_ma
  const standbyMa = system.power.current_consumption_ma.standby_ma
  
  const averageMa = (activeMa * activeTimePercent + standbyMa * (100 - activeTimePercent)) / 100
  const averageMw = averageMa * system.power.voltage_v

  // Daily consumption in mAh
  const dailyMah = (averageMa * 24)

  return {
    average_ma: averageMa,
    average_mw: averageMw,
    daily_mah: dailyMah,
  }
}

/**
 * Validate safety requirements for embedded system
 */
export function validateSafetyRequirements(system: EmbeddedSystem): {
  compliant: boolean
  checks: { requirement: string; satisfied: boolean; details: string }[]
} {
  const checks = []
  const sil = system.safety.safety_integrity_level

  // Check watchdog
  checks.push({
    requirement: 'Hardware Watchdog',
    satisfied: system.hardware.watchdog,
    details: system.hardware.watchdog
      ? 'Watchdog enabled'
      : 'Watchdog required for safety-critical systems',
  })

  // Check fault detection
  const requiredMechanisms = ['CRC', 'WATCHDOG']
  const hasRequired = requiredMechanisms.every(m => 
    system.safety.fault_detection.mechanisms.includes(m as any)
  )
  checks.push({
    requirement: 'Fault Detection Mechanisms',
    satisfied: hasRequired,
    details: hasRequired
      ? `All required mechanisms present: ${system.safety.fault_detection.mechanisms.join(', ')}`
      : `Missing required mechanisms: ${requiredMechanisms.join(', ')}`,
  })

  // Check diagnostics coverage for high safety levels
  if (sil.includes('ASIL') || sil.includes('SIL')) {
    const requiredCoverage = sil.includes('ASIL_D') || sil.includes('SIL_4') ? 99 :
                              sil.includes('ASIL_C') || sil.includes('SIL_3') ? 90 :
                              sil.includes('ASIL_B') || sil.includes('SIL_2') ? 60 : 60
    checks.push({
      requirement: 'Diagnostics Coverage',
      satisfied: system.safety.diagnostics_coverage_percent >= requiredCoverage,
      details: `Coverage: ${system.safety.diagnostics_coverage_percent}% (required: ${requiredCoverage}%)`,
    })
  }

  // Check redundancy for high safety levels
  if (sil.includes('ASIL_C') || sil.includes('ASIL_D') || sil.includes('SIL_3') || sil.includes('SIL_4')) {
    checks.push({
      requirement: 'Redundancy',
      satisfied: system.safety.redundancy.type !== 'NONE',
      details: system.safety.redundancy.type !== 'NONE'
        ? `Redundancy configured: ${system.safety.redundancy.type}`
        : 'Redundancy required for high safety levels',
    })
  }

  // Check secure boot for safety systems
  if (sil !== 'NONE') {
    checks.push({
      requirement: 'Secure Boot',
      satisfied: system.boot.secure_boot || system.boot.verified_boot,
      details: system.boot.secure_boot || system.boot.verified_boot
        ? 'Boot integrity verification enabled'
        : 'Boot verification recommended for safety systems',
    })
  }

  const allSatisfied = checks.every(c => c.satisfied)

  return {
    compliant: allSatisfied,
    checks,
  }
}

/**
 * Generate DBC (CAN Database) file content
 */
export function generateDBCFile(system: EmbeddedSystem): string {
  const canComm = system.communications.find(c => c.protocol === 'CAN' || c.protocol === 'CANFD')
  
  if (!canComm) {
    throw new Error('No CAN/CANFD communication protocol found')
  }

  let dbc = `VERSION ""\n\n`
  dbc += `NS_ :\n\tNS_DESC_\n\tCM_\n\tBA_DEF_\n\tBA_\n\tVAL_\n\tCAT_DEF_\n\tCAT_\n\tFILTER\n\tBA_DEF_DEF_\n\tEV_DATA_\n\tENVVAR_DATA_\n\tSGTYPE_\n\tSGTYPE_VAL_\n\tBA_DEF_SGTYPE_\n\tBA_SGTYPE_\n\tSIG_TYPE_REF_\n\tVAL_TABLE_\n\tSIG_GROUP_\n\tSIG_VALTYPE_\n\tSIGTYPE_VALTYPE_\n\tBO_TX_BU_\n\tBA_DEF_REL_\n\tBA_REL_\n\tBA_SGTYPE_REL_\n\tSG_MUL_VAL_\n\n`
  dbc += `BS_:\n\n`
  dbc += `BU_: ECU\n\n`

  // Add messages
  canComm.message_definitions.forEach(msg => {
    const msgId = parseInt(msg.msg_id, 16) || parseInt(msg.msg_id)
    dbc += `BO_ ${msgId} ${msg.name}: ${msg.length_bytes} ECU\n`

    // Add signals
    msg.signals.forEach(sig => {
      const byteOrder = sig.byte_order === 'LITTLE_ENDIAN' ? '1' : '0'
      const signedness = sig.type === 'SIGNED' ? '-' : '+'
      const scale = sig.scale || 1
      const offset = sig.offset || 0
      dbc += ` SG_ ${sig.name} : ${sig.start_bit}|${sig.length_bits}@${byteOrder}${signedness} (${scale},${offset}) [0|0] "${sig.unit || ''}" ECU\n`
    })

    dbc += `\n`
  })

  return dbc
}

/**
 * Export embedded system configuration to JSON
 */
export function exportEmbeddedSystemJSON(system: EmbeddedSystem): string {
  return JSON.stringify(system, null, 2)
}
