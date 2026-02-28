"""Service management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def service_get(serviceids: Optional[List[str]] = None,
                output: Union[str, List[str]] = "extend",
                search: Optional[Dict[str, str]] = None,
                filter: Optional[Dict[str, Any]] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get services from Zabbix.

    Args:
        serviceids: List of service IDs to retrieve
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of services
    """
    params = build_params(
        required={"output": output},
        optional={"serviceids": serviceids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("service", "get", params)


@mcp.tool()
def service_create(name: str, algorithm: int,
                   sortorder: int = 0,
                   description: Optional[str] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new service in Zabbix.

    Args:
        name: Service name
        algorithm: Status calculation algorithm (0=set OK, 1=most critical of children, 2=most critical if all children have problems)
        sortorder: Sort order for display
        description: Service description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "algorithm": algorithm, "sortorder": sortorder},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("service", "create", params)


@mcp.tool()
def service_update(serviceid: str, name: Optional[str] = None,
                   algorithm: Optional[int] = None,
                   sortorder: Optional[int] = None,
                   description: Optional[str] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a service in Zabbix.

    Args:
        serviceid: Service ID to update
        name: New name
        algorithm: New algorithm
        sortorder: New sort order
        description: New description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"serviceid": serviceid},
        optional={"name": name, "algorithm": algorithm, "sortorder": sortorder,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("service", "update", params)


@mcp.tool()
def service_delete(serviceids: List[str]) -> str:
    """Delete services from Zabbix.

    Args:
        serviceids: List of service IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("service", serviceids)
