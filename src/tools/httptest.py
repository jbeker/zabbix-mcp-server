"""Web scenario (httptest) management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def httptest_get(httptestids: Optional[List[str]] = None,
                 hostids: Optional[List[str]] = None,
                 output: Union[str, List[str]] = "extend",
                 search: Optional[Dict[str, str]] = None,
                 filter: Optional[Dict[str, Any]] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get web scenarios from Zabbix.

    Args:
        httptestids: List of web scenario IDs
        hostids: List of host IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"httptestids": httptestids, "hostids": hostids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("httptest", "get", params)


@mcp.tool()
def httptest_create(name: str, hostid: str,
                    steps: List[Dict[str, Any]],
                    delay: str = "1m",
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a web scenario in Zabbix.

    Args:
        name: Web scenario name
        hostid: Host ID
        steps: List of scenario steps
        delay: Execution interval
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "hostid": hostid, "steps": steps, "delay": delay},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("httptest", "create", params)


@mcp.tool()
def httptest_update(httptestid: str, name: Optional[str] = None,
                    steps: Optional[List[Dict[str, Any]]] = None,
                    status: Optional[int] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a web scenario in Zabbix.

    Args:
        httptestid: Web scenario ID
        name: New name
        steps: New steps
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"httptestid": httptestid},
        optional={"name": name, "steps": steps, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("httptest", "update", params)


@mcp.tool()
def httptest_delete(httptestids: List[str]) -> str:
    """Delete web scenarios from Zabbix.

    Args:
        httptestids: List of web scenario IDs to delete
    """
    return zabbix_delete("httptest", httptestids)
