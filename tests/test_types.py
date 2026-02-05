"""Tests for type definitions."""

from __future__ import annotations

from codex_sdk import (
    ApprovalMode,
    ModelReasoningEffort,
    SandboxMode,
    WebSearchMode,
)


class TestEnums:
    """Tests for enum types."""

    def test_sandbox_mode_values(self) -> None:
        """Test SandboxMode enum values."""
        assert SandboxMode.READ_ONLY == "read-only"
        assert SandboxMode.WORKSPACE_WRITE == "workspace-write"
        assert SandboxMode.DANGER_FULL_ACCESS == "danger-full-access"

    def test_approval_mode_values(self) -> None:
        """Test ApprovalMode enum values."""
        assert ApprovalMode.NEVER == "never"
        assert ApprovalMode.ON_REQUEST == "on-request"
        assert ApprovalMode.ON_FAILURE == "on-failure"
        assert ApprovalMode.UNTRUSTED == "untrusted"

    def test_model_reasoning_effort_values(self) -> None:
        """Test ModelReasoningEffort enum values."""
        assert ModelReasoningEffort.MINIMAL == "minimal"
        assert ModelReasoningEffort.LOW == "low"
        assert ModelReasoningEffort.MEDIUM == "medium"
        assert ModelReasoningEffort.HIGH == "high"
        assert ModelReasoningEffort.XHIGH == "xhigh"

    def test_web_search_mode_values(self) -> None:
        """Test WebSearchMode enum values."""
        assert WebSearchMode.DISABLED == "disabled"
        assert WebSearchMode.CACHED == "cached"
        assert WebSearchMode.LIVE == "live"

    def test_enum_string_conversion(self) -> None:
        """Test that enums can be used as strings."""
        mode = SandboxMode.READ_ONLY
        assert str(mode) == "read-only"
        assert f"Mode: {mode}" == "Mode: read-only"
