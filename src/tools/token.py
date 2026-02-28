"""Token management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def token_get(tokenids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              search: Optional[Dict[str, str]] = None,
              filter: Optional[Dict[str, Any]] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get API tokens from Zabbix.

    Args:
        tokenids: List of token IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"tokenids": tokenids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("token", "get", params)


@mcp.tool()
def token_create(name: str, userid: str,
                 expires_at: Optional[int] = None,
                 description: Optional[str] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create an API token in Zabbix.

    Args:
        name: Token name
        userid: User ID the token belongs to
        expires_at: Expiration Unix timestamp (0=never)
        description: Token description
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "userid": userid},
        optional={"expires_at": expires_at, "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("token", "create", params)


@mcp.tool()
def token_update(tokenid: str, name: Optional[str] = None,
                 status: Optional[int] = None,
                 expires_at: Optional[int] = None,
                 description: Optional[str] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an API token in Zabbix.

    Args:
        tokenid: Token ID
        name: New name
        status: New status (0=enabled, 1=disabled)
        expires_at: New expiration timestamp
        description: New description
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"tokenid": tokenid},
        optional={"name": name, "status": status, "expires_at": expires_at,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("token", "update", params)


@mcp.tool()
def token_delete(tokenids: List[str]) -> str:
    """Delete API tokens from Zabbix.

    Args:
        tokenids: List of token IDs to delete
    """
    return zabbix_delete("token", tokenids)


@mcp.tool()
def token_generate(tokenids: List[str],
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Generate (regenerate) auth strings for API tokens.

    Args:
        tokenids: List of token IDs to generate auth strings for
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"tokenids": tokenids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("token", "generate", params)
