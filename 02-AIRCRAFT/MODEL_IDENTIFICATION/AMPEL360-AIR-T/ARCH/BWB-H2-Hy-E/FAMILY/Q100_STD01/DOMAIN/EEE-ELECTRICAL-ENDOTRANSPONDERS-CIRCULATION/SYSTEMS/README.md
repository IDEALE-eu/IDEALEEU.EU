# EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION — SYSTEMS

**Ruta:** `IDEALEEU.EU/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/CONF/BASELINE/FAMILY/Q100_STD01/VERSION/Q100/DOMAINS/EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/`

## Meta
- **Dominio:** EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION
- **Norma de organización:** PLM/CAx **solo** bajo `SUBSYSTEMS/`

## Índice de Sistemas

| Sistema | Descripción | ATA |
|---------|-------------|-----|
| [24-ELECTRICAL-POWER/](./24-ELECTRICAL-POWER/) | Electrical Power Generation, Storage, Distribution | ATA 24 |
| [33-LIGHTS/](./33-LIGHTS/) | Aircraft Lighting Systems | ATA 33 |
| [39-ELECTRICAL_PANELS/](./39-ELECTRICAL_PANELS/) | Electrical Panels and Distribution Boxes | ATA 39 |
| [80-STARTING/](./80-STARTING/) | Engine Starting Systems | ATA 80 |

## Matriz de Interfaces

Ver: [INTERFACE_MATRIX/EEE↔31_33_39_42_44_71_72_80_92_93_94_26.csv](./INTERFACE_MATRIX/EEE↔31_33_39_42_44_71_72_80_92_93_94_26.csv)

## Convenciones clave

- Estructura base: `…/SYSTEMS/{SYSTEM}/{INTERFACE_MATRIX, SUBSYSTEMS}`
- Documentación de sistema en nivel de sistema. Detalle técnico y PLM en `SUBSYSTEMS/…`
- Todos los cableados y arneses (EWIS) pertenecen a ATA 92, no a EEE (ver NOTES.txt)
- Índices enlazables por carpeta mediante `README.md` o `INDEX.md`

## Notas importantes

Ver [NOTES.txt](./NOTES.txt) para detalles sobre la ubicación de EWIS en ATA 92.
