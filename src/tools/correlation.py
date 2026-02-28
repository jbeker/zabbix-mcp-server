"""Correlation management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def correlation_get(correlationids: Optional[List[str]] = None,
                    output: Union[str, List[str]] = "extend",
                    search: Optional[Dict[str, str]] = None,
                    filter: Optional[Dict[str, Any]] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get correlations from Zabbix.

    Args:
        correlationids: List of correlation IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"correlationids": correlationids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("correlation", "get", params)


@mcp.tool()
def correlation_create(name: str,
                       filter_: Dict[str, Any],
                       operations: List[Dict[str, Any]],
                       description: Optional[str] = None,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a correlation in Zabbix.

    Args:
        name: Correlation name
        filter_: Correlation filter conditions
        operations: Correlation operations
        description: Description
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "filter": filter_, "operations": operations},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("correlation", "create", params)


@mcp.tool()
def correlation_update(correlationid: str, name: Optional[str] = None,
                       status: Optional[int] = None,
                       description: Optional[str] = None,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a correlation in Zabbix.

    Args:
        correlationid: Correlation ID
        name: New name
        status: New status (0=enabled, 1=disabled)
        description: New description
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"correlationid": correlationid},
        optional={"name": name, "status": status, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("correlation", "update", params)


@mcp.tool()
def correlation_delete(correlationids: List[str]) -> str:
    """Delete correlations from Zabbix.

    Args:
        correlationids: List of correlation IDs to delete
    """
    return zabbix_delete("correlation", correlationids)
