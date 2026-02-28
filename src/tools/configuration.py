"""Configuration export/import tools for Zabbix MCP Server."""

from typing import Any, Dict, Optional

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write


@mcp.tool()
def configuration_export(format: str = "json",
                         options: Optional[Dict[str, Any]] = None,
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Export configuration from Zabbix.

    Args:
        format: Export format (json, xml)
        options: Export options
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted export result
    """
    params = build_params(
        required={"format": format},
        optional={"options": options},
        extra_params=extra_params,
    )
    return zabbix_get("configuration", "export", params)


@mcp.tool()
def configuration_import(format: str, source: str,
                         rules: Dict[str, Any],
                         extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Import configuration to Zabbix.

    Args:
        format: Import format (json, xml)
        source: Configuration data to import
        rules: Import rules
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted import result
    """
    params = build_params(
        required={"format": format, "source": source, "rules": rules},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("configuration", "import_", params)


@mcp.tool()
def configuration_importcompare(format: str, source: str,
                                rules: Dict[str, Any],
                                extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Compare import data with current configuration without applying changes.

    Args:
        format: Import format (json, xml)
        source: Configuration data to compare
        rules: Import rules
        extra_params: Additional Zabbix API parameters

    Returns:
        str: JSON formatted comparison result
    """
    params = build_params(
        required={"format": format, "source": source, "rules": rules},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_get("configuration", "importcompare", params)
