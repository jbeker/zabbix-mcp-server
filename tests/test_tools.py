"""Meta-tests and tool-specific tests for all registered tools."""

import json
import pytest
from unittest.mock import MagicMock, patch

from src._core import mcp


def call_tool(tool_func, **kwargs):
    """Call a tool function, handling FastMCP's FunctionTool wrapper."""
    if hasattr(tool_func, "fn"):
        return tool_func.fn(**kwargs)
    return tool_func(**kwargs)


class TestToolRegistration:
    """Verify properties across all registered tools."""

    def _get_all_tools(self):
        return mcp._tool_manager._tools

    def test_tool_count_above_200(self):
        tools = self._get_all_tools()
        assert len(tools) >= 200, f"Expected 200+ tools, got {len(tools)}"

    def test_all_tool_names_use_underscore_convention(self):
        for name in self._get_all_tools():
            assert "_" in name, f"Tool {name} does not follow object_method naming"


class TestHostTools:
    def test_host_get(self, mock_zabbix_client):
        mock_zabbix_client.host.get.return_value = [{"hostid": "1", "host": "test"}]
        from src.tools.host import host_get
        result = call_tool(host_get, hostids=["1"])
        mock_zabbix_client.host.get.assert_called_once()
        data = json.loads(result)
        assert data[0]["hostid"] == "1"

    def test_host_get_with_extra_params(self, mock_zabbix_client):
        mock_zabbix_client.host.get.return_value = []
        from src.tools.host import host_get
        call_tool(host_get, extra_params={"selectInterfaces": "extend"})
        call_kwargs = mock_zabbix_client.host.get.call_args[1]
        assert call_kwargs["selectInterfaces"] == "extend"

    def test_host_create(self, mock_zabbix_client):
        mock_zabbix_client.host.create.return_value = {"hostids": ["10"]}
        from src.tools.host import host_create
        result = call_tool(host_create,
            host="newhost",
            groups=[{"groupid": "1"}],
            interfaces=[{"type": 1, "main": 1, "useip": 1, "ip": "127.0.0.1",
                         "dns": "", "port": "10050"}],
        )
        assert "10" in json.loads(result)["hostids"]

    def test_host_create_blocked_read_only(self, mock_zabbix_client, read_only_env):
        from src.tools.host import host_create
        with pytest.raises(ValueError, match="read-only"):
            call_tool(host_create,
                host="test",
                groups=[{"groupid": "1"}],
                interfaces=[],
            )

    def test_host_delete(self, mock_zabbix_client):
        mock_zabbix_client.host.delete.return_value = {"hostids": ["1"]}
        from src.tools.host import host_delete
        result = call_tool(host_delete, hostids=["1"])
        mock_zabbix_client.host.delete.assert_called_once_with("1")

    def test_host_massadd(self, mock_zabbix_client):
        mock_zabbix_client.host.massadd.return_value = {"hostids": ["1"]}
        from src.tools.host import host_massadd
        result = call_tool(host_massadd,
            hosts=[{"hostid": "1"}],
            groups=[{"groupid": "2"}],
        )
        mock_zabbix_client.host.massadd.assert_called_once()


class TestItemTools:
    def test_item_get(self, mock_zabbix_client):
        mock_zabbix_client.item.get.return_value = [{"itemid": "100"}]
        from src.tools.item import item_get
        result = call_tool(item_get, hostids=["1"])
        assert json.loads(result)[0]["itemid"] == "100"

    def test_item_create(self, mock_zabbix_client):
        mock_zabbix_client.item.create.return_value = {"itemids": ["200"]}
        from src.tools.item import item_create
        result = call_tool(item_create,
            name="CPU load", key_="system.cpu.load",
            hostid="1", type=0, value_type=0,
        )
        assert "200" in json.loads(result)["itemids"]


class TestTriggerTools:
    def test_trigger_get(self, mock_zabbix_client):
        mock_zabbix_client.trigger.get.return_value = [{"triggerid": "50"}]
        from src.tools.trigger import trigger_get
        result = call_tool(trigger_get, hostids=["1"])
        assert json.loads(result)[0]["triggerid"] == "50"


class TestTemplateTools:
    def test_template_massadd(self, mock_zabbix_client):
        mock_zabbix_client.template.massadd.return_value = {"templateids": ["1"]}
        from src.tools.template import template_massadd
        result = call_tool(template_massadd,
            templates=[{"templateid": "1"}],
            groups=[{"groupid": "2"}],
        )
        mock_zabbix_client.template.massadd.assert_called_once()


class TestUserMacroTools:
    def test_usermacro_create(self, mock_zabbix_client):
        mock_zabbix_client.usermacro.create.return_value = {"hostmacroids": ["5"]}
        from src.tools.usermacro import usermacro_create
        result = call_tool(usermacro_create, hostid="1", macro="{$TEST}", value="123")
        mock_zabbix_client.usermacro.create.assert_called_once()

    def test_usermacro_createglobal(self, mock_zabbix_client):
        mock_zabbix_client.usermacro.createglobal.return_value = {"globalmacroids": ["1"]}
        from src.tools.usermacro import usermacro_createglobal
        result = call_tool(usermacro_createglobal, macro="{$GLOBAL}", value="val")
        mock_zabbix_client.usermacro.createglobal.assert_called_once()


class TestNewPhase2Tools:
    def test_hostinterface_get(self, mock_zabbix_client):
        mock_zabbix_client.hostinterface.get.return_value = [{"interfaceid": "1"}]
        from src.tools.hostinterface import hostinterface_get
        result = call_tool(hostinterface_get, hostids=["1"])
        assert json.loads(result)[0]["interfaceid"] == "1"

    def test_sla_getsli(self, mock_zabbix_client):
        mock_zabbix_client.sla.getsli.return_value = {"sli": []}
        from src.tools.sla import sla_getsli
        result = call_tool(sla_getsli, slaid="1")
        mock_zabbix_client.sla.getsli.assert_called_once()

    def test_script_execute(self, mock_zabbix_client):
        mock_zabbix_client.script.execute.return_value = {"response": "success"}
        from src.tools.script import script_execute
        result = call_tool(script_execute, scriptid="1", hostid="2")
        mock_zabbix_client.script.execute.assert_called_once()


class TestNewPhase3Tools:
    def test_drule_get(self, mock_zabbix_client):
        mock_zabbix_client.drule.get.return_value = [{"druleid": "1"}]
        from src.tools.drule import drule_get
        result = call_tool(drule_get)
        assert json.loads(result)[0]["druleid"] == "1"

    def test_httptest_create(self, mock_zabbix_client):
        mock_zabbix_client.httptest.create.return_value = {"httptestids": ["1"]}
        from src.tools.httptest import httptest_create
        result = call_tool(httptest_create,
            name="Test scenario", hostid="1",
            steps=[{"name": "Step 1", "url": "http://example.com", "no": 1}],
        )
        mock_zabbix_client.httptest.create.assert_called_once()


class TestNewPhase4Tools:
    def test_role_get(self, mock_zabbix_client):
        mock_zabbix_client.role.get.return_value = [{"roleid": "1"}]
        from src.tools.role import role_get
        result = call_tool(role_get)
        assert json.loads(result)[0]["roleid"] == "1"

    def test_token_generate(self, mock_zabbix_client):
        mock_zabbix_client.token.generate.return_value = [{"tokenid": "1", "token": "abc"}]
        from src.tools.token import token_generate
        result = call_tool(token_generate, tokenids=["1"])
        mock_zabbix_client.token.generate.assert_called_once()


class TestNewPhase5Tools:
    def test_alert_get(self, mock_zabbix_client):
        mock_zabbix_client.alert.get.return_value = [{"alertid": "1"}]
        from src.tools.alert import alert_get
        result = call_tool(alert_get)
        assert json.loads(result)[0]["alertid"] == "1"

    def test_hanode_get(self, mock_zabbix_client):
        mock_zabbix_client.hanode.get.return_value = [{"ha_nodeid": "1"}]
        from src.tools.hanode import hanode_get
        result = call_tool(hanode_get)
        assert json.loads(result)[0]["ha_nodeid"] == "1"

    def test_proxygroup_create(self, mock_zabbix_client):
        mock_zabbix_client.proxygroup.create.return_value = {"proxy_groupids": ["1"]}
        from src.tools.proxygroup import proxygroup_create
        result = call_tool(proxygroup_create, name="Test Group")
        mock_zabbix_client.proxygroup.create.assert_called_once()
