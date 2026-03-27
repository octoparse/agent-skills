# VS Code MCP Configuration

## Configuration File Locations

| Scope | Path | Format |
|-------|------|--------|
| **Project** | `.vscode/mcp.json` | Standalone MCP file (Recommended) |
| **User** | User settings (`settings.json`) | `mcp.servers` object |
| **Workspace** | Workspace settings | `mcp.servers` object |

Access via Command Palette: **MCP: Open User Configuration** or **MCP: Open Workspace Folder Configuration**

## OAuth 2.1 Configuration

### Using `.vscode/mcp.json` (Recommended)

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

### Using `settings.json`

```json
{
  "mcp": {
    "servers": {
      "octoparse": {
        "type": "http",
        "url": "https://mcp.octoparse.com"
      }
    }
  }
}
```

## API Key Configuration

### Using `.vscode/mcp.json` (Recommended)

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

### Using `settings.json`

```json
{
  "mcp": {
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
}
```

## Client-Specific Options

### Secure Input Variables

For API keys, use the `inputs` array to prompt for secrets securely:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "octoparse-api-key",
      "description": "Octoparse API Key",
      "password": true
    }
  ],
  "servers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "${input:octoparse-api-key}"
      }
    }
  }
}
```

### Required VS Code Settings

Enable these settings in VS Code (`Ctrl/Cmd + ,`):

1. **Chat: Agent Enabled** (`chat.agent.enabled`) - Enable agent mode
2. **Chat: MCP Enabled** (`chat.mcp.enabled`) - Enable MCP support
3. **Chat: MCP Discovery Enabled** (`chat.mcp.discovery.enabled`) - Auto-discover servers
4. **Chat: MCP AutoStart** (`chat.mcp.autostart`) - Auto-start servers on config changes

### VS Code Commands

Access via Command Palette (`Ctrl/Cmd + Shift + P`):

| Command | Purpose |
|---------|---------|
| **MCP: Add Server** | Add new server via guided flow |
| **MCP: List Servers** | View, start, stop, restart servers |
| **MCP: Open User Configuration** | Edit global `mcp.json` |
| **MCP: Open Workspace Folder Configuration** | Edit workspace `.vscode/mcp.json` |

### Dev Container Configuration

Add to `devcontainer.json` under `customizations.vscode.mcp`:

```json
{
  "customizations": {
    "vscode": {
      "mcp": {
        "servers": {
          "octoparse": {
            "type": "http",
            "url": "https://mcp.octoparse.com"
          }
        }
      }
    }
  }
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP commands not available | Ensure GitHub Copilot Chat extension is installed and enabled |
| Server not connecting | Check that Agent Mode is enabled in chat settings |
| "401 Unauthorized" | API key is invalid; verify at https://www.octoparse.com/console/account-center/api-keys |
| Configuration not loading | Use command "MCP: List Servers" to verify configuration |
| Transport errors | Ensure `type` is set to `"http"` (HTTP Streamable) |
