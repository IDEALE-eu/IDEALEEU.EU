# Q100 Data Module - Estructura y Codificación

## Propósito

Este documento describe el Módulo de Datos (Data Module) creado con el código Q100 siguiendo las convenciones S1000D v5.x para el programa AMPEL360 AIR-T, configuración BWB-H2-Hy-E.

## Información del Módulo de Datos

### Identificación Completa

El módulo de datos Q100 está disponible en dos versiones de idioma:

**Versión en Español**: `DMC-Q100-53-10-00-00-00-0-000-0-A_es-ES_001-00.xml`

**Versión en Inglés STE**: `DMC-Q100-53-10-00-00-00-0-000-0-A_en-US_001-00.xml`

**Ubicación**: 
```
02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/53-FUSELAGE-STRUCTURES/SUBSYSTEMS/53-10_CENTER-BODY/PLM/CAx/CAS/CSDB/DataModules/Descriptive/00_GENERAL/DMC/
```

### Componentes del Código DMC

| Componente | Valor | Descripción |
|------------|-------|-------------|
| **modelIdentCode** | Q100 | Identificador de versión/familia (VERSION_ID) |
| **systemDiffCode** | 53 | Sistema ATA 53 - Estructuras del Fuselaje |
| **systemCode** | 10 | Subsistema 53-10 - Cuerpo Central |
| **subSystemCode** | 00 | Código de sub-subsistema |
| **subSubSystemCode** | 00 | Código de sub-sub-subsistema |
| **assyCode** | 00 | Código de ensamblaje |
| **disassyCode** | 0 | Código de desensamblaje (general) |
| **disassyCodeVariant** | 0 | Variante de desensamblaje |
| **infoCode** | 000 | Descripción general |
| **infoCodeVariant** | 0 | Variante de información |
| **itemLocationCode** | A | Ubicación del elemento |
| **languageIsoCode** | es / en | Idioma: Español o Inglés |
| **countryIsoCode** | ES / US | País: España o Estados Unidos |
| **issueNumber** | 001 | Primera emisión |
| **inWork** | 00 | Liberado (no en trabajo) |

## Versiones de Idioma

### Versión en Español (es-ES)

- **Archivo**: DMC-Q100-53-10-00-00-00-0-000-0-A_es-ES_001-00.xml
- **Idioma**: Español (España)
- **Contenido**: Texto completo en español
- **Uso**: Documentación técnica para usuarios de habla hispana

### Versión en Inglés STE (en-US)

- **Archivo**: DMC-Q100-53-10-00-00-00-0-000-0-A_en-US_001-00.xml
- **Idioma**: Inglés (Estados Unidos)
- **Estándar**: ASD-STE-100 (Simplified Technical English)
- **Contenido**: Traducción siguiendo las reglas de STE:
  - Oraciones cortas (≤ 25 palabras para descripciones)
  - Voz activa
  - Tiempo presente
  - Palabras simples y aprobadas del diccionario STE
  - Una idea por oración
  - Términos técnicos usados consistentemente
- **Uso**: Documentación técnica internacional estándar

## Contexto del Programa

### Programa y Segmento

- **PROGRAM**: 02-AIR-TRANSPORT
- **SEGMENTO**: PAX_AIRBORNE
- **PLM**: COMPUTER_AIDED-TIMECYCLE_PROCESS
- **CAx**: CAS (Computer-Aided Systems)
- **CSDB**: DataModel

### Identificación del Modelo

- **MODEL_ID**: AMPEL360-AIR-T
- **CONF_BASE**: BWB-H2-Hy-E (Blended Wing Body - Hydrogen - Hybrid-Electric)
- **VERSION_ID**: Q100
- **DOMAIN_ID**: AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS

### Sistema y Subsistema

- **SYSTEMS_ID**: 53-FUSELAGE-STRUCTURES
- **SUBSYSTEMS_ID**: 53-10_CENTER-BODY

### Elemento de Configuración

- **CI**: CONFIGURATION_ITEM
- **DOC TIPO**: SUBPRODUCT-MANUAL
- **CSDB OBJ**: DATA_MODULE

## Metadatos y Trazabilidad

### Metadatos del DM

```xml
<dmTitle>
  <techName>Cuerpo Central - Estructuras del Fuselaje</techName>
  <infoName>Descripción General</infoName>
</dmTitle>
```

### Responsables

- **responsiblePartnerCompany**: AAA (AMPEL360 AIR-T Publicaciones Técnicas)
- **originator**: AAA (AMPEL360 AIR-T Ingeniería)
- **skillLevel**: 1-3 según manual

### Aplicabilidad

El módulo incluye etiquetas de aplicabilidad que especifican:

- **PRODUCT**: AMPEL360-AIR-T
- **CONFIG_BASE**: BWB-H2-Hy-E
- **VERSION**: Q100
- **DOMAIN**: AAA
- **SYSTEM**: 53
- **SUBSYSTEM**: 53-10
- **CI**: CONFIGURATION_ITEM
- **DOCTYPE**: SUBPRODUCT-MANUAL

### UTCS (Universal Traceability Code System)

```xml
<utcs id="UTCS-Q100-AAA-53-10-DMC-001"/>
```

## BREX y Esquema

### BREX Aplicable

**Archivo**: `DMC-Q100-BREX-AAA-STRUCTURES-00-00-0-0-000-A-A_es-ES_001-00.xml`

**Ubicación**: 
```
02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/53-FUSELAGE-STRUCTURES/SUBSYSTEMS/53-10_CENTER-BODY/PLM/CAx/CAS/CSDB/BREX/
```

**Propósito**: Business Rules Exchange para el dominio AAA-STRUCTURES con reglas específicas para Q100

### Esquemas S1000D

- **Estándar**: S1000D v5.x / v6.0
- **Namespace**: `http://www.s1000d.org/S1000D_6-0/xml_schema_flat`
- **Esquemas**: 
  - `descript.xsd` para módulos descriptivos
  - `pm.xsd` para módulos de publicación

## Checks y Validación

### Alineación de Códigos

✓ **SYSTEMS_ID 53** alineado con ATA 53 (Fuselaje - Estructuras)
✓ **SUBSYSTEMS_ID 53-10** normalizado a código sin espacios
✓ **infoCode 000** para descripción general
✓ Nombres normalizados a códigos en CSDB

### Validación XML

- [x] XML bien formado (well-formed)
- [x] Estructura S1000D v6.0 válida
- [x] Namespaces correctos
- [x] Metadatos completos

### Diferencias con Convención AMP360

Este módulo utiliza **Q100** como `modelIdentCode` en lugar de **AMP360**:

- **AMP360**: Convención general del proyecto (en-US)
- **Q100**: Identificador específico de versión/familia (es-ES)

Ambas convenciones son válidas en S1000D, siendo Q100 más específico para la familia/versión del producto.

## Contenido del Módulo

El módulo contiene:

1. **Descripción General** del Cuerpo Central
2. **Resumen** de la estructura BWB
3. **Características Principales** del componente
4. **Identificación del Sistema** (ATA 53-10)
5. **Dominio y Trazabilidad CSDB**
6. **Normativa de Referencia** (S1000D v5.x, ATA iSpec 2200)
7. **Notas sobre Codificación** detalladas

Todo el contenido está en **español (es-ES)** según lo especificado.

## Referencias

### Documentación Relacionada

- **Conventions.md**: Convenciones de nombrado AMPEL360
- **TEMPLATES/README.md**: Plantillas de Data Modules
- **CSDB/DataModules/README.md**: Repositorio de módulos de datos
- **VALIDATION/README.md**: Pipeline de validación

### Estándares

- **S1000D Issue 5.x/6.0**: Especificación técnica
- **ATA iSpec 2200**: Numeración de capítulos/secciones
- **ASD-STE-100**: Inglés Técnico Simplificado (para versiones en inglés)

### Sistemas Relacionados

- **Sistema 53**: FUSELAGE-STRUCTURES
- **Subsistema 53-10**: CENTER-BODY
- **Dominio AAA**: AIRFRAMES-AERODYNAMICS-AIRWORTHINESS

## Historial de Cambios

| Versión | Fecha | Autor | Descripción |
|---------|-------|-------|-------------|
| 001-00 | 2025-10-15 | AMPEL360 Engineering | Emisión inicial - Descripción general Q100 |

---

**Estado**: Liberado (Released)  
**Idioma**: Español (España) - es-ES  
**Clasificación**: 01 (No clasificado)  
**Control de Exportación**: false
