"""Audit log tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def auditlog_get(output: Union[str, List[str]] = "extend",
                 time_from: Optional[int] = None,
                 time_till: Optional[int] = None,
                 userids: Optional[List[str]] = None,
                 filter: Optional[Dict[str, Any]] = None,
                 limit: Optional[int] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get audit log entries from Zabbix.

    Args:
        output: Output format
        time_from: Start time (Unix timestamp)
        time_till: End time (Unix timestamp)
        userids: List of user IDs to filter by
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"time_from": time_from, "time_till": time_till,
                  "userids": userids, "filter": filter, "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("auditlog", "get", params)
