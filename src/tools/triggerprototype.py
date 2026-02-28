"""Trigger prototype management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def triggerprototype_get(triggerids: Optional[List[str]] = None,
                         discoveryids: Optional[List[str]] = None,
                         hostids: Optional[List[str]] = None,
                         output: Union[str, List[str]] = "extend",
                         search: Optional[Dict[str, str]] = None,
                         filter: Optional[Dict[str, Any]] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get trigger prototypes from Zabbix.

    Args:
        triggerids: List of trigger prototype IDs to retrieve
        discoveryids: List of LLD rule IDs to filter by
        hostids: List of host IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"triggerids": triggerids, "discoveryids": discoveryids,
                  "hostids": hostids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("triggerprototype", "get", params)


@mcp.tool()
def triggerprototype_create(description: str, expression: str,
                            priority: int = 0, status: int = 0,
                            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a trigger prototype in Zabbix.

    Args:
        description: Trigger prototype description
        expression: Trigger expression
        priority: Severity (0-5)
        status: Status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"description": description, "expression": expression,
                  "priority": priority, "status": status},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("triggerprototype", "create", params)


@mcp.tool()
def triggerprototype_update(triggerid: str, description: Optional[str] = None,
                            expression: Optional[str] = None,
                            priority: Optional[int] = None,
                            status: Optional[int] = None,
                            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a trigger prototype in Zabbix.

    Args:
        triggerid: Trigger prototype ID to update
        description: New description
        expression: New expression
        priority: New priority
        status: New status
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"triggerid": triggerid},
        optional={"description": description, "expression": expression,
                  "priority": priority, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("triggerprototype", "update", params)


@mcp.tool()
def triggerprototype_delete(triggerids: List[str]) -> str:
    """Delete trigger prototypes from Zabbix.

    Args:
        triggerids: List of trigger prototype IDs to delete
    """
    return zabbix_delete("triggerprototype", triggerids)
