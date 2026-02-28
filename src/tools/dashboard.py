"""Dashboard management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def dashboard_get(dashboardids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get dashboards from Zabbix.

    Args:
        dashboardids: List of dashboard IDs to retrieve
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of dashboards
    """
    params = build_params(
        required={"output": output},
        optional={"dashboardids": dashboardids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("dashboard", "get", params)


@mcp.tool()
def dashboard_create(name: str,
                     pages: Optional[List[Dict[str, Any]]] = None,
                     userid: Optional[str] = None,
                     private_: Optional[int] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new dashboard in Zabbix.

    Args:
        name: Dashboard name
        pages: Dashboard pages with widgets
        userid: Owner user ID
        private_: Dashboard sharing (0=public, 1=private)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name},
        optional={"pages": pages, "userid": userid, "private": private_},
        extra_params=extra_params,
    )
    return zabbix_write("dashboard", "create", params)


@mcp.tool()
def dashboard_update(dashboardid: str, name: Optional[str] = None,
                     pages: Optional[List[Dict[str, Any]]] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a dashboard in Zabbix.

    Args:
        dashboardid: Dashboard ID to update
        name: New name
        pages: New pages
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"dashboardid": dashboardid},
        optional={"name": name, "pages": pages},
        extra_params=extra_params,
    )
    return zabbix_write("dashboard", "update", params)


@mcp.tool()
def dashboard_delete(dashboardids: List[str]) -> str:
    """Delete dashboards from Zabbix.

    Args:
        dashboardids: List of dashboard IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("dashboard", dashboardids)
