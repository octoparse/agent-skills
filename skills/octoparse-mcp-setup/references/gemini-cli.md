# Gemini CLI MCP Configuration

## Configuration File Locations

| Scope | Path (macOS/Linux) | Path (Windows) |
|-------|-------------------|----------------|
| **Global** | `~/.gemini/settings.json` | `%USERPROFILE%\.gemini\settings.json` |
| **Project** | `.gemini/settings.json` | `.gemini\settings.json` |

Priority: Project-level configuration overrides global settings.

## OAuth 2.1 Configuration

### Using Config File

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com"
    }
  }
}
```

### Using CLI

```bash
gemini mcp add octoparse --type http https://mcp.octoparse.com
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
      }
    }
  }
}
```

### Using CLI

```bash
gemini mcp add octoparse --type http https://mcp.octoparse.com \
  --header "x-api-key:YOUR_API_KEY"
```

## Client-Specific Options

### Trust Mode

Skip tool call confirmation prompts:

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

Or via CLI:
```bash
gemini mcp add octoparse --type http https://mcp.octoparse.com --trust
```

### Environment Variables

Gemini CLI supports `$VAR` syntax:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "$OCTOPARSE_API_KEY"
      }
    }
  }
}
```

### Tool Filtering

Control which tools are available:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
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
      "timeout": 600000
    }
  }
}
```

## CLI Commands

```bash
# List all servers
gemini mcp list

# Remove server
gemini mcp remove octoparse

# Enable/disable server
gemini mcp enable octoparse
gemini mcp disable octoparse

# Add to user config (global)
gemini mcp add -s user octoparse --type http https://mcp.octoparse.com

# Add to project config (default)
gemini mcp add -s project octoparse --type http https://mcp.octoparse.com
```

### In-Chat Commands

```bash
# Check MCP server status
/mcp

# Authenticate with specific server (OAuth)
/mcp auth octoparse
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not in list | Use `gemini mcp list` to verify server is registered |
| "401 Unauthorized" | API key is invalid; verify at https://www.octoparse.com/console/account-center/api-keys |
| Configuration file not found | Check that the settings.json file is in the correct location |
| Transport errors | Ensure `--type http` is used for HTTP Streamable transport |
| Tool calls requiring confirmation | Set `"trust": true` to skip confirmations |
| Timeout errors | Increase `timeout` value (default is 600000ms / 10 minutes) |
| OAuth issues | OAuth tokens are stored in `~/.gemini/mcp-oauth-tokens.json` |
