---
title: "Authentication"
aliases:
  - "authentication"
  - "Authentication"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/authentication"
status: "verified"
last_updated: "2026-10"
---

# Authentication

## Executive Summary
> Log in to Claude Code and configure authentication for individuals, teams, and organizations.

## Technical Mechanics & Documentation

Claude Code supports multiple authentication methods depending on your setup. Individual users can log in with a claude.ai account, while teams can use Claude for Teams or Enterprise, the Claude Console, or a cloud provider like Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry.

## Log in to Claude Code

After [[Advanced_setup|installing Claude Code]], run `claude` in your terminal. On first launch, Claude Code opens a browser window for you to log in. If you've set the `ANTHROPIC_API_KEY` environment variable and you approve the key when Claude Code asks whether to use it, Claude Code skips the login prompt.

If the browser doesn't open automatically, press `c` to copy the login URL to your clipboard, then paste it into your browser.

If your browser shows a login code instead of redirecting back after you sign in, paste it into the terminal at the `Paste code here if prompted` prompt. This happens when the browser can't reach Claude Code's local callback server, which is common in WSL2, SSH sessions, and containers.

When login completes, the terminal shows `Login successful` and prompts you to press `Enter` to continue.

You can authenticate with any of these account types:

* **Claude Pro or Max subscription**: log in with your claude.ai account. Subscribe at [claude.com/pricing](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_pro_max).
* **Claude for Teams or Enterprise**: log in with the claude.ai account your team admin invited you to.
* **Claude Console**: log in with your Console credentials. Your admin must have [invited you](#claude-console-authentication) first. You can sign in with or without [creating an API key](#sign-in-without-an-api-key).
* **Cloud providers**: if your organization uses [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock]], [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform]], or [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry]], set the required environment variables before running `claude`, or select **3rd-party platform** at the login prompt, which launches an interactive setup wizard for Bedrock and Vertex AI. No browser login is needed.
* **Cloud gateway**: if your organization runs a self-hosted [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]], sign in with corporate SSO through `/login`. The gateway-issued token is the session's only credential.

Admins can direct which login method developers use and require claude.ai logins to belong to a specific organization; see [Restrict login to your organization](#restrict-login-to-your-organization).

To log out and re-authenticate, type `/logout` at the Claude Code prompt. Logging out also resets your first-launch setup state, so the next time you run `claude` it walks you through login and setup again.

If you're having trouble logging in, see [[Troubleshoot_installation_and_login|authentication troubleshooting]].

### Log in with multiple accounts

To stay signed in to multiple accounts at once, such as work and personal accounts, give each account its own configuration directory. When you start `claude`, set the [[Environment_variables|`CLAUDE_CONFIG_DIR`]] environment variable to the directory for the account you want to use. Each directory has its own settings, session history, and claude.ai login or API key. For example, in Bash or Zsh, add this alias to `~/.bashrc` or `~/.zshrc` so that `claude-work` uses your work account while `claude` keeps your personal one:

```bash theme={null}
alias claude-work='CLAUDE_CONFIG_DIR=~/.claude-work claude'
```

After you open a new terminal and run `claude-work` for the first time, Claude Code walks you through login and setup for the new directory. Separate directories don't keep two Claude Console sign-ins [without an API key](#sign-in-without-an-api-key) apart, because Claude Code stores that kind of sign-in outside the configuration directory.

## Set up team authentication

For teams and organizations, you can configure Claude Code access in one of these ways:

* [Claude for Teams or Enterprise](#claude-for-teams-or-enterprise), recommended for most teams
* [Claude Console](#claude-console-authentication)
* [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]], a self-hosted gateway that signs developers in with your IdP and routes inference to the cloud provider you configure
* [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock]]
* [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform]]
* [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry]]

### Claude for Teams or Enterprise

[Claude for Teams](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_teams#team-&-enterprise) and [Claude for Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_enterprise) provide the best experience for organizations using Claude Code. Team members get access to both Claude Code and Claude on the web with centralized billing and team management.

* **Claude for Teams**: self-service plan with collaboration features, admin tools, SSO, billing management, and [[Configure_server-managed_settings|server-managed settings]] for organization-wide Claude Code configuration. Best for smaller teams.
* **Claude for Enterprise**: adds domain capture, role-based permissions, and the compliance API. Best for larger organizations with security and compliance requirements.

<Steps>
  <Step title="Subscribe">
    Subscribe to [Claude for Teams](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_teams_step#team-&-enterprise) or contact sales for [Claude for Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_enterprise_step).
  </Step>

  <Step title="Invite team members">
    Invite team members from the admin dashboard.
  </Step>

  <Step title="Install and log in">
    Team members install Claude Code and log in with their claude.ai accounts.
  </Step>
</Steps>

### Claude Console authentication

For organizations that prefer API-based billing, you can set up access through the Claude Console.

<Steps>
  <Step title="Create or use a Console account">
    Use your existing Claude Console account or create a new one.
  </Step>

  <Step title="Add users">
    You can add users through either method:

    * Bulk invite users from within the Console: Settings -> Members -> Invite
    * [Set up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)
  </Step>

  <Step title="Assign roles">
    When inviting users, assign one of:

    * **Claude Code** role: users can only create Claude Code API keys
    * **Developer** role: users can create any kind of API key
  </Step>

  <Step title="Users complete setup">
    Each invited user needs to:

    * Accept the Console invite
    * [[Advanced_setup|Check system requirements]]
    * [[Advanced_setup|Install Claude Code]]
    * Log in with Console account credentials
  </Step>
</Steps>

#### Sign in without an API key

You can sign in to your Console account without creating an API key, even when your organization doesn't let developers create them. Choose the Anthropic Console account at the `/login` prompt and Claude Code asks how you want to sign in. Requires Claude Code v2.1.242 or later. Both routes sign you in to Console in the browser and differ in what Claude Code stores afterwards:

* **Sign in with your Console account**, labeled `(recommended)`: Claude Code keeps the OAuth token from that sign-in and stores it as an [Anthropic profile](#anthropic-profiles-and-federation-credentials). It creates no API key
* **Create an API key**, labeled `(legacy)`: Claude Code creates a Console API key for you and stores it with your other credentials

In practice, the profile stores an OAuth login while an API key is a static credential: Claude Code refreshes the profile's login automatically, and when refresh fails, requests fail with [[Error_reference|Anthropic profile login expired]] until you sign in again.

You don't get the choice on every machine. Claude Code creates an API key without asking in these cases:

* You run against a cloud provider, such as [[Enterprise_deployment_overview|Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry]] or [[Claude_Code_on_Claude_Platform_on_AWS|Claude Platform on AWS]]
* Any settings file sets [`forceLoginOrgUUID`](#restrict-login-to-your-organization), or sets `forceLoginMethod` to `"claudeai"` or `"console"`
* A managed settings source on your machine, such as the managed settings file, an MDM profile, or the cached server-managed settings, exists but Claude Code [[Deploy_managed_settings|can't read it]] and no other managed source supplies a policy

Unset `ANTHROPIC_API_KEY` before you sign in without a key.

After you sign in without a key, you have a profile instead of a stored API key:

* **Which profile it writes**: Claude Code writes the profile named by `ANTHROPIC_PROFILE`, or your active profile, or `default`. If that profile is a federation profile, Claude Code refuses the sign-in instead of overwriting it
* **What it signs you out of**: Claude Code signs you out of any claude.ai login stored on the machine
* **How to undo it**: run `/logout`, which removes and revokes the credential this sign-in wrote

If your organization uses [[Configure_server-managed_settings|server-managed settings]], they apply to this sign-in on Claude Code v2.1.257 or later.

Everything else about profiles applies to this sign-in, including where it ranks against your other credentials, the `Profile` row you get in `/status`, and the features that need a claude.ai login. See [Anthropic profiles and federation credentials](#anthropic-profiles-and-federation-credentials).

### Cloud provider authentication

For teams using Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry:

<Steps>
  <Step title="Follow provider setup">
    Follow the [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock docs]], [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform docs]], or [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry docs]].
  </Step>

  <Step title="Distribute configuration">
    Distribute the environment variables and instructions for generating cloud credentials to your users. Read more about how to [[Settings_files_and_precedence|manage configuration here]].
  </Step>

  <Step title="Install Claude Code">
    Users can [[Advanced_setup|install Claude Code]].
  </Step>
</Steps>

### Restrict login to your organization

To require that developers' claude.ai logins belong to a specific Anthropic organization, set [[All_settings|`forceLoginMethod`]] and [[All_settings|`forceLoginOrgUUID`]] in [[Deploy_managed_settings|managed settings]]. Set `forceLoginOrgUUID` to your organization ID, shown in [claude.ai admin settings](https://claude.ai/admin-settings/organization) for Claude for Teams or Enterprise organizations. Claude Code reports an error for a claude.ai login to any other organization and exits at startup if the claude.ai credential in use belongs to an organization that isn't listed.

For Claude Console logins, Claude Code uses `forceLoginOrgUUID` to pre-select the organization on the Console sign-in page when you set it to a single Console organization ID, shown at [platform.claude.com/settings/organization](https://platform.claude.com/settings/organization). It doesn't check which organization the resulting Console credential belongs to, at login or at startup. A developer who logged in with a Console account before you deployed the keys stays logged in, and that saved key is blocked on a machine that also requires the [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|gateway]] sign-in or in a session that selects a cloud provider.

If you set `forceLoginOrgUUID` in any settings file, Claude Code stops offering the [keyless Console sign-in](#sign-in-without-an-api-key) in the sessions that file applies to and creates an API key instead. To direct developers to claude.ai sign-in instead, set `forceLoginMethod` to `"claudeai"`.

On Claude Code v2.1.212 or later, every login path listed here applies `forceLoginMethod`. On the terminal's interactive login screen, reached by `/login` or first-run onboarding, Claude Code pre-selects a `claudeai` or `console` method without enforcing it, so even with `forceLoginMethod` set to `"claudeai"`, a developer can still complete a Console login there.

The paths differ on `forceLoginOrgUUID`:

* **Terminal, [[Use_Claude_Code_in_VS_Code|VS Code extension]], and Agent SDK logins**: verify `forceLoginOrgUUID` for claude.ai account logins
* **`claude setup-token` and `/install-github-app`**: enforce only `forceLoginMethod`, so they can mint a token in a different organization
* **[[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Gateway]] sign-in**: selected by `forceLoginMethod: "gateway"` rather than restricted by it, and doesn't authenticate against an Anthropic organization, so `forceLoginOrgUUID` doesn't apply; use your gateway identity provider to restrict access

Deploy the keys through your device management tooling. [[Configure_server-managed_settings|Server-managed settings]] reach only accounts that are already authenticated into your organization, so they can't redirect a developer's first login. If your organization distributes server-managed settings as well, set the keys in both places: managed-settings sources [[Configure_server-managed_settings|don't merge]], and cached server-managed settings replace the device-managed file apart from a few [[Configure_server-managed_settings|per-key exceptions]]. `forceLoginOrgUUID` and the `"claudeai"` and `"console"` values of `forceLoginMethod` aren't among those exceptions, so keep them in both places.

In a [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|gateway]] deployment, also keep `forceLoginMethod` and `forceLoginOrgUUID` out of the [[Claude_apps_gateway_configuration|settings the gateway serves]].

The keys also decide whether a session that doesn't use a login credential can start. See [[All_settings|`forceLoginOrgUUID`]] in the settings reference for the full behavior.

* **`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper`**: blocked at startup. Under `forceLoginOrgUUID`, organization membership can't be verified for an environment credential, and under `forceLoginMethod` the credential would stand in for the required sign-in. When the managed settings also require the [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|gateway]] sign-in, Claude Code blocks an API key saved by an earlier Claude Console login the same way. See [[Error_reference|Administrator policy requires a Cloud gateway sign-in]]
* **Cloud provider sessions such as Amazon Bedrock**: blocked only while an `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` credential, or an API key saved by an earlier Claude Console login, is still present on the machine. Remove it and the session starts. These sessions authenticate against your cloud provider, whose access policies govern them
* **[Anthropic profile or federation credentials](#anthropic-profiles-and-federation-credentials)**: not blocked unless an `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` credential, or an API key saved by an earlier Claude Console login, is also present on the machine. The keys don't check which organization the profile belongs to

### Restrict which API providers a machine may use

[[All_settings|`allowedProviders`]] in [[Deploy_managed_settings|managed settings]] lists which services a managed machine may reach Claude through, such as the Anthropic API, Amazon Bedrock, or an LLM gateway. It complements `forceLoginMethod` and `forceLoginOrgUUID`, which govern which account a session uses when it talks to Anthropic. Requires Claude Code v2.1.285 or later.

```json managed-settings.json theme={null}
{
  "forceLoginMethod": "claudeai",
  "forceLoginOrgUUID": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"],
  "allowedProviders": ["anthropic", "bedrock"]
}
```

With this file, a developer signed in to your claude.ai organization or configured for Amazon Bedrock starts normally. A session set up for any other provider is refused at startup, and a running session that switches to one is refused on its next request. [[Error_reference|Managed settings don't allow this API provider]] shows each message.

* **Allow an LLM gateway or proxy**: list `"customEndpoint"` and set the gateway's URL in the managed `env` block of the same source. The [[All_settings|settings reference]] lists every value and says which endpoint variables need a managed `env` pin.
* **Deploy on managed machines**: put the list in the managed source that carries the rest of your policy. The entry's [[All_settings|Scope note]] says how a server-managed list combines with it.
* **Server-managed settings only**: a list you set only in [[Configure_server-managed_settings|server-managed settings]] reaches only sessions that fetch your organization's settings, so treat it as a convenience for machines you can't reach with device management, not as enforcement. [[Configure_server-managed_settings|Platform availability]] lists which sessions fetch them.

## Credential management

Claude Code securely manages your authentication credentials:

* **Storage location**:
  * On macOS, credentials are stored in the encrypted macOS Keychain. When the Keychain rejects the write, such as when it's locked in an SSH session, Claude Code stores your login in `~/.claude/.credentials.json` with file mode `0600` instead, the same storage it uses on Linux. A Console login that creates an API key fails until the Keychain is writable. To move your login back into the Keychain, follow [[Troubleshoot_installation_and_login|the recovery steps]].
  * On Linux, credentials are stored in `~/.claude/.credentials.json` with file mode `0600`.
  * On Windows, credentials are stored in `%USERPROFILE%\.claude\.credentials.json` and inherit the access controls of your user profile directory, which restricts the file to your user account by default.
  * If you've set the `CLAUDE_CONFIG_DIR` environment variable, Claude Code keeps the `.credentials.json` file under that directory instead, including the file the macOS fallback writes, and keys the macOS Keychain entry to that directory too, so a session with a different `CLAUDE_CONFIG_DIR` reads a different entry.
  * Claude Code manages `.credentials.json` through `/login` and `/logout`. To route requests through a custom API endpoint, set the [[Environment_variables|`ANTHROPIC_BASE_URL`]] environment variable instead.
* **Supported authentication types**: claude.ai credentials, Claude API credentials, Microsoft Foundry Auth, Bedrock Auth, Vertex Auth, Anthropic profile and [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) credentials, and [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] session tokens.
* **Custom credential scripts**: configure the [[All_settings|`apiKeyHelper`]] setting to run a shell script that returns an API key.
* **Refresh intervals**: see [[All_settings|`apiKeyHelper`]] for the cases in which Claude Code re-runs the helper.
* **Slow helper notice**: if `apiKeyHelper` takes longer than 10 seconds to return a key, Claude Code displays a warning notice in the prompt bar showing the elapsed time. If you see this notice regularly, check whether your credential script can be optimized.
* **Helper failures**: when the script exits with an error, times out, or prints nothing, requests fail with [[Error_reference|`Your apiKeyHelper script is failing`]] within three attempts.

`apiKeyHelper`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_AUTH_TOKEN` apply to the CLI and the surfaces that wrap it, including the VS Code extension, the Agent SDK, and GitHub Actions. Claude Desktop and cloud sessions do not call `apiKeyHelper` or read these environment variables: they use OAuth, except desktop sessions running a [[Connect_Claude_Code_to_an_LLM_gateway|third-party inference configuration]], which authenticate with that configuration's credential.

### Renew an expiring login

When the login you created with `/login` is within three days of expiring, Claude Code shows a warning at startup: `Your login expires in 3 days · run /login to renew`.

Run `/login` to renew. The warning is informational and never blocks a request: authentication keeps working until the login actually expires.

Once the stored login expires and can't be refreshed, each model request fails with [[Error_reference|`Login expired · Please run /login`]] until you sign in again.

You can check for this state before a request fails: [[Commands|`/status`]] shows a `Login` row reading `Expired — log in again`, plus the organization and email it has saved for the expired login. The row appears only when the saved claude.ai login is the active credential. The row requires Claude Code v2.1.210 or later.

The warning appears only when a claude.ai login is the active credential, and not when a cloud provider, `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` supplies the credential.

Renewing early matters most for sessions that run unattended. A [[Manage_multiple_agents_with_agent_view|background session in agent view]] or a [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] session that outlives the login stops making progress once the credential expires and can't recover until you sign in again.

### Authentication precedence

When multiple credentials are present, Claude Code chooses one in this order:

1. Cloud provider credentials, when `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, or `CLAUDE_CODE_USE_FOUNDRY` is set. See [[Enterprise_deployment_overview|third-party integrations]] for setup.
2. `ANTHROPIC_AUTH_TOKEN` environment variable. Sent as the `Authorization: Bearer` header. Use this when routing through an [[Other_LLM_gateways|LLM gateway or proxy]] that authenticates with bearer tokens rather than Anthropic API keys.
3. `ANTHROPIC_API_KEY` environment variable. Sent as the `X-Api-Key` header. Use this for direct Anthropic API access with a key from the [Claude Console](https://platform.claude.com). In interactive mode, you are prompted once to approve or decline the key, and your choice is remembered. To change it later, use the "Use custom API key" toggle in `/config`. The toggle only appears while `ANTHROPIC_API_KEY` is set in your environment. In non-interactive mode (`-p`), the key is always used when present.
4. [[All_settings|`apiKeyHelper`]] script output. Use this for dynamic or rotating credentials, such as short-lived tokens fetched from a vault.
5. `CLAUDE_CODE_OAUTH_TOKEN` environment variable. A long-lived OAuth token generated by [`claude setup-token`](#generate-a-long-lived-token). Use this for CI pipelines and scripts where browser login isn't available. If you run `/login` while the variable is set, Claude Code switches the current session to the new login, but reads the variable again in every new session until you remove it from your shell profile or the `env` block of a [[Settings_files_and_precedence|settings file]].
6. Anthropic profile and federation credentials, the credentials that the `ant` CLI and Workload Identity Federation use. A profile that `ant auth login` wrote ranks here only when you name it in `ANTHROPIC_PROFILE`; otherwise it ranks below `/login`. See [Anthropic profiles and federation credentials](#anthropic-profiles-and-federation-credentials).
7. Subscription OAuth credentials from `/login`. This is the default for Claude Pro, Max, Team, and Enterprise users.

A signed-in [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] session sits outside this list: it is a provider selection like Amazon Bedrock or Google Cloud's Agent Platform, and it outranks them. When a gateway session exists, the CLI authenticates with the gateway token even if `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, or `CLAUDE_CODE_USE_FOUNDRY` is set, and credential sources above such as the bearer token, API key, `apiKeyHelper`, and profiles are not used.

If your machine's [[Deploy_managed_settings|managed settings]] set [[All_settings|`forceLoginMethod`]] to `"gateway"` or set [[All_settings|`forceLoginGatewayUrl`]], and you don't select a cloud provider through a variable such as `CLAUDE_CODE_USE_BEDROCK` or `CLAUDE_CODE_USE_VERTEX`, your session uses only the gateway sign-in. Claude Code skips the other credential sources and asks you to sign in with `/login`. See [[Error_reference|Administrator policy requires a Cloud gateway sign-in]] for what you see with each leftover credential. Requires Claude Code v2.1.261 or later, or v2.1.265 or later on a machine that sets only `forceLoginGatewayUrl`.

If you have an active Claude subscription but also have `ANTHROPIC_API_KEY` set in your environment, Claude Code uses the API key once you approve it. This can cause authentication failures if the key belongs to a disabled or expired organization.

Run `unset ANTHROPIC_API_KEY` to fall back to your subscription, and check `/status` to confirm which method is active. When a login and an API key are both configured, `/status` marks the credential that isn't in use.

[[Use_Claude_Code_in_the_cloud|Cloud sessions]] always use your subscription credentials. If you set `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` in the cloud environment, it doesn't override your subscription credentials.

#### Anthropic profiles and federation credentials

A profile is a named credential configuration file in your [Anthropic configuration directory](https://platform.claude.com/docs/en/manage-claude/wif-reference#configuration-directory), by default `~/.config/anthropic` on macOS and Linux or `%APPDATA%\Anthropic` on Windows. A profile's auth mode is `oidc_federation` when you set it up for [Workload Identity Federation (WIF)](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) or `user_oauth` when [`ant auth login`](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication) wrote it or you [signed in to a Console account without an API key](#sign-in-without-an-api-key).

Claude Code doesn't read profiles or federation variables in [[Run_Claude_Code_programmatically|bare mode]], in Claude Desktop, or in cloud sessions. In those sessions, `/status` shows no `Profile` row.

Claude Code checks three sources in this order and stops at the first one that is set. The table shows what sets each source and where it ranks against your `/login` credential.

| Source | Set by | Rank against `/login` |
| :- | :- | :- |
| Named profile | `ANTHROPIC_PROFILE` | Above, whichever auth mode the profile has |
| Federation variables | `ANTHROPIC_FEDERATION_RULE_ID` and `ANTHROPIC_ORGANIZATION_ID`, both set | Above |
| Active profile | The [`active_config` file](https://platform.claude.com/docs/en/manage-claude/wif-reference#active-profile) in your configuration directory, or a profile named `default` | Above when its auth mode is `oidc_federation`; below a working `/login` credential when its auth mode is `user_oauth` |

For the federation variables, Claude Code also reads the other variables in the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference#environment-variables), such as `ANTHROPIC_IDENTITY_TOKEN_FILE`, when it exchanges your identity token. For the profile file format, see the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference#profile-configuration-file).

To confirm which source Claude Code chose, run `/status`. A `Profile` row names the source in place of the `Login method` row. When the profile is the credential in use, `Organization` and `Email` rows show its account.

When a `user_oauth` profile's login has expired and Claude Code can't renew it, requests fail with [[Error_reference|Anthropic profile login expired]].

Features that need your claude.ai login, such as [[Connect_Claude_Code_to_tools_via_MCP|claude.ai connectors]] and [[Automate_work_with_routines|`/schedule`]], aren't available while one of these sources is selected. To stop Claude Code from selecting a source:

* **Named profile or federation variables**: unset `ANTHROPIC_PROFILE`, or unset either federation variable
* **Active profile**: run `/logout` for a `user_oauth` profile whose current credential you wrote by [signing in to a Console account without an API key](#sign-in-without-an-api-key), run `ant auth logout` for one whose current credential `ant auth login` wrote, or delete the profile's file from `configs/` in your configuration directory for either auth mode

### Generate a long-lived token

For CI pipelines, scripts, or other environments where interactive browser login isn't available, generate a one-year OAuth token with `claude setup-token`:

```bash theme={null}
claude setup-token
```

The command opens the same browser authorization flow as `/login`, and the token prints to the terminal after you approve access in the browser. It does not save the token anywhere; copy it and set it as the `CLAUDE_CODE_OAUTH_TOKEN` environment variable wherever you want to authenticate:

<Tabs>
  <Tab title="macOS, Linux, WSL">
    ```bash theme={null}
    export CLAUDE_CODE_OAUTH_TOKEN=your-token
    ```
  </Tab>

  <Tab title="Windows PowerShell">
    ```powershell theme={null}
    $env:CLAUDE_CODE_OAUTH_TOKEN = "your-token"
    ```
  </Tab>

  <Tab title="Windows CMD">
    ```batch theme={null}
    set CLAUDE_CODE_OAUTH_TOKEN=your-token
    ```
  </Tab>
</Tabs>

This token authenticates with your Claude subscription and requires a Pro, Max, Team, or Enterprise plan. It can only make model requests, so it can't establish [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] sessions or fetch [[Connect_Claude_Code_to_tools_via_MCP|claude.ai connectors]]. MCP servers you configure locally still work.

[[Run_Claude_Code_programmatically|Bare mode]] does not read `CLAUDE_CODE_OAUTH_TOKEN`. If your script passes `--bare`, authenticate with `ANTHROPIC_API_KEY` or an `apiKeyHelper` instead.

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
