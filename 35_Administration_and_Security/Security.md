---
title: "Security"
aliases:
  - "security"
  - "Security"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/security"
status: "verified"
last_updated: "2026-10"
---

# Security

## Executive Summary
> Learn about Claude Code's security safeguards and best practices for safe usage.

## Technical Mechanics & Documentation

## How we approach security

### Security foundation

Your code's security is paramount. Claude Code is built with security at its core, developed according to Anthropic's comprehensive security program. Learn more and access resources (SOC 2 Type 2 report, ISO 27001 certificate, etc.) at [Anthropic Trust Center](https://trust.anthropic.com).

### Permission-based architecture

A session's permission mode sets which actions Claude can take without asking you first. Auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions. [[Choose_a_permission_mode|Which mode a session starts in]] covers earlier versions, other surfaces, and the settings that change the starting permission mode.

* **Auto mode**: A separate classifier model reviews actions instead of you and blocks the ones it judges unsafe. [[Choose_a_permission_mode|How the classifier evaluates actions]] lists which actions Claude Code approves outright, which it sends to the classifier, and which Claude Code still asks you about. Your explicit ask and deny rules still apply, and your organization can [[Choose_a_permission_mode|turn auto mode off]]
* **Manual mode**: Claude Code starts with read-only permissions. When it needs to edit files, run tests, or execute commands, it asks you first, and you choose whether to approve the action once or allow it from then on. It runs a built-in set of [[Configure_permissions|read-only commands]] such as `ls`, `cat`, and `git status` without asking

You and your organization configure these permissions directly. For detailed permission configuration, see [[Configure_permissions|Permissions]].

### Built-in protections

To mitigate risks in agentic systems:

* **Sandboxed bash tool**: [[Configure_the_sandboxed_Bash_tool|Sandbox]] bash commands with filesystem and network isolation, reducing permission prompts while maintaining security. Configure with `/sandbox` to define boundaries where Claude Code can work autonomously
* **Working directory boundary**: In Manual mode, Claude Code asks you before its file tools read or write outside the folder where it was started and its subfolders. The boundary is a permission prompt, so a Bash command you approve can still write anywhere your user account can
  * To read a folder without the prompt, add it as an [[Configure_permissions|additional directory]]
  * To restrict Bash commands at the operating system level, turn on [[Configure_the_sandboxed_Bash_tool|sandboxing]]
* **Prompt fatigue mitigation**: Support for allowlisting frequently used safe commands per-user, per-codebase, or per-organization
* **Accept Edits mode**: Auto-approves file edits and a fixed set of filesystem Bash commands like `mkdir`, `touch`, `rm`, `mv`, `cp`, and `sed` for paths in the working directory. Other Bash commands and out-of-scope paths still prompt

### User responsibility

You're responsible for reviewing proposed code and commands for safety before approval.

## Protect against prompt injection

Prompt injection is a technique where an attacker attempts to override or manipulate an AI assistant's instructions by inserting malicious text. Claude Code includes several safeguards against these attacks:

### Core protections

* **Permission system**: In Manual mode, sensitive operations require explicit approval
* **Network command approval**: Commands that fetch content from the web such as `curl` and `wget` are not auto-approved by default. In Manual mode they prompt like any other non-read-only Bash command, so you can still approve once or add an explicit allow rule like `Bash(curl *)`. To stop Claude from running them, add them to [[Configure_permissions|`permissions.deny`]]. A deny rule matches the command [[Configure_permissions|as written]]; for network enforcement that doesn't depend on the command text, see [[Configure_the_sandboxed_Bash_tool|sandbox network isolation]]

### Privacy safeguards

We have implemented several safeguards to protect your data, including:

* Limited retention periods for sensitive information (see the [Privacy Center](https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-my-data) to learn more)
* Restricted access to user session data
* User control over data training preferences. Consumer users can change their [privacy settings](https://claude.ai/settings/privacy) at any time.

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (for Team, Enterprise, and API users) or [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (for Free, Pro, and Max users) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

### Additional safeguards

* **Network request approval**: In Manual mode, most tools that make network requests require user approval by default
* **Web page summaries**: For most fetches, WebFetch runs a separate model call over the page, and Claude receives that call's answer instead of the raw page. See [[Tools_reference|WebFetch tool behavior]]
* **Trust verification**: In an interactive session, Claude Code shows the workspace trust dialog when you start it in a folder you haven't trusted. Servers in a project's `.mcp.json` have their own approval prompt, and [[Connect_Claude_Code_to_tools_via_MCP|Project scope]] lists the sessions that skip it
  * Note: A `-p` session shows neither prompt. [[Configure_permissions|What runs before you trust a folder]] lists what a repository's files can run there
  * Note: When you start Claude Code directly in your home directory, trust acceptance is held for the current session only and is not written to disk, so the prompt reappears on each launch. There is no setting to persist it. Start Claude Code from a project subdirectory instead, where trust acceptance is saved per directory
* **Command injection detection**: In Manual mode, Claude Code asks before running a Bash command it can't fully analyze. An allow rule for part of a command, such as `Bash(git *)`, doesn't skip that prompt. [[Configure_permissions|Sandboxed commands]] can run without it
* **Fail-closed matching**: In Manual mode, unmatched commands require approval by default
* **Secure credential storage**: API keys and tokens are stored in the macOS Keychain when available. On Linux they're stored in a file with mode `0600`, and on Windows in a file that inherits the access controls of your user profile directory. See [[Authentication|Credential Management]]

<Warning>
  **Windows WebDAV security risk**: When running Claude Code on Windows, we recommend against enabling WebDAV or allowing Claude Code to access paths such as `\\*` that may contain WebDAV subdirectories. [WebDAV has been deprecated by Microsoft](https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features#:~:text=The%20Webclient%20\(WebDAV\)%20service%20is%20deprecated) due to security risks. Enabling WebDAV may allow Claude Code to trigger network requests to remote hosts, bypassing the permission system.
</Warning>

**Best practices for working with untrusted content**:

1. Review suggested commands before approval
2. Avoid piping untrusted content directly to Claude
3. Verify proposed changes to critical files
4. Use virtual machines (VMs) to run scripts and make tool calls, especially when interacting with external web services
5. Report suspicious behavior with `/feedback`

<Warning>
  While these protections significantly reduce risk, no system is completely
  immune to all attacks. Always maintain good security practices when working
  with any AI tool.
</Warning>

## MCP security

You can connect Claude Code to Model Context Protocol (MCP) servers. Project-scoped servers are defined in `.mcp.json`, which you can check into source control. Servers at [[Connect_Claude_Code_to_tools_via_MCP|other scopes]] and [[Connect_Claude_Code_to_tools_via_MCP|claude.ai connectors]] are configured outside the repository, and plugins can add servers too, so reviewing `.mcp.json` doesn't show every server a session can load. To restrict which servers run in your organization, see [[Control_MCP_server_access_for_your_organization|Managed MCP configuration]].

We encourage either writing your own MCP servers or using MCP servers from providers that you trust. You are able to configure Claude Code permissions for MCP servers. Anthropic reviews connectors against its [listing criteria](https://claude.com/docs/connectors/building/review-criteria) before adding them to the [Anthropic Directory](https://claude.ai/directory), but does not security-audit or manage any MCP server.

## IDE security

See [[Use_Claude_Code_in_VS_Code|VS Code security and privacy]] for more information on running Claude Code in an IDE.

## Cloud execution security

When you use [[Use_Claude_Code_in_the_cloud|cloud sessions]], additional security controls are in place. Sessions your organization routes to a [[Self-hosted_environments|self-hosted environment]] run on your own infrastructure, where isolation, network egress, and git credentials are your deployment's responsibility. In Anthropic-hosted environments:

* **Isolated virtual machines**: Each cloud session runs in an isolated, Anthropic-managed VM
* **Network access controls**: Network access is limited by default and can be configured to be disabled or allow only specific domains
* **Credential protection**: GitHub credentials are stored encrypted on Anthropic's servers and never enter the session VM. The VM holds a short-lived credential scoped to that session, and GitHub traffic goes through an [[Configure_cloud_environments|Anthropic proxy]] that attaches the GitHub credential on the server side. See [[Use_Claude_Code_in_the_cloud|GitHub authentication options]] for how you grant access
* **Push restrictions**: The [[Configure_cloud_environments|GitHub proxy]] rejects branch deletions and pushes of anything other than a branch, such as a tag. GitHub decides which branches a session can update by applying your repository's branch protection rules and rulesets to the GitHub access you connected. A rule that access can bypass doesn't block a session's push
* **Audit logging**: All operations in cloud sessions are logged for compliance and audit purposes
* **Automatic cleanup**: Session VMs are reclaimed after a period of inactivity
* **Deletion**: You can [[Use_Claude_Code_in_the_cloud|delete a session]] at any time. See [[Data_usage|Cloud execution data flow]] for what Anthropic stores for a cloud session

For more details on cloud execution, see [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]]; to configure network access for cloud sessions, see [[Configure_cloud_environments|Configure cloud environments]].

[[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] sessions work differently: the web interface connects to a Claude Code process running on your local machine. All code execution and file access stays local, and session traffic travels through the Anthropic API over TLS; while connected, the session transcript is stored on Anthropic servers to sync the conversation across devices, as described in [[Continue_local_sessions_from_any_device_with_Remote_Control|Connection and security]]. No cloud VMs or sandboxing are involved. The connection uses multiple short-lived, narrowly scoped credentials, each limited to a specific purpose and expiring independently, to limit the blast radius of any single compromised credential.

## Security best practices

### Working with sensitive code

* Review all suggested changes before approval
* Use project-specific permission settings for sensitive repositories
* For additional isolation, run the whole Claude Code (local mode) process inside the [[Choose_a_sandbox_environment|sandbox runtime]] or a [[Development_containers|dev container]]
* Regularly audit your permission settings with `/permissions`

### Team security

* Use [[Settings_files_and_precedence|managed settings]] to enforce organizational standards
* Share approved permission configurations through version control
* Train team members on security best practices
* Monitor Claude Code usage through [[Monitoring|OpenTelemetry metrics]]
* Audit or block settings changes during sessions with [[Hooks_reference|`ConfigChange` hooks]]

### Reporting security issues

If you discover a security vulnerability in Claude Code:

1. Do not disclose it publicly
2. Report it through our [HackerOne program](https://hackerone.com/4f1f16ba-10d3-4d09-9ecc-c721aad90f24/embedded_submissions/new)
3. Include detailed reproduction steps
4. Allow time for us to address the issue before public disclosure

## Related resources

* [[Catch_security_issues_as_Claude_writes_code|Security guidance plugin]]: have Claude review and fix vulnerabilities in its own code changes during the session
* [[Commands|`/security-review`]]: run an on-demand security pass over the changes on your current branch
* [[Choose_a_sandbox_environment|Sandbox environments]]: compare isolation approaches and choose one for your threat model
* [[Configure_the_sandboxed_Bash_tool|Sandboxing]]: filesystem and network isolation for Bash commands
* [[Configure_permissions|Permissions]]: configure permissions and access controls
* [[Monitoring|Monitoring usage]]: track and audit Claude Code activity
* [[Development_containers|Development containers]]: secure, isolated environments
* [Anthropic Trust Center](https://trust.anthropic.com): security certifications and compliance
* [CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai): a security leader's framework for assessing agentic AI deployments

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
