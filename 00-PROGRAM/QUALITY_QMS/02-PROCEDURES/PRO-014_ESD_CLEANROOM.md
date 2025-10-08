# PRO-014: ESD and Cleanroom Control

**Procedure Number:** PRO-014  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Manufacturing Director

## 1. Purpose

Establish requirements for Electrostatic Discharge (ESD) control and cleanroom operations to protect sensitive electronic components and maintain product cleanliness.

## 2. Scope

Applies to:
- Electronics assembly and test areas
- Cleanroom operations
- Handling of ESD-sensitive devices (ESDS)
- Contamination-sensitive operations

## 3. ESD Control Program

### 3.1 ESD Sensitive Devices

**Classification per ANSI/ESD S20.20:**
- Class 0: < 50V (extremely sensitive)
- Class 1A: 50-99V
- Class 1B: 100-199V
- Class 1C: 200-999V
- Class 2: 1,000-3,999V
- Class 3: 4,000-15,999V

### 3.2 ESD Protected Area (EPA)

**Requirements:**
- Defined boundaries (floor markings, signs)
- Access control
- ESD protective equipment required
- Monitoring and auditing
- Controlled entry/exit procedures

**EPA Levels:**
- Level 1: Assembly and handling of bare components
- Level 2: PCB assembly areas
- Level 3: System-level assembly and test

### 3.3 ESD Control Measures

**Personnel Grounding:**
- Wrist straps (1 MΩ resistor)
- ESD footwear + conductive flooring
- Garments (smocks, jackets) if required
- Continuous ground monitoring systems

**Worksurfaces:**
- Static-dissipative or conductive mats
- Grounded to earth/common point
- Resistance: 1 × 10⁶ to 1 × 10⁹ Ω to ground

**Seating:**
- Conductive or dissipative chairs
- No fabric or foam that generates charge

**Flooring:**
- Conductive or dissipative floor finish
- Resistance: < 1 × 10⁹ Ω to ground

**Tools and Equipment:**
- Conductive or dissipative materials
- Grounded soldering irons
- Ionizers for insulators
- Grounded test equipment

**Packaging:**
- Metallized shielding bags (Faraday cage)
- Conductive tote boxes
- ESD-safe foam
- Labeled per ANSI/ESD S20.20

### 3.4 ESD Training

**Topics:**
- Principles of ESD
- Device sensitivity
- Grounding techniques
- Proper handling procedures
- Packaging requirements
- EPA rules

**Frequency:** Annual refresher

### 3.5 ESD Auditing

**Daily:**
- Wrist strap testing (before start of shift)
- Visual verification of ESD controls

**Monthly:**
- Resistance measurements (worksurfaces, floors, footwear)
- Ionizer testing
- Equipment verification

**Annual:**
- Complete EPA audit per ANSI/ESD S20.20
- Third-party audit for certification

## 4. Cleanroom Control

### 4.1 Cleanroom Classification

**Per ISO 14644-1:**
- **ISO Class 5:** ≤ 3,520 particles/m³ (≥ 0.5 μm) [Class 100]
- **ISO Class 6:** ≤ 35,200 particles/m³ [Class 1,000]
- **ISO Class 7:** ≤ 352,000 particles/m³ [Class 10,000]
- **ISO Class 8:** ≤ 3,520,000 particles/m³ [Class 100,000]

**Application:**
- Spacecraft assembly: ISO 7-8
- Precision optics: ISO 5-6
- Avionics assembly: ISO 7-8

### 4.2 Cleanroom Design

**Features:**
- HEPA/ULPA filtered air supply
- Positive pressure (relative to adjacent areas)
- Unidirectional airflow (laminar) for critical areas
- Air changes per hour (ACH): 15-600 depending on class
- Smooth, non-shedding surfaces
- Minimal horizontal surfaces
- Sealed penetrations

**Monitoring:**
- Particle counters (continuous or periodic)
- Differential pressure gauges
- Temperature and humidity monitoring
- Airflow velocity measurements

### 4.3 Cleanroom Entry Procedures

**Personnel:**
1. Remove street clothing and jewelry
2. Don cleanroom garments:
   - Coverall or smock
   - Hood or bouffant cap
   - Face mask
   - Gloves (nitrile or latex)
   - Shoe covers or dedicated shoes
3. Pass through air shower (if required)
4. Enter via gowning area/airlock

**Gowning Levels:**
- ISO 5-6: Full coverage (hood, mask, gloves)
- ISO 7-8: Partial coverage (smock, hair cover)

**Materials:**
1. Clean and inspect before entry
2. Wipe down with cleanroom-compatible cleaner
3. Transfer through pass-through chamber
4. Document entry in logbook

### 4.4 Cleanroom Practices

**Allowed:**
- Cleanroom-compatible materials only
- Minimal movement
- Organized work areas
- Regular cleaning
- Approved tools and equipment

**Prohibited:**
- Food, drink, gum
- Cosmetics, perfume, lotions
- Paper (sheds particles)
- Cardboard (generates particles)
- Uncovered hair
- Excessive movement or talking
- Non-cleanroom materials

### 4.5 Cleaning and Maintenance

**Routine Cleaning:**
- Daily: Floors, work surfaces
- Weekly: Walls, equipment exteriors
- Monthly: Ceilings, light fixtures

**Methods:**
- HEPA-filtered vacuum only
- Cleanroom mops (laundered)
- IPA (Isopropyl Alcohol) or approved cleaners
- Sticky mats at entries

**Maintenance:**
- HEPA filter replacement per schedule
- Seal integrity tests annually
- Equipment calibration per PRO-011

### 4.6 Contamination Control

**Sources:**
- Personnel (skin, hair, clothing)
- Materials and packaging
- Equipment and tools
- Air infiltration
- Process-generated particles

**Controls:**
- Minimize personnel in cleanroom
- Use cleanroom-compatible materials
- Enclose particle-generating equipment
- Maintain pressure differentials
- Regular monitoring

### 4.7 Cleanroom Monitoring

**Particle Counting:**
- At-rest condition: No activity, settled state
- Operational condition: Normal operations
- Frequency: Daily for ISO 5-6, weekly for ISO 7-8

**Testing:**
- Classification testing (initial and annual)
- Airflow visualization (smoke test)
- HEPA filter leak test
- Recovery test (time to return to classification)

## 5. Training

**ESD Training:**
- Initial: 4 hours
- Annual refresher: 2 hours
- Hands-on practice

**Cleanroom Training:**
- Initial: 2-4 hours
- Gowning procedures
- Cleanroom practices
- Annual refresher

**Records:** LOG_TRAINING_RECORD.csv

## 6. Records

- ESD daily test logs
- ESD audit results
- Cleanroom particle counts
- Cleanroom maintenance logs
- Filter change records
- Training records (LOG_TRAINING_RECORD.csv)
- Nonconformances

**Retention:** 5 years minimum

## 7. Related Documents

- ANSI/ESD S20.20 (ESD Control Program)
- IEC 61340-5-1 (ESD Protection)
- ISO 14644 (Cleanroom Classification)
- PRO-016_TRAINING_COMPETENCE
- PRO-004_NONCONFORMANCE

## 8. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Manufacturing Director |
