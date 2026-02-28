"""User directory management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def userdirectory_get(userdirectoryids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      search: Optional[Dict[str, str]] = None,
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get user directories from Zabbix.

    Args:
        userdirectoryids: List of user directory IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"userdirectoryids": userdirectoryids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("userdirectory", "get", params)


@mcp.tool()
def userdirectory_create(name: str, idp_type: int,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a user directory in Zabbix.

    Args:
        name: User directory name
        idp_type: IdP type (1=LDAP, 2=SAML)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "idp_type": idp_type},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("userdirectory", "create", params)


@mcp.tool()
def userdirectory_update(userdirectoryid: str, name: Optional[str] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a user directory in Zabbix.

    Args:
        userdirectoryid: User directory ID
        name: New name
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"userdirectoryid": userdirectoryid},
        optional={"name": name},
        extra_params=extra_params,
    )
    return zabbix_write("userdirectory", "update", params)


@mcp.tool()
def userdirectory_delete(userdirectoryids: List[str]) -> str:
    """Delete user directories from Zabbix.

    Args:
        userdirectoryids: List of user directory IDs to delete
    """
    return zabbix_delete("userdirectory", userdirectoryids)


@mcp.tool()
def userdirectory_test(userdirectoryid: str,
                       test_username: str, test_password: str,
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Test a user directory configuration.

    Args:
        userdirectoryid: User directory ID to test
        test_username: Username for test authentication
        test_password: Password for test authentication
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"userdirectoryid": userdirectoryid,
                  "test_username": test_username, "test_password": test_password},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("userdirectory", "test", params)
