import aiohttp
import json
import os

async def submit_mcp_server(url: str, avatar_url: str):
    payload = {
        "url": url,
        "avatar_url": avatar_url
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                os.getenv("MCP_SERVER_SUBMIT_URL"),
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload)
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"submit mcp server failed: HTTP {response.status}")
              
    except Exception as e:
        raise Exception(f"submit mcp server failed: {str(e)}")