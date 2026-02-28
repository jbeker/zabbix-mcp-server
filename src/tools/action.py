"""Action management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def action_get(actionids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               search: Optional[Dict[str, str]] = None,
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get actions from Zabbix.

    Args:
        actionids: List of action IDs to retrieve
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of actions
    """
    params = build_params(
        required={"output": output},
        optional={"actionids": actionids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("action", "get", params)


@mcp.tool()
def action_create(name: str, eventsource: int,
                  esc_period: str = "1h",
                  operations: Optional[List[Dict[str, Any]]] = None,
                  filter_: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new action in Zabbix.

    Args:
        name: Action name
        eventsource: Event source (0=triggers, 1=discovery, 2=autoregistration, 3=internal, 4=service)
        esc_period: Default escalation period
        operations: List of action operations
        filter_: Action filter conditions
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "eventsource": eventsource, "esc_period": esc_period},
        optional={"operations": operations, "filter": filter_},
        extra_params=extra_params,
    )
    return zabbix_write("action", "create", params)


@mcp.tool()
def action_update(actionid: str, name: Optional[str] = None,
                  status: Optional[int] = None,
                  esc_period: Optional[str] = None,
                  operations: Optional[List[Dict[str, Any]]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an action in Zabbix.

    Args:
        actionid: Action ID to update
        name: New action name
        status: New status (0=enabled, 1=disabled)
        esc_period: New escalation period
        operations: New operations
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"actionid": actionid},
        optional={"name": name, "status": status, "esc_period": esc_period,
                  "operations": operations},
        extra_params=extra_params,
    )
    return zabbix_write("action", "update", params)


@mcp.tool()
def action_delete(actionids: List[str]) -> str:
    """Delete actions from Zabbix.

    Args:
        actionids: List of action IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("action", actionids)
