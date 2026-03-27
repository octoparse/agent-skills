# Qwen Code MCP Configuration

> ⚠️ **Note**: Configuration based on community practice. Official MCP documentation may not be publicly available yet.

## Configuration File Locations

| Scope | Path (macOS/Linux) | Path (Windows) |
|-------|-------------------|----------------|
| **Global** | `~/.qwen/settings.json` | `%USERPROFILE%\.qwen\settings.json` |
| **Project** | `.qwen/settings.json` | `.qwen\settings.json` |

Priority: Project-level configuration overrides global settings.

## OAuth 2.1 Configuration

### Using Config File

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "trust": true
    }
  }
}
```

### Using CLI

```bash
qwen mcp add octoparse --type http https://mcp.octoparse.com --trust
```

## API Key Configuration

### Using Config File

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "your-api-key"
      },
      "trust": true
    }
  }
}
```

### Using CLI

```bash
qwen mcp add octoparse --type http https://mcp.octoparse.com \
  --header "x-api-key:YOUR_API_KEY" --trust
```

## Client-Specific Options

### Trust Mode (Important)

Qwen Code requires `"trust": true` to skip tool call confirmation prompts:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "trust": true
    }
  }
}
```

### Environment Variables

Qwen Code supports environment variable expansion:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "$OCTOPARSE_API_KEY"
      },
      "trust": true
    }
  }
}
```

Supported formats: `$VAR_NAME` or `${VAR_NAME}`

### Tool Filtering

Control which tools are available:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "trust": true,
      "includeTools": ["get_user_account_info", "search_user_task_list"],
      "excludeTools": ["delete_task"]
    }
  }
}
```

### Timeout Configuration

Default timeout is 600000ms (10 minutes):

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "trust": true,
      "timeout": 600000
    }
  }
}
```

### Global MCP Settings

Control server discovery globally:

```json
{
  "mcp": {
    "allowed": ["octoparse"],
    "excluded": []
  },
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "trust": true
    }
  }
}
```

## CLI Commands

```bash
# List all servers
qwen mcp list

# Remove server
qwen mcp remove octoparse

# Add to user config (global)
qwen mcp add --scope user octoparse --type http https://mcp.octoparse.com

# Add to project config (default)
qwen mcp add --scope project octoparse --type http https://mcp.octoparse.com
```

### In-Chat Commands

```bash
# List servers needing auth
/mcp auth

# Authenticate with specific server
/mcp auth octoparse
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not connecting | Use `qwen mcp list` to verify server is registered |
| "401 Unauthorized" | API key is invalid; verify at https://www.octoparse.com/console/account-center/api-keys |
| Tool calls requiring confirmation | Set `"trust": true` to skip confirmations |
| Timeout errors | Increase `timeout` value (default is 600000ms / 10 minutes) |
| Transport errors | Ensure `type` is set to `"http"` for HTTP Streamable |
| OAuth token issues | Check `~/.qwen/mcp-oauth-tokens.json` for stored tokens |
