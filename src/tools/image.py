"""Image management tools for Zabbix MCP Server."""

from typing import Any, Dict, List, Optional, Union

from src._core import mcp
from src.tools._registry import build_params, zabbix_get, zabbix_write, zabbix_delete


@mcp.tool()
def image_get(imageids: Optional[List[str]] = None,
              output: Union[str, List[str]] = "extend",
              search: Optional[Dict[str, str]] = None,
              filter: Optional[Dict[str, Any]] = None,
              extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Get images from Zabbix.

    Args:
        imageids: List of image IDs
        output: Output format
        search: Search criteria
        filter: Filter criteria
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"output": output},
        optional={"imageids": imageids, "search": search, "filter": filter},
        extra_params=extra_params,
    )
    return zabbix_get("image", "get", params)


@mcp.tool()
def image_create(name: str, imagetype: int, image: str,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Create an image in Zabbix.

    Args:
        name: Image name
        imagetype: Image type (1=icon, 2=background)
        image: Base64 encoded image
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"name": name, "imagetype": imagetype, "image": image},
        optional={},
        extra_params=extra_params,
    )
    return zabbix_write("image", "create", params)


@mcp.tool()
def image_update(imageid: str, name: Optional[str] = None,
                 image: Optional[str] = None,
                 extra_params: Optional[Dict[str, Any]] = None) -> str:
    """Update an image in Zabbix.

    Args:
        imageid: Image ID
        name: New name
        image: New base64 encoded image
        extra_params: Additional Zabbix API parameters
    """
    params = build_params(
        required={"imageid": imageid},
        optional={"name": name, "image": image},
        extra_params=extra_params,
    )
    return zabbix_write("image", "update", params)


@mcp.tool()
def image_delete(imageids: List[str]) -> str:
    """Delete images from Zabbix.

    Args:
        imageids: List of image IDs to delete
    """
    return zabbix_delete("image", imageids)
