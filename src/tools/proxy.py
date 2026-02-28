"""Proxy management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def proxy_get(proxyids: Optional[List[str]] = None,
              output: str = "extend",
              search: Optional[Dict[str, str]] = None,
              filter: Optional[Dict[str, Any]] = None,
              limit: Optional[int] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get proxies from Zabbix with optional filtering.

    Args:
        proxyids: List of proxy IDs to retrieve
        output: Output format (extend, shorten, or specific fields)
        search: Search criteria
        filter: Filter criteria
        limit: Maximum number of results
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of proxies
    """
    params = build_params(
        required={"output": output},
        optional={"proxyids": proxyids, "search": search, "filter": filter,
                  "limit": limit},
        extra_params=extra_params,
    )
    return zabbix_get("proxy", "get", params)


@mcp.tool()
def proxy_create(host: str, status: int = 5,
                 description: Optional[str] = None,
                 tls_connect: int = 1,
                 tls_accept: int = 1,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new proxy in Zabbix.

    Args:
        host: Proxy name
        status: Proxy status (5=active proxy, 6=passive proxy)
        description: Proxy description
        tls_connect: TLS connection settings (1=no encryption, 2=PSK, 4=certificate)
        tls_accept: TLS accept settings (1=no encryption, 2=PSK, 4=certificate)
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"host": host, "status": status,
                  "tls_connect": tls_connect, "tls_accept": tls_accept},
        optional={"description": description},
        extra_params=extra_params,
    )
    return zabbix_write("proxy", "create", params)


@mcp.tool()
def proxy_update(proxyid: str, host: Optional[str] = None,
                 status: Optional[int] = None,
                 description: Optional[str] = None,
                 tls_connect: Optional[int] = None,
                 tls_accept: Optional[int] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an existing proxy in Zabbix.

    Args:
        proxyid: Proxy ID to update
        host: New proxy name
        status: New proxy status (5=active proxy, 6=passive proxy)
        description: New proxy description
        tls_connect: New TLS connection settings
        tls_accept: New TLS accept settings
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"proxyid": proxyid},
        optional={"host": host, "status": status, "description": description,
                  "tls_connect": tls_connect, "tls_accept": tls_accept},
        extra_params=extra_params,
    )
    return zabbix_write("proxy", "update", params)


@mcp.tool()
def proxy_delete(proxyids: List[str]) -> str:
    """Delete proxies from Zabbix.

    Args:
        proxyids: List of proxy IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("proxy", proxyids)
