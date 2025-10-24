"""
Guardrails validation engine.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import re


@dataclass
class GuardrailCheck:
    """Result of a guardrail check."""
    check_name: str
    passed: bool
    severity: str  # info, warning, error
    message: Optional[str] = None


class GuardrailsEngine:
    """
    Validates LLM inputs and outputs against safety and compliance rules.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.checks_enabled = self.config.get("enabled_checks", [
            "pii_detection",
            "prohibited_content",
            "prompt_injection",
            "output_validation"
        ])
    
    async def validate_input(self, text: str, context: Dict[str, Any]) -> List[GuardrailCheck]:
        """Validate user input before sending to LLM."""
        checks = []
        
        # PII detection
        if "pii_detection" in self.checks_enabled:
            checks.append(self._check_pii(text))
        
        # Prompt injection detection
        if "prompt_injection" in self.checks_enabled:
            checks.append(self._check_prompt_injection(text))
        
        # Prohibited content
        if "prohibited_content" in self.checks_enabled:
            checks.append(self._check_prohibited_content(text))
        
        return checks
    
    async def validate_output(self, text: str, context: Dict[str, Any]) -> List[GuardrailCheck]:
        """Validate LLM output before returning to user."""
        checks = []
        
        # Output validation
        if "output_validation" in self.checks_enabled:
            checks.append(self._check_output_safety(text))
        
        # PII in output
        if "pii_detection" in self.checks_enabled:
            checks.append(self._check_pii(text, context="output"))
        
        return checks
    
    def _check_pii(self, text: str, context: str = "input") -> GuardrailCheck:
        """Check for Personally Identifiable Information."""
        # Simplified PII patterns (in production, use Presidio or similar)
        pii_patterns = [
            (r'\b\d{3}-\d{2}-\d{4}\b', "SSN"),  # US SSN
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "Email"),
            (r'\b\d{16}\b', "Credit Card"),
            (r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', "Phone Number"),
        ]
        
        found_pii = []
        for pattern, pii_type in pii_patterns:
            if re.search(pattern, text):
                found_pii.append(pii_type)
        
        if found_pii:
            return GuardrailCheck(
                check_name=f"pii_detection_{context}",
                passed=False,
                severity="error",
                message=f"Detected PII: {', '.join(found_pii)}"
            )
        
        return GuardrailCheck(
            check_name=f"pii_detection_{context}",
            passed=True,
            severity="info"
        )
    
    def _check_prompt_injection(self, text: str) -> GuardrailCheck:
        """Check for prompt injection attempts."""
        # Common prompt injection patterns
        injection_patterns = [
            r'ignore\s+(previous|all)\s+instructions',
            r'disregard\s+(previous|all)\s+instructions',
            r'forget\s+(previous|all)\s+instructions',
            r'system:\s*you\s+are',
            r'[<\[]system[>\]]',
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return GuardrailCheck(
                    check_name="prompt_injection",
                    passed=False,
                    severity="error",
                    message="Potential prompt injection detected"
                )
        
        return GuardrailCheck(
            check_name="prompt_injection",
            passed=True,
            severity="info"
        )
    
    def _check_prohibited_content(self, text: str) -> GuardrailCheck:
        """Check for prohibited or sensitive content."""
        # Aerospace-specific prohibited topics
        prohibited_keywords = [
            "itar",
            "export control",
            "classified",
            "confidential proprietary",
            "cui",  # Controlled Unclassified Information
        ]
        
        text_lower = text.lower()
        found_prohibited = [kw for kw in prohibited_keywords if kw in text_lower]
        
        if found_prohibited:
            return GuardrailCheck(
                check_name="prohibited_content",
                passed=False,
                severity="warning",
                message=f"Potentially sensitive content detected: {', '.join(found_prohibited)}"
            )
        
        return GuardrailCheck(
            check_name="prohibited_content",
            passed=True,
            severity="info"
        )
    
    def _check_output_safety(self, text: str) -> GuardrailCheck:
        """Validate output is safe and appropriate."""
        # Check for common harmful patterns
        harmful_patterns = [
            r'<script[^>]*>.*?</script>',  # XSS
            r'javascript:',
            r'onerror\s*=',
        ]
        
        for pattern in harmful_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return GuardrailCheck(
                    check_name="output_safety",
                    passed=False,
                    severity="error",
                    message="Unsafe content detected in output"
                )
        
        return GuardrailCheck(
            check_name="output_safety",
            passed=True,
            severity="info"
        )
    
    def sanitize_output(self, text: str) -> str:
        """Sanitize output by removing potentially harmful content."""
        # Remove HTML/script tags
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r'<[^>]+>', '', text)
        
        return text
    
    async def validate_full_interaction(
        self,
        input_text: str,
        output_text: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Validate a full LLM interaction (input and output).
        
        Returns:
            {
                "passed": bool,
                "input_checks": List[GuardrailCheck],
                "output_checks": List[GuardrailCheck],
                "sanitized_output": Optional[str]
            }
        """
        input_checks = await self.validate_input(input_text, context)
        output_checks = await self.validate_output(output_text, context)
        
        all_passed = all(check.passed for check in input_checks + output_checks)
        
        # Sanitize output if needed
        sanitized_output = None
        if not all_passed:
            sanitized_output = self.sanitize_output(output_text)
        
        return {
            "passed": all_passed,
            "input_checks": input_checks,
            "output_checks": output_checks,
            "sanitized_output": sanitized_output
        }
