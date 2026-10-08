---
title: "Deploy managed settings"
aliases:
  - "managed-settings"
  - "Deploy managed settings"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/managed-settings"
status: "verified"
last_updated: "2026-10"
---

# Deploy managed settings

## Executive Summary
> Deploy managed settings to every developer's machine: delivery mechanisms per OS, how Claude Code combines managed sources, and how to verify enforcement.

## Technical Mechanics & Documentation

Managed settings are the settings your organization deploys to every developer's machine. Claude Code applies them above every other level, so no user, project, local, or `--settings` value overrides them, apart from a few [[Settings_files_and_precedence|security-sensitive exceptions]] where a stricter value from a lower level still counts.

This page is for the administrator who deploys managed settings or debugs why one isn't applying. To decide what to enforce, start with the [[Set_up_Claude_Code_for_your_organization|Decide what to enforce]] table. For the claude.ai console path, see [[Configure_server-managed_settings|Server-managed settings]]. For which file a developer's own values go in, see [[Settings_files_and_precedence|Settings]].

## Deploy a managed settings file

This is the quickest way to put a policy on each machine: a `managed-settings.json` file. If you haven't picked how to deliver managed settings yet, or your devices are under MDM or developers run cloud sessions, read [Choose a delivery mechanism](#choose-a-delivery-mechanism) first.

<Steps>
  <Step title="Write managed-settings.json">
    Write a `managed-settings.json` that holds the keys you've decided to enforce, in the same JSON shape as `settings.json`. The [[Set_up_Claude_Code_for_your_organization|Decide what to enforce]] table lists the keys behind each control, and each entry in the [[All_settings|settings reference]] says whether a managed source can set it. This file blocks two file reads, turns off bypass mode, and makes Claude Code ignore permission rules from user, project, and local files and from `--allowedTools`:

    ```json managed-settings.json theme={null}
    {
      "permissions": {
        "deny": [
          "Read(./.env)",
          "Read(./secrets/**)"
        ],
        "disableBypassPermissionsMode": "disable"
      },
      "allowManagedPermissionRulesOnly": true
    }
    ```

    For a fuller example that shows the shape of more managed keys, including the login method, models, MCP servers, and marketplaces, see [[Example_settings_files|An organization's managed settings]].
  </Step>

  <Step title="Place the file on each machine">
    Save the file as `managed-settings.json` in the system directory for the operating system, using whatever tooling already places files on your fleet:

    * **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
    * **Linux and WSL**: `/etc/claude-code/managed-settings.json`
    * **Windows**: `C:\Program Files\ClaudeCode\managed-settings.json`
  </Step>

  <Step title="Confirm the policy applied">
    On one machine, run `/status` inside Claude Code. The `Setting sources` line shows `Enterprise managed settings (file)`. Roll out to the rest of the fleet after that; [Check that a policy is in force](#check-that-a-policy-is-in-force) covers what to look at when the line is missing.
  </Step>
</Steps>

<span id="managed-settings-delivery" />

<span id="delivery-mechanisms" />

## Choose a delivery mechanism

The file in the steps above is one of four ways to get managed settings onto a machine. Every mechanism carries the same policy keys as a `settings.json` file, so the [[All_settings|settings reference]] applies to all of them. A few keys are tied to particular sources, and each entry's Scope line says which:

* **Delivery controls**: [[All_settings|`policyHelper`]], [[All_settings|`wslInheritsWindowsSettings`]], and [[All_settings|`managedSourcesBehavior`]]
* **Gateway login keys**: [[All_settings|`forceLoginGatewayUrl`]], [[All_settings|`gatewayInternalNetworks`]], and the `"gateway"` value of [[All_settings|`forceLoginMethod`]]

A managed settings file, an MDM profile, or the claude.ai console applies one policy to everyone it reaches. To give one group of developers a different policy, deploy a different file or profile to that group; the claude.ai console [[Configure_server-managed_settings|can't target a group yet]], while a self-hosted [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] delivers managed settings per IdP group.

When more than one mechanism delivers a policy to the same machine, Claude Code by default uses one and ignores the others. [How Claude Code combines managed sources](#how-claude-code-combines-managed-sources) gives the order and the opt-in that applies every source.

The MDM and file rows are together called endpoint-managed settings, because the policy is stored on the developer's device, as opposed to the server-managed row, where Claude Code fetches it.

Pick a mechanism by how you already manage devices, using the table below.

| Mechanism | How you deliver it | When Claude Code reads it | Use it when |
| :- | :- | :- | :- |
| [[Configure_server-managed_settings|Server-managed settings]] | In the claude.ai admin console, or on a self-hosted [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]] | Fetched at startup and polled hourly; see [changes that need approval](#where-and-when-a-policy-applies) | You want one place to change policy for a claude.ai organization without touching each machine |
| MDM or OS-level policy | As a macOS configuration profile or a Windows `HKLM` registry value, through Jamf, Intune, Group Policy, or a similar tool; see [where each mechanism stores the policy](#where-each-mechanism-stores-the-policy) | Read at startup and checked for changes every 30 minutes | You already manage devices with MDM or Group Policy |
| File-based | As `managed-settings.json` in a system directory on each machine; see [where each mechanism stores the policy](#where-each-mechanism-stores-the-policy) | Read at startup and reloaded when a file changes | Machines without MDM, Linux hosts, or images you build yourself |
| HKCU registry, Windows and WSL | As a Windows `HKCU` registry value; see [where each mechanism stores the policy](#where-each-mechanism-stores-the-policy) | Read at startup and checked for changes every 30 minutes; Claude Code uses it only when [no admin document is present above it](#present-admin-documents) and no [host-supplied parent settings](#let-an-embedding-host-add-policy) supply a restrictive key | You can't write the machine-level `HKLM` key |

Starter templates for Jamf, Iru, Intune, and Group Policy are in the [MDM examples repository](https://github.com/anthropics/claude-code/tree/main/examples/mdm).

For managed MCP servers, which you deploy alongside any of these through `managed-mcp.json` or provide through the [[All_settings|`managedMcpServers`]] key, see [[Control_MCP_server_access_for_your_organization|Managed MCP configuration]].

### Where and when a policy applies

A deployed policy reaches the developer's sessions as follows:

* **Surfaces**: on the developer's machine, the terminal, the VS Code and JetBrains extensions, the desktop app's Code tab, and [[Agent_SDK_reference_-_TypeScript|Agent SDK]] sessions read all of these sources. Agent SDK sessions load managed settings even when `settingSources` excludes the user, project, and local files.
* **Cloud sessions**: a session in an Anthropic-hosted environment doesn't read a device's MDM profile or file, so policy for it has to come from server-managed settings. A session in a [[Self-hosted_environments|self-hosted environment]] also reads the managed settings file in its runner image, by default only when server-managed settings deliver no policy key, apart from the [keys Claude Code reads from every admin source](#keys-read-from-every-admin-source). [How Claude Code combines managed sources](#how-claude-code-combines-managed-sources) covers the opt-in that applies both.
* **Claude Tag sessions**: [Claude Tag](https://claude.com/docs/claude-tag/overview) sessions run in cloud environments but don't receive server-managed settings. In a [[Self-hosted_environments|self-hosted environment]], they still read the managed settings file in the runner image. Configure Claude Tag itself in the [Claude Tag admin settings](https://claude.com/docs/claude-tag/admins/customize).
* **Cowork sessions**: [Cowork](https://claude.com/docs/cowork/overview) in the Claude Desktop app runs its sessions on Claude Code. In a Cowork session, Claude Code never fetches server-managed settings from the claude.ai admin console, even when the user signs in with a Team or Enterprise account, so which policy applies depends on where the session runs:

  * **On the user's machine**: by default, Claude Code in a Cowork session reads the MDM or OS-level policy and the managed settings file on that device, so deploy policy there.
  * **In a full VM sandbox**: when your Claude Desktop managed configuration sets [`requireCoworkFullVmSandbox`](https://claude.com/docs/third-party/claude-desktop/configuration#requirecoworkfullvmsandbox), Claude Code runs inside a virtual machine where the device's MDM policy and managed settings file aren't present.
  * **Remote Cowork sessions**: these run on Anthropic-managed VMs, where Claude Code has no device policy to read.

  Wherever the session runs, claude.ai applies the admin console's [[All_settings|`strictKnownMarketplaces`]] and [[All_settings|`blockedMarketplaces`]] lists itself when anyone adds a marketplace from a git repository on claude.ai or from **Customize** in the Cowork tab. [[Manage_Claude_Code_plugins_for_your_organization|How restrictions work]] describes that check. The [[Model_configuration|surface coverage]] table compares Cowork with the other surfaces.
* **Running sessions**: most changes reach a running session on the schedule in the [delivery mechanism table](#choose-a-delivery-mechanism), without a restart.
  * Changes to [[All_settings|`forceRemoteSettingsRefresh`]], [[All_settings|`requiredMinimumVersion`]], and [[Settings_files_and_precedence|some user-editable keys]] take effect at the next session start.
  * A new or changed [[All_settings|`policyHelper`]] entry takes effect at the next launch. If server-managed settings shadow the helper at that launch, the helper runs as soon as a fetch reports those settings removed.
* **Changes that need approval**: apart from the [[Configure_server-managed_settings|updates that wait for the next launch]], a server-managed change to a setting that [[Configure_server-managed_settings|needs approval]], such as a hook or an `env` variable, waits for the developer to accept the dialog in an interactive session, and applies for the current run in a session an IDE extension or the Agent SDK hosts. Other server-managed changes apply on the next poll.
* **Long-lived sessions**: a session left open for weeks can still lag a rollout. [[All_settings|`requiredMinimumVersion`]] blocks an outdated binary from starting and doesn't end a session that's already running.

<span id="format-the-policy-for-each-platform" />

### Where each mechanism stores the policy

The keys are the same everywhere, but each mechanism stores them in a different place and shape:

* **Server-managed**: Anthropic's servers, or your gateway, hold the policy. Claude Code keeps a local cache that it applies at startup and [[Configure_server-managed_settings|replaces on each successful fetch]].
* **macOS configuration profile**: the `com.anthropic.claudecode` managed preferences domain. Use the same top-level keys as `managed-settings.json`, with nested settings as dictionaries and lists as plist arrays.
* **Windows HKLM registry**: the JSON as a `REG_SZ` or `REG_EXPAND_SZ` value named `Settings` under `HKLM\SOFTWARE\Policies\ClaudeCode`.
* **File-based**: `managed-settings.json`, an optional `managed-settings.d/` directory, and `managed-mcp.json` in the system directory: `/Library/Application Support/ClaudeCode/` on macOS, `/etc/claude-code/` on Linux and WSL, and `C:\Program Files\ClaudeCode\` on Windows. Claude Code doesn't read the legacy Windows path `C:\ProgramData\ClaudeCode\managed-settings.json`.
* **Windows HKCU registry**: the same `Settings` value under `HKCU\SOFTWARE\Policies\ClaudeCode`.

### Split a file-based policy across teams

If several teams own parts of one policy, put each part in its own file in `managed-settings.d/`, next to `managed-settings.json` in the same system directory, instead of editing one shared file.

Claude Code merges `managed-settings.json` first, then every `*.json` file in the directory in alphabetical order. Name the files with numeric prefixes to control the order, such as `10-telemetry.json` and `20-security.json`. Claude Code ignores hidden files and files that don't end in `.json`.

When two files set the same key, Claude Code combines them by these rules:

* **Single values**, such as `"model": "opus"` or `"cleanupPeriodDays": 7`: the later file's value replaces the earlier one
* **Lists**, such as `permissions.deny` or `sandbox.network.allowedDomains`: the two lists combine, with duplicates removed
* **Nested blocks**, such as `env` or `sandbox`: the two blocks merge key by key, and each key inside follows these same rules
* **`fallbackModel`**: the later chain replaces the earlier one whole
* **[[All_settings|`extraKnownMarketplaces`]] and [[All_settings|`managedMcpServers`]]**: a later entry with the same name replaces the earlier one whole
* **[[All_settings|`modelPicker`]]**: the later lineup replaces the earlier one whole

<span id="precedence-within-the-managed-tier" />

<span id="which-managed-source-claude-code-uses" />

## How Claude Code combines managed sources

When your organization delivers more than one managed source to the same machine, the [[All_settings|`managedSourcesBehavior`]] key decides what Claude Code does with the others:

* **`"first-wins"`, the default**: Claude Code uses the highest-ranked source that delivers at least one policy key and ignores the rest rather than merging them, apart from the keys in [Keys read from every admin source](#keys-read-from-every-admin-source). Claude Code shows no warning for the sources it skips; `/status` [names the source it used and the ones it skipped](#read-the-source-in-/status).
* **`"merge"`**: Claude Code applies every admin source that delivers a policy key and combines them by kind of key: on most keys the higher-ranked source's value applies, lists union, and locks take the strictest value. [Compose every managed source](#compose-every-managed-source) says where to set the key and how each kind of key combines. Requires Claude Code v2.1.242 or later.

Both settings rank the sources the same way. These terms recur in this section:

* **Policy key**: any settings key other than the two control keys, [[All_settings|`wslInheritsWindowsSettings`]] and [[All_settings|`managedSourcesBehavior`]]. A managed settings file or MDM policy that contains only those doesn't count, and Claude Code moves on to the next source.
* **Admin source**: one of the first three sources below. The HKCU registry is user-writable and isn't one.

Claude Code checks the sources in this order, highest priority first:

1. Remote settings, delivered from claude.ai as [[Configure_server-managed_settings|server-managed settings]] or by a [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]]. Claude Code fetches this source only when the session authenticates to Anthropic's API directly with an [[Configure_server-managed_settings|eligible login or key]], or signs in to a gateway with `/login`. On other providers, or when `ANTHROPIC_BASE_URL` points somewhere other than Anthropic's API, it starts at the next source
2. MDM or OS-level policies: the macOS plist or the HKLM registry key
3. Managed settings files, `managed-settings.d/*.json` and `managed-settings.json` merged together
4. The HKCU registry, on Windows, and on WSL once the HKLM registry or the Windows managed settings file turns [[All_settings|`wslInheritsWindowsSettings`]] on and the HKCU value also sets it. Claude Code reads it only when [no admin document is present above it](#present-admin-documents) and no [host-supplied parent settings](#let-an-embedding-host-add-policy) supply a restrictive key

This diagram shows the ranking, with examples of the cross-source keys Claude Code reads from the first three sources under either setting:

<img src="https://mintcdn.com/claude-code/zuWID2B-Rxm8DEC8/images/managed-source-precedence.svg?fit=max&auto=format&n=zuWID2B-Rxm8DEC8&q=85&s=53f6be49f06eff48e01422c8ae1bc2e6" className="dark:hidden" alt="Diagram showing the four managed settings sources ranked from remote settings at the top through MDM, managed settings files, and the HKCU registry at the bottom. By default the first source with a policy key supplies the policy and the rest are skipped; with managedSourcesBehavior set to merge, every admin source with a policy key contributes, combined by kind of key, and the HKCU registry stays out. A side panel shows that cross-source keys such as the sandbox locks, forceRemoteSettingsRefresh, and the per-variable env merge are read from every admin source, which excludes the HKCU registry." width="680" height="330" data-path="images/managed-source-precedence.svg" />

<img src="https://mintcdn.com/claude-code/zuWID2B-Rxm8DEC8/images/managed-source-precedence-dark.svg?fit=max&auto=format&n=zuWID2B-Rxm8DEC8&q=85&s=ae407a9a08a3d680e80cf1a2af845d71" className="hidden dark:block" alt="Diagram showing the four managed settings sources ranked from remote settings at the top through MDM, managed settings files, and the HKCU registry at the bottom. By default the first source with a policy key supplies the policy and the rest are skipped; with managedSourcesBehavior set to merge, every admin source with a policy key contributes, combined by kind of key, and the HKCU registry stays out. A side panel shows that cross-source keys such as the sandbox locks, forceRemoteSettingsRefresh, and the per-variable env merge are read from every admin source, which excludes the HKCU registry." width="680" height="330" data-path="images/managed-source-precedence-dark.svg" />

<h3 id="present-admin-documents">
  When an admin document counts as present
</h3>

In the [ranking of managed sources](#how-claude-code-combines-managed-sources), Claude Code never applies the user-writable HKCU registry beneath an admin document that is present. A document is present when:

* It sets any policy key to a value other than `null`, even a value Claude Code can't read
* It is an HKLM value, managed settings file, or `managed-settings.d` directory that exists but can't be read

On WSL, `/etc/claude-code` is user-writable as well, and the [[All_settings|`wslInheritsWindowsSettings`]] entry says when the Windows documents stand above it.

### Keys read from every admin source

Under the default `"first-wins"` setting, Claude Code reads most keys only from the [source it selected](#how-claude-code-combines-managed-sources), and ignores a value in a lower-ranked source even when the selected source leaves that key unset.

A few keys work differently. Claude Code reads them from every admin source, so a lower-ranked MDM policy or managed settings file can still set them when the selected source doesn't. Claude Code leaves the user-writable HKCU registry out of that scan; when HKCU is the only source and no host supplies parent settings, HKCU applies like any selected source.

The cross-source keys include:

* `sandbox.network.allowManagedDomainsOnly` and `sandbox.filesystem.allowManagedReadPathsOnly`: a `true` in any admin source turns the lock on. While a lock is on, Claude Code unions the allowlist it locks, `sandbox.network.allowedDomains` together with `WebFetch(domain:...)` allow rules, or `sandbox.filesystem.allowRead`, across every admin source. Without the lock, Claude Code treats the allowlist like any other key, so under `"first-wins"` an unselected admin source's allowlist is ignored
* `allowAllClaudeAiMcps`
* `allowManagedMcpServersOnly`: a `true` in any admin source turns the MCP allowlist lock on. While the lock is on, the managed `allowedMcpServers` list comes from the highest-ranked admin source that sets one. A server-managed list replaces a lower source's list rather than combining with it.

  If no admin source sets a list, every server that passes the denylist loads, unless [parent settings](#let-an-embedding-host-add-policy) supply a list.

  Without the lock, Claude Code reads `allowedMcpServers` from the managed source it applies, so under `"first-wins"` an unselected admin source's list is ignored. Requires Claude Code v2.1.273 or later
* `deniedMcpServers` and [[All_settings|`disableClaudeAiConnectors`]]: an entry or a `true` in any admin source applies. Requires Claude Code v2.1.273 or later
* The sandbox binary paths `sandbox.bwrapPath` and `sandbox.socatPath`
* The sandbox `ripgrep` binary, [[All_settings|`sandbox.ripgrep`]]
* `sandbox.filesystem.disabled` and `sandbox.network.strictAllowlist`
* [[All_settings|`useAutoModeDuringPlan`]], [[All_settings|`syncClaudeAiSkills`]], and [[All_settings|`syncClaudeAiPlugins`]], where a `false` from any admin source turns the behavior off. A `false` in the developer's user or local settings turns it off too; each key can only deny
* [[All_settings|`enableArtifact`]], where a `false` from any admin source turns the [[Share_session_output_as_artifacts|Artifact tool]] off. A `false` in the developer's user, project, or local settings turns it off too, and no source turns it back on; see [[Settings_files_and_precedence|which lower-level values still count]]. Requires Claude Code v2.1.242 or later
* [[All_settings|`maxEffortLevel`]], where the lowest cap in any admin source applies. If a developer sets a lower cap in their own settings or with `--settings`, Claude Code applies that one; no source can raise the cap. Requires Claude Code v2.1.267 or later
* A commit-trailer opt-out in `attribution`, or in the deprecated `includeCoAuthoredBy`, from any tier
* [[Configure_server-managed_settings|`forceRemoteSettingsRefresh`]]
* `env`, merged per variable across the admin sources: each variable comes from the highest-priority source that defines it, so lower sources fill in variables the higher ones leave unset. A few variables follow their own rules; [[Configure_server-managed_settings|Per-key exceptions across managed sources]] names each one. Requires Claude Code v2.1.223 or later. Before v2.1.223, Claude Code applied the selected source's whole `env` block only

The [gateway login keys](#choose-a-delivery-mechanism) follow a separate rule. Claude Code never reads them from server-managed settings, so while server-managed settings are the selected source, the highest-ranked admin source on the machine that carries a policy key still supplies them. A value in an admin source ranked below that one, or in the HKCU registry, is ignored.

[[All_settings|`allowedProviders`]] has its own rule: its entry's Scope note says how a list set on the machine combines with a server-managed one. Requires Claude Code v2.1.285 or later.

When an admin source sets `allowManagedMcpServersOnly` or an `allowedMcpServers` list and that value isn't the one in force, `/status` and `claude doctor` name that source and key.

### Compose every managed source

To have Claude Code apply every admin source your organization delivers, set [[All_settings|`managedSourcesBehavior`]] to `"merge"` in the highest-ranked source you deploy. Claude Code reads the key only from the highest-ranked source that carries either the key or a policy key, so a lower source can't opt itself into merging with the source above it, and a machine that never receives server-managed settings needs the key in its MDM profile too. The user-writable HKCU registry never merges with another source. Requires Claude Code v2.1.242 or later.

Under `"merge"`, Claude Code adds a lower source's list entries, such as `permissions.allow` rules and hooks, to the policy, so turn it on only when every source ranked below your highest one is under an administrator's control.

This table shows how Claude Code combines each kind of key under `"merge"`. The [[All_settings|`managedSourcesBehavior` entry]] names every key in three of the rows: restriction allowlists, values taken whole, and keys read from the highest-ranked source only.

| Kind of key | How Claude Code combines it | Examples |
| :- | :- | :- |
| Lists | Combines the entries from every source | `permissions.allow`, `hooks`, `sandbox.network.allowedDomains`, `deniedMcpServers`, `deniedModels` |
| Locks | Applies the strictest value any source sets; a looser value applies only from the highest-ranked source | `allowManagedHooksOnly`, `permissions.disableBypassPermissionsMode`, `crossSessionInbound`, `availableModelsMatch` |
| Restriction allowlists | Takes the list whole from the highest-ranked source that sets it, without adding entries from lower sources | `availableModels`, `allowedMcpServers`, `strictKnownMarketplaces`, `allowedChannelPlugins`, and the `fallbackModel` chain |
| Values taken whole | Takes the value whole from the highest-ranked source that sets it, without combining entries or fields from lower sources | `sandbox.credentials.awsPairs`, `sandbox.ripgrep` |
| Provided MCP servers | Combines the server names from every source; when two sources set the same name, applies the higher-ranked source's whole entry | `managedMcpServers` |
| Keys read from the highest-ranked source only | Ignores the key in every lower source, even when the highest-ranked source leaves it unset | Credential helpers such as `apiKeyHelper`, login pins such as `forceLoginOrgUUID`, `modelPicker`, `permissions.defaultMode` |
| `env` | Merges per variable across admin sources under either setting, as [Keys read from every admin source](#keys-read-from-every-admin-source) describes | |
| Every other key | Takes the value from the highest-ranked source that sets it | `model`, `cleanupPeriodDays` |

To confirm which sources combined on a machine, [read the `Setting sources` line in `/status`](#read-the-source-in-/status); that section says what each label means.

### Compute the policy with a helper program

A [[All_settings|`policyHelper`]] is an executable your MDM policy or managed settings file names, and Claude Code runs it to compute managed settings at startup. When the selected source configures one and the helper emits a `managedSettings` object, that output changes what Claude Code reads:

* **The emitted `managedSettings` object is the only managed settings for the session**, including for the [keys it otherwise reads from every admin source](#keys-read-from-every-admin-source), apart from [[All_settings|`forceRemoteSettingsRefresh`, which has its own startup rule]]

For which helper runs fail, and what Claude Code does when one does, see [[All_settings|Helper failures]].

<span id="parent-settings-from-embedding-hosts" />

<span id="control-policy-from-an-embedding-host" />

<span id="merge-policy-from-an-embedding-host" />

### Let an embedding host add policy

When another application launches Claude Code, such as Claude Desktop, an IDE extension, or an Agent SDK app, that host can pass its own managed settings through the SDK `managedSettings` option. Claude Code calls these parent settings.

By default, Claude Code ignores parent settings whenever an admin source is present: server-managed settings, an MDM or OS-level policy, or a managed settings file.

To have Claude Code merge parent settings alongside an admin source, set [[All_settings|`parentSettingsBehavior`]] to `"merge"` in the highest-priority managed source; Claude Code reads the key from that source only.

Claude Code then keeps only the host's values that restrict what Claude can do, with one gap to know about: unless you also set the `allowManaged*Only` locks, the host's permission allow rules and sandbox allowlists still apply. See [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Restrict parent settings]] for the locks.

A [[All_settings|`policyHelper`]] can turn parent merging off regardless of this key; its entry says when.

Claude Code also applies these checks to parent-supplied values on their own:

* When any admin source sets `allowManagedPermissionRulesOnly`, Claude Code drops [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|parent-supplied]] permission allow rules and `additionalDirectories` as it reads them, even when a higher-priority source leaves the key unset. The key's effect on your own permission rules comes from the managed settings Claude Code applies, or from parent settings you've chosen to merge
* Claude Code enforces the `forceLoginOrgUUID` or `allowedMcpServers` value in the managed settings it applies and blocks a parent-supplied one. Outside the MCP allowlist lock, a value in a lower admin source that Claude Code doesn't apply neither applies nor blocks the parent's.

  On Claude Code v2.1.273 or later, while `allowManagedMcpServersOnly` is on, the `allowedMcpServers` list from the highest-ranked admin source that sets one applies and blocks the parent's, as a [cross-source key](#keys-read-from-every-admin-source). The parent's list applies only when no admin source sets one. The [[All_settings|`managedSourcesBehavior`]] entry says which source supplies each key under `"merge"`. Before v2.1.223, a value in any admin source blocked the parent's
* For `availableModels`, Claude Code enforces the value in the managed settings it applies and blocks a parent-supplied list
* For `strictKnownMarketplaces`, Claude Code likewise enforces the list in the managed settings it applies and blocks a parent-supplied one. The parent's list applies only when no applied managed source sets one. Requires Claude Code v2.1.282 or later
* For `allowedProviders`, a list in the [selected managed source](#which-managed-source-claude-code-uses) blocks a parent-supplied one, and under the [[All_settings|`managedSourcesBehavior`]] `"merge"` opt-in a list in any admin source does. Requires Claude Code v2.1.285 or later
* A parent-supplied `blockedMarketplaces` applies in addition to any blocklist that a managed source sets. Requires Claude Code v2.1.282 or later

#### Keep Cowork folder access when only managed rules apply

[Cowork](https://claude.com/docs/cowork/overview) in the Claude Desktop app runs its sessions on Claude Code and grants each session access to its working folders, such as the folder the user connects, through allow rules it supplies when it launches the session. When your managed policy sets [[All_settings|`allowManagedPermissionRulesOnly`]], Claude Code keeps only the allow rules in the managed policy: it drops allow rules a host supplies as parent settings, as `--allowedTools`, or in a settings file, so writes to those folders lose their pre-approval. In a Cowork session that asks before edits, Cowork can't show the prompt, and Claude reports each write as blocked because the path resolves to a protected location or a path outside the connected folder.

To restore the writes, add allow rules for those folders to the managed source Claude Code [selects](#precedence-within-the-managed-tier) on those machines: on an MDM-managed fleet, that's the MDM policy rather than a separate managed settings file. This example uses the file form, and an MDM policy takes the same keys. It keeps `allowManagedPermissionRulesOnly` set and allows edits under a `CoworkProjects` folder in each user's home directory; replace the path with the folders your users connect:

```json managed-settings.json theme={null}
{
  "allowManagedPermissionRulesOnly": true,
  "permissions": {
    "allow": [
      "Edit(~/CoworkProjects/**)"
    ]
  }
}
```

After you deploy the policy, Claude can save files under that folder in a new Cowork session. [[Configure_permissions|Read and Edit rules]] cover the path syntax, including the `//` form for absolute paths.

### What a developer can change

A developer's own settings files, `--settings` values, and project files never override a managed value; the [[Settings_files_and_precedence|exceptions]] only let a stricter lower-level value count. These cases sit outside that rule:

* **The model for a session**: a managed `model` is a default, not a lock. `--model` and `ANTHROPIC_MODEL` still pick the model for that session, so deploy [[All_settings|`availableModels`]] to restrict the choice.
* **The auto-compact window for a session**: a managed [[All_settings|`autoCompactWindow`]] is a default too. The `--autocompact` flag and the `CLAUDE_CODE_AUTO_COMPACT_WINDOW` variable still set the [[Model_configuration|auto-compact window]] for that session.
* **Local admin rights**: a developer who is an administrator on the machine can edit the managed source itself, which is why MDM tooling can redeploy the profile or file on a schedule and why the HKLM registry and the macOS managed preferences domain exist.
* **The server-managed cache**: server-managed settings come from Anthropic's servers, and an edit to the local cache [[Configure_server-managed_settings|lasts only until the next successful fetch]].
* **Other tools**: managed settings bind Claude Code only. A developer who calls the API from another tool isn't under them.

<span id="verify-enforcement" />

<span id="verify-that-a-policy-is-in-force" />

## Check that a policy is in force

A developer reports that a policy isn't applying, or you want to confirm a rollout landed before pushing it to the fleet. Two commands on that machine answer it: `/status` shows which managed source Claude Code selected, and `claude doctor` lists what it dropped.

### Read the source in /status

On the developer's machine, run `/status` inside Claude Code and read the `Setting sources` line. When a managed source is in effect, the line lists `Enterprise managed settings` with the source Claude Code selected in parentheses:

* `(remote)`: server-managed settings from claude.ai or a gateway
* `(plist)` or `(HKLM)`: an MDM or OS policy
* `(file)`, `(drop-ins)`, or `(file + drop-ins)`: `managed-settings.json`, the drop-in directory, or both
* `(remote + file, merged)`, or another list ending in `, merged`: your organization [composes every managed source](#compose-every-managed-source), and Claude Code merged the listed sources into the policy. A lower source can still supply `env` variables without appearing in the list. Requires Claude Code v2.1.242 or later
* `(HKCU)`: the user-writable registry fallback
* `(parent process)`: an [embedding host](#let-an-embedding-host-add-policy) supplied restrictive settings
* `(helper)`: a [[All_settings|`policyHelper`]] configured by the selected MDM or file source

When Claude Code found a managed source on the machine and didn't select it, a second line, `Skipped sources`, names each such source. Read it to distinguish a policy that never reached the machine from one that reached it and that a higher-priority source overrode. Requires Claude Code v2.1.242 or later.

When the policy isn't applying, the `Setting sources` line tells you which of two problems you have:

* **The line is missing**: Claude Code found no managed source that delivers a policy key.

  If you deployed a managed settings file, check that it sits at the path for the OS and that it contains a [policy key](#how-claude-code-combines-managed-sources) rather than only the control keys. A file that isn't valid JSON doesn't produce this state; Claude Code [refuses to start](#find-entries-claude-code-dropped) instead.

  When you deployed through server-managed settings instead, run `claude doctor`, which reports the [[Configure_server-managed_settings|fetch outcome]].
* **The line names a source other than the one you deployed**: a higher-priority source is present and Claude Code ignored yours, and `Skipped sources` lists it. [How Claude Code combines managed sources](#how-claude-code-combines-managed-sources) gives the order.

<span id="invalid-entries-in-managed-settings" />

### Find entries Claude Code dropped

If your managed settings file, MDM profile, registry value, or server-managed payload fails schema validation, Claude Code first skips each individual entry it can repair, such as one invalid permission rule, and warns about each one. Claude Code then drops any value that still fails, unless the value belongs to one of the keys that [fail closed](#keys-that-fail-closed) instead.

Claude Code is stricter with the `managedSettings` a [[All_settings|`policyHelper`]] emits: it makes the same entry repairs, but any schema violation that survives fails the whole helper run, and at startup Claude Code refuses to start, the same as for a helper that exits non-zero.

When a managed settings file, drop-in file, MDM plist, or HKLM registry value is present but can't be parsed as a JSON object, Claude Code refuses to start and prints [[Error_reference|an error naming the source]], even when another admin source delivers a valid policy. Each source fails this way when:

* **Managed settings file or drop-in file**: the file isn't valid JSON, or its top level isn't an object
* **MDM plist**: macOS's `plutil` reports the plist malformed, or its converted content isn't a JSON object
* **HKLM registry value**: the `Settings` value isn't a string, is empty, or doesn't hold a JSON object

Three source states don't cause this refusal:

* An absent file, profile, or registry value isn't a failure; Claude Code runs without that source.
* An empty managed settings file counts as `{}`.
* A malformed value in the user-writable HKCU registry key never blocks launch. Claude Code reports it as a notice in `/status` and `claude doctor` instead.

When a managed settings file, drop-in file, `managed-settings.d/` directory, MDM profile, or HKLM registry value exists but can't be read, and no admin source supplies a policy, what happens depends on why the read failed:

* If the operating system denied the read, for example on a root-only file, every session starts without that source's policies. `/status` and `claude doctor` record the failure, and a run with `-p` also prints it to stderr.
* For any other read failure, such as an I/O error, every session exits at startup with [[Error_reference|a message to contact an administrator]].

To find a dropped entry, look in one of three places:

* Interactive sessions show a dialog at startup listing the invalid entries.
* Non-interactive runs with `-p` print a summary to stderr.
* [[Debug_your_configuration|`claude doctor`]] lists each invalid entry with its source and field.

#### Keys that fail closed

When a managed source sets a top-level key that has a single restrictive value, such as `allowManagedPermissionRulesOnly`, `disableAutoMode`, or `skipDangerousModePermissionPrompt`, to something Claude Code can't read, the key reads as that value until you fix it. The report says the key `was present but invalid` and names the value Claude Code treats it as. For a key inside `sandbox`, see [Invalid values inside `sandbox`](#invalid-values-inside-sandbox).

These cases don't fail closed:

* A `null` removes the key.
* An invalid `disableAllHooks`, even a quoted boolean, is dropped with a warning, because enforcing `true` would also unload the hooks your own managed settings deploy.
* For every other boolean key the rule covers, the string `"true"` or `"false"` reads as that boolean, with a notice in `/status` asking you to drop the quotes.

Claude Code repairs the `permissions`, `autoMode`, `worktree`, and `attribution` blocks per field instead of dropping them whole:

* A lock inside one, such as `permissions.disableBypassPermissionsMode`, reads as its restrictive value.
* An invalid `permissions.defaultMode` reads as `default`.
* While a `deny` or `ask` list in `permissions` can't be read at all, Claude Code withholds `allow` and `additionalDirectories`, so the grants never apply without the restrictions written beside them. The report names each withheld grant and the list that couldn't be read.
* In `autoMode`, a `soft_deny` or `hard_deny` list that can't be read, or that lost an invalid entry, withholds `allow` and `environment` the same way.

The fail-closed rule for keys with a single restrictive value and the per-field repairs require Claude Code v2.1.282 or later.

These keys have their own fallback:

| Field | Behavior when present but invalid |
| :- | :- |
| `allowedMcpServers` | Enforced as an empty allowlist until the value is fixed, so no MCP servers that users add are admitted. Servers your organization delivers through [[All_settings|`managedMcpServers`]] still load, and `managed-mcp.json` servers load per [[Control_MCP_server_access_for_your_organization|Servers that skip the allowlist check]]. An individual invalid entry is stripped and the valid subset is enforced. |
| [[All_settings|`allowedProviders`]] | Enforced as an empty allowlist until the value is fixed, so every API provider is refused and Claude Code doesn't start on the machine. If only an individual entry isn't a known provider name, Claude Code drops and reports that entry and enforces the rest. |
| `allowedHttpHookUrls` | Claude Code enforces an empty managed [[All_settings|allowlist]] until you fix the value, so an HTTP hook runs only if another settings file lists its URL. If only an individual entry is invalid, Claude Code strips that entry and enforces the rest. |
| `httpHookAllowedEnvVars` | Claude Code enforces an empty managed [[All_settings|allowlist]] until you fix the value, so a header variable is interpolated only if another settings file names it. If only an individual entry is invalid, Claude Code strips that entry and enforces the rest. |
| `allowedChannelPlugins` | Claude Code enforces an empty allowlist until you fix the value, so no channel plugin passed to `--channels` is admitted. If only an individual entry is invalid, it strips that entry and enforces the rest. |
| `strictKnownMarketplaces` | Enforced as an empty allowlist until the value is fixed, so no [[Manage_Claude_Code_plugins_for_your_organization|marketplace source]] is admitted. An individual entry that is invalid or can't be enforced, such as a `hostPattern` regex that doesn't compile, is stripped and the valid subset is enforced. |
| `availableModels` | Enforced as an empty allowlist until fixed, so only the Default model is available; a non-string entry is stripped and the valid subset enforced. |
| [[All_settings|`availableModelsMatch`]] | Treated as `exact` until the value is fixed. |
| `forceLoginOrgUUID` | No organization is permitted to log in until the value is fixed. |
| `gatewayInternalNetworks` | When the invalid value comes from the highest managed source on the machine, `/login` refuses every new [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|cloud gateway]] sign-in on that machine until the value is fixed. |
| `crossSessionInbound` | Treated as `refuse`, the most restrictive value, so inbound [[Message_your_other_Claude_Code_sessions|cross-session messages]] are refused until the value is fixed. The developer sees [[Error_reference|a warning]]. |
| `deniedMcpServers` | An individual invalid entry is stripped and the valid subset is enforced. A wholly invalid value is dropped with a warning, since denying every server would block servers the policy never named. |
| [[All_settings|`deniedModels`]] | A non-string entry is stripped and the rest of the list is enforced. A wholly invalid value is dropped with a warning and blocks no models until it is fixed. |
| `blockedMarketplaces` | An individual invalid entry is stripped and the valid subset is enforced. An entry that parses but can never match, such as a `hostPattern` regex that doesn't compile, is kept with a warning. It blocks nothing until fixed, but [[Manage_Claude_Code_plugins_for_your_organization|marketplace restrictions]] stay active. A wholly invalid value is dropped with a warning, since blocking every marketplace would block sources the policy never named. |
| `sandbox` | When one value inside the block is invalid, Claude Code doesn't drop the whole block. For what happens to each kind of invalid field, see [Invalid values inside `sandbox`](#invalid-values-inside-sandbox). |
| `sandbox.credentials` | A recoverable invalid entry is degraded to `mode: "deny"` with a warning; an unrecoverable one is stripped; valid entries stay enforced. See [[All_settings|invalid credential entries]]. |
| `strictPluginOnlyCustomization` | Treated as `true`, locking all four surfaces, when the value is neither a boolean nor an array. An array entry that this version doesn't recognize as a surface locks nothing; a status note counts such entries so you can check them for typos. |
| `enabledPlugins` | An invalid entry is dropped with a warning and the other entries stay enforced. A value that isn't a map of plugin IDs, or whose every entry is invalid, is dropped whole with a warning. |

`allowedHttpHookUrls` and `httpHookAllowedEnvVars` merge across settings files, so entries in your user, project, or local settings still apply while the managed list is empty.

The fallbacks for those two keys and for `allowedChannelPlugins` require Claude Code v2.1.267 or later; earlier versions drop the whole key when its value or any entry is invalid. The `strictKnownMarketplaces` and `blockedMarketplaces` fallbacks require Claude Code v2.1.277 or later; earlier versions drop the whole key when its value or any entry is invalid. The `strictPluginOnlyCustomization` and `enabledPlugins` fallbacks require Claude Code v2.1.282 or later.

`requiredMinimumVersion` and `requiredMaximumVersion` fail open by design: an invalid value is dropped rather than enforced.

This tolerance applies only to managed settings. User, project, and local settings files remain strict: a file whose JSON or top-level shape fails validation is rejected as a whole and reported, and an individual entry that fails, such as a malformed permission rule, is skipped with a warning while the rest of the file applies.

#### Invalid values inside `sandbox`

When one value in your managed `sandbox` block is invalid, Claude Code doesn't drop the whole block, because it validates each field on its own. This per-field handling requires Claude Code v2.1.283 or later. On versions before v2.1.283, Claude Code drops every `sandbox` field except [[All_settings|`credentials`]] when a value outside `credentials` is invalid.

The warning you get for an invalid field names the field and tells you what happens to it. What happens depends on what the field controls:

* If you set a Boolean key to a quoted `"true"` or `"false"`, the value counts as that Boolean. Instead of a warning, `/status` shows a notice asking you to remove the quotes.
* If `failIfUnavailable` is invalid, Claude Code drops the value rather than treating it as `true`, so an unreadable value never stops sessions from starting across your fleet.
* Claude Code treats every other invalid Boolean as the value that keeps the sandbox strictest until you fix it. A key that turns the sandbox or one of its restrictions on, such as `enabled` or `network.allowManagedDomainsOnly`, counts as `true`. A key that loosens it, such as `allowUnsandboxedCommands`, counts as `false`.
* In a list outside `credentials`, such as `excludedCommands` or `network.allowedDomains`, Claude Code drops an invalid entry and keeps the rest of the list. A list that isn't an array, or that has no valid entry, doesn't apply at all.
* While `network.deniedDomains` or any entry in it is invalid, Claude Code also withholds `network.allowedDomains`, so the managed allowlist grants nothing until you fix the deny list.
* While `filesystem.denyRead`, `filesystem.denyWrite`, or any entry in either is invalid, Claude Code also withholds both `filesystem.allowRead` and `filesystem.allowWrite` until you fix the deny list.

<span id="managed-only-settings" />

## Keys only a managed source can set

Claude Code reads the following keys only from a managed source; placing them in user or project settings files has no effect.

Most of them are locks: the value a lock governs, such as permission rules or `sandbox.network.allowedDomains`, is an ordinary key that any level can set, and the lock tells Claude Code to honor only the managed value.

The table covers the permission, plugin, and delivery controls. For any key not listed here, the Scope column of the [[All_settings|settings reference]] index says whether it's managed-only.

| Setting | Description |
| :- | :- |
| [[All_settings|`allowAllClaudeAiMcps`]] | Load the claude.ai connectors Claude Code fetches itself alongside a deployed `managed-mcp.json` instead of suppressing them |
| [[All_settings|`allowedChannelPlugins`]] | Allowlist of channel plugins that may push messages. Replaces the default Anthropic allowlist when set. Requires `channelsEnabled: true`. See [[Push_events_into_a_running_session_with_channels|Restrict which channel plugins can run]] |
| [[All_settings|`allowManagedHooksOnly`]] | When `true`, restricts which hooks run; see [[All_settings|what runs under `allowManagedHooksOnly`]] for the full effect list |
| [[All_settings|`allowManagedMcpServersOnly`]] | When `true`, only `allowedMcpServers` from managed settings are respected. `deniedMcpServers` still merges from all sources. See [Keys read from every admin source](#keys-read-from-every-admin-source) for which managed sources can set it, and [[Control_MCP_server_access_for_your_organization|Managed MCP configuration]] |
| [[All_settings|`allowManagedPermissionRulesOnly`]] | Makes managed settings the only settings source of permission rules. The entry lists every source it ignores |
| [[All_settings|`blockedMarketplaces`]] | Blocklist of marketplace sources. Blocked sources are checked before downloading, so they never touch the filesystem. See [[Manage_Claude_Code_plugins_for_your_organization|managed marketplace restrictions]] |
| [[All_settings|`channelsEnabled`]] | Allow [[Push_events_into_a_running_session_with_channels|channels]] for the organization. See [[Push_events_into_a_running_session_with_channels|enterprise controls]] for the default on each plan |
| [[All_settings|`disableCommandPluginSources`]] | When `true`, blocks [[Marketplace_reference|`command` plugin sources]] entirely, so the marketplace-declared command never runs. Also blocks marketplace [[Host_and_maintain_a_marketplace|`headersHelper` commands]], except for a marketplace that managed settings themselves declare. When unset, follows `allowManagedHooksOnly`. Requires Claude Code v2.1.229 or later, and the `headersHelper` block requires v2.1.238 or later |
| [[All_settings|`disableSideloadFlags`]] | Reject the `--plugin-dir`, `--plugin-url`, `--agents`, and `--mcp-config` flags at startup. In cloud sessions, Claude Code instead starts the session and drops the server-delivered `--mcp-config` servers, apart from the exceptions its [[All_settings|reference entry]] lists. Requires Claude Code v2.1.193 or later |
| [[All_settings|`forceRemoteSettingsRefresh`]] | When `true`, blocks CLI startup until remote managed settings are freshly fetched and exits if the fetch fails. See [[Configure_server-managed_settings|fail-closed enforcement]] |
| [[All_settings|`managedMcpServers`]] | Remote MCP servers provided to every user alongside their own. It provides servers rather than locking anything down. See [[Control_MCP_server_access_for_your_organization|Provide servers through managed settings]]. Requires Claude Code v2.1.259 or later |
| [[All_settings|`managedSourcesBehavior`]] | Whether Claude Code applies only the highest-priority managed source or [composes every one of them](#compose-every-managed-source) |
| [[All_settings|`parentSettingsBehavior`]] | Whether host-supplied parent settings merge under the managed policy |
| [[All_settings|`pluginSuggestionMarketplaces`]] | Marketplaces whose plugins Claude Code may suggest to users |
| [[All_settings|`pluginTrustMessage`]] | Custom message appended to the plugin trust warning shown before installation |
| [[All_settings|`policyHelper`]] | Executable that computes managed settings at startup; see [[All_settings|Compute managed settings with a policy helper]] |
| [[All_settings|`sandbox.filesystem.allowManagedReadPathsOnly`]] | When `true`, only `filesystem.allowRead` paths from managed settings are respected. `denyRead` still merges from all sources |
| [[All_settings|`sandbox.network.allowManagedDomainsOnly`]] | Honor only managed `allowedDomains` and `WebFetch(domain:...)` allow rules; block other domains without prompting |
| [[All_settings|`strictKnownMarketplaces`]] | Controls which plugin marketplace sources users can add and install plugins from. See [[Manage_Claude_Code_plugins_for_your_organization|managed marketplace restrictions]] |
| [[All_settings|`strictPluginOnlyCustomization`]] | Block skills, agents, hooks, and MCP servers from user and project sources; `true` locks all four, an array names which |
| [[All_settings|`wslInheritsWindowsSettings`]] | When set in the HKLM registry or a file under `C:\Program Files\ClaudeCode`, have WSL read the Windows policy chain, and read `/etc/claude-code` only when [no Windows admin document is present](#present-admin-documents); the entry gives the order |

<Note>
  On Team and Enterprise plans, an Owner enables or disables [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] and [[Use_Claude_Code_in_the_cloud|cloud sessions]] organization-wide in [Claude Code admin settings](https://claude.ai/admin-settings/claude-code). When an Owner turns Remote Control off, already-connected sessions that run Claude Code v2.1.286 or later disconnect too. Each one disconnects the next time it refreshes your organization's policy, about once an hour. For what happens in those sessions, see [[Continue_local_sessions_from_any_device_with_Remote_Control|`Remote Control was turned off by your organization's policy`]].

  Remote Control can additionally be disabled per device with the [[All_settings|`disableRemoteControl`]] setting. Cloud sessions have no per-device managed settings key.

  To check whether these organization settings reached a given machine, run `claude doctor` there and read the `Organization policy` line, which says where Claude Code loaded the policy from or why it didn't load. Requires Claude Code v2.1.261 or later. In a running session, `/status` shows the same line when the policy didn't load.
</Note>

## Turn telemetry off for your organization

Claude Code sends Anthropic operational [[Data_usage|telemetry]] by default on sessions that use the Anthropic API, whether directly, through an LLM gateway, or through a custom `ANTHROPIC_BASE_URL`; [[Data_usage|Default behaviors by API provider]] says which providers send it. To turn it off for every developer without relying on each person's shell, deliver `DISABLE_TELEMETRY` through the `env` block of your managed settings. This example sets `DISABLE_TELEMETRY` for everyone the policy reaches:

```json theme={null}
{
  "env": {
    "DISABLE_TELEMETRY": "1"
  }
}
```

Claude Code applies a value of `1` without showing the user the [[Configure_server-managed_settings|approval dialog]].

If you turn telemetry off, Claude Code stops sending the usage data that feeds your organization's [[Track_team_usage_with_analytics|analytics dashboard]] for the developers the policy reaches. The variable also turns off [[Environment_variables|feature-flag fetching]] for those developers. For Remote Control, see the [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control requirements]].

[Where and when a policy applies](#where-and-when-a-policy-applies) says which delivery mechanism reaches each surface, and [[Configure_server-managed_settings|Platform availability]] says which sessions skip the server-managed settings fetch.

If your organization uses customer-managed encryption keys and routes Claude Code through a gateway, [[Enterprise_deployment_overview|Configure proxies and gateways]] says why those sessions need this variable.

## See also

* [[Set_up_Claude_Code_for_your_organization|Set up Claude Code for your organization]]: decide what to enforce and how
* [[Configure_server-managed_settings|Server-managed settings]]: deliver policy from the claude.ai console or a gateway
* [[Control_MCP_server_access_for_your_organization|Managed MCP configuration]]: control which MCP servers developers can use
* [[All_settings|All settings]]: every key, with whether a managed source can set it
* [[Example_settings_files|Example settings files]]: a complete `managed-settings.json` showing the shape of the managed keys

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
