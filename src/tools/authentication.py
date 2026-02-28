"""Authentication settings tools for Zabbix MCP Server."""

from typing import Any, Dict, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def authentication_get(output: str = "extend",
                       extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get authentication settings from Zabbix.

    Args:
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("authentication", "get", params)


@mcp.tool()
def authentication_update(authentication_type: Optional[int] = None,
                           extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update authentication settings in Zabbix.

    Args:
        authentication_type: Authentication type (0=internal, 1=LDAP)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={},
        optional={"authentication_type": authentication_type},
        extra_params=extra_params,
    )
    return zabbix_write("authentication", "update", params)
