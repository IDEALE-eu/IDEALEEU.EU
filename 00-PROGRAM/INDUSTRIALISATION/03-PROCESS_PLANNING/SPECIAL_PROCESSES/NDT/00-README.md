# NDT

Non-Destructive Testing procedures and specifications for aerospace components.

## Overview

Non-Destructive Testing (NDT) methods used to detect internal and surface defects without damaging parts. Required for flight-critical structures and special processes.

## NDT Methods

### Ultrasonic Testing (UT)
- **Principle:** High-frequency sound waves detect internal defects
- **Applications:** Composites (delaminations, porosity), metals (cracks, inclusions)
- **Methods:** Pulse-echo, through-transmission, C-scan imaging

### Radiographic Testing (RT)
- **Principle:** X-rays or gamma rays detect density variations
- **Applications:** Castings, welds (porosity, cracks, incomplete fusion)
- **Methods:** Film radiography, digital radiography, computed tomography (CT)

### Liquid Penetrant Testing (PT)
- **Principle:** Capillary action draws dye into surface-breaking defects
- **Applications:** Non-porous materials, surface cracks
- **Methods:** Visible dye, fluorescent dye (more sensitive)

### Magnetic Particle Testing (MT)
- **Principle:** Magnetic field and iron particles reveal surface/near-surface defects
- **Applications:** Ferromagnetic materials only (steel, some stainless)
- **Methods:** Dry powder, wet suspension, AC/DC magnetization

### Eddy Current Testing (ET)
- **Principle:** Electromagnetic induction detects surface/near-surface defects
- **Applications:** Conductivity, surface cracks, coating thickness
- **Methods:** Surface probe, encircling coil

## NDT Personnel Qualification

### Certification Standard: NAS 410 or ASNT SNT-TC-1A
- **Level I:** Performs testing under supervision
- **Level II:** Performs and interprets results, trains Level I
- **Level III:** Establishes procedures, interprets codes, certifies personnel

### Qualification Requirements
- **Training:** Classroom and practical (method-specific hours)
- **Experience:** Method-specific hours
- **Examination:** Written (general, specific, practical)
- **Vision test:** Annual near-vision and color perception (if applicable)
- **Recertification:** Every 5 years (NAS 410) or 3 years (some SNT-TC-1A)

## Ultrasonic Testing (UT)

### UT Methods

**Pulse-Echo**
- Single transducer sends and receives
- Detects reflections from defects or back wall
- A-scan display (amplitude vs. time)

**Through-Transmission**
- Separate transmit and receive transducers
- Loss of signal indicates defect
- Used for composites

**C-Scan**
- Automated scanning produces image
- Color-coded amplitude or time-of-flight
- Permanent record of laminate quality

### UT Procedure Elements
- **Equipment:** Ultrasonic flaw detector, transducers, couplant
- **Frequency:** 2.25-10 MHz typical (higher for thin/fine-grained materials)
- **Calibration:** Reference standards with known defects
- **Scan pattern:** Grid or raster, 100% coverage or sample
- **Acceptance criteria:** Amplitude limits, defect size/distribution

### UT for Composites
- **Application:** Detect delaminations, porosity, foreign objects
- **Method:** Through-transmission or pulse-echo
- **Acceptance:** <2% porosity, no delaminations >0.25" diameter

### UT for Metals
- **Application:** Detect cracks, inclusions, voids
- **Method:** Pulse-echo, angle beam (for welds)
- **Acceptance:** Per ASTM or customer specification

## Radiographic Testing (RT)

### RT Equipment
- **X-ray:** Portable or cabinet X-ray machines
- **Isotope:** Iridium-192, Cobalt-60 (field radiography)
- **Detectors:** Film, digital detectors, computed radiography

### RT Procedure Elements
- **Technique:** Source-to-part distance, exposure time, energy
- **Image quality indicators (IQI):** Penetrameters verify sensitivity
- **Viewing:** Film viewed on lighted screen, digital on monitor
- **Interpretation:** Trained Level II personnel
- **Acceptance:** Per ASTM or customer specification (e.g., ASTM E1742 for castings)

### RT Applications
- **Castings:** Porosity, shrinkage, inclusions
- **Welds:** Lack of fusion, porosity, cracks
- **Assemblies:** Verify internal configuration

### RT Safety
- **Radiation hazard:** Exposure to ionizing radiation
- **Controls:** Shielding, distance, time, dosimetry
- **Licensing:** NRC or state license for radioactive sources

## Liquid Penetrant Testing (PT)

### PT Process
1. **Pre-clean:** Remove contamination (solvent, detergent)
2. **Apply penetrant:** Spray or dip, dwell 10-30 minutes
3. **Remove excess:** Wipe or water rinse
4. **Apply developer:** Draws penetrant from defects
5. **Inspect:** UV light (fluorescent) or visible light (dye)
6. **Post-clean:** Remove developer and penetrant

### PT Procedure Elements
- **Penetrant type:** Visible dye or fluorescent
- **Sensitivity:** Level 1 (low), 2 (medium), 3 (high), 4 (ultra-high)
- **Removal method:** Water-washable, post-emulsifiable, solvent-removable
- **Developer:** Dry, wet, non-aqueous
- **Inspection conditions:** UV intensity (≥1000 µW/cm²), ambient light (<2 fc)

### PT Acceptance Criteria
- **Relevant indications:** Linear >1/16", rounded >3/32"
- **Pattern:** Multiple indications in line (suggests crack)
- **Evaluation:** Per ASTM E1417 or customer specification

### PT Applications
- **Aerospace:** Aluminum, titanium, steel parts
- **Typical:** Machined parts, welds, forgings, castings

## Magnetic Particle Testing (MT)

### MT Process
1. **Pre-clean:** Remove contamination
2. **Magnetize:** Apply magnetic field (prod, coil, yoke)
3. **Apply particles:** Dry powder or wet suspension
4. **Inspect:** Particles accumulate at defects
5. **Demagnetize:** Remove residual magnetism (if required)
6. **Post-clean:** Remove particles

### MT Procedure Elements
- **Magnetization method:** Direct, indirect, prod, coil, yoke
- **Current type:** AC (surface), DC (subsurface), HWDC (half-wave)
- **Particle type:** Dry, wet, visible, fluorescent
- **Field strength:** Verified with field indicator or test piece

### MT Acceptance Criteria
- **Relevant indications:** Linear >1/16", grouped
- **Evaluation:** Per ASTM E1444 or customer specification

### MT Applications
- **Ferromagnetic only:** Carbon steel, some stainless steels
- **Typical:** Forgings, welds, machined steel parts

## Eddy Current Testing (ET)

### ET Applications
- **Conductivity measurement:** Aluminum alloy verification, heat treat
- **Crack detection:** Surface and near-surface cracks
- **Coating thickness:** Paint, anodize thickness

### ET Procedure Elements
- **Probe type:** Surface probe, encircling coil, sliding probe
- **Frequency:** 100 kHz to several MHz (higher for surface, lower for depth)
- **Standards:** Reference standards for calibration
- **Scan:** Manual or automated

### ET for Conductivity
- **Application:** Verify aluminum heat treatment (T6, T7, etc.)
- **Acceptance:** Per AMS or customer specification (e.g., 7075-T6: 33-37% IACS)

## NDT Acceptance Criteria

### General Approach
- **Zero defects:** Flight-critical, no cracks allowed
- **Accept/Reject limits:** Size, count, distribution per specification
- **Engineering disposition:** Evaluate indications per stress analysis

### Typical Criteria Sources
- **ASTM standards:** E1444 (MT), E1417 (PT), E1742 (RT castings)
- **Customer specifications:** OEM-specific acceptance criteria
- **AMS specifications:** Material or process specifications

## NDT Procedure Development

### Procedure Content
- **Scope:** Applicable parts and defect types
- **Equipment:** Specific equipment and models
- **Calibration:** Reference standards and setup
- **Technique:** Step-by-step instructions
- **Acceptance criteria:** Accept/reject limits
- **Documentation:** Report format and content

### Procedure Qualification
- **Validation:** Demonstrate detection of relevant defects
- **Sensitivity:** Use reference standards with known defects
- **Repeatability:** Multiple operators achieve same results

## Documentation

### NDT Reports
- Part identification (number, serial)
- NDT method and procedure number
- Inspector name, certification level, date
- Equipment used and calibration status
- Inspection results (accept/reject, defect locations)
- Signature of Level II or III

### Record Retention
- **Flight-critical parts:** Permanent
- **Non-critical parts:** 10 years minimum

## Quality Assurance

### NDT Quality Control
- **Daily checks:** Equipment function checks
- **Calibration:** Periodic per procedure (daily, weekly, monthly)
- **Reference standards:** Known defects for comparison
- **Proficiency testing:** Operator skill verification

### Audits
- **Internal:** Regular audits of NDT procedures and practices
- **External:** Customer or third-party audits
- **Findings:** Corrective actions and follow-up

## References

- NAS 410: Certification and Qualification of NDT Personnel
- ASNT SNT-TC-1A: Personnel Qualification (alternative to NAS 410)
- ASTM E1444: Magnetic Particle Testing
- ASTM E1417: Liquid Penetrant Testing
- ASTM E1742: Radiographic Examination of Castings
- Link to **CONTROL_PLAN/** for NDT requirements
- Link to **08-QUALITY/** for quality procedures
- Link to **13-TRAINING_COMPETENCY/** for NDT personnel certification tracking
