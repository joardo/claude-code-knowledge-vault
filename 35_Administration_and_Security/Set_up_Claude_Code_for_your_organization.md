---
title: "Set up Claude Code for your organization"
aliases:
  - "admin-setup"
  - "Set up Claude Code for your organization"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/admin-setup"
status: "verified"
last_updated: "2026-10"
---

# Set up Claude Code for your organization

## Executive Summary
> A decision map for administrators deploying Claude Code, covering API providers, managed settings, policy enforcement, usage monitoring, and data handling.

## Technical Mechanics & Documentation

Claude Code enforces organization policy through managed settings that take precedence over local developer configuration. You deliver those settings from the Claude admin console, your mobile device management (MDM) system, or a file on disk. The settings control which tools, commands, servers, and network destinations Claude can reach.

This page walks through the deployment decisions in order. Each row links to the section below and to the reference page for that area.

<Note>
  SSO, SCIM provisioning, and seat assignment are configured at the Claude account level. See the [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) and [seat assignment](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan) for those steps.
</Note>

| Decision | What you're choosing | Reference |
| :- | :- | :- |
| [Choose your API provider](#choose-your-api-provider) | Where Claude Code authenticates and how it's billed | [[Authentication]], [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock]], [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform]], [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry]] |
| [Decide how settings reach devices](#decide-how-settings-reach-devices) | How managed policy reaches developer machines | [[Configure_server-managed_settings|Server-managed settings]], [[Deploy_managed_settings|Delivery mechanisms]] |
| [Decide what to enforce](#decide-what-to-enforce) | Which tools, commands, and integrations are allowed | [[Configure_permissions|Permissions]], [[Configure_the_sandboxed_Bash_tool|Sandboxing]] |
| [Set up usage visibility](#set-up-usage-visibility) | How you track spend and adoption | [[Track_team_usage_with_analytics|Analytics]], [[Monitoring]], [[Manage_costs_effectively|Costs]] |
| [Review data handling](#review-data-handling) | Data retention and compliance posture | [[Data_usage|Data usage]], [[Security]] |

## Choose your API provider

Claude Code connects to Claude through one of several API providers. Your choice affects billing, authentication, which compliance posture you inherit, and which Claude Code features your developers can use.

| Provider | Choose this when |
| :- | :- |
| Claude for Teams / Enterprise | You want Claude Code and claude.ai under one per-seat subscription with no infrastructure to run. This is the default recommendation. |
| Claude Console | You're API-first or want pay-as-you-go billing |
| Amazon Bedrock | You want to inherit existing AWS compliance controls and billing |
| Google Cloud's Agent Platform | You want to inherit existing GCP compliance controls and billing |
| Microsoft Foundry | You want to inherit existing Azure compliance controls and billing |

Some Claude Code features require a claude.ai account. [[Use_Claude_Code_in_the_cloud|Cloud sessions]], [[Automate_work_with_routines|Routines]], [[Code_Review|Code Review]], [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]], and the [[Use_Claude_Code_with_Chrome|Chrome extension]] aren't available through Console API keys or cloud-provider credentials alone. If you deploy through Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry, plan whether developers also need Claude for Teams or Enterprise seats. Each feature page lists its plan requirements.

For the full provider comparison covering authentication, regions, and feature parity, see the [[Enterprise_deployment_overview|enterprise deployment overview]]. Each provider's auth setup is in [[Authentication]].

Proxy and firewall requirements in [[Enterprise_network_configuration|Network configuration]] apply regardless of provider. If you want a single endpoint in front of multiple providers or centralized request logging, see [[Other_LLM_gateways|LLM gateway]].

## Decide how settings reach devices

Managed settings define organization policy. Claude Code checks the four sources in the table below in priority order. [[Deploy_managed_settings|How Claude Code combines managed sources]] says which of them apply, what a policy helper changes, and how to compose every source. The table is the decision map.

| Mechanism | Delivery | Priority | Platforms |
| :- | :- | :- | :- |
| Server-managed | claude.ai admin console, or a self-hosted [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] for gateway sign-ins | Highest | All |
| plist / registry policy | macOS: `com.anthropic.claudecode` plist<br />Windows: `HKLM\SOFTWARE\Policies\ClaudeCode` | High | macOS, Windows |
| File-based managed | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`<br />Linux and WSL: `/etc/claude-code/managed-settings.json`<br />Windows: `C:\Program Files\ClaudeCode\managed-settings.json` | Medium | All |
| Windows user registry | `HKCU\SOFTWARE\Policies\ClaudeCode` | Lowest | Windows only |

Claude Code fetches server-managed settings at startup and refreshes them hourly during the session, with no endpoint infrastructure to deploy. Delivery through the claude.ai admin console requires a Claude for Teams or Enterprise plan. Deployments on Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry can get the same remote delivery by running a [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]], or use one of the file-based or OS-level mechanisms instead.

If your organization mixes providers, configure [[Configure_server-managed_settings|server-managed settings]] for claude.ai users plus a [[Deploy_managed_settings|file-based or plist/registry fallback]] so other users still receive managed policy.

The plist and HKLM registry locations work with any provider and resist tampering because they require admin privileges to write. The Windows user registry at HKCU is writable without elevation, so treat it as a convenience default rather than an enforcement channel.

By default, WSL reads only the Linux file path at `/etc/claude-code`. To extend your Windows registry and `C:\Program Files\ClaudeCode` policy to WSL on the same machine, set [[All_settings|`wslInheritsWindowsSettings: true`]] in either of those admin-only Windows sources.

Whichever mechanism you choose, managed values take precedence over user and project settings, apart from a few security-sensitive [[Settings_files_and_precedence|exceptions]]. Array settings such as `permissions.allow` and `permissions.deny` merge entries from all sources, so developers can extend managed lists but not remove from them. For `fallbackModel`, `availableModels`, and [[All_settings|`modelPicker`]], the managed value replaces lower layers rather than merging.

### WSL sessions in Claude Code Desktop

On Windows, [[Claude_Code_Desktop_in_WSL|Claude Code Desktop can run Code sessions inside a WSL 2 distribution]]. The session's Claude Code process runs inside the distribution, so it resolves managed settings through the WSL discovery path above: Windows-only sources don't reach it unless `wslInheritsWindowsSettings: true` is deployed.

Claude Desktop turns off WSL sessions by default on devices it detects as organization-managed, for example when `C:\Program Files\ClaudeCode\managed-settings.json` exists. To turn them on, deploy a Windows registry policy, which requires Claude Desktop v1.19367.0 or later:

* Create a value named `disableWslSessions` under `HKLM\SOFTWARE\Policies\Claude` and set it to the `REG_SZ` string `false` or the `REG_DWORD` `0`. This value sits under the Claude Desktop policy key, separate from the `ClaudeCode` key that carries managed settings. Deploy the value under HKLM, which requires administrator privileges to write. A value under HKCU doesn't enable WSL sessions.
* Leave `C:\Program Files\ClaudeCode\managed-settings.json` in place if you deploy it. Once `disableWslSessions` is `false` under HKLM, Desktop allows WSL sessions even though that file is present.

Desktop reads the policy each time a WSL session starts, so you don't need to restart the app after deploying it.

If a device still refuses WSL sessions, open **Help > Troubleshooting > Show Logs in File Explorer** in Claude Desktop on that device, which saves a copy of its log folder to Downloads. Search `main.log` in that copy for `[wslPolicyGate] denying WSL session`. The reason for the denial follows in parentheses, such as `(cli-file-present)`.

After WSL sessions are enabled, extend your managed settings to them:

* Deploy `wslInheritsWindowsSettings: true` through the HKLM registry or the `C:\Program Files\ClaudeCode` file so WSL sessions inherit the same policy as host sessions.
* Verify by running `/status` inside a WSL session and reading the `Setting sources` line. To interpret what it lists, see [[Deploy_managed_settings|Read the source in /status]].

Processes inside the WSL 2 utility VM aren't visible to Windows-side endpoint detection sensors. To observe in-distro process and file activity, check your endpoint detection vendor's WSL guidance for a Linux sensor you can run inside the distribution and the exclusions it needs. Claude Code's [[Monitoring|OpenTelemetry tool-execution telemetry]] is emitted identically for WSL and native sessions.

## Decide what to enforce

Managed settings can lock down tools, sandbox execution, restrict MCP servers and plugin sources, and control which hooks run. Each row is a control surface with the setting keys that drive it.

| Control | What it does | Key settings |
| :- | :- | :- |
| [[Configure_permissions|Permission rules]] | Allow, ask, or deny specific tools and commands | `permissions.allow`, `permissions.deny` |
| [[Configure_permissions|Permission lockdown]] | Make managed settings the [[All_settings|only settings source of permission rules]]. Disable `--dangerously-skip-permissions` | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` |
| [[Choose_a_permission_mode|Starting permission mode]] | Choose the permission mode your developers' terminal sessions start in instead of the built-in starting permission mode, or remove auto mode. [[Choose_a_permission_mode|Switch permission modes]] lists when the VS Code extension reads a `defaultMode` you set | `permissions.defaultMode`, `permissions.disableAutoMode` |
| [[Configure_the_sandboxed_Bash_tool|Sandboxing]] | OS-level filesystem and network isolation with domain allowlists | `sandbox.enabled`, `sandbox.network.allowedDomains` |
| [[How_Claude_remembers_your_project|Managed policy CLAUDE.md]] | Org-wide instructions loaded in every session, can't be excluded | File at the managed policy path |
| [[Control_MCP_server_access_for_your_organization|MCP server control]] | Restrict which MCP servers users can add or connect to, deploy a fixed set, or provide remote servers to every user alongside their own | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, `managedMcpServers`, or a deployed `managed-mcp.json` file |
| [[Manage_Claude_Code_plugins_for_your_organization|Plugin marketplace control]] | Restrict which marketplace sources users can add and install from, reject the CLI flags that sideload plugins, agents, and MCP servers for a single run, block [[Marketplace_reference|`command` plugin sources]], and allowlist which marketplaces' plugins can be suggested | `strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags`, `disableCommandPluginSources`, `pluginSuggestionMarketplaces` |
| [[All_settings|Customization lockdown]] | Block skills, agents, hooks, and MCP servers from user and project sources, so they can only come from plugins or managed settings. Locking skills also stops the [[Extend_Claude_with_skills|skills your developers enable on claude.ai]] from syncing | `strictPluginOnlyCustomization` |
| [[All_settings|Disable claude.ai sync]] | Stop Claude Code from loading the [[Extend_Claude_with_skills|skills]] and [[Plugin_loading_reference|plugins]] your developers enable on claude.ai. If you turn off Skills for your organization on claude.ai, Claude Code stops syncing both, and on v2.1.273 or later it also removes the ones it already synced. To stop either one without turning Skills off, set its key to `false` in managed settings | `syncClaudeAiSkills`, `syncClaudeAiPlugins` |
| [[All_settings|Hook restrictions]] | Restrict which hooks run and restrict HTTP hook URLs; see [[All_settings|what runs under `allowManagedHooksOnly`]] for the full effect list | `allowManagedHooksOnly`, `allowedHttpHookUrls` |
| [[All_settings|Login enforcement]] | Restrict login to a specific method or Anthropic organization. The method restriction applies across the VS Code extension, Agent SDK, `claude setup-token`, and `/install-github-app`, and the terminal's interactive login screen, reached by `/login` or first-run onboarding, pre-selects the method without enforcing it; Claude Code verifies the organization for claude.ai account logins in the terminal, VS Code extension, and Agent SDK, and doesn't check it for Claude Console logins or for [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|gateway]] sign-in. Before v2.1.212, only terminal logins applied either key. When set, sessions authenticated by `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` are blocked at startup; cloud provider sessions aren't affected unless one of those credentials, or an API key saved by an earlier Claude Console login, is also present | `forceLoginMethod`, `forceLoginOrgUUID` |
| [[All_settings|Provider restrictions]] | Limit which API providers a machine may use. A session on a provider that isn't listed is refused at startup, at login, and when it next contacts the API. Requires Claude Code v2.1.285 or later | `allowedProviders` |
| [[Manage_multiple_agents_with_agent_view|Disable agent view]] | Turn off `claude agents`, `--bg`, `/background`, and the on-demand supervisor | `disableAgentView` |
| [[Run_Claude_Code_behind_a_corporate_launcher|Configure the corporate launcher]] | Prefix the [[Manage_multiple_agents_with_agent_view|background-agent supervisor]], its workers, and the [[Run_Claude_Code_behind_a_corporate_launcher|other covered background processes]] with a required corporate launcher instead of turning agent view off | `processWrapper` |
| [[Model_configuration|Model restrictions]] | `availableModels` filters which models appear in the picker. Adding `enforceAvailableModels` also constrains the auto-selected default model. See [[Model_configuration|surface coverage]] for how this setting reaches the CLI, web, and IDE | `availableModels`, `enforceAvailableModels` |
| [[All_settings|Effort cap]] | Cap the [[Model_configuration|effort level]] for every model or per model, on every provider | `maxEffortLevel` |
| [[All_settings|Version floor]] | Prevent auto-update from installing below an org-wide minimum | `minimumVersion` |
| [[All_settings|Required version range]] | Refuse to start at all when the running version is outside an org-approved range. Stronger than `minimumVersion`, which only blocks downgrades | `requiredMinimumVersion`, `requiredMaximumVersion` |
| [[Data_usage|Telemetry opt-out]] | Turn off Anthropic-bound usage metrics, error reports, and surveys on every device | `env` with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set to `1`; the linked section lists the per-category variables |

If your members sign in through claude.ai or the Anthropic API and you're on a Claude Enterprise plan, you can also govern models from your organization's admin settings without deploying anything:

* [[Model_configuration|Organization model restrictions]]: disable individual models. Enforced server-side.
* [[Model_configuration|Organization default model]]: set which model new sessions start on. Members can still switch models. To return them to your default at launch, turn on the override that section describes. To limit which models they can pick, use [[Model_configuration|organization model restrictions]].
* [[Model_configuration|Organization effort limits]]: cap effort levels per role. Enforced server-side.

None of these controls reach sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or [[Claude_Code_on_Claude_Platform_on_AWS|Claude Platform on AWS]]. On those providers, use managed settings instead: `availableModels` for restrictions, `model` for a default, and [[All_settings|`maxEffortLevel`]] for an effort cap.

[[Use_Claude_Code_in_the_cloud|Cloud sessions]] have their own admin surfaces on claude.ai:

* **Cloud environments page**: Owners create [[Configure_cloud_environments|organization-shared environments]] that set the [[Configure_cloud_environments|network access level]], environment variables, and setup script for members' cloud sessions.
* **Default environment**: Owners choose the organization's default environment separately, at [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code).
* **Git providers page**: see [Connected GitHub accounts](#connected-github-accounts) for the GitHub accounts linked to your organization.

Permission rules and sandboxing cover different layers. Denying WebFetch blocks Claude's fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level.

For the threat model these controls defend against, see [[Security]].

### Connected GitHub accounts

On Team and Enterprise plans, the GitHub section of [**Organization settings > Git providers**](https://claude.ai/admin-settings/source-control) lists the GitHub organizations and personal accounts linked to your Claude organization through the [Claude GitHub App](https://github.com/apps/claude). Claude Code, [Claude Tag](https://claude.com/docs/claude-tag/admins/configure-github), and Claude Security share the list. Opening the page requires an admin role in your Claude organization.

An admin or a member can link an account:

* **Admin connection**: an admin clicks **Connect** in that section, or **Add organization** once an account is connected, and installs the Claude GitHub App on a GitHub organization. Linking an organization this way requires someone who is both an owner of the GitHub organization and an admin of your Claude organization.
* **Member connection**: when a member connects their GitHub account to Claude, for example while [[Get_started_with_Claude_Code_in_the_cloud|setting up cloud sessions]], Claude links the GitHub accounts that member owns where the Claude GitHub App is already installed. That can include their personal account and GitHub organizations they own.

A row marked **Not linked** comes from your own GitHub sign-in. It's an account you can see on GitHub where the Claude GitHub App is installed.

To unlink an account from your Claude organization, open its row's menu and select **Unlink from this workspace**. Unlinking leaves the Claude GitHub App installed on GitHub, and the account is linked again the next time one of its owners connects GitHub to Claude. To keep it from being linked again, uninstall the Claude GitHub App from that account on GitHub.

On Enterprise plans, the [Compliance API](https://platform.claude.com/docs/en/api/compliance/activities/list) activity types for linking and unlinking are `github_app_installation_linked` and `github_app_installation_unlinked`.

## Set up usage visibility

Choose monitoring based on what you need to report on. The dashboards, APIs, and spend controls differ between Claude for Teams or Enterprise plans and Claude Console organizations, so check the Availability column before you plan your reporting around a capability.

| Capability | What you get | Availability | Where to start |
| :- | :- | :- | :- |
| Usage monitoring | OpenTelemetry export of sessions, tools, and tokens | All providers | [[Monitoring|Monitoring usage]] |
| Analytics dashboard | Adoption and contribution metrics with a leaderboard on Teams / Enterprise; per-user usage and spend metrics on Console | Teams / Enterprise at [claude.ai/analytics](https://claude.ai/analytics/claude-code), Console at [platform.claude.com/claude-code](https://platform.claude.com/claude-code) | [[Track_team_usage_with_analytics|Analytics]] |
| Programmatic reporting | Per-user usage and cost data over an API | [Enterprise Analytics API](https://platform.claude.com/docs/en/api/admin/analytics) for Enterprise, [Claude Code Analytics API](https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api) for Console | [[Manage_costs_effectively|Costs]] |
| Spend controls | Spend limits and rate limits | Organization settings for Teams / Enterprise, workspace limits for Console; on third-party clouds, cloud budget controls or a [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] with per-user [[Claude_apps_gateway_spend_limits|spend limits]] | [[Manage_costs_effectively|Costs]] |

On Teams and Enterprise, per-user usage and spend numbers come from the [spend report](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans) in your organization's analytics settings, not the analytics dashboard. Cloud providers expose spend through AWS Cost Explorer, GCP Billing, or Azure Cost Management. For planning enterprise budgets across Claude chat, Claude Code, and Cowork, see the [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide).

## Review data handling

On Team, Enterprise, Claude API, and cloud provider plans, Anthropic doesn't train models on your code or prompts. Your API provider determines retention and compliance posture.

| Topic | What to know | Where to start |
| :- | :- | :- |
| Data usage policy | What Anthropic collects, how long it's retained, what's never used for training | [[Data_usage|Data usage]] |
| Zero Data Retention (ZDR) | Nothing stored after the request completes. Available to qualified accounts on Claude for Enterprise | [[Zero_data_retention|Zero data retention]] |
| HIPAA configuration | For Claude for Enterprise organizations that have HIPAA enabled. Some Claude Code (local mode) features are turned off and others are off by default | [[Set_up_Claude_Code_local_mode_for_a_HIPAA-ready_organization|Set up Claude Code (local mode) for a HIPAA-ready organization]] |
| Security architecture | Network model, encryption, authentication, audit trail | [[Security]] |

If you need request-level audit logging or to route traffic by data sensitivity, we recommend you place a gateway between developers and your provider: a self-hosted [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] records a per-request audit log with IdP identity, or you can use another [[Other_LLM_gateways|LLM gateway]]. Sessions that go through a gateway aren't eligible for the HIPAA configuration. [[Set_up_Claude_Code_local_mode_for_a_HIPAA-ready_organization|Check how developers sign in and connect]] lists which sign-in and connection methods are. For regulatory requirements and certifications, see [[Legal_and_compliance|Legal and compliance]].

## Verify and onboard

After configuring managed settings, have a developer run `/status` inside Claude Code. On the **Status** tab, the `Setting sources` line shows `Enterprise managed settings` followed by the source that won in parentheses; [[Deploy_managed_settings|Verify enforcement]] lists the labels.

Share these resources to help developers get started:

* [[Quickstart]]: first-session walkthrough from install to working with a project
* [[Common_workflows|Common workflows]]: patterns for everyday tasks like code review, refactoring, and debugging
* [Claude Code 101](https://academy.claude.com/courses/claude-code-101) and [Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action): free self-paced courses on [Claude Academy](https://academy.claude.com/)

For login issues, point developers to [[Troubleshoot_installation_and_login|authentication troubleshooting]]. The most common fixes are:

* Run `/logout` then `/login` to switch accounts
* Run `claude update` if the enterprise auth option is missing
* Restart the terminal after updating

If a developer sees "You haven't been added to your organization yet," their seat doesn't include Claude Code access and needs to be updated in the admin console.

## Next steps

With provider and delivery mechanism chosen, move on to detailed configuration:

* [[Configure_server-managed_settings|Server-managed settings]]: deliver managed policy from the Claude admin console
* [[All_settings|All settings]]: every setting key, with where it goes and an example
* [[Settings_files_and_precedence|Which value Claude Code uses]]: the precedence rules across managed, project, local, and user settings
* [[Set_up_Claude_Code_in_a_monorepo_or_large_codebase|Monorepos and large repos]]: per-directory configuration patterns for organizations deploying into a monorepo
* [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock]], [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform]], [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry]]: provider-specific deployment
* [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide): SSO, SCIM, seat management, and rollout playbook

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
