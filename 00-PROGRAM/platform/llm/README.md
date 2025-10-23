# LLM Playground

Multi-tenant sandbox for trained, contextualized AI over IDEALE-EU data.

## Overview

The LLM Playground provides a secure, multi-tenant environment for interacting with Large Language Models (LLMs) in the context of aerospace systems data. It includes:

- **Multi-provider support**: OpenAI, Anthropic, and more
- **Tenant isolation**: Strict namespace separation with audit trails
- **RAG integration**: Context-aware responses grounded in documentation
- **Guardrails**: Safety validation for inputs and outputs
- **Evaluation framework**: Metrics and golden sets for quality assessment

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Playground UI                             │
│              (Multi-tenant Web Interface)                    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    LLM Gateway                               │
│        (Authentication, Routing, Audit)                      │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ OpenAI   │  │Anthropic │  │  Azure   │  │  Custom  │   │
│  │ Provider │  │ Provider │  │ OpenAI   │  │ Provider │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
         │                │                │
         ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Guardrails  │  │     RAG      │  │   Embeddings │
│   Service    │  │  Retrieval   │  │   Service    │
└──────────────┘  └──────────────┘  └──────────────┘
                          │
                          ▼
                  ┌──────────────┐
                  │ Vector Store │
                  │  (pgvector/  │
                  │   Qdrant)    │
                  └──────────────┘
```

## Components

### 1. LLM Gateway (`/00-PROGRAM/platform/llm/gateway`)

Central service for LLM interactions with multi-provider support.

**Key Features:**
- Multi-provider abstraction (OpenAI, Anthropic, Azure OpenAI)
- Tenant/project namespace isolation
- JWT-based authentication
- Request/response audit logging
- Rate limiting
- Cost tracking
- KMS integration for encryption

**API Endpoints:**
- `POST /llm/chat` - Chat completion
- `POST /llm/embed` - Generate embeddings
- `POST /knowledge/sync` - Sync knowledge base
- `POST /contexts` - Create context

**Configuration:**
```bash
IDEALE_DB_URL=postgresql://user:pass@localhost:5432/ideale_llm
JWT_SIGNING_KEY=your-secret-key
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
KMS_PROVIDER=aws|azure|gcp|local
```

### 2. Guardrails Service (`/00-PROGRAM/platform/llm/guardrails`)

Validates inputs and outputs for safety and compliance.

**Checks:**
- PII detection (email, SSN, credit cards, phone numbers)
- Prompt injection detection
- Prohibited content (ITAR, export control, classified)
- Output safety (XSS, malicious content)

**Usage:**
```python
from guardrails.engine import GuardrailsEngine

engine = GuardrailsEngine()

# Validate input
checks = await engine.validate_input(user_input, context={})

# Validate output
checks = await engine.validate_output(llm_output, context={})

# Full interaction validation
result = await engine.validate_full_interaction(
    input_text=user_input,
    output_text=llm_output,
    context={}
)
```

### 3. Embedding Service (`/00-PROGRAM/platform/llm/embed`)

Generate embeddings for text using multiple models.

**Supported Models:**
- sentence-transformers (local)
- OpenAI embeddings (API)
- Custom models

**Usage:**
```python
from embed.service import EmbeddingService

service = EmbeddingService()

result = await service.generate_embeddings(
    texts=["Document text here"],
    model="sentence-transformers/all-MiniLM-L6-v2",
    normalize=True
)

# Compute similarity
similarity = await service.compute_similarity(
    embedding1=[...],
    embedding2=[...]
)
```

### 4. RAG Service (`/00-PROGRAM/platform/llm/rag`)

Retrieval-Augmented Generation for context-aware responses.

**Components:**
- Document processor: Chunking and metadata extraction
- Retriever: Vector search and context formatting

**Usage:**
```python
from rag.document_processor import DocumentProcessor
from rag.retriever import RAGRetriever

# Process documents
processor = DocumentProcessor(chunk_size=512, chunk_overlap=50)
chunks = processor.process_text(text, document_id="doc1")

# Retrieve relevant context
retriever = RAGRetriever(vector_store, embedding_service)
result = await retriever.retrieve_and_format(
    query="What is the propulsion system?",
    context_id="aerospace-docs",
    top_k=5
)
```

### 5. Vector Store (`/00-PROGRAM/platform/vector`)

Adapters for vector databases.

**Supported Backends:**
- PostgreSQL with pgvector
- Qdrant

**Usage:**
```python
from vector.pgvector_adapter import PgVectorAdapter
# or
from vector.qdrant_adapter import QdrantAdapter

# Initialize
vector_store = PgVectorAdapter(connection_url="postgresql://...")

# Create collection
await vector_store.create_collection(
    collection_name="docs",
    dimension=384
)

# Insert vectors
await vector_store.insert(
    collection_name="docs",
    vectors=[[0.1, 0.2, ...]],
    texts=["Document text"],
    metadata=[{"source": "manual.pdf"}]
)

# Search
results = await vector_store.search(
    collection_name="docs",
    query_vector=[0.1, 0.2, ...],
    top_k=5
)
```

### 6. Evaluation Framework (`/00-PROGRAM/platform/llm/eval`)

Metrics and golden sets for quality assessment.

**Metrics:**
- Exact Match (EM)
- Token-level F1 Score
- Groundedness Score
- Latency Statistics
- Cost Statistics

**Usage:**
```python
from eval.metrics import EvaluationMetrics
from eval.golden_sets import GoldenSetManager, GoldenExample

# Calculate metrics
em_score = EvaluationMetrics.exact_match(prediction, reference)
f1_score = EvaluationMetrics.f1_score(prediction, reference)

groundedness = EvaluationMetrics.groundedness_score(
    prediction=llm_output,
    context=retrieved_docs,
    threshold=0.7
)

# Manage golden sets
manager = GoldenSetManager(storage_path="./golden_sets")

example = GoldenExample(
    id="ex1",
    query="What is the wingspan?",
    reference_answer="35 meters",
    context="..."
)

manager.add_example("aircraft_qa", example)
manager.save_golden_set("aircraft_qa")
```

### 7. Playground UI (`/00-PROGRAM/platform/playground-ui`)

Web interface for interacting with the LLM Playground.

**Features:**
- Model selection (GPT-4, Claude, etc.)
- Temperature and max tokens configuration
- Context selection for RAG
- Real-time chat interface
- Status indicators (gateway, guardrails, audit)

**Run:**
```bash
cd 00-PROGRAM/platform/playground-ui
pip install -r requirements.txt
python main.py
# Open http://localhost:8080
```

## Security

### Tenant Isolation

All requests are scoped to `{tenant_id}/{project_id}` namespaces. JWT tokens enforce access control:

```json
{
  "user_id": "user123",
  "tenant_id": "tenant1",
  "project_id": "project1",
  "exp": 1234567890
}
```

### KMS Integration

Sensitive data is encrypted using KMS:

- AWS KMS
- Azure Key Vault
- Google Cloud KMS
- Local encryption (development only)

### Audit Logging

All interactions are logged:

```json
{
  "timestamp": "2025-10-23T17:00:00Z",
  "request_id": "req-123",
  "tenant_id": "tenant1",
  "project_id": "project1",
  "user_id": "user123",
  "action": "chat",
  "model": "gpt-4",
  "tokens": 150,
  "latency_ms": 1234,
  "cost_usd": "0.003",
  "guardrails_passed": true
}
```

### Retention

- Audit logs: 90 days (configurable)
- PII is never stored
- Prompt/response data can be configured for retention

## API Reference

### POST /llm/chat

Chat completion endpoint.

**Request:**
```json
{
  "messages": [
    {"role": "user", "content": "What is the wingspan?"}
  ],
  "model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 1024,
  "context_ids": ["ctx-1"],
  "tenant_id": "tenant1",
  "project_id": "project1"
}
```

**Response:**
```json
{
  "id": "req-123",
  "model": "gpt-4",
  "content": "The wingspan is 35 meters...",
  "prompt_tokens": 50,
  "completion_tokens": 100,
  "total_tokens": 150,
  "latency_ms": 1234,
  "cost_usd": "0.003",
  "guardrails_passed": true,
  "retrieved_contexts": [...]
}
```

### POST /llm/embed

Generate embeddings.

**Request:**
```json
{
  "input": "Text to embed",
  "model": "text-embedding-ada-002",
  "tenant_id": "tenant1",
  "project_id": "project1"
}
```

**Response:**
```json
{
  "id": "req-124",
  "model": "text-embedding-ada-002",
  "embeddings": [[0.1, 0.2, ...]],
  "tokens": 5,
  "latency_ms": 234,
  "cost_usd": "0.00001"
}
```

## Testing

Each component has comprehensive tests:

```bash
# Gateway tests
cd 00-PROGRAM/platform/llm/gateway
pip install -r requirements.txt
pytest tests/ -v --cov=.

# Guardrails tests
cd 00-PROGRAM/platform/llm/guardrails
pip install -r requirements.txt
pytest tests/ -v --cov=.

# Evaluation tests
cd 00-PROGRAM/platform/llm/eval
pip install -r requirements.txt
pytest tests/ -v --cov=.
```

## Deployment

### Local Development

```bash
# Set environment variables
export IDEALE_DB_URL="postgresql://user:pass@localhost:5432/ideale"
export JWT_SIGNING_KEY="dev-secret-key"
export OPENAI_API_KEY="sk-..."

# Run gateway
cd 00-PROGRAM/platform/llm/gateway
pip install -r requirements.txt
python main.py

# Run playground UI (separate terminal)
cd 00-PROGRAM/platform/playground-ui
pip install -r requirements.txt
python main.py
```

### Docker

```bash
# Build images
docker build -t ideale-llm-gateway ./00-PROGRAM/platform/llm/gateway
docker build -t ideale-playground-ui ./00-PROGRAM/platform/playground-ui

# Run with docker-compose
docker-compose up -d
```

### Kubernetes

```bash
# Deploy with Helm
helm install ideale-llm ./infra/helm/idealeeu-llm \
  --set gateway.replicas=3 \
  --set postgresql.enabled=true
```

## Monitoring

### Metrics

- Request rate (requests/sec)
- Latency (p50, p95, p99)
- Error rate
- Token usage
- Cost per tenant/project

### Logs

Structured JSON logs with:
- Request ID (trace)
- Tenant/project context
- User ID
- Action
- Outcome
- Timing

### Alerts

- High error rate
- Guardrails violations
- Quota exceeded
- Unusual cost patterns

## Cost Management

Track and limit costs per tenant/project:

```python
# Configure quotas in TenantConfig
config = TenantConfig(
    tenant_id="tenant1",
    max_requests_per_day=1000,
    max_tokens_per_request=4096,
    allowed_models=["gpt-3.5-turbo", "gpt-4"]
)
```

## Golden Sets

Example golden set for aerospace Q&A:

```json
[
  {
    "id": "ex1",
    "query": "What is the maximum takeoff weight?",
    "reference_answer": "The maximum takeoff weight (MTOW) is 79,000 kg.",
    "context": "Technical specifications document excerpt...",
    "metadata": {
      "category": "specifications",
      "difficulty": "easy"
    }
  }
]
```

## Shadow Runs

Test model changes without impacting users:

```python
# Run shadow evaluation
shadow_results = await run_shadow_evaluation(
    golden_set="aircraft_qa",
    baseline_model="gpt-3.5-turbo",
    candidate_model="gpt-4",
    metrics=["em", "f1", "groundedness", "latency", "cost"]
)
```

## References

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [Qdrant Documentation](https://qdrant.tech/documentation/)

## Support

For issues or questions, open a GitHub issue or contact the team.
