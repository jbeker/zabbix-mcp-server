"""Template group management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def templategroup_get(groupids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      search: Optional[Dict[str, str]] = None,
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get template groups from Zabbix.

    Args:
        groupids: List of group IDs to retrieve
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of template groups
    """
    params = build_params(
        required={"output": output},
        optional={"groupids": groupids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("templategroup", "get", params)


@mcp.tool()
def templategroup_create(name: str,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new template group in Zabbix.

    Args:
        name: Template group name
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("templategroup", "create", params)


@mcp.tool()
def templategroup_update(groupid: str, name: str,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a template group in Zabbix.

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
    return zabbix_write("templategroup", "update", params)


@mcp.tool()
def templategroup_delete(groupids: List[str]) -> str:
    """Delete template groups from Zabbix.

    Args:
        groupids: List of group IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("templategroup", groupids)


@mcp.tool()
def templategroup_massadd(groups: List[Dict[str, str]],
                          templates: Optional[List[Dict[str, str]]] = None,
                          extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass add templates to template groups.

    Args:
        groups: List of template groups (format: [{"groupid": "1"}])
        templates: Templates to add
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groups": groups},
        optional={"templates": templates},
        extra_params=extra_params,
    )
    return zabbix_write("templategroup", "massadd", params)


@mcp.tool()
def templategroup_massremove(groupids: List[str],
                             templateids: Optional[List[str]] = None,
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass remove templates from template groups.

    Args:
        groupids: List of template group IDs
        templateids: Template IDs to remove
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groupids": groupids},
        optional={"templateids": templateids},
        extra_params=extra_params,
    )
    return zabbix_write("templategroup", "massremove", params)


@mcp.tool()
def templategroup_massupdate(groups: List[Dict[str, str]],
                             templates: Optional[List[Dict[str, str]]] = None,
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass update template groups — replaces all templates.

    Args:
        groups: List of template groups (format: [{"groupid": "1"}])
        templates: Replace templates in the groups
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"groups": groups},
        optional={"templates": templates},
        extra_params=extra_params,
    )
    return zabbix_write("templategroup", "massupdate", params)


@mcp.tool()
def templategroup_propagate(groups: List[Dict[str, str]],
                            permissions: bool = False,
                            tag_filters: bool = False,
                            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Propagate permissions and tag filters to child template groups.

    Args:
        groups: List of template groups (format: [{"groupid": "1"}])
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
    return zabbix_write("templategroup", "propagate", params)
