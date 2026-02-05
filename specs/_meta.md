# Project Chimera: Meta Specification
## Vision
Project Chimera is the "Factory" that builds Autonomous AI Influencers. It is a spec-driven, MCP-native architecture designed to orchestrate swarms of goal-directed AI agents capable of research, content creation, and agentic commerce.

## Prime Directive
**Ambiguity is the enemy of AI**. All implementation MUST strictly adhere to the definitions in specs/functional.md and specs/technical.md. If a behavior is not defined here, it does not exist.

## Constraints
1. **MCP Only**: All external interactions (Twitter, Wallet, News) must use the Model Context Protocol. No direct API calls in agent logic.
2. **Stateless Workers**: Workers must be ephemeral. State is managed by Redis and the Database.
3. **Governance**: All financial actions require a "CFO Judge" check. All content below 0.7 confidence requires Human HITL.
## Stack
- Python 3.10+
- AsyncIO (no blocking threads)
- Pydantic (Strict types)
- Redis (Queues)
- PostgreSQL + Weaviate (Storage)