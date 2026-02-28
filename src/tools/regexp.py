"""Regular expression management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def regexp_get(regexpids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               search: Optional[Dict[str, str]] = None,
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get regular expressions from Zabbix.

    Args:
        regexpids: List of regular expression IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"regexpids": regexpids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("regexp", "get", params)


@mcp.tool()
def regexp_create(name: str, expressions: List[Dict[str, Any]],
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a regular expression in Zabbix.

    Args:
        name: Regular expression name
        expressions: List of expression objects
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "expressions": expressions},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("regexp", "create", params)


@mcp.tool()
def regexp_update(regexpid: str, name: Optional[str] = None,
                  expressions: Optional[List[Dict[str, Any]]] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a regular expression in Zabbix.

    Args:
        regexpid: Regular expression ID
        name: New name
        expressions: New expressions
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"regexpid": regexpid},
        optional={"name": name, "expressions": expressions},
        extra_params=extra_params,
    )
    return zabbix_write("regexp", "update", params)


@mcp.tool()
def regexp_delete(regexpids: List[str]) -> str:
    """Delete regular expressions from Zabbix.

    Args:
        regexpids: List of regular expression IDs to delete
    """
    return zabbix_delete("regexp", regexpids)
