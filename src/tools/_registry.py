"""
Registry helpers to reduce per-tool boilerplate.

Provides utility functions for building API parameters and calling
Zabbix API methods with proper read-only guards.
"""

from typing import Any, Dict, List, Optional

from src._core import get_zabbix_client, format_response, validate_read_only


def build_params(required: Dict[str, Any], optional: Dict[str, Any],
                 extra_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Merge required params with non-None optional params and extra_params.

    Args:
        required: Parameters that are always included.
        optional: Parameters included only when not None.
        extra_params: Additional arbitrary params to merge in.

    Returns:
        Merged parameter dictionary.
    """
    params = dict(required)
    for key, value in optional.items():
        if value is not None:
            params[key] = value
    if extra_params:
        params.update(extra_params)
    return params


def zabbix_get(api_object: str, api_method: str, params: Dict[str, Any]) -> str:
    """Call a read API method, return formatted JSON.

    Args:
        api_object: Zabbix API object name (e.g. "host").
        api_method: Method name (e.g. "get").
        params: Parameters to pass.

    Returns:
        JSON formatted response string.
    """
    client = get_zabbix_client()
    obj = getattr(client, api_object)
    method = getattr(obj, api_method)
    result = method(**params)
    return format_response(result)


def zabbix_write(api_object: str, api_method: str, params: Dict[str, Any]) -> str:
    """Guard read-only, call a write API method, return formatted JSON.

    Args:
        api_object: Zabbix API object name (e.g. "host").
        api_method: Method name (e.g. "create").
        params: Parameters to pass.

    Returns:
        JSON formatted response string.
    """
    validate_read_only()
    client = get_zabbix_client()
    obj = getattr(client, api_object)
    method = getattr(obj, api_method)
    result = method(**params)
    return format_response(result)


def zabbix_delete(api_object: str, ids: List[str]) -> str:
    """Guard read-only, call delete with unpacked IDs.

    Args:
        api_object: Zabbix API object name (e.g. "host").
        ids: List of IDs to delete.

    Returns:
        JSON formatted response string.
    """
    validate_read_only()
    client = get_zabbix_client()
    obj = getattr(client, api_object)
    result = obj.delete(*ids)
    return format_response(result)
