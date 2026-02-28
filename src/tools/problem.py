"""Problem management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def problem_get(eventids: Optional[List[str]] = None,
                groupids: Optional[List[str]] = None,
                hostids: Optional[List[str]] = None,
                objectids: Optional[List[str]] = None,
                output: Union[str, List[str]] = "extend",
                time_from: Optional[int] = None,
                time_till: Optional[int] = None,
                recent: bool = False,
                severities: Optional[List[int]] = None,
                limit: Optional[int] = None,
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get problems from Zabbix with optional filtering.

    Args:
        eventids: List of event IDs to retrieve
        groupids: List of host group IDs to filter by
        hostids: List of host IDs to filter by
        objectids: List of object IDs to filter by
        output: Output format (extend or list of specific fields)
        time_from: Start time (Unix timestamp)
        time_till: End time (Unix timestamp)
        recent: Only recent problems
        severities: List of severity levels to filter by
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of problems
    """
    params = build_params(
        required={"output": output},
        optional={"eventids": eventids, "groupids": groupids, "hostids": hostids,
                  "objectids": objectids, "time_from": time_from, "time_till": time_till,
                  "recent": recent if recent else None, "severities": severities,
                  "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("problem", "get", params)
