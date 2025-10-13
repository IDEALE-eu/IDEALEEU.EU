# Language Guide — ASD-STE-100 for AMPEL360 AIR-T

## Purpose

This guide provides language standards based on **ASD-STE-100 (Simplified Technical English)** for AMPEL360 AIR-T technical documentation. STE ensures clarity, consistency, and translatability of technical content.

## What is ASD-STE-100?

**Simplified Technical English (STE)** is:
- A controlled language specification
- Designed for aerospace maintenance documentation
- Focuses on clarity and simplicity
- Reduces ambiguity and misunderstanding
- Improves translatability

### Core Principles

1. **Use simple words**: One meaning per word
2. **Short sentences**: Maximum 20-25 words
3. **Active voice**: "Remove the cover" not "The cover should be removed"
4. **Present tense**: For procedures and descriptions
5. **Imperative mood**: For instructions

## Approved Word Types

### Technical Words
**Technical words** are specific to your technical domain:
- Component names: "actuator", "manifold", "bulkhead"
- System names: "hydraulic system", "fuel cell"
- Technical verbs: "torque", "calibrate", "pressurize"

**Rules:**
- Use consistently (same word for same item)
- Define on first use if not in dictionary
- Avoid synonyms

### General Words
**General words** are from the STE dictionary (~900 words):
- Common verbs: make, do, get, put, remove, install
- Common nouns: part, equipment, person, tool
- Common adjectives: clean, dry, hot, cold

**Rules:**
- Use only approved meaning
- Check STE dictionary for allowed usage
- One meaning per word

## Sentence Structure

### Maximum Length
- **Procedural sentences**: 20 words maximum
- **Descriptive sentences**: 25 words maximum
- **Tables and notes**: 25 words maximum

**Example:**
- ❌ "Before you start to do the procedure, make sure that you have all the necessary tools and that you have read all the safety warnings that apply to this procedure." (32 words)
- ✅ "Before you start, read the safety warnings. Make sure that you have all the necessary tools." (17 words)

### One Instruction Per Sentence
- ❌ "Remove the cover and disconnect the cable."
- ✅ "Remove the cover. Disconnect the cable."

**Exception**: Related actions can be combined if total ≤ 20 words:
- ✅ "Remove the two screws and lift off the cover."

### Sentence Structure Patterns

#### Simple Sentences (Preferred)
```
Subject + Verb + Object
"The technician removes the panel."
```

#### Imperative (For instructions)
```
Verb + Object
"Remove the panel."
```

#### Conditional (When needed)
```
If/When + Condition, Action
"If the light is on, turn off the power."
```

## Voice and Tense

### Active Voice (Required)
- ✅ Active: "Remove the cover."
- ❌ Passive: "The cover should be removed."
- ❌ Passive: "The cover is removed by the technician."

**Exceptions**: Passive allowed when:
- Agent is unknown or unimportant
- Focus is on the object, not the agent

Example: "The component is manufactured in Germany." (origin is the focus)

### Present Tense (Required)
- ✅ Present: "The pump supplies hydraulic pressure."
- ❌ Future: "The pump will supply hydraulic pressure."
- ❌ Past: "The pump supplied hydraulic pressure."

**Exception**: Past tense for maintenance history or troubleshooting:
- "The component failed during the last inspection."

### Imperative Mood (For Instructions)
- ✅ Imperative: "Install the gasket."
- ❌ Infinitive: "To install the gasket..."
- ❌ Future: "You will install the gasket."
- ❌ Permissive: "You should install the gasket."

## Word Choice

### Approved Verbs (Examples)

| Approved | Not Approved | Reason |
|----------|-------------|---------|
| remove | take off | Ambiguous |
| install | put in | Vague |
| torque | tighten to torque | Wordy |
| connect | hook up | Informal |
| disconnect | unhook | Informal |
| examine | check, inspect | Use "examine" for close inspection |
| clean | wipe | "Clean" covers all methods |

### Prohibited Words and Phrases

#### Vague Adverbs
- ❌ carefully
- ❌ properly
- ❌ sufficiently
- ❌ adequately
- ❌ correctly

**Instead**: Provide specific instructions
- ✅ "Torque to 25 N⋅m ±2 N⋅m." (not "Tighten carefully")
- ✅ "Align the marks on the shaft and housing." (not "Align properly")

#### Intensifiers
- ❌ very
- ❌ really
- ❌ quite
- ❌ extremely

**Instead**: Use precise adjectives
- ✅ "critical" (not "very important")
- ✅ "essential" (not "really necessary")

#### Vague Adjectives
- ❌ approximately
- ❌ about (in measurements)
- ❌ around (in measurements)

**Instead**: Provide tolerances
- ✅ "25 mm ±1 mm" (not "approximately 25 mm")

#### Permissive Language
- ❌ may
- ❌ might
- ❌ should
- ❌ could

**Instead**: Use imperative or state facts
- ✅ "Remove the cover if the seal is damaged." (not "You may remove...")
- ✅ "The pressure can decrease." (not "The pressure might decrease.")

## Special Constructions

### Articles (a, an, the)
**Use articles** to improve clarity:
- ✅ "Remove the cover." (specific cover)
- ✅ "Install a new gasket." (any new gasket)

**Omit articles** in:
- Lists
- Part number references
- Headings

### Noun Clusters
**Limit to 3 nouns** in a cluster:
- ❌ "fuel cell hydrogen supply line pressure regulator valve"
- ✅ "pressure regulator valve for the hydrogen supply line of the fuel cell"

**Break into smaller parts** or use prepositions:
- Use "of", "for", "in", "on"

### Verb Forms
**Use simple verb forms**:
- ✅ "The pump starts." (present simple)
- ❌ "The pump is starting." (present continuous)
- ❌ "The pump has started." (present perfect)

**Exception**: Use -ing form after prepositions:
- ✅ "Before starting the engine..."

## Numbers and Measurements

### Writing Numbers
- **One through nine**: Write as words in text
  - "Install three bolts."
- **10 and above**: Use numerals
  - "Install 12 bolts."
- **With units**: Always use numerals
  - "5 mm", "3 kg", "7 bolts"
- **At sentence start**: Write as words
  - "Twenty bolts are required."

### Units of Measure
**Use SI units** with proper spacing:
- ✅ 25 mm (space between number and unit)
- ❌ 25mm (no space)

**Abbreviations** (no period):
- mm, cm, m, km
- g, kg
- N, kN
- Pa, kPa, MPa
- °C (note: degree symbol)

**U.S. equivalents** (in parentheses):
- "25 mm (0.98 in)"
- "10 kg (22 lb)"

### Tolerances
**Always specify tolerances**:
- ✅ "25 mm ±1 mm"
- ✅ "100 N⋅m ±5 N⋅m"
- ❌ "approximately 25 mm"

## Punctuation

### Period (.)
- End of sentences
- Abbreviations with multiple words: "e.g.", "i.e."
- Not after single-word abbreviations: mm, kg, V

### Comma (,)
- Separate items in lists: "Remove the cover, gasket, and seal."
- After introductory phrases: "After removal, clean the surface."
- Between independent clauses with conjunctions: "Remove the cover, and disconnect the cable."

### Colon (:)
- Introduce lists
- Introduce explanations
- Not after "such as" or "including"

### Hyphen (-)
- Compound adjectives before nouns: "high-pressure line"
- Not after adverbs ending in -ly: "highly pressurized line"
- Number ranges: "10-15 mm"

### Parentheses ( )
- U.S. equivalents: "25 mm (0.98 in)"
- Alternative names: "APU (Auxiliary Power Unit)"
- Clarifications: "Install the new gasket (P/N 12345)."

## Lists

### When to Use Lists
- **Three or more items**: Use a list instead of commas
- **Sequential steps**: Use numbered list
- **Unordered items**: Use bulleted list

### List Structure
**Parallel structure required**:
- ✅ All items start with verbs: "Remove...", "Install...", "Connect..."
- ✅ All items are nouns: "Wrench", "Screwdriver", "Pliers"
- ❌ Mixed: "Remove the cover", "Installation of gasket", "Connect"

**Capitalization**:
- First word capitalized
- No period at end of items (unless full sentences)

**Example**:
```
Tools:
- 10 mm wrench
- Torque wrench (50-250 N⋅m)
- Digital multimeter
```

## Technical Descriptions

### Component Descriptions
**Pattern**: Location + Function + Characteristics
- "The fuel pump (1) is on the forward side of the tank. It supplies fuel to the engine. The pump has a maximum flow rate of 50 L/min."

### System Descriptions
**Pattern**: Purpose + Components + Operation
- "The hydraulic system supplies pressure for flight controls. The system has a pump, reservoir, and distribution manifold. The pump pressurizes fluid to 3000 psi."

### Specifications
**Use tables** for specifications:

| Parameter | Value |
|-----------|-------|
| Voltage | 28 V DC ±2 V |
| Current | 5 A maximum |
| Temperature range | -40°C to +85°C |

## Procedures

### Procedural Step Pattern
```
[Condition] + Action + [Object] + [Method] + [Result]
```

**Examples**:
- Simple: "Remove the cover."
- With condition: "If the seal is damaged, install a new seal."
- With method: "Remove the cover with a 10 mm wrench."
- With result: "Torque the bolt to 25 N⋅m. The bolt is tight."

### Conditional Steps
**Use "if" or "when"**:
- ✅ "If the light is on, turn off the power."
- ✅ "When the engine stops, close the fuel valve."
- ❌ "In case the light is on..." (wordy)

### Sequential Steps
**Number steps explicitly**:
```
1. Turn off the power.
2. Wait 5 minutes.
3. Disconnect the cable.
```

## Warnings and Cautions

### Language Requirements
- **First sentence**: State the hazard
- **Second sentence**: State the consequence
- **Third sentence**: State the preventive action

**Example**:
```
WARNING
High voltage is present. Risk of electrocution can occur.
Make sure that the power is off before you start.
```

### Clarity in Safety Messages
- ✅ "Do not touch the hot surface."
- ❌ "Be careful not to touch the surface."

- ✅ "Risk of burns can occur."
- ❌ "You might get burned."

## Common Mistakes and Corrections

### Mistake 1: Passive Voice
- ❌ "The cover should be removed."
- ✅ "Remove the cover."

### Mistake 2: Future Tense
- ❌ "You will disconnect the cable."
- ✅ "Disconnect the cable."

### Mistake 3: Vague Adverbs
- ❌ "Tighten the bolt carefully."
- ✅ "Torque the bolt to 25 N⋅m ±2 N⋅m."

### Mistake 4: Long Sentences
- ❌ "Before you start to do the procedure, make sure that the power is off and that you have all the tools that you need." (25 words)
- ✅ "Before you start, make sure that the power is off. Make sure that you have all the tools." (19 words)

### Mistake 5: Noun Clusters
- ❌ "fuel cell hydrogen supply line pressure regulator"
- ✅ "pressure regulator for the hydrogen supply line of the fuel cell"

### Mistake 6: Permissive Language
- ❌ "You may remove the cover."
- ✅ "Remove the cover if necessary."

## AMPEL360-Specific Terminology

### Hydrogen Systems
- **Approved**: hydrogen, H₂ (subscript 2), cryogenic hydrogen
- **Not approved**: liquid hydrogen fuel (use "cryogenic hydrogen")

### Fuel Cell
- **Approved**: fuel cell, fuel cell stack
- **Not approved**: fuel cell system (use "fuel cell" or specify: "fuel cell and control unit")

### Battery Systems
- **Approved**: battery, battery pack, high-voltage battery
- **Not approved**: HV battery (spell out on first use)

### Airframe
- **Approved**: center body, forward section, aft section
- **Not approved**: fuselage (BWB has no traditional fuselage; use "center body")

## Tools and Resources

### ASD-STE-100 Dictionary
- Download from ASD website
- Check approved words and meanings
- Propose additions through technical publications office

### AMPEL360 Terminology Database
- Program-specific approved terms
- Component names and part numbers
- System and subsystem names

### Validation Tools
- STE checker software
- BREX rules enforce STE compliance
- Automated sentence length checking

## Compliance Checklist

- [ ] Sentences ≤ 20-25 words
- [ ] Active voice used
- [ ] Present tense used
- [ ] Imperative mood for instructions
- [ ] No vague adverbs (carefully, properly, etc.)
- [ ] No intensifiers (very, really, quite)
- [ ] Specific measurements with tolerances
- [ ] Articles (a, an, the) used correctly
- [ ] Noun clusters ≤ 3 words
- [ ] Technical terms defined on first use
- [ ] Safety messages clear and specific

## Support and Training

### Training Resources
- ASD-STE-100 online training
- AMPEL360 STE workshops (quarterly)
- Technical writing certification program

### Support Contacts
- **STE Questions**: simplified-english@ampel360.eu
- **Terminology**: terminology@ampel360.eu
- **Technical Publications**: tech-pubs@ampel360.eu

---

**Version**: 1.0.0  
**Based on**: ASD-STE-100 Issue 8  
**Last Updated**: 2025-10-10  
**Owner**: Technical Publications Office  
**Review Cycle**: With ASD-STE-100 updates
