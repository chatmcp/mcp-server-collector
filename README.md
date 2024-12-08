# mcp-server-collector MCP server

A MCP Server used to collect MCP Servers over the internet.

## Components

### Resources

No resources yet.

### Prompts

No prompts yet.

### Tools

The server implements 3 tools:

- extract-mcp-servers-from-url: Extracts MCP Servers from given URL.
  - Takes "url" as required string argument
- extract-mcp-servers-from-content: Extracts MCP Servers from given content.
  - Takes "content" as required string argument
- submit-mcp-server: Submits a MCP Server to the MCP Server Directory like mcp.so.
  - Takes "url" as required string argument and "avatar_url" as optional string argument

## Configuration

.env file is required to be set up.

```txt
OPENAI_API_KEY="sk-xxx"
OPENAI_BASE_URL="https://api.openai.com/v1"
OPENAI_MODEL="gpt-4o-mini"

MCP_SERVER_SUBMIT_URL="https://mcp.so/api/submit-project"
```

## Quickstart

### Install

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

<details>
  <summary>Development/Unpublished Servers Configuration</summary>
  ```
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "mcp-server-collector": {
      "command": "uv",
      "args": [
        "--directory",
        "path-to/mcp-server-collector",
        "run",
        "mcp-server-collector"
      ],
      "env": {
        "OPENAI_API_KEY": "sk-xxx",
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
        "OPENAI_MODEL": "gpt-4o-mini",
        "MCP_SERVER_SUBMIT_URL": "https://mcp.so/api/submit-project"
      }
    }
  }
  ```
</details>

<details>
  <summary>Published Servers Configuration</summary>
  ```
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "mcp-server-collector": {
      "command": "uvx",
      "args": [
        "mcp-server-collector"
      ],
      "env": {
        "OPENAI_API_KEY": "sk-xxx",
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
        "OPENAI_MODEL": "gpt-4o-mini",
        "MCP_SERVER_SUBMIT_URL": "https://mcp.so/api/submit-project"
      }
    }
  }
  ```
</details>

## Development

### Building and Publishing

To prepare the package for distribution:

1. Sync dependencies and update lockfile:

```bash
uv sync
```

2. Build package distributions:

```bash
uv build
```

This will create source and wheel distributions in the `dist/` directory.

3. Publish to PyPI:

```bash
uv publish
```

Note: You'll need to set PyPI credentials via environment variables or command flags:

- Token: `--token` or `UV_PUBLISH_TOKEN`
- Or username/password: `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging

Since MCP servers run over stdio, debugging can be challenging. For the best debugging
experience, we strongly recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

You can launch the MCP Inspector via [`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) with this command:

```bash
npx @modelcontextprotocol/inspector uv --directory path-to/mcp-server-collector run mcp-server-collector
```

Upon launching, the Inspector will display a URL that you can access in your browser to begin debugging.

## Community

- [MCP Server Telegram](https://t.me/+N0gv4O9SXio2YWU1)
- [MCP Server Discord](https://discord.gg/RsYPRrnyqg)

## About the author

- [idoubi](https://bento.me/idoubi)
- [mcp.so](https://mcp.so)
