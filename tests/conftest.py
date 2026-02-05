"""Pytest configuration and fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_schema() -> dict:
    """Sample JSON schema for testing."""
    return {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "status": {"type": "string", "enum": ["ok", "error"]},
        },
        "required": ["summary", "status"],
        "additionalProperties": False,
    }
