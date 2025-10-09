# 06-DIMENSIONS-STATIONS System Documentation

![Validation Status](https://img.shields.io/badge/structure-valid-success)

## Overview
Sistema ATA-06 DIMENSIONS-STATIONS define la geometría de referencia, sistemas de coordenadas, estaciones de medición y puntos de control dimensional para el aircraft AMPEL360-AIR-T modelo BWB Q100.

## Directory Structure

```
06-DIMENSIONS-STATIONS/
├── INTEGRATION_VIEW.md                    # Vista de integración del sistema
├── INTERFACE_MATRIX/                      # Matrices de interfaces
│   └── 06-DIMENSIONS-STATIONS↔OTROS.csv  # Interfaces con otros sistemas ATA
├── SUBSYSTEMS/                            # Subsistemas del sistema 06
│   ├── 06-10_REFERENCE_FRAMES/           # Ejes de referencia, puntos datum
│   ├── 06-20_MEASUREMENT_POINTS/         # Estaciones físicas, puntos de medición
│   ├── 06-30_ALIGNMENT_TARGETS/          # Targets ópticos, fiduciales
│   ├── 06-40_CALIBRATION_PROTOCOLS/      # Procedimientos de calibración
│   └── 06-50_GEOMETRIC_MODELS/           # Modelos CAD nominales, digital twin
└── README.md                              # Este archivo
```

## Subsystems

### 06-10_REFERENCE_FRAMES
**Purpose**: Definición de ejes, puntos de referencia, alineamientos globales

- Sistema de coordenadas global del aircraft
- Puntos de referencia principales (datum points)
- Ejes de alineamiento para fabricación y ensamblaje
- Marcos de referencia para mediciones y tolerancias

**Key Interfaces**: ATA-51 (Estructuras), ATA-70 (Motores), ATA-32 (Landing Gear)

### 06-20_MEASUREMENT_POINTS
**Purpose**: Estaciones físicas, puntos de medición, geometría de control

- Definición de estaciones de medición (stations) a lo largo del fuselaje
- Puntos de control dimensional críticos
- Grid de medición para control de calidad
- Puntos de inspección dimensional

**Key Interfaces**: ATA-53 (Fuselage), ATA-57 (Wings), ATA-55 (Stabilizers), ATA-92 (EWIS)

### 06-30_ALIGNMENT_TARGETS
**Purpose**: Targets ópticos, fiduciales, retroreflectores

- Targets ópticos para fotogrametría
- Marcadores fiduciales para alineamiento
- Retroreflectores para láser tracking
- Sistemas de marcaje permanente y temporal

**Key Interfaces**: ATA-51 (Estructuras), IIF (Equipment de medición industrial)

### 06-40_CALIBRATION_PROTOCOLS
**Purpose**: Procedimientos de calibración, tolerancias, test alignment

- Protocolos de calibración de equipment de medición
- Definición de tolerancias dimensionales
- Procedimientos de verificación de alineamiento
- Trazabilidad metrológica

**Key Interfaces**: ATA-51/53/55/57 (Estructuras), LIB (Documentación), IIF (Calibración)

### 06-50_GEOMETRIC_MODELS
**Purpose**: Modelos CAD de geometría nominal, deformaciones esperadas

- Modelo digital maestro (Master Digital Model)
- Geometría nominal de referencia
- Modelos de deformación esperada
- Digital twin geométrico

**Key Interfaces**: Todos los sistemas estructurales (ATA-51-57), PPP (Propulsión)

## Subsystem Structure

Cada subsistema sigue el patrón estándar:

```
SUBSYSTEMS/06-XX_SUBSYSTEM_NAME/
├── README.md                              # Descripción del subsistema
├── META.json                              # Metadata (scope: "instance")
├── inherit.json                           # Referencias a templates de dominio
├── DELs/                                  # Data Exchange Lists
├── PAx/                                   # Package Exchange
│   ├── ONB/                              # Onboarding packages
│   └── OUT/                              # Output packages
├── PLM/                                   # Product Lifecycle Management
│   ├── EBOM_LINKS.md                     # Engineering BOM links
│   └── CAx/                              # Computer-Aided X
│       ├── CAD/                          # Design models
│       ├── CAE/                          # Engineering analysis
│       ├── CAO/                          # Optimization
│       ├── CAM/                          # Manufacturing
│       ├── CAI/                          # Inspection
│       ├── CAV/                          # Validation
│       ├── CAP/                          # Process planning
│       ├── CAS/                          # Service
│       └── CMP/                          # Configuration management
├── PROCUREMENT/VENDORSCOMPONENTS/        # Procurement data
├── QUANTUM_OA/                           # Quantum optimization algorithms
├── SUPPLIERS/                            # Supplier data
│   ├── BIDS/
│   └── SERVICES/
├── policy/                               # Policies and rules
└── tests/                                # Test artifacts
```

## Validation

### Manual Validation
Para validar la estructura manualmente:

```bash
./scripts/validate-06-dimensions-stations.sh
```

### CI/CD Validation
La validación automática se ejecuta en GitHub Actions cuando se modifican archivos en este sistema:

- **Workflow**: `.github/workflows/validate-06-dimensions-stations.yml`
- **Triggers**: Push y Pull Request en paths relevantes
- **Validation Jobs**:
  1. `validate-structure`: Valida la estructura general del sistema
  2. `validate-subsystems`: Valida cada subsistema individualmente (5 jobs en paralelo)
  3. `generate-summary`: Genera un resumen con badges de estado

### Validation Criteria

#### System Level
- ✅ `INTEGRATION_VIEW.md` presente y con contenido (>10 líneas)
- ✅ `INTERFACE_MATRIX/` directorio presente
- ✅ Al menos un archivo CSV en `INTERFACE_MATRIX/` con header estándar
- ✅ `SUBSYSTEMS/` directorio presente
- ❌ NO debe existir `PLM/CAx/` a nivel sistema (solo en subsistemas)

#### Subsystem Level (cada uno de los 5)
- ✅ `README.md` presente
- ✅ `META.json` presente con `scope: "instance"`
- ✅ `inherit.json` presente
- ✅ `PLM/EBOM_LINKS.md` presente
- ✅ `PLM/CAx/` con todos los 9 subdirectorios: CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP

## Integration with UTCS

Todos los artefactos dimensionales están integrados con el Unified Traceability & Compliance System (UTCS) para:

- Trazabilidad completa desde requisitos hasta as-built
- Validación de conformidad dimensional
- Gestión de configuración geométrica
- Auditoría de cambios dimensionales

## Standards and Compliance

- **ISO 1151**: Flight dynamics — Concepts, quantities and symbols
- **ISO 8855**: Road vehicles — Vehicle dynamics and road-holding ability
- **ASME Y14.5**: Geometric Dimensioning and Tolerancing (GD&T)
- **MIL-STD-1916**: DOD Preferred Methods for Acceptance of Product

## Contributing

Al contribuir artefactos a este sistema:

1. Seguir la estructura de directorios definida
2. Actualizar `INTEGRATION_VIEW.md` si hay cambios en interfaces
3. Mantener `INTERFACE_MATRIX/` actualizada con ICDs relevantes
4. Documentar artefactos CAx en `PLM/EBOM_LINKS.md` de cada subsistema
5. Ejecutar validación antes de commit: `./scripts/validate-06-dimensions-stations.sh`

## Status Badges

### System Structure
![Structure](https://img.shields.io/badge/structure-valid-success)

### Subsystems
- ![06-10](https://img.shields.io/badge/06--10__REFERENCE__FRAMES-valid-success)
- ![06-20](https://img.shields.io/badge/06--20__MEASUREMENT__POINTS-valid-success)
- ![06-30](https://img.shields.io/badge/06--30__ALIGNMENT__TARGETS-valid-success)
- ![06-40](https://img.shields.io/badge/06--40__CALIBRATION__PROTOCOLS-valid-success)
- ![06-50](https://img.shields.io/badge/06--50__GEOMETRIC__MODELS-valid-success)

---

*This system follows the unified pattern: `/SYSTEMS/ → SUBSYSTEMS/ → PLM/CAx`*
*For questions, contact the AAA (Airframes-Aerodynamics-Airworthiness) domain team.*
