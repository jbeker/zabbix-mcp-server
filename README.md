# Zabbix MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A comprehensive Model Context Protocol (MCP) server for Zabbix integration using FastMCP and python-zabbix-utils. This server provides **216 tools** covering the full Zabbix API across **57 object types**.

<a href="https://glama.ai/mcp/servers/@mpeirone/zabbix-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@mpeirone/zabbix-mcp-server/badge" alt="zabbix-mcp-server MCP server" />
</a>

## Features

All tools support an `extra_params` argument for passing any additional Zabbix API parameters not in the explicit signature.

### Host Management
- `host_get` - Retrieve hosts with advanced filtering
- `host_create` - Create new hosts with interfaces and templates
- `host_update` - Update existing host configurations
- `host_delete` - Remove hosts from monitoring
- `host_massadd` - Mass add groups, templates, macros, or interfaces to hosts
- `host_massremove` - Mass remove groups, templates, or macros from hosts
- `host_massupdate` - Mass update hosts with the same properties

### Host Group Management
- `hostgroup_get` - Retrieve host groups
- `hostgroup_create` - Create new host groups
- `hostgroup_update` - Modify existing host groups
- `hostgroup_delete` - Remove host groups
- `hostgroup_massadd` - Mass add hosts or templates to groups
- `hostgroup_massremove` - Mass remove hosts or templates from groups
- `hostgroup_massupdate` - Mass update (replace) hosts/templates in groups
- `hostgroup_propagate` - Propagate permissions and tag filters to child groups

### Host Interface Management
- `hostinterface_get` - Retrieve host interfaces
- `hostinterface_create` - Create new host interfaces
- `hostinterface_update` - Update host interfaces
- `hostinterface_delete` - Remove host interfaces
- `hostinterface_massadd` - Mass add interfaces to hosts
- `hostinterface_massremove` - Mass remove interfaces from hosts
- `hostinterface_replacehostinterfaces` - Replace all interfaces on a host

### Item Management
- `item_get` - Retrieve monitoring items with filtering
- `item_create` - Create new monitoring items
- `item_update` - Update existing items
- `item_delete` - Remove monitoring items

### Trigger Management
- `trigger_get` - Retrieve triggers and alerts
- `trigger_create` - Create new triggers
- `trigger_update` - Modify existing triggers
- `trigger_delete` - Remove triggers

### Template Management
- `template_get` - Retrieve monitoring templates
- `template_create` - Create new templates
- `template_update` - Update existing templates
- `template_delete` - Remove templates
- `template_massadd` - Mass add groups, hosts, or macros to templates
- `template_massremove` - Mass remove groups, hosts, or macros from templates
- `template_massupdate` - Mass update templates

### Template Group Management
- `templategroup_get` - Retrieve template groups
- `templategroup_create` - Create template groups
- `templategroup_update` - Update template groups
- `templategroup_delete` - Remove template groups
- `templategroup_massadd` - Mass add templates to groups
- `templategroup_massremove` - Mass remove templates from groups
- `templategroup_massupdate` - Mass update template groups
- `templategroup_propagate` - Propagate permissions to child groups

### Problem & Event Management
- `problem_get` - Retrieve current problems and issues
- `event_get` - Get historical events
- `event_acknowledge` - Acknowledge events and problems

### Data Retrieval
- `history_get` - Access historical monitoring data
- `history_clear` - Clear history data for items
- `history_push` - Push history data to Zabbix
- `trend_get` - Retrieve trend data and statistics

### User Management
- `user_get` - Retrieve user accounts
- `user_create` - Create new users
- `user_update` - Update user information
- `user_delete` - Remove user accounts
- `user_checkauthentication` - Check or validate a user session
- `user_unblock` - Unblock users blocked by failed login attempts

### User Group Management
- `usergroup_get` - Retrieve user groups
- `usergroup_create` - Create user groups
- `usergroup_update` - Update user groups
- `usergroup_delete` - Remove user groups

### User Directory Management
- `userdirectory_get` - Retrieve user directories (LDAP/SAML)
- `userdirectory_create` - Create user directories
- `userdirectory_update` - Update user directories
- `userdirectory_delete` - Remove user directories
- `userdirectory_test` - Test a user directory configuration

### Role Management
- `role_get` - Retrieve roles
- `role_create` - Create roles
- `role_update` - Update roles
- `role_delete` - Remove roles

### Token Management
- `token_get` - Retrieve API tokens
- `token_create` - Create API tokens
- `token_update` - Update API tokens
- `token_delete` - Remove API tokens
- `token_generate` - Generate (regenerate) auth strings for tokens

### Proxy Management
- `proxy_get` - Retrieve Zabbix proxies with filtering
- `proxy_create` - Create new proxies
- `proxy_update` - Update existing proxies
- `proxy_delete` - Remove proxies

### Proxy Group Management
- `proxygroup_get` - Retrieve proxy groups
- `proxygroup_create` - Create proxy groups
- `proxygroup_update` - Update proxy groups
- `proxygroup_delete` - Remove proxy groups

### Maintenance Management
- `maintenance_get` - Retrieve maintenance periods
- `maintenance_create` - Schedule maintenance windows
- `maintenance_update` - Modify maintenance periods
- `maintenance_delete` - Remove maintenance schedules

### Graph Management
- `graph_get` - Retrieve graph configurations
- `graph_create` - Create graphs
- `graph_update` - Update graphs
- `graph_delete` - Remove graphs
- `graphitem_get` - Retrieve graph items

### LLD (Low-Level Discovery) Rules
- `discoveryrule_get` - Get LLD rules
- `discoveryrule_create` - Create LLD rules
- `discoveryrule_update` - Update LLD rules
- `discoveryrule_delete` - Remove LLD rules

### LLD Prototypes
- `itemprototype_get` / `create` / `update` / `delete` - Item prototypes
- `triggerprototype_get` / `create` / `update` / `delete` - Trigger prototypes
- `graphprototype_get` / `create` / `update` / `delete` - Graph prototypes
- `hostprototype_get` / `create` / `update` / `delete` - Host prototypes

### Network Discovery
- `drule_get` / `create` / `update` / `delete` - Network discovery rules
- `dcheck_get` - Discovery checks
- `dhost_get` - Discovered hosts
- `dservice_get` - Discovered services

### Action & Alert Management
- `action_get` / `create` / `update` / `delete` - Actions
- `alert_get` - Alerts
- `mediatype_get` / `create` / `update` / `delete` - Media types

### Script Management
- `script_get` / `create` / `update` / `delete` - Scripts
- `script_execute` - Execute a script on a host or event
- `script_getscriptsbyhosts` - Get scripts available on hosts
- `script_getscriptsbyevents` - Get scripts available for events

### Service & SLA Management
- `service_get` / `create` / `update` / `delete` - Services
- `sla_get` / `create` / `update` / `delete` - SLAs
- `sla_getsli` - Get SLI (Service Level Indicator) data

### Dashboard Management
- `dashboard_get` / `create` / `update` / `delete` - Dashboards
- `templatedashboard_get` / `create` / `update` / `delete` - Template dashboards

### Web Scenario Management
- `httptest_get` / `create` / `update` / `delete` - Web scenarios

### Correlation Management
- `correlation_get` / `create` / `update` / `delete` - Event correlations

### User Macro Management
- `usermacro_get` - Retrieve user macros
- `usermacro_create` / `update` / `delete` - Host macros
- `usermacro_createglobal` / `updateglobal` / `deleteglobal` - Global macros

### Value Map Management
- `valuemap_get` / `create` / `update` / `delete` - Value maps

### Map Management
- `map_get` / `create` / `update` / `delete` - Network maps

### Configuration Management
- `configuration_export` - Export Zabbix configurations
- `configuration_import` - Import configurations
- `configuration_importcompare` - Compare import data with current config

### Report Management
- `report_get` / `create` / `update` / `delete` - Scheduled reports

### Administration
- `autoregistration_get` / `update` - Autoregistration settings
- `authentication_get` / `update` - Authentication settings
- `settings_get` / `update` - Global settings
- `housekeeping_get` / `update` - Housekeeping settings
- `auditlog_get` - Audit log entries
- `hanode_get` - HA cluster nodes
- `task_get` / `create` - Tasks (check now, diagnostics)

### Image & Icon Management
- `image_get` / `create` / `update` / `delete` - Images
- `iconmap_get` / `create` / `update` / `delete` - Icon maps

### Module & Connector Management
- `module_get` / `create` / `update` / `delete` - Modules
- `connector_get` / `create` / `update` / `delete` - Connectors

### Regular Expression Management
- `regexp_get` / `create` / `update` / `delete` - Regular expressions

### System Info
- `apiinfo_version` - Get API version information

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Access to a Zabbix server with API enabled

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mpeirone/zabbix-mcp-server.git
   cd zabbix-mcp-server
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure environment variables:**
   ```bash
   cp config/.env.example .env
   # Edit .env with your Zabbix server details
   ```

4. **Test the installation:**
   ```bash
   uv run python scripts/test_server.py
   ```

## Configuration

### Required Environment Variables

- `ZABBIX_URL` - Your Zabbix server API endpoint (e.g., `https://zabbix.example.com`)

### Authentication (choose one method)

**Method 1: API Token (Recommended)**
- `ZABBIX_TOKEN` - Your Zabbix API token

**Method 2: Username/Password**
- `ZABBIX_USER` - Your Zabbix username
- `ZABBIX_PASSWORD` - Your Zabbix password

### Optional Configuration

- `READ_ONLY` - Set to `true`, `1`, or `yes` to enable read-only mode (only GET operations allowed)
- `VERIFY_SSL` - Enable/disable SSL certificate verification (default: `true`)

### Transport Configuration

- `ZABBIX_MCP_TRANSPORT` - Transport type: `stdio` (default) or `streamable-http`

**HTTP Transport Configuration** (only used when `ZABBIX_MCP_TRANSPORT=streamable-http`):
- `ZABBIX_MCP_HOST` - Server host (default: `127.0.0.1`)
- `ZABBIX_MCP_PORT` - Server port (default: `8000`)
- `ZABBIX_MCP_STATELESS_HTTP` - Stateless mode (default: `false`)
- `AUTH_TYPE` - Must be set to `no-auth` for streamable-http transport

## Usage

### Running the Server

**With startup script (recommended):**
```bash
uv run python scripts/start_server.py
```

**Direct execution:**
```bash
uv run python src/zabbix_mcp_server.py
```

### Transport Options

The server supports two transport methods:

#### STDIO Transport (Default)
Standard input/output transport for MCP clients like Claude Desktop:
```bash
# Set in .env or environment
ZABBIX_MCP_TRANSPORT=stdio
```

#### HTTP Transport
HTTP-based transport for web integrations:
```bash
# Set in .env or environment
ZABBIX_MCP_TRANSPORT=streamable-http
ZABBIX_MCP_HOST=127.0.0.1
ZABBIX_MCP_PORT=8000
ZABBIX_MCP_STATELESS_HTTP=false
AUTH_TYPE=no-auth
```

**Note:** When using `streamable-http` transport, `AUTH_TYPE` must be set to `no-auth`.

### Testing

**Run unit tests:**
```bash
uv run pytest tests/ -v
```

**Run integration smoke tests:**
```bash
uv run python scripts/test_server.py
```

### Read-Only Mode

When `READ_ONLY=true`, the server will only expose GET operations (retrieve data) and block all create, update, and delete operations. This is useful for:

- Monitoring dashboards
- Read-only integrations
- Security-conscious environments
- Preventing accidental modifications

### Example Tool Calls

**Get all hosts:**
```python
host_get()
```

**Get hosts in specific group:**
```python
host_get(groupids=["1"])
```

**Get hosts with extra API parameters:**
```python
host_get(extra_params={"selectInterfaces": "extend", "selectGroups": "extend"})
```

**Create a new host:**
```python
host_create(
    host="server-01",
    groups=[{"groupid": "1"}],
    interfaces=[{
        "type": 1,
        "main": 1,
        "useip": 1,
        "ip": "192.168.1.100",
        "dns": "",
        "port": "10050"
    }]
)
```

**Get recent problems:**
```python
problem_get(recent=True, limit=10)
```

**Get history data:**
```python
history_get(
    itemids=["12345"],
    time_from=1640995200,
    limit=100
)
```

**Create a host macro:**
```python
usermacro_create(hostid="1", macro="{$MY_MACRO}", value="secret", type=1)
```

**Get SLI data for an SLA:**
```python
sla_getsli(slaid="1", period_from=1704067200, period_to=1706745600)
```

**Execute a script on a host:**
```python
script_execute(scriptid="1", hostid="2")
```

## MCP Integration

This server is designed to work with MCP-compatible clients like Claude Desktop. See [MCP_SETUP.md](MCP_SETUP.md) for detailed integration instructions.

## Docker Support

### Using Docker Compose

1. **Configure environment:**
   ```bash
   cp config/.env.example .env
   # Edit .env with your settings
   ```

2. **Run with Docker Compose:**
   ```bash
   docker compose up -d
   ```

### Building Docker Image

```bash
docker build -t zabbix-mcp-server .
```

## Development

### Project Structure

```
zabbix-mcp-server/
├── src/
│   ├── __init__.py                # Package metadata
│   ├── _core.py                   # FastMCP instance, client management, utilities
│   ├── zabbix_mcp_server.py       # Slim entrypoint with backward-compat re-exports
│   └── tools/
│       ├── __init__.py            # Imports all tool modules to register them
│       ├── _registry.py           # Helper functions (build_params, zabbix_get/write/delete)
│       ├── host.py                # Host management tools
│       ├── hostgroup.py           # Host group management tools
│       ├── item.py                # Item management tools
│       ├── trigger.py             # Trigger management tools
│       ├── template.py            # Template management tools
│       └── ...                    # 57 tool modules total (one per API object type)
├── tests/
│   ├── conftest.py                # Shared fixtures (mock client, env vars)
│   ├── test_core.py               # Tests for _core module
│   ├── test_registry.py           # Tests for _registry helpers
│   └── test_tools.py              # Tests for tool functions
├── scripts/
│   ├── start_server.py            # Startup script with validation
│   └── test_server.py             # Integration smoke tests
├── config/
│   ├── .env.example               # Environment configuration template
│   └── mcp.json                   # MCP client configuration example
├── pyproject.toml                 # Python project configuration
├── requirements.txt               # Dependencies
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Docker Compose setup
├── README.md                      # This file
├── MCP_SETUP.md                   # MCP integration guide
├── CONTRIBUTING.md                # Contribution guidelines
├── CHANGELOG.md                   # Version history
└── LICENSE                        # MIT license
```

### Architecture

The server uses a modular architecture:

- **`_core.py`** holds the shared FastMCP instance, Zabbix client management, and utility functions (`format_response`, `validate_read_only`, `get_transport_config`)
- **`tools/_registry.py`** provides helper functions (`build_params`, `zabbix_get`, `zabbix_write`, `zabbix_delete`) that reduce per-tool boilerplate
- **`tools/<object>.py`** modules each define tools for one Zabbix API object type using `@mcp.tool()` decorators
- **`zabbix_mcp_server.py`** is a slim entrypoint that re-exports core objects and imports all tool modules

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Running Tests

```bash
# Unit tests
uv run pytest tests/ -v

# Unit tests with coverage
uv run pytest tests/ --cov=src --cov-report=term-missing

# Integration smoke tests (requires Zabbix connection)
uv run python scripts/test_server.py

# Test with Docker
docker-compose exec zabbix-mcp python scripts/test_server.py
```

## Error Handling

The server includes comprehensive error handling:

- Authentication errors are clearly reported
- Read-only mode violations are blocked with descriptive messages
- Invalid parameters are validated
- Network and API errors are properly formatted
- Detailed logging for troubleshooting

## Security Considerations

- Use API tokens instead of username/password when possible
- Enable read-only mode for monitoring-only use cases
- Secure your environment variables
- Use HTTPS for Zabbix server connections
- Regularly rotate API tokens
- Store configuration files securely

## Troubleshooting

### Common Issues

**Connection Failed:**
- Verify `ZABBIX_URL` is correct and accessible
- Check authentication credentials
- Ensure Zabbix API is enabled

**Permission Denied:**
- Verify user has sufficient Zabbix permissions
- Check if read-only mode is enabled when trying to modify data

**Tool Not Found:**
- Ensure all dependencies are installed: `uv sync`
- Verify Python version compatibility (3.10+)

### Debug Mode

Set environment variable for detailed logging:
```bash
export DEBUG=1
uv run python scripts/start_server.py
```

## Dependencies

- [FastMCP](https://github.com/jlowin/fastmcp) - MCP server framework
- [python-zabbix-utils](https://github.com/zabbix/python-zabbix-utils) - Official Zabbix Python library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Zabbix](https://www.zabbix.com/) for the monitoring platform
- [Model Context Protocol](https://modelcontextprotocol.io/) for the integration standard
- [FastMCP](https://github.com/jlowin/fastmcp) for the server framework

## Support

- [Documentation](README.md)
- [Issue Tracker](https://github.com/mpeirone/zabbix-mcp-server/issues)
- [Discussions](https://github.com/mpeirone/zabbix-mcp-server/discussions)

---

**Made with care for the Zabbix and MCP communities**
