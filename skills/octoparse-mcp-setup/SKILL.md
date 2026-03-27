---
name: octoparse-mcp-setup
description: Configure and authorize the Octoparse MCP server with OAuth 2.1 or API Key authentication.
---

## When to use

Use this skill when:
- Octoparse MCP server is not detected in the system
- User receives "MCP server not found" or connection errors
- Authorization is required before using Octoparse tools
- User asks to configure Octoparse MCP for a specific IDE/editor

## Authentication Methods

Choose ONE method:

1. **OAuth 2.1** - Browser-based login (recommended for interactive use)
2. **API Key** - Direct API key authentication (for automated/headless environments)

## Decision Tree

```
Start
  │
  ▼
Step 1: Detect Client
  │
  ├── Claude/Cursor/Gemini/Qwen ──► Use mcpServers format
  ├── VS Code/TRAE ───────────────► Use servers format
  └── OpenClaw ───────────────────► Use mcporter + stdio
  │
  ▼
Step 2: Check Current Status
  │
  ├── Already configured & working ──► EXIT (inform user)
  └── Not configured / Invalid ─────► Continue
  │
  ▼
Step 3: Choose Auth Method
  │
  ├── OAuth 2.1 ──► Path A
  │   ├── OAuth succeeds ──► DONE
  │   └── OAuth fails 3x ──► Offer API Key fallback
  │
  └── API Key ────► Path B
      ├── API Key obtained ──► Configure & Verify
      └── API Key fails 3x ──► Suggest regenerating key
```

## Token Optimization Note

**To minimize token usage:**
- For basic configuration, use the JSON examples in Step A1/B2 directly
- Read reference files ONLY when:
  - Need client-specific options (trust, tool filtering, etc.)
  - Troubleshooting client-specific errors
  - User asks for advanced configuration

## Instructions

### Step 1: Detect MCP Client

**Primary detection** (check current runtime environment):
- Check environment variables:
  - `CLYDE_CODE_VERSION` or `CLAUDE_CODE_VERSION` → **Claude Code**
  - `CURSOR_VERSION` → **Cursor**
  - `GEMINI_CLI_VERSION` → **Gemini CLI**
  - `QWEN_CODE_VERSION` → **Qwen Code**
  - `VSCODE_PID` or `VSCODE_CWD` → **VS Code** (may need confirmation)
  - `TRAE_VERSION` → **TRAE**
  - `OPENCLAW_VERSION` → **OpenClaw**
- Check execution context (which AI assistant invoked this skill)

**Secondary detection** (if primary unclear, check config files):
1. **Claude Code**: `~/.claude/settings.json` or `.claude/settings.json`
2. **Cursor**: `~/.cursor/mcp.json` or `.cursor/mcp.json`
3. **VS Code**: `.vscode/mcp.json` or VS Code settings
4. **Gemini CLI**: `~/.gemini/settings.json` or `.gemini/settings.json`
5. **Qwen Code**: `~/.qwen/settings.json` or `.qwen/settings.json`
6. **TRAE**: `.trae/mcp.json`
7. **OpenClaw**: `~/.config/openclaw/openclaw.json5` or `~/.openclaw/openclaw.json`

**If multiple clients detected:** Ask the user which one to configure.

### Step 2: Check Current MCP Status

**Check if already configured:**
1. Read the detected client's config file
2. Look for `octoparse` entry:
   - In `mcpServers` (Claude/Cursor/Gemini/Qwen)
   - In `servers` (VS Code/TRAE)
   - In `mcp.servers` with `command` field (OpenClaw)
3. If found:
   - **OAuth**: Try calling `get_user_account_info()`
   - **API Key**: Check if `headers.x-api-key` is set, then test connection
4. **If test succeeds:** Already configured and authorized, inform user and EXIT
5. **If test fails:** Configuration exists but invalid, proceed to reconfigure

### Step 3: Choose Authentication Method

Ask the user to choose:
- **1. OAuth 2.1** - Browser login (recommended for interactive use)
- **2. API Key** - Direct API key (for automated/headless environments)

If user cannot decide, recommend OAuth 2.1 for interactive use.

---

## Path A: OAuth 2.1 Authentication

### Step A1: Add MCP Server Configuration

Configure based on the detected client. Use the appropriate format below:

**For Claude Code / Cursor / Gemini CLI / Qwen Code** (uses `mcpServers`):
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

**For VS Code** (in `.vscode/mcp.json`, uses `servers`):
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

**For TRAE** (in `.trae/mcp.json`, uses `servers`):
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

**For OpenClaw** (uses stdio transport with mcporter):
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

Re-initialize the MCP connection to apply changes.

### Step A2: OAuth Authorization

1. Execute `/mcp` command and select "octoparse" server
2. Guide user through browser login if prompted
3. Wait for authorization callback to complete
4. Verify by calling `get_user_account_info()`

**Success:** Proceed to Completion Confirmation

**Failure handling:**
- **1st failure:** Inform user, ask to check browser and retry
- **2nd failure:** Check network connectivity, ensure no firewall blocking
- **3rd failure:** Offer fallback to API Key authentication:
  > "OAuth authorization unsuccessful after 3 attempts. Would you like to try API Key authentication instead?"

---

## Path B: API Key Authentication

### Step B1: Obtain API Key

Instruct user to:
1. Go to: https://www.octoparse.com/console/account-center/api-keys
2. Log in to their Octoparse account
3. Click "Create API Key"
4. Copy the API Key and provide it to you

**If user doesn't have Octoparse account:**
- Provide sign-up link: https://www.octoparse.com
- Wait for account creation and API key generation

**If user cannot access API keys page:**
- Check if user's subscription plan includes API access
- Suggest contacting Octoparse support

### Step B2: Configure MCP Server

Configure based on the detected client with API Key:

**For Claude Code / Cursor / Gemini CLI / Qwen Code** (uses `mcpServers`):
```json
{
  "mcpServers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "USER_PROVIDED_API_KEY"
      }
    }
  }
}
```

**For VS Code** (in `.vscode/mcp.json`, uses `servers`):
```json
{
  "servers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "USER_PROVIDED_API_KEY"
      }
    }
  }
}
```

**For TRAE** (in `.trae/mcp.json`, uses `servers`):
```json
{
  "servers": {
    "octoparse": {
      "type": "http",
      "url": "https://mcp.octoparse.com",
      "headers": {
        "x-api-key": "USER_PROVIDED_API_KEY"
      }
    }
  }
}
```

**For OpenClaw** (requires mcporter with API key):
```bash
# First configure mcporter with API key
mcporter config add octoparse https://mcp.octoparse.com
mcporter config set octoparse header.x-api-key "USER_PROVIDED_API_KEY"
```

Then add to OpenClaw config:
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

Replace `USER_PROVIDED_API_KEY` with the actual key.

Re-initialize the MCP connection to apply changes.

### Step B3: Verify Authentication

Test by calling `get_user_account_info()`.

**Success:** Proceed to Completion Confirmation

**Failure handling:**
- **1st failure (401/403):** Ask user to verify API key is copied correctly
- **2nd failure:** Ask user to check if API key is active in their account
- **3rd failure:**
  - Check API key format (should start with `op_sk_`)
  - Verify network connectivity to https://mcp.octoparse.com
  - Suggest regenerating API key at https://www.octoparse.com/console/account-center/api-keys
  - If still failing, inform user and exit with error

---

## Completion Confirmation

Once setup is complete, confirm:
1. **Configuration successful:** "Octoparse MCP server configured for [CLIENT] with [AUTH_METHOD]"
2. **Capability unlocked:** User can now use other Octoparse skills
3. **Resume original request:** If this was triggered by another skill, signal that the original request can proceed

Example confirmation message:
> ✅ Octoparse MCP server is now configured for **Claude Code** with **OAuth 2.1** authentication. You can now use Octoparse tools to manage scraping tasks.

---

## Troubleshooting

### General Issues

| Issue | Solution |
|-------|----------|
| "Cannot connect to MCP server" | Verify URL: `https://mcp.octoparse.com` and type: `http` |
| "401 Unauthorized" / "403 Forbidden" | API key invalid or expired; verify at https://www.octoparse.com/console/account-center/api-keys |
| "Authorization timeout" | Ask user to check browser and complete login; check firewall settings |
| "Transport not supported" | Use `type: "http"` for HTTP Streamable transport |
| Configuration format error | Ensure using correct structure: `mcpServers` for Claude/Cursor/Gemini/Qwen, `servers` for VS Code/TRAE |
| Client detection failed | Ask user explicitly: "Which IDE/editor are you using?" |

### Client-Specific Issues

Read the appropriate reference file for detailed client-specific troubleshooting:
- Claude Code → [references/claude-code.md](references/claude-code.md)
- Cursor → [references/cursor.md](references/cursor.md)
- VS Code → [references/vs-code.md](references/vs-code.md)
- Gemini CLI → [references/gemini-cli.md](references/gemini-cli.md)
- Qwen Code → [references/qwen-code.md](references/qwen-code.md)
- TRAE → [references/trae.md](references/trae.md)
- OpenClaw → [references/openclaw.md](references/openclaw.md)

### Switching Authentication Methods

- **OAuth → API Key:** Remove OAuth authorization from config, follow Path B
- **API Key → OAuth:** Remove API key from headers, follow Path A

### Emergency Fallback

If all configuration attempts fail:
1. Check Octoparse service status: https://status.octoparse.com
2. Verify network connectivity: `curl -I https://mcp.octoparse.com`
3. Try using Octoparse web interface directly: https://www.octoparse.com
4. Contact Octoparse support: support@octoparse.com
