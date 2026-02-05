
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
## 2. Negotiation Protocol (Inbox)
Chimera listens on a private queue for contract offers.
Incoming Offer: `{ "campaign_id": "x", "offer_amount": 100, "requirements": [...] }`
Response: Chimera signs the offer hash with its wallet to accept.

## 3. Reputation Protocol (Query)
Before engaging with a new agent, Chimera queries the Reputation Ledger.
Query: `GET /reputation/{agent_address}`
Response: `{ "score": 0.98, "flags": [] }`