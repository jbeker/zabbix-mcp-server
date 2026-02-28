"""LLD (Low-Level Discovery) rule management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def discoveryrule_get(itemids: Optional[List[str]] = None,
                      hostids: Optional[List[str]] = None,
                      templateids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      search: Optional[Dict[str, str]] = None,
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get LLD rules from Zabbix with optional filtering.

    Args:
        itemids: List of discovery rule IDs to retrieve
        hostids: List of host IDs to filter by
        templateids: List of template IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of discovery rules
    """
    params = build_params(
        required={"output": output},
        optional={"itemids": itemids, "hostids": hostids, "templateids": templateids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("discoveryrule", "get", params)


@mcp.tool()
def discoveryrule_create(name: str, key_: str, hostid: str, type: int,
                         delay: str = "1h",
                         lifetime: Optional[str] = None,
                         description: Optional[str] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new LLD rule in Zabbix.

    Args:
        name: LLD rule name
        key_: LLD rule key
        hostid: Host ID
        type: Item type (0=Zabbix agent, 2=Zabbix trapper, etc.)
        delay: Update interval
        lifetime: Time period after which items not discovered will be deleted (e.g. "30d")
        description: LLD rule description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "key_": key_, "hostid": hostid,
                  "type": type, "delay": delay},
        optional={"lifetime": lifetime, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("discoveryrule", "create", params)


@mcp.tool()
def discoveryrule_update(itemid: str, name: Optional[str] = None,
                         key_: Optional[str] = None, delay: Optional[str] = None,
                         status: Optional[int] = None,
                         lifetime: Optional[str] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing LLD rule in Zabbix.

    Args:
        itemid: LLD rule ID to update
        name: New LLD rule name
        key_: New LLD rule key
        delay: New update interval
        status: New status (0=enabled, 1=disabled)
        lifetime: New lifetime for discovered entities
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"itemid": itemid},
        optional={"name": name, "key_": key_, "delay": delay,
                  "status": status, "lifetime": lifetime},
        extra_params=extra_params,
    )
    return zabbix_write("discoveryrule", "update", params)


@mcp.tool()
def discoveryrule_delete(itemids: List[str]) -> str:
    """Delete LLD rules from Zabbix.

    Args:
        itemids: List of LLD rule IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("discoveryrule", itemids)
