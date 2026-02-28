"""Item prototype management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def itemprototype_get(itemids: Optional[List[str]] = None,
                      discoveryids: Optional[List[str]] = None,
                      hostids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      search: Optional[Dict[str, str]] = None,
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get item prototypes from Zabbix with optional filtering.

    Args:
        itemids: List of item prototype IDs to retrieve
        discoveryids: List of discovery rule IDs to filter by
        hostids: List of host IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of item prototypes
    """
    params = build_params(
        required={"output": output},
        optional={"itemids": itemids, "discoveryids": discoveryids,
                  "hostids": hostids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("itemprototype", "get", params)


@mcp.tool()
def itemprototype_create(name: str, key_: str, hostid: str, ruleid: str,
                         type: int, value_type: int, delay: str = "1m",
                         units: Optional[str] = None,
                         description: Optional[str] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new item prototype in Zabbix.

    Args:
        name: Item prototype name
        key_: Item prototype key
        hostid: Host ID
        ruleid: LLD rule ID this prototype belongs to
        type: Item type (0=Zabbix agent, 2=Zabbix trapper, etc.)
        value_type: Value type (0=float, 1=character, 3=unsigned int, 4=text)
        delay: Update interval
        units: Value units
        description: Item prototype description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "key_": key_, "hostid": hostid, "ruleid": ruleid,
                  "type": type, "value_type": value_type, "delay": delay},
        optional={"units": units, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("itemprototype", "create", params)


@mcp.tool()
def itemprototype_update(itemid: str, name: Optional[str] = None,
                         key_: Optional[str] = None, delay: Optional[str] = None,
                         status: Optional[int] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing item prototype in Zabbix.

    Args:
        itemid: Item prototype ID to update
        name: New item prototype name
        key_: New item prototype key
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
    return zabbix_write("itemprototype", "update", params)


@mcp.tool()
def itemprototype_delete(itemids: List[str]) -> str:
    """Delete item prototypes from Zabbix.

    Args:
        itemids: List of item prototype IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("itemprototype", itemids)
