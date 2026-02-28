"""Tests for _registry module."""

import json
import pytest
from unittest.mock import MagicMock, patch

from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


class TestBuildParams:
    def test_required_only(self):
        result = build_params({"a": 1}, {})
        assert result == {"a": 1}

    def test_optional_none_skipped(self):
        result = build_params({"a": 1}, {"b": None, "c": 2})
        assert result == {"a": 1, "c": 2}

    def test_extra_params_merged(self):
        result = build_params({"a": 1}, {}, {"d": 3})
        assert result == {"a": 1, "d": 3}

    def test_extra_params_overrides(self):
        result = build_params({"a": 1}, {}, {"a": 99})
        assert result == {"a": 99}

    def test_no_extra_params(self):
        result = build_params({"a": 1}, {"b": 2}, None)
        assert result == {"a": 1, "b": 2}


class TestZabbixGet:
    def test_calls_correct_method(self, mock_zabbix_client):
        mock_zabbix_client.host.get.return_value = [{"hostid": "1"}]
        result = zabbix_get("host", "get", {"output": "extend"})
        mock_zabbix_client.host.get.assert_called_once_with(output="extend")
        assert json.loads(result) == [{"hostid": "1"}]


class TestZabbixWrite:
    def test_calls_correct_method(self, mock_zabbix_client):
        mock_zabbix_client.host.create.return_value = {"hostids": ["10"]}
        result = zabbix_write("host", "create", {"host": "test"})
        mock_zabbix_client.host.create.assert_called_once_with(host="test")
        assert json.loads(result) == {"hostids": ["10"]}

    def test_blocked_in_read_only(self, mock_zabbix_client, read_only_env):
        with pytest.raises(ValueError, match="read-only mode"):
            zabbix_write("host", "create", {"host": "test"})


class TestZabbixDelete:
    def test_calls_delete_unpacked(self, mock_zabbix_client):
        mock_zabbix_client.host.delete.return_value = {"hostids": ["1", "2"]}
        result = zabbix_delete("host", ["1", "2"])
        mock_zabbix_client.host.delete.assert_called_once_with("1", "2")
        assert json.loads(result) == {"hostids": ["1", "2"]}

    def test_blocked_in_read_only(self, mock_zabbix_client, read_only_env):
        with pytest.raises(ValueError, match="read-only mode"):
            zabbix_delete("host", ["1"])
