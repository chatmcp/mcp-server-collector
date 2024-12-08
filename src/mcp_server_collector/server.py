import logging
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio
from mcp_server_collector.fetch import call_fetch_tool
from mcp_server_collector.extract import extract_mcp_servers_from_content
from mcp_server_collector.submit import submit_mcp_server
from dotenv import load_dotenv
import json
load_dotenv()

logger = logging.getLogger("mcp-server-collector")
logger.setLevel(logging.INFO)

server = Server("mcp-server-collector")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="extract-mcp-servers-from-url",
            description="Extract MCP Servers from a URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                },
                "required": ["url"],
            },
        ),
        types.Tool(
            name="extract-mcp-servers-from-content",
            description="Extract MCP Servers from given content",
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "content containing mcp servers",
                    },
                },
                "required": ["content"],
            },
        ),
        types.Tool(
            name="submit-mcp-server",
            description="Submit MCP Server to MCP Servers Directory like mcp.so",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL of the MCP Server to submit",
                    },
                    "avatar_url": {
                        "type": "string",
                        "description": "avatar URL of the MCP Server to submit",
                    },
                },
                "required": ["url"],
            },
        ),
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if not arguments:
        raise ValueError("Missing arguments")

    content = None
    
    match name:
        case "extract-mcp-servers-from-url":
            url = arguments.get("url")
            if not url:
                raise ValueError("Missing url")

            content = await call_fetch_tool(url)
            
        case "extract-mcp-servers-from-content":
            content = arguments.get("content")
            
        case "submit-mcp-server":
            url = arguments.get("url")
            avatar_url = arguments.get("avatar_url") or ""
            result = await submit_mcp_server(url, avatar_url)
            content = json.dumps(result)

            return [
                types.TextContent(
                    type="text",
                    text=content,
                )
            ]
        case _:
            raise ValueError(f"Unknown tool: {name}")

    if not content:
        raise ValueError("Missing content")

    logger.info(f"Fetched content from {url}: {content}")

    mcp_servers = await extract_mcp_servers_from_content(content)
    if not mcp_servers:
        raise ValueError("Extracted no MCP Servers")

    logger.info(f"Extracted MCP Servers from {url}: {mcp_servers}")

    return [
        types.TextContent(
            type="text",
            text=mcp_servers,
        )
    ]   

async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-server-collector",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )