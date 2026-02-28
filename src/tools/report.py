"""Report management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def report_get(reportids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get scheduled reports from Zabbix.

    Args:
        reportids: List of report IDs
        output: Output format
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"reportids": reportids, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("report", "get", params)


@mcp.tool()
def report_create(name: str, dashboardid: str,
                  period: int = 0,
                  users: Optional[List[Dict[str, Any]]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a scheduled report in Zabbix.

    Args:
        name: Report name
        dashboardid: Dashboard ID for the report
        period: Reporting period (0=previous day, 1=previous week, 2=previous month, 3=previous year)
        users: Recipients
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "dashboardid": dashboardid, "period": period},
        optional={"users": users},
        extra_params=extra_params,
    )
    return zabbix_write("report", "create", params)


@mcp.tool()
def report_update(reportid: str, name: Optional[str] = None,
                  status: Optional[int] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a scheduled report in Zabbix.

    Args:
        reportid: Report ID
        name: New name
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"reportid": reportid},
        optional={"name": name, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("report", "update", params)


@mcp.tool()
def report_delete(reportids: List[str]) -> str:
    """Delete scheduled reports from Zabbix.

    Args:
        reportids: List of report IDs to delete
    """
    return zabbix_delete("report", reportids)
