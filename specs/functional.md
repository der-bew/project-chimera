# Functional Requirements
### 1. Perception System (FR 2.0)
**As a Planner Agent**, I need to continuously poll mcp://news/latest so that I can detect emerging trends relevant to the agent's persona.**Acceptance Criteria**: Planner must poll every 5 minutes.

**As a Planner Agent**, I need to filter incoming news through a Semantic Filter so that I only create tasks for high-relevance content (Relevance > 0.75).

### 2. Creative Engine (FR 3.0)
**As a Worker Agent**, I need to generate images using mcp://image_gen/create so that I can produce visual assets.Constraint: All image requests MUST include a character_reference_id to ensure face consistency (FR 3.1).

### 3. Action System (FR 4.0)
**As a Worker Agent**, I need to publish content to Twitter using mcp://twitter/post so that I can engage the audience.**Constraint**: The post payload MUST include the is_generated flag for transparency.

### 4. Agentic Commerce (FR 5.0)
**As a Chimera Agent**, I need a non-custodial wallet so that I can receive payments.**As a CFO Judge**, I need to intercept any send_payment action so that I can enforce daily budget limits (MAX_DAILY_LIMIT = 50 USDC).

### 5. Orchestration (FR 6.0)
**As a Planner**, I need to decompose a Goal (e.g., "Hype sneakers") into a DAG of Tasks (Research -> Script -> Image -> Post).**As a Judge**, I need to implement Optimistic Concurrency Control (OCC) to prevent state collisions.