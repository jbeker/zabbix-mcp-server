"""Trend management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def trend_get(itemids: List[str], time_from: Optional[int] = None,
              time_till: Optional[int] = None,
              limit: Optional[int] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get trend data from Zabbix.

    Args:
        itemids: List of item IDs to get trends for
        time_from: Start time (Unix timestamp)
        time_till: End time (Unix timestamp)
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted trend data
    """
    params = build_params(
        required={"itemids": itemids},
        optional={"time_from": time_from, "time_till": time_till, "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("trend", "get", params)
