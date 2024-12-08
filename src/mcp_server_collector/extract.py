import os
import logging
from openai import OpenAI
from mcp_server_collector.prompts import extract_mcp_servers_prompt

logger = logging.getLogger("mcp-server-collector")

async def extract_mcp_servers_from_content(content: str) -> str | None:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )

    user_content = extract_mcp_servers_prompt.format(content=content)

    logger.info(f"Extract prompt: {user_content}")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_content,
            }
        ],
        model=os.getenv("OPENAI_MODEL"),
        response_format={"type": "json_object"},
    )

    return chat_completion.choices[0].message.content
