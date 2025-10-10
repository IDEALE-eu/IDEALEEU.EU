# AMPEL360 AIR-T Style Guide

## Purpose

This guide defines style and formatting standards for S1000D technical documentation in the AMPEL360 AIR-T program, ensuring consistency, clarity, and compliance with ASD-STE-100 Simplified Technical English.

## General Principles

### Clarity and Precision
- Use simple, direct language
- One idea per sentence
- Active voice preferred
- Present tense for procedures
- Imperative mood for instructions

### Consistency
- Follow approved terminology
- Use standard phrases
- Maintain uniform structure
- Apply consistent formatting

### Safety First
- Safety messages precede hazardous steps
- Use correct safety message types
- Never bury safety in notes
- Highlight critical information

## Language Standards

### ASD-STE-100 Compliance

#### Approved Word Usage
- Use only approved technical words
- Use general words in approved sense
- Maximum 25 words per sentence (preferred)
- Simple grammatical structures

#### Forbidden Constructions
- ❌ Passive voice: "The cover should be removed"
- ✅ Active voice: "Remove the cover"

- ❌ Future tense: "You will remove the cover"
- ✅ Imperative: "Remove the cover"

- ❌ Vague adverbs: "carefully", "properly", "sufficiently"
- ✅ Specific instructions: "Torque to 25 N⋅m ±2 N⋅m"

- ❌ Intensifiers: "very", "really", "quite"
- ✅ Precise descriptions: "critical", "essential"

### U.S. English Standards

#### Spelling
- ✅ color (not colour)
- ✅ center (not centre)
- ✅ aluminum (not aluminium)
- ✅ analyze (not analyse)
- ✅ defense (not defence)

#### Terminology
- Use "airplane" (not "aeroplane")
- Use "gasoline" (not "petrol")
- Use "wrench" (not "spanner")

#### Numbers and Units
- Use SI units with U.S. equivalents in parentheses
- Example: "25 mm (0.98 in)"
- Use period as decimal separator: 3.14 (not 3,14)
- Use comma as thousands separator: 1,000 (not 1.000)

## Document Structure

### Data Module Organization

```xml
<dmodule>
  <identAndStatusSection>
    <!-- Metadata, security, QA -->
  </identAndStatusSection>
  <content>
    <description|procedure|faultIsolation|...>
      <!-- Content organized by information type -->
    </...>
  </content>
</dmodule>
```

### Headings and Titles
- Level 1: Data Module title (auto-generated from DMC)
- Level 2: Major sections
- Level 3: Subsections
- Level 4: Detail sections (avoid if possible)
- Maximum 3 heading levels preferred

### Paragraphs
- One topic per paragraph
- 3-5 sentences per paragraph (guideline)
- Use lists for 3+ related items
- Blank line between paragraphs (in source)

## Safety Messages

### Types and Usage

#### WARNING (Red)
**Use for**: Risk of death or serious injury

```xml
<warning>
  <warningType>warning</warningType>
  <warningText>
    <para>High voltage present. Risk of electrocution.</para>
  </warningText>
</warning>
```

**Examples:**
- Electrical hazards (>50V)
- Hydrogen leaks or fire risk
- Structural collapse hazards
- Moving machinery (crush hazards)

#### CAUTION (Yellow/Orange)
**Use for**: Risk of equipment damage or minor injury

```xml
<caution>
  <cautionType>caution</cautionType>
  <cautionText>
    <para>Do not exceed torque limit. Excessive torque can damage threads.</para>
  </cautionText>
</caution>
```

**Examples:**
- Tool or equipment damage
- Data loss or corruption
- Surface damage (scratches, dents)
- Minor cuts or abrasions

#### NOTE (Blue/Green)
**Use for**: Additional information, tips, or reminders

```xml
<note>
  <noteText>
    <para>Apply lubricant to threads before installation.</para>
  </noteText>
</note>
```

**Not for safety**: Never use notes for safety-critical information.

### Safety Message Placement
1. **Before the hazardous step**: Always
2. **Close to the hazard**: Within 1-2 steps
3. **Repeated if necessary**: For multiple hazardous steps
4. **Never nested**: Don't put safety inside notes or other safety messages

### AMPEL360-Specific Safety

#### Hydrogen Systems
**Required elements:**
- Ventilation requirements
- Ignition source warnings
- Leak detection procedures
- Emergency shutdown procedures
- PPE requirements

```xml
<warning>
  <warningType>warning</warningType>
  <warningText>
    <para>Hydrogen gas is highly flammable. Ensure adequate ventilation. 
    Remove all ignition sources before opening hydrogen system components.</para>
  </warningText>
</warning>
```

#### Cryogenic Systems
**Required elements:**
- Cold burn hazards
- Pressure hazards
- PPE (cryogenic gloves, face shield)
- Material embrittlement warnings

#### High Voltage Systems
**Required elements:**
- LOTO (Lock-Out Tag-Out) procedures
- Voltage levels and locations
- Discharge procedures
- PPE (insulated gloves, safety glasses)
- Qualified personnel requirements

## Procedural Content

### Step Structure

```xml
<proceduralStep>
  <stepPara>Disconnect the battery negative cable.</stepPara>
  <stepPara>Wait 5 minutes for capacitor discharge.</stepPara>
</proceduralStep>
```

### Step Numbering
- Automatic numbering preferred
- Use sub-steps for detail
- Maximum 2 levels of sub-steps
- Restart numbering for new procedures

### Prerequisites

```xml
<preliminaryRqmts>
  <requiredPersons>
    <person>
      <personType>mechanic</personType>
      <numberOfPersons>1</numberOfPersons>
    </person>
  </requiredPersons>
  <tools>
    <tool>10 mm wrench</tool>
    <tool>Digital multimeter</tool>
  </tools>
  <consumables>
    <consumable>Isopropyl alcohol, 100 ml</consumable>
  </consumables>
</preliminaryRqmts>
```

### Close-out Requirements

```xml
<closeRqmts>
  <closeRqmtsStatement>Perform operational check per procedure XXX.</closeRqmtsStatement>
  <closeRqmtsStatement>Document maintenance action in aircraft log.</closeRqmtsStatement>
</closeRqmts>
```

## Lists

### Sequential Lists (Ordered)
Use for steps that must be done in order:

```xml
<sequentialList>
  <listItem>Turn power switch to OFF.</listItem>
  <listItem>Wait for system shutdown (30 seconds).</listItem>
  <listItem>Disconnect power cable.</listItem>
</sequentialList>
```

### Random Lists (Unordered)
Use for items with no required order:

```xml
<randomList>
  <listItem>Torque wrench (50-250 N⋅m range)</listItem>
  <listItem>Socket set (10-19 mm)</listItem>
  <listItem>Extension bars (150 mm, 300 mm)</listItem>
</randomList>
```

### Nesting Rules
- Maximum 2 levels of nesting
- No mixing sequential and random at same level
- Use sub-steps instead of deeply nested lists

## Illustrations and Graphics

### ICN Naming Convention

**Pattern:**
```
ICN-<chapter>-<section>-<subsection>-<seq>-<issue>.<format>
```

**Example:**
```
ICN-53-10-10-0001-A.svg
ICN-53-10-20-0002-A.png
ICN-53-10-95-0003-A.svg
```

**Components:**
- **chapter**: ATA chapter (e.g., 53 = Fuselage Structures)
- **section**: Subsystem (e.g., 10 = Center Body)
- **subsection**: Component code (10-89 for specific components, 90-99 for generic)
- **seq**: Sequential number (0001-9999)
- **issue**: Revision letter (A-Z)
- **format**: File extension (svg, png, cgm)

### ICN Storage Location

All ICNs are stored in the **Centralized Illustration Repository (CIR)**:
```
CSDB/Illustrations/CIR/53-10/DERIVED/SVG/ICN-53-10-10-0001-A.svg
```

Data Modules reference ICNs using relative paths:
```xml
<graphicRef xlink:href="../../../Illustrations/CIR/53-10/DERIVED/SVG/ICN-53-10-10-0001-A.svg"/>
```

### Figure Titles
- Descriptive and specific
- Include system and component
- Use sentence case
- No period at end

**Examples:**
- ✅ "Center Body Forward Bulkhead Installation"
- ✅ "Hydraulic Line Routing, Isometric View"
- ❌ "Figure 1"
- ❌ "Installation."

### Callouts
- Use numbers (1, 2, 3, ...)
- Start at 1 for each figure
- Follow logical sequence (clockwise or left-to-right)
- Define all callouts in figure legend

### Image Formats
- **SVG**: Preferred for technical drawings
- **PNG**: Photos, screenshots (min 300 DPI)
- **CGM**: Legacy format (convert to SVG if possible)
- **Prohibited**: JPEG (lossy compression), GIF, BMP

### File Size
- SVG: No limit (optimized recommended)
- PNG: Maximum 5 MB per file
- Optimize for web delivery

## Tables

### Table Structure

```xml
<table>
  <title>Torque Values for M8 Fasteners</title>
  <tgroup cols="3">
    <thead>
      <row>
        <entry>Material</entry>
        <entry>Dry Torque (N⋅m)</entry>
        <entry>Lubricated Torque (N⋅m)</entry>
      </row>
    </thead>
    <tbody>
      <row>
        <entry>Steel</entry>
        <entry>25 ±2</entry>
        <entry>20 ±2</entry>
      </row>
      <row>
        <entry>Aluminum</entry>
        <entry>15 ±1</entry>
        <entry>12 ±1</entry>
      </row>
    </tbody>
  </tgroup>
</table>
```

### Table Guidelines
- Include descriptive title
- Define column headers
- Use units in headers
- Include tolerances
- Avoid overly wide tables (max 6 columns preferred)

## References and Links

### Internal References

```xml
<internalRef internalRefId="proc-001">
  <internalRefText>Procedure 001</internalRefText>
</internalRef>
```

### External References

```xml
<externalRef xlink:href="https://standards.easa.europa.eu/CS-25">
  <externalRefText>CS-25 Amendment 27</externalRefText>
</externalRef>
```

### Cross-References
- Use descriptive link text
- Avoid "click here" or "see below"
- Include document number/title
- Verify links during validation

## Acronyms and Abbreviations

### First Use
Define on first use in each DM:

```xml
<para>The <definedTerm>Auxiliary Power Unit (APU)</definedTerm> provides 
electrical power during ground operations.</para>
```

### Subsequent Use
Use acronym without definition:

```xml
<para>Start the APU using the cockpit APU start switch.</para>
```

### Common Acronyms (No definition needed)
- APU, ATA, EASA, FAA, ICAO
- SI units: kg, m, N, Pa, V, A, W
- Standard abbreviations: max, min, approx (avoid)

## Formatting

### Emphasis
- **Bold**: Component names, part numbers
- *Italic*: Software menu items, screen text
- `Monospace`: Code, file names, commands

### Capitalization
- Sentence case for headings and titles
- Title case for proper nouns only
- UPPERCASE for placeholders: CUSTOMER_NAME

### Numbers
- Write out one through nine (procedural)
- Use numerals for 10 and above
- Always use numerals with units: 5 mm
- Use numerals in tables and specifications

### Units
- Use SI units (metric)
- Provide U.S. equivalents in parentheses for dimensions
- Space between number and unit: 25 mm (not 25mm)
- Use standard abbreviations: mm, cm, m, kg, N, Pa

## Quality and Review

### Self-Review Checklist
- [ ] ASD-STE-100 compliance
- [ ] U.S. English spelling
- [ ] Active voice used
- [ ] Safety messages positioned correctly
- [ ] All acronyms defined
- [ ] Figures titled and captioned
- [ ] Cross-references valid
- [ ] UTCS anchor present
- [ ] DMC follows convention
- [ ] Metadata complete

### Peer Review Focus
- Technical accuracy
- Procedural completeness
- Safety adequacy
- Clarity and readability
- Illustration relevance

### QA Review
- BREX compliance (120 rules)
- Schema validation
- Link checking
- Traceability completeness

## Tools and Resources

### Validation Tools
- `validate_brex.py`: BREX rule checker
- XML schema validators
- Schematron processors
- Link checkers

### Reference Materials
- ASD-STE-100 Specification
- S1000D Issue 6.0 Specification
- AMPEL360 Terminology Database
- ATA iSpec 2200

### Support
- Technical Publications: tech-pubs@ampel360.eu
- ASD-STE-100 Questions: simplified-english@ampel360.eu
- BREX Issues: validation@ampel360.eu

---

**Version**: 1.0.0  
**Last Updated**: 2025-10-10  
**Owner**: Technical Publications Office  
**Review Cycle**: Annually or with S1000D/STE updates
