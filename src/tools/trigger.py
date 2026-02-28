"""Trigger management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def trigger_get(triggerids: Optional[List[str]] = None,
                hostids: Optional[List[str]] = None,
                groupids: Optional[List[str]] = None,
                templateids: Optional[List[str]] = None,
                output: Union[str, List[str]] = "extend",
                search: Optional[Dict[str, str]] = None,
                filter: Optional[Dict[str, Any]] = None,
                limit: Optional[int] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get triggers from Zabbix with optional filtering.

    Args:
        triggerids: List of trigger IDs to retrieve
        hostids: List of host IDs to filter by
        groupids: List of host group IDs to filter by
        templateids: List of template IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of triggers
    """
    params = build_params(
        required={"output": output},
        optional={"triggerids": triggerids, "hostids": hostids, "groupids": groupids,
                  "templateids": templateids, "search": search, "filter": filter,
                  "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("trigger", "get", params)


@mcp.tool()
def trigger_create(description: str, expression: str,
                   priority: int = 0, status: int = 0,
                   comments: Optional[str] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new trigger in Zabbix.

    Args:
        description: Trigger description
        expression: Trigger expression
        priority: Severity (0=not classified, 1=info, 2=warning, 3=average, 4=high, 5=disaster)
        status: Status (0=enabled, 1=disabled)
        comments: Additional comments
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"description": description, "expression": expression,
                  "priority": priority, "status": status},
        optional={"comments": comments},
        extra_params=extra_params,
    )
    return zabbix_write("trigger", "create", params)


@mcp.tool()
def trigger_update(triggerid: str, description: Optional[str] = None,
                   expression: Optional[str] = None, priority: Optional[int] = None,
                   status: Optional[int] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing trigger in Zabbix.

    Args:
        triggerid: Trigger ID to update
        description: New trigger description
        expression: New trigger expression
        priority: New severity level
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"triggerid": triggerid},
        optional={"description": description, "expression": expression,
                  "priority": priority, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("trigger", "update", params)


@mcp.tool()
def trigger_delete(triggerids: List[str]) -> str:
    """Delete triggers from Zabbix.

    Args:
        triggerids: List of trigger IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("trigger", triggerids)
