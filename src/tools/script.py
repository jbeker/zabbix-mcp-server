"""Script management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def script_get(scriptids: Optional[List[str]] = None,
               hostids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               search: Optional[Dict[str, str]] = None,
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get scripts from Zabbix.

    Args:
        scriptids: List of script IDs to retrieve
        hostids: List of host IDs to filter by
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted list of scripts
    """
    params = build_params(
        required={"output": output},
        optional={"scriptids": scriptids, "hostids": hostids,
                  "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("script", "get", params)


@mcp.tool()
def script_create(name: str, type: int, command: str,
                  scope: int = 1,
                  execute_on: Optional[int] = None,
                  groupid: Optional[str] = None,
                  description: Optional[str] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create a new script in Zabbix.

    Args:
        name: Script name
        type: Script type (0=script, 1=IPMI, 2=SSH, 3=Telnet, 5=webhook)
        command: Script command or webhook body
        scope: Scope (1=action operation, 2=manual host action, 4=manual event action)
        execute_on: Where to execute (0=agent, 1=server, 2=proxy)
        groupid: Host group to restrict to
        description: Script description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted creation result
    """
    params = build_params(
        required={"name": name, "type": type, "command": command, "scope": scope},
        optional={"execute_on": execute_on, "groupid": groupid,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("script", "create", params)


@mcp.tool()
def script_update(scriptid: str, name: Optional[str] = None,
                  type: Optional[int] = None, command: Optional[str] = None,
                  description: Optional[str] = None,
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update a script in Zabbix.

    Args:
        scriptid: Script ID to update
        name: New name
        type: New script type
        command: New command
        description: New description
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted update result
    """
    params = build_params(
        required={"scriptid": scriptid},
        optional={"name": name, "type": type, "command": command,
                  "description": description},
        extra_params=extra_params,
    )
    return zabbix_write("script", "update", params)


@mcp.tool()
def script_delete(scriptids: List[str]) -> str:
    """Delete scripts from Zabbix.

    Args:
        scriptids: List of script IDs to delete

    Returns:
        str: JSON formatted deletion result
    """
    return zabbix_delete("script", scriptids)


@mcp.tool()
def script_execute(scriptid: str, hostid: Optional[str] = None,
                   eventid: Optional[str] = None,
                   extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Execute a script on a host or event.

    Args:
        scriptid: Script ID to execute
        hostid: Host ID to execute on
        eventid: Event ID to execute on
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted execution result
    """
    params = build_params(
        required={"scriptid": scriptid},
        optional={"hostid": hostid, "eventid": eventid},
        extra_params=extra_params,
    )
    return zabbix_write("script", "execute", params)


@mcp.tool()
def script_getscriptsbyhosts(hostids: List[str],
                             extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get scripts available on hosts.

    Args:
        hostids: List of host IDs
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted scripts by hosts
    """
    params = build_params(
        required={"hostids": hostids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("script", "getscriptsbyhosts", params)


@mcp.tool()
def script_getscriptsbyevents(eventids: List[str],
                              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get scripts available for events.

    Args:
        eventids: List of event IDs
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted scripts by events
    """
    params = build_params(
        required={"eventids": eventids},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("script", "getscriptsbyevents", params)
