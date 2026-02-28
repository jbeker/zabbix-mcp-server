"""Maintenance management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def maintenance_get(maintenanceids: Optional[List[str]] = None,
                    groupids: Optional[List[str]] = None,
                    hostids: Optional[List[str]] = None,
                    output: Union[str, List[str]] = "extend",
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get maintenance periods from Zabbix.

    Args:
        maintenanceids: List of maintenance IDs to retrieve
        groupids: List of host group IDs to filter by
        hostids: List of host IDs to filter by
        output: Output format (extend or list of specific fields)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of maintenance periods
    """
    params = build_params(
        required={"output": output},
        optional={"maintenanceids": maintenanceids, "groupids": groupids,
                  "hostids": hostids},
        extra_params=extra_params,
    )
    return zabbix_get("maintenance", "get", params)


@mcp.tool()
def maintenance_create(name: str, active_since: int, active_till: int,
                       groupids: Optional[List[str]] = None,
                       hostids: Optional[List[str]] = None,
                       timeperiods: Optional[List[Dict[str, Any]]] = None,
                       description: Optional[str] = None,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new maintenance period in Zabbix.

    Args:
        name: Maintenance name
        active_since: Start time (Unix timestamp)
        active_till: End time (Unix timestamp)
        groupids: List of host group IDs
        hostids: List of host IDs
        timeperiods: List of time periods
        description: Maintenance description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "active_since": active_since, "active_till": active_till},
        optional={"groupids": groupids, "hostids": hostids,
                  "timeperiods": timeperiods, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("maintenance", "create", params)


@mcp.tool()
def maintenance_update(maintenanceid: str, name: Optional[str] = None,
                       active_since: Optional[int] = None, active_till: Optional[int] = None,
                       description: Optional[str] = None,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing maintenance period in Zabbix.

    Args:
        maintenanceid: Maintenance ID to update
        name: New maintenance name
        active_since: New start time (Unix timestamp)
        active_till: New end time (Unix timestamp)
        description: New maintenance description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"maintenanceid": maintenanceid},
        optional={"name": name, "active_since": active_since,
                  "active_till": active_till, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("maintenance", "update", params)


@mcp.tool()
def maintenance_delete(maintenanceids: List[str]) -> str:
    """Delete maintenance periods from Zabbix.

    Args:
        maintenanceids: List of maintenance IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("maintenance", maintenanceids)
