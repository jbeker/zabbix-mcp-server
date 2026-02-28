"""Host group management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def hostgroup_get(groupids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get host groups from Zabbix.

    Args:
        groupids: List of group IDs to retrieve
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of host groups
    """
    params = build_params(
        required={"output": output},
        optional={"groupids": groupids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("hostgroup", "get", params)


@mcp.tool()
def hostgroup_create(name: str,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new host group in Zabbix.

    Args:
        name: Host group name
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "create", params)


@mcp.tool()
def hostgroup_update(groupid: str, name: str,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing host group in Zabbix.

    Args:
        groupid: Group ID to update
        name: New group name
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"groupid": groupid, "name": name},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "update", params)


@mcp.tool()
def hostgroup_delete(groupids: List[str]) -> str:
    """Delete host groups from Zabbix.

    Args:
        groupids: List of group IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("hostgroup", groupids)


@mcp.tool()
def hostgroup_massadd(groups: List[Dict[str, str]],
                      hosts: Optional[List[Dict[str, str]]] = None,
                      templates: Optional[List[Dict[str, str]]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass add hosts or templates to host groups.

    Args:
        groups: List of host groups (format: [{"groupid": "1"}])
        hosts: Hosts to add to the groups
        templates: Templates to add to the groups
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groups": groups},
        optional={"hosts": hosts, "templates": templates},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "massadd", params)


@mcp.tool()
def hostgroup_massremove(groupids: List[str],
                         hostids: Optional[List[str]] = None,
                         templateids: Optional[List[str]] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass remove hosts or templates from host groups.

    Args:
        groupids: List of host group IDs to update
        hostids: Host IDs to remove from the groups
        templateids: Template IDs to remove from the groups
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groupids": groupids},
        optional={"hostids": hostids, "templateids": templateids},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "massremove", params)


@mcp.tool()
def hostgroup_massupdate(groups: List[Dict[str, str]],
                         hosts: Optional[List[Dict[str, str]]] = None,
                         templates: Optional[List[Dict[str, str]]] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass update host groups — replaces all hosts/templates in groups.

    Args:
        groups: List of host groups (format: [{"groupid": "1"}])
        hosts: Replace hosts in the groups
        templates: Replace templates in the groups
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groups": groups},
        optional={"hosts": hosts, "templates": templates},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "massupdate", params)


@mcp.tool()
def hostgroup_propagate(groups: List[Dict[str, str]],
                        permissions: bool = False,
                        tag_filters: bool = False,
                        extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Propagate permissions and tag filters to child host groups.

    Args:
        groups: List of host groups (format: [{"groupid": "1"}])
        permissions: Whether to propagate permissions
        tag_filters: Whether to propagate tag filters
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groups": groups},
        optional={"permissions": permissions if permissions else None,
                  "tag_filters": tag_filters if tag_filters else None},
        extra_params=extra_params,
    )
    return zabbix_write("hostgroup", "propagate", params)
