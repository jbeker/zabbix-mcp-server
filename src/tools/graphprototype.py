"""Graph prototype management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def graphprototype_get(graphids: Optional[List[str]] = None,
                       discoveryids: Optional[List[str]] = None,
                       hostids: Optional[List[str]] = None,
                       output: Union[str, List[str]] = "extend",
                       search: Optional[Dict[str, str]] = None,
                       filter: Optional[Dict[str, Any]] = None,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get graph prototypes from Zabbix.

    Args:
        graphids: List of graph prototype IDs
        discoveryids: List of LLD rule IDs to filter by
        hostids: List of host IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"graphids": graphids, "discoveryids": discoveryids,
                  "hostids": hostids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("graphprototype", "get", params)


@mcp.tool()
def graphprototype_create(name: str, gitems: List[Dict[str, Any]],
                          width: Optional[int] = None, height: Optional[int] = None,
                          graphtype: Optional[int] = None,
                          extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a graph prototype in Zabbix.

    Args:
        name: Graph prototype name
        gitems: Graph items
        width: Width in pixels
        height: Height in pixels
        graphtype: Graph type (0=normal, 1=stacked, 2=pie, 3=exploded)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "gitems": gitems},
        optional={"width": width, "height": height, "graphtype": graphtype},
        extra_params=extra_params,
    )
    return zabbix_write("graphprototype", "create", params)


@mcp.tool()
def graphprototype_update(graphid: str, name: Optional[str] = None,
                          gitems: Optional[List[Dict[str, Any]]] = None,
                          extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a graph prototype in Zabbix.

    Args:
        graphid: Graph prototype ID
        name: New name
        gitems: New graph items
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"graphid": graphid},
        optional={"name": name, "gitems": gitems},
        extra_params=extra_params,
    )
    return zabbix_write("graphprototype", "update", params)


@mcp.tool()
def graphprototype_delete(graphids: List[str]) -> str:
    """Delete graph prototypes from Zabbix.

    Args:
        graphids: List of graph prototype IDs to delete
    """
    return zabbix_delete("graphprototype", graphids)
