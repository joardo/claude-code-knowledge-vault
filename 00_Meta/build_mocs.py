#!/usr/bin/env python3
"""
MOC (Maps of Content) Generator for Claude Code Obsidian Vault.
Builds the central graph entrypoints and category-specific MOCs.
"""

import os

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOC_DIR = os.path.join(VAULT_DIR, "00_MOC")
os.makedirs(MOC_DIR, exist_ok=True)

mocs = {}

mocs["MOC_Claude_Code.md"] = """---
title: "Master Map of Content - Claude Code Platform"
aliases:
  - "MOC_Claude_Code"
  - "Claude Code Index"
  - "Master MOC"
tags:
  - "claude-code"
  - "moc"
  - "index"
status: "verified"
last_updated: "2026-10"
---

# Master Map of Content: Claude Code Platform

> The central nexus and master index for the official Claude Code documentation knowledge vault. This vault is organized according to Open Knowledge atomic note principles with dense bidirectional `[[wikilinks]]`.

---

## Knowledge Domains (Category MOCs)

Explore the Claude Code ecosystem across 9 specialized structural domains:

1. [[MOC_Core_Architecture|Core Architecture & Foundations]]
   - The agentic loop (Gather -> Act -> Verify), context window mechanics, prompt caching hit-rates, model tiers (Sonnet, Opus, Haiku), advisor tool, checkpointing, and permissions foundations.
2. [[MOC_CLI_and_Runtime|CLI Commands & Terminal Runtime]]
   - Command-line flags (`-p`, `-c`, `-r`, `--dangerously-skip-permissions`), slash commands (`/compact`, `/doctor`, `/rewind`, `/clear`), REPL shortcuts, session persistence, and terminal ergonomics.
3. [[MOC_Memory_and_Context|Memory, Context & Configuration]]
   - `CLAUDE.md` and `AGENTS.md` hierarchy, auto-memory (`MEMORY.md`), `settings.json` scopes and precedence, output styles, and prompt caching economics.
4. [[MOC_Extensibility_and_MCP|Extensibility, MCP & Plugins]]
   - Model Context Protocol (MCP) servers, tool schemas, channels, custom skills, full-featured plugins, mods interface, and private/public marketplaces.
5. [[MOC_Hooks_and_Automation|Lifecycle Hooks & Event Automation]]
   - Deterministic event triggers (`pre-tool-use`, `post-tool-use`, `stop`, `prompt`), JSON payloads, validation scripts, security guardrails, `/loop` and cron scheduling.
6. [[MOC_Workflows_and_Patterns|Agentic Workflows & Multi-Agent Coordination]]
   - Parallel subagents, worktree git isolation, agent view, agent teams, cross-session messaging, autonomous `/goal`, headless scripting, CI/CD pipelines, and cloud routines.
7. [[MOC_Agent_SDK|Claude Agent SDK (Python & TypeScript)]]
   - Programmatic agent building, custom in-process tools, structured outputs (Pydantic/Zod), streaming events, session storage persistence, and telemetry.
8. [[MOC_Administration_and_Security|Enterprise Administration, Gateways & Security]]
   - Organization setup, managed settings, server-managed policies, Claude apps gateway, AWS Bedrock, Google Cloud, Microsoft Foundry, HIPAA compliance, and Zero Data Retention.
9. [[MOC_Release_Notes|Platform Changelogs & Weekly Releases]]
   - Historical release digests from 2026-w13 through 2026-w37 documenting the evolution of Claude Code capabilities.

---

## Decision Trees & Selection Matrices

When choosing the optimal tool, execution mode, or architecture for your goal, consult the comparative matrices:

- [[Matrix_Execution_Modes|Execution Modes: Interactive vs Headless vs Loop vs Multi-Agent]]
- [[Matrix_Extensibility|Extensibility Options: Skills vs Slash Commands vs MCP vs Hooks vs Plugins vs Mods]]
- [[Matrix_Memory_Architectures|Memory Hierarchy: Root CLAUDE.md vs Nested vs Auto-Memory vs Ephemeral]]
- [[Matrix_Tool_Approval_and_Security|Security & Approval: Interactive vs Auto-Mode vs Sandbox vs Devcontainers]]
- [[Matrix_Agentic_Coordination|Multi-Agent Coordination: Inline vs Subagents vs Worktrees vs Agent Teams]]

---

## Master Agent Skill

- [[claude-platform-master/SKILL|Claude Platform Master Skill (`SKILL.md`)]]: Autonomous consultant skill designed to triage any user goal and recommend the optimal combination of Claude Code features, flags, tools, and extensions.
- [[capability_cheat_sheet|Claude Capabilities Exhaustive Cheat Sheet]]

---

## Vault Statistics & Graph Audit

- [[Vault_Statistics_and_Audit|Vault Statistics & Link Integrity Audit Report]]
"""

mocs["MOC_Core_Architecture.md"] = """---
title: "MOC: Core Architecture & Foundations"
aliases:
  - "MOC_Core_Architecture"
tags:
  - "claude-code"
  - "moc"
  - "architecture"
status: "verified"
last_updated: "2026-10"
---

# MOC: Core Architecture & Foundations

> Architectural mechanics governing Claude Code's agentic loop, context window budgeting, prompt caching, model tiers, and tool execution engines.

## 1. The Agentic Loop & Reasoning
- [[How_Claude_Code_works|How Claude Code works]]: The fundamental three-phase cycle (Gather Context -> Take Action -> Verify Results), agentic harness structure, and user steering.
- [[Model_configuration|Model Configuration]]: Selecting Sonnet, Opus, and Haiku tiers, effort levels (`low`, `medium`, `high`, `xhigh`), and token parameters.
- [[Escalate_hard_decisions_with_the_advisor_tool|Advisor Tool]]: Autonomous escalation protocol pairing primary models with a secondary reasoning advisor.

## 2. Context Window & Memory Economics
- [[Explore_the_context_window|Explore the Context Window]]: Context budget dynamics, system prompt allocations, tool result overhead, and automatic context compacting.
- [[How_Claude_Code_uses_prompt_caching|Prompt Caching Mechanics]]: 5-minute caching TTL, breakpoint rules, cache write/read cost differences, and cache-friendly practices.

## 3. Sandboxing & Safety Architecture
- [[Configure_permissions|Configure Permissions]]: Fine-grained permission rules, tool allowlists, and execution boundaries.
- [[Choose_a_permission_mode|Choose a Permission Mode]]: Interactive mode, auto mode classifier, accept-edits mode, and bypass mode.
- [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash Tool]]: Containerized command execution, network egress limits, and filesystem jails.
- [[Choose_a_sandbox_environment|Sandbox Environments]]: Comparative breakdown of local sandbox, devcontainers, Docker, and VM boundaries.
- [[Tools_reference|Tools Reference]]: Complete reference of built-in file operations, search regex, shell execution, and web tools.
- [[Checkpointing|Checkpointing & State Rewind]]: Snapshotting file modifications and rolling back conversation states.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_CLI_and_Runtime|CLI & Runtime]]
- [[Matrix_Tool_Approval_and_Security|Security & Approval Matrix]]
"""

mocs["MOC_CLI_and_Runtime.md"] = """---
title: "MOC: CLI Commands & Terminal Runtime"
aliases:
  - "MOC_CLI_and_Runtime"
tags:
  - "claude-code"
  - "moc"
  - "cli"
status: "verified"
last_updated: "2026-10"
---

# MOC: CLI Commands & Terminal Runtime

> The operational surface of Claude Code: terminal commands, flags, slash commands, REPL controls, and interactive ergonomics.

## 1. Primary Entrypoints & References
- [[Overview|Overview of Claude Code]]: System capabilities across CLI, Desktop, IDE, and Cloud.
- [[Quickstart|Quickstart Guide]]: Initial installation, login, first command, and interactive onboarding.
- [[CLI_reference|CLI Reference]]: Exhaustive guide to commands (`claude`, `claude -p`, `claude -c`, `claude -r`, `claude auth`, `claude agents`, `claude daemon`).
- [[Commands|Built-in Commands & Slash Commands]]: Complete list of in-session commands (`/compact`, `/doctor`, `/cost`, `/rewind`, `/clear`, `/bug`, `/resume`, `/config`).
- [[Environment_variables|Environment Variables Reference]]: Environment variable controls for models, API endpoints, telemetry, and paths.

## 2. Interactive REPL & Session Management
- [[Interactive_mode|Interactive Mode]]: Keybindings, Shift+Tab mode switching, multi-line prompts, shell-escape (`!`), and command completion.
- [[Manage_sessions|Manage Sessions]]: Resuming sessions via `--resume` or `--continue`, naming sessions, PR correlation, and transcript export.
- [[Common_workflows|Common Workflows]]: Step-by-step terminal guides for code exploration, refactoring, test fixes, and documentation generation.
- [[Prompt_library|Prompt Library]]: Battle-tested prompt recipes categorized by engineering role.
- [[Best_practices_for_Claude_Code|Best Practices for Claude Code]]: Guidelines for pacing, token efficiency, verification, and commit hygiene.

## 3. Terminal Customization & Ergonomics
- [[Configure_your_terminal_for_Claude_Code|Configure Your Terminal]]: Newline keybindings, bell notifications, tmux integration, and Vim mode.
- [[Fullscreen_rendering|Fullscreen Rendering]]: Flicker-free terminal canvas with mouse support.
- [[Customize_your_status_line|Customize Your Status Line]]: Real-time status bar tracking context window consumption, costs, and git status.
- [[Customize_keyboard_shortcuts|Customize Keyboard Shortcuts]]: Custom keybindings configuration file syntax.
- [[Voice_dictation|Voice Dictation]]: Hands-free voice input via push-to-talk.
- [[Use_Claude_Code_with_a_screen_reader|Accessibility & Screen Readers]]: Screen reader compatibility mode.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Memory_and_Context|Memory & Context]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
"""

mocs["MOC_Memory_and_Context.md"] = """---
title: "MOC: Memory, Context & Configuration"
aliases:
  - "MOC_Memory_and_Context"
tags:
  - "claude-code"
  - "moc"
  - "memory"
status: "verified"
last_updated: "2026-10"
---

# MOC: Memory, Context & Configuration

> How Claude Code accumulates persistent project knowledge, reads multi-tier configuration, and controls behavioral persona.

## 1. Project Memory & Conventions
- [[How_Claude_remembers_your_project|How Claude Remembers Your Project]]: The authoritative guide to `CLAUDE.md`, `AGENTS.md`, and auto-memory (`MEMORY.md`).
- [[Explore_the_claude_directory|Explore the .claude Directory]]: Architectural layout of project-local `.claude/` vs global `~/.claude/` directories.
- [[Output_styles|Output Styles]]: Customizing personality, brevity, and tone (Concise, Explanatory, Custom).

## 2. Settings & Precedence Architecture
- [[Settings_files_and_precedence|Settings Files & Precedence]]: 5-tier settings hierarchy (Enterprise Managed -> Project `.claude/settings.json` -> User `~/.claude/settings.json` -> CLI Flags).
- [[All_settings|All Settings Reference]]: Complete schema reference of every key in `settings.json`.
- [[Example_settings_files|Example Settings Files]]: Production settings templates for solo developers, teams, and enterprise orgs.
- [[Configure_cloud_environments|Configure Cloud Environments]]: Cloud VM runner environments, secrets, and setup scripts.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Core_Architecture|Core Architecture]]
- [[Matrix_Memory_Architectures|Memory Hierarchy Matrix]]
"""

mocs["MOC_Extensibility_and_MCP.md"] = """---
title: "MOC: Extensibility, MCP & Plugins"
aliases:
  - "MOC_Extensibility_and_MCP"
tags:
  - "claude-code"
  - "moc"
  - "extensibility"
  - "mcp"
status: "verified"
last_updated: "2026-10"
---

# MOC: Extensibility, MCP & Plugins

> Extending Claude Code's capabilities through Model Context Protocol (MCP), custom skills, modular plugins, and terminal UI mods.

## 1. Model Context Protocol (MCP)
- [[Connect_to_MCP_servers|Connect to MCP Servers Quickstart]]: Fast setup for stdio and HTTP/SSE MCP servers.
- [[Connect_Claude_Code_to_tools_via_MCP|Connect Claude Code to Tools via MCP]]: Comprehensive guide to MCP configurations, authentication, and custom servers.
- [[Control_MCP_server_access_for_your_organization|Managed MCP Configuration]]: Enterprise restriction allowlists and global server distribution.

## 2. Skills & Custom Commands
- [[Extend_Claude_with_skills|Extend Claude with Skills]]: Authoring custom reusable skills, YAML metadata, and slash commands.
- [[Share_session_output_as_artifacts|Share Session Output as Artifacts]]: Generating interactive web artifacts and sharing links.

## 3. Plugins Ecosystem
- [[Plugins_overview|Plugins Overview]]: Understanding the plugin packaging model.
- [[Install_and_manage_plugins|Install and Manage Plugins]]: Installing from registries, local paths, and git repos.
- [[Anthropics_marketplaces|Anthropic's Marketplaces]]: Official, community, and partner marketplaces.
- [[Code_intelligence_plugins|Code Intelligence Plugins]]: Integrating Language Server Protocol (LSP) for compiler diagnostics and symbol search.
- [[Create_a_Claude_Code_plugin|Create a Claude Code Plugin]]: Step-by-step authoring of new plugins.
- [[Add_components_to_a_plugin|Add Components to a Plugin]]: Bundling skills, hooks, and MCP servers into single packages.
- [[Plugin_dependencies|Plugin Dependencies]]: SemVer dependency resolution.
- [[Test_plugins_with_evals|Test Plugins with Evals]]: Automated test suites and performance evaluation.
- [[Publish_and_distribute_a_plugin|Publish and Distribute a Plugin]]: Releasing to marketplaces.
- [[Plugin_manifest_reference|Plugin Manifest Reference]]: Complete `plugin.json` schema.

## 4. Mods (UI & Event Interceptors)
- [[Mods_overview|Mods Overview]]: Enhancing the terminal interface and tool interceptors.
- [[Mod_Create_a_mod|Create a Mod]]: Writing custom JavaScript/TypeScript mods.
- [[Mods_reference|Mods Reference]]: Mod APIs, lifecycle hooks, and render targets.
- [[Mod_Draw_in_the_interface_with_a_mod|Draw in Interface]]: Custom panels, status bars, and UI widgets.
- [[Mod_React_to_events_with_a_mod|React to Events]]: Intercepting prompts, tool calls, and LLM turns.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Hooks_and_Automation|Hooks & Automation]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
"""

mocs["MOC_Hooks_and_Automation.md"] = """---
title: "MOC: Lifecycle Hooks & Event Automation"
aliases:
  - "MOC_Hooks_and_Automation"
tags:
  - "claude-code"
  - "moc"
  - "hooks"
  - "automation"
status: "verified"
last_updated: "2026-10"
---

# MOC: Lifecycle Hooks & Event Automation

> Deterministic control planes: lifecycle hooks, push notification channels, and recurring background scheduling.

## 1. Lifecycle Hooks
- [[Automate_actions_with_hooks|Automate Actions with Hooks]]: Practical guide to triggering shell scripts, linters, notifications, and validators.
- [[Hooks_reference|Hooks Reference]]: Exhaustive reference for all hook events (`PreToolUse`, `PostToolUse`, `Prompt`, `Stop`), JSON input/output schemas, exit codes, and async hooks.

## 2. Channels (Push Events into Sessions)
- [[Push_events_into_a_running_session_with_channels|Push Events with Channels Guide]]: Ingesting external events (webhooks, alerts, chat) into live sessions.
- [[Channels_reference|Channels Reference]]: The MCP channel contract, notification events, and reply tools.

## 3. Scheduling & Background Loops
- [[Run_prompts_on_a_schedule|Run Prompts on a Schedule]]: Scheduling recurring checks with `/loop`, cron expressions, and timers.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns]]
- [[Matrix_Extensibility|Extensibility Matrix]]
"""

mocs["MOC_Workflows_and_Patterns.md"] = """---
title: "MOC: Agentic Workflows & Multi-Agent Coordination"
aliases:
  - "MOC_Workflows_and_Patterns"
tags:
  - "claude-code"
  - "moc"
  - "workflows"
  - "multi-agent"
status: "verified"
last_updated: "2026-10"
---

# MOC: Agentic Workflows & Multi-Agent Coordination

> Strategies for single-agent autonomy, multi-agent swarms, headless automation, and platform integrations.

## 1. Multi-Agent & Parallel Execution
- [[Run_agents_in_parallel|Run Agents in Parallel]]: Comparative overview of subagents, agent view, agent teams, and worktrees.
- [[Create_custom_subagents|Create Custom Subagents]]: Task-specific subagents with isolated context windows.
- [[Manage_multiple_agents_with_agent_view|Agent View]]: Dispatching and monitoring multiple background sessions from one dashboard.
- [[Orchestrate_teams_of_Claude_Code_sessions|Agent Teams]]: Inter-agent coordination, shared tasks, and cross-session messaging.
- [[Message_your_other_Claude_Code_sessions|Cross-Session Messaging]]: Sending peer messages between running Claude Code instances.
- [[Run_parallel_sessions_with_worktrees|Worktree Git Isolation]]: Zero-collision parallel branch execution using Git worktrees.
- [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Dynamic Workflows]]: Programmatically generating subagent orchestration scripts.

## 2. Autonomous Execution & Scripting
- [[Keep_Claude_working_toward_a_goal|Autonomous Goal (/goal)]]: Long-running completion criteria that prevent premature exit.
- [[Run_Claude_Code_programmatically|Run Claude Code Programmatically (Headless)]]: Scripting `claude -p` in bash and pipelines.
- [[Launch_sessions_from_links|Deep Links (`claude-cli://`)]]: One-click session launch from URLs.

## 3. Code Review & CI/CD
- [[Code_Review|Automated Code Review]]: Multi-agent PR review pipelines.
- [[Find_bugs_with_ultrareview|Ultrareview]]: Cloud-based deep bug analysis.
- [[Claude_Code_GitHub_Actions|GitHub Actions]]: Automated bot integration for issues and PRs.
- [[Claude_Code_GitLab_CICD|GitLab CI/CD]]: GitLab pipeline integration.
- [[Catch_security_issues_as_Claude_writes_code|Security Guidance Plugin]]: Real-time vulnerability patching.
- [[Scan_your_codebase_for_vulnerabilities|Claude Security]]: In-session repository security auditing.

## 4. Platforms & Interfaces
- [[Platforms_and_integrations|Platforms Overview]]: Choosing between CLI, Desktop, Web, IDEs, and Mobile.
- [[Desktop_application|Claude Code Desktop]]: Multi-pane visual workspace, app previews, and iOS simulator.
- [[Use_Claude_Code_in_VS_Code|VS Code Extension]]: Inline diffs and editor integration.
- [[JetBrains_IDEs|JetBrains Integration]]: IntelliJ, PyCharm, and WebStorm support.
- [[Use_Claude_Code_with_Chrome|Chrome Integration]]: Browser automation, DOM testing, and console log capture.
- [[Let_Claude_use_your_computer_from_the_CLI|Computer Use]]: GUI desktop automation from terminal.
- [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]: Controlling terminal sessions from web/mobile.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Agent_SDK|Agent SDK]]
- [[Matrix_Agentic_Coordination|Agentic Coordination Matrix]]
"""

mocs["MOC_Agent_SDK.md"] = """---
title: "MOC: Claude Agent SDK"
aliases:
  - "MOC_Agent_SDK"
tags:
  - "claude-code"
  - "moc"
  - "sdk"
status: "verified"
last_updated: "2026-10"
---

# MOC: Claude Agent SDK

> Building production-grade autonomous AI agents using Claude Code as a programmatic library in Python and TypeScript.

## 1. Architecture & Core Concepts
- [[Agent_SDK_overview|Agent SDK Overview]]: Architecture of Claude Code as a library.
- [[Agent_SDK_Quickstart|SDK Quickstart]]: First agent script in Python and TypeScript.
- [[Agent_SDK_How_the_agent_loop_works|How the Agent Loop Works]]: In-depth lifecycle of SDK turns, context, and message streaming.
- [[Agent_SDK_Use_Claude_Code_features_in_the_SDK|Use Claude Code Features in SDK]]: Loading `CLAUDE.md`, skills, and hooks programmatically.

## 2. Tools & Custom Extensions
- [[Agent_SDK_Give_Claude_custom_tools|Custom In-Process Tools]]: Exposing internal functions and APIs directly as agent tools.
- [[Agent_SDK_Connect_to_external_tools_with_MCP|MCP in the SDK]]: Connecting external MCP servers.
- [[Agent_SDK_Scale_to_many_tools_with_tool_search|Tool Search]]: Handling 1,000+ tools with dynamic vector discovery.
- [[Agent_SDK_Subagents_in_the_SDK|Subagents in SDK]]: Programmatic subagent delegation.

## 3. Input, Output & State
- [[Agent_SDK_Streaming_Input|Streaming Input]]: Single mode vs streaming input patterns.
- [[Agent_SDK_Stream_responses_in_real-time|Real-Time Streaming Output]]: Consuming token and tool event streams.
- [[Agent_SDK_Get_structured_output_from_agents|Structured Outputs]]: Guaranteed JSON validation via Pydantic and Zod.
- [[Agent_SDK_Work_with_sessions|Sessions Management]]: Saving, resuming, and branching programmatic sessions.
- [[Agent_SDK_Persist_sessions_to_external_storage|External Session Storage]]: Mirroring transcripts to Redis, S3, or PostgreSQL.

## 4. References & Guides
- [[Agent_SDK_reference_-_Python|Python SDK Reference]]
- [[Agent_SDK_reference_-_TypeScript|TypeScript SDK Reference]]
- [[Agent_SDK_Hosting_the_Agent_SDK|Hosting & Deployment in Production]]

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
"""

mocs["MOC_Administration_and_Security.md"] = """---
title: "MOC: Enterprise Administration, Gateways & Security"
aliases:
  - "MOC_Administration_and_Security"
tags:
  - "claude-code"
  - "moc"
  - "enterprise"
  - "security"
status: "verified"
last_updated: "2026-10"
---

# MOC: Enterprise Administration, Gateways & Security

> Governance, compliance, cloud infrastructure providers, and policy enforcement across engineering teams.

## 1. Enterprise Setup & Centralized Governance
- [[Set_up_Claude_Code_for_your_organization|Organization Setup Guide]]: Administrator decision tree for company-wide rollouts.
- [[Deploy_managed_settings|Deploy Managed Settings]]: Operating system delivery policies (MDM, GPO, filesystem lock).
- [[Configure_server-managed_settings|Server-Managed Settings]]: Dynamic centralized policy distribution without MDM.
- [[Manage_costs_effectively|Manage Costs Effectively]]: Token budget enforcement, telemetry, and spend caps.

## 2. Gateways & Cloud Providers
- [[Run_Claude_Code_through_a_gateway|Run Claude Code Through a Gateway]]: Architectural overview of self-hosted enterprise proxies.
- [[Claude_apps_gateway_configuration|Claude Apps Gateway Configuration]]: `gateway.yaml` reference for OIDC SSO, telemetry, and upstream routing.
- [[Claude_Code_on_Amazon_Bedrock|Claude Code on Amazon Bedrock]]: AWS IAM setup and VPC endpoints.
- [[Claude_Code_on_Google_Clouds_Agent_Platform|Claude Code on Google Cloud's Agent Platform]]: GCP Service Account integration.
- [[Claude_Code_on_Microsoft_Foundry|Claude Code on Microsoft Foundry]]: Azure AI Foundry configuration.

## 3. Compliance & Security Boundaries
- [[Security|Security Safeguards]]: Anthropic's multi-layered security architecture.
- [[Zero_data_retention|Zero Data Retention (ZDR)]]: ZDR policies and enterprise qualification.
- [[Set_up_Claude_Code_local_mode_for_a_HIPAA-ready_organization|HIPAA Compliance Setup]]: Hardening local developer machines for HIPAA compliance.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[Matrix_Tool_Approval_and_Security|Tool Approval Matrix]]
"""

mocs["MOC_Release_Notes.md"] = """---
title: "MOC: Platform Changelogs & Weekly Releases"
aliases:
  - "MOC_Release_Notes"
tags:
  - "claude-code"
  - "moc"
  - "changelog"
status: "verified"
last_updated: "2026-10"
---

# MOC: Platform Changelogs & Weekly Releases

> Weekly digests and feature chronicles of Claude Code.

## Master Changelog
- [[Claude_Code_changelog|Full Claude Code Changelog]]
- [[Release_Whats_new|Weekly Digests Hub]]

## 2026 Weekly Digests
- [[Release_2026-w37|Week 37 · Sept 2026]]: Plugin evals, pop-out desktop panes.
- [[Release_2026-w36|Week 36 · Sept 2026]]: Claude Fable 5.1, desktop background computer use, live `/diff`.
- [[Release_2026-w35|Week 35 · Aug 2026]]: Resume terminal in desktop, draft feedback reports, restricted mode.
- [[Release_2026-w34|Week 34 · Aug 2026]]: `/design` skill artboards, concise output style, mobile remote trigger.
- [[Release_2026-w33|Week 33 · Aug 2026]]: Auto-continue limits, default fork mode, GitLab merge requests.
- [[Release_2026-w32|Week 32 · Aug 2026]]: Cross-session messaging, self-hosted environments, default auto-mode.
- [[Release_2026-w30|Week 30 · July 2026]]: Opus 5 default, iOS simulator pane, Claude Security plugin.
- [[Release_2026-w29|Week 29 · July 2026]]: MCP connectors in artifacts, screen reader mode.
- [[Release_2026-w28|Week 28 · July 2026]]: Desktop built-in browser, `/doctor` diagnostics.
- [[Release_2026-w27|Week 27 · June 2026]]: Sonnet 5 default, Claude in Chrome GA, background subagents, Linux desktop.
- [[Release_2026-w26|Week 26 · June 2026]]: `claude mcp login`, shell output reply with `!`, `/rewind`.
- [[Release_2026-w25|Week 25 · June 2026]]: Artifacts publishing, param-matching deny rules, `/config`.
- [[Release_2026-w24|Week 24 · June 2026]]: Session `/cd`, recursive subagent spawning, safe mode.
- [[Release_2026-w23|Week 23 · June 2026]]: Auto-mode on Bedrock/GCP/Foundry, acceptEdits mode, version ranges.
- [[Release_2026-w22|Week 22 · May 2026]]: Opus 4.8, dynamic workflows, security-guidance plugin, fast mode.
- [[Release_2026-w21|Week 21 · May 2026]]: Auto-mode on Pro & Sonnet 4.6, `/usage` attribution, `/code-review`.
- [[Release_2026-w20|Week 20 · May 2026]]: Agent view multi-session manager, `/goal` loop condition, Opus 4.7.
- [[Release_2026-w19|Week 19 · May 2026]]: Zip/URL plugins, Ctrl+R history, remote branch worktrees, hard deny rules.
- [[Release_2026-w18|Week 18 · Apr 2026]]: Windows without Git Bash, pasted OAuth login, `claude project purge`, PR resume.
- [[Release_2026-w17|Week 17 · Apr 2026]]: `/ultrareview`, terminal return recaps, custom color themes, redesigned web.
- [[Release_2026-w16|Week 16 · Apr 2026]]: Opus 4.7 xhigh effort, web routines, mobile push alerts, native binaries.
- [[Release_2026-w15|Week 15 · Apr 2026]]: Ultraplan, Monitor tool with self-pacing `/loop`, `/team-onboarding`, `/autofix-pr`.
- [[Release_2026-w14|Week 14 · Mar 2026]]: CLI computer use, interactive lessons, flicker-free rendering, tool size overrides.
- [[Release_2026-w13|Week 13 · Mar 2026]]: Auto mode launch, built-in computer use, cloud PR auto-fix, Windows PowerShell tool.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
"""

for fn, content in mocs.items():
    p = os.path.join(MOC_DIR, fn)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created MOC: {fn}")

print("All MOCs generated successfully!")
