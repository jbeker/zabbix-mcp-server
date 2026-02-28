"""Tests for _core module."""

import json
import pytest
from unittest.mock import patch, MagicMock

from src._core import (
    format_response,
    is_read_only,
    validate_read_only,
    get_transport_config,
    mcp,
)


class TestFormatResponse:
    def test_dict(self):
        result = format_response({"key": "value"})
        assert json.loads(result) == {"key": "value"}

    def test_list(self):
        result = format_response([1, 2, 3])
        assert json.loads(result) == [1, 2, 3]

    def test_string(self):
        result = format_response("hello")
        assert json.loads(result) == "hello"

    def test_nested(self):
        data = {"hosts": [{"hostid": "1", "host": "test"}]}
        result = format_response(data)
        assert json.loads(result) == data


class TestIsReadOnly:
    def test_default_is_false_with_env(self, monkeypatch):
        monkeypatch.setenv("READ_ONLY", "false")
        assert is_read_only() is False

    def test_true(self, monkeypatch):
        monkeypatch.setenv("READ_ONLY", "true")
        assert is_read_only() is True

    def test_yes(self, monkeypatch):
        monkeypatch.setenv("READ_ONLY", "yes")
        assert is_read_only() is True

    def test_one(self, monkeypatch):
        monkeypatch.setenv("READ_ONLY", "1")
        assert is_read_only() is True


class TestValidateReadOnly:
    def test_raises_when_read_only(self, read_only_env):
        with pytest.raises(ValueError, match="read-only mode"):
            validate_read_only()

    def test_no_raise_when_writable(self):
        # mock_env sets READ_ONLY=false
        validate_read_only()  # should not raise


class TestGetTransportConfig:
    def test_default_stdio(self):
        config = get_transport_config()
        assert config["transport"] == "stdio"

    def test_invalid_transport(self, monkeypatch):
        monkeypatch.setenv("ZABBIX_MCP_TRANSPORT", "invalid")
        with pytest.raises(ValueError, match="Invalid ZABBIX_MCP_TRANSPORT"):
            get_transport_config()

    def test_http_requires_auth_type(self, monkeypatch):
        monkeypatch.setenv("ZABBIX_MCP_TRANSPORT", "streamable-http")
        monkeypatch.delenv("AUTH_TYPE", raising=False)
        with pytest.raises(ValueError, match="AUTH_TYPE"):
            get_transport_config()

    def test_http_config(self, monkeypatch):
        monkeypatch.setenv("ZABBIX_MCP_TRANSPORT", "streamable-http")
        monkeypatch.setenv("AUTH_TYPE", "no-auth")
        monkeypatch.setenv("ZABBIX_MCP_HOST", "0.0.0.0")
        monkeypatch.setenv("ZABBIX_MCP_PORT", "9090")
        config = get_transport_config()
        assert config["transport"] == "streamable-http"
        assert config["host"] == "0.0.0.0"
        assert config["port"] == 9090


class TestMcpInstance:
    def test_mcp_name(self):
        assert mcp.name == "Zabbix MCP Server"
