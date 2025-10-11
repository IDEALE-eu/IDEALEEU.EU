# 80-STARTING — SYSTEMS

**Ruta:** `IDEALEEU.EU/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/DOMAINS/EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/80-STARTING/`

## Meta
- **Sistema:** 80-STARTING
- **ATA Chapter:** 80
- **Descripción:** Engine Starting Systems
- **Norma de organización:** PLM/CAx **solo** bajo `SUBSYSTEMS/`

## Índice de Subsistemas

| Subsistema | Descripción |
|------------|-------------|
| [80-00_STANDARDS_GENERAL/](./SUBSYSTEMS/80-00_STANDARDS_GENERAL/) | General Standards and Documentation |
| [80-10_STARTER_GENERATORS_SG_PMSM/](./SUBSYSTEMS/80-10_STARTER_GENERATORS_SG_PMSM/) | Starter-Generator Units (PMSM-based) |
| [80-20_START_POWER_ELECTRONICS_SPCU/](./SUBSYSTEMS/80-20_START_POWER_ELECTRONICS_SPCU/) | Start Power Control Unit (SPCU) Electronics |
| [80-30_START_SEQUENCE_CONTROL_IF_73_76/](./SUBSYSTEMS/80-30_START_SEQUENCE_CONTROL_IF_73_76/) | Start Sequence Control and Interface to ATA 73 & 76 |

## Convenciones clave

- Estructura base: `…/SYSTEMS/80-STARTING/{INTEGRATION_VIEW.md, INTERFACE_MATRIX, SUBSYSTEMS}`
- Documentación de sistema en este nivel. Detalle técnico y PLM en `SUBSYSTEMS/…`
- Ver [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) para vista de integración
- Ver [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) para interfaces con otros sistemas
- EWIS (cableado) está en ATA 92, no aquí (ver ../NOTES.txt)

## Arquitectura del Sistema

El sistema de arranque del BWB-H2-Hy-E incluye:

- **Starter-Generators (SG):** Unidades duales basadas en PMSM (Permanent Magnet Synchronous Motor)
  - Modo arranque: Motor eléctrico de alta potencia
  - Modo generación: Generador eléctrico después del arranque
  
- **Unidad de Control de Potencia de Arranque (SPCU):** Electrónica de potencia avanzada
  - Conversión DC/AC de alta potencia (típicamente 270VDC a trifásica variable)
  - Control vectorial de campo orientado para PMSM
  - Protección de sobrecorriente y temperatura
  
- **Control de Secuencia de Arranque:** Lógica coordinada con propulsión
  - Interfaz con FADEC (ATA 73)
  - Coordinación con sistema de combustible H₂ (ATA 28)
  - Coordinación con sistema de propulsión (ATA 76)
  - Secuencias de arranque normal, cross-bleed, y emergencia

## Consideraciones Especiales H₂

- Warmup de fuel cell stacks
- Gestión de flujo de H₂ criogénico
- Enclavamientos de seguridad H₂
- Coordinación térmica con sistemas criogénicos
