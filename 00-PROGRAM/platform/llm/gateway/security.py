"""
Security utilities for LLM Gateway.
"""

from typing import Optional
import uuid
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SecurityManager:
    """Manages authentication and authorization."""
    
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def create_access_token(
        self,
        data: dict,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=1)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Optional[dict]:
        """Verify and decode a JWT token."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against a hash."""
        return pwd_context.verify(plain_password, hashed_password)
    
    def hash_password(self, password: str) -> str:
        """Hash a password."""
        return pwd_context.hash(password)


class TenantIsolation:
    """Ensures tenant isolation and namespace validation."""
    
    @staticmethod
    def validate_tenant_access(
        token_tenant_id: str,
        request_tenant_id: str,
        token_project_id: Optional[str] = None,
        request_project_id: Optional[str] = None
    ) -> bool:
        """
        Validate that the token allows access to the requested tenant/project.
        """
        if token_tenant_id != request_tenant_id:
            return False
        
        if token_project_id and request_project_id:
            if token_project_id != request_project_id:
                return False
        
        return True
    
    @staticmethod
    def get_namespace(tenant_id: str, project_id: str) -> str:
        """Get the namespace identifier for tenant/project."""
        return f"{tenant_id}/{project_id}"


class AuditLogger:
    """Audit logging for security events."""
    
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
    
    async def log_request(
        self,
        request_id: str,
        tenant_id: str,
        project_id: str,
        user_id: str,
        action: str,
        details: dict
    ):
        """Log a request for audit purposes."""
        if not self.enabled:
            return
        
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "request_id": request_id,
            "tenant_id": tenant_id,
            "project_id": project_id,
            "user_id": user_id,
            "action": action,
            "details": details
        }
        
        # In production, this would write to a secure, append-only log store
        # For now, we'll just use structured logging
        import structlog
        logger = structlog.get_logger()
        logger.info("audit_log", **log_entry)
    
    async def log_guardrails_violation(
        self,
        request_id: str,
        tenant_id: str,
        project_id: str,
        user_id: str,
        violations: list
    ):
        """Log guardrails violations."""
        await self.log_request(
            request_id=request_id,
            tenant_id=tenant_id,
            project_id=project_id,
            user_id=user_id,
            action="guardrails_violation",
            details={"violations": violations}
        )


class KMSManager:
    """Key Management Service integration."""
    
    def __init__(self, provider: str = "local", **kwargs):
        self.provider = provider
        self.config = kwargs
    
    async def encrypt(self, plaintext: str, key_id: str) -> str:
        """Encrypt data using KMS."""
        if self.provider == "local":
            # For local development, use simple encoding
            # In production, use actual KMS
            import base64
            return base64.b64encode(plaintext.encode()).decode()
        
        elif self.provider == "aws":
            import boto3
            kms = boto3.client("kms")
            response = kms.encrypt(
                KeyId=key_id,
                Plaintext=plaintext.encode()
            )
            import base64
            return base64.b64encode(response["CiphertextBlob"]).decode()
        
        else:
            raise NotImplementedError(f"KMS provider {self.provider} not implemented")
    
    async def decrypt(self, ciphertext: str, key_id: str) -> str:
        """Decrypt data using KMS."""
        if self.provider == "local":
            import base64
            return base64.b64decode(ciphertext.encode()).decode()
        
        elif self.provider == "aws":
            import boto3
            import base64
            kms = boto3.client("kms")
            ciphertext_blob = base64.b64decode(ciphertext.encode())
            response = kms.decrypt(
                CiphertextBlob=ciphertext_blob
            )
            return response["Plaintext"].decode()
        
        else:
            raise NotImplementedError(f"KMS provider {self.provider} not implemented")
