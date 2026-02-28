"""Host interface management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def hostinterface_get(interfaceids: Optional[List[str]] = None,
                      hostids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get host interfaces from Zabbix.

    Args:
        interfaceids: List of interface IDs to retrieve
        hostids: List of host IDs to filter by
        output: Output format
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of host interfaces
    """
    params = build_params(
        required={"output": output},
        optional={"interfaceids": interfaceids, "hostids": hostids, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("hostinterface", "get", params)


@mcp.tool()
def hostinterface_create(hostid: str, type: int, main: int, useip: int,
                         ip: str = "", dns: str = "", port: str = "",
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new host interface in Zabbix.

    Args:
        hostid: Host ID
        type: Interface type (1=agent, 2=SNMP, 3=IPMI, 4=JMX)
        main: Whether this is the default interface (0=no, 1=yes)
        useip: Whether to connect using IP (0=DNS, 1=IP)
        ip: IP address
        dns: DNS name
        port: Port number
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"hostid": hostid, "type": type, "main": main, "useip": useip,
                  "ip": ip, "dns": dns, "port": port},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostinterface", "create", params)


@mcp.tool()
def hostinterface_update(interfaceid: str, type: Optional[int] = None,
                         main: Optional[int] = None, useip: Optional[int] = None,
                         ip: Optional[str] = None, dns: Optional[str] = None,
                         port: Optional[str] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a host interface in Zabbix.

    Args:
        interfaceid: Interface ID to update
        type: Interface type
        main: Default interface flag
        useip: Connection method
        ip: IP address
        dns: DNS name
        port: Port number
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"interfaceid": interfaceid},
        optional={"type": type, "main": main, "useip": useip,
                  "ip": ip, "dns": dns, "port": port},
        extra_params=extra_params,
    )
    return zabbix_write("hostinterface", "update", params)


@mcp.tool()
def hostinterface_delete(interfaceids: List[str]) -> str:
    """Delete host interfaces from Zabbix.

    Args:
        interfaceids: List of interface IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("hostinterface", interfaceids)


@mcp.tool()
def hostinterface_massadd(hosts: List[Dict[str, str]],
                          interfaces: List[Dict[str, Any]],
                          extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass add interfaces to hosts.

    Args:
        hosts: List of hosts (format: [{"hostid": "1"}])
        interfaces: Interfaces to add
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hosts": hosts, "interfaces": interfaces},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostinterface", "massadd", params)


@mcp.tool()
def hostinterface_massremove(hostids: List[str],
                             interfaceids: List[str],
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Mass remove interfaces from hosts.

    Args:
        hostids: List of host IDs
        interfaceids: Interface IDs to remove
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hostids": hostids, "interfaceids": interfaceids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostinterface", "massremove", params)


@mcp.tool()
def hostinterface_replacehostinterfaces(hostid: str,
                                        interfaces: List[Dict[str, Any]],
                                        extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Replace all interfaces on a host.

    Args:
        hostid: Host ID
        interfaces: New interfaces to set
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted result
    """
    params = build_params(
        required={"hostid": hostid, "interfaces": interfaces},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostinterface", "replacehostinterfaces", params)
