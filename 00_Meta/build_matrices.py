#!/usr/bin/env python3
"""
Decision Matrix Generator for Claude Code Obsidian Vault.
Creates structured comparative trade-off matrices in 70_Tool_Selection_Matrix/.
"""

import os

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX_DIR = os.path.join(VAULT_DIR, "70_Tool_Selection_Matrix")
os.makedirs(MATRIX_DIR, exist_ok=True)

matrices = {}

matrices["Matrix_Execution_Modes.md"] = """---
title: "Decision Matrix: Claude Code Execution Modes"
aliases:
  - "Matrix_Execution_Modes"
  - "Execution Modes Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "decision-tree"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Claude Code Execution Modes

> Comparative evaluation of operational modes: Interactive Terminal REPL, Headless Scripting (`-p`), Autonomous Loops (`/goal`), Background Daemons, and Agent Teams.

## Comparative Matrix

| Mode | Interactivity | Autonomy Level | State / Context | Best Used For | Key Commands / Flags |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Interactive REPL** | Full real-time steering | Semi-autonomous (turns pause for user feedback) | Continuous in-session context, resumable | Exploratory coding, pair programming, debugging, multi-file refactoring | `claude`, `claude "initial prompt"` |
| **Headless Script (`-p`)** | Zero (non-interactive) | One-shot execution until task completion or exit | Fresh session or continued with `-c` | CI/CD pipelines, shell scripting, piped input (`cat x \| claude -p`), pre-commit hooks | `claude -p "query"`, `claude -c -p "followup"` |
| **Autonomous Goal (`/goal`)** | Intermittent oversight | Persistent autonomy until explicit condition met | Auto-compacting long-context loop | Complex overnight refactors, test-suite fixing, exhaustive migrations | `/goal "condition"`, [[Keep_Claude_working_toward_a_goal]] |
| **Recurring Cron (`/loop`)** | Asynchronous | Periodic polling & execution | Retains handle or runs fresh | Long-running build monitoring, deployment polling, hourly security audits | `/loop 5m "check tests"`, [[Run_prompts_on_a_schedule]] |
| **Background Agent View** | Dashboard oversight | Full background parallel execution | Independent sessions, attached on demand | Running 5+ concurrent feature branches or audits | `claude agents`, `claude attach <id>`, [[Manage_multiple_agents_with_agent_view]] |
| **Claude Agent SDK** | Fully programmatic | Custom workflow logic | Programmatic session storage (S3/Redis/SQL) | Building custom AI applications, custom IDE integrations, SaaS agent workers | `ClaudeAgentOptions`, [[Agent_SDK_overview]] |

---

## Decision Flowchart

1. **Do you need human-in-the-loop steering while writing code?**
   - **YES** -> Use **[[Interactive_mode|Interactive REPL]]** (`claude`).
   - **NO** -> Proceed to Step 2.
2. **Is this running in an automated environment (CI/CD, cron, git hook)?**
   - **YES** -> Use **[[Run_Claude_Code_programmatically|Headless Mode]]** (`claude -p "..."`).
   - **NO** -> Proceed to Step 3.
3. **Does the task take hours and require Claude to keep trying until an explicit verification check passes?**
   - **YES** -> Use **[[Keep_Claude_working_toward_a_goal|Goal Mode]]** (`/goal`).
   - **NO** -> Proceed to Step 4.
4. **Do you have multiple independent tasks that should run simultaneously?**
   - **YES** -> Use **[[Manage_multiple_agents_with_agent_view|Agent View]]** (`claude agents`) with **[[Run_parallel_sessions_with_worktrees|Worktree isolation]]**.
   - **NO** -> Use standard REPL or SDK.

---
## Related References
- [[MOC_Claude_Code|Master Index]]
- [[CLI_reference|CLI Reference]]
- [[Matrix_Agentic_Coordination|Agentic Coordination Matrix]]
"""

matrices["Matrix_Extensibility.md"] = """---
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
"""

matrices["Matrix_Memory_Architectures.md"] = """---
title: "Decision Matrix: Memory & Context Architectures"
aliases:
  - "Matrix_Memory_Architectures"
  - "Memory Hierarchy Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "memory"
  - "context"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Memory & Context Architectures

> Choosing where instructions, project conventions, and learnings should live across the Claude Code hierarchy.

## Comparative Matrix

| Layer | File / Location | Scope | Persistence | Token Cost Impact | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Enterprise Managed Settings** | `/etc/claude-code/` or cloud server | Organization-wide | Immutable by developer | Injected into system config | Enforcing security policies, approved models, telemetry endpoints |
| **User Global Memory** | `~/.claude/CLAUDE.md` | All projects for this user | Permanent | Injected on every session startup | Personal coding preferences, preferred style, terminal preferences |
| **Project Root Memory** | `<repo>/CLAUDE.md` or `AGENTS.md` | Entire repository | Version-controlled with git | Cached via Prompt Caching (high hit rate) | Project build/test commands, architecture principles, code conventions |
| **Subdirectory Memory** | `<repo>/packages/<pkg>/CLAUDE.md` | Subtree / monorepo package | Activated when Claude operates in subtree | Injected on context entry | Package-specific build scripts, local architecture rules in monorepos |
| **Auto-Memory** | `~/.claude/projects/<proj>/MEMORY.md` | Project-specific (accumulated) | Automatically saved by Claude | First 200 lines / 25KB loaded on startup | Learnings Claude discovers over time (quirks, failed approaches) |
| **Ephemeral Session Context** | Live conversation history | Current session only | Discarded on session clear | Grows per turn; pruned by `/compact` | Active task progress, transient investigation logs, debug outputs |

---

## Memory Architecture Principles

1. **Keep `CLAUDE.md` Terse & High-Signal**:
   - Do NOT duplicate documentation that exists in README or code comments.
   - Store **build commands**, **test commands**, **lint commands**, and non-obvious project traps.
   - Format with bullet points; avoid verbose prose to maximize prompt cache efficiency.
2. **Leverage Prompt Caching**:
   - Editing `CLAUDE.md` in the middle of a session invalidates prompt caching for subsequent turns. Keep base memory stable.
3. **Monorepo Strategy**:
   - Root `CLAUDE.md`: High-level repo layout, overall build orchestration, global git guidelines.
   - Package `CLAUDE.md`: Local commands (e.g. `pnpm --filter @app/core test`).

---
## Related References
- [[How_Claude_remembers_your_project|How Claude Remembers Your Project]]
- [[Settings_files_and_precedence|Settings Files & Precedence]]
- [[Set_up_Claude_Code_in_a_monorepo_or_large_codebase|Monorepo Setup Guide]]
"""

matrices["Matrix_Tool_Approval_and_Security.md"] = """---
title: "Decision Matrix: Tool Approval & Security Boundaries"
aliases:
  - "Matrix_Tool_Approval_and_Security"
  - "Security Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "security"
  - "permissions"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Tool Approval & Security Boundaries

> Selecting the appropriate isolation, permission mode, and sandboxing level for local, cloud, and enterprise environments.

## Comparative Matrix

| Mode / Mechanism | Prompt Behavior | Filesystem Boundary | Network Boundary | Threat Model Fit |
| :--- | :--- | :--- | :--- | :--- |
| **Default Interactive Mode** | Asks for Bash commands & critical edits | Host machine | Host network | Standard local development with human oversight |
| **Auto Mode (`autoMode`)** | AI classifier auto-approves safe actions; prompts on destructive actions | Host machine | Host network | Experienced developers wanting frictionless local flow |
| **Accept Edits Mode** | Auto-approves file edits; prompts for Bash commands | Host machine | Host network | Code refactoring where shell execution requires manual review |
| **Bypass (`--dangerously-skip-permissions`)** | **Never prompts** (unrestricted) | Host machine | Host network | **Disposable containers ONLY**; strictly forbidden on production host machines |
| **Sandboxed Bash Tool** | Configurable prompts | Restricted to project root jail | Restricted egress domain whitelist | Mitigating prompt injection when analyzing untrusted open-source repos |
| **Devcontainers / Docker** | Isolated environment | Container mount only | Container bridge network | Team consistency; untrusted third-party dependencies |
| **Cloud Self-Hosted Runners** | Cloud orchestrated | Isolated cloud VM runner | Enterprise VPC egress | Zero developer machine exposure; air-gapped internal corporate code |

---

## Security Selection Rules

1. **Analyzing an untrusted external repo (e.g. assessing CVEs or unfamiliar PRs)?**
   - **Enforce [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash]]** or run inside a **[[Development_containers|Devcontainer]]**. Never run unrestricted permissions on untrusted repositories.
2. **Running unattended CI/CD jobs?**
   - Run in an isolated container/runner with ephemeral tokens. Use fine-grained permission rules rather than blanket bypass where possible.
3. **Enterprise Governance?**
   - Enforce settings using [[Deploy_managed_settings|Managed Settings]] to lock down allowed models, disable telemetry leakage, and restrict MCP servers with [[Control_MCP_server_access_for_your_organization|Managed MCP]].

---
## Related References
- [[Choose_a_permission_mode|Choose a Permission Mode]]
- [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash Tool]]
- [[Set_up_Claude_Code_for_your_organization|Organization Setup]]
"""

matrices["Matrix_Agentic_Coordination.md"] = """---
title: "Decision Matrix: Multi-Agent Coordination & Swarm Patterns"
aliases:
  - "Matrix_Agentic_Coordination"
  - "Multi-Agent Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "multi-agent"
  - "subagents"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Multi-Agent Coordination & Swarm Patterns

> When to keep execution inline vs dispatching subagents, worktrees, agent teams, or dynamic workflows.

## Comparative Matrix

| Pattern | Context Window Isolation | Filesystem Isolation | Concurrency | Communication Channel | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Inline Agent** | Single shared context | Same workspace | 1 (Sequential) | Direct chat | Quick edits, linear tasks, targeted bug fixes |
| **Subagents (`sub-agents`)** | **Complete context isolation** | Same workspace | Multi (runs in background) | Task prompt in -> Summary report out | Deep codebase research, isolated refactor passes without context pollution |
| **Worktree Subagents** | Complete context isolation | **Isolated Git Worktree** | Multi (parallel branches) | Git branch merge / PR | Concurrent feature development where file writes would collide |
| **Agent View Dashboard** | Independent sessions | Independent directories / worktrees | High (monitor 10+ sessions) | Shell attach & dashboard | Engineering leads overseeing multiple background projects |
| **Agent Teams** | Multi-agent network | Shared or independent repos | Multi-agent collaboration | Inter-session peer messaging | Complex swarm tasks with dedicated specialized roles (Architect, Coder, Tester) |
| **Dynamic Workflows** | Scripted subagent DAG | Script-defined isolation | Controlled fan-out / fan-in | Script outputs / JSON artifacts | Large-scale repo migrations, exhaustive vulnerability scans across 100 packages |

---

## Architectural Rule of Thumb

- **Will reading 30 files blow up your primary context window?**
  - **Spawn a [[Create_custom_subagents|Subagent]]** for research. The subagent reads the 30 files, summarizes the findings in 500 tokens, and returns only the necessary insight to the orchestrator.
- **Will two agents edit the same codebase simultaneously?**
  - **Always use [[Run_parallel_sessions_with_worktrees|Git Worktrees]]** (`--worktree`). Parallel sessions in the same working directory will overwrite each other's edits and corrupt git staging.
- **Need a repeatable migration pipeline across hundreds of files?**
  - **Use [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Dynamic Workflows]]**.

---
## Related References
- [[Run_agents_in_parallel|Run Agents in Parallel]]
- [[Create_custom_subagents|Create Custom Subagents]]
- [[Run_parallel_sessions_with_worktrees|Parallel Sessions with Worktrees]]
"""

for fn, content in matrices.items():
    p = os.path.join(MATRIX_DIR, fn)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created Decision Matrix: {fn}")

print("All Decision Matrices generated successfully!")
