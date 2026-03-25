---
name: octoparse-mcp-setup
description: Configure and authorize the Octoparse MCP server. Use when the Octoparse MCP server is not configured or needs authorization. Supports both OAuth 2.1 and API Key authentication methods.
---

## Overview

This skill handles the one-time setup required for all Octoparse skills. It configures the MCP server with your choice of authentication method:
1. **OAuth 2.1** - Dynamic client registration with browser login
2. **API Key** - Direct API key authentication

## When to use

Use this skill when:
- Octoparse MCP server is not detected in the system
- User receives "MCP server not found" or connection errors
- Authorization is required before using Octoparse tools
- Any Octoparse skill fails due to missing MCP configuration

## Authentication Methods

You must choose ONE authentication method (cannot use both simultaneously):

### Option 1: OAuth 2.1 (Recommended for most users)
- Browser-based login to your Octoparse account
- Automatic token management
- Best for interactive use

### Option 2: API Key (For automated/headless environments)
- Direct API key authentication
- No browser interaction required
- Best for scripts and automated workflows

## Instructions

### Step 1: Check Current MCP Status

First, verify if Octoparse MCP server is already configured:
- Check if `octoparse` MCP server exists in the system
- If already configured and authorized, inform user and exit

### Step 2: Choose Authentication Method

**Ask the user to choose one authentication method:**

```
Please choose an authentication method for Octoparse MCP server:

1. OAuth 2.1 - Login via browser (recommended for most users)
2. API Key - Use direct API key authentication

Which would you prefer? (Enter 1 or 2)
```

**Wait for user response** and proceed with the selected method below.

---

## Path A: OAuth 2.1 Authentication

### Step A1: Add MCP Server Configuration

If Octoparse MCP is not configured:

1. **Add the MCP server** using the appropriate configuration method:
   ```json
   {
     "mcpServers": {
       "octoparse": {
         "url": "https://mcp.octoparse.com"
       }
     }
   }
   ```

2. **Re-initialize the MCP connection** to apply the new configuration

3. **Confirm addition** - Verify the server now appears in the MCP server list

### Step A2: OAuth 2.1 Authorization (Dynamic Client Registration)

**CRITICAL: Authorization must be completed before using any Octoparse tools.**

1. **Initiate authorization flow**:
   - Execute the `/mcp` command to open the MCP server selection menu
   - Instruct the user to select the "octoparse" server from the list

2. **Guide through OAuth flow**:
   - The system will automatically handle dynamic client registration
   - If a browser window opens, instruct the user to complete login in the browser
   - Wait for the authorization callback to complete

3. **Verify authorization**:
   - Attempt to call `get_user_account_info()` to confirm connection is working
   - If successful, authorization is complete

4. **Handle failures**:
   - If authorization fails, report the specific error
   - Do not proceed until authorization succeeds

---

## Path B: API Key Authentication

### Step B1: Obtain API Key (User Action Required)

**Instruct the user to get their API Key:**

1. Go to: https://www.octoparse.com/console/account-center/api-keys
2. Log in to your Octoparse account if not already logged in
3. Click "Create API Key" (or similar button)
4. Copy the generated API Key

**Wait for the user to provide their API Key.**

### Step B2: Configure MCP Server with API Key

Once the user provides their API Key:

1. **Add the MCP server with API Key header**:
   ```json
   {
     "mcpServers": {
       "octoparse": {
         "url": "https://mcp.octoparse.com",
         "headers": {
           "x-api-key": "{USER_PROVIDED_API_KEY}"
         }
       }
     }
   }
   ```

   **IMPORTANT**: Replace `{USER_PROVIDED_API_KEY}` with the actual API key provided by the user.

2. **Re-initialize the MCP connection** to apply the new configuration

3. **Confirm addition** - Verify the server now appears in the MCP server list

### Step B3: Verify API Key Authentication

1. **Test the connection**:
   - Attempt to call `get_user_account_info()` to confirm connection is working
   - If successful, API key authentication is complete

2. **Handle failures**:
   - If authentication fails with 401/403 errors, the API key may be invalid or expired
   - Ask the user to:
     - Verify the API key is copied correctly
     - Check if the API key is active in their account
     - Generate a new API key if needed
   - Do not proceed until authentication succeeds

---

## Completion Confirmation

Once setup is complete:

1. **Confirm the authentication method used**:
   - For OAuth: "Octoparse MCP server is now configured with OAuth 2.1 authorization"
   - For API Key: "Octoparse MCP server is now configured with API Key authentication"

2. **Inform user they can now use other Octoparse skills**

3. **If this was triggered by another skill, signal that the original request can proceed**

## Configuration Reference

### OAuth 2.1 Configuration

| Service | URL | Protocol |
|---------|-----|----------|
| Octoparse | `https://mcp.octoparse.com` | OAuth 2.1 with Dynamic Client Registration |

**Authorization Details:**
- **Protocol**: OAuth 2.1
- **Client Registration**: Dynamic (automatic)
- **User Action Required**: Browser login to Octoparse account
- **Scope**: Full Octoparse API access

### API Key Configuration

| Service | URL | Protocol |
|---------|-----|----------|
| Octoparse | `https://mcp.octoparse.com` | API Key Authentication |

**API Key Details:**
- **Header Name**: `x-api-key`
- **Header Value**: User's API key from https://www.octoparse.com/console/account-center/api-keys
- **User Action Required**: Create and copy API key from account center
- **Scope**: Full Octoparse API access

## Troubleshooting

### OAuth 2.1 Issues

| Issue | Solution |
|-------|----------|
| "Cannot connect to MCP server" | Verify URL is correct: `https://mcp.octoparse.com` |
| "Authorization timeout" | Ask user to check browser and complete login |
| "Dynamic registration failed" | Retry authorization flow from Step A2 |
| "Already authorized" | Skip authorization, configuration is complete |

### API Key Issues

| Issue | Solution |
|-------|----------|
| "401 Unauthorized" or "403 Forbidden" | API key is invalid or expired; ask user to verify or regenerate at https://www.octoparse.com/console/account-center/api-keys |
| "Cannot connect to MCP server" | Verify URL is correct: `https://mcp.octoparse.com` |
| "Missing x-api-key header" | Ensure the header is configured exactly as: `"x-api-key": "your-api-key"` |
| "API key not working" | Verify the key is active in the user's Octoparse account center |

## Migration Between Methods

To switch authentication methods:

1. **OAuth → API Key**:
   - Remove OAuth authorization
   - Follow Path B (API Key) steps

2. **API Key → OAuth**:
   - Remove the API key from MCP configuration
   - Follow Path A (OAuth 2.1) steps
