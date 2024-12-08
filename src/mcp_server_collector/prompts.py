extract_mcp_servers_prompt = """Please extract all MCP Servers from the following content and return a JSON array. Each item should contain:
- name: extracted from the repository name in the URL
- title: a human readable title
- description: a brief description of the server
- url: the full GitHub repository URL
- author_name: extracted from the GitHub username in the URL

Example response format:
[
    {{
        "name": "mcp-server-example",
        "title": "MCP Server Example",
        "description": "A sample MCP server implementation",
        "url": "https://github.com/username/mcp-server-example",
        "author_name": "username"
    }}
]

Content to analyze:
{content}
"""