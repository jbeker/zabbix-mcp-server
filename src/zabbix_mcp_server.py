#!/usr/bin/env python3
"""
Zabbix MCP Server - Complete integration with Zabbix API using python-zabbix-utils

This server provides comprehensive access to Zabbix API functionality through
the Model Context Protocol (MCP), enabling AI assistants and other tools to
interact with Zabbix monitoring systems.

Author: Zabbix MCP Server Contributors
License: MIT
"""

import logging
import os

import click

# Re-export core objects for backward compatibility (scripts, tests, etc.)
from src._core import (  # noqa: F401
    mcp,
    get_zabbix_client,
    format_response,
    validate_read_only,
    is_read_only,
    set_read_only,
)

# Import all tool modules to register tools with the mcp instance
import src.tools  # noqa: F401

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--mode",
    type=click.Choice(["read-only", "read-write"], case_sensitive=False),
    default=None,
    help="Access mode controlling which tools are exposed.",
)
@click.option(
    "--transport",
    type=click.Choice(["stdio", "streamable-http"], case_sensitive=False),
    default=None,
    help="MCP transport to use.",
)
@click.option(
    "--host",
    type=str,
    default=None,
    help="Host for HTTP transports.",
)
@click.option(
    "--port",
    type=int,
    default=None,
    help="Port for HTTP transports.",
)
@click.option(
    "--verify-ssl/--no-verify-ssl",
    default=None,
    help="Enable or disable SSL certificate verification.",
)
def main(mode, transport, host, port, verify_ssl):
    """Zabbix MCP Server."""
    # CLI flags override env vars
    if mode is not None:
        set_read_only(mode == "read-only")
    if verify_ssl is not None:
        os.environ["VERIFY_SSL"] = str(verify_ssl).lower()

    transport = transport or os.getenv("ZABBIX_MCP_TRANSPORT", "stdio")
    transport = transport.lower()
    host = host or os.getenv("ZABBIX_MCP_HOST", "0.0.0.0")
    port = port or int(os.getenv("ZABBIX_MCP_PORT", "8002"))

    logger.info("Starting Zabbix MCP Server")
    logger.info(f"Transport: {transport}")
    logger.info(f"Read-only mode: {is_read_only()}")
    logger.info(f"Zabbix URL: {os.getenv('ZABBIX_URL', 'Not configured')}")

    try:
        if transport == "stdio":
            mcp.run()
        else:  # streamable-http
            mcp.run(
                transport="streamable-http",
                host=host,
                port=port,
            )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


if __name__ == "__main__":
    main()
