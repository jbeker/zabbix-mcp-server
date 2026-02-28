"""Icon map management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def iconmap_get(iconmapids: Optional[List[str]] = None,
                output: Union[str, List[str]] = "extend",
                search: Optional[Dict[str, str]] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get icon maps from Zabbix.

    Args:
        iconmapids: List of icon map IDs
        output: Output format
        search: Search criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"iconmapids": iconmapids, "search": search},
        extra_params=extra_params,
    )
    return zabbix_get("iconmap", "get", params)


@mcp.tool()
def iconmap_create(name: str, default_iconid: str,
                   mappings: List[Dict[str, Any]],
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create an icon map in Zabbix.

    Args:
        name: Icon map name
        default_iconid: Default icon ID
        mappings: Icon mappings
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "default_iconid": default_iconid, "mappings": mappings},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("iconmap", "create", params)


@mcp.tool()
def iconmap_update(iconmapid: str, name: Optional[str] = None,
                   default_iconid: Optional[str] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an icon map in Zabbix.

    Args:
        iconmapid: Icon map ID
        name: New name
        default_iconid: New default icon ID
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"iconmapid": iconmapid},
        optional={"name": name, "default_iconid": default_iconid},
        extra_params=extra_params,
    )
    return zabbix_write("iconmap", "update", params)


@mcp.tool()
def iconmap_delete(iconmapids: List[str]) -> str:
    """Delete icon maps from Zabbix.

    Args:
        iconmapids: List of icon map IDs to delete
    """
    return zabbix_delete("iconmap", iconmapids)
