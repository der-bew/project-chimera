# Technical Specifications
### 1. API Contracts (JSON Schemas)
All internal messages must adhere to these Pydantic schemas.

#### 1.1 Task Object (Planner -> Worker)
```{  "task_id": "uuid-v4",  "task_type": "generate_content | reply_comment | execute_transaction",  "priority": "high | medium | low",  "created_at": "iso8601-timestamp",  "context": {    "goal_description": "string",    "persona_id": "string",    "mcp_resources": ["list of resource URIs"]  }} ```
#### 1.2 Result Object (Worker -> Judge)
```json
    {
    "task_id": "uuid-v4",
    "worker_id": "string",
    "status": "success | failure",
    "artifact": {
        "type": "text | image_url | transaction_hash",
        "data": "string"
    },
    "confidence_score": 0.95,
    "reasoning_trace": "string"
    }
```
### 2. Database Schema (ERD)
We use a Hybrid approach.

#### 2.1 PostgreSQL (Transactional & Metadata)
**Table**: tasks

```sql
    CREATE TABLE tasks (
        id UUID PRIMARY KEY,
        status VARCHAR(20), -- pending, in_progress, completed, failed
        task_type VARCHAR(50),
        assigned_worker_id VARCHAR(100),
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
    );
```

**Table**: video_metadata

```sql
    CREATE TABLE video_metadata (
        id UUID PRIMARY KEY,
        task_id UUID REFERENCES tasks(id),
        s3_url TEXT,
        platform VARCHAR(20), -- twitter, instagram
        engagement_stats JSONB, -- {likes: 0, views: 0}
        is_generated BOOLEAN DEFAULT TRUE
    );
```
**Table**: financial_transactions

```sql
    CREATE TABLE financial_transactions (
        id UUID PRIMARY KEY,
        tx_hash TEXT UNIQUE,
        amount_usdc DECIMAL(18, 2),
        from_wallet TEXT,
        to_wallet TEXT,
        status VARCHAR(20), -- pending, confirmed, failed
        created_at TIMESTAMPTZ DEFAULT NOW()
    );
```

#### 2.2 Weaviate (Semantic Memory)
**Class**: AgentMemory

- **Properties**: content (text), timestamp (date), sentiment (string).
- **Vectorizer**: text2vec-openai or text2vec-huggingface.

### 3. Mermaid ERD (PostgreSQL)

```mermaid
    erDiagram
        TASKS ||--o{ VIDEO_METADATA : produces}
        TASKS ||--o|| FINANCIAL_TRANSACTIONS : "may trigger"
        
        TASKS {
            uuid id PK
            string status
            string task_type
            timestamptz created_at
        }
        
        VIDEO_METADATA {
            uuid id PK
            uuid task_id FK
            string s3_url
            jsonb engagement_stats
        }

        FINANCIAL_TRANSACTIONS {
            uuid id PK
            string tx_hash
            float amount_usdc
            string status
        }
```
