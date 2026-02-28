"""Host management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def host_get(hostids: Optional[List[str]] = None,
             groupids: Optional[List[str]] = None,
             templateids: Optional[List[str]] = None,
             output: Union[str, List[str]] = "extend",
             search: Optional[Dict[str, str]] = None,
             filter: Optional[Dict[str, Any]] = None,
             limit: Optional[int] = None,
             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get hosts from Zabbix with optional filtering.

    Args:
        hostids: List of host IDs to retrieve
        groupids: List of host group IDs to filter by
        templateids: List of template IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of hosts
    """
    params = build_params(
        required={"output": output},
        optional={"hostids": hostids, "groupids": groupids, "templateids": templateids,
                  "search": search, "filter": filter, "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("host", "get", params)


@mcp.tool()
def host_create(host: str, groups: List[Dict[str, str]],
                interfaces: List[Dict[str, Any]],
                templates: Optional[List[Dict[str, str]]] = None,
                inventory_mode: int = -1,
                status: int = 0,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new host in Zabbix.

    Args:
        host: Host name
        groups: List of host groups (format: [{"groupid": "1"}])
        interfaces: List of host interfaces
        templates: List of templates to link (format: [{"templateid": "1"}])
        inventory_mode: Inventory mode (-1=disabled, 0=manual, 1=automatic)
        status: Host status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"host": host, "groups": groups, "interfaces": interfaces,
                  "inventory_mode": inventory_mode, "status": status},
        optional={"templates": templates},
        extra_params=extra_params,
    )
    return zabbix_write("host", "create", params)


@mcp.tool()
def host_update(hostid: str, host: Optional[str] = None,
                name: Optional[str] = None, status: Optional[int] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing host in Zabbix.

    Args:
        hostid: Host ID to update
        host: New host name
        name: New visible name
        status: New status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"hostid": hostid},
        optional={"host": host, "name": name, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("host", "update", params)


@mcp.tool()
def host_delete(hostids: List[str]) -> str:
    """Delete hosts from Zabbix.

    Args:
        hostids: List of host IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("host", hostids)


@mcp.tool()
def host_massadd(hosts: List[Dict[str, str]],
                 groups: Optional[List[Dict[str, str]]] = None,
                 interfaces: Optional[List[Dict[str, Any]]] = None,
                 templates: Optional[List[Dict[str, str]]] = None,
                 macros: Optional[List[Dict[str, str]]] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass add host groups, templates, macros, or interfaces to hosts.

    Args:
        hosts: List of hosts to update (format: [{"hostid": "1"}])
        groups: Host groups to add
        interfaces: Host interfaces to add
        templates: Templates to link
        macros: Macros to add
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hosts": hosts},
        optional={"groups": groups, "interfaces": interfaces,
                  "templates": templates, "macros": macros},
        extra_params=extra_params,
    )
    return zabbix_write("host", "massadd", params)


@mcp.tool()
def host_massremove(hostids: List[str],
                    groupids: Optional[List[str]] = None,
                    templateids: Optional[List[str]] = None,
                    templateids_clear: Optional[List[str]] = None,
                    macros: Optional[List[str]] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass remove host groups, templates, or macros from hosts.

    Args:
        hostids: List of host IDs to update
        groupids: Host group IDs to remove
        templateids: Template IDs to unlink
        templateids_clear: Template IDs to unlink and clear
        macros: Macro names to remove
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hostids": hostids},
        optional={"groupids": groupids, "templateids": templateids,
                  "templateids_clear": templateids_clear, "macros": macros},
        extra_params=extra_params,
    )
    return zabbix_write("host", "massremove", params)


@mcp.tool()
def host_massupdate(hosts: List[Dict[str, str]],
                    groups: Optional[List[Dict[str, str]]] = None,
                    templates: Optional[List[Dict[str, str]]] = None,
                    status: Optional[int] = None,
                    inventory_mode: Optional[int] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass update hosts with the same properties.

    Args:
        hosts: List of hosts to update (format: [{"hostid": "1"}])
        groups: Replace host groups
        templates: Replace linked templates
        status: New status (0=enabled, 1=disabled)
        inventory_mode: Inventory mode (-1=disabled, 0=manual, 1=automatic)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hosts": hosts},
        optional={"groups": groups, "templates": templates,
                  "status": status, "inventory_mode": inventory_mode},
        extra_params=extra_params,
    )
    return zabbix_write("host", "massupdate", params)
