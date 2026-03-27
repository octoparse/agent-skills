# Cursor IDE MCP Configuration

## Configuration File Locations

| Scope | Path (macOS/Linux) | Path (Windows) |
|-------|-------------------|----------------|
| **Global** | `~/.cursor/mcp.json` | `%USERPROFILE%\.cursor\mcp.json` |
| **Project** | `.cursor/mcp.json` | `.cursor\mcp.json` |

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

### Using UI

1. Open **Cursor Settings** → **Tools & MCP**
2. Click **"Add new MCP server"**
3. Fill in:
   - **Name**: `octoparse`
   - **Type**: `HTTP` (HTTP Streamable)
   - **URL**: `https://mcp.octoparse.com`

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

### Using UI

1. Open **Settings** → **Tools & MCP**
2. Click **"Add new MCP server"**
3. Fill in:
   - **Name**: `octoparse`
   - **Type**: `HTTP` (HTTP Streamable)
   - **URL**: `https://mcp.octoparse.com`
   - **Headers**: Add `x-api-key` with your API key value

## Client-Specific Options

### Variable Interpolation

Cursor supports environment variables in configuration:

```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "${env:OCTOPARSE_API_KEY}"
      }
    }
  }
}
```

### Important Requirements

- **Tool Limit**: ~40 active tools maximum
- **Required Mode**: Agent Mode must be enabled (not Ask Mode)
- **Minimum Version**: v0.40+ for MCP support

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Configuration not working | Restart Cursor completely after configuration changes |
| Yellow indicator shown | Click **"Connect"** to complete OAuth/setup |
| Agent Mode required | Cursor must be in Agent Mode (not Ask Mode) to access MCP tools |
| "401 Unauthorized" | API key is invalid; verify at https://www.octoparse.com/console/account-center/api-keys |
| Transport not supported | Ensure you select **HTTP** type, not SSE or stdio |
| Environment variable not working | Check variable is set in system environment |
