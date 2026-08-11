# Client-specific configuration

Read this only when a symptom is specific to one client. The endpoint and transport are
identical everywhere — `https://mcp.octoparse.com` over HTTP — so the only things that
differ are where the config file lives, what the wrapper key is called, and a handful of
per-client quirks.

## Where the config lives

| Client | File | Wrapper key |
|---|---|---|
| Claude Code | `~/.claude.json` (written by `claude mcp add`), or `.claude/settings.json` per project | `mcpServers` |
| Cursor | `~/.cursor/mcp.json`, or `.cursor/mcp.json` per project | `mcpServers` |
| Gemini CLI | `~/.gemini/settings.json`, or `.gemini/settings.json` | `mcpServers` |
| Qwen Code | `~/.qwen/settings.json`, or `.qwen/settings.json` | `mcpServers` |
| VS Code | `.vscode/mcp.json` (preferred), or user settings | `servers` in the file; `mcp.servers` in settings |
| TRAE | Settings → MCP (preferred), or `.trae/mcp.json` | `servers` |
| OpenClaw | `~/.openclaw/openclaw.json`, `.json5`, or `.yaml` | `mcp.servers`, launched through `mcporter` |

The entry itself is the same in every `mcpServers` / `servers` client:

```json
{
  "octoparse": {
    "type": "http",
    "url": "https://mcp.octoparse.com"
  }
}
```

Windows paths substitute `%USERPROFILE%` for `~` (`%APPDATA%` for OpenClaw).

## Per-client quirks

### Cursor

- **Tool ceiling of roughly 40 active tools.** Octoparse contributes 11. If other servers
  push the total past the ceiling, Octoparse tools silently stop appearing — disable
  another server rather than reconfiguring this one.
- **Agent Mode must be on.** MCP tools are unavailable in Ask Mode.
- Requires Cursor v0.40 or later.

### VS Code

- Prefer `.vscode/mcp.json` with the `servers` key. User and workspace settings use a
  nested `mcp.servers` object instead — mixing the two shapes is the most common failure.
- Supports secure input variables for credentials, which is the right place for an API key
  in this client.
- Dev containers need the server declared inside the container config, not only on the
  host.

### TRAE

- The Settings → MCP panel is the supported path; `.trae/mcp.json` works but is
  community-discovered rather than documented.
- Has a built-in MCP Market — check whether Octoparse is listed there before editing files
  by hand.

### Gemini CLI and Qwen Code

These two behave nearly identically.

- **Trust mode** may need to be granted before tools are callable.
- **Tool filtering** can allow- or deny-list individual tools per server. If only some
  Octoparse tools appear, check the filter before assuming a connection problem.
- Timeout is configurable per server; raise it if long-running `execute_task` calls are
  cut off.

### OpenClaw

- Connects through `mcporter` rather than talking to the endpoint directly, so the server
  entry is a `command` invocation.
- Accepts JSON, JSON5, or YAML. JSON5 allows comments, which is useful when several
  servers share a file.
- If tools do not appear, verify `mcporter` itself resolves the server before touching
  OpenClaw's config.

## Diagnosis order

Symptoms look alike across clients, so work in this order rather than jumping to the
client-specific notes:

1. **No `mcp__octoparse__*` tools at all** — not registered, or the client was not
   restarted after registering. Restart first; it resolves most of these.
2. **Tools present, every call returns 401/403** — registered but not authorized. Run
   `/mcp`, or have the user add an API key to their own config.
3. **Some tools missing, others working** — tool filtering (Gemini, Qwen) or the tool
   ceiling (Cursor). Not a connection problem.
4. **Worked yesterday, fails today** — an expired OAuth session or a rotated API key.
   Re-authorize before reconfiguring.

Only after ruling those out is a client-specific quirk the likely cause.
