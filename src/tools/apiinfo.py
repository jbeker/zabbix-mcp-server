"""API info tools for Zabbix MCP Server."""

from src._core import mcp, get_zabbix_client, format_response


@mcp.tool()
def apiinfo_version() -> str:
    """Get Zabbix API version information.

    Returns:
        str: JSON formatted API version info
    """
    client = get_zabbix_client()
    result = client.apiinfo.version()
    return format_response(result)
