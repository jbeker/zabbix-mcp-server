"""User macro management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def usermacro_get(globalmacroids: Optional[List[str]] = None,
                  hostids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get user macros from Zabbix with optional filtering.

    Args:
        globalmacroids: List of global macro IDs to retrieve
        hostids: List of host IDs to filter by (for host macros)
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of user macros
    """
    params = build_params(
        required={"output": output},
        optional={"globalmacroids": globalmacroids, "hostids": hostids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("usermacro", "get", params)


@mcp.tool()
def usermacro_create(hostid: str, macro: str, value: str,
                     type: int = 0,
                     description: Optional[str] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new host macro in Zabbix.

    Args:
        hostid: Host ID the macro belongs to
        macro: Macro name (e.g. {$MACRO_NAME})
        value: Macro value
        type: Macro type (0=text, 1=secret, 2=vault)
        description: Macro description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"hostid": hostid, "macro": macro, "value": value, "type": type},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("usermacro", "create", params)


@mcp.tool()
def usermacro_createglobal(macro: str, value: str,
                           type: int = 0,
                           description: Optional[str] = None,
                           extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new global macro in Zabbix.

    Args:
        macro: Macro name (e.g. {$MACRO_NAME})
        value: Macro value
        type: Macro type (0=text, 1=secret, 2=vault)
        description: Macro description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"macro": macro, "value": value, "type": type},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("usermacro", "createglobal", params)


@mcp.tool()
def usermacro_update(hostmacroid: str, macro: Optional[str] = None,
                     value: Optional[str] = None, type: Optional[int] = None,
                     description: Optional[str] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a host macro in Zabbix.

    Args:
        hostmacroid: Host macro ID to update
        macro: New macro name
        value: New macro value
        type: New macro type (0=text, 1=secret, 2=vault)
        description: New macro description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"hostmacroid": hostmacroid},
        optional={"macro": macro, "value": value, "type": type,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("usermacro", "update", params)


@mcp.tool()
def usermacro_updateglobal(globalmacroid: str, macro: Optional[str] = None,
                           value: Optional[str] = None, type: Optional[int] = None,
                           description: Optional[str] = None,
                           extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a global macro in Zabbix.

    Args:
        globalmacroid: Global macro ID to update
        macro: New macro name
        value: New macro value
        type: New macro type (0=text, 1=secret, 2=vault)
        description: New macro description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"globalmacroid": globalmacroid},
        optional={"macro": macro, "value": value, "type": type,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("usermacro", "updateglobal", params)


@mcp.tool()
def usermacro_delete(hostmacroids: List[str]) -> str:
    """Delete host macros from Zabbix.

    Args:
        hostmacroids: List of host macro IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("usermacro", hostmacroids)


@mcp.tool()
def usermacro_deleteglobal(globalmacroids: List[str]) -> str:
    """Delete global macros from Zabbix.

    Args:
        globalmacroids: List of global macro IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    from src._core import validate_read_only, get_zabbix_client, format_response
    validate_read_only()
    client = get_zabbix_client()
    result = client.usermacro.deleteglobal(*globalmacroids)
    return format_response(result)
