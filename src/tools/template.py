"""Template management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def template_get(templateids: Optional[List[str]] = None,
                 groupids: Optional[List[str]] = None,
                 hostids: Optional[List[str]] = None,
                 output: Union[str, List[str]] = "extend",
                 search: Optional[Dict[str, str]] = None,
                 filter: Optional[Dict[str, Any]] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get templates from Zabbix with optional filtering.

    Args:
        templateids: List of template IDs to retrieve
        groupids: List of host group IDs to filter by
        hostids: List of host IDs to filter by
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of templates
    """
    params = build_params(
        required={"output": output},
        optional={"templateids": templateids, "groupids": groupids,
                  "hostids": hostids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("template", "get", params)


@mcp.tool()
def template_create(host: str, groups: List[Dict[str, str]],
                    name: Optional[str] = None, description: Optional[str] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new template in Zabbix.

    Args:
        host: Template technical name
        groups: List of host groups (format: [{"groupid": "1"}])
        name: Template visible name
        description: Template description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"host": host, "groups": groups},
        optional={"name": name, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("template", "create", params)


@mcp.tool()
def template_update(templateid: str, host: Optional[str] = None,
                    name: Optional[str] = None, description: Optional[str] = None,
                    extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing template in Zabbix.

    Args:
        templateid: Template ID to update
        host: New template technical name
        name: New template visible name
        description: New template description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"templateid": templateid},
        optional={"host": host, "name": name, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("template", "update", params)


@mcp.tool()
def template_delete(templateids: List[str]) -> str:
    """Delete templates from Zabbix.

    Args:
        templateids: List of template IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("template", templateids)


@mcp.tool()
def template_massadd(templates: List[Dict[str, str]],
                     groups: Optional[List[Dict[str, str]]] = None,
                     hosts: Optional[List[Dict[str, str]]] = None,
                     macros: Optional[List[Dict[str, str]]] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass add groups, hosts, or macros to templates.

    Args:
        templates: List of templates (format: [{"templateid": "1"}])
        groups: Host groups to add
        hosts: Hosts to link
        macros: Macros to add
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"templates": templates},
        optional={"groups": groups, "hosts": hosts, "macros": macros},
        extra_params=extra_params,
    )
    return zabbix_write("template", "massadd", params)


@mcp.tool()
def template_massremove(templateids: List[str],
                        groupids: Optional[List[str]] = None,
                        hostids: Optional[List[str]] = None,
                        macros: Optional[List[str]] = None,
                        extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass remove groups, hosts, or macros from templates.

    Args:
        templateids: List of template IDs to update
        groupids: Host group IDs to remove
        hostids: Host IDs to unlink
        macros: Macro names to remove
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"templateids": templateids},
        optional={"groupids": groupids, "hostids": hostids, "macros": macros},
        extra_params=extra_params,
    )
    return zabbix_write("template", "massremove", params)


@mcp.tool()
def template_massupdate(templates: List[Dict[str, str]],
                        groups: Optional[List[Dict[str, str]]] = None,
                        hosts: Optional[List[Dict[str, str]]] = None,
                        macros: Optional[List[Dict[str, str]]] = None,
                        extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass update templates — replaces all groups/hosts/macros.

    Args:
        templates: List of templates (format: [{"templateid": "1"}])
        groups: Replace host groups
        hosts: Replace linked hosts
        macros: Replace macros
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"templates": templates},
        optional={"groups": groups, "hosts": hosts, "macros": macros},
        extra_params=extra_params,
    )
    return zabbix_write("template", "massupdate", params)
