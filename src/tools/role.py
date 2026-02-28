"""Role management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def role_get(roleids: Optional[List[str]] = None,
             output: Union[str, List[str]] = "extend",
             search: Optional[Dict[str, str]] = None,
             filter: Optional[Dict[str, Any]] = None,
             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get roles from Zabbix.

    Args:
        roleids: List of role IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"roleids": roleids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("role", "get", params)


@mcp.tool()
def role_create(name: str, type: int,
                rules: Optional[Dict[str, Any]] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a role in Zabbix.

    Args:
        name: Role name
        type: User type (1=user, 2=admin, 3=super admin)
        rules: Role rules
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "type": type},
        optional={"rules": rules},
        extra_params=extra_params,
    )
    return zabbix_write("role", "create", params)


@mcp.tool()
def role_update(roleid: str, name: Optional[str] = None,
                type: Optional[int] = None,
                rules: Optional[Dict[str, Any]] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a role in Zabbix.

    Args:
        roleid: Role ID
        name: New name
        type: New user type
        rules: New rules
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"roleid": roleid},
        optional={"name": name, "type": type, "rules": rules},
        extra_params=extra_params,
    )
    return zabbix_write("role", "update", params)


@mcp.tool()
def role_delete(roleids: List[str]) -> str:
    """Delete roles from Zabbix.

    Args:
        roleids: List of role IDs to delete
    """
    return zabbix_delete("role", roleids)
