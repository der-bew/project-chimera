
# Skill: Execute Payment

## Description
Initiates a USDC transfer on the Base network using the Coinbase AgentKit MCP server.
**CRITICAL:** This skill MUST be wrapped by the CFO Judge before execution.

## Input Contract (Pydantic Model)
```python
    class PaymentInput(BaseModel):
        to_address: str  # Valid Ethereum/Base address
        amount_usdc: float
        description: str
```

## Output Contract (Pydantic Model)

```python
    class PaymentOutput(BaseModel):
        transaction_hash: str
        status: str  # "pending" or "confirmed"
        from_address: str
```

## MCP Tool Required
`mcp-server-coinbase`: Tool `transfer_erc20`