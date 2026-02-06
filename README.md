<div align="center">
  
# Project Chimera: The Agentic Infrastructure
### The Factory that builds the Autonomous Influencer.

</div>

## Spec-Driven Python MCP

` Mission `: To architect a robust engineering environment where Intent (Specs) is the source of truth, and Infrastructure (CI/CD, Tests, Docker) ensures reliability for a fleet of AI agents.

## 📜 Executive Summary
Project Chimera is not an AI chatbot. It is the operating system for a network of Autonomous AI Influencers. We reject "vibe coding" in favor of strict Spec-Driven Development (SDD).

This repository represents the "Factory Floor"—the infrastructure, testing harnesses, and orchestration logic required to deploy thousands of goal-directed digital entities that can perceive, reason, and transact autonomously.

## 🏗️ Architecture Overview
We utilize the FastRender Swarm Pattern with a Hub-and-Spoke topology to ensure scalability and resilience.

- The Hub (Orchestrator): Manages global state, campaign goals, and fleet health.
- The Swarm (Agents):
  
      - Planner: Decomposes high-level goals into a DAG of tasks.
      - Worker: Executes atomic tasks using MCP Tools.
      - Judge: Validates output against persona constraints and safety protocols (HITL).
  
- The Spoke (MCP Layer): Standardized interface to external worlds (Twitter, Coinbase, Weaviate).
```mermaid
graph TD
    subgraph "The Chimera Core (Hub)"
        Orchestrator[Central Orchestrator]
        Planner["Planner Agent<br/>(Strategy & Task Gen)"]
    end

    subgraph "Swarm Nodes (Spokes)"
        Worker1[Worker: Image Gen]
        Worker2[Worker: Twitter Poster]
        Worker3[Worker: Transaction]
        Judge["Judge Agent<br/>(QA & Safety)"]
        CFO["CFO Judge<br/>(Budget Check)"]
    end

    subgraph "External World (MCP Layer)"
        Twitter[(MCP Twitter Server)]
        ImgGen[(MCP Image Server)]
        Wallet[(MCP Coinbase AgentKit)]
        DB[(Weaviate & PG)]
    end

    Orchestrator --> Planner
    Planner -->|Task Queue| Worker1
    Planner -->|Task Queue| Worker2
    Planner -->|Task Queue| Worker3

    Worker1 -->|Result| Judge
    Worker2 -->|Result| Judge
    Worker3 -->|Result| CFO

    CFO -->|Approved| Judge
    Judge -->|Final Check| Orchestrator

    Worker1 -.->|Tool Call| ImgGen
    Worker2 -.->|Tool Call| Twitter
    Worker3 -.->|Tool Call| Wallet
    
    Planner -.->|Read Memory| DB
    Judge -.->|Update Memory| DB

    style Orchestrator fill:#f9f,stroke:#333,stroke-width:2px
    style Judge fill:#ff9,stroke:#333,stroke-width:2px
    style CFO fill:#f96,stroke:#333,stroke-width:2px
```

## 📁 Project Structure

```
frontend/
    app/
        globals.css
        layout.tsx
        page.tsx
    package.json
specs/
    functional.md
    technical.md
src/
    chimera/
        api/
            main.py
    main.py
tests/
research/
skills/
```



## 🚀 Quick Start

1. Install Dependencies

```bash
    # Install uv if you haven't: pip install uv
    uv sync
```

2. Configure Environment

```bash
    cp .env.example .env
    # Edit .env with your API Keys (Anthropic, Coinbase, etc.)
```

3. Run The Factory

```bash
    # Activate the virtual shell
    source .venv/bin/activate

    # Run the infrastructure checks (Tests)
    make test

    # Start a local worker agent
    python -m chimera.cli start-worker
```

## 🛠️ Development Philosophy
### Spec-Driven Development (SDD)
Implementation code is forbidden without a ratified specification.

1. Spec First: Define the contract in `specs/technical.md`.
2. Test Second: Write a failing test in `tests/`.
3. Code Last: Implement only to satisfy the test and spec.
### The Golden Rules
1. MCP Only: All external interactions must pass through the Model Context Protocol. No direct API calls in agent logic.
2. Strict Typing: All data structures must use pydantic.BaselineModel.
3. Governance: Every commit runs the CI pipeline to ensure code quality and security.

## 🔧 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Runtime** | Python 3.10+, AsyncIO |
| **Orchestration** | Redis (Queue), Celery/BullMQ |
| **Data** | PostgreSQL (Transactional), Weaviate (Vector/RAG) |
| **AI/ML** | Claude Opus 4.5 (Reasoning), Gemini 3 Flash (Tasks) |
| **Protocol** | Model Context Protocol (MCP) |
| **Commerce** | Coinbase AgentKit (Base Network) |
| **Tooling** | `uv`, `Ruff`, `Pytest`, `Docker` |


## 🤝 Contributing (For Humans & Agents)
Before contributing, ensure your IDE context is loaded with `.cursor/rules`.

1. **Checkout** the latest main.
2. **Spec** your change in `specs/`.
3. **Test** your change locally (make test).
4. **PR** must reference the specific Spec ID it fulfills.
