# 33-LIGHTS — SYSTEMS

**Ruta:** `IDEALEEU.EU/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/DOMAINS/EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/33-LIGHTS/`

## Meta
- **Sistema:** 33-LIGHTS
- **ATA Chapter:** 33
- **Descripción:** Aircraft Lighting Systems
- **Norma de organización:** PLM/CAx **solo** bajo `SUBSYSTEMS/`

## Índice de Subsistemas

| Subsistema | Descripción |
|------------|-------------|
| [33-00_STANDARDS_GENERAL/](./SUBSYSTEMS/33-00_STANDARDS_GENERAL/) | General Standards and Documentation |
| [33-10_EXTERNAL_NAV_STROBE_BEACON/](./SUBSYSTEMS/33-10_EXTERNAL_NAV_STROBE_BEACON/) | External Navigation, Strobe, and Beacon Lights |
| [33-20_LANDING_TAXI_TAKEOFF_LIGHTS/](./SUBSYSTEMS/33-20_LANDING_TAXI_TAKEOFF_LIGHTS/) | Landing, Taxi, and Takeoff Lighting |
| [33-30_LOGO_WING_INSPECTION_LIGHTS/](./SUBSYSTEMS/33-30_LOGO_WING_INSPECTION_LIGHTS/) | Logo, Wing, and Inspection Lights |
| [33-40_EMERGENCY_EXT_MARKINGS_PWR_IF/](./SUBSYSTEMS/33-40_EMERGENCY_EXT_MARKINGS_PWR_IF/) | Emergency Lighting, Exit Markings, Power Interface |

## Convenciones clave

- Estructura base: `…/SYSTEMS/33-LIGHTS/{INTEGRATION_VIEW.md, INTERFACE_MATRIX, SUBSYSTEMS}`
- Documentación de sistema en este nivel. Detalle técnico y PLM en `SUBSYSTEMS/…`
- Ver [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) para vista de integración
- Ver [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) para interfaces con otros sistemas
- EWIS (cableado) está en ATA 92, no aquí (ver ../NOTES.txt)

## Arquitectura del Sistema

El sistema de iluminación del BWB-H2-Hy-E incluye:

- **Iluminación externa de navegación:** Luces de posición, estroboscópicas, anticolisión
- **Iluminación de aterrizaje:** Luces de aterrizaje, taxi, despegue de alta intensidad LED
- **Iluminación de inspección:** Iluminación de alas, logo, y puntos de inspección
- **Iluminación de emergencia:** Luces de evacuación, señalización de salidas
- **Control y dimming:** Control digital centralizado con atenuación automática
- **Interfaz de potencia:** Conexiones a sistema eléctrico principal y de emergencia
