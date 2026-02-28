"""History management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def history_get(itemids: List[str], history: int = 0,
                time_from: Optional[int] = None,
                time_till: Optional[int] = None,
                limit: Optional[int] = None,
                sortfield: str = "clock",
                sortorder: str = "DESC",
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get history data from Zabbix.

    Args:
        itemids: List of item IDs to get history for
        history: History type (0=float, 1=character, 2=log, 3=unsigned, 4=text)
        time_from: Start time (Unix timestamp)
        time_till: End time (Unix timestamp)
        limit: Maximum number of results
        sortfield: Field to sort by
        sortorder: Sort order (ASC or DESC)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted history data
    """
    params = build_params(
        required={"itemids": itemids, "history": history,
                  "sortfield": sortfield, "sortorder": sortorder},
        optional={"time_from": time_from, "time_till": time_till, "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("history", "get", params)


@mcp.tool()
def history_clear(itemids: List[str],
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Clear history data for items.

    Args:
        itemids: List of item IDs to clear history for
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"itemids": itemids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("history", "clear", params)


@mcp.tool()
def history_push(data: List[Dict[str, Any]],
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Push history data to Zabbix.

    Args:
        data: List of history entries, each with host, key, value, and optionally clock
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"data": data},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("history", "push", params)
