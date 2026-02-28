"""Graph management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def graph_get(graphids: Optional[List[str]] = None,
              hostids: Optional[List[str]] = None,
              templateids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              search: Optional[Dict[str, str]] = None,
              filter: Optional[Dict[str, Any]] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get graphs from Zabbix with optional filtering.

    Args:
        graphids: List of graph IDs to retrieve
        hostids: List of host IDs to filter by
        templateids: List of template IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of graphs
    """
    params = build_params(
        required={"output": output},
        optional={"graphids": graphids, "hostids": hostids, "templateids": templateids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("graph", "get", params)


@mcp.tool()
def graph_create(name: str, gitems: List[Dict[str, Any]],
                 width: Optional[int] = None, height: Optional[int] = None,
                 graphtype: Optional[int] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new graph in Zabbix.

    Args:
        name: Graph name
        gitems: List of graph items (format: [{"itemid": "1", "color": "00AA00"}])
        width: Graph width in pixels
        height: Graph height in pixels
        graphtype: Graph type (0=normal, 1=stacked, 2=pie, 3=exploded)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "gitems": gitems},
        optional={"width": width, "height": height, "graphtype": graphtype},
        extra_params=extra_params,
    )
    return zabbix_write("graph", "create", params)


@mcp.tool()
def graph_update(graphid: str, name: Optional[str] = None,
                 gitems: Optional[List[Dict[str, Any]]] = None,
                 width: Optional[int] = None, height: Optional[int] = None,
                 graphtype: Optional[int] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing graph in Zabbix.

    Args:
        graphid: Graph ID to update
        name: New graph name
        gitems: New graph items
        width: New graph width in pixels
        height: New graph height in pixels
        graphtype: New graph type
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"graphid": graphid},
        optional={"name": name, "gitems": gitems, "width": width,
                  "height": height, "graphtype": graphtype},
        extra_params=extra_params,
    )
    return zabbix_write("graph", "update", params)


@mcp.tool()
def graph_delete(graphids: List[str]) -> str:
    """Delete graphs from Zabbix.

    Args:
        graphids: List of graph IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("graph", graphids)
