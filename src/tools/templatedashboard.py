"""Template dashboard management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def templatedashboard_get(dashboardids: Optional[List[str]] = None,
                          templateids: Optional[List[str]] = None,
                          output: Union[str, List[str]] = "extend",
                          extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get template dashboards from Zabbix.

    Args:
        dashboardids: List of dashboard IDs
        templateids: List of template IDs to filter by
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"dashboardids": dashboardids, "templateids": templateids},
        extra_params=extra_params,
    )
    return zabbix_get("templatedashboard", "get", params)


@mcp.tool()
def templatedashboard_create(name: str, templateid: str,
                             pages: Optional[List[Dict[str, Any]]] = None,
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a template dashboard in Zabbix.

    Args:
        name: Dashboard name
        templateid: Template ID
        pages: Dashboard pages
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "templateid": templateid},
        optional={"pages": pages},
        extra_params=extra_params,
    )
    return zabbix_write("templatedashboard", "create", params)


@mcp.tool()
def templatedashboard_update(dashboardid: str, name: Optional[str] = None,
                             pages: Optional[List[Dict[str, Any]]] = None,
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a template dashboard in Zabbix.

    Args:
        dashboardid: Dashboard ID
        name: New name
        pages: New pages
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"dashboardid": dashboardid},
        optional={"name": name, "pages": pages},
        extra_params=extra_params,
    )
    return zabbix_write("templatedashboard", "update", params)


@mcp.tool()
def templatedashboard_delete(dashboardids: List[str]) -> str:
    """Delete template dashboards from Zabbix.

    Args:
        dashboardids: List of dashboard IDs to delete
    """
    return zabbix_delete("templatedashboard", dashboardids)
