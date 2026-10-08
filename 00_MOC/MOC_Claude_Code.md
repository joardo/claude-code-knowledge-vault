---
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
