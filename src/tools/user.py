"""User management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def user_get(userids: Optional[List[str]] = None,
             output: Union[str, List[str]] = "extend",
             search: Optional[Dict[str, str]] = None,
             filter: Optional[Dict[str, Any]] = None,
             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get users from Zabbix with optional filtering.

    Args:
        userids: List of user IDs to retrieve
        output: Output format (extend or list of specific fields)
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of users
    """
    params = build_params(
        required={"output": output},
        optional={"userids": userids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("user", "get", params)


@mcp.tool()
def user_create(username: str, passwd: str, usrgrps: List[Dict[str, str]],
                name: Optional[str] = None, surname: Optional[str] = None,
                email: Optional[str] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new user in Zabbix.

    Args:
        username: Username
        passwd: Password
        usrgrps: List of user groups (format: [{"usrgrpid": "1"}])
        name: First name
        surname: Last name
        email: Email address
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"username": username, "passwd": passwd, "usrgrps": usrgrps},
        optional={"name": name, "surname": surname, "email": email},
        extra_params=extra_params,
    )
    return zabbix_write("user", "create", params)


@mcp.tool()
def user_update(userid: str, username: Optional[str] = None,
                name: Optional[str] = None, surname: Optional[str] = None,
                email: Optional[str] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing user in Zabbix.

    Args:
        userid: User ID to update
        username: New username
        name: New first name
        surname: New last name
        email: New email address
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"userid": userid},
        optional={"username": username, "name": name, "surname": surname, "email": email},
        extra_params=extra_params,
    )
    return zabbix_write("user", "update", params)


@mcp.tool()
def user_delete(userids: List[str]) -> str:
    """Delete users from Zabbix.

    Args:
        userids: List of user IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("user", userids)


@mcp.tool()
def user_checkauthentication(token: Optional[str] = None,
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Check if the user is authenticated or validate a session.

    Args:
        token: Session token to validate (uses current session if not provided)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted authentication check result
    """
    params = build_params(
        required={},
        optional={"token": token},
        extra_params=extra_params,
    )
    return zabbix_get("user", "checkAuthentication", params)


@mcp.tool()
def user_unblock(userids: List[str],
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Unblock users that have been blocked due to failed login attempts.

    Args:
        userids: List of user IDs to unblock
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"userids": userids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("user", "unblock", params)
