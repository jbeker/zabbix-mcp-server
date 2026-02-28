"""Map management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def map_get(sysmapids: Optional[List[str]] = None,
            output: Union[str, List[str]] = "extend",
            search: Optional[Dict[str, str]] = None,
            filter: Optional[Dict[str, Any]] = None,
            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get maps from Zabbix.

    Args:
        sysmapids: List of map IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"sysmapids": sysmapids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("map", "get", params)


@mcp.tool()
def map_create(name: str, width: int = 800, height: int = 600,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a map in Zabbix.

    Args:
        name: Map name
        width: Map width in pixels
        height: Map height in pixels
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "width": width, "height": height},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("map", "create", params)


@mcp.tool()
def map_update(sysmapid: str, name: Optional[str] = None,
               width: Optional[int] = None, height: Optional[int] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a map in Zabbix.

    Args:
        sysmapid: Map ID
        name: New name
        width: New width
        height: New height
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"sysmapid": sysmapid},
        optional={"name": name, "width": width, "height": height},
        extra_params=extra_params,
    )
    return zabbix_write("map", "update", params)


@mcp.tool()
def map_delete(sysmapids: List[str]) -> str:
    """Delete maps from Zabbix.

    Args:
        sysmapids: List of map IDs to delete
    """
    return zabbix_delete("map", sysmapids)
