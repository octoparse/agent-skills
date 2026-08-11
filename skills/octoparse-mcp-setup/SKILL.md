---
name: octoparse-mcp-setup
description: Connect and authorize the Octoparse MCP server. Use when Octoparse tools are missing or unavailable, when a call fails with an authorization or 401/403 error, when the user asks to set up or reconnect Octoparse, or when another Octoparse skill cannot reach the service.
---

# Octoparse MCP setup

Gets `search_templates`, `execute_task`, `export_data` and the rest reachable. Once they
respond, hand back to `octoparse-ultimate-scraper`.

## Start here: is configuration even needed?

**If this repository is installed as a plugin, the server is already declared** — the
plugin ships `mcp.json` (Agent Plugins spec) and `.mcp.json` (Claude Code), both pointing
at `https://mcp.octoparse.com`. The client wires it up on install. Configuration is not
the problem; **authorization** almost always is.

Check in this order:

1. **Are the tools present at all?** If `mcp__octoparse__*` tools are absent, the server
   is not registered — go to [Register the server](#register-the-server).
2. **Do they respond?** Call `search_tasks()`. Success means everything is working; say so
   and stop.
3. **Does it fail with 401 / 403 / an authorization prompt?** The server is registered but
   not authorized — go to [Authorize](#authorize).

Do not reconfigure a server that is already registered. Re-registering does not fix an
authorization failure and usually creates a duplicate entry.

## Register the server

Only needed when the plugin is not installed, or the client does not read plugin-provided
MCP configuration.

**CLI (fastest, Claude Code):**

    claude mcp add --transport http octoparse https://mcp.octoparse.com

**By hand** — the endpoint and transport are the same everywhere; only the wrapper key
differs:

| Client | File | Key |
|---|---|---|
| Claude Code, Cursor, Gemini CLI, Qwen Code | `~/.claude.json`, `~/.cursor/mcp.json`, `~/.gemini/settings.json`, `~/.qwen/settings.json` | `mcpServers` |
| VS Code, TRAE | `.vscode/mcp.json`, `.trae/mcp.json` | `servers` |
| OpenClaw | `~/.config/openclaw/openclaw.json5` | `mcp.servers`, via `mcporter` |

```json
{
  "octoparse": {
    "type": "http",
    "url": "https://mcp.octoparse.com"
  }
}
```

**Newly registered servers do not appear in the running session.** Restart the client
before expecting the tools. Tell the user this explicitly — otherwise a correct setup
looks like a failure.

## Authorize

Two methods. OAuth for interactive use, API key for headless.

### OAuth (recommended)

1. Run `/mcp` and select `octoparse`.
2. Complete the browser login.
3. Verify with `search_tasks()`.

Failure handling, in order:

- **1st** — ask the user to check for an unfinished browser tab and retry.
- **2nd** — check network reachability: `curl -I https://mcp.octoparse.com`.
- **3rd** — stop retrying and offer the API key path.

### API key

For CI, headless environments, or when OAuth fails three times.

1. Create a key at https://www.octoparse.com/console/account-center/api-keys
2. Add it as a header on the existing server entry:

```json
{
  "octoparse": {
    "type": "http",
    "url": "https://mcp.octoparse.com",
    "headers": { "x-api-key": "USER_PROVIDED_API_KEY" }
  }
}
```

3. Restart the client, then verify with `search_tasks()`.

**Do not put an API key in the plugin's own `mcp.json` or `.mcp.json`.** Those files are
distributed package data, and the Agent Plugins specification forbids credentials in
`headers`. A key belongs in the user's own client configuration, never in the repository.

Failure handling:

- **1st (401/403)** — verify the key was copied whole, with no whitespace.
- **2nd** — confirm the key is still active in the account console.
- **3rd** — regenerate the key. If it still fails, check whether the plan includes API
  access and stop.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| No `mcp__octoparse__*` tools | not registered, or client not restarted | register, then restart |
| Tools present, every call 401/403 | registered but not authorized | run `/mcp`, or add an API key |
| "Transport not supported" | wrong transport | `type: "http"` for Claude-family, `streamable-http` in Agent Plugins `mcp.json` |
| Config edited, nothing changed | session caches MCP config at startup | restart, or `/reload-plugins` |
| Works in one client, not another | wrapper key differs | `mcpServers` vs `servers` — see the table above |
| Two `octoparse` entries | re-registered instead of authorizing | remove the duplicate, keep one |

Client-specific detail lives in `references/` — read one only when the symptom is
specific to that client:
[claude-code](references/claude-code.md) ·
[cursor](references/cursor.md) ·
[vs-code](references/vs-code.md) ·
[gemini-cli](references/gemini-cli.md) ·
[qwen-code](references/qwen-code.md) ·
[trae](references/trae.md) ·
[openclaw](references/openclaw.md)

If everything fails: check https://status.octoparse.com, then contact support@octoparse.com.

## When it works

Confirm which client and which auth method, then hand back:

> Octoparse MCP is connected and authorized. You can now ask for the data you need —
> `octoparse-ultimate-scraper` will pick the template and run it.
