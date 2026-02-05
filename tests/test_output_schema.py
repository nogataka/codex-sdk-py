"""Tests for output schema file utilities."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from codex_sdk.output_schema_file import create_output_schema_file


class TestOutputSchemaFile:
    """Tests for output schema file creation."""

    @pytest.mark.asyncio
    async def test_create_with_none(self) -> None:
        """Test creating with no schema."""
        result = await create_output_schema_file(None)
        assert result.schema_path is None
        await result.cleanup()  # Should not raise

    @pytest.mark.asyncio
    async def test_create_with_schema(self) -> None:
        """Test creating with a valid schema."""
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
            },
        }
        result = await create_output_schema_file(schema)

        assert result.schema_path is not None
        assert Path(result.schema_path).exists()

        # Verify content
        with open(result.schema_path) as f:
            saved_schema = json.load(f)
        assert saved_schema == schema

        # Cleanup
        await result.cleanup()
        assert not Path(result.schema_path).exists()

    @pytest.mark.asyncio
    async def test_create_with_invalid_schema(self) -> None:
        """Test creating with an invalid schema type."""
        with pytest.raises(ValueError, match="must be a plain JSON object"):
            await create_output_schema_file("not a dict")

        with pytest.raises(ValueError, match="must be a plain JSON object"):
            await create_output_schema_file([1, 2, 3])
