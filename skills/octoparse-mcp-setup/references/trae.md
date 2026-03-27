# TRAE IDE MCP Configuration

## Configuration File Locations

| Scope | Path | Method |
|-------|------|--------|
| **Project** | `.trae/mcp.json` | Manual configuration file *(Community-discovered)* |
| **UI** | Settings → MCP | GUI configuration *(Officially recommended)* |

> ⚠️ **Note**: `.trae/mcp.json` path is based on community practice. Official documentation recommends using the UI configuration method.

## OAuth 2.1 Configuration

### Using Config File

```json
{
  "servers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com"
    }
  }
}
```

### Using UI

1. Open TRAE IDE
2. Click the **Settings** icon
3. Navigate to **MCP** in the left sidebar
4. Click **Add > Manually Add**
5. Enter configuration:
   - **Name**: `octoparse`
   - **Type**: HTTP (HTTP Streamable)
   - **URL**: `https://mcp.octoparse.com`

## API Key Configuration

### Using Config File

```json
{
  "servers": {
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

1. Open **Settings > MCP**
2. Click **Add > Manually Add**
3. Enter configuration:
   - **Name**: `octoparse`
   - **Type**: HTTP (HTTP Streamable)
   - **URL**: `https://mcp.octoparse.com`
   - **Headers**: Add `x-api-key` with your API key value

## Client-Specific Options

### Environment Variables

TRAE supports environment variables in configuration:

```json
{
  "servers": {
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

### Using MCP in Chat

Once configured:

1. Save the configuration
2. Return to the TRAE chat interface
3. Select **"Builder with MCP"** or your custom agent
4. The AI can now use the configured MCP tools

### MCP Market (Built-in)

For supported MCP servers:

1. Open TRAE Settings → MCP
2. Click **Add > Add from Market**
3. Search for "Octoparse"
4. Select and fill in required configuration

## Server Types

| Type | Use Case | Description |
|------|----------|-------------|
| `http` | **HTTP Streamable - Recommended for Octoparse** | Remote servers over HTTP |
| `stdio` | Local command-based servers | Command execution |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Configuration not loading | Restart TRAE after configuration changes |
| Server not appearing | Check Settings > MCP for server status |
| "401 Unauthorized" | API key is invalid; verify at https://www.octoparse.com/console/account-center/api-keys |
| Cannot add manually | Ensure you select **Manually Add** from the dropdown |
| Agent not using MCP | Ensure you select **"Builder with MCP"** agent |
| Transport errors | Ensure **Type** is set to **HTTP** (HTTP Streamable) |
| Environment variable not working | Check variable is set in system environment |
