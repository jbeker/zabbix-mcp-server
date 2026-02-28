"""Host prototype management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def hostprototype_get(hostids: Optional[List[str]] = None,
                      discoveryids: Optional[List[str]] = None,
                      output: Union[str, List[str]] = "extend",
                      search: Optional[Dict[str, str]] = None,
                      filter: Optional[Dict[str, Any]] = None,
                      extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get host prototypes from Zabbix.

    Args:
        hostids: List of host prototype IDs
        discoveryids: List of LLD rule IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"hostids": hostids, "discoveryids": discoveryids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("hostprototype", "get", params)


@mcp.tool()
def hostprototype_create(host: str, ruleid: str,
                         groupLinks: List[Dict[str, str]],
                         status: int = 0,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a host prototype in Zabbix.

    Args:
        host: Host prototype technical name
        ruleid: LLD rule ID
        groupLinks: Group links (format: [{"groupid": "1"}])
        status: Status (0=monitored, 1=unmonitored)
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"host": host, "ruleid": ruleid, "groupLinks": groupLinks, "status": status},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("hostprototype", "create", params)


@mcp.tool()
def hostprototype_update(hostid: str, host: Optional[str] = None,
                         status: Optional[int] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a host prototype in Zabbix.

    Args:
        hostid: Host prototype ID
        host: New technical name
        status: New status
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"hostid": hostid},
        optional={"host": host, "status": status},
        extra_params=extra_params,
    )
    return zabbix_write("hostprototype", "update", params)


@mcp.tool()
def hostprototype_delete(hostids: List[str]) -> str:
    """Delete host prototypes from Zabbix.

    Args:
        hostids: List of host prototype IDs to delete
    """
    return zabbix_delete("hostprototype", hostids)
