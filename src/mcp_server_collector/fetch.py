from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uvx",
    args=["mcp-server-fetch"],
    env=None
)

async def call_fetch_tool(url: str):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "fetch",
                arguments={
                    "url": url,
                    "max_length": 100000,
                    "raw": True
                }
            )

            return result.content[0].text
