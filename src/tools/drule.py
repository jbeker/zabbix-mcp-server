"""Network discovery rule management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def drule_get(druleids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              search: Optional[Dict[str, str]] = None,
              filter: Optional[Dict[str, Any]] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get network discovery rules from Zabbix.

    Args:
        druleids: List of discovery rule IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"druleids": druleids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("drule", "get", params)


@mcp.tool()
def drule_create(name: str, iprange: str,
                 dchecks: List[Dict[str, Any]],
                 delay: str = "1h",
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a network discovery rule in Zabbix.

    Args:
        name: Discovery rule name
        iprange: IP range to scan (e.g. "192.168.1.1-255")
        dchecks: List of discovery checks
        delay: Check interval
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "iprange": iprange, "dchecks": dchecks, "delay": delay},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("drule", "create", params)


@mcp.tool()
def drule_update(druleid: str, name: Optional[str] = None,
                 iprange: Optional[str] = None,
                 delay: Optional[str] = None,
                 status: Optional[int] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a network discovery rule in Zabbix.

    Args:
        druleid: Discovery rule ID
        name: New name
        iprange: New IP range
        delay: New check interval
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"druleid": druleid},
        optional={"name": name, "iprange": iprange, "delay": delay, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("drule", "update", params)


@mcp.tool()
def drule_delete(druleids: List[str]) -> str:
    """Delete network discovery rules from Zabbix.

    Args:
        druleids: List of discovery rule IDs to delete
    """
    return zabbix_delete("drule", druleids)
