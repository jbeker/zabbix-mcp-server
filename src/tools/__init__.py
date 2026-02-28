"""
Zabbix MCP Server tool modules.

Importing this package registers all tool functions with the FastMCP instance.
Each sub-module defines tools for a specific Zabbix API object type.
"""

from src.tools import (  # noqa: F401
    # Phase 0/1: Original + completed object types
    apiinfo,
    configuration,
    discoveryrule,
    event,
    graph,
    history,
    host,
    hostgroup,
    item,
    itemprototype,
    maintenance,
    problem,
    proxy,
    template,
    trend,
    trigger,
    user,
    usermacro,
    # Phase 2: Core infrastructure
    hostinterface,
    templategroup,
    action,
    mediatype,
    script,
    dashboard,
    service,
    sla,
    # Phase 3: Discovery, prototypes, automation
    triggerprototype,
    graphprototype,
    hostprototype,
    drule,
    dcheck,
    dhost,
    dservice,
    httptest,
    correlation,
    valuemap,
    graphitem,
    map,
    # Phase 4: User/RBAC and administration
    usergroup,
    userdirectory,
    role,
    token,
    autoregistration,
    authentication,
    settings,
    housekeeping,
    auditlog,
    # Phase 5: Remaining objects
    templatedashboard,
    report,
    task,
    hanode,
    iconmap,
    image,
    regexp,
    module,
    connector,
    proxygroup,
    alert,
)
