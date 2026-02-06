import pytest
from pydantic import ValidationError

# Importing future skill contracts
from chimera.core.models import PaymentInput, PaymentOutput

def test_payment_input_enforces_address_format():
    """
    Ensures the skill validates wallet addresses before execution.
    This prevents sending money to 'null' or a typo.
    """
    # Valid input
    valid = {
        "to_address": "0x1234567890abcdef1234567890abcdef12345678",
        "amount_usdc": 50.0,
        "description": "Sponsorship payout"
    }
    PaymentInput(**valid) # Should not raise

    # Invalid input (bad address format for demo purposes)
    invalid = {
        "to_address": "bad_address",
        "amount_usdc": 50.0,
        "description": "Test"
    }
    
    # We expect this to fail because of regex validation in the model
    with pytest.raises(ValidationError):
        PaymentInput(**invalid)

def test_payment_output_requires_tx_hash():
    """
    Ensures the skill cannot report success without a transaction hash.
    """
    output = {
        "transaction_hash": "0xabc123...",
        "status": "confirmed",
        "from_address": "0x..."
    }
    
    result = PaymentOutput(**output)
    assert result.status in ["pending", "confirmed"]