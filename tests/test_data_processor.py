# tests/test_data_processor.py
# Unit tests for the SecurePipe data processor module

from unittest.mock import patch, MagicMock
import pytest
from src.data_processor import (
    get_database_connection_string,
    run_ping,
    process_data,
)


class TestGetDatabaseConnectionString:
    def test_raises_error_when_password_not_set(self, monkeypatch):
        monkeypatch.delenv("DATABASE_PASSWORD", raising=False)
        with pytest.raises(RuntimeError, match="DATABASE_PASSWORD"):
            get_database_connection_string()

    def test_returns_connection_string_when_password_set(self, monkeypatch):
        monkeypatch.setenv("DATABASE_PASSWORD", "test_password_123")
        monkeypatch.setenv("DATABASE_HOST", "testhost")
        result = get_database_connection_string()
        assert "test_password_123" in result
        assert "testhost" in result


class TestRunPing:
    def test_raises_error_for_disallowed_host(self):
        with pytest.raises(ValueError, match="not in the approved"):
            run_ping("malicious-site.com")

    @patch("src.data_processor.subprocess.run")
    def test_calls_subprocess_with_safe_arguments(self, mock_run):
        mock_run.return_value = MagicMock(stdout="PING google.com")
        result = run_ping("google.com")
        mock_run.assert_called_once_with(
            ["/usr/bin/ping", "-c", "1", "google.com"],
            shell=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert "PING" in result


class TestProcessData:
    def test_processes_valid_data(self):
        assert process_data("  hello world  ") == "HELLO WORLD"

    def test_raises_error_for_empty_string(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            process_data("")

    def test_raises_error_for_none(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            process_data(None)
