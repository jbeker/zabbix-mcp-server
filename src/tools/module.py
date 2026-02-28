"""Module management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def module_get(moduleids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               search: Optional[Dict[str, str]] = None,
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get modules from Zabbix.

    Args:
        moduleids: List of module IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"moduleids": moduleids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("module", "get", params)


@mcp.tool()
def module_create(id: str, relative_path: str,
                  status: int = 1,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a module in Zabbix.

    Args:
        id: Module ID string
        relative_path: Module relative path
        status: Status (0=disabled, 1=enabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"id": id, "relative_path": relative_path, "status": status},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("module", "create", params)


@mcp.tool()
def module_update(moduleid: str, status: Optional[int] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a module in Zabbix.

    Args:
        moduleid: Module ID
        status: New status (0=disabled, 1=enabled)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"moduleid": moduleid},
        optional={"status": status},
        extra_params=extra_params,
    )
    return zabbix_write("module", "update", params)


@mcp.tool()
def module_delete(moduleids: List[str]) -> str:
    """Delete modules from Zabbix.

    Args:
        moduleids: List of module IDs to delete
    """
    return zabbix_delete("module", moduleids)
