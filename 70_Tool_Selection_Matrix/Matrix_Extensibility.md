---
title: "Decision Matrix: Claude Code Extensibility Mechanisms"
aliases:
  - "Matrix_Extensibility"
  - "Extensibility Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "tools"
  - "extensibility"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Claude Code Extensibility Mechanisms

> When to use Skills, Custom Slash Commands, Model Context Protocol (MCP) Servers, Lifecycle Hooks, Plugins, or Terminal Mods.

## Comparative Matrix

| Mechanism | Scope / Where It Runs | Mechanism Type | Deterministic vs LLM | Best Used For | Configuration Location |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Custom Skills** | Prompt & instruction extension | Reusable agent instructions & prompt macros | LLM reasoning & tool chaining | Complex prompt recipes, standard operating procedures (SOPs), role guidelines | `.claude/skills/` or `~/.claude/skills/` (`SKILL.md`) |
| **Custom Slash Commands** | Session shortcut | Command-line prompt template | LLM triggered via alias | Quick conversational macros (`/refactor`, `/review`) | `.claude/commands/` or `.claude/skills/` |
| **MCP Servers** | External tool provider | Protocol (stdio, SSE, HTTP) | Exposes deterministic APIs to LLM tool calls | Database queries, Jira/GitHub integration, Figma, internal API calls | `~/.claude/settings.json` (`mcpServers`) |
| **Lifecycle Hooks** | Shell event interceptor | OS processes on lifecycle triggers | **100% Deterministic** (No LLM hallucinations) | Code formatting on file write, blocking dangerous commands, CI alerts | `.claude/settings.json` (`hooks`) |
| **Plugins** | Packaged bundle | Composite archive or git repo | Multi-component | Distributing skills + hooks + MCP servers together to a team | Marketplaces or `plugins/` |
| **Mods** | Terminal UI & event rewriting | In-process JavaScript/TypeScript | UI rendering & event transformation | Live diff panels, custom status widgets, interactive buttons in terminal | `.claude/mods/` |

---

## Technical Selection Heuristic

- **Need deterministic enforcement that NEVER depends on the LLM's mood?**
  - **Use [[Automate_actions_with_hooks|Lifecycle Hooks]]**. A `PreToolUse` hook can exit with non-zero code to strictly forbid `git push --force` or run `prettier --write` after every edit without wasting LLM tokens.
- **Need to connect Claude to an external system, DB, or API?**
  - **Use [[Connect_Claude_Code_to_tools_via_MCP|Model Context Protocol (MCP)]]**. Claude dynamically discovers tool schemas and invokes them.
- **Need to encode multi-step domain workflows and prompt techniques?**
  - **Use [[Extend_Claude_with_skills|Custom Skills]]**. Embed role definitions, checklists, and recommended patterns.
- **Need to package your whole team's setup (linters, skills, MCP servers) into a single installable package?**
  - **Use [[Plugins_overview|Claude Code Plugins]]**.
- **Need to add GUI elements or custom status indicators to the terminal interface?**
  - **Use [[Mods_overview|Claude Code Mods]]**.

---
## Related References
- [[MOC_Extensibility_and_MCP|Extensibility & MCP MOC]]
- [[MOC_Hooks_and_Automation|Hooks & Automation MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
