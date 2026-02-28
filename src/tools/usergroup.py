"""User group management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def usergroup_get(usrgrpids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get user groups from Zabbix.

    Args:
        usrgrpids: List of user group IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"usrgrpids": usrgrpids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("usergroup", "get", params)


@mcp.tool()
def usergroup_create(name: str, gui_access: int = 0,
                     users_status: int = 0,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a user group in Zabbix.

    Args:
        name: User group name
        gui_access: Frontend access (0=default, 1=internal, 2=LDAP, 3=disabled)
        users_status: Status (0=enabled, 1=disabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "gui_access": gui_access, "users_status": users_status},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("usergroup", "create", params)


@mcp.tool()
def usergroup_update(usrgrpid: str, name: Optional[str] = None,
                     gui_access: Optional[int] = None,
                     users_status: Optional[int] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a user group in Zabbix.

    Args:
        usrgrpid: User group ID
        name: New name
        gui_access: New frontend access
        users_status: New status
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"usrgrpid": usrgrpid},
        optional={"name": name, "gui_access": gui_access, "users_status": users_status},
        extra_params=extra_params,
    )
    return zabbix_write("usergroup", "update", params)


@mcp.tool()
def usergroup_delete(usrgrpids: List[str]) -> str:
    """Delete user groups from Zabbix.

    Args:
        usrgrpids: List of user group IDs to delete
    """
    return zabbix_delete("usergroup", usrgrpids)
