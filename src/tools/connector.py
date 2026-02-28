"""Connector management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def connector_get(connectorids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get connectors from Zabbix.

    Args:
        connectorids: List of connector IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"connectorids": connectorids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("connector", "get", params)


@mcp.tool()
def connector_create(name: str, url: str,
                     data_type: int = 0,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a connector in Zabbix.

    Args:
        name: Connector name
        url: Connector URL
        data_type: Data type (0=item values, 1=events)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "url": url, "data_type": data_type},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("connector", "create", params)


@mcp.tool()
def connector_update(connectorid: str, name: Optional[str] = None,
                     url: Optional[str] = None,
                     status: Optional[int] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a connector in Zabbix.

    Args:
        connectorid: Connector ID
        name: New name
        url: New URL
        status: New status (0=disabled, 1=enabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"connectorid": connectorid},
        optional={"name": name, "url": url, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("connector", "update", params)


@mcp.tool()
def connector_delete(connectorids: List[str]) -> str:
    """Delete connectors from Zabbix.

    Args:
        connectorids: List of connector IDs to delete
    """
    return zabbix_delete("connector", connectorids)
