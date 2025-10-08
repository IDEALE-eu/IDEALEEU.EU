# PFMEA

Process Failure Mode and Effects Analysis documentation.

## Overview

PFMEA (Process Failure Mode and Effects Analysis) is a structured approach to identify potential process failures, assess their risk, and establish controls to prevent or detect failures.

## PFMEA Methodology

### Risk Priority Number (RPN)
**RPN = Severity × Occurrence × Detection**

- **Severity (1-10):** Impact on customer/product
- **Occurrence (1-10):** Likelihood of failure cause
- **Detection (1-10):** Ability to detect before delivery

### Risk Rankings

**Severity:**
- 9-10: Hazardous, regulatory non-compliance
- 7-8: Major performance degradation
- 4-6: Minor performance impact
- 1-3: Negligible impact

**Occurrence:**
- 9-10: Very high (>1 in 10)
- 7-8: High (1 in 20 to 1 in 10)
- 4-6: Moderate (1 in 100 to 1 in 20)
- 1-3: Low (<1 in 1000)

**Detection:**
- 9-10: Almost certain not to detect
- 7-8: Low likelihood of detection
- 4-6: Moderate likelihood of detection
- 1-3: High likelihood of detection

## PFMEA Structure

### Header Information
- Process name and number
- PFMEA team members
- Revision date and level
- Responsible engineer

### PFMEA Columns
1. **Process Step** - Operation from process flow
2. **Potential Failure Mode** - How the process could fail
3. **Potential Effects** - Impact on customer/next operation
4. **Severity** - Effect severity rating
5. **Potential Causes** - Root causes of failure
6. **Occurrence** - Cause occurrence rating
7. **Current Process Controls** - Prevention and detection methods
8. **Detection** - Detection rating
9. **RPN** - Risk Priority Number
10. **Recommended Actions** - Risk mitigation activities
11. **Responsibility** - Action owner
12. **Actions Taken** - Completed actions
13. **New RPN** - RPN after actions

## Action Priority

### High Priority (RPN > 100 or Severity = 9-10)
- Immediate action required
- Review at weekly team meetings
- Senior management escalation

### Medium Priority (RPN 50-100)
- Action plan within 30 days
- Monthly review

### Low Priority (RPN < 50)
- Monitor and review annually
- Kaizen opportunities

## Example PFMEA Entries

### Aircraft Wing Assembly

**Process Step:** Composite layup

| Failure Mode | Effects | S | Causes | O | Controls | D | RPN | Actions |
|--------------|---------|---|--------|---|----------|---|-----|---------|
| Missing plies | Structural weakness | 9 | Operator error | 4 | Ply count verification | 3 | 108 | Add automated counting system |
| Wrong orientation | Load path misalignment | 8 | Unclear instructions | 3 | Visual aids, inspection | 4 | 96 | Improve work instructions with photos |
| Contamination | Poor bond quality | 7 | Foreign material | 5 | Clean room, inspection | 4 | 140 | Enhanced cleaning protocols |

### Spacecraft Propulsion Integration

**Process Step:** Thruster installation

| Failure Mode | Effects | S | Causes | O | Controls | D | RPN | Actions |
|--------------|---------|---|--------|---|----------|---|-----|---------|
| Misalignment | Thrust vector error | 9 | Tooling error | 2 | Alignment check | 2 | 36 | None - acceptable |
| Torque error | Leakage or structural failure | 9 | Tool miscalibration | 3 | Calibrated torque wrench | 3 | 81 | Add torque verification step |
| Contamination | Valve malfunction | 8 | Handling | 4 | Cleanroom, covers | 3 | 96 | Improve contamination controls |

## PFMEA Updates

### When to Update
- Design or process changes
- New failure modes discovered
- After quality issues or escapes
- Annual review minimum

### Change Control
- Document revisions with date and reason
- Maintain history of changes
- Communicate to affected personnel
- Update related control plans

## Integration with Control Plans

PFMEA drives control plan requirements:
- High severity items → 100% inspection or SPC
- High occurrence items → Enhanced preventive controls
- High detection items → Improved detection methods

## Documentation

- **PFMEA Template:** See 18-TEMPLATES/PFMEA_TEMPLATE.yaml
- **Storage:** PLM system with revision control
- **Access:** Manufacturing engineering, quality, operators
- **Review Cycle:** Annual or triggered by changes

## References

- Link to **CONTROL_PLAN/** for resulting control requirements
- Link to **PROCESS_FLOW.md** for process steps
- Link to **08-QUALITY** for quality procedures
- Link to **18-TEMPLATES** for PFMEA template
