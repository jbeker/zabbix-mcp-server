"""Value map management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def valuemap_get(valuemapids: Optional[List[str]] = None,
                 hostids: Optional[List[str]] = None,
                 output: Union[str, List[str]] = "extend",
                 search: Optional[Dict[str, str]] = None,
                 filter: Optional[Dict[str, Any]] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get value maps from Zabbix.

    Args:
        valuemapids: List of value map IDs
        hostids: List of host IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"valuemapids": valuemapids, "hostids": hostids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("valuemap", "get", params)


@mcp.tool()
def valuemap_create(name: str, hostid: str,
                    mappings: List[Dict[str, str]],
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a value map in Zabbix.

    Args:
        name: Value map name
        hostid: Host or template ID
        mappings: List of value mappings (format: [{"value": "0", "newvalue": "OK"}])
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "hostid": hostid, "mappings": mappings},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("valuemap", "create", params)


@mcp.tool()
def valuemap_update(valuemapid: str, name: Optional[str] = None,
                    mappings: Optional[List[Dict[str, str]]] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a value map in Zabbix.

    Args:
        valuemapid: Value map ID
        name: New name
        mappings: New mappings
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"valuemapid": valuemapid},
        optional={"name": name, "mappings": mappings},
        extra_params=extra_params,
    )
    return zabbix_write("valuemap", "update", params)


@mcp.tool()
def valuemap_delete(valuemapids: List[str]) -> str:
    """Delete value maps from Zabbix.

    Args:
        valuemapids: List of value map IDs to delete
    """
    return zabbix_delete("valuemap", valuemapids)
