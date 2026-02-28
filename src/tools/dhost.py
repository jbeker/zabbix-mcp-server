"""Discovered host tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def dhost_get(dhostids: Optional[List[str]] = None,
              druleids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get discovered hosts from Zabbix.

    Args:
        dhostids: List of discovered host IDs
        druleids: List of discovery rule IDs to filter by
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"dhostids": dhostids, "druleids": druleids},
        extra_params=extra_params,
    )
    return zabbix_get("dhost", "get", params)
