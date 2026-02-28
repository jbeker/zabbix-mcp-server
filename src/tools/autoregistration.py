"""Autoregistration management tools for Zabbix MCP Server."""

from typing import Any, Dict, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def autoregistration_get(output: str = "extend",
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get autoregistration configuration from Zabbix.

    Args:
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("autoregistration", "get", params)


@mcp.tool()
def autoregistration_update(tls_accept: Optional[int] = None,
                            tls_psk_identity: Optional[str] = None,
                            tls_psk: Optional[str] = None,
                            extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update autoregistration configuration in Zabbix.

    Args:
        tls_accept: TLS accept connections (1=unencrypted, 2=PSK)
        tls_psk_identity: PSK identity
        tls_psk: PSK value
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={},
        optional={"tls_accept": tls_accept, "tls_psk_identity": tls_psk_identity,
                  "tls_psk": tls_psk},
        extra_params=extra_params,
    )
    return zabbix_write("autoregistration", "update", params)
