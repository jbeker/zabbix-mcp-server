"""Proxy group management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def proxygroup_get(proxy_groupids: Optional[List[str]] = None,
                   output: Union[str, List[str]] = "extend",
                   search: Optional[Dict[str, str]] = None,
                   filter: Optional[Dict[str, Any]] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get proxy groups from Zabbix.

    Args:
        proxy_groupids: List of proxy group IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"proxy_groupids": proxy_groupids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("proxygroup", "get", params)


@mcp.tool()
def proxygroup_create(name: str, failover_delay: str = "1m",
                      min_online: str = "1",
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a proxy group in Zabbix.

    Args:
        name: Proxy group name
        failover_delay: Failover delay
        min_online: Minimum number of online proxies
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "failover_delay": failover_delay, "min_online": min_online},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("proxygroup", "create", params)


@mcp.tool()
def proxygroup_update(proxy_groupid: str, name: Optional[str] = None,
                      failover_delay: Optional[str] = None,
                      min_online: Optional[str] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a proxy group in Zabbix.

    Args:
        proxy_groupid: Proxy group ID
        name: New name
        failover_delay: New failover delay
        min_online: New minimum online proxies
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"proxy_groupid": proxy_groupid},
        optional={"name": name, "failover_delay": failover_delay, "min_online": min_online},
        extra_params=extra_params,
    )
    return zabbix_write("proxygroup", "update", params)


@mcp.tool()
def proxygroup_delete(proxy_groupids: List[str]) -> str:
    """Delete proxy groups from Zabbix.

    Args:
        proxy_groupids: List of proxy group IDs to delete
    """
    return zabbix_delete("proxygroup", proxy_groupids)
