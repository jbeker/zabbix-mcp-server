"""Housekeeping management tools for Zabbix MCP Server."""

from typing import Any, Dict, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def housekeeping_get(output: str = "extend",
                     extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get housekeeping settings from Zabbix.

    Args:
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("housekeeping", "get", params)


@mcp.tool()
def housekeeping_update(extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update housekeeping settings in Zabbix. Pass settings via extra_params.

    Args:
        extra_params: Housekeeping settings to update
    """
    params = build_params(
        required={},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("housekeeping", "update", params)
