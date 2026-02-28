"""Graph item tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get


@mcp.tool()
def graphitem_get(graphids: Optional[List[str]] = None,
                  itemids: Optional[List[str]] = None,
                  output: Union[str, List[str]] = "extend",
                  extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get graph items from Zabbix.

    Args:
        graphids: List of graph IDs to filter by
        itemids: List of item IDs to filter by
        output: Output format
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"graphids": graphids, "itemids": itemids},
        extra_params=extra_params,
    )
    return zabbix_get("graphitem", "get", params)
