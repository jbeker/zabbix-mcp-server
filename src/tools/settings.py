"""Settings management tools for Zabbix MCP Server."""

from typing import Any, Dict, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def settings_get(output: str = "extend",
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get global settings from Zabbix.

    Args:
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("settings", "get", params)


@mcp.tool()
def settings_update(extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update global settings in Zabbix. Pass settings via extra_params.

    Args:
        extra_params: Settings to update (e.g. {"default_theme": "dark-theme"})
    """
    params = build_params(
        required={},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("settings", "update", params)
