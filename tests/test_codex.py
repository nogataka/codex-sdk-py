"""Tests for the Codex class."""

from __future__ import annotations

from codex_sdk import Codex, Thread


class TestCodex:
    """Tests for the Codex class."""

    def test_init_default(self) -> None:
        """Test default initialization."""
        codex = Codex()
        assert codex is not None

    def test_init_with_options(self) -> None:
        """Test initialization with options."""
        codex = Codex({
            "base_url": "https://api.example.com",
            "api_key": "test-key",
        })
        assert codex is not None

    def test_start_thread(self) -> None:
        """Test starting a new thread."""
        codex = Codex()
        thread = codex.start_thread()
        assert isinstance(thread, Thread)
        assert thread.id is None  # ID is set after first turn

    def test_start_thread_with_options(self) -> None:
        """Test starting a thread with options."""
        codex = Codex()
        thread = codex.start_thread({
            "model": "gpt-4",
            "working_directory": "/tmp",
        })
        assert isinstance(thread, Thread)

    def test_resume_thread(self) -> None:
        """Test resuming a thread."""
        codex = Codex()
        thread = codex.resume_thread("test-thread-id")
        assert isinstance(thread, Thread)
        assert thread.id == "test-thread-id"
