import pytest
from pydantic import ValidationError

# This import will fail initially because the file/class doesn't exist yet.
# This defines the "Empty Slot" the AI must fill.
from chimera.core.models import TrendFetchInput, TrendFetchOutput

def test_trend_input_schema_matches_spec():
    """
    Ensures the input model accepts the exact JSON structure defined in specs/technical.md.
    """
    valid_input = {
        "topic": "tech",
        "max_results": 10,
        "time_range": "24h"
    }
    
    # This should pass once the model is created correctly
    model = TrendFetchInput(**valid_input)
    assert model.topic == "tech"
    assert model.max_results == 10

def test_trend_output_structure():
    """
    Ensures the output model wraps the article list correctly.
    """
    valid_output = {
        "articles": [
            {
                "title": "AI Revolution",
                "url": "http://example.com",
                "relevance_score": 0.9,
                "published_at": "2026-02-04T12:00:00"
            }
        ],
        "total_fetched": 1
    }

    model = TrendFetchOutput(**valid_output)
    assert model.total_fetched == 1
    assert len(model.articles) > 0

def test_trend_input_rejects_invalid_data():
    """
    Strictness Check: The schema should reject bad data types.
    """
    invalid_input = {
        "topic": "tech",
        "max_results": "not_a_number" # Should be int
    }
    
    with pytest.raises(ValidationError):
        TrendFetchInput(**invalid_input)