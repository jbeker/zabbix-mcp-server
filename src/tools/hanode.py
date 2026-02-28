"""HA node tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def hanode_get(ha_nodeids: Optional[List[str]] = None,
               output: Union[str, List[str]] = "extend",
               filter: Optional[Dict[str, Any]] = None,
               extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get HA cluster nodes from Zabbix.

    Args:
        ha_nodeids: List of HA node IDs
        output: Output format
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"ha_nodeids": ha_nodeids, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("hanode", "get", params)
