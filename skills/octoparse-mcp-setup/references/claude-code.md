# Claude Code MCP Configuration

## Configuration File Locations

| Scope | Path (macOS/Linux) | Path (Windows) |
|-------|-------------------|----------------|
| **Global** | `~/.claude/settings.json` | `%USERPROFILE%\.claude\settings.json` |
| **Project** | `.claude/settings.json` | `.claude\settings.json` |

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
# Add Octoparse MCP server (OAuth)
claude mcp add octoparse --type http https://mcp.octoparse.com
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
# Add with API Key
claude mcp add octoparse --type http https://mcp.octoparse.com --header "x-api-key:YOUR_API_KEY"
```

## Client-Specific Options

### Configuration Parameters Reference

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | Yes | Transport type. Use `"http"` for HTTP Streamable |
| `url` | string | Yes | MCP server endpoint URL |
| `headers` | object | No | HTTP headers including API key authentication |
| `headers.x-api-key` | string | No | Your Octoparse API key |

### Timeout Configuration

Optional timeout setting (default varies by version):

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "timeout": 60000
    }
  }
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Cannot connect to MCP server" | Verify URL is correct: `https://mcp.octoparse.com` and type is `http` |
| "401 Unauthorized" | API key is invalid or expired; verify at https://www.octoparse.com/console/account-center/api-keys |
| Configuration not loading | Ensure Claude Code is updated to the latest version |
| Transport errors | Ensure you are using `type: "http"` (HTTP Streamable), not legacy SSE |
