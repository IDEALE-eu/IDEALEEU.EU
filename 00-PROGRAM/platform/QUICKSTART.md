# Quick Start Guide

## Prerequisites

- Python 3.11+
- PostgreSQL 14+ with pgvector extension
- (Optional) Qdrant for vector storage
- OpenAI and/or Anthropic API keys

## Installation

### 1. Database Setup

```bash
# Install PostgreSQL and pgvector
# On Ubuntu/Debian:
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install postgresql-14-pgvector

# Create database
sudo -u postgres psql
CREATE DATABASE ideale_llm;
CREATE DATABASE ideale_vectors;
CREATE USER ideale WITH PASSWORD 'changeme';
GRANT ALL PRIVILEGES ON DATABASE ideale_llm TO ideale;
GRANT ALL PRIVILEGES ON DATABASE ideale_vectors TO ideale;
\q
```

### 2. Environment Configuration

```bash
cd 00-PROGRAM/platform
cp .env.example .env
# Edit .env with your API keys and database URLs
```

### 3. Install Gateway

```bash
cd llm/gateway
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run Gateway

```bash
# Still in llm/gateway directory with venv activated
python main.py
# Gateway runs on http://localhost:8000
```

### 5. Install and Run Playground UI

```bash
# New terminal
cd 00-PROGRAM/platform/playground-ui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
# UI runs on http://localhost:8080
```

## Testing

### Run Gateway Tests

```bash
cd llm/gateway
source venv/bin/activate
pip install pytest pytest-asyncio pytest-cov
pytest tests/ -v --cov=.
```

### Run Guardrails Tests

```bash
cd llm/guardrails
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

### Run Evaluation Tests

```bash
cd llm/eval
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Example Usage

### 1. Get Access Token

```bash
# Use the security manager to create a token
python3 << EOF
from llm.gateway.security import SecurityManager
from datetime import timedelta

manager = SecurityManager(secret_key="your-secret-key")
token = manager.create_access_token(
    data={
        "user_id": "demo-user",
        "tenant_id": "demo-tenant",
        "project_id": "demo-project"
    },
    expires_delta=timedelta(hours=24)
)
print(f"Token: {token}")
EOF
```

### 2. Chat Completion

```bash
curl -X POST http://localhost:8000/llm/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "messages": [
      {"role": "user", "content": "What is the wing span of the BWB aircraft?"}
    ],
    "model": "gpt-4",
    "temperature": 0.7,
    "tenant_id": "demo-tenant",
    "project_id": "demo-project"
  }'
```

### 3. Generate Embeddings

```bash
curl -X POST http://localhost:8000/llm/embed \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "input": "The aircraft has a wingspan of 35 meters",
    "model": "text-embedding-ada-002",
    "tenant_id": "demo-tenant",
    "project_id": "demo-project"
  }'
```

### 4. Create Context for RAG

```bash
curl -X POST http://localhost:8000/contexts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "name": "aircraft-specs",
    "description": "Aircraft technical specifications",
    "tenant_id": "demo-tenant",
    "project_id": "demo-project"
  }'
```

## Production Deployment

### Docker Compose

```yaml
version: '3.8'
services:
  postgres:
    image: pgvector/pgvector:pg14
    environment:
      POSTGRES_DB: ideale_llm
      POSTGRES_USER: ideale
      POSTGRES_PASSWORD: changeme
    volumes:
      - postgres_data:/var/lib/postgresql/data

  gateway:
    build: ./llm/gateway
    ports:
      - "8000:8000"
    environment:
      - IDEALE_DB_URL=postgresql://ideale:changeme@postgres:5432/ideale_llm
      - JWT_SIGNING_KEY=${JWT_SIGNING_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - postgres

  playground:
    build: ./playground-ui
    ports:
      - "8080:8080"
    depends_on:
      - gateway

volumes:
  postgres_data:
```

### Kubernetes

```bash
# Using Helm
helm install ideale-llm ./infra/helm/idealeeu-llm \
  --set gateway.replicas=3 \
  --set postgresql.enabled=true \
  --set ingress.enabled=true \
  --set ingress.host=llm.idealeeu.eu
```

## Monitoring

### Health Checks

```bash
# Gateway health
curl http://localhost:8000/health

# Playground health
curl http://localhost:8080/health
```

### Logs

Gateway uses structured logging. Example:

```json
{
  "timestamp": "2025-10-23T17:00:00Z",
  "level": "info",
  "event": "request_completed",
  "request_id": "req-123",
  "tenant_id": "demo-tenant",
  "action": "chat",
  "latency_ms": 1234,
  "status": "success"
}
```

## Troubleshooting

### Database Connection Issues

```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Test connection
psql -h localhost -U ideale -d ideale_llm
```

### pgvector Extension Not Found

```sql
-- In psql:
CREATE EXTENSION IF NOT EXISTS vector;
```

### Import Errors

```bash
# Ensure you're in the virtual environment
which python
# Should show path to venv

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## Next Steps

1. Configure production API keys
2. Set up monitoring (Prometheus, Grafana)
3. Enable TLS/SSL
4. Configure backup and retention policies
5. Set up CI/CD pipelines
6. Add custom LLM providers
7. Integrate with existing authentication system

## Support

For issues or questions:
- Open a GitHub issue
- Check the documentation: `00-PROGRAM/platform/llm/README.md`
- Review implementation summary: `00-PROGRAM/platform/IMPLEMENTATION_SUMMARY.md`
