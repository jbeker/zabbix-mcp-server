"""Alert tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def alert_get(alertids: Optional[List[str]] = None,
              actionids: Optional[List[str]] = None,
              eventids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              time_from: Optional[int] = None,
              time_till: Optional[int] = None,
              filter: Optional[Dict[str, Any]] = None,
              limit: Optional[int] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get alerts from Zabbix.

    Args:
        alertids: List of alert IDs
        actionids: List of action IDs to filter by
        eventids: List of event IDs to filter by
        output: Output format
        time_from: Start time (Unix timestamp)
        time_till: End time (Unix timestamp)
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"alertids": alertids, "actionids": actionids, "eventids": eventids,
                  "time_from": time_from, "time_till": time_till,
                  "filter": filter, "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("alert", "get", params)
