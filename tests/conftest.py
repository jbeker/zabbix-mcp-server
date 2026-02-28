"""Shared pytest fixtures for Zabbix MCP Server tests."""

import os
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    """Set default environment variables for all tests."""
    monkeypatch.setenv("ZABBIX_URL", "http://zabbix.test/api_jsonrpc.php")
    monkeypatch.setenv("ZABBIX_TOKEN", "test-token-123")
    monkeypatch.setenv("READ_ONLY", "false")
    monkeypatch.setenv("VERIFY_SSL", "true")


@pytest.fixture
def read_only_env(monkeypatch):
    """Switch to read-only mode."""
    monkeypatch.setenv("READ_ONLY", "true")


@pytest.fixture
def mock_zabbix_client():
    """Provide a mocked ZabbixAPI client.

    Patches get_zabbix_client to return a MagicMock, then yields
    the mock so tests can inspect calls.
    """
    mock_client = MagicMock()
    with patch("src._core.get_zabbix_client", return_value=mock_client) as _:
        # Also patch in the registry since it imports from _core
        with patch("src.tools._registry.get_zabbix_client", return_value=mock_client):
            yield mock_client


@pytest.fixture
def reset_zabbix_api():
    """Reset the global zabbix_api to None after test."""
    import src._core
    original = src._core.zabbix_api
    yield
    src._core.zabbix_api = original
