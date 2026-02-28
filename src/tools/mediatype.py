"""Media type management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def mediatype_get(mediatypeids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  search: Optional[Dict[str, str]] = None,
                  filter: Optional[Dict[str, Any]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get media types from Zabbix.

    Args:
        mediatypeids: List of media type IDs to retrieve
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of media types
    """
    params = build_params(
        required={"output": output},
        optional={"mediatypeids": mediatypeids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("mediatype", "get", params)


@mcp.tool()
def mediatype_create(name: str, type: int,
                     description: Optional[str] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new media type in Zabbix.

    Args:
        name: Media type name
        type: Transport type (0=email, 1=script, 2=SMS, 4=webhook)
        description: Description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "type": type},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("mediatype", "create", params)


@mcp.tool()
def mediatype_update(mediatypeid: str, name: Optional[str] = None,
                     type: Optional[int] = None,
                     status: Optional[int] = None,
                     description: Optional[str] = None,
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a media type in Zabbix.

    Args:
        mediatypeid: Media type ID to update
        name: New name
        type: New transport type
        status: New status (0=enabled, 1=disabled)
        description: New description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"mediatypeid": mediatypeid},
        optional={"name": name, "type": type, "status": status,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("mediatype", "update", params)


@mcp.tool()
def mediatype_delete(mediatypeids: List[str]) -> str:
    """Delete media types from Zabbix.

    Args:
        mediatypeids: List of media type IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("mediatype", mediatypeids)
