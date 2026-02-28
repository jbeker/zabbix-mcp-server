"""Item management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def item_get(itemids: Optional[List[str]] = None,
             hostids: Optional[List[str]] = None,
             groupids: Optional[List[str]] = None,
             templateids: Optional[List[str]] = None,
             output: Union[str, List[str]] = "extend",
             search: Optional[Dict[str, str]] = None,
             filter: Optional[Dict[str, Any]] = None,
             limit: Optional[int] = None,
             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get items from Zabbix with optional filtering.

    Args:
        itemids: List of item IDs to retrieve
        hostids: List of host IDs to filter by
        groupids: List of host group IDs to filter by
        templateids: List of template IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of items
    """
    params = build_params(
        required={"output": output},
        optional={"itemids": itemids, "hostids": hostids, "groupids": groupids,
                  "templateids": templateids, "search": search, "filter": filter,
                  "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("item", "get", params)


@mcp.tool()
def item_create(name: str, key_: str, hostid: str, type: int,
                value_type: int, delay: str = "1m",
                units: Optional[str] = None,
                description: Optional[str] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new item in Zabbix.

    Args:
        name: Item name
        key_: Item key
        hostid: Host ID
        type: Item type (0=Zabbix agent, 2=Zabbix trapper, etc.)
        value_type: Value type (0=float, 1=character, 3=unsigned int, 4=text)
        delay: Update interval
        units: Value units
        description: Item description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "key_": key_, "hostid": hostid,
                  "type": type, "value_type": value_type, "delay": delay},
        optional={"units": units, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("item", "create", params)


@mcp.tool()
def item_update(itemid: str, name: Optional[str] = None,
                key_: Optional[str] = None, delay: Optional[str] = None,
                status: Optional[int] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing item in Zabbix.

    Args:
        itemid: Item ID to update
        name: New item name
        key_: New item key
        delay: New update interval
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"itemid": itemid},
        optional={"name": name, "key_": key_, "delay": delay, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("item", "update", params)


@mcp.tool()
def item_delete(itemids: List[str]) -> str:
    """Delete items from Zabbix.

    Args:
        itemids: List of item IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("item", itemids)
