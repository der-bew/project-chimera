
# OpenClaw Integration Protocol

## Objective
Define how Chimera interacts with the external Agent Social Network.

## 1. Discovery Protocol (Broadcast)
Chimera will advertise its availability via a standardized "Heartbeat" packet sent to a shared discovery topic (e.g., `agent/availability`).
**Payload:**
```json
    {
    "agent_id": "chimera_01",
    "capabilities": ["text_gen", "image_gen", "base_tx"],
    "wallet_address": "0x123...",
    "status": "online"
    }
```