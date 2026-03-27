# OpenClaw MCP Configuration

## Configuration File Locations

| Scope | Path (macOS/Linux) | Path (Windows) |
|-------|-------------------|----------------|
| **Global** | `~/.openclaw/openclaw.json` | `%APPDATA%\openclaw\openclaw.json` |
| **Project** | `.openclaw/openclaw.json` | `.openclaw\openclaw.json` |

Priority: Project-level configuration overrides global settings.

> ⚠️ **Note**: OpenClaw uses a special stdio transport via mcporter, different from other clients' HTTP transport.

## OAuth 2.1 Configuration

### Step 1: Install mcporter

```bash
# Install or update mcporter
npm install -g mcporter

# Verify installation
mcporter --version
```

### Step 2: Configure Octoparse in mcporter

```bash
# Add Octoparse MCP server
mcporter config add octoparse https://mcp.octoparse.com
```

### Step 3: Configure OpenClaw

Add to your OpenClaw configuration:

```json
{
  "mcp": {
    "servers": {
      "octoparse": {
        "command": "mcporter",
        "args": ["run", "stdio", "--server", "octoparse"]
      }
    }
  }
}
```

## API Key Configuration

### Step 1: Install mcporter

```bash
# Install or update mcporter
npm install -g mcporter

# Verify installation
mcporter --version
```

### Step 2: Configure Octoparse with API Key

```bash
# Add Octoparse MCP server
mcporter config add octoparse https://mcp.octoparse.com

# Set API Key for authentication
mcporter config set octoparse header.x-api-key "your-api-key"
```

### Step 3: Configure OpenClaw

Add to your OpenClaw configuration:

```json
{
  "mcp": {
    "servers": {
      "octoparse": {
        "command": "mcporter",
        "args": ["run", "stdio", "--server", "octoparse"]
      }
    }
  }
}
```

## Client-Specific Options

### mcporter CLI Commands

```bash
# List configured servers
mcporter list

# Test Octoparse connection
mcporter call octoparse.get_user_info

# Remove server configuration
mcporter config remove octoparse

# Get current API key (to verify)
mcporter config get octoparse header.x-api-key
```

### OpenClaw Configuration Formats

OpenClaw supports multiple config formats:
- **JSON**: `~/.openclaw/openclaw.json`
- **JSON5**: `~/.openclaw/openclaw.json5` (allows comments)
- **YAML**: `~/.openclaw/openclaw.yaml`

### Environment Variables

You can use environment variables in the configuration:

```json
{
  "mcp": {
    "servers": {
      "octoparse": {
        "command": "mcporter",
        "args": ["run", "stdio", "--server", "octoparse"],
        "env": {
          "OCTOPARSE_API_KEY": "$OCTOPARSE_API_KEY"
        }
      }
    }
  }
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| mcporter command not found | Ensure npm global bin is in PATH, or use `npx mcporter <command>` |
| API Key not working | Verify with `mcporter config get octoparse header.x-api-key`. If empty, re-set the key |
| Server connection failed | 1. Check network connectivity to https://mcp.octoparse.com<br>2. Verify mcporter is running: `mcporter list`<br>3. Restart OpenClaw and try again |
| OpenClaw not recognizing tools | Ensure MCP config is in correct location:<br>- macOS: `~/.openclaw/openclaw.json`<br>- Windows: `%APPDATA%\openclaw\openclaw.json` |
| "401 Unauthorized" | API key is invalid or expired; verify at https://www.octoparse.com/console/account-center/api-keys |
| Configuration file not found | Check that openclaw.json exists in the correct location |
| Transport errors | Ensure mcporter is properly installed and accessible in PATH |
