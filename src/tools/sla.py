"""SLA management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def sla_get(slaids: Optional[List[str]] = None,
            serviceids: Optional[List[str]] = None,
            output: Union[str, List[str]] = "extend",
            search: Optional[Dict[str, str]] = None,
            filter: Optional[Dict[str, Any]] = None,
            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get SLAs from Zabbix.

    Args:
        slaids: List of SLA IDs to retrieve
        serviceids: List of service IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of SLAs
    """
    params = build_params(
        required={"output": output},
        optional={"slaids": slaids, "serviceids": serviceids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("sla", "get", params)


@mcp.tool()
def sla_create(name: str, slo: float, period: int,
               timezone: str = "UTC",
               service_tags: Optional[List[Dict[str, str]]] = None,
               description: Optional[str] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new SLA in Zabbix.

    Args:
        name: SLA name
        slo: SLO percentage (e.g. 99.9)
        period: Reporting period (0=daily, 1=weekly, 2=monthly, 3=quarterly, 4=annually)
        timezone: Timezone
        service_tags: Service tags to match
        description: SLA description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "slo": slo, "period": period, "timezone": timezone},
        optional={"service_tags": service_tags, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("sla", "create", params)


@mcp.tool()
def sla_update(slaid: str, name: Optional[str] = None,
               slo: Optional[float] = None,
               period: Optional[int] = None,
               status: Optional[int] = None,
               description: Optional[str] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an SLA in Zabbix.

    Args:
        slaid: SLA ID to update
        name: New name
        slo: New SLO percentage
        period: New reporting period
        status: New status (0=enabled, 1=disabled)
        description: New description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"slaid": slaid},
        optional={"name": name, "slo": slo, "period": period,
                  "status": status, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("sla", "update", params)


@mcp.tool()
def sla_delete(slaids: List[str]) -> str:
    """Delete SLAs from Zabbix.

    Args:
        slaids: List of SLA IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("sla", slaids)


@mcp.tool()
def sla_getsli(slaid: str, serviceids: Optional[List[str]] = None,
               period_from: Optional[int] = None,
               period_to: Optional[int] = None,
               periods: Optional[int] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get SLI (Service Level Indicator) data for an SLA.

    Args:
        slaid: SLA ID
        serviceids: List of service IDs to get SLI for
        period_from: Start of reporting period (Unix timestamp)
        period_to: End of reporting period (Unix timestamp)
        periods: Number of reporting periods to return
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted SLI data
    """
    params = build_params(
        required={"slaid": slaid},
        optional={"serviceids": serviceids, "period_from": period_from,
                  "period_to": period_to, "periods": periods},
        extra_params=extra_params,
    )
    return zabbix_get("sla", "getsli", params)
