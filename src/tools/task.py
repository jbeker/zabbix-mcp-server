"""Task management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def task_get(taskids: Optional[List[str]] = None,
             output: Union[str, List[str]] = "extend",
             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get tasks from Zabbix.

    Args:
        taskids: List of task IDs
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"taskids": taskids},
        extra_params=extra_params,
    )
    return zabbix_get("task", "get", params)


@mcp.tool()
def task_create(type: int, request: Dict[str, Any],
                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a task in Zabbix (e.g. check now, diagnostic info).

    Args:
        type: Task type (6=check now, 7=diagnostic info)
        request: Task request object
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"type": type, "request": request},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("task", "create", params)
